"""
SD5913 · Week 04 — Interfaces: giving the work a surface.

The 2025 deck's strongest argument was the sequence from blocking input, through
polling, to callbacks. This deck keeps that sequence and puts it in the setting
students will use: a browser-facing interface, a small Streamlit app, and a FastAPI
service. Python syntax, pygame and local-model setup are not repeated here.
"""
from pathlib import Path

from deckgen import attach_reports
from deckgen.layouts import (title, agenda, content, cards, section, statement,
                             question, two_col, code_panel, timeline, end)

COURSE = 'SD5913'
SITE = 'sd5913.github.io/teaching'
EYE = 'SD5913 · WEEK 04'
S = []

# 00 · Landing and the work from last week
S.append(title(EYE, 'Interfaces', 'Giving the work a surface.'))
S.append(agenda(EYE, [
    'Your first plot — brought forward from the tutorial',
    'A picture becomes an interface',
    'Input, state, response',
    'Waiting, polling, callbacks',
    'The browser as an interactive surface',
    'A small Streamlit app',
    'A FastAPI service',
    'Write a test before the code',
    'Let GitHub run the tests and refresh the data',
    'Workshop — put a surface on your work',
]))
S.append(question('image_upload', 'Upload your first plot.',
                  hint='Caption, 50 characters or fewer: phenomenon · source',
                  notes='Open with the plot made in the week 3 tutorial. Give students a '
                        'minute to upload. Read captions rather than names. Ask what each '
                        'picture lets a viewer notice, then move to the question of what a '
                        'viewer can do with it.'))
S.append(content('SD5913 · WEEK 04 · WORDS', 'Words you will hear today', [
    '- **interface** — the part of a program a person can see and use.',
    '- **input** — information or an action a person gives the program.',
    '- **state** — what the program remembers between actions.',
    '- **event** — something that happens, such as a click or a new request.',
    '- **callback** — a function the program runs when an event happens.',
    '- **request / response** — a message sent to a service, and the reply it sends back.',
    '- **endpoint** — one address a service responds to.',
    '',
    '{muted:Every word from the slides, in plain language:} '
    '[sd5913.github.io/teaching/glossary.html](https://' + SITE + '/glossary.html)',
], body_size=30, notes='Point out the glossary; do not read the definitions aloud. The '
                         'important distinction is between an event (the click) and a '
                         'callback (the code that runs because of it).'))

# 01 · From picture to interface
S.append(section('01', 'Give it a surface', 'A viewer can look, choose, and change something'))
S.append(statement('A picture shows a result. An interface lets someone act on it.',
                   eyebrow_text='01 · THE SHIFT',
                   notes='Use the uploaded plots as the starting point. A surface does not '
                         'need many controls. One meaningful choice can make the viewer part '
                         'of the work.'))
S.append(cards('01 · THE SHIFT', 'What can a viewer do?', [
    ('look', 'See the result', 'A chart, image, map, sound, or moving picture.'),
    ('choose', 'Set an input', 'A date, threshold, colour, place, or mode.'),
    ('change', 'See a response', 'The program updates what is shown.'),
], notes='Ask for examples from the plots on the upload slide. Keep the focus on an action '
         'and the response it should cause.'))
S.append(two_col('01 · A SMALL SPEC', 'Describe one interaction', [
    'Start with a sentence a person can test:',
    '',
    '“When I choose a month, the chart shows only that month.”',
    '',
    'It names an action, a change in the program, and an observable result. That is enough '
    'to begin building.',
], [
    'action  →  choose a month',
    'state   →  selected month',
    'rule    →  keep matching rows',
    'result  →  redraw the chart',
], lang=None, notes='This is the same specification habit used in the earlier assignments: '
         'state what must happen so another person can check it.'))

# 02 · Input, state and response
S.append(section('02', 'Input, state, response', 'The pattern behind an interactive program'))
S.append(cards('02 · THE PATTERN', 'Three parts of an interaction', [
    ('01 · input', 'A person acts', 'Click, type, choose, move, speak, or send a request.'),
    ('02 · state', 'The program remembers', 'The selected value, current page, or current result.'),
    ('03 · response', 'The surface changes', 'Update a label, redraw a chart, return data, play sound.'),
], notes='Trace each part on one example. A control without a visible response is hard to '
         'understand; a response without a remembered state cannot build on the last action.'))
