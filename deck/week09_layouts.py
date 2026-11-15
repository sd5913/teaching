"""Week 9 teaching compositions using Deckgen's native exportable elements."""

from deckgen.core import (
    BLUE, CODE, DEEP_TEAL, INK, LINE, MUTED, PAPER,
    Figure, Para, Rect, Run, Slide, T, Text, run_width,
)
from deckgen.figures import Canvas

ACTION = '#B74912'
CLIENT = BLUE
SERVER = DEEP_TEAL


def page(title, notes):
    slide = Slide(title=title, notes=notes)
    slide.els.append(T(120, 144, 1680, 164, title, 'xbold', 76, INK,
                       lh=1.02, spc=-0.025, name='lesson-title'))
    return slide


def takeaway(slide, text):
    if text:
        slide.els += [Rect(120, 848, 1680, 112, PAPER),
                      T(152, 870, 1616, 80, text, size=44, lh=1.18)]


def compare(title, left, right, notes, conclusion='', colors=(CLIENT, SERVER)):
    """Put equivalent ideas on the same baseline and the same surface."""
    slide = page(title, notes)
    for x, (heading, main, detail), color in (
        (120, left, colors[0]), (1000, right, colors[1]),
    ):
        slide.els += [Rect(x, 332, 760, 2, LINE),
                      T(x, 362, 760, 88, heading, 'bold', 56, color),
                      T(x, 478, 760, 144, main, 'semibold', 52, INK, lh=1.15),
                      T(x, 668, 760, 120, detail, size=40, color=MUTED, lh=1.25)]
    takeaway(slide, conclusion)
    return slide


def rows(title, items, notes, conclusion=''):
    slide = page(title, notes)
    colors = (CLIENT, SERVER, ACTION)
    for i, (label, text) in enumerate(items):
        y = 340 + i * 160
        slide.els += [Rect(120, y - 20, 1680, 2, LINE),
                      T(120, y + 12, 470, 114, label, 'bold', 52,
                        colors[i % len(colors)], lh=1.12),
                      T(650, y + 16, 1150, 114, text, size=46, lh=1.18)]
    takeaway(slide, conclusion)
    return slide


def _arrow(color):
    canvas = Canvas(80, 44)
    canvas.line(2, 22, 74, 22, color, 4)
    canvas.poly([(78, 22), (61, 10), (61, 34)], fill=color)
    return canvas.finish('week09-flow-arrow-' + color[1:])


def steps(title, items, notes, conclusion=''):
    slide = page(title, notes)
    colors = (CLIENT, ACTION, SERVER)
    for i, (heading, detail) in enumerate(items):
        x = 120 + i * 590
        slide.els += [T(x, 352, 130, 128, str(i + 1), 'xbold', 96, colors[i]),
                      T(x, 498, 480, 132, heading, 'bold', 54, lh=1.12),
                      T(x, 664, 480, 132, detail, size=40, color=MUTED, lh=1.25)]
        if i < len(items) - 1:
            svg, png = _arrow(colors[i])
            slide.els.append(Figure(x + 472, 390, 80, 44, svg, png))
    takeaway(slide, conclusion)
    return slide


def diagram(title, figure, notes):
    slide = page(title, notes)
    svg, png = figure
    slide.els.append(Figure(120, 320, 1680, 640, svg, png))
    return slide


def address(title, notes, remote=False):
    """Keep the URL intact; identify its parts with both labels and color."""
    slide = page(title, notes)
    parts = [
        ('https://' if remote else 'http://', 'Scheme', 'How to talk', MUTED),
        ('gallery.example' if remote else '127.0.0.1', 'Host', 'Which computer', CLIENT),
        ('/artworks/7' if remote else ':8009', 'Resource' if remote else 'Port',
         'Which artwork' if remote else 'Which service', ACTION if remote else SERVER),
    ]
    if not remote:
        parts.append(('/state', 'Path', 'What to request', ACTION))
    sizes = [run_width(Run(value, 'monobold', 64)) for value, *_ in parts]
    x = 120
    for width, (value, label, meaning, color) in zip(sizes, parts):
        slide.els.append(T(x, 422, round(width) + 4, 100, value, 'monobold', 64, color))
        x += width
    col_width = 1680 // len(parts)
    for i, (_, label, meaning, color) in enumerate(parts):
        x = 120 + i * col_width
        slide.els += [Rect(x, 594, col_width - 32, 2, color),
                      T(x, 626, col_width - 32, 72, label, 'bold', 48, color),
                      T(x, 718, col_width - 32, 104, meaning, size=40, lh=1.2)]
    takeaway(slide, 'The **address** names the resource. The **method** says what to do.' if remote else
              '**127.0.0.1** always means the computer making this request.')
    return slide


def lookup(notes):
    slide = page('DNS helps turn a name into an address.', notes)
    slide.els += [T(120, 350, 760, 72, 'Name', 'bold', 48, CLIENT),
                  T(120, 468, 760, 112, 'gallery.example', 'monobold', 70, CLIENT),
                  T(1120, 350, 680, 72, 'Example IP address', 'bold', 48, SERVER),
                  T(1120, 468, 680, 112, '192.0.2.23', 'monobold', 70, SERVER),
                  T(120, 664, 760, 96, 'Convenient for people.', size=44),
                  T(1120, 664, 680, 96, 'Used to reach the host.', size=44),
                  T(900, 418, 200, 72, 'DNS', 'bold', 48, ACTION)]
    svg, png = _arrow(ACTION)
    slide.els.append(Figure(930, 518, 80, 44, svg, png))
    takeaway(slide, 'Illustrative lookup. **127.0.0.1** is already an address: no lookup needed.')
    return slide


def code(title, lines, notes, conclusion, focus=()):
    from deckgen.syntax import LIGHT, highlight_runs
    from deckgen.core import runs

    slide = page(title, notes)
    slide.els.append(Rect(120, 340, 1680, 460, PAPER))
    for index in focus:
        slide.els.append(Rect(144, 382 + index * CODE * 1.45,
                              1632, CODE * 1.45, '#D3E7E8'))
    slide.els.append(Text(160, 382, 1600, 390,
                          [Para(highlight_runs(runs(line or ' ', 'mono', CODE),
                                              LIGHT, 'py'), lh=1.45)
                           for line in lines], name='code'))
    takeaway(slide, conclusion)
    return slide
