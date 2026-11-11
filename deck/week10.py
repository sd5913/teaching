"""Persistent model classes and a source-backed, conversation-aware handbook bot."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen import Figure, INK, MUTED, Slide, T, WHITE, attach_reports
from deckgen.core import PAPER, Rect, Text
from deckgen.layouts import agenda, code_panel, code_paras, code_slide, content, end, section, statement, title, finalize
import week10_figures as F
import week09_layouts as L

S = []
EYE = 'SD5913 / WEEK 10 / 12 NOVEMBER 2026'
PFAD = 'https://github.com/sd5913/pfad/blob/ef4fd16bc1df69fd7f2d51f8184a48a3e130afc5/week10'
HANDBOOK = ('https://www.polyu.edu.hk/ar/docdrive/polyu-students/student-handbook/'
            'Student_Handbook_2026-27_English.pdf')


def diagram(heading, figure, notes):
    svg, png = figure
    slide = Slide(bg=WHITE, notes=notes, title=heading)
    slide.chrome = False
    slide.els = [T(80, 76, 1760, 90, heading, 'xbold', 60, INK),
                 Figure(80, 190, 1760, 792, svg, png)]
    return slide


def sql_example(label, heading, lines, figure, notes):
    slide = code_slide(label, heading, lines, figure=figure, notes=notes, code_size=36)
    # The pinned renderer highlights Python/JS only; keep SQL verbatim.
    code = next(el for el in slide.els if getattr(el, 'name', '') == 'code')
    code.paras = code_paras(lines, 36, lang=None)
    return slide


def orm_example(label, heading, python_lines, sql_lines, params, conclusion, notes):
    slide = L.page(heading, notes)
    slide.els += [
        T(120, 88, 1680, 40, label, 'mono', 22, MUTED),
        T(120, 330, 780, 60, 'Python / Peewee ORM', 'bold', 44),
        T(1020, 330, 780, 60, 'Generated SQL', 'bold', 44),
        Rect(120, 420, 780, 400, PAPER),
        Rect(1020, 420, 780, 400, PAPER),
        Text(144, 444, 732, 360, code_paras(python_lines, 30), name='code'),
        Text(1044, 444, 732, 286, code_paras(sql_lines, 30, lang=None), name='sql'),
        T(1044, 754, 732, 56, 'Bound values: ' + params, 'mono', 32),
    ]
    L.takeaway(slide, conclusion)
    return slide


# 0-10: one question connects storage, history and source evidence.
S.append(title(EYE, 'What survives\na conversation?',
    'Persistent objects, relationships and database choices.', size=130,
    notes='0-2 minutes. A player returns to a game NPC and asks: what if I find the original later? '
    'A convincing voice is easy to mistake for reliable memory. Today we inspect one small system '
    'in enough detail to distinguish remembered conversation from handbook evidence. Week 7 classes, '
    'Week 8 verification and Week 9 request/process ideas are prerequisites; do not repeat constructors. '
    'Week 9’s Scene resets after restart. Reuse Week 6 Pip for speech. '
    'Lecture: 120 minutes including a 10-minute break; separate tutorial: 120 minutes.'))
S.append(statement('A returning user asks:\n“What about the original?”', size=100,
    notes='2-6 minutes. Ask what the word original refers to. Without the preceding discussion it is '
    'ambiguous. In our later real example the user lost a student identity card. The assistant needs '
    'the previous conversation to understand the reference and current handbook passages to answer '
    'the policy question. Ask what should survive closing the app, then reopening it. '
    'Use one conversation as the running example throughout the lesson.'))
S.append(agenda(EYE, ['Save an object', 'Connect related records',
    'Choose and query a database', '10-minute break',
    'Find handbook evidence', 'Give Pip history and a voice'],
    notes='6-10 minutes. First-half outcomes: explain persistence and identity; model relationships; '
    'choose storage from the data and access pattern; distinguish schema, keys, indexes and ORM. '
    'These are conceptual quiz/revision topics, not just code-reading tasks. Exact timing: '
    '10-20 persistence; 20-34 relationships; 34-46 database choices/schema/keys; 46-60 SQL/ORM and '
    'a short SQLite/D1 demonstration; 60-70 break; 70-83 Semantle/word/text embeddings; '
    '83-95 handbook/tool retrieval; 95-115 typed '
    'conversation, reload/isolation and speech; 115-120 recap/handoff. Optional two-minute news '
    'discussion replaces part of this opening: Peewee 4.5.3 write-execution fix, '
    'https://github.com/coleifer/peewee/releases/tag/4.5.3 (checked 29 October). '
    'Ask whether saving twice should update a record or create another; no release trivia in quiz scope. '
    'Explain that the application '
    'requires retrieval, while the local model composes the query and judges source support. This '
    'bounded tool workflow is a step toward next week’s application tools, not an autonomous agent demo.'))

# 10-20: persistent state, stored identity and reconstruction before library syntax.
S.append(section('01 / PERSISTENCE', 'Persistence',
    'What survives a restart?', bg=INK,
    notes='Transition at minute 10. Move from the returning-user question to saved state. '
    'This divider is a signpost within the existing block, not additional lecture time.'))
S.append(L.compare('Persistence: data that survives a restart.',
    ('In memory', 'A live object in\nthe running program.', 'An unsaved change\nis lost on restart.'),
    ('In storage', 'Saved values, IDs\nand relationships.', 'A new process can\nload them again.'),
    notes='10-13 minutes. A variable, object or server connection in RAM is temporary state. '
    'Writing data to persistent storage gives a later process something to read. Restarting a '
    'program is not the same operation as deleting its saved file or database volume. Persistence '
    'also does not promise backups, permanent retention or survival of every disk failure. '
    'A message can be displayed successfully before it has been saved: ask what evidence '
    'would distinguish the two. Use the already-observed Week 9 restart as the contrast.',
    conclusion='Data survives; methods come from the program.'))
S.append(diagram('Save data. Reload a new object.', F.restart(),
    '13-17 minutes. Follow the three numbered stages. Process A saves conversation 3, '
    'its owner ID and title, then stops. '
    'The SQLite file stays on disk. Process B imports the class definitions and queries the '
    'saved ID, creating a new Python instance with the saved values. Its stored identity can '
    'match even though it is a different live object. The methods work because their code '
    'was imported, not because SQLite stored Python functions. This is also why editing a '
    'class method changes later behavior without changing every saved row. '
    'Pause for the visible question: if the live title changes without saving, the new '
    'process still reads the earlier saved title. The owner link and stored ID survive too. '
    'A stable database ID is not Python id(obj), which has no cross-process identity guarantee.'))
S.append(L.compare('A save file or a database?',
    ('Serialized file', 'Write a snapshot\nsuch as a JSON save.', 'Useful when you load\nand replace a whole save.'),
    ('Database', 'Organize and query\nmany stored records.', 'Indexes, constraints\nand transactions help.'),
    notes='17-20 minutes. Serialization encodes selected values into a storable form. A JSON '
    'document can preserve a small scene or settings snapshot; the application still decides '
    'how to represent IDs and links. As related records and partial updates grow, a database '
    'provides query, integrity and transaction facilities. This is not file versus server: '
    'SQLite is a real database stored in a file. A remote service is another deployment choice. '
    'Neither a JSON file nor a database automatically saves every future object mutation.',
    conclusion='SQLite is a database stored in a file.'))

# 20-34: restore the 2025 relationship explanations and active modelling drills.
S.append(section('02 / RELATIONSHIPS', 'Relationships',
    'How do saved records connect?', bg=INK,
    notes='Transition at minute 20. We know which values survive; now explain their links.'))
S.append(diagram('One-to-many: one owner, many conversations.', F.one_to_many(),
    '20-23 minutes. Cardinality means how many records may be linked. Count in both '
    'directions. Ada owns conversations 3 and 4. Each conversation has exactly one owner '
    'in this application. Storing the owner ID on each conversation represents the link; '
    'copying Ada and her name into every conversation creates repeated data that can disagree '
    'after a rename. Loading a conversation can follow that stable reference to its owner. '
    'A user with no conversations is allowed. The diagram shows example records, not a '
    'requirement to store one fixed number of conversations. Historical 2025 pages 15-16.'))
S.append(diagram('One-to-one: at most one profile per user.', F.one_to_one(),
    '23-25 minutes. Count the links in both directions, then ask whether zero is allowed. '
    'These are declared example rules, not claims about every app. '
    'One-to-one may split optional or separately controlled details into another record; '
    'a unique constraint on the reference can enforce the maximum of one. A foreign key '
    'alone does not turn a one-to-many relation into one-to-one. Here a user can have '
    'zero or one profile; each profile requires one valid user. Profile is a modelling '
    'transfer example, not an implemented feature in the supplied app.'))
S.append(diagram('Many-to-many: count in both directions.', F.many_to_many(),
    '25-26 minutes. Follow Ada to Lantern and Orbit, then Lantern to Ada and Bo. '
    'Both sides can have many links. Ask where to store Ada\'s team role: she leads '
    'Lantern but is an artist in Orbit. Keep these exact links in view on the next '
    'slide, which represents each link as a Membership record.'))
S.append(diagram('Many-to-many: add a junction record.', F.junction(),
    '26-28 minutes. Ada joins Lantern and Orbit; Lantern contains Ada and Bo. '
    'Users can join many teams, and teams can contain many users. Each Membership '
    'refers to one User and one Team; each parent can have '
    'many memberships. This represents the many-to-many relation through two one-to-many '
    'relations. Follow the three joining rows: 1/7, 2/7 and 1/9. The '
    'role belongs to the membership: Ada may lead one team and be an artist in another. '
    'A joined-at date would belong here too. For a current-membership table, making the '
    'user/team pair unique prevents duplicate links. Historical membership history may '
    'need a different rule; declare the purpose before choosing the constraint.'))
S.append(diagram('Self-reference: a message replies to a message.', F.self_reference(),
    '28-30 minutes. The reply-to reference points to the same record type, Message. Message '
    '8 replies to 7, and 9 replies to 8; the first has no parent reply. A self-reference is '
    'not automatically one-to-one: many replies could reference the same message. It is '
    'also not inheritance or an object containing itself. Directed reply/supervisor links '
    'differ from symmetric friendship; additional application rules may be needed for '
    'cycles or symmetry. This is an illustrative modelling transfer, not a field claimed '
    'to be implemented by the supplied Message class. Historical page 19.'))
S.append(L.rows('Try it: name the relationship.', [
    ('Player / Score', 'A player has many scores; each score has one player.'),
    ('Player / Team', 'Each player joins at most one team; a team can have many players.'),
    ('Tag / Post', 'Posts can have many tags; a tag can label many posts.'),
], notes='30-34 minutes. Pair discussion: state the cardinality and where references '
    'or a junction belong. Player/Score is one-to-many. A team may have many players, '
    'so the second rule gives '
    'Team-to-Player one-to-many; do not memorize Player/Team as always many-to-many. '
    'Tag/Post needs a joining relation. Ask what changes if players can join several teams. '
    'User/Group and Conversation/Message are further cases in the PFAD revision section; '
    'all five historical 2025 exercises remain available without repeating them on slides.'))

# 34-46: database families, schema and keys are visible conceptual material.
S.append(section('03 / DATABASE TYPES', 'Database types',
    'Choose storage for the question.', bg=INK,
    notes='Transition at minute 34. Compare the models used to organize and retrieve data.'))
S.append(diagram('Database types: the map.', F.database_taxonomy(),
    '34-35 minutes. Classify by data model first: relational tables versus the common '
    'non-relational families grouped under NoSQL. NoSQL is an umbrella, not one database '
    'and not an absence of rules. SQL is a query language; some non-relational systems '
    'also offer SQL-like query languages. Products can support several models, so this '
    'is a teaching taxonomy rather than mutually exclusive product boxes. Local file '
    'versus hosted service is a deployment choice, not another data-model family. '
    'The orange band marks a different dimension: similarity search can be provided by '
    'a specialist vector database or added to another database. Introduce the map here, '
    'then unpack the families and vector search on the next two slides.'))
S.append(L.rows('Four common NoSQL families.', [
    ('Key-value', 'One key selects a value: preferences (Redis).'),
    ('Document', 'A nested record: a scene and its settings (MongoDB).'),
    ('Wide-column', 'Rows grouped for known queries: device events (Cassandra).'),
    ('Graph', 'Nodes and edges: who is connected? (Neo4j).'),
], notes='35-37 minutes. Key-value retrieves a value by a key; a document keeps nested '
    'fields/lists together; wide-column organizes keyed rows into column families for '
    'chosen access patterns; a graph makes relationships first-class edges to traverse. '
    'Cassandra is a wide-column example, not a synonym for a columnar analytics engine. '
    'Product names are examples, not quiz memorization targets or installation tasks. '
    'Document stores may validate schemas; relational databases can also store JSON. '
    'NoSQL alone does not imply no relationships, no transactions or unlimited scale. '
    'Source: https://aws.amazon.com/nosql/ .'))
S.append(L.compare('Vector search: find similar items.',
    ('Vector database', 'Store vectors;\nrank similar items.', 'Qdrant: a specialist\nnon-relational database.'),
    ('Vector feature', 'Add similarity search\nto an existing database.', 'PostgreSQL + pgvector\nkeeps relational tables.'),
    notes='37-39 minutes. A vector represents an item as numbers. A vector database '
    'specializes in storing/indexing vectors and ranking nearby candidates, often with '
    'metadata filters. Specialist vector databases such as Qdrant are non-relational. '
    'This is useful for semantic search and recommendations; proximity '
    'does not prove truth. It differs from an exact key lookup or a declared foreign key. '
    'Vector search is also available as a capability in relational/document systems. '
    'For example, pgvector adds vector columns and similarity queries to PostgreSQL; '
    'it does not replace its relational tables. Our bot combines SQLite history and '
    'Qdrant knowledge for clarity; two separate products are not a universal requirement. '
    'Primary example checked through Context7: https://github.com/pgvector/pgvector . '
    'The second half shows actual vectors, rankings and Qdrant rather than another taxonomy.',
    conclusion='Vector search can coexist with exact queries and filters.'))
S.append(L.rows('Try it: choose storage for the job.', [
    ('Team accounts', 'Find every message in one user-owned conversation.'),
    ('Scene save', 'Load one nested scene with its object settings.'),
    ('Handbook search', 'Find passages with meaning similar to a new question.'),
], notes='39-41 minutes. Suggested fits are related rows, a nested document/save and '
    'vectors with source metadata. Accept another design when the student explains '
    'how it serves the access pattern and integrity needs. A simple JSON save may '
    'suffice for the scene; SQLite may also store its nested document. Similarity '
    'does not guarantee policy support. Ask why the same bot uses relational history '
    'and vector knowledge instead of forcing both jobs into one representation. '
    'This restores the archive page 38 decision exercise, not a product recall quiz.'))
S.append(diagram('Schema: the rules for stored data.', F.schema(),
    '41-43 minutes. The left side describes fields, types and constraints; the right side '
    'contains particular rows conforming to that schema. Required, unique and valid '
    'reference rules are different constraints. Updating a title changes data; adding '
    'a new required field changes the schema and can require a migration of existing '
    'data. The database can enforce declared constraints; the ORM maps class operations '
    'to queries and is not the only source of integrity. This corrects the archive '
    'page 26 conflation of schema enforcement with ORM.'))
S.append(diagram('Keys identify and connect. Indexes help lookup.', F.keys(),
    '43-45 minutes. Primary key: uniquely identifies this row within its table. Foreign '
    'key: stores a reference to a parent row; enforced integrity rejects missing parents. '
    'An ordinary index is extra lookup structure that helps selected searches/orderings '
    'and costs storage/work on writes. An indexed foreign-key column can do both jobs. '
    'An ordinary index need not be unique; names can repeat even when IDs cannot. '
    'No measured speedup is claimed for this tiny dataset. A semantic vector index '
    'answers a different kind of question. Historical page 25, with corrected limits.'))
S.append(content('DISCUSS / keys and indexes', 'Which job needs which mechanism?', [
    'Identify a conversation after its title changes.',
    'Link it to an existing user.',
    'Help find its messages in order.',
], body_size=46,
    notes='45-46 minutes. Practice retrieval of the concepts: a stable primary key '
    'identifies the conversation; an owner foreign key references a User and an '
    'enforced constraint checks existence; a suitable index helps a lookup. '
    'A foreign key does not authenticate the caller. Ask whether a missing '
    'parent can be accepted when the constraint is enforced. A saved ID is not '
    'a memory address and an index is not a copy of the owner object.'))

# 46-60: connect the theory to a compact, real implementation and restart check.
S.append(section('04 / SQL', 'Query the records',
    'Read the keywords. Follow the rows.', bg=INK,
    notes='Transition at minute 46. Start with a plain SQL query before showing ORM code.'))
S.append(L.rows('Read a SQL query.', [
    ('SELECT', 'Which columns should the result contain?'),
    ('FROM', 'Which table supplies the rows?'),
    ('WHERE', 'Which rows meet the condition?'),
    ('ORDER BY', 'In what order should the result appear?'),
], notes='46-47 minutes. These are instructions for describing a result. Read the '
    'four phrases before showing a complete query. In the next example we want '
    'message IDs and text, from the message table, only for conversation 3, '
    'ordered by message ID. A foreign key can be used as a filter in one table; '
    'you do not need a JOIN just to find the children of a known parent.'))
S.append(sql_example('SQL / FILTER BY A FOREIGN KEY', 'Find messages in conversation 3.', [
    'SELECT id, content',
    'FROM message',
    'WHERE conversation_id = 3',
    'ORDER BY id;',
], figure=F.sql_history(),
    notes='47-48 minutes. Read the query in ordinary language: return each message\'s '
    'ID and content from message, keep rows whose conversation_id is 3, then order '
    'by message ID. conversation_id is the foreign key referring to conversation.id; '
    'message.id is the primary key of each individual message. Follow the source '
    'rows on the right: messages 7 and 8 both reference conversation 3. Message 9 '
    'references conversation 5 and is excluded. The source view shows only the '
    'two ID columns; the result shows the selected ID and content. SELECT chooses '
    'columns; WHERE chooses rows. Ask what WHERE id = 3 would mean instead: one '
    'message with primary key 3, not every message in conversation 3. '
    'This fictional text is prepared storage data, not a live answer or policy '
    'advice. We use literal 3 to make this first query readable. In application '
    'code, bind a runtime value with WHERE conversation_id = ?; the inspected '
    'Peewee query prints that parameter separately. Store.history_query checks '
    'owner access first. A matching foreign key alone does not grant access or '
    'put the selected history into the model prompt. '
    'Reference: https://www.sqlite.org/lang_select.html .'))
S.append(content('SQL / operations on related records', 'SQL reads and changes rows.', [
    'INSERT adds rows; SELECT reads matching rows.',
    'UPDATE changes values; DELETE removes rows.',
    'WHERE selects matches; ORDER BY sets their order.',
    'JOIN combines related rows by a matching condition.',
], body_size=44,
    notes='48-49 minutes, with the next slide. Extend the worked SELECT to '
    'the other operations, then connect it to the actual Python models and ORM. '
    'SQL is declarative: describe the result/change, not a Python loop over '
    'every object. A JOIN commonly matches a foreign key to a parent primary key, '
    'but a query join does not itself declare or enforce a stored foreign key. '
    'The worked queries filter one conversation, join owners to titles and update one '
    'saved record. Students should '
    'explain what the operation does; memorizing an installation command is not the goal.'))
S.append(code_panel('PFAD / models.py', 'The same relationships in Python.', [
    'class User(Record):', '    name = TextField(unique=True)', '',
    'class Conversation(Record):',
    '    owner = ForeignKeyField(User)', '    title = TextField()', '',
    'class Message(Record):',
    '    conversation = ForeignKeyField(Conversation)',
    '    role = TextField()', '    content = TextField()',
], caption='Excerpt: the full file also defines the database, constraints and index.',
    notes=f'48-49 minutes, continued. Read {PFAD}/models.py. Students now recognize the '
    'one-to-many relationships before reading the fields. Record inherits Peewee '
    'Model, then these classes inherit Record. Each model receives an integer '
    'primary key. Point to owner and conversation as references, and title/role/'
    'content as values. Keep this as evidence for the diagrams, not a second '
    'constructor lecture or a requirement to memorize library syntax.'))
S.append(diagram('ORM: Python operations become SQL.', F.mapping(),
    '49-50 minutes, with the next slide. ORM means Object-Relational Mapper. '
    'It translates model methods into SQL '
    'and constructs model instances from returned rows. Peewee supplies these '
    'inherited methods; SQLite stores data and enforces declared constraints. '
    'Trace chat.save() to an UPDATE of the same row ID. Attribute '
    'assignment alone changes the live object; a saved update changes the record '
    'that a later process can load. The generated stored ID is not Python id(chat). '
    'The query arrow reconstructs another live instance from stored values. '
    'This ties the earlier persistence prediction to a method students can inspect '
    'in storage_demo.py. Methods remain in the program, not in the row.'))
S.append(orm_example('ORM / FOREIGN-KEY SELECT', 'Python builds the same foreign-key query.', [
    'query = (Message',
    '    .select(Message.id, Message.content)',
    '    .where(Message.conversation == 3)',
    '    .order_by(Message.id))',
    'sql, params = query.sql()',
    'messages = list(query)',
], [
    'SELECT "t1"."id", "t1"."content"',
    'FROM "message" AS "t1"',
    'WHERE ("t1"."conversation_id" = ?)',
    'ORDER BY "t1"."id"',
], params='[3]', conclusion='Build a query. Inspect its SQL. Run it and load Message objects.',
    notes='49-50 minutes, continued. Match select to SELECT, Message to FROM message, '
    'where to WHERE and order_by to ORDER BY. Message.conversation is the Python '
    'foreign-key field; Peewee maps it to the conversation_id SQL column. The '
    'query is a Python query object: constructing it does not run SELECT. '
    'query.sql() compiles and returns the SQL string and separate bound values; '
    'it still does not run the query. list(query) sends SQL and values to SQLite '
    'and turns the returned rows into new Message instances. Their IDs/content '
    'are 7/Lost card? and 8/Apply online., just as in the earlier SQL slide. '
    't1 is a generated table alias, not a different table. The displayed SQL '
    'is Peewee 4.5.3 output, line-wrapped for reading. The ORM generates SQL; '
    'the database executes it and enforces constraints. This is core quiz scope: '
    'explain the translation and execution, not merely expand the acronym. '
    'Reference: https://docs.peewee-orm.com/en/latest/peewee/querying.html .'))
S.append(diagram('JOIN: match the stored IDs.', F.relations(),
    '50-51 minutes, with the next slide. These are two actual table shapes from the supplied model. '
    'Ada\'s name appears once in user; conversations 3 and 4 store owner_id 1. '
    'Trace both links to user.id 1, and the third conversation to Bo, user.id 2. '
    'A JOIN reads these matches to construct a result. It does not copy Ada\'s '
    'name into the saved conversations or modify the source rows. The next '
    'slide asks for Ada\'s conversation titles together with her name.'))
S.append(orm_example('ORM / JOIN', 'Whose conversations are these?', [
    'query = (Conversation',
    '    .select(Conversation.id, User.name,',
    '            Conversation.title)',
    '    .join(User)',
    '    .where(User.id == 1)',
    '    .order_by(Conversation.id))',
    'sql, params = query.sql()',
    'rows = list(query.tuples())',
], [
    'SELECT "t1"."id", "t2"."name",',
    '       "t1"."title"',
    'FROM "conversation" AS "t1"',
    'INNER JOIN "user" AS "t2"',
    '  ON ("t1"."owner_id" = "t2"."id")',
    'WHERE ("t2"."id" = ?)',
    'ORDER BY "t1"."id"',
], params='[1]', conclusion='Result: (3, Ada, Handbook), (4, Ada, Game notes).',
    notes='50-51 minutes, continued. The model fields let Peewee construct the '
    'correct JOIN: Conversation.owner is a ForeignKeyField(User), so .join(User) '
    'uses owner_id = user.id. The database does the join, not a Python loop '
    'loading every user. t1 and t2 are generated aliases. '
    'ON states how records match: the stored owner reference equals the user\'s '
    'primary key. WHERE keeps user 1, so the result contains Ada\'s conversations '
    '3 and 4 with her name beside each title. Conversation 5 belongs to Bo and '
    'is excluded. Repeating Ada in a query result is different from storing '
    'duplicate user records. This inner JOIN returns matching rows only; it '
    'does not itself declare a foreign key or authenticate the requesting caller. '
    'The chained methods build a query object. query.sql() returns the actual '
    'SQL/parameters without execution; list(query.tuples()) runs it and asks '
    'for tuple rows so the three selected columns can be compared directly. '
    'Without a different result mode, SELECT normally constructs model instances. '
    'Reference: https://www.sqlite.org/lang_select.html .'))
S.append(orm_example('ORM / UPDATE', 'Change one title. Keep its identity.', [
    'query = (Conversation',
    '    .update(title="Game ideas")',
    '    .where(Conversation.id == 3))',
    'sql, params = query.sql()',
    'changed = query.execute()',
], [
    'UPDATE "conversation"',
    'SET "title" = ?',
    'WHERE ("conversation"."id" = ?)',
], params="['Game ideas', 3]", conclusion='1 row updated. Same ID and owner; new title.',
    notes='51-52 minutes. Match .update to UPDATE/SET and .where to WHERE. '
    'Building or inspecting the query changes no rows; .execute() sends it '
    'to SQLite and returns the affected-row count, here 1. '
    'Bind Game ideas, then 3, in placeholder order. The '
    'UPDATE targets the existing row, changing its title but keeping ID 3 and '
    'owner 1. UPDATE returns an affected-row count, not SELECT result rows. '
    'Ask what would happen without WHERE: every '
    'conversation title would change. A nonexistent ID updates zero rows. '
    'An instance method chat.save() also builds and runs an UPDATE for that '
    'instance\'s ID; by default Peewee may write other loaded fields too. '
    'Assignment alone does not run an UPDATE. The application must '
    'check owner access before allowing a change. '
    'Reference: https://www.sqlite.org/lang_update.html .'))
S.append(code_slide('PRACTICE / ORM AND PERSISTENCE', 'Check: is this change saved?', [
    'chat = Conversation.get_by_id(3)',
    'chat.title = "Game ideas"',
], figure=F.orm_check(), code_size=36,
    notes='52-53 minutes. Ungraded practice, not an official quiz item. Start '
    'a fresh example whose database row 3 is titled Handbook. The first line '
    'runs a SELECT and constructs a Conversation object; the assignment '
    'changes only its in-memory title. Ask what another process loads before '
    'any .save(): B, Handbook. A confuses an attribute assignment with a '
    'database write; C confuses changing a live value with deleting a row. '
    'Ask which extra operation would persist the change: chat.save(), which '
    'generates and executes UPDATE for row 3. Explain the complete ORM job: '
    'translate model operations to SQL/values, send them to the database, '
    'and construct Python instances for query results. SQL and constraints '
    'still exist underneath. A second short question can ask which line on '
    'the earlier SELECT slide runs SQL: list(query), not query.sql().'))
S.append(L.steps('Transaction: save both messages together.', [
    ('Write question', 'The first new\nmessage row.'),
    ('Write answer', 'The second new\nmessage row.'),
    ('Commit both', 'Make the complete\nturn persistent.'),
], notes='53-54 minutes. A transaction groups changes into one unit: commit '
    'all of them or roll back the new changes on failure. If the answer violates '
    'the nonempty-content rule, the newly inserted question must also roll back; '
    'older committed turns remain. Atomicity is the all-or-nothing property. '
    'This is different from a foreign key or an index. In our example the '
    'model call finishes and validates before this database transaction; '
    'the transaction does not make the network request atomic.',
    conclusion='If either write fails, roll back both new rows; keep older saved turns.'))
S.append(code_panel('LIVE / prepared terminal in pfad/week10', 'Save, restart, check.', [
    'uv run python storage_demo.py seed',
    'uv run python storage_demo.py inspect',
    'uv run python storage_demo.py rename',
    'uv run python storage_demo.py inspect',
    'uv run python storage_demo.py invalid',
], lang=None, caption='Each command is a new process. Predict the saved title, ID and references.',
    notes='54-56 minutes. Use prepared terminals and a disposable database; run the '
    'prepared command sequence without setup or live typing. '
    'Seed creates fictional '
    'profiles and two explicitly prepared storage messages, not a model answer. '
    'Inspect prints rows, generated SQL/parameters and index names. Rename changes '
    'the title and saves it; the new inspect process reads the changed title with '
    'the same ID and owner reference. Invalid rejects an orphan via the enforced '
    'foreign key. Ask students to explain the evidence using persistence, identity '
    'and integrity. Reused IDs can differ; do not promise every file starts at 1. '
    'Longer edits and the rollback experiment belong in the separate tutorial.'))
S.append(code_panel('D1 / reuse the Week 4 API idea', 'Put the database behind an API.', [
    '# Simplified shape inside week10/d1/src/worker.py',
    'SQL = "SELECT * FROM message WHERE conversation_id = ?1"',
    'result = await self.env.DB.prepare(SQL).bind(conversation).all()',
    'return Response.json(result)',
], lang=None, caption='The complete prepared example joins messages to their conversation title.',
    notes='56-58 minutes. Prepared D1 demo only: GET /messages?conversation=1 '
    'on port 8010. Trace HTTP request, checked ID, bound SQL/JOIN and JSON result. '
    'Show the prepared changed title surviving a Worker restart. Week 4 used '
    'a Python Worker reading a JSON tide file; it had no D1 binding. D1 is a '
    'SQLite-based relational service; local emulation stores state separately '
    'from Worker memory. This async shape is an excerpt inside fetch, not a '
    'standalone script. No account, remote database or deployment is needed. '
    'Keep the demo to two minutes; full commands and restart work are in the '
    'tutorial. Reference https://developers.cloudflare.com/d1/examples/query-d1-from-python-workers/ .'))
S.append(L.rows('Three questions for any saved system.', [
    ('Persistence', 'Which values and links survive, and where are they stored?'),
    ('Relationships', 'What are the rules in both directions? Which IDs link records?'),
    ('Database choice', 'What must be retrieved, changed together and kept consistent?'),
], notes='58-60 minutes. Ask for one explanation using a save file, team membership '
    'or conversation. These are quiz/revision concepts students can apply to an '
    'unfamiliar scenario. Distinguish primary key, foreign key, index, schema, '
    'SQL, ORM and transaction; knowing a library name is insufficient. '
    'The second half applies the same choices to relational conversation '
    'history and a vector knowledge index, not a new definition of persistence.'))
S.append(section('60-70 / BREAK', '10-minute break',
    'Next: what can the handbook actually support?', bg=INK,
    notes='60-70 minutes. Ten-minute break inside the 120-minute lecture. Keep the '
    'inspected rows available. Before resuming, check the prepared Qdrant service '
    'on 127.0.0.1:6333 and tool-capable LM Studio model on 127.0.0.1:1234/v1. '
    'No model download or new platform installation belongs in the lesson.'))

# 70-83: Semantle motivates word embeddings, then text embeddings and retrieval.
S.append(section('05 / RETRIEVAL', 'Retrieval',
    'Find handbook passages by meaning.', bg=INK,
    notes='Transition at minute 70. Start with the instructor\'s Semantle example before '
    'showing vectors or the handbook system. Ask how a computer could compare meaning '
    'rather than matching the same letters. The next sequence develops word embeddings '
    'into passage/question embeddings before the existing Qdrant/Pip demonstration.'))
S.append(content('LIVE / WORD EMBEDDINGS', 'Semantle: guess by meaning.', [
    '[Open semantle.com](https://semantle.com/).',
    'Guess one word; inspect its similarity score.',
    'Try a word with related meaning. What changes?',
    'How can a computer measure semantic similarity?',
], body_size=44,
    notes='70-73 minutes. Instructor-led live example, not a separate tutorial exercise. '
    'Open https://semantle.com/ in a browser. Ask for a broad first guess, then two or '
    'three related guesses and compare the actual scores. The aim is to notice the '
    'feedback, not solve the daily puzzle. A related guess need not improve the score. '
    'The current How to play text explicitly names word2vec and says similarity '
    'concerns meaning rather than spelling, checked 11 November. Do not invent '
    'scores, reveal the daily answer or assume yesterday\'s ranking is today\'s. '
    'Use the observed words to introduce a learned representation of meaning. '
    'If the site is unavailable, explain the single-word guess/similarity loop '
    'without claiming a live round. Source: https://semantle.com/faq .'))
S.append(diagram('An embedding is a learned list of numbers.', F.word_embedding(),
    '73-75 minutes. A vector is a list of numbers. An embedding is a learned numeric '
    'representation of an input in a vector space. With word2vec, training learns '
    'word vectors from word/context patterns in a large text corpus. At use time '
    'the trained model supplies a vector for a known word. Words used in related '
    'contexts often have similar vectors, which gives a numerical similarity '
    'signal. Related is broader than synonym: opposites can appear in similar '
    'contexts too. The values are not a word ID, spelling code or a hand-written '
    'list of dictionary properties. Individual coordinates need not have readable '
    'names such as friendliness. Training establishes this space; playing Semantle '
    'does not retrain it after each guess. No fixed dimension or exact score is '
    'asserted for the current game.'))
S.append(L.compare('From one word to a passage.',
    ('Word embeddings', 'One word has\na learned vector.', 'Semantle compares\nguess and target words.'),
    ('Text embeddings', 'A sentence or passage\nhas a learned vector.', 'Our bot compares\na question and passages.'),
    notes='75-77 minutes. Carry over the idea of comparing learned representations, '
    'then change the unit of input. A text encoder considers the words together '
    'and produces one fixed-size vector for a sentence or short passage. This '
    'is not a claim that Semantle\'s word2vec vectors can be reused in our bot, '
    'or that MiniLM simply looks up a whole sentence in a dictionary. Our trained '
    'sentence encoder uses context-sensitive token representations and pooling; '
    'do not teach arbitrary averaging of static word vectors as this model. '
    'The game\'s word space and our MiniLM text space are different. Within the '
    'handbook system, questions and passages use the same compatible encoder. '
    'For example, card replacement cost can be relevant to How much is a new '
    'student card? despite different phrasing. Similarity still needs checking.',
    conclusion='The same idea scales from words to short passages.'))
S.append(diagram('Embed both questions and passages.', F.text_embeddings(),
    '77-79 minutes. Follow both inputs through the same trained MiniLM text encoder. '
    'Each output has 384 numbers even though the input lengths differ. That '
    'fixed-size vector represents learned semantic features of the whole short '
    'text, not a list of word IDs. The question and passage can then be compared '
    'numerically. The fee wording is an illustrative short paraphrase of the '
    'supplied fee row, not a verbatim quote or a newly generated answer. '
    'The handbook passages are encoded during preparation; a new question is '
    'encoded when asked. The encoder creates vectors; the vector database later '
    'stores and compares them. No part of this step writes a conversational '
    'answer or proves the passage supports one. This diagram uses placeholders '
    'rather than invented vector coordinates. Reference: '
    'https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html .'))
S.append(code_panel('REAL / MiniLM handbook fixture', 'Text becomes a vector.', [
    '# Source: hb2026-p020-replacement, PDF page 20',
    '# vector[:8] from the supplied real learned fixture:',
    '-0.060211, 0.055605, 0.027168, -0.040987, 0.053495, -0.023228, 0.058877, -0.033763', '',
    '# Full vector: 384 values, L2 normalized',
    '# Same pinned encoder is used for every new question.',
], caption='The full vector, passage and encoder revision travel together in handbook.json.',
    notes=f'79-80 minutes. Now inspect the numeric representation already explained. '
    f'Read {PFAD}/fixtures/handbook.json and run uv run python handbook.py. '
    'These displayed numbers are copied from the genuine generated fixture, not made-up coordinates. '
    'MiniLM revision1110a243fdf4706b3f48f1d95db1a4f5529b4d41, masked-mean pooling,384 dimensions, '
    'normalization and256-token maximum. This is a sentence-transformer trained on text, replacing '
    'the earlier short-context CLIP feasibility candidate. The index stores text/page/source identity too.'))
S.append(diagram('Compare question and passage vectors.', F.search(),
    '80-81 minutes. Documents and questions use the same pinned MiniLM snapshot and normalization. '
    'Matching384 dimensions alone is insufficient: two unrelated encoders can both emit384 numbers. '
    'Our code compares the full encoder identity and rejects a mismatch; the constructor loads '
    'the pinned public revision locally. Input longer than256 tokens is rejected rather than '
    'silently truncated. New question input needs the actual encoder, not a keyword substitute.'))
S.append(diagram('Similarity ranks possible matches.', F.ranking(),
    '81-82 minutes. The exact prepared fee question ranks the fee row0.892566 and replacement '
    'rule0.737337. These are observed cosine similarities from the shipped vector fixture. '
    'A long noisy fee-table extract initially missed the desired top two; the revised exact row '
    'extract improves this question. This is a measured result for one question, not a benchmark '
    'or proof all policy questions work. Keep the HK$ table heading in section metadata.'))
S.append(statement('An unrelated question\nstill has a\nnearest neighbour.', size=100,
    notes='82-83 minutes. Ask whether a high-ish score proves the passage contains a Wi-Fi password. '
    'No: ranking chooses candidates from the available set, even when none supports the question. '
    'The model must inspect the returned text; humans must inspect factual claims and citations. '
    'We deliberately do not turn one convenient score threshold into a universal truth detector.'))

# 83-95: provenance, extraction, retriever tool and bounded context.
S.append(diagram('PDF, chunks, vectors: keep the source.', F.ingestion(),
    f'83-84 minutes. Official source {HANDBOOK}. Verified11November: Student Handbook for Taught '
    'Programmes2026/27, Academic Registry, PDF modified10November,137PDF pages,7,809,020bytes, SHA256 '
    '43ac3a6a7697b2ce78f1964f673dae0aa2ccf79ba7c58fb310b469dc2b380a1b. '
    'Six short whitespace-normalized extracts from PDF positions20,25,76. PDF20 is printed9; '
    'PDF25 printed14; PDF76 printed61. The full PDF is downloaded only into ignored output. '
    'Preparation verifies each extract against pdftotext for its page; class inspects the small bundle.'))
S.append(content('SOURCE / inspect the citation', 'Read the source.', [
    '[Official handbook, PDF page 20](%s#page=20).' % HANDBOOK,
    'Apply for a replacement online; a fee is charged.',
    'If the original is found, return it for cancellation.',
], body_size=44,
    notes='84-86 minutes. Open the actual PDF at page20, compare the chunk and read neighbouring '
    'text. Chunk ID hb2026-p020-replacement; printed page9. The source says the fee is non-refundable '
    'and non-transferable and possessing multiple cards for the same programme is an offence. '
    'The amount comes from the separate fee row on PDF76, not from this paragraph. These are '
    'teaching extracts, not institutional advice or the whole handbook; direct students to the '
    'current official source for actual decisions.'))
S.append(code_panel('QDRANT / API over the same learned vectors', 'Store, query, inspect', [
    'docker compose up -d qdrant',
    'uv run python qdrant_index.py seed',
    'uv run python qdrant_index.py query',
    '# Open http://127.0.0.1:6333/dashboard',
], lang=None, caption='Run from pfad/week10; Docker and the image are prepared before class.',
    notes='86-89 minutes. Inspect three real fixture queries against Qdrant, comparing the same '
    'rankings as the in-process reference. Read the payload: source ID, page, section, original '
    'text. Six points, 384 dimensions, Cosine distance. A named Docker volume persists vectors; '
    'restart the service then query without reseeding. Don’t use down -v. Content-addressed '
    'collections prevent a changed encoder/corpus silently overwriting another set. Missing '
    'server or unseeded collection fails visibly. No Docker? Pair with the prepared tutor; '
    'handbook.py is explicitly an in-process fallback, not evidence of a Qdrant API call.'))
S.append(content('QDRANT / connect the dashboard to HTTP', 'Store vectors. Query vectors.', [
    'PUT collection: define 384D vectors and Cosine distance.',
    'PUT points: store vectors with passage metadata.',
    'POST points/query: send a vector; get ranked passages.',
], body_size=43,
    notes='89-91 minutes. Open the dashboard and select the printed collection; inspect a point '
    'and its original text. The point UUID identifies a stored point; payload id identifies a '
    'citation. GET /collections lists collections. Python uses POST '
    '/collections/NAME/points/query with query, limit=2 and with_payload=true. The matching '
    'MiniLM encoder embeds text before Qdrant receives it; Qdrant does not do that in this example. '
    'The dashboard and Python talk to the same server. Keep source headings/table units and '
    'exceptions: a chunk can lose context. Similarity is not a foreign key or a truth check. '
    'Official API: https://api.qdrant.tech/api-reference/search/query-points .'))
S.append(code_panel('TOOL / structured arguments', 'The model asks Python to search.', [
    '{', '  "name": "retrieve_handbook",',
    '  "arguments": {', '    "query": "student identity card replacement cost"',
    '  }', '}',
], lang=None, caption='A real model-composed query from the verified local run.',
    notes='91-93 minutes. A tool is a callable operation with structured arguments and results. '
    'The adapter requires retrieval on every turn; the model composes a standalone query using '
    'history. Python validates the query, encodes it and searches the index. This is the native '
    'tool-call route through Pip’s OpenAI-compatible local HTTP client, not an MCP server or a keyword script. The forced '
    'retrieval policy is deliberate; do not describe it as the model independently choosing '
    'whether evidence is necessary. Later weeks add creative application actions.'))
S.append(diagram('Ask, search, answer.', F.tool_loop(),
    '93-95 minutes. Trace actual data at every boundary. The first model call proposes the '
    'retrieval query. Python executes search and returns page/ID/text/score/source metadata. '
    'The answer phase has no tools and a constrained JSON schema: answer and source_ids. '
    'The model generates these values; the app formats bracketed IDs or the canonical refusal, '
    'validates allowed IDs and atomically saves. A JSON grammar constrains shape, not factual '
    'truth. The bounded dispatcher also rejects unknown tools, missing evidence and overlong loops.'))

# 95-115: integrated endpoint and evidence, including independent speech checks.
S.append(section('06 / PIP', 'Pip: memory\nand voice',
    'Combine history, evidence and speech.', bg=INK,
    notes='Transition at minute 95. Connect the prepared knowledge index and related '
    'saved history to the returning-user conversation and audible output.'))
S.append(code_panel('LIVE / prepared local machine', 'Type a question; inspect the answer', [
    'uv run --extra encoder --extra pip python -m streamlit run pip_app.py', '',
    'What should I do if I lose my student identity card?',
    'If I find the original later, should I keep both?',
], lang=None, caption='Keep LM Studio and Qdrant running; use Pip’s typed chat and audio widget.',
    notes=f'95-98 minutes. Follow {PFAD}/QDRANT-PIP.md. LM Studio is the familiar Week 6 '
    'server, normally loopback1234/v1; choose the exact loaded tool/JSON-capable model. Qdrant '
    'and encoder/Kokoro assets are prepared before class. Pip’s local_reply client carries the '
    'requests; Week 10’s bounded agent adds evidence and saved history. Type both questions in '
    'Streamlit, expand the real request/tool trace and listen to the Kokoro audio widget. '
    'Browser autoplay may require a click. A failed model or index must not save a turn. '
    'A speech failure retains the displayed saved answer. Pair if setup fails.'))
S.append(content('OBSERVED / supported answer', 'Two sources support one answer.', [
    'Submit the replacement application online.',
    'Replacement fee: HK$150.',
    'Found the original? Return it for cancellation.',
], body_size=48,
    notes='98-100 minutes. Recorded alternate CLI output on29October, not a fresh Pip result: Submit an online '
    'application for a replacement. A non-refundable fee of HK$150 will be charged. If the '
    'original card is found, return it to the Academic Registry for cancellation. Sources '
    '[hb2026-p020-replacement] [hb2026-p076-fees]. This slide is a recorded result for inspection; '
    'the terminal run is live. Open each passage and compare every claim. The app adds the '
    'bracket formatting from the source_ids actually generated by the model.'))
S.append(diagram('History helps explain the follow-up.', F.prompt(),
    '100-102 minutes. Expand the Pip trace or open out/pip-last-turn.json after the follow-up. '
    'Find the actual earlier pair, current question, tool call and returned evidence. The '
    'historical CLI recording demonstrates its own earlier run, not a fresh Pip response. '
    'History resolves references; it is not authoritative handbook policy.'))
S.append(code_panel('LIVE / a new Python process', 'Reopen the printed conversation ID', [
    '# Pip sidebar: same profile + printed conversation ID',
    '# Restart Streamlit; enter your actual saved ID.', '',
    '# Pip sidebar: profile Bo + conversation ID 0',
    '# ID 0 creates a separate conversation.',
], lang=None, caption='Restart the app; inspect the reloaded history in its trace.',
    notes='102-105 minutes. Record the app’s printed ID. Stop/restart Streamlit and use the '
    'same profile and ID in the sidebar; ID0 creates a new conversation. Show the prior pair '
    'entering the next model call. Select Bo and ID0; Ada’s prior turns must be absent. Select '
    'Ada’s ID under Bo and observe the ownership rejection. Local profiles are not auth.'))
S.append(statement('Ask: what is the\nWi-Fi password at\nthe campus cafeteria?', size=95,
    notes='105-107 minutes. This is unsupported by our six-extract corpus. The real model '
    'composes a retrieval query, receives nearest neighbours, then emits an empty source_ids list '
    'and no source IDs. The app displays I cannot answer from these sources. This is not a '
    'claim the entire university handbook lacks that fact; it is a claim about the evidence '
    'available to this answer. The model’s source selection can still be wrong; inspect sources.'))
S.append(diagram('Text, voice, playback.', F.speech(),
    '107-110 minutes. Week 6’s synthesise_onnx.synthesise_reply uses prepared Kokoro assets, '
    'after the successful two-row save. Inspect the browser audio widget, listen and stop '
    'playback. Synthesis and audible room playback are separate checks; autoplay may require '
    'a click. Speech failure retains the displayed saved turn. The recorded alternate eSpeak '
    'WAV is not evidence of live Kokoro. Typed input is core; Week 6 microphone is optional.'))
S.append(content('RECOVER / preserve the successful work', 'One component fails. What remains?', [
    'Missing index or model → no answer saved.',
    'Unsupported evidence → explicit refusal.',
    'Speech failure → answer and history remain.',
], body_size=46,
    notes='110-113 minutes. Stop Qdrant, ask a fictional question and inspect unchanged history; '
    'restart it then retry without reseeding. A missing model, incompatible tool response or '
    'unseeded collection gives a visible error before a new turn is saved. A Kokoro failure '
    'preserves a completed saved answer. The speech checkbox is an explicit text-only fallback. '
    'Keep out/pip.sqlite and the Qdrant named volume; the trace is temporary diagnostic data.'))
S.append(content('CHECK / explain the complete path', 'Follow one question through the system.', [
    'Which rows entered this model request?',
    'Which source text supports this claim?',
    'Which result proves save, synthesis and playback?',
], body_size=46,
    notes='113-115 minutes. Ask partners to trace user input, owner-scoped history query, tool '
    'query, same-space vector search, returned passage, structured model answer, citation '
    'validation, atomic save and speech. The knowledge index is shared; history is isolated; '
    'the prompt is temporary. Green protocol tests use explicit doubles and do not prove '
    'live model reasoning. The public prepared response trace is labelled recorded evidence.'))

# 115-120: recap the system students have now seen, then tutorial handoff.
S.append(diagram('Knowledge, history, prompt, audio.', F.four_states(),
    '115-117 minutes. Recap after seeing the system: shared handbook knowledge supplies '
    'evidence; owner-scoped conversation rows supply history; the prompt combines them '
    'for this turn; audio is an output. The vector index and relational database serve '
    'different queries. A saved trace is a diagnostic snapshot, not the memory database. '
    'Ask which state is shared, which belongs to a user and which is temporary.'))
S.append(content('PFAD / separate 120-minute tutorial', 'Run, change, check and recover.', [
    '[Complete tutorial and exact commands](%s/README.md).' % PFAD,
    '0-50: related rows, SQL, restart; prepared D1 API demo.',
    '50-60 break; 60-100 Qdrant API, Pip, memory and speech.',
    '100-120: tutor review and project support.',
], body_size=42,
    notes='117-119 minutes. The separate README has setup/recovery within0-10, model work10-30, '
    'query/index/update/restart/D1 demo30-50, break50-60, real vectors60-70, typed follow-up/speech70-90, '
    'reload/isolation/failure90-100 and tutor/project support100-120. Pair at minute10 if model '
    'setup is not ready. Tutor12November meetings use allocated slots. No ClassPoint login or '
    'new assessment upload is required. Quiz revision includes models/keys/queries, real vector '
    'retrieval, source support, history and tool boundaries, not dated news or model version trivia.'))
S.append(end('Keep evidence.\nKeep context.', 'Keep their jobs separate.',
    'PFAD / WEEK 10',
    notes='119-120 minutes. Four lifetimes: handbook knowledge, conversation history, current '
    'prompt and audio. Invite questions and optional project transfer: a save owner, an NPC '
    'conversation or a source-checking assistant. No AI feature is required in the group project. '
    'Policy remains40% of course,25/50/25 idea/code/execution; public sd5913-owned repository '
    'with teammate Write access; deadline6December2026 at23:59HKT. GitHub Projects recommended, '
    'equivalent accessible progress record valid. Canvas is the submission system.'))

attach_reports(S, Path(__file__).resolve().parent / 'week10-reports.json')
DECK = dict(title='SD5913 / Persistent objects and a talking handbook agent / Week 10',
            slides=finalize(S, 'SD5913 / WEEK 10 / 12 NOVEMBER 2026'), pdf='SD5913-week10.pdf')
