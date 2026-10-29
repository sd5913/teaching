"""Week 12: actual state, numbered actions and evidence at room-readable size."""
import base64
from pathlib import Path
from deckgen.figures import Canvas, INK, ORANGE

WHITE = '#FFFFFF'
TEAL = '#145A61'
PAPER = '#FAF8F4'
RED = '#BD4435'


def label(c, x, y, value, size=44, color=INK, anchor='start'):
    c.text(x, y, value, size=size, color=color, anchor=anchor)


def box(c, x, y, w, title, detail, color=INK, h=220):
    from deckgen.core import pil_font
    for value, size in [(title, 48), (detail, 40)]:
        if pil_font('monomed', size).getlength(value) > w - 32:
            raise ValueError(f'diagram label exceeds its box: {value}')
    c.rect(x, y, w, h, fill=color)
    label(c, x + w / 2, y + 88, title, 48, WHITE, 'middle')
    label(c, x + w / 2, y + 156, detail, 40, WHITE, 'middle')


def arrow(c, x1, y1, x2, y2, color=ORANGE):
    c.line(x1, y1, x2, y2, color=color, width=7)
    if x1 == x2:
        sign = 1 if y2 > y1 else -1
        c.poly([(x2,y2),(x2-15,y2-sign*24),(x2+15,y2-sign*24)], fill=color)
    else:
        sign = 1 if x2 > x1 else -1
        c.poly([(x2,y2),(x2-sign*24,y2-15),(x2-sign*24,y2+15)], fill=color)


def feedback():
    c = Canvas(1680, 640, bg=WHITE)
    box(c, 25, 80, 460, '1 Observe', '2 lights; t180')
    box(c, 610, 80, 460, '2 Choose', 'speed 125 to 275', TEAL)
    box(c, 1195, 80, 460, '3 Act + check', '3 lights; t166')
    arrow(c, 490, 190, 600, 190)
    arrow(c, 1080, 190, 1185, 190)
    c.line(1425, 305, 1425, 420, color=TEAL, width=7)
    arrow(c, 1425, 420, 255, 420, TEAL)
    arrow(c, 255, 420, 255, 310, TEAL)
    label(c, 840, 485, '4 Pass: stop edits. Fail: observe again within budget.', 42, anchor='middle')
    label(c, 840, 580, 'The model chooses here; the tool does not choose a repair.', 42, anchor='middle')
    return c.finish('week12-feedback')


def process():
    c = Canvas(1680, 640, bg=WHITE)
    box(c, 25, 110, 460, '1 Python set', 'world.json: 275')
    box(c, 610, 110, 460, '2 New engine', '_ready: JSON', TEAL)
    box(c, 1195, 110, 460, '3 Observation', 'WORLD_CHECK')
    arrow(c, 490, 220, 600, 220)
    arrow(c, 1080, 220, 1185, 220)
    label(c, 840, 455, 'Stored config persists. Player / lights / ticks restart.', 44, anchor='middle')
    label(c, 840, 555, 'An already running game keeps its loaded config.', 44, anchor='middle')
    return c.finish('week12-process')


def state():
    c = Canvas(1680, 640, bg=WHITE)
    for x, title, detail, color in [(25,'0, 1, 2 lights','exit locked',INK),
                                  (610,'3 lights','exit open',TEAL),
                                  (1195,'At exit + 3','won = true',INK)]:
        box(c,x,100,460,title,detail,color)
    arrow(c,490,210,600,210)
    arrow(c,1080,210,1185,210)
    label(c, 840, 430, '1 Collect in order     2 Unlock     3 Reach the exit', 44, anchor='middle')
    label(c, 840, 545, 'After winning: no further movement or tick increments.', 42, anchor='middle')
    return c.finish('week12-state')


