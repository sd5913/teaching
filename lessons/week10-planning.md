# Week 10 production design and source crosswalk

Status: **source-backed integrated CPU route verified; replacement deck authored**.
Updated 29 October 2026. The earlier artwork/JSON-only draft is superseded.
Physical room audibility and non-Linux platforms remain explicit rehearsal
checks. See the paired run sheet and complete PFAD tutorial for exact timing.

## Prior knowledge and new ideas

| Already taught | Use here | New contribution |
| --- | --- | --- |
| W7 Ball class/attributes/methods/instances | Read a model and instance without repeating constructors | Inherited ORM methods; model -> SQL -> persistent row -> reloaded object |
| W8 inspected code, dependencies, testing, teamwork | Run a small local environment and check a purposeful change | Owner-scoped queries, keys/references/indexes, constraints and transactions |
| W9 requests/messages/process lifetimes | Observe a model request/tool response | Source-backed retrieval plus persisted conversation context |
| W6 speech input/output | Keep typed input and visible answer | Synthesis/playback/stop as separate checked outputs; microphone optional |

The design/game scenario is one returning user's handbook conversation, not a
second login app or a generic SQL worksheet. SaveFile, Membership and reply-to
relationships transfer the modelling idea without adding application builds.

## Source-to-lesson crosswalk

Page numbers are PDF positions, read from the actual archived 2025 Week 10 PDF.
The archived PFAD source was inspected at `512edb07927c5d77cacc7279ba6be601b33dc601`.
Week 11 PDF and PPTX numbering differ; do not silently substitute slide numbers.

| Historical source | Purpose | Current destination and status |
| --- | --- | --- |
| W10 pp14-19; PFAD `login_app/model.py` | Typed model attributes; one-to-many, many-to-many, self-reference | Retained/updated: real Peewee User/Conversation/Message classes, 10-40 lecture; SaveFile/Membership/reply drills |
| W10 pp20-24 | Active cardinality questions | Retained: short transfer questions at lecture25-40/tutorial30-50; no extra app |
| W10 pp25-30 | IDs, ordinary indexes, schema, SQL, inherited ORM persistence/query methods | Restored: `.create()`, `.save()`, `.select()`, explicit SQL/parameters/rows, FK/PK/index distinction, fresh-process reload; lecture10-60/tutorial10-50 |
| W10 pp35,38 | Related records vs nested/document vs vector retrieval | Retained with corrected modern caveats: lecture115-120/tutorial tutor review; JSON is a representation, document stores may validate schemas |
| W10 pp39-43 | Account records, registration/login operations | Updated: user ownership of conversations/messages; no separate auth UI and no unsafe bare SHA-256 password hashing |
| W10 pp44-54 | RAG, word vectors, learned embeddings, chunking, vector store and retriever tool | Core restored: current handbook PDF -> cited chunks -> same-space vectors -> tool -> inspected answer; lecture70-115/tutorial60-100; actual current-source/model/tool proof recorded |
| W10 pp59-64; PFAD `word2vec_example.py` | Learned neighbour/analogy intuition | Updated: brief word-neighbour intuition and real local text-vector probe; no huge fastText download in class |
| PFAD `qdrant_store.py`, `qdrant_add_pdf.py` | Shared encoder/space, chunk metadata, real semantic query | Updated: bounded local cosine index carries weight/tokenizer hashes, dimension and source IDs; full ingestion prepared before class; real six-extract/current PDF fixture supplied |
| PFAD `pdf_bot.py` | Retriever exposed as agent tool | Restored and corrected: actual model tool request dispatched; prior ordered messages loaded and passed; ID alone not called memory; actual model/follow-up/reload/isolation recorded |
| W11 pp14-17,p22 | Reuse the same handbook embedding space | Retained in handbook retriever/agent; no unrelated corpus substituted |
| W11 pp18-30 | Orange/t-SNE/matrix exploration | **Removed by explicit instructor decision** to give Blender/Godot more time; not a missing prerequisite or quiz requirement |
| W11 pp31-39 and creative-app examples | Python controls creative applications | Moved/retained in W11 Blender/Godot; this week ends with retrieval as a reusable tool |
| W6 speech material | Input/output surrounding a bot | Retained/updated: typed input core, live offline TTS, recorded-audio fallback explicitly labeled; microphone optional |

## Final implementation and evidence boundary

Peewee 4.5.3 maps the real User/Conversation/Message classes to SQLite, with
explicit FK enforcement, role/nonempty checks, compound history lookup index
and atomic two-row writes. Method→SQL→rows→fresh-process reload, ownership,
rollback and bounded chronological history are tested. No unsafe login scheme
or second app is introduced; local profile names are fictional, not authentication.

The actual official 2026/27 handbook was retrieved and inspected 29 October:
137 pages, 7,658,316 bytes,SHA256
`108956feb2ffac665f8ca0f5a8f68d7150a85fda15e219916785ec50331a4e94`.
Six short verbatim whitespace-normalized extracts from PDF 20, 25, 76 retain
section/printed-page mapping. A pinned MiniLM sentence encoder replaces the
short-context CLIP feasibility candidate:384D,masked-mean,L2-normalized,max 256tokens.
Real compatible passage/query fixtures rank all three inspected queries.
The fee row was shortened after a noisy table excerpt missed retrieval; ambiguous
leave-table columns were excluded rather than inventing their relationship.

The local CPU Qwen3.5-2B Q4_K_M model runs through llama.cpp b11972 on loopback 11440.
The application requires native retrieval; the model composes its query. The
answer phase generates answer/source_ids under a schema; the app formats
citations or an empty-source refusal. This makes the bounded retrieval policy
explicit rather than claiming autonomous tool selection. Initial natural-language
citation omissions and a confused boolean support field were rejected/removed;
no prepared policy answer is substituted. Valid schema/IDs still do not prove
factual support. Actual supported/unsupported answers, contextual follow-up in
a new process, retained messages entering model calls and isolated Bo history
are recorded separately from scripted protocol tests.

Actual cited-answer eSpeak synthesis,ffplay completion,Ctrl+C stop and device
failure are checked. Physical listener intelligibility/volume remains a room
preflight task. Recorded answer/trace and prepared refusal audio are accurately
labelled fallbacks. Clean isolated uv CPU installation from an empty cache passed;
Windows/macOS remain unverified and use prepared partners when necessary.

## Authoring and review handoff

The replacement deck uses the approved120-minute run sheet, incumbent course
fonts/palette/layouts,deckgen.CODE,large primary diagram labels and substantive
notes. It connects the actual current PDF/compatible vectors/tool/selected
history/spoken output without repeating Week7 constructors or Week9 boundaries.
The separate PFAD README budgets its own120minutes with break/recovery/tutor
support. Render/build/independent-review evidence belongs in the private report;
source alone is not proof of visual readability.

No shared navigation/registration,root environment,official presenter,classes
or assessment policy was changed. Keep both PRs open; no merge/release is implied.