S.append(code_panel('02 · TRACE THE CHANGE', 'Same data, different choice', [
    'month = "September"',
    'visible_rows = [row for row in rows if row.month == month]',
    'draw_chart(visible_rows)',
], caption='The interface chooses which rows reach the chart.',
    notes='This is schematic Python, not a complete app. Point to the value that changes '
          '(month), then the derived rows, then the redraw.'))
S.append(content('02 · WHAT COUNTS AS STATE?', 'State is what the next action needs', [
    '- A selected month is state if the next redraw uses it.',
    '- A typed message is state if the reply refers to it.',
    '- A counter is state if each click changes the next value.',
    '',
    'Ask: **what must the program remember for the next response to make sense?**',
], notes='Distinguish stored state from a value that can be recomputed. A design decision '
         'about state is also a design decision about what users can revisit or change.'))

# 03 · From waiting to events (the carried-forward 2025 spine)
S.append(section('03', 'Waiting is not interaction', 'Why input, polling, and callbacks behave differently'))
S.append(content('03 · THE STARTING POINT', 'A script usually runs from top to bottom', [
    'It starts, performs its steps, and finishes. The person chooses the input before the '
    'run, or the program asks and waits.',
    '',
    'With a blocking input call, the program stops at that line until a person answers.',
    '',
    '{orange:While it waits, that same flow of code cannot update the picture.}',
], notes='The 2025 deck introduced this through input(). Keep the idea, without another '
         'Python basics block: waiting in the middle of a single sequence pauses the rest '
         'of that sequence.'))
S.append(two_col('03 · BLOCKING INPUT', 'One line waits', [
    'The program reaches the question and stops there. The person answers; the program '
    'continues.',
    '',
    'Good for a simple command-line conversation. Awkward when the same program must keep '
    'drawing, listening, or responding to other actions.',
], [
    'name = input("Name? ")',
    'print("Hello", name)',
], notes='Ask what the program can do between the prompt appearing and the answer arriving. '
         'The answer: nothing else along this execution path.'))
S.append(statement('A screen that must keep moving cannot stop to ask.',
                   eyebrow_text='03 · THE PROBLEM',
                   notes='Pause here. This is the problem the rest of this section solves.'))
S.append(content('03 · APPROACH 1', 'Check again and again: polling', [
    'A loop checks for input at regular intervals, then updates the picture.',
    '',
    '- Check often: the response feels quick.',
    '- Check less often: the response can feel delayed.',
    '- Do too much between checks: the next check is late.',
], notes='The 2025 slides used a 60 frames-per-second game as the concrete case. At 60 fps '
         'a frame has about 16.7 ms; use it to make the time budget tangible, not as a '
         'promise that every program can meet it.'))
S.append(code_panel('03 · POLLING', 'The repeated check', [
    'while running:',
    '    events = check_for_events()',
    '    update_state(events)',
    '    draw_frame()',
], caption='The idea behind a game loop; library details are hidden.',
    notes='Do not teach this as a Python recipe. Trace the repeated cycle: collect events, '
          'change state, draw. Ask what happens if update_state takes too long.'))
S.append(cards('03 · A TIME BUDGET', 'A frame has a deadline', [
    ('60 fps', 'About 16 ms', 'One frame must be ready before the next is due.'),
    ('too much work', 'The loop overruns', 'The picture stutters; checks arrive late.'),
    ('slow work', 'Move it elsewhere', 'Do not freeze the interaction while it runs.'),
], notes='The simple loop explains the problem. Real systems use scheduling, worker threads '
         'or asynchronous work as appropriate; the key is keeping slow work from blocking '
         'the response the person is waiting for.'))
S.append(content('03 · APPROACH 2', 'Describe what should happen on an event', [
    'Instead of asking “is there a click yet?” every moment, the program registers what to '
    'do when a click happens.',
    '',
    'The browser or interface toolkit watches for the event. When it arrives, it calls the '
    'function attached to it.',
    '',
    '{orange:Event: the click. Callback: the response code.}',
], notes='Callbacks move the waiting and watching into the environment built to do it. The '
         'program describes a response; it does not need to spin in a loop asking whether '
         'something happened.'))
S.append(code_panel('03 · CALLBACK', 'One action, one response', [
    'button.on_click(update_chart)',
    '',
    'def update_chart(event):',
    '    selected_month = month_picker.value',
    '    chart.show(rows_for(selected_month))',
], caption='Pseudocode: each toolkit names events and callbacks differently.',
    notes='This is deliberately pseudocode. Do not claim the method names are shared across '
          'libraries. The pattern is portable: connect an event to a response.'))
