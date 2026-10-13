"""The physical origin and an audible, finite demo belong before code excerpts."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'deck'))


class PhysicsOpeningTests(unittest.TestCase):
    def test_air_measurement_and_live_audio_precede_sample_code(self):
        import week06

        titles = [slide.title for slide in week06.S]
        air = titles.index('A vibration travels through air')
        lab = titles.index('Hear the rule. See its samples.')
        code = titles.index('A sound gives values positions in time')
        self.assertLess(air, lab)
        self.assertLess(lab, code)
        self.assertLess(lab, 8)
        self.assertTrue(any(el.kind == 'sketch' for el in week06.S[lab].html_only))
        self.assertIn('no microphone', week06.S[lab].notes.lower())

    def test_browser_source_is_finite_and_safe_by_default(self):
        source = (ROOT / 'deck/week06_sound_lab.js').read_text()
        self.assertIn('22050', source)
        self.assertIn('2 * RATE', source)
        self.assertIn('createBuffer', source)
        self.assertIn('slide:stop', source)
        self.assertNotIn('getUserMedia', source)
        self.assertNotIn('autoplay', source.lower())
        resources = (ROOT / 'site/week06/resources.html').read_text()
        self.assertIn('href="sketches/week06-sound-lab.html"', resources)
        self.assertIn('starts silent', resources)


if __name__ == '__main__':
    unittest.main()
