"""Visual course recap, reusing the earlier lessons' data and drawing primitives."""
import math

from deckgen.figures import Canvas
from week10_figures import box, text, TEAL as AQUA, VIOLET
from week12_figures import arrow, INK, ORANGE, PAPER, TEAL, WHITE


def prose(c, x, y, value, size=44, color=INK, anchor='start', bold=False):
    c.text(x, y, value, size, color, mono=False, anchor=anchor,
           weight=700 if bold else 500)


def schedule():
    c = Canvas(1680, 640, bg=WHITE)
    prose(c, 0, 60, 'Thursday 3 December', 52, bold=True)
    c.line(150, 265, 1500, 265, TEAL, 6)
    for x in (150, 650, 1500):
        c.circle(x, 265, 15, fill=TEAL)
    arrow(c, 740, 265, 1410, 265)
    prose(c, 1075, 220, '3 days to finish', 48, TEAL, 'middle', True)
    for x, lines in ((20, ['10:30', 'Final quiz', 'TU103']),
                     (520, ['Then', 'Final project', 'review']),
                     (1350, ['6 December', '23:59 HKT', 'Repository due'])):
        for row, value in enumerate(lines):
            prose(c, x, 365 + row * 70, value, 44, bold=row == 0)
    prose(c, 840, 615, 'Bring your working candidate, evidence and main blocker.',
          44, anchor='middle')
    return c.finish('week12-review-schedule')


def delivery_paths():
    c = Canvas(1680, 640, bg=WHITE)
    prose(c, 840, 50, 'Your shared repository', 48, anchor='middle', bold=True)
    c.line(840, 80, 840, 105, TEAL, 5)
    c.line(400, 105, 1280, 105, TEAL, 5)
    arrow(c, 400, 105, 400, 135, TEAL)
    arrow(c, 1280, 105, 1280, 135, TEAL)
    prose(c, 400, 195, 'Web deployment', 52, anchor='middle', bold=True)
    prose(c, 1280, 195, 'GitHub Actions builds', 48, anchor='middle', bold=True)
    c.rect(0, 235, 800, 135, fill=PAPER, stroke=TEAL, width=3)
    prose(c, 400, 290, 'Hosted app', 46, anchor='middle', bold=True)
    prose(c, 400, 350, 'Share the live URL', 44, TEAL, 'middle')
    for x, platform in ((900, 'Web'), (1160, 'Windows'), (1420, 'Linux')):
        c.rect(x, 235, 240, 135, fill=PAPER, stroke=TEAL, width=3)
        prose(c, x + 120, 290, platform, 42, anchor='middle', bold=True)
        prose(c, x + 120, 350, 'build', 42, TEAL, 'middle')
    prose(c, 840, 435, 'A deployed version is still a work in progress.',
          46, anchor='middle', bold=True)
    for index, (x, value) in enumerate(((100, 'Deliver'), (540, 'Try'),
                                      (980, 'Observe'), (1420, 'Refine'))):
        prose(c, x, 535, value, 44, TEAL, 'middle')
        if index < 3:
            arrow(c, x + 125, 520, x + 305, 520)
    c.line(1420, 555, 1420, 585, TEAL, 4)
    c.line(100, 585, 1420, 585, TEAL, 4)
    arrow(c, 100, 585, 100, 555, TEAL)
    prose(c, 840, 625, 'Keep improving the delivered version over the coming week.',
          40, anchor='middle')
    return c.finish('week12-review-delivery-paths')


def program_path():
    c = Canvas(1680, 640, bg=WHITE)
    prose(c, 840, 70, 'Terminal command: python sketch.py', 48,
          anchor='middle', bold=True)
    box(c, 0, 165, 450, 285, 'sketch.py', ['print(2 + 3)'], AQUA)
    box(c, 615, 165, 450, 285, 'Python', ['Read source', 'Execute it'], VIOLET)
    c.rect(1230, 165, 450, 285, fill=INK)
    prose(c, 1260, 230, 'Terminal output', 46, WHITE, bold=True)
    text(c, 1455, 365, '5', 96, WHITE, 'middle')
    arrow(c, 470, 305, 595, 305)
    arrow(c, 1085, 305, 1210, 305)
    for x, value in ((0, 'Editor changes the file'), (615, 'Interpreter runs it'),
                     (1230, 'Read the result')):
        prose(c, x, 540, value, 40, TEAL)
    return c.finish('week12-review-program-path')