S.append(two_col('03 · THE TRADE', 'Polling and callbacks', [
    'Polling is direct and visible: check, update, draw. It suits a continuous simulation '
    'where each frame has work to do.',
    '',
    'Callbacks suit discrete events: a click, key press, completed request, or timer. The '
    'environment calls your code when the event arrives.',
], [
    'continuous motion  →  loop',
    'button click       →  callback',
    'network reply      →  callback',
    'slow computation   →  keep off the UI thread',
], lang=None, notes='Neither pattern is universally better. Choose based on whether the '
         'program continuously advances or reacts to separate events.'))
S.append(two_col('03 · A CALLBACK FROM WEEK 01', 'Stay in flow', [
    'In week 1, this was a picture of a semester: keep going while the semester is on, '
    'choose a problem, and respond to how it feels.',
    '',
    'Now the loop has a meaning. A program can keep checking and updating, or it can let '
    'events call the response. Week 13 runs the semester loop as code.',
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
    '        simplify(problem)',
], right_size=22,
   notes='This is the week 1 “Stay in flow” slide, revisited as promised after while loops '
         'and repeated checks have a meaning. The full original also tries a skill upgrade '
         'and sleeps; this shorter view keeps the loop and the decision visible. Week 13 '
         'runs the semester model as code.'))

# 04 · Browser, client and server
S.append(section('04', 'The browser is a surface', 'Pages can respond to people, not only send them elsewhere'))
S.append(content('04 · FROM HYPERTEXT', 'A click can do more than change pages', [
    'A link can take you to another document. A button can change something on the page '
    'you are already viewing.',
    '',
    'Browsers provide familiar controls, draw text and images, and run code in response to '
    'events. That makes the browser a flexible home for interactive work.',
], notes='2025 introduced the shift from hypertext to interactive content. Keep that useful '
         'distinction, and move quickly from static links to controls that affect state.'))
S.append(two_col('04 · TWO PROGRAMS', 'A browser can ask a service for help', [
    'The **client** is the program in the browser. The **server** receives a request and '
    'sends a response.',
    '',
    'The client can draw the interface. The server can load data, save work, or perform '
    'computation that should not happen in the browser.',
], [
    'person',
    '  ↓ action',
    'browser (client)',
    '  ↓ request',
    'service (server)',
    '  ↑ response',
    'browser updates',
], lang=None, notes='Use the arrows as a conversation. A service is not the interface itself; '
         'it supplies a capability or data to the client.'))
S.append(cards('04 · REQUEST / RESPONSE', 'A web request has a shape', [
    ('address', 'Where to ask', 'A URL identifies the service and the resource.'),
    ('method', 'What to do', 'GET reads; POST sends information to be processed.'),
    ('response', 'What comes back', 'A status and a body, often JSON data.'),
], notes='Keep this at the level needed to read the examples. HTTP has more methods and '
         'details; the important idea is that requests and replies have a structure.'))
S.append(code_panel('04 · A SERVICE', 'A tiny FastAPI example', [
    'from fastapi import FastAPI',
    '',
    'app = FastAPI()',
    '',
    '@app.get("/hello")',
    'def hello():',
    '    return {"message": "Hello"}',
], caption='GET /hello → JSON: {"message": "Hello"}',
    notes='This is the shape of a small API, not a complete installation recipe. The '
          'decorator connects an address and method to a function. FastAPI turns the returned '
          'dictionary into a JSON response.'))
S.append(content('04 · ADDRESS AND RESULT', 'One endpoint can serve one clear purpose', [
    '- **GET /tides** — return the available tide data.',
    '- **GET /tides?month=9** — return data for a chosen month.',
    '- **POST /notes** — send a note to be saved or processed.',
    '',
    'An endpoint is a small agreement: send this kind of request here, and expect this kind '
    'of response.',
], notes='The examples are a design sketch, not a deployed service. A good endpoint has a '
         'clear job and a response shape the client can use.'))

