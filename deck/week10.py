"""Week 10: a class, two separate objects, and the records they can leave behind."""

from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from deckgen import Figure, INK, MUTED, Slide, T, WHITE, attach_reports
from deckgen.layouts import agenda, code_panel, content, end, section, statement, title, two_col
import week10_figures as F

S = []
EYE = 'SD5913 · WEEK 10'


def diagram(eyebrow, heading, figure, notes):
    svg, png = figure
    slide = Slide(bg=WHITE, notes=notes, title=heading)
    slide.chrome = False
    slide.els = [
        T(80, 24, 1760, 32, eyebrow, 'monomed', 22, MUTED),
        T(80, 76, 1760, 80, heading, 'xbold', 60, INK),
        Figure(80, 170, 1760, 792, svg, png),
    ]
    return slide


S.append(title(EYE, 'One class, two objects', 'And somewhere to keep them.',
    notes='Content Week 10; teaching date unconfirmed. The 2025 Week 10 PDF is a historical '
    'data-storage source, not the 2026 timetable. Begin with an artwork or other fictional '
    'project thing, not a login account. The core outcome is to create two independent '
    'instances, describe one method, then save and retrieve small records.'))
S.append(agenda(EYE, [
    'A recipe and two independent objects',
    'Predict one change; trace a method',
    'IDs and relationships between records',
    'Save, close, reload: what survives?',
    'Apply it to your project; optional retrieval',
], notes='The first four blocks are core. Make time for a paper trace and a restart '
    'check. The retrieval and MCP discussion can be skipped if foundational work '
    'needs more time. No current news item is claimed: add one only after checking '
    'its date, primary source and relevance near the actual class.'))
S.append(section('01 · OBJECTS', 'A recipe is not a thing',
    'Define once; make two different things.',
    notes='Ask students to name one repeatable type of thing in an interactive artwork '
    'before showing the class. The example uses two fictional artworks.'))
S.append(diagram('01 · CLASS AND INSTANCES', 'One recipe; two artworks', F.two_objects(),
    notes='An Artwork class describes what fields and behaviours an artwork can have. '
    'amber and blue are two instances. This picture represents live Python objects, '
    'not database rows. Ask which values differ, and whether changing amber must '
    'also change blue. The shapes and relationship are original, adapted from '
    'historical SD5913 Week 10 PDF pp. 13-18.'))
S.append(code_panel('01 · A CLASS', 'Construct two objects', [
    'class Artwork:',
    '    def __init__(self, title, views):',
    '        self.title = title',
    '        self.views = views',
    '',
    'amber = Artwork("Amber", 2)',
    'blue = Artwork("Blue", 7)',
    'print(amber.title, blue.title)  # Amber Blue',
], caption='The constructor runs each time we call Artwork(...).',
    notes='Runnable as shown in Python 3 without packages. A class is a definition; '
    'Artwork(...) creates one instance each time. self means the particular instance '
    'being initialized. The two calls supply distinct attribute values; these are '
    'not shared class variables. Ask a student to identify each title.'))
S.append(two_col('01 · READ IT ALOUD', 'Class, object, attribute, method', [
    'Artwork: shared definition',
    'amber: one object',
    'amber.views: one attribute',
    'amber.view(): one behaviour',
], [
    'class Artwork:',
    '    def view(self):',
    '        self.views += 1',
    '',
    'amber.view()',
    'print(amber.views)',
], notes='The method excerpt assumes amber was constructed on the preceding slide '
    'and view was added inside that class definition; it is not standalone. Ask '
    'what self points to when calling amber.view(). Do not introduce inheritance '
    'or an ORM before this distinction is secure.'))
S.append(statement('PREDICT BEFORE RUNNING\namber.view()\nWhat happens to blue.views?',
    notes='Think-pair-share. Keep the previous construction and method in view. '
    'Write amber.views and blue.views after the call before revealing the next '
    'slide. Expected: 3 and 7. If someone predicts both change, ask which '
    'self is passed to view(). This is an unassessed inspection activity.'))
