"""Persistent model classes and a source-backed, conversation-aware handbook bot."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen import Figure, INK, MUTED, Slide, T, WHITE, attach_reports
from deckgen.layouts import agenda, code_panel, content, end, section, statement, title, finalize
import week10_figures as F

S = []
EYE = 'SD5913 / WEEK 10 / 12 NOVEMBER 2026'
PFAD = 'https://github.com/sd5913/pfad/blob/c59fae0/week10'
HANDBOOK = ('https://www.polyu.edu.hk/ar/docdrive/polyu-students/student-handbook/'
            'Student_Handbook_2026-27_English.pdf')


def diagram(heading, figure, notes):
    svg, png = figure
    slide = Slide(bg=WHITE, notes=notes, title=heading)
    slide.chrome = False
    slide.els = [T(80, 76, 1760, 90, heading, 'xbold', 60, INK),
                 Figure(80, 190, 1760, 792, svg, png)]
    return slide


# 0-10: opening, current news and a precise system boundary.
S.append(title(EYE, 'What survives\na conversation?',
    'Persistent objects, handbook evidence and a spoken reply.', size=130,
    notes='0-2 minutes. A player returns to a game NPC and asks: what if I find the original later? '
    'A convincing voice is easy to mistake for reliable memory. Today we inspect one small system '
    'in enough detail to distinguish remembered conversation from handbook evidence. Week 7 classes, '
    'Week 8 verification and Week 9 request/process ideas are prerequisites; do not repeat constructors. '
    'Lecture120 minutes including a10-minute break; the PFAD tutorial is another120 minutes.'))
S.append(statement('A returning user asks:\n“What about the original?”', size=100,
    notes='2-4 minutes. Ask what the word original refers to. Without the preceding discussion it is '
    'ambiguous. In our later real example the user lost a student identity card. The assistant needs '
    'the previous conversation to understand the reference and current handbook passages to answer '
    'the policy question. Invite a game/app equivalent; do not promise every project needs an AI bot.'))
S.append(content('NEWS / CHECKED 29 OCTOBER', 'A save button is a behavior.', [
    '[Peewee 4.5.3 released 7 October 2026](https://github.com/coleifer/peewee/releases/tag/4.5.3).',
    'One fix: explicitly executing a write again must really execute it.',
    'Your save button runs twice. What should happen?',
], body_size=44,
    notes='4-6 minutes; news is outside quiz scope. The maintainer reports that explicitly executing '
    'a write query with RETURNING now runs the write again rather than reusing a cached result. '
    'Do not generalize this as every save duplicating rows, or require PostgreSQL/RETURNING knowledge. '
    'Primary release checked29October; current PyPI version4.5.3 verified. Our actual SQLite operations '
    'are tested, not every maintainer release-note claim. Ask whether a save creates a new slot or '
    'updates an existing slot: behavior follows the design, then needs a check.'))
S.append(diagram('Four kinds of state; four different jobs', F.four_states(),
    '6-8 minutes. Knowledge: the same attributed handbook chunks and learned vectors for everyone. '
    'History: owner/conversation-scoped user and assistant rows. Prompt: the temporary collection '
    'of rules/history/question/tool evidence sent for this turn. Audio: a generated output file, '
    'with independent playback. Source knowledge and conversation history both persist, but answer '
    'different questions. A trace JSON is a diagnostic snapshot, not the memory database.'))
S.append(agenda(EYE, ['Models become related rows', 'Keys, exact queries and restart',
    '10-minute break', 'Real handbook vectors and retrieval', 'History, tools and spoken answers',
    'PFAD: trace, change, check, recover'],
    notes='8-10 minutes. Exact timing:10-25 model-to-row;25-40 relations/keys/index;40-60 persistence '
    'experiment;60-70 break;70-80 embeddings;80-95 handbook/tool retrieval;95-115 integrated typed '
    'conversation, reload/isolation and speech;115-120 comparison/handoff. Explain that the application '
    'requires retrieval, while the local model composes the query and judges source support. This '
    'bounded tool workflow is a step toward next week’s application tools, not an autonomous agent demo.'))

# 10-25: use classes to explain persistent domain models.
S.append(section('1 / MODEL TO ROW', 'An object can\nleave a record.',
    'Values persist. Python methods remain code.', bg=INK,
    notes='10-12 minutes. Reuse existing class knowledge. A model is a Python class mapped to a '
    'database table. An instance represents one row, with a stable stored primary key. The ORM '
    'is a library that maps class operations to database queries; the database still enforces '
    'constraints. Avoid saying the whole object or its methods are saved.'))
S.append(code_panel('PFAD / models.py', 'Three models, one conversation system', [
    'class User(Record):', '    name = TextField(unique=True)', '',
    'class Conversation(Record):',
    '    owner = ForeignKeyField(User)', '    title = TextField()', '',
    'class Message(Record):',
    '    conversation = ForeignKeyField(Conversation)',
    '    role = TextField()', '    content = TextField()',
], caption='Excerpt: the complete file also defines the database and constraints.',
    notes=f'12-15 minutes. Read {PFAD}/models.py. Record inherits Peewee Model, then these classes '
    'inherit Record. The full file names backrefs, deletion behavior, checks and indexes. This '
    'display is a class-definition excerpt, not a complete standalone program. Each model gets '
    'an automatic integer primary key. Ask which field expresses ownership and which attaches '
    'a message to its conversation. A role is user or assistant here, not a student role.'))
S.append(code_panel('PFAD / inherited methods', 'The method call becomes a write', [
    'store = Store("out/chat.sqlite")',
    'ada = User.create(name="Ada")',
    'chat = Conversation.create(owner=ada, title="Handbook")',
    'print(chat.id, chat.owner_id)', '',
    'chat.title = "My game questions"',
    'chat.save()',
], caption='Excerpt: imports and cleanup are in storage_demo.py.',
    notes='15-18 minutes. .create() and .save() are real inherited ORM methods. Trace the Python '
    'call to INSERT or UPDATE, affected row, and later SELECT. The generated stored ID is not '
    'Python id(chat), a memory address or the title. A title can change while identity remains. '
    'Use the complete storage_demo.py rather than retyping a partial snippet into the wrong folder. '
    'Prediction: remove only chat.save(); what would a new process see?'))
S.append(diagram('One instance maps to one stored row', F.mapping(),
    '18-21 minutes. IDs in this explanatory figure are fictional example values, not fixed output '
    'requirements. The Python object has attributes; the conversation table stores selected fields. '
    '.save() sends an UPDATE; a query reconstructs a new instance from the result. A foreign-key '
    'attribute has an owner_id value even when reading chat.owner can load a related User. '
    'The method implementations remain in Python/Peewee, not in the SQLite row.'))
S.append(statement('Predict:\nchange chat.title\nwithout chat.save().', size=105,
    notes='21-23 minutes. Pairs predict whether a separate inspection process sees the change. '
    'Expected: no, because an attribute assignment alone changes the live object. Then restore '
    '.save() and compare. Ask a student to name the stored value and the operation that changes it. '
    'Do not confuse a pending database transaction with an unsaved Python attribute.'))
S.append(diagram('Close one process. Reconstruct in another.', F.restart(),
    '23-25 minutes. Run storage_demo.py rename, let the process exit, then run inspect. The '
    'same primary key and new title are read in a new Python process. The old object no longer '
    'exists. Methods work because the new process imports the class code. This is stronger '
    'evidence than printing the original object again in one notebook cell.'))

# 25-40: relations, exact queries, ordinary indexes and modelling transfer.
S.append(diagram('Who owns this conversation and these messages?', F.relations(),
    '25-28 minutes. User1 owns Conversation3; Message7 refers to Conversation3. One user can '
    'have many conversations; one conversation many messages. Example IDs illustrate the schema, '
    'not an expected sequence in a reused database. Ask which field would change if another '
    'message is added versus another conversation. References point to IDs, not duplicated parents.'))
S.append(diagram('Identity, reference and lookup index', F.keys(),
    '28-31 minutes. PK: identifies a message row. FK: references an existing conversation when '
    'foreign_keys is enabled. Ordinary compound index: helps find/order rows for a conversation. '
    'Indexes store extra lookup structure and incur write/storage cost. A foreign-key column can '
    'also be indexed: these jobs can coexist. This lookup index is different from a semantic '
    'vector index. No claim of measured speedup is made for our tiny dataset.'))
S.append(code_panel('PFAD / Store.history_query()', 'Ask an exact, scoped question', [
    'self.owned_conversation(owner_id, conversation_id)',
    'return (Message.select()',
    '    .where(Message.conversation == conversation_id)',
    '    .order_by(Message.id))',
], caption='Method-body excerpt: ownership is checked before messages are queried.',
    notes='31-33 minutes. Read models.py history_query. The owner check first loads the selected '
    'conversation and compares owner_id; a missing conversation or wrong owner is rejected. '
    'The SELECT then matches one conversation exactly and orders by stable insertion ID. Fictional '
    'local profile names are not authenticated accounts; do not claim this is secure login. '
    'Think of a game with multiple save slots: choose the right owner and slot before loading.'))
S.append(code_panel('SAME QUERY / SQL shape', 'Python does not hide the query', [
    'SELECT id, conversation_id, role, content',
    'FROM message',
    'WHERE conversation_id = ?',
    'ORDER BY id;',
], lang=None, caption='Simplified SQL shape. The real ORM trace prints aliases and bound values.',
    notes='33-35 minutes. storage_demo.py inspect prints the actual Peewee-generated SELECT and '
    'parameter list. This slide simplifies aliases/quoting while keeping meaning. The question '
    'mark is a bound parameter; the ID is a value, not pasted SQL text. Ask why matching a title '
    'is weaker than selecting a stable ID. The database evaluates the query; Python reconstructs '
    'instances from returned rows.'))
S.append(content('TRANSFER / model the relation', 'Which records would you connect?', [
    'User → SaveFile: one owner, many saves.',
    'User → Membership ← Team: a joining record.',
    'Message → Message: a reply-to reference.',
], body_size=46,
    notes='35-38 minutes. Retains historical Week10 cardinality drills without building three '
    'more apps. Ask pairs to choose IDs for a SaveFile owner, then explain why a membership can '
    'have its own joined_at or role. A reply-to field is optional and self-referential. A foreign '
    'key enforces existence, not every business rule or absence of cycles. No auth/password app '
    'is introduced; the historical unsafe bare password hashing is not reused.'))
S.append(statement('A reference to\nconversation 999999:\nwhat must happen?', size=100,
    notes='38-40 minutes. Predict the failure before storage_demo.py invalid. On this demo database '
    'that ID is absent, so the enforced foreign key rejects the insert. Name the boundary: '
    'a database constraint prevents an orphan message. This does not prove a user is authorized '
    'to read an otherwise valid conversation; that is the separate ownership check.'))

# 40-60: real terminal experiment and inspected failure/recovery.
S.append(code_panel('LIVE / terminal in pfad/week10', 'Create, inspect, update, reload', [
    'uv run python storage_demo.py seed',
    'uv run python storage_demo.py inspect',
    'uv run python storage_demo.py rename',
    'uv run python storage_demo.py inspect',
    'uv run python storage_demo.py invalid',
], lang=None, caption='Every command starts a fresh Python process.',
    notes='40-43 minutes. Use a prepared disposable SQLite file. Seed prints IDs and adds two '
    'prepared storage messages, explicitly not model-generated answers. Inspect prints rows, '
    'SQL/parameters, reconstructed history and index names. Rename changes the title while '
    'retaining its ID. Invalid shows the FK error. A reused file may have different IDs and '
    'seed behavior after a rename; do not promise every run prints1. See README recovery.'))
S.append(code_panel('LIVE / inspect the result', 'Rows become message dictionaries', [
    'history = store.history(ada.id, chat.id)',
    'print(history)',
    '# [{"role": "user", "content": "..."},',
    '#  {"role": "assistant", "content": "..."}]',
], caption='Shape excerpt. Read the actual saved content in the terminal.',
    notes='43-45 minutes. Each row contains conversation ID, role and content. The returned '
    'ordered dictionaries are the format used in model requests later. Ask why losing order '
    'changes meaning. Do not present the ellipsis as real handbook evidence or a live generated '
    'reply. The seed says prepared storage example; no model was called.'))
S.append(content('BOUNDARIES / three rejected writes', 'A failed write should tell you why.', [
    'Missing parent → reject the orphan.',
    'Role outside user / assistant → reject.',
    'Empty answer → roll back the whole turn.',
], body_size=46,
    notes='45-48 minutes. The real Store tests cover these constraints. foreign_keys pragma is '
    'explicitly enabled; SQLite does not enforce FKs by default. Message role/nonempty checks '
    'live in the schema. append_turn uses db.atomic; an assistant insert failure rolls back '
    'the preceding user insert. Check rows after the failure, not only the error message.'))
S.append(code_panel('PFAD / Store.append_turn()', 'Save one complete turn atomically', [
    'with self.db.atomic():',
    '    self.owned_conversation(owner_id, conversation_id)',
    '    Message.create(conversation=conversation_id,',
    '                   role="user", content=question)',
    '    Message.create(conversation=conversation_id,',
    '                   role="assistant", content=answer)',
], caption='Method-body excerpt: both rows commit together or neither does.',
    notes='48-51 minutes. Walk a successful user insert followed by a rejected empty assistant '
    'insert. A transaction groups these operations so history has no half-turn. The classroom '
    'CLI assumes one active writer; this is not a full multi-client production service. '
    'A database transaction does not make an external model request atomic with a disk write. '
    'The model completes and validates before append_turn is called.'))
S.append(statement('Check the rows\nafter the error.\nWhat survived?', size=105,
    notes='51-54 minutes. Give pairs a minute: list whether the user row, assistant row and '
    'previous older turns survive. In the failed two-row transaction neither new row persists; '
    'previous committed rows remain. Run the actual behavior checks or inspect a disposable '
    'database. Do not delete students’ work to reset this experiment.'))
S.append(content('HISTORY POLICY / a deliberate limit', 'Keep four complete turns in context.', [
    'Select the newest eight message rows.',
    'Restore chronological order for the model.',
    'Older rows remain saved in SQLite.',
], body_size=46,
    notes='54-57 minutes. history() sorts descending, limits turns*2, then reverses that window. '
    'append_turn guarantees complete pairs for this single-writer path. The policy prevents '
    'unbounded prompt growth but is not unlimited memory or a summary. Students can change '
    'four to two in Bot, compare the next prompt and explain which rows still exist on disk. '
    'A conversation ID alone does not send any history.'))
S.append(content('CHECK / predict, inspect, recover', 'Explain a restart to a partner.', [
    'Name one model method and its SQL action.',
    'Find the same ID in a fresh process.',
    'Show an invalid write and the unchanged rows.',
], body_size=46,
    notes='57-60 minutes. Pause for explanations rather than more vocabulary. Ask a student to '
    'point to .save(), the SQL UPDATE, the stored title and a fresh loaded instance. Another '
    'distinguishes primary key, FK and ordinary index. Recover by restoring the one title edit; '
    'keep disposable files separate. This completes the first-half acceptance, not the bot.'))
S.append(section('60-70 / BREAK', '10-minute break',
    'Next: what can the handbook actually support?', bg=INK,
    notes='60-70 minutes. Ten-minute break inside the120-minute lecture. Keep the inspected '
    'database and source available. Before resuming, verify the prepared local model is healthy '
    'on127.0.0.1:11440; no remote class, paid API or automatic model download is involved.'))

# 70-80: learned representations and honest numerical evidence.
S.append(section('2 / REPRESENTATION', 'Similar meaning,\ndifferent words.',
    'Learned vectors are useful features, not policy fields.', bg=INK,
    notes='70-72 minutes. Historical word2vec represented words and supported neighbour/analogy '
    'experiments. Sentence encoders represent longer text. Reuse the intuition that learned '
    'features put related language closer, without claiming individual dimensions have named '
    'meanings or that similarity is truth. No large fastText download, Orange or t-SNE practical '
    'is required; Orange was deliberately removed to make room for creative applications.'))
S.append(code_panel('REAL / MiniLM handbook fixture', 'A passage becomes 384 numbers', [
    '# Source: hb2026-p020-replacement, PDF page 20',
    '# vector[:8] from the supplied real learned fixture:',
    '-0.060211, 0.055605, 0.027168, -0.040987, 0.053495, -0.023228, 0.058877, -0.033763', '',
    '# Full vector: 384 values, L2 normalized',
    '# Same pinned encoder is used for every new question.',
], caption='The full vector, passage and encoder revision travel together in handbook.json.',
    notes=f'72-74 minutes. Read {PFAD}/fixtures/handbook.json and run uv run python handbook.py. '
    'These displayed numbers are copied from the genuine generated fixture, not made-up coordinates. '
    'MiniLM revision1110a243fdf4706b3f48f1d95db1a4f5529b4d41, masked-mean pooling,384 dimensions, '
    'normalization and256-token maximum. This is a sentence-transformer trained on text, replacing '
    'the earlier short-context CLIP feasibility candidate. The index stores text/page/source identity too.'))
S.append(diagram('Embed the question in the same space', F.search(),
    '74-76 minutes. Documents and questions use the same pinned MiniLM snapshot and normalization. '
    'Matching384 dimensions alone is insufficient: two unrelated encoders can both emit384 numbers. '
    'Our code compares the full encoder identity and rejects a mismatch; the constructor loads '
    'the pinned public revision locally. Input longer than256 tokens is rejected rather than '
    'silently truncated. New question input needs the actual encoder, not a keyword substitute.'))
S.append(diagram('A measured ranking from real handbook vectors', F.ranking(),
    '76-78 minutes. The exact prepared fee question ranks the fee row0.892566 and replacement '
    'rule0.737337. These are observed cosine similarities from the shipped vector fixture. '
    'A long noisy fee-table extract initially missed the desired top two; the revised exact row '
    'extract improves this question. This is a measured result for one question, not a benchmark '
    'or proof all policy questions work. Keep the HK$ table heading in section metadata.'))
S.append(statement('An unrelated question\nstill has a\nnearest neighbour.', size=100,
    notes='78-80 minutes. Ask whether a high-ish score proves the passage contains a Wi-Fi password. '
    'No: ranking chooses candidates from the available set, even when none supports the question. '
    'The model must inspect the returned text; humans must inspect factual claims and citations. '
    'We deliberately do not turn one convenient score threshold into a universal truth detector.'))

# 80-95: provenance, extraction, retriever tool and bounded context.
S.append(diagram('From the current official PDF to cited vectors', F.ingestion(),
    f'80-82 minutes. Official source {HANDBOOK}. Verified29October: Student Handbook for Taught '
    'Programmes2026/27, Academic Registry, July2026,137PDF pages,7,658,316bytes, SHA256 '
    '108956feb2ffac665f8ca0f5a8f68d7150a85fda15e219916785ec50331a4e94. '
    'Six short whitespace-normalized extracts from PDF positions20,25,76. PDF20 is printed9; '
    'PDF25 printed14; PDF76 printed61. The full PDF is downloaded only into ignored output. '
    'Preparation verifies each extract against pdftotext for its page; class inspects the small bundle.'))
S.append(content('SOURCE / inspect the citation', 'Lost card: what does the source say?', [
    '[Official handbook, PDF page 20](%s#page=20).' % HANDBOOK,
    'Apply for a replacement online; a fee is charged.',
    'If the original is found, return it for cancellation.',
], body_size=44,
    notes='82-84 minutes. Open the actual PDF at page20, compare the chunk and read neighbouring '
    'text. Chunk ID hb2026-p020-replacement; printed page9. The source says the fee is non-refundable '
    'and non-transferable and possessing multiple cards for the same programme is an offence. '
    'The amount comes from the separate fee row on PDF76, not from this paragraph. These are '
    'teaching extracts, not institutional advice or the whole handbook; direct students to the '
    'current official source for actual decisions.'))
S.append(code_panel('LIVE / no model download needed', 'Inspect the prepared search', [
    'uv run python handbook.py', '',
    '# Inspect: source URL / hash / PDF page / chunk ID',
    '# Query 1: lost student identity card',
    '# Query 2: requesting leave from class',
    '# Query 3: replacement fee',
], lang=None, caption='The fixture supplies real vectors for three exact prepared questions.',
    notes='84-87 minutes. Run the command from pfad/week10. Read the three exact question strings '
    'printed by the program; the comment labels on this slide abbreviate their topics. Lost-card '
    'first result is replacement; leave is the leave section; fee is the row on PDF76. Inspect '
    'scores and text, not only the order. Fixture mode supports only the exact stored question '
    'vectors; arbitrary typed questions need Encoder. A missing or unknown query fails visibly.'))
S.append(content('CHUNKING / what can disappear?', 'A short extract can lose context.', [
    'Keep source ID, page and section with the text.',
    'Check headings, table columns and exceptions.',
    'Rebuild both passage and query vectors after encoder changes.',
], body_size=45,
    notes='87-89 minutes. The fee row uses HK$ from its table heading, retained in section metadata. '
    'The leave form table had two columns; naive flattening made the location unclear, so the '
    'prepared extracts retain unambiguous prose and separate the decision paragraph. Do not '
    'invent the missing column relationship. Show actual neighbouring PDF text. A changed chunk '
    'needs a new vector; a changed encoder requires all stored and query vectors to be rebuilt.'))
S.append(code_panel('TOOL / structured arguments', 'Expose retrieval as a capability', [
    '{', '  "name": "retrieve_handbook",',
    '  "arguments": {', '    "query": "student identity card replacement cost"',
    '  }', '}',
], lang=None, caption='A real model-composed query from the verified local run.',
    notes='89-92 minutes. A tool is a callable operation with structured arguments and results. '
    'The adapter requires retrieval on every turn; the model composes a standalone query using '
    'history. Python validates the query, encodes it and searches the index. This is the native '
    'tool-call route of local llama.cpp, not an MCP server or a keyword script. The forced '
    'retrieval policy is deliberate; do not describe it as the model independently choosing '
    'whether evidence is necessary. Later weeks add creative application actions.'))
S.append(diagram('Model request → tool result → inspected answer', F.tool_loop(),
    '92-95 minutes. Trace actual data at every boundary. The first model call proposes the '
    'retrieval query. Python executes search and returns page/ID/text/score/source metadata. '
    'The answer phase has no tools and a constrained JSON schema: answer and source_ids. '
    'The model generates these values; the app formats bracketed IDs or the canonical refusal, '
    'validates allowed IDs and atomically saves. A JSON grammar constrains shape, not factual '
    'truth. The bounded dispatcher also rejects unknown tools, missing evidence and overlong loops.'))

# 95-115: integrated endpoint and evidence, including independent speech checks.
S.append(code_panel('LIVE / prepared local machine', 'Type a question; inspect the answer', [
    'uv run --extra encoder python bot.py', '',
    'What should I do if I lose my student identity card?',
    'If I find the original later, should I keep both?',
], lang=None, caption='Terminal 1 runs the prepared model server; terminal 2 runs the bot.',
    notes=f'95-98 minutes. Setup/server commands are in {PFAD}/REHEARSAL.md; all public weights '
    'are prepared before class. Loopback port11440, CPU-only Qwen3.5-2B Q4_K_M, no paid model API. '
    'The CLI prints the user/conversation ID, trace and answer, then synthesizes and plays it. '
    'Type the two questions in sequence. An empty line exits; Ctrl+C during speech stops the player. '
    'If setup fails, pair with a prepared machine; trace replay is explicitly a fallback, not live proof.'))
S.append(content('OBSERVED / supported answer', 'Two sources support one answer.', [
    'Submit the replacement application online.',
    'Replacement fee: HK$150.',
    'Found the original? Return it for cancellation.',
], body_size=48,
    notes='98-100 minutes. Actual verified Qwen3.5-2B output on29October: Submit an online '
    'application for a replacement. A non-refundable fee of HK$150 will be charged. If the '
    'original card is found, return it to the Academic Registry for cancellation. Sources '
    '[hb2026-p020-replacement] [hb2026-p076-fees]. This slide is a recorded result for inspection; '
    'the terminal run is live. Open each passage and compare every claim. The app adds the '
    'bracket formatting from the source_ids actually generated by the model.'))
S.append(diagram('The follow-up receives selected conversation history', F.prompt(),
    '100-102 minutes. Open out/last-turn.json after the follow-up. It contains the actual user '
    'and assistant pair, the current question, model tool call and returned evidence. The '
    'reopened real run composed return original card if found and answered to return/cancel '
    'rather than keep both. Do not substitute the conversation number for this evidence. '
    'History resolves the reference; it is not authoritative policy. The diagram is a readable '
    'summary, with exact serialized content available in the trace.'))
S.append(code_panel('LIVE / a new Python process', 'Reopen the printed conversation ID', [
    'uv run --extra encoder python bot.py --conversation 1',
    '# Replace 1 with the ID printed by your own first run.', '',
    'uv run --extra encoder python bot.py --user Bo',
    '# Omitting --conversation creates a separate conversation.',
], lang=None, caption='Use a fresh terminal process and inspect its selected history.',
    notes='102-105 minutes. The1 is an example for a fresh file, not a universal ID. The actual '
    'rehearsal reopened a saved conversation in a new process, included the earlier pair and '
    'resolved a vague follow-up. Bo’s separate conversation starts without Ada’s prior turns. '
    'Ask a specific leave question and compare prompts; a correct answer alone does not prove '
    'isolation. Wrong-owner --user Bo --conversation AdaID is rejected. Missing IDs now give '
    'a recoverable error; names in this local app are profiles, not authentication.'))
S.append(statement('Ask: what is the\nWi-Fi password at\nthe campus cafeteria?', size=95,
    notes='105-107 minutes. This is unsupported by our six-extract corpus. The real model '
    'composes a retrieval query, receives nearest neighbours, then emits an empty source_ids list '
    'and no source IDs. The app displays I cannot answer from these sources. This is not a '
    'claim the entire university handbook lacks that fact; it is a claim about the evidence '
    'available to this answer. The model’s source selection can still be wrong; inspect sources.'))
S.append(diagram('Displayed, synthesized and heard are separate checks', F.speech(),
    '107-110 minutes. Real eSpeak NG synthesis runs after the successful two-row save. The '
    'prepared machine verified a PCM22050Hz mono WAV from the actual cited answer and ffplay '
    'completion. A longer live speech test was stopped with Ctrl+C and the player exited. '
    'Physical intelligibility, room speakers and volume still need a listener at class preflight. '
    'The supplied prerecorded refusal WAV is only a fallback; it does not prove live retrieval '
    'or memory. Typed input is core; microphone recognition is optional Week6 reuse.'))
S.append(content('RECOVER / preserve the successful work', 'One component fails. What remains?', [
    'Missing index or model → no answer saved.',
    'Unsupported evidence → explicit refusal.',
    'Speech failure → answer and history remain.',
], body_size=46,
    notes='110-113 minutes. Show --bundle out/missing.json: visible missing-index error. Stop the '
    'prepared local model only when needed, retry, inspect unchanged message count, then restart. '
    'Speech-only invalid text fails visibly; a playback device failure reports SPEECH FAILED '
    'while retaining the saved displayed answer. The prepared audio is not a silent substitute. '
    'A player exit code alone can be misleading: the code also checks the file exists before '
    'starting ffplay; a tested missing-file regression originally returned player success.'))
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

# 115-120: compare storage by the needed retrieval, then tutorial handoff.
S.append(content('STORAGE / choose by the question', 'Different questions need different structures.', [
    'Related rows: whose ordered conversation is this?',
    'Nested save document: what is the whole scene state?',
    'Vectors + metadata: which passages resemble this query?',
], body_size=44,
    notes='115-117 minutes. Preserve the historical relational/document/vector comparison without '
    'a second database installation. JSON is a representation, not the absence of schema. '
    'Document stores can validate schemas and relational systems can store nested data. Rows '
    'are useful for ownership/joins/constraints; nested data for restoring a coherent document; '
    'vectors for semantic candidates that still need source checking. No representation wins '
    'every access pattern. Ordinary B-tree lookup and semantic vector ranking are different.'))
S.append(content('PFAD / separate 120-minute tutorial', 'Run, change, check and recover.', [
    '[Complete tutorial and exact commands](%s/README.md).' % PFAD,
    '0-50: models, rows, exact queries and restart.',
    '50-60 break; 60-100 retrieval, memory and speech.',
    '100-120: tutor review and project support.',
], body_size=42,
    notes='117-119 minutes. The separate README has setup/recovery within0-10, model work10-30, '
    'query/index/update/restart30-50, break50-60, real vectors60-70, typed follow-up/speech70-90, '
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
