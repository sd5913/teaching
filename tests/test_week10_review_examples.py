"""Check syntax of the actual Python excerpts students read on the slides."""
import ast
from pathlib import Path
import unittest

SOURCE = Path(__file__).resolve().parents[1] / 'deck' / 'week10.py'


class DisplayedPythonTests(unittest.TestCase):
    def test_python_panels_compile_in_their_documented_method_context(self):
        for node in ast.walk(ast.parse(SOURCE.read_text())):
            if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                    and node.func.id == 'code_panel'):
                continue
            if any(k.arg == 'lang' and ast.literal_eval(k.value) is None for k in node.keywords):
                continue
            heading = ast.literal_eval(node.args[1])
            code = '\n'.join(ast.literal_eval(node.args[2]))
            if heading in ('Ask an exact, scoped question', 'Save one complete turn atomically'):
                code = 'def excerpt(self, owner_id, conversation_id, question, answer):\n' + '\n'.join(
                    '    ' + line for line in code.splitlines())
            with self.subTest(heading=heading):
                compile(code, str(SOURCE), 'exec')


if __name__ == '__main__':
    unittest.main()
