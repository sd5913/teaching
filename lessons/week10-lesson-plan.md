# Week 10: relational storage, APIs and a talking handbook

**Thursday 12 November 2026. 120-minute lecture; separate 120-minute PFAD tutorial.**
Relational databases remain the centre: tables, relationships, keys, SQL, indexes,
constraints and persistence. Qdrant is a complementary similarity-search example;
Cloudflare D1 shows related SQL rows behind an API.

## Teaching continuity and source choices

Keep this year's deckgen layouts, large diagrams, short visible claims and fuller
speaker notes. Continue the practical rhythm: predict → run → inspect → change →
check → recover. Week 7 supplies classes; Week 8 supplies inspection/team workflow;
Week 9 supplies HTTP/WebSockets and Multiboxes. Its in-memory Scene resets on
server restart. The reusable talking bot is **Week 6 Pip**, not Week 9.

Both private historical references were materialized and inspected separately:
67 slides each, matching lecture/tutorial sequence. Retain their progression from
object relations and keys to SQL/Peewee, storage and PDF/vector retrieval, adapted
to this year's code and visual language. Do not publish either source file. Avoid
the historical HTTP UPDATE verb, blanket 'NoSQL is schemaless' claim and bare
password-hash/login exercise. Keep fictional local profiles and explicit limits.

Recent completed Week 8 and Week 9 decks/notes/practicals supply the level,
large-canvas figures and theory → concrete code → observation → project transfer
rhythm. Existing Week 10 and November 11 news files remain intact; optional news
replaces at most two opening minutes, not another teaching block or quiz topic.

## Exact lecture route

| Minutes | Work | Observable evidence |
| --- | --- | --- |
| 0-10 | Returning-user question, dated news, four lifetimes | Distinguish knowledge, saved history, current prompt and audio |
| 10-25 | Model → instance → row | Peewee create/save/select; values persist, methods remain code |
| 25-40 | Relationships, exact queries, PK/FK/index | User → Conversation → Message; scoped ordered SQL; junction/self-reference transfer |
| 40-54 | Seed, rename, restart, invalid write and transaction | Same ID/new title; rejected orphan; failed pair rolls back |
| 54-60 | Prepared D1 API demo and check | HTTP → Python Worker → bound SQL/JOIN → JSON; changed title survives restart |
| 60-70 | Break | Ten minutes |
| 70-80 | Embeddings and similarity | Real compatible 384D vectors, ranking, unknown question still has neighbours |
| 80-95 | PDF provenance, Qdrant API/dashboard and tool | Page/text/ID; six persisted points; API returns cited passages |
| 95-115 | Pip question/follow-up, history, speech and recovery | Actual request trace, saved rows, reopened owner, Kokoro audio, visible failures |
| 115-120 | Storage comparison and tutorial handoff | Choose by the query; keep relational relationships distinct from similarity |

## Relational first half

Run PFAD `week10/storage_demo.py` seed/inspect/rename/inspect/invalid, each in a
new process. `Record` inherits Peewee `Model`; three subclasses define fields.
A primary key identifies a row; a foreign key references a parent; an ordinary
compound index helps filter/order and costs storage/write work. Avoid claiming
an unmeasured speedup. `id(obj)` is not a database ID. Assignment needs `.save()`.
An ORM maps operations; the database still enforces constraints.

Inspect the actual query and bound parameters. Ownership is checked before
history retrieval; FK existence alone is not authorization. `append_turn()`
saves a complete user/assistant pair inside a transaction. A failed second
insert rolls back the first. Model/network calls happen before that transaction.
The prompt receives four complete recent pairs; older rows remain in SQLite.
Use a new disposable filename for experiments, never erase needed work.

D1 is new: Week 4's `api.py` read a tide JSON file and had no D1 binding.
The small `week10/d1/src/worker.py` uses a configured `DB` binding and a prepared
JOIN. Prepare `npm ci`, `npm run seed`, `npm run dev` beforehand. GET
`/messages?conversation=1`, change the title through local SQL, restart, GET
again. Local emulation needs no cloud account/credentials; no remote flag or
deployment. The read-only API exposes fictional teaching rows, not private
history/authentication. D1 is a SQLite-based relational service, not a Peewee
local file or vector store. Keep this to six lecture minutes and five tutorial
minutes inside the relational block.

