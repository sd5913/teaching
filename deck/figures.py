"""
Drawn figures for the SD5913 decks. Each returns (svg_markup, png_path), the pair
`deckgen.layouts` takes as `figure=`. The Canvas they are built on ships with deckgen;
these drawings are course-specific, so they live here.

    uv run deck/figures.py       # redraw them all into deck/assets/generated/

The week 3 figures are all drawn from the two files committed under deck/assets/data/ —
the Observatory's tide table for 2026 and a month of USGS earthquakes — so a slide and
the tutorial's scripts are reading the same numbers. Nothing here is traced.
"""
from __future__ import annotations

import csv
import json
import math
import random
from datetime import date
from pathlib import Path

from deckgen.figures import Canvas, INK, ORANGE, MUTED, LINE, TEAL, VIOLET

PAPER = '#FAF8F4'
DATA = Path(__file__).resolve().parent / 'assets' / 'data'

# 17 September 2026 — the day of the class, and row 259 of the Observatory's file.
DAY = 259


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


def nake(name='nake', n=30, size=600, h_prob=0.20, seed=1966):
    """Frieder Nake, Walk-through-Raster, 1966 — the rule of pfad's 2025 `extra/nake/main.py`, drawn
    with lines instead of characters. Column by column, top down: a vertical bar is likelier the
    closer the cell is to the diagonal; a horizontal cap is drawn only when the cell above was
    left empty. That second condition is the one the picture lets you check."""
    c = Canvas(size, size, bg=PAPER)
    rng = random.Random(seed)
    g = size / (n + 2)
    last_empty = False
    for w in range(n):
        for h in range(n):
            x, y = (w + 1) * g, (h + 1) * g
            bar = rng.randint(0, n - 2) >= abs(w - h)
            cap = rng.randint(0, n) > h_prob * n and last_empty
            if bar:
                c.line(x, y, x, y + g, INK, 1.6, cap='butt')
            if cap:
                c.line(x, y, x + g, y, INK, 1.6, cap='butt')
            last_empty = not (bar or cap)
    return c.finish(name)


# ───────────────────────── week 3 · the numbers themselves ─────────────────────────
#
# Everything below reads deck/assets/data/. tides-QUB-2026.json is the Hong Kong
# Observatory's hourly tide table for Quarry Bay, verbatim (fields, then 365 rows of
# month, day and 24 heights in metres above chart datum, as strings).
# earthquakes-2026-09.csv is mag,lng,lat,depth,time trimmed from the USGS 2.5+ month
# feed. The slides quote both; these drawings are made from them so the two agree.


def _year(station='QUB', year=2026):
    """[(date, [24 floats]), …] — one entry per day of the Observatory's file."""
    raw = json.loads((DATA / f'tides-{station}-{year}.json').read_text(encoding='utf-8'))
    return [(date(year, int(r[0]), int(r[1])), [float(v) for v in r[2:]])
            for r in raw['data']]


def _day(index=DAY):
    return _year()[index][1]


def _month(month=9):
    return [(d, h) for d, h in _year() if d.month == month]


NEW_MOON = date(2000, 1, 6)          # a known new moon — the slide shows this constant


def _moon_age(day):
    """Days since the last new moon, on a 29.53-day cycle. The same five lines as the slide."""
    return (day - NEW_MOON).days % 29.53


def _mix(a, b, t):
    """Blend two #rrggbb strings. t=0 gives a, t=1 gives b."""
    t = min(1.0, max(0.0, t))
    pa = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    pb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return '#%02X%02X%02X' % tuple(round(x + (y - x) * t) for x, y in zip(pa, pb))


# ── the two panels every tide figure is built from ──