S.append(diagram('01 · AFTER ONE METHOD CALL', 'Only the called object changes',
    F.separate_state(), notes='Answer to the preceding prediction: amber.views '
    'moves from 2 to 3; blue.views remains 7. Each instance has its own state. '
    'Have students explain the result in terms of self, not memorization.'))
S.append(code_panel('01 · RUN THE TRACE', 'Check the prediction in Python', [
    'class Artwork:',
    '    def __init__(self, title, views):',
    '        self.title, self.views = title, views',
 '    def view(self):',
    '        self.views += 1',
 'amber = Artwork("Amber", 2)',
 'blue = Artwork("Blue", 7)',
 'amber.view()',
 'print(amber.views, blue.views)  # 3 7',
], caption='Predict, run, then explain the different values.',
    notes='This full example is runnable as-is in Python 3. Invite a student to '
    'change blue instead; predict the result before running. Paper trace is the '
    'fallback if a Python interpreter is unavailable. Aligns with PFAD Week 10 '
    'companion PR #13 Activity 1, which is still a planning README, not runnable files.'))
S.append(content('01 · YOUR TURN', 'Trace a thing from your project', [
    'Name a class: artwork, scene, message or player.',
    'Choose two attributes and one small method.',
    'Describe two instances; change only one.',
    'Swap traces: can someone else explain the result?',
], notes='Give students time for a two-object paper trace. Fictional data only. '
    'Do not promise a prebuilt PFAD script: companion PR #13 has a planning '
    'activity and explicitly defers runnable examples. Circulate to distinguish '
    'one shared definition from the values belonging to each instance.'))
S.append(section('02 · RELATIONSHIPS', 'Which things belong together?',
    'Give each stored thing an ID before connecting it.',
    notes='Historical Week 10 PDF pp. 15-25 asks students to identify relationship '
    'types, then introduces IDs. Here use the same invented exhibition and '
    'artwork throughout. A relationship is a design choice, not an assessment rule.'))
S.append(diagram('02 · ONE TO MANY', 'One exhibition, many artworks', F.relation(),
    notes='Exhibition e1 has two artworks, a1 and a2. Each artwork stores the '
    'exhibition ID e1; its own ID identifies the artwork. The arrows show the '
    'conceptual one-to-many link; the actual saved records hold ID values, not '
    'Python object references. Ask which field connects a1 to e1. Historical '
    'source: Week 10 PDF pp. 15-18, 21-25.'))
S.append(two_col('02 · PREDICT A LINK', 'Which ID connects these records?', [
    'One exhibition has two artworks.',
    'Each artwork remembers the exhibition ID.',
    'What if the ID points to nothing?',
], [
    'exhibition = {"id": "e1",',
    '              "name": "Night"}',
    'artworks = [',
    '  {"id": "a1", "exhibition_id": "e1"},',
    '  {"id": "a2", "exhibition_id": "e1"},',
    ']',
], notes='Ask the room to find e1 in both records and to invent one broken '
    'reference (e99). A JSON file does not enforce foreign keys; an application '
    'must check references or choose a database with constraints. Do not imply '
    'that IDs are globally unique; only require uniqueness within this tiny set.'))
S.append(content('02 · OTHER SHAPES', 'When one-to-many is not enough', [
    'A player can join many teams.',
    'A team can contain many players.',
    'A membership record links their IDs.',
    'Start simple: use one-to-many unless you need more.',
], notes='Optional recognition, not required code. Historical Week 10 PDF pp. '
    '17-18 and 24 includes many-to-many. Do not teach ORM inheritance or schema '
    'migrations here. Ask whether an exhibition can belong to two artworks; '
    'clarify the difference between an exhibition with many artworks and an '
    'artwork linked to many exhibitions.'))
