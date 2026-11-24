"""Thursday 26 November 2026. Course review followed by a group AMA."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from deckgen.layouts import content, end, figure_slide, question, statement, title
from figures import schotter
from week05_figures import frame_sequence
from week06_figures import w06_waveform
import week09_figures as NETWORK
import week09_layouts as L
import week10_figures as DATA
import week11_figures as TOOLS
import week12_figures as F

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


S.append(title(EYE, 'What makes it work?', 'The ideas behind eleven weeks of programming, followed by a group AMA.',
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
S.append(content('WEEK 1 · RULES AND REPRODUCIBILITY', 'Code makes a design rule repeatable', [
    'Schotter uses one rule to increase disorder down a grid.',
    'A parameter changes the rule’s effect. A seed repeats a sequence of random choices.',
    week(1, 'Week 1 · the sketch, its commit and README'),
], figure=schotter(), body_size=40, notes='4–7. Point to the order at the top and variation at the bottom. Fix the seed and vary chaos to compare the effect of one parameter. A commit identifies the version and the README explains how to run it. Ask what information another person needs to reproduce the drawing.'))

page('WEEK 2 · READING A PROGRAM', 'Types, rules and expected results', [
    'Types affect what an operation means. With strings, + joins text.',
    'A condition chooses a path. A loop applies a rule repeatedly.',
    'A list records a sequence. A dictionary gives values meaningful keys.',
    week(2, 'Week 2 · predict, break, fix'),
], '7–11. Use the tide exercise to trace an ordered list through a loop and a choice. Ask what happens for an empty list or a quoted height. Give the expected result before inspecting implementation. Distinguish a runtime error from a plausible value that violates the brief. A dependency declaration helps another person run the same checks.')

page('WEEK 3 · DATA AND VISUAL ENCODING', 'One day of tides, several pictures', [
    'Save the measurements with their source, time and units.',
    'Use position, length or angle to encode a value.',
    'A line chart and a tide clock can show the same 24 readings.',
    week(3, 'Week 3 · tide plots and their source data'),
], '11–15. Ask which picture makes it easier to see when today repeats yesterday’s pattern, and which makes it easier to compare exact heights. Changing the plot can change what a person notices even when the data stays the same. A missing hour must remain identifiable rather than being silently interpreted as zero.')

page('WEEK 4 · INTERACTION AND TESTING', 'A control changes state', [
    'An event changes the selected day. The view shows that day’s chart and caption.',
    'An API supplies data. A view decides how to present it.',
    'A test states the expected response and checks it with known input.',
    week(4, 'Week 4 · the day selector and red/green test'),
], '15–19. Predict the valid selection after switching from January 31 to February. Then ask what the chart and caption should show. Compare an event callback with polling and a Streamlit rerun. Recall the lesson on making a test fail for the expected reason before implementing a rule. A saved sample lets the test run without the live service.')

page('WEEK 5 · VISUAL REPRESENTATION', 'A picture is a grid. A clip orders grids in time.', [
    'A pixel has a position and channel values. Resolution fixes the size of the grid.',
    'Frame order and duration change how motion appears.',
    'An edge map can guide a generator. Check the result against the intended shape.',
    week(5, 'Week 5 · pixels, frames and image generation'),
], '19–22. Reverse three frames of the moving dot. Ask why motion reverses even though every pixel stays the same within its frame. Connect the earlier numbers-to-pictures principle to a renderer interpreting the values. Recall that a diffusion model iteratively denoises a representation under guidance. An edge guide constrains structure without certifying that the generated result meets the brief.')

S.append(figure_slide('WEEK 5 · FRAME SEQUENCE', 'How does order change what you see?', frame_sequence(),
    notes='22–23. Have students predict how the movement changes if they exchange the first and last frames. Ask what property changes if they halve every frame duration. Keep the same images for both predictions.'))

page('WEEK 6 · SOUND AND SPEECH', 'Sound is a signal sampled in time', [
    'Frequency changes pitch. Amplitude changes signal strength.',
    'A spectrum shows frequency content. A waveform shows change over time.',
    'Speech recognition turns sound into text. Synthesis turns text into sound.',
    week(6, 'Week 6 · sound, music and speech'),
], '23–26. Ask students to predict what doubling 220 Hz to 440 Hz changes if amplitude stays fixed. Link the time axis to last week’s ordered frames. Ask which artifact to inspect first if an installation reacts to the wrong spoken word. Check the transcript before changing the response rule. Voice output will return in the Week 10 agent. Recall that a Strudel pattern schedules events, which are rendered as sound.')
S.append(figure_slide('WEEK 6 · WAVEFORM', 'What would an octave higher look like?', w06_waveform(),
    notes='26–27. Point to the horizontal time axis and vertical amplitude. With a pure tone, doubling frequency fits twice as many cycles into the same time. At fixed amplitude the peak height stays the same.'))

S.append(L.compare('A class defines behavior for its instances',
    ('Model', 'Each Ball has its own position.', 'A method changes the state of that Ball.'),
    ('Views', 'Terminal and Pygame draw it.', 'Both read the same simulation state.'),
    '27–29. Advance the red Ball once. Ask what happens to the blue Ball and why. Then ask what changes if we replace the renderer. Discuss which values must be owned by each instance.',
    'Where would you put the rule for bouncing off a wall?'))
page('WEEK 7 · OBJECTS AND VIEWS', 'One rule can serve multiple views', [
    'The model owns the state and updates it.',
    'A renderer reads that state to make it visible.',
    'A project can test the rule and its presentation independently.',
    week(7, 'Week 7 · one moving model, two renderers'),
], '29–31. If red bounces at the wrong place in both views, inspect the model rule first. If one view alone draws the wall at the wrong position, compare the coordinate conversion and display layout. Reuse this distinction for clients and servers next.')

page('WEEK 8 · COLLABORATION', 'A PR makes a change reviewable', [
    'Make one usable increment with a visible acceptance check.',
    'A branch contains a proposed change. The PR exposes the diff and checks.',
    'A prepared environment runs tasks. CI checks a revision. Delivery reaches a user.',
    week(8, 'Week 8 · teamwork, CI and camera inputs'),
], '31–34. Distinguish a goal in the backlog from evidence of a usable increment. Ask someone what they would check on an agent-authored PR before merge. A passing CI job can establish that its checks ran on that revision. It takes a further observation to establish that a visitor can use the delivered build.')

S.append(L.steps('Vision produces observations for a rule', [
    ('Capture', 'Read a camera frame.'),
    ('Detect', 'Estimate hand landmarks.'),
    ('Decide', 'Map a landmark to a tile or clear the selection.'),
], '34–38. Recall normalized coordinates and rescaling to image position. Distinguish a landmark (a point) from a segmentation mask (which pixels belong in a region). Ask what input the application receives when no hand is detected, and what should be visible then. A recorded frame can test the decision without a live camera.',
    'What should the interaction do when the hand leaves the frame?'))

page('WEEK 9 · NETWORKS', 'An address gets a message to a service', [
    'IP identifies a network destination. A port selects a service endpoint.',
    'TCP gives an ordered byte stream. UDP carries individual datagrams.',
    'The application protocol defines how to interpret the messages.',
    week(9, 'Week 9 · the connected scene and Multiboxes'),
], '38–41. Follow a request by name, address, port and path. DNS resolves a host name and localhost reaches this machine. Mention that TCP can split or combine writes when exposing bytes to a reader. UDP preserves datagram boundaries and leaves delivery and ordering guarantees to the application if it needs them. Ask what layer to check when the server works on its own laptop but another computer cannot reach it.')

S.append(L.compare('A snapshot or continuing updates?',
    ('HTTP', 'Request a snapshot.', 'A later request can get a newer one.'),
    ('WebSocket', 'Keep a connection open.', 'Either side can send a message.'),
    '41–43. In the connected scene an HTTP GET asks for current state once. The open WebSocket receives later changes. Polling uses repeated requests. TLS protects data in transit on HTTPS or WSS. Ask which exchange fits a gallery entry and which fits a shared live scene.',
    'Choose the exchange that fits the interaction.'))
S.append(L.diagram('The server owns the shared scene', NETWORK.journey(2),
    '43–45. Browser A asks to set x to 25. The server checks the action, updates the shared Scene, and sends revision 1 to both tabs. A state message describes the world. An ack names the accepted action, and a rejection leaves state unchanged. A slider edit alone changes only local input.'))
page('WEEK 9 · RECOVERY', 'A reconnect recovers the current view', [
    'A disconnected tab may show an old revision.',
    'On reconnect, read the server’s current snapshot.',
    'After a server restart, recovery depends on what was saved.',
], '45–47. Disconnect A, move the object from B, then predict A’s value when it reconnects. Contrast losing the connection with losing the authoritative process. A missing reply leaves the sender uncertain about whether an action was applied. Check an updated snapshot or action result before repeating an action that might run twice.')

S.append(figure_slide('WEEK 10 · PERSISTENCE', 'Persistence means surviving a restart', DATA.restart(),
    notes='47–49. The saved title is Handbook. Change an attribute in memory and quit without saving. Which title reloads? A fresh process creates a new instance from saved values and an ID. Its methods come from the program. The file or database gives the record a longer lifetime than the process.'))
S.append(figure_slide('WEEK 10 · RELATIONAL DATA', 'Related rows represent ownership', DATA.relations(),
    notes='49–52. Ada owns conversations 3 and 4. Bo owns 5. Each conversation can have many ordered messages. Read the relationship in both directions. Ask where to put a role when one person belongs to many teams and each team contains many people. The role belongs to the membership row. Distinguish a primary key from a foreign key that refers to a parent.'))
page('WEEK 10 · QUERIES AND STORAGE', 'How should a program find what it needs?', [
    'A model method can issue SQL and map result rows into objects.',
    'Keys identify and relate rows. An index speeds a lookup. A transaction groups writes.',
    'Use a nested document for a scene snapshot and exact row queries for an owner’s messages.',
    week(10, 'Week 10 · model classes, storage and query examples'),
], '52–55. Contrast ORDER BY for message history with loading a nested game save. A relational system can also store a document. In the talking handbook, writing a question and reply together avoids half-saved turns. Ask what should happen if the second insert fails. Then ask which index job differs from finding a passage by meaning.')

S.append(figure_slide('WEEK 10 · EMBEDDINGS', 'An encoder represents text as vectors', DATA.text_embeddings(),
    notes='55–57. An embedding is a learned numerical representation. The same compatible encoder must encode the passages and the question. The course model returns 384 numbers for a short text. A different model with the same number of dimensions can still define a different space. Ask what could make replacement fee close to new student card cost without an exact word match.'))
S.append(figure_slide('WEEK 10 · SEMANTIC RETRIEVAL', 'Similarity ranks passages for inspection', DATA.ranking(),
    notes='57–60. Follow the two ranked results from the course’s six-passage fixture. The index retains IDs, page information and the source text alongside vectors. A similarity score ranks candidates. Read the fee row and rule to check what they support. Ask what to do with a nearby passage that concerns a different fee. Bring that answer back after the break.'))

S.append(statement('Ten-minute break', '60–70 MINUTES', size=112,
    notes='60–70. Resume with the difference between finding sources and remembering a conversation.'))

S.append(figure_slide('WEEK 10 · RETRIEVAL-AUGMENTED GENERATION', 'Pip calls a tool to retrieve evidence', DATA.tool_loop(),
    notes='70–73. The agent uses the question and available history to form a retrieval query. The tool returns source IDs, page numbers and passage text. The model composes an answer with those sources. RAG means supplying retrieved evidence for generation. Ask what the answer should say when the retrieved passages fail to support the claim.'))
S.append(figure_slide('WEEK 10 · HISTORY AND VOICE', 'Knowledge, memory and voice have different jobs', DATA.four_states(),
    notes='73–75. Handbook passages are shared source knowledge. Ordered conversation rows belong to one conversation and user. The request assembles selected prior turns and retrieved evidence for this response. The speech component reads the answer. A correct citation, a private history and audible output each require their own check. Ask what should change when a different user opens the same question.'))

S.append(L.compare('Identity and permission are separate checks',
    ('Authentication', 'Who made the request?', 'Verify credentials or a session.'),
    ('Authorization', 'What may they access?', 'Apply permission to the requested resource.'),
    '75–77. An account row represents an identity. A credential supplies proof. Registration creates an account and login verifies a returning user. Compare a salted password verifier with reversible encryption. Ask whether a successful sign-in permits access to every conversation or note.',
    'A signed-in visitor can read their own private note.'))
S.append(L.diagram('GitHub sign-in starts an app session', TOOLS.oauth_identity(),
    '77–79. In class the browser went to GitHub and returned to the app with temporary code and state. State ties the callback to the login attempt. The server exchanges the code, verifies the profile and issues the app’s signed session cookie. Later requests present the app session. The server uses its verified ID to select the owner’s row. Ask which step fails when the browser is signed out.'))
page('WEEK 11 · DEPLOYMENT', 'Source, running service and data live apart', [
    'GitHub holds the source and runs workflow jobs. A Worker serves requests.',
    'Runtime secrets, the callback address and the database belong to an environment.',
    'A migration prepares the schema. A two-account test checks owner isolation.',
    week(11, 'Week 11 · OAuth, deployment and creative tools'),
], '79–81. Ask where to look if sign-in works locally but fails after deployment. Trace the callback origin and remote runtime configuration before diagnosing storage. A correct build and a correct deployment can coexist with a missing remote migration. Explain why the browser sends a session and the server holds the signing secret.')

S.append(L.diagram('A Blender object places a mesh in a scene', TOOLS.scene_parts(),
    '81–82. Move or scale an object and predict what stays true about the stored mesh. Distinguish geometry, material and transform. Camera framing and light determine what a render shows, so inspect the scene and the picture. Blender owns these objects and runs the bpy calls.'))
S.append(L.diagram('The agent reaches Blender through MCP', TOOLS.live_mcp(),
    '82–84. Follow Codex to the Blender Lab server and the add-on inside Blender. The model chooses a tool and passes structured input. Blender performs the operation. The tool returns observations. A script specifies the actions in advance. Ask what evidence confirms the object changed and the camera can see it.'))
S.append(L.diagram('An asset crosses into a different runtime', TOOLS.asset_path(),
    '84–86. A GLB can carry geometry and materials into Godot. Compare the mesh, transform, scale, axes and pivot in the actual scene. Collision and interaction belong to the game logic and need separate checks. A figure can look correct in the engine and still fail to block a player.'))

S.append(figure_slide('WEEK 12 · AGENT FEEDBACK', 'The check gives the agent its next observation',
    F.feedback(), notes='86–88. The recorded model saw two lights at speed 125 after 180 ticks. It chose 275; the same engine check reached the exit with three lights at tick 166. Edits stopped. A useful loop has a goal, permitted actions, observations and stop rules for a pass or exhausted budget. Replaying the trace runs the recorded decisions.'))
S.append(figure_slide('WEEK 12 · RECORDED RESULT', 'The replay shows the visible ending',
    F.screenshot('frame-end.png'), notes='88–89. This is the final frame from the later deterministic replay of the model-selected world. Point out the ending state. Ask what a person would need to try to show whether the controls are understandable.'))
page('WEEK 12 · EVIDENCE', 'What did the checker and film establish?', [
    f'[Recorded decision and engine observations]({COMPANION}/model-episode.json) show the goal and result.',
    f'[Later film]({COMPANION}/evidence/model-selected-world.mp4) shows the ending from the same final source. [Provenance]({COMPANION}/evidence/provenance.json)',
    f'[Optional Godot practical]({COMPANION}/godot-practice.md) reproduces the check.',
], '89–90. Ask which form of evidence the team lacks. Today’s tutor focus is a delivery candidate: build, deployment or installation. Bring the last working interaction if the current version is broken.')
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
