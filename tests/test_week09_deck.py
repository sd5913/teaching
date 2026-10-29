"""Export contracts for the Week 9 network lesson; runtime checks live in PFAD."""
import re
import sys
import tomllib
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'deck'))
import week09
import week09_figures as F

NS = '{http://www.w3.org/2000/svg}'


class Week09DeckTests(unittest.TestCase):
    def test_every_slide_has_speaker_notes(self):
        self.assertTrue(week09.S)
        self.assertTrue(all(slide.notes.strip() for slide in week09.S))

    def test_companion_is_pinned_to_a_commit(self):
        self.assertRegex(week09.PRACTICAL, r'/blob/[0-9a-f]{40}/week09/README\.md$')
        self.assertEqual(week09.SOURCE.rsplit('/', 2)[1], week09.REVISION)

    def test_message_figures_keep_legible_geometry(self):
        figures = [F.address(), F.layers(), F.framing(), F.uncertainty()]
        figures += [F.journey(stage) for stage in range(4)]
        for svg, png in figures:
            with self.subTest(asset=png):
                root = ET.fromstring(svg)
                self.assertEqual(root.attrib['width'], '1680')
                self.assertTrue(Path(png).is_file())
                labels = root.findall(f'.//{NS}text')
                self.assertTrue(labels)
                self.assertTrue(all(float(t.attrib['font-size']) >= 40 for t in labels))

    def test_registered_entry_has_both_public_links(self):
        config = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertIn('week09', config['course']['decks'])
        self.assertIn('week09/', [item['href'] for item in config['nav']])
        site = (ROOT / 'site/index.html').read_text()
        self.assertIn('href="week09/"', site)
        self.assertIn('href="week09/SD5913-week09.pdf"', site)


if __name__ == '__main__':
    unittest.main()
