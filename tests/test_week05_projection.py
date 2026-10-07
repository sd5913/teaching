import importlib.util
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from deckgen.core import pil_font

DECK_DIR = Path(__file__).resolve().parents[1] / 'deck'
sys.path.insert(0, str(DECK_DIR))

import week05_figures as F


FIGURES = (
    'pixel_grid', 'grayscale_grid', 'frame_sequence', 'clip_alignment',
    'diffusion_training', 'vae_path', 'latent_diffusion', 'controlnet_canny',
)
WIDE_FIGURES = FIGURES[2:]
SVG_NS = '{http://www.w3.org/2000/svg}'


class Week05ProjectionFigureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Render each real Canvas once, including the PNG export used by PowerPoint.
        cls.rendered = {name: getattr(F, name)() for name in FIGURES}
        spec = importlib.util.spec_from_file_location('week05_projection',
                                                     DECK_DIR / 'week05.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        cls.placed = {
            Path(el.png).stem: el for slide in module.DECK['slides'] for el in slide.els
            if el.kind == 'figure'
        }

    def render(self, name):
        svg, png_path = self.rendered[name]
        self.assertTrue(svg.startswith('<svg'))
        self.assertTrue(Path(png_path).is_file())
        return svg

    def labels(self, name):
        return list(ET.fromstring(self.render(name)).iter(f'{SVG_NS}text'))

    def test_assets_have_week05_names(self):
        for name, (_, png_path) in self.rendered.items():
            with self.subTest(figure=name):
                self.assertEqual(Path(png_path).name,
                                 f"week05-{name.replace('_', '-')}.png")

    def test_primary_diagram_labels_are_at_least_40_slide_pixels(self):
        for name in FIGURES:
            source = ET.fromstring(self.render(name))
            figure = self.placed[f"week05-{name.replace('_', '-')}"]
            scale = figure.w / float(source.attrib['width'])
            primary = [label for label in self.labels(name)
                       if int(label.attrib['font-weight']) >= 700]
            self.assertTrue(primary, name)
            for label in primary:
                with self.subTest(figure=name, text=label.text):
                    self.assertGreaterEqual(float(label.attrib['font-size']) * scale, 40)

    def test_secondary_wide_diagram_labels_remain_readable(self):
        for name in WIDE_FIGURES:
            for label in self.labels(name):
                with self.subTest(figure=name, text=label.text):
                    self.assertGreaterEqual(float(label.attrib['font-size']), 30)

    def test_diagram_text_fits_the_canvas_and_its_box(self):
        for name in FIGURES:
            root = ET.fromstring(self.render(name))
            width, height = float(root.attrib['width']), float(root.attrib['height'])
            boxes = []
            for polygon in root.iter(f'{SVG_NS}polygon'):
                pts = [tuple(map(float, pair.split(',')))
                       for pair in polygon.attrib['points'].split()]
                boxes.append((min(x for x, _ in pts), min(y for _, y in pts),
                              max(x for x, _ in pts), max(y for _, y in pts)))
            bounds = []
            for label in self.labels(name):
                x, y = float(label.attrib['x']), float(label.attrib['y'])
                size = round(float(label.attrib['font-size']) * 2)
                mono = 'monospace' in label.attrib['font-family']
                font = pil_font('monomed' if mono else 'semibold', size)
                text_width = font.getlength(label.text) / 2
                ascent, _ = font.getmetrics()
                glyph = font.getbbox(label.text)
                anchor = label.attrib['text-anchor']
                left = x - text_width * {'start': 0, 'middle': .5, 'end': 1}[anchor]
                top, bottom = y - ascent / 2 + glyph[1] / 2, y - ascent / 2 + glyph[3] / 2
                right = left + text_width
                with self.subTest(figure=name, text=label.text):
                    self.assertGreaterEqual(left, 8)
                    self.assertLessEqual(right, width - 8)
                    self.assertGreaterEqual(top, 8)
                    self.assertLessEqual(bottom, height - 8)
                    for bx0, by0, bx1, by1 in boxes:
                        if bx0 < x < bx1 and by0 < y < by1:
                            self.assertGreaterEqual(left, bx0 + 8)
                            self.assertLessEqual(right, bx1 - 8)
                            self.assertGreaterEqual(top, by0 + 8)
                            self.assertLessEqual(bottom, by1 - 8)
                bounds.append((label.text, left, top, right, bottom))
            for i, (text, x0, y0, x1, y1) in enumerate(bounds):
                for other, ox0, oy0, ox1, oy1 in bounds[i + 1:]:
                    with self.subTest(figure=name, text=text, other=other):
                        self.assertFalse(x0 < ox1 and ox0 < x1 and y0 < oy1 and oy0 < y1,
                                         'diagram labels overlap')

    def test_diffusion_diagram_separates_training_and_generation(self):
        svg = self.render('diffusion_training')
        for label in ('TRAIN', 'GENERATE', 'U-Net', 'predict noise', 'compare',
                      'prediction vs noise', 'VAE decoder', 'RGB image'):
            self.assertIn(label, svg)

    def test_diffusion_diagram_shows_latent_encoding_before_training_noise(self):
        labels = [label.text for label in self.labels('diffusion_training')]
        self.assertLess(labels.index('VAE encoder'), labels.index('add noise'))
        for label in ('image to latent z0', 'noisy latent zt', 'random noise zT',
                      'clean latent z0'):
            self.assertIn(label, labels)

    def test_grayscale_grid_maps_sample_values_to_positions(self):
        svg = self.render('grayscale_grid')
        self.assertIn('one value at each row, column', svg)
        self.assertIn('240', svg)

    def test_clip_diagram_shows_two_encoders_and_similarity(self):
        svg = self.render('clip_alignment')
        for label in ('Text encoder', 'Image encoder', 'similarity', 'not a generator'):
            self.assertIn(label, svg)

    def test_vae_keeps_encoder_latent_decoder_order(self):
        labels = [label.text for label in self.labels('vae_path')]
        for before, after in (('image x', 'encoder'), ('encoder', 'latent z'),
                              ('latent z', 'decoder'), ('decoder', 'image x-hat')):
            self.assertLess(labels.index(before), labels.index(after))

    def test_classic_sd_path_keeps_prompt_conditioning_and_latent_decode(self):
        labels = [label.text for label in self.labels('latent_diffusion')]
        for before, after in (('latent noise', 'U-Net x N'), ('U-Net x N', 'clean latent'),
                              ('clean latent', 'VAE decoder'), ('VAE decoder', 'image')):
            self.assertLess(labels.index(before), labels.index(after))
        self.assertIn('text encoder', labels)
        self.assertIn('prompt vectors', labels)


if __name__ == '__main__':
    unittest.main()
