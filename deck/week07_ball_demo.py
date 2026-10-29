"""Short classes introduction using the runnable PFAD Week 7 physics model."""

from deckgen import Rect, T, INK, WHITE, PAPER, ORANGE
from deckgen.layouts import code_panel, content


CLASS_CODE = '''class Ball:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = 1'''

UPDATE_CODE = '''class Ball:
    # __init__ is shown on the previous slide.

    def update(self, seconds):
        self.vy += GRAVITY * seconds
        self.x += self.vx * seconds
        self.y += self.vy * seconds'''

OBJECT_CODE = '''red = Ball(x=16, y=8, vx=14, vy=-5)
blue = Ball(x=44, y=14, vx=-10, vy=-9)

red.update(0.1)
print(f"red=({red.x:.2f}, {red.y:.2f})")
print(f"blue=({blue.x}, {blue.y})")'''


def excerpt(heading, code, caption, notes):
    slide = code_panel('AFTER THE BREAK / CLASSES / PFAD WEEK 7', heading,
                       code.splitlines(), caption=caption, notes=notes)
    for element in slide.els:
        if getattr(element, 'name', '') == 'code':
            for paragraph in element.paras:
                for run in paragraph.runs:
                    run.size = 40
    return slide


def ball_demo_slides():
    slides = [excerpt('A class defines each ball.', CLASS_CODE,
        'Ball is the class. Each object gets its own position and velocity.',
        '10:35: open ~/Work/sd5913/pfad/week07/ball.py on this laptop. '
        'This is the actual Ball.__init__ excerpt, not a replacement script. '
        'A class groups attributes and methods. Calling Ball(...) creates an instance; '
        '__init__ sets its starting attributes. x and y are position; vx and vy are '
        'velocity; radius controls the size. self refers to the particular object. '
        'Keep this the only new theory after the test. Students can watch; no setup '
        'or extra submission is required.'),
        excerpt('A method changes this ball.', UPDATE_CODE,
        'GRAVITY = 28. self is this ball; seconds is the time to advance.',
        'This abbreviated class shows the first three lines of Ball.update. '
        'The module defines GRAVITY = 28 above the class; point to it in the open source. '
        'Gravity changes vertical velocity, then velocity changes position. '
        'Coordinates start at the top left, so increasing y moves down. '
        'The rest of the real method handles wall/floor bounces. Do not introduce '
        'simulation clocks, watcher internals or renderer architecture as more theory.'),
        excerpt('Call red. Does blue move?', OBJECT_CODE,
        'Predict first. Run ball.py to check which object moves.',
        'Ask for a prediction before running the output on the laptop. '
        'Run uv run week07/ball.py from ~/Work/sd5913/pfad. '
        'Expected: red=(17.40, 7.78), blue=(44, 14). '
        'Only red moves after red.update(0.1); blue keeps its own attributes. '
        'Then the script also calls blue.update(0.1), which moves blue independently. '
        'A shared class does not mean shared position attributes.'),
    ]

    views = content('ONE MODEL / TWO VIEWS', 'Same motion. Two ways to draw it.', [],
        notes='In ball_both.py, one Simulation owns the same red and blue Ball '
        'objects and advances them once per tick. Both renderers read those positions. '
        'ASCII uses character cells, so tiny moves can stay within one cell; Pygame '
        'draws circles at finer resolution. Separately starting the two standalone '
        'programs gives independent clocks. Use the combined launcher for this demo.')
    views.els = views.els[:2]
    views.els += [
        Rect(120, 410, 560, 380, PAPER),
        T(160, 450, 480, 70, 'One simulation', 'xbold', 48, INK),
        T(160, 560, 480, 70, 'red + blue', 'semibold', 44, INK),
        T(160, 660, 480, 70, 'x, y, vx, vy', 'mono', 40, INK),
        Rect(680, 598, 190, 4, ORANGE),
        Rect(866, 450, 4, 300, ORANGE),
        Rect(870, 450, 180, 4, ORANGE),
        Rect(870, 746, 180, 4, ORANGE),
        Rect(1050, 330, 750, 250, INK),
        T(1090, 365, 670, 70, 'ASCII', 'xbold', 48, WHITE),
        T(1090, 460, 670, 70, 'R             B', 'mono', 48, WHITE),
        Rect(1050, 650, 750, 250, PAPER),
        T(1090, 685, 670, 70, 'Pygame', 'xbold', 48, INK),
        T(1090, 780, 670, 70, 'Coloured circles', 'body', 40, INK),
        T(120, 920, 1680, 60, 'Both views read the same Ball objects.',
          'body', 36, INK),
    ]
    slides.append(views)
    slides.append(content('LAPTOP DEMO / WATCH, PREDICT, SAVE',
        'Change the class. Watch both views.', [
            'From pfad: uv run week07/ball_both.py',
            'Keep week07/ball.py open beside the two views.',
            'Predict: what changes if GRAVITY goes from 28 to 56?',
            'Save. Both views reset and use the edited class.',
            '[Example and optional practice](https://github.com/sd5913/pfad/tree/2026/week07)',
        ], body_size=38,
        notes='Finish the physics demo by about 10:42. Use 10:42-10:44 for inspiration '
        'and 10:44-10:45 for Canvas registration, one minute maximum. Run from '
        '~/Work/sd5913/pfad; uv supplies dependencies with no flags. '
        'Arrange the terminal and Pygame side by side. Change GRAVITY = 28 to '
        'GRAVITY = 56, ask for a prediction, save, and observe the stronger fall. '
        'Saving reloads the class and resets both views to their starting state. '
        'Restore 28 and save after the comparison. A bad edit keeps the previous '
        'model or freezes the last valid frame until fixed. Space pauses/resumes; '
        'R resets; closing Pygame stops both. watchfiles handles saves but its '
        'implementation is optional tutorial reading, not another theory topic.'))
    return slides
