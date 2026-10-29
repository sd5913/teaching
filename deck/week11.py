"""19 November 2026: Python, application state, real creative-tool APIs and MCP."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import week11_figures as F
from deckgen import CODE, Image, T
from deckgen.layouts import (title, agenda, section, statement, content,
                             code_panel, figure_slide, end)

E = 'SD5913 / WEEK 11 / 19 NOVEMBER 2026'
# Coordinator refreshes this only after the companion is verified and committed.
PFAD = 'https://github.com/sd5913/pfad/tree/494316a2a6248e92448a2d57a4ebac5eada3b60a/week11'
SOURCE = PFAD.replace('/tree/', '/blob/')
BLENDER = 'https://docs.blender.org/api/current/'
GODOT = 'https://docs.godotengine.org/en/stable/'
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


def compare(heading, left, right, labels, notes):
    slide = content('ACTUAL APPLICATION OUTPUT / 29 OCTOBER 2026', heading, [], notes=notes)
    slide.els.extend([Image(120, 355, 790, 545, str(ASSETS / left), 'contain'),
                      Image(1010, 355, 790, 545, str(ASSETS / right), 'contain'),
                      T(120, 905, 790, 65, labels[0], 'semibold', 42, '#000B1C'),
                      T(1010, 905, 790, 65, labels[1], 'semibold', 42, '#000B1C')])
    S.append(slide)


S.append(title(E, 'Python controls\ncreative software.',
    'Inspect a scene. Change it. Check what actually happened.', size=130,
    notes='Thursday 19 November 2026. Complete 120-minute lecture, then a separate 120-minute PFAD tutorial. '
    'Both Blender and Godot appear in the lecture; students choose one application for the tutorial. '
    'Use the exact run sheet in lessons/week11-lesson-plan.md. The core examples use no model account, '
    'paid generation, downloaded artwork, camera or microphone. They show real application operations, '
    'not the earlier browser-opacity simulation. Source: ' + PFAD))
S.append(agenda(E, ['0-10 / opening, news and tool handoff',
    '10-35 / Blender: data, camera, save, render', '35-60 / real MCP: request to live scene',
    '60-70 / break', '70-95 / Godot: Python, files and behavior',
    '95-110 / failure, recovery and visible evidence', '110-120 / questions and tutorial handoff'],
    notes='Protect the full break and the two live-application blocks. Budget terminal/window switching, '
    'predictions and questions inside these times. The tutorial is another 120 minutes; do not collapse '
    'its tasks into the lecture. Outcomes: trace an API/tool request, distinguish scene/file/image, '
    'predict one parameter change and diagnose a failed application check.'))
S.append(statement('Which creative task\nwould you automate?', size=110,
    notes='0-3 minutes. Ask for a concrete operation: repositioning a camera, rendering variants, '
    'adding a label, checking that an exit opens. Take two examples. Identify an input, a target and '
    'a visible result. Reuse existing knowledge of objects and messages; do not reteach basic classes. '
    'A good answer names what a human would inspect afterwards. This is an informal discussion.'))
prose('News: a stable engine still needs checking.', [
    '[Godot 4.7.2 stable / 18 August 2026](https://github.com/godotengine/godot/releases/tag/4.7.2-stable)',
    'Our 29 October check uses Godot 4.7.2.',
    'What would you rerun after an engine update?',
], '3-6 minutes. Verified the release tag and GitHub published_at 2026-08-18T16:12:28Z on 29 October. '
   'This is a dated maintenance-release news item, not a claim about unverified new features. '
   'Connect the release to creative practice: a project and its automation bridge have separate '
   'compatibility boundaries. Inspect a saved scene, run its behavior check and verify graphics after '
   'updating. Refresh this brief story near class. Dated product news is outside quiz scope.', label='DATED NEWS / OUTSIDE QUIZ SCOPE')
prose('A tool can retrieve knowledge or change a scene.', [
    'Week 10: a handbook query returns sources.', 'Today: a scene action changes application state.',
    'Both need named inputs and a result we can inspect.',
], '6-10 minutes. Brief handoff from the same Week 10 handbook retriever and conversation-aware talking '
   'agent. Its handbook embedding index, saved conversation history, per-call prompt and spoken output '
   'remain distinct. We keep that knowledge path; we are not exporting it into Orange. Orange, t-SNE '
   'and required matrix/projection visualization were removed by the instructor. This week adds external '
   'application operations. The client used today is human-directed; the agent choosing next actions '
   'belongs to Week 12. Ask: does a successful retrieval prove the answer, or a tool response prove the artwork?')
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
prose('A property assignment changes live data.', [
    'The object name chooses the target.', 'The three scale values affect its local axes.',
    'Saving and rendering are separate operations.',
], 'Pause for prediction around minute 20. Ask what remains after setting scale if Blender exits '
   'before saving. The running scene held the edit, but the previous .blend on disk still contains '
   'its earlier state. Relate to Week 10 persistence without repeating ORM mechanics: data survives '
   'only when saved; Python method definitions are still code. bpy.ops invokes Blender operations '
   'that may depend on application context; named data access is usually easier to trace for properties.')
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
prose('Run the actual camera comparison.', [
    'cd week11', 'uv run python blender_variants.py',
    'Compare angle-1 and angle-2 in .output/blender.',
    '[Inspect the runnable source](' + SOURCE + '/blender_variants.py)',
], 'Approximately minutes 27-31: run two quick CPU renders, open both PNGs and each inspect.json. '
   'If Blender is not found, fix PATH or use the prepared machine; uv cannot install the desktop '
   'application. A successful helper exit confirms subprocess completion, not visual composition. '
   'Ask for a deliberate alternate camera pair, such as (5,-10), then restore the supplied pair. '
   'Keep outputs ignored; students retain their own evidence locally.')
code('A useful failure names the missing target.', [
    'blender --background --factory-startup -noaudio',
    '  --python-exit-code 1 --python blender_scene.py',
    '  -- --target MissingObject',
], 'Projection wraps one shell command across lines for legibility; copy the single-line command '
   'from the README. Around minutes 31-34, run it and read "Missing object: MissingObject; use '
   'Sculpture". Expect nonzero exit before saving/rendering. A previous image remains on disk, so '
   'do not present it as this failed run\'s result. Restore the target to Sculpture. Distinguish '
   'a missing object from a missing Blender executable or a renderer failure.', lang=None)
S.append(statement('The file exists.\nDid this run succeed?', size=112,
    notes='Minute 34-35 checkpoint. Give students 20 seconds to explain the stale-output trap. '
    'Look for a process status, current inspection and the new image. A green exit alone cannot '
    'judge composition; an old picture alone cannot establish a successful new process. Transition '
    'to MCP: wrapping an operation in a protocol does not remove these checks.'))
S.append(section('35-60 / MCP', 'Follow the request.',
    'Discovery -> call -> live scene -> checked result', bg='#000B1C',
    notes='Start second block at minute 35. No general permissions-card lesson: build directly on '
    'Week 9 process/messages and the Week 10 retriever tool. MCP supplies a shared interface for '
    'discovery and tool calls. The Blender/Godot bridges are community projects, not official '
    'application features. The supplied clients make a fixed human-directed sequence of calls.'))
prose('Three interfaces, different jobs.', [
    'API: Python reads or changes Blender data.', 'CLI: another process starts Blender with arguments.',
    'MCP: a client discovers and calls named tools.',
], 'Define API as the programming interface exposed by an application; CLI as its command-line '
   'interface; MCP as a protocol between client and server. They can be layered together. The '
   'bounded course adapter launches Blender CLI; the community MCP for Blender uses a live socket '
   'add-on which calls bpy. The protocol does not decide the next action and does not guarantee '
   'semantic correctness. Ask which layer knows that the object is called Sculpture.')
diagram('Ask what tools exist, then call one.', F.discovery(),
    'Actual MCP lifecycle: initialize, notifications/initialized, tools/list, tools/call, close. '
    'tools/list returns a tool name, description and JSON input schema; tools/call names a tool '
    'and arguments. A request ID correlates its response. Tool errors may arrive in a normal '
    'response with isError true; a JSON-RPC envelope alone is not success. The stdlib teaching '
    'client shows these messages directly. Source: official MCP Python SDK v1.30 client docs and '
    'our mcp_client.py. No model or network model API is used.')
code('A tool call carries explicit arguments.', [
    '{"method": "tools/call",', ' "params": {"name": "execute_blender_code",',
    '   "arguments": {"code":',
    '     "bpy.data.objects.get(\'Sculpture\').scale = (1.5, 1.5, 1.5)"}}}',
], 'JSON shape shown without the outer jsonrpc/id fields added by Session.send. Real demo code '
   'imports bpy and also adjusts center z to keep the cube on the floor. Read the tool schema '
   'before making a call. execute_blender_code accepts Python code for the live application, '
   'which is much broader than a bounded scale-only function. Today\'s reviewed script targets '
   'only the disposable supplied scene. Source: ' + SOURCE + '/blender_live.py', lang=None)
diagram('Where does the request become bpy?', F.live_mcp(),
    'The actual third-party mcp-for-blender 2.2.6 has a Python stdio MCP server and an add-on loaded '
    'inside the live Blender window. The server sends requests to a loopback TCP socket; the '
    'add-on runs the scene action in Blender. Our disposable session chooses a free port rather '
    'than assuming default 9876 is available. Our Python client and the server are separate '
    'processes. Identify which hop fails if the add-on is stopped but the stdio server remains.')
prose('Watch the real application change.', [
    'uv run python setup_blender.py', 'uv run python blender_live.py',
    'Inspect Sculpture. Press Enter to close the session.',
    '[Live bridge source](' + SOURCE + '/blender_live.py)',
], 'Approximately minutes 42-50. Setup downloads pinned MIT add-on source and installs the community '
   'package in .tools/blender-env; it changes no global Blender/client preferences. Actual Linux '
   'cold install measured 4.602s with empty uv cache on 29 October, excluding Blender installation. '
   'The helper creates a baseline, opens disposable GUI Blender, discovers tools, reads scene scale, '
   'sets 1.5, reinspects, renders/saves, then waits. Show the actual object and PNG. Press Enter '
   'to close stdio, stop/unregister add-on and quit Blender. No assets/generation tools or model '
   'calls are invoked; telemetry/update checks are disabled.')
code('Check the result and the cleanup.', [
    '"scale": [1.5, 1.5, 1.5],', '"blender_exit": 0,',
    '"socket_closed": true',
], 'Selected actual fields in .output/blender-live-result.json. Show both live reinspection in the '
   'trace and the actual image/scene output. The result is only accepted after the application exits '
   'and the loopback port stops listening. Automatic --verify uses the same real GUI/change/render '
   'path but closes without waiting for Enter. It is useful for a tutor preflight, not evidence that '
   'a student inspected the artwork. The live community server exposes more tools than the course '
   'adapter; do not call asset/generation services.', lang=None)
prose('The smaller adapter answers a narrower question.', [
    'uv run python mcp_client.py --blender list',
    'uv run python mcp_client.py --blender inspect_scene',
    'Course adapter: saved JSON. Community bridge: live scene.',
], 'Minutes 50-54. The course-owned Blender CLI adapter provides render_scene with a 0.5-2 scale '
   'range and inspect_scene for the latest saved inspection. It starts a fresh background Blender '
   'process per render, unlike the live community add-on. After a previous render, inspect_scene '
   'can succeed while a different open editor contains another state. Demonstrate a rejected scale '
   '5 using the exact README command; isError true should arrive before Blender starts. Name both '
   'implementations accurately. Source: ' + SOURCE + '/blender_tools.py')
diagram('A response is one layer of evidence.', F.evidence(),
    'Minutes 54-57. Protocol evidence: the expected request ID and no isError. Behavior evidence: '
    'the requested target/scale changed and later Godot conditions pass. Experience evidence: a '
    'human sees the correct image/window and the clip plays. None substitutes for the others. '
    'Ask which check would detect the wrong active camera, a misspelled object, an old PNG or a '
    'running process that never stops. Use these as ordinary debugging questions, not new assessment.')
S.append(statement('Who owns the value\nat each step?', size=112,
    notes='Minutes 57-60. Pair explanation for one minute, then hear one trace: JSON code string '
    'in client memory -> server -> add-on -> bpy object property -> saved scene/image. Distinguish '
    'the model from the client: today no model chooses an action. A Week 12 agent can use tool '
    'results to choose another bounded action; the application still needs independent checks.'))
S.append(statement('Ten-minute break.\nBack at minute 70.', size=108,
    notes='Protect lecture minutes 60-70. Close the disposable Blender session first. Keep the '
    'prepared Godot project ready for after the break. This is the lecture break; the separate '
    'tutorial keeps its own 55-65 break.'))
S.append(section('70-95 / GODOT', 'Make a tiny world.',
    'Python validates; Godot runs the game', bg='#000B1C',
    notes='Resume at minute 70. Godot 4.7.2 latest stable is the verified runtime. Use the standard '
    'editor rather than .NET; no export templates or purchased assets are needed. Today\'s scene '
    'uses GDScript inside Godot, with Python controlling configuration and process execution. '
    'Students who choose Blender today receive first-time Godot setup/orientation in Week 12 '
    'minutes 0-20, with a prepared partner-machine handoff at minute 20 if necessary.'))
photo('Three lights. One locked exit.', 'world-start.png',
    'Actual Godot 4.7.2 rendered frame from the supplied world. Arrow keys move the white player. '
    'The three yellow pickups must be collected before reaching the exit at the right. Ask what '
    'the visible interface tells a player before any movement. The frame is extracted from a '
    'deterministic replay, not a photograph of keyboard play and not an agent-generated level. '
    'Source: ' + SOURCE + '/godot/world.gd')
diagram('Python and Godot have different jobs.', F.godot_boundary(),
    'world.py validates bounded values and writes world.json. On startup, world.gd loads that '
    'file and implements the world. Python starts the separate Godot executable for play/check/film. '
    'GDScript is Godot\'s scripting language, not Python. Saved config is inspectable even with '
    'the engine stopped; it is not a live editor observation. A running window keeps its loaded '
    'config until restarted. This is the same process/state distinction students saw with Blender.')
code('Validate before writing the file.', [
    'low, high = BOUNDS[key]', 'if not low <= value <= high:',
    '    raise ValueError("value outside allowed range")', 'config = load_config(path)',
    'config[key] = value', 'Path(path).write_text(json.dumps(config, indent=2))',
], 'Actual update_config excerpt, error text shortened. Before these lines, the function rejects '
   'unknown keys and types other than int/float, including bool. speed accepts 60-480; pickup_radius '
   '8-48; exit_x 720-880. NaN/infinity fail the bounds condition. Values are rejected rather than '
   'silently clamped, so the old file remains intact. These are deliberate course design limits, '
   'not limits imposed by the Godot API. Inspect the exact implementation: ' + SOURCE + '/world.py')
code('Speed becomes distance each time step.', [
    'if automatic:',
    '    player = player.move_toward(', '        target, float(config.speed) * delta)',
], 'GDScript excerpt from advance(delta, automatic). speed is pixels per simulated second; delta '
   'is seconds for this step. At speed 300 and delta 1/60, the maximum movement is 5 pixels. '
   'move_toward approaches the current target without overshooting. The manual branch uses '
   'Input.get_vector and the same speed*delta relationship. Ask students to predict maximum step '
   'distance at speed 120: 2 pixels. The check\'s fixed timestep is simulated time, not a claim '
   'that this machine computes 60 updates in one real second.', lang=None)
diagram('One behavior function serves three routes.', F.behavior(),
    'advance() moves toward the next pickup during automatic replay/check, counts a pickup within '
    'pickup_radius and sets won only when all three have been collected and the player is near '
    'the exit. In manual play it reads arrow-key input instead. The engine check disables automatic '
    'physics and calls advance 180 times at 1/60. The film uses actual graphical frame rendering. '
    'A shared implementation reduces divergent test logic, but a deterministic check does not '
    'verify keyboard feel, graphic legibility or whether the game is enjoyable.')
prose('Inspect, check and play the same world.', [
    'uv run python world.py inspect', 'uv run python world.py check',
    'uv run python world.py play', '[World source](' + SOURCE + '/world.py)',
], 'Approximately minutes 78-85. Run from week11. inspect says file_state_only true and prints '
   'the exact absolute project/config path. check runs real Godot/GDScript and writes '
   '.output/check.json; default speed 300 yields three pickups, player_x 840 and a win at tick 152. '
   'play opens the actual window for arrow keys; close it to stop. Set GODOT_PATH if the standard '
   'executable is not on PATH. Rehearse projected keyboard play separately; the verified film '
   'establishes graphical rendering, not a completed classroom rehearsal.')
prose('A community bridge can create scene nodes.', [
    'uv run python setup_bridge.py', 'uv run python mcp_client.py demo',
    'Inspect godot/probe.tscn in the editor.',
    '[Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp)',
], 'Minutes 85-90. Actual third-party Coding-Solo source commit 1209744, version 0.1.1; not an '
   'official Godot feature. It uses stdio and separate Godot CLI/GDScript operations, not a generic '
   'live editor socket. The course explicitly adapts its declared SDK 0.6 to tested JS SDK 1.30.0 '
   'with Node 26 native TypeScript. Fresh public install passed in 3.606s with empty npm cache; '
   'this excludes editor/Node installation. demo discovers project info, creates probe.tscn, '
   'adds Marker and Caption nodes, runs the main world, reads debug output, stops and closes stdio. '
   'The added probe is separate from the playable main scene; inspect its saved node/property.')
code('A node call names its parent and property.', [
    '"name": "add_node",', '"arguments": {', '  "scenePath": "probe.tscn",',
    '  "parentNodePath": ".", "nodeType": "Label",',
    '  "nodeName": "Caption",', '  "properties": {"text": "THREE LIGHTS"}}',
], 'Selected fields from a real tools/call; projectPath must also contain the absolute supplied '
   'Godot project path. Read the full request in mcp_client.py. A scene file is a tree: . refers '
   'to its root. The server creates a Label child called Caption with the text property. '
   'Saving this node does not automatically display it in a different main scene. Inspect the '
   'actual .tscn and open probe.tscn in the editor. A MissingParent experiment should fail; read '
   'the error rather than assuming the new node exists.', lang=None)
prose('Which state did you inspect?', [
    'The config file can change while the window stays old.',
    'A saved probe scene can differ from the main scene.',
    'Restart the right scene, then observe it.',
], 'Minutes 90-95: ask two pairs to name a plausible stale-state failure. world.py inspect only '
   'reads files. The community server\'s project metadata is also not a complete live viewport '
   'observation. A run_project acknowledgement occurs before useful visual readiness; examine '
   'debug output and the actual rendered result. Stop the process before changing/resetting '
   'for the next demo. Contrast this with live Blender get_scene_info from the add-on.')
diagram('A running engine can fail the design check.', F.failure(),
    'Minutes 95-99: predict the slow-speed result first. Set speed 120 and run check. The actual '
    'engine still executes successfully, but fails the declared requirement to collect all three '
    'and win within 180 steps. It reaches x440 and collects two. Restore 300: three pickups and '
    'win by tick152 at x840. These values are recorded actual Godot 4.7.2 results. The failure '
    'shows why process completion and behavior acceptance are different.')
code('Read the failing fields before changing code.', [
    '"collected": 2,', '"player_x": 440.0,', '"ticks": 180,',
    '"won_by_180_frames": false,', '"passed": false',
], 'Selected fields from the actual speed120 failure. Ask what the result supports: movement '
   'occurred; two lights were collected; the time-budget condition failed. It does not imply a '
   'network error, a missing engine or a broken display. The automatic route was used rather '
   'than keyboard input. At 120 pixels/second, three simulated seconds allow 360 pixels from '
   'x80 to x440. Choose the next action from the evidence rather than editing several settings.', lang=None)
prose('Make one change and verify recovery.', [
    'uv run python world.py set speed 300', 'uv run python world.py check',
    'uv run python world.py set exit_x 2000',
    'The last request must fail without changing the file.',
], 'Minutes 99-103. Restore the passing baseline, then demonstrate validation before mutation. '
   'exit_x2000 is outside 720-880 and should raise a readable ValueError with nonzero exit. '
   'Compare the file before/after: exit stays860. A human chooses this recovery; it is not an '
   'autonomous model loop. In Week12 a bounded agent will observe/check/adapt/stop using the same '
   'kind of evidence, with explicit mutation/time limits and an actual playable capture.')
compare('The film shows collection and completion.', 'world-middle.png', 'world-complete.png',
    ['Three lights -> exit opens', 'Player reaches exit -> COMPLETE'],
    'Actual extracted frames from the 29 October Godot4.7.2 clip: four seconds, 960x540,120 frames. '
    'The start frame earlier showed all three pickups and a locked exit; these frames show the '
    'changed state and final outcome. Full MP4 decode passed. Xvfb with Mesa software rendering '
    'was the verified Linux graphical path, not a dummy headless renderer. A film establishes '
    'visible playback; it does not replace manual playtesting or show a model making decisions.')
prose('Capture is another operation to check.', [
    'uv run python world.py capture',
    '120 rendered frames / 30 fps / four seconds',
    'Play .output/world.mp4 and inspect the ending.',
], 'Minutes 103-107. Optional Week11 extension and Week12 preparation. Needs FFmpeg/ffprobe and '
   'working graphical rendering; no dedicated GPU required. world.py uses official --write-movie '
   'with an absolute AVI path, --fixed-fps30 and --quit-after120, then converts to H264/yuv420p. '
   'Graceful quit matters: Ctrl+C can leave AVI duration metadata incomplete. The three-second '
   'behavior check and four-second recording have different purposes. Verified Linux command '
   'can be prefixed xvfb-run -a for CI. Source: ' + GODOT + 'tutorials/animation/creating_movies.html')
prose('Creative connections carry different data.', [
    'MCP: named tools, arguments and returned results.',
    'OSC: addressed control messages between programs.',
    'NDI: networked audio/video transport.',
], 'Minutes 107-110. Preserve the archive\'s TouchDesigner/Python, OSC/MediaPipe and NDI examples '
   'as linked creative extensions; no extra installation today. Week9 handles the networking/vision '
   'message bridge and server-owned state. A numeric OSC send does not prove a receiver changed '
   'a property, just as MCP acknowledgement does not prove a scene is correct. NDI carries media '
   'rather than replacing a semantic tool API. Archive: https://github.com/sd5913/pfad/tree/2025/week11')
S.append(statement('What would count\nas proof for your project?', size=112,
    notes='Minutes 110-113. Ask about one real team idea: a camera variant, a scene-building action '
    'or a game interaction. Name a small accepted result, a useful failure and a recovery. '
    'Do not require every project to use Blender, Godot, AI or MCP. Existing code tests plus '
    'human feedback can support a small usable increment. Give one concrete example then questions.'))
prose('Tutorial: choose one real application.', [
    '0-55 / setup, inspect, change and trace a tool request',
    '55-65 / break', '65-100 / purposeful edit, failure and recovery',
    '100-120 / tutor playtest, feedback and project support',
    '[Complete two-hour tutorial](' + SOURCE + '/README.md)',
], 'Minutes113-116. Blender and Godot are alternatives today, not two required installations. '
   'Follow README with exact working directory, outputs and troubleshooting. If no baseline by '
   'minute15, join a prepared partner, take turns and retain your own change/check/result. '
   'Blender-only students get Godot first-time setup/orientation next week in minutes0-20; '
   'at20 use the prepared partner if necessary. Tutorial runs independently of instructor '
   'ClassPoint/login. Practice evidence is not a new upload or grade.')
prose('Use the tutor time for the next useful step.', [
    '19 November / show an increment, playtest and discuss feedback.',
    'Project: 40% / idea 25%, code 50%, execution 25%.',
    'Due 6 December 2026 / 23:59 HKT / Canvas instructions.',
], 'Minutes116-118. Preserve the reviewed group-project policy: shared public sd5913-owned team '
   'repository with teammate Write access. GitHub Projects recommended; an equivalent accessible '
   'progress record is valid. Tutor times sit inside the allocated tutorial slot. This is not '
   'a new defence, additional grade or requirement to add today\'s tools. Existing Canvas '
   'submission instructions remain authoritative. Source brief: '
   'https://github.com/sd5913/pfad/blob/4358b4e47b874ef40c120e63b2f6329acbe9b7d5/assignments/group-project.md')
prose('Explain the chain before adding an agent.', [
    'Which process owns the scene?', 'Which input chooses the target?',
    'What survives after the process stops?', 'What observation proves the requested result?',
], 'Minutes118-120. Invite a concise chain using one of the real routes. Core revision concepts: '
   'API/CLI/MCP boundaries, named data/property operations, scene/file/image distinction, '
   'validation before mutation, fixed-step behavior versus graphical evidence, and failure/recovery. '
   'Dated news and optional OSC/NDI/TouchDesigner installations are not quiz scope. Orange/tSNE/ '
   'matrix projection is removed by instructor decision. Do not display assessment answers or keys.')
S.append(end('Make the change.\nCheck the result.', 'Then explain why the evidence is enough.',
    'SD5913 / PFAD / WEEK 11',
    notes='Close at minute120. Sources and commands live in the pinned companion README and this '
    'deck\'s notes. Leave questions for tutorial support where appropriate. Next week adds a bounded '
    'agent choosing tool actions and stopping after verified results; today\'s fixed client sequence '
    'must not be relabeled as a live model loop. No remote class, paid generation or account access '
    'is necessary for the tutorial. Companion: ' + PFAD))

DECK = {'title': 'SD5913 · Week 11 — Python controls creative software',
        'pdf': 'SD5913-week11.pdf', 'slides': S}
