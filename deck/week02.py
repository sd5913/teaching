"""
SD5913 · Week 02 — Python you must be able to read.

    deckgen build --pptx        # export/ only, no node needed
    deckgen build               # everything, as the workflows run it

The reframe from docs/course-plan-2026.md: this week is no longer "learn to write
Python", it is "learn to read Python well enough to tell whether what you were handed
is right". Same material — types, control flow, data structures, uv — inverted
exercises: given working code predict the output, given broken code find the fault,
given a spec decide whether the code meets it.

The 1-2-4-All carries over from week 1, where the room ran out of time.

DRAFT — the structure and the anchors are from the course plan; the prose is a first
cut and wants a pass before it is shown.
"""
from deckgen.layouts import (title, agenda, section, statement, content, cards,
                             question, two_col, activity, timeline, end)

COURSE = 'SD5913'
SITE = 'venetanji.github.io/sd5913-teaching'
REPO = 'github.com/sd5913/pfad'
EYE = 'SD5913 · WEEK 02'

S = []

# ───────────────────────── 0 · landing ─────────────────────────
S.append(title(EYE, 'Reading code',
               'You will be handed code you did not write.'))

S.append(agenda(EYE, [
    'Where week 1 left off',
    '1-2-4-All: what you want to make',
    'The five things Python is made of',
    'uv: one command, every dependency',
    'Workshop — read it, break it, fix it',
]))

# ───────────────────────── 1 · loose ends from week 1 ─────────────────────────
S.append(section('01', 'Loose ends', 'Where week 1 left off'))

S.append(content('01 · LOOSE ENDS', 'Three things from last week', [
    '- The **org invitation** is in the email you signed up to GitHub with. '
    'It {orange:expires after seven days} — accept it even if you do nothing else.',
    '- Being in the org is {bold:not} push access. Assignment 1 lives on '
    '**your own account**, which is why it does not matter yet.',
    '- Not registered at {mono:pfad.ait4x.org}? Do it now, it takes a minute. '
    'Nothing is marked until your ID and your GitHub username are the same row.',
], notes='Ask for hands: who has NOT accepted. Expect a third of the room. '
         'Anyone whose invitation expired — take the username, re-invite after class.'))

S.append(question('short_answer', 'What broke for you last week?',
                  hint='One line. Git, the terminal, VS Code, the registry — anything.',
                  notes='Two minutes, no more. This is triage, not a discussion. Read three '
                        'out loud and fix them live if they are quick.'))

# ───────────────────────── 2 · 1-2-4-All (carried from week 1) ─────────────────────────
S.append(section('02', 'What do you want to make?', 'Carried over from week 1'))

S.append(activity('1-2-4-All', 12, 'What do you want to make by December?', [
    '**1 minute — alone.** Write one sentence. Not a technology, a thing: '
    'an object, a screen, a sound, an installation, a tool for your own practice.',
    '**2 minutes — in pairs.** Read each other yours. Find what they have in common.',
    '**4 minutes — in fours.** Merge into {orange:one} idea the four of you would '
    'actually want to see exist.',
    '**All.** One sentence per table, out loud.',
], notes='This is ideation, not team formation — say so. Groups of four by seating '
         'adjacency is the wrong instrument for skill-diverse teams at 112 students; '
         'the group project forms in week 7 by a different mechanism. '
         'Capture the sentences: they are the best read on what the second half of the '
         'course should contain.'))

S.append(question('word_cloud', 'One word: the thing your table would build.',
                  notes='Run it while the tables are still talking. Screenshot it — '
                        'it goes next to the week-1 survey results.'))

# ───────────────────────── 3 · the language ─────────────────────────
S.append(section('03', 'Python, read not written', 'The five things it is made of'))

S.append(statement('You will not memorise the syntax.\nYou will learn to check it.',
                   eyebrow_text='03 · THE SHIFT'))

