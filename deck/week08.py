"""SD5913 Week 8: teamwork, cloud environments, delivery and computer vision."""
from pathlib import Path
from deckgen import Slide, Rect, T, INK, WHITE, PAPER, ORANGE, MUTED, attach_reports
from deckgen.layouts import title, agenda, section, statement, content, question, code_panel, end, finalize

EYE = 'SD5913 / WEEK 08 / 29 OCTOBER 2026'
PFAD = 'https://github.com/sd5913/pfad/tree/2d99258f3a3d495ca68d7939ce5fde39d403b8ab/week08'
S = []


def boxes(eye, heading, blocks, note):
    slide = Slide(bg=WHITE, title=heading, notes=note)
    slide.chrome = False
    slide.els = [T(80, 24, 1760, 34, eye, 'monomed', 24, MUTED),
                 T(80, 80, 1760, 110, heading, 'xbold', 62, INK)]
    count = len(blocks)
    width = (1680 - 40 * (count - 1)) / count
    for i, (head, a, b) in enumerate(blocks):
        x = 120 + i * (width + 40)
        slide.els += [Rect(x, 300, width, 390, PAPER),
                      T(x + 30, 320, width - 60, 130, head, 'xbold', 96 if head.endswith('%') else 48, INK),
                      T(x + 30, 445, width - 60, 120, a, 'body', 42, INK),
                      T(x + 30, 565, width - 60, 120, b, 'body', 42, INK)]
    return slide

S.append(title(EYE, 'Build together.\nShip something.', 'Teamwork, cloud environments, delivery and computer vision.',
    notes='Two-hour lecture on 29 October, followed by a two-hour PFAD tutorial. Live camera demos start after the break.'))
S.append(question('multiple_choice', 'What is your group idea becoming?',
    choices=['A game', 'An app or creative tool', 'An installation', 'Something else / still deciding'],
    eyebrow_text='OPENING / YOUR GROUP PROJECT',
    notes='Invite each team to choose the closest direction. These categories overlap and an idea can change. ClassPoint if available; otherwise show of hands. Ask one or two teams what a person will do.'))
S.append(agenda(EYE, ['Group project and assessment', 'Teamwork: changes, review and conflicts', 'Codex cloud environments for app and game starters', 'Break', 'Actions, artifacts and deployment secrets', 'Live camera: OpenCV and MediaPipe', 'PFAD tutorial'],
    notes='Suggested pacing: opening/news/project 10 min; Git 20; cloud 25; break 10; Actions 20; camera demos 30; tutorial handoff 5 = 120 minutes.'))
S.append(content('NEWS / 28 OCTOBER', 'Who gets to build and remix?', [
    '[Switch 2](https://www.polygon.com/nintendo-switch-2-hackers-jailbreak-dumping-files-modding/): new access enables homebrew and mods.',
    '[Indie games](https://arstechnica.com/gaming/2026/10/ai-game-clones-are-making-indie-developers-afraid-to-show-their-work/): fear of AI clones delays a demo.',
    '[Agent research](https://alignment.anthropic.com/2026/red-teaming-auto-mode/): automated monitors can be bypassed.',
    '[OpenAI announcement](https://openai.com/index/introducing-gpt-6-1-terra/): test what coding agents produce.',
], body_size=42, notes='Use three minutes inside the opening; choose one or two stories, not four separate discussions. '
    'Polygon reported on 22 and 26 October that a Switch 2 exploit enabled modding and later file-system access on a specific firmware; '
    'the published demo is temporary and is not a general permanent jailbreak or kernel access. We have not tested a console. '
    'Ask: what would you add to a closed platform, and how does that differ from copying someone’s game or assets? '
    'Ars Technica reports a developer postponed a public demo over cloning concerns; that is a concern about potential copying, not proof the demo was copied. '
    'Anthropic’s 22 October research tested September configurations under controlled adversarial conditions, not everyday failure rates. '
    'Installed tools and automated monitors do not themselves authorize publishing or sharing data. '
    'The linked OpenAI announcement was inaccessible during the 28 October source check; do not quote its claims without verifying it.'))
