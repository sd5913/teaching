"""Thursday 26 November 2026. Visual course review, eSFQ and subject AMA."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from deckgen.core import DEEP_TEAL, LINE, Image, Rect, Slide, T, eyebrow
from deckgen.layouts import content, figure_slide, question, title
from week05_figures import frame_sequence
import week09_layouts as L
import week11_figures as TOOLS
import week12_figures as REVIEW
import week12_review_figures as VISUAL

EYE = 'SD5913 · THURSDAY 26 NOVEMBER 2026'
PIN = '92061c101aed3a83a4708a7e07766db8571ee197'
COURSE = 'https://github.com/sd5913/pfad/blob/2026'
COMPANION = f'https://github.com/sd5913/pfad/blob/{PIN}/week12'
ANT = 'https://www.anthropic.com/news/ipo-close'
NVIDIA = 'https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Board-Reinstates-Jensen-Huang-as-President-CEO-and-Board-Director/default.aspx'
ROCKSTAR = 'https://www.rockstargames.com/newswire/article/39akk424a9oo53/grand-theft-auto-vi-now-available'
ESFQ_IMAGE = 'https://images.edm.polyu.edu.hk/resource/beefree/5b8ce21a598aab0001db7d32/SFQ%20QR%20code%20and%20Instruction.png'
ESFQ = 'https://esfqprod.polyu.edu.hk/esfqstud/login.zul'
S = []
TIDE_LOOP = [
    'heights = [1.05, 2.19]',
    'for hour, height in enumerate(heights, start=1):',
    '    if height > 2:',
    '        print(hour, height)',
]


def week(number, label):
    return f'[{label}]({COURSE}/week{number:02}/README.md)'


def page(label, heading, lines, notes):
    S.append(content(label, heading, lines, body_size=44, notes=notes))


S.append(title(EYE, 'Programming concepts', 'Week-by-week reference and subject AMA',
               size=112, notes='0–0:30. Today we revisit the ideas that let us explain a program, predict what it will do and check the result. Keep one concept you want to ask about in mind for the AMA.'))
slide = L.page('Thoughts on GTA VI?',
    '0:30–2. Invite impressions from people who have played or watched it. '
    'What impressed or disappointed them? Which interaction or system would '
    'they like to understand? Follow an example into objects and state, '
    'input, animation, sound, simulation or delivery. Keep this an open '
    'design/computing discussion rather than a quiz or a claim that we have '
    'tested the game. The image is official launch artwork, not a gameplay '
    'screenshot. Rockstar\'s source announcement says the console version is '
    'available on PlayStation 5 and Xbox Series X|S. Source: ' + ROCKSTAR)
slide.cp = {'type': 'short_answer', 'hide_names': False, 'multiple': True}
slide.els.extend((
    eyebrow(120, 94, 'OPENING DISCUSSION · OUTSIDE QUIZ SCOPE'),
    Image(120, 320, 1040, 585, str(HERE / 'week12-assets/gta-vi-official.jpg'),
          'contain', url=ROCKSTAR),
    T(1250, 350, 550, 220, 'What impressed or disappointed you?',
      'bold', 52, DEEP_TEAL, lh=1.12),
    T(1250, 620, 550, 250, 'Which system would you like to understand?',
      size=48, lh=1.18),
    T(120, 925, 1040, 64, f'[Official Rockstar launch artwork]({ROCKSTAR})',
      size=36),
))
S.append(slide)
S.append(figure_slide('NEXT THURSDAY · 3 DECEMBER 2026',
   'Final quiz and last project review', VISUAL.schedule(),
   notes='2–2:30. Instructor confirmed on 25 November: next Thursday is 3 December; '
   'the quiz starts at 10:30 in TU103 and is followed by the final group-project '
   'review. This supersedes the older proposed 10:00–10:30 quiz window. '
   'Three days refers to the interval from the 3 December review to the '
   '6 December final repository deadline, not three days from today. '
   'Keep the existing Canvas and public sd5913-owned repository requirements; '
   'this reminder introduces no additional submission. The deadline is Sunday '
   '6 December 2026, 23:59 HKT. Bring a working candidate, test or playtest '
   'evidence and the main blocker to the final review.'))
page('NEWS · OUTSIDE QUIZ SCOPE', 'What did the companies announce?', [
    f'[Anthropic]({ANT}) began trading Nov 19. The offer price was $83.',
    'Nov 20 close: $93.5B gross, including the option. Separate placement: $26B.',
    f'[NVIDIA]({NVIDIA}) reinstated Jensen Huang as president, CEO and board director on Nov 23.',
], '2:30–4. The offer price and the first market trade measure different things. The IPO gross includes selling shareholders.')


VISUAL_RECAPS = {
    'Source code and the tools that run it': VISUAL.program_path,
    'Git, GitHub and reproducibility': VISUAL.git_history,
    'Event, state, view and handler': VISUAL.interface_state,
    'Image and video dimensions': VISUAL.pixel_shape,
    'Sampling and synthesis': VISUAL.sampling,
    'Waveform, spectrum and speech': VISUAL.speech_path,
    'Classes, objects and methods': VISUAL.ball_instances,
    'Simulation and rendering': VISUAL.shared_views,
    'Scrum artifacts and commitments': VISUAL.scrum_artifacts,
    'Pull requests and coding agents': VISUAL.pull_request_graph,
    'GitHub Actions, CI and delivery': VISUAL.ci_delivery,
    'HTTP and WebSocket': VISUAL.http_websocket,
    'Relational models and keys': VISUAL.relations,
    'Embeddings and semantic search': VISUAL.embeddings,
    'RAG, conversation memory and speech': VISUAL.model_context,
    'GitHub OAuth and app sessions': TOOLS.oauth_identity,
    'MCP and creative tools': TOOLS.live_mcp,
    'From Blender source to Godot runtime': TOOLS.asset_path,
    'Agents, tools and stop conditions': REVIEW.feedback,
}


def recap(number, heading, rows, notes):
    if heading in VISUAL_RECAPS:
        definitions = '\n\nReference:\n' + '\n'.join(
            f'{term}: {definition}' for term, definition in rows)
        S.append(figure_slide(
            week(number, f'Week {number:02} · Class material') if number < 12 else 'Week 12 · Review',
            heading, VISUAL_RECAPS[heading](), notes=notes + definitions))
        return
    slide = L.page(heading, notes)
    if number < 12:
        source = week(number, f'Week {number:02} · Class material')
    else:
        source = 'Week 12 · Review'
    slide.els.append(eyebrow(120, 94, source))

    row_height = 140 if len(rows) == 4 else 176
    for index, (term, definition) in enumerate(rows):
        y = 320 + row_height * index
        slide.els.extend((
            Rect(120, y, 1680, 2, LINE),
            T(120, y + 18, 443, row_height - 28, term, 'bold', 48, DEEP_TEAL, lh=1.10),
            T(600, y + 19, 1200, row_height - 30, definition, size=44, lh=1.16),
        ))
    S.append(slide)


recap(1, 'Source code and the tools that run it', [
    ('Source code', 'Instructions written in a programming language'),
    ('Editor', 'Tool for editing source files'),
    ('Terminal', 'Text interface for running commands'),
    ('Interpreter', 'Program that executes the source, e.g. Python'),
], '4–5. Have students point to the editor, terminal and Python interpreter they used in the first lab.')

recap(1, 'Git, GitHub and reproducibility', [
    ('Git', 'Version history: working files → stage changes → commit'),
    ('GitHub', 'Remote repository: clone a copy, push commits, pull updates'),
    ('README', 'Run instructions and prerequisites for another person'),
    ('Generative rule', 'Schotter: more disorder by row. Parameter = amount. Seed = repeatable random sequence.'),
], '5–7. Ask what another person needs to repeat the sketch from a specific commit.')

recap(2, 'Python values and types', [
    ('{mono:int} / {mono:float}', 'Whole number / floating-point approximation\n{mono:2 + 3} → {mono:5}'),
    ('{mono:str}', 'Text. {mono:"2" + "3"} → {mono:"23"}. {mono:int("2")} → {mono:2}.'),
    ('{mono:bool}', '{mono:True} or {mono:False}. {mono:2 < 3} → {mono:True}.'),
    ('{mono:None}', 'Value representing absence. A function without an explicit return result gives {mono:None}.'),
], '7–8. Cover the right-hand column verbally, then ask for the result of each expression.')

recap(2, 'Containers, lookup and assignment', [
    ('List', 'Ordered, mutable sequence. {mono:[10, 20][0]} → {mono:10}.'),
    ('Tuple', 'Ordered, immutable sequence. {mono:(hour, height)}.'),
    ('Dictionary', 'Keys map to values. In {"day": 17}, the key {mono:"day"} maps to {mono:17}.'),
    ('Aliasing', '{mono:b = a} names the same object. {mono:a.copy()} makes a shallow copy.'),
], '8–9. Ask what b shows when a is a list and an element is changed through a. A shallow copy still shares nested objects.')

slide = L.code('Control flow and verification', TIDE_LOOP,
    '9–11. Reuse the Week 3 enumerate/filter loop with two real Quarry Bay heights. '
    'Predict before running: the numeric list prints 2 2.19. Replacing the list '
    'with ["1.05", "2.19"] raises TypeError at height > 2 before anything prints. '
    'An empty list prints nothing because the body never runs. Convert incoming '
    'numeric text with float before the comparison. Missing values need a stated '
    'policy; do not infer that no output proves valid input. if/elif/else choose '
    'a branch; for visits items; while repeats while a condition holds. Indentation '
    'defines the body. Source: Week 3 Once for each number; the full day is in '
    'deck/assets/data/tides-QUB-2026.json, 17 September.',
    'What prints? Then try ["1.05", "2.19"], then [].')
slide.els.extend((
    eyebrow(120, 94, week(2, 'Week 02 · Class material')),
    T(160, 668, 1600, 112,
      'A branch chooses a block. A loop repeats it.\nIndentation groups the body. Predict → run → compare.',
      size=44, lh=1.18),
))
S.append(slide)

recap(3, 'Functions, modules and libraries', [
    ('Function', 'Named operation. {mono:def bar(height):} defines it. {mono:bar(1.2)} calls it.'),
    ('Input and result', 'Parameter = name in the definition. Argument = value passed in. {mono:return} sends a result to the caller.'),
    ('Module', 'Importable code unit. {mono:from math import sin} loads a name from a module.'),
    ('Library', 'Reusable code for a task. {mono:math}: standard library. Matplotlib: external plotting library.'),
], '11–13. Contrast displaying a bar with print and returning the bar for another function to use. An external library must be available in the project environment.')

recap(3, 'Dimensions, vectors and transforms', [
    ('1 dimension', 'One value per observation, e.g. tide height in metres'),
    ('2 dimensions', 'Vector: ordered values with meaning per position. {mono:(hour, height)} → x and y.'),
    ('3 dimensions', '{mono:(longitude, latitude, magnitude)} → x, y and marker size'),
    ('Transformation', 'Map input to output. Translate {mono:(x, y)} → {mono:(x + dx, y + dy)}.'),
], '13–14. Name each coordinate and its unit before assigning a visual channel.')

S.append(figure_slide(week(3, 'Week 03 · Class material'),
    'The same data, two visual encodings', REVIEW.review_tides(),
    notes='14–15. Both plots use the same 24 Quarry Bay heights for 17 September '
    '2026 from the original Week 3 data and plotting functions. The line maps '
    'hour to horizontal position and height to vertical position; the clock maps '
    'hour to angle and height to radius. High water is 2.19 m at 01:00; low water '
    'is 1.05 m at 07:00. The values and units stay fixed when the encoding changes. '
    'Ask which plot makes the time of high tide easiest to read, and which '
    'emphasizes the daily cycle. Source: deck/assets/data/tides-QUB-2026.json.'))

recap(4, 'Event, state, view and handler', [
    ('Event', 'An occurrence, e.g. the user selects day 17'),
    ('State', 'Current values the interaction depends on, e.g. selected month and day'),
    ('Handler', 'Code run in response to an event. Update the selected day.'),
    ('View', 'Rendered output derived from state: chart and caption for day 17'),
], '15–17. Ask where a selection can be valid in January but invalid in February.')

recap(4, 'Interfaces, APIs and tests', [
    ('API', 'Contract between programs. Browser requests a month. Service returns tide records.'),
    ('Callback', 'Run when an event occurs. Polling asks at intervals. Streamlit reruns on a widget change.'),
    ('Fixture', 'Known input with a known expected result, e.g. saved tide records'),
    ('TDD cycle', 'Red: failing test → green: make it pass → refactor: preserve behavior'),
], '17–19. Trace the request and response, then check the selector rule using a saved fixture.')

recap(5, 'Image and video dimensions', [
    ('Grayscale', '{mono:(H, W)}. Access a value with {mono:image[y][x]}.'),
    ('RGB / RGBA', '{mono:(H, W, C)}. Three color channels, with a fourth for alpha if present.'),
    ('Raw size', '{mono:H × W × C × bytes per channel}. 512 × 512 RGB at 8 bits = 768 KiB.'),
    ('Video array', '{mono:(frames, H, W, C)}. Playback time = frames ÷ frames per second at constant rate.'),
], '19–21. H is rows, W is columns. Explain that Pillow reports size as W by H, and encoded files use compression.')

recap(5, 'Image libraries and generation', [
    ('NumPy', 'Array shape and dtype. {mono:uint8} holds integers from 0 to 255.'),
    ('Pillow / OpenCV', 'Pillow reads, converts and saves images. OpenCV handles image operations and video capture.'),
    ('Diffusion', 'Repeated denoising under guidance, e.g. a prompt or edge map'),
], '21–22. In the course example NumPy holds pixels and Pillow interprets them. Check channel order when moving between libraries.')

S.append(figure_slide('WEEK 5 · FRAME SEQUENCE', 'Frame order and playback speed', frame_sequence(),
    notes='22–23. Reverse the frames for opposite motion. Halve the duration per frame for faster playback.'))

recap(6, 'Sampling and synthesis', [
    ('Sample rate', 'Samples per second. At 44,100 Hz, sample {mono:i} is at {mono:i / 44100} seconds.'),
    ('Frequency', 'Cycles per second (Hz). A 440 Hz tone is an octave above 220 Hz.'),
    ('Amplitude', 'Signal magnitude. A sine wave has peak amplitude {mono:A}.'),
    ('Sine wave', '{mono:sample = A × sin(2π × frequency × time)}'),
], '23–25. Compare sample rate with the frequency of the tone. Doubling tone frequency doubles cycles in the same span. '
   'The plotted curves cover the same 10 ms at the same peak amplitude A. '
   'The dots are every twentieth sample of a 44,100 samples/second signal, '
   'not a claim that the full signal has only these displayed samples.')

recap(6, 'Waveform, spectrum and speech', [
    ('Waveform', 'Signal amplitude by time'),
    ('Spectrum', 'Frequency content. A spectrogram shows how it changes over time.'),
    ('Music pattern', 'Timed events. The renderer produces audio for the notes or samples.'),
    ('Speech pipeline', 'Audio → speech recognition → transcript → response text → speech synthesis → audio'),
], '25–27. Follow sound through the recognizer and the response rule. Ask which output to inspect first when a control reacts to the wrong word. '
   'The turn-left transcript and response are illustrative. Speech recognition '
   'produces text; the response rule/model decides the answer; synthesis '
   'produces new audio. Waveform is amplitude over time, spectrum is '
   'frequency content, and a spectrogram tracks that content over time.')

recap(7, 'Classes, objects and methods', [
    ('Class', 'Definition of a type and its behavior, e.g. {mono:Ball}'),
    ('Instance', 'One object created from the class, e.g. {mono:Ball(5, 6, 1, 0)}'),
    ('Attribute', 'Value stored on the instance, e.g. {mono:red.x} or {mono:red.vx}'),
    ('Method', 'Function accessed through an object. {mono:red.update(dt)} acts on {mono:self = red}.'),
], '27–29. Ask which position changes when red updates and blue has its own instance. '
   'The figure reuses the actual Week 7 values: red starts at (16, 8) with '
   '(vx, vy) = (14, -5), blue at (44, 14). GRAVITY is 28. '
   'red.update(0.1) gives (17.40, 7.78); blue is not updated. '
   'Source: PFAD week07/ball.py and the Week 7 class demonstration.')

recap(7, 'Simulation and rendering', [
    ('Model', 'Ball state: position + velocity. Update: {mono:x ← x + vx × dt}.'),
    ('Simulation', 'Advance all instances by the elapsed time. Apply the bounce rule.'),
    ('View', 'Translate state into a screen representation. Terminal and Pygame read the same model.'),
], '29–31. Ask where to inspect a bad bounce seen in both renderers. '
   'Reuse the Week 7 One model, two views diagram. The terminal gives discrete '
   'cell positions; Pygame draws circles at finer resolution. The figure is a '
   'schematic of those two representations, not a screenshot. The combined '
   'launcher advances shared objects once per tick; independent standalone '
   'programs have their own clocks.')

recap(8, 'Agile and Scrum', [
    ('Agile', 'Adaptive development through usable software, collaboration and feedback'),
    ('Iterative', 'Improve the same feature over repeated cycles.'),
    ('Incremental', 'Add a usable piece to the product.'),
    ('Scrum', 'Sprint-based framework. Transparency → inspection → adaptation.'),
], '31–32. A pause menu can be a usable increment. Revising it after a playtest is iteration.')

recap(8, 'Scrum artifacts and commitments', [
    ('Product Backlog', 'Ordered work for the product → Product Goal'),
    ('Sprint Backlog', 'Selected work + delivery plan → Sprint Goal'),
    ('Increment', 'Usable, integrated work → Definition of Done'),
    ('Project board', 'Tool for making work, owners and progress visible'),
], '32–33. Match each artifact to its commitment. Notice which one contains usable work. '
   'The pause menu, save game and sound cues are an illustrative product backlog. '
   'The Sprint Backlog selects the pause menu and a delivery plan; the Increment '
   'is usable integrated work meeting the Definition of Done. A project board '
   'makes work visible but does not replace a working Increment.')

recap(8, 'Scrum accountabilities and events', [
    ('Product Owner', 'Maximize value and order the Product Backlog.'),
    ('Developers', 'Plan and create a usable Increment.'),
    ('Scrum Master', 'Help the team use Scrum effectively.'),
    ('Sprint events', 'Plan the work. Adapt daily. Review the product. Retrospect on how the team works.'),
], '33–34. Distinguish the Sprint Review of the product from the Retrospective about the way the team works.')

recap(8, 'Pull requests and coding agents', [
    ('Git workflow', 'Branch → commit → push → PR → review → merge → pull'),
    ('Pull request', 'Proposed change, diff, discussion and checks against a base branch'),
    ('Agent task', 'Goal + repo context + tools + acceptance criteria'),
    ('Review evidence', 'Inspect the diff, check the revision and try the result.'),
], '34–35. The agent uses its configured environment. Reviewers judge the submitted change and its evidence.')

recap(8, 'GitHub Actions, CI and delivery', [
    ('Workflow', 'YAML in {mono:.github/workflows/}. Event (push, PR) → jobs → steps.'),
    ('CI', 'Continuous integration: automatically test changes. A runner executes each job.'),
    ('Artifact', 'Output saved by a job, e.g. a build or test report'),
    ('Deployment', 'Publish or install a build at its destination. Verify the running result.'),
], '35–36. Distinguish the agent environment from the workflow runner and the public service.')

recap(8, 'Computer vision outputs', [
    ('Frame', 'One image from the camera stream'),
    ('Landmark', 'Estimated feature point. Normalized x and y scale by frame width and height.'),
    ('Mask', 'Per-pixel region membership or confidence'),
    ('Interaction', 'Observation → application rule → action. Handle missing detection explicitly.'),
], '36–38. Trace a hand landmark to a selected tile. Ask which valid fallback the app should use when the detector returns no hand.')

recap(9, 'Network addresses and layers', [
    ('Link', 'Local transfer, e.g. Wi-Fi, Ethernet or loopback'),
    ('IP and DNS', 'IP addresses a host/interface. DNS resolves names. {mono:127.0.0.1} is loopback.'),
    ('Transport', 'TCP / UDP. Destination port identifies an endpoint on the host.'),
    ('Application', '{mono:http://127.0.0.1:8009/state}\nScheme + host + port + path'),
], '38–40. Label every part of the loopback URL before explaining what the endpoint returns.')

recap(9, 'TCP, UDP and TLS', [
    ('TCP', 'Reliable ordered byte stream. The app needs message framing.'),
    ('UDP', 'Datagrams. Delivery and order have no guarantee.'),
    ('TLS', 'Protects data in transit and authenticates the server in HTTPS and WSS.'),
], '40–41. Two writes on TCP can appear as one read or several reads. Application framing and application acknowledgement serve different jobs.')

recap(9, 'HTTP and WebSocket', [
    ('HTTP request', 'Method + resource path. {mono:GET /state} requests a snapshot.'),
    ('HTTP response', 'Status + headers + optional body. {mono:2xx} success, {mono:4xx} request error, {mono:5xx} server error.'),
    ('REST', 'Resource-oriented API. Use methods such as GET, POST and PATCH to operate on resources.'),
    ('WebSocket', 'Open connection with message framing. Both endpoints can send.'),
], '41–43. Compare loading one gallery item with synchronizing a live scene.')

S.append(figure_slide('WEEK 9 · SERVER AUTHORITY', 'One shared scene, two clients', VISUAL.shared_scene(),
    notes='43–45. Browser A proposes a change. The server validates it and broadcasts the updated snapshot. A browser slider also has private local state.'))

recap(9, 'Actions, acknowledgements and recovery', [
    ('Action', 'Request to change state. Action ID correlates the request and result.'),
    ('State', 'Snapshot with values and a revision. The server owns the shared state.'),
    ('Acknowledgement', 'Result for a specific action. A missing reply leaves the outcome uncertain.'),
    ('Recovery', 'Reconnect → fetch current snapshot. Process restart → reload saved state if available.'),
], '45–47. The Week 9 scene starts fresh after a server restart. Ask what a tab should display while it is disconnected.')

S.append(figure_slide('WEEK 10 · PERSISTENCE', 'Saved data and fresh objects', REVIEW.review_restart(),
    notes='47–49. The persistent ID and saved values survive the process. The new instance gets its methods from Python.'))

recap(10, 'Relational models and keys', [
    ('One-to-many', 'User → conversations → messages. Each child row stores a parent reference.'),
    ('Many-to-many', 'Membership row links one user and one team. Put the team role on that row.'),
    ('Primary key', 'Unique row identity, e.g. {mono:User.id}'),
    ('Foreign key', 'Reference to a parent row, e.g. {mono:Conversation.owner_id → User.id}'),
], '49–51. Read the relationship in both directions. A many-to-many relationship uses two foreign keys on its junction table.')

recap(10, 'SQL, ORM, indexes and transactions', [
    ('SQL', '{mono:SELECT} columns {mono:FROM} table {mono:WHERE} predicate {mono:ORDER BY} column'),
    ('ORM', 'Maps classes and queries to tables and SQL, and rows back to objects.'),
    ('Lookup index', 'Data structure for finding or ordering rows efficiently'),
    ('Transaction', 'Group writes so they commit together or roll back together.'),
], '51–53. Use an owner filter and order by message ID. A question and reply can be written in one transaction.')

recap(10, 'Storage models and access patterns', [
    ('Relational', 'Keys, constraints, filters and joins. Example: account and conversation rows.'),
    ('Document', 'Nested record. Example: a game save with inventory and player state.'),
    ('Key-value', 'Value looked up by an exact key. Example: saved preferences.'),
    ('Graph / wide-column', 'Follow relationships / query rows organized around keys.'),
], '53–55. A storage product can support more than one access pattern. SQLite is a database in a file. Graph and wide-column databases are further NoSQL families. Vector search can be added to multiple database models.')

recap(10, 'Embeddings and semantic search', [
    ('Embedding', 'Learned numeric vector, e.g. 384 values for one passage in the course model'),
    ('Indexing', 'PDF → passages → embed → store vector with text, page and source ID'),
    ('Query', 'Question → same compatible encoder → compare query vector with passage vectors'),
    ('Similarity', 'Cosine similarity ranks candidates. Inspect the returned passages for support.'),
], '55–57. A different model with 384 outputs can define a different vector space. Ask why student card cost and replacement fee might be close.')

slide = L.page('What does a replacement card cost?',
    '57–60. These are actual excerpts and cosine scores from the six-passage '
    'MiniLM fixture, not the full-PDF Qwen index. The prepared query is '
    'How much does replacing a lost student identity card cost? '
    'PDF 76 supplies the amount, 150; its table is in HK dollars. PDF 20 supplies '
    'the application rule. Ask students to point to the supporting words, then '
    'compose an answer containing both amount and required action. A higher '
    'similarity score is not a truth probability. Source IDs: hb2026-p076-fees '
    'and hb2026-p020-replacement, fixtures/chunks.json at the pinned companion revision.')
slide.els.append(eyebrow(120, 94, week(10, 'Week 10 · Class material')))
for x, source, quote, role in (
    (120, 'PDF 76 · fee table · 0.893',
     '"Fee for replacement of the student identity card 150"', 'Find the amount.'),
    (1020, 'PDF 20 · replacement · 0.737',
     '"... you should submit an application for a replacement online."', 'Find the required action.'),
):
    slide.els.extend((
        Rect(x, 320, 780, 2, LINE),
        T(x, 350, 780, 112, source, 'bold', 44, DEEP_TEAL, lh=1.12),
        T(x, 478, 780, 250, quote, size=48, lh=1.22),
        T(x, 758, 780, 76, role, 'bold', 44, DEEP_TEAL),
    ))
L.takeaway(slide, 'Similarity ranks passages. The text supplies the evidence.')
S.append(slide)

S.append(figure_slide('WEEK 10 · RETRIEVAL-AUGMENTED GENERATION', 'The retrieval tool call', REVIEW.review_tool_loop(),
    notes='70–73. Follow the retrieval request and returned evidence. The model uses the passages when composing its response.'))

recap(10, 'RAG, conversation memory and speech', [
    ('RAG', 'Retrieval-augmented generation: supply source passages to the model for the current answer.'),
    ('Conversation memory', 'Ordered past messages scoped to the owner and conversation. Reload and select relevant history.'),
    ('Model context', 'Instructions + current question + selected history + retrieved sources'),
    ('Text-to-speech', 'Synthesizes audio from the answer text. Check the citations and playback.'),
], '73–75. Ask which inputs change if a new conversation asks the same question. The handbook index and per-user message store have different lifetimes.')

recap(11, 'Identity, credentials and permissions', [
    ('Identity', 'Account identifier. Registration creates the account.'),
    ('Authentication', 'Verify who is making the request using credentials or a session.'),
    ('Authorization', 'Check the authenticated caller’s permission for the requested resource.'),
    ('Permission rule', 'Verify the session, then select the note using the user ID from that session.'),
], '75–76. A successful sign-in gives the app a caller identity. The server must still enforce the note access rule.')

recap(11, 'Password hashing, encryption and sessions', [
    ('Password verifier', 'Store a slow salted hash. Verify a candidate using the same salt and settings.'),
    ('Encryption', 'Recover plaintext with a key. Protects confidentiality.'),
    ('Session', 'Credential issued after login and sent with later requests, e.g. a browser cookie.'),
    ('Signed cookie', 'App verifies signature and expiry. The signature protects integrity.'),
], '76–77. Compare a password verifier, encrypted content and a signed session.')

recap(11, 'GitHub OAuth and app sessions', [
    ('Authorize', 'OAuth delegates access. GitHub sends an authorization code and state to the app callback.'),
    ('Verify and exchange', 'Check state. Server exchanges code + app credentials + PKCE verifier for an access token.'),
    ('Identify', 'Server calls GitHub’s user API with the access token and obtains the stable user ID.'),
    ('Create session', 'App issues its own signed cookie. Later requests use that cookie.'),
], '77–79. OAuth delegates access. In the course app that access lets the app verify the GitHub profile and establish its own session.')

recap(11, 'Deployment configuration and data', [
    ('GitHub Actions', 'Workflow runs checks and deploys with a deployment credential.'),
    ('Worker', 'Runtime for the server routes. Use the environment’s callback URL and runtime secrets.'),
    ('D1', 'Persistent database. Apply migrations to create or update its schema.'),
    ('Environment', 'Local and deployed versions each have configuration, credentials and data.'),
], '79–81. Distinguish deployment token, OAuth client secret and session signing secret. The two-account check exercises the deployed authorization rule.')

S.append(figure_slide('WEEK 11 · BLENDER PYTHON', 'Objects, meshes and materials', TOOLS.scene_parts(),
    notes='81–82. A transform sets position, rotation and scale. A mesh stores geometry. bpy reads and changes scene data inside Blender.'))

recap(11, 'MCP and creative tools', [
    ('MCP', 'Model Context Protocol. The host uses a client to connect to a tool server.'),
    ('Discover', '{mono:tools/list} exposes tool names and input schemas.'),
    ('Call and observe', '{mono:tools/call} sends arguments and returns a result. Verify the change in the application.'),
    ('Blender Lab', 'Codex → MCP server → Blender add-on → scene. Blender owns the scene state.'),
], '82–84. The model chooses a tool. The server exposes operations. The Blender add-on performs an action in the scene. Ask which result proves that the correct object changed.')

recap(11, 'From Blender source to Godot runtime', [
    ('Source', 'Blender object = transform + referenced mesh + materials.'),
    ('Export', '{mono:.glb} carries mesh, materials and transforms to another application.'),
    ('Import', 'Godot instantiates the asset in a scene. Check axes, scale and pivot.'),
    ('Game behavior', 'Collision shapes and gameplay logic live in the Godot project.'),
], '84–86. Compare the asset’s appearance with the player’s ability to collide with it.')

recap(12, 'Agents, tools and stop conditions', [
    ('Agent', 'Model uses a goal, state and tool observations to choose the next action.'),
    ('Tool', 'Defined operation with inputs and a result, e.g. set speed or check level'),
    ('Feedback loop', 'Observe → choose action → run tool → inspect result → continue or stop'),
    ('Limits', 'Stop on success, tool failure or exhausted action, write or time budget.'),
], '86–88. In the recorded episode the check failed at speed 125 and passed after the model chose 275. The checker and goal stayed fixed.')

page('WEEK 12 · RECORDED EVIDENCE', 'Behavior, replay and playtest', [
    f'**Behavior check:** 3 lights and exit at tick 166. [Model episode]({COMPANION}/model-episode.json)',
    f'**Visible result:** deterministic capture from the final source. [Film]({COMPANION}/evidence/model-selected-world.mp4) · [Provenance]({COMPANION}/evidence/provenance.json)',
    f'**Playtest:** a visitor tries the actual experience. [Optional Godot practical]({COMPANION}/godot-practice.md) · [Tutorial reference]({COMPANION}/README.md)',
], '88–90. Ask which evidence answers which question. Invite questions about '
   'the subject material for the closing AMA, after time for eSFQ.')

S.append(figure_slide('TODAY\'S TUTORIAL · GROUP PROJECT DELIVERY',
    'Make your project available to try', VISUAL.delivery_paths(),
    notes='90–92. Tutorial time is primarily for moving the group project '
    'forward; the PFAD concept prompts and Godot exercise are optional references. '
    'The main two paths discussed in class are a deployed web app with a '
    'shareable URL, or GitHub Actions producing downloadable builds for the '
    'project\'s target platforms. The Godot course template exports Web, '
    'Windows and Linux; other projects can choose appropriate platforms. '
    'Do not require every platform or an app-store release. If the web app '
    'uses a backend, verify its deployed data/configuration too. A deployment '
    'or a successful build is a version to try, not a claim that the project '
    'is ready. Have someone use the delivered version, record an observation '
    'and make the next small improvement over the coming week. Source: '
    'https://github.com/sd5913/godot-game-template/blob/'
    'f4e774ce11f0d9e231cb9be229490530cd6ef0fb/.github/workflows/build.yml'))

slide = L.page('Examples you can open',
    '92–95. These are delivery examples in progress, not model answers or '
    'claims that every feature is ready. BothPls and Pixel Paws public web '
    'pages returned HTTP 200 on 25 November. BothPls source is '
    'a0790918f40dd085be9d09e6d9ef3f791eb82f05. Pixel Paws run '
    '45406859556 passed web and Android jobs and has unexpired web and '
    'android-debug-apk artifacts; its release job was skipped, so link to '
    'Actions artifacts rather than claiming a published release. Monster '
    'Staff Access run 45606353689 passed and has an unexpired Windows '
    'artifact at 2427203da9bf17ab8b4f1e4efb7d44e6c0517a71. '
    'Artifact downloads may require GitHub sign-in and eventually expire; '
    'use the latest successful workflow run if needed. Public-page access '
    'and package presence do not establish complete gameplay, login or '
    'save/reload acceptance. Ask a teammate to try the delivered version '
    'on the intended device, then use their observation for the next iteration.')
slide.els.append(eyebrow(120, 94, 'COURSE PROJECTS · DELIVERY EXAMPLES'))
for y, name, links, detail in (
    (320, 'BothPls',
     '[Open web app](https://the-aliien-repo-oqpi.vercel.app) · '
     '[Source](https://github.com/sd5913/The-Aliien-Repo)',
     'Mobile web app in development.'),
    (495, 'Pixel Paws',
     '[Play on the web](https://sd5913.github.io/Pixel-Paws/) · '
     '[CI build downloads](https://github.com/sd5913/Pixel-Paws/actions/runs/45406859556)',
     'Web + Android debug packages (GitHub sign-in).'),
    (670, 'Monster Staff Access',
     '[Windows build](https://github.com/sd5913/ae4pa/actions/runs/45606353689) · '
     '[Source](https://github.com/sd5913/ae4pa)',
     'Download, extract, then test on Windows.'),
):
    slide.els.extend((
        Rect(120, y, 1680, 2, LINE),
        T(120, y + 24, 530, 120, name, 'bold', 48, DEEP_TEAL, lh=1.12),
        T(720, y + 24, 1080, 68, links, size=44, lh=1.18),
        T(720, y + 96, 1080, 70, detail, size=40, lh=1.18),
    ))
L.takeaway(slide, 'Today: share a URL or build, have someone try it, then refine it.')
S.append(slide)

S.append(Slide(title='Student Feedback Questionnaire (eSFQ)',
    els=[Image(0, 0, 1920, 1080, str(HERE / 'week12-assets/esfq-instructions.png'),
               'contain', url=ESFQ)],
    notes='95–105. Give students up to ten minutes to complete the eSFQ. '
    'Use the official university graphic unchanged. Scan its QR code, log in '
    'with Student ID and password, and complete the form. The graphic states '
    'that feedback is anonymous to teachers and does not affect grades. '
    'Do not collect credentials or ask students to show their responses. '
    'Keep the QR visible while students complete it, then move to the open '
    'subject AMA. Source supplied by the instructor on 25 November 2026: ' + ESFQ_IMAGE))
S.append(question('short_answer', 'Ask me anything.',
    eyebrow_text='SUBJECT AMA · 105–120 MINUTES', size=112,
    hint='Questions about the subject material. Ask aloud or send a question.',
    cp={'type': 'short_answer', 'hide_names': False, 'multiple': True},
    notes='105–120. Open questions to the instructor about the subject material '
    'across the course. Revisit a diagram, trace a short example or explain a '
    'concept in response. Accept spoken questions, paper slips or the optional '
    'question inbox. No group preparation, spokesperson, project decision '
    'template or extra submission is required. Finish at minute 120.'))

DECK = {'title': 'SD5913 · Week 12 · Course review and subject AMA',
        'pdf': 'SD5913-week12.pdf', 'presenter_start_slide': 1, 'slides': S}
