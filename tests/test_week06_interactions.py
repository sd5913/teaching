"""The main lesson must offer participation beyond instructor demonstrations."""
import sys
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'deck'))


class Week06InteractionTests(unittest.TestCase):
    def test_prediction_checks_and_browser_exercise_are_in_the_main_path(self):
        import week06

        questions = [slide for slide in week06.S if slide.cp]
        self.assertGreaterEqual(len(questions), 1)
        self.assertTrue(any('frequency' in slide.title.lower() for slide in questions))
        exercise = next(el for slide in week06.S for el in slide.els
                        if el.kind == 'exercise' and el.eid == 'stretch-the-audio-clock')
        output = StringIO()
        with redirect_stdout(output):
            exec(exercise.code.replace('rate = 8', 'rate = 4'), {})
        self.assertIn('>2s<', output.getvalue())
        self.assertIn('cx="650"', output.getvalue())

    def test_click_to_score_precedes_four_layer_live_coding(self):
        import week06

        grid = next(i for i, slide in enumerate(week06.S)
                    if 'A click changes the score' in slide.title)
        layers = next(i for i, slide in enumerate(week06.S)
                      if slide.title == 'Hi-hat')
        self.assertLess(grid, layers)
        self.assertTrue(any('Stop' in slide.notes for slide in week06.S[grid:layers]))


if __name__ == '__main__':
    unittest.main()
