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

Section 05, "Reading a rule", is the Frieder Nake challenge from the 2025 deck (s9, s93),
answered with the model script pfad kept on the 2025 branch at extra/nake/main.py. It
replaced a list-of-dicts reading exercise that was a programmer's example, not a
designer's: the rule has a picture, and the picture is the test.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import figures as F                                   # noqa: E402
from deckgen import attach_reports, INK, PAPER, WHITE  # noqa: E402
from deckgen.layouts import (title, agenda, section, statement, content, cards,   # noqa: E402
                             question, two_col, activity, timeline, exercise,
                             code_panel, image_full, live, end)

COURSE = 'SD5913'
SITE = 'sd5913.github.io/teaching'
REPO = 'github.com/sd5913/pfad'
EYE = 'SD5913 · WEEK 02'

S = []

# ───────────────────────── 0 · landing ─────────────────────────
S.append(title(EYE, 'Reading code',
               'You will be handed code you did not write.'))

S.append(agenda(EYE, [
    'Assignment 1: two files, and until Sunday',
    'Design the mark — week 1 ran out of time',
    'Reading, not writing',
    'Six types, on your laptop',
    'Reading a rule: Nake, 1966',
    'Four things that will surprise you',
    'uv: one command, every dependency',
    'Workshop — predict, break, fix',
]))

# ───────────────────────── 1 · loose ends ─────────────────────────
# Written against the first 25 assignment-1 repos on Canvas (checked 2026-09-09 with
# ~/dev/sd5913/scripts/check_submissions.py). Counts only — no repo, name or username
# from that check belongs in a public deck, and none is here.
S.append(section('01', 'Loose ends', 'One address, two files, until Sunday'))

S.append(content('01 · ONE ADDRESS', 'pfad.ait4x.org has everything', [
    'The slides, the course repo, the org and the lab setup are at the bottom of that page — '
    '**no sign-in needed**. Bookmark it; it is the one address to remember.',
    '',
    '- Sign in and you get a **dashboard**: what Canvas received for each assignment, and '
    'whether that repo is on the account you registered. {orange:A mismatch is flagged '
    'there, with what to do about it.}',
    '- The **org invitation** goes to accounts whose submission matches. It comes by email '
    'and {bold:expires after seven days} — accept it when it arrives.',
    '- Not registered? Do it now, from the account you push with.',
], notes='Put the address on the board. The links are public; the dashboard is per student '
         'and shows the Canvas URL against the registered login. "I never got the invitation" '
         'usually means the repo is on a different account than the one they registered — the '
         'dashboard says so. Being in the org is still not push access.'))

S.append(two_col('01 · ASSIGNMENT 1', 'A finished repo is two files', [
    '**README.md** is the essay. 500–1000 words, headings, links that work, '
    'a {bold:References} heading at the bottom with APA entries.',
    '',
    '**PROCESS.md** is how you used AI: the tools, one thing kept and why, one thing '
    'rejected and why. {muted:“I used none” is a fine PROCESS.md, in one sentence.}',
    '',
    'Public, on **the account you registered**, with a history that shows the essay '
    'was written: several commits, more than one day, messages that say what changed.',
], [
    'why-are-we-here/',
    '├── README.md     the essay',
    '└── PROCESS.md    how you used AI',
    '',
    '$ git log --oneline',
    'e4f1c0a  Add references',
    'b72d9e1  Cut 200 words from the middle',
    '9c0a5d2  Second draft: one example',
    '51ab3f8  First draft',
    '0d3e7aa  Initial commit',
], lang=None, right_size=26, left_size=30,
   notes='Two files at the top level, those exact names. Everything else on the right is '
         'what a history looks like when the essay was written rather than pasted: five '
         'commits, three of them with a verb in them. The Schotter repo from the tutorial '
         'is a different repo — it stays where it is.'))

S.append(content('01 · THE FIRST 25', 'What has come in so far', [
    'Of the first 25 repos on Canvas: **14 are essays**, 4 are essays missing one thing, '
    'and **7 are not the assignment** — the Schotter repo from the tutorial, an empty '
    'README, or the week 1 folder copied in, {mono:.DS_Store} included.',
    '',
    '- {muted:Not so good:} one commit called {mono:Initial commit}, or ten commits in twenty minutes',
    '- {muted:Not so good:} a {mono:PROCESS.md} that is empty, in a subfolder, or says {mono:?}',
    '- {muted:Not so good:} an outline with the {mono:[ write your example here ]} prompts still in it',
    '- {orange:Good:} seventeen commits over four days, each saying what changed',
    '- {orange:Good:} a {mono:PROCESS.md} that names the paragraph it threw away, and why',
], notes='Patterns, not people — do not name anyone, and do not open a repo on the '
         'projector. Everyone in the room can place themselves in one of the three groups, '
         'and the next slide tells them what to do about it.'))

