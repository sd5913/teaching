"""
SD5913 · Week 04 — Interfaces: one control, one clear response.

The deck keeps the useful 2025 sequence from blocking input to polling and
callbacks, but makes one runnable 2026 example the spine: choose a day and see
that day's 24 Quarry Bay tide heights. The Streamlit client, FastAPI endpoint,
pure transformation and tests are the files in sd5913/pfad/week04.
"""
from pathlib import Path

from deckgen import attach_reports
from deckgen.layouts import (title, agenda, content, cards, section, statement,
                             question, two_col, code_panel, exercise, timeline, image_full,
                             end)

COURSE = 'SD5913'
SITE = 'sd5913.github.io/teaching'
EYE = 'SD5913 · WEEK 04'
S = []

# 00 · Landing and the work from last week
S.append(title(EYE, 'Interfaces', 'One control, one clear response.'))
S.append(agenda(EYE, [
    'The top three marks — choose the course winner',
    'Your first plot becomes something a person can use',
    'One action travels through a Streamlit app',
    'Waiting, polling and callbacks',
    'A service, a test and a two-hour workshop',
    'Assignment 2: read the template check',
]))
S.append(question('image_upload', 'Upload your first plot.',
                  hint='Caption, 50 characters or fewer: phenomenon · source',
                  notes='Open with the plot made in the week 3 tutorial. Give students one '
                        'minute to upload. Show two or three responses and ask one question: '
                        'what could a viewer choose that would change this picture? Carry '
                        'their answers into the working app on slide 6.'))
S.append(content('SD5913 · THE MARK', 'The class vote: three finalists', [
    '**1 · Mark 38** — score 4.04 · 28 wins / 5 losses · 33 comparisons',
    '**2 · Mark 04** — score 3.40 · 27 wins / 6 losses · 33 comparisons',
    '**3 · Mark 18** — score 3.01 · 26 wins / 7 losses · 33 comparisons',
    '',
    'Now choose the one mark that should represent the course.',
], body_size=30, notes='These are the current Bradley–Terry standings from the registry. '
                         'The next slide is the final class vote; collect one response per '
                         'student and announce the result.'))
S.append(question('multiple_choice', 'Final vote: which mark is the SD5913 mark?',
                  choices=['A — Mark 38', 'B — Mark 04', 'C — Mark 18'],
                  eyebrow_text='THE FINAL THREE',
                  notes='This is the deciding ClassPoint poll. Each student gets one vote. '
                        'The option with the most votes wins. If tied, the higher Bradley–Terry '
                        'rank wins (38, then 04, then 18), so the result is always decisive.'))
S.append(content('SD5913 · WEEK 04 · WORDS', 'Four words for one interaction', [
    '- **interface** — the part of a program a person can see and use.',
    '- **input** — information or an action a person gives the program.',
    '- **state** — what the program remembers between actions.',
    '- **response** — the visible result of an action.',
    '',
    '{muted:More words appear when they have a job:} '
    '[sd5913.github.io/teaching/glossary.html](https://' + SITE + '/glossary.html)',
], body_size=32, notes='Thirty seconds. Name the four parts students need to read the next '
                         'three slides. Event, callback, client and endpoint arrive later, '
                         'beside the examples that give them meaning.'))

# 01 · See the complete interaction first
S.append(section('01', 'The surface', 'See the complete interaction before opening the code'))
S.append(image_full('week04-streamlit.png', '01 · THE WORKING APP',
                    'Choose a day. See its 24 hourly tide heights.', fit='contain',
                    notes='This is the actual pfad/week04/app.py, not a mock-up. Ask students '
                          'to point to the input and the response before naming state. The '
                          'month first chooses the available rows; the day chooses one record.'))
S.append(statement('One control, one clear response.', eyebrow_text='01 · THE SCOPE',
                   notes='The app has two selectors because a year needs a month before a day, '
                         'but the promise being tested is deliberately smaller: changing the '
                         'day changes the 24 values in the chart.'))
S.append(two_col('01 · THE PROMISE', 'Describe one interaction', [
    'A person should be able to say what happened without reading the code:',
    '',
    '“When I choose a day, the chart shows that day’s 24 hourly tide heights.”',
    '',
    'That sentence gives the interface and the test one shared target.',
], [
    'input     day selector',
    'state     selected day',
    'rule      find that record',
    'response  draw 24 heights',
], lang=None, notes='Read the sentence once. Every example after this should point back to '
         'one of its four lines. This is also the first sentence in pfad/week04/README.md.'))
