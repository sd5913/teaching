"""Run the real offline demos and inspect their PCM data, without playback."""
import importlib
import math
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
import unittest
import wave

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'site/week06/examples'))


class WavExamples(unittest.TestCase):
    def test_scripts_make_two_second_mono_pcm_files(self):
        for script in ('noise.py', 'tone.py'):
            with self.subTest(script=script), tempfile.TemporaryDirectory() as tmp:
                result = subprocess.run([sys.executable, str(ROOT / 'site/week06/examples' / script),
                                         '--out', tmp], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                path = Path(tmp) / script.replace('.py', '.wav')
                self.assertTrue(path.is_file())
                with wave.open(str(path), 'rb') as audio:
                    self.assertEqual(audio.getparams()[:4], (1, 2, 22050, 44100))
                    self.assertEqual(audio.getcomptype(), 'NONE')
                    values = struct.unpack('<44100h', audio.readframes(44100))
                self.assertEqual(values[0], 0)
                self.assertEqual(values[-1], 0)
                self.assertLessEqual(max(map(abs, values)), round(32767 * 0.08))

    def test_noise_repeats_with_same_seed(self):
        noise = importlib.import_module('noise')
        self.assertEqual(noise.make_samples(seed=7), noise.make_samples(seed=7))
        self.assertNotEqual(noise.make_samples(seed=7), noise.make_samples(seed=8))

    def test_tone_formula_matches_220_hz(self):
        tone = importlib.import_module('tone')
        samples = tone.make_samples()
        self.assertEqual(len(samples), 44100)
        self.assertAlmostEqual(samples[1000], 0.08 * math.sin(2 * math.pi * 220 * 1000 / 22050))

    def test_frequency_and_amplitude_are_independent(self):
        tone = importlib.import_module('tone')
        normal = tone.make_samples()
        quiet = tone.make_samples(amplitude=0.04)
        self.assertTrue(all(abs(a / 2 - b) < 1e-12 for a, b in zip(normal, quiet)))
        high = tone.make_samples(frequency=440)
        self.assertNotEqual(normal[1000:1100], high[1000:1100])

    def test_invalid_parameters_fail_before_file_write(self):
        noise = importlib.import_module('noise')
        tone = importlib.import_module('tone')
        for args in ({'seconds': 0}, {'seconds': 11}, {'amplitude': -1},
                     {'amplitude': float('nan')}, {'sample_rate': 0}):
            with self.subTest(args=args), self.assertRaises(ValueError):
                noise.make_samples(**args)
        with self.assertRaises(ValueError):
            tone.make_samples(frequency=11025)

    def test_writer_refuses_out_of_range_or_nonfinite_data(self):
        helper = importlib.import_module('wav_support')
        with tempfile.TemporaryDirectory() as tmp:
            for samples in ([2.0], [float('nan')], []):
                with self.subTest(samples=samples), self.assertRaises(ValueError):
                    helper.save_wav(Path(tmp) / 'bad.wav', samples, 22050)


if __name__ == '__main__':
    unittest.main()
