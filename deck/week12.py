"""Thursday 26 November 2026. Course review followed by a group AMA."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from deckgen.layouts import content, end, figure_slide, question, statement, title
from figures import schotter
import week09_layouts as L
import week12_figures as F

EYE = 'SD5913 · THURSDAY 26 NOVEMBER 2026'
PIN = '365905e19c307cc245223ed626653d6f4c87438d'
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


S.append(title(EYE, 'What makes it work?', 'A whole-course review and group AMA about your delivery candidate.',
               size=112, notes='0–1. Bring to mind one visitor, one action and what they should experience.'))
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
S.append(L.steps('What can your team show today?', [
    ('A visitor', 'Who is the first person to try it?'),
    ('An action', 'What input changes the experience?'),
    ('Evidence', 'What would convince someone it worked?'),
], '4–8. In pairs, describe your current candidate in one sentence. Ask your partner to name something they could actually observe.', 'Keep the same interaction in mind throughout the review.'))
S.append(content('WEEK 1 → WEEK 5', 'What did the artist choose?', [
    'In the Week 1 Schotter study, each row shifts and rotates more.',
    'Keep the seed fixed. Change CHAOS. Which differences come from your rule?',
    f'[Revisit the sketch]({COURSE}/week01/first-repo/sketch.py) · [Week 5 seeded noise]({COURSE}/week05/noise.py)',
], figure=schotter(), body_size=40, notes='8–10. Look from the orderly top row to the lower rows. Changing a seed selects another arrangement under the same rule. Changing chaos alters the rule’s strength. Which parameter should the visitor control in your piece?'))
page('WEEKS 1 + 2 → WEEK 8', 'Could a teammate repeat your result?', [
    week(1, 'Publish a repository') + ' with the files a second person needs.',
    week(2, 'Predict, break, fix') + ' gives that person an expected result.',
    week(8, 'Review a small change') + ' against the same expectation.',
], '10–13. Recall writing the first README and using the checker to expose a missing requirement. Try describing how a teammate could tell a missing prerequisite from a broken interaction.')
S.append(L.steps('Turn one day of tides into a promise', [
    ('File', 'Saved Quarry Bay tide heights.'),
    ('Rule', 'One numeric height per bar.'),
    ('Control', 'Choose a day; show its 24 heights and caption.'),
], '13–19. Read the sequence left to right. Compare changing the bar scale in Week 3 with choosing another day in Week 4. The first changes the encoding, the second changes the records.', 'What should stay true when the visitor changes the day?'))
page('WEEKS 3 + 4 → YOUR INTERFACE', 'Try January 31, then February', [
    week(3, 'Week 3 · tides.py') + ' reads the saved source for every drawing.',
    week(4, 'Week 4 · the tide selector') + ' changes the chart and caption together.',
    'February has fewer days. What should the visitor be allowed to select?',
], '19–24. Compare the Streamlit rerun with the browser client. The browser retrieves a month and can switch days within that response. Teams name one invalid input their own interface should handle.')
S.append(L.compare('Which change can a visitor perceive?',
    ('Moving dot', 'Reverse three frames.', 'Same images, opposite direction.'),
    ('Sine tone', 'Double 220 Hz to 440 Hz.', 'Higher pitch at the same amplitude.'),
    '24–29. Predict before answering. Changing the GIF frame duration changes speed; changing amplitude alters loudness. Ask which property communicates success in the team project.',
    'If sound is muted, which visual cue still tells the visitor what happened?'))
page('WEEKS 5 + 6 → WEEK 8', 'Turn a camera frame into one action', [
    week(5, 'Week 5 · pixels and frames') + ' gives each image a position in time.',
    week(8, 'Week 8 · hand landmarks') + ' maps a detected hand to a tile.',
    week(6, 'Week 6 · sound') + ' offers another way to acknowledge a selection.',
], '29–35. In the camera example, coordinates become positions in the frame. If the hand leaves, should the last tile stay selected? Try the decision without a camera. Live song generation and local speech setup were optional in Week 6.')
S.append(L.compare('Who owns the position?',
    ('Week 7 · two views', 'Red and blue are Ball instances.', 'Terminal and Pygame draw the same objects.'),
    ('Week 9 · two tabs', 'Each tab sends an action.', 'The server sends back the shared scene.'),
    '35–42. Advancing red does not move blue. Likewise, painting a new x in one tab does not change the server. Compare one model drawn twice with two clients receiving a snapshot.',
    'Your project opens a second view. Which copy decides what is true?'))
page('WEEKS 7 + 9 → WEEK 10', 'Close the tab. Restart the server.', [
    week(7, 'The Ball demo') + ' gives every instance its own position.',
    week(9, 'The connected scene') + ' gives a reconnecting tab the current snapshot.',
    week(10, 'The talking handbook') + ' can reopen saved conversation rows.',
], '42–48. A browser reconnect and a fresh server are different tests. Week 9 in-memory state resets on server restart. Ask teams which data may disappear and which should be restored.')
S.append(L.steps('Where did Pip get that answer?', [
    ('Source', 'Retrieve the relevant handbook passage.'),
    ('Context', 'Add prior turns for this conversation.'),
    ('Voice', 'Speak the answer using Pip’s voice.'),
], '48–54. Week 10 connects Week 6 speech with Week 9 message exchange. A fluent voice is no evidence for a policy. Ask for the cited passage, then reopen the conversation as another user. The full PDF index and the optional six-passage teaching fixture have different coverage.',
    'A correct citation and a private history need separate checks.'))
page('WEEKS 8 + 10 + 11', 'Try the candidate as a second person', [
    week(11, 'Route A · signed-in note') + ' — sign out, sign in as someone else, check whose note opens.',
    'Route B · Blender into Godot — identify the same object after export and import.',
    week(8, 'Team review') + ' — ask another teammate to check the result on the target device.',
], '54–60. Week 11 offered a choice of two tutorial routes. Connect the app route to Week 10 ownership and the asset route to Week 7 model/view. Pairs choose whichever check fits their actual delivery target.')
S.append(statement('Ten-minute break', '60–70 MINUTES', size=112,
    notes='60–70. Resume at minute 70 with the same project decision.'))
S.append(figure_slide('RECORDED EXAMPLE · OPTIONAL GODOT RESOURCE', 'One change, one unchanged check',
    F.feedback(), notes='70–74. The recorded model saw two lights at speed 125 after 180 ticks. It chose 275. The unchanged engine check reached the exit with three lights at tick 166. Edits stopped. Replaying this episode does not run fresh inference.'))
S.append(figure_slide('LATER DETERMINISTIC CAPTURE', 'What does the final frame establish?',
    F.screenshot('frame-end.png'), notes='74–78. The later film used the exact final source. The finish frame shows the visible ending. It does not show how the next action was chosen or prove that another build works. Ask which observation a project visitor can supply.'))
page('OPTIONAL EVIDENCE', 'Trace, film and playtest answer different questions', [
    f'[Recorded decision and engine observations]({COMPANION}/model-episode.json)',
    f'[Later film from the final source]({COMPANION}/evidence/model-selected-world.mp4) · [provenance]({COMPANION}/evidence/provenance.json)',
    f'[Optional Godot practical]({COMPANION}/godot-practice.md) · use your own project for today’s review.',
], '78–81. Compare the behavior check, the visible ending and a visitor understanding how to reach it. Only the last needs a human playtest.')
page('WEEK 8 → DELIVERY CANDIDATE', 'Two proposals, eleven seconds apart', [
    f'Leonida [#7366]({LEONIDA}/pull/7366) and [#7367]({LEONIDA}/pull/7367) proposed a fix for the same repository check.',
    'One tested additional containers; the other included cases that should pass.',
    f'The [coordination issue]({LEONIDA}/issues/7333) asks contributors to claim work first.',
], '81–86. Both descriptions include controls. Ask what unchanged test you would run on each revision before merging, which useful cases to preserve, and how to credit both contributors. Only the public PR discussions are needed.')
page('THURSDAY’S TUTOR MEETING', 'Which decision needs another pair of eyes?', [
    'Show the delivery candidate: a build, deployment or installation setup.',
    'Bring one playtest observation and the blocker it exposed.',
    f'[Group-project brief]({COURSE}/assignments/group-project.md) · [team progress guide]({COURSE}/week08/teamwork.md)',
], '86–90. Reuse last week’s feedback. For a broken build, show the last working interaction and say what has yet to be tested. The 26 November scheduled tutor meeting is part of the existing project.')
S.append(question('short_answer', 'Our visitor tries ___.\nWe saw ___.\nShould we change ___ or ___?',
    eyebrow_text='GROUP AMA · 90–95 MINUTES', size=88,
    hint='3 min to prepare, 2 min to choose a speaker. Ask aloud or pass a paper slip.',
    notes='90–95. Group AMA begins. Give each team three minutes to form one question and two to choose a spokesperson and an observation. On paper, write the question or ask it aloud. No login, vote or submission is needed.'))
S.append(L.rows('Group AMA · 95–115 minutes', [
    ('Ask', 'One group names the decision and what they tried.'),
    ('Answer', 'A second group offers a check; the tutor invites a follow-up.'),
    ('Rotate', 'Move to another group or a different kind of blocker.'),
], '95–115. Allow four rounds of five minutes (one to ask, three for answers, one for follow-up). Combine related questions in a large room and carry remaining questions to tutor support. With no network, collect paper slips and read them aloud.',
    'Ask what to cut, keep or test with a visitor.'))
page('AMA · 115–120 MINUTES', 'What will you try next?', [
    'Say the next check, who will try it, and what result would change your decision.',
    'Use your existing team progress record for tutor feedback and the next goal.',
    f'[Thursday’s paired tutorial]({COMPANION}/README.md) · break 55–65 · tutor support 100–120.',
], '115–119. Give teams two minutes to decide and hear one or two exits aloud. The tutorial is a separate 120 minutes. This conversation creates no extra grade or upload.')
S.append(end('One next check.', 'Take your candidate and your question to the tutor.',
    'SD5913 · WEEK 12', notes='119–120. Finish at minute 120. The public project brief remains the source for assessment.'))

DECK = {'title': 'SD5913 · Week 12 · Course review and group AMA',
        'pdf': 'SD5913-week12.pdf', 'slides': S}
