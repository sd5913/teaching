"""Use an agent on a real Blender scene, then carry its mesh into Godot."""
from deckgen.layouts import section, statement, code_panel
import week09_layouts as L
import week11_figures as F
from week11_layouts import capture, comparison

BLENDER = 'https://docs.blender.org/api/current/'
GODOT = 'https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/index.html'


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
        notes='85-86 minutes. This is where the model enters. It can read the script, make a focused '
        'edit, run the real application, read errors/JSON and open the image, then choose its next '
        'action from that observation. The deterministic scene script itself is not an agent. The '
        'human remains responsible for the brief, review and acceptance.'))
    s.append(L.rows('Ask the agent to use Blender.', [
        ('Goal', 'Make Sculpture wider and shallower.'),
        ('Keep fixed', 'Name, material, camera, light and floor contact.'),
        ('Finish with', 'A small diff, fresh render and explained dimensions.')],
        notes='86-88 minutes. Give the full bounded prompt in agent-pr-workflow.md. Allow the agent to '
        'inspect/edit blender_scene.py, run disposable Blender, read JSON and view PNGs. First x '
        'scale=1.6*s, y=.75*s, z=s. Render scale 1.25 into .output/blender/first and compare with before. '
        'If cropped/floating, diagnose and revise before stopping. No downloads, personal scene or '
        'merge is required. Ask students which files and observations they would include in a request. '
        'Source: ' + source + '/agent-pr-workflow.md#ask-an-agent-to-use-blender'))
    code('The first change has a predictable result.', [
        's = options.scale',
        'target.scale = (1.6 * s, 0.75 * s, s)',
        'target.location.z = s',
        '# At s=1.25: scale = (2, 0.9375, 1.25)',
        '# Dimensions = (4, 1.875, 2.5)',
    ], '88-90 minutes. A small proposed edit to the existing two assignment lines. The first width is 4, '
       'depth 1.875, height 2.5. The vertical centre/height are unchanged, so bottom remains0. Read '
       'the diff before executing it. The agent should discover/reuse existing scene/material/camera '
       'code rather than replace it. A calculation predicts state; the render judges the visual goal.')
    s.append(comparison('Observe the result before accepting it.', 'blender-baseline.png', 'blender-first.png',
        ['Before / dimensions 2.5, 2.5, 2.5', 'First / dimensions 4, 1.875, 2.5'],
        '90-92 minutes. Actual prepared Blender renders18 November 2026 using temporary copies of the '
        'same source. They are author rehearsal, not model session evidence. Camera/material/light '
        'are fixed. Ask what changed in silhouette and whether it stays grounded/uncropped. In the '
        'student exercise the agent must open its own fresh image; a text success report cannot '
        'judge composition. Keep the actual command/status/JSON with each observation.'))
    s.append(L.compare('A script repeats. An agent chooses.',
        ('Fixed automation', 'Run these\nknown steps.', 'A loop can render a supplied list of camera poses.'),
        ('Agent', 'Choose the next\naction from results.', 'Inspect an error/image, then revise or stop.'),
        notes='92-94 minutes. Same API/CLI can support either. Model-directed tool use is the distinction '
        'we want to observe. Ask students to retain a short real action/observation log, not invent '
        'an autonomous story around a fixed helper. With no model access, a partner can perform '
        'the same Python/render/review exercise and label the work human-directed.'))
    s.append(L.rows('Tools expose actions the agent can request.', [
        ('Blender API', 'bpy reads and changes application data.'),
        ('Command line', 'Start Blender with a script and arguments.'),
        ('MCP tool', 'Discover a named operation and send structured arguments.')],
        notes='94-96 minutes. MCP is an optional interface, not a prerequisite for an agent using '
        'Blender. Our bounded CLI adapter launches disposable Blender; the community bridge uses '
        'a server/add-on and live loopback socket. Both ultimately execute Blender Python. A tool '
        'description/schema says what may be called, not whether the art is good. Existing community '
        'bridge is pinned and tested; do not install a random replacement during the lecture.'))
    code('A tool call carries explicit arguments.', [
        '{"jsonrpc":"2.0", "id":3, "method":"tools/call",',
        ' "params":{"name":"execute_blender_code",',
        ' "arguments":{"code":',
        ' "import bpy; print(bpy.data.objects.get(\\"Sculpture\\"))"}}}',
    ], '96-97 minutes. Syntactically valid illustrative MCP JSON request to the community server. '
       'The code string is valid embedded Python and prints the named object. Our real client '
       'builds requests through the SDK rather than hand-typing JSON. Request id correlates a '
       'response; a successful response is not proof of a saved scene/render. Do not confuse '
       'this community tool name with the course adapter\'s render_scene/inspect_scene. Source: '
       + source + '/blender_live.py', lang=None)
    s.append(L.rows('Review the result in the same PR.', [
        ('First PR', 'A focused diff plus the actual before/after result.'),
        ('Review', 'Reduce x to 1.3 * s. Keep everything else fixed.'),
        ('Revision', 'Rerender, compare, update the existing branch.')],
        notes='97-99 minutes. Human reviewer requests less width while preserving height/depth/camera. '
        'Give that request back to the agent on the same branch. Run git diff --check, read the '
        'diff and attach current observations to the existing PR. Generated scenes/caches stay '
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
