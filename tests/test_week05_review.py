import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'deck'))

from week05 import S


class Week05ReviewTests(unittest.TestCase):
    def test_dates_are_at_the_front(self):
        self.assertIn('22 October', S[1].title)
        self.assertIn('1 November', S[1].title)
        self.assertIn('23:59', str(S[1].els))

    def test_number_every_slide(self):
        for index, slide in enumerate(S, 1):
            self.assertTrue(any(e.name == 'week05-slide-number' for e in slide.els), index)

    def test_replaced_polls_and_exit_with_open_question(self):
        titles = [slide.title for slide in S]
        self.assertNotIn('What crosses an image-generation API?', titles)
        self.assertNotIn('Which is the strongest first interaction to prototype?', titles)
        self.assertIn('What interaction do you want to make?', titles)

    def test_saved_outputs_are_shown(self):
        for title in ('The four pixels after Pillow saves them',
                      'What does seeded noise look like?'):
            slide = next(slide for slide in S if slide.title == title)
            self.assertTrue(any(e.kind == 'image' for e in slide.els), title)


if __name__ == '__main__':
    unittest.main()
