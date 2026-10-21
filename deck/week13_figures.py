"""Large, successive Week 13 diagrams for projection."""

from deckgen.figures import Canvas

INK = '#000B1C'
TEAL = '#246E70'
ORANGE = '#E87835'
PAPER = '#FAF8F4'
MUTED = '#5C6470'


def box(c, x, y, title, detail, color=TEAL, w=430):
    c.rect(x, y, w, 330, fill='#FFFFFF', stroke=color, width=5)
    c.rect(x, y, w, 14, fill=color)
    c.text(x + 28, y + 115, title, 58, INK, weight=700)
    c.text(x + 28, y + 205, detail, 42, MUTED)


def arrow(c, start, end, y):
    c.line(start, y, end, y, color=ORANGE, width=8)
    c.poly([(end, y), (end - 30, y - 18), (end - 30, y + 18)], fill=ORANGE)


def interaction():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 0, 150, 'Input', 'choose a value')
    box(c, 585, 150, 'State', 'remember it')
    box(c, 1170, 150, 'Output', 'show a result')
    arrow(c, 450, 565, 340)
    arrow(c, 1035, 1150, 340)
    c.text(800, 660, 'Which line changes the next result?', 50, TEAL, anchor='middle')
    return c.finish('week13-interaction')


def loop_step():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 0, 150, 'Test', 'step < limit')
    box(c, 585, 150, 'Change', 'step += 1')
    box(c, 1170, 150, 'Stop', 'test is false')
    arrow(c, 450, 565, 340)
    c.text(505, 295, 'true', 40, TEAL, anchor='middle')
    c.line(215, 150, 215, 90, color=ORANGE, width=7)
    c.line(215, 90, 1385, 90, color=ORANGE, width=7)
    c.line(1385, 90, 1385, 140, color=ORANGE, width=7)
    c.poly([(1385, 150), (1367, 120), (1403, 120)], fill=ORANGE)
    c.rect(720, 62, 160, 54, fill=PAPER)
    c.text(800, 100, 'false', 40, TEAL, anchor='middle')
    c.line(800, 480, 800, 565, color=TEAL, width=7)
    c.line(800, 565, 215, 565, color=TEAL, width=7)
    c.line(215, 565, 215, 495, color=TEAL, width=7)
    c.poly([(215, 480), (197, 510), (233, 510)], fill=TEAL)
    c.rect(430, 538, 200, 55, fill=PAPER)
    c.text(530, 575, 'repeat', 40, TEAL, anchor='middle')
    c.text(800, 675, 'Without the change, what makes the loop stop?', 48, TEAL, anchor='middle')
    return c.finish('week13-loop')


def reproduction():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 0, 150, 'Repo', 'code + data')
    box(c, 585, 150, 'Run', 'clear steps')
    box(c, 1170, 150, 'Check', 'expected result')
    arrow(c, 450, 565, 340)
    arrow(c, 1035, 1150, 340)
    c.text(800, 660, 'Can another computer reach the same result?', 48, TEAL, anchor='middle')
    return c.finish('week13-reproduction')


def tool_boundary():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 0, 150, 'Agent', 'suggests action')
    box(c, 585, 150, 'MCP', 'exposes tool')
    box(c, 1170, 150, 'Tool', 'acts on files')
    arrow(c, 450, 565, 340)
    arrow(c, 1035, 1150, 340)
    c.text(800, 660, 'Permission belongs at the action boundary.', 48, TEAL, anchor='middle')
    return c.finish('week13-tool-boundary')