S.append(section('03 · SAVED DATA', 'The program will close',
    'What should still exist when we start it again?',
    notes='Move from live objects to stored records. The demonstrated route is '
    'a local JSON file and Python standard library; no database service, '
    'Docker, account or paid API.'))
S.append(diagram('03 · LIFETIMES', 'A live object is not a saved record', F.lifetimes(),
    notes='The picture shows two distinct things: an in-memory Python instance '
    'and a file containing a serializable record. Save converts values to a '
    'JSON-compatible dictionary; load reads values to make a new instance. '
    'Closing Python removes the live instance, not the local file. This '
    'simplifies historical PDF pp. 25-38.'))
S.append(code_panel('03 · SERIALIZE', 'Choose what belongs in a record', [
    'record = {',
    '    "id": "a1",',
    '    "title": amber.title,',
    '    "views": amber.views,',
    '    "exhibition_id": "e1",',
    '}',
    'print(record["views"])  # 3',
], caption='Record = data we want to keep; not the whole Python object.',
    notes='Assumes amber exists and was viewed once as in the trace. A record '
    'selects simple values to save; methods are not JSON data. An ID is stable '
    'for this fictional dataset and should not be confused with a title that '
    'someone might rename. A real project needs an ID assignment strategy.'))
S.append(code_panel('03 · SAVE', 'Write a small local JSON file', [
    'import json',
    'from pathlib import Path',
    '',
    'records = [',
    '    {"id": "a1", "title": "Amber", "views": 3,',
    '     "exhibition_id": "e1"},',
    '    {"id": "a2", "title": "Blue", "views": 7,',
    '     "exhibition_id": "e1"},',
    ']',
    'Path("artworks.json").write_text(',
    '    json.dumps(records, indent=2), encoding="utf-8")',
], caption='Run in a writable folder. Inspect artworks.json.',
    notes='Self-contained Python 3 standard-library snippet. write_text '
    'overwrites a file of the same name; warn before rerunning against anyone\'s '
    'own data. This is a tiny fictional demo, not a durable concurrent '
    'database or a secure credential store. The file is created in the '
    'current working directory. For live teaching use a disposable folder.'))
S.append(code_panel('03 · RESTART TEST', 'Close Python. Read the file back.', [
    'import json',
    'from pathlib import Path',
    '',
    'records = json.loads(Path("artworks.json").read_text(',
    '    encoding="utf-8"))',
    'for record in records:',
    '    print(record["id"], record["views"],',
    '          record["exhibition_id"])',
    '# a1 3 e1',
    '# a2 7 e1',
], caption='Run this as a fresh process in the same folder.',
    notes='Run after the save slide, in the same working directory. Exit '
    'Python first to demonstrate persistence across processes. If the file '
    'is missing or malformed, FileNotFoundError or JSONDecodeError tells us '
    'the demo cannot load it; no credentials or private records belong in '
    'this file. The e1 link survives as a string but is not checked against '
    'a saved exhibition record. Paper fallback: inspect a drawn JSON record.'))
S.append(two_col('03 · RECONSTRUCT', 'A loaded record can become a new object', [
    'The file contains values, not methods.',
    'A new object receives saved values.',
    'Its method works again after loading.',
], [
    'record = records[0]',
    'restored = Artwork(',
    '    record["title"], record["views"]',
    ')',
    'restored.view()',
    'print(restored.views)  # 4',
], notes='This excerpt assumes the Artwork class from the complete trace '
    'and records from the read slide are already defined in the interpreter. '
    'A fresh Python process would need the class definition again. Calling '
    'view() updates only the new in-memory object; save again to change the '
    'file. This is deliberate: students distinguish reconstructing from '
    'persisting a later update.'))
S.append(statement('CHECK THE FAILURE\nWhat if artworks.json is missing\nor an ID points to e99?',
    notes='Pair discussion. Missing file raises FileNotFoundError; a valid '
    'JSON file with a nonexistent exhibition_id loads normally, but the '
    'reference cannot be resolved. JSON by itself has no foreign-key '
    'validation. Ask where a test or validation check belongs. Overwriting '
    'a file is another risk; no multi-user guarantees here.'))
