"""Editable Week 8 diagrams on the course's standard slide grid."""
from deckgen import (
    Slide, Rect, T, eyebrow, INK, WHITE, PAPER, MUTED, LINE,
    ORANGE, TEAL, BLUE, RED, GREEN, CODE,
)


def canvas(eye, heading, notes):
    slide = Slide(bg=WHITE, title=heading, notes=notes)
    slide.els = [
        eyebrow(120, 96, eye),
        T(120, 184, 1680, 110, heading, 'xbold', 64, INK, lh=0.95),
    ]
    return slide


def grading(notes):
    slide = canvas('GROUP PROJECT / 40% OF COURSE GRADE',
                   'How the project is marked', notes)
    for x, width, share, heading, detail, fill, color in [
        (120, 400, '25%', 'Creative idea', 'Novelty\nand value', PAPER, INK),
        (540, 840, '50%', 'Code', 'Works, meets the brief\nand handles complexity', INK, WHITE),
        (1400, 400, '25%', 'Execution', 'Steady work;\nweekly progress', TEAL, INK),
    ]:
        slide.els += [
            Rect(x, 360, width, 430, fill),
            T(x + 32, 392, width - 64, 140, share, 'xbold', 112, color),
            T(x + 32, 555, width - 64, 75, heading, 'semibold', 48, color),
            T(x + 32, 660, width - 64, 110, detail, 'body', 42, color),
        ]
    slide.els.append(T(120, 870, 1680, 60,
        'These are shares of the group-project mark.', 'body', 40, MUTED))
    return slide


def submission(brief_url, notes):
    slide = canvas('GROUP PROJECT / CANVAS', 'Register your repository now.', notes)
    for y, number, action in [
        (350, '1', 'Create one shared GitHub repository for your team.'),
        (470, '2', 'Submit its URL on Canvas; an initial README is enough.'),
        (590, '3', 'Keep building and documenting progress in that repository.'),
    ]:
        slide.els += [
            T(120, y, 80, 80, number, 'xbold', 56, ORANGE),
            T(230, y + 8, 1570, 80, action, 'body', 44, INK),
        ]
    slide.els += [
        Rect(120, 735, 1680, 115, INK),
        T(150, 764, 1620, 65, 'Sunday 6 December 2026, 23:59 HKT',
          'semibold', 48, WHITE),
        T(120, 895, 1680, 60, f'[Read the group-project brief →]({brief_url})',
          'body', 40, BLUE),
    ]
    return slide


def starters(notes):
    slide = canvas('THREE STARTERS / CHOOSE YOUR PROJECT',
                   'Choose a starting point.', notes)
    for x, heading, kind, outputs, repository in [
        (120, 'Capacitor', 'Web interface', 'Web + Android', 'capacitor-app-template'),
        (700, 'Godot', '2D game', 'Desktop + web', 'godot-game-template'),
        (1280, 'Python + uv', 'Python app', 'Source + desktop bundles', 'python-uv-app-template'),
    ]:
        slide.els += [
            Rect(x, 350, 520, 435, PAPER),
            T(x + 30, 385, 460, 80, heading, 'xbold', 56, INK),
            T(x + 30, 495, 460, 65, kind, 'body', 44, INK),
            T(x + 30, 580, 460, 110, outputs, 'body', 40, INK),
            T(x + 30, 710, 460, 60,
              f'[Open template →](https://github.com/sd5913/{repository})',
              'semibold', 40, BLUE),
        ]
    slide.els.append(T(120, 865, 1680, 65,
        'Create a team repository → open it in Codex → check CI.', 'body', 42, INK))
    return slide


def conflict(notes):
    slide = canvas('TEAMWORK / CONFLICT', 'Two people changed the same line.', notes)
    slide.els += [
        T(120, 330, 740, 65, 'Git marks both versions', 'semibold', 44, INK),
        T(1050, 330, 750, 65, 'Agree on the result', 'semibold', 44, INK),
        Rect(120, 430, 740, 350, PAPER),
        T(150, 465, 680, 280,
          '<<<<<<< HEAD\nlabel = "Play"\n=======\nlabel = "Start"\n>>>>>>> feature/start-button',
          'mono', CODE, INK, lh=1.45),
        T(900, 535, 110, 100, '→', 'xbold', 72, ORANGE, align='c'),
        Rect(1050, 430, 750, 140, INK),
        T(1080, 475, 690, 65, 'label = "Play"', 'mono', CODE, WHITE),
        T(1050, 630, 750, 150, 'Remove the markers.\nRun it; commit the resolution.',
          'body', 42, INK),
        T(120, 875, 1680, 65, 'Resolve the intention together; then test the interaction.',
          'body', 42, INK),
    ]
    return slide


