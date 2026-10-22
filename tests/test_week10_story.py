"""Keep the Week 10 class-to-record progression and examples honest."""

import ast
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'deck'))


class Week10Tests(unittest.TestCase):
    @staticmethod
    def example(title):
        source = Path(__file__).resolve().parents[1] / 'deck' / 'week10.py'
        tree = ast.parse(source.read_text(encoding='utf-8'))
        for node in ast.walk(tree):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                    and node.func.id == 'code_panel' and len(node.args) >= 3
                    and isinstance(node.args[1], ast.Constant)
                    and node.args[1].value == title):
                return '\n'.join(ast.literal_eval(node.args[2]))
        raise AssertionError(f'No code panel titled {title!r}')

    def test_story_moves_from_independent_objects_to_saved_records(self):
        import week10

        titles = [slide.title for slide in week10.S]
        self.assertLess(titles.index('One recipe; two artworks'),
                        titles.index('Only the called object changes'))
        self.assertLess(titles.index('Only the called object changes'),
                        titles.index('One exhibition, many artworks'))
        self.assertLess(titles.index('One exhibition, many artworks'),
                        titles.index('A live object is not a saved record'))
        self.assertLess(titles.index('Close Python. Read the file back.'),
                        titles.index('Find evidence before answering'))
        self.assertGreaterEqual(len(week10.S), 25)
        self.assertTrue(all(slide.notes for slide in week10.S))

    def test_save_load_and_independent_state(self):
        trace = self.example('Check the prediction in Python')
        save = self.example('Write a small local JSON file')
        load = self.example('Close Python. Read the file back.')
        with tempfile.TemporaryDirectory() as directory:
            for example, expected in ((trace, '3 7'), (save, ''),
                                      (load, 'a1 3 e1\na2 7 e1')):
                with self.subTest(expected=expected):
                    result = subprocess.run([sys.executable, '-c', example],
                                            cwd=directory, text=True, capture_output=True,
                                            check=True)
                    self.assertEqual(result.stdout.strip(), expected)
            retry = subprocess.run([sys.executable, '-c', save],
                                   cwd=directory, text=True, capture_output=True)
            self.assertNotEqual(retry.returncode, 0)
            self.assertIn('FileExistsError', retry.stderr)


if __name__ == '__main__':
    unittest.main()
