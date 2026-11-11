# Week 10: relational storage, APIs and a talking handbook

**Thursday 12 November 2026. 120-minute lecture; separate 120-minute PFAD tutorial.**
The first hour explains persistent objects, relationships and database choices
before showing code. Relational databases remain the centre: schema, keys, SQL,
indexes and constraints. Qdrant is a complementary similarity-search example;
Cloudflare D1 briefly shows related SQL rows behind an API. Use one saved
conversation throughout; the deck has 65 slides, including six numbered section
dividers and worked query results. Dividers mark transitions inside each block.

## Teaching continuity and source choices

Keep this year's deckgen layouts, large diagrams, short visible claims and fuller
speaker notes. Continue the practical rhythm: predict → run → inspect → change →
check → recover. Week 7 supplies classes; Week 8 supplies inspection/team workflow;
Week 9 supplies HTTP/WebSockets and Multiboxes. Its in-memory Scene resets on
server restart. The reusable talking bot is **Week 6 Pip**, not Week 9.

The archived 2025 Week 10 PDF and matching PPTX were inspected separately:
67 pages/slides each. Retain their progression from
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
| 0-10 | Returning-user question and route | What should the app remember after closing? Optional news stays in opening notes |
| 10-20 | Memory, persistence, identity and reconstruction | Explain saved values/references versus live objects and imported methods; restart prediction |
| 20-34 | Cardinality, optionality, junction records and self-reference | Explain the conversation model, then discuss three transfer cases |
| 34-46 | Database taxonomy, storage choice, schema and keys | Place the four NoSQL families and vector search; justify a choice; distinguish PK/FK/index |
| 46-54 | SQL, related rows, ORM and transactions | Explain keywords and a foreign-key filter; pair Python with generated SQL; predict when a write happens |
| 54-58 | Prepared SQLite reload and brief D1 demo | Same stored ID/new object; rejected orphan; HTTP → bound SQL → JSON |
| 58-60 | Concept recap | Explain a save/team/conversation design without library syntax |
| 60-70 | Break | Ten minutes |
| 70-83 | Semantle, word embeddings, text embeddings and similarity | Observe word similarity, explain a learned vector, extend to question/passage embeddings, inspect real ranking |
| 83-95 | PDF provenance, Qdrant API/dashboard and tool | Page/text/ID; six persisted points; API returns cited passages |
| 95-115 | Pip question/follow-up, history, speech and recovery | Actual request trace, saved rows, reopened owner, Kokoro audio, visible failures |
| 115-120 | Four kinds of state and tutorial handoff | Distinguish knowledge, history, prompt and audio after seeing the system |

## Relational first half

Teach the definitions and diagrams before the terminal. Persistence concerns
selected values and relationships outliving a process, not preserving a running
object or storing method bodies. A JSON snapshot can preserve a whole save;
SQLite adds database facilities while still using a file. Separate data model
from deployment, and persistence from backups.

State relationship rules in both directions. Separate maximum cardinality from
optionality. Explain one-to-one, one-to-many, many-to-many through Membership,
and Message reply-to as a self-reference. Use the one-to-one diagram at 23-25,
many-to-many links at 25-26, then the same three Membership rows at 26-28.
A role belongs to a membership rather
than to a user globally. Use Player/Score, Player/Team and Tag/Post on one
discussion slide; nouns alone do not determine the answer. User/Group and
Conversation/Message remain in the PFAD guide, keeping all five historical
practice cases available. Membership/reply-to are transfer diagrams, not
additions to the implemented app. Profile is also an illustrative extension;
its unique user reference enforces at most one profile, not a requirement that
every user has one.

Use three slides within the existing 34-39 block: taxonomy map at 34-35; four
NoSQL families at 35-37; vector search at 37-39. Relational is a data model;
NoSQL groups common key-value, document, wide-column and graph models. Vector
databases specialize in similarity search; that capability can also be added
to relational/document systems. Qdrant and PostgreSQL + pgvector make the
overlap concrete. Product names are examples, not quiz memorization targets.
Do not imply NoSQL means no rules or relational systems cannot store JSON.
The same application uses related rows for exact history and vectors for
similarity. Show schema versus particular rows before introducing keys/SQL/ORM.

An embedded restart prediction and three short discussion slides ask students
to classify relationships, choose storage and identify PK/FK/index jobs. These are
revision material, not official quiz items. Quiz preparation includes applying
persistence, identity, cardinality, schema, queries, ORM and transactions to a
new scenario; package installation and dated news are outside that scope.

Run PFAD `week10/storage_demo.py` seed/inspect/rename/inspect/invalid, each in a
new process during minutes 54-56, using a prepared command sequence with no
setup or live typing. `Record` inherits
Peewee `Model`; three subclasses define fields.
A primary key identifies a row; a foreign key references a parent; an ordinary
compound index helps filter/order and costs storage/write work. Avoid claiming
an unmeasured speedup. `id(obj)` is not a database ID. Assignment needs `.save()`.
An ORM maps operations; the database still enforces constraints.