S.append(content('01 · UNTIL SUNDAY', 'You can still fix it', [
    'Deadline **Sunday 13 September, 23:59**. Nothing is marked before then, and the URL '
    'on Canvas keeps working — push to the same repo and it is fixed.',
    '',
    '- Wrong repo? Make the right one and **resubmit the URL** on Canvas. Attempts are unlimited.',
    '- Essay done, no {mono:PROCESS.md}? Add it — top level, that exact name.',
    '- Everything in one commit? Too late to undo, not too late to add: every edit this '
    'week is a commit with a message.',
    '- Pushed from an account other than the one you registered? Your dashboard at '
    '{mono:pfad.ait4x.org} flags it — fix the registration, or resubmit the right URL.',
], bg=INK, notes='The point of showing the first 25 is that there are four days left. The '
                 'check runs again after the deadline; what it finds then is what gets marked.'))

S.append(two_col('01 · CHECK IT', 'Ask a script whether it meets the spec', [
    'The whole course in one command: a spec, a repo, and a program that says whether '
    'one meets the other. Run it **inside your assignment repo**.',
    '',
    'It checks what a script can check — two files, the word count, a References '
    'heading, a {mono:PROCESS.md} that says something, a history over more than one '
    'sitting. {muted:Whether the essay is good is still a person\'s call.}',
    '',
    'Copy {mono:assignments/check.yml} into your repo as {mono:.github/workflows/check.yml} '
    'and GitHub runs it on every push: {orange:a green tick, or a red cross.}',
], [
    '$ uv run https://raw.githubusercontent.com/',
    '        sd5913/pfad/2026/assignments/check.py',
    '',
    'Assignment 1 — why-are-we-here',
    '',
    '  ok    README.md: 820 words',
    '  FAIL  README.md has no References heading',
    '  FAIL  PROCESS.md is empty',
    '  ok    12 commits over 3 days',
    '  ok    just the files that belong',
    '',
    '2 thing(s) to fix. Push again when you have.',
], lang=None, right_size=24, left_size=30,
   notes='Do this live on the projector with the test account\'s repo: run the check, read '
         'the list, fix one thing, push, and show the Actions tab turn green. It is the '
         '"does the code meet the spec" question from section 03, pointed at their own '
         'work — and the green tick at the end of the workshop is this same workflow.'))

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
   notes='Two things land here. One: a dict is looked up by name and a list by position — '
         'grid[w][h] in the Nake rule is two list lookups in a row. '
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

# ───────────── 5 · reading a rule — Nake, 1966, from pfad's 2025 extra/nake/main.py ─────────────
# The 2025 deck asked this on s9 and s93 and never answered it: "What is the pattern? What
# combination never occurs? How do you draw progressively and ensure this condition?" The
# model answer, 25 lines that print the picture as characters, sat in extra/nake/main.py
# and no slide referenced it. Both the deck review and docs/week02-lesson-plan.md say to
# build the reading around it, because it is the three exercise shapes with a picture as
# the test: predict what the rule draws, find the line that forbids a combination, decide
# whether a rewrite still meets that spec. The algorithm is the 2025 script's, line for
# line; what changed for the slide: the two conditions are called bar and cap (as on the
# reading slide, and so the lines fit the panel), the cap is a macron (¯) rather than
# U+23B4, which the browser's mono font lacks, and size is 24 so a row fits the output
# pane without wrapping. The verbatim file stays in pfad for the tutorial.

NAKE = '''import random
size = 24
grid = []
last_square_empty = False
for w in range(size):
    grid.append([])
    for h in range(size):
        bar = random.randint(0, size - 2) >= abs(w - h)
        cap = (random.randint(0, size) > 0.2 * size
               and last_square_empty)
        grid[w].append((bar, cap))
        if bar or cap:
            last_square_empty = False
        else:
            last_square_empty = True

for h in range(size):
    for w in range(size):
        print("|" if grid[w][h][0] else " ", end="")
        print("¯" if grid[w][h][1] else " ", end="")
    print()'''