def _line_panel(c, heights, x, y, w, h, lo=0.8, hi=2.45, dots=True, labels=True,
                color=ORANGE, width=3.4, grid=True):
    """A day as a line: hour across, metres up."""
    pad_l = 64 if labels else 10
    pad_b = 40 if labels else 10
    px, py = x + pad_l, y + 14
    pw, ph = w - pad_l - 14, h - pad_b - 14

    def X(hour):
        return px + (hour - 1) / 23 * pw

    def Y(v):
        return py + (hi - v) / (hi - lo) * ph

    if grid:
        for v in (1.0, 1.5, 2.0):
            c.line(px, Y(v), px + pw, Y(v), LINE, 1.5)
            if labels:
                c.text(px - 12, Y(v) + 7, f'{v:.1f}', 20, MUTED, anchor='end')
        for hour in (1, 6, 12, 18, 24):
            c.line(X(hour), py, X(hour), py + ph, LINE, 1.5)
            if labels:
                c.text(X(hour), py + ph + 30, f'{hour:02d}', 20, MUTED, anchor='middle')
    pts = [(X(i + 1), Y(v)) for i, v in enumerate(heights)]
    for a, b in zip(pts, pts[1:]):
        c.line(a[0], a[1], b[0], b[1], color, width)
    if dots:
        for p in pts:
            c.circle(p[0], p[1], 4.6, fill=color)
    return X, Y


def _clock_panel(c, heights, x, y, w, h, labels=True, hi=2.45,
                 color=ORANGE, width=3.4, dots=True):
    """The same day bent round: hour -> angle, height -> radius.

    Exactly the `to_xy` of the drill — x = r·cos(a), y = r·sin(a) — drawn in screen
    coordinates, where y counts downwards, so midnight sits at the right and the day
    runs clockwise."""
    cx, cy = x + w / 2, y + h / 2
    rad = min(w, h) / 2 - (46 if labels else 16)

    def R(v):
        return max(0.0, v) / hi * rad

    for v in (1.0, 2.0):
        c.circle(cx, cy, R(v), stroke=LINE, width=1.5)
    for hour in range(0, 24, 3):
        a = hour / 24 * 2 * math.pi
        c.line(cx, cy, cx + rad * math.cos(a), cy + rad * math.sin(a), LINE, 1.2)
    if labels:
        for hour in (6, 12, 18, 24):
            a = hour / 24 * 2 * math.pi
            c.text(cx + (rad + 28) * math.cos(a), cy + (rad + 28) * math.sin(a) + 7,
                   f'{hour:02d}', 20, MUTED, anchor='middle')
        c.text(cx + 12, cy - R(1.0) + 7, '1 m', 18, MUTED)
        c.text(cx + 12, cy - R(2.0) + 7, '2 m', 18, MUTED)
    pts = []
    for hour, v in enumerate(heights, start=1):
        a = hour / 24 * 2 * math.pi
        pts.append((cx + R(v) * math.cos(a), cy + R(v) * math.sin(a)))
    c.poly(pts, stroke=color, width=width)
    if dots:
        for p in pts:
            c.circle(p[0], p[1], 4.4, fill=color)
    return cx, cy, rad


# ── the seven figures the week 3 deck asks for ──

def tide_day(name='tide-day', w=820, h=560):
    """One day of the Observatory's table as a line: the 24 numbers of the lecture.
    High water at 01:00, low water at 07:00 — both are marked, because the picture has
    to agree with the file a student can open."""
    hs = _day()
    c = Canvas(w, h, bg=PAPER)
    X, Y = _line_panel(c, hs, 0, 0, w, h - 34)
    lo_i, hi_i = hs.index(min(hs)), hs.index(max(hs))
    c.circle(X(lo_i + 1), Y(hs[lo_i]), 9, stroke=TEAL, width=3)
    c.text(X(lo_i + 1) + 16, Y(hs[lo_i]) + 30, f'low {hs[lo_i]:.2f} m at {lo_i + 1:02d}:00',
           20, TEAL)
    c.circle(X(hi_i + 1), Y(hs[hi_i]), 9, stroke=INK, width=3)
    c.text(X(hi_i + 1) + 16, Y(hs[hi_i]) - 14, f'high {hs[hi_i]:.2f} m at {hi_i + 1:02d}:00',
           20, INK)
    c.text(10, h - 8, 'Quarry Bay · 17 September 2026 · metres above chart datum',
           20, MUTED)
    return c.finish(name)


