"""Export contracts for the Week 9 network lesson; runtime checks live in PFAD."""
import re
from deckgen.core import pil_font
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
        figures = [F.address(), F.layers(), F.framing(), F.uncertainty(),
                   F.network_growth(), F.osi_layers(), F.tcp_handshake(),
                   F.endpoint_connections(), F.host_route(),
                   F.encapsulation(), F.request_response()]
        figures += [F.packet_delivery(mode) for mode in
                    ('unicast', 'broadcast', 'multicast')]
        figures += [F.journey(stage) for stage in range(4)]
        for svg, png in figures:
            with self.subTest(asset=png):
                root = ET.fromstring(svg)
                self.assertEqual(root.attrib['width'], '1680')
                self.assertTrue(Path(png).is_file())
                labels = root.findall(f'.//{NS}text')
                self.assertTrue(labels)
                self.assertTrue(all(float(t.attrib['font-size']) >= 40 for t in labels))
                # Measure the rendered label extent, not only its anchor point.
                width, height = float(root.attrib['width']), float(root.attrib['height'])
                for label in labels:
                    size = float(label.attrib['font-size'])
                    font = pil_font('monomed', round(size * 2))
                    span = font.getlength(''.join(label.itertext())) / 2
                    x, y = float(label.attrib['x']), float(label.attrib['y'])
                    anchor = label.attrib.get('text-anchor', 'start')
                    left = x - (span / 2 if anchor == 'middle' else span if anchor == 'end' else 0)
                    self.assertGreaterEqual(left, 0, label.text)
                    self.assertLessEqual(left + span, width, label.text)
                    self.assertGreaterEqual(y - size, 0, label.text)
                    self.assertLessEqual(y, height, label.text)

    def test_delivery_modes_produce_distinct_diagrams_and_reject_unknown_mode(self):
        diagrams = {F.packet_delivery(mode)[0] for mode in
                    ('unicast', 'broadcast', 'multicast')}
        self.assertEqual(len(diagrams), 3)
        with self.assertRaises(ValueError):
            F.packet_delivery('websocket')

    def test_project_ama_accepts_open_responses_without_a_quiz_key(self):
        activity = next(slide.cp for slide in week09.S
                        if slide.title == 'Ask me anything about the group project')
        self.assertEqual(activity['type'], 'short_answer')
        self.assertNotIn('choices', activity)
        self.assertNotIn('correct', activity)

    def test_registered_entry_has_both_public_links(self):
        config = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertIn('week09', config['course']['decks'])
        self.assertIn('week09/', [item['href'] for item in config['nav']])
        site = (ROOT / 'site/index.html').read_text()
        self.assertIn('href="week09/"', site)
        self.assertIn('href="week09/SD5913-week09.pdf"', site)


if __name__ == '__main__':
    unittest.main()