# 05 · Streamlit and the surface
S.append(section('05', 'A surface in Python', 'Streamlit turns a script into a small web interface'))
S.append(content('05 · STREAMLIT', 'A quick way to put controls beside a result', [
    'Streamlit provides text, buttons, selectors, charts and other page elements from a '
    'Python script.',
    '',
    'It is useful for prototypes, data tools and class demonstrations: place a control, '
    'use its value, and show the result.',
    '',
    '{muted:Its execution model is specific to Streamlit. It is not how every web interface works.}',
], notes='The 2025 deck called Streamlit “a library for HTML interfaces”, which hid its '
         'distinctive rerun behavior. Be explicit: Streamlit is convenient for a quick app, '
         'but its model should not stand in for the browser event loop.'))
S.append(code_panel('05 · STREAMLIT', 'A selector and a chart', [
    'import streamlit as st',
    '',
    'month = st.selectbox("Month", months)',
    'rows = [r for r in data if r.month == month]',
    'st.line_chart(rows, x="day", y="height")',
], caption='The chosen month determines which rows are shown.',
    notes='Walk through the same interaction model from slide 8. The widget provides an '
          'input; the script uses its value; the chart displays a response.'))
S.append(content('05 · HOW STREAMLIT RUNS', 'A changed control reruns the script', [
    'When a user changes a widget, Streamlit runs the script again from top to bottom. The '
    'widget value is available during that run.',
    '',
    'That makes simple apps easy to write. For values that must persist between runs, '
    'Streamlit provides session state.',
    '',
    '{orange:This is a framework choice, not a general rule for interactive programs.}',
], notes='Name the trade clearly. Rerunning a script is Streamlit’s design; a browser app '
         'written with JavaScript usually handles an event with a callback and updates part '
         'of the page. Neither description should be mistaken for all web programming.'))
S.append(two_col('05 · REMEMBERING', 'When the value must persist', [
    'A rerun starts the script again. If a value should survive that rerun, store it in '
    'session state rather than in a temporary local variable.',
    '',
    'This is one reason to keep the interaction small: decide what should be remembered, '
    'and when it should reset.',
], [
    'if "count" not in st.session_state:',
    '    st.session_state.count = 0',
    '',
    'if st.button("Add one"):',
    '    st.session_state.count += 1',
    '',
    'st.write(st.session_state.count)',
], notes='Illustrates the session state pattern from Streamlit. It is not a general Python '
         'or browser feature. Ask what happens on a page refresh or in a different session.'))

# 06 · TDD and assignment automation
S.append(section('06', 'Test the promise', 'Write a check before the implementation'))
S.append(content('06 · FROM SPEC TO TEST', 'A test makes one promise checkable', [
    'Week 2 asked: **what should this code do, and what evidence would convince you?** '
    'A test turns one answer into a check the computer can repeat.',
    '',
    'For the assignment, test a small rule in your own data work — for example, selecting '
    'the rows for one month. Use a tiny fixture you can inspect by eye.',
    '',
    '{orange:Keep network requests out of unit tests. The test should give the same answer every time.}',
], notes='Connect to week 2’s spec and week 3’s cached data. Tests should check our code '
         'against known input, not ask a live service for whatever it happens to return today.'))
S.append(code_panel('06 · TEST FIRST · RED', 'Say what the selection must do', [
    'from transform import select_month',
    '',
    'def test_select_month_keeps_matching_rows():',
    '    rows = [{"month": 9, "day": 17},',
    '            {"month": 10, "day": 1}]',
    '    assert select_month(rows, 9) == [rows[0]]',
], caption='Run week04/tdd/test_transform.py before implementing the function.',
    notes='Read the assertion as a sentence: when the input has September and October, '
          'selecting September returns only the first row. Write and run this test before '
          'implementing select_month. Its first failure is useful evidence.'))
S.append(code_panel('06 · IMPLEMENT · GREEN', 'Write the smallest rule that passes', [
    'def select_month(rows, month):',
    '    return [row for row in rows if row["month"] == month]',
    '',
    '# see week04/transform.py',
], caption='Then change the code; run the same test again.',
    notes='The sequence is red, green, refactor: see the test fail for the right reason, '
          'make the smallest change that passes, then improve the code while keeping the '
          'test green. This is test-driven development (TDD), not merely testing after you finish.'))
S.append(cards('06 · TEST THE BOUNDARY', 'Separate your code from the service', [
    ('known input', 'Fixture', 'A few rows saved with the test; no internet needed.'),
    ('your rule', 'Unit test', 'Check filtering, parsing, or a calculation.'),
    ('outside system', 'Refresh step', 'Fetch separately, then check the new file shape.'),
], notes='Tests for the data transformation are deterministic. A refresh can fail because '
         'the publisher is offline or changes its format; report that failure without making '
         'all tests depend on the network.'))
