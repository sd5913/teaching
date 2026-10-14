"""Shared lesson scores and links must stay reproducible and safe to open."""
import base64
import importlib.util
from pathlib import Path
import tomllib
import sys
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

class Week06StrudelTests(unittest.TestCase):
    def module(self):
        path = ROOT / 'deck/week06_strudel.py'
        self.assertTrue(path.exists(), 'Week 6 Strudel stage module is missing')
        spec = importlib.util.spec_from_file_location('week06_strudel', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_four_stages_add_exactly_one_layer(self):
        m = self.module()
        self.assertEqual([s['id'] for s in m.STAGES], ['hi-hat', 'bass', 'chords', 'melody'])
        previous = []
        for stage in m.STAGES:
            score = stage['code']
            self.assertIn('setcpm(100/4)', score)
            layers = [line for line in score.splitlines() if line.startswith('  ')]
            self.assertEqual(layers[:-1], previous)
            previous = layers
            self.assertNotIn('.play(', score)
            self.assertNotIn('.bank(', score)
            self.assertNotIn('samples(', score)
        self.assertIn('hh*8', m.STAGES[0]['code'])
        self.assertIn('triangle', m.STAGES[1]['code'])
        self.assertIn('[c3,e3,g3]', m.STAGES[2]['code'])

    def test_links_decode_to_exact_source_and_downloads_match(self):
        m = self.module()
        for stage in m.STAGES:
            url = urlsplit(m.editor_link(stage['code']))
            self.assertEqual((url.scheme, url.netloc, url.path), ('https', 'strudel.cc', '/'))
            self.assertEqual(base64.b64decode(unquote(url.fragment)).decode(), stage['code'])
            saved = ROOT / 'site/week06/strudel' / (stage['id'] + '.strudel')
            self.assertTrue(saved.is_file())
            self.assertEqual(saved.read_text(), stage['code'])

    def test_resources_include_stages_pending_video_and_no_guessed_mock_url(self):
        m = self.module()
        page = (ROOT / 'site/week06/resources.html').read_text()
        for stage in m.STAGES:
            self.assertIn(m.editor_link(stage['code']), page)
        self.assertIn('Tutorial video: pending', page)
        self.assertIn('mock test on Canvas', page)
        self.assertNotIn('canvas.instructure.com', page)
        self.assertNotIn('<iframe', page)

    def test_stage_links_do_not_overlap_other_text(self):
        sys.path.insert(0, str(ROOT / 'deck'))
        from week06_livecoding_slides import livecoding_slides
        stages = livecoding_slides()[3:7]
        for slide in stages:
            texts = [el for el in slide.els if el.kind == 'text']
            link = next(el for el in texts if any(
                run.url and run.url.startswith('https://strudel.cc/#')
                for para in el.paras for run in para.runs))
            for other in texts:
                if other is link:
                    continue
                overlap = (link.x < other.x + other.w and link.x + link.w > other.x
                           and link.y < other.y + other.h and link.y + link.h > other.y)
                self.assertFalse(overlap, 'Strudel link overlaps another text box')

    def test_week06_is_registered_without_an_unconfirmed_date(self):
        cfg = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertIn('week06', cfg['course']['decks'])
        self.assertTrue(any(n['href'] == 'week06/' for n in cfg['nav']))
        page = (ROOT / 'site/index.html').read_text()
        self.assertIn('href="week06/"', page)
        self.assertNotIn('15 OCT', page)

if __name__ == '__main__':
    unittest.main()
