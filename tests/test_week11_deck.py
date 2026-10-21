"""Week 11 content guardrails without requiring a live creative tool."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Week11DeckTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('week11', ROOT / 'deck/week11.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        cls.deck = module.DECK
        cls.notes = '\n'.join(slide.notes or '' for slide in cls.deck['slides'])

    def test_order_and_outcome(self):
        titles = [slide.title for slide in self.deck['slides']]
        self.assertEqual(len(titles), 29)
        for text in ('Find the object', 'The receiver chooses the effect',
                     'What happens when sending stops?', 'MCP exposes a bounded capability'):
            self.assertIn(text, titles)
        self.assertLess(titles.index('Find the object'), titles.index('The receiver chooses the effect'))
        self.assertLess(titles.index('The receiver chooses the effect'), titles.index('What happens when sending stops?'))

    def test_notes_make_simulation_and_scope_explicit(self):
        for phrase in ('not a runnable', 'simulation', 'not OSC', 'read-only', 'disposable'):
            self.assertIn(phrase.lower(), self.notes.lower())

    def test_registration_and_links(self):
        config = (ROOT / 'deckgen.toml').read_text()
        site = (ROOT / 'site/index.html').read_text()
        self.assertIn('"week11"', config)
        self.assertIn('href="week11/"', site)
        self.assertIn('week11/SD5913-week11.pdf', site)


if __name__ == '__main__':
    unittest.main()
