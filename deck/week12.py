"""Thursday 26 November 2026. Course review followed by a group AMA."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from deckgen.core import DEEP_TEAL, LINE, Rect, T, eyebrow
from deckgen.layouts import content, end, figure_slide, question, statement, title
from week05_figures import frame_sequence
import week09_figures as NETWORK
import week09_layouts as L
import week10_figures as DATA
import week11_figures as TOOLS

EYE = 'SD5913 · THURSDAY 26 NOVEMBER 2026'
PIN = '362ad2318e1bf42bee28a3ab43dec89d6e8a17ec'
COURSE = 'https://github.com/sd5913/pfad/blob/2026'
COMPANION = f'https://github.com/sd5913/pfad/blob/{PIN}/week12'
ANT = 'https://www.anthropic.com/news/ipo-close'
NVIDIA = 'https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Board-Reinstates-Jensen-Huang-as-President-CEO-and-Board-Director/default.aspx'
ROCKSTAR = 'https://www.rockstargames.com/newswire/article/39akk424a9oo53/grand-theft-auto-vi-now-available'
LEONIDA = 'https://github.com/ItsNotRexed/Leonida'
WINDOW = LEONIDA + '/pulls?q=is%3Apr+created%3A2026-11-23T16%3A25%3A00Z..2026-11-23T16%3A34%3A59Z'
S = []


def week(number, label):
    return f'[{label}]({COURSE}/week{number:02}/README.md)'


def page(label, heading, lines, notes):
    S.append(content(label, heading, lines, body_size=44, notes=notes))


S.append(title(EYE, 'Programming concepts', 'Week-by-week reference and group AMA',
               size=112, notes='0–1. Today we revisit the ideas that let us explain a program, predict what it will do and check the result. Keep one interaction from your team project in mind for the AMA.'))
page('NEWS · OUTSIDE QUIZ SCOPE', 'What did the companies announce?', [
    f'[Anthropic]({ANT}) began trading Nov 19. The offer price was $83.',
    'Nov 20 close: $93.5B gross, including the option. Separate placement: $26B.',
    f'[NVIDIA]({NVIDIA}) reinstated Jensen Huang as president, CEO and board director on Nov 23.',
], '1–2. The offer price and the first market trade measure different things. The IPO gross includes selling shareholders.')
page('NEWS · OUTSIDE QUIZ SCOPE', 'Which game actually runs?', [
    f'[Rockstar]({ROCKSTAR}) announced the GTA VI console launch.',
    'A claimed Xbox build leak is a separate claim. What could verify its origin and platform?',
    'For a PC claim, look for an authorized, independently reproducible run on identified hardware.',
], '2–3. A console release establishes availability on consoles. A screenshot or a file name cannot establish the origin or playability of a different build.')
page('NEWS · OUTSIDE QUIZ SCOPE', 'What does a pull request count?', [
    f'[55 PRs opened]({WINDOW}) in 10 completed minutes: 5.5 per minute.',
    '24 Nov, 00:25 to 00:35 HKT (end excluded). Counts submissions.',
    f'At inspection, [Leonida’s README]({LEONIDA}/blob/c646bf836777ef63587ecdbea44bd62df827c433/README.md#project-status) said the game did not boot.',
], '3–4. Counted created_at timestamps from GitHub for Nov 23, 16:25–16:35 UTC. PR volume establishes neither the number of agents nor a working game. Return to this distinction when reviewing team evidence.')
def recap(number, heading, rows, notes):
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

recap(2, 'Control flow and verification', [
    ('Branch', '{mono:if} / {mono:elif} / {mono:else}: choose a block by condition'),
    ('Loop', '{mono:for}: each item in a sequence. {mono:while}: repeat while a condition holds.'),
    ('Indentation', 'Indented lines form the body of a branch, loop or function.'),
    ('Verification', 'Expected result → run typical and boundary cases → compare actual result'),
], '9–11. Use one normal tide list and an empty list. Ask what the specification should require for each.')

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

recap(3, 'Data source and visual encoding', [
    ('Source record', 'Source + timestamp + numeric value + units'),
    ('Visual encoding', 'Tide line: hour → horizontal position. Height → vertical position.'),
    ('Polar encoding', 'Tide clock: hour → angle. Height → radius.'),
], '14–15. The same day can produce both plots. Ask which plot makes it easier to spot the hour of high tide.')

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
], '23–25. Compare sample rate with the frequency of the tone. Doubling tone frequency doubles cycles in the same span.')

recap(6, 'Waveform, spectrum and speech', [
    ('Waveform', 'Signal amplitude by time'),
    ('Spectrum', 'Frequency content. A spectrogram shows how it changes over time.'),
    ('Music pattern', 'Timed events. The renderer produces audio for the notes or samples.'),
    ('Speech pipeline', 'Audio → speech recognition → transcript → response text → speech synthesis → audio'),
], '25–27. Follow sound through the recognizer and the response rule. Ask which output to inspect first when a control reacts to the wrong word.')

recap(7, 'Classes, objects and methods', [
    ('Class', 'Definition of a type and its behavior, e.g. {mono:Ball}'),
    ('Instance', 'One object created from the class, e.g. {mono:Ball(5, 6, 1, 0)}'),
    ('Attribute', 'Value stored on the instance, e.g. {mono:red.x} or {mono:red.vx}'),
    ('Method', 'Function accessed through an object. {mono:red.update(dt)} acts on {mono:self = red}.'),
], '27–29. Ask which position changes when red updates and blue has its own instance.')

recap(7, 'Simulation and rendering', [
    ('Model', 'Ball state: position + velocity. Update: {mono:x ← x + vx × dt}.'),
    ('Simulation', 'Advance all instances by the elapsed time. Apply the bounce rule.'),
    ('View', 'Translate state into a screen representation. Terminal and Pygame read the same model.'),
], '29–31. Ask where to inspect a bad bounce seen in both renderers.')

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
], '32–33. Match each artifact to its commitment. Notice which one contains usable work.')

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

S.append(figure_slide('WEEK 9 · SERVER AUTHORITY', 'One shared scene, two clients', NETWORK.journey(2),
    notes='43–45. Browser A proposes a change. The server validates it and broadcasts the updated snapshot. A browser slider also has private local state.'))

recap(9, 'Actions, acknowledgements and recovery', [
    ('Action', 'Request to change state. Action ID correlates the request and result.'),
    ('State', 'Snapshot with values and a revision. The server owns the shared state.'),
    ('Acknowledgement', 'Result for a specific action. A missing reply leaves the outcome uncertain.'),
    ('Recovery', 'Reconnect → fetch current snapshot. Process restart → reload saved state if available.'),
], '45–47. The Week 9 scene starts fresh after a server restart. Ask what a tab should display while it is disconnected.')

S.append(figure_slide('WEEK 10 · PERSISTENCE', 'Saved data and fresh objects', DATA.restart(),
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

S.append(figure_slide('WEEK 10 · SEMANTIC RETRIEVAL', 'Ranked results and source pages', DATA.ranking(),
    notes='57–60. These scores are from the six-passage fixture. Ask which passage provides the amount and which provides the rule.'))

S.append(statement('Ten-minute break', '60–70 MINUTES', size=112,
    notes='60–70. Resume with retrieval, conversation history and generation.'))

S.append(figure_slide('WEEK 10 · RETRIEVAL-AUGMENTED GENERATION', 'The retrieval tool call', DATA.tool_loop(),
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
    ('Permission rule', 'Private note: use the verified session ID to select its owner’s row.'),
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
    f'**Playtest:** a visitor tries the actual experience. [Optional Godot practical]({COMPANION}/godot-practice.md)',
], '88–90. Ask which evidence the team needs for the delivery candidate. Bring that decision into the AMA.')

S.append(question('short_answer', 'Our visitor tries ___.\nWe saw ___.\nShould we change ___ or ___?',
    eyebrow_text='GROUP AMA · 90–95 MINUTES', size=88,
    hint='3 min to prepare, 2 min to choose a speaker. Ask aloud or pass a paper slip.',
    notes='90–95. Give each team three minutes to form one question and two to choose a spokesperson and an observation. On paper, write the question or ask it aloud. No login, vote or submission is needed.'))
S.append(L.rows('Group AMA · 95–115 minutes', [
    ('Ask', 'One group names the decision and what they tried.'),
    ('Answer', 'A second group offers a check; the tutor invites a follow-up.'),
    ('Rotate', 'Move to another group or a different kind of blocker.'),
], '95–115. Allow four rounds of five minutes (one to ask, three for answers, one for follow-up). Combine related questions in a large room and carry remaining questions to tutor support. With no network, collect paper slips and read them aloud.',
    'Ask what to cut, keep or test with a visitor.'))
page('AMA · 115–120 MINUTES', 'What will you try next?', [
    'Say the next check, who will try it, and what result would change your decision.',
    f'Use the existing team progress record for tutor feedback. [Group-project brief]({COURSE}/assignments/group-project.md)',
    f'[Thursday’s paired tutorial]({COMPANION}/README.md) · break 55–65 · tutor support 100–120.',
], '115–119. Give teams two minutes to decide and hear one or two exits aloud. The tutorial is a separate 120 minutes. This conversation creates no extra grade or upload.')
S.append(end('One next check.', 'Take your candidate and your question to the tutor.',
    'SD5913 · WEEK 12', notes='119–120. Finish at minute 120. The public project brief remains the source for assessment.'))

DECK = {'title': 'SD5913 · Week 12 · Course review and group AMA',
        'pdf': 'SD5913-week12.pdf', 'slides': S}
