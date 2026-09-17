"""
SD5913 · Week 03 — Numbers into pictures.

    deckgen build --pptx        # export/ only, no node needed
    deckgen build               # everything, as the workflows run it

Sources this is built from:

  ~/dev/sd5913/docs/week03-lesson-plan.md — the contract between this deck and the
                               tutorial folder pfad/week03/, written 2026-09-15. The
                               names it fixes are load-bearing and appear in both:
                               tides.py, bar, moon_age, to_xy, move, scale, rotate,
                               data/, out/, and the four ClassPoint activities in order.
  deck/assets/data/tides-QUB-2026.json — the Hong Kong Observatory's hourly tide table
                               for Quarry Bay, 2026, verbatim (fields, then 365 rows of
                               month, day and 24 heights as strings). Row 259 is
                               17 September, the day of the class. Every drill, every
                               figure and the live sketch use those same 24 numbers, so
                               a student who opens the Observatory's page finds it agrees.
  deck/assets/data/earthquakes-2026-09.csv — mag,lng,lat,depth,time trimmed from the
                               USGS 2.5+ month feed: 2,130 rows, largest 6.7.
  ~/dev/sd5913/docs/deck-review/weeks-02-04.md — the 2025 week 3 deck was 94 slides of
                               screenshots and re-taught week 2 byte for byte. What the
                               review says to keep is s28–38 (dimensions, vectors,
                               transformations) and s63 (the two paths); both are here,
                               rewritten, and nothing else from it is.

Week 2 was delivered in full; only the four ClassPoint activities after the mark
were not run. uv was mentioned once, so the tutorial and the reference page carry it.

Deliberately NOT here:

  fractals and the complex plane (2025 s39–51)  — good material, wrong week
  pip, venv, activation, Set-ExecutionPolicy    — uv run replaced all of it in week 2
  Jupyter (2025 s26, s59)                       — not used this year
  issues, PRs, Copilot-assigned issues (s52–56) — week 8
  pandas                                        — the 2025 code is broken by pandas 3,
                                                  and a list of tuples is all this needs
  the 2025 s13 function slide                   — wrong twice, never reused

In-slide drills are Pyodide and the standard library only: no matplotlib, no requests,
no numpy inside an exercise(). Every `expect` below was produced by running the
reference solution in CPython, never typed by hand; tests/exercises.test.py holds those
solutions and fails the build if a drill starts solved or cannot be solved.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import figures as F                                   # noqa: E402
from deckgen import attach_reports, INK               # noqa: E402
from deckgen.layouts import (title, agenda, section, statement, content, cards, image_full,   # noqa: E402
                             question, two_col, timeline, exercise, figure_slide,
                             code_panel, code_slide, sketch_slide, live, end)

COURSE = 'SD5913'
SITE = 'sd5913.github.io/teaching'
REPO = 'github.com/sd5913/pfad'
EYE = 'SD5913 · WEEK 03'

# The 24 numbers of the lecture: Quarry Bay, 17 September 2026, hours 01:00 to 24:00,
# metres above chart datum. deck/assets/data/tides-QUB-2026.json, row 259, as floats.
# Kept as source so every drill shows the identical list and figures.py reads the file.
HEIGHTS = ('heights = [2.19, 2.09, 1.90, 1.63, 1.36,\n'
           '           1.14, 1.05, 1.08, 1.15, 1.24,\n'
           '           1.29, 1.35, 1.44, 1.47, 1.47,\n'
           '           1.42, 1.38, 1.38, 1.46, 1.65,\n'
           '           1.86, 2.04, 2.14, 2.17]')

TIDE_CLOCK_JS = '''const heights = [2.19, 2.09, 1.90, 1.63, 1.36, 1.14,
                 1.05, 1.08, 1.15, 1.24, 1.29, 1.35,
                 1.44, 1.47, 1.47, 1.42, 1.38, 1.38,
                 1.46, 1.65, 1.86, 2.04, 2.14, 2.17];
const C = 310, K = 250 / 2.45;
let i = 1;

function setup() {
  createCanvas(620, 620);
  frameRate(8);
}

function toXY(hour, height) {
  const a = hour / 24 * TWO_PI, r = height * K;
  return [C + r * cos(a), C + r * sin(a)];
}

function draw() {
  background('#FAF8F4');
  noFill(); stroke('#E1E1DE'); strokeWeight(1.5);
  circle(C, C, 2 * K); circle(C, C, 4 * K);
  stroke('#ED6D24'); strokeWeight(3);
  beginShape();
  for (let h = 1; h <= i; h++) {
    const p = toXY(h, heights[h - 1]);
    vertex(p[0], p[1]);
  }
  endShape();
  const hand = toXY(i, heights[i - 1]);
  stroke('#000B1C'); strokeWeight(2);
  line(C, C, hand[0], hand[1]);
  noStroke(); fill('#5C6470'); textSize(24); textAlign(CENTER);
  text(nf(i, 2) + ':00  ' + nf(heights[i - 1], 1, 2) + ' m', C, 604);
  i = i % 24 + 1;
}'''

TIDE_CLOCK_EXTRA = '''function mousePressed() { i = 1; }'''

S = []

# ───────────────────────── 0 · landing ─────────────────────────
S.append(title(EYE, 'Numbers into pictures',
               'A phenomenon, a file of numbers, and every way to look at it.'))

S.append(agenda(EYE, [
    'Assignment 2: a natural phenomenon, and a picture of it',
    'Twenty-four numbers — a loop and a function',
    'Where the numbers come from',
    'Dimensions, vectors, transformations',
    'Simple rules, complex results: double, square, add c',
    'Plotting: the same numbers, five ways',
    'Two paths — designer, artist',
    'Workshop — your repo, your first picture',
]))

S.append(content('SD5913 · WEEK 03 · WORDS', 'Words you will hear today', [
    '- **data** — numbers somebody measured and published. **JSON** — a common file '
    'format for them: lists and dicts, written out as text.',
    '- **parse** — turn a file of text into lists and numbers you can use. '
    '**cache** — fetch once, save the file, read the file from then on.',
    '- **plot** — draw numbers as a picture. **axis** — one direction of the picture, '
    'and what it means: hour across, metres up.',
    '- **vector** — a list of numbers where each position means something: '
    '{mono:(hour, height)}. **transformation** — a rule that turns one vector into another.',
    '- **frame** — one picture of an animation. **library** — code somebody else wrote, '
    'that draws for you.',
    '- **iterate** — run the rule again on its own result. **chaos** — a rule that '
    'doubles every error, so a tenth of a degree becomes the whole circle.',
    '',
    '{muted:Every word from the slides, in plain language:} [' + SITE + '/glossary.html](https://' + SITE + '/glossary.html)',
], body_size=30, notes='One minute, pointing, not reading. Six of these ten are new this '
                       'week and all six are in the glossary before the class. The one to '
                       'say out loud is transformation: it is the spine of the middle hour '
                       'and the room will assume it means something to do with robots.'))

# ───────────────────────── 1 · loose ends ─────────────────────────
# Counts only. No repo, name, username or ClassPoint response belongs in a public deck,
# and none is here — the same rule as week 2 s7.
S.append(content('01 · ASSIGNMENT 1', 'It closed on Sunday', [
    'Marking starts this week. What a passing repo looked like, in three lines:',
    '',
    '- **Two files at the top level**, with those exact names: {mono:README.md} '
    'and {mono:PROCESS.md}. A {mono:PROCESS.md} in a subfolder is a missing {mono:PROCESS.md}.',
    '- **A References heading** with real entries under it. It is the check\'s most '
    'common complaint, and the cheapest one to have fixed.',
    '- **Commits on more than one day.** One commit called {mono:Initial commit} says '
    'the essay arrived from somewhere else, whether or not it did.',
    '',
    '{muted:Late work is marked, with the late penalty in the course outline. Submit it '
    'anyway — a late repo is worth more than no repo.}',
], notes='Counts only, and no repo on the projector. Say that the check they ran is the '
         'same one the tutors run from outside their repo, and that the tick is evidence, '
         'not proof — week 2 s11. Anyone who has still not submitted a URL on Canvas: see '
         'me at the break, not now. Assignment 2 is set in four slides and it matters more.'))

S.append(content('01 · WEEK 02', 'Last week, if you want it again', [
    'Week 2 is **all in the browser**: [' + SITE + '/week02/](https://' + SITE + '/week02/). '
    'Every drill still runs, still checks itself, still keeps your answer.',
    '',
    '- The tutorial [week02/README.md](https://' + REPO + '/blob/2026/week02/README.md) is the '
    'long version: the faults and the spec exercise.',
    '- {mono:uv} got one mention. It runs everything in today\'s tutorial, and '
    '[reference/uv.md](https://' + REPO + '/blob/2026/reference/uv.md) is the ten minutes on what it does.',
    '',
    '{muted:Two facts from last week come back today, on the slides where they are needed.}',
], notes='One minute. Week 2 was delivered in full; only the activities after the mark were '
         'not run, so nothing is owed and nobody is behind. Point, do not summarise. uv is the '
         'one thing said once that matters today: the tutorial opens with it and the reference '
         'page carries it. The two facts this deck repeats on the way past: a function with no '
         'return hands back None (week 2 s46), and square brackets look up a list and a dict '
         'the same way (s28).'))

S.append(image_full('marks-2026-09-10.jpg', '01 · LOOSE ENDS · THE MARK',
                    '56 marks. Two at a time, pick the better one: [pfad.ait4x.org/vote](https://pfad.ait4x.org/vote) — the picture is the link too.',
                    fit='contain', url='https://pfad.ait4x.org/vote',
                    notes='Thirty seconds. Week 2\'s "photograph the sketch" got 58 uploads, 56 of them '
                          'marks — most of them made with a model or a pixel editor rather than '
                          'drawn, which is its own conversation for week 4. Nobody can pick one out '
                          'of fifty-six, so nobody has to: the vote page shows two at a time and you '
                          'click the better one. Bradley-Terry ranks them from everyone\'s pairs. Ask '
                          'them to do ten pairs on their phones right now, then keep going during '
                          'the week; week 4 opens with the top ten and a play with image generation '
                          'on the shortlist. That page is also the week 4 example: two pictures, one '
                          'click, one row in a database.'))


S.append(question('word_cloud', 'Name a natural phenomenon.',
                  hint='One or two words. Tide, rain, wind, moon, birds, earthquakes. '
                       'Traffic is not one.',
                  notes='Ninety seconds. This is the seed of assignment 2 and we come back '
                        'to the cloud in section 08, so leave it up while the brief is on '
                        'the next slide. Expect tide, rain, typhoon, earthquake, and one '
                        'person who says traffic — take it, then ask whether the numbers '
                        'are published. That question is the assignment.'))

# ───────────────────────── 2 · assignment 2 ─────────────────────────
S.append(cards('02 · ASSIGNMENT 2', 'Numbers about a natural phenomenon, and a picture', [
    ('obtain', 'From a file somebody publishes',
     'JSON, CSV or an HTML page. Somebody already did the measuring — the Observatory, '
     'the USGS, Wikipedia. The raw file you fetched is committed in {mono:data/}.'),
    ('make', 'A picture from them',
     'Informative, artistic, or animated. Any library. The script says what it needs, '
     'so it runs on somebody else\'s machine.'),
    ('say', 'What it is, and where it came from',
     '{mono:README.md}: the phenomenon, the source as a link, the picture, how to run it. '
     '{mono:PROCESS.md} as before. Commits over more than one day.'),
    ('due', 'Sunday 4 October, 23:59',
     '{orange:10% of the course.} A repo on your own account, the URL on Canvas. '
     'Set today, so you have two and a half weeks.'),
], notes='Three minutes on this slide and no more — the next two answer the questions it '
         'raises. The deadline is the Sunday after the 1 October holiday, not week 5. '
         'The one line to say out loud: a natural phenomenon means numbers somebody else '
         'measured and published, not numbers you invented. If the phenomenon has no '
         'public file behind it, it is the wrong phenomenon for this assignment.'))

S.append(two_col('02 · ASSIGNMENT 2', 'What a finished repo looks like', [
    'A folder is a list of names. A path is an address: {mono:tidal-clock/data/tides.json}. '
    '{mono:.} is here, {mono:..} is the folder above.',
    '',
    'Names that start with a dot are hidden by Finder and Explorer — not by git, not by '
    'VS Code. Every repo you make has three.',
    '',
    '**README.md** the phenomenon, the picture. **PROCESS.md** the tools. '
    '**data/** the raw file, so it runs offline. **out/** the picture.',
    '',
    '{orange:Start from the template:} [sd5913/assignment-2-template → Use this template]'
    '(https://github.com/sd5913/assignment-2-template/generate). '
    '[pfad/reference/files.md](https://github.com/sd5913/pfad/blob/2026/reference/files.md) is the ten-minute version.',
], [
    'tidal-clock/',
    '├── .git/             the history. never open it',
    '├── .github/',
    '│   └── workflows/',
    '│       └── check.yml what GitHub runs',
    '├── .gitignore        never committed: site/',
    '├── README.md',
    '├── PROCESS.md',
    '├── fetch.py          HERE / "data" / FILE',
    '├── plot.py',
    '├── data/             the raw file',
    '└── out/              the picture',
], lang=None, right_size=22, left_size=26,
   notes='The tree on the right is the template as ls -a shows it; leave it up. New this '
         'year: the three dot names, said out loud, because Finder and Explorer hide them and '
         'nobody in this room grew up with a file system — phones do not have one. .git is the '
         'history; .github/workflows is the exact address GitHub looks at (week 2\'s empty '
         'Actions tabs were this); .gitignore is the list of what never gets committed. data/ '
         'is still the part people skip: fetch once, save the reply, parse the saved file. '
         'The template ships all of it, so the first push already gets a red cross with the '
         'list of what is left to do. reference/files.md in pfad is the ten-minute version for later.'))

S.append(exercise('02 · DRILL · A PATH', 'Predict the path', [
    'Every script in the tutorial starts like this: {mono:HERE} is the folder the script is in. '
    '{mono:/} joins two paths; {mono:.parent} is {mono:..} in code; {mono:.name} is the last piece.',
    '',
    '**Predict the three lines.** Then fix {mono:DATA}: the raw file is in {mono:data/} '
    '**beside** {mono:out/}, not inside it.',
], code='from pathlib import Path\n\n'
        'HERE = Path("/Users/mia/tidal-clock")\n'
        'OUT = HERE / "out"\n'
        'DATA = OUT / "data" / "tides.json"   # wrong\n\n'
        'print(HERE.parent)\n'
        'print(DATA)\n'
        'print(DATA.name)',
   expect='/Users/mia\n/Users/mia/tidal-clock/data/tides.json\ntides.json',
   hint='OUT.parent is the folder above out/ — or start from HERE.',
   notes='Two minutes. Ask the first line out loud: HERE.parent is /Users/mia, the folder '
         'above — that is cd .. in code. As given, the second line prints '
         '/Users/mia/tidal-clock/out/data/tides.json: a perfectly real-looking address for '
         'a file that does not exist, which is exactly how "no such file" happens on Sunday '
         'night. Either fix passes — OUT.parent / "data" or HERE / "data". Windows people: '
         'their real HERE starts with C:\\ and Python still joins with /.'))

S.append(content('02 · ASSIGNMENT 2', 'Name it properly, before you start', [
    'We said this in week 2 and it applies from today: the repo name is the first thing '
    'anyone sees, and it is in your portfolio for longer than it is in my gradebook.',
    '',
    '- {muted:Bad:} {mono:assignment2} · {mono:ass2} · {mono:data-viz-final-FINAL}',
    '- {orange:Good:} {mono:tidal-clock} · {mono:quakes-this-month} · {mono:rainfall-kowloon}',
    '',
    'Short, lowercase, hyphens, and it says what the thing does. '
    '{muted:You can rename a GitHub repo later, but the URL you put on Canvas will not follow.}',
], notes='Thirty seconds, straight callback to week 2 s53 — which was delivered, so do not '
         're-explain it. The new line is the last one: renaming breaks the submitted URL, so '
         'name it before the first commit, not after.'))

# ───────── 3 · twenty-four numbers — the loop and the function, on real data ─────────
S.append(statement('Twenty-four numbers.\nHow many ways can you look at them?',
                   eyebrow_text='03 · THE NUMBERS', size=110))

S.append(code_panel('03 · THE NUMBERS', 'The tide at Quarry Bay, today', [
    '# Hong Kong Observatory, station QUB, 17 September 2026',
    '# metres above chart datum, one per hour, 01:00 to 24:00',
    '',
] + HEIGHTS.split('\n') + [
    '',
    'print(len(heights), min(heights), max(heights))',
], caption='data.weather.gov.hk · one row of a file with 365 of them · '
           'the tutorial fetches it, this deck quotes it',
   notes='Say where it is from and that they can check it: the Observatory publishes the '
         'same table on a web page, so the 2.19 at 01:00 is falsifiable. That matters more '
         'than it sounds — every number on every slide this term should be checkable '
         'against something outside the room. Low water is 1.05 at 07:00, high water 2.19 '
         'at 01:00. These exact 24 numbers are in all six drills today.'))

S.append(exercise('03 · D1 · A LOOP', 'Once for each number', [
    'A loop does the indented lines once for every item. {mono:enumerate} hands you the '
    'position too, and {mono:start=1} makes the first hour 1, not 0.',
    '',
    '**How many lines will it print?** Say it, then run it.',
    '',
    'Now change one character: print the hours **under 1.1**.',
], code=HEIGHTS + '\n\n'
        'for hour, height in enumerate(heights, start=1):\n'
        '    if height > 2:\n'
        '        print(hour, height)',
   expect='7 1.05\n8 1.08',
   hint='> 2 becomes < 1.1',
   notes='Make them commit to a number out loud before anyone runs it. It prints five lines '
         '(hours 1, 2, 22, 23, 24). Then the change: two lines, hours 7 and 8 — low water, '
         'which is where the 1.05 on the previous slide lives. The loop is not the lesson; '
         'the lesson is that a question about the sea became one character.'))

S.append(content('03 · A LOOP', 'That is a loop, and that is all of it', [
    '{mono:for hour, height in enumerate(heights, start=1):}',
    '',
    '- **once for each item** — twenty-four numbers, twenty-four turns',
    '- **the names change each turn** — {mono:hour} and {mono:height} mean something '
    'different every time round',
    '- **the indented lines are what happens** — the four spaces are the loop',
    '',
    '{orange:Everything else today is this, with something other than print at the end.}',
], body_size=32,
   notes='One minute, pointing at the drill they just ran, not at grammar. The four spaces '
         'are worth saying: indentation is the logic in Python, and it is the one piece of '
         'syntax that has no equivalent in the languages they might have seen. Do not take '
         'questions about while loops, ranges or break here.'))

S.append(exercise('03 · D2 · A FUNCTION', 'It prints None twenty-four times', [
    '{mono:bar} is a rule with a name: a height goes in, a row of {mono:#} should come out. '
    '{mono:"#" * 11} is eleven hashes — {mono:*} repeats text.',
    '',
    'Run it. **One word is missing.** Find it, and make it print bars.',
], code='def bar(height):\n'
        '    "#" * round(height * 10)\n\n'
        + HEIGHTS + '\n\n'
        'for hour, height in enumerate(heights, start=1):\n'
        '    print(f"{hour:2} {bar(height)}")',
   expect=' 1 ######################\n'
          ' 2 #####################\n'
          ' 3 ###################\n'
          ' 4 ################\n'
          ' 5 ##############\n'
          ' 6 ###########\n'
          ' 7 ##########\n'
          ' 8 ###########\n'
          ' 9 ############\n'
          '10 ############\n'
          '11 #############\n'
          '12 ##############\n'
          '13 ##############\n'
          '14 ###############\n'
          '15 ###############\n'
          '16 ##############\n'
          '17 ##############\n'
          '18 ##############\n'
          '19 ###############\n'
          '20 ################\n'
          '21 ###################\n'
          '22 ####################\n'
          '23 #####################\n'
          '24 ######################',
   hint='no return, nothing comes out',
   notes='This is week 2 s46, which the room never got, taught here because they need it. '
         'Python does NOT hand back the last statement — a function with no return gives '
         'None, silently, and f-strings will happily print the word None twenty-four times. '
         'When the bars appear, stop: that is the first visualisation of the day and no '
         'library made it. bar() is the same function the tutorial\'s tides.py uses.'))

S.append(figure_slide('03 · THE FIRST PICTURE', 'No library drew this', F.tide_bars(),
                      body=['Twenty-four rows of hashes, one call of {mono:bar} each. It is a '
                            'bar chart, and it is nine lines of Python.'],
                      caption='Quarry Bay, 17 September 2026 · teal is low water at 07:00, '
                              'orange is high water at 01:00',
                      notes='Hold this for thirty seconds. The argument of the whole day is on '
                            'it: a picture is a transformation applied to every number by a '
                            'loop, and matplotlib is a convenience, not a requirement. Ask '
                            'what the shape says — two highs and two lows in a day, which is '
                            'the Earth turning under a bulge of water in two places. Then ask '
                            'what it hides: you cannot read 1.47 off a row of hashes.'))

S.append(content('03 · A FUNCTION', 'A rule with a name', [
    '{mono:def bar(height):} — something goes **in**, something comes **out**.',
    '',
    '- The name in the brackets is a name for whatever you hand it. It exists only inside.',
    '- {orange:No} {mono:return}{orange:, nothing comes out.} Python hands back {mono:None}, '
    'silently, and your picture is empty for a reason you cannot see.',
    '- Four spaces of indentation say which lines are inside the function.',
    '',
    '{muted:This is the mistake generated code makes more than any other. You just found it.}',
], body_size=30, notes='Week 2 s46, said once, here, because D2 needed it. The 2025 deck '
                       'claimed Python automatically returns the last statement and that '
                       'bodies are indented two spaces; both are false and that slide is '
                       'never coming back. Say the None fact, point at the drill, move on. '
                       'The tutorial has bar() in tides.py with a return.'))

S.append(exercise('03 · D3 · HIGHEST', 'When is high water?', [
    'A loop that remembers: keep the biggest height you have seen, and the hour it '
    'happened. {mono:best} carries from one turn to the next — that is **state**.',
    '',
    'Fill in the {mono:___}. **Predict the answer first** — you have seen the picture.',
], code=HEIGHTS + '\n\n'
        'def high_tide(heights):\n'
        '    best_hour = 0\n'
        '    best = 0\n'
        '    for hour, height in enumerate(heights, start=1):\n'
        '        if ___:\n'
        '            best = height\n'
        '            best_hour = hour\n'
        '    return best_hour\n\n'
        'print(high_tide(heights))',
   expect='1',
   hint='compare height with best',
   notes='They should say 1 before running, from the bar chart two slides ago — high water '
         'is the first row. The answer is height > best. Two things to draw out: max(heights) '
         'would give the height but not the hour, which is why the loop exists; and best '
         'starting at 0 is a choice that only works because heights are never negative. If '
         'someone writes >= they still get 1, because 2.19 occurs once — say that is luck, '
         'not correctness.'))

S.append(content('03 · THE TOOLKIT', 'That was the whole toolkit', [
    'A **loop** over the numbers. A **function** per number. That is it.',
    '',
    'Everything for the rest of today is those two, with something else at the end of '
    'the loop: a library drawing a line instead of {mono:print} writing hashes.',
    '',
    '{orange:The picture is the check.} If the bars had come out flat, you would have '
    'known — which is more than most tests tell you.',
], bg=INK, body_size=34,
   notes='Close the section here and do not let it drift into more syntax. The honest claim '
         'is that they can now read the whole tutorial: every script in pfad/week03 is a '
         'loop, a function and a call to matplotlib. The last line is the course method '
         'again — verification, with the eye as the test.'))

# ───────────── 4 · where the numbers come from ─────────────
S.append(code_panel('04 · THE SOURCE', 'Somebody already did the measuring', [
    '{muted:# one address, and 365 days come back}',
    'https://data.weather.gov.hk/weatherAPI/opendata/opendata.php',
    '    ?dataType=HHOT&station=QUB&year=2026&rformat=json',
    '',
    '{muted:# what it says, with most of it cut out}',
    '{"fields": ["MM", "DD", "01", "02", ..., "24"],',
    ' "data": [["01", "01", "0.68", "0.64", ..., "1.09"],',
    '          ["01", "02", "0.69", "0.46", ..., "0.85"],',
    '          {orange:["09", "17", "2.19", "2.09", ..., "2.17"]}]}',
], caption='HHOT = hourly heights of tide · QUB = Quarry Bay · the whole year is 66 KB',
   notes='Read the URL out loud once: it is four questions — which table, which station, '
         'which year, which format. Every open-data endpoint is shaped like that. Then the '
         'reply: a dict with two keys, one of them a list of 365 lists. The orange row is '
         'today. Point at the quotes around 2.19 and leave the question hanging for the '
         'next two slides. The same file is committed in the tutorial under data/.'))

S.append(content('04 · JSON', 'A dict of lists of lists, and one way in', [
    'Square brackets ask a dict **and** a list the same question: {bold:give me the one at ___}. '
    'A dict answers to a name, a list to a position, counting from 0.',
    '',
    '- {mono:d["data"]} — the list of 365 rows',
    '- {mono:d["data"][259]} — row 259, which is 17 September',
    '- {mono:d["data"][259][2]} — the first hour of that row: {orange:"2.19"}',
    '',
    'Three brackets, three steps, and you are at one number. '
    '{muted:Which is not yet a number — look at the quotes.}',
], body_size=30,
   notes='Week 2 s28 again: one slide, said once. Do not teach indexing '
         'again after this. The row number 259 is worth a beat — it is 31+28+31+30+31+30+31+31+16, '
         'i.e. the day of the year minus one, and the tutorial computes it rather than typing '
         'it. The quotes are the next slide and the whole point.'))

S.append(question('multiple_choice', 'What type is d["data"][259][2]?',
                  choices=['int', 'float', 'str', 'list'],
                  eyebrow_text='04 · JSON · MULTIPLE CHOICE',
                  notes='C — str. The quotes in the file are what make it text, and the '
                        'Observatory wrote them. Most of the room will say float because it '
                        'looks like a number. This is week 2 s27 (a = "6"; b = "6"; a + b is '
                        '"66") pointed at a real file: every scraped number is text until you '
                        'say float(). Ask what "2.19" + 1 would do before you move on — it is '
                        'a TypeError, which is the kind day; "2.19" + "1" is the unkind one.'))

S.append(exercise('04 · D4 · READ THE FILE', 'The quotes are still there', [
    'Two rows of the real file. {mono:d["data"][1]} is the 17th; position {mono:8} in a '
    'row is 07:00, because {mono:0} and {mono:1} are the month and the day.',
    '',
    'Make it print the 07:00 height **as a number, plus one**.',
], code='d = {"fields": ["MM", "DD", "01", "02", "03",\n'
        '                "04", "05", "06", "07"],\n'
        '     "data": [["09", "16", "2.26", "2.25",\n'
        '               "2.12", "1.88", "1.59",\n'
        '               "1.31", "1.11"],\n'
        '              ["09", "17", "2.19", "2.09",\n'
        '               "1.90", "1.63", "1.36",\n'
        '               "1.14", "1.05"]]}\n\n'
        '# 07:00 on the 17th, as a number, plus one\n'
        'print(d["data"][1][8])',
   expect='2.05',
   hint='float(...) + 1',
   notes='It prints 1.05 as it stands, and 1.05 looks like a number, which is the trap. '
         'float() is the whole answer. Ask what happens without it: "1.05" + 1 raises '
         'TypeError, and that is Python being kind — the version that hurts is "1.05" + "1", '
         'which quietly gives "1.051". The tutorial\'s tides.py does this float() conversion '
         'once, in load_year, which is the right place for it.'))

S.append(cards('04 · FOUR RULES', 'Four rules for taking somebody else\'s numbers', [
    ('cache', 'Fetch once, keep the file',
     'Fetch, save the raw reply into {mono:data/}, then parse the **file**. Your script '
     'runs with no internet, and the committed file is what makes the repo reproducible.'),
    ('html', 'Same idea, messier',
     'No JSON? A web page is a tree, and one line of BeautifulSoup walks it: '
     '{mono:select("table.wikitable")}, then the rows. The typhoon season table on '
     'Wikipedia is one.'),
    ('rot', 'Watch the line rot',
     'The tidal-stream endpoint behind week 2\'s rings moved in 2023 — '
     '[fetch_tides.py](https://github.com/sd5913/pfad/blob/2026/week02/tides/fetch_tides.py) says so in a comment. A cached file outlives the URL it came from.'),
    ('polite', 'Be polite',
     'A {mono:User-Agent} that says who you are and what for. One request, not a loop of '
     'them. You are a guest on somebody else\'s server.'),
], notes='Two minutes. Cache is the one that changes their code today, and it is also the '
         'one the check looks for: a data/ folder with a file in it. The line-rot card is '
         'not a warning about the future, it is a thing that already happened to this '
         'course — name it, because naming the real failure is what makes the rule stick. '
         'Politeness: Wikipedia blocks the default Python user-agent outright.'))

# ───────── 5 · dimensions, vectors, transformations — 2025 s28–38, rewritten ─────────
S.append(section('05', 'Dimensions', 'A chart type is a transformation'))

S.append(cards('05 · DIMENSIONS', 'One number, two numbers, three', [
    ('1-D', 'A number on its own',
     'A height. A time. A brightness. All you can do is put it somewhere on a line — '
     'or make it a length, which is what {mono:bar} did.'),
    ('2-D', 'Two numbers, and a decision',
     '{mono:(hour, height)} is a point on a plane. So is {mono:(lat, lng)}, and so is '
     '{mono:(angle, distance)}. Same pair, three different pictures.'),
    ('3-D', 'Three, and something has to give',
     '{mono:(lng, lat, magnitude)} on a flat page: two go to position, the third to '
     'size, or colour. {mono:(r, g, b)} is three numbers you see as one colour.'),
], notes='The point of the three cards is the sentence under them: a chart is a decision '
         'about which dimension goes where. There is no fourth card because the fourth '
         'dimension is time, and that is the animation slide at the end of the next section. '
         'From 2025 s28–33, which the deck review says to keep; it is the only part of that '
         'deck worth carrying forward.'))

S.append(content('05 · VECTORS', 'A vector is a list with a meaning per position', [
    '{mono:(hour, height)} — first the hour, then the metres. Swap them and the picture '
    'is nonsense, so the **order is part of the meaning**.',
    '',
    'In Python it is a **tuple**: a list you do not change. Every dot on the right is one.',
    '',
    '{muted:Week 2\'s rings read (knot, deg) — speed and direction — which is the same idea '
    'in polar form.}',
], figure=F.tide_day(), body_size=30,
   caption='24 vectors, drawn where they say to draw them',
   notes='Keep it to the one idea: a vector is not an arrow in physics class, it is a list '
         'where position carries meaning. (hour, height) and (knot, deg) are both vectors '
         'and they mean completely different pictures. Tuple versus list is a footnote — if '
         'asked: round brackets, cannot be changed after it is made, which is what you want '
         'for a coordinate.'))

S.append(code_slide('05 · TRANSFORMATIONS', 'Three rules, three lines each',
                    'from math import cos, sin\n\n'
                    'shape = [(0, 0), (100, 0), (50, 80)]\n\n'
                    'def move(p, dx, dy):\n'
                    '    return (p[0] + dx, p[1] + dy)\n\n'
                    'def scale(p, k):\n'
                    '    return (p[0] * k, p[1] * k)\n\n'
                    'def rotate(p, a):\n'
                    '    return (p[0] * cos(a) - p[1] * sin(a),\n'
                    '            p[0] * sin(a) + p[1] * cos(a))\n\n'
                    'moved = [move(p, 70, 40) for p in shape]',
                    figure=F.transforms(),
                    caption='the faint triangle is the original · a is in radians, so 0.5 is about 29°',
                    notes='Three functions, each one a rule about a single point, and the last '
                          'line is the loop that applies one of them to every point — the same '
                          'shape as D1 and D2. Say that the comprehension is a loop written on '
                          'one line and nothing more; they will meet it in the tutorial. rotate '
                          'turns about the origin, not about the shape, which is why the '
                          'triangle swings away from the corner — that is the usual surprise '
                          'and the reason move-rotate-move back is a thing. These names are the '
                          'names in pfad/week03/tide_clock.py.'))

S.append(exercise('05 · D5 · MOVE THE SHAPE', 'Predict the three points', [
    'One rule, applied to every point by a loop written on one line.',
    '',
    '**Say the three pairs out loud before you run it.** Then fill in the blank.',
], code='shape = [(0, 0), (100, 0), (50, 80)]\n\n'
        'def move(p, dx, dy):\n'
        '    return (p[0] + dx, p[1] + dy)\n\n'
        '# move every point 10 across and 20 down\n'
        'print([___ for p in shape])',
   expect='[(10, 20), (110, 20), (60, 100)]',
   hint='move(p, 10, 20)',
   notes='Thirty seconds, and the prediction is the exercise — the arithmetic is trivial and '
         'that is deliberate. What they are practising is reading a comprehension: for each p '
         'in shape, do this, collect the answers. If someone writes a for loop with append '
         'instead, it is correct and the check will pass it; say so, and say the one-liner is '
         'what they will be handed by an assistant.'))

S.append(content('05 · MATRICES', 'Those three rules have one name', [
    'Rotate-and-scale together is four numbers in a 2×2 table, and the table **is** the '
    'transformation. Put the numbers in, get the moved point out.',
    '',
    '- Matplotlib, CSS and p5.js all call it {mono:transform}. Same idea, three spellings.',
    '- Chaining two of them — rotate, then scale — is one multiplication, done once, '
    'then applied to every point.',
    '',
    '{muted:You do not need the multiplication rule this week. You need to recognise the '
    'word when a library or an assistant uses it.}',
], bg=INK, body_size=32,
   notes='One slide, not five, and no worked matrix multiplication — the 2025 deck spent six '
         'on it and the review says that is where the room fell off. If someone asks how '
         'translation fits in a 2x2 table: it does not, you need a 3x3 with a row of '
         '(0, 0, 1) — homogeneous coordinates — and that is a footnote for anyone who wants '
         'it after class, not a slide.'))

S.append(figure_slide('05 · BENT', 'The same 24 numbers, bent into a circle', F.tide_clock(),
                      caption='the clock is to_xy(hour, height) applied to every pair · '
                              'midnight at the right, the day running clockwise',
                      notes='Spend a minute here; it is the hinge of the deck. Ask which one '
                            'is better and refuse to answer: the line shows you that the tide '
                            'came back, the clock shows you that a day is a cycle, and the '
                            'clock makes the two highs sit opposite each other, which the line '
                            'cannot. Then the claim: a chart type is a transformation. Bar, '
                            'line, pie, polar, map — each is a different function from your '
                            'numbers to a position on the page.'))

S.append(exercise('05 · D6 · POLAR TO XY', 'Round, into flat', [
    'The clock in two lines: the hour decides the **angle**, the height decides the '
    '**radius**. {mono:cos} and {mono:sin} turn that pair back into x and y.',
    '',
    'One full turn is 24 hours, and a full turn is {mono:2 * math.pi}. Fill in the angle.',
], code='import math\n\n'
        'def to_xy(hour, height):\n'
        '    angle = ___\n'
        '    r = height * 100\n'
        '    return (round(r * math.cos(angle), 2),\n'
        '            round(r * math.sin(angle), 2))\n\n'
        '# hour 6 is 1.14 m, hour 12 is 1.35 m\n'
        'print(to_xy(6, 1.14))\n'
        'print(to_xy(12, 1.35))',
   expect='(0.0, 114.0)\n(-135.0, 0.0)',
   hint='hour / 24 * 2 * math.pi',
   notes='The two answers are quarter turns, so they come out clean: hour 6 is a quarter of '
         'the way round and lands straight down the y axis, hour 12 is half way and lands on '
         'the negative x axis. If the room is quick, ask why the y of hour 6 is positive when '
         'it is drawn at the bottom — because screen y counts downwards, which is the one '
         'thing that catches everyone. to_xy is the name the tutorial uses in tide_clock.py, '
         'where the angle is written radians(90 - hour / 24 * 360) so midnight sits at the top '
         'and the day runs clockwise, like a clock. Same transformation, one quarter turn; the '
         'ROTATE knob in that file is the quarter turn made visible.'))

S.append(content('05 · WEEK 2 WAS THIS', 'The rings you ran last week were this', [
    '[tides.py](https://github.com/sd5913/pfad/blob/2026/week02/tides/tides.py) in week 2 drew twenty-four rings of tidal current. Every one of them:',
    '',
    '- a circle — {mono:to_xy} in a loop, 200 times round',
    '- {mono:scale} — ring {mono:n} drawn at {mono:(n + 1) / 24} of full size',
    '- {mono:move} — to the centre of the window',
    '- then each vertex pushed by one {mono:(knot, deg)} vector from the data',
    '',
    '{muted:You ran it without knowing that. Open pfad/week02/tides/tides.svg again.}',
], figure=F.tide_clock('tide-clock-solo', pair=False), body_size=28,
   caption='the same construction, one ring, the tide height instead of the current',
   notes='Ninety seconds, and it is a callback, not new material — the room ran that script '
         'in the week 2 tutorial and most of them changed a knob. The payoff is that the four '
         'words on this slide are the four things they just learned, and they were in the '
         'code all along. Put tides.svg on the projector from the repo if the wifi holds: '
         'github.com/sd5913/pfad/blob/2026/week02/tides/tides.svg.'))

# ───────── 6 · simple rules, complex results — 2025 s39–51, back as live sketches ─────────
# Three p5.js sketches run in the html deck (the pptx and the PDF show the stills in
# deck/assets/sketches/); the two drills are Python, like every other drill this term.

DOUBLE_JS = '''let start, steps;
function setup() {
  createCanvas(600, 600); noLoop();
  start = createSlider(0, 360, 100, 0.1, 'start');
  steps = createSlider(1, 60, 12, 1, 'steps');
}
function dot(a) {                 // an angle, as a point
  return [300 + 250 * cos(radians(a)),
          300 - 250 * sin(radians(a))];
}
function draw() {
  background(255); stroke(0); noFill();
  circle(300, 300, 500);
  let a = start.value();
  for (let i = 0; i < steps.value(); i++) {
    let b = (a * 2) % 360;        // the rule
    let [x1, y1] = dot(a), [x2, y2] = dot(b);
    stroke(214, 89, 29); line(x1, y1, x2, y2);
    fill(0); circle(x1, y1, 9);
    if (i < 8) text(nf(a, 1, 1), x1 + 8, y1 - 8);
    a = b;
  }
}'''

# One more step every second, until someone touches a slider.
DOUBLE_EXTRA = '''let touched = false;
document.addEventListener('pointerdown', function (e) { if (e.target && e.target.type === 'range') touched = true; });
if (window._dblTimer) clearInterval(window._dblTimer);
window._dblTimer = setInterval(function () {
  if (touched || !steps) return;
  steps.value(steps.value() % 60 + 1);
  steps.elt.dispatchEvent(new Event('input'));
}, 900);'''

JULIA_JS = '''let cr, ci;
function setup() {
  createCanvas(600, 600); noLoop(); pixelDensity(1);
  cr = createSlider(-1.5, 0.5, 0, 0.01, 'c, real');
  ci = createSlider(-1, 1, 0, 0.01, 'c, imaginary');
}
function stays(x, y, a, b) {      // 30 times: square, add c
  for (let i = 0; i < 30; i++) {
    [x, y] = [x * x - y * y + a, 2 * x * y + b];
    if (x * x + y * y > 4) return false;   // it left
  }
  return true;
}
function draw() {
  let a = cr.value(), b = ci.value();
  loadPixels();
  for (let py = 0; py < 600; py++)
    for (let px = 0; px < 600; px++) {
      let x = (px - 300) / 150, y = (300 - py) / 150;
      let v = stays(x, y, a, b) ? 0 : 255;
      let k = 4 * (py * 600 + px);
      pixels[k] = pixels[k + 1] = pixels[k + 2] = v;
      pixels[k + 3] = 255;
    }
  updatePixels();
}'''

JULIA_COLOUR_JS = '''let cr, ci;
function setup() {
  createCanvas(600, 600); noLoop(); pixelDensity(1);
  cr = createSlider(-1.5, 0.5, -0.4, 0.01, 'c, real');
  ci = createSlider(-1, 1, 0.6, 0.01, 'c, imaginary');
}
function gone(x, y, a, b) {       // steps before it leaves
  for (let i = 0; i < 30; i++) {
    [x, y] = [x * x - y * y + a, 2 * x * y + b];
    if (x * x + y * y > 4) return i;
  }
  return 30;                      // never: it is in the set
}
function draw() {
  let a = cr.value(), b = ci.value(); loadPixels();
  for (let py = 0; py < 600; py++)
    for (let px = 0; px < 600; px++) {
      let n = gone((px - 300) / 150, (300 - py) / 150, a, b);
      let k = 4 * (py * 600 + px), v = n == 30 ? 0 : 60 + n * 6;
      pixels[k] = v * 1.1; pixels[k + 1] = v * 0.75;   // black,
      pixels[k + 2] = v * 0.4; pixels[k + 3] = 255;    // to orange
    }
  updatePixels();
}'''

# Not on a code panel: the page's ↗ shows it. Left: the c-plane, 0 iterated 40 times for
# every c. Right: the Julia set of the c under the mouse, 2 px blocks so a move redraws fast.
MANDEL_JS = '''let re = -0.4, im = 0.6, map, pal = [];
function gone(x, y, a, b, n) {         // steps before it leaves, or n
  for (let i = 0; i < n; i++) {
    [x, y] = [x * x - y * y + a, 2 * x * y + b];
    if (x * x + y * y > 4) return i;
  }
  return n;
}
function setup() {
  createCanvas(1200, 600); noLoop(); pixelDensity(1);
  for (let n = 0; n <= 40; n++) {           // black, to orange
    let v = n == 40 ? 0 : 60 + n * 4.5;
    pal[n] = [min(255, v * 1.1), v * 0.75, v * 0.4];
  }
  map = createImage(600, 600); map.loadPixels();   // every c, once
  for (let py = 0; py < 600; py++)
    for (let px = 0; px < 600; px++) {
      let n = gone(0, 0, (px - 450) / 200, (300 - py) / 200, 40);
      let k = 4 * (py * 600 + px);
      [map.pixels[k], map.pixels[k + 1], map.pixels[k + 2]] = pal[n];
      map.pixels[k + 3] = 255;
    }
  map.updatePixels();
}
function draw() {
  image(map, 0, 0);
  loadPixels();                                    // the Julia set of c
  for (let py = 0; py < 600; py += 2)
    for (let px = 600; px < 1200; px += 2) {
      let n = gone((px - 900) / 150, (300 - py) / 150, re, im, 30);
      let [r, g, b] = pal[n == 30 ? 40 : Math.round(n * 4 / 3)];
      for (let dy = 0; dy < 2; dy++)
        for (let dx = 0; dx < 2; dx++) {
          let k = 4 * ((py + dy) * 1200 + px + dx);
          pixels[k] = r; pixels[k + 1] = g; pixels[k + 2] = b; pixels[k + 3] = 255;
        }
    }
  updatePixels();
  stroke(0); strokeWeight(2); fill(255);
  circle(450 + re * 200, 300 - im * 200, 12);      // this c, on the map
  noStroke(); fill(0); rect(600, 0, 600, 36); fill(255); textSize(20);
  text('c = ' + nf(re, 1, 2) + (im < 0 ? ' - ' : ' + ') + nf(abs(im), 1, 2) + ' i', 616, 25);
}
function mouseMoved() {
  if (mouseX >= 0 && mouseX < 600 && mouseY >= 0 && mouseY < 600) {
    re = (mouseX - 450) / 200; im = (300 - mouseY) / 200; redraw();
  }
}
function mouseDragged() { mouseMoved(); }'''

S.append(section('06', 'Simple rules, complex results',
                 'Double an angle. Square a point. Add c.',
                 notes='Fifteen minutes, and the only stretch of the day with no data in it. '
                       'The point is the one the artist path of assignment 2 needs: a rule of '
                       'one line, run on its own result, makes a picture nobody could draw by '
                       'hand. Back from the 2025 deck (s39–51), as three sketches you can '
                       'drag instead of five slides of algebra.'))

S.append(code_slide('06 · DOUBLE THE ANGLE', 'Take an angle. Double it. Again.', DOUBLE_JS,
                    caption='Double the angle, back onto the circle, again. 120: two points forever. '
                            '90: stuck at 0 after three. 100: a seven-point star. 100.1: the same '
                            'star for eight steps, then anywhere.',
                    code_size=19,
                    sketch=live('double-angle', DOUBLE_JS, 600, 600,
                                hint='it steps on its own · drag start', extra=DOUBLE_EXTRA),
                    notes='JavaScript on the slide because the browser is, and the shape is the '
                          'loop from D1: once per step, one rule at the end. Let it step on its '
                          'own for ten seconds, then drag start to 120 (two points), 90 (three, '
                          'then stuck at 0), 100 (a seven-point star). Then 100.1 and steps to 60: '
                          'the same star for eight steps, then it comes apart. Say the word: '
                          'chaos is not randomness, it is a rule that doubles every error. That '
                          'is also why a weather forecast is worth nothing past ten days. The '
                          'drill next is the same rule in Python.'))

S.append(exercise('06 · D7 · DOUBLE IT', 'Which angles come back?', [
    'A circle is 360 degrees; {mono:%} keeps a doubled angle on it.',
    '',
    '**Say the six numbers before you run it.** Then fill in the blank.',
    '',
    'Now start at 90. Then 100. Then 100.1 — how many steps before it stops looking like 100?',
], code='angle = 120\n\n'
        'for step in range(6):\n'
        '    print(angle)\n'
        '    angle = ___   # double it, stay on the circle',
   expect='120\n240\n120\n240\n120\n240',
   hint='angle * 2 % 360',
   notes='Two minutes. 120 and 240 for ever: periodic. 90: 180, 0, 0, 0 — it falls onto a '
         'fixed point. 100: seven values round and round. 100.1 matches 100 to the first '
         'decimal for eight steps and is nowhere near it by twelve: the doubling doubles the '
         'error too, and that is the whole of chaos in five lines. If someone asks: every '
         'whole number of degrees comes back eventually; it is the fractions of a degree that '
         'never settle. Do not go further than that.'))

S.append(code_slide('06 · SQUARE, THEN ADD c', 'Every point on the plane, thirty times', JULIA_JS,
                    caption='Squaring doubles the angle and squares the length: the x·x − y·y line. '
                            'c = 0 is a disc. Drag c: −1 pinches it into beads; −0.4 + 0.6i (the '
                            'still) grows arms; further out, dust.',
                    code_size=18,
                    sketch=live('julia', JULIA_JS, 600, 600, hint='drag c · the disc bends'),
                    notes='The doubling of the angle, now for every point of the plane at once, '
                          'and with a length: squaring a point doubles its angle and squares its '
                          'distance from 0. That is the one line with x·x − y·y in it, and it is '
                          'all the complex numbers this course needs. With c = 0 the room can '
                          'predict the picture: inside the circle shrinks to 0 (black), outside '
                          'leaves (white). Then drag c, real to −1, slowly: the disc pinches into '
                          'a string of beads, each a point that comes back every two steps. Then '
                          'imaginary to 0.6, real to −0.4: arms. Then real to 0.4: dust, because '
                          'now even 0 leaves. The set of points that stay is a Julia set, and the '
                          'code is nine lines longer than the drill. The still in the pptx is '
                          'c = −0.4 + 0.6i; the html deck starts at 0.'))

S.append(code_slide('06 · ADD COLOURS', 'How fast a point leaves is a colour', JULIA_COLOUR_JS,
                    caption='Same rule; gone() counts the steps before a point leaves, and the count '
                            'is a colour: black for never, brighter the longer it stayed. The '
                            'outside now shows how close it came.',
                    code_size=18,
                    sketch=live('julia-colour', JULIA_COLOUR_JS, 600, 600, hint='drag c · try −0.8 + 0.16i'),
                    notes='Two changes from the previous slide, point at each: stays became gone '
                          'and returns a count instead of true or false; the pixel takes a shade '
                          'from its count, black for never, orange for nearly. Everything in '
                          'the picture that is not black is the outside, coloured by patience. '
                          'This is the picture the 2025 deck showed as a matplotlib image; now it '
                          'is thirty lines they can read, and every number in it is a knob. Drag '
                          'c to −0.8 + 0.16i for the one on every poster.'))

S.append(exercise('06 · D8 · ADD c', 'Which c come back?', [
    'Python has {mono:i} built in: {mono:1j}. {mono:1j * 1j} is {mono:-1}, and '
    '{mono:z * z + c} works whether c is {mono:-1} or {mono:1j}.',
    '',
    '**Say the six values for c = -1 before you run it.** Then fill in the blank.',
    '',
    'Now c = 1. Then -2, 0.25, 1j. Which settle, which come back, which leave?',
], code='c = -1\nz = 0\n\n'
        'for step in range(6):\n'
        '    print(z)\n'
        '    z = ___   # square it, add c',
   expect='0\n-1\n0\n-1\n0\n-1',
   hint='z * z + c',
   notes='Two minutes. c = −1: 0, −1, 0, −1 — comes back every two steps. c = 1: 0, 1, 2, 5, '
         '26, 677 — leaves. c = −2: 0, −2, 2, 2, 2 — settles. c = 0.25: creeps towards 0.5 and '
         'never leaves, the edge. c = 1j: 0, 1j, (−1+1j), −1j, (−1+1j), −1j — comes back, and '
         'Python printed a complex number without being asked. The question on the next slide '
         'is this drill for every c at once.'))

S.append(sketch_slide('06 · MANDELBROT', 'Every c on the left is a picture on the right.',
                      live('mandelbrot', MANDEL_JS, 1200, 600, hint='move the mouse over the left picture'),
                      body=['Left: the drill for every c at once — start at 0, square, add c, forty times. '
                            'Black if it comes back, coloured by how fast it leaves. That is the Mandelbrot set. '
                            'Right: the Julia set of the c under your mouse. Inside the black it is one piece; '
                            'outside, it is dust.'],
                      caption='Mandelbrot, 1980, on an IBM at Yorktown Heights: the first picture of this set was a '
                              'line printer\'s asterisks. Every point of it is a whole picture; the rule is one line.',
                      notes='The payoff. Move the mouse along the real axis from −2 to 0.3 and watch the '
                            'right side: dust, beads, the disc, arms, dust again. Then into the top bulb '
                            '(around −0.1 + 0.75i): three arms, because points there come back every '
                            'three steps. The black on the left is D8 answered for every c; the picture '
                            'on the right is the slider slide for that c. Say it once, plainly: a rule of '
                            'one line, a loop, and a picture no hand could draw. Assignment 2\'s artist '
                            'path can be this: numbers from the sea as the c, or as the colours. Then '
                            'back to the tide: plotting.'))

# ───────────────────────── 7 · plotting ─────────────────────────
S.append(section('07', 'Plotting', 'The library runs the loop; you still choose the axes'))

S.append(code_slide('07 · MATPLOTLIB', 'Eight lines, and the loop is gone',
                    'import json\n'
                    'import matplotlib.pyplot as plt\n\n'
                    'd = json.load(open("data/tides-QUB-2026.json"))\n'
                    'row = d["data"][259]          # 17 September\n'
                    'heights = [float(v) for v in row[2:]]\n'
                    'hours = range(1, 25)\n\n'
                    'plt.plot(hours, heights)\n'
                    'plt.xlabel("hour")\n'
                    'plt.ylabel("metres above chart datum")\n'
                    'plt.savefig("out/tide-day.png", dpi=150)\n'
                    'plt.show()',
                    figure=F.tide_day(),
                    caption='the file comes from data/, the picture goes to out/ · both are committed',
                    notes='Walk down it once: open the cached file, take one row, turn the '
                          'text into numbers — the float() from D4, in a comprehension — and '
                          'hand two lists to plot. There is no loop on this slide and there '
                          'are twenty-four points on the right, which is the whole idea of a '
                          'library. The two lines to defend are xlabel and ylabel: an '
                          'unlabelled axis is the single commonest failure in assignment 2, '
                          'and it costs marks under Picture.'))

S.append(figure_slide('07 · FIVE WAYS', 'The same numbers, five ways', F.tide_ways(),
                      caption='a line · bars · the clock · thirty days overlaid · '
                              'September as a grid, one row per day, one cell per hour',
                      notes='The slide of the day — give it three minutes and make the room '
                            'do the work. Ask what each one is FOR. The line: did it come '
                            'back. The bars: which hour, exactly. The clock: a day is a cycle, '
                            'and the two highs are opposite. The thirty overlaid: how much the '
                            'days differ, and that they all cross at the same hours. The grid: '
                            'the fortnightly beat — the dark and light diagonal bands are '
                            'spring and neap tides, and you cannot see them in any of the '
                            'other four. Same file, five transformations, five different '
                            'questions answered. That is assignment 2 in one picture.'))

S.append(question('multiple_choice', 'When are the tides biggest?',
                  choices=['New and full moon', 'Half moon', 'The same all month',
                           'When it rains'],
                  eyebrow_text='07 · THE MOON · MULTIPLE CHOICE',
                  notes='A — new and full moon, when the Sun and the Moon pull in line and '
                        'their bulges add. Ask BEFORE the next slide: this is a prediction, '
                        'and the next slide is the data that judges it. Most rooms get this '
                        'right and are still surprised by how badly the model fits, which is '
                        'the point.'))

S.append(code_slide('07 · THE MOON', 'Five lines of astronomy',
                    'from datetime import date\n'
                    'from tides import load_year\n\n'
                    'NEW_MOON = date(2000, 1, 6)     # a known new moon\n\n'
                    'def moon_age(day):\n'
                    '    return (day - NEW_MOON).days % 29.53\n\n'
                    'days, ranges = [], []\n'
                    'for day, heights in load_year():\n'
                    '    if day.month != 9:\n'
                    '        continue\n'
                    '    days.append(day.day)\n'
                    '    ranges.append(max(heights) - min(heights))\n\n'
                    'plt.bar(days, ranges)\n'
                    'plt.savefig("out/moon.png")',
                    figure=F.tide_moon(),
                    caption='daily range against the day · the moon marks come from moon_age',
                    notes='The verification moment of the course, with the sea as the spec. '
                          'The model says biggest at new and full. The data says: biggest on '
                          '9 September at 1.92 m, which is two days BEFORE the model\'s new '
                          'moon on the 11th; smallest on the 18th at 1.10 m, near first '
                          'quarter; and the full-moon spring at the end of the month is '
                          'weaker than the new-moon one. Both are true. The lag is real — '
                          'water has inertia and Hong Kong\'s harbour geometry adds to it — '
                          'and 29.53 days is an average, so the model drifts by a day. Do not '
                          'smooth it away and do not apologise for it: the roughness is the '
                          'interesting part, and noticing it is the skill. The second import '
                          'is worth a beat: tides.py is a file they wrote, imported like any '
                          'library.'))

S.append(content('07 · THREE NUMBERS', 'Three numbers a point, and the map draws itself', [
    'Every earthquake of the last month: {mono:(lng, lat, magnitude)}.',
    '',
    '- Two numbers become **position** — longitude across, latitude up. That is the '
    'cheapest map projection there is, and it is a transformation you did not write.',
    '- The third becomes **size**. It could have been colour.',
    '',
    '{orange:Nobody drew the coastlines. The plate boundaries drew themselves.}',
], figure=F.quake_map(), body_size=28,
   caption='USGS, magnitude 2.5+, one month · 2,130 points, largest 6.7',
   notes='Thirty seconds on the projection: lng to x and lat to y stretches everything near '
         'the poles, which is why Alaska looks enormous — say it, because the honest caption '
         'is part of the mark. Then the real point: the shape on the page is not a decision '
         'anyone made, it is the data. That is the best argument for plotting numbers you '
         'have not looked at yet. The file is data/earthquakes-2026-09.csv in the tutorial, '
         'and earthquakes.py plays the month back day by day.'))

S.append(content('07 · A FRAME IS A FUNCTION OF TIME', 'Animation is a loop with a picture in it', [
    'One more number, one more dimension: {mono:i}, which frame it is.',
    '',
    '{mono:def frame(i):} draws the first {mono:i} hours — nothing else changes. '
    'The library calls it 24 times and saves the pictures in order.',
    '',
    '{muted:A function of time is all an animation is. The hand is the hour it is drawing.}',
], figure=F.tide_clock('tide-clock-solo', pair=False),
   sketch=live('tide-clock', TIDE_CLOCK_JS, 620, 620,
               hint='it sweeps the day · click to start it again', extra=TIDE_CLOCK_EXTRA),
   body_size=28,
   notes='Live in the html deck; the pptx and the PDF show the still, which is the same '
         'clock from section 05. Let it run a full cycle while you talk. The sketch is '
         'JavaScript because the browser is, but the shape is identical to the Python on the '
         'left — to_xy in a loop, drawn up to hour i. Say that out loud: they will meet the '
         'same idea in three languages this term and it is one idea. The next slide is the '
         'Python that makes the GIF.'))

S.append(code_panel('07 · MAKE IT MOVE', 'Ten lines, and it is a GIF', [
    'from matplotlib.animation import FuncAnimation',
    '',
    'fig, ax = plt.subplots()',
    '',
    'def frame(i):                  {muted:# i counts up: 0, 1, 2, ...}',
    '    ax.clear()',
    '    ax.plot(hours[:i], heights[:i])',
    '',
    'anim = FuncAnimation(fig, frame, frames=25, interval=80)',
    'anim.save("out/tide-clock.gif", writer="pillow")',
], caption='pfad/week03/animate.py · needs pillow, which the script block asks for',
   notes='Do not explain FuncAnimation, explain frame: it is a function whose only argument '
         'is which picture this is, and everything else follows. hours[:i] is "the first i of '
         'them" — the same square brackets as everything else, with a colon in. ax.clear() is '
         'the line people forget, and the symptom is a picture that gets steadily more solid. '
         'They run this in the workshop at 0:40.'))

# ───────────────────────── 8 · two paths ─────────────────────────
S.append(two_col('08 · TWO PATHS', 'Both of these are assignment 2', [
    '**The designer.** Pick the chart the dimensions ask for. Label the axes. '
    'One message per picture.',
    '',
    'Someone who was not in the room has to get the answer without you next to them.',
    '',
    '**The artist.** The numbers are material. Week 2\'s rings do not tell you the '
    'current at 14:00 and never meant to.',
    '',
    'The picture need not explain itself — but {orange:you still say where the numbers '
    'came from}, and they are still real measurements.',
], [
    'designer',
    '  one question, one picture',
    '  axes labelled, units named',
    '  the source, as a link',
    '',
    'artist',
    '  the numbers are the material',
    '  the rule is yours',
    '  the source, as a link',
    '',
    'both',
    '  it runs on somebody else\'s',
    '  machine, from a cached file',
], lang=None, right_size=26, left_size=28,
   notes='Two minutes. The 2025 deck closed on this and it is the best thing in it. The line '
         'that matters: the only clause both columns share is the source. An artistic piece '
         'made from numbers you invented is not this assignment — it is a nice thing that '
         'would get a poor mark, and saying that now is kinder than saying it in October. '
         'Point back at the word cloud from the first section while you say it.'))

S.append(content('08 · TWO PATHS · ONE EXAMPLE', 'What assignment 2 can look like', [
    'Week 2\'s current data, five days of it, with the two numbers the rings threw away '
    'put back: **longitude and latitude**. Every arrow returns to its place in the sea; '
    '120 hours become 120 frames, ten tides in ten seconds.',
    '',
    '- {mono:to_xy} — the bearing into a vector, as on the clock',
    '- {mono:to_pixel} — the round Earth onto the flat map tiles',
    '- {mono:frame(i)} — one hour into one picture',
    '',
    '[week03/currents.py](https://github.com/sd5913/pfad/blob/2026/week03/currents.py) · {mono:--drift} lets 2,500 specks of water ride the arrows '
    'instead. {orange:One published file, one picture nobody could draw by hand.}',
], image='currents-2026-09-14.png', fit='contain', body_size=28,
   caption='[github.com/sd5913/tidal-streams](https://github.com/sd5913/tidal-streams) — the finished repo · [sd5913.github.io/tidal-streams](https://sd5913.github.io/tidal-streams/) — the page, live',
   notes='Play out/currents.webp and then out/currents-drift.webp from the repo on the projector — '
         'the pptx only has the still. The point to make: nothing new was needed. Three '
         'functions the room has already read today, a loop, and a map fetched once and cached '
         'in data/ like everything else. The drift version is the same numbers with the rule '
         'changed: instead of drawing the arrow, follow it. That is the whole difference '
         'between the two paths, and it is one line of code.'))

S.append(two_col('08 · TWO PATHS · PUBLISHED', 'The page builds itself', [
    'The same arrows once more, as a **web page**: [currents_web.py](https://github.com/sd5913/pfad/blob/2026/week03/currents_web.py) writes one HTML '
    'file with {mono:folium}, and the browser does the drawing — pan, zoom, a play button.',
    '',
    'Open the file on your laptop. If it plays there, it plays anywhere.',
    '',
    'Then one workflow file from [assignments/pages.yml](https://github.com/sd5913/pfad/blob/2026/assignments/pages.yml): on every push, GitHub '
    'runs the {orange:same command you ran} and publishes the result at '
    '{mono:you.github.io/your-repo}.',
    '',
    '{mono:site/} is never committed. It is made fresh from {mono:data/} every time.',
], [
    'on:',
    '  push:',
    '    branches: [main]',
    '',
    'jobs:',
    '  build:',
    '    steps:',
    '      - uses: actions/checkout@v4',
    '      - uses: astral-sh/setup-uv@v6',
    '      - run: uv run currents_web.py',
    '      - uses: actions/upload-pages-artifact@v3',
    '        with: { path: site }',
    '  deploy:',
    '    needs: build',
    '    steps:',
    '      - uses: actions/deploy-pages@v4',
], lang=None, right_size=24, left_size=28,
   notes='Optional for assignment 2, and the first sight of the deployment spine the course '
         'runs on from week 8: a script that makes a thing, a workflow that runs the script, '
         'a URL. The two lines to say out loud: the workflow runs the same command they ran, so '
         '"works on my laptop" means a file that is not in the repo; and site/ is output, so it '
         'is gitignored and rebuilt. The right column is the real file with the permissions and '
         'names cut for the slide — the full one is in assignments/pages.yml, and it is running on '
         'github.com/sd5913/tidal-streams, whose page is live. Settings → Pages → '
         'Source: GitHub Actions is the one click GitHub does not do for them.'))

S.append(question('short_answer', 'Your phenomenon, and where its numbers come from.',
                  hint='One line. For example: rainfall · HKO daily extract · JSON.',
                  example='Not sure yet? Say the phenomenon on its own and we will find you a file.',
                  notes='Three minutes, and this is the most useful three minutes of the day. '
                        'Read a dozen aloud. Anyone whose line has a phenomenon and no source '
                        'gets the first fifteen minutes of the tutorial with a tutor and a '
                        'search box — that is the hard part of assignment 2 and it is much '
                        'cheaper to solve now than on 3 October. Answers come back to this '
                        'slide as a link after class.'))

# ───────────────────────── 9 · workshop ─────────────────────────
S.append(section('09', 'Workshop', 'Your numbers, your repo, your first picture'))

S.append(content('09 · WORKSHOP', 'The tutorial is in the repo', [
    'Everything for the next two hours is one folder in the course repo, and the '
    'walkthrough is its README:',
    '',
    '- [' + REPO + ' · week03/README.md](https://github.com/sd5913/pfad/blob/2026/week03/README.md)',
    '- {mono:git pull} brings it down; {mono:uv run tides.py} is the first thing it asks for. '
    'What {mono:uv run} does: [reference/uv.md](https://' + REPO + '/blob/2026/reference/uv.md).',
    '- No clone, or a lab machine you have not used? Download and double-click '
    '[setup.bat](https://github.com/ait4x/v915-setup/releases/latest/download/setup.bat).',
    '',
    '{muted:Everything in week03/ runs from the cached files in data/, so it works with the '
    'wifi off. Leave with a repo, a data file and one picture in it.}',
], notes='Put the README link on the board next to the slides URL. Same shape as week 2 s51. '
         'The wifi line is not a throwaway: thirty laptops fetching the USGS feed at once is '
         'exactly when the room stalls, and every script in week03 reads data/ first. '
         'Anybody who cannot pull is still stuck on week 1 — deal with them at the back.'))

S.append(timeline('09 · WORKSHOP', 'Two hours', [
    ('0:00', 'uv run tides.py', 'The year, cached to {mono:data/}, and today\'s 24 numbers as a text chart. D2 on the real file.'),
    ('0:15', 'One day, four ways', '[plot_day.py](https://github.com/sd5913/pfad/blob/2026/week03/plot_day.py), [tide_clock.py](https://github.com/sd5913/pfad/blob/2026/week03/tide_clock.py), [tide_month.py](https://github.com/sd5913/pfad/blob/2026/week03/tide_month.py), [moon.py](https://github.com/sd5913/pfad/blob/2026/week03/moon.py). Predict, run, change one knob.'),
    ('0:40', 'Make it move', '[animate.py](https://github.com/sd5913/pfad/blob/2026/week03/animate.py) sweeps the clock and writes a GIF into {mono:out/}.'),
    ('0:55', 'Three numbers', '[earthquakes.py](https://github.com/sd5913/pfad/blob/2026/week03/earthquakes.py) — a map sized by magnitude; [currents.py](https://github.com/sd5913/pfad/blob/2026/week03/currents.py) — week 2\'s arrows back on the map, moving.'),
    ('1:10', 'Same idea, messier', '[typhoons.py](https://github.com/sd5913/pfad/blob/2026/week03/typhoons.py) — an HTML table, wind against pressure.'),
    ('1:20', 'Your repo', 'Use the template, cache your file, one plot, the check, the URL on Canvas.'),
    ('1:50', 'Swap screens', 'Your plot on your screen, your neighbour\'s on theirs. One sentence each: what does it hide?'),
    ('1:55', 'Next week', 'Read [teaching PR #3](https://github.com/sd5913/teaching/pull/3). React or comment: what do you want more of?'),
], notes='The blocks that must happen are 0:00 and 1:20. Everything between them is a menu — '
         'a group that is flying can skip to their own data at 0:40 and a group that is stuck '
         'on git should be at 1:20 the whole time. moon.py is the one worth insisting on: it '
         'is the only script where the picture disagrees with the model, and that '
         'conversation is the point of the week. Every file has its knobs at the top and '
         'writes to out/ as well as showing a window. No ClassPoint in the tutorial: the room '
         'is run without the presenter login, so the record of the day is the URL on Canvas, '
         'and the plots come to the week 4 lecture as its opening image upload.'))

S.append(end('See you next week',
             'Week 4: interfaces. Assignment 2 is due Sunday 4 October.',
             '[' + SITE + '](https://' + SITE + '/)'))

# Links each question slide to the answers the room gave. Written after the class by
# classpoint.py's weekly.py, and a no-op until that file exists.
attach_reports(S, Path(__file__).resolve().parent / 'week03-reports.json')

DECK = {'title': f'{COURSE} · Week 3 — Numbers into pictures', 'pdf': f'{COURSE}-week03.pdf',
        'slides': S}
