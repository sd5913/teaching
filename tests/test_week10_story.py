"""Execute the displayed SQL against interleaved conversation rows."""
import ast
from pathlib import Path
import sqlite3
import unittest

SOURCE = Path(__file__).resolve().parents[1] / 'deck' / 'week10.py'


def panel(heading):
    for node in ast.walk(ast.parse(SOURCE.read_text())):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == 'code_panel' and node.args[1].value == heading):
            return '\n'.join(ast.literal_eval(node.args[2]))
    raise AssertionError(heading)


class DisplayedQueryTests(unittest.TestCase):
    def test_query_filters_one_conversation_and_restores_message_order(self):
        db = sqlite3.connect(':memory:')
        self.addCleanup(db.close)
        db.execute('CREATE TABLE message (id INTEGER, conversation_id INTEGER, role TEXT, content TEXT)')
        db.executemany('INSERT INTO message VALUES (?, ?, ?, ?)', [
            (4, 1, 'assistant', 'second answer'), (2, 2, 'user', 'other conversation'),
            (1, 1, 'user', 'first question'), (3, 1, 'user', 'second question')])
        query = panel('Python does not hide the query')
        self.assertEqual([row[0] for row in db.execute(query, (1,))], [1, 3, 4])
        self.assertEqual([row[3] for row in db.execute(query, (2,))], ['other conversation'])
        self.assertEqual(list(db.execute(query, (999,))), [])


if __name__ == '__main__':
    unittest.main()