def episode():
    c = Canvas(1680,640,bg=WHITE)
    c.rect(30,50,780,450,fill=INK);c.rect(870,50,780,450,fill=TEAL)
    for x, heading, lines in [(65,'1 Baseline', ['speed 125', '2 lights / x455', '180 ticks / no win']),
                              (905,'2 Model revision', ['speed 275', '3 lights / x840.83', '166 ticks / win'])]:
        label(c,x,125,heading,52,WHITE)
        for i,line in enumerate(lines):label(c,x,235+i*85,line,46,WHITE)
    label(c,840,595,'Unchanged goal and checker. Model stops further edits.',44,anchor='middle')
    return c.finish('week12-episode')


def budgets():
    c=Canvas(1680,640,bg=WHITE)
    for x,title,detail in [(25,'8 actions','read/set/check'),(610,'4 writes','reserve first'),(1195,'180 seconds','time since start')]:
        box(c,x,100,460,title,detail,TEAL if x==610 else INK)
    label(c,840,450,'Pass / budget / missing observation / tool error: STOP.',44,anchor='middle')
    label(c,840,555,'A failed tool still spends an action. No silent reset.',44,anchor='middle')
    return c.finish('week12-budgets')


def timing():
    c=Canvas(1680,640,bg=WHITE)
    label(c,40,75,'Same simulated time, two clocks',52)
    for i in range(5):
        x=120+i*350
        c.line(x,150,x,195,color=INK,width=5)
        label(c,x,250,str(i)+' s',44,anchor='middle')
    c.line(120,175,1520,175,color=INK,width=6)
    label(c,40,375,'Physics: 60 ticks/s. Goal: win within 180 ticks.',46)
    label(c,40,475,'Film: 30 frames/s x 4 s = 120 rendered frames.',46)
    label(c,40,575,'At 275: win at tick 166; then hold the ending.',44,TEAL)
    return c.finish('week12-timing')


def evidence():
    c=Canvas(1680,640,bg=WHITE)
    for x,title,detail in [(25,'1 Behavior','lights/time/stop'),(610,'2 File','decode / frames'),(1195,'3 Visible','motion / COMPLETE')]:
        box(c,x,100,460,title,detail,TEAL if x==610 else INK)
    arrow(c,490,210,600,210);arrow(c,1080,210,1185,210)
    label(c,840,450,'A passing checker can accompany a black or stale movie.',44,anchor='middle')
    label(c,840,555,'Keep config + observations + clip together.',46,TEAL,anchor='middle')
    return c.finish('week12-evidence')


def editor():
    from io import BytesIO
    from PIL import Image
    c = Canvas(1680, 640, bg=WHITE)
    assets = Path(__file__).parent / 'week12-assets'

    def crop(filename, bounds, x, y, w, h):
        picture = Image.open(assets / filename).convert('RGBA')
        if bounds:
            picture = picture.crop(bounds)
        stream = BytesIO()
        picture.save(stream, format='PNG')
        data = base64.b64encode(stream.getvalue()).decode('ascii')
        c.svg.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="data:image/png;base64,{data}"/>')
        c.im.paste(picture.resize((w * c.scale, h * c.scale)), (x * c.scale, y * c.scale))

    for x, title, detail in [(40, '1 Open scene', 'world.tscn'),
                              (620, '2 Select 2D', 'Editor workspace'),
                              (1200, '3 Run F6', 'Visible world')]:
        label(c, x, 90, title, 48)
        label(c, x, 165, detail, 40, TEAL)
    crop('editor-orientation.png', (30, 694, 225, 724), 40, 290, 468, 72)
    crop('editor-orientation.png', (510, 0, 575, 42), 670, 250, 325, 210)
    crop('frame-start.png', None, 1170, 240, 480, 270)
    label(c, 840, 600, 'The runtime draws the world; the editor canvas may be empty.', 40, anchor='middle')
    return c.finish('week12-editor-actions')


def screenshot(filename):
    path=Path(__file__).parent/'week12-assets'/filename
    data=base64.b64encode(path.read_bytes()).decode('ascii')
    # Real bitmap embedded unchanged, so native/PDF/HTML share the same evidence.
    from PIL import Image
    w,h=Image.open(path).size
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><image width="{w}" height="{h}" href="data:image/png;base64,{data}"/></svg>',str(path))
