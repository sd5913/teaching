"""Focused invariants for the static Week 12 teaching trace."""
import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'deck'))
spec = importlib.util.spec_from_file_location('week12', ROOT / 'deck/week12.py')
week12 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(week12)


class Week12TraceTests(unittest.TestCase):
    def test_pure_example(self):
        def add(a: int, b: int) -> int:
            return a + b

        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-2, 2), 0)
        self.assertEqual(len(week12.DECK['slides']), 21)

    def test_permission_diagrams_distinguish_execution_from_refusal(self):
        allowed, _ = week12.F.permission(True)
        blocked, _ = week12.F.permission(False)
        self.assertIn('runs add(3, 4)', allowed)
        self.assertIn('result 7', allowed)
        self.assertIn('NO CALL', blocked)
        self.assertIn('not allowed', blocked)
        self.assertNotIn('runs add(3, 4)', blocked)
        self.assertIn('TRUST BOUNDARY', allowed)
        self.assertIn('TRUST BOUNDARY', blocked)

    def test_figures_keep_primary_labels_large(self):
        for draw in (week12.F.roles, week12.F.outbound, week12.F.inbound):
            svg, _ = draw()
            self.assertIn('font-size="40"', svg)
            self.assertIn('font-size="56"', svg)

    def test_source_and_navigation_link_the_draft_not_unshipped_code(self):
        self.assertIn('/pull/15/files', (ROOT / 'deck/week12.py').read_text())
        self.assertIn('week12/', (ROOT / 'site/index.html').read_text())
        self.assertIn('"week12"', (ROOT / 'deckgen.toml').read_text())


if __name__ == '__main__':
    unittest.main()
