"""Original Week 8 classroom diagrams; each image is a single, large teaching step."""
from deckgen.figures import Canvas, INK, MUTED, ORANGE, TEAL, VIOLET

PAPER = '#FAF8F4'


def text(c, x, y, value, size=46, color=INK, anchor='start'):
    c.text(x, y, value, size=size, color=color, anchor=anchor)


def box(c, x, y, title, detail='', color=TEAL, w=430, h=270):
    c.rect(x, y, w, h, fill=PAPER)
    c.rect(x, y, 10, h, fill=color)
    text(c, x + 38, y + 110, title, 54)
    if detail:
        text(c, x + 38, y + 184, detail, 40, MUTED)


def arrow(c, a, b, caption='', color=ORANGE):
    x1, y1 = a
    x2, y2 = b
    c.line(x1, y1, x2, y2, color=color, width=8)
    if x2 > x1:
        c.poly([(x2, y2), (x2 - 25, y2 - 16), (x2 - 25, y2 + 16)], fill=color)
    if caption:
        text(c, (x1 + x2) / 2, 94, caption, 42, color, anchor='middle')


def scope():
    c = Canvas(1600, 720)
    box(c, 20, 180, 'PERSON', 'What do they do?')
    box(c, 585, 180, 'ACTION', 'One input', ORANGE)
    box(c, 1150, 180, 'RESPONSE', 'What changes?', VIOLET)
    arrow(c, (465, 310), (555, 310))
    arrow(c, (1030, 310), (1120, 310))
    text(c, 800, 610, 'Test the smallest complete loop', 52, anchor='middle')
    return c.finish('week08-scope')


def increment(step):
    """Hold geometry steady while revealing backlog -> chosen task -> usable result."""
    c = Canvas(1600, 720)
    box(c, 20, 165, 'GOAL', 'Useful response', TEAL)
    box(c, 585, 165, 'BACKLOG', 'Ordered tasks', ORANGE)
    box(c, 1150, 165, 'INCREMENT', 'Works now', VIOLET)
    if step >= 2:
        arrow(c, (465, 295), (555, 295), 'break down')
    if step >= 3:
        arrow(c, (1030, 295), (1120, 295), 'choose + test')
    captions = {
        1: 'First: name the experience and its user.',
        2: 'Next: order tasks by value and uncertainty.',
        3: 'Then: build and verify one usable slice.',
    }
    text(c, 800, 600, captions[step], 43, anchor='middle')
    return c.finish(f'week08-increment-{step}')


def git_path(step):
    """Three successive views of the same branch, review and integration path."""
    c = Canvas(1600, 720)
    box(c, 20, 170, 'MAIN', 'Working baseline', TEAL)
    box(c, 585, 170, 'BRANCH', 'One small change', ORANGE)
    box(c, 1150, 170, 'REVIEW', 'Evidence + check', VIOLET)
    if step >= 1:
        arrow(c, (465, 300), (555, 300), 'start')
    if step >= 2:
        arrow(c, (1030, 300), (1120, 300), 'open PR')
    if step >= 3:
        c.line(1370, 465, 1370, 575, color=TEAL, width=8)
        c.line(1370, 575, 240, 575, color=TEAL, width=8)
        c.line(240, 575, 240, 465, color=TEAL, width=8)
        c.poly([(240, 450), (224, 476), (256, 476)], fill=TEAL)
        c.rect(570, 532, 460, 76, fill='#FFFFFF')
        text(c, 800, 585, 'merge after review', 40, TEAL, anchor='middle')
    return c.finish(f'week08-git-{step}')


def runtime(step):
    c = Canvas(1600, 720)
    box(c, 20, 170, 'IMAGE', 'Packaged recipe', TEAL)
    box(c, 585, 170, 'CONTAINER', 'Running process', ORANGE)
    box(c, 1150, 170, 'LOCAL FILE', 'Lost on removal', VIOLET)
    arrow(c, (465, 300), (555, 300), 'run')
    if step >= 2:
        arrow(c, (1030, 300), (1120, 300), 'writes')
    text(c, 800, 600, 'A stopped container is not the same as a removed container.',
         41, anchor='middle')
    return c.finish(f'week08-runtime-{step}')


def persistence():
    c = Canvas(1600, 720)
    box(c, 20, 155, 'HOST', 'Your project folder', TEAL)
    box(c, 585, 155, 'CONTAINER', 'App reads /work', ORANGE)
    box(c, 1150, 155, 'DATA', 'Write /work/out', VIOLET)
    arrow(c, (465, 285), (555, 285), 'bind mount')
    arrow(c, (1030, 285), (1120, 285), 'write')
    text(c, 800, 570, 'Named volume: another persistent store managed by Docker.',
         42, anchor='middle')
    text(c, 800, 635, 'No mount: removal loses container-only writes.',
         42, anchor='middle')
    return c.finish('week08-persistence')


def agent_tool(step):
    c = Canvas(1600, 720)
    box(c, 20, 170, 'PERSON', 'Grants scope', TEAL)
    box(c, 585, 170, 'AGENT', 'Proposes a call', ORANGE)
    box(c, 1150, 170, 'MCP SERVER', 'Offers tools', VIOLET)
    arrow(c, (465, 305), (555, 305), 'request')
    if step >= 2:
        arrow(c, (1030, 305), (1120, 305), 'allowed call')
    text(c, 800, 610, 'The tool executes only within granted permissions.', 45, anchor='middle')
    return c.finish(f'week08-agent-{step}')