def git_history():
    c = Canvas(1680, 640, bg=WHITE)
    for x, heading, detail in ((0, 'Working files', 'edit'),
                               (560, 'Staged changes', 'git add'),
                               (1120, 'Commit history', 'git commit')):
        prose(c, x, 85, heading, 48, bold=True)
        text(c, x, 160, detail, 42, TEAL)
    c.rect(0, 225, 420, 160, fill=PAPER)
    text(c, 30, 315, 'sketch.py', 48)
    c.rect(560, 225, 420, 160, fill=PAPER)
    text(c, 590, 315, 'saved diff', 48)
    arrow(c, 440, 305, 540, 305)
    arrow(c, 1000, 305, 1100, 305)
    c.line(1170, 305, 1610, 305, INK, 6)
    for x in (1170, 1390, 1610):
        c.circle(x, 305, 22, fill=WHITE, stroke=TEAL, width=6)
    arrow(c, 1390, 350, 1390, 455)
    arrow(c, 1500, 455, 1500, 350)
    prose(c, 1180, 505, 'push / pull', 44, TEAL)
    prose(c, 1180, 565, 'GitHub copy', 48, bold=True)
    prose(c, 0, 560, 'Same commit + parameters + seed', 44)
    prose(c, 0, 620, 'A teammate can repeat the drawing.', 44, TEAL)
    return c.finish('week12-review-git-history')


def interface_state():
    import figures as tides

    c = Canvas(1680, 640, bg=WHITE)
    box(c, 0, 20, 450, 245, 'Event', ['Select day 17'], AQUA)
    box(c, 615, 20, 450, 245, 'Handler', ['Validate', 'Update state'], VIOLET)
    box(c, 1230, 20, 450, 245, 'State', ['month: 9', 'day: 17'], AQUA)
    arrow(c, 470, 140, 595, 140)
    arrow(c, 1085, 140, 1210, 140)
    c.line(1455, 285, 1455, 335, TEAL, 6)
    c.line(350, 335, 1455, 335, TEAL, 6)
    arrow(c, 350, 335, 350, 380, TEAL)
    arrow(c, 1300, 335, 1300, 380, TEAL)
    prose(c, 0, 430, 'Chart: day 17', 46, bold=True)
    tides._line_panel(c, tides._day(), 10, 450, 690, 105,
                      labels=False, width=4)
    prose(c, 960, 430, 'Caption: day 17', 46, bold=True)
    prose(c, 960, 515, 'Quarry Bay, 17 September', 44)
    prose(c, 840, 620, 'Both views are derived from the same selected state.',
          44, anchor='middle')
    return c.finish('week12-review-interface-state')


def pixel_shape():
    c = Canvas(1680, 640, bg=WHITE)
    prose(c, 80, 55, 'x: 3 columns', 44, bold=True)
    samples = ['#FF2814', '#14C846', '#1E5AF0', '#FFD228', '#505050', '#F0E6D7']
    for row in range(2):
        text(c, 40, 205 + row * 150, str(row), 44, INK, 'middle')
        for col in range(3):
            x, y = 80 + col * 250, 130 + row * 150
            c.rect(x, y, 240, 140, fill=samples[row * 3 + col])
            if row == 0:
                text(c, x + 120, 105, str(col), 44, INK, 'middle')
    prose(c, 80, 500, 'y: 2 rows', 44, bold=True)
    c.rect(575, 125, 250, 150, stroke=ORANGE, width=7)
    arrow(c, 850, 200, 1000, 200)
    text(c, 1050, 70, 'image[0][2]', 48)
    for index, (name, value, color) in enumerate((('R', 30, '#B74912'),
                                                ('G', 90, '#145A61'),
                                                ('B', 240, '#245AAB'))):
        x = 1060 + index * 195
        c.rect(x, 430 - value, 130, value, fill=color)
        text(c, x + 65, 470, name, 44, INK, 'middle')
        text(c, x + 65, 150, str(value), 44, color, 'middle')
    text(c, 950, 555, '(H, W, C) = (2, 3, 3)', 44)
    prose(c, 840, 625, '512 x 512 RGB at 8 bits/channel = 768 KiB raw',
          44, anchor='middle')
    return c.finish('week12-review-pixel-shape')


