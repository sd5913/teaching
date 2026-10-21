"""SD5913 Week 8: turn a project idea into a reviewed, reproducible increment.

The class meets Thursday 29 October 2026. The archive informs concepts, not 2026 policy.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import week08_figures as F

from deckgen import Figure, Slide, T, INK, WHITE, MUTED, attach_reports
from deckgen.layouts import (title, agenda, section, statement, content, two_col,
                             cards, question, code_panel, end)

EYE = 'SD5913 · WEEK 08 · THU 29 OCT 2026'
S = []
TILE_EXAMPLE = '''class Tile:
    def __init__(self, colour):
        self.colour = colour
        self.selected = False

    def choose(self):
        self.selected = True

blue = Tile("blue")
blue.choose()
print(blue.selected)  # True'''


def diagram(eye, heading, figure, notes):
    svg, png = figure
    s = Slide(bg=WHITE, title=heading, notes=notes)
    s.chrome = False
    s.els = [T(80, 24, 1760, 32, eye, 'monomed', 22, MUTED),
             T(80, 76, 1760, 80, heading, 'xbold', 60, INK),
             Figure(80, 170, 1760, 792, svg, png)]
    return s


S.append(title(EYE, 'One piece that works', 'Team workflow and reproducible projects.',
    notes='Week 8 content is taught Thursday 29 October 2026. Start from the Week 7 idea '
          'and mock-up, not from a new assessment brief. Today: scope -> useful increment -> '
          'review -> reproducible run. Ask whose experience the team wants to improve.'))
S.append(agenda(EYE, [
    'From idea and mock-up to one testable interaction',
    'Goal, ordered tasks and a usable increment',
    'Branches, pull requests and review',
    'Reproduce the project: code, dependencies and data',
    'Optional container model and bounded agent tools',
    'Team workshop: choose, test and explain one next step',
], notes='No live news item has been verified for the actual class date; omit the optional '
         'news opening rather than inventing an announcement. Allow substantial discussion '
         'and a break once the session length is confirmed. The workshop uses the draft '
         'PFAD companion PR #11; verify release status before class.'))

S.append(section('01', 'Find the smallest loop', 'Week 7 gave us an idea; now make it testable.',
    notes='Ask for the Week 7 user and mock-up before discussing implementation.'))
S.append(diagram('01 · FROM THE MOCK-UP', 'A person acts. Something responds.', F.scope(),
    'Use a running invented example: a visitor taps a colour tile and hears a short tone. '
    'Person: gallery visitor; input: tap one tile; response: one locally generated short '
    'tone and a visible selected tile. No audio is required for a team project; choose '
    'whatever input and response suits its idea. Ask what is visible if speakers fail. '
    'The user/action/response vocabulary continues Week 4 interfaces.'))
S.append(two_col('01 · WORKED EXAMPLE', 'Make a promise someone can test', [
    '**Visitor:** someone using a colour-and-sound installation.',
    '**Action:** tap the blue tile once.',
    '**Response:** highlight blue and play one short tone.',
    '**Evidence:** a second person can try it without help.',
], [
    'def choose_tile(colour):',
    '    return {',
    '        "highlight": colour,',
    '        "tone": "short"',
    '    }',
], notes='The function is an illustrative model of a response, not the finished player or '
         'an audio API. Walk through choose_tile("blue") as a simple dictionary; '
         'a UI and tone player would still be needed. Ask whether the visible selection '
         'alone provides enough feedback if sound is unavailable.'))
S.append(two_col('01 · A SMALL CLASS', 'One object remembers one choice', [
    '**Class:** a recipe for a tile with a colour and a selected state.',
    '**Object:** blue is one tile made from that recipe.',
    'Calling blue.choose() changes this object\'s state.',
    'The screen would still need code to display that change.',
], TILE_EXAMPLE.splitlines(),
    notes='Run with ordinary Python or read line by line. __init__ gives each Tile '
          'its own colour and False starting state; blue is an instance. '
          'choose updates that instance only. This is a tiny executable state '
          'example, not an audio player or a compulsory project architecture. '
          'Compare the simple response function on the previous slide: a '
          'function can return values, while this object holds changing state.'))
S.append(question('multiple_choice', 'What would test the promise best?',
    choices=['A polished poster', 'A second person taps blue and sees/hears the result',
             'A list of possible features', 'An untested code suggestion'],
    eyebrow_text='01 · PREDICT BEFORE BUILDING',
    notes='Answer: the second option. Let pairs choose before revealing; if ClassPoint '
          'is unavailable ask for a show of hands. Do not collect project ideas or '
          'personal data in ClassPoint. A no-speaker fallback should still show the '
          'highlight, but cannot verify audible playback.'))
S.append(content('01 · SCOPE CONVERSATION', 'Find the risky assumption', [
    'What must work before this idea is worth expanding?',
    'Which input can you test with a second person?',
    'What counts as a visible or audible response?',
    'What can you leave out of the first version?',
], notes='Allow teams to compare their Week 7 mock-up against a short success statement. '
         'For the running example, the risk may be that the response is not clear '
         'in a noisy room. A bounded first test uses one tile and one response, '
         'not a complete gallery application. Scope agreement follows the existing '
         'course plan; this slide does not define a submission procedure.'))

S.append(section('02', 'Work in increments', 'A plan is useful only when it leads to something usable.',
    notes='Move from a large design intention to a small observable behaviour.'))
for step, heading, note in [
    (1, 'Start with a product goal', 'Product goal: a visitor can explore a visual choice '
     'and get clear feedback. The historical Scrum material names formal roles; today '
     'we borrow its planning vocabulary without assigning Scrum roles.'),
    (2, 'Order the next tasks', 'Example backlog: tile responds to click, highlight selection, '
     'play tone, write a one-sentence run instruction, collect one visitor observation. '
     'Order by value and uncertainty; not all tasks fit the first slice.'),
    (3, 'Show a usable increment', 'Choose a short sprint goal: one clickable tile gives '
     'feedback. A sprint is a short work period and its increment must work together '
     'with the existing project, not merely exist as isolated code. This is an '
     'adaptation of Scrum, not a compulsory formal process.'),
]:
    S.append(diagram(f'02 · STEP {step} OF 3', heading, F.increment(step), note))
S.append(cards('02 · WORKED EXAMPLE', 'Choose less; test more', [
    ('goal', 'Clear feedback', 'A visitor knows a tile was selected.'),
    ('selected', 'One tile works', 'Click blue -> highlight; test with a visitor.'),
    ('later', 'Other sounds', 'Multiple tones and polish can wait.'),
], notes='Do not call a task list an increment: usable means another person can '
         'experience the behaviour. In the first slice, visible highlighting alone '
         'can be complete if the team revises the promise accordingly. '
         'Show the choice and its rationale, not a grading rubric.'))
S.append(content('02 · TEAM CHECK', 'Say the next goal out loud', [
    'Our user wants to ___.',
    'By the end of the next short work period, they can ___.',
    'We will check that by ___.',
    'The next risk is ___; the rest stays in the backlog.',
], notes='Give pairs time to draft one small testable goal from their mock-up. '
         'Invite one example and ask whether it has a real user action and response. '
         'Team working notes are not a newly assessed submission.'))

S.append(section('03', 'Make the change reviewable', 'A branch is a safe place to try one idea.',
    notes='Recall earlier Git work before tracing the three stable diagram steps.'))
for step, heading, note in [
    (1, 'Start from working main', 'One contributor branches from a baseline that can run. '
     'A branch is a named line of commits, not a separate copy of all team decisions.'),
    (2, 'Open a small pull request', 'Commit the tile/highlight change on the branch and '
     'open a pull request. Describe the intended behaviour, the exact run steps and '
     'what was tested. A PR is a request for review, not an automatic merge.'),
    (3, 'Review, then integrate', 'Another teammate reads the change, tries the '
     'interaction and reports what happened. Discuss/fix problems before merging. '
     'Fork-and-PR or collaborator branches can both follow this same review path; '
     'no organization or permission scheme is mandated.'),
]:
    S.append(diagram(f'03 · STEP {step} OF 3', heading, F.git_path(step), note))
S.append(two_col('03 · REVIEW EXAMPLE', 'What does a reviewer need?', [
    '**Claim:** clicking blue highlights blue.',
    '**Evidence:** run locally; click blue once.',
    '**Check:** blue is selected; another tile is not.',
    '**Question:** what happens on a second click?',
], [
    'Branch: tile-feedback',
    '',
    'Change: click handler + visible state',
    'Run: use the existing project README',
    'Test: tap blue; inspect selection',
], notes='This is an example PR description, not a real branch or a claim that '
         'a tile project exists in PFAD. Connect to the course Git reference '
         'https://github.com/sd5913/pfad/blob/2026/reference/git.md. '
         'Never ask students to paste credentials into a PR.'))
S.append(question('multiple_choice', 'Two people edit the same line: where is the risk?',
    choices=['When each branch is created', 'When the changes are combined',
             'When the reviewer opens the PR', 'Only after release'],
    eyebrow_text='03 · PREDICT A CONFLICT',
    notes='Answer: combining the changes may create a merge conflict; it is possible '
          'to discover one earlier while updating a branch. Example: two edits to '
          'the same colour-to-tone mapping. Ask a pair to describe how they would '
          'choose the intended behaviour and rerun the check. Show of hands if ClassPoint is unavailable.'))
S.append(content('03 · IF INTEGRATION FAILS', 'A green branch can still break main', [
    'Two changes may conflict in the same file.',
    'A merge may succeed but the behaviours may not work together.',
    'Read the difference, agree the intended behaviour, then test again.',
], notes='Distinguish text conflicts from semantic conflicts. In the example, two people '
         'may independently rename a tile or assume different response values. '
         'After integration another person must run the combined project; neither '
         'a green PR nor a successful merge alone proves the interaction works.'))

S.append(section('04', 'Make it reproducible', 'Another person needs more than the source code.',
    notes='First explain the familiar local route; containers are optional context.'))
S.append(cards('04 · PROJECT INGREDIENTS', 'What travels with the project?', [
    ('code', 'The instructions', 'Source files and a named entry point.'),
    ('dependencies', 'The environment', 'Package versions and a repeatable setup.'),
    ('data', 'The inputs', 'Shareable samples or an explicit acquisition path.'),
], notes='Relate this to the current uv/local run instructions from earlier weeks. '
         'A README explains commands, working directory, input sample and expected '
         'result. Keep private data and credentials out of repositories and images. '
         'If source data cannot be shared, provide a safe sample and a clear limit.'))
S.append(content('04 · PAIR INSPECTION', 'Can your teammate run it?', [
    'Find the command in your existing README.',
    'Identify the code, dependencies and sample data it needs.',
    'Predict the first error on a different machine.',
    'Change one instruction so a new person can repeat the test.',
], notes='Use one real current project or a known existing weekly example; do not promise '
         'a new runnable Week 8 download. If no machine is available, partners '
         'inspect the written steps and state what they cannot verify. This '
         'activity asks for a run observation, not a new graded artefact.'))
S.append(diagram('04 · OPTIONAL CONTAINERS · 1 OF 2', 'Image is not container', F.runtime(1),
    'Image: packaged filesystem/configuration used to create containers. '
    'Container: an instance with a running or stopped process and writable layer. '
    'The original archive used Docker to make a multi-service bot repeatable. '
    'We use a minimal conceptual example; local uv remains a valid path.'))
S.append(diagram('04 · OPTIONAL CONTAINERS · 2 OF 2', 'A process writes data', F.runtime(2),
    'Ask what happens if a program writes a file only to the container writable '
    'layer. Stopping and restarting the SAME container keeps that layer; removing '
    'it removes that unmounted data. Rebuilding the image is not a backup. '
    'Use a prepared trace if no container environment is available.'))
S.append(diagram('04 · PERSISTENCE', 'Choose what survives removal', F.persistence(),
    'With a bind mount, a selected host folder is visible at a chosen path '
    'inside the container. A named volume persists independently of a container. '
    'Both can preserve data beyond container removal when correctly mounted. '
    'Volumes do NOT require a running container to exist; inspect/manage them '
    'with Docker independently. Do not mount secrets or broad personal folders.'))
S.append(cards('04 · TRACE · NOT A LIVE DEMO', 'Predict what stays', [
    ('same container', 'Stop -> restart', 'Container-only file can remain.'),
    ('new container', 'Remove -> recreate', 'Container-only file is gone.'),
    ('mounted data', 'Remove -> recreate', 'Data in the same mount persists.'),
], notes='Prepared conceptual trace, not output from a command run in this deck. '
         'Ask for predictions before showing the third card. Changes inside an '
         'image are not happening here; the container writable layer is separate. '
         'A bind mount can also mask files at its destination. Data survives only '
         'if the new container reconnects the same mount; removing the volume '
         'explicitly destroys it. Verify any classroom example on its actual host.'))
S.append(content('04 · COMPOSE', 'One recipe can start several services', [
    'Compose describes services, their networks and any named storage.',
    'A project can run locally without Compose or without containers.',
    'Starting one service first does not prove it is ready for requests.',
], notes='Historical deck pp. 30-43 used a Streamlit bot and local model. '
         'Keep that as context, not a required install or a new live model exercise. '
         'Do not suggest adding users to a privileged Docker group. If demonstrating '
         'several services, verify readiness with an actual health check or a '
         'successful request, not only start order. Diagram-only fallback is sufficient.'))

S.append(section('05', 'Tools have boundaries', 'An agent can propose actions, not grant its own access.',
    notes='Transition from reviewable human changes to bounded machine-assisted suggestions.'))
S.append(diagram('05 · AGENT AND MCP · 1 OF 2', 'A request is not permission', F.agent_tool(1),
    'Recall Week 4 API client/server and the historical Week 8 agent/tool recap. '
    'An MCP server can expose tool descriptions. A model may suggest a call, '
    'but cannot authorize one. The person and runtime decide what tools and '
    'resources it is allowed to access. No live agent is required today.'))
S.append(diagram('05 · AGENT AND MCP · 2 OF 2', 'Check the scope before a tool call', F.agent_tool(2),
    'Bounded demonstration: ask an agent to inspect a safe sample README and '
    'suggest the next test; permit read-only access to that folder, not write, '
    'network, secrets or shell execution. Show an illustrative tool call '
    'read_file(path="README.md") and a human checking the suggested test. '
    'Actual MCP tools and permissions depend on the client and server; '
    'this diagram is not a claim that every student has one installed.'))
S.append(question('multiple_choice', 'The agent suggests deleting a folder. What next?',
    choices=['The suggestion gives permission', 'Check scope and decline until authorized',
             'The MCP server decides the course rules', 'Run it to see what happens'],
    eyebrow_text='05 · PERMISSION CHECK',
    notes='Answer: check scope and decline until specifically authorized. Even if a '
          'tool exists and accepts a call, the suggestion does not grant permission. '
          'Use a spoken pair vote if ClassPoint is unavailable. No real deletion, '
          'credential sharing or broad filesystem access is part of this activity.'))
S.append(content('05 · OPTIONAL CONNECTION', 'Vision can supply an input', [
    'A camera gesture or pointer can become the same action: select a tile.',
    'Test with a sample coordinate sequence when a camera is unavailable.',
    'Capture is opt-in; do not record or upload people by default.',
], notes='Historical PDF pp. 44-49 and 51-61 introduced OpenCV, MediaPipe '
         'and diffusion. They are optional future-input ideas, not a second '
         'Week 8 installation path, model requirement or permission to infer '
         'someone’s feelings/attention from a camera. No live camera or model '
         'is needed for this class.'))

S.append(section('06', 'Team workshop', 'Leave with a small test and a runnable path.',
    notes='Return to the companion activity: one testable task and one repeatable observation.'))
S.append(content('06 · DO THIS IN YOUR TEAM', 'One goal, one change, one check', [
    'Return to your Week 7 idea and mock-up.',
    'Agree one user action, one response and evidence it works.',
    'Order a few tasks; choose a small next increment and owner.',
    'Name a branch/PR review path and a second person to test it.',
], notes='Use the draft student companion at https://github.com/sd5913/pfad/pull/11 '
         'until its Week 8 README is merged to the 2026 branch. Do not pretend '
         'the PR contains a tested Docker/Compose project; it contains a planning '
         'activity, tested stdlib Tile demo, environment inspection and no-install fallback. No class '
         'length is assumed; leave time for the paired test and questions.'))
S.append(content('06 · SHARE A REPRODUCIBLE TRACE', 'Can someone else repeat it?', [
    'Point to the entry command, needed packages and a safe sample input.',
    'Try one known interaction or inspect prepared output.',
    'Explain what you observed versus what you still only expect.',
    'If you use containers: identify image, container, host and mounted data.',
], notes='Pairs swap written run steps or project screens. If Docker is unavailable, '
         'the host/container diagrams and prepared stop/recreate trace provide '
         'the same conceptual prediction. Never require Docker installation, '
         'privileged group changes, a camera, live model or paid API. '
         'Record working notes locally; do not ask for an additional submission.'))
S.append(content('06 · EXIT CHECK', 'What can the team show next?', [
    'A small usable increment and the evidence it worked.',
    'A change another person can review before combining.',
    'Steps and sample data another person can use to run it.',
    'One limitation or risk and the next test.',
], notes='Ask a few teams for a spoken one-sentence goal and a next test. '
         'If they have no working code, a specific runnable plan and a '
         'clearly labelled unverified expectation are honest outcomes. '
         'Scope agreement is the existing Week 8 course-plan checkpoint; '
         'confirm the actual process with the instructor rather than '
         'inventing a date or submission route.'))
S.append(end('Build one piece that works',
    'Make it reviewable. Make it repeatable.',
    'sd5913.github.io/teaching',
    notes='Close by asking what another person will be able to do with the '
          'project after the next change. No historical 2025 deadlines, team '
          'size or archived Blackboard instructions carry over.'))

attach_reports(S, Path(__file__).resolve().parent / 'week08-reports.json')
DECK = {'title': 'SD5913 · Week 8 · Team workflow and reproducible projects',
        'pdf': 'SD5913-week08.pdf', 'slides': S}
