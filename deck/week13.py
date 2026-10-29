"""Week 13: final quiz/revision and delivery support. Final class date TBC."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import week13_figures as F
from deckgen import Figure, Slide, T, INK, MUTED, WHITE, attach_reports
from deckgen.layouts import agenda, code_panel, content, end, statement, title

HERE = Path(__file__).resolve().parent
PRACTICAL = 'https://github.com/sd5913/pfad/blob/cf3c9a40a2645b7d087a289fe65e053e02b61e47/week13/README.md'
EYE = 'SD5913 / WEEK 13 / FINAL CLASS DATE TBC'
S = []


def diagram(heading, figure, notes):
    svg, png = figure
    slide = Slide(bg=WHITE, title=heading, notes=notes)
    slide.chrome = False
    slide.els = [T(80, 24, 1760, 32, EYE, 'monomed', 22, MUTED),
                 T(80, 76, 1760, 80, heading, 'xbold', 60, INK),
                 Figure(80, 170, 1760, 792, svg, png)]
    return slide


S.append(title(EYE, 'Explain it.\nMake it run.',
    'Revision / Canvas final quiz / project support',
    notes='120-minute final class, prepared 29 October 2026. Final class date and any '
    'tutorial rescheduling remain TBC. Confirm arrangements before classroom use. '
    'Instructor confirmed quiz 10:00-10:30 HKT, matching the midterm. Do not infer '
    'format, question count, tool permissions or other policy. Weeks 9-12 are '
    'approved production material, not yet delivered/readiness-proven; check the '
    'scope ledger against actual delivery before using their revision prompts.'))
S.append(agenda(EYE, ['Diagnose a trace, then ask anything',
    'Canvas final quiz: 10:00-10:30 HKT', '10-minute break',
    'Return to difficult concepts and project blockers',
    'Check the delivery; choose final fixes'],
    notes='Example assumes 09:30 start: 0-15 diagnostic revision; 15-30 AMA; '
    '30-60 quiz; 60-70 break; 70-100 targeted revision/project blockers; '
    '100-115 delivery; 115-120 owners/actions. Only quiz clock time/duration '
    'is confirmed. Check actual date/start. No new practical or compulsory '
    'showcase. Optional dated news is outside quiz scope; see '
    'lessons/week13-news-20261029.md.'))
S.append(code_panel('REVISION / STATE / 0-7 MIN', 'Two names. How many balls?', [
    'red = Ball(16, 8, 14, -5)', 'selected = red',
    'selected.update(0.1)', '', 'print(red.x, selected.x)',
], caption='PFAD root: uv run week07/ball.py',
    notes='Source: https://github.com/sd5913/pfad/blob/a4370bec4be29d5f4a37b1a8ecd477e25a73fc3d/week07/ball.py . '
    'Public diagnostic practice, not a graded quiz question/key. Use actual '
    'Week 7 Ball constructor and method in pfad/week07/ball.py. Did selected = red '
    'call the constructor? Both names refer to the same object. Its x changes '
    'from 16 to 17.4, observed through either name, subject to float display. '
    'Methods remain program code; attributes are changing state. Optional '
    'existing command from PFAD root: uv run week07/ball.py. Do not repeat the '
    'whole two-object lesson. No new standalone code file is promised here.'))
S.append(content('REVISION / MESSAGES / 7-11 MIN', 'The reply never arrives.', [
    'Client sends: {"action": "move", "dx": 1}',
    'The connection closes before an acknowledgement.',
    'Did the server change the scene?', 'What evidence would make a retry safe?',
], body_size=42, notes='Two possible timelines: action applied then reply lost; '
    'action never applied. Missing reply alone cannot distinguish them. Inspect '
    'server state or request ID/result if supported; repeating a relative move '
    'may apply it twice. This does not claim Week 9 implements durable '
    'deduplication. Trace client, validation, authoritative state and reply in '
    'the delivered example. Rejected input differs from connection failure. '
    'No port-number trivia or new networking setup.'))
S.append(content('REVISION / GIT / 11-15 MIN', 'It is committed. Can the team run it?', [
    'Alice commits a tested fix on her laptop.',
    'Bob pulls main. The fix is missing.',
    'Trace the missing steps from local change to shared main.',
    'Which check needs Bob to run the interaction?',
], body_size=42, notes='Use actual Week 8 workflow: push branch, open PR, teammate '
    'reviews/tests, fix feedback, merge, teammates update main. Local commit is '
    'not automatically shared; pulling main does not put an unmerged feature '
    'into main. Review checks diff and behavior; green build alone does not '
    'prove an interaction. Ask for one actual team blocker. Reference '
    'pfad/week08/teamwork.md; do not test command memorization.'))
S.append(statement('What can you name,\nbut cannot yet explain?',
    eyebrow_text='AMA / 15-30 MIN', notes='Protect 15 minutes. Ask for a trace, '
    'failed prediction or project blocker. Group related questions; use one '
    'small example. Reserve longer traces for 70-100. Keep private code/data '
    'off screen. Record unconfirmed assessment rules for the instructor.'))
S.append(statement('Canvas final quiz\n10:00-10:30 HKT',
    eyebrow_text='CONFIRMED / 30 MINUTES', notes='Existing final quiz. Follow '
    'instructor and actual Canvas instructions. Scheduling reply confirms '
    'time/duration only; no public graded questions/keys, permissions, count '
    'or format here. Stop revision at 10:00; finish at 10:30. Confirm Canvas '
    'access and final-class date before teaching. ClassPoint is not the quiz.'))
S.append(statement('Break / 10 minutes', eyebrow_text='60-70 MIN',
    notes='Example 09:30 start gives 10:30-10:40 HKT break. Keep the break. '
    'Choose useful diagnostic routes from the following slides after it; '
    'these are revision/support, not a new practical.'))
S.append(code_panel('TARGETED REVISION / STORED STATE', 'Which messages come back?', [
    'Message: id | conversation_id | text',
    '         11 | 7               | hello',
    '         12 | 8               | private draft',
    '         13 | 7               | next step?', '',
    'SELECT text FROM message', 'WHERE conversation_id = 7 ORDER BY id;',
], lang=None, notes='70-100 is a choice of routes, not nine full mini-lectures. '
    'Predict the two selected texts in order. Trace a model method creating '
    'another Message: attributes -> INSERT/commit -> row -> SELECT -> new '
    'instance after restart. Values/relationships survive; method bodies '
    'remain source code. Use delivered Week 10 methods, not invented API '
    'syntax. Check the selected user owns conversation 7; conversation '
    'filter alone is not user authorization. These are invented diagnostic rows.'))
S.append(diagram('Three jobs in the same database', F.record_keys(),
    notes='Ask which mechanism is broken for duplicate identity, missing parent, '
    'or correct but slow history lookup. Primary key identifies row; foreign '
    'key references parent, with enforcement needed for integrity; ordinary '
    'lookup index accelerates matching at storage/write cost. Removing that '
    'index should not change correct selected rows. None is the handbook '
    'vector index. Transfer: User -> SaveFile ownership; many-to-many team '
    'membership uses a linking record.'))
S.append(content('TARGETED REVISION / STORAGE CHOICE', 'What question must the data answer?', [
    'All messages in this user-owned conversation?',
    'The levels and settings inside one saved game?',
    'Handbook passages relevant to a paraphrased question?',
    'What would be hard to ask of each representation?',
], body_size=42, notes='Compare related rows/exact filters, nested save/config '
    'document, and real embeddings/source metadata ranked by similarity. '
    'Retrieval needs, not rigid product categories: JSON can live in a file '
    'or database; relational systems can store nested data. A vector is not '
    'an identity, source document or truth score. No new database install.'))
S.append(diagram('A close neighbour can still be wrong.', F.retrieval(),
    notes='Trace delivered Week 10 handbook: versioned PDF -> page/source chunks '
    '-> learned vectors in identified space. Query and stored vectors need '
    'same compatible encoder/space, not merely same dimensions. After encoder '
    'or PDF change, rebuild/revalidate affected index and provenance; do not '
    'mix spaces. Inspect source/page/text before accepting answer. Similarity '
    'ranks candidates; RAG adds context, does not train model or guarantee '
    'correctness. Never invent a handbook page citation.'))
S.append(diagram('Restart the bot. What should survive?', F.lifetimes(),
    notes='Same handbook bot throughout. Source index persists independently of '
    'history. Ordered user-owned history must be scoped, loaded and actually '
    'passed to later model call; thread ID alone proves none of that. Prompt '
    'is assembled for one call from instructions, question, selected history '
    'and evidence. Speech outputs displayed answer; synthesis/playback can '
    'fail separately. If follow-up forgets topic but retrieval works, inspect '
    'history and assembled context; check restart/reload and isolation. '
    'Hearing audio does not prove correct sources.'))
S.append(code_panel('TARGETED REVISION / TOOLS', 'Did the scene actually change?', [
    'request: set_speed(value=360)', 'result:  {"ok": true}', '',
    'check: read saved speed', 'check: run game and observe movement',
], lang=None, notes='Illustrative trace, not a transcript of live model run. '
    'Separate request, validation/execution, result, saved scene and running '
    'application. Successful transport cannot prove correct file changed or '
    'running process reloaded it. What if wrong scene is open? Use delivered '
    'Week 11/12 API/MCP example for actual request/result. No repeat permission '
    'lecture or addition-tool exercise. Direct API and MCP expose different '
    'boundaries; both need observable application evidence.'))
S.append(diagram('What made the next action change?', F.feedback(),
    notes='Fixed workflow follows programmed build/render steps; agent chooses '
    'an action after observation. Diagram is conceptual, not live proof. '
    'Use delivered Week 12 trace only after live gate passes: failed check, '
    'model revises action, passing check, stop within bounds. A repeated '
    'script or replay alone does not prove model choice. Stop for passing '
    'requirements, failure limit or budget; limit reached can mean incomplete. '
    'A clip is an artifact, not proof every behavior passed.'))
S.append(content('TARGETED REVISION / AGILE & SCRUM', 'A board is full. What improved?', [
    'Choose one usable change from the last iteration.',
    'Which test or user feedback changed the next decision?',
    'What belongs in the next small goal?',
    'Connect the plan to the running result.',
], body_size=42, notes='Week 8: product goal/backlog, sprint goal/selected work, '
    'usable increment, review feedback, retrospective improvement. Sprint is '
    'bounded, not guarantee all planned work finishes. Review concerns product; '
    'retrospective concerns how team worked. Card/commit counts, attendance '
    'and formal roles do not determine execution mark. Git, planning record, '
    'tests and user feedback provide different evidence. Projects recommended; '
    'equivalent accessible record valid.'))
S.append(content('PROJECT SUPPORT / PICK A QUEUE', 'What blocks the next person?', [
    'Cannot start: directory, dependency, input or access?',
    'Starts, but core interaction fails: smallest failing case?',
    'Working: fresh run, boundary case and README check.',
    'One blocker, one owner and one check.',
    f'[Complete Week 13 support guide]({PRACTICAL})',
], body_size=42, notes='Use remainder of 70-100 for actual blockers after selected '
    'revision. Prioritize teams without running core; working teams peer-test. '
    'Reduce scope around useful interaction rather than add stack. No required '
    'AI, camera, engine or account. PFAD Week 13 provides separate full '
    '120-minute support route, earlier-week recovery and differentiated queues. '
    f'Pinned complete student/TA route: {PRACTICAL}'))
S.append(diagram('Let another person follow the README.', F.reproduction(),
    notes='100-115: partner gets URL and documented starting point, no hidden '
    'verbal setup. Separate fresh folder/other computer: identify revision, '
    'follow setup/run, normal input, boundary/failure, expected visible result. '
    'Protect existing work; no destructive reset. Record actual OS/runtime, '
    'result and limits. Paper trace is useful diagnosis if machine unavailable '
    'but does not prove a fresh run.'))
S.append(content('FINAL DELIVERY / ACCESS', 'Can the marker reach the work?', [
    'Public team repository owned by sd5913.',
    'Teammates: Write access; progress record: accessible.',
    'README: setup, run, expected result and known limits.',
    'Canvas: check the actual submitted repository URL.',
], body_size=42, notes='Check signed-out public view; teammate Write is separate. '
    'Project access is also separate from repo access. Projects recommended; '
    'equivalent accessible record valid. Use actual Canvas assignment; no '
    'invented URL/group settings, new upload or defence. Source: '
    'https://github.com/sd5913/pfad/blob/2026/assignments/group-project.md.'))
S.append(content('FINAL DELIVERY / CREDIT & EVIDENCE', 'Make the result repeatable.', [
    'Run the documented build or launch from shared source.',
    'Permitted sample inputs; no private paths or secrets.',
    'Credit assets, code, libraries and AI assistance used.',
    'Link tests, feedback and progress; name limitations.',
], body_size=42, notes='Check asset source and license/permission; attribution '
    'does not grant reuse rights. Distinguish original/reused work and meaningful '
    'AI assistance without publishing private conversations. Never copy secrets '
    'or student records to make setup work. State device/account prerequisites '
    'and honest fallback. Recording illustrates result but cannot hide known '
    'failure. Retest fixed blocker. PFAD checklist includes precise steps.'))
S.append(content('FINAL FIVE MINUTES', 'Leave with a testable finish.', [
    'One essential fix; one owner; one time to recheck.',
    'Group project: 40% of the course.',
    'Project rubric: 25% idea / 50% code / 25% execution.',
    'Deadline: 6 December 2026, 23:59 HKT.',
], body_size=42, notes='115-120: keep next actions in existing progress record, '
    'not a new submission. Deadline unchanged despite class/tutorial date TBC. '
    'Rubric shares divide project mark. Final tutorial supports unfinished and '
    'working teams, scheduling to confirm. Actual brief and Canvas instructions '
    'remain authoritative; no compulsory defence, new grade or deliverable.'))
S.append(end('Build something\nworth trying.',
    'Explain the behavior. Check the evidence. Credit the work.',
    'SD5913 / FINAL CLASS DATE TBC', notes='Close 120-minute class. Refer to '
    'PFAD Week 13 separate final support, subject to confirmed scheduling. '
    'Only confirmed final-quiz timing is 10:00-10:30 HKT. Check remaining '
    'classroom facts and delivered scope before using this draft.'))
attach_reports(S, HERE / 'week13-reports.json')
DECK = dict(title='SD5913 / Week 13 / Explain it. Make it run.',
            pdf='SD5913-week13.pdf', slides=S)
