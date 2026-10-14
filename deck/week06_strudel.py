"""Cumulative Strudel scores shared by the slides, resources and tests.

Only bundled drums/native oscillators: website and Easel timbres may differ.
"""
import base64
from urllib.parse import quote

LAYERS = [
    's("hh*8").gain(.12)',
    'note("c2 ~ g2 ~").s("triangle").gain(.15)',
    'note("[c3,e3,g3]").s("sine").gain(.08)',
    'note("c4 e4 g4 b4").s("sine").gain(.12)',
]
STAGES = [
    {'id': key, 'label': label,
     'code': 'setcpm(100/4)\nstack(\n' + ''.join('  ' + line + ',\n' for line in LAYERS[:i+1]) + ')\n'}
    for i, (key, label) in enumerate([
        ('hi-hat', 'Hi-hat'), ('bass', 'Add bass'),
        ('chords', 'Add chords'), ('melody', 'Add melody'),
    ])
]


def editor_link(code):
    """The public Strudel editor decodes a base64 score from its URL fragment."""
    return 'https://strudel.cc/#' + quote(base64.b64encode(code.encode()).decode(), safe='')
