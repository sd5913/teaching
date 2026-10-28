"""SD5913 Week 8: teamwork, cloud environments, delivery and computer vision."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen import Rect, T, INK, WHITE, PAPER, ORANGE, MUTED, attach_reports
from deckgen.layouts import title, agenda, section, statement, content, question, code_panel, end, finalize
from week08_visuals import (
    canvas, grading, submission, conflict, starters, camera_frame, objects, fingertip, tiles, tutorial,
)
from week08_agile import agile_slides

EYE = 'SD5913 / WEEK 08 / 29 OCTOBER 2026'
PFAD = 'https://github.com/sd5913/pfad/blob/f88e2d37a90160868b90f0d9ced810c1137622f8/week08'
S = []


def boxes(eye, heading, blocks, note, flow=False, caption=None):
    slide = canvas(eye, heading, note)
    count = len(blocks)
    gap = 80 if flow else 40
    width = (1680 - gap * (count - 1)) / count
    for i, (head, a, b) in enumerate(blocks):
        x = 120 + i * (width + gap)
        slide.els += [Rect(x, 370, width, 390, PAPER),
                      T(x + 28, 400, width - 56, 100, head, 'xbold', 44, INK),
                      T(x + 28, 535, width - 56, 100, a, 'body', 40, INK),
                      T(x + 28, 650, width - 56, 100, b, 'body', 40, INK)]
        if flow and i < count - 1:
            slide.els.append(T(x + width + 8, 525, gap - 16, 90,
                               '→', 'xbold', 60, ORANGE, align='c'))
    if caption:
        slide.els.append(T(120, 860, 1680, 85, caption, 'body', 40, INK))
    return slide

S.append(title(EYE, 'Build together.\nShip something.', 'Teamwork, cloud environments, delivery and computer vision.',
    notes='Two-hour lecture on 29 October, followed by a two-hour PFAD tutorial. Live camera demos start after the break.'))
S.append(question('multiple_choice', 'What is your group idea becoming?',
    choices=['A game', 'An app or creative tool', 'An installation', 'Something else / still deciding'],
    eyebrow_text='OPENING / YOUR GROUP PROJECT',
    notes='Invite each team to choose the closest direction. These categories overlap and an idea can change. ClassPoint if available; otherwise show of hands. Ask one or two teams what a person will do.'))
S.append(agenda(EYE, ['Project, assessment and news', 'Agile, Scrum and GitHub tracking', 'Git workflow + Codex environments', '10-minute break', 'Actions, builds and deployment secrets', 'Live camera: OpenCV + MediaPipe', 'PFAD: the two-hour tutorial'],
    notes='Suggested pacing: opening/news/project 10 min; Agile/Scrum 20; Git 15; cloud 15; break 10; Actions 15; camera demos 30; tutorial handoff 5 = 120 minutes.'))
S.append(content('NEWS / 28 OCTOBER', 'Who gets to build and remix?', [
    '**Switch 2:** [new access enables homebrew and mods](https://www.polygon.com/nintendo-switch-2-hackers-jailbreak-dumping-files-modding/).',
    '**Indie games:** [fear of AI clones delays a demo](https://arstechnica.com/gaming/2026/10/ai-game-clones-are-making-indie-developers-afraid-to-show-their-work/).',
    '**Agent research:** [automated monitors can be bypassed](https://alignment.anthropic.com/2026/red-teaming-auto-mode/).',
    '**OpenAI announcement:** [test what coding agents produce](https://openai.com/index/introducing-gpt-6-1-terra/).',
], body_size=42, notes='Use three minutes inside the opening; choose one or two stories, not four separate discussions. '
    'Polygon reported on 22 and 26 October that a Switch 2 exploit enabled modding and later file-system access on a specific firmware; '
    'the published demo is temporary and is not a general permanent jailbreak or kernel access. We have not tested a console. '
    'Ask: what would you add to a closed platform, and how does that differ from copying someone’s game or assets? '
    'Ars Technica reports a developer postponed a public demo over cloning concerns; that is a concern about potential copying, not proof the demo was copied. '
    'Anthropic’s 22 October research tested September configurations under controlled adversarial conditions, not everyday failure rates. '
    'Installed tools and automated monitors do not themselves authorize publishing or sharing data. '
    'The linked OpenAI announcement was inaccessible during the 28 October source check; do not quote its claims without verifying it.'))
S.append(section('01', 'Your group project', 'An ambitious idea, built and delivered together.', notes='Connect to the Week 7 idea and mock-up.'))
S.append(submission('https://github.com/sd5913/pfad/blob/f88e2d37a90160868b90f0d9ced810c1137622f8/assignments/group-project.md',
    'Canvas repository submissions open this week. Final deadline: Sunday 6 December 2026, 23:59 HKT. '
    'Students accept the sd5913 organization invitation with their registered GitHub account. '
    'One teammate creates a public repository with Owner: sd5913, for example group-your-project, '
    'then grants teammates Write access. Missing Owner option means membership needs checking. '
    'Help teams transfer an existing personal project and preserve its history. '
    'Canvas assignment URL was not supplied. Instructor: add its actual link when available. Website URL submission; ensure the team submission settings match the actual Canvas group set. This does not change individual Assignment 3.'))
S.append(grading(
    'These are shares of the group-project mark, not separate course-grade percentages. Code includes handling complexity well. Execution is 25%: small steady increments, visible team planning and review, and documented weekly progress. The Agile/Scrum and GitHub tracking block makes this concrete.'))
S.append(content('PROJECT / FIRST AGREEMENT', 'Make the next step testable.', [
    'Who uses it, and what do they do?', 'What visible or audible response makes the idea special?',
    'What is the smallest working interaction your team can test?', 'Agree the scope together; credit code, assets and tools.',
], body_size=42, notes='An app, game, installation or another interactive project can use the workflow. AI assistance is allowed but need not be a feature.'))
S.append(section('02', 'Work as a team', 'Plan together. Build, review and adapt.', notes='Agile/Scrum concepts are quiz material. Connect team planning and progress evidence to the 25% execution criterion, then explain Git using one teammate adding a start button to a shared app.'))
S.extend(agile_slides(f'{PFAD}/teamwork.md'))
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
    slide = canvas('TEAMWORK / SAME CHANGE / STEP %d OF 3' % stage,
                   heads[stage - 1], notes)
    for index, (label, action, detail) in enumerate(steps, start=1):
        x = 120 + (index - 1) * 590
        slide.els += [Rect(x, 370, 500, 450, PAPER),
                      T(x + 30, 395, 440, 95, str(index), 'xbold', 72, ORANGE),
                      T(x + 30, 505, 440, 75, label, 'xbold', 40, INK),
                      T(x + 30, 605, 440, 80, action, 'body', 44, INK),
                      T(x + 30, 720, 440, 75, detail, 'body', 40, INK)]
        if index < 3:
            slide.els.append(T(x + 510, 540, 80, 110, '→', 'xbold', 72, ORANGE))
    return slide

for stage in (1, 2, 3):
    S.append(git_walkthrough(stage))
S.append(boxes('TEAMWORK / SHARED REPOSITORY', 'From change to shared main', [
    ('1 / Branch', 'Update main', 'New branch'), ('2 / Change', 'Edit and test', 'Commit; push'),
    ('3 / Review', 'Open a PR', 'Teammate tests'), ('4 / Merge', 'Merge on GitHub', 'Everyone pulls')],
    'Distinguish local checkout from GitHub. A commit is local until pushed; PR compares branch to main; review precedes merge; teammates pull afterward.',
    flow=True, caption='A local commit becomes shared when you push. Teammates update when they pull.'))
S.append(code_panel('TEAMWORK / LOCAL TERMINAL', 'A small change, step by step', [
    'git switch main', 'git pull origin main', 'git switch -c feature/start-button',
    '# edit and run the project checks', 'git add .', 'git commit -m "Add start button"', 'git push -u origin feature/start-button',
], caption='Then open a pull request on GitHub.', lang=None, notes='Review git status and the staged diff before committing; never stage secrets. Explain each command and which state is local.'))
S.append(content('TEAMWORK / PULL REQUEST', 'Make it easy to review.', [
    'What changed? “Start button opens the first game screen.”', 'How can a teammate run it and try the change?',
    'What did you test? What is still untested?', 'Reviewer checks the diff and tries the interaction before merge.',
], body_size=42, notes='Show a real diff and PR if possible. Review feedback may require another commit and another test.'))
S.append(conflict('Worked example: both edit the start button label: one says Play, other Start. '
    'Git marks both versions when it cannot combine edits. Read both intentions with your teammate. '
    'The agreed result shown here is Play; Start or a new label could be correct for another team. '
    'Decide together, delete markers, run the project and tests, git add and complete the merge. '
    'Do not blindly choose one side. After merge: teammates switch to main and pull.'))
def collaboration_paths():
    slide = canvas('TEAMWORK / REPOSITORY ACCESS', 'Choose how the team collaborates.', (
        'The shared team repository is the suggested path: teammates have write access, '
        'push feature branches to that repository, and open a PR into its main branch. '
        'In the fork path, a contributor first creates their own GitHub copy of the team '
        'repository, pushes a branch there, then opens a cross-repository PR back to the '
        'team repository. A maintainer reviews and merges it; a fork contributor does '
        'not need write access to the team repository. Both paths need review and '
        'communication. Do not expose secrets in PRs. Git reference: '
        'https://github.com/sd5913/pfad/blob/2026/reference/git.md'))
    slide.els += [
        T(120, 325, 1680, 65, '1 / Shared repository', 'xbold', 48, INK),
        Rect(120, 400, 1680, 205, PAPER),
        T(150, 415, 1620, 55, 'ONE TEAM REPOSITORY  /  teammates have write access', 'semibold', 40, INK),
        Rect(155, 490, 400, 90, WHITE),
        T(175, 505, 360, 58, 'Feature branch', 'semibold', 42, INK),
        T(580, 500, 90, 70, '→', 'xbold', 56, ORANGE),
        Rect(685, 490, 400, 90, WHITE),
        T(705, 505, 360, 58, 'Pull request', 'semibold', 42, INK),
        T(1110, 500, 90, 70, '→', 'xbold', 56, ORANGE),
        Rect(1215, 490, 520, 90, INK),
        T(1235, 505, 480, 58, 'Team main', 'semibold', 42, WHITE),
        T(120, 655, 1680, 65, '2 / Fork + pull request', 'xbold', 48, INK),
        Rect(120, 740, 610, 150, PAPER),
        T(150, 755, 550, 55, 'Contributor’s fork', 'semibold', 44, INK),
        T(150, 820, 550, 55, 'Their own copy + branch', 'body', 40, INK),
        T(750, 735, 420, 55, 'PULL REQUEST', 'semibold', 40, INK, align='c'),
        Rect(810, 828, 240, 5, ORANGE),
        T(1035, 795, 80, 80, '→', 'xbold', 52, ORANGE),
        Rect(1190, 740, 610, 150, INK),
        T(1220, 755, 550, 55, 'Team repository', 'semibold', 44, WHITE),
        T(1220, 820, 550, 55, 'Review + merge to main', 'body', 40, WHITE),
        T(120, 925, 1680, 55, '[Git reference](https://github.com/sd5913/pfad/blob/2026/reference/git.md)  /  Both paths need review.', 'body', 36, MUTED),
    ]
    return slide


S.append(collaboration_paths())
S.append(section('03', 'Build in the cloud', 'A coding environment is a prepared workspace.', notes='Demonstrate creating environments for the two starter repositories.'))
S.append(boxes('ENVIRONMENTS / THREE DISTINCT PLACES', 'Where does the work happen?', [
    ('Codex cloud', 'Develop a change', 'Tools + repository'), ('GitHub Actions', 'Run a fresh job', 'Tests + build'),
    ('Destination', 'Deliver the result', 'Artifact or website')],
    'A published Codex environment prepares later coding tasks; it does not deploy the app. Actions runner starts from workflow setup. A built artifact is not automatically a live deployment.',
    flow=True, caption='Prepare a workspace → build a change → deliver and try the result.'))
S.append(content('CODEX / DEMONSTRATION', 'Create a cloud environment.', [
    '**1 / Connect** GitHub and choose the repository.', '**2 / Prepare** an environment; review setup and dependencies.',
    '**3 / Publish** the environment, then start a task with it.', '**4 / Verify** one change: review the diff and check the result.',
    '[Official Codex cloud guide](https://learn.chatgpt.com/docs/environments/cloud-environments)',
], body_size=42, notes='Rehearse actual interface and permissions before class: Work in > Cloud > Select environment > Create environment, select repository, Get started, review setup, save and Publish, then start a task. UI and account availability may vary. Have a pre-created environment as a download-time fallback.'))
S.append(starters('Use this template > Create a new repository, choose Owner: sd5913, and create one public group repository. Students must first accept their organization invitation. The creator or instructor grants teammates Write access. Demonstrate Capacitor and Godot environment creation and one traceable change within the planned 15 minutes. Use prepared repositories and setup commands: about five minutes for each environment and five for the task/review. Python + uv is a third option: run source with uv and bundle desktop apps with PyInstaller; each OS builds on its own runner. Teams may choose other frameworks and targets.'))
S.append(content('CODEX / A USEFUL TASK', 'Ask for one verifiable change.', [
    '“Make the player move faster after collecting a star.”', 'Name the file or behaviour and the expected result.',
    'Ask for the relevant checks and how to run the result.', 'Inspect the diff, run it, request a teammate review.',
], body_size=42, notes='AI output is a proposed change, not acceptance evidence. Do not upload private camera frames, passwords or student data.'))
S.append(statement('Take a break.\nBack in 10 minutes.', eyebrow_text='BREAK / 10 MINUTES', notes='Prepare the camera, lighting and examples before resuming.'))
S.append(section('04', 'From commit to delivery', 'GitHub Actions runs the workflow for your team.', notes='Use Tetrilaunch as a concrete multiplatform case, not a requirement to build every target.'))
S.append(boxes('GITHUB ACTIONS / CHANGE TO OUTPUT', 'Follow the result', [
    ('Push / PR', 'Workflow starts', 'Fresh runner'), ('Checks', 'Install and test', 'Build on each OS'),
    ('Artifact', 'Download and run', 'Or deploy website')],
    'A CI job uses its own runner and workflow, independent of the Codex environment. A green job is evidence for commands it actually ran, not proof of usability.',
    flow=True, caption='Open the run → inspect the jobs → download or visit the result.'))
S.append(content('CASE STUDY / TETRILAUNCH', 'One project, several delivery paths.', [
    '[Desktop workflow](https://github.com/venetanji/tetrilaunch/blob/main/.github/workflows/desktop.yml): Windows, macOS and Linux matrix.',
    '[Android](https://github.com/venetanji/tetrilaunch/blob/main/.github/workflows/android.yml) and [iOS](https://github.com/venetanji/tetrilaunch/blob/main/.github/workflows/ios.yml): mobile builds and signing.',
    '[Production deployment](https://github.com/venetanji/tetrilaunch/blob/main/.github/workflows/production.yml): Cloudflare Worker.',
    'Build artifacts first. Stores and release signing are additional steps.',
], body_size=42, notes='Tetrilaunch started as a Python/Pygame prototype; its client uses Capacitor and Electron desktop packaging. The root web build is a marketing site, not the whole game. Explain a matrix and downloaded artifact. Do not trigger releases.'))
S.append(content('GITHUB / SECRETS', 'Give a job access to a token.', [
    '**1 / Create** a scoped provider token for the destination.',
    '**2 / Open** repository Settings → Secrets and variables → Actions.',
    '**3 / Add** a New repository secret: CLOUDFLARE_API_TOKEN.',
    '**4 / Reference** it in the workflow; keep the value out of Git.',
], body_size=42, notes='Show the settings path with fake values only. A GitHub environment can hold environment-scoped secrets; a job must name that environment to access them. Protection rules are configured settings, not guaranteed by the YAML name.'))
S.append(code_panel('GITHUB ACTIONS / DEPLOYMENT EXAMPLE', 'A secret is supplied to the job', [
    'jobs:', '  deploy:', '    environment: production', '    runs-on: ubuntu-latest', '    steps:', '      # checkout, install and build first', '      - run: npx wrangler deploy', '        env:', '          CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}',
], caption='Configure the destination and token separately.', lang=None, notes='Illustrative excerpt, not a complete workflow. Compare Tetrilaunch production.yml. GitHub secrets are not source control; do not print them. A token embedded in a public browser bundle is visible to users. Separate deploy tokens, signing credentials and runtime secrets.'))
S.append(content('DELIVERY / TROUBLESHOOT', 'The build is green. Is it delivered?', [
    'Open the Actions run: which job ran, and which artifact exists?', 'Download and run the artifact, or open the deployed destination.',
    'Environment-scoped secret missing? Check the job names that environment.', 'Provider tokens need access to the correct destination.',
], body_size=42, notes='Tetrilaunch desktop workflow documents a missing environment binding that prevented access to signing secrets. Named environment alone does not prove approval protection.'))
S.append(section('05', 'Camera → interaction', 'OpenCV captures frames. MediaPipe finds structure.', notes='Live camera demo: reserve 30 minutes. Preflight device, lighting, dependencies and model downloads.'))
S.append(boxes('LIVE DEMO / PIPELINE', 'From light to an action', [
    ('OpenCV', 'Camera → frame', 'BGR → RGB'), ('MediaPipe', 'Model → landmarks', 'Coordinates + confidence'),
    ('Your code', 'Map the result', 'Draw or change state')],
    'No hand is a valid result: make the response safe when detection disappears. Models can fail under poor light, occlusion or unfamiliar camera angles.',
    flow=True, caption='A model predicts structure. Your code decides what happens next.'))
S.append(camera_frame(
    'A frame is a numerical array: rows and columns locate pixels; three channel values describe colour. '
    'OpenCV normally gives this camera image in BGR order; MediaPipe expects an SRGB image, so the example converts to RGB. '
    'Point out that faster frame processing gives more frequent updates, but a model takes time to run.'))
S.append(objects(
    'A class describes a kind of object. red was one Ball instance, with its own position; update was its method. '
    'camera is an instance of VideoCapture and read is its method. tracker is a HandLandmarker instance; '
    'detect_for_video is its method. A method is a function accessed through an object; '
    'the object may hold state and resources. The real call also takes an image and a timestamp.'))


def vision_code(heading, lines, caption, notes):
    slide = code_panel('PYTHON / PFAD WEEK 8', heading, lines, caption=caption, notes=notes)
    for element in slide.els:
        if getattr(element, 'name', '') == 'code':
            for paragraph in element.paras:
                for run in paragraph.runs:
                    run.size = 40
    caption_box = slide.els[-1]
    caption_box.h = 80
    for paragraph in caption_box.paras:
        for run in paragraph.runs:
            run.size = 40
            run.color = INK
    return slide


S.append(vision_code('Read a frame from the camera', [
    'camera = cv2.VideoCapture(camera_index)',
    'ok, frame = camera.read()',
    'if not ok:',
    '    raise RuntimeError("Camera frame unavailable")',
    'frame = cv2.flip(frame, 1)',
    'rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)',
], 'One method call returns a success flag and an image array.',
    'Excerpt adapted from hand_tiles.py: the real program checks isOpened and reads inside a while loop. '
    'camera_index chooses the device. read() returns two values: ok is a Boolean and frame is an image array. '
    'If reading fails, do not process an empty frame. flip mirrors the image horizontally. '
    'The real code passes cvtColor directly to mp.Image rather than assigning rgb.'))
S.append(vision_code('Configure the tracker', [
    'base = mp.tasks.BaseOptions(model_asset_path=str(model_path))',
    'options = mp.tasks.vision.HandLandmarkerOptions(',
    '    base_options=base,',
    '    running_mode=mp.tasks.vision.RunningMode.VIDEO,',
    '    num_hands=1,',
    ')',
], 'Options describe the task; the .task file contains the trained model.',
    'This is the options excerpt from hand_tiles.py, after imports and model selection. '
    'MediaPipe is the runtime library; the model asset contains learned parameters used for prediction. '
    'Options are an object describing model path, video mode and maximum hands. '
    'The next slide creates the tracker from these options; it is reused across frames, not rebuilt each frame.'))
S.append(vision_code('Call a method for each frame', [
    'with HandLandmarker.create_from_options(options) as tracker:',
    '    # Repeat for each RGB frame and increasing timestamp',
    '    image = mp.Image(image_format=mp.ImageFormat.SRGB,',
    '                     data=rgb)',
    '    result = tracker.detect_for_video(image, timestamp_ms)',
], 'The method returns a result object; it does not choose a game action.',
    'Abbreviated from hand_tiles.py: HandLandmarker here stands for mp.tasks.vision.HandLandmarker; '
    'rgb is the converted frame shown on the prior slide. The actual method call is inside a while loop. '
    'VIDEO mode requires each frame timestamp in milliseconds; the example uses a monotonic clock and '
    'ensures strictly increasing integers. create_from_options is a class method that creates tracker; '
    'detect_for_video is called on that instance. with closes the tracker when the block exits.'))
S.append(content('LIVE / FACE + HAND', 'Look at what the model returns.', [
    'Face detector: a box around each detected face.', 'Hand Landmarker: 21 points per hand, including index fingertip 8.',
    'Move closer, rotate your hand, hide it: when does tracking fail?',
    '[Modern source and run commands](https://github.com/sd5913/pfad/blob/f88e2d37a90160868b90f0d9ced810c1137622f8/week08/README.md)',
], body_size=42, notes='From the PFAD root, cd week08; run uv run python vision.py face; then hand. Press q to stop. Show vision.py and the model source. Camera demo requires graphical desktop and permission.'))
S.append(fingertip(
    'A result object contains hand_landmarks, a list of detected hands. Each hand is a list of 21 landmark objects; '
    'index 8 is the index fingertip. Its x and y are normalised to image width and height: '
    'x=0 is the left edge and x=1 the right edge; y increases downwards. These are predictions, '
    'and coordinates can fall outside the image. An empty hand list means no hand was found.'))
S.append(vision_code('What if no hand is found?', [
    'if result.hand_landmarks:',
    '    x = result.hand_landmarks[0][8].x',
    'else:',
    '    x = None',
    'selected = tile_for_x(x)',
], 'Check the list before indexing; None means no input.',
    'Equivalent expanded form of the conditional expression in hand_tiles.py. '
    'An empty list is false in Python; indexing its first element would fail. '
    'The point object has an x attribute. tile_for_x is our own function, '
    'not a MediaPipe method: it translates the result into application behaviour.'))
S.append(vision_code('Turn a position into a choice', [
    'def tile_for_x(x):',
    '    if x is None or not isinstance(x, (int, float)):',
    '        return None',
    '    if not math.isfinite(x) or not 0 <= x <= 1:',
    '        return None',
    '    return "blue" if x < 0.5 else "red"',
], 'Predict: 0.49 → ?     0.50 → ?     None → ?',
    'Actual tile_for_x function from hand_tiles.py; math is imported in that file. '
    'Ask students first: 0.49 returns blue, 0.50 returns red, and None returns None. '
    'The guards also reject nonnumeric, nonfinite and out-of-frame values. '
    'From the PFAD root, cd week08 and run uv run python hand_tiles.py for the synthetic no-camera examples. '
    'This is an authored threshold, not a gesture classification by the model.'))
S.append(tiles('https://github.com/sd5913/pfad/blob/f88e2d37a90160868b90f0d9ced810c1137622f8/week08/hand_tiles.py',
    'From the PFAD root, cd week08. Run no-camera sample first: uv run python hand_tiles.py. Then if preflighted: uv run python hand_tiles.py --camera --model models/hand.task. Add --camera-index 1 if using the second camera. Check exact command and model before lecture.'))
S.append(vision_code('Draw a point on the frame', [
    'height, width = frame.shape[:2]',
    'for point in points:',
    '    pixel = (int(point.x * width),',
    '             int(point.y * height))',
    '    cv2.circle(frame, pixel, 2, colour, -1)',
], 'Normalised coordinates × image size → pixel coordinates.',
    'Adapted from draw_points in vision.py: the original passes the calculated tuple directly to cv2.circle. '
    'shape gives image dimensions in height, width order; drawing uses x, y order. '
    'For a 640 by 480 frame, (0.5, 0.5) maps to (320, 240). '
    'A coordinate at exactly 1 maps to width or height, just beyond the last pixel; '
    'a real interaction may clamp or reject points outside the image.'))
S.append(content('LIVE / GESTURE + POSE', 'Compare two kinds of output.', [
    'Gesture Recognizer: a trained model returns a gesture label and score.',
    'Pose Landmarker: body points can drive an interaction.',
    'A score is model confidence, not proof of intent.',
    '[Examples and source](https://github.com/sd5913/pfad/blob/f88e2d37a90160868b90f0d9ced810c1137622f8/week08/vision.py)',
], body_size=42, notes='Run gesture; choose pose or segmentation as the second demo according to time. This modern trained recognizer differs from the 2025 handwritten landmark rules. Discuss what happens when the hand or body leaves view.'))
S.append(content('LIVE / SEGMENTATION', 'A mask changes the background.', [
    'The model estimates a person mask for each frame.', 'OpenCV combines foreground with a replacement background.',
    'Try hair, a raised hand and a busy background.', '[All Week 8 vision exercises](https://github.com/sd5913/pfad/tree/f88e2d37a90160868b90f0d9ced810c1137622f8/week08)',
], body_size=42, notes='If choosing segmentation, from week08 run uv run python vision.py segment. Otherwise explain the mask briefly and leave the live example for the tutorial. Segmentation estimates pixels, distinct from landmarks. No camera data needs uploading or saving.'))
S.append(tutorial(
    f'{PFAD}/README.md',
    'https://stackblitz.com/github/google-ai-edge/mediapipe-samples-web?file=src%2Ftasks%2Fhand-landmarker.ts',
    'The tutorial is led by the TA using the README, independent of instructor ClassPoint login. '
    'For each example: run it, observe, change one thing and discuss a limitation. '
    'The project prompt is inspiration only: no team is required to use computer vision. '
    'The linked browser demo is Google’s JavaScript example; the README also links native Android and iOS samples. '
    'Optional team cloud setup follows the camera work where time allows.'))
S.append(end('Build together.\nShow your work.', 'One idea. One shared repository. A working next step.', EYE,
    notes='Remind teams to submit the shared repository URL and continue developing until 6 December 23:59 HKT.'))
for slide in S:
    if slide.cp:
        slide.els[0].name = 'question-eyebrow'
attach_reports(S, Path(__file__).resolve().parent / 'week08-reports.json')
DECK = dict(title='SD5913 / Programming / Week 08', slides=finalize(S, EYE), pdf='SD5913-week08.pdf')
