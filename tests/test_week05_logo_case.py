import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Week05LogoCaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('week05', ROOT / 'deck/week05.py')
        cls.deck = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.deck)
        cls.data = json.loads((ROOT / 'deck/week05_ascii_frames.json').read_text())

    def test_frames_trace_back_to_public_source_mark(self):
        source = ROOT / 'deck/assets/mark-18.png'
        self.assertEqual(self.data['source_sha256'], hashlib.sha256(source.read_bytes()).hexdigest())
        widths = [frame['columns'] for frame in self.data['frames']]
        self.assertEqual(widths, list(range(12, 67, 6)))
        self.assertGreater(len(set(frame['text'] for frame in self.data['frames'])), 3)
        self.assertTrue(all('\n' in frame['text'] for frame in self.data['frames']))

    def test_case_keeps_draft_edits_distinct_from_originals(self):
        for name in ('mark-18.png', 'mark-38.jpeg', 'week05-mark18-display-crop.png',
                     'week05-mark18-ascii-edit-input.png', 'week05-mark18-crt-draft.png',
                     'week05-mark38-wool-draft.png'):
            self.assertTrue((ROOT / 'deck/assets' / name).is_file(), name)
        titles = [slide.title for slide in self.deck.DECK['slides']]
        self.assertIn('Two marks, two source images', titles)
        self.assertIn('Keep the input; change the scene', titles)
        self.assertIn('Keep the shapes; change the material', titles)
        self.assertIn('Generated text is not guaranteed text', titles)

    def test_ascii_slider_and_python_are_separate_venues(self):
        slides = self.deck.DECK['slides']
        sketch = [el for slide in slides for el in slide.html_only
                  if el.kind == 'sketch' and el.name == 'logo-ascii-resolution']
        self.assertEqual(len(sketch), 1)
        self.assertIn('createSlider', sketch[0].code)
        code_slide = next(slide for slide in slides
                          if slide.title == 'One mark, several text widths')
        panel = ''.join(run.text for para in code_slide.els[3].paras for run in para.runs)
        self.assertIn('AsciiArt', panel)


if __name__ == '__main__':
    unittest.main()
