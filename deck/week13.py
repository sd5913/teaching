"""SD5913 Week 13: provisional semester synthesis and reproducibility review.

Class date: Thursday 3 December 2026; duration and final-quiz time/format remain unconfirmed.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import week13_figures as F
from deckgen import Figure, Slide, T, INK, MUTED, WHITE, attach_reports
from deckgen.layouts import (agenda, cards, code_panel, content, end,
                             section, statement, title, two_col)

HERE = Path(__file__).resolve().parent
EYE = 'SD5913 · WEEK 13 · THU 3 DEC 2026'
S = []


def diagram(eye, heading, figure, notes):
    """Keep the labels large and let the figure occupy the slide body."""
    svg, png = figure
    slide = Slide(bg=WHITE, title=heading, notes=notes)
    slide.chrome = False
    slide.els = [
        T(80, 24, 1760, 32, eye, 'monomed', 22, MUTED),
        T(80, 76, 1760, 80, heading, 'xbold', 60, INK),
        Figure(80, 170, 1760, 792, svg, png),
    ]
    return slide

S.append(title(EYE, 'Explain the loop', 'Semester synthesis · test it on another computer',
    notes='Planning draft for Thursday 3 December 2026: confirm class duration, final-quiz '
    'time/format and scope before teaching. Do not copy the historical 10am final '
    'slot or Blackboard instructions. No new assessed task is introduced.'))
S.append(agenda(EYE, [
    'Trace a small interaction from input to result',
    'Predict a loop; inspect a boundary case',
    'Connect the concepts to work actually taught',
    'Test whether another person can run your work',
    'Ask questions and decide what to improve',
], notes='Keep the assessment slot flexible until instructor confirms time and format. '
    'Use the recap before or after that slot as appropriate. The archive Week 13 PDF p. 2 '
    'has a recap, final and conclusion; its 10am time is historical only.'))
S.append(statement('Can someone else explain what your program does?',
    eyebrow_text='THE REVIEW QUESTION',
    notes='Ask for one concrete artefact a student has made. Invite them to identify '
    'one change of input that would produce a different result. No need to share private '
    'project code publicly.'))
S.append(section('01', 'A path through the semester',
    'From reading values to showing a result',
    notes='Open with confirmed Weeks 1–6. Let students supply one example from '
    'their own work, rather than listing tools from the archive.'))
S.append(cards('01 · RECALL THE WORK', 'Start with the first six content weeks', [
    ('01–02', 'Read and predict', 'Git, Python values, control flow and a check.'),
    ('03–04', 'Make and respond', 'Data into pictures; an interface and an API.'),
    ('05–06', 'Add media', 'Images, frames, sound samples and interaction.'),
], notes='These are anchored in the current 2026 Week 1–6 decks; content numbers '
    'do not imply dates. Ask students for one example from their own work at each stop. '
    'Do not claim planned later weeks were already delivered.'))
S.append(diagram('01 · ONE INTERACTION', 'Input becomes a visible result',
    F.interaction(), notes='Use the Week 4 tide interface or a student-chosen example. '
    'A selected day is an input; the app retains a selected value as state; the chart '
    'is output. State may live in a variable or framework widget; it is not identical '
    'to a click or to the whole dataset. Week 4 lecture deck and pfad/week04 are '
    'current-course evidence. Ask which line or operation changes the next result.'))
S.append(two_col('01 · APPLY THE MAP', 'Name the pieces in your own work', [
    'Choose one small interaction, plot or script.',
    'What enters? What changes or is remembered?',
    'What appears, gets saved or is returned?',
    'If the input changes, what should change?',
], [
    'input  ->  state  ->  output',
    '',
    'day 17 -> selected day -> chart',
    '',
    'Your example: _______  _______  _______',
], notes='Individual reflection, then invite optional comparison with a neighbor. '
    'Do not require teams to present or submit anything. Allow a paper example '
    'or a prior weekly example if project work is not available.'))

S.append(section('02', 'A loop with an end',
    'Predict first; then follow the state change',
    notes='Allow quiet prediction before stepping through each condition.'))
S.append(code_panel('02 · THE ENTIRE EXAMPLE', 'What prints?', [
    'limit = 3',
    'step = 0',
    '',
    'while step < limit:',
    '    print(step)',
    '    step += 1',
    '',
    'print("done")',
], notes='Pause before revealing the next slide. Have students write the sequence '
    'of printed values. These eight lines use only values, assignment and while '
    'from Week 2. The historical PDF p. 6 asks for a semester while loop; this '
    'bounded example replaces its simulation rather than reproducing old marks '
    'or assessment names.'))
S.append(diagram('02 · TRACE THE RULE', 'Test, change, stop', F.loop_step(),
    notes='The diagram is a conceptual path, not literal straight-line execution: '
    'after each true test, the body prints and increments step, then control returns '
    'to the test. At step 3 the test is false and execution proceeds to done. '
    'Ask what happens if step += 1 is removed: the loop never reaches its '
    'stopping condition; interrupt execution instead of running that version.'))
S.append(two_col('02 · CHECK YOUR PREDICTION', 'Every pass changes one value', [
    'The condition is checked before each pass.',
    'The body prints the old step, then adds one.',
    'At step = 3, 3 < 3 is false.',
    'After the loop, print("done") runs once.',
], [
    'test       printed     next step',
    '0 < 3      0           1',
    '1 < 3      1           2',
    '2 < 3      2           3',
    '3 < 3      --          3',
    '',
    'output: 0, 1, 2, done',
], notes='Allow a student to reconcile the trace with their prediction. '
    'The loop prints on separate lines, not a Python list. -- means no body '
    'execution for the false test.'))
S.append(content('02 · A BOUNDARY CASE', 'What if limit is zero?', [
    'Keep step = 0. Change only limit from 3 to 0.',
    'Predict the output. Then run the bounded snippet or trace it on paper.',
    'Which test decides whether the body runs even once?',
    '',
    '{muted:Follow-up: remove step += 1 on paper only. What stops the loop?}',
], notes='Expected: 0 < 0 is false, so only done prints. If increment is '
    'removed with limit 3, the condition stays true; do not demonstrate an '
    'unbounded print loop live. Ask how to add a finite safeguard if an input '
    'comes from elsewhere. This is a limitation students can explain, not a new '
    'quiz question.'))
S.append(statement('A result is not enough. Explain why it stops.',
    eyebrow_text='02 · THE REUSABLE HABIT',
    notes='Bring the reasoning back to image iteration, sound generation or '
    'polling only if those examples were actually taught. Distinguish a for '
    'loop over known items from a while loop guarded by a condition.'))

S.append(section('03', 'A map, not a new syllabus',
    'Connect only the topics the class actually encountered',
    notes='Preflight this block against the actual delivered later weeks; '
    'skip optional slides that were not taught.'))
S.append(cards('03 · THREE DIFFERENT QUESTIONS', 'Which kind of problem is this?', [
    ('STATE', 'What changes?', 'Values, objects, callbacks and loop progress.'),
    ('PATH', 'Where does it go?', 'Files, requests, interfaces and networks.'),
    ('EVIDENCE', 'How do we know?', 'Prediction, tests, README and a second run.'),
], notes='Use the students\' own examples. Current 2026 material supports '
    'values, callbacks, APIs and tests through Week 6. Classes/objects, Scrum, '
    'Docker, networks and MCP are candidate later-week review prompts from '
    'the historical PDF pp. 8, 13–17, 25–26; omit or adapt those if not '
    'actually covered in 2026. This is not a claim about final-quiz coverage.'))
S.append(two_col('03 · IF TAUGHT · CLASSES & OBJECTS', 'A class describes; an object remembers', [
    'A class defines a shape and behavior.',
    'An object is one instance with its own state.',
    'A method can change that state.',
    'What value would you inspect after one call?',
], [
    'class Counter:',
    '    def __init__(self):',
    '        self.value = 0',
    '    def advance(self):',
    '        self.value += 1',
    '',
    'counter = Counter()',
    'counter.advance()  # value is 1',
], notes='Optional review only if classes and objects have been taught. '
    'The historical PDF p. 8 names class and object. This tiny code is '
    'original illustrative Python, not a promised PFAD starter file. '
    'Compare counter.value with step from the loop: both are state.'))
S.append(content('03 · IF TAUGHT · WORKING TOGETHER', 'Two different kinds of checks', [
    'Git: can we identify and combine changes without losing work?',
    'A short iteration: did the result improve after feedback?',
    'A test: does this behavior still work after a change?',
    '',
    '{muted:Use the workflow actually practiced; no prescribed team size or sprint length.}',
], notes='The historical PDF p. 13 describes Scrum sprints. Review only if '
    'the class used that vocabulary. Do not turn a methodology definition '
    'into a new group-project requirement. Repo history is evidence of '
    'changes; a test checks behavior; neither substitutes for design feedback.'))
S.append(content('03 · IF TAUGHT · NETWORKS AND DOCKER', 'Where does the program run?', [
    'Browser and API may run in different processes or computers.',
    'A request needs an address and a response you can inspect.',
    'A container bundles an environment; it does not fix missing data or secrets.',
], notes='This is an optional conceptual bridge from the current Week 4 browser '
    'and API example to archival PDF pp. 14–17. Only review Docker/network '
    'material if taught. Avoid layer-stack memorisation or a new install. '
    'Explain localhost from whose computer? A container cannot make an '
    'uncommitted file appear on another machine.'))
S.append(diagram('03 · IF TAUGHT · TOOL PERMISSIONS',
    'A suggestion is not permission to act', F.tool_boundary(),
    notes='Optional if agent/MCP tools were taught. The agent proposes a call; '
    'an MCP server exposes a tool contract; the tool may read or write '
    'resources. Validate the target and grant only intended access before '
    'execution; the model\'s proposed call is not authorization. Historical '
    'PDF pp. 25–26 mentions MCP and an addition tool. No account, API key '
    'or AI feature is required for student projects.'))
S.append(content('03 · PERMISSION CHECK', 'Would you allow this action?', [
    'Request: "Read a local file and publish its contents."',
    'What is the file? Who can view the destination?',
    'Would a sample with invented data answer the same question?',
    '',
    '{muted:Do not send secrets, submissions or personal data to test a tool.}',
], notes='Discussion only. A correct response asks for scope, destination '
    'and authorization or refuses. Use fictional data. If MCP was not '
    'covered, frame this as a general software-permission question or '
    'omit both tool slides.'))

S.append(section('04', 'Can someone else run it?',
    'Make a small result reproducible without exposing private data',
    notes='Transition from explaining a behavior to making it repeatable '
    'on a different computer or as a documented paper trace.'))
S.append(diagram('04 · REPRODUCIBILITY', 'From repository to checked result',
    F.reproduction(), notes='The archive tutorial PDF p. 28 asks for testing on '
    'another computer. Adopt the reproducibility question, not its '
    'Blackboard instructions. A second person needs tracked source and '
    'allowed sample data, actual commands, dependencies, and an expected '
    'observation. A local success alone is not proof of a clean run.'))
S.append(cards('04 · THREE CLUES', 'When it works only for you', [
    ('FILES', 'Missing input', 'Is the needed sample committed or documented?'),
    ('PATHS', 'Your computer', 'Does an absolute path point only to your disk?'),
    ('SETUP', 'Hidden step', 'Are dependencies and run commands stated?'),
], notes='Show an example by using a harmless sample file from a prior week. '
    'Never commit credentials, student records, proprietary media or '
    'private submissions just to make a demonstration run. A permitted '
    'small stand-in input is safer. The PFAD companion PR #16 Week 13 README '
    'proposes the same run-on-another-computer check.'))
S.append(content('04 · TRY IT OR TRACE IT', 'One small reproducibility check', [
    'Choose an example already available from a taught 2026 week.',
    'Give a partner its repository link and run instructions; or simulate a fresh start on paper.',
    'Predict one output before running. Record one observed result and one limitation.',
    'Fix one missing instruction, path or dependency if you can.',
], notes='Optional partner comparison, not a compulsory group activity or '
    'new submission. If no other device is available, use the paper trace '
    'and inspect the README. PFAD PR #16 includes a runnable stdlib loop; '
    'the paper trace remains a fallback. Link to course '
    'companion after that PR is merged, or open the draft directly.'))
S.append(two_col('04 · EXPLAIN A FAILURE', 'A useful report has four parts', [
    'What you expected to happen.',
    'What happened instead.',
    'One clue: error, line or missing file.',
    'The next small change to test.',
], [
    'Expected: 3 lines + done',
    'Observed: only done',
    'Clue: limit = 0',
    'Next: check the input value',
], notes='Use the earlier loop to model evidence before moving to student '
    'work. Do not equate this example with a grading requirement. If '
    'the work cannot be run safely, a clear limitation is honest evidence.'))

S.append(section('05', 'Open questions', 'Review what was taught; name what remains uncertain',
    notes='Leave genuine room for unresolved conceptual and project questions.'))
S.append(content('05 · ASK ME ANYTHING', 'What still needs an explanation?', [
    'A concept you can name but cannot yet apply?',
    'A test you do not trust?',
    'A project decision you want to make smaller?',
    '',
    '{muted:We can trace a real example, but we do not need private code on screen.}',
], notes='Invite questions and keep examples bounded. If a question '
    'depends on an unconfirmed final-quiz format, scheduling or permitted '
    'tools, record it for the instructor rather than inventing an answer. '
    'The archive p. 27 similarly reserves AMA time.'))
S.append(content('05 · ASSESSMENT BOUNDARY', 'Use confirmed course instructions', [
    'The course overview lists a final quiz worth 10%.',
    'The group project is a separate 40% assessment.',
    'Follow the current instructor and actual brief for timing, scope and submission.',
    '',
    '{muted:No quiz questions, timing, new deadline or new submission route on these slides.}',
], notes='Week 1 2026 assessment overview supports these weights. Its '
    'class date is Thursday 3 December 2026, but it does not confirm a quiz hour or format. '
    'Do not transfer the midterm format or archive 10am slot to the final. '
    'Do not repeat historical Blackboard hand-in instructions.'))
S.append(end('Explain it. Test it. Make it repeatable.',
    'Start from one small result another person can inspect.',
    'sd5913.github.io/teaching',
    notes='Close with a voluntary one-sentence reflection: what worked, '
    'what surprised you, what would you change next? Point students to '
    'their current PFAD materials and confirmed announcements.'))

attach_reports(S, HERE / 'week13-reports.json')

DECK = {'title': 'SD5913 · Week 13 · Explain the loop',
        'pdf': 'SD5913-week13.pdf', 'slides': S}
