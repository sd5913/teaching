"""The Week 6 deck uses the same student sketches it teaches."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'deck'))


class NewSketches(unittest.TestCase):
    def test_piano_harmonics_and_voice_surface_live_in_student_module_and_deck(self):
        import week06
        titles = [slide.title for slide in week06.S]
        for title in ('Play a small keyboard piano', 'Build harmonics from a base frequency',
                      'Speak and see a flowing spectrum'):
            self.assertIn(title, titles)
        pfad = ROOT.parent / 'pfad-week06-review' / 'week06' / 'browser'
        for name in ('piano', 'harmonics', 'voice_surface'):
            self.assertTrue((ROOT / 'deck' / f'week06_{name}.js').is_file())
            if pfad.exists():
                self.assertEqual((ROOT / 'deck' / f'week06_{name}.js').read_bytes(),
                                 (pfad / f'{name}.js').read_bytes())
        if pfad.exists():
            for name in ('wav_support.py', 'noise.py', 'tone.py', 'request_song.py'):
                self.assertEqual((ROOT / 'site/week06/examples' / name).read_bytes(),
                                 (pfad.parent / 'sound' / name).read_bytes())
            for name in ('speech_webrtc.py', 'speech_webrtc_requirements.txt'):
                self.assertEqual((ROOT / 'site/week06/examples' / name).read_bytes(),
                                 (pfad.parent / 'speech' / name).read_bytes())

    def test_remove_artcraft_slide_and_ask_software_companies_question(self):
        import week06
        titles = [slide.title for slide in week06.S]
        self.assertNotIn('Rebuilding creative tools', titles)
        source = (ROOT / 'deck/news_20261014.py').read_text()
        self.assertIn('What is the future of software companies if anyone can create and modify software?', source)

    def test_resources_link_to_student_source_and_embedded_sketches(self):
        resources = (ROOT / 'site/week06/resources.html').read_text()
        speech = (ROOT / 'site/week06/speech.html').read_text()
        for path in ('sound/noise.py', 'sound/tone.py', 'sound/request_song.py',
                     'browser/piano.js', 'browser/harmonics.js', 'browser/voice_surface.js'):
            self.assertIn('week06/' + path, resources)
        for name in ('piano', 'harmonics', 'voice-surface'):
            self.assertIn(f'sketches/week06-{name}.html', resources)
        self.assertIn('week06/speech/speech_webrtc.py', speech)


if __name__ == '__main__':
    unittest.main()