S.append(question('multiple_choice', 'After someone chooses day 17, what is the state?',
                  choices=['The mouse click', '17', 'The 24 plotted heights', 'The JSON file'],
                  eyebrow_text='01 · INPUT, STATE, RESPONSE',
                  notes='B — 17. The click is the event, 17 is the selected value the next '
                        'run uses, and the heights are the response. Ask why “the JSON file” '
                        'is data rather than the changing state of this interaction.'))

# 02 · Trace the exact Streamlit code
S.append(section('02', 'One action through the app', 'The selector supplies a value; the chart uses one record'))
S.append(cards('02 · THE PATH', 'Three parts of the interaction', [
    ('input', 'A person chooses', 'The day selector supplies 17.'),
    ('state', 'The app keeps the value', 'The current run sees day = 17.'),
    ('response', 'The surface changes', 'The chart draws that record.'),
], notes='Use the exact same day on every slide. Do not switch back to a month example. '
         'The month narrows the server response; the day is the interaction we are tracing.'))
S.append(code_panel('02 · THE EXACT CODE', 'The selector reaches the chart', [
    'day = st.selectbox(',
    '    "Day", [row["day"] for row in rows]',
    ')',
    'record = select_day(rows, day)',
    '',
    'chart = pd.DataFrame(',
    '    {"Height (m)": record["heights"]},',
    '    index=range(1, 25),',
    ')',
    'st.line_chart(chart)',
], caption='The same lines are in pfad/week04/app.py.',
    notes='Trace values rather than syntax: the selector returns an integer; select_day '
          'returns a dictionary; record["heights"] is a list of 24 floats; the DataFrame '
          'gives those floats an hour index; Streamlit draws them.'))
S.append(content('02 · STREAMLIT', 'A changed widget reruns the script', [
    'When someone changes a selector, Streamlit runs the script again from top to bottom.',
    '',
    'The widget keeps its selected value. During the new run, {mono:day} contains that value, '
    '{mono:select_day} returns a different record, and the chart is drawn again.',
    '',
    '{orange:This rerun model belongs to Streamlit. Other interfaces handle events differently.}',
], notes='Keep this concrete. No session_state example is needed because this app does not '
         'use it. The widgets preserve their values for this interaction. Session state can '
         'arrive later when students need a value that no widget owns.'))

# 03 · From waiting to events, compressed from the 2025 sequence
S.append(section('03', 'Waiting and events', 'Blocking input, a repeated check, or a response function'))
S.append(two_col('03 · BLOCKING INPUT', 'One line waits', [
    'A command-line prompt stops at {mono:input()} until a person answers.',
    '',
    'That works for a short conversation. It does not work for a screen that must keep '
    'drawing or respond to other actions while it waits.',
], [
    'name = input("Name? ")',
    'print("Hello", name)',
], notes='This is the durable idea from the 2025 deck. Ask what this execution path can do '
         'between the prompt appearing and the answer arriving: nothing.'))
S.append(code_panel('03 · POLLING', 'A loop checks repeatedly', [
    'while running:',
    '    events = check_for_events()',
    '    update_state(events)',
    '    draw_frame()',
], caption='A game loop checks, updates and draws again.',
    notes='At 60 frames per second, each cycle has about 16.7 ms. The loop is a useful '
          'pattern for continuous motion. If one update takes too long, input and drawing '
          'both arrive late.'))
S.append(code_panel('03 · CALLBACK', 'An event calls a response function', [
    'button.on_click(update_chart)',
    '',
    'def update_chart(event):',
    '    day = day_picker.value',
    '    chart.show(select_day(rows, day))',
], caption='Pseudocode: each toolkit names events differently.',
    notes='Event: the click. Callback: update_chart. The browser or toolkit watches for '
          'the event and calls the function. Say clearly that these method names are '
          'pseudocode; the next slide compares the patterns.'))
S.append(cards('03 · THREE PATTERNS', 'Match the response to the program', [
    ('command line', 'Wait', 'Ask once, then continue.'),
    ('continuous picture', 'Poll', 'Check input during every frame.'),
    ('discrete action', 'Callback', 'Run a function when an event arrives.'),
], notes='Streamlit offers a fourth implementation detail: a widget change triggers a '
         'rerun. Its visible interaction still has the same input, state and response.'))
S.append(two_col('03 · WEEK 01 REVISITED', 'The semester loop', [
    'In week 1, this was a picture of a semester: keep working while the semester is on, '
    'then respond to the current problem and state.',
    '',
    'Now the loop has a technical meaning. It checks a condition, updates values and '
    'decides what happens next.',
], [
    'while semester() == 1:',
    '    problem = current_problem()',
    '    try:',
    '        problem.solve()',
    '    except:',
    '        simplify(problem)',
], notes='This is a loop revisited, not a callback. The shorter excerpt keeps the callback '
         'section honest and avoids asking the room to read the full Week 1 program again.'))
