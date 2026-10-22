"""Week 8 story, companion alignment and accessible diagram constraints."""
import sys
import tomllib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'deck'))


class Week08DeckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import week08
        cls.deck = week08
        cls.titles = [s.title for s in week08.S]

    def test_stages_stay_in_teaching_order(self):
        self.assertLess(self.titles.index('Make a promise someone can test'),
                        self.titles.index('One object remembers one choice'))
        self.assertLess(self.titles.index('One object remembers one choice'),
                        self.titles.index('What would test the promise best?'))
        self.assertLess(self.titles.index('A person acts. Something responds.'),
                        self.titles.index('Show a usable increment'))
        self.assertLess(self.titles.index('Show a usable increment'),
                        self.titles.index('Review, then integrate'))
        self.assertLess(self.titles.index('Review, then integrate'),
                        self.titles.index('Same project. Separate settings.'))
        self.assertLess(self.titles.index('Same project. Separate settings.'),
                        self.titles.index('A frame becomes landmarks'))
        self.assertLess(self.titles.index('A frame becomes landmarks'),
                        self.titles.index('One goal, one change, one check'))

    def test_diagram_canvas_and_notes(self):
        diagrams = [s for s in self.deck.S if any(e.kind == 'figure' for e in s.els)]
        self.assertGreaterEqual(len(diagrams), 10)
        for slide in diagrams:
            fig = next(e for e in slide.els if e.kind == 'figure')
            self.assertGreaterEqual(fig.w, 1700, slide.title)
            self.assertGreaterEqual(fig.h, 760, slide.title)
            self.assertTrue(slide.notes, slide.title)
        self.assertTrue(all(s.notes for s in self.deck.S))

    def test_formative_checks_have_fallbacks(self):
        questions = [s for s in self.deck.S if s.cp]
        self.assertEqual(len(questions), 3)
        self.assertTrue(all('ClassPoint' in s.notes for s in questions))
        self.assertTrue(all('Answer:' in s.notes or 'Answer: the' in s.notes for s in questions))

    def test_tile_class_runs_without_extra_packages(self):
        from contextlib import redirect_stdout
        from io import StringIO

        result = StringIO()
        with redirect_stdout(result):
            exec(self.deck.TILE_EXAMPLE, {})
        self.assertEqual(result.getvalue(), 'True\n')

    def test_only_verified_draft_companion_is_linked(self):
        notes = ' '.join(s.notes for s in self.deck.S)
        self.assertIn('https://github.com/sd5913/pfad/pull/11', notes)
        self.assertIn('uv/local', notes)
        self.assertIn('GitHub Actions', notes)
        self.assertIn('Codex cloud', notes)
        self.assertIn('MediaPipe', notes)
        self.assertIn('no input', notes)
        self.assertNotIn('Docker', notes)
        self.assertNotIn('asyncio', notes)
        self.assertNotIn('Dec 1', notes)

    def test_registered_deck_and_site_download(self):
        conf = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertIn('week08', conf['course']['decks'])
        self.assertIn('week08/', [n['href'] for n in conf['nav']])
        page = (ROOT / 'site/index.html').read_text()
        self.assertIn('week08/SD5913-week08.pdf', page)
        self.assertIn('WEEK 08 · THU 29 OCT 2026', page)


if __name__ == '__main__':
    unittest.main()