def sampling():
    c = Canvas(1680, 640, bg=WHITE)
    for frequency, baseline in ((220, 165), (440, 400)):
        text(c, 0, baseline + 15, f'{frequency} Hz', 44)
        c.line(180, baseline, 1220, baseline, '#D7D9D7', 2)
        points = [(180 + i / 441 * 1040,
                   baseline - 90 * math.sin(2 * math.pi * frequency * i / 44100))
                  for i in range(442)]
        for first, second in zip(points, points[1:]):
            c.line(*first, *second, ORANGE, 4)
        for point in points[::20]:
            c.circle(*point, 5, fill=TEAL)
    prose(c, 1300, 130, 'Same peak', 44, bold=True)
    prose(c, 1300, 190, 'amplitude A', 44, bold=True)
    prose(c, 1300, 355, 'Twice the', 44, TEAL)
    prose(c, 1300, 415, 'frequency', 44, TEAL)
    text(c, 180, 540, '0 ms', 40)
    text(c, 1220, 540, '10 ms', 40, anchor='end')
    prose(c, 840, 620, '44,100 samples/s. Dots show every 20th sample.',
          44, anchor='middle')
    return c.finish('week12-review-sampling')


def speech_path():
    c = Canvas(1680, 640, bg=WHITE)
    box(c, 0, 0, 450, 240, 'Audio input', ['Recorded samples'], AQUA)
    box(c, 615, 0, 450, 240, 'Recognition', ['Speech to text'], VIOLET)
    box(c, 1230, 0, 450, 240, 'Transcript', ['"turn left"'], AQUA)
    box(c, 1230, 380, 450, 240, 'Response text', ['"Turning left"'], AQUA)
    box(c, 615, 380, 450, 240, 'Synthesis', ['Text to speech'], VIOLET)
    box(c, 0, 380, 450, 240, 'Audio output', ['Hear / stop'], AQUA)
    arrow(c, 470, 120, 595, 120)
    arrow(c, 1085, 120, 1210, 120)
    arrow(c, 1455, 260, 1455, 360)
    prose(c, 1420, 320, 'rule / model', 40, anchor='end')
    arrow(c, 1210, 500, 1085, 500)
    arrow(c, 595, 500, 470, 500)
    return c.finish('week12-review-speech-path')


def ball_instances():
    c = Canvas(1680, 640, bg=WHITE)
    c.rect(535, 0, 610, 160, fill=PAPER, stroke=TEAL, width=3)
    prose(c, 840, 65, 'Ball class', 52, anchor='middle', bold=True)
    text(c, 840, 130, 'update(seconds)', 44, INK, 'middle')
    c.line(840, 160, 840, 190, TEAL, 5)
    c.line(325, 190, 1355, 190, TEAL, 5)
    arrow(c, 325, 190, 325, 220, TEAL)
    arrow(c, 1355, 190, 1355, 220, TEAL)
    box(c, 0, 220, 650, 285, 'red.update(0.1)',
        ['x: 16 to 17.40', 'y: 8 to 7.78'], ORANGE)
    box(c, 1030, 220, 650, 285, 'blue',
        ['x: 44 stays 44', 'y: 14 stays 14'], AQUA)
    prose(c, 840, 610, 'Only red updates. Each instance owns its attributes.',
          46, anchor='middle')
    return c.finish('week12-review-ball-instances')


def shared_views():
    c = Canvas(1680, 640, bg=WHITE)
    box(c, 0, 180, 600, 280, 'One simulation',
        ['red + blue objects', 'One update per tick'], AQUA)
    c.line(620, 320, 780, 320, TEAL, 6)
    c.line(780, 130, 780, 510, TEAL, 6)
    arrow(c, 780, 130, 930, 130, TEAL)
    arrow(c, 780, 510, 930, 510, TEAL)
    c.rect(950, 0, 730, 255, fill=INK)
    prose(c, 980, 65, 'ASCII: character cells', 44, WHITE, bold=True)
    text(c, 980, 145, 'R: (17, 8)', 46, WHITE)
    text(c, 980, 215, 'B: (44, 14)', 46, WHITE)
    c.rect(950, 380, 730, 240, fill=PAPER)
    prose(c, 980, 445, 'Pygame: circles', 44, bold=True)
    c.circle(1160, 515, 25, fill='#B74912')
    c.circle(1485, 565, 25, fill='#245AAB')
    prose(c, 0, 590, 'Both views read the same state.', 44, TEAL)
    return c.finish('week12-review-shared-views')


