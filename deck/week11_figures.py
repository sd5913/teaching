"""Concrete process/state diagrams in the established SD5913 palette."""
from deckgen.figures import Canvas, INK, ORANGE, TEAL, MUTED

PAPER = '#FAF8F4'


def label(c, x, y, text, size=46, color=INK, anchor='start'):
    c.text(x, y, text, size=size, color=color, anchor=anchor, weight=700)


def node(c, x, number, heading, line1, line2, width=470):
    c.rect(x, 175, width, 290, fill=PAPER, stroke=TEAL, width=2)
    label(c, x + 30, 232, f'{number}. {heading}', 46)
    label(c, x + 30, 325, line1, 42)
    label(c, x + 30, 400, line2, 42)


def arrow(c, x1, x2, y=325):
    c.line(x1, y, x2, y, color=ORANGE, width=6)
    c.poly([(x2, y), (x2 - 20, y - 14), (x2 - 20, y + 14)], fill=ORANGE)


def sequence(name, nodes, conclusion):
    c = Canvas(1680, 640)
    for i, (heading, line1, line2) in enumerate(nodes):
        node(c, 20 + i * 580, i + 1, heading, line1, line2)
        if i < 2:
            arrow(c, 510 + i * 580, 570 + i * 580)
    label(c, 840, 580, conclusion, 46, anchor='middle')
    return c.finish('week11-' + name)


def scene_outputs():
    return sequence('scene-outputs', [('Scene', 'scale = 1.5', 'live memory'),
        ('Save', 'sculpture.blend', 'scene data'), ('Render', 'sculpture.png', 'camera image')],
        'Changing, saving and rendering have separate evidence')


def blender_boundary():
    return sequence('blender-boundary', [('uv Python', 'start process', 'CLI arguments'),
        ('Blender', 'bpy + scene', 'owns objects'), ('Files', '.blend + PNG', 'inspect result')],
        'bpy executes inside Blender, not the uv environment')


def live_mcp():
    return sequence('live-mcp', [('Our client', 'tools/call', 'stdio JSON'),
        ('MCP server', 'local socket', '127.0.0.1'), ('Blender', 'add-on -> bpy', 'live scene')],
        'A request crosses two boundaries before the scene changes')


def discovery():
    return sequence('discovery', [('Discover', 'tools/list', 'name + schema'),
        ('Call', 'tool + inputs', 'request ID'), ('Inspect', 'result + scene', 'isError?')],
        'A schema describes accepted input; check the application too')


def godot_boundary():
    return sequence('godot-boundary', [('Python', 'validate speed', 'write JSON'),
        ('Godot', 'read on start', 'GDScript runs'), ('Observe', 'check + window', 'same behavior')],
        'Editing a file does not update an already-running process')


def behavior():
    return sequence('behavior', [('Move', 'speed * delta', 'distance/step'),
        ('Collect', 'near a light?', 'count += 1'), ('Exit', 'all 3 + near?', 'won = true')],
        'advance() is reused by play, deterministic replay and check')


def evidence():
    return sequence('evidence', [('Protocol', 'response ID', 'no tool error'),
        ('Behavior', '3 pickups', 'won by 180'), ('Experience', 'window + film', 'visible result')],
        'Each check answers a different question')


def failure():
    c = Canvas(1680, 640)
    node(c, 60, 1, 'Speed 120', '2 lights / 180', 'x = 440', 690)
    node(c, 930, 2, 'Speed 300', '3 lights / 152', 'x = 840', 690)
    arrow(c, 785, 895)
    label(c, 840, 580, 'Read the failure, then choose a purposeful change', 44, anchor='middle')
    return c.finish('week11-failure')


def agent():
    return sequence('agent', [('Goal', 'two useful views', 'keep sculpture'),
        ('Action', 'edit camera pair', 'run Blender'),
        ('Observe', 'diff + PNGs', 'revise or stop')],
        'An agent chooses its next action from the observation')


def pull_request():
    return sequence('pull-request', [('Branch', 'camera-study', 'diff + renders'),
        ('Review', 'show more front', 'keep target'),
        ('Revise', 'same PR', 'rerun + compare')],
        'Checks and a human review precede the human merge')


def oauth_redirect():
    return sequence('oauth-redirect', [('Our app', 'make state', 'remember it'),
        ('GitHub', 'sign in + allow', 'code + state'),
        ('Callback', 'match state', 'reject mismatch')],
        'The client secret stays on the server')


def oauth_session():
    return sequence('oauth-session', [('Worker', 'code + secret', 'server request'),
        ('GitHub API', 'verified user', 'numeric ID'),
        ('Our session', 'signed cookie', 'ID + expiry')],
        'Use the GitHub token for identity; then discard it')


def session_request():
    return sequence('session-request', [('Browser', 'session cookie', 'GET /api/note'),
        ('Worker', 'signature valid?', 'not expired?'),
        ('D1 query', 'session user ID', 'owner filter')],
        'The verified session determines the owner')


def ownership():
    c = Canvas(1680, 640)
    for y, user_id, body in [(135, '101', 'camera plan'), (360, '202', 'sound plan')]:
        c.rect(40, y, 530, 165, fill=PAPER, stroke=TEAL, width=2)
        c.rect(880, y, 760, 165, fill=PAPER, stroke=TEAL, width=2)
        label(c, 70, y + 65, 'Session ID: ' + user_id, 46)
        label(c, 70, y + 125, 'verified by server', 42)
        arrow(c, 610, 830, y + 85)
        label(c, 910, y + 65, 'notes.github_id = ' + user_id, 46)
        label(c, 910, y + 125, 'body: ' + body, 42)
    label(c, 840, 610, 'Signed-in 101: WHERE github_id = 101', 46, anchor='middle')
    return c.finish('week11-ownership')


def deploy():
    return sequence('deploy', [('PR checks', 'tests + types', 'build artifact'),
        ('Main / manual', 'migrate D1', 'deploy + secrets'),
        ('Live Worker', 'DB binding', 'runtime secrets')],
        'A green check does not establish a working public sign-in')


def credential_transfer():
    return sequence('credential-transfer', [('Repo secrets', 'GitHub Actions', '8 setup values'),
        ('Deploy job', 'temporary file', '--secrets-file'),
        ('Worker', 'OAuth + session', 'runtime env')],
        'The deploy job installs Worker runtime secrets')
