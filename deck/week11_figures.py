"""Original Week 11 diagrams: synthetic values only; no live tool connection."""
from deckgen.figures import Canvas, INK, ORANGE, TEAL, MUTED

PAPER = '#FAF8F4'
VIOLET = '#67518B'


def label(c, x, y, text, size=46, color=INK, anchor='start'):
    c.text(x, y, text, size=size, color=color, anchor=anchor, weight=700)


def box(c, x, y, w, title, detail, accent=TEAL):
    c.rect(x, y, w, 290, fill=PAPER, stroke=accent, width=4)
    c.rect(x, y, 12, 290, fill=accent)
    label(c, x + 35, y + 82, title, 52)
    label(c, x + 35, y + 163, detail, 41)


def arrow(c, x1, x2, y, text, color=ORANGE):
    c.line(x1, y, x2, y, color=color, width=7)
    c.poly([(x2, y), (x2 - 25, y - 15), (x2 - 25, y + 15)], fill=color)
    label(c, (x1+x2)/2, 125, text, 41, color, 'middle')


def object_step(step):
    c = Canvas(1680, 690)
    box(c, 60, 205, 690, 'Python object', ['name = "Cube"', 'scale = 1.0', 'set_scale(2.0)'][step], TEAL)
    if step:
        box(c, 930, 205, 690, 'Creative result', 'Larger cube' if step == 2 else 'Visible cube', VIOLET)
        arrow(c, 775, 905, 350, 'method' if step == 2 else 'attribute')
    label(c, 840, 615, ['A name identifies one thing', 'An attribute holds a value', 'A method asks for a change'][step], 46, INK, 'middle')
    return c.finish(f'week11-object-{step}')


def path(step):
    c = Canvas(1680, 690)
    box(c, 30, 185, 470, 'Sender', 'Python', TEAL)
    if step:
        box(c, 610, 185, 470, 'Boundary', 'OSC message', ORANGE)
        arrow(c, 525, 580, 340, '/control 0.50')
    if step > 1:
        box(c, 1190, 185, 470, 'Receiver', 'Visual tool', VIOLET)
        arrow(c, 1095, 1160, 340, 'parsed value')
    label(c, 840, 610, ['First: decide what to control', 'Next: name the message', 'Finally: map it to a result'][step], 44, INK, 'middle')
    return c.finish(f'week11-path-{step}')


def mapping():
    c = Canvas(1680, 690)
    box(c, 35, 170, 690, 'Control', '0.00 to 1.00', TEAL)
    box(c, 955, 170, 690, 'Opacity', '0% to 100%', VIOLET)
    arrow(c, 750, 925, 315, 'x 100')
    label(c, 840, 575, '0.50 becomes 50% opacity', 48, INK, 'middle')
    return c.finish('week11-mapping')


def silence():
    c = Canvas(1680, 690)
    for x, number, action, color in [(40, '0.50', 'new value', TEAL), (610, '...', 'no updates', ORANGE), (1180, '0.00', 'reset to safe', VIOLET)]:
        box(c, x, 185, 460, number, action, color)
    arrow(c, 525, 580, 340, 'stop')
    arrow(c, 1095, 1150, 340, 'timeout')
    label(c, 840, 615, 'Silence is not the number zero', 47, INK, 'middle')
    return c.finish('week11-silence')


def mcp(step):
    c = Canvas(1680, 690)
    box(c, 25, 180, 460, 'Person', 'approves action', TEAL)
    box(c, 620, 180, 460, 'Agent', 'proposes call', ORANGE)
    arrow(c, 510, 590, 335, 'scope')
    if step:
        box(c, 1195, 180, 460, 'MCP server', 'exposes tool', VIOLET)
        arrow(c, 1105, 1165, 335, 'tool call')
    label(c, 840, 608, 'A suggestion is not permission' if not step else 'Read only first; no automatic write', 45, INK, 'middle')
    return c.finish(f'week11-mcp-{step}')
