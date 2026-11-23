"""Check the formative Week 10 relationship activities and opening AMA."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'deck'))
import week10


class Week10ClassPointTests(unittest.TestCase):
    def test_project_ama_is_open_and_ungraded(self):
        ama = next(slide for slide in week10.S
                   if slide.title == 'Ask me anything about the group project')
        self.assertEqual(ama.cp['type'], 'short_answer')
        self.assertNotIn('choices', ama.cp)
        self.assertNotIn('correct', ama.cp)
        self.assertLess(week10.S.index(ama), 3)

    def test_relationship_checks_cover_three_cardinalities_and_self_reference(self):
        checks = [slide for slide in week10.S
                  if slide.cp and slide.cp.get('type') == 'multiple_choice']
        self.assertEqual(len(checks), 4)
        self.assertTrue(all(slide.cp['choices'] == ['A', 'B', 'C', 'D'] for slide in checks))
        for slide in checks[:3]:
            visible = [run.text for el in slide.els for para in (getattr(el, 'paras', None) or [])
                       for run in para.runs]
            for label in ('One-to-one', 'One-to-many', 'Many-to-many', 'Self-reference'):
                self.assertIn(label, visible)
        visible = [run.text for el in checks[3].els for para in (getattr(el, 'paras', None) or [])
                   for run in para.runs]
        self.assertIn('Both records are Messages', visible)
        self.assertTrue(all('correct' not in slide.cp for slide in checks))
        self.assertTrue(all(slide.notes.strip() for slide in checks))


if __name__ == '__main__':
    unittest.main()
