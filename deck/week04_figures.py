"""Diagrams fill a 1600 × 720 surface; short labels stay large on a projector."""
from deckgen.figures import Canvas, INK, ORANGE, MUTED, TEAL, VIOLET

PAPER = '#FAF8F4'


def label(c, x, y, text, size=42, color=INK, anchor='start'):
    c.text(x, y, text, size=size, color=color, mono=False, anchor=anchor)


def node(c, x, y, tag, title, lines, accent=TEAL, w=620, h=510):
    c.rect(x, y, w, h, fill=PAPER)
    c.rect(x, y, 10, h, fill=accent)
    label(c, x + 36, y + 65, tag, 32, MUTED)
    label(c, x + 36, y + 155, title, 58)
    for i, line in enumerate(lines):
        label(c, x + 36, y + 255 + i * 70, line)


def arrow(c, x1, y, x2, text='', color=ORANGE):
    direction = 1 if x2 > x1 else -1
    c.line(x1, y, x2, y, color=color, width=7)
    c.poly([(x2, y), (x2 - direction * 22, y - 14),
            (x2 - direction * 22, y + 14)], fill=color)
    if text:
        label(c, (x1 + x2) / 2, y - 30, text, 40, anchor='middle')


def frontend_request():
    c = Canvas(1600, 720)
    label(c, 800, 75, '/tides?month=9', 52, anchor='middle')
    node(c, 0, 150, 'BROWSER', 'Frontend', ['Choose September', 'Ask for records'])
    node(c, 980, 150, 'SERVER', 'Backend', ['Validate month', 'Read saved data'], VIOLET)
    arrow(c, 650, 420, 950, 'GET')
    return c.finish('week04-frontend-request')


def backend_response():
    c = Canvas(1600, 720)
    label(c, 800, 75, '200 OK · 30 daily records', 52, anchor='middle')
    node(c, 0, 150, 'BROWSER', 'Frontend', ['Choose a day', 'Draw 24 heights'])
    node(c, 980, 150, 'SERVER', 'Backend', ['September records', 'Return JSON'], VIOLET)
    arrow(c, 950, 420, 650, 'JSON', TEAL)
    return c.finish('week04-backend-response')


def streamlit_path():
    c = Canvas(1600, 720)
    node(c, 0, 80, 'BROWSER', 'The page', ['Choose day 17', 'See its chart'])
    node(c, 980, 80, 'PYTHON PROCESS', 'Streamlit', ['Read local JSON', 'Select 24 heights'], VIOLET)
    arrow(c, 650, 315, 950, 'day = 17')
    arrow(c, 950, 485, 650, 'chart', TEAL)
    label(c, 800, 690, 'A changed widget reruns app.py', 46, anchor='middle')
    return c.finish('week04-streamlit-path')


def event_cycle():
    c = Canvas(1600, 720)
    for x, tag, title, lines, color in [
        (0, '01 · EVENT', 'Click', ['Choose day 17'], TEAL),
        (590, '02 · CALLBACK', 'Respond', ['Update the data'], ORANGE),
        (1180, '03 · RENDER', 'Draw', ['Show the chart'], VIOLET),
    ]:
        node(c, x, 80, tag, title, lines, color, w=420, h=430)
    arrow(c, 450, 300, 560)
    arrow(c, 1040, 300, 1150)
    c.line(1390, 545, 1390, 650, color=TEAL, width=7)
    c.line(1390, 650, 210, 650, color=TEAL, width=7)
    c.line(210, 650, 210, 545, color=TEAL, width=7)
    c.poly([(210, 525), (196, 549), (224, 549)], fill=TEAL)
    c.rect(430, 607, 740, 80, fill='#FFFFFF')
    label(c, 800, 665, 'Ready for the next event', 46, anchor='middle')
    return c.finish('week04-event-cycle')


def image_service():
    c = Canvas(1600, 720)
    node(c, 0, 80, 'CLIENT', 'Our script', ['Send a prompt', 'Save the image'])
    node(c, 980, 80, 'SERVER', 'Image API', ['Run the model', 'Return image data'], VIOLET)
    arrow(c, 650, 315, 950, 'POST')
    arrow(c, 950, 485, 650, 'image data', TEAL)
    label(c, 800, 690, 'Prompt → generation → image', 46, anchor='middle')
    return c.finish('week04-image-service')