S.append(content('03 · THE SHIFT', 'Three questions, all week', [
    'Every exercise this week is one of these, and so is every quiz question:',
    '',
    '- Here is code that runs. **What does it print?**',
    '- Here is code that is wrong. **Where?**',
    '- Here is a spec and some code. **Does the code meet it?**',
    '',
    '{muted:None of them ask you to write a program from a blank file. That comes later, '
    'and by then you will be able to tell whether what you wrote is right.}',
], notes='Land this hard. The room expects a syntax lecture; it is not one. The reason: '
         'they will be handed generated code all semester and the only defensible skill '
         'is verification.'))

S.append(cards('03 · THE LANGUAGE', 'Five things, and that is most of it', [
    ('01 · TYPES', 'Values have types',
     'int, float, str, bool. Most bugs you meet are a str where a number was wanted.'),
    ('02 · NAMES', 'Names point at values',
     'Assignment does not copy. Two names can point at one list, and changing one changes both.'),
    ('03 · FLOW', 'if · for · while',
     'The indentation is the structure. Python has no braces, so the shape on screen is the shape of the logic.'),
    ('04 · DATA', 'list · dict · tuple · set',
     'Nearly everything you scrape, load or generate arrives as a list of dicts.'),
    ('05 · FUNCTIONS', 'A name for a block',
     'Inputs, and one output. Read the signature first, the body second.'),
]))

S.append(two_col('03 · READING', 'Read it out loud', [
    'Reading code is a skill you practise, not a thing you know.',
    '',
    '- Start at the **bottom**: what does it return?',
    '- Then the signature: what does it take?',
    '- Only then the middle.',
    '',
    'Say the types out loud as you go. "A list of dicts, each with a name and a year."',
], [
    'def tide(rows, year):',
    '    out = []',
    '    for r in rows:',
    '        if r["year"] == year:',
    '            out.append(r["height"])',
    '    return sum(out) / len(out)',
]))

S.append(question('multiple_choice', 'What does that function return for an empty year?',
                  choices=['0', 'None', 'It crashes', 'An empty list'],
                  notes='Answer: it crashes — ZeroDivisionError on len(out) == 0. This is '
                        'the whole week in one slide. The code is not wrong-looking; it is '
                        'wrong for an input nobody tried.'))

# ───────────────────────── 4 · uv ─────────────────────────
S.append(section('04', 'uv', 'One command, every dependency'))

S.append(content('04 · UV', 'Why your code runs and theirs does not', [
    'Last year every single week of this course shipped a {mono:requirements.txt} that '
    'was missing something. The tutorial did not run on a clean machine — not because '
    'the code was wrong, but because the {orange:environment was never written down}.',
    '',
    '- {mono:uv run script.py} — runs it, in its own environment, installing what it needs',
    '- {mono:uv add pandas} — records the dependency where the next person will find it',
    '- {mono:uv sync} — makes your machine match the file',
    '',
    '**A repo that does not say what it needs is not finished.** That is a grading '
    'criterion, not a style note.',
], notes='Be honest that this is a fix for a real failure in last year\'s course. '
         'It lands better as "here is what went wrong" than as a tool tour.'))

# ───────────────────────── 5 · workshop ─────────────────────────
S.append(section('05', 'Workshop', 'Read it, break it, fix it'))

S.append(timeline('05 · WORKSHOP', 'Two hours', [
    ('0:00', 'Clone the week 2 folder', f'{REPO} — {{mono:git pull}} first'),
    ('0:15', 'Predict, then run', 'Six short programs. Write your answer down before you run it.'),
    ('0:45', 'Find the fault', 'Four programs that run and are wrong. One is the tide function.'),
    ('1:20', 'Meet the spec', 'A brief and three candidate solutions. Which one is right?'),
    ('1:45', 'Commit and push', 'Your answers, in your own repo, as a markdown file.'),
]))

S.append(question('image_upload', 'Push your answers, then screenshot the green tick.',
                  notes='The upload is the attendance signal and the "it actually worked" '
                        'signal in one. Anyone who cannot push is stuck on week 1 — deal '
                        'with them at the back of the room.'))

S.append(end('See you next week', 'Week 3: getting data, and making it look like something.', SITE))

DECK = {'title': f'{COURSE} · Week 2 — Reading code', 'pdf': f'{COURSE}-week02.pdf', 'slides': S}
