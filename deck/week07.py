"""22 October: recap, AMA, midterm, and ambitious team-project ideas."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen import attach_reports
from deckgen.layouts import title, agenda, statement, content, activity, question, end, finalize
from week07_recap import recap_slides

S = []
S.append(title('SD5913 / WEEK 07 / 22 OCTOBER 2026',
    'Build something\namazing.', 'Recap. Ask anything. Midterm. Your team’s next big idea.',
    notes='Keep the week07 content number aligned with PFAD. Teaching date: Thursday 22 October 2026. '
    'The fixed test window is 10:00–10:30 HKT. Reserve fifteen minutes for recap and fifteen for AMA '
    'before 10:00; exact class opening follows the timetable. Never put assessed questions or keys in this public deck.'))
S.append(agenda('TODAY / RECAP → QUIZ → BUILD', [
    'Before 10:00 / key slides from Weeks 1–6, then Ask Me Anything',
    '10:00–10:30 / midterm on Canvas / 40 questions',
    'After 10:30 / inspiration and team-registration demo',
    'Step 1 / 20 minutes / form your team and submit your idea',
    'Step 2 / 20 minutes / submit an image mock-up of the project',
], notes='Suggested pacing if class opens at 09:30: recap 09:30–09:45 and AMA 09:45–10:00. '
    'Only the 10:00–10:30 test window is fixed by the instructor. Inspiration is after the test.'))
RECAP = recap_slides(first_number=len(S)+1)
S.extend(RECAP)
S.append(question('short_answer', 'Ask me anything.',
    hint='What still feels unclear?\nSend your questions before the 10:00 test.',
    eyebrow_text='BEFORE 10:00 / CLASSPOINT / YOUR QUESTIONS',
    cp={'type':'short_answer','hide_names':False,'multiple':True},
    notes='Use this as a question inbox. Read and discuss selected questions; more than one per person is welcome. '
    'This is not graded. End at 10:00 so students get the full thirty minutes.'))
S.append(content('MIDTERM / 22 OCTOBER / 10% OF COURSE', 'Get ready for Canvas.', [
    '40 multiple-choice questions. 30 minutes. Open book.',
    'The test covers taught material from Weeks 1–6.',
    'Open the quiz when instructed. Report access problems immediately.',
    'Follow the announced rules for tools and collaboration.',
], body_size=36, notes='Confirm actual Canvas timer, availability, accommodations and result visibility. '
    'Open-book does not establish AI permission. Instructor must announce that policy. No questions or keys here.'))
S.append(statement('Midterm quiz.\n10:00–10:30.',
    eyebrow_text='CANVAS / 40 QUESTIONS / 30 MINUTES', size=112,
    notes='Leave this holding slide up throughout the test. At 10:30 confirm submission, then move into teams. '
    'Support access issues privately; do not shorten the test for the workshop.'))
S.append(statement('Build something amazing\nwith your team.',
    eyebrow_text='AFTER 10:30 / YOUR GROUP PROJECT', size=96,
    notes='Aim high. The project can be a useful app, a creative instrument, or a game. '
    'AI can help build it, but AI inside the finished product is not a requirement.'))
S.append(content('INSPIRATION / REINVENT AN APP', 'What do you wish it did?', [
    'Choose an app you know, or a tool you genuinely need.',
    'Observe one useful behaviour. Describe its inputs, outputs and edge cases.',
    'Rebuild that interaction in your own way. Add the feature you wish existed.',
    '[Explore REA: tools for inspecting software](https://github.com/morluto/rea)',
], body_size=34, notes='REA is the reference already discussed in Week 6; do not attribute it to Hera. '
    'Treat the link as inspiration, not a requirement to install or use reverse-engineering tools. '
    'Work on software you have permission to inspect, or a teacher-owned toy interface. '
    'An analysis tool’s license grants no rights over its targets. Use original or licensed code/assets; '
    'do not bypass access controls. Observable behaviour and independent tests are useful starting points.'))
S.append(content('INSPIRATION / GAME MASHUPS', 'Two mechanics. A new experience.', [
    'What if a puzzle game had rhythm? What if a racing game changed with sound?',
    'Combine mechanics around one compelling player action.',
    'Give the result its own rules, look and sound.',
    '[Explore Melty’s game-remix examples](https://melty.gg/)',
], body_size=35, notes='Show examples rather than installing in class. Do not claim arbitrary game pairs work, '
    'or that Melty uses REA. Owning a game does not automatically permit redistributing its assets. '
    'An original small game inspired by mechanics is a valid ambitious direction.'))
S.append(content('AMBITION / A BIG VISION, A FIRST PLAYABLE MOMENT', 'Start with the exciting part.', [
    'Imagine the version you would love to use or play.',
    'Choose one interaction that makes the idea special.',
    'What will a person do? What changes? What feedback tells them it worked?',
    'Identify the hardest assumption. Make that your first experiment.',
], body_size=35, notes='Keep ambition high while making the next step concrete. Examples: a drawing tool that becomes '
    'an instrument, a personal workflow app, or a game combining unfamiliar mechanics. No additional deliverable today.'))
S.append(content('LIVE DEMO / TEAM REGISTRATION', 'Find your people. Join one team.', [
    'Watch Gio demonstrate the actual Canvas group-registration route.',
    'Form a team around an idea you want to build together.',
    'Choose one representative for the text and image submissions.',
    'Use the same team name on both. Ask for help if you need a team.',
], body_size=35, notes='Check the actual Canvas group set before class. Team size follows the instructor’s course '
    'arrangements; no new number is imposed here. Demonstrate both ClassPoint collection routes. '
    'Keep student membership and submissions out of this public repository.'))
S.append(activity('01 / TEAM IDEA', 20, 'Form your team. Aim big.', [
    'Join the same Canvas team. Pick a direction everyone wants to make.',
    'Describe who it is for, what they do, and how your app or game responds.',
    'Name what you will reinvent or combine, and the first interaction you will test.',
    'One representative submits one idea text on ClassPoint, with your team name.',
], eyebrow_text='TEAM TEXT', cp={'type':'short_answer','hide_names':False,'multiple':False},
    notes='Twenty minutes including forming/registering, discussing and submitting. Suggested split: '
    'five minutes team setup, ten minutes choosing/describing, five minutes upload/check. '
    'No new word count, grading weight or extra proposal upload. This is a provisional idea for feedback.'))
S.append(activity('02 / PROJECT MOCK-UP', 20, 'Show what you want to build.', [
    'Sketch, mock up or generate one image of the app or game in use.',
    'Show the main screen or moment of play. Label the action and response.',
    'Match the idea you just submitted. A photographed paper sketch is fine.',
    'The same representative submits one image on ClassPoint, with the team name.',
], eyebrow_text='TEAM IMAGE', cp={'type':'image_upload','hide_names':False},
    notes='Twenty minutes including image creation and checking the upload. No paid tool or new account required. '
    'The image illustrates the intended experience; it is not evidence of a working prototype. '
    'No video, pitch deck or extra critique submission today.'))
S.append(content('FINISH / TWO SUBMISSIONS', 'One idea. One image. One team.', [
    'Your idea text and image mock-up are both visible in ClassPoint.',
    'Both use the same team name and describe the same project.',
    'Everyone has joined the correct Canvas team.',
    'Reopen both submissions together; ask for help before leaving.',
], body_size=37, notes='Checking is part of the two activity timers. Use remaining time for optional discussion and '
    'support, not an additional required submission.'))
S.append(content('GROUP PROJECT / 40%', 'Turn the idea into a shared build.', [
    'One shared GitHub repository showing everyone’s contributions.',
    'Original code and multimedia. Credit the tools and assets you use.',
    'Agree the project scope by Week 8.',
    'Today’s idea and mock-up are the starting point for that conversation.',
], body_size=36, notes='Preserve the existing SD5913 assessment described in Week 1. Do not import SD2112’s '
    'AI + X condition, team-size rule, poster/video/mediation deliverables or rubric. '
    'Scope agreement and the full project brief remain with the instructor.'))
S.append(content('SEPARATE / INDIVIDUAL ASSIGNMENT 3 / 15%', 'Your interactive experience.', [
    'Due Sunday 1 November 2026, 23:59 HKT.',
    'Build something with meaningful user input and clear feedback.',
    'Submit your own GitHub repository URL on Canvas.',
    'Follow the existing brief, README, PROCESS and credit requirements.',
], body_size=36, notes='Assignment 3 remains individual and distinct from today’s team work. '
    'Existing brief: syllabus/03-interactive-experience.md. No changes to its deadline, weight or rubric.'))
S.append(end('Aim big.\nBuild together.', 'An idea worth making. An interaction worth trying.',
    'SD5913 / WEEK 07 / 22 OCTOBER 2026'))
for slide in S:
    if slide.cp:
        slide.els[0].name = 'question-eyebrow'
attach_reports(S, Path(__file__).resolve().parent / 'week07-reports.json')
DECK = dict(title='SD5913 / Programming / Week 07',
            slides=finalize(S, 'SD5913 / WEEK 07 / 22 OCTOBER 2026'), pdf='SD5913-week07.pdf')