NAKE_JS = '''let seed = 1966, hProb = 0.2;
const n = 30;

function setup() {
  createCanvas(600, 600);
  stroke(20); strokeWeight(1.6);
  noLoop();
}

function draw() {
  background('#faf8f4');
  randomSeed(seed);
  const g = width / (n + 2);
  let lastEmpty = false;
  for (let w = 0; w < n; w++) {
    for (let h = 0; h < n; h++) {
      const x = (w + 1) * g, y = (h + 1) * g;
      const bar = floor(random(n - 1)) >= abs(w - h);
      const cap = random() > hProb && lastEmpty;
      if (bar) line(x, y, x, y + g);
      if (cap) line(x, y, x + g, y);
      lastEmpty = !(bar || cap);
    }
  }
}'''
NAKE_EXTRA = '''function mouseMoved() { hProb = constrain(mouseX / width, 0, 1); redraw(); }
function mousePressed() { seed = floor(random(1000000)); redraw(); }'''

S.append(section('05', 'Reading a rule', 'Nake, 1966 · the picture is the test'))

S.append(image_full('nake-walk-through-raster-1966.jpg', '05 · FRIEDER NAKE · WALK-THROUGH-RASTER · 1966',
                    'Week 1 showed you this and asked whether a program can make art. Here is the program. '
                    'Twenty-five lines. You are going to read them.',
                    fit='contain', bg=WHITE,
                    notes='Callback to week 1 s11. Last year this deck asked "what is the pattern? what '
                          'combination never occurs?" on the last slide and never answered it. Today the '
                          'room answers it by reading the rule.'))

S.append(two_col('05 · READING', 'Read it out loud', [
    'Reading code is a skill you practise, not a thing you know.',
    '',
    '- Start at the **bottom**: what does it print?',
    '- Then the loops: what is {mono:w}, what is {mono:h}, which one moves faster?',
    '- Only then the two conditions.',
    '',
    'Say the types as you go. "A list of columns. Each column is a list. Each cell is a '
    'pair of booleans."',
], [
    'for w in range(size):        # columns',
    '    for h in range(size):    # rows, top down',
    '        bar = (random.randint(0, size - 2)',
    '               >= abs(w - h))',
    '        cap = (random.randint(0, size)',
    '               > 0.2 * size',
    '               and last_square_empty)',
    '        grid[w].append((bar, cap))',
    '        if bar or cap:',
    '            last_square_empty = False',
    '        else:',
    '            last_square_empty = True',
], right_size=22, notes='The two conditions, and the state carried between cells. Ask what '
                        'last_square_empty was last set by: the cell above, because h is the inner loop. '
                        'That single fact is the next four slides.'))

S.append(question('multiple_choice', 'Where will the picture be dense?',
                  choices=['Along the top row', 'Along the diagonal', 'Everywhere the same',
                           'Along the left edge'],
                  notes='B. abs(w - h) is the distance from the diagonal; a bar is drawn when a random '
                        'number up to size-2 is at least that distance, so near the diagonal almost always, '
                        'far from it almost never. Do not run it yet — predict first, then the next slide.'))

S.append(exercise('05 · READ IT', 'Run the rule', [
    'This is the whole program. Press Run and compare the picture with your prediction.',
    '',
    'Run it again. What changes, and what never does?',
], code=NAKE, hint='predict, then run · run twice',
   notes='What changes: every bar and cap. What never does: the dense diagonal, and one more thing '
         'they have to find on the next slide. The output pane scrolls; the console (›_) shows it '
         'taller. First Run on this deck downloads Pyodide if they skipped section 04.'))

S.append(question('short_answer', 'Which combination never occurs?',
                  hint='Two marks that are never found together, and the line that forbids it.',
                  example='e.g. "a ___ directly ___ a ___ — because line __ says ___"',
                  notes='Give them three minutes with the code and the picture. The answer: a cap (¯) '
                        'directly below a cell that has anything in it. cap needs '
                        'last_square_empty, which is the cell above, because h is the inner loop. Read '
                        'the best two answers out loud, then the next slide.'))

S.append(content('05 · THE LINE THAT FORBIDS IT', 'A cap never sits under a drawn cell', [
    '{mono:cap = (... and last_square_empty)}',
    '',
    '{mono:last_square_empty} was set by the previous {mono:h} in the same {mono:w} — the cell '
    '**above**. So a cap is only drawn under an empty cell, and the picture can be checked: find '
    'a cap under a bar and the code is wrong.',
    '',
    '{orange:That is a specification.} A sentence about the output that is either true or false, '
    'and a program that draws progressively has to carry state to keep it true.',
], bg=INK, body_size=32, notes='The 2025 question, answered. "Draw progressively and ensure this '
                                'condition" means: keep one boolean from the previous cell. Every '
                                'generative rule they write this semester has a sentence like this in '
                                'it, and the sentence is what you verify — not the code.'))

