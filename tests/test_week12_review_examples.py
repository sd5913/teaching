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

    def test_ama_follows_the_break_and_preserves_the_offline_route(self):
        notes = [s.notes for s in week12.S]
        pause = next(i for i, note in enumerate(notes) if note.startswith('60–70'))
        opening = next(i for i, note in enumerate(notes) if note.startswith('90–95'))
        rounds = next(i for i, note in enumerate(notes) if note.startswith('95–115'))
        self.assertLess(pause, opening)
        self.assertLess(opening, rounds)
        self.assertIn('paper', notes[rounds])
        self.assertTrue(notes[-1].startswith('119–120'))
