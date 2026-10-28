"""Week 13 export contract; revision prose is reviewed in rendered artifacts."""

import importlib.util
import tomllib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Week13Deck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('week13', ROOT / 'deck/week13.py')
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)

    def test_registered_with_site_and_navigation(self):
        config = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertIn('week13', config['course']['decks'])
        self.assertIn('week13/', [nav['href'] for nav in config['nav']])
        site = (ROOT / 'site/index.html').read_text()
        self.assertIn('href="week13/"', site)
        self.assertIn('week13/SD5913-week13.pdf', site)

    def test_public_deck_has_notes_without_graded_activity_payloads(self):
        slides = self.module.DECK['slides']
        self.assertTrue(all(slide.notes for slide in slides))
        self.assertFalse(any(slide.cp for slide in slides))

    def test_diagrams_fill_export_body(self):
        for slide in self.module.DECK['slides']:
            for figure in (el for el in slide.els if type(el).__name__ == 'Figure'):
                self.assertGreaterEqual(figure.w, 1700)
                self.assertGreaterEqual(figure.h, 780)


if __name__ == '__main__':
    unittest.main()
