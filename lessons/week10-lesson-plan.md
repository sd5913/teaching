# Week 10: persistent objects and a talking handbook agent

**Thursday 12 November 2026. 120-minute lecture; separate 120-minute PFAD tutorial.**
The replacement deck now follows the approved model-to-row → current handbook
vectors → retriever tool → persisted conversation → spoken-output progression.
The prior artwork/optional-retrieval narrative is superseded; its JSON example
remains supplementary in PFAD, not the core lesson.

[Companion source](https://github.com/sd5913/pfad/tree/67f5297dc6f8878ceea51c431d726cfeb1934b4a/week10),
[complete tutorial](https://github.com/sd5913/pfad/blob/67f5297dc6f8878ceea51c431d726cfeb1934b4a/week10/README.md)
and [preparation](https://github.com/sd5913/pfad/blob/67f5297dc6f8878ceea51c431d726cfeb1934b4a/week10/REHEARSAL.md).
Sources are pinned while paired PR #13 remains open. No merge/release is implied.

## Exact lecture route

| Minutes | Sequence | Observable teaching work |
| --- | --- | --- |
| 0-10 | Opening, dated news, four kinds of state | Returning user's vague follow-up; distinguish knowledge, history, current prompt and audio |
| 10-25 | User/Conversation/Message model → instance → row | Real Peewee inherited methods, stable ID, `.save()`, new process reconstructs values |
| 25-40 | Relations, exact queries, keys and ordinary indexes | Owner check, conversation filter/order, PK/FK/index; short SaveFile/Membership/reply transfer drills |
| 40-60 | SQL/rows/restart/failure/transaction experiment | Seed/inspect/update/new process; rejected orphan/role/empty content; rollback and history window |
| 60-70 | Break | Ten minutes inside the lecture |
| 70-80 | Learned representations and compatible search | Real 384D vector excerpt; same encoder; actual fee-query ranking; unknown still has neighbours |
| 80-95 | Official PDF → chunks → index → retriever TOOL | Inspect source page/metadata, three prepared queries, table/chunk boundary, actual structured tool call |
| 95-115 | Typed bot, saved history, fresh process, isolation and speech | Source-supported and unsupported answers; inspect previous pair reaching model; reopen/second profile; synthesize/play/stop/failure |
| 115-120 | Storage comparison and tutorial handoff | Related rows/nested save/vector candidates; four lifetimes; separate exact tutorial route |

## 0-10: opening and current news

The concrete scenario is a returning user asking “what about the original?”
after discussing a lost identity card. History resolves the reference; the
handbook supplies policy evidence. Ask for a game NPC equivalent without making
AI a project requirement.

Use at most two minutes on the verified [Peewee 4.5.3 release](https://github.com/coleifer/peewee/releases/tag/4.5.3),
published 7 October, checked 29 October. Maintainer claim: explicitly executing
a write query with `RETURNING` now executes again rather than reusing a cached
result. Ask what a save button should do if pressed twice. This news is outside
quiz scope. Our SQLite behavior is tested; the entire release note is not.

Give the four-state diagram the slide: shared versioned knowledge/index,
user-owned persistent history, temporary assembled prompt and audio output.
A diagnostic JSON snapshot is not the memory database.

## 10-40: model methods, records and relationships

Use the actual PFAD `models.py`, not another two-object constructor recap.
`Record` inherits Peewee `Model`; User, Conversation and Message inherit it.
Trace `.create()`, assignment, `.save()` and `.select()` to INSERT/UPDATE/SELECT,
affected rows and reconstructed objects. Stable stored IDs are not `id(obj)`.
Methods remain code; values and references persist.

Prediction: omit `.save()` after changing the title. A fresh process sees the
previous saved value. Restore `.save()` and inspect the changed title/same ID.
Explain one-to-many User→Conversation→Message; a foreign key references an ID
rather than copying a parent. Ownership checking is separate from FK existence.
These are fictional local profiles, not authenticated accounts.

Trace `history_query()`'s ownership check before its filtered/ordered message
query. Show actual generated SQL/parameters in the terminal; the slide shows a
simplified equivalent. A primary key identifies a row, FK references a parent,
ordinary compound `(conversation_id,id)` index helps lookup/order. Indexes cost
storage/write work; do not claim an unmeasured speedup on six rows. This is not
the semantic index used after the break.

Use short transfer drills: User/SaveFile one-to-many; User/Membership/Team via a
junction row; Message replying to Message self-reference. Do not build another
app or reintroduce unsafe historical bare password hashing.

## 40-60: persistence experiment

Terminal working directory: PFAD `week10`.

```bash
uv run python storage_demo.py seed
uv run python storage_demo.py inspect
uv run python storage_demo.py rename
uv run python storage_demo.py inspect
uv run python storage_demo.py invalid
```

Each command is a new process. A fresh database begins with one Ada, one
conversation and two explicitly prepared storage messages; no model is called
by seed. Inspect prints the actual query/parameters, rows, reconstructed role/
content dictionaries and ordinary index names. Reused files can have different
IDs; after renaming, seed can create another Handbook title. Use a disposable
`--db out/experiment.sqlite` for a fresh test; do not erase work to reset it.

Show the FK failure and unchanged previous rows, then inspect role/nonempty
checks and `append_turn()`'s atomic pair. If assistant insertion fails, the new
user insertion rolls back. A transaction does not include external model calls:
model/evidence validation happens before saving. The classroom CLI has one
active writer, not a production multi-client concurrency contract.

History selects the last four complete pairs in chronological order. Older
rows remain on disk. Changing four to two changes the selected request, not the
saved database. Check rows after failures and explain them with a partner.

## 70-95: the actual source and learned retrieval

Official PDF: *Student Handbook for Taught Programmes 2026/27*, Academic Registry,
July 2026. Downloaded/inspected 29 October: 137 pages, 7,658,316 bytes, SHA-256
`108956feb2ffac665f8ca0f5a8f68d7150a85fda15e219916785ec50331a4e94`.
The official URL is on the deck and in the bundle. PDF20=printed9,
PDF25=printed14, PDF76=printed61. Six short extracts retain source IDs, section,
text and page. Do not redistribute the full PDF or ingest it during class.

```bash
uv run python handbook.py
```

The real pinned MiniLM encoder yields 384D normalized vectors for passages and
questions, max 256 tokens. It replaces the earlier cached CLIP feasibility
candidate; same dimension alone is insufficient compatibility. Word2vec's
historical neighbour intuition is retained briefly; no huge word-model download
or Orange/t-SNE practical is required. Orange's removal is an instructor decision.

Inspect lost-card, leave and fee results. The fee's measured0.892566/0.737337
cosines rank the exact fee row and replacement rule. A noisy full-table chunk
initially missed the fee row; the bounded row extract improved this case. HK$
comes from the table heading in section metadata. Ambiguous flattened leave-table
columns are excluded; clear prose and decision paragraphs are separate chunks.
Source checking, not a magic similarity threshold, determines support.

Show actual model tool query `student identity card replacement cost` and its
result. The app requires retrieval; the model composes a query using history.
Python encodes/searches/returns passage IDs/pages/text/scores/source metadata.
The model then generates `answer` and `source_ids` under a JSON schema. Empty
IDs become the standard refusal; bracketed citations are formatted from the
model's selected IDs. Shape/ID validation does not establish factual correctness.
This is a bounded RAG/tool workflow, not autonomous arbitrary tool selection.

## 95-115: integrated live route

Prepare the public model, encoder and audio before class using REHEARSAL.md.
Terminal1 runs llama.cpp b11972 with Qwen3.5-2B Q4_K_M on CPU, loopback 11440;
wait for its listening message. Terminal2:

```bash
uv run --extra encoder python bot.py
```

Ask the exact lost-card question then the “original later / keep both?” follow-up.
Inspect the visible `TOOL TRACE`, cited passages and `out/last-turn.json`.
The first answer in the recorded real run gives online replacement, HK$150 and
return-for-cancellation, supported by two cited sections. The follow-up resolves
the reference and says return/cancel rather than keep both. The model generates
policy wording; no prepared answer script is used.

Exit/reopen with `--conversation ACTUAL_ID` and the same database. Inspect the
previous user/assistant pair actually entering the next model call; a thread
label alone proves nothing. Start `--user Bo` without a conversation ID; ask
about leave and verify Ada's history is absent. Wrong-owner access is rejected.
Ask the cafeteria Wi-Fi password: the six-extract corpus cannot support it, so
the actual model emits no source IDs and the app displays its standard refusal.

The successful answer is saved before live eSpeak synthesis/ffplay. Verified
actual cited-answer WAV: mono PCM22050Hz,18.76sec. Player completion and a longer
Ctrl+C stop passed; invalid driver failure is separate and preserves displayed
text/history. A physical listener must check room intelligibility/volume before
class. A completed player is not a listener report. Typed input is core;
microphone recognition is optional Week6 reuse.

For a failure, use `--bundle out/missing.json`, stop the prepared model then
retry, or use the preparation guide's invalid audio driver. Explain which state
survives. Do not silently substitute the recording for a live result. Public
recorded trace/audio are useful clearly labelled fallbacks; protocol unit tests
use doubles and prove different things.

## 115-120: comparison and handoff

Compare storage by needed retrieval: related rows for ownership/ordered history;
a nested save/config for a whole scene; vectors+metadata for semantic candidates.
JSON is a representation; document databases may validate schemas and relational
systems may hold nested data. No new database installation is needed.

The PFAD tutorial is exactly:0-10 setup;10-30 models;30-50 query/index/update/
restart/constraints;50-60 break;60-70 vectors;70-90 typed follow-up/speech;
90-100 reload/isolation/failure;100-120 tutor review/project support. Pair at
minute10 if setup fails. Tutor12November meetings follow allocated slots.
Canvas submission; no ClassPoint dependency, new grade/upload or defence.

Group project remains40%, 25/50/25 rubric, public sd5913-owned repository with
teammate Write access, due 6 December 2026 at 23:59 HKT. GitHub Projects recommended;
equivalent accessible progress record remains valid.

## Verification boundary

Linux x86_64, Python 3.12.15, Peewee 4.5.3, Torch 2.14.1+cpu,
Transformers 5.19.0, Sentence Transformers 6.2.0, llama.cpp b11972 and eSpeak NG 1.52.0.1.
Clean CPU dependency installation, real current PDF/vector fixture, actual
model/tool/supported/refusal/follow-up/fresh-process/isolation and live synthesis/
player completion/stop/failure are recorded in the private author report.
20 PFAD tests distinguish synthetic protocol checks from learned fixtures.
Physical speaker listening, Windows/macOS and the room's displays remain
instructor rehearsal checks; small-model semantic mistakes remain possible.