S.append(content('06 · A CHECK ON EVERY PUSH', 'GitHub Actions can repeat the check', [
    'An Action starts a job on GitHub when an event happens. For a repo with tests, run '
    'them on every push so the result is visible beside the commit.',
    '',
    '- Week 3 already used an Action to rebuild and publish a page.',
    '- Assignment 2’s template already checks the repo shape.',
    '- A test workflow checks whether your own code still meets its promises.',
], notes='Connect to week 3’s pages.yml workflow and the assignment template’s check.yml. '
         'These checks answer different questions: publish a result, check submission shape, '
         'and test program behavior.'))
S.append(code_panel('06 · THE EVENT', 'Run the tests after each push', [
    'name: Tests',
    'on: [push]',
    'permissions:',
    '  contents: read',
    'jobs:',
    '  test:',
    '    runs-on: ubuntu-latest',
    '    steps:',
    '      - uses: actions/checkout@v6',
    '      - uses: astral-sh/setup-uv@v6',
    '      - run: uv run --with pytest python -m pytest week04/tests',
], caption='Save as .github/workflows/tests.yml',
    notes='This is intentionally small: push is the event, GitHub supplies a Linux machine, '
          'the repository is checked out, uv is installed, and pytest runs. In a real repo, '
          'adjust the test command and dependency setup to match its files.'))
S.append(content('06 · REFRESH ON PURPOSE', 'Tests should not quietly change your data', [
    'The raw source belongs in {mono:data/} so the assignment can be rerun later. A refresh '
    'is separate and deliberate: fetch a new snapshot, validate it, then commit the changed file.',
    '',
    'Use a manual {mono:workflow_dispatch} while you are developing. Add a schedule only '
    'when you have a reason for the data to keep changing.',
    '',
    '{muted:Keep the old snapshot in Git history; never replace the only copy without a check.}',
], notes='This balances fresh data with reproducibility. A scheduled run can surprise a '
         'student or consume a provider’s rate limit, so begin with a manual trigger. The '
         'commit records what changed and when.'))
S.append(two_col('06 · REFRESH · VALIDATE · SAVE', 'The refresh workflow', [
    'Run manually: fetch a snapshot, run the tests, then commit data/ if validation passes.',
    '',
    'The refresher writes to a temporary file, checks the response, then replaces the '
    'cached file only if it is valid.',
    '',
    '{orange:contents: write} lets the workflow push its commit.',
    '',
    'Full runnable examples and exact commands: '
    '[pfad/week04/README.md](https://github.com/sd5913/pfad/blob/2026/week04/README.md).',
], [
    'on: workflow_dispatch',
    'permissions:',
    '  contents: write',
    'jobs:',
    '  refresh:',
    '    runs-on: ubuntu-latest',
    '    steps:',
    '      - uses: actions/checkout@v6',
    '      - uses: astral-sh/setup-uv@v6',
    '      - run: uv run week04/refresh_data.py',
    '      - run: uv run --with pytest python -m pytest week04/tests',
    '      - run: git config user.name "github-actions[bot]"',
    '      - run: git config user.email "41898282+github-actions[bot]@users.noreply.github.com"',
    '      - run: git add week03/data/tides-QUB-2026.json',
    '      - run: git diff --cached --quiet || git commit -m "Refresh data"',
    '      - run: git push',
], right_size=22, lang=None,
    notes='This matches the runnable refresh action in pfad/week04/refresh_data.py: it writes '
          'to a temporary file, checks the HKO structure, then atomically replaces the cache. '
          'The workflow needs contents: write because it pushes a commit. The unit tests use '
          'fixtures and stay offline; refresh_data.py separately checks that the fetched file '
          'has the expected 365 rows and 26 fields. If the request, validation or tests fail, '
          'the job stops before committing. The complete workflow is linked from the tutorial.'))
S.append(content('06 · A GREEN TICK', 'A test is evidence, not proof', [
    'A green run means these checks passed on this version of the repo.',
    '',
    '- Did the test check the promise you meant to make?',
    '- Does it cover an empty file or a missing value?',
    '- Does the refreshed data still have the fields your code reads?',
    '',
    'Read the test and its result. Do not treat the tick as a quality score.',
], notes='Week 2’s verification principle applies to tests too. An agent can write a test '
         'that agrees with its own bug; check the expectation against the spec and a known example.'))

