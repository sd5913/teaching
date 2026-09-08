"""
SD5913 · Week 02 — Reading code.

    deckgen build --pptx        # export/ only, no node needed
    deckgen build               # everything, as the workflows run it

Sources this is built from, all in the admin workspace ~/dev/sd5913:

  docs/course-plan-2026.md   — the reframe: no longer "learn to write Python" but
                               "learn to read Python well enough to tell whether what
                               you were handed is right". Types, control flow, data
                               structures, uv. Workshop: reading and breaking code
                               that already works.
  docs/deck-review/weeks-02-04.md — the 2025 deck was 94 slides, ~60% screenshots, and
                               ~45 slides across weeks 2–4 re-taught the same syntax.
                               The review says collapse to ~8 slides of "things that
                               surprise you" and keep s30 (float equality), s36–37
                               (mutable vs immutable) and s76 (project naming).
  archive/SD5913-week01.pptx — what the room actually got in week 1.

Deliberately NOT here, because week 1 2026 already covered it (archive deck s24–38):
Turing machines, kernel and shell, the terminal, PATH, package managers, compiled vs
interpreted, syntax, "Python is a program that interprets text". Do not re-teach it —
re-teaching is the single biggest failure of the 2025 decks.

Also deliberately not here: the 2025 s42 claims. Function bodies are indented FOUR
spaces (PEP 8), and Python does NOT automatically return the last statement. That slide
was wrong in 2025 and was repeated in week 3; it is not coming back.

Section 02, "Design the mark", is ported from archive/SD5913-week01.pptx slides 53–57,
where it was written but never run — the room ran out of time. Its wording is carried
over, not rewritten.
"""
from pathlib import Path

from deckgen import attach_reports, INK, PAPER
from deckgen.layouts import (title, agenda, section, statement, content, cards,
                             question, two_col, activity, timeline, exercise,
                             code_panel, end)

COURSE = 'SD5913'
SITE = 'sd5913.github.io/teaching'
REPO = 'github.com/sd5913/pfad'
EYE = 'SD5913 · WEEK 02'

S = []

# ───────────────────────── 0 · landing ─────────────────────────
S.append(title(EYE, 'Reading code',
               'You will be handed code you did not write.'))

S.append(agenda(EYE, [
    'Loose ends from week 1',
    'Design the mark — week 1 ran out of time',
    'Reading, not writing',
    'Six types, on your laptop',
    'Reading code that does something',
    'Five things that will surprise you',
    'uv: one command, every dependency',
    'Workshop — predict, break, fix',
]))

# ───────────────────────── 1 · loose ends ─────────────────────────
S.append(section('01', 'Loose ends', 'Where week 1 left off'))

S.append(content('01 · LOOSE ENDS', 'Three things from last week', [
    '- The **org invitation** is in the email you signed up to GitHub with. '
    'It {orange:expires after seven days} — accept it even if you do nothing else.',
    '- Being in the org is {bold:not} push access. Assignment 1 lives on '
    '**your own account**, which is why it does not matter yet.',
    '- Not registered at {mono:pfad.ait4x.org}? Do it now. Nothing is marked until '
    'your student ID and your GitHub username are the same row.',
], notes='Ask for hands: who has NOT accepted. Expect a third of the room. Anyone whose '
         'invitation expired — take the username, re-invite after class.'))

S.append(question('short_answer', 'What broke for you last week?',
                  hint='One line. Git, the terminal, VS Code, the registry — anything.',
                  notes='Two minutes, no more. Triage, not discussion. Read three out '
                        'loud and fix them live if they are quick.'))

# ───────────── 2 · Design the mark — from week 1, slides 53–57 ─────────────
S.append(section('02', 'Design the mark', 'Eight minutes, no software'))

S.append(activity('1 — ALONE', 1, 'Name one thing it could be built from.', [
    'This course needs a mark — a logo, the thing on the repo and at the top of the '
    'slides. {bold:You are the client.}',
    '',
    '**Silent. Pen and paper.** A thing you could point at: an object, a shape, a tool. '
    'Not an adjective — you cannot draw {muted:“innovative”}.',
    '',
    '{muted:e.g. a cursor that is also a pencil · a grid coming apart at one corner · '
    'two square brackets facing each other}',
], eyebrow_text='DESIGN THE MARK',
   notes='One minute, silent, paper. One concrete object the course mark could be built '
         'from. Not an adjective.'))