def tide_bars(name='tide-bars', w=1560, h=470):
    """The first picture of the day, and no library made it: one row per hour, one block
    per `round(height * 10)`. This is what `bar()` prints, drawn. Twelve hours a column,
    so it reads across a projector rather than down one."""
    hs = _day()
    c = Canvas(w, h, bg=PAPER)
    box, gap, y0 = 26, 4, 30
    for i, v in enumerate(hs):
        col, row = divmod(i, 12)
        x0 = 92 + col * 780
        y = y0 + row * (box + gap)
        c.text(x0 - 16, y + box - 5, f'{i + 1:2d}', 22, MUTED, anchor='end')
        fill = TEAL if v == min(hs) else ORANGE if v == max(hs) else INK
        for k in range(round(v * 10)):
            c.rect(x0 + k * (box + gap), y, box, box, fill=fill)
    c.text(92, h - 16, 'bar(height) = "#" * round(height * 10)    ·    '
                       'hours 01-12 on the left, 13-24 on the right', 22, MUTED)
    return c.finish(name)


def tide_clock(name='tide-clock', pair=True, size=620, gap=64):
    """The same 24 numbers, bent. `pair` puts the line and the clock side by side —
    one transformation apart — and `pair=False` gives the clock on its own, which is
    what the live sketch is laid over."""
    w = size * 2 + gap if pair else size
    c = Canvas(w, size, bg=PAPER)
    hs = _day()
    ox = 0
    if pair:
        _line_panel(c, hs, 0, 0, size, size - 34)
        c.text(size / 2, size - 8, 'hour across, height up', 20, MUTED, anchor='middle')
        ox = size + gap
    _clock_panel(c, hs, ox, 0, size, size - 34)
    c.text(ox + size / 2, size - 8, 'hour round, height out', 20, MUTED, anchor='middle')
    return c.finish(name)


def tide_ways(name='tide-ways', w=1680, h=600):
    """Five ways to look at the same table: the day as a line, as bars, as a clock;
    the whole of September overlaid; September as a grid of colour, day by hour."""
    c = Canvas(w, h, bg=PAPER)
    hs = _day()
    sept = _month(9)
    m, g = 16, 14
    pw = (w - 2 * m - 4 * g) / 5
    ph = h - 74

    def panel(i):
        return m + i * (pw + g)

    def cap(i, text):
        c.text(panel(i) + pw / 2, h - 22, text, 21, MUTED, anchor='middle')

    # 1 · the line
    _line_panel(c, hs, panel(0), 0, pw, ph, labels=False, dots=False, width=3)
    cap(0, 'a line')

    # 2 · bars
    x0, y0 = panel(1) + 14, 20
    bw, bh = (pw - 28) / 24, ph - 40
    for i, v in enumerate(hs):
        t = (v - 0.8) / 1.65
        c.rect(x0 + i * bw + 1.5, y0 + (1 - t) * bh, bw - 3, t * bh + 2, fill=INK)
    cap(1, 'bars')

    # 3 · the clock
    _clock_panel(c, hs, panel(2), 0, pw, ph, labels=False, dots=False, width=2.6)
    cap(2, 'a clock')

    # 4 · thirty days overlaid
    for d, day_hs in sept:
        _line_panel(c, day_hs, panel(3), 0, pw, ph, lo=0.45, hi=2.55, labels=False,
                    dots=False, grid=d.day == 1, color=_mix(PAPER, MUTED, 0.85), width=1.4)
    _line_panel(c, hs, panel(3), 0, pw, ph, lo=0.45, hi=2.55, labels=False, dots=False,
                grid=False, color=ORANGE, width=3)
    cap(3, 'thirty days at once')

    # 5 · the month as a grid of colour
    gx, gy = panel(4) + 8, 16
    cw, ch = (pw - 16) / 24, (ph - 24) / len(sept)
    for r, (d, day_hs) in enumerate(sept):
        for hour, v in enumerate(day_hs):
            c.rect(gx + hour * cw, gy + r * ch, cw + 0.6, ch + 0.6,
                   fill=_mix(TEAL, INK, (v - 0.75) / 1.75))
    cap(4, 'a month, day x hour')
    return c.finish(name)


