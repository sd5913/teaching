"""Diagram labels and direction must preserve the actual feedback distinction."""
import importlib.util
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
from deckgen.project import configure
configure(ROOT)
sys.path.insert(0, str(ROOT / 'deck'))
spec = importlib.util.spec_from_file_location('week12_figures', ROOT / 'deck/week12_figures.py')
figures = importlib.util.module_from_spec(spec)
spec.loader.exec_module(figures)


class FeedbackDiagrams(unittest.TestCase):
    def test_feedback_includes_observation_choice_result_and_stop(self):
        svg, _ = figures.feedback()
        for value in ['2 lights; t180', 'speed 125 to 275',
                      '3 lights; t166', 'Pass: stop edits']:
            self.assertIn(value, svg)

    def test_state_diagram_distinguishes_open_exit_and_winning(self):
        svg, _ = figures.state()
        for value in ['0, 1, 2 lights', 'exit locked', '3 lights',
                      'exit open', 'At exit + 3', 'won = true']:
            self.assertIn(value, svg)

    def test_primary_labels_remain_at_least_forty_design_pixels(self):
        for draw in [figures.feedback, figures.process, figures.state,
                     figures.episode, figures.budgets, figures.timing, figures.evidence, figures.editor]:
            svg, _ = draw()
            sizes = [int(v) for v in re.findall(r'font-size="(\d+)"', svg)]
            self.assertTrue(sizes)
            self.assertGreaterEqual(min(sizes), 40)
            self.assertIn('viewBox="0 0 1680 640"', svg)


if __name__ == '__main__':
    unittest.main()
