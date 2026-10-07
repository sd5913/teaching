import ast
import importlib.util
from pathlib import Path
import tempfile
import unittest

from deckgen.core import html_slide

ROOT = Path(__file__).resolve().parents[1]
PROMPT = 'Should a developer understand every line of code they ship?'


def text_of(slide):
    return '\n'.join(run.text for el in slide.els if el.kind == 'text'
                     for para in el.paras for run in para.runs)


class Week05NewsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('week05', ROOT / 'deck/week05.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        cls.slides = module.DECK['slides']

    def test_poll_declarations_match_after_class_scanner_order(self):
        # Match weekly.py's literal question/layout(cp=...) contract, without
        # importing its network/reporting code. Both new polls must be visible.
        tree = ast.parse((ROOT / 'deck/week05.py').read_text())
        found = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
                continue
            if node.func.id == 'question':
                args = node.args[1:]
            elif node.func.id == 'content' and any(k.arg == 'cp' for k in node.keywords):
                args = node.args[1:2]
            else:
                continue
            label = next((a.value for a in args
                          if isinstance(a, ast.Constant) and isinstance(a.value, str)), None)
            found.append((node.lineno, label))
        self.assertEqual([title for _, title in sorted(found)],
                         [slide.title for slide in self.slides if slide.cp])

    def test_news_helper_invalidates_pptx_cache(self):
        workflow = (ROOT / '.github/workflows/pptx.yml').read_text()
        self.assertIn("hashFiles('deck/**/*.py'", workflow)

    def test_three_opening_slides_keep_the_existing_lesson(self):
        self.assertEqual(len(self.slides), 57)
        self.assertIn('Images & video', self.slides[0].title)
        self.assertEqual(self.slides[5].title, 'Start with values')
        self.assertEqual(sum(slide.title == 'A value becomes a shade' for slide in self.slides), 1)
        self.assertIn('8 October 2026', text_of(self.slides[0]))
        self.assertIn('1 October holiday', text_of(self.slides[0]))
        self.assertNotIn('1 November 2026', '\n'.join(text_of(s) for s in self.slides))

    def test_before_after_are_independent_polls_with_identical_prompt_and_choices(self):
        before, after = self.slides[1], self.slides[3]
        self.assertIn(PROMPT, text_of(before))
        self.assertIn(PROMPT, text_of(after))
        self.assertEqual(before.cp, {'type': 'multiple_choice', 'choices': ['A', 'B', 'C']})
        self.assertEqual(before.cp, after.cp)
        self.assertIsNot(before.cp, after.cp)
        for slide in (before, after):
            self.assertIn('A  Agree', text_of(slide))
            self.assertIn('B  Unsure', text_of(slide))
            self.assertIn('C  Disagree', text_of(slide))
            self.assertTrue(any(el.name == 'question-eyebrow' for el in slide.els))
        self.assertNotEqual(before.title, after.title)

    def test_sources_and_dates_do_not_imply_september_29_caused_the_keynote(self):
        before, news, after = self.slides[1:4]
        self.assertIn('13 MAY 2025', text_of(before))
        self.assertIn('23 SEPTEMBER 2026', text_of(after))
        self.assertIn('came after the keynote', text_of(news))
        for source in ('https://www.anthropic.com/claude-opus-5-5',
                       'https://openai.com/index/introducing-gpt-6-1-sol/',
                       'https://openai.com/index/introducing-dots/'):
            self.assertIn(source, news.notes)
        self.assertIn('vendor', text_of(news).lower())
        self.assertIn('different tests', text_of(news).lower())

    def test_official_video_has_an_embed_and_timestamped_static_fallback(self):
        after = self.slides[3]
        embeds = [el for el in after.html_only if el.kind == 'embed']
        self.assertEqual(len(embeds), 1)
        self.assertEqual(embeds[0].yt, 'vDjW_dRyKXY')
        self.assertEqual(embeds[0].thumb, 'week05-keynote-poster.png')
        self.assertIn('28:14–31:14', text_of(after))
        urls = [run.url for el in after.els if el.kind == 'text'
                for para in el.paras for run in para.runs if run.url]
        self.assertIn('https://www.youtube.com/watch?v=vDjW_dRyKXY&t=1694s', urls)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            rendered = html_slide(after, 4, root, root / 'assets', 'assets')
        self.assertIn('https://www.youtube-nocookie.com/embed/vDjW_dRyKXY?rel=0', rendered)
        self.assertIn('print-only', rendered)
        self.assertIn('t=1694s', rendered)


if __name__ == '__main__':
    unittest.main()