S.append(section('01', 'Your group project', 'An ambitious idea, built and delivered together.', notes='Connect to the Week 7 idea and mock-up.'))
S.append(content('GROUP PROJECT / CANVAS', 'Register your repository now.', [
    'Create one shared GitHub repository for your team.',
    'Submit its URL on Canvas from this week; an initial README is enough.',
    'Keep building and documenting progress in that same repository.',
    'Final deadline: Sunday 6 December 2026, 23:59 HKT.',
    '[Group project brief](https://github.com/sd5913/pfad/blob/2d99258f3a3d495ca68d7939ce5fde39d403b8ab/assignments/group-project.md)',
], body_size=42, notes='Canvas assignment URL was not supplied. Instructor: add its actual link when available. Website URL submission; ensure the team submission settings match the actual Canvas group set. This does not change individual Assignment 3.'))
S.append(boxes('GROUP PROJECT / 40% OF COURSE GRADE', 'How the project is marked', [
    ('25%', 'Creative idea', 'Novelty and value'), ('50%', 'Code', 'Works; meets the brief'), ('25%', 'Execution', 'Steady, documented work')],
    'These are shares of the group-project mark, not separate course-grade percentages. Code includes handling complexity well. Execution means small steady increments and documented weekly progress.'))
S.append(content('PROJECT / FIRST AGREEMENT', 'Make the next step testable.', [
    'Who uses it, and what do they do?', 'What visible or audible response makes the idea special?',
    'What is the smallest working interaction your team can test?', 'Agree the scope together; credit code, assets and tools.',
], body_size=42, notes='An app, game, installation or another interactive project can use the workflow. AI assistance is allowed but need not be a feature.'))
S.append(section('02', 'Work as a team', 'One shared repository. Small, reviewable changes.', notes='Explain each step using one teammate adding a start button to a shared app.'))
def git_walkthrough(stage):
    heads = ['1. Alice starts a change', '2. Bob reviews the PR', '3. Both update main']
    steps = [
        [('ALICE / LOCAL', 'Pull main; branch', 'Edit, test, commit'),
         ('ALICE / LOCAL', 'Push to GitHub', 'git push'),
         ('ALICE / GITHUB', 'Open the PR', 'Request a review')],
        [('BOB / REVIEW', 'Read the PR', 'Run and test it'),
         ('BOB / GITHUB', 'Request a change', 'Explain the problem'),
         ('ALICE / LOCAL', 'Fix and test', 'Commit and push')],
        [('BOB / GITHUB', 'Check the fix', 'Approve the PR'),
         ('ALICE / GITHUB', 'Merge the PR', 'Integrate into main'),
         ('BOTH / LOCAL', 'Switch to main', 'Pull the update')],
    ][stage - 1]
    notes = [
        'In order: Alice pulls current main, creates feature/start-button, edits, tests and commits. She pushes the branch to GitHub, then opens a pull request comparing it with main and requests Bob’s review.',
        'In order: Bob reads the PR and diff, checks out the branch and tests it. He requests a change on the PR. Alice fixes and tests locally, then commits and pushes; the existing PR updates.',
        'In order: Bob checks the revised PR and approves it. Alice merges it into main on GitHub. Both teammates switch to main and git pull origin main before their next branch; their local copies do not update automatically.',
    ][stage - 1]
    slide = Slide(bg=WHITE, title=heads[stage - 1], notes=notes)
    slide.chrome = False
    slide.els = [T(80, 24, 1760, 34, 'TEAMWORK / SAME CHANGE / STEP %d OF 3' % stage, 'monomed', 24, MUTED),
                 T(80, 80, 1760, 100, heads[stage - 1], 'xbold', 62, INK)]
    for index, (label, action, detail) in enumerate(steps, start=1):
        x = 120 + (index - 1) * 590
        slide.els += [Rect(x, 300, 500, 430, PAPER),
                      T(x + 30, 325, 440, 95, str(index), 'xbold', 72, ORANGE),
                      T(x + 30, 435, 440, 75, label, 'xbold', 40, INK),
                      T(x + 30, 535, 440, 80, action, 'body', 44, INK),
                      T(x + 30, 635, 440, 75, detail, 'body', 40, INK)]
        if index < 3:
            slide.els.append(T(x + 510, 455, 80, 110, '→', 'xbold', 72, ORANGE))
    return slide

