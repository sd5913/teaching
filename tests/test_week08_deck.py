"""The Week 8 lesson must keep the agreed order and assessment details."""
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
        cls.slides = week08.S
        cls.titles = [slide.title for slide in cls.slides]
        cls.source = (ROOT / 'deck/week08.py').read_text()

    def test_lecture_order(self):
        titles = ['What is your group idea becoming?', 'Register your repository now.',
                  '1. Alice starts a change', 'Create a cloud environment.',
                  'One project, several delivery paths.', 'From light to an action',
                  'Try all nine vision examples.']
        positions = [self.titles.index(title) for title in titles]
        self.assertEqual(positions, sorted(positions))
        self.assertTrue(all(slide.notes for slide in self.slides))

    def test_group_assessment_and_submission(self):
        for text in ('25%', '50%', '40% OF COURSE GRADE',
                     'Sunday 6 December 2026, 23:59 HKT',
                     'assignments/group-project.md'):
            self.assertIn(text, self.source)

    def test_linked_examples_and_environment_distinctions(self):
        for text in ('week08/vision.py', 'week08/hand_tiles.py',
                     'capacitor-app-template', 'godot-game-template',
                     'CLOUDFLARE_API_TOKEN', 'GitHub Actions', 'Codex cloud',
                     'MediaPipe', 'OpenCV'):
            self.assertIn(text, self.source)

    def test_opening_has_presentation_fallback(self):
        opening = self.slides[self.titles.index('What is your group idea becoming?')]
        self.assertTrue(opening.cp)
        self.assertIn('show of hands', opening.notes)

    def test_registered_with_week07_and_site_download(self):
        conf = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertIn('week07', conf['course']['decks'])
        self.assertIn('week08', conf['course']['decks'])
        self.assertIn('week08/', [n['href'] for n in conf['nav']])
        self.assertIn('week08/SD5913-week08.pdf', (ROOT / 'site/index.html').read_text())


if __name__ == '__main__':
    unittest.main()
