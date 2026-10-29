"""Primary diagram labels must remain readable and inside their actual canvas."""
import ast
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

from deckgen.core import pil_font
from deckgen.figures import Canvas

ROOT = Path(__file__).resolve().parents[1]


class DiagramTests(unittest.TestCase):
    def test_projected_tool_request_is_valid_json_and_python(self):
        tree = ast.parse((ROOT / 'deck/week11.py').read_text())
        for call in ast.walk(tree):
            if (isinstance(call, ast.Call) and isinstance(call.func, ast.Name)
                    and call.func.id == 'code' and call.args
                    and isinstance(call.args[0], ast.Constant)
                    and call.args[0].value == 'A tool call carries explicit arguments.'):
                request = json.loads('\n'.join(ast.literal_eval(call.args[1])))
                compile(request['params']['arguments']['code'], '<projected-tool>', 'exec')
                return
        self.fail('No projected tool request found')

    def test_primary_labels_fit_without_shrinking(self):
        spec = importlib.util.spec_from_file_location('week11_figures', ROOT / 'deck/week11_figures.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with patch.object(Canvas, 'finish', lambda self, name: '\n'.join(self.svg) + '</svg>'):
            for name in ['scene_outputs', 'blender_boundary', 'live_mcp', 'discovery',
                         'godot_boundary', 'behavior', 'evidence', 'failure']:
                svg = ET.fromstring(getattr(module, name)())
                for label in svg.findall('{http://www.w3.org/2000/svg}text'):
                    with self.subTest(diagram=name, text=label.text):
                        size = float(label.attrib['font-size'])
                        self.assertGreaterEqual(size, 40)
                        width = pil_font('monomed', round(size)).getlength(label.text or '')
                        x = float(label.attrib['x'])
                        anchor = label.attrib['text-anchor']
                        left = x - (width / 2 if anchor == 'middle' else width if anchor == 'end' else 0)
                        self.assertGreaterEqual(left, 0)
                        self.assertLessEqual(left + width, float(svg.attrib['width']))


if __name__ == '__main__':
    unittest.main()
