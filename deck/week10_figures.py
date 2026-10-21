"""Week 10 object and persistence diagrams, on a projector-sized canvas."""

from deckgen.figures import Canvas, INK, MUTED, ORANGE, TEAL, VIOLET

PAPER = '#FAF8F4'
WHITE = '#FFFFFF'


def text(c, x, y, value, size=46, color=INK, anchor='start'):
    c.text(x, y, value, size=size, color=color, anchor=anchor, weight=700)


def box(c, x, y, w, h, heading, rows, color=TEAL):
    c.rect(x, y, w, h, fill=WHITE, stroke=color, width=5)
    c.rect(x, y, 12, h, fill=color)
    text(c, x + 36, y + 84, heading, 52)
    for i, row in enumerate(rows):
        text(c, x + 36, y + 174 + 76 * i, row, 43, INK)


def arrow(c, x1, y1, x2, y2, color=ORANGE):
    c.line(x1, y1, x2, y2, color=color, width=8)
    dx = 1 if x2 >= x1 else -1
    c.poly([(x2, y2), (x2 - dx * 24, y2 - 16),
            (x2 - dx * 24, y2 + 16)], fill=color)


def two_objects():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 470, 10, 660, 205, 'Class: Artwork', ['the shared recipe'], VIOLET)
    arrow(c, 700, 225, 360, 305)
    arrow(c, 900, 225, 1240, 305)
    box(c, 50, 310, 700, 360, 'Object: amber', ['title: "Amber"', 'views: 2'], TEAL)
    box(c, 850, 310, 700, 360, 'Object: blue', ['title: "Blue"', 'views: 7'], ORANGE)
    return c.finish('week10-two-objects')


def separate_state():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 50, 175, 680, 390, 'amber.view()', ['views: 2  ->  3', 'only amber changes'], TEAL)
    box(c, 870, 175, 680, 390, 'blue', ['views: 7', 'still 7'], ORANGE)
    return c.finish('week10-separate-state')


def relation():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 40, 190, 650, 340, 'Exhibition', ['id: "e1"', 'name: "Night"'], VIOLET)
    box(c, 950, 35, 600, 290, 'Artwork', ['id: "a1"', 'exhibition_id: "e1"'], TEAL)
    box(c, 950, 375, 600, 290, 'Artwork', ['id: "a2"', 'exhibition_id: "e1"'], ORANGE)
    arrow(c, 700, 250, 930, 210)
    arrow(c, 700, 440, 930, 500)
    return c.finish('week10-one-to-many')


def lifetimes():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 40, 180, 680, 340, 'Running Python', ['amber.views = 3', 'close -> object gone'], TEAL)
    box(c, 880, 180, 680, 340, 'artworks.json', ['saved record: 3', 'reopen -> read again'], VIOLET)
    arrow(c, 745, 265, 855, 265)
    arrow(c, 855, 425, 745, 425, TEAL)
    text(c, 800, 156, 'save', 42, ORANGE, 'middle')
    text(c, 800, 560, 'load', 42, TEAL, 'middle')
    return c.finish('week10-lifetimes')


def grounded_answer():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 30, 175, 430, 340, 'Question', ['Open today?'], TEAL)
    box(c, 585, 175, 430, 340, 'Search', ['find a passage', 'keep source'], VIOLET)
    box(c, 1140, 175, 430, 340, 'Response', ['check evidence', 'or say unknown'], ORANGE)
    arrow(c, 475, 360, 570, 360)
    arrow(c, 1030, 360, 1125, 360)
    return c.finish('week10-grounded-answer')


def permission_boundary():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 30, 190, 430, 320, 'Agent', ['proposes call'], TEAL)
    box(c, 585, 190, 430, 320, 'MCP server', ['offers a tool'], VIOLET)
    box(c, 1140, 190, 430, 320, 'Local data', ['read-only demo'], ORANGE)
    arrow(c, 475, 365, 570, 365)
    arrow(c, 1030, 365, 1125, 365)
    text(c, 800, 600, 'Permission belongs at the boundary', 48, INK, 'middle')
    return c.finish('week10-permission-boundary')
