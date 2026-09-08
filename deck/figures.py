"""
Drawn figures for the SD5913 decks. Each returns (svg_markup, png_path), the pair
`deckgen.layouts` takes as `figure=`. The Canvas they are built on ships with deckgen;
these drawings are course-specific, so they live here.

    uv run deck/figures.py       # redraw them all into deck/assets/generated/
"""
from __future__ import annotations

import math
import random

from deckgen.figures import Canvas, INK

PAPER = '#FAF8F4'


def schotter(name='schotter', cols=12, rows=22, square=32, margin=40, chaos=1.0, seed=5913, w=None, h=None):
    """Georg Nees, Schotter, 1968 — the same rule as pfad/week01/first-repo/sketch.py, so the slide
    shows exactly what the tutorial file draws with its default numbers. Squares in a grid; each row
    is rotated and displaced a little more than the one above, and the damage grows with the square
    of the depth so the top stays calm and the bottom comes apart."""
    w = w or cols * square + margin * 2
    h = h or rows * square + margin * 2
    c = Canvas(w, h, bg=PAPER)
    rng = random.Random(seed)
    for row in range(rows):
        damage = chaos * (row / rows) ** 2
        for col in range(cols):
            x = margin + col * square
            y = margin + row * square
            angle = math.radians(rng.uniform(-1, 1) * damage * 45)
            dx = rng.uniform(-1, 1) * damage * square * 0.5
            dy = rng.uniform(-1, 1) * damage * square * 0.5
            cx, cy = x + square / 2 + dx, y + square / 2 + dy
            half = square / 2
            pts = []
            for px, py in ((-half, -half), (half, -half), (half, half), (-half, half)):
                pts.append((cx + px * math.cos(angle) - py * math.sin(angle),
                            cy + px * math.sin(angle) + py * math.cos(angle)))
            c.poly(pts, stroke=INK, width=1.4)
    return c.finish(name)


if __name__ == '__main__':
    print(schotter()[1])
