import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'deck'))
import week07 as W
from week07_recap import SELECTION

class Week07Tests(unittest.TestCase):
    def test_recap(self):
        self.assertEqual(sum(map(len, SELECTION.values())), 20)
        self.assertEqual(len(W.RECAP), 20)
        self.assertTrue(all(s.cp is None and not s.report for s in W.RECAP))
    def test_recap_has_current_presenter_cues(self):
        slides = {s.title: s for s in W.RECAP}
        self.assertIn('not a live exercise today', slides['One promise, four steps'].notes)
        self.assertNotIn('they just ran', slides['That is a loop, and that is all of it'].notes)
        self.assertNotIn('2025 question', slides['A cap never sits under a drawn cell'].notes)
        function = slides['A rule with a name']
        body = ' '.join(''.join(run.text for run in para.runs) for para in function.els[2].paras)
        self.assertIn('No return, Python returns None', body)
        self.assertNotIn('more than any other', body)
        self.assertNotIn('Everything else today', ''.join(
            run.text for para in slides['That is a loop, and that is all of it'].els[2].paras
            for run in para.runs))
        diffusion = slides['Learn to remove noise; then use that skill.']
        self.assertEqual(diffusion.els[3].paras[0].runs[1].url,
                         'https://github.com/sd5913/pfad/blob/2026/week05/diffusion/generate.py')
    def test_sequence(self):
        titles = [s.title for s in W.S]
        self.assertLess(titles.index('Ask me anything.'), titles.index('Midterm quiz.\n10:00–10:30.'))
        self.assertLess(titles.index('Midterm quiz.\n10:00–10:30.'), titles.index('What do you wish it did?'))
        self.assertLess(titles.index('Form your team. Aim big.'), titles.index('Show what you want to build.'))
    def test_three_collections(self):
        active = [s for s in W.S if s.cp]
        self.assertEqual(len(active), 3)
        self.assertEqual([s.cp['type'] for s in active], ['short_answer','short_answer','image_upload'])
        self.assertTrue(active[0].cp['multiple'])
        self.assertFalse(active[1].cp['multiple'])
    def test_assessment_separation(self):
        source = Path('deck/week07.py').read_text()
        self.assertIn('10:00–10:30', source)
        self.assertIn('40 multiple-choice questions. 30 minutes. Open book.', source)
        self.assertIn('GROUP PROJECT / 40%', source)
        self.assertIn('1 November 2026, 23:59 HKT', source)
        self.assertIn('Agree the project scope by Week 8.', source)
    def test_registration(self):
        self.assertIn('"week07"', Path('deckgen.toml').read_text())
        self.assertIn('href="week07/"', Path('site/index.html').read_text())

if __name__ == '__main__': unittest.main()