S.append(activity('2 — IN PAIRS', 2, 'Two answers in. One answer out.', [
    'Turn to your neighbour. Read each other your object. Leave with {orange:one} object '
    '— not two, not a mix of two.',
    '',
    'Keep one, or build a third thing from both. **You may not keep both.**',
    '',
    "Whoever's object gets dropped says in one line what was good about it. "
    'Write that down too.',
], eyebrow_text='DESIGN THE MARK',
   notes="Two minutes in pairs. Two answers in, one out. The dropped idea's owner says "
         'in one line what was good about it.'))

S.append(activity('4 — TWO PAIRS', 4, 'Now it has to survive 16 pixels.', [
    'Join the pair behind you. Four people, one object. It must work at {orange:16 px wide} '
    '— the favicon on your repo, the avatar next to your name.',
    '',
    'At 16 px you get one shape and one idea. Detail disappears. Decide what survives: '
    '{mono:“ours is a ___, and at 16px you can still tell, because ___.”}',
    '',
    'Then one line of anti-brief: the one thing it must **never** look like.',
], eyebrow_text='DESIGN THE MARK',
   notes='Four minutes in fours. The twist: it must work at 16 pixels — the favicon and '
         'the GitHub avatar. One person writes.'))

S.append(question('short_answer', 'Scribes only. One line per four.',
                  eyebrow_text='DESIGN THE MARK · CAPTURE · 2 MIN · SHORT ANSWER',
                  hint='OBJECT — what survives at 16px — never: ___',
                  example='e.g. “A grid with one tile falling out — the gap where the '
                          'tile was — never: a gear.”',
                  notes='ClassPoint short answer. Scribes only, one line per four — about '
                        '28 lines, not 112. These go into a design tool on the projector.'))

S.append(content('DESIGN THE MARK · WHAT JUST HAPPENED', 'That was a design brief.', [
    'Eight minutes, no software. The room now agrees on an object, what survives at '
    '16 pixels, and one thing it must never be. Everything after this — drawing, '
    'variations, file formats — is {muted:craft}.',
    '',
    '{orange:A machine can draw it. It cannot decide it.}',
], bg=INK, notes='The payoff. Do not rush it — this is the argument for the whole course, '
                 'and the last thing they should remember from the activity.'))

# ───────────────────────── 3 · the shift ─────────────────────────
S.append(section('03', 'Reading, not writing', 'The shift'))

S.append(statement('You will not memorise the syntax.\nYou will learn to check it.',
                   eyebrow_text='03 · THE SHIFT'))

S.append(content('03 · THE SHIFT', 'Three questions, all semester', [
    'Every exercise this week is one of these, and so is every quiz question:',
    '',
    '- Here is code that runs. **What does it print?**',
    '- Here is code that is wrong. **Where?**',
    '- Here is a spec and some code. **Does the code meet it?**',
    '',
    '{muted:None of them ask you to write a program from a blank file. That comes later, '
    'and by then you will be able to tell whether what you wrote is right.}',
], notes='Land this hard — the room expects a syntax lecture and it is not one. The '
         'reason: they will be handed generated code all semester, and verification is '
         'the only defensible skill left.'))

S.append(content('03 · YOUR LAPTOP', 'Open the slides on your laptop', [
    'Everything from here has a box you can type in. **The Python runs in your browser** — '
    'nothing to install, nothing to hand in.',
    '',
    '- {orange:' + SITE + '/week02/}',
    '- Press {mono:Run}, or {mono:ctrl+enter}.',
    '- Backtick ({mono:`}) opens a console on any slide.',
    '',
    '{muted:Your answers are saved in the browser, so a reload does not lose them.}',
], notes='Put the URL on the board and leave it there. First Run downloads ~12 MB, so it '
         'takes a few seconds — say that out loud or they will think it has hung. If the '
         'room wifi dies, every exercise is still readable on the slide.'))


# ───────────── 4 · six types — the on-ramp week 1 never gave them ─────────────
# Week 1 taught no Python mechanics at all: no print, no variables, no types, no REPL
# (checked against archive/SD5913-week01.pptx — s34 shows a Python-looking snippet to
# illustrate what "syntax" means, s36 states in passing that Python is dynamically
# typed, and that is the lot). Going straight from there to reading a list of dicts is
# a cliff. Five one-liners first, each one thing, each with a green tick at the end.
# Ported from the 2025 python_foundations notebooks rather than from the 2025 slides,
# which are screenshots.