def tide_moon(name='tide-moon', w=820, h=600):
    """September's daily range (max - min of the 24 heights) against the moon.
    The model says the tide is biggest at new and full moon. The data agrees, roughly,
    and the roughness is the interesting part — the peaks land a day or two early."""
    sept = _month(9)
    c = Canvas(w, h, bg=PAPER)
    px, py = 78, 104
    pw, ph = w - px - 24, h - py - 92
    ranges = [max(hs) - min(hs) for _, hs in sept]
    hi = 2.0
    bw = pw / len(sept)

    def Y(v):
        return py + (hi - v) / hi * ph

    for v in (0.5, 1.0, 1.5, 2.0):
        c.line(px, Y(v), px + pw, Y(v), LINE, 1.5)
        c.text(px - 12, Y(v) + 7, f'{v:.1f}', 20, MUTED, anchor='end')
    c.line(px, Y(0), px + pw, Y(0), MUTED, 1.5)

    # the two days the model calls new and full moon
    ages = [_moon_age(d) for d, _ in sept]
    new_i = min(range(len(ages)), key=lambda i: min(ages[i], 29.53 - ages[i]))
    full_i = min(range(len(ages)), key=lambda i: abs(ages[i] - 29.53 / 2))
    for i, label in ((new_i, 'new moon'), (full_i, 'full moon')):
        x = px + (i + 0.5) * bw
        c.line(x, py - 22, x, Y(0), _mix(PAPER, VIOLET, 0.55), 2)
        c.text(x, py - 32, label, 20, VIOLET, anchor='middle')
        c.circle(x, py - 62, 12, fill=VIOLET if label == 'new moon' else PAPER,
                 stroke=VIOLET, width=2.5)

    for i, v in enumerate(ranges):
        top = Y(v)
        c.rect(px + i * bw + 2, top, bw - 4, Y(0) - top, fill=ORANGE)
    for i in (0, 9, 19, 29):
        c.text(px + (i + 0.5) * bw, Y(0) + 32, f'{sept[i][0].day:02d}', 20, MUTED,
               anchor='middle')
    peak = max(range(len(ranges)), key=lambda i: ranges[i])
    trough = min(range(len(ranges)), key=lambda i: ranges[i])
    c.text(px + (peak + 0.5) * bw, Y(ranges[peak]) - 14,
           f'{ranges[peak]:.2f}', 20, INK, anchor='middle')
    c.text(px + (trough + 0.5) * bw, Y(ranges[trough]) - 14,
           f'{ranges[trough]:.2f}', 20, INK, anchor='middle')
    c.text(px - 66, py - 10, 'metres', 20, MUTED)
    c.text(px, h - 18, 'daily range = max - min of the 24 heights', 20, MUTED)
    return c.finish(name)


