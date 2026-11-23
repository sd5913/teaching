"""Week 11 compositions reuse the established Week 9/10 slide grid."""
from pathlib import Path

from deckgen import Image, T
from deckgen.core import INK, MUTED
import week09_layouts as L

ASSETS = Path(__file__).resolve().parent / 'assets/week11'


def capture(heading, filename, caption, notes, url=''):
    slide = L.page(heading, notes)
    slide.els.append(Image(120, 320, 1680, 530, str(ASSETS / filename), 'contain'))
    text = f'[{caption}]({url})' if url else caption
    slide.els.append(T(120, 885, 1680, 94, text, size=40, color=MUTED, lh=1.16))
    return slide


def comparison(heading, left, right, labels, notes):
    slide = L.page(heading, notes)
    for x, filename, label in [(120, left, labels[0]), (1000, right, labels[1])]:
        slide.els.append(Image(x, 330, 800, 525, str(ASSETS / filename), 'contain'))
        slide.els.append(T(x, 884, 800, 90, label, 'semibold', 42, INK, lh=1.14))
    return slide


def github_details(heading, top, bottom, explanation, notes, wide=False):
    """Project tight, unaltered UI crops at a readable scale."""
    slide = L.page(heading, notes)
    slide.els.append(Image(120, 332, 1680, 300, str(ASSETS / top), 'contain'))
    if wide:
        slide.els += [Image(120, 652, 1680, 170, str(ASSETS / bottom), 'contain'),
                      T(120, 858, 1680, 110, explanation, size=44, color=INK, lh=1.2)]
    else:
        slide.els += [Image(120, 660, 840, 300, str(ASSETS / bottom), 'contain'),
                      T(1010, 682, 790, 260, explanation, size=44, color=INK, lh=1.2)]
    return slide
