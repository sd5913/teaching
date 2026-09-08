"""
SD5913 · Week 01 — Programming for artists and designers.

    deckgen build --pptx        # export/ only, no node needed
    deckgen build               # everything, as the workflows run it

Delivered 2026-09-03 from archive/SD5913-week01.pptx, a 64-slide PptxGenJS deck whose
generator is not on this box. This file is that deck re-authored in deckgen, so week 1
gets what every later week has: the phone reading view, the console, and the links to
what the room answered. The argument, the order and the speaker notes are the delivered
deck's; the wording is carried over, not rewritten.

What is different from the file that was shown:

  - Slides 53–57, "Design the mark", are not here. They were written but never run — the
    room ran out of time — and they live in week 2 now (deck/week02.py, section 02).
  - The five ClassPoint activities the room ran are the five ClassPoint slides here, in
    the order they ran; deck/week01-reports.json links each to its answers. The two
    activities that were built but never run (the "quick check" on s38 and the Design the
    mark capture on s56) are therefore not ClassPoint slides — the quick check is a show of
    hands. attach_reports() raises if this drifts.
  - Attribution fixes from docs/week01-lesson-plan.md: Lovelace is the Carpenter portrait,
    not the generated image; Babbage is credited to the Science Museum Group (CC BY-NC-SA);
    Nake's 1966 print is a photograph of a plotter drawing, not a C-type print; the 1965
    piece carries its accessioned title.
  - The tutorial install slide points at ait4x/v915-setup rather than at Copilot running
    winget, which is what the room actually used from week 2 on.
  - Schotter is drawn from the same rule as pfad/week01/first-repo/sketch.py (figures.py),
    and runs live in the html deck. The delivered deck had it as a linked image.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import figures as F                                   # noqa: E402
from deckgen import attach_reports, INK, WHITE        # noqa: E402
from deckgen.layouts import (title, agenda, section, statement, quote, content, cards,   # noqa: E402
                             question, image_full, timeline, two_col, assessment, video,
                             live, end)

COURSE = 'SD5913'
SITE = 'sd5913.github.io/teaching'
REPO = 'github.com/sd5913/pfad'
EYE = 'SD5913 · WEEK 01'

S = []

# ───────────────────────── 0 · landing ─────────────────────────
S.append(title(EYE + ' · LECTURE', 'Programming for artists and designers',
               'PolyU School of Design · pfad.ait4x.org', size=120,
               notes='Welcome. Say the course code and that this is the lecture half; '
                     'tutorial follows in the afternoon.'))

S.append(agenda(EYE, [
    'Why are we here?',
    'Who are we?',
    'Computers',
    'Programs',
    'Programming languages',
    'Python',
    'Tools for the job',
    'Assignments and tutorials',
], notes='Eight stops. Point out the two interactive moments and the tutorial block at the end.'))

# ───────────────────────── 1 · why are we here ─────────────────────────
S.append(question('short_answer', 'Why are we here?',
                  eyebrow_text='01 · QUESTION · SHORT ANSWER',
                  hint='One sentence. Why a programming course for art and design?',
                  notes='ClassPoint short answer. One sentence each. Leave it on screen for a '
                        'minute, then read a few aloud.'))

# ───────────────────────── 2 · who are we ─────────────────────────
S.append(content('02 · WHO IS TEACHING YOU', 'I came to this from economics.', [
    'No computer science degree. I learned to code because **I wanted to make things** that '
    'could not be made any other way. That is still the only reason I use it.',
    '',
    '{mono:// what I made with it}',
    '- **Musical Fruitstand** — fruit you can play. No screen.',
    '- **A-Eye** — the audience, repainted live at M+.',
    '- **Featherman** — a mobile game, with WWF Mai Po.',
    '- {muted:giovannilion.link — later, not now.}',
], notes='Economics background, no CS. The reason to code is to make things that cannot be '
         'made another way.'))

S.append(quote('The robot rebooted minutes before the cue.',
               "2017–2019 · Hanson Robotics · I was Sophia's operator for two years. Someone knocked "
               'out a power cable during setup, in front of thousands of people. It came back. '
               'The show went on.',
               notes='Hanson Robotics 2017-2019. Cable knocked out before a show for thousands. It '
                     'rebooted; the show went on. Point: things break, you keep going.'))

S.append(section('02', 'Who are we?', "Artists and designers · what's your X?",
                 notes='Chapter two. Who are you? Two questions coming.'))

S.append(question('multiple_choice', 'Are you an artist or a designer?',
                  choices=['Artist', 'Designer', 'Both / not sure'],
                  notes='ClassPoint multiple choice. Show the split, no judgement.'))

S.append(quote('“…a subjective perspective that reminds us of the human condition.”',
               'Artists? — Hannah Arendt, The Human Condition, 1958',
               notes='Arendt, The Human Condition, 1958. Art keeps a subjective view alive.'))

S.append(question('multiple_choice', 'Is programming an art?',
                  choices=['Yes', 'No', 'It can be'],
                  notes='ClassPoint multiple choice. Then show two Nake pieces and let them '
                        'decide again.'))

S.append(image_full('nake-homage-to-paul-klee-1965.jpg', '1965 · FRIEDER NAKE · HOMMAGE À PAUL KLEE, 13/9/65 NR.2',
                    'A program drew this. Screenprint after a plotter drawing, 49.2 × 49.2 cm. '
                    'Victoria and Albert Museum, E.951-2008.',
                    fit='contain', bg=WHITE,
                    notes='1965. A program drew this. It hangs in the V&A.'))

S.append(image_full('nake-walk-through-raster-1966.jpg', '1966 · FRIEDER NAKE · WALK-THROUGH-RASTER, SERIES 2, 1–4',
                    'Same idea: a rule, run many times, with a little randomness. Photograph of a '
                    'plotter drawing. Victoria and Albert Museum, E.955-2008.',
                    fit='contain', bg=WHITE,
                    notes='1966. Same idea: a rule, run many times, with a little randomness. Next '
                          'week you read the rule.'))

S.append(video('TALK · DYLAN BEATTIE', 'The Art of Code', '6avJHaC3C2U', [
    'Inspiration for assignment 1.',
    '',
    '{muted:youtube.com/watch?v=6avJHaC3C2U}',
], thumb='yt/6avJHaC3C2U.jpg', notes="Play a few minutes of Dylan Beattie's talk. This is the reference for assignment 1."))

SCHOTTER_JS = '''let chaos = 1.0, seed = 5913;

function setup() {
  createCanvas(464, 784);
  noFill(); stroke(17); strokeWeight(1.4);
  noLoop();
}

function draw() {
  background('#faf8f4');
  randomSeed(seed);
  for (let row = 0; row < 22; row++) {
    const damage = chaos * (row / 22) ** 2;
    for (let col = 0; col < 12; col++) {
      push();
      translate(56 + col * 32 + random(-1, 1) * damage * 16,
                56 + row * 32 + random(-1, 1) * damage * 16);
      rotate(random(-1, 1) * damage * PI / 4);
      rect(-16, -16, 32, 32);
      pop();
    }
  }
}'''
SCHOTTER_EXTRA = '''function mouseMoved() { chaos = constrain(mouseX / width * 2, 0, 2); redraw(); }
function mousePressed() { seed = floor(random(1000000)); redraw(); }'''

S.append(content('GEORG NEES · SCHOTTER · 1968', 'One rule. One number.', [
    '12 squares across, 22 down. The top row is perfect. Every row after it is rotated and '
    'moved a little more, until the bottom is rubble.',
    '',
    'In the tutorial you change that number and watch it become a different picture.',
    '',
    '{mono:CHAOS = 1.0}',
    '',
    '{muted:Drawn by the rule in pfad/week01/first-repo/sketch.py, seed 5913.}',
], figure=F.schotter(), sketch=live('schotter', SCHOTTER_JS, 464, 784,
                                    hint='move the mouse: chaos · click: new seed',
                                    extra=SCHOTTER_EXTRA),
   notes='Georg Nees, 1968. 12 across, 22 down. One rule: rotate and shift each row a little '
         'more. In the tutorial you change that one number. In the html deck the picture is '
         'live — mouse left to right is chaos 0 to 2, a click reseeds it.'))

S.append(quote('…a creative perspective that is data-driven and user-centric.',
               'Designers?',
               notes='Designers: creative, but they answer to data and to the user.'))

S.append(image_full('babbage-analytical-engine.jpg', '1837 · CHARLES BABBAGE · THE ANALYTICAL ENGINE',
                    'A computer is a physical thing. Brass, steel and gears, cut by hand by craftsmen. '
                    'This one was designed but never finished. Someone wrote a program for it anyway. '
                    'Trial model, Science Museum Group 1878-3, CC BY-NC-SA 4.0.',
                    notes="Babbage's Analytical Engine, 1837 onwards. Brass and steel, cut by hand by "
                          'craftsmen. A computer is a physical, tangible machine — and this one was '
                          'never finished. Ada Lovelace wrote a program for it anyway.'))

S.append(quote("Wrote the first program — for Babbage's Analytical Engine, a computer that did not exist yet.",
               'Ada Lovelace, Note G, 1843 · Portrait by Margaret Sarah Carpenter, 1836, Government Art Collection',
               image='ada-lovelace-portrait.jpg', fit='cover', size=64,
               notes='Note G, 1843: the first published algorithm, written for a machine that was '
                     'never built.'))

S.append(content('AGILEMANIFESTO.ORG · 2001', 'Is programming a craft?', [
    '**Individuals and interactions** {muted:over processes and tools}',
    '**Working software** {muted:over comprehensive documentation}',
    '**Customer collaboration** {muted:over contract negotiation}',
    '**Responding to change** {muted:over following a plan}',
], notes='Agile manifesto, 2001. Craft: individuals, working software, collaboration, '
         'responding to change.'))

S.append(statement('Both want to change attitudes and behaviour.', eyebrow_text='ART AND DESIGN',
                   notes='Both want to change how people think and act. Code is one more way to do that.'))

S.append(content('CULTURE AND TECHNOLOGY', 'Mediated perception', [
    'Technologies do not exist “in themselves.” They exist in relation to people and culture.',
    '',
    '{muted:— Don Ihde}',
    '',
    '{mono:you  ←→  tool  ←→  world}',
], notes='Don Ihde: a tool is never neutral. It changes how we see. Code is a tool like that.'))

S.append(question('word_cloud', "What's your X?",
                  hint='One word. What do you want to make with code this semester?',
                  notes='ClassPoint word cloud to close. One word: what do you want to make with '
                        'code this semester?'))

S.append(two_col('HOW TO SURVIVE THE SEMESTER', 'Stay in flow', [
    'Bored? Find a harder problem.',
    '',
    'Anxious? Learn a skill, or make the problem smaller.',
    '',
    'Then sleep.',
    '',
    '{muted:You will read this loop again in week 4, once while means something, and run it '
    'for real in week 13.}',
], [
    'problem = None',
    'while semester() == 1:',
    '    if not problem:',
    '        problem = Problem.current()',
    '    while not problem.solved:',
    '        try:',
    '            code = self.challenge(problem)',
    '            problem.solved = code.run(problem)',
    '        except:',
    '            panic = reality_check()',
    '            break',
    '    state = check_state()',
    '    if state == "bored" or problem.solved:',
    '        problem = Problem.find_harder(problem)',
    '    elif state == "anxious" or panic:',
    '        try:',
    '            skill_upgrade(self)',
    '        except:',
    '            simplify(problem)',
    '        finally:',
    '            sleep(8 * 60 * 60)',
], right_size=21, notes='Read the loop out loud. Too easy: find a harder problem. Too hard: '
                        'upgrade a skill or simplify. Then sleep.'))

S.append(assessment('ASSESSMENT', 'Five components', [
    ('10%', 'Participation', 'Come, or tell us before you do not.', False),
    ('30%', 'Individual assignments', 'Three, on GitHub, on time.', False),
    ('10%', 'Mid-term quiz', 'In class, week 7.', False),
    ('40%', 'Group project', "A GitHub repo with everyone's commits. Original code. Multimedia. "
                             'Scope agreed by week 8.', True),
    ('10%', 'Final quiz', 'In class, week 13.', False),
], notes='Five parts. The group project is the big one. Participation means: come, or tell us '
         "before you don't."))

S.append(cards('INDIVIDUAL ASSIGNMENTS · 30%', 'Three repos, three dates', [
    ('01 · 5%', 'Reflection', ['Why are we here? 500–1000 words.', '', '{orange:DUE SUN 13 SEP}']),
    ('02 · 10%', 'Data visualisation', ['Get data about a natural phenomenon. Show it.', '', '{orange:DUE SUN 27 SEP}']),
    ('03 · 15%', 'Interactive experience', ['Something people can play with.', '', '{muted:LATER IN THE SEMESTER}']),
], notes='Three assignments, all as GitHub repos. Dates on screen.'))

S.append(video('VIDEO', "The programmer's mindset", '3o63D0-_x2k', [
    'Programmers are not smarter. They are used to being wrong and trying again.',
    '',
    '{muted:youtube.com/watch?v=3o63D0-_x2k}',
], thumb='yt/3o63D0-_x2k.jpg', notes='Short video. Programmers are not smarter — they are used to being wrong and trying again.'))

# ───────────────────────── 3 · computers ─────────────────────────
S.append(section('03', 'Computers', 'Turing, 1936',
                 notes='Chapter three. Turing, 1936: On Computable Numbers. Every computer you own '
                       'is one of these machines.'))

S.append(two_col('03 · COMPUTERS', 'Computers are Turing machines', [
    'Turing, 1936 — {muted:On Computable Numbers, with an Application to the Entscheidungsproblem}.',
    '',
    'A tape of symbols, a head that reads one at a time, and a table of rules.',
    '',
    '**Read a symbol. Follow a rule. Write. Move. Repeat.**',
    '',
    '{muted:The machine in the paper is a thought experiment. Turing never built one.}',
], [
    'TAPE   … 1 0 1 1 0 0 …',
    '                ^',
    'HEAD   reads one cell',
    '',
    'RULES  (state, symbol) ->',
    '       (write, move, next state)',
    '',
    'read . rule . write . move',
    'repeat',
], notes='Turing, 1936: On Computable Numbers. Every computer you own is one of these machines. '
         'The photo you usually see is a modern demonstration model in a vitrine; the machine in '
         'the paper is a thought experiment.'))

# ───────────────────────── 4 · programs ─────────────────────────
S.append(section('04', 'Programs', 'Instructions for changing state',
                 notes='Chapter four. A program reads a state, applies instructions, writes a new state.'))

S.append(cards('04 · PROGRAMS', 'Programs are instructions for changing state', [
    ('STATE 0', 'Before', 'A blank canvas, a file, a number.'),
    ('PROGRAM', 'Instructions', 'Step, step, step…'),
    ('STATE 1', 'After', 'A picture, a saved file, a result.'),
], notes='A program reads a state, applies instructions, writes a new state. That is all.'))

S.append(cards('04 · PROGRAMS', 'A program might have…', [
    ('01', 'Inputs', ''),
    ('02', 'Outputs', ''),
    ('03', 'Errors', ''),
    ('04', 'Infinite loops', ''),
], notes='Four things to expect. Infinite loops are not a failure of character — they are a Tuesday.'))

S.append(two_col('04 · PROGRAMS', 'Where are your programs running right now?', [
    'All programs run as **processes** inside your operating system.',
    '',
    '…except for one.',
    '',
    '- **CPU** does the steps',
    '- **RAM** holds what is running',
    '- **Disk** — SSD, HDD — keeps files when the power is off',
], [
    'YOUR COMPUTER',
    '',
    '  process: browser',
    '  process: vscode',
    '  process: python',
    '  ...',
    '',
    '  kernel',
    '',
    '  CPU  RAM  disk',
], right_font='mono', notes='CPU does the steps, RAM holds what is running, disk keeps it when the '
                            'power goes. Every program is a process managed by the OS — except the OS itself.'))

S.append(two_col('04 · PROGRAMS', 'Kernel and shell', [
    'The **kernel** talks to the hardware.',
    '',
    'The **shell** is the layer you talk to.',
    '',
    'A terminal is a shell you type into.',
], [
    'YOU',
    ' |',
    'APPS      TERMINAL',
    ' |            |',
    ' |          SHELL',
    ' |            |',
    '      KERNEL',
    '        |',
    '     hardware',
], notes='Pistachio: the kernel is the nut, the shell is what you touch. A terminal is a shell '
         'you type into.'))

S.append(content('04 · PROGRAMS', 'A terminal', [
    "When you type a program's name, the terminal looks for it inside the folders listed in "
    'the {mono:PATH} variable.',
    '',
    '- PowerShell · Terminal · bash · zsh',
    '',
    '{muted:If it is not in one of those folders: command not found.}',
], image='powershell.png', fit='contain',
   notes="When you type a command, the shell looks in the folders listed in PATH. If it's not "
         'there: command not found.'))

S.append(cards('04 · PROGRAMS', 'Programs that install programs', [
    ('WINDOWS', 'scoop', ['{mono:scoop.sh}', '', '{mono:scoop install git python}']),
    ('MACOS', 'brew', ['{mono:brew.sh}', '', '{mono:brew install git python}']),
], sub='Set one up. It will make your life simpler. In the lab, setup.bat does this for you — see the tutorial.',
   notes='Package managers. Set one up in the tutorial; it saves hours later. On the V915 '
         'machines ait4x/v915-setup does the installing.'))

# ───────────────────────── 5 · programming languages ─────────────────────────
S.append(section('05', 'Programming languages', 'Shared conventions for giving instructions',
                 notes='Chapter five. A language is an agreement about how to write instructions.'))

S.append(cards('05 · PROGRAMMING LANGUAGES', 'Compiled or interpreted', [
    ('COMPILED', 'C, C++, Go, Rust, Zig', [
        'source code → compiler → machine code → run',
        '',
        'Translate everything first. Then run fast, many times.']),
    ('INTERPRETED', 'Python, JavaScript, Ruby', [
        'source code → interpreter reads and runs, line by line',
        '',
        'No separate build step. Slower, but you see results right away.']),
], sub='Hybrid — Java. Transpiled — TypeScript → JavaScript.',
   notes='Compiled: translate the whole thing first, then run. Interpreted: read one line, do it, '
         'next line. Python is interpreted.'))

S.append(two_col('05 · PROGRAMMING LANGUAGES', 'Languages have syntax', [
    '- **Statements**',
    '- **Variables**',
    '- **Operators** and **functions**',
    '- **Keywords** for flow control',
    '',
    '{muted:You will see all four in the first tutorial file.}',
], [
    '# variable',
    'rows = 22',
    '',
    '# operator + function',
    'step = 90 / rows',
    '',
    '# keyword: flow control',
    'for row in range(rows):',
    '    # statement',
    '    draw(row, step * row)',
], notes='Four building blocks. You will see all of them in the first tutorial file.'))

# ───────────────────────── 6 · python ─────────────────────────
S.append(section('06', 'Python', 'A program that interprets text',
                 notes="Chapter six. Python: a program that reads text and executes it, following "
                       "Python's conventions."))

S.append(statement("A program that interprets text and executes the instructions, following Python's conventions.",
                   eyebrow_text='06 · PYTHON', size=84,
                   notes='Python is itself a program. It reads your file as text and does what it says.'))

S.append(cards('06 · PYTHON', 'Python is…', [
    ('01', 'Interpreted', 'No build step. Run it and see.'),
    ('02', 'Dynamically typed', 'A variable can hold a number now and text later.'),
    ('03', 'High-level', 'Close to how you think, far from the hardware.'),
    ('04', 'Indented', 'Spaces decide what belongs to what.'),
    ('05', 'Slower', 'Than C or Rust. Fast enough for us.'),
], notes='Five facts. Indentation is not decoration — it is the grammar.'))

S.append(two_col('06 · PYTHON', '>>> import this', [
    'The Zen of Python, by Tim Peters. Nineteen lines. Here are eight.',
    '',
    '{muted:Type it into any Python and read two or three lines aloud. The console on these '
    'slides will do — press backtick.}',
], [
    'Beautiful is better than ugly.',
    'Explicit is better than implicit.',
    'Simple is better than complex.',
    'Flat is better than nested.',
    'Readability counts.',
    'Errors should never pass silently.',
    'Now is better than never.',
    'If the implementation is hard to',
    "explain, it's a bad idea.",
], right_font='body', right_size=30, notes='Type import this in Python. Read two or three lines aloud.'))

S.append(content('06 · QUICK CHECK · HANDS UP', 'Python reads your code line by line while it runs. Python is…', [
    '- **A** — Compiled',
    '- **B** — Interpreted',
    '- **C** — Transpiled',
], title_size=64, notes='Hands up, not ClassPoint — this one was never run as an activity. Answer: '
                        'interpreted.'))

# ───────────────────────── 7 · tools for the job ─────────────────────────
S.append(section('07', 'Tools for the job', 'Environment · editor · version control',
                 notes='Chapter seven. Three tools: something to run Python, something to edit it, '
                       'something to track changes.'))

S.append(cards('07 · TOOLS FOR THE JOB', 'Three tools', [
    ('01', 'A Python environment', 'Something that runs your code.'),
    ('02', 'A way to edit code', 'Something that shows it to you properly.'),
    ('03', 'A way to track changes', 'Something that remembers every version.'),
], notes='Three tools: something to run Python, something to edit it, something to track changes.'))

S.append(cards('07 · TOOLS · 01 + 02', 'Environment and editor', [
    ('INSTALL PYTHON', 'Many ways. Pick one.', [
        '{mono:python.org/downloads}',
        '{mono:anaconda.com}',
        '{mono:github.com/pyenv/pyenv} · pyenv-win',
        '',
        'or: {mono:scoop} / {mono:brew install python}',
        '',
        '{orange:This year: uv.} It fetches a Python for you.']),
    ('TEXT EDITOR', 'VS Code. The easy choice.', [
        '{mono:code.visualstudio.com}',
        '',
        "The hacker's choice: vim · neovim"]),
], notes='Install Python any way you like; scoop/brew is easiest, and uv — which the setup '
         'script installs — fetches an interpreter on its own. VS Code is the easy editor choice.'))

S.append(content('07 · TOOLS · 03', 'Git and GitHub', [
    '**Git** tracks every change on your computer. {mono:git-scm.com}',
    '',
    '**GitHub** keeps a copy online and lets others see it. {mono:github.com}',
    '',
    '- {mono:github.com/settings/education/benefits} — add your PolyU email first',
    '- {mono:github.com/git-guides}',
    '',
    '{orange:GitHub Education only accepts a PolyU address} — polyu.edu.hk, connect.polyu.hk '
    'and the other school-issued domains.',
], notes='Git tracks changes on your machine. GitHub hosts them online. Register with your '
         'PolyU email for the education benefits.'))

S.append(timeline('07 · TOOLS · HOW GITHUB WORKS', 'Issue → fork → commit → pull request', [
    ('01', 'Issue — say what is wrong', 'A bug, a feature idea, or “I want to help.” Explain how the code should behave.'),
    ('02', 'Fork — your own copy', 'A fork is your version of the repo. It can pull in new changes from the original any time.'),
    ('03', 'Commit — save a change', 'Each commit is a named snapshot. Push it and it is public.'),
    ('04', 'Pull request — ask to merge', 'Propose your commits to the original repo. If accepted, they are merged in.'),
], notes='Found a bug or want a feature? Open an issue. Want to change code? Fork, commit, open a '
         'pull request. Accepted PRs get merged.'))

S.append(statement('github.com/sd5913/pfad', eyebrow_text='A PUBLIC REPO · THE COURSE LIVES ON GITHUB', size=100,
                   notes='Everything for the course lives here. Our organisation is github.com/sd5913. '
                         'Found a bug? Open an issue. Fork it in the tutorial.'))

# ───────────────────────── 8 · assignments and tutorials ─────────────────────────
S.append(section('08', 'Assignments and tutorials', 'Two repos, four rooms',
                 notes='Chapter eight. Assignment 1 now, assignment 2 previewed, then the tutorial.'))

S.append(content('ASSIGNMENT 01 · 5% · DUE SUN 13 SEP, 23:59', 'Why are we here?', [
    '500–1000 words on why you are in this course.',
    '',
    '- A **public GitHub repo**. Not a PDF.',
    '- {mono:README.md} is the essay',
    '- {mono:PROCESS.md} is how you used AI',
    '- Submit the repo URL on Canvas — {mono:canvas.polyu.edu.hk}',
], notes='Due end of week 2. A public repo, not a PDF. README is the essay; PROCESS.md says how '
         'AI was used. Submit the URL on Canvas.'))

S.append(cards('ASSIGNMENT 02 · 10% · WHAT TO EXPECT', 'Data visualisation — two high-level tasks', [
    ('TASK 01', 'Obtain data about a natural phenomenon', ''),
    ('TASK 02', 'Visualise the data you collected', ''),
], notes='Two high-level tasks. Everything else is breaking these down.'))

S.append(timeline('ASSIGNMENT 02 · BREAK IT DOWN', 'Example: tides', [
    ('01', 'Phenomenon', 'Tides in Hong Kong.'),
    ('02', 'Data provider', '{mono:hko.gov.hk/en/tide/ttext.htm}'),
    ('03', 'The problem', 'Find the pattern …inside a web page.'),
    ('04', 'Weeks 2–3', 'Visualise. Art, or design?'),
], notes='Example: Hong Kong tides. Pick a phenomenon, find who publishes the data, then the '
         'real problem: find the pattern in a web page.'))

S.append(timeline('ASSIGNMENT 02 · INPUTS AND OUTPUTS', '“Find the pattern in a web page” — five steps', [
    ('01', 'Get', 'Make an http request. {mono:requests}'),
    ('02', 'Save', 'Write the page to a file, so you ask the server only once.'),
    ('03', 'Parse', 'Read the response as XML and find the pattern. {mono:lxml}'),
    ('04', 'Store', 'Keep the data you found in a clean shape.'),
    ('05', 'Show', 'What data and metadata matter? How is it consumed? What must be validated?'),
], notes='Five steps. Each step has an input and an output. Requests for http, lxml for parsing.'))

S.append(two_col('ASSIGNMENT 02 · STEP 02', 'Save the page', [
    'Check if the file exists. If not, request it and save it. If yes, just read it.',
    '',
    '{muted:This is the first if/else you will write, and it is the reason your script does '
    'not hit the server every time you run it.}',
], [
    'file exists?',
    '',
    '  NO  -> make the http request',
    '         save the file',
    '',
    '  YES -> read the file',
    '',
    'then: parse',
], notes='Caching logic. Check first, then decide. This is the first if/else you will write.'))

S.append(content('ASSIGNMENT 02 · 10% · DUE SUN 27 SEP', 'Data visualisation', [
    'Code committed to a GitHub repo. Submit the URL on Canvas. It should obtain data about a '
    'natural phenomenon and visualise it.',
    '',
    '{orange:Are you a precrastinator? Start here:}',
    '- 1 · Install Python',
    '- 2 · Clone the repo',
    '- 3 · Run the code',
    '- 4 · Make it work for the website you need',
], notes='Precrastinators: install Python, clone the repo, run the code, adapt it to your '
         'website. Due Sun 27 Sep.'))

S.append(question('multiple_choice',
                  'Do you want to leave your current tutorial group and join the 15:30 laptop group instead?',
                  choices=['Yes — I will bring my own laptop', 'No — I stay in my group', "I don't mind either"],
                  eyebrow_text='TUTORIALS · MULTIPLE CHOICE',
                  notes='ClassPoint multiple choice. Only the 15:30 group in V1102 is laptop-based. '
                        'Count the yeses to size the room. Recorded, deliberately not linked: '
                        'tutorial reallocation, not course material.'))

S.append(cards('08 · TUTORIALS', 'Use the tutorials to work on your assignments', [
    ('V915 · PC', '12:30–14:30', 'Gio'),
    ('V915 · PC', '14:30–16:30', 'Nicola'),
    ('V915 · PC', '16:30–18:30', 'Nicola'),
    ('V1102 · YOUR LAPTOP', '15:30–17:30', 'Gio — the laptop group'),
], notes='Four groups. Three on university PCs in V915, one laptop group in V1102.'))

S.append(content('08 · WEEK 1 TUTORIAL GOALS', 'Leave today with…', [
    '- A GitHub account — 2FA on, PolyU email added',
    '- {muted:[Laptop]} git and VS Code installed; git name + email set',
    '- Registered at {mono:pfad.ait4x.org} — student ID matched',
    '- {muted:[Laptop]} A clone of the course repo + Python installed',
    '- {mono:github.com/sd5913/pfad} open, {mono:week01/README.md} read',
    '- **Your own public repo** — the sketch in it, run, two commits pushed',
    '',
    '{muted:You can do every step inside VS Code. The terminal is optional today.}',
], body_size=32, notes='Seven things to leave with today. Everything can be done inside VS Code; '
                       'the terminal is optional.'))

# ───────────────────────── tutorial ─────────────────────────
S.append(section('T', 'Tutorial', 'Sign up · register · run week01 · make your own repo', bg=INK,
                 notes='Tutorial half. Tasks are marked TASK.'))

S.append(two_col('TUTORIAL · GITHUB', 'Your GitHub account is your portfolio', [
    'Every commit in this course shows up on your profile. Put it on your CV.',
    '',
    '{muted:github.com/venetanji}',
], [
    '# github.com/education/students',
    '',
    'if not you.has_account:',
    '    register("student email")',
    'else:',
    '    you.account.add_email(',
    '        "student email")',
], notes='Your commits become your portfolio. Register with the student email for GitHub Education.'))

S.append(cards('[TASK] · DO IT NOW · ONE MINUTE', 'Sign up, then register', [
    ('01 · GITHUB.COM', 'Sign up', [
        'Go to {mono:github.com}. Use your student email.',
        '',
        'Turn on **two-factor authentication** — you will need it.']),
    ('02 · PFAD.AIT4X.ORG', 'Match your work', [
        'Go to {mono:pfad.ait4x.org} and sign in with GitHub. Enter the last 4 digits and the '
        'letter of your PolyU student ID.',
        '',
        '{muted:Public profile only · no password · no access to your repos}']),
], notes='Two tasks now. GitHub with MFA. Then pfad.ait4x.org: sign in with GitHub, enter the '
         'last 4 digits and letter of your student ID. Public profile only.'))

S.append(content('[TASK] · SET UP THE MACHINE', 'One file. Double-click it.', [
    '{orange:github.com/ait4x/v915-setup} → download **setup.bat**, double-click.',
    '',
    '- Installs git, VS Code and uv, then clones the course repo.',
    '- Asks for your name and email — use the ones on your GitHub account.',
    '- Windows will say “Windows protected your PC”: **More info → Run anyway**.',
    '- Safe to run again. Already have the folder? Double-click {mono:setup.bat} inside it.',
    '',
    '{muted:On a Mac: brew install git, then VS Code — week01/README.md has the lines.}',
    '{orange:Lab machine? Double-click signout.bat when you leave} — or the next person pushes as you.',
], body_size=32, notes='The 25-minute install block used to overrun every year. Now it is one '
                       'file from github.com/ait4x/v915-setup. It prompts for the git identity, '
                       'flags the Microsoft Store python stub, and signout.bat clears cached '
                       'logins on a shared machine. Restart VS Code after it finishes.'))

S.append(content('[TASK] · RUN WEEK01', 'VS Code + Copilot in agent mode', [
    '- **Step 1 · Open** — VS Code, sign in with GitHub, open Copilot chat. Choose **Agent**.',
    '- **Step 2 · Clone** — if setup.bat did not: {mono:Can you help me clone '
    'https://github.com/sd5913/pfad and open it?} Or from a terminal: {mono:code pfad}',
    '- **Step 3 · Run and commit** — open {mono:week01/README.md}. Run the sketch. Commit from '
    'the Source Control panel.',
    '',
    '{muted:Works best with Claude as the model.}',
], body_size=32, notes='Open VS Code, sign in with GitHub, open Copilot chat in agent mode. Clone '
                       'the repo if the setup script has not, open the folder, run the sketch.'))

S.append(content('OPTION · NO INSTALL', 'VS Code in Codespaces', [
    "A full VS Code in your browser, running on GitHub's computer. {mono:github.com/codespaces}",
    '',
    '- 1 · Create a codespace',
    '- 2 · Assign it the repo {mono:sd5913/pfad}',
    '- 3 · Work as in VS Code',
    '',
    '{orange:Stop the codespace when you are done} — it uses your free hours.',
], notes='No install needed: a VS Code in the browser. Create a codespace, assign the repo. '
         'Stop it when done — it uses your free hours.'))

S.append(content('[TASK] · YOUR REPO', 'Make your own repo', [
    'You cannot push to a public repo unless you are a collaborator — and being in the org is '
    'read access, not push. To commit code, create **your own new repo**.',
    '',
    'Do it on {mono:github.com} — Copilot cannot do this for you.',
    '',
    '- **github.com** — New repository → public',
    '- **VS Code** — copy the week01 sketch in, run it',
    '- **Source Control** — two commits, pushed',
], body_size=32, notes='You cannot push to the course repo. Make your own on github.com — Copilot '
                       'cannot do this for you — then push your sketch there.'))

S.append(end('See you next week',
             'Want more challenges? Code Schotter, with your own number.',
             SITE, notes='Want more? Code Schotter with your own number. See you next week.'))

# Links each question slide to the answers the room gave on 2026-09-03. Five activities,
# in the order they ran; the tutorial poll is recorded but withheld.
attach_reports(S, Path(__file__).resolve().parent / 'week01-reports.json')

DECK = {'title': f'{COURSE} · Week 1 — Programming for artists and designers',
        'pdf': f'{COURSE}-week01.pdf', 'slides': S}