Start SQL with the four clause meanings at 46-47, immediately followed by
`SELECT id, content FROM message WHERE conversation_id = 3 ORDER BY id` at
47-48. The source-ID table shows messages 7/8 linked to conversation 3 and
message 9 linked to conversation 5; only 7/8 appear in the result. Distinguish
selecting columns from filtering rows, and a foreign-key filter from looking up
one message by its primary key. Use literal 3 here; introduce bound values as
the application version. No JOIN is needed to find children of a known parent.

Connect operations and model fields at 48-49. At 49-50, spell out
Object-Relational Mapper and follow Python operations → ORM-generated SQL and
bound values → database execution → returned model instances. Pair the earlier
foreign-key query with the real Peewee version. Building the query and calling
`.sql()` do not execute it; the first `list(query)` does.

Match `conversation.owner_id` to `user.id` and compare the JOIN's Python/SQL
at 50-51; compare the UPDATE's Python/SQL at 51-52. Each paired slide shows
the actual Peewee 4.5.3 SQL, bound values and result/affected-row summary.
Peewee infers this JOIN's ON condition from the declared foreign key. The
database still executes SQL and enforces constraints. The fictional snapshot
uses users 1/2 and conversations 3/4/5; actual demo IDs may differ. The assistant
text is prepared storage data, not policy advice or a new model response.
Ask which rows are excluded, why Ada appears twice in the JOIN result, and what
an UPDATE without WHERE would change. Keep IDs/owner links stable after renaming.
At 52-53, pause on the ungraded ORM/persistence checkpoint: start a fresh row
3 titled Handbook, load it, then assign Game ideas without saving. Ask which
title another process loads and which operation would persist the change.
Speaker notes explain the answer. This checks the ORM's job and the distinction
between changing a Python object and running UPDATE; it is not an official quiz
item. The transaction explanation follows at 53-54. SQL references checked against
https://www.sqlite.org/lang_select.html and https://www.sqlite.org/lang_update.html .
Peewee translation, lazy execution, tuple results and save behavior checked
against https://docs.peewee-orm.com/en/latest/peewee/querying.html and
https://docs.peewee-orm.com/en/latest/peewee/writing.html .

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
local file or vector store. Keep this to two lecture minutes (56-58) and five
tutorial minutes inside the relational block. Pre-run the title update and
restart; show the prepared evidence rather than adding setup during the lecture.

## PDF, Qdrant and the existing Pip

Begin with the instructor's Semantle example before any raw vector values.
At 70-73, open https://semantle.com/ and compare two or three guesses using
the actual similarity feedback. The game explicitly describes word2vec and
semantic rather than spelling similarity. Stop after three minutes rather
than solving the daily puzzle. If unavailable, explain the guess/feedback loop
without claiming a live round; do not use fabricated scores or reveal an answer.

At 73-75, define an embedding as a learned numeric representation: a vector is
a list of numbers, and words used in related contexts can have similar vectors.
Training learns the representation; guessing does not retrain the model. At
75-77, extend from a single word to a sentence/short passage. Semantle's word
space and our MiniLM text space are different; we reuse the idea, not its vectors.
At 77-79, follow a question and passage through the same text encoder, yielding
two compatible 384D vectors. The encoder creates these features; Qdrant stores
and compares them. Inspect the actual values at 79-80, the compatible query
path at 80-81, real ranking at 81-82 and unsupported-neighbour caution at 82-83.
Individual dimensions need not be human-named properties; similar is broader
than synonym and is not proof of source support. Semantle is a lecture example,
not an extra required tutorial task. Primary instructions checked 11 November:
https://semantle.com/ and https://semantle.com/faq . Text-embedding reference:
https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html .

Use the supplied six short extracts of the official 2026/27 handbook with PDF
page, printed page, section, source URL/hash and chunk ID. The historical source
decks do not become the bot corpus. `download_handbook.py` and `prepare_index.py`
show the rebuild path; full ingestion/model downloads happen before class.
The remaining route is 83-84 provenance; 84-86 source reading; 86-89 prepared
Qdrant query/dashboard/restart; 89-91 API; 91-93 tool arguments; 93-95 tool loop.
Keep Pip at 95-115 and the handoff at 115-120. Prepare services and assets
before class; the extra conceptual introduction does not add setup time.

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

See `week10/VALIDATION.md` in the paired PFAD PR for current checks and honest
limits. Re-run room/projector/audio and the actual LM Studio model before class;
old recorded evidence isn't proof of a fresh Pip run. Both PRs are open for review.

Paired companion source pinned for review: https://github.com/sd5913/pfad/tree/c177bff158426b0ed2f285fb61a6630db80909b4/week10 .

Final source refresh: the official PDF changed on 10 November; all six extracts
remain exact matches on the same pages. Re-downloaded, inspected and re-embedded
11 November. Current source hash: `43ac3a6a7697b2ce78f1964f673dae0aa2ccf79ba7c58fb310b469dc2b380a1b`.
Old CLI recordings retain their original October provenance.