for stage in (1, 2, 3):
    S.append(git_walkthrough(stage))
S.append(boxes('TEAMWORK / SHARED REPOSITORY', 'From change to shared main', [
    ('1 / Branch', 'Update main', 'Create a feature branch'), ('2 / Change', 'Edit and test', 'Commit and push'),
    ('3 / Review', 'Open a pull request', 'Teammate tries it'), ('4 / Merge', 'Integrate on GitHub', 'Everyone updates main')],
    'Distinguish local checkout from GitHub. A commit is local until pushed; PR compares branch to main; review precedes merge; teammates pull afterward.'))
S.append(code_panel('TEAMWORK / LOCAL TERMINAL', 'A small change, step by step', [
    'git switch main', 'git pull origin main', 'git switch -c feature/start-button',
    '# edit and run the project checks', 'git add .', 'git commit -m "Add start button"', 'git push -u origin feature/start-button',
], caption='Then open a pull request on GitHub.', notes='Review git status and the staged diff before committing; never stage secrets. Explain each command and which state is local.'))
S.append(content('TEAMWORK / PULL REQUEST', 'Make it easy to review.', [
    'What changed? “Start button opens the first game screen.”', 'How can a teammate run it and try the change?',
    'What did you test? What is still untested?', 'Reviewer checks the diff and tries the interaction before merge.',
], body_size=42, notes='Show a real diff and PR if possible. Review feedback may require another commit and another test.'))
S.append(content('TEAMWORK / CONFLICT', 'Two people changed the same line.', [
    'Git marks both versions when it cannot combine the edits.', 'Read both intentions with your teammate; choose the correct combined result.',
    'Remove conflict markers, run the project and tests, then commit the resolution.',
    'After merge: teammates switch to main and pull.',
], body_size=42, notes='Worked example: both edit the start button label: one says Play, other Start. Show <<<<<<<, ======= and >>>>>>> in editor. Decide together, delete markers, test, git add and complete merge. Do not blindly choose one side.'))
S.append(content('TEAMWORK / REPOSITORY ACCESS', 'Choose how the team collaborates.', [
    'Shared repository: teammates have access and make feature branches.',
    'Fork + pull request: contributors propose changes from their own copy.',
    'Use descriptive commits and review; both routes need communication.',
    '[Git reference](https://github.com/sd5913/pfad/blob/2026/reference/git.md)',
], body_size=42, notes='The shared team repository is the suggested path. Do not expose secrets in PRs.'))
S.append(section('03', 'Build in the cloud', 'A coding environment is a prepared workspace.', notes='Demonstrate creating environments for the two starter repositories.'))
S.append(boxes('ENVIRONMENTS / THREE DISTINCT PLACES', 'Where does the work happen?', [
    ('Codex cloud', 'Develop a change', 'Tools + repository'), ('GitHub Actions', 'Run a fresh job', 'Tests + build'),
    ('Destination', 'Deliver the result', 'Artifact or website')],
    'A published Codex environment prepares later coding tasks; it does not deploy the app. Actions runner starts from workflow setup. A built artifact is not automatically a live deployment.'))
