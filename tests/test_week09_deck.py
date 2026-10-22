"""Week 9 story, diagrams and companion-link regression checks."""
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
    def test_story_from_existing_api_to_failure_and_project_choice(self):
        titles = [slide.title for slide in week09.S]
        stages = [titles.index(title) for title in (
            'One choice, one request',
            'The browser asks for records',
            'The server sends JSON back',
            'Two messages, one connection',
            'If the server stops after red, what can you conclude about blue?',
            'Agent, MCP server, tool',
            'Make the choice visible',
        )]
        self.assertEqual(stages, sorted(stages))
        self.assertEqual(len(week09.S), 29)
        self.assertTrue(all(slide.notes for slide in week09.S))

    def test_student_companion_is_linked_without_confusing_tcp_and_websocket(self):
        source = (ROOT / 'deck/week09.py').read_text()
        self.assertIn('plan/week09-companion-activity/week09/README.md', source)
        self.assertIn('not a runnable Python client', source)
        self.assertIn('tested stdlib loopback TCP echo starter, not WebSocket', source)
        self.assertNotIn('uv run week09/', source)

    def test_figures_are_readable_and_show_the_direction_of_messages(self):
        for method in (F.address, F.request, F.response, F.echo, F.tool_boundary):
            with self.subTest(figure=method.__name__):
                svg, png = method()
                root = ET.fromstring(svg)
                self.assertTrue(Path(png).is_file())
                labels = root.findall(f'.//{NS}text')
                self.assertTrue(labels)
                # Canvas width matches figure_slide width, so source pixels are design pixels.
                self.assertEqual(root.attrib['width'], '1680')
                self.assertTrue(all(float(t.attrib['font-size']) >= 40 for t in labels))
        self.assertIn('GET /tides?month=9', F.request()[0])
        self.assertIn('200 OK + JSON', F.response()[0])
        self.assertIn('send: hello', F.echo()[0])
        self.assertIn('reply: hello', F.echo()[0])
        self.assertIn('Human permission bounds the action.', F.tool_boundary()[0])

    def test_week09_is_registered_and_has_site_links(self):
        config = tomllib.loads((ROOT / 'deckgen.toml').read_text())
        self.assertIn('week09', config['course']['decks'])
        self.assertIn('week09/', [item['href'] for item in config['nav']])
        site = (ROOT / 'site/index.html').read_text()
        self.assertIn('href="week09/"', site)
        self.assertIn('href="week09/SD5913-week09.pdf"', site)
        self.assertIn('WEEK 09 · THU 5 NOV 2026', site)


if __name__ == '__main__':
    unittest.main()