S.append(section('04', 'Six types', 'Everything you will be handed is one of these'))

S.append(code_panel('04 · TYPES', 'Six types, and that is most of it', [
    '3             int      a whole number',
    '3.14          float    a number with a decimal point',
    '"3"           str      text. The quotes are what make it text',
    'True          bool     yes or no',
    '[3, 1, 4]     list     several things, in order',
    '{"n": 3}      dict     values you look up by name',
], caption='You will meet tuple and set later. These six carry the whole course.',
   notes='Two minutes, no more. Do not explain each one — the drills do that. The only '
         'line worth saying out loud is the third: "3" and 3 are different things, and '
         'every type bug a student hits this semester is a version of that.'))

S.append(exercise('04 · ONE-LINER 01', 'Does the box work?', [
    'Press {mono:Run}. That is the whole exercise.',
    '',
    '{muted:The first run downloads Python into your browser, so give it a few seconds. '
    'After that it is instant.}',
], code='print("hello")',
   expect='hello',
   hint='just press Run',
   notes='Deliberately free. It passes on the first press, everyone sees a green tick, '
         'and the ~12 MB Pyodide download happens here rather than in the middle of a '
         'drill that has actual thinking in it. Say the download out loud or the room '
         'will think it has hung. Hands up for anyone who did NOT go green — fix those '
         'now, because every slide after this needs it.'))

S.append(exercise('04 · ONE-LINER 02', 'Ask Python what it is', [
    '{mono:type(x)} tells you what kind of thing {mono:x} is. You will use it all '
    'semester to check what an agent actually handed you.',
    '',
    'Predict the three lines, then add a fourth for an {bold:empty list}.',
], code='print(type(3))\n'
        'print(type(3.14))\n'
        'print(type("3"))\n'
        '# add a line that prints the type of an empty list',
   expect="<class 'int'>\n<class 'float'>\n<class 'str'>\n<class 'list'>",
   hint='type([])',
   notes='Make them predict line 3 before running — a good number of the room will say '
         "int. It is str, because of the quotes. That single fact is the next drill and "
         'half of the type errors they will hit all year.'))

S.append(exercise('04 · ONE-LINER 03', 'The quotes change the answer', [
    '{mono:+} means add for numbers and {bold:join} for text. Same symbol, two jobs, and '
    'Python picks by type — not by what you meant.',
    '',
    'Make it print {mono:12} rather than {mono:66}.',
], code='a = "6"\n'
        'b = "6"\n\n'
        'print(a + b)',
   expect='12',
   hint='int(a)',
   notes='The canonical one. Ask what it prints before running — the room says 12, it '
         'says 66. Nothing is broken and nothing errors; the code just quietly did the '
         'other job. This is what "verify what you were handed" means in practice, and '
         'it is why every scraped number needs int() or float() before it is arithmetic.'))

S.append(exercise('04 · ONE-LINER 04', 'Everything is looked up the same way', [
    'Square brackets ask a str, a list and a dict the same question: {bold:give me the '
    'one at ___}. Positions count from {mono:0}; {mono:-1} is the last.',
    '',
    'Add the two missing lines — the {bold:last} colour, and the year.',
], code='word = "design"\n'
        'colours = ["red", "green", "blue"]\n'
        'student = {"name": "Ada", "year": 2026}\n\n'
        'print(len(word))\n'
        'print(word[0])\n'
        'print(student["name"])\n'
        '# the last colour, then the year',
   expect='6\nd\nAda\nblue\n2026',
   hint='colours[-1] and student["year"]',
   notes='Two things land here. One: a dict is looked up by name, not by position, which '
         'is exactly what the reading exercise on the next slide does with r["year"]. '
         'Two: len() works on all three. Someone will try colours[3] and get an '
         'IndexError — good, read it together, it names the line.'))