def camera_frame(notes):
    slide = canvas('COMPUTER VISION / DATA', 'What is a camera frame?', notes)
    slide.els += [
        T(120, 325, 680, 65, 'A grid of colour values', 'semibold', 44, INK),
        T(1000, 325, 800, 65, 'One pixel: three channels', 'semibold', 44, INK),
    ]
    shades = [INK, BLUE, TEAL, PAPER, TEAL, BLUE]
    for row in range(4):
        for col in range(6):
            slide.els.append(Rect(120 + col * 104, 420 + row * 84,
                                  96, 76, shades[(row + col) % len(shades)]))
    slide.els += [
        Rect(328, 504, 96, 76, WHITE, ORANGE, 6),
        T(805, 492, 120, 95, '→', 'xbold', 72, ORANGE),
    ]
    for x, label, color in [(1000, 'B', BLUE), (1270, 'G', GREEN), (1540, 'R', RED)]:
        slide.els += [
            Rect(x, 440, 240, 170, color),
            T(x, 482, 240, 85, label, 'xbold', 64, INK if color == GREEN else WHITE,
              align='c'),
        ]
    slide.els += [
        T(1000, 655, 800, 100, 'OpenCV: BGR\nMediaPipe input: RGB', 'body', 42, INK),
        Rect(120, 820, 1680, 2, LINE),
        T(120, 860, 1680, 65, 'Video = frame → frame → frame over time',
          'semibold', 44, INK),
    ]
    return slide


def objects(notes):
    slide = canvas('PYTHON / WEEK 7 REVISITED', 'Classes, objects and methods', notes)
    columns = [(150, 470, 'Class'), (670, 300, 'Object'), (1020, 750, 'Method call')]
    for x, width, label in columns:
        slide.els.append(T(x, 330, width, 60, label, 'semibold', 42, MUTED))
    for y, values in [
        (420, ('Ball', 'red', 'red.update(0.1)')),
        (565, ('VideoCapture', 'camera', 'camera.read()')),
        (710, ('HandLandmarker', 'tracker', 'tracker.detect_for_video(...)')),
    ]:
        slide.els.append(Rect(120, y, 1680, 115, PAPER))
        for (x, width, _), value in zip(columns, values):
            slide.els.append(T(x, y + 30, width, 65, value, 'body', 42, INK))
    slide.els.append(T(120, 890, 1680, 65,
        'Create an object once. Call its methods as the program runs.', 'body', 42, INK))
    return slide


def fingertip(notes):
    slide = canvas('PYTHON / FOLLOW THE RESULT', 'Find the index fingertip', notes)
    slide.els += [
        T(120, 320, 1680, 70, 'result.hand_landmarks[0][8].x', 'semibold', 54, INK),
    ]
    for x, heading, detail in [
        (120, 'hand_landmarks', 'List of detected hands'),
        (700, '[0][8]', 'First hand → fingertip 8'),
        (1280, '.x', 'Horizontal position'),
    ]:
        slide.els += [
            Rect(x, 460, 520, 240, PAPER),
            T(x + 28, 490, 464, 80, heading, 'semibold', 44, INK),
            T(x + 28, 600, 464, 90, detail, 'body', 40, INK),
        ]
        if x < 1280:
            slide.els.append(T(x + 528, 530, 52, 85, '→', 'xbold', 52, ORANGE))
    slide.els += [
        Rect(120, 810, 1680, 8, INK),
        Rect(960, 790, 4, 48, ORANGE),
        T(120, 860, 500, 65, '0 / left edge', 'body', 42, INK),
        T(710, 860, 500, 65, '0.5 / centre', 'body', 42, INK, align='c'),
        T(1300, 860, 500, 65, '1 / right edge', 'body', 42, INK, align='r'),
    ]
    return slide


def tiles(example_url, notes):
    slide = canvas('LIVE / HAND TO RESPONSE', 'A coordinate becomes a choice.', notes)
    slide.els += [
        T(120, 325, 1680, 65, 'Index fingertip / landmark 8 / horizontal position x',
          'body', 42, INK),
        Rect(120, 440, 840, 310, BLUE),
        Rect(960, 440, 840, 310, RED),
        T(160, 480, 760, 100, 'Blue', 'xbold', 72, WHITE),
        T(1000, 480, 760, 100, 'Red', 'xbold', 72, WHITE),
        T(160, 640, 760, 65, 'x < 0.5', 'semibold', 48, WHITE),
        T(1000, 640, 760, 65, 'x ≥ 0.5', 'semibold', 48, WHITE),
        T(120, 795, 1680, 65, 'No hand → None → neither tile is selected.',
          'semibold', 42, INK),
        T(120, 890, 1680, 60, f'[Open the hand-to-tile example →]({example_url})',
          'body', 40, BLUE),
    ]
    return slide


def tutorial(tutorial_url, browser_url, notes):
    slide = canvas('TUTORIAL / TWO HOURS', 'Try all nine vision examples.', notes)
    slide.els += [
        T(120, 350, 1680, 100,
          'Camera → face / hand / pose → mesh / gesture', 'semibold', 44, INK),
        T(120, 465, 1680, 100,
          'Combine models. Try segmentation. Question expression labels.', 'body', 42, INK),
        T(120, 585, 1680, 70, f'[Open the PFAD Week 8 tutorial →]({tutorial_url})',
          'semibold', 42, BLUE),
        Rect(120, 715, 1680, 235, PAPER),
        T(150, 740, 1620, 75, 'Could this inspire your project?', 'xbold', 52, INK),
        T(150, 845, 1620, 85,
          f'Computer vision is optional. [Try hand tracking in a browser →]({browser_url})',
          'body', 40, INK),
    ]
    return slide
