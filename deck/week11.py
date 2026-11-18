"""19 November 2026: agents, Blender PRs and authenticated D1 applications."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import week11_figures as F
from deckgen import CODE, Image, T
from deckgen.layouts import (title, agenda, section, statement, content,
                             code_panel, figure_slide, end)

E = 'SD5913 / WEEK 11 / 19 NOVEMBER 2026'
# Coordinator refreshes this only after the companion is verified and committed.
PFAD = 'https://github.com/sd5913/pfad/tree/e02fd99bc51c5df2b46c89eb4491b9da591b843d/week11'
SOURCE = PFAD.replace('/tree/', '/blob/')
BLENDER = 'https://docs.blender.org/api/current/'
TEMPLATE = 'https://github.com/sd5913/github-oauth-d1-template'
OAUTH = 'https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps'
CF = 'https://developers.cloudflare.com/'
ASSETS = Path(__file__).resolve().parent / 'assets/week11'
S = []


def prose(heading, lines, notes, label='CREATIVE APPLICATIONS'):
    S.append(content(label, heading, lines, body_size=40, notes=notes))


def code(heading, lines, notes, label='TRACE THE CODE', lang='py'):
    S.append(code_panel(label, heading, lines, notes=notes, lang=lang))


def diagram(heading, figure, notes):
    S.append(figure_slide('FOLLOW THE STATE', heading, figure, notes=notes))


def photo(heading, filename, notes):
    slide = content('ACTUAL APPLICATION OUTPUT / 29 OCTOBER 2026', heading, [], notes=notes)
    # Use the standard title/chrome, replacing the diagram with the actual capture.
    slide.els = slide.els[:2] + [Image(120, 320, 1680, 640, str(ASSETS / filename), 'contain')]
    S.append(slide)


def compare(heading, left, right, labels, notes, date='29 OCTOBER 2026'):
    slide = content('ACTUAL APPLICATION OUTPUT / ' + date, heading, [], notes=notes)
    slide.els.extend([Image(120, 355, 790, 545, str(ASSETS / left), 'contain'),
                      Image(1010, 355, 790, 545, str(ASSETS / right), 'contain'),
                      T(120, 905, 790, 65, labels[0], 'semibold', 42, '#000B1C'),
                      T(1010, 905, 790, 65, labels[1], 'semibold', 42, '#000B1C')])
    S.append(slide)


S.append(title(E, 'Agents, tools\nand evidence.',
    'Two cases: Blender scenes and an authenticated web app.', size=130,
    notes='0-1 minutes. Thursday 19 November 2026. This lecture is 120 minutes including a 55-65 break; '
    'the separate PFAD tutorial is another 120 minutes. Students choose Blender or the authentication '
    'template for tutorial practice. Explain an agent goal/action/observation/stop, inspect a Blender '
    'change through a reviewed PR, trace OAuth identity into owner-scoped D1 rows and distinguish '
    'CI evidence from a working deployment. Godot moves to Week 12 preparation, preserving its '
    'existing runnable files. No live autonomous episode is claimed today. Companion: ' + PFAD))
# Four dated news items fit within the existing ten-minute opening.
prose('GPT-6.2 Astra and Sol', [
    '17 November / OpenAI releases new coding and work models.',
    'OpenAI reports better outputs, but also omitted blockers in two tests.',
    'What should an agent say when the scene file is missing?',
], '1-2 minutes. Available in ChatGPT Work/Codex for Plus, Pro, Enterprise and Edu, and API. '
   'OpenAI reports a Codex instruction mitigation for obstacle omissions. These are vendor '
   'observations, not an independent classroom comparison. Ask for an honest stop and evidence '
   'before changing the scene. No new model run or account is required. Source, checked '
   '18 November 2026: https://openai.com/index/introducing-gpt-6-2-astra-sol/',
   label='AI NEWS / 17 NOVEMBER 2026 / OPENAI')
prose('Gemini 4 Hydrogen', [
    '12 November / Google releases a model for fast agent execution.',
    'An orchestrator can switch between Carbon and Hydrogen.',
    'What must an editing agent hand to a separate verifier?',
], '2-3 minutes. Google article updated 16 November, checked 18 November 2026. '
   'Available across Gemini, AI Studio and API tiers; Antigravity requires Pro or Ultra. '
   'Google reports near-Carbon task success with 24% less quota and 19% faster completion '
   'on Terminal-Bench 4.0. This vendor benchmark does not establish our camera task quality. '
   'Keep the same brief and acceptance criterion; inspect the diff and current render. Source: '
   'https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/',
   label='AI NEWS / 12 NOVEMBER 2026 / GOOGLE')
prose('Qwen4-Max', [
    '16 November / Alibaba releases vision and tool use with long context.',
    'Available through QwenCloud, QwenWork and QwenStudio.',
    'Which intermediate result would you review before the next action?',
], '3-4 minutes. Alibaba announces a one-million-token context window. Long context and '
   'vendor demonstrations do not guarantee a correct long-running task. Ask for a small diff, '
   'a current render and a clear stop condition. Smaller open-weight Qwen4 models are promised; '
   'this announcement does not establish Max as open source. Checked 18 November 2026. Source: '
   'https://www.alibabacloud.com/en/press-room/alibaba-unveils-qwen4-max?_p_lc=1',
   label='AI NEWS / 16 NOVEMBER 2026 / ALIBABA')
prose('Seedream 5.5 and Layers', [
    '12 November / Runway Dev adds image generation and layer extraction.',
    'Layers returns a base image and transparent PNG layers.',
    'After moving one object, which edges and hidden areas need checking?',
], '4-5 minutes. Runway documents source-image decomposition into raster layers, not native '
   'vector objects. Compare a selective edit with whole-image regeneration in discussion; '
   'do not add another live practical. maxImages caps returned images (2-100, default 30); '
   'billing is per returned image after a credit reservation. Use an instructor-owned synthetic '
   'image only if preparing an optional later example; no upload or paid call is needed today. '
   'Checked 18 November 2026. Source: https://docs.dev.runwayml.com/api-details/api_changelog/',
   label='AI NEWS / 12 NOVEMBER 2026 / RUNWAY DEV')
S.append(agenda(E, ['0-10 / news, agent goals, tools and evidence',
    '10-35 / Blender: inspect, change and render', '35-55 / branch, PR, review and revision',
    '55-65 / break', '65-90 / GitHub OAuth: redirects, state and session',
    '90-110 / private D1 notes and deployment', '110-120 / tutorial handoff and questions'],
    notes='5-6 minutes. Keep terminal/UI work and discussion inside each block. The same evidence loop connects '
    'both cases: a small brief, allowed changes, a result, review and a stopping condition. The '
    'tutorial completes one route, with its own 55-65 break and 100-120 project/tutor support. '
    'Do not add a third Godot practical or remove the W10 handbook retrieval/memory progression.'))
S.append(statement('Which result would\nyou accept?', size=112,
    notes='6-7 minutes. Ask for one concrete creative task: two useful camera views, or a private '
    'project note that survives restart. Have students name the observation that would convince '
    'them. A model saying done is a claim; a diff, current render, failed ownership attempt or '
    'fresh-process reload supplies evidence. Hear two answers; no new submission is required.'))
diagram('An agent chooses the next action.', F.agent(),
    '7-8 minutes. An agent pursues a goal by choosing actions using observations, subject to limits '
    'and a stopping condition. For our Blender example: preserve sculpture/material/light; change '
    'only the camera pair; inspect the diff and actual renders; revise if the second view needs '
    'more of the front face; stop after the accepted comparison or ask a human when the tool fails. Tool execution '
    'and action selection are different responsibilities. Next week examines an actual recorded '
    'model/check/revise/stop episode in Godot; today we use a human-directed worked example.')
prose('A script and an agent can use the same tool.', [
    'A script can run a fixed list of camera poses.',
    'An agent can choose a new pose after seeing a result.',
    'Both still need checks and a human acceptance decision.',
], '8-9 minutes. A loop over two coordinates is deterministic automation, not proof of agentic '
   'decision-making. Our supplied Blender client executes a fixed reviewed sequence; call it '
   'that. In an agent-assisted coding task the model may propose edits, run tools and revise '
   'using observations, while the student owns the brief, review and merge. Do not fake a live '
   'autonomous run or attribute an instructor-selected coordinate to a model.')
prose('The handbook agent keeps its knowledge path.', [
    'Week 10: retrieve handbook sources and retain conversation history.',
    'Today: call a creative tool or build a signed-in application.',
    'A source, a tool result and a session have different jobs.',
], '9-10 minutes. Preserve the same handbook embedding index/retriever, isolated persisted '
   'conversation rows, assembled prompt and spoken reply from Week 10. They are not replaced '
   'by Blender or a login page. An authenticated identity could later choose a conversation '
   'owner; it does not turn a cookie into knowledge or make a retrieved answer correct. Week '
   '10 local User rows used fictional names and were not authentication. Orange/t-SNE/matrix '
   'projection was removed by explicit instructor decision, outside revision scope.')
S.append(section('10-35 / BLENDER', 'Work on the scene.',
    'Application data -> saved scene -> rendered image', bg='#000B1C',
    notes='Start Blender block at minute 10. Show a simple actual scene before any protocol diagram. '
    'The supplied script creates a disposable Blender process; it never loads personal work. '
    'Blender 5.2.3 LTS was tested on Linux. bpy is the Python API inside Blender, not a package '
    'students should install into the uv environment. Source: ' + SOURCE + '/blender_scene.py'))
photo('One sculpture, one camera, one light.', 'sculpture-one.png',
    'Actual CPU Cycles render from Blender 5.2.3, 640x480, eight samples, generated 29 October. '
    'Identify the cube, its floor, visible faces and shadow. Geometry and code are original course '
    'work; no asset or generation service was used. Predict the image if scale becomes 1.5 while '
    'camera, material and light remain fixed. Do not confuse this rendered image with a live viewport. '
    'Live command from week11: blender --background --factory-startup -noaudio --python-exit-code 1 '
    '--python blender_scene.py -- --scale 1')
compare('Predict first. Then compare the result.', 'sculpture-one.png', 'sculpture-large.png',
    ['Scale (1, 1, 1)', 'Scale (1.5, 1.5, 1.5)'],
    'Two actual Blender renders with the same camera/light. The helper moves the cube center to z=scale '
    'so its bottom stays on the floor. Thus both scale and center height change intentionally; it is '
    'not a pure one-property transformation. Length on each local axis increases 1.5 times. The '
    'projection and shadow also depend on camera/light. Ask students why "50% larger" needs a stated '
    'measure. Run the scale 1.5 command, open the new PNG and inspect the JSON rather than trusting '
    'the command text alone. Source: ' + SOURCE + '/blender_scene.py')
diagram('Where does this Python execute?', F.blender_boundary(),
    'Trace the exact boundary: uv runs our standard Python helper; subprocess starts the Blender '
    'executable; Blender runs blender_scene.py with its own embedded Python and bpy module. The scene '
    'objects belong to that process. After it exits, files remain. A normal uv Python import of bpy '
    'is not this route. CLI arguments after -- are read by our script rather than by Blender. '
    'Ask where a misspelled object name would fail and where an unavailable executable would fail.')
code('Find a named object before changing it.', [
    'target = bpy.data.objects.get(options.target)', 'if target is None:',
    '    raise ValueError("Missing object")', 'before = list(target.scale)',
    'target.scale = (1.5, 1.5, 1.5)', 'target.location.z = 1.5',
], 'Actual API excerpt from blender_scene.py; error text shortened for projection. bpy.data.objects '
   'is a collection of scene objects. .get(name) returns an object or None. Checking None before '
   'property access gives a useful recovery. list(target.scale) snapshots the old three numbers; '
   'the assignment changes the named object. Explain tuple values x,y,z and why z changes to preserve '
   'floor contact. Direct data access avoids relying on which object is selected in the interface. '
   'API source: ' + BLENDER + 'info_quickstart.html')
diagram('Three results, three places to check.', F.scene_outputs(),
    'The arrows show a workflow, not one atomic operation. Inspect target.scale for the current object; '
    'open the saved .blend for persisted scene data; view the PNG for the camera/render result. A render '
    'can be visually wrong even when a file exists. The .blend contains scene configuration and objects; '
    'the PNG does not preserve editable geometry. If a previous PNG remains after a failed run, its '
    'existence cannot prove the new run succeeded. Use process status and new inspection data too.')
code('Save scene data. Render a camera view.', [
    'scene = bpy.context.scene', 'scene.render.filepath = str(output / "sculpture.png")',
    'bpy.ops.wm.save_as_mainfile(', '    filepath=str(output / "sculpture.blend"))',
    'bpy.ops.render.render(write_still=True)',
], 'Excerpt with a simplified fixed image filename; runnable source uses a scale-named PNG. '
   'save_as_mainfile writes the current scene; render(write_still=True) writes an image using the '
   'active scene camera and render.filepath. Our source explicitly chooses CPU Cycles, eight samples '
   'and 640x480; this is a quick evidence render, not final artwork quality. Use --python-exit-code 1 '
   'so a Python exception produces a nonzero Blender status. Sources: ' + BLENDER + 'bpy.ops.wm.html '
   'and ' + BLENDER + 'bpy.ops.render.html')
compare('Change the observation: move the camera.', 'camera-one.png', 'camera-two.png',
    ['Camera (7, -9, 6)', 'Camera (9, -7, 6)'],
    'Actual paired renders generated 29 October. The sculpture scale stays 1.25 and both cameras look '
    'at the same target. Ask which face becomes more visible and which remains the same object. This '
    'retains the original 2025 multi-angle-dataset concept as a two-image controlled experiment. '
    'No generated mesh, large dataset or specialist GPU is required. Inspect camera coordinates in '
    'each output folder\'s inspect.json. Source: ' + SOURCE + '/blender_variants.py')
code('Position and direction are separate values.', [
    'bpy.ops.object.camera_add(location=(x, y, 6))', 'camera = bpy.context.object',
    'direction = Vector((0, 0, 1.1)) - camera.location',
    'camera.rotation_euler = direction.to_track_quat(', "    '-Z', 'Y').to_euler()",
], 'Equivalent excerpt of the actual camera code. A position says where the camera is; orientation '
   'says where it looks. Subtracting camera position from a target produces a direction. Blender '
   'cameras look along local negative Z, with Y as up; to_track_quat converts a direction into an '
   'orientation and to_euler supplies the camera rotation representation. Students need to explain '
   'the target/direction distinction, not memorize quaternion internals. A camera moved without '
   're-aiming may miss the sculpture. Source: Blender mathutils/current API.')
code('A short list becomes repeatable views.', [
    'poses = [(7, -9), (9, -7)]', 'for number, (x, y) in enumerate(poses, start=1):',
    '    folder = OUTPUT / "blender" / f"angle-{number}"',
    '    # Start Blender with x, y and this output folder.',
], 'Simplified control-flow excerpt from blender_variants.py, not a complete standalone script. '
   'Read its subprocess.run argument list in the editor. Enumerate adds a stable output number; '
   'tuple unpacking supplies coordinates; separate folders prevent the two image/scene results '
   'overwriting each other. A loop makes systematic changes, but never decides whether a view is '
   'good. Human review and a check of the recorded camera coordinates complete the experiment.')
code('A useful failure names the missing target.', [
    'blender --background --factory-startup -noaudio',
    '  --python-exit-code 1 --python blender_scene.py',
    '  -- --target MissingObject',
], 'Projection wraps one shell command across lines for legibility; copy the single-line command '
   'from the README. Around minutes 27-29, run it and read "Missing object: MissingObject; use '
   'Sculpture". Expect nonzero exit before saving/rendering. A previous image remains on disk, so '
   'do not present it as this failed run\'s result. Restore the target to Sculpture. Distinguish '
   'a missing object from a missing Blender executable or a renderer failure.', lang=None)
S.append(statement('The file exists.\nDid this run succeed?', size=112,
    notes='Minute 29 checkpoint. Give students 20 seconds to explain the stale-output trap. '
    'Look for a process status, current inspection and the new image. A green exit alone cannot '
    'judge composition; an old picture alone cannot establish a successful new process. Transition '
    'to MCP: wrapping an operation in a protocol does not remove these checks.'))
prose('API, CLI and MCP expose different boundaries.', [
    'API: bpy reads or changes scene objects.', 'CLI: our helper starts a Blender process.',
    'MCP: a client discovers and calls named tools.',
], '29-31 minutes. These interfaces can be layered. The bounded course adapter starts Blender CLI '
   'and returns saved inspection JSON. The community MCP for Blender has a stdio server plus a '
   'loopback socket add-on in live Blender. Both ultimately use bpy. Neither protocol decides '
   'whether the composition meets the brief. The bridges are community/course software, not '
   'official Blender Foundation MCP features. Source: ' + SOURCE + '/blender_tools.py')
diagram('Discover a schema before calling a tool.', F.discovery(),
    '31-32 minutes. Reuse the W9 message boundary: initialize, tools/list, tools/call, close. A '
    'tool name and input schema describe accepted arguments. The request ID correlates the '
    'response; isError true is a failure even inside a valid JSON-RPC response. Source: official '
    'MCP tools specification https://modelcontextprotocol.io/specification/2025-06-18/server/tools '
    'and the pinned course mcp_client.py. This fixed client is not a model choosing actions.')
code('A tool call carries explicit arguments.', [
    '{"method": "tools/call",', ' "params": {"name": "execute_blender_code",',
    '   "arguments": {"code":',
    '     "bpy.data.objects.get(\'Sculpture\').scale = (1.5, 1.5, 1.5)"}}}',
], '32-33 minutes. Request body without the outer jsonrpc/id fields. Actual demo code imports bpy '
   'and adjusts center z too. execute_blender_code can run arbitrary Python inside the disposable '
   'application, unlike the smaller scale-only course adapter. Read the schema and review the '
   'code before execution. The request is an input, not evidence of a changed scene. Source: '
   + SOURCE + '/blender_live.py', lang=None)
diagram('The live bridge still needs inspection.', F.live_mcp(),
    '33-35 minutes. Trace client -> stdio server -> loopback add-on -> bpy. The optional actual '
    'community bridge is mcp-for-blender 2.2.6, pinned source 8782963. From week11 run uv run python '
    'setup_blender.py, then uv run python blender_live.py. It opens a disposable Blender window, '
    'discovers tools, inspects, changes scale, reinspects and renders/saves. Press Enter to close. '
    'No model or paid asset service is called. Use uv run python blender_live.py --verify for '
    'automatic closure preflight. Expect scale [1.5,1.5,1.5], blender_exit 0 and socket_closed true. '
    'This optional longer demo belongs in tutorial/preflight; keep the lecture on schedule. '
    'A saved JSON file, a live object and the rendered camera image are separate observations.')
S.append(section('35-55 / AGENT WORK IN A PR', 'A change worth reviewing.',
    'Brief -> branch -> diff -> render -> review -> revision', bg='#000B1C',
    notes='35-36 minutes. A worked example using the actual supplied camera script and real Blender '
    'outputs. The brief/reviewer messages are an instructional example, not a claim that a public '
    'PR conversation or fresh autonomous episode took place. A student can use a configured '
    'coding agent, but remains responsible for the diff, evidence and human merge.'))
prose('Acceptance criterion: two useful views.', [
    'Keep sculpture scale 1.25, material, light and target fixed.',
    'Save each camera view in its own output folder.',
    'Show more front and less side in the second view; keep it uncropped.',
], '36-38 minutes. This is a specific brief for an agent-assisted camera study. Scope the edit to '
   'blender_variants.py; do not change blender_scene.py, the sculpture or the acceptance rule to '
   'manufacture success. Ask students which part can be tested numerically and which needs a '
   'person looking at the image. The model can propose a pose, but a human decides whether the '
   'views are useful. No credentials, personal scenes or ignored local files belong in a prompt.')
code('A focused branch keeps the evidence together.', [
    '# branch: agent/camera-study',
    '# Supplied first attempt: inspect and render it.',
    'poses = [(7, -9), (9, -7)]',
    'for number, (x, y) in enumerate(poses, start=1):',
    '    # Render into angle-1/ and angle-2/.',
], '38-40 minutes. Projected excerpt/branch name for the worked PR. The first attempt is already '
   'supplied. Ask the agent to inspect it, render it and write a small credential-free evidence '
   'note; that note is the first PR diff. Preserve the first pose and run uv run python '
   'blender_variants.py from week11. Open the actual source and its subprocess arguments. The '
   'PR description should give the criterion, source file, exact command, current inspect.json '
   'coordinates, before/after images and limitations. An agent commit is a proposal for review, '
   'not authority to merge. Runnable source: ' + SOURCE + '/blender_variants.py')
compare('The initial comparison is reviewable.', 'camera-one.png', 'camera-two.png',
    ['First view (7, -9, 6)', 'Proposed second (9, -7, 6)'],
    '40-42 minutes. Actual course renders from 29 October, same scale 1.25, material, light and '
    'look target. These supply the proposed comparison in the worked PR. Inspect image and '
    'coordinates together. The second view changes face visibility, but the reviewer can still '
    'ask to see more of the front face. A PNG alone does not establish which source produced it; retain '
    'the exact commit/command and inspection alongside your own evidence. No invented GitHub UI.')
diagram('Review changes the next action.', F.pull_request(),
    '42-44 minutes. 1 agent/camera-study initially contains the evidence note for the supplied '
    'views. 2 a human '
    'reviews against the fixed criterion and asks for a precise revision. 3 the author/agent '
    'commits the revision on the same branch, so the same PR keeps the discussion and updated '
    'checks. Review is not a new disconnected branch/PR. Human approval and merge come only '
    'after the updated diff, current images and checks have been inspected.')
prose('Reviewer request: show more of the front face.', [
    'Keep the first pose and the sculpture unchanged.',
    'Try second camera (5, -10, 6), aimed at the same target.',
    'Rerender both; attach the new comparison to this PR.',
], '44-46 minutes. Read this concrete worked reviewer request aloud. It gives a target change '
   'and things to preserve, rather than a vague improve it. The agent may explain a different '
   'pose, but must provide comparable evidence and keep scope. Ask students why changing the '
   'cube too would weaken the comparison. The coordinate is an instructor-selected revision '
   'example, not a claimed model choice or a student requirement to use this exact composition.')
compare('The revision has a visible result.', 'camera-two.png', 'camera-revision.png',
    ['Before: second (9, -7, 6)', 'Revised: second (5, -10, 6)'],
    '46-49 minutes. Left: actual 29 October course render. Right: actual 15 November CPU Blender '
    'render using the unchanged blender_scene.py, scale 1.25, camera x5/y-10, same target. The '
    'right-hand view shows a different face balance. Keep the original first view (7,-9,6) for '
    'the acceptance comparison; this slide isolates the revised second view. Run uv run python '
    'blender_variants.py after changing only the second pose. Actual image provenance is in '
    'deck/assets/week11/camera-revision-source.md. This is a worked PR example, not live agent proof.',
    date='29 OCT / 15 NOV 2026')
prose('Checks, review and merge answer different questions.', [
    'Diff: only the intended camera pair changed.',
    'Command and inspect.json: this source produced current outputs.',
    'Images: the views meet the visual criterion.',
    'Human: approve the revision, then merge the same PR.',
], '49-52 minutes. Look at the one-line diff and the new render timestamps/coordinates; rerun '
   'relevant tests if code changed beyond data. A passing check cannot judge composition. A '
   'human should request another revision or stop if the result is wrong. Record a failed '
   'MissingObject attempt and useful recovery if it occurred; do not erase the failure by '
   'showing an older PNG. The branch/check/PR approach transfers to auth changes after the break.')
S.append(statement('A green check.\nA useful result?', size=112,
    notes='52-55 minutes. Pairs name one result a CI test can establish and one result requiring '
    'human inspection for this PR. Then use the private-note case: tests can check forged cookies '
    'and owner filters, but a real sign-in needs actual GitHub/Cloudflare configuration. Keep '
    'the brief and limits visible while deciding whether to revise, merge or ask for help.'))
S.append(statement('Ten-minute break.\nBack at minute 65.', size=108,
    notes='Protect lecture minutes 55-65. Close any disposable Blender session and stop its loopback '
    'bridge. Prepare the template README and browser tabs after the break. Never project secret '
    'values or account settings containing credentials. The separate tutorial has its own break.'))
S.append(section('65-90 / AUTHENTICATED IDENTITY', 'Who is making the request?',
    'GitHub OAuth -> our session -> owner-scoped data', bg='#000B1C',
    notes='65-66 minutes. Introduce the second approved case: adapt the existing course registry '
    'architecture into a small private project-note app. The new template uses personal GitHub '
    'OAuth Apps for sign-in, Cloudflare Workers for server code and D1 for stored rows. It does '
    'not request repository access, use a PAT or create/install a GitHub App. Source: ' + TEMPLATE))
prose('A local User row was not a login.', [
    'Week 10 stored fictional local User IDs and relationships.',
    'A browser can type any name into an ordinary form.',
    'Today GitHub confirms identity; our server checks the session.',
], '66-68 minutes. Persistent identity within a database is not authentication. The W10 demo '
   'used selected local profiles to teach owner-scoped conversation/message queries; it did '
   'not prove who was at the keyboard. Authentication establishes the caller. Authorization '
   'then decides which note that caller may access. GitHub login names can change; the '
   'template uses GitHub numeric user ID as its stable owner identity. Do not invent passwords '
   'or add a password database to this lesson.')
prose('One private project note per signed-in user.', [
    'Sign in with GitHub; write a short project note.',
    'Save, reload and restart: the note remains.',
    'A second account sees only its own note.',
    '[Use the course template](' + TEMPLATE + ')',
], '68-70 minutes. These are the observable acceptance criteria. GET /api/note and POST /api/note '
   'require a valid session. POST accepts JSON body with one body string of at most 2000 '
   'characters; it never accepts an owner chosen by the browser. Use an invented project note, '
   'not student records. The template is a teaching adaptation of github-student-registry, '
   'with roster/assessment/admin features removed. Do not touch the production registry.')
diagram('The browser follows the authorization redirects.', F.oauth_redirect(),
    '70-73 minutes. 1 GET /api/auth/github generates unpredictable state and remembers it in '
    'a protected short-lived cookie. The template also uses PKCE: send a hashed challenge, '
    'retain the verifier and prove it during exchange. 2 the browser visits GitHub authorization with client_id, '
    'the configured redirect_uri and state. The person signs in/authorizes on github.com. '
    '3 GitHub redirects the browser to APP_URL/api/auth/github/callback with a temporary code '
    'and state. The callback must compare state before proceeding; mismatch or missing/expired '
    'state aborts. This binds the callback to the flow this browser began. Source: ' + OAUTH)
code('The callback belongs to this application.', [
    'APP_URL + "/api/auth/github/callback"',
    '',
    'GET /api/auth/github',
    'GET /api/auth/github/callback?code=...&state=...',
], '73-74 minutes. These are URL/route shapes, not runnable standalone JavaScript. APP_URL is '
   'the exact origin configured for this environment, including localhost port or deployed '
   'https origin. Use the same callback value in the personal OAuth App and template. Do '
   'not derive the destination from an arbitrary incoming Host header. The code is temporary '
   'and must not be pasted into an issue, prompt or screenshot. Source: template README and '
   + OAUTH, lang=None)
prose('A wrong state must stop the flow.', [
    'Missing or mismatched state: reject the callback.',
    'Wrong callback URL: fix configuration and begin sign-in again.',
    'Cancel authorization: show a useful failure, never a session.',
], '74-76 minutes. Ask what would happen if a callback from another browser were accepted. '
   'A fresh random state value is checked against the initiating browser before code exchange. '
   'A successful HTTP response or the presence of a code parameter is not proof of a valid '
   'flow. Tests can simulate wrong state and denied consent. Use a fresh sign-in after '
   'correcting callback configuration; never try to reuse a displayed temporary code. '
   'Source: ' + OAUTH)
diagram('The server exchanges the code and verifies identity.', F.oauth_session(),
    '76-79 minutes. The Worker sends code/client ID/client secret/configured redirect_uri to '
    'GitHub over HTTPS, then uses the returned access token to request the authenticated user '
    'profile. It validates the profile shape and numeric ID before issuing our signed session '
    'cookie. The token is not our session and is not stored in D1. The browser never receives '
    'the client secret. No private-repository scope is requested. The app needs identity, '
    'not permission to change a repository. Source: ' + OAUTH + ' and '
    'https://docs.github.com/en/rest/users/users#get-the-authenticated-user')
diagram('Later requests carry our session cookie.', F.session_request(),
    '79-81 minutes. Our signed session contains identity and expiry. HttpOnly prevents ordinary '
    'page JavaScript reading the cookie; SameSite controls cross-site sending; Secure is used '
    'in production HTTPS. The signature detects tampering but does not encrypt the payload, '
    'so store no token or private note in it. Every API request verifies signature and expiry. '
    'Logout clears the cookie. A valid cookie can remain after a server restart; the note '
    'survives in D1. Mutations also reject a mismatched Origin. Template source: ' + TEMPLATE)
prose('Create a personal GitHub OAuth App.', [
    'GitHub personal Settings > Developer settings > OAuth Apps.',
    'Set Homepage URL to this environment\'s APP_URL.',
    'Set callback to APP_URL + /api/auth/github/callback.',
    'Keep the client secret private; use no PAT or repo scope.',
], '81-83 minutes. Open the real GitHub UI/docs; no fictional screenshot is supplied. Use '
   'https://github.com/settings/applications/new . The student owns this OAuth App and their '
   'Cloudflare account. Separate local and deployed OAuth Apps make the two environments '
   'easy to reason about; do not claim GitHub supports only one callback. Copy values directly '
   'to ignored .dev.vars or repository secret fields, never into prompts/source. Local APP_URL is '
   'http://127.0.0.1:3000; callback adds /api/auth/github/callback. Source: '
   'https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app')
prose('Repository setup values: Cloudflare.', [
    'CLOUDFLARE_API_TOKEN / deployment permission',
    'CLOUDFLARE_ACCOUNT_ID / which account',
    'CLOUDFLARE_D1_DATABASE_ID / which D1 database',
    'CLOUDFLARE_WORKER_NAME / which Worker',
], '83-85 minutes. All eight template setup values are entered at repository Settings > '
   'Secrets and variables > Actions > Repository secrets. Some are public identifiers, '
   'but we use one consistent setup location in this classroom flow. The Cloudflare API '
   'token authorizes the deploy job for the student account; it is not a browser key or '
   'an app user session. Use the README\'s least-required Workers/D1 permissions. Never '
   'project any value. Source: https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/')
prose('Repository setup values: app and sign-in.', [
    'APP_URL / exact app origin',
    'OAUTH_CLIENT_ID / identifies the OAuth App',
    'OAUTH_CLIENT_SECRET / server-only OAuth credential',
    'SESSION_SECRET / signs our app\'s session cookies',
], '85-87 minutes. Add the remaining four values as repository secrets, matching names exactly. '
   'Client ID and APP_URL identify configuration; client secret and session secret must stay '
   'confidential. A random session secret is unrelated to the GitHub password/access token '
   'and Cloudflare deployment token. Local .dev.vars holds GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET '
   'and SESSION_SECRET. Optional .env holds public local configuration. Both filled files are ignored. '
   'Source: template README and https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions')
code('Actions names map to runtime names.', [
    'OAUTH_CLIENT_ID     -> GITHUB_CLIENT_ID',
    'OAUTH_CLIENT_SECRET -> GITHUB_CLIENT_SECRET',
    'SESSION_SECRET     -> SESSION_SECRET',
], '87 minutes. These are name mappings, not secret values or shell commands. GitHub reserves '
   'repository-secret names beginning GITHUB_, so use OAUTH_CLIENT_ID and OAUTH_CLIENT_SECRET '
   'in Actions. The Worker keeps the original registry runtime names. The mapping in deploy.yml '
   'writes the temporary secrets file without logging its contents. Source: template deploy.yml '
   'and https://docs.github.com/en/actions/reference/security/secrets#naming-your-secrets', lang=None)
diagram('Repository secrets need a deployment step.', F.credential_transfer(),
    '87-90 minutes. A repository secret exists in GitHub Actions; creating it does not magically '
    'create a Worker runtime binding. The deploy job writes the three OAuth/session runtime '
    'values to an unlogged temporary file: OAUTH_CLIENT_ID becomes GITHUB_CLIENT_ID; OAUTH_CLIENT_SECRET '
    'becomes GITHUB_CLIENT_SECRET. SESSION_SECRET keeps its name. wrangler deploy --secrets-file '
    'installs that file as runtime env bindings. APP_URL and the D1 binding are separate configuration. The Cloudflare '
    'API token stays with the deployment job. Never log or commit the temporary file. '
    'Current docs checked through Context7 15 November: ' + CF + 'workers/configuration/secrets/#upload-secrets-alongside-code')
S.append(section('90-110 / D1 AND DEPLOYMENT', 'Keep the note with its owner.',
    'Authenticated request -> server filter -> persistent row', bg='#000B1C',
    notes='90-91 minutes. Reuse W10 SQL/relationships instead of repeating a database taxonomy. '
    'D1 is the hosted SQL database bound to the Worker. The important new boundary is a '
    'server-verified session ID becoming the owner filter on every read and write.'))
diagram('The owner ID comes from the verified session.', F.ownership(),
    '91-94 minutes. Schematic example IDs 101/202 and invented note bodies, not actual accounts. '
    'The session carries the GitHub numeric identity; notes.github_id is that owner key. '
    'Authentication says the request is from 101. Authorization limits the query to 101. '
    'Never trust a user_id/owner_id hidden input, query parameter or JSON property supplied '
    'by the browser. The API route supports only the current session user\'s note. An ordinary '
    'SQL row or foreign key does not enforce this policy by itself.')
code('A parameter carries the current owner.', [
    'SELECT body FROM notes WHERE github_id = ?;',
    '',
    'INSERT INTO notes (github_id, body, updated_at)',
    'VALUES (?, ?, ?) ON CONFLICT(github_id)',
    'DO UPDATE SET body = excluded.body,',
    '              updated_at = excluded.updated_at;',
], '94-96 minutes. Projected SQL shape for one-note-per-owner storage. The server binds the '
   'verified session ID as github_id, never concatenates request text into SQL. body and the '
   'timestamp are other bound values. The unique/primary owner constraint makes an upsert replace that owner\'s '
   'existing note. Both GET and POST need session checks; checking only the UI button is '
   'insufficient. The template adds request/schema/origin checks around this query. Read '
   'the exact lib/handlers.ts source; this SQL panel is not a full API route. Source: ' + TEMPLATE + ' and '
   'https://developers.cloudflare.com/d1/worker-api/prepared-statements/', lang=None)
prose('Reload and restart test different lifetimes.', [
    'Save a note; reload the browser and read it again.',
    'Stop and restart the local server; read it again.',
    'D1 stores the row; server memory is not the database.',
], '96-98 minutes. Use the documented local D1 directory and migrate it before starting dev. '
   'Restart the same environment without deleting .wrangler state. A page reload alone '
   'may still be reading an in-memory server, so restart is additional evidence. Local and '
   'remote D1 are different databases; a successful local reload does not prove production '
   'migrations or binding. The browser session may expire or be cleared, requiring sign-in '
   'again; the owner\'s note should still exist after that. No real note/identity data in logs.')
diagram('PR checks and deployment have different authority.', F.deploy(),
    '98-101 minutes. PR checks run npm ci, tests, typecheck and build without deployment '
    'credentials or real OAuth. A human reviews/merges the PR. The main/manual deploy job '
    'uses repository secrets, applies remote D1 migrations and installs code/runtime secrets '
    'with Wrangler. A main-branch push is already a consequential action: review the changes '
    'before merging. Green CI is not evidence that APP_URL, callback, permissions or live '
    'GitHub sign-in work. Source: template .github/workflows and ' + CF + 'd1/reference/migrations/')
code('Use the template\'s checked commands.', [
    'npm ci', 'npm test', 'npm run typecheck', 'npm run build',
    'npm run db:migrate:local', 'npm run dev',
], '101-103 minutes. Run from a new repository created with Use this template; follow its README '
   'for ignored local config and personal OAuth App. npm ci uses the committed lockfile. '
   'Migrate local D1 before dev; open http://127.0.0.1:3000. npm run deploy is '
   'the documented deploy path after credential/config setup, while GitHub Actions supplies '
   'the classroom main/manual deployment. Inspect the workflow rather than guessing which '
   'secret reaches which process. All commands belong to the new template, not PFAD. '
   'Source: ' + TEMPLATE, lang=None)
prose('Diagnose the boundary that failed.', [
    'Callback mismatch: compare APP_URL and OAuth App callback.',
    'Missing runtime credential: inspect the deploy step, not the PR check.',
    'No such table: check migration and the selected D1 database.',
    'Another user\'s note: stop and inspect server owner filters.',
], '103-106 minutes. Read status/error category without printing credentials, cookies or OAuth '
   'codes. Wrong state/forged/expired session should be refused. A database binding error '
   'is different from an absent migration. A successful local migration does not migrate '
   'remote D1. For any data isolation failure, stop using real data, preserve a sanitized '
   'reproduction and fix the server check before further deployment. A model suggestion '
   'to disable state or remove the owner filter evades acceptance, just as editing a checker would.')
prose('Live acceptance needs two separate sessions.', [
    'Account A: sign in, save a harmless note, reload.',
    'Account B: use a separate browser profile and sign in.',
    'B sees its own note; A\'s note remains unchanged.',
    'Sign out: the note API refuses anonymous requests.',
], '106-108 minutes. Use two willing students\' own accounts/browser profiles, never ask for '
   'their passwords or print their records. B should see an empty/own note, and saving B\'s '
   'note must not change A\'s. Reopen A to verify. Front-end screenshots alone do not prove '
   'authorization: automated tests also exercise anonymous/forged/expired cookies and owner '
   'queries. Real GitHub/Cloudflare acceptance remains credential-dependent and must be '
   'reported separately from mock OAuth/unit tests. Do not claim a deployment was rehearsed '
   'when only build/tests ran.')
prose('A useful fallback keeps the boundary visible.', [
    'No deployment access: inspect routes and run local tests.',
    'Mock OAuth is labelled; it does not verify GitHub sign-in.',
    'Use a prepared partner for the real application step.',
], '108-110 minutes. Core tutorial is independent of the instructor login. The authentication '
   'route needs students\' personal GitHub OAuth App and Cloudflare account for a live deployment. '
   'If setup is unavailable, run the credential-free tests, trace state/session/owner paths '
   'and pair with a prepared machine; alternatively choose Blender. Do not force paid plans, '
   'API billing or a repository-access token to complete course practice. Record exactly '
   'which checks are local, mock or live.')
prose('Tutorial: choose one of the two cases.', [
    'Blender: brief, focused edit, renders, PR review and revision.',
    'Authentication: personal OAuth App, private D1 note and checks.',
    '55-65 / break; 100-120 / tutor and project support.',
    '[Complete separate two-hour tutorial](' + SOURCE + '/README.md)',
], '110-113 minutes. The README provides setup, timed tasks, expected observations, failure '
   'and recovery for one selected route. Agent assistance is optional if no configured '
   'account is available; human-directed edits still teach the same computing boundaries. '
   'A prepared partner handoff preserves hands-on work. Evidence is practice, not a new '
   'upload/grade. Authentication uses the separate template repository; Blender stays in PFAD.')
prose('Godot preparation remains for Week 12.', [
    'Keep the supplied world, checks and capture helpers.',
    'Week 12: bounded agent, failure, revision, check and film.',
    'First-time Godot setup and partner handoff are already budgeted.',
], '113-115 minutes. Godot practical work moves out of Week 11 by explicit instructor decision '
   '15 November; its files and existing Week 12 0-20 first-time setup/prepared-partner path '
   'remain. Do not modify the Week 12 lesson here. The full handbook retrieval/memory/spoken '
   'reply arc stays intact. Historical TouchDesigner/Python, OSC control messages and NDI '
   'audio/video transport remain optional archive extensions; Week 9 retains networking/vision. '
   'Archive: https://github.com/sd5913/pfad/tree/2025/week11')
prose('Use tutor time for the next useful increment.', [
    '19 November / show working evidence, feedback and a blocker.',
    'Project: 40% / idea 25%, code 50%, execution 25%.',
    'Due 6 December 2026 / 23:59 HKT / Canvas instructions.',
], '115-117 minutes. Shared public sd5913-owned group repository with teammate Write access '
   'remains required; personal ownership of the OAuth App does not change that. GitHub '
   'Projects is recommended; an equivalent accessible progress record is valid. Tutor support '
   'stays in the allocated tutorial slot. No new defence, grade, upload or requirement to '
   'add Blender/AI/authentication to the group project. Source brief: '
   'https://github.com/sd5913/pfad/blob/4358b4e47b874ef40c120e63b2f6329acbe9b7d5/assignments/group-project.md')
prose('Explain the evidence and its limit.', [
    'Why is a fixed tool script not itself an agent episode?',
    'Why do state, session signature and owner filter all matter?',
    'Why can green PR checks coexist with failed live sign-in?',
], '117-120 minutes. Core revision: goal/action/observation/stop; API/CLI/MCP boundaries; '
   'scene/file/render; focused PR review/revision; authentication versus authorization; '
   'OAuth browser redirects/server exchange/state; signed expiring cookie; server-derived '
   'ownership; persistent rows; CI versus deploy; credential locations. Current syntax is '
   'available in source/docs, not a memorization requirement. Optional archive tools and '
   'dated product news are outside quiz scope. Do not project private assessment answers.')
S.append(end('Make a small change.\nKeep the evidence.', 'Review, revise and let a human accept it.',
    'SD5913 / PFAD / WEEK 11',
    notes='Close at minute 120. The lecture teaches both cases; the separate tutorial chooses one '
    'and reserves 100-120 for project support. No new credentials, remote class or registry '
    'production action is used for authoring. Keep live OAuth/Cloudflare and classroom display '
    'rehearsal distinct from exported slides and offline tests. Sources: ' + PFAD + ' and ' + TEMPLATE))

DECK = {'title': 'SD5913 · Week 11 — Agents, tools and evidence',
        'pdf': 'SD5913-week11.pdf', 'slides': S}