S.append(question('multiple_choice', 'Which pattern best fits a browser button?',
                  choices=['Blocking input', 'A callback', 'A 60 fps loop', 'A file refresh'],
                  eyebrow_text='03 · WAITING AND EVENTS',
                  notes='B — a callback. A browser can attach a function to the click event. '
                        'A game may still poll for input; Streamlit reacts by rerunning the '
                        'script. The user-facing action can look similar while the program '
                        'structure differs.'))

# 04 · Client and service, using the deployed Python Worker
S.append(section('04', 'Client and service', 'The interface asks a Python Worker for one month of data'))
S.append(cards('04 · ONE REQUEST', 'The month crosses a boundary', [
    ('client', 'Streamlit asks', 'Send the selected month to the service.'),
    ('endpoint', 'GET /tides?month=9', 'The address and query identify the request.'),
    ('response', 'JSON records', 'One record per September day comes back.'),
], notes='Keep the vocabulary beside the running app. Streamlit is the person-facing '
         'client. FastAPI runs as a Cloudflare Python Worker. JSON is the response format.'))
S.append(code_panel('04 · THE CLIENT', 'Ask for one month', [
    'API = (',
    '    "https://sd5913-week04-tides.venetanji.workers.dev"',
    '    "/tides"',
    ')',
    '',
    'response = requests.get(',
    '    API, params={"month": month}, timeout=10',
    ')',
    'response.raise_for_status()',
    'rows = response.json()',
], caption='Exact extract from pfad/week04/app.py.',
    notes='Requests turns params into ?month=9. raise_for_status stops on an HTTP error. '
          'response.json turns the response body into Python lists and dictionaries.'))
S.append(code_panel('04 · THE SERVICE', 'Return the matching rows', [
    'from workers import asgi',
    '',
    '@app.get("/tides")',
    'def tides(month: int = Query(ge=1, le=12)):',
    '    return select_month(load_rows(), month)',
    '',
    'Default = asgi.entrypoint(app)',
], caption='GET /tides?month=9 returns September records.',
    notes='These are the exact route and Worker adapter in pfad/week04/api.py. Month is '
          'required and must be from 1 to 12. Cloudflare receives the request; the ASGI '
          'adapter passes it to FastAPI; FastAPI returns JSON and documents the endpoint.'))
S.append(cards('04 · PYTHON WORKER', 'Same FastAPI app, a different server', [
    ('code', 'FastAPI route', 'The Python function still defines the endpoint.'),
    ('adapter', 'ASGI entrypoint', 'Cloudflare connects a Worker request to the app.'),
    ('runtime', 'Pyodide at the edge', 'Python runs in WebAssembly inside a Worker isolate.'),
], notes='Locally, uvicorn can serve an ASGI app. On Cloudflare, workers.asgi supplies the '
         'server role. The route and the pure select_month rule do not change. Open '
         'pfad/wrangler.jsonc after this slide to show the main module and compatibility flag.'))
S.append(content('04 · ONE RECORD', 'The response already has the chart values', [
    '{mono:month 9 · day 17 · 24 hourly heights}',
    '',
    'The service returns data rather than a chart. The client chooses one daily record and '
    'decides how to draw its 24 heights.',
    '',
    '[Open the live FastAPI docs](https://sd5913-week04-tides.venetanji.workers.dev/docs) '
    'and try month 9.',
], body_size=30, notes='The record shape matches transform.parse_rows exactly. The ellipsis is '
                         'display shorthand; the real response contains all 24 floats.'))
S.append(exercise('04 · LIVE DATA · PYTHON IN THE BROWSER',
                  'Ask the deployed API for September', [
    'Run one Python request in the browser. Read the number of daily records, the first day, '
    'and its first four heights.',
], code='import json\nfrom pyodide.http import open_url\n\n'
        'url = (\n'
        '    "https://sd5913-week04-tides.venetanji.workers.dev"\n'
        '    "/tides?month=9"\n'
        ')\nresponse = open_url(url)\nrows = json.loads(response.read())\n\n'
        'first = rows[0]\n'
        'print(len(rows), "daily records")\n'
        'print("first:", first["month"], first["day"])\n'
        'print(first["heights"][:4])',
    eid='ask-the-deployed-api', rows=9,
    notes='This is a live request through Pyodide in the browser. The API must return '
          'Access-Control-Allow-Origin for https://sd5913.github.io. If the browser blocks '
          'it, the service has not picked up the CORS change yet. Do not rerun repeatedly: '
          'this is one request for a month of committed data.'))
