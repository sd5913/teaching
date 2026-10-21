"""Original Week 12 diagrams: a proposal is not an authorized action."""

from deckgen.figures import Canvas, INK, ORANGE

PAPER = '#FAF8F4'
WHITE = '#FFFFFF'
RED = '#BD4435'
DARK_TEAL = '#145A61'


def text(c, x, y, value, size=48, color=INK, anchor='start'):
    c.text(x, y, value, size=size, color=color, anchor=anchor)


def box(c, x, y, w, h, title, subtitle, color=INK):
    c.rect(x, y, w, h, fill=color)
    text(c, x + w / 2, y + 135, title, 56, WHITE, 'middle')
    text(c, x + w / 2, y + 210, subtitle, 40, WHITE, 'middle')


def arrow(c, x1, y, x2, label, color=ORANGE):
    c.line(x1, y, x2, y, color=color, width=8)
    direction = 1 if x2 > x1 else -1
    c.poly([(x2, y), (x2 - direction * 25, y - 16),
            (x2 - direction * 25, y + 16)], fill=color)
    text(c, (x1 + x2) / 2, y - 35, label, 42, color, 'middle')


def roles():
    c = Canvas(1680, 640, bg=WHITE)
    text(c, 840, 68, 'Three roles. One proposed call.', 52, anchor='middle')
    box(c, 50, 170, 395, 330, 'Agent host', 'model + client')
    box(c, 640, 170, 395, 330, 'MCP server', 'tool registry', DARK_TEAL)
    box(c, 1230, 170, 395, 330, 'add(a, b)', 'runs a + b', INK)
    arrow(c, 455, 330, 630, 'MCP')
    arrow(c, 1045, 330, 1220, 'call')
    text(c, 840, 565, 'The model suggests; the host decides whether to call.', 41,
         anchor='middle')
    return c.finish('week12-three-roles')


def outbound():
    c = Canvas(1680, 640, bg=WHITE)
    text(c, 840, 68, 'Request: "add 3 and 4"', 53, anchor='middle')
    box(c, 50, 170, 395, 330, 'Agent host', 'proposes add')
    box(c, 640, 170, 395, 330, 'MCP server', 'checks args', DARK_TEAL)
    box(c, 1230, 170, 395, 330, 'add(a, b)', 'returns 7')
    arrow(c, 455, 330, 630, 'call')
    arrow(c, 1045, 330, 1220, 'run')
    text(c, 840, 580, 'A call is an action, not just words in a reply.', 42,
         anchor='middle')
    return c.finish('week12-outbound')


def inbound():
    c = Canvas(1680, 640, bg=WHITE)
    text(c, 840, 68, 'The result travels back', 53, anchor='middle')
    box(c, 50, 170, 395, 330, 'Agent host', 'reports 7')
    box(c, 640, 170, 395, 330, 'MCP server', 'passes result', DARK_TEAL)
    box(c, 1230, 170, 395, 330, 'add(a, b)', 'result: 7')
    arrow(c, 1220, 330, 1045, 'result', DARK_TEAL)
    arrow(c, 630, 330, 455, 'result', DARK_TEAL)
    text(c, 840, 580, 'Check the actual result before claiming success.', 42,
         anchor='middle')
    return c.finish('week12-inbound')


def permission(allowed):
    c = Canvas(1680, 640, bg=WHITE)
    text(c, 840, 60, 'A proposed action meets a trust boundary', 50,
         anchor='middle')
    box(c, 40, 170, 470, 330, 'Proposal',
        'add(3, 4)' if allowed else 'overwrite file')
    gate_color = DARK_TEAL if allowed else RED
    box(c, 605, 170, 470, 330, 'Host policy',
        'allow: add only' if allowed else 'not allowed', gate_color)
    arrow(c, 515, 330, 598, 'ask')
    c.line(1115, 145, 1115, 525, color=gate_color, width=9)
    text(c, 1145, 135, 'TRUST BOUNDARY', 41, gate_color)
    if allowed:
        box(c, 1175, 170, 460, 330, 'MCP server', 'runs add(3, 4)', DARK_TEAL)
        arrow(c, 1080, 330, 1168, 'go', DARK_TEAL)
        text(c, 840, 585, 'Allowed call -> result 7 -> inspect -> answer.', 40,
             anchor='middle')
    else:
        c.rect(1175, 170, 460, 330, fill=PAPER)
        text(c, 1405, 295, 'NO CALL', 60, RED, 'middle')
        text(c, 1405, 380, 'stop / ask a person', 41, RED, 'middle')
        text(c, 840, 585, 'A valid schema is not permission to act.', 42,
             anchor='middle')
    return c.finish('week12-allowed' if allowed else 'week12-blocked')