S.append(exercise('04 · ONE-LINER 05', 'Put a value inside a sentence', [
    'An {mono:f} before the quotes lets you drop a value into the text with '
    '{mono:\u007b\u007d}. This is how every label, caption and error message you write '
    'gets made.',
    '',
    'Make it print {mono:Ada is 36}.',
], code='name = "Ada"\n'
        'years = 36\n\n'
        'print("...")',
   expect='Ada is 36',
   hint='f"{name} is {years}"',
   notes='Show the failure first: print("name is years") prints the words. The f is the '
         'whole trick. Worth saying that string formatting is the single most common '
         'thing they will ask an agent for, so recognising it matters more than recalling '
         'the syntax.'))

S.append(content('04 · TYPES', 'That is the syntax, and it is over', [
    'Five lines, five minutes, and you can now read most of what you will be handed.',
    '',
    'What is left is not more syntax. It is {orange:noticing when the type is not the '
    'one you assumed} — which is the next hour, and the rest of the semester.',
    '',
    '{muted:The console is always there: press backtick (}{mono:`}{muted:) on any slide '
    'and type into it. Every drill has a }{mono:\u203a_}{muted: button that loads it in.}',
], bg=INK, notes='Close the section fast. The point of the last line is that they now '
                 'have a scratchpad — tell them to use it during the reading exercises '
                 'rather than guessing.'))

# ───────────── 5 · reading code that does something ─────────────
S.append(section('05', 'Reading code', 'Now with all six types in one function'))

S.append(two_col('05 · READING', 'Read it out loud', [
    'Reading code is a skill you practise, not a thing you know.',
    '',
    '- Start at the **bottom**: what does it return?',
    '- Then the signature: what does it take?',
    '- Only then the middle.',
    '',
    'Say the types out loud as you go. "A list of dicts, each with a year and a height."',
], [
    'def mean_height(rows, year):',
    '    out = []',
    '    for r in rows:',
    '        if r["year"] == year:',
    '            out.append(r["height"])',
    '    return sum(out) / len(out)',
]))

S.append(question('multiple_choice', 'What does it do for a year with no rows?',
                  choices=['Returns 0', 'Returns None', 'Raises ZeroDivisionError',
                           'Returns an empty list'],
                  notes='C. len(out) is 0. This is the whole week in one slide: the code '
                        'does not look wrong, it is wrong for an input nobody tried. Ask '
                        'who would have shipped it.'))

S.append(exercise('05 · READ IT', 'Run it and see', [
    'This is the function from the last slide, with a year that has no rows.',
    '',
    'Predict what happens {bold:before} you press Run.',
], code='rows = [{"year": 2024, "height": 2.1},\n'
        '        {"year": 2024, "height": 2.5}]\n\n'
        'def mean_height(rows, year):\n'
        '    out = []\n'
        '    for r in rows:\n'
        '        if r["year"] == year:\n'
        '            out.append(r["height"])\n'
        '    return sum(out) / len(out)\n\n'
        'print(mean_height(rows, 2025))',
   hint='predict first, then run',
   notes='Let them run it and hit the ZeroDivisionError themselves. The error message names '
         'the line — read it together. This is the first time most of them have read a '
         'traceback on purpose.'))

S.append(exercise('05 · FIX IT', 'Now make it survive', [
    'Give it something sensible when there are no rows for that year.',
    '',
    'It should print {mono:None} rather than raising.',
], code='rows = [{"year": 2024, "height": 2.1}]\n\n'
        'def mean_height(rows, year):\n'
        '    out = [r["height"] for r in rows if r["year"] == year]\n'
        '    # your line here\n'
        '    return sum(out) / len(out)\n\n'
        'print(mean_height(rows, 2025))',
   expect='None',
   hint='one line, before the return',
   notes='Most will write `if not out: return None`. Some will write `if len(out) == 0:` — '
         'both are right, and the difference is exactly the truthiness exercise later. '
         'Nobody needs to have memorised anything to do this.'))

# ───────── 6 · the surprises (2025 s30, s36–37, collapsed per the deck review) ─────────
S.append(section('06', 'Five things that will surprise you', 'The parts that bite'))

S.append(question('multiple_choice', 'What is the output of 0.1 + 0.1 + 0.1 == 0.3 ?',
                  choices=['True', 'False'],
                  eyebrow_text='06 · SURPRISE 01 · NUMBERS',
                  notes='B — False. Binary floating point cannot represent 0.1 exactly, '
                        'so the sum is 0.30000000000000004. Carried over from 2025 s30, '
                        'which the deck review calls a verification lesson disguised as '
                        'trivia. Never compare floats with ==; compare a difference '
                        'against a tolerance.'))