S.append(exercise('05 · FIND THE FAULT', 'Half the picture is solid', [
    'One character is missing from this copy. Run it: one half is solid bars.',
    '',
    'Find the line, and say **why** that side.',
], code=NAKE.replace('>= abs(w - h)', '>= w - h'),
   check='bars = sum(cell[0] for col in grid for cell in col)\n'
         'ok = bars < 0.74 * size * size\n'
         'msg = "" if ok else "still too many bars — the distance to the diagonal can go negative"',
   hint='where does the distance go negative?',
   notes='abs is gone, so where w < h the distance is negative and any random number beats it: '
         'every cell above the diagonal has a bar. The check counts bars. The lesson is not abs, it '
         'is that the picture told them something was wrong before the code did.'))

S.append(exercise('05 · MEET THE SPEC', 'Does this still meet the spec?', [
    'Someone tidied the code: the state is now set right after the bar is decided. It runs, and '
    'the picture looks about right.',
    '',
    'The spec: {bold:a cap never sits under a drawn cell.} Run it — the check reads the grid. '
    'Then fix it.',
], code=NAKE.replace(
        '        cap = (random.randint(0, size) > 0.2 * size\n'
        '               and last_square_empty)\n'
        '        grid[w].append((bar, cap))\n'
        '        if bar or cap:\n'
        '            last_square_empty = False\n'
        '        else:\n'
        '            last_square_empty = True\n',
        '        last_square_empty = not bar\n'
        '        cap = (random.randint(0, size) > 0.2 * size\n'
        '               and last_square_empty)\n'
        '        grid[w].append((bar, cap))\n'),
   check='ok = all(not (grid[w][h][1] and (grid[w][h - 1][0] or grid[w][h - 1][1]))\n'
         '         for w in range(size) for h in range(1, size))\n'
         'msg = "" if ok else "a cap sits under a drawn cell — which cell is \'last\', and when is it set?"',
   hint="'last' is the cell above, and it is set after the cell is done",
   notes='Two faults in one move: the state is set before the cap is decided, so "last" means this '
         'cell; and it only looks at the bar, so a cell with a cap counts as empty. The picture is '
         'nearly indistinguishable — this is the one only the spec catches. Fix: move the update '
         'below, and include the cap. That is the whole verification argument of the course in '
         'one drill.'))

assert NAKE.replace('>= abs(w - h)', '>= w - h') != NAKE and 'last_square_empty = not bar' not in NAKE

S.append(content('05 · THE RULE, DRAWN', 'Same rule, lines instead of characters', [
    'Twenty-five lines print it. Twenty-five different lines draw it: the rule does not care '
    'what a bar is made of.',
    '',
    '- Mouse left to right: how often a cap is allowed',
    '- Click: a new roll of the dice',
    '',
    '{muted:Week 3 you write the drawing version yourself, with data instead of dice.}',
], figure=F.nake(), sketch=live('nake', NAKE_JS, 600, 600,
                                 hint='move the mouse: cap chance · click: reroll', extra=NAKE_EXTRA),
   notes='Live in the html deck. Slide the mouse to the right and caps disappear — that is the 0.2. '
         'Then ask: does the spec still hold at every setting? It does, because the state logic '
         'did not change. Close the section here.'))


# ───────── 6 · the surprises (2025 s30, s36–37, collapsed per the deck review) ─────────
S.append(section('06', 'Four things that will surprise you', 'The parts that bite'))

S.append(question('multiple_choice', 'What is the output of 0.1 + 0.1 + 0.1 == 0.3 ?',
                  choices=['True', 'False'],
                  eyebrow_text='06 · SURPRISE 01 · NUMBERS',
                  notes='B — False. Binary floating point cannot represent 0.1 exactly, '
                        'so the sum is 0.30000000000000004. Carried over from 2025 s30, '
                        'which the deck review calls a verification lesson disguised as '
                        'trivia. Never compare floats with ==; compare a difference '
                        'against a tolerance.'))

S.append(cards('06 · SURPRISES', 'The four that actually bite', [
    ('01 · NUMBERS', 'Floats are not decimals',
     '{mono:0.1+0.1+0.1 != 0.3}. Compare a difference against a tolerance, never with =='),
    ('02 · ALIASING', 'Two names, one list',
     'Immutable — int, float, bool, str, tuple — copies on assignment. Mutable — list, '
     'dict, set — copies the reference. Change one name, the other changes.'),
    ('03 · TRUTHINESS', 'Empty is False',
     '{mono:[]}, {mono:""}, {mono:0} and {mono:None} are all falsy. {mono:if not problem:} '
     'in the flow loop from week 1 relies on it. {mono:if rows:} and {mono:if rows is not '
     'None:} are different questions.'),
    ('04 · INDENTATION', 'The shape is the logic',
     '**Four** spaces, and Python does {bold:not} return the last statement — a function '
     'with no {mono:return} gives you {mono:None}.'),
], notes='Card 4 is the one to slow down on: a function with no return gives None, and '
         'generated code forgets the return more often than anything else.'))

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

