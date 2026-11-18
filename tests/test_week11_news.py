"""News integration preserves the existing lesson and evidence boundaries."""
import importlib.util
from pathlib import Path
import unittest
ROOT = Path(__file__).resolve().parents[1]
class NewsTest(unittest.TestCase):
    def test_four_news_slides_have_primary_sources_and_notes(self):
        spec = importlib.util.spec_from_file_location('news_week11', ROOT/'deck/week11.py')
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for slide, title, domain in zip(m.S[1:5], ['GPT-6.2 Astra and Sol', 'Gemini 4 Hydrogen', 'Qwen4-Max', 'Seedream 5.5 and Layers'], ['openai.com/', 'blog.google/', 'alibabacloud.com/', 'docs.dev.runwayml.com/']):
            self.assertEqual(slide.title, title)
            self.assertIn(domain, slide.notes)
        self.assertIn('open source', m.S[3].notes)
        self.assertIn('not native', m.S[4].notes)