S.append(content('03 · CHOOSE THE SIMPLEST STORE', 'Store only what your work needs', [
    'A JSON file: small, local, one writer.',
    'SQLite: queries and relational constraints later.',
    'Hosted and vector stores: different needs, more setup.',
    'Never store real credentials in this exercise.',
], notes='Historical PDF pp. 26-38 introduces SQL, Peewee, NoSQL, vectors '
    'and Docker. Retain the decision question, not the framework walkthrough. '
    'SQLite comes with Python but is not required. Historical pp. 39-43 '
    'show an insecure bare SHA-256 password pattern: do not copy it. '
    'Authentication requires a separate reviewed approach.'))
S.append(section('04 · APPLY', 'Does this serve your project?',
    'A small design sketch before adding infrastructure.',
    notes='Core application exercise aligned with the proposed PFAD Week 10 '
    'companion PR #13: two-object trace and record/relationship sketch '
    'are working evidence, not an assessed submission.'))
S.append(content('04 · PROJECT SKETCH', 'Draw the data you actually need', [
    'Two objects of one class; one method on just one.',
    'Two records and their stable IDs.',
    'One link if your design needs it.',
    'Circle values that must survive a restart.',
], notes='Ask partners to exchange sketches and predict one changed value '
    'and one broken ID. Prefer fictional data. A project need not use AI or '
    'sound, and this activity adds no new assessed requirement. If a team '
    'does not need persistent state, it should say why rather than add a '
    'database by default.'))
S.append(diagram('OPTIONAL · RETRIEVAL', 'Find evidence before answering', F.grounded_answer(),
    notes='Teacher-only optional bridge from historical PDF pp. 44-55. Put '
    'three invented public exhibit-note passages on paper; ask which '
    'passage supports the opening-hours question, and what happens if none '
    'does. Matching a passage is not proof of a correct response. No '
    'embeddings, Qdrant, Ollama or live handbook documents are needed.'))
S.append(diagram('OPTIONAL · AGENT TOOLS', 'A tool offer is not permission', F.permission_boundary(),
    notes='Conceptual path: an agent proposes a call, an MCP server exposes '
    'a bounded tool, and the host/user sets permissions for access to data. '
    'Use a read-only lookup over fictional records as an example. Do not '
    'run writes, collect secrets or equate a model suggestion with '
    'authorization. This is a direction marker for later agent work, not '
    'a required installation today.'))
S.append(content('LOOKING AHEAD', 'Tools support the work; they are not the work', [
    'Git: share and review the project source.',
    'Scrum: agree a small next step and check it.',
    'Docker and networks: deploy only if a service needs them.',
    'Agent tools: design permissions before granting access.',
], notes='Visible map of current teaching direction, not a promise that '
    'these topics occur on particular dates or a new team process rule. '
    'Scrum, Git teamwork, Docker/networks and agent-to-MCP-to-tool are '
    'topics to place appropriately in the course sequence. No required '
    'asyncio and no compulsory AI for team projects.'))
S.append(end('What should survive?', 'Two objects now; the right records later.',
    'sd5913.github.io/teaching', notes='Exit prompt: name one attribute to '
    'save and one value to recompute; say which ID resolves a relationship. '
    'Do not set a deadline or collect real data.'))

attach_reports(S, HERE / 'week10-reports.json')

for index, slide in enumerate(S, 1):
    slide.els.append(T(1400, 1000, 400, 32, f'{index:02d}', 'monomed', 22,
        '#CCDADD' if slide.bg not in ('#FFFFFF', '#F4F4F2') else '#5C6470',
        lh=1.2, align='r', valign='b', spc=0.14, name='week10-slide-number'))

DECK = {'title': 'SD5913 · Week 10 · Classes, objects and saved data',
        'pdf': 'SD5913-week10.pdf', 'slides': S}
