"""Week 4 diagrams, drawn as SVG for the web and PNG for PowerPoint."""
from deckgen.figures import Canvas, INK, ORANGE, MUTED, TEAL, VIOLET

PAPER = '#FAF8F4'


def label(c, x, y, text, size=26, color=INK):
    c.text(x, y, text, size=size, color=color, mono=False)


def box(c, x, y, w, h, tag, title, lines, accent=TEAL):
    c.rect(x, y, w, h, fill=PAPER)
    c.rect(x, y, 7, h, fill=accent)
    label(c, x + 28, y + 42, tag, 20, MUTED)
    label(c, x + 28, y + 90, title, 34)
    for i, line in enumerate(lines):
        label(c, x + 28, y + 139 + i * 35, line)


def arrow(c, x1, y, x2, text, color=ORANGE):
    direction = 1 if x2 > x1 else -1
    c.line(x1, y, x2, y, color=color, width=4)
    c.poly([(x2, y), (x2 - direction * 13, y - 8),
            (x2 - direction * 13, y + 8)], fill=color)
    c.text((x1 + x2) / 2, y - 18, text, size=24, color=INK,
           mono=False, anchor='middle')


def frontend_backend():
    c = Canvas(1600, 550)
    box(c, 0, 110, 465, 315, 'FRONTEND · IN THE BROWSER', 'Choose and draw',
        ['The person chooses a month.', 'JavaScript asks for records.', 'The chart uses the reply.'])
    box(c, 1110, 110, 490, 315, 'BACKEND · ON THE SERVER', 'Read and return',
        ['FastAPI checks the request.', 'Python selects the records.', 'The saved JSON supplies data.'], VIOLET)
    arrow(c, 490, 215, 1080, 'GET /tides?month=9')
    arrow(c, 1080, 345, 490, '200 OK + JSON records', TEAL)
    label(c, 0, 510, 'GitHub Pages delivers the frontend files.', 25, MUTED)
    label(c, 935, 510, 'Cloudflare runs this Python backend.', 25, MUTED)
    return c.finish('week04-frontend-backend')


def streamlit_path():
    c = Canvas(1600, 550)
    box(c, 0, 130, 420, 260, 'BROWSER', 'Choose day 17',
        ['A widget sends a value.', 'The page shows the chart.'])
    box(c, 785, 80, 815, 380, 'PYTHON PROCESS · YOUR LAPTOP OR A SERVER',
        'Streamlit reruns app.py', ['Read the local JSON file.',
        'Select the day’s 24 heights.', 'Build the updated chart.'], VIOLET)
    arrow(c, 445, 210, 755, 'widget value')
    arrow(c, 755, 350, 445, 'page update', TEAL)
    label(c, 0, 525, 'There is still a browser and a server. You write one Python app; no separate /tides API.', 27, MUTED)
    return c.finish('week04-streamlit-path')


def event_cycle():
    c = Canvas(1600, 550)
    for x, tag, title, lines, color in [
        (0, '01 · EVENT', 'A person clicks', ['The browser queues', 'the event.'], TEAL),
        (580, '02 · CALLBACK', 'Your function runs', ['Read the selected day.', 'Update the chart data.'], ORANGE),
        (1160, '03 · RENDER', 'The page updates', ['The browser gets', 'a chance to draw.'], VIOLET),
    ]:
        box(c, x, 80, 440, 280, tag, title, lines, color)
    arrow(c, 465, 225, 550, '')
    arrow(c, 1045, 225, 1130, '')
    c.line(1380, 390, 1380, 455, color=TEAL)
    c.line(1380, 455, 220, 455, color=TEAL)
    c.line(220, 455, 220, 390, color=TEAL)
    c.poly([(220, 378), (212, 392), (228, 392)], fill=TEAL)
    c.rect(515, 428, 570, 58, fill='#FFFFFF')
    label(c, 555, 465, 'Ready for the next event', 30)
    return c.finish('week04-event-cycle')


def image_service():
    c = Canvas(1600, 500)
    box(c, 0, 70, 460, 280, 'CLIENT · OUR PYTHON SCRIPT', 'Describe an image',
        ['Send a prompt + model.', 'Keep the key on the server.'])
    box(c, 1110, 70, 490, 280, 'SERVICE · EASEL', 'Generate an image',
        ['Qwen Image 2.1', 'ComfyUI runs the workflow.'], VIOLET)
    arrow(c, 490, 170, 1080, 'POST /v1/images/generations')
    arrow(c, 1080, 295, 490, 'JSON containing image data', TEAL)
    label(c, 0, 440, 'Decode the reply → save a PNG → place it in these slides.', 34)
    return c.finish('week04-image-service')