S.append(question('multiple_choice', 'What crosses from the service to the client?',
                  choices=['The finished chart', 'JSON records', 'The mouse click', 'The PowerPoint'],
                  eyebrow_text='04 · CLIENT AND SERVICE',
                  notes='B — JSON records. The client draws the chart. This distinction is '
                        'the reason app.py can change the surface without changing api.py.'))

# 05 · Test the pure rule that connects the choice to the record
S.append(section('05', 'Test the promise', 'A tiny fixture checks the rule without a browser or network'))
S.append(cards('05 · TDD · THE LOOP', 'Red, green, refactor', [
    ('red', 'Describe one behavior', 'Write a small test and see it fail for the expected reason.'),
    ('green', 'Make it pass', 'Write the smallest clear implementation that satisfies the test.'),
    ('refactor', 'Improve the design', 'Clean up names or structure while every test stays green.'),
], notes='TDD is a short feedback loop, not a demand to predict an entire program. Red proves '
         'the test can detect the missing behavior. Green establishes the behavior. Refactor '
         'improves the code with the passing test as a safety net.'))
S.append(two_col('05 · TDD · WHY', 'What does test-first change?', [
    'Before coding, you must state the next observable behavior precisely.',
    '',
    'Small steps make failures easier to explain and mistakes easier to locate.',
    '',
    'The tests become executable examples of the promises the code already keeps.',
], [
    'TDD is most useful when:',
    '',
    '• the rule can be isolated',
    '• examples are easy to write',
    '• the expected result is clear',
    '',
    'Use a separate check for layout, network access and other outside systems.',
], lang=None, notes='Keep the claim proportionate: TDD helps shape testable rules and provides fast '
                    'feedback. It does not replace trying the interface. In this example we '
                    'extract select_day so its promise can be checked without Streamlit or FastAPI.'))
S.append(content('05 · FROM PROMISE TO TEST', 'The interface depends on one small rule', [
    'The visible promise says that choosing a day shows that day’s heights.',
    '',
    'The smallest rule underneath it is {mono:select_day(rows, day)}. Give it two known '
    'records and check that it returns the matching one.',
    '',
    '{orange:The test supplies its own rows. It does not open the app or contact the API.}',
], notes='Connect this to Week 2’s question: what should the code do, and what evidence '
         'would convince you? The fixture is small enough to inspect by eye.'))
S.append(code_panel('05 · TEST FIRST · RED', 'The expected record comes first', [
    'from transform import select_day',
    '',
    'def test_select_day_returns_the_matching_record():',
    '    rows = [',
    '        {"month": 9, "day": 17},',
    '        {"month": 9, "day": 18},',
    '    ]',
    '    assert select_day(rows, 17) == rows[0]',
], caption='Run week04/tdd/test_transform.py while select_day is still a stub.',
    notes='This is exactly the unfinished exercise in pfad/week04/tdd. See the failure for '
          'the right reason before writing the rule. Read the assertion aloud as a sentence.'))
S.append(question('multiple_choice', 'What should select_day(rows, 18) return?',
                  choices=['rows[0]', 'rows[1]', '18', 'Both rows'],
                  eyebrow_text='05 · READ THE TEST',
                  notes='B — rows[1]. Ask what a missing day should return before revealing '
                        'the implementation: this version returns None.'))
S.append(code_panel('05 · IMPLEMENT · GREEN', 'The smallest matching rule', [
    'def select_day(rows, day):',
    '    return next(',
    '        (row for row in rows if row["day"] == day),',
    '        None,',
    '    )',
], caption='The same function is used by app.py and the completed tests.',
    notes='next returns the first matching row. None is the result when the generator has '
          'no match. Run the test green, add the missing-day case, then refactor only while '
          'both expectations stay green.'))
S.append(cards('05 · TEST THE BOUNDARY', 'Keep outside systems out of the unit test', [
    ('known input', 'Fixture', 'Two records written beside the test.'),
    ('our rule', 'Unit test', 'Check which record select_day returns.'),
    ('outside system', 'Separate check', 'Fetch or refresh data elsewhere.'),
], notes='The unit test should answer the same way on every machine. The network refresh '
         'has its own validation and can fail without making the selection rule uncertain.'))
S.append(code_panel('05 · ON EVERY PUSH', 'GitHub repeats the completed tests', [
    'on: [push, pull_request]',
    'jobs:',
    '  test:',
    '    runs-on: ubuntu-latest',
    '    steps:',
    '      - uses: actions/checkout@v4',
    '      - run: uv run --with pytest python -m pytest week04/tests',
], caption='.github/workflows/week04-tests.yml (excerpt)',
    notes='The event starts a job, GitHub checks out the repository, then runs the tests. '
          'The complete workflow also pins Python and sets up uv.'))
