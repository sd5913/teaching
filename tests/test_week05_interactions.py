import importlib.util
import json
import sys
import unittest
from pathlib import Path

import deckgen

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = Path(deckgen.__file__).parent / 'js' / 'pyodide-runtime.py'


class Week05InteractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('week05', ROOT / 'deck/week05.py')
        cls.deck = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.deck)
        cls.exercises = {
            el.eid: el for slide in cls.deck.DECK['slides'] for el in slide.els
            if el.kind == 'exercise'
        }
        runtime = {}
        exec(RUNTIME.read_text(), runtime)
        cls.execute = staticmethod(runtime['_dg_run'])

    def test_browser_python_draws_and_checks_a_grayscale_image(self):
        ex = self.exercises['a-value-becomes-a-shade']
        initial = json.loads(self.execute(ex.code, ex.check, ex.expect))
        self.assertFalse(initial['ok'])
        self.assertIn('<svg', initial['out'])
        self.assertIn('<rect', initial['out'])
        fixed = json.loads(self.execute(ex.code.replace('255 - value', 'value'), ex.check, ex.expect))
        self.assertTrue(fixed['ok'], fixed['msg'])

    def test_browser_python_draws_and_checks_a_spatial_colour_rule(self):
        ex = self.exercises['change-the-rule-change-the-image']
        initial = json.loads(self.execute(ex.code, ex.check, ex.expect))
        self.assertFalse(initial['ok'])
        fixed = json.loads(self.execute(ex.code.replace('blue = 255 if x < 6 else 0',
                                               'blue = 255 if y < 6 else 0'),
                                   ex.check, ex.expect))
        self.assertTrue(fixed['ok'], fixed['msg'])

    def test_editable_frame_sketch_and_browser_exercises_share_deck(self):
        self.assertEqual(len(self.exercises), 3)
        sketches = [el for slide in self.deck.DECK['slides'] for el in slide.html_only]
        self.assertTrue(any(el.kind == 'editor' and el.eid == 'moving-pixels' for el in sketches))
        self.assertTrue(any(el.kind == 'sketch' and el.name == 'moving-pixels' for el in sketches))

    def test_api_browser_example_prints_json_without_sending_a_request(self):
        ex = self.exercises['a-prompt-is-part-of-the-request']
        self.assertNotIn('urlopen', ex.code)
        initial = json.loads(self.execute(ex.code, ex.check, ex.expect))
        self.assertFalse(initial['ok'])
        self.assertEqual(json.loads(initial['out'])['size'], '1024x1024')
        fixed = ex.code.replace('An orange circle', 'An orange circle on paper, centered')
        self.assertTrue(json.loads(self.execute(fixed, ex.check, ex.expect))['ok'])


if __name__ == '__main__':
    unittest.main()
