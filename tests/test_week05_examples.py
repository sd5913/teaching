import contextlib
import io
import os
import sys
import tempfile
import unittest
from pathlib import Path

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
        self.assertIn('os.environ["EASEL_KEY"]', examples.API_EXAMPLE)
        self.assertIn('https://easel.ait4x.org/v1/images/generations', examples.API_EXAMPLE)
        self.assertNotIn('Bearer sk-', examples.API_EXAMPLE)


if __name__ == '__main__':
    unittest.main()