def scrum_artifacts():
    c = Canvas(1680, 640, bg=WHITE)
    for x, heading, goal in ((0, 'Product Backlog', 'Product Goal'),
                             (590, 'Sprint Backlog', 'Sprint Goal'),
                             (1180, 'Increment', 'Definition of Done')):
        prose(c, x, 65, heading, 46, bold=True)
        prose(c, x, 610, goal, 44, TEAL)
    for row, item in enumerate(('Pause menu', 'Save game', 'Sound cues')):
        c.rect(0, 150 + row * 105, 460, 85, fill=PAPER)
        prose(c, 24, 208 + row * 105, item, 44)
    arrow(c, 485, 190, 565, 190)
    c.rect(590, 150, 460, 300, fill=PAPER)
    prose(c, 615, 210, 'Pause menu', 44, bold=True)
    prose(c, 615, 310, 'Build + test plan', 40)
    arrow(c, 1075, 300, 1155, 300)
    c.rect(1180, 150, 500, 300, fill=TEAL)
    prose(c, 1210, 220, 'Pause menu works', 44, WHITE, bold=True)
    prose(c, 1210, 320, 'Integrated + usable', 40, WHITE)
    return c.finish('week12-review-scrum-artifacts')


def pull_request_graph():
    c = Canvas(1680, 640, bg=WHITE)
    prose(c, 0, 60, 'main', 48, bold=True)
    c.line(100, 145, 1560, 145, INK, 6)
    c.line(100, 145, 550, 380, TEAL, 6)
    c.line(550, 380, 1080, 380, TEAL, 6)
    c.line(1080, 380, 1560, 145, TEAL, 6)
    for x, y, color in ((100, 145, INK), (550, 380, TEAL),
                         (1080, 380, TEAL), (1560, 145, INK)):
        c.circle(x, y, 23, fill=WHITE, stroke=color, width=7)
    prose(c, 280, 320, 'branch', 44, TEAL, 'middle')
    prose(c, 550, 475, 'commit + push', 44, anchor='middle')
    prose(c, 1080, 475, 'PR + review', 44, anchor='middle')
    prose(c, 1540, 80, 'merge', 44, anchor='middle')
    prose(c, 840, 615, 'Inspect the diff. Try the change. Then everyone pulls main.',
          44, anchor='middle')
    return c.finish('week12-review-pull-request')


def ci_delivery():
    from week11_figures import sequence

    return sequence('week12-ci-delivery', [
        ('PR checks', 'tests + types', 'build artifact'),
        ('Deploy job', 'migrate D1', 'deploy + secrets'),
        ('Live Worker', 'DB binding', 'runtime secrets'),
    ], 'Verify sign-in and private notes on the deployed app')


def http_websocket():
    c = Canvas(1680, 640, bg=WHITE)
    for x, heading in ((0, 'HTTP snapshot'), (900, 'WebSocket connection')):
        prose(c, x, 55, heading, 48, bold=True)
        for endpoint, who in ((x + 40, 'Client'), (x + 700, 'Server')):
            c.line(endpoint, 140, endpoint, 485, TEAL, 4)
            prose(c, endpoint, 115, who, 40,
                  anchor='start' if who == 'Client' else 'end')
    arrow(c, 60, 235, 680, 235)
    text(c, 370, 205, 'GET /state', 42, INK, 'middle')
    arrow(c, 680, 400, 60, 400, TEAL)
    text(c, 370, 370, '200 + JSON', 42, INK, 'middle')
    for y, label, reverse in ((215, 'open once', False),
                               (325, 'action', False), (435, 'state', True)):
        arrow(c, 1580 if reverse else 960, y,
              960 if reverse else 1580, y, TEAL if reverse else ORANGE)
        text(c, 1270, y - 30, label, 42, INK, 'middle')
    prose(c, 0, 595, 'One request and response', 42)
    prose(c, 900, 595, 'Both endpoints send messages', 42)
    return c.finish('week12-review-http-websocket')