S.append(content('CODEX / DEMONSTRATION', 'Create a cloud environment.', [
    'Connect GitHub and choose the repository.', 'Create an environment; inspect its setup and dependency commands.',
    'Publish the environment, then start a task with it.', 'Ask for one change and checks; review the diff and output.',
    '[Official Codex cloud guide](https://learn.chatgpt.com/docs/environments/cloud-environments)',
], body_size=42, notes='Rehearse actual interface and permissions before class: Work in > Cloud > Select environment > Create environment, select repository, Get started, review setup, save and Publish, then start a task. UI and account availability may vary. Have a pre-created environment as a download-time fallback.'))
S.append(content('THREE STARTERS / CHOOSE YOUR PROJECT', 'Choose a starting point.', [
    '[Capacitor app starter](https://github.com/sd5913/capacitor-app-template): web interface and Android build.',
    '[Godot game starter](https://github.com/sd5913/godot-game-template): 2D game and desktop/web exports.',
    '[Python + uv app starter](https://github.com/sd5913/python-uv-app-template): Python source and desktop bundles.',
    'Create a team repository, open it in Codex and check CI.',
], body_size=42, notes='Demonstrate Capacitor and Godot environment creation and one traceable change within the planned 25 minutes. Python + uv is a third option: run source with uv and bundle desktop apps with PyInstaller; each OS builds on its own runner. Teams may choose other frameworks and targets.'))
S.append(content('CODEX / A USEFUL TASK', 'Ask for one verifiable change.', [
    '“Make the player move faster after collecting a star.”', 'Name the file or behaviour and the expected result.',
    'Ask for the relevant checks and how to run the result.', 'Inspect the diff, run it, request a teammate review.',
], body_size=42, notes='AI output is a proposed change, not acceptance evidence. Do not upload private camera frames, passwords or student data.'))
S.append(statement('Take a break.\nBack in 10 minutes.', eyebrow_text='BREAK / 10 MINUTES', notes='Prepare the camera, lighting and examples before resuming.'))
S.append(section('04', 'From commit to delivery', 'GitHub Actions runs the workflow for your team.', notes='Use Tetrilaunch as a concrete multiplatform case, not a requirement to build every target.'))
S.append(boxes('GITHUB ACTIONS / CHANGE TO OUTPUT', 'Follow the result', [
    ('Push / PR', 'Workflow starts', 'Fresh runner'), ('Checks', 'Install and test', 'Build on each OS'),
    ('Artifact', 'Download and run', 'Or deploy website')],
    'A CI job uses its own runner and workflow, independent of the Codex environment. A green job is evidence for commands it actually ran, not proof of usability.'))
S.append(content('CASE STUDY / TETRILAUNCH', 'One project, several delivery paths.', [
    '[Desktop workflow](https://github.com/venetanji/tetrilaunch/blob/main/.github/workflows/desktop.yml): Windows, macOS and Linux matrix.',
    '[Android](https://github.com/venetanji/tetrilaunch/blob/main/.github/workflows/android.yml) and [iOS](https://github.com/venetanji/tetrilaunch/blob/main/.github/workflows/ios.yml): mobile builds and signing.',
    '[Production deployment](https://github.com/venetanji/tetrilaunch/blob/main/.github/workflows/production.yml): Cloudflare Worker.',
    'Build artifacts first. Stores and release signing are additional steps.',
], body_size=42, notes='Tetrilaunch started as a Python/Pygame prototype; its client uses Capacitor and Electron desktop packaging. The root web build is a marketing site, not the whole game. Explain a matrix and downloaded artifact. Do not trigger releases.'))
S.append(content('GITHUB / SECRETS', 'Give a job access to a token.', [
    'Create a scoped provider token for the destination.', 'Repository → Settings → Secrets and variables → Actions → New repository secret.',
    'Use a placeholder today: CLOUDFLARE_API_TOKEN.', 'The workflow references the secret; the value stays out of Git.',
], body_size=42, notes='Show the settings path with fake values only. A GitHub environment can hold environment-scoped secrets; a job must name that environment to access them. Protection rules are configured settings, not guaranteed by the YAML name.'))
S.append(code_panel('GITHUB ACTIONS / DEPLOYMENT EXAMPLE', 'A secret is supplied to the job', [
    'jobs:', '  deploy:', '    environment: production', '    runs-on: ubuntu-latest', '    steps:', '      # checkout, install and build first', '      - run: npx wrangler deploy', '        env:', '          CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}',
], caption='Configure the destination and token separately.', notes='Illustrative excerpt, not a complete workflow. Compare Tetrilaunch production.yml. GitHub secrets are not source control; do not print them. A token embedded in a public browser bundle is visible to users. Separate deploy tokens, signing credentials and runtime secrets.'))
S.append(content('DELIVERY / TROUBLESHOOT', 'The build is green. Is it delivered?', [
    'Open the Actions run: which job ran, and which artifact exists?', 'Download and run the artifact, or open the deployed destination.',
    'Environment-scoped secret missing? Check the job names that environment.', 'Provider tokens need access to the correct destination.',
], body_size=42, notes='Tetrilaunch desktop workflow documents a missing environment binding that prevented access to signing secrets. Named environment alone does not prove approval protection.'))
S.append(section('05', 'Camera → interaction', 'OpenCV captures frames. MediaPipe finds structure.', notes='Live camera demo: reserve 30 minutes. Preflight device, lighting, dependencies and model downloads.'))
S.append(boxes('LIVE DEMO / PIPELINE', 'From light to an action', [
    ('OpenCV', 'Camera → frame', 'BGR → RGB'), ('MediaPipe', 'Model → landmarks', 'Coordinates + confidence'),
    ('Your code', 'Map the result', 'Draw or change state')],
    'No hand is a valid result: make the response safe when detection disappears. Models can fail under poor light, occlusion or unfamiliar camera angles.'))
