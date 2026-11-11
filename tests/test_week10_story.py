"""Execute the displayed SQL against interleaved conversation rows."""
import ast
from pathlib import Path
import sqlite3
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1] / 'deck' / 'week10.py'


def panel(heading):
    for node in ast.walk(ast.parse(SOURCE.read_text())):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id in ('code_panel', 'sql_example', 'orm_example')
                and isinstance(node.args[1], ast.Constant)
                and node.args[1].value == heading):
            index = 3 if node.func.id == 'orm_example' else 2
            return '\n'.join(ast.literal_eval(node.args[index]))
    raise AssertionError(heading)


class DisplayedQueryTests(unittest.TestCase):
    def teaching_database(self, filename=':memory:'):
        db = sqlite3.connect(filename)
        self.addCleanup(db.close)
        db.execute('PRAGMA foreign_keys = ON')
        db.executescript('''
            CREATE TABLE user (id INTEGER PRIMARY KEY, name TEXT UNIQUE NOT NULL);
            CREATE TABLE conversation (
                id INTEGER PRIMARY KEY, owner_id INTEGER NOT NULL REFERENCES user(id),
                title TEXT NOT NULL);
            CREATE TABLE message (
                id INTEGER PRIMARY KEY,
                conversation_id INTEGER NOT NULL REFERENCES conversation(id),
                role TEXT NOT NULL, content TEXT NOT NULL);
            INSERT INTO user VALUES (1, 'Ada'), (2, 'Bo'), (3, 'Cy');
            INSERT INTO conversation VALUES
                (5, 2, 'Leave'), (4, 1, 'Game notes'), (3, 1, 'Handbook');
            INSERT INTO message VALUES
                (8, 3, 'assistant', 'Apply online.'),
                (9, 5, 'user', 'Another conversation'),
                (7, 3, 'user', 'Lost card?');
        ''')
        return db

    def test_query_filters_one_conversation_and_restores_message_order(self):
        db = sqlite3.connect(':memory:')
        self.addCleanup(db.close)
        db.execute('CREATE TABLE message (id INTEGER, conversation_id INTEGER, role TEXT, content TEXT)')
        db.executemany('INSERT INTO message VALUES (?, ?, ?, ?)', [
            (4, 3, 'assistant', 'second answer'), (2, 2, 'user', 'other conversation'),
            (1, 3, 'user', 'first question'), (3, 3, 'user', 'second question')])
        query = panel('Find messages in conversation 3.')
        self.assertEqual(list(db.execute(query)), [
            (1, 'first question'), (3, 'second question'), (4, 'second answer')])
        db.execute('UPDATE message SET conversation_id = 999 WHERE conversation_id = 3')
        self.assertEqual(list(db.execute(query)), [])

    def test_select_returns_the_displayed_rows(self):
        db = self.teaching_database()
        self.assertEqual(list(db.execute(panel('Find messages in conversation 3.'))), [
            (7, 'Lost card?'), (8, 'Apply online.')])

    def test_join_matches_owners_without_leaking_other_conversations(self):
        db = self.teaching_database()
        query = panel('Whose conversations are these?')
        self.assertEqual(list(db.execute(query, (1,))), [
            (3, 'Ada', 'Handbook'), (4, 'Ada', 'Game notes')])
        self.assertEqual(list(db.execute(query, (2,))), [(5, 'Bo', 'Leave')])
        self.assertEqual(list(db.execute(query, (3,))), [])
        self.assertEqual(list(db.execute(query, (999,))), [])

    def test_update_survives_reload_and_preserves_other_rows_and_links(self):
        with tempfile.TemporaryDirectory() as directory:
            filename = Path(directory) / 'chat.sqlite'
            db = self.teaching_database(filename)
            query = panel('Change one title. Keep its identity.')
            self.assertEqual(db.execute(query, ('Game ideas', 3)).rowcount, 1)
            db.commit()
            db.close()
            with sqlite3.connect(filename) as reopened:
                self.assertEqual(list(reopened.execute(
                    'SELECT id, owner_id, title FROM conversation ORDER BY id')), [
                    (3, 1, 'Game ideas'), (4, 1, 'Game notes'), (5, 2, 'Leave')])
                self.assertEqual(list(reopened.execute(
                    panel('Find messages in conversation 3.'))), [
                    (7, 'Lost card?'), (8, 'Apply online.')])
                self.assertEqual(reopened.execute(query, ('Missing', 999)).rowcount, 0)


if __name__ == '__main__':
    unittest.main()
