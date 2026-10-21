"""Execute the displayed examples, not copied implementations."""
import ast
import contextlib
import io
from pathlib import Path
import tempfile
import os
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "deck" / "week11.py"

def panel(title, kind="code_panel", index=2):
    tree = ast.parse(SOURCE.read_text())
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == kind and len(node.args) > index
                and isinstance(node.args[1], ast.Constant) and node.args[1].value == title):
            return "\n".join(ast.literal_eval(node.args[index]))
    raise AssertionError(title)

class ReviewExamples(unittest.TestCase):
    def test_displayed_opacity_rejects_nonfinite_and_boolean_inputs(self):
        scope = {}
        with contextlib.redirect_stdout(io.StringIO()):
            exec(panel("Validate before you use it"), scope)
        opacity = scope["opacity"]
        for value in (True, False, None, "oops", float("nan"), float("inf"), -float("inf")):
            with self.subTest(value=value):
                self.assertEqual(opacity(value), 0)
        for value, expected in ((0, 0), (.5, 50), (1, 100), (3, 100), (-1, 0)):
            self.assertEqual(opacity(value), expected)

if __name__ == "__main__":
    unittest.main()