def shared_scene():
    import week09_figures as network

    c = Canvas(1680, 640, bg=WHITE)
    network.node(c, 0, 'Browser A', ['input: 25', 'x = 25'])
    network.node(c, 630, 'Python Scene', ['x = 25', 'revision = 1'])
    network.node(c, 1260, 'Browser B', ['input: 50', 'x = 25'])
    network.arrow(c, 1058, 1250, 320, 'state')
    network.arrow(c, 620, 430, 320, 'state', AQUA)
    network.text(c, 840, 560, '{"type":"state", "x":25, "revision":1}',
                 44, anchor='middle')
    return c.finish('week12-review-shared-scene')


def relations():
    c = Canvas(1680, 640, bg=WHITE)
    box(c, 0, 175, 500, 235, 'User', ['id: 1', 'name: Ada'], AQUA)
    for y, identity in ((0, 3), (330, 4)):
        box(c, 580, y, 500, 235, 'Conversation',
            [f'id: {identity}', 'owner_id: 1'], VIOLET)
    for y, identity in ((0, 7), (330, 8)):
        box(c, 1160, y, 520, 235, 'Message',
            [f'id: {identity}', 'conversation_id: 3'], AQUA)
    c.line(500, 290, 540, 290, ORANGE, 5)
    c.line(540, 117, 540, 447, ORANGE, 5)
    arrow(c, 540, 117, 575, 117)
    arrow(c, 540, 447, 575, 447)
    c.line(1080, 117, 1120, 117, ORANGE, 5)
    c.line(1120, 117, 1120, 447, ORANGE, 5)
    arrow(c, 1120, 117, 1155, 117)
    arrow(c, 1120, 447, 1155, 447)
    prose(c, 840, 620, 'Primary key: row identity. Foreign key: parent reference.',
          42, anchor='middle')
    return c.finish('week12-review-relations')


def embeddings():
    c = Canvas(1680, 640, bg=WHITE)
    box(c, 0, 15, 500, 235, 'Question', ['Card replacement', 'cost?'], AQUA)
    box(c, 0, 330, 500, 235, 'Passage', ['Replacement fee', 'HK$150'], VIOLET)
    c.poly([(645, 155), (1015, 155), (1080, 300),
            (1015, 445), (645, 445), (580, 300)], fill=PAPER, stroke=ORANGE, width=4)
    prose(c, 830, 270, 'Same trained', 46, anchor='middle', bold=True)
    prose(c, 830, 340, 'encoder', 46, anchor='middle', bold=True)
    prose(c, 830, 405, 'MiniLM / 384D', 40, TEAL, 'middle')
    c.line(500, 130, 555, 130, ORANGE, 5)
    arrow(c, 555, 130, 555, 245)
    c.line(555, 245, 605, 245, ORANGE, 5)
    c.line(500, 480, 555, 480, ORANGE, 5)
    arrow(c, 555, 480, 555, 355)
    c.line(555, 355, 605, 355, ORANGE, 5)
    text(c, 1190, 170, 'Query vector', 44)
    text(c, 1190, 240, '[q1, ..., q384]', 42, TEAL)
    text(c, 1190, 440, 'Passage vector', 44)
    text(c, 1190, 510, '[p1, ..., p384]', 42, TEAL)
    arrow(c, 1050, 210, 1160, 210)
    arrow(c, 1050, 390, 1160, 390)
    prose(c, 840, 620, 'Compare compatible vectors. Keep text, page and source ID.',
          42, anchor='middle')
    return c.finish('week12-review-embeddings')


def model_context():
    c = Canvas(1680, 640, bg=WHITE)
    box(c, 0, 0, 450, 235, 'Handbook index',
        ['Shared passages', 'Retrieved text'], VIOLET)
    box(c, 0, 365, 450, 235, 'Saved history',
        ['Owner + chat', 'Selected turns'], AQUA)
    box(c, 590, 155, 500, 345, 'This model call',
        ['Rules + question', 'Selected history', 'Retrieved text'], ORANGE)
    for source_y, target_y in ((120, 260), (485, 395)):
        c.line(450, source_y, 520, source_y, ORANGE, 5)
        c.line(520, source_y, 520, target_y, ORANGE, 5)
        arrow(c, 520, target_y, 570, target_y)
    box(c, 1230, 165, 450, 235, 'Answer', ['Text + citations'], AQUA)
    arrow(c, 1110, 285, 1210, 285)
    arrow(c, 1455, 420, 1455, 470)
    prose(c, 1455, 545, 'Speech playback', 44, anchor='middle', bold=True)
    return c.finish('week12-review-model-context')
