"""Original Week 9 message diagrams; SVG and PNG share the same geometry."""
from deckgen.figures import Canvas, INK, MUTED, ORANGE, TEAL, VIOLET

PAPER = '#FAF8F4'
WHITE = '#FFFFFF'


def label(c, x, y, text, color=INK, size=44, anchor='start'):
    c.text(x, y, text, size=size, color=color, mono=False, anchor=anchor)


def box(c, x, tag, title, detail, accent=TEAL, w=590):
    c.rect(x, 152, w, 390, fill=PAPER)
    c.rect(x, 152, 12, 390, fill=accent)
    label(c, x + 38, 222, tag, MUTED, 40)
    label(c, x + 38, 332, title, INK, 64)
    label(c, x + 38, 420, detail, INK, 43)


def arrow(c, x1, x2, y, text, color=ORANGE):
    sign = 1 if x2 > x1 else -1
    c.line(x1, y, x2, y, color, 8)
    c.poly([(x2, y), (x2 - sign * 24, y - 16), (x2 - sign * 24, y + 16)], fill=color)
    label(c, (x1 + x2) / 2, y - 42, text, INK, 43, 'middle')


def address(name='week09-address'):
    c = Canvas(1680, 640, bg=WHITE)
    box(c, 20, 'SAME LAPTOP', 'Client', 'A browser or script')
    box(c, 1070, 'SAME LAPTOP', 'Server', 'One listening process', VIOLET)
    arrow(c, 650, 1030, 320, '127.0.0.1 : 8000')
    label(c, 840, 590, 'Host finds the machine. Port finds the service.', INK, 44, 'middle')
    return c.finish(name)


def request(name='week09-request'):
    c = Canvas(1680, 640, bg=WHITE)
    box(c, 20, 'CLIENT', 'Browser', 'Choose September')
    box(c, 1070, 'SERVER', 'Tide API', 'Read local records', VIOLET)
    arrow(c, 650, 1030, 320, 'GET /tides?month=9')
    label(c, 840, 590, 'A fresh HTTP request asks for one resource.', INK, 42, 'middle')
    return c.finish(name)


def response(name='week09-response'):
    c = Canvas(1680, 640, bg=WHITE)
    box(c, 20, 'CLIENT', 'Browser', 'Draw the records')
    box(c, 1070, 'SERVER', 'Tide API', 'Return JSON', VIOLET)
    arrow(c, 1030, 650, 320, '200 OK + JSON', TEAL)
    label(c, 840, 590, 'The response belongs to that request.', INK, 44, 'middle')
    return c.finish(name)


def echo(name='week09-echo'):
    c = Canvas(1680, 640, bg=WHITE)
    box(c, 20, 'CLIENT', 'Local client', 'Keep connection')
    box(c, 1070, 'SERVER', 'Echo server', 'Keep connection', VIOLET)
    arrow(c, 650, 1030, 302, 'send: hello')
    arrow(c, 1030, 650, 474, 'reply: hello', TEAL)
    label(c, 840, 604, 'Repeat until either side disconnects.', INK, 42, 'middle')
    return c.finish(name)


def tool_boundary(name='week09-tool-boundary'):
    c = Canvas(1680, 640, bg=WHITE)
    for x, tag, title, detail, color in [
        (0, '01', 'Agent', 'Suggests action', TEAL),
        (565, '02', 'MCP server', 'Offers a tool', ORANGE),
        (1130, '03', 'Tool', 'Reads local data', VIOLET),
    ]:
        c.rect(x, 160, 520, 335, fill=PAPER)
        c.rect(x, 160, 12, 335, fill=color)
        label(c, x + 32, 224, tag, MUTED, 40)
        label(c, x + 32, 323, title, INK, 54)
        label(c, x + 32, 415, detail, INK, 40)
    arrow(c, 525, 555, 332, '', ORANGE)
    arrow(c, 1090, 1120, 332, '', ORANGE)
    label(c, 840, 583, 'Human permission bounds the action.', INK, 46, 'middle')
    return c.finish(name)
