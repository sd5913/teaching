"""
SD5913 · Week 04 — Interfaces: one control, one clear response.

The deck keeps the useful 2025 sequence from blocking input to polling and
callbacks, but makes one runnable 2026 example the spine: choose a day and see
that day's 24 Quarry Bay tide heights. It contrasts a Streamlit app that reads
a local data file with a static browser frontend that calls the FastAPI service.
The endpoint, transformations and tests are in sd5913/pfad/week04.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import week04_figures as F

from deckgen import Image, T, PAPER, attach_reports
from deckgen.layouts import (title, agenda, content, cards, section, statement,
                             question, two_col, code_panel, exercise, timeline, image_full,
                             figure_slide, end)

COURSE = 'SD5913'
SITE = 'sd5913.github.io/teaching'
EYE = 'SD5913 · WEEK 04'
S = []


def finalist_gallery(eyebrow_text, title_text, items, notes=''):
    """Three submitted marks in a labelled, equal-width row."""
    s = content(eyebrow_text, title_text, [], notes=notes)
    s.els = s.els[:2]  # keep the eyebrow and title; replace the empty body
    gap = 48
    col_w = (1680 - gap * 2) // 3
    for i, (mark, path, stats) in enumerate(items):
        x = 120 + i * (col_w + gap)
        s.els += [
            Image(x, 340, col_w, 330, path, 'contain'),
            T(x, 680, col_w, 48, f'Mark {mark}', 'xbold', 34, '#000B1C', align='c'),
            T(x, 738, col_w, 112, stats, 'body', 27, '#5C6470', lh=1.35, align='c'),
        ]
    return s

def annotated_code(eye, heading, explanation, lines, notes='', lang='py'):
    """A short explanation beside a large, legible excerpt."""
    return two_col(eye, heading, explanation, lines, notes=notes,
                   left_size=34, right_size=32, lang=lang)


# 00 · Landing and the work from last week
cover = title(EYE, 'Interfaces', 'One control, one clear response.')
cover.els.insert(0, Image(1080, 150, 720, 720, 'week04-image-api-wave.png', 'contain'))
cover.notes = 'The wave is an illustration generated through an image API. Return to it in section 04 to reveal the request and response.'
S.append(cover)
S.append(agenda(EYE, [
    'Your first plot, and the final vote for our mark',
    'Turn a picture into something a person can use',
    'One action travels through a Streamlit app',
    'Waiting, polling and callbacks',
    'APIs: tide records and a generated image',
    'One test, the workshop and Assignment 2',
]))
S.append(question('image_upload', 'Upload your first plot.',
                  hint='Caption, 50 characters or fewer: phenomenon · source',
                  notes='Open with the plot made in the week 3 tutorial. Give students one '
                        'minute to upload. Show two or three responses and ask one question: '
                        'what could a viewer choose that would change this picture? Carry '
                        'their answers into the working app in section 01.'))
S.append(finalist_gallery('SD5913 · THE MARK', 'The class vote: three finalists', [
    ('38', 'mark-38.jpeg', 'Score 4.04\n28 wins · 5 losses · 33 comparisons'),
    ('04', 'mark-04.jpg', 'Score 3.40\n27 wins · 6 losses · 33 comparisons'),
    ('18', 'mark-18.png', 'Score 3.01\n26 wins · 7 losses · 33 comparisons'),
], notes='These are the current Bradley–Terry standings from the registry. '
         'The next slide is the final class vote; collect one response per '
         'student and announce the result.'))
vote = question('multiple_choice', 'Which mark should represent SD5913?',
                  choices=['A — Mark 38', 'B — Mark 04', 'C — Mark 18'],
                  eyebrow_text='THE FINAL THREE',
                  notes='This is the deciding ClassPoint poll. Each student gets one vote. '
                  'The option with the most votes wins. If tied, the higher Bradley–Terry '
                  'rank wins (38, then 04, then 18), so the result is always decisive.',
                  size=64)
vote.els[1].y = 190
vote.els[1].h = 100
# Keep the question and ClassPoint choice metadata; draw the choices under the images.
vote.els = vote.els[:2]
gallery = []
for i, (letter, mark, path) in enumerate([
    ('A', '38', 'mark-38.jpeg'), ('B', '04', 'mark-04.jpg'), ('C', '18', 'mark-18.png'),
]):
    gap = 48
    col_w = (1680 - gap * 2) // 3
    x = 120 + i * (col_w + gap)
    gallery += [
        Image(x, 340, col_w, 360, path, 'contain'),
        T(x, 730, col_w, 64, f'{letter} — Mark {mark}', 'xbold', 38, '#000B1C', align='c'),
    ]
vote.els.extend(gallery)
S.append(vote)
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
S.append(statement('“When I choose a day, the chart shows that day’s 24 hourly tide heights.”',
                   eyebrow_text='01 · THE PROMISE', size=88, bg=PAPER,
                   notes='A testable promise, carried from the week 2 spec habit into the week 3 data. '
                         'Ask students to name the input, state and response.'))
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
         'The month narrows the local rows; the day is the interaction we are tracing.'))
S.append(annotated_code('02 · THE EXACT CODE', 'The value reaches the chart', [
    '**17** — the selector returns a day.', '',
    '**One record** — select_day finds it.', '',
    '**24 heights** — the chart draws them.',
], [
    'day = st.selectbox(',
    '    "Day", [r["day"] for r in rows]',
    ')',
    'record = select_day(rows, day)',
    'chart = pd.DataFrame(',
    '    {"Height (m)": record["heights"]},',
    '    index=range(1, 25),',
    ')',
    'st.line_chart(chart)',
], notes='Excerpt from pfad/week04/app.py; row shortened to r to fit. '
         'https://github.com/sd5913/pfad/blob/2026/week04/app.py '
         'Trace the integer, dictionary and list. Imports and data loading omitted.'))
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
S.append(annotated_code('03 · POLLING', 'Check, update, draw. Repeat.', [
    'A loop checks input during each frame.', '',
    'At **60 fps**, the whole cycle has about **16.7 ms**.', '',
    'A slow update delays the next check and the next frame.',
], [
    'while running:',
    '    events = check_for_events()',
    '    update_state(events)',
    '    draw_frame()',
], notes='Pseudocode: a useful structure for continuous motion. These function names '
    'describe jobs; they are not built-in Python functions.'))
S.append(figure_slide('03 · THE BROWSER EVENT LOOP', 'An event becomes a visible change',
    F.event_cycle(), notes='A conceptual sequence, not browser source code. Events queue; '
    'callbacks run; rendering happens when the browser has an opportunity. A long callback '
    'delays both the next event and the next paint.'))
S.append(annotated_code('03 · CALLBACK', 'Connect an event to a function', [
    '**Event:** the click.', '',
    '**Callback:** update_chart.', '',
    'The toolkit calls your function when the event arrives.',
], [
    'def update_chart(event):',
    '    day = day_picker.value',
    '    record = select_day(rows, day)',
    '    chart.show(record)',
    '',
    'button.on_click(update_chart)',
], notes='Pseudocode: each toolkit names events differently. Define the function before '
    'registering it. The diagram on the previous slide shows where this callback fits.'))
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
    '',
    '[Week 1 source](https://github.com/sd5913/teaching/blob/week04/deck/week01.py)',
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

# 04 · Frontends and a data backend
S.append(section('04', 'Frontend and backend', 'Two examples, two data paths'))
S.append(figure_slide('04 · FRONTEND / BACKEND', 'Two places, one conversation',
    F.frontend_backend(), notes='Frontend means the code providing the surface in the browser; '
    'backend means the service running elsewhere. Trace the outward request and returning JSON. '
    'Choosing a day can then use the month already downloaded. A browser app need not call '
    'the server for every action. GitHub Pages hosts files; Cloudflare runs this service.'))
S.append(figure_slide('04 · STREAMLIT · ONE PYTHON APP', 'Streamlit connects the two sides for you',
    F.streamlit_path(), notes='The earlier app reads the bundled file. It does not call our '
    '/tides API, but browser and Streamlit process still communicate over the network. '
    'When running locally, browser and server happen to be on the same laptop.'))
S.append(annotated_code('04 · FRONTEND · JAVASCRIPT', 'Ask, read, then draw', [
    '**Ask** for September records.', '',
    '**Read** the JSON reply.', '',
    '**Draw** one day in the browser.',
], [
    'const response = await fetch(',
    '  API + "/tides?month=9"',
    ');',
    'const rows = await response.json();',
    'const record = rows[0];',
    '',
    'drawChart(record.heights);',
], lang='js', notes='Teaching excerpt. API is the deployed Worker origin; drawChart is a '
    'placeholder for the frontend chart function, not a browser built-in. This shows day 1. '
    'A day selector can choose another record from rows. await yields while the request runs; '
    'the browser can handle other work. A complete app also checks response.ok and handles errors.'))
S.append(annotated_code('04 · MEET FASTAPI', 'A Python function, available at a URL', [
    '**FastAPI** is a Python framework for building HTTP APIs.', '',
    'Connect a URL to a function. Return a dictionary or list as JSON.', '',
    'It also builds an interactive **/docs** page. [Try our tide API](https://sd5913-week04-tides.venetanji.workers.dev/docs).',
], [
    'from fastapi import FastAPI',
    '',
    'app = FastAPI()',
    '',
    '@app.get("/hello")',
    'def hello():',
    '    return {"message": "Hello"}',
], notes='Introduce the framework before the tide endpoint. GET /hello calls hello(). '
    'FastAPI serialises the dictionary as JSON. This minimal example is complete as main.py. '
    'Run with uv run --with "fastapi[standard]" fastapi dev main.py; open '
    'http://127.0.0.1:8000/docs. Official reference: https://fastapi.tiangolo.com/tutorial/first-steps/'))
S.append(annotated_code('04 · BACKEND · PYTHON', 'Return the matching records', [
    '**GET /tides?month=9**', '',
    'FastAPI reads month as an integer from 1 to 12.', '',
    'Our function selects the records. FastAPI sends them as JSON.',
], [
    '@app.get("/tides")',
    'def tides(',
    '    month: int = Query(ge=1, le=12)',
    '):',
    '    return select_month(',
    '        load_rows(), month',
    '    )',
], notes='The route from https://github.com/sd5913/pfad/blob/2026/week04/api.py, '
    'line-wrapped for projection. Imports and app setup omitted. Cloudflare runs it via '
    'workers.asgi.entrypoint(app); keep the adapter detail in the source walkthrough. '
    'A missing or invalid month gets a validation error rather than a successful data reply.'))
S.append(cards('04 · CONNECT THE TWO', 'Three things to check', [
    ('address', 'The right endpoint', 'The frontend asks the Worker URL for /tides?month=9.'),
    ('browser permission', 'The allowed origin', 'CORS lets the teaching site read the API response.'),
    ('response', 'The expected shape', 'Each record has a month, a day and 24 heights.'),
], notes='Open https://sd5913-week04-tides.venetanji.workers.dev/docs and try month 9. '
    'CORS is already configured in api.py for https://sd5913.github.io and local port 8000. '
    'An origin is scheme + host + port, without /teaching/. CORS is a browser reading rule, '
    'not authentication. Keep configuration code for troubleshooting, not a slide of middleware.'))
S.append(exercise('04 · LIVE DATA · PYTHON IN THE BROWSER',
                  'Ask the deployed API for September', [
    'Run the request. Find **how many days**, **which first date**, and **four heights** in the reply.',
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
    notes='This is a live request through Pyodide in the browser. The API allows the published '
          'teaching site and the local preview at http://127.0.0.1:8000. If the browser blocks '
          'it, check the page origin and deployed CORS response. Do not rerun repeatedly: this '
          'is one request for a month of committed data.'))
S.append(content('04 · AN API CAN MAKE SOMETHING', 'This image came back from an API', [
    'A prompt went out. Image data came back.', '',
    '**Prompt:** “Editorial paper sculpture of a tidal wave becoming a flowing ribbon…”', '',
    'Qwen Image 2.1 · ComfyUI',
], image='week04-image-api-wave.png', fit='contain', body_size=32,
    caption='Generated illustration · not measured tide data',
    notes='Made for this deck using an image generation endpoint. The exact prompt and parameters '
    'are committed beside the PNG, and scripts/image_api_example.py reproduces the request. '
    'This is an illustration: its wave shape is not derived from the Quarry Bay measurements.'))
S.append(figure_slide('04 · THE SAME REQUEST / RESPONSE PATTERN', 'A prompt goes in. An image comes back.',
    F.image_service(), notes='We used an authenticated POST to /v1/images/generations. '
    'The response format requested is b64_json; the script decodes it and saves a PNG. '
    'An image API extends what a program can do, just as the tide API supplies data. '
    'A public frontend should call your own backend, which holds the secret key.'))
S.append(annotated_code('04 · READ THE IMAGE REQUEST', 'Describe the job in JSON', [
    '**POST** sends a job to the service.', '',
    '**model** chooses the generator. **prompt** describes the image.', '',
    'The script reads the **API key** from its environment.',
], [
    '{',
    '  "model": "qwen-image-2.1",',
    '  "prompt": "Editorial paper ...",',
    '  "size": "1024x1024",',
    '  "n": 1,',
    '  "response_format": "b64_json"',
    '}',
], lang=None, notes='Prompt abbreviated for the slide. Full runnable standard-library example: '
    'scripts/image_api_example.py. Authentication is an Authorization: Bearer header, not part of '
    'this JSON. Never place the key in browser source or a public repo. Generation takes time: '
    'show a working state while waiting, then show the result or a useful error.'))
S.append(question('multiple_choice', 'In the tide app, what does the service send back?',
                  choices=['The finished chart', 'JSON records', 'The mouse click', 'The PowerPoint'],
                  eyebrow_text='04 · CLIENT AND SERVICE',
                  notes='B — JSON records. The client draws the chart. This distinction is '
                        'why the static browser UI can change without changing api.py.'))

# 05 · One test-first loop, against the API students have just seen
S.append(section('05', 'Test the API', 'One file. One feature. Red, then green.'))
S.append(code_panel('05 · RED · WRITE THE TEST FIRST', 'One file checks the API', [
    'def test_september_tides():',
    '    with urlopen(API) as response:',
    '        assert response.status == 200',
    '        rows = load(response)',
    '    first = rows[0]',
    '    assert (first["month"], first["day"]) == (9, 1)',
    '    assert len(first["heights"]) == 24',
    '    assert isinstance(first["heights"][0], float)',
], caption='[week04/tdd/test_api.py](https://github.com/sd5913/pfad/blob/2026/week04/tdd/test_api.py) · run first: watch it fail.',
    notes='This single Python file asks for September and checks status, the first date and '
          'the 24 numeric heights. It uses only the standard library. Run it against the local '
          'Worker while developing; before /tides exists, the request fails.'))
S.append(code_panel('05 · GREEN · ADD THE ROUTE', 'Return the data in that format', [
    '@app.get("/tides")',
    'def tides(month: int):',
    '    rows = load_rows()',
    '    return [row for row in rows if row["month"] == month]',
], caption='Source: [week04/api.py](https://github.com/sd5913/pfad/blob/2026/week04/api.py) · rerun [test_api.py](https://github.com/sd5913/pfad/blob/2026/week04/tdd/test_api.py).',
    notes='This small example shows the feature under test: return one month as a list of '
          'records, each with month, day and 24 heights. The real Worker uses a little more '
          'code to parse the committed source and validate the month. Keep the lesson on the '
          'feedback loop: test fails, add the route, test passes.'))
S.append(timeline('05 · THE LOOP', 'One promise, four steps', [
    ('01', 'Write the test', 'Say what response would convince you.'),
    ('02', 'See it fail', 'Read the failure: does it point to the missing feature?'),
    ('03', 'Add the route', 'Implement the smallest change that meets the promise.'),
    ('04', 'Run it again', 'The same test now passes.'),
], notes='Run against a local Worker where the feature is initially missing. A network failure '
    'alone does not show a missing implementation. The deployed completed API should already pass.'))

# 06 · Workshop: demos, adaptation, assignment time
S.append(section('06', 'Workshop', 'Try the demos, adapt an idea, then work on your assignment'))
S.append(content('06 · BEFORE YOU START', 'The tutorial is one continuous path', [
    'Use the first hour to try all the demo code: Streamlit with the local file, the browser/API '
    'request, the event-loop examples and the red-to-green API test.',
    '',
    'Then adapt one idea to your own project. Use the final half-hour to work on Assignment 2.',
    '',
    '[github.com/sd5913/pfad/tree/2026/week04](https://github.com/sd5913/pfad/tree/2026/week04)',
], notes='Open the README and use its commands for the demos. The branch link resolves after '
         'the PR merges; during class it is on 2026. Students should work from the repository root.'))
S.append(timeline('06 · WORKSHOP', 'Two hours', [
    ('0:00–1:00', 'Try every demo', 'Run the local-file Streamlit app, browser/API request, event-loop examples and red-to-green test. Change a value and inspect what happens.'),
    ('1:00–1:30', 'Adapt what you learned', 'Bring one idea into your own project: add a useful control, respond to an event, show data or write a small check.'),
    ('1:30–2:00', 'Work on Assignment 2', 'Last chance to ask tutors about your submission. Use the rest for your question, data, plot, README and PROCESS.md.'),
], notes='The first hour is for trying every demo in the lesson. Students then adapt one idea '
         'to their own work before spending the final half-hour on Assignment 2.'))
S.append(content('06 · ASSIGNMENT 2', 'Keep the data picture moving', [
    'Assignment 2 is due **Sunday 4 October, 23:59**.',
    '',
    'This interface can help you explore your data. The submitted work still needs its own '
    'question, source, picture, README and PROCESS.md.',
    '',
    '{muted:Every control should help someone see or ask something.}',
], notes='This is a reminder rather than a new brief. The deadline and requirements remain '
    'those in assignments/02-data-visualisation.md.'))
S.append(cards('06 · ASSIGNMENT 2 · TEMPLATE CLINIC', 'Read the check in three groups', [
    ('explain', 'README + process', '150+ words, the picture shown, and a meaningful PROCESS.md.'),
    ('reproduce', 'Code + data', 'Python parses, dependencies declared, raw data and picture committed.'),
    ('show progress', 'Commit history', 'At least three commits across two or more days.'),
], notes='Use sd5913/assignment-2-template. Its GitHub Action runs the same assignment check '
    'on every push. A green check confirms these conditions; a person still assesses the analysis.'))
S.append(code_panel('06 · ASSIGNMENT 2 · RUN IT LOCALLY', 'The same check, on your laptop', [
    'uv run https://raw.githubusercontent.com/sd5913/pfad/2026/assignments/check.py --assignment 2',
], caption='Run from your assignment repo. Read the result, fix one item, then push again.',
    lang=None, notes='Single-line command, so it can be copied on Windows or macOS. '
    'Source: https://github.com/sd5913/pfad/blob/2026/assignments/check.py'))
S.append(end('One control, one clear response',
             'No class on 1 October · Assignment 2 due 4 October.',
             '[' + SITE + '](https://' + SITE + '/)'))

attach_reports(S, Path(__file__).resolve().parent / 'week04-reports.json')

DECK = {'title': f'{COURSE} · Week 4 — Interfaces', 'pdf': f'{COURSE}-week04.pdf',
        'slides': S}