S.append(content('LIVE / FACE + HAND', 'Look at what the model returns.', [
    'Face detector: a box around each detected face.', 'Hand Landmarker: 21 points per hand, including index fingertip 8.',
    'Move closer, rotate your hand, hide it: when does tracking fail?',
    '[Modern source and run commands](https://github.com/sd5913/pfad/blob/2d99258f3a3d495ca68d7939ce5fde39d403b8ab/week08/README.md)',
], body_size=42, notes='From PFAD root run: uv run --project week08 python week08/vision.py face; then hand. Press q to stop. Show vision.py and the model source. Camera demo requires graphical desktop and permission.'))
S.append(content('LIVE / HAND TO RESPONSE', 'A coordinate becomes a choice.', [
    'Read landmark 8: the index fingertip.', 'Map x < 0.5 to blue and x ≥ 0.5 to red.',
    'If no hand is detected, select neither.', '[Hand-to-tile example](https://github.com/sd5913/pfad/blob/2d99258f3a3d495ca68d7939ce5fde39d403b8ab/week08/hand_tiles.py)',
], body_size=42, notes='Run no-camera sample first: python -B week08/hand_tiles.py. Then if preflighted: uv run --project week08 python week08/hand_tiles.py --camera --model week08/models/hand.task. Add --camera-index 1 if using the second camera. Check exact command and model before lecture.'))
S.append(content('LIVE / GESTURE + POSE', 'Compare two kinds of output.', [
    'Gesture Recognizer: a trained model returns a gesture label and score.',
    'Pose Landmarker: body points can drive an interaction.',
    'A score is model confidence, not proof of intent.',
    '[Examples and source](https://github.com/sd5913/pfad/blob/2d99258f3a3d495ca68d7939ce5fde39d403b8ab/week08/vision.py)',
], body_size=42, notes='Run gesture then pose. This modern trained recognizer differs from the 2025 handwritten landmark rules. Discuss what happens when the hand or body leaves view.'))
S.append(content('LIVE / SEGMENTATION', 'A mask changes the background.', [
    'The model estimates a person mask for each frame.', 'OpenCV combines foreground with a replacement background.',
    'Try hair, a raised hand and a busy background.', '[All Week 8 vision exercises](https://github.com/sd5913/pfad/tree/2d99258f3a3d495ca68d7939ce5fde39d403b8ab/week08)',
], body_size=42, notes='Run uv run --project week08 python week08/vision.py segment. Segmentation estimates pixels, distinct from landmarks. No camera data needs uploading or saving.'))
S.append(content('TUTORIAL / TWO HOURS', 'Try all nine vision examples.', [
    'Start with camera setup, face and hand; then pose, mesh and gestures.',
    'Combine models, try segmentation, and examine expression output critically.',
    'For each example: run it, observe, change one thing, and discuss a limitation.',
    '[Open the PFAD Week 8 tutorial](https://github.com/sd5913/pfad/blob/2d99258f3a3d495ca68d7939ce5fde39d403b8ab/week08/README.md)',
], body_size=42, notes='The tutorial is led by the TA using the README, independent of instructor ClassPoint login. Optional team cloud setup follows the camera work where time allows.'))
S.append(end('Build together.\nShow your work.', 'One idea. One shared repository. A working next step.', EYE,
    notes='Remind teams to submit the shared repository URL and continue developing until 6 December 23:59 HKT.'))
for slide in S:
    if slide.cp:
        slide.els[0].name = 'question-eyebrow'
attach_reports(S, Path(__file__).resolve().parent / 'week08-reports.json')
DECK = dict(title='SD5913 / Programming / Week 08', slides=finalize(S, EYE), pdf='SD5913-week08.pdf')