S.append(cards('06 · SURPRISES', 'The five that actually bite', [
    ('01 · NUMBERS', 'Floats are not decimals',
     '{mono:0.1+0.1+0.1 != 0.3}. Compare a difference against a tolerance, never with =='),
    ('02 · ALIASING', 'Two names, one list',
     'Immutable — int, float, bool, str, tuple — copies on assignment. Mutable — list, '
     'dict, set — copies the reference. Change one name, the other changes.'),
    ('03 · TRUTHINESS', 'Empty is False',
     '{mono:[]}, {mono:{}}, {mono:""}, {mono:0} and {mono:None} are all falsy. '
     '{mono:if rows:} and {mono:if rows is not None:} are different questions.'),
    ('04 · DEFAULTS', 'The list that remembers',
     '{mono:def f(x, seen=[]):} — the default is built once, at definition, and every '
     'call shares it.'),
    ('05 · INDENTATION', 'The shape is the logic',
     '**Four** spaces, and Python does {bold:not} return the last statement — a function '
     'with no {mono:return} gives you {mono:None}.'),
], notes='Card 5 corrects two errors that were on 2025 week 2 slide 42 and repeated in '
         'week 3: it said two spaces, and it said Python returns the last statement '
         'automatically. Both wrong. Say so — being wrong in public about your own '
         'material is the best possible demonstration of why you verify.'))

S.append(exercise('06 · DRILL 01 · NUMBERS', 'Make the comparison true', [
    'Floats are stored in binary, and 0.1 has no exact binary form — so the sum is '
    '{mono:0.30000000000000004}.',
    '',
    'Compare a **difference against a tolerance** instead.',
], code='total = 0.1 + 0.1 + 0.1\n\n'
        '# change this line so it prints True\n'
        'print(total == 0.3)',
   expect='True',
   hint='abs(a - b) < 1e-9',
   notes='The point is not the trick, it is that == on floats is a question about '
         'representation, not about maths. Ask what else in the course is a float — every '
         'coordinate, every tide height.'))

S.append(exercise('06 · DRILL 02 · ALIASING', 'Stop the aliasing', [
    '{mono:b = a} does not copy the list. It gives the same list a second name, so '
    'appending through one shows up in the other.',
    '',
    'Make {mono:a} print unchanged.',
], code='a = [1, 2, 3]\n'
        'b = a\n'
        'b.append(4)\n\n'
        'print(a)',
   expect='[1, 2, 3]',
   hint='a.copy() or list(a)',
   notes='This is the bug an agent writes and you cannot see in a diff. Immutable things — '
         'int, float, bool, str, tuple — copy on assignment; mutable ones — list, dict, set '
         '— do not. Carried from 2025 week 2 s36-37, which the deck review says to keep.'))

S.append(exercise('06 · DRILL 03 · TRUTHINESS', 'Two different questions', [
    '{mono:[]}, {mono:0}, {mono:""} and {mono:None} are all falsy, so '
    '{mono:if rows:} and {mono:if rows is not None:} do {bold:not} ask the same thing.',
    '',
    'An empty list is a real answer. Missing data is not. Make it tell them apart.',
], code='def describe(rows):\n'
        '    if rows:\n'
        '        return "got data"\n'
        '    return "no data"\n\n'
        'print(describe([1, 2]))\n'
        'print(describe([]))\n'
        'print(describe(None))',
   expect='got data\nempty\nmissing',
   hint='empty list -> "empty", None -> "missing"',
   notes='Three lines out: "got data", "empty", "missing". They have to check None '
         'explicitly and before the truthiness test. This is the distinction that makes '
         'the fix in the reading exercise correct rather than lucky.'))

S.append(exercise('06 · DRILL 04 · DEFAULTS', 'The list that remembers', [
    'A default argument is built {bold:once}, when the function is defined — not on each '
    'call. Every call then shares the same list.',
    '',
    'Make the second call print one item, not two.',
], code='def collect(item, seen=[]):\n'
        '    seen.append(item)\n'
        '    return seen\n\n'
        'print(collect("a"))\n'
        'print(collect("b"))',
   expect="['a']\n['b']",
   hint='default to None, build inside',
   notes='The fix is `seen=None` then `if seen is None: seen = []`. Which is drill 03 again, '
         'used for real. Say that — the drills are not five unrelated facts.'))

