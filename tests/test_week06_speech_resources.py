"""Speech extensions stay optional and describe the tested interface honestly."""
from html.parser import HTMLParser
from pathlib import Path
import importlib.util
import sys
import unittest
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]

class Tags(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.items=[]
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        self.items.append((tag, dict(attrs)))

class SpeechResourcesTests(unittest.TestCase):
    def page(self):
        path=ROOT/'site/week06/speech.html'
        self.assertTrue(path.exists(), 'Speech exercise page is missing')
        return path.read_text()

    def module(self):
        path=ROOT/'deck/week06_speech_slides.py'
        self.assertTrue(path.exists(), 'Speech slides are missing')
        spec=importlib.util.spec_from_file_location('week06_speech_slides',path)
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_six_speech_slides_follow_music(self):
        slides=self.module().speech_slides()
        self.assertEqual(len(slides),6)
        sys.path.insert(0,str(ROOT/'deck'))
        import week06
        self.assertEqual(len(week06.S),65)

    def test_resource_page_has_local_navigation_and_no_recording_or_autoplay(self):
        for tag,attrs in Tags(self.page()).items:
            self.assertNotIn(tag,('script','iframe','audio','video'))
            self.assertNotIn('autoplay',attrs)
            href=attrs.get('href','')
            url=urlsplit(href)
            if href and not url.scheme and not url.netloc and url.path:
                self.assertTrue((ROOT/'site/week06'/url.path).exists(),href)
        self.assertIn('speech.html',(ROOT/'site/week06/resources.html').read_text())
        self.assertIn('examples/speech_webrtc.py', self.page())

    def test_speech_page_discloses_chunking_dependencies_and_verification_limits(self):
        page=self.page()
        for text in ('Kokoro','faster-whisper','Python 3.12','espeak-ng',
                     'chunked','Ctrl+C','model weights','consent','No microphone',
                     'not run','KittenTTS'):
            self.assertIn(text,page)
        self.assertNotIn('pip install whisper',page)

    def test_speech_page_distinguishes_input_and_output_sample_rates(self):
        page=self.page()
        self.assertIn('24,000',page)
        self.assertIn('16,000',page)
        self.assertIn('resampl',page)
        self.assertIn('hallucinat',page)

    def test_run_sheet_preserves_workshop_time_and_updates_slide_numbers(self):
        notes=(ROOT/'lessons/week06-lesson-plan.md').read_text()
        for text in ('50–70 | 25–34','70–88 | 35–38','92–106 | 46–52',
                     '106–116 | 54'):
            self.assertIn(text,notes)
        self.assertIn('bounded',notes)

if __name__ == '__main__':
    unittest.main()
