"""Execute the displayed examples, not copied implementations."""
import ast
import contextlib
import io
from pathlib import Path
import tempfile
import os
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "deck" / "week12.py"

def panel(title, kind="code_panel", index=2):
    tree = ast.parse(SOURCE.read_text())
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == kind and len(node.args) > index
                and isinstance(node.args[1], ast.Constant) and node.args[1].value == title):
            return "\n".join(ast.literal_eval(node.args[index]))
    raise AssertionError(title)

class ReviewExamples(unittest.TestCase):
    def test_displayed_review_executes_success_and_invalid_input(self):
        code = panel("A review you can explain", "two_col", 3)
        self.assertIn("except", code)
        scope, out = {}, io.StringIO()
        with contextlib.redirect_stdout(out):
            exec(code, scope)
        self.assertEqual(out.getvalue().strip(), "Use ints")
        self.assertEqual(scope["add"](3, 4), 7)
        for a, b in (("3",4),(True,4),(3,4.0)):
            with self.assertRaises(ValueError):
                scope["add"](a,b)

    def test_pure_function_panel_is_the_same_validated_implementation(self):
        scope = {}
        exec(panel("Nothing outside the two inputs"), scope)
        self.assertEqual(scope["add"](-2, 2), 0)
        with self.assertRaises(ValueError):
            scope["add"]("3", 4)

if __name__ == "__main__":
    unittest.main()
