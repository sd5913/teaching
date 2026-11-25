"""Check the course cross-links and the order in which the classroom uses them."""
from pathlib import Path
import sys
import unittest

from deckgen.project import configure

ROOT = Path(__file__).resolve().parents[1]
configure(ROOT)
sys.path.insert(0, str(ROOT / 'deck'))
import week12


def links(slide):
    return {run.url for element in slide.els
            for para in getattr(element, 'paras', [])
            for run in para.runs if run.url}


class CourseReview(unittest.TestCase):
    def test_every_earlier_week_has_a_student_facing_source(self):
        urls = set().union(*(links(slide) for slide in week12.S))
        for number in range(1, 12):
            self.assertIn(f'{week12.COURSE}/week{number:02}/README.md', urls)

    def test_optional_evidence_and_tutorial_use_same_immutable_revision(self):
        urls = set().union(*(links(slide) for slide in week12.S))
        self.assertRegex(week12.PIN, r'^[0-9a-f]{40}$')
        for path in ('README.md', 'godot-practice.md', 'model-episode.json',
                     'evidence/provenance.json', 'evidence/model-selected-world.mp4'):
            self.assertIn(f'{week12.COMPANION}/{path}', urls)

    def test_feedback_then_subject_ama_allow_offline_questions(self):
        notes = [s.notes for s in week12.S]
        feedback = next(i for i, slide in enumerate(week12.S)
                        if any(getattr(e, 'url', '') == week12.ESFQ for e in slide.els))
        self.assertEqual(feedback, len(week12.S) - 2)
        self.assertTrue(notes[feedback].startswith('95–105'))
        self.assertTrue(notes[-1].startswith('105–120'))
        self.assertIn('paper', notes[-1])
        self.assertEqual(week12.S[-1].cp['type'], 'short_answer')
        self.assertTrue(week12.S[-1].cp['multiple'])
