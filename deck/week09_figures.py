"""Actual Week 9 messages, rendered with the established course palette."""
from deckgen.figures import Canvas, INK, MUTED, ORANGE, TEAL

WHITE = '#FFFFFF'
PAPER = '#FAF8F4'


def text(c, x, y, value, size=44, color=INK, anchor='start'):
    c.text(x, y, value, size=size, color=color, mono=True, anchor=anchor)


def node(c, x, title, lines, width=420, y=130, height=330):
    c.rect(x, y, width, height, fill=PAPER, stroke=TEAL, width=2)
    text(c, x + 24, y + 65, title, 48)
    for i, line in enumerate(lines):
        text(c, x + 24, y + 155 + i * 65, line)


def arrow(c, x1, x2, y, label='', color=ORANGE):
    c.line(x1, y, x2, y, color, 7)
    sign = 1 if x2 > x1 else -1
    c.poly([(x2, y), (x2-sign*22, y-14), (x2-sign*22, y+14)], fill=color)
    if label:
        text(c, (x1+x2)/2, y-28, label, 40, anchor='middle')


def address():
    c = Canvas(1680, 640, bg=WHITE)
    values = [('http', '1 / protocol'), ('127.0.0.1', '2 / host'), ('8009', '3 / port'), ('/state', '4 / route')]
    for i, (value, label) in enumerate(values):
        x = i*425
        node(c, x, value, [label], width=405, y=155, height=280)
    text(c, 840, 560, 'One URL: http://127.0.0.1:8009/state', 46, anchor='middle')
    return c.finish('week09-url')


def layers():
    c = Canvas(1680, 640, bg=WHITE)
    rows = [('4 / Application', 'HTTP / WebSocket / JSON action'), ('3 / Transport', 'TCP stream / UDP datagrams'), ('2 / Address', 'IP: which machine?'), ('1 / Link', 'Wi-Fi / Ethernet / loopback')]
    for i, (name, detail) in enumerate(rows):
        y = 30+i*145
        c.rect(20, y, 1640, 120, fill=PAPER)
        text(c, 50, y+77, name, 46)
        text(c, 620, y+77, detail, 44)
    return c.finish('week09-layers')


def journey(stage=0):
    c = Canvas(1680, 640, bg=WHITE)
    changed = stage >= 1
    node(c, 0, 'Browser A', ['input: 25', 'x = 25' if stage >= 2 else 'x = 50'])
    node(c, 630, 'Python Scene', ['x = 25' if changed else 'x = 50', 'revision = 1' if changed else 'revision = 0'])
    node(c, 1260, 'Browser B', ['input: 50', 'x = 25' if stage >= 2 else 'x = 50'])
    if stage == 0:
        arrow(c, 430, 620, 320, '1 / send')
        text(c, 840, 560, '{"id":"a-1", "action":"set_x", "x":25}', 44, anchor='middle')
    elif stage == 1:
        text(c, 840, 560, 'Validate, then change the one authoritative Scene.', 44, anchor='middle')
    elif stage == 2:
        arrow(c, 1058, 1250, 320, '2 / state')
        arrow(c, 620, 430, 320, '2 / state', TEAL)
        text(c, 840, 560, '{"type":"state", "x":25, "revision":1}', 44, anchor='middle')
    else:
        arrow(c, 620, 430, 320, '3 / ack', TEAL)
        text(c, 840, 560, '{"type":"ack", "id":"a-1", "revision":1}', 44, anchor='middle')
    return c.finish(f'week09-journey-{stage}')


def framing():
    c = Canvas(1680, 640, bg=WHITE)
    node(c, 20, 'Application writes', ['red\\n', 'blue\\n'], width=570)
    node(c, 1090, 'Possible reads', ['red\\nblu', 'e\\n'], width=570)
    arrow(c, 610, 1070, 315, 'TCP bytes')
    text(c, 840, 565, 'Keep a buffer; extract a message at each newline.', 44, anchor='middle')
    return c.finish('week09-framing')


def uncertainty():
    c = Canvas(1680, 640, bg=WHITE)
    node(c, 0, 'A / no ack', ['result unknown', 'do not resend'])
    node(c, 630, 'Server', ['x = 73', 'action applied'])
    node(c, 1260, 'B / observed', ['x = 73', 'state received'])
    arrow(c, 1058, 1250, 320, 'state')
    text(c, 840, 560, 'Missing observation does not prove a missing action.', 44, anchor='middle')
    return c.finish('week09-uncertainty')
