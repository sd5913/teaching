"""Use an agent on a real Blender scene, then carry its mesh into Godot."""
from deckgen.layouts import section, statement, code_panel
import week09_layouts as L
import week11_figures as F
from week11_layouts import capture, comparison

BLENDER = 'https://docs.blender.org/api/current/'
GODOT = 'https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/index.html'
LAB_MCP = 'https://www.blender.org/lab/mcp-server/'
LAB_SOURCE = 'https://projects.blender.org/lab/blender_mcp'
CODEX_MCP = 'https://developers.openai.com/codex/extend/mcp'


def build(source):
    s = []

    def code(heading, lines, notes, lang='py'):
        s.append(code_panel('READ THE APPLICATION CODE', heading, lines, notes=notes, lang=lang))

    s.append(section('03 / BLENDER', 'Ask an agent\nto use a tool.',
        'A visual brief -> Python scene -> observed result',
        notes='65-66 minutes. Start with the actual sculpture, not a protocol diagram. We will ask an '
        'agent to change its proportions while preserving the camera, material and floor contact. '
        'Then the SAME saved object becomes an asset in Godot. The prepared images are real application '
        'outputs from an author rehearsal, not a transcript of a model choosing actions. Students use '
        'their own agent in the tutorial, with a labelled partner fallback. Source: ' + source))
    s.append(capture('A scene produces a view of an object.', 'blender-baseline.png',
        'Blender / Sculpture at scale 1.25 / actual CPU render, 18 November 2026',
        '66-68 minutes. Identify the terracotta cube, its floor, camera view and shadow. This is a '
        '640x480 Cycles render from Blender 5.3.0, eight samples. The scene is original course work, '
        'with no downloaded/generated asset. The saved .blend contains editable scene data; this PNG '
        'is one flattened observation. Ask what should remain fixed if the artist requests a wider '
        'and shallower sculpture. Source: ' + source + '/blender_scene.py'))
    s.append(L.diagram('Object, mesh and material describe different things.', F.scene_parts(),
        '68-70 minutes. An object has a name and transform and references mesh data. The mesh contains '
        'vertices/faces; a material controls its surface response. Multiple objects can share data. '
        'The scene also holds cameras, lights and the floor. Changing the object scale does not rewrite '
        'the original mesh vertices; applying/baking scale can. A material assignment does not change '
        'the silhouette. Source: ' + BLENDER + 'info_quickstart.html'))
    s.append(L.rows('A transform places the object in the scene.', [
        ('Location', 'Where is its origin? Three coordinates: x, y, z.'),
        ('Rotation', 'Which way do its local axes point?'),
        ('Scale', 'How much is each local axis stretched?')],
        notes='70-72 minutes. Blender uses Z-up. Use your hands to identify horizontal x/y and vertical z. '
        'Transforms are relative to a parent when one exists; this example has no parent and no rotation. '
        'An origin/pivot is the point about which transformations operate, not necessarily a corner of '
        'the visible geometry. Our cube begins with side 2 and origin at its centre.'))
    code('Predict size and floor contact.', [
        's = 1.25',
        'target.scale = (s, s, s)',
        'target.location.z = s',
        '# Base cube: side length 2; origin at centre.',
        '# Height = 2 * s = 2.5',
        '# Bottom = centre_z - height / 2 = 0',
    ], '72-74 minutes. Trace real assignments in blender_scene.py. At scale 1.25, dimensions are '
       '2.5 by 2.5 by 2.5. Raising the centre to1.25 keeps the bottom at0. If z scale changes without '
       'changing the centre, the cube may float or sink. This calculation assumes the original '
       'axis-aligned cube with no rotation/parent/modifiers. The first agent task preserves z scale; '
       'students can therefore predict floor contact before seeing a render. Source: ' + source + '/blender_scene.py')
    s.append(L.diagram('Python runs inside the Blender application.', F.blender_boundary(),
        '74-76 minutes. A standard Python helper can start Blender as a child process. Blender then '
        'executes our script in its embedded Python where bpy exists. The script can also be run in '
        'Blender\'s scripting workspace. Do not pip-install bpy into the course uv environment for this '
        'workflow. CLI arguments after -- belong to our script. A missing executable fails before '
        'any scene code; a missing object fails inside Blender.'))
    code('Find the named object before changing it.', [
        'target = bpy.data.objects.get(options.target)',
        'if target is None:',
        '    raise ValueError("Missing object")',
        'before = list(target.scale)',
        'target.scale = (s, s, s)',
        'target.location.z = s',
    ], '76-78 minutes. Real API excerpt, with error text and options.scale shortened. The object '
       'collection supports .get(name), which returns an object or None. Check the result before '
       'property access. list(target.scale) snapshots three numbers; it does not keep a reference '
       'to a changing vector. Direct named data access avoids depending on current selection. The '
       'agent should inspect the existing script before proposing a replacement. Source: ' + BLENDER + 'bpy.types.BlendData.html')
    s.append(L.compare('Camera position and aim are separate.',
        ('Position', '(7, -9, 6)', 'Where the camera is in the scene.'),
        ('Direction', 'Target - position', 'Which point the camera looks towards.'),
        notes='78-80 minutes. A camera moved sideways while retaining its old orientation may miss the '
        'object. Our script derives its orientation from Vector((0,0,1.1))-camera.location. Blender '
        'cameras look along local negative Z, with local Y as up. to_track_quat maps that direction '
        'to an orientation. Explain the geometry; quaternion internals are not memorization material. '
        'Hold the camera/light fixed when comparing proportions. The optional variants loop retains '
        'the 2025 multi-angle render idea without adding another practical.'))
    code('Save the editable scene, then render an image.', [
        'scene = bpy.context.scene',
        'scene.render.filepath = str(output / "sculpture.png")',
        'bpy.ops.wm.save_as_mainfile(',
        '    filepath=str(output / "sculpture.blend"))',
        'bpy.ops.render.render(write_still=True)',
    ], '80-82 minutes. Excerpt with a simplified image filename; runnable code uses scale in the name. '
       'Assignment changes in-memory state. save_as_mainfile persists editable data. render writes '
       'the camera view using the scene settings. These are separate operations and can fail at '
       'different times. A PNG does not contain editable geometry. The helper writes current '
       'inspection JSON after a successful render. Sources: ' + BLENDER + 'bpy.ops.wm.html and bpy.ops.render.html')
    code('Run Blender and read a useful failure.', [
        'blender --background --factory-startup -noaudio',
        '  --python-exit-code 1 --python blender_scene.py',
        '  -- --target MissingObject',
    ], '82-85 minutes. These lines visually wrap ONE shell command; use the single-line README command. '
       'Run from PFAD/week11. Expect nonzero status and Missing object: MissingObject; use Sculpture '
       'before a new save/render. --python-exit-code 1 makes Python errors visible to the caller. '
       'Restore the default target and render scale 1.25 into .output/blender/before. An old PNG '
       'may still exist after failure. Ask why its existence cannot prove this run succeeded.', lang=None)
    s.append(section('04 / AGENT-ASSISTED WORK', 'Give a visual goal.',
        'Inspect -> act -> observe -> revise or stop',
        notes='85-86 minutes. This is where the model enters. Codex can inspect the running Blender '
        'scene, choose an MCP tool, read its result and view the actual application before choosing '
        'its next action. The Python API explains how the change happens inside Blender. The '
        'deterministic scene script is not itself an agent. The human sets the goal and accepts '
        'the result. Keep the prepared script route for a failed connection or unavailable model.'))
    s.append(L.diagram('Codex can drive the open Blender scene.', F.live_mcp(),
        '86-87 minutes. Blender Lab provides two pieces: an add-on executing inside Blender and '
        'a separate blender-mcp process launched by Codex. Codex uses MCP over stdio; that process '
        'talks to the add-on at loopback TCP port9876. The add-on socket is not an HTTP MCP URL. '
        'The Lab guide uses Llama.cpp as one client example; we use Codex. Python remains the '
        'execution API, while the model chooses which action to request next. This is the Lab '
        'project, distinct from the older Ahuja community bridge. Sources, checked19 November2026: '
        + LAB_MCP + ' and ' + LAB_SOURCE))
    s.append(L.rows('The add-on and the Codex connection.', [
        ('Blender', 'Install MCP from lab.blender.org; start its bridge.'),
        ('Connection', 'Host 127.0.0.1 and port 9876 on both sides.'),
        ('Codex', 'Register the stdio server, reopen, inspect the scene.')],
        notes='87-88 minutes. Preconfigure before class. Blender Preferences > Get Extensions: add '
        'https://lab.blender.org/, install MCP, allow online access and expand its Add-ons '
        'preferences. Start MCP Bridge Server; expect Server is running. PFAD README supplies '
        'the pinned uvx-based codex mcp add command and equivalent config.toml. Codex launches '
        'blender-mcp --transport stdio; BLENDER_MCP_HOST/PORT must match the add-on. Use local '
        'Codex on the same machine, not a remote environment whose localhost is elsewhere. '
        'Reopen the client; /mcp in the CLI lists tools. Ask for a read-only get_objects_summary '
        'and compare its names with the Outliner before an edit. Keep another agent\'s scene '
        'untouched and use a disposable course file for the exercise. No Llama.cpp installation '
        'is needed. Sources: ' + CODEX_MCP + ' and ' + source + '/README.md#connect-blender-lab-mcp-to-codex-before-class'))
    s.append(L.rows('A prompt for direct control in Codex.', [
        ('Inspect', 'Read Sculpture and report its current dimensions.'),
        ('Change', 'Make it wider and shallower; keep it grounded.'),
        ('Check', 'Show the result, save a new copy, stop for review.')],
        notes='88-90 minutes. Open the saved disposable baseline in Blender first; do not reset '
        'a personal or shared scene. Give the complete live MCP prompt from PFAD README. Codex '
        'should inspect the named object, preserve mesh/material/camera/light and set scale '
        '(2,.9375,1.25), centre z1.25. It requests the available tools, reads before/after '
        'values and inspects a fresh screenshot or render before deciding to revise or stop. '
        'Save a NEW first/sculpture.blend using an absolute output path; Blender and Codex '
        'may have different working directories. Also make the matching source edit for '
        'reproduction. At class, show the actual tool calls and changing application. A typed '
        'success claim is insufficient. Source: ' + source + '/README.md#35-55-let-the-agent-use-blender'))
    code('The first change has a predictable result.', [
        's = options.scale',
        'target.scale = (1.6 * s, 0.75 * s, s)',
        'target.location.z = s',
        '# At s=1.25: scale = (2, 0.9375, 1.25)',
        '# Dimensions = (4, 1.875, 2.5)',
    ], '90-91 minutes. The same assignments can be applied through the live MCP Python tool or '
       'retained as a small source edit. The first width is 4, '
       'depth 1.875, height 2.5. The vertical centre/height are unchanged, so bottom remains0. Read '
       'the diff before executing it. The agent should discover/reuse existing scene/material/camera '
       'code rather than replace it. A calculation predicts state; the render judges the visual goal.')
    s.append(comparison('Observe the result before accepting it.', 'blender-baseline.png', 'blender-first.png',
        ['Before / dimensions 2.5, 2.5, 2.5', 'First / dimensions 4, 1.875, 2.5'],
        '91-92 minutes. Inspect the fresh live result before showing this prepared comparison. '
        'These are actual prepared Blender renders18 November 2026 using temporary copies of the '
        'same source. They are author rehearsal, not model session evidence. Camera/material/light '
        'are fixed. Ask what changed in silhouette and whether it stays grounded/uncropped. In the '
        'student exercise the agent must open its own fresh image; a text success report cannot '
        'judge composition. Keep the actual command/status/JSON with each observation.'))
    s.append(L.compare('A script repeats. An agent chooses.',
        ('Fixed automation', 'Run these\nknown steps.', 'A loop can render a supplied list of camera poses.'),
        ('Agent', 'Choose the next\naction from results.', 'Inspect an error/image, then revise or stop.'),
        notes='92-93 minutes. The same Python API and MCP tools can support either. Model-directed tool use is the distinction '
        'we want to observe. Ask students to retain a short real action/observation log, not invent '
        'an autonomous story around a fixed helper. With no model access, a partner can perform '
        'the same Python/render/review exercise and label the work human-directed.'))
    s.append(L.rows('The tools return different observations.', [
        ('Read state', 'get_objects_summary'),
        ('See the view', 'get_screenshot_of_window_as_image'),
        ('Change state', 'execute_blender_code runs bpy inside Blender')],
        notes='93-94 minutes. Actual tools exposed by the configured Blender Lab server. Prefer '
        'the dedicated inspection tools, including get_object_detail_summary. Use Python execution '
        'when a required edit has no more specific tool. It has broad application access, so keep '
        'the change scoped to the named object. A returned object/scale and a screenshot answer '
        'different questions. A screenshot shows the current view, which may differ from a camera '
        'render. Listing tools proves discovery; a successful read also proves the connection to '
        'Blender. A good changed/saved result needs further observations. Source: ' + LAB_SOURCE))
    code('A tool call carries explicit arguments.', [
        '{"jsonrpc":"2.0", "id":3, "method":"tools/call",',
        ' "params":{"name":"execute_blender_code",',
        ' "arguments":{"code":',
        ' "import bpy; result = {\\"count\\": len(bpy.data.objects)}"}}}',
    ], '94-96 minutes. Valid illustrative MCP request using the Blender Lab execute_blender_code '
       'schema. Assign a JSON-compatible dictionary to result to return data; printing alone is '
       'not the Lab tool\'s structured return convention. This read-only code counts objects to '
       'show the API boundary; normally prefer the dedicated object-inspection tool. Codex '
       'constructs calls from the tool schema, not from a user typing JSON. Request id correlates '
       'the response. Execution, saving a .blend and inspecting an image remain separate. Source: '
       + LAB_SOURCE + '/src/commit/dbbf836ad4b1025f14a2b3b504c43903f39e0b04/mcp/blmcp/tools/execute_blender_code.py', lang=None)
    s.append(L.rows('Review the result in the same PR.', [
        ('First PR', 'A focused diff plus the actual before/after result.'),
        ('Review', 'Reduce x to 1.3 * s. Keep everything else fixed.'),
        ('Revision', 'Rerender, compare, update the existing branch.')],
        notes='96-99 minutes. Human reviewer requests less width while preserving height/depth/camera. '
        'In the same Codex session, reinspect live Sculpture, set x scale to1.625 and preserve y/z, '
        'then inspect a new screenshot/render and save revised/sculpture.blend. Update the matching '
        'source and evidence note on the same branch. Run git diff --check, read the diff and '
        'attach current observations to the existing PR. Live scene memory, the saved file and '
        'source code can disagree; verify which one Godot will receive. Generated scenes/caches stay '
        'ignored. A person makes the merge decision; a practice PR can remain open. The teaching '
        'example is a rehearsed request, not a fabricated GitHub PR screenshot.'))
    s.append(comparison('One requested revision: less width.', 'blender-first.png', 'blender-revised.png',
        ['First / x = 1.6 * s', 'Revised / x = 1.3 * s'],
        '99-101 minutes. Actual CPU renders from the same fixed camera. Revised scale at s = 1.25 is '
        '[1.625,.9375,1.25], dimensions [3.25,1.875,2.5]. Ask why the comparison can support a width '
        'claim only because the other factors stayed fixed. Accept or request another focused '
        'revision. Stop after the criterion is met, retaining known limits.'))
    s.append(statement('Can we use this\neditable object\nin a game?', size=110,
        notes='101-103 minutes. The PNG can be a flat image, but cannot provide the original mesh for '
        'a 3D camera to orbit. The .blend is the source document. We need a portable asset containing '
        'geometry/materials that the engine can import. Carry the same revised Sculpture forward.'))
    s.append(section('05 / BLENDER TO GODOT', 'Carry the object\ninto a scene.',
        'Export the saved model. Import it. Instantiate it.',
        notes='103-104 minutes. This is a small continuation of the Blender task, not another game '
        'assignment. Week 12 retains its full bounded model/check/revise/film episode. The old Godot '
        'demo is Node2D; this mesh needs the separate supplied Node3D preview.'))
    s.append(L.diagram('The same object crosses an asset boundary.', F.asset_path(),
        '104-106 minutes. Load the saved revised .blend; select ONLY Sculpture. Export its mesh and '
        'terracotta material as binary glTF (.glb). Exclude Blender camera/light/floor because Godot '
        'provides its own scene. The .blend remains editable source, .glb is handoff, imported scene '
        'is the engine resource, and its instance is one occurrence in our running scene. Godot can '
        'also import .blend with Blender installed; explicit GLB makes the transfer inspectable and '
        'portable. Source: ' + GODOT))
    code('Export the saved scene, then open Godot.', [
        'uv run python asset_handoff.py export',
        '  .output/blender/revised/sculpture.blend',
        'uv run python asset_handoff.py check',
        'uv run python asset_handoff.py play',
    ], '106-108 minutes. First TWO projected lines are ONE export command. Run from PFAD/week11; '
       'README has the copyable single line. Export reads the saved source instead of rebuilding '
       'a cube. check performs actual engine import/instantiation and verifies mesh, material, '
       'dimensions and ground contact. play opens the rendered preview; close its window normally. '
       'Check source path/timestamp if a stale shape appears. Do not overwrite personal projects. '
       'Source: ' + source + '/asset_handoff.py', lang=None)
    code('An imported model becomes a scene instance.', [
        'extends Node3D',
        '',
        'func _ready():',
        '    var asset = load("res://sculpture.glb").instantiate()',
        '    asset.name = "Asset"',
        '    add_child(asset)',
    ], '108-110 minutes. Actual first lines from godot3d/preview.gd. Godot imports the GLB as '
       'a PackedScene resource. instantiate creates a node hierarchy; add_child attaches it to '
       'our Node3D so the scene can show it. It does not create a second Blender source mesh. '
       'The rest of the script adds floor, Camera3D, light and environment. A Node2D game uses '
       'a different spatial system; this small preview isolates the new 3D concept. Source: '
       + source + '/godot3d/preview.gd', lang=None)
    s.append(L.rows('Check axes, scale and pivot at the boundary.', [
        ('Axes', 'Blender Z-up becomes Godot Y-up.'),
        ('Dimensions', '(3.25, 1.875, 2.5) -> (3.25, 2.5, 1.875)'),
        ('Pivot', 'Bottom centre; instance at origin; bottom y = 0.')],
        notes='110-112 minutes. The exporter handles axis conversion; do not add a second 90-degree '
        'rotation. The helper shifts the origin to the bottom centre and bakes scale in export '
        'memory, leaving the saved .blend byte-identical. Godot instance retains identity transform. '
        'The check measures actual world-space bounds. If importing another object, inspect its '
        'units, hierarchy/parent transforms and material support rather than assuming this cube\'s '
        'conditions. No collider is generated by the supplied exporter.'))
    s.append(comparison('The same mesh and material, in two applications.', 'blender-revised.png', 'godot-revised.png',
        ['Blender / saved revised source', 'Godot / actual running renderer'],
        '112-114 minutes. Actual18 November 2026 captures. Blender 5.3.0 Cycles versus Godot 4.7.2 '
        'Compatibility renderer; camera/lighting/floor intentionally differ. The shared geometry '
        'and base material do not imply pixel-identical shading. Verify silhouette, proportions, '
        'grounding and material in the live preview, then inspect export.json/check.json. Actual '
        'baseline and revised checks prove source-to-engine dimensions, not just file presence. '
        'Source/provenance: deck/assets/week11/blender-godot-source.md.'))
    s.append(L.compare('A visible mesh is not a solid game object.',
        ('Render geometry', 'What the\ncamera sees.', 'Mesh, material, light and camera produce the image.'),
        ('Collision geometry', 'What physics\ncan hit.', 'Choose a body and collision shape for the gameplay.'),
        notes='114-115 minutes. Our small preview demonstrates imported appearance only. A player can '
        'pass through a mesh with no collision shape. For a static block, an appropriate StaticBody3D '
        'and box collision could be a later addition. Collision complexity and physics behavior '
        'depend on the game; do not assume any imported mesh is automatically playable. Transition '
        'to the selected tutorial route and reserve final questions.'))
    return s
