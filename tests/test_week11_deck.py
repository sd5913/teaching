"""Check export prerequisites that break actual Week 11 presentation output."""
import importlib.util
from pathlib import Path
import unittest

from deckgen import Image

ROOT = Path(__file__).resolve().parents[1]


class Week11DeckTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('week11', ROOT / 'deck/week11.py')
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)

    def test_every_embedded_application_capture_is_available(self):
        captures = [element for slide in self.module.S for element in slide.els
                    if isinstance(element, Image)]
        self.assertTrue(captures)
        for capture in captures:
            self.assertTrue(Path(capture.src).is_file(), capture.src)

    def test_notes_and_runnable_companion_are_exportable(self):
        for slide in self.module.S:
            self.assertTrue(slide.notes.strip(), slide.title)
        self.assertNotIn('WEEK11_COMPANION', self.module.PFAD)
        self.assertRegex(self.module.PFAD, r'/tree/[0-9a-f]{40}/week11$')


if __name__ == '__main__':
    unittest.main()