## PDF, Qdrant and the existing Pip

Use the supplied six short extracts of the official 2026/27 handbook with PDF
page, printed page, section, source URL/hash and chunk ID. The historical source
decks do not become the bot corpus. `download_handbook.py` and `prepare_index.py`
show the rebuild path; full ingestion/model downloads happen before class.

`QDRANT-PIP.md` is the second-half route. Docker Compose pins Qdrant, binds
6333 to loopback and mounts a named volume. `qdrant_index.py` seeds deterministic
UUID points into a content-addressed collection; repeat seeding doesn't create
duplicates. Compare three actual prepared query rankings with the in-process
reference. Open `/dashboard`, inspect six points/384D Cosine config/payloads.
Explain GET collections, PUT collection/points, POST points/query. The encoder
creates vectors; Qdrant stores/ranks them. Restart then query without reseeding.
Keep the volume; don't use `down -v`. No Docker? Observe a prepared machine;
the in-process reference is labelled as a different route.

Source IDs and database UUIDs do different jobs. Matching dimension is not
matching encoder identity. Keep table units/headings and exceptions with chunks;
nearest neighbours are not policy truth, probabilities or declared SQL links.

Pip reuses `week06/speech/local_reply.py` for local HTTP and
`synthesise_onnx.py` for Kokoro. `pip_adapter.py` retains Week 10's bounded
retrieval/tool/structured-answer loop. `pip_app.py` uses Streamlit, the same
related SQLite store and Qdrant. Typed input is core; existing WebRTC/microphone
code is an optional later addition. No second mandatory model/speech stack.

The exact loaded LM Studio model must support tools and JSON-schema output;
simple Week 6 chat capability alone is insufficient. Prepare encoder/Kokoro
assets and model before class. Read `QDRANT-PIP.md` for commands. The original
llama.cpp/eSpeak CLI remains an alternate reference, with its old recordings
clearly labelled as evidence of that earlier route only.

Ask the lost-card question and the original-card follow-up. Expand the actual
request trace; check the earlier pair, model-composed query, Qdrant text and
citations. The model composes the answer; citation membership doesn't prove
support. Save after validation; synthesize after save. Browser autoplay may
need a click; a physical listener must check room audibility. Unsupported
questions should receive a source-limited refusal; inspect actual behavior.
Stop/restart the app, reopen the printed ID, use a second profile and verify
isolation. Stop Qdrant and verify no new turn is saved; restart without reseeding.
Speech failures retain completed saved text. Local profiles aren't authentication.

## Separate 120-minute tutorial

0-10 setup/pair fallback; 10-30 models/tables; 30-50 exact queries, constraints,
restart and a prepared five-minute D1 demonstration; 50-60 break; 60-70 Qdrant
API/dashboard and rankings; 70-90 Pip question/follow-up/trace/voice; 90-100
reopen/isolate/failure/recovery; **100-120 tutor review and project support**.
Keep the allocated tutor slots. No surprise installations in support time.

Project policy stays **40%**, **25% idea / 50% code / 25% execution**, deadline
**6 December 2026 23:59 HKT**; public **sd5913-owned** team repository, teammate
Write access; GitHub Projects recommended or an equivalent accessible progress
record. Canvas remains submission. No new compulsory technology, grade or upload.

## Verification boundary

See `week10/VALIDATION.md` in the paired PFAD draft for current checks and honest
limits. Re-run room/projector/audio and the actual LM Studio model before class;
old recorded evidence isn't proof of a fresh Pip run. Keep both PRs draft/open.

Paired companion source pinned for review: https://github.com/sd5913/pfad/tree/58139f79270f5dc095655c87d8489f938c64e363/week10 .

Final source refresh: the official PDF changed on 10 November; all six extracts
remain exact matches on the same pages. Re-downloaded, inspected and re-embedded
11 November. Current source hash: `43ac3a6a7697b2ce78f1964f673dae0aa2ccf79ba7c58fb310b469dc2b380a1b`.
Old CLI recordings retain their original October provenance.
