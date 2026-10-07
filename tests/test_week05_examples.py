import contextlib
import base64
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from PIL import Image

DECK_DIR = Path(__file__).resolve().parents[1] / 'deck'
sys.path.insert(0, str(DECK_DIR))

import week05_examples as examples


class Week05RunnableExampleTests(unittest.TestCase):
    def test_week05_deck_source_is_valid_python(self):
        source = (DECK_DIR / 'week05.py').read_text()
        compile(source, 'week05.py', 'exec')

    def test_all_complete_examples_are_used_in_slide_code_panels(self):
        import ast

        tree = ast.parse((DECK_DIR / 'week05.py').read_text())
        panel_examples = {
            node.value.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Attribute)
            and node.attr == 'splitlines'
            and isinstance(node.value, ast.Name)
        }
        slide_constants = {
            'tiny image': 'TINY_PIXEL_EXAMPLE',
            'random noise': 'NOISE_EXAMPLE',
            'frame animation': 'FRAME_EXAMPLE',
            'image API': 'API_EXAMPLE',
        }
        self.assertEqual(set(examples.RUNNABLE_EXAMPLES), set(slide_constants))
        self.assertTrue(set(slide_constants.values()) <= panel_examples)

    def run_example(self, name, code):
        tmp = tempfile.TemporaryDirectory()
        previous = Path.cwd()
        try:
            os.chdir(tmp.name)
            with contextlib.redirect_stdout(io.StringIO()):
                exec(compile(code, name, 'exec'), {'__name__': '__main__'})
            return tmp, Path(tmp.name)
        except Exception:
            tmp.cleanup()
            raise
        finally:
            os.chdir(previous)

    def test_slide_examples_are_valid_python(self):
        for name, code in examples.RUNNABLE_EXAMPLES.items():
            with self.subTest(name=name):
                compile(code, name, 'exec')

    def test_tiny_pixel_example_renders_expected_rgb_values(self):
        tmp, output = self.run_example('tiny_pixels', examples.TINY_PIXEL_EXAMPLE)
        try:
            with Image.open(output / 'tiny-image.png') as image:
                self.assertEqual(image.size, (120, 120))
                self.assertEqual(image.getpixel((30, 30)), (255, 0, 0))
                self.assertEqual(image.getpixel((90, 30)), (0, 255, 0))
        finally:
            tmp.cleanup()

    def test_advertised_pixel_edit_changes_only_the_top_right_pixel(self):
        import ast

        tree = ast.parse((DECK_DIR / 'week05.py').read_text())
        slide = next(node for node in ast.walk(tree)
                     if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                     and node.func.id == 'two_col' and len(node.args) >= 4
                     and isinstance(node.args[1], ast.Constant)
                     and node.args[1].value == 'Position first, channels second')
        panel = ast.literal_eval(slide.args[3])
        edit = next(line for line in panel if line.startswith('pixels[0][1] ='))
        code = examples.TINY_PIXEL_EXAMPLE.replace(
            '\nimage = Image.new', '\n' + edit + '\nimage = Image.new')
        tmp, output = self.run_example('edited_pixels', code)
        try:
            with Image.open(output / 'tiny-image.png') as image:
                self.assertEqual(image.getpixel((90, 30)), (255, 255, 255))
                self.assertEqual(image.getpixel((30, 30)), (255, 0, 0))
                self.assertEqual(image.getpixel((30, 90)), (0, 0, 255))
                self.assertEqual(image.getpixel((90, 90)), (255, 255, 0))
        finally:
            tmp.cleanup()

    def test_noise_example_saves_a_small_rgb_image(self):
        tmp, output = self.run_example('random_noise', examples.NOISE_EXAMPLE)
        try:
            with Image.open(output / 'noise.png') as image:
                self.assertEqual(image.size, (256, 256))
                self.assertEqual(image.mode, 'RGB')
        finally:
            tmp.cleanup()

    def test_frame_example_creates_an_ordered_three_frame_gif(self):
        tmp, output = self.run_example('moving_dot', examples.FRAME_EXAMPLE)
        try:
            with Image.open(output / 'moving-dot.gif') as image:
                self.assertEqual(image.n_frames, 3)
                self.assertEqual(image.info['duration'], 200)
            self.assertNotIn('streamlit', examples.FRAME_EXAMPLE.lower())
        finally:
            tmp.cleanup()

    def test_api_example_uses_environment_key_without_calling_the_service(self):
        response = io.BytesIO(json.dumps({
            'data': [{'b64_json': base64.b64encode(b'image fixture').decode()}],
        }).encode())
        with patch.dict(os.environ, {'EASEL_KEY': 'test-only-key'}), \
                patch('urllib.request.urlopen', return_value=response) as send:
            tmp, output = self.run_example('image_api', examples.API_EXAMPLE)
        try:
            request = send.call_args.args[0]
            self.assertEqual(request.full_url,
                             'https://easel.ait4x.org/v1/images/generations')
            self.assertEqual(request.get_header('Authorization'), 'Bearer test-only-key')
            self.assertEqual(json.loads(request.data)['n'], 1)
            self.assertEqual((output / 'api-image.png').read_bytes(), b'image fixture')
        finally:
            tmp.cleanup()


if __name__ == '__main__':
    unittest.main()