S.append(exercise('06 · DRILL 03 · RETURN', 'It gives you None', [
    'Python does {bold:not} return the last statement. A function with no {mono:return} '
    'hands back {mono:None}, silently.',
], code='def double(x):\n'
        '    x * 2\n\n'
        'print(double(21))',
   expect='42',
   hint='one word',
   notes='The 2025 deck claimed Python returns the last statement automatically and that '
         'bodies are indented two spaces; both wrong, and this room never saw it. Just teach '
         'the fact: no return, None comes back, silently — and print shows it.'))

# ───────────────────────── 7 · uv ─────────────────────────
S.append(section('07', 'uv', 'One command, every dependency'))

S.append(content('07 · UV', 'Why your code runs and theirs does not', [
    'Your script needs Python, and a version of it, and every library it imports, and a '
    'version of each of those. None of that is in the file. It is in **your machine**.',
    '',
    'So it runs for you and breaks for the next person — a groupmate, a marker, you on a '
    'lab PC next week. {orange:The code is fine. The environment was never written down.}',
    '',
    '- {mono:uv run script.py} — runs it in its own environment, installing what it needs',
    '- {mono:uv add pandas} — records the dependency where the next person will find it',
    '- {mono:uv sync} — makes your machine match the file',
], notes='Frame it as the group project and the marker: a repo that only runs on the laptop it '
         'was written on has not been handed in. uv writes the environment down in pyproject.toml '
         'and uv.lock, and "uv run" is the one command to say — it fetches an interpreter if there '
         'is none, and it sidesteps the Microsoft Store python stub on a fresh Windows machine. '
         'It replaces the pip + virtualenv tour entirely.'))

S.append(statement('A repo that does not say what it needs\nis not finished.',
                   eyebrow_text='07 · UV', size=100))

# ───────────────────────── 8 · workshop ─────────────────────────
S.append(section('08', 'Workshop', 'Predict, break, fix'))

S.append(content('08 · WORKSHOP', 'The tutorial is in the repo', [
    'Everything for the next two hours is one folder in the course repo, and the '
    'walkthrough is its README:',
    '',
    '- [github.com/sd5913/pfad · week02/README.md](https://github.com/sd5913/pfad/blob/2026/week02/README.md)',
    '- {mono:git pull} in your clone brings it down; {mono:uv run schotter.py} is the first thing it asks for.',
    '- No clone, or a lab machine you have not used? Download and double-click '
    '[setup.bat](https://github.com/ait4x/v915-setup/releases/latest/download/setup.bat) — '
    'it installs the tools, clones the repo, fetches a Python and opens VS Code in the folder.',
    '',
    '{muted:The drills you just did are the short version. The README is the long one, on your machine, with real windows.}',
], notes='Put the README link on the board next to the slides URL. setup.bat does the whole '
         'chain on a fresh machine — tools, clone into Documents\\pfad, Python, VS Code open in '
         'the repo — so a student who missed week 1 is running schotter.py in five minutes. '
         'Signout.bat at the end, as always.'))

S.append(timeline('08 · WORKSHOP', 'Two hours', [
    ('0:00', 'uv run, and nothing else', f'{{mono:git pull}} in your clone of {REPO}, then {{mono:uv run schotter.py}}'),
    ('0:10', 'Read first, run second', 'Schotter, Nake and a Schotter of cubes — in pygame, on your machine. Predict, run, change one knob.'),
    ('0:40', 'Tides', 'A tidal forecast for Hong Kong waters, drawn as rings. Somebody else\'s data, your rule.'),
    ('1:00', 'Find the fault', 'Four programs that run and are wrong. One of them is Nake.'),
    ('1:25', 'Meet the spec', 'Four sentences about a picture, three candidates side by side. Exactly one passes — say which, and point at what the others get wrong.'),
    ('1:45', 'Commit and push', '{mono:week02-answers.md} in your own repo, then the assignment check on your assignment repo.'),
], notes='The drills in the slides are 30 seconds each and prove the idea. The tutorial is '
         'where they do it on their own machine, in a repo, with uv — which is the thing '
         'that has to work in the exam and in assignment 2. Everything is in pfad/week02: '
         'schotter.py, nake.py, schotter3d.py, tides/, faults/, spec/. The answer key is in '
         'the admin workspace, not the repo.'))

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