S.append(exercise('06 · DRILL 05 · RETURN', 'It gives you None', [
    'Python does {bold:not} return the last statement. A function with no {mono:return} '
    'hands back {mono:None}, silently.',
    '',
    '{muted:Last year this course told you otherwise, on a slide, twice. It was wrong.}',
], code='def double(x):\n'
        '    x * 2\n\n'
        'print(double(21))',
   expect='42',
   hint='one word',
   notes='This corrects 2025 week 2 s42, repeated as week 3 s13, which claimed Python '
         'automatically returns the last statement and that bodies are indented two spaces '
         '(PEP 8 says four). Own it out loud — being publicly wrong about your own material '
         'is the best argument for verifying that you will ever get.'))

# ───────────────────────── 7 · uv ─────────────────────────
S.append(section('07', 'uv', 'One command, every dependency'))

S.append(content('07 · UV', 'Why your code runs and theirs does not', [
    'Last year, {orange:every single week} of this course shipped a {mono:requirements.txt} '
    'that was missing something. Week 2 was missing matplotlib, drawsvg and pandas — so two '
    'of five scripts broke {bold:after} you followed the install instructions.',
    '',
    'The code was fine. The environment was never written down.',
    '',
    '- {mono:uv run script.py} — runs it in its own environment, installing what it needs',
    '- {mono:uv add pandas} — records the dependency where the next person will find it',
    '- {mono:uv sync} — makes your machine match the file',
], notes='Be honest that this is a fix for a real failure in last year\'s course — it '
         'lands far better as "here is what went wrong" than as a tool tour. uv replaces '
         'the pip + virtualenv block from 2025 s52–54 entirely.'))

S.append(statement('A repo that does not say what it needs\nis not finished.',
                   eyebrow_text='07 · UV', size=100))

# ───────────────────────── 8 · workshop ─────────────────────────
S.append(section('08', 'Workshop', 'Predict, break, fix'))

S.append(timeline('08 · WORKSHOP', 'Two hours', [
    ('0:00', 'Pull week 2', f'{{mono:git pull}} in your clone of {REPO}'),
    ('0:15', 'The rest of the drills', 'Same shape as the five you just did, on your own machine with uv.'),
    ('0:50', 'Find the fault', 'Four programs that run and are wrong.'),
    ('1:20', 'Meet the spec', 'A brief and three candidate solutions. Which one is right?'),
    ('1:45', 'Commit and push', 'Your answers, as a markdown file, in your own repo.'),
], notes='The drills in the slides are 30 seconds each and prove the idea. The tutorial is '
         'where they do it on their own machine, in a repo, with uv — which is the thing '
         'that has to work in the exam and in assignment 2.'))

S.append(content('08 · WORKSHOP', 'Name it properly while you are here', [
    'Assignment 2 is set next week and it lives in a repo with your name on it. '
    'The name is the first thing anyone sees.',
    '',
    '- {muted:Bad:} {mono:assignment2} · {mono:ass2} · {mono:asdgjfjdj}',
    '- {orange:Good:} {mono:tidal-spiral} · {mono:rainmaps-sz}',
    '',
    'Short, lowercase, easy to type, and it says what the thing does. '
    'This repo is in your portfolio for longer than it is in my gradebook.',
], notes='Carried from 2025 s76, which the deck review flags as worth keeping. Landing it '
         'in week 2 rather than week 3 means they name it before they start.'))

S.append(question('image_upload', 'Push your answers, then screenshot the green tick.',
                  notes='The upload is the attendance signal and the "it actually worked" '
                        'signal in one. Anyone who cannot push is still stuck on week 1 — '
                        'deal with them at the back of the room.'))

S.append(end('See you next week',
             'Week 3: getting data, and making it look like something. Assignment 2 is set.',
             SITE))

# Links each question slide to the answers the room gave. Written after the class by
# classpoint.py's weekly.py, and a no-op until that file exists.
attach_reports(S, Path(__file__).resolve().parent / 'week02-reports.json')

DECK = {'title': f'{COURSE} · Week 2 — Reading code', 'pdf': f'{COURSE}-week02.pdf', 'slides': S}