def transforms(name='transforms', w=820, h=480):
    """One triangle, three functions. The faint shape is the original in every panel;
    the solid one is what `move`, `scale` and `rotate` gave back. A loop applies one of
    them to every point, which is the whole of the next four slides."""
    shape = [(0, 0), (100, 0), (50, 80)]

    def mv(p, dx, dy):
        return (p[0] + dx, p[1] + dy)

    def sc(p, k):
        return (p[0] * k, p[1] * k)

    def rot(p, a):
        return (p[0] * math.cos(a) - p[1] * math.sin(a),
                p[0] * math.sin(a) + p[1] * math.cos(a))

    c = Canvas(w, h, bg=PAPER)
    panels = [('the shape', shape, INK),
              ('move(p, 70, 40)', [mv(p, 70, 40) for p in shape], ORANGE),
              ('scale(p, 1.6)', [sc(p, 1.6) for p in shape], TEAL),
              ('rotate(p, 0.5)', [rot(p, 0.5) for p in shape], VIOLET)]
    pw, ph = w / 2, h / 2
    for i, (label, pts, col) in enumerate(panels):
        ox = (i % 2) * pw + 56
        oy = (i // 2) * ph + 90
        c.text(ox - 20, oy - 34, label, 22, col)
        c.line(ox - 16, oy, ox + pw - 90, oy, LINE, 1.5)
        c.line(ox, oy - 16, ox, oy + 142, LINE, 1.5)
        if i:
            c.poly([(ox + x, oy + y) for x, y in shape], stroke=_mix(PAPER, MUTED, 0.6),
                   width=2)
        c.poly([(ox + x, oy + y) for x, y in pts], stroke=col, width=3.4)
    return c.finish(name)


def quake_map(name='quake-map', w=1060, h=560):
    """Every earthquake of magnitude 2.5 and up in the USGS month feed: three numbers a
    point — longitude, latitude, magnitude. The projection is the cheapest one there is
    (lng -> x, lat -> y, equirectangular), and the plate boundaries draw themselves."""
    c = Canvas(w, h, bg=PAPER)
    px, py = 20, 24
    pw, ph = w - 40, h - 92
    c.rect(px, py, pw, ph, stroke=LINE, width=1.5)
    for lng in range(-120, 180, 60):
        x = px + (lng + 180) / 360 * pw
        c.line(x, py, x, py + ph, LINE, 1.2)
    for lat in (-60, -30, 0, 30, 60):
        y = py + (90 - lat) / 180 * ph
        c.line(px, y, px + pw, y, MUTED if lat == 0 else LINE, 1.6 if lat == 0 else 1.2)
    biggest = None
    with (DATA / 'earthquakes-2026-09.csv').open(encoding='utf-8') as fh:
        for row in csv.DictReader(fh):
            mag = float(row['mag'])
            x = px + (float(row['lng']) + 180) / 360 * pw
            y = py + (90 - float(row['lat'])) / 180 * ph
            r = 2.4 + max(0.0, mag - 2.5) * 1.9
            col = ORANGE if mag >= 5 else INK if mag >= 4 else TEAL
            c.circle(x, y, r, stroke=col, width=1.8)
            if biggest is None or mag > biggest[0]:
                biggest = (mag, x, y)
    c.circle(biggest[1], biggest[2], 22, stroke=ORANGE, width=3)
    c.text(biggest[1] + 32, biggest[2] + 9, f'M {biggest[0]}', 26, ORANGE)
    c.text(px + 10, py + ph / 2 - 12, 'equator', 24, MUTED)
    kx, ky = px + 24, py + ph - 30
    for i, (col, lab) in enumerate(((TEAL, 'M 2.5-4'), (INK, 'M 4-5'), (ORANGE, 'M 5+'))):
        c.circle(kx + i * 200, ky, 4 + i * 5, stroke=col, width=2.4)
        c.text(kx + i * 200 + 26, ky + 9, lab, 24, MUTED)
    c.text(px, h - 18, 'USGS · magnitude 2.5 and up · one month', 24, MUTED)
    return c.finish(name)


if __name__ == '__main__':
    for fig in (schotter, nake, tide_day, tide_bars, tide_clock, tide_ways,
                tide_moon, transforms, quake_map):
        print(fig()[1])
    print(tide_clock('tide-clock-solo', pair=False)[1])
