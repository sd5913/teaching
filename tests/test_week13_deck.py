"""Checks for the provisional Week 13 deck and its navigation."""

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

    def test_complete_unassessed_review_sequence(self):
        slides = self.module.DECK['slides']
        self.assertEqual(len(slides), 29)
        self.assertTrue(all(slide.notes for slide in slides))
        self.assertFalse(any(slide.cp for slide in slides))
        titles = [slide.title for slide in slides]
        for title in ('What prints?', 'What if limit is zero?',
                      'A suggestion is not permission to act',
                      'From repository to checked result', 'What still needs an explanation?'):
            self.assertIn(title, titles)

    def test_diagrams_fill_the_body_and_have_large_labels(self):
        for slide in self.module.DECK['slides']:
            if slide.title not in ('Input becomes a visible result',
                                   'Test, change, stop',
                                   'A suggestion is not permission to act',
                                   'From repository to checked result'):
                continue
            figure = next(el for el in slide.els if type(el).__name__ == 'Figure')
            self.assertGreaterEqual(figure.w, 1700)
            self.assertGreaterEqual(figure.h, 780)
        source = (ROOT / 'deck/week13_figures.py').read_text()
        self.assertIn('58, INK', source)
        self.assertIn('42, MUTED', source)


if __name__ == '__main__':
    unittest.main()
