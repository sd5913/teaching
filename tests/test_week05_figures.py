import sys
import unittest
from pathlib import Path

DECK_DIR = Path(__file__).resolve().parents[1] / 'deck'
sys.path.insert(0, str(DECK_DIR))

import week05_figures as F


class Week05FigureTests(unittest.TestCase):
    def render(self, name):
        self.assertTrue(hasattr(F, name), f'missing figure function: {name}')
        svg, png_path = getattr(F, name)()
        self.assertTrue(svg.startswith('<svg'))
        self.assertTrue(Path(png_path).is_file())
        return svg

    def test_diffusion_diagram_separates_training_and_generation(self):
        svg = self.render('diffusion_training')
        self.assertIn('TRAIN', svg)
        self.assertIn('GENERATE', svg)
        self.assertIn('U-Net', svg)
        self.assertIn('noise', svg)

    def test_diffusion_diagram_shows_latent_encoding_before_training_noise(self):
        svg = self.render('diffusion_training')
        self.assertIn('VAE encoder -> z0', svg)
        self.assertIn('sample zt', svg)
        self.assertIn('noisy latent', svg)
        self.assertIn('random noise zT', svg)
        self.assertIn('updates model weights', svg)
        self.assertIn('weights stay fixed', svg)

    def test_grayscale_grid_maps_sample_values_to_positions(self):
        svg = self.render('grayscale_grid')
        self.assertIn('one value at each row, column', svg)
        self.assertIn('240', svg)

    def test_clip_diagram_shows_two_encoders_and_similarity(self):
        svg = self.render('clip_alignment')
        self.assertIn('Text encoder', svg)
        self.assertIn('Image encoder', svg)
        self.assertIn('similarity', svg)
        self.assertIn('not a generator', svg)

    def test_prompt_conditions_denoiser_and_vae_samples_latent(self):
        self.assertIn('prompt', self.render('latent_diffusion'))
        self.assertIn('conditioning', self.render('latent_diffusion'))
        self.assertIn('mean + variance', self.render('vae_path'))
        self.assertIn('sample z', self.render('vae_path'))


if __name__ == '__main__':
    unittest.main()
