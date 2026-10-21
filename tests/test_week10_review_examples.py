"""Execute the displayed examples, not copied implementations."""
import ast
import contextlib
import io
from pathlib import Path
import tempfile
import os
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "deck" / "week10.py"

def panel(title, kind="code_panel", index=2):
    tree = ast.parse(SOURCE.read_text())
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == kind and len(node.args) > index
                and isinstance(node.args[1], ast.Constant) and node.args[1].value == title):
            return "\n".join(ast.literal_eval(node.args[index]))
    raise AssertionError(title)

class ReviewExamples(unittest.TestCase):
    def test_method_fragment_cannot_be_mistaken_for_a_second_class_or_call(self):
        excerpt = panel("Class, object, attribute, method", "two_col", 3)
        self.assertIn("EXCERPT", excerpt)
        self.assertNotIn("class Artwork:", excerpt)
        self.assertNotIn("amber.view()", excerpt)
        self.assertIn("Fresh run", SOURCE.read_text())
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            exec(panel("Check the prediction in Python"), {})
        self.assertEqual(out.getvalue().strip(), "3 7")

    def test_reconstruction_has_its_own_class_after_a_fresh_load(self):
        here = os.getcwd()
        with tempfile.TemporaryDirectory() as directory:
            try:
                os.chdir(directory)
                exec(panel("Write a small local JSON file"), {})
                fresh = {}
                with contextlib.redirect_stdout(io.StringIO()):
                    exec(panel("Close Python. Read the file back."), fresh)
                self.assertNotIn("Artwork", fresh)
                out = io.StringIO()
                with contextlib.redirect_stdout(out):
                    exec(panel("A loaded record can become a new object", "two_col", 3), fresh)
                self.assertEqual(out.getvalue().strip(), "4")
            finally:
                os.chdir(here)

if __name__ == "__main__":
    unittest.main()