# 07 · Choosing a structure and workshop
S.append(section('07', 'Choose the structure', 'A fast prototype or a client and service'))
S.append(cards('07 · CHOOSE A TOOL', 'Match the structure to the work', [
    ('quick prototype', 'Streamlit', 'A compact Python app, controls and results together.'),
    ('separate client', 'Browser UI', 'The browser owns the surface and event callbacks.'),
    ('shared capability', 'FastAPI', 'A service exposes data or actions through endpoints.'),
], notes='These can also be combined. A browser interface can call a FastAPI service; '
         'Streamlit can also be a client of a service. Choose based on what needs to be '
         'separate and who will use it.'))
S.append(content('07 · BUILD FROM THE SPEC', 'One control, one clear response', [
    'Take a plot from the tutorial and add one meaningful choice:',
    '',
    '- Which value can a viewer change?',
    '- What state does the program need to remember?',
    '- What visible response proves the choice worked?',
    '',
    'Start with the sentence: **When I ___, the interface ___.**',
    '',
    '{muted:Runnable code, tests, and Actions:} '
    '[pfad/week04/README.md](https://github.com/sd5913/pfad/blob/2026/week04/README.md)',
], notes='Keep the scope small enough to finish. One interaction that works and can be '
         'explained is a better prototype than a page of controls with no clear purpose.'))
S.append(two_col('07 · FIND THE FILE', 'The working folder is part of the app', [
    'The 2025 tutorial ended with PATH and the current working directory. Keep the useful '
    'debugging question: **which folder is this process using?**',
    '',
    'A relative path is resolved from the process working directory. If an app cannot find '
    'its data file, check where it was started before changing the filename.',
], [
    'project/',
    '├── app.py',
    '├── data/',
    '│   └── tides.csv',
    '└── requirements.txt',
], lang=None, notes='Port the durable idea from the 2025 path tutorial, not its stale screenshot '
         'sequence. A launch command, project structure and relative file path belong together. '
         'This becomes relevant again when running a local web app.'))
S.append(timeline('07 · WORKSHOP', 'Two hours', [
    ('0:00', 'Open the week 3 project', 'Run the plot from its project folder. Find the cached file it reads.'),
    ('0:10', 'Write one interaction', '“When I ___, the interface ___.” Name input, state and visible response.'),
    ('0:25', 'Test a data rule first', 'Use a tiny fixture. Run it red, implement the rule, run it green.'),
    ('0:50', 'Build a Streamlit surface', 'Add one control beside the result. Change one value and observe the rerun.'),
    ('1:15', 'Read the FastAPI example', 'Trace a request to a function and the JSON response back to a client.'),
    ('1:25', 'Add a test Action', 'Create the push workflow, commit it, then read the run in the Actions tab.'),
    ('1:45', 'Try a manual refresh', 'Fetch a new snapshot, validate it, and keep the old data if a check fails.'),
    ('1:55', 'Swap and close', 'A partner tries the control. Keep Assignment 2 moving; Assignment 3 begins in week 6.'),
], notes='This is a working session plan, not a promise that the course repo already contains '
         'a week04 starter. Confirm the tutorial files before class and replace the first-step '
         'instructions with their final paths. The learning goal is a single working '
         'interaction and a clear explanation of its input, state and response.'))
S.append(content('07 · ASSIGNMENT 2', 'Keep the data picture moving', [
    'Assignment 2 is due **Sunday 4 October, 23:59**.',
    '',
    'This week’s interface work can help you explore your data, but the assignment still '
    'needs its own clear question, source, picture, README and PROCESS.md.',
    '',
    '{muted:Do not add controls just to make a plot look like an app. Each one should help someone see or ask something.}',
], notes='This is a reminder, not a new assignment brief. The deadline and requirements are '
         'from the existing assignment 2 brief in week 3.'))
S.append(end('Give it a surface', 'Next week: sound, microphones, and live transcription.',
             '[' + SITE + '](https://' + SITE + '/)'))

attach_reports(S, Path(__file__).resolve().parent / 'week04-reports.json')

DECK = {'title': f'{COURSE} · Week 4 — Interfaces', 'pdf': f'{COURSE}-week04.pdf',
        'slides': S}