S.append(content('05 · OPTIONAL REFRESH', 'Fresh data is a separate operation', [
    'The maintainer workflow runs manually:',
    '',
    '1. Fetch a new 2026 snapshot.',
    '2. Check all 365 dates, 26 fields and numeric heights.',
    '3. Run the offline fixture tests.',
    '4. Update the Week 03 source and the Worker snapshot.',
    '5. Commit only when every check passes.',
    '',
    '{muted:The full workflow is in pfad/.github/workflows/refresh-tides.yml.}',
], body_size=30, notes='This replaces the unreadable full YAML slide. The refresh is optional '
                         'reading after the core workshop. The validator now rejects missing '
                         'or duplicated dates, not merely the wrong number of rows.'))
S.append(content('05 · A GREEN TICK', 'Read the check as evidence', [
    'A green run means these expectations passed on this version of the repository.',
    '',
    '- Does the test describe the interaction you intended?',
    '- Does it check a missing day as well as a matching day?',
    '- Does the data validator check the dates and the values?',
    '',
    'Read the test and its result together.',
], notes='A green tick is useful evidence, but an agent can write a test that agrees with '
         'its own bug. Compare the assertion with the promise and a known example.'))

# 06 · Four workshop milestones rather than eight tiny columns
S.append(section('06', 'Workshop', 'Run it, trace it, test it, change it'))
S.append(content('06 · BEFORE YOU START', 'The tutorial is one continuous path', [
    'Keep the Streamlit page open while you trace its request to the deployed Worker.',
    '',
    'The completed code lives in {mono:week04/}. The deliberately unfinished test-first '
    'version lives in {mono:week04/tdd/}.',
    '',
    '[github.com/sd5913/pfad/tree/2026/week04](https://github.com/sd5913/pfad/tree/2026/week04)',
], notes='Open the README and use its commands. The branch link resolves after the PR merges; '
         'during class it is on 2026. Students should work from the repository root.'))
S.append(timeline('06 · WORKSHOP', 'Two hours', [
    ('0:00', 'Run the interaction', 'Start Streamlit. Change the day and watch the chart.'),
    ('0:30', 'Trace one choice', 'Follow day from the widget, through select_day, to the 24 heights.'),
    ('1:00', 'Test the rule', 'Run red. Implement select_day. Run green. Add the missing-day case.'),
    ('1:30', 'Change and explain', 'Add one visible behavior, test its rule, then swap with a partner.'),
], notes='Four blocks remain readable from the back of the room and match the README headings. '
         'The Python Worker is traced rather than built from scratch. The refresh workflow is optional.'))
S.append(content('06 · ASSIGNMENT 2', 'Keep the data picture moving', [
    'Assignment 2 is due **Sunday 4 October, 23:59**.',
    '',
    'This interface can help you explore your data. The submitted work still needs its own '
    'question, source, picture, README and PROCESS.md.',
    '',
    '{muted:Every control should help someone see or ask something.}',
], notes='This is a reminder rather than a new brief. The deadline and requirements remain '
    'those in assignments/02-data-visualisation.md.'))
S.append(two_col('06 · ASSIGNMENT 2 · TEMPLATE CLINIC', 'What does the check tell you?', [
    'Start from **sd5913/assignment-2-template**. Its GitHub Action runs the Assignment 2 check on each push.',
    '',
    'Run the same check locally from your repo:',
    '',
    'uv run https://raw.githubusercontent.com/sd5913/pfad/2026/assignments/check.py --assignment 2',
], [
    'It checks:',
    '• README: 150+ words and shows your picture',
    '• PROCESS.md: present and meaningful',
    '• Python parses; dependencies are declared',
    '• raw data in data/; picture committed',
    '• 3 commits across at least 2 days',
    '',
    'A green check confirms these conditions, not the quality of the analysis.',
], lang=None, notes='Open the template repository and its .github/workflows/check.yml. '
         'The workflow calls the same check.py script with --assignment 2. A red item tells '
         'you what to fix; push again to rerun it. Ask students to distinguish mechanical '
         'checks from the human question: does the picture reveal something about the data?'))
S.append(end('One control, one clear response',
             'Next week: sound, microphones and live transcription.',
             '[' + SITE + '](https://' + SITE + '/)'))

attach_reports(S, Path(__file__).resolve().parent / 'week04-reports.json')

DECK = {'title': f'{COURSE} · Week 4 — Interfaces', 'pdf': f'{COURSE}-week04.pdf',
        'slides': S}
