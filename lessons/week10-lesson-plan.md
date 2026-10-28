# Week 10: persistent objects and a talking handbook agent

**Thursday 12 November 2026. 120-minute lecture, followed by a separate
120-minute PFAD tutorial.** The approved scope supersedes the earlier JSON-only
outline. The incumbent deck is deliberately preserved pending feasibility;
its artwork/optional-retrieval narrative is **not the approved replacement**.
Do not present that deck as this run sheet or mark this lesson ready.

## Production gate

The SQLite/Peewee User/Conversation/Message path and bounded tool/memory plumbing
are implemented and tested. Real cached CLIP text inference and eSpeak NG WAV
synthesis work independently. The instructor supplied the exact current
[2026-27 handbook URL](https://www.polyu.edu.hk/ar/docdrive/polyu-students/student-handbook/Student_Handbook_2026-27_English.pdf),
but this production host cannot resolve it. There is no verified extracted
handbook bundle or live local chat model. Playback was denied by the environment.
The required source-supported/unsupported answers, contextual follow-up,
fresh-process live recall, isolation and heard/stopped spoken reply therefore
remain **core feasibility gaps**, not merely final classroom rehearsal.

The companion implementation and tutorial are reviewable in [PFAD PR #13](https://github.com/sd5913/pfad/pull/13),
with the [current source pinned](https://github.com/sd5913/pfad/tree/adaf624/week10).
Refresh this link to the independently reviewed commit before replacement slides are built. Do not write a long
replacement deck around an unproven endpoint. Do not substitute keyword search,
invented vectors, an unused thread ID, scripted model outputs or prerecorded
speech for these gates. The physical playback check is separate from the model
and index checks.

## Exact lecture run sheet

| Minutes | Teaching sequence | Demonstration / student observation |
| --- | --- | --- |
| 0-10 | Opening, short dated news, four kinds of state | Which parts of a talking handbook bot survive closing Python? Separate knowledge, history, prompt and audio. |
| 10-25 | User/Conversation/Message; model, instance, stable ID, row | Read the actual Peewee class beside one instance and its stored row. Inherited methods issue SQL; method bodies are not stored. |
| 25-40 | Relations, exact queries, keys/indexes, cardinality | Trace one user to conversations to messages; compare PK, FK and ordinary index. Brief User/SaveFile, Membership/Team and reply-to-message drills. |
| 40-60 | ORM -> SQL -> rows -> loaded history | Seed, inspect, update, restart; reject orphan/invalid role; explain atomic user/assistant write and rollback. |
| 60-70 | Break | Keep the inspected source and database available. |
| 70-80 | Learned representations, dimensions and similarity | Brief word-neighbour intuition; inspect a real cited handbook vector and a compatible query. No arbitrary coordinate cartoon presented as data. |
| 80-95 | PDF -> chunks -> index -> retriever TOOL | Bounded prepared ingestion/search trace; two queries; inspect actual cited PDF sections and unsupported question. |
| 95-115 | Typed conversation, memory, reopen/isolation, speech | Actual model chooses retrieval; tool result reaches model; next call receives retained history; fresh process reload; independent conversation; synthesis/playback/stop/failure. |
| 115-120 | Storage comparison and handoff | Related bot rows, nested scene/save document, semantic vectors; recap four lifetimes and exact PFAD commands. |

### 0-10: opening and news

Begin with a concrete creative-design scenario: a player returns to a game NPC,
asks "what about that rule?", and expects the previous conversation to matter.
The bot needs both current handbook knowledge and the player's particular
history; a nice voice does not prove either is correct.

Use at most two minutes for the verified [Peewee 4.5.3 release](https://github.com/coleifer/peewee/releases/tag/4.5.3),
published **7 October 2026**, checked **29 October**. One concrete release-note
claim: explicitly executing a write query with `RETURNING` now executes again,
rather than reusing a cached result. Ask: if a save button runs twice, what
should happen? This is a current maintenance story about observable state, not
a demand to memorize `RETURNING` or PostgreSQL. We tested the actual version's
SQLite path; we did not independently reproduce every release-note fix. Keep
news outside quiz scope and update it near class only from a checked source.

Draw four distinct destinations, not one "memory" box: versioned handbook
chunks/vectors; user-owned messages in SQLite; the assembled request for one
model call; synthesized audio output. Ask students which survive a restart and
which are personalized. The exercise trace snapshot is a diagnostic artifact,
not the authoritative memory store.

### 10-25: the class-to-row mapping

Use PFAD `week10/models.py` throughout. Show `class User(Record)` and its `name`
field, then `Conversation.owner = ForeignKeyField(User)` and
`Message.conversation = ForeignKeyField(Conversation)`. `Record` inherits the
real ORM's `Model`, which supplies `.create()`, `.save()` and queries. Avoid a
repeat of Week 7's two-ball constructor lesson. Trace one instance's stable ID
to the row; a new process reconstructs another Python object with that same ID.

Prediction: change `chat.title` without calling `.save()`; does SQLite change?
Run the actual `.save()` version, then a separate inspect process. Point to SQL
and bound parameters; do not claim Python's in-memory `id()` is the primary key.
The database stores values and references, not methods or an entire process.

### 25-40: relationships and indexes

Spend six minutes on User -> Conversation -> Message and the precise question
"which messages belong to this user's selected conversation, in order?"
Ownership is checked before the message query. Explain the single local CLI
writer assumption and fictional profiles: this is not an authentication service.

Use six minutes for PK/FK/index. PK identifies a row; FK stores a reference and
can enforce existence; an ordinary index helps find/order matching rows. Show
SQLite's `(conversation_id, id)` index and its storage/write cost. It is neither
a relational relationship nor the handbook's embedding index.

Use three minutes for cardinality predictions: User/SaveFile one-to-many;
User/Team many-to-many via Membership; Message.reply_to self-reference. Do not
build another app. A membership record can have attributes of its own, such as
joined time; the relationship is modelled, not inferred from matching names.

### 40-60: the whole persistence experiment

From PFAD `week10`, run:

```bash
uv run python storage_demo.py seed
uv run python storage_demo.py inspect
uv run python storage_demo.py rename
uv run python storage_demo.py inspect
uv run python storage_demo.py invalid
```

Each invocation is a fresh process. On a new `out/chat.sqlite`, expect one
fictional Ada, one conversation and two prepared messages. The seed assistant
is explicitly a storage example, not a live model response. Rename keeps the
same ID; invalid parent ID fails. The first inspect prints SQL/parameters,
rows, reconstructed message dictionaries and ordinary index names.

Budget five minutes for the update/prediction, five for restart evidence, five
for rejected role/reference/empty-content checks and five for atomicity/history
window. `append_turn()` uses a transaction: if assistant insert fails, the user
insert rolls back too. A failed retrieval/model answer writes no turn.
History retains four complete pairs in each next prompt; older rows remain in
SQLite. Students change the window and inspect the actual serialized request.
Prepared unit-test doubles prove plumbing, not a model's contextual recall.

### 70-95: the real handbook representation

Preparation must fetch the instructor's official PDF and confirm title/year,
SHA-256 and PDF-page/printed-page correspondence. Select short useful passages;
keep full extraction/indexing out of class. Run the bounded prepared command
`uv run python handbook.py` to print provenance, real numeric vectors and two
ranked results. Its prepared queries require exact question strings; arbitrary
new input needs the same live encoder. No keyword substitute is implemented.

Teach learned vectors as many numeric features useful for comparing text, not
human-readable policy fields. Similarity is approximate; unknown questions
still have nearest neighbours. Same dimension is insufficient: name, actual
weights, tokenizer, pooling and normalization define compatibility. The local
CLIP feasibility encoder is limited to 77 tokens and was trained for
image/text relationships; its usefulness for the selected handbook questions
must be measured. Short chunks may cut a qualification; inspect neighbouring
text and the full cited section. Do not manufacture a correct result to fit it.

Expose the actual retriever tool request and result before the model answer.
A tool is a callable capability with structured arguments/results. Here it
returns passage ID, PDF page, text, score and source metadata. It does not
return policy truth or change the model's weights. This is the bridge from
retrieval to a tool-using agent, not another MCP permissions lecture.

### 95-115: the integrated endpoint

The prepared machine needs the verified local model and matching encoder.
The proposed command is `uv run python bot.py --encoder-path /path/to/snapshot`;
replace the path with the prepared actual snapshot and pin that provenance.
The default model is currently a candidate, not a verified endpoint.

Allocate: first typed question/tool/source inspection (five minutes), follow-up
and inspected request history (five), fresh-process reopen plus second isolated
conversation (five), audible reply/stop and one failure (five). For each, retain
actual evidence. A current Codex conversation alone does not prove this portable
student application. Unsupported question must visibly refuse without invented
citations. Programmatic citation membership is necessary but not sufficient:
a correct source ID can still accompany an unsupported claim.

Synthesis happens after a successful atomic save. A speech error must say text
is saved but speech failed. `speech.py` produces a live waveform; the supplied
prepared refusal WAV is explicitly prerecorded fallback. Neither a WAV file
nor a successful player exit proves that a listener heard intelligible speech.
Show how Ctrl+C stops playback and how to exit the typed loop. Typed input is
core; Week 6 microphone recognition is optional reuse only.

### 115-120: the transfer

Compare relational rows for ownership/ordered history, a nested save/config
for restoring a whole scene, and vector+metadata storage for semantic candidates.
JSON is one representation; document databases may validate schemas and
relational databases can store nested data. The choice follows the question,
not a rigid SQL/NoSQL taxonomy. Finish by identifying the four state lifetimes
again and linking the exact reviewed PFAD files and commands.

## Separate tutorial and tutor support

The companion README supplies the complete approved 120-minute route:
0-10 setup; 10-30 related model save/load; 30-50 exact query/index/update/restart/
constraint; 50-60 break; 60-70 real vectors/two queries; 70-90 typed follow-up and
speech; 90-100 reload/isolation/failure; 100-120 tutor review/project support.
The tutor's 12 November meeting follows allocated slots. No ClassPoint login,
new assessed upload, extra grade or compulsory defence is added.

Preserve 40% project weighting, 25/50/25 rubric, public sd5913-owned team repo
with teammate Write access, and 6 December 2026 23:59 HKT deadline. GitHub
Projects remains recommended; equivalent accessible progress evidence is valid.

## Feasibility evidence needed before deck replacement

1. Retrieve/inspect current PDF; include exact provenance and a small cited extract.
2. Run real compatible chunk/query vectors; inspect two meaningful rankings and an irrelevant question.
3. Run the actual local model/tool/evidence/answer path; check supported and unsupported answers.
4. Prove follow-up uses prior messages, fresh-process recall and second-conversation isolation.
5. Prove live synthesis, audible playback, stop and visible failure separately.
6. Verify simple uv commands from a clean weekly environment and a prepared partner-machine fallback.
7. Only then author replacement slides with rich notes, large diagrams, real excerpts and pinned links; inspect HTML/PDF/both PPTX with overflow enabled.

Keep offline/protocol tests, actual live behavior and physical classroom checks
separate in the review evidence. Do not mark core feasibility as an optional
instructor-only rehearsal or let an attractive render conceal the gap.
