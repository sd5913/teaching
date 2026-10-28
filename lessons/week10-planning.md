# Week 10 production design and source crosswalk

Status: **independent implementation and complete timing prepared; integrated
core incomplete, replacement deck gated**. Updated 29 October 2026. The earlier
artwork/JSON-only draft is superseded by the instructor-approved progression.
Its source is preserved until feasibility passes, not endorsed as the final
lesson. The paired run sheet and PFAD README define the intended teaching route.

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
| W10 pp44-54 | RAG, word vectors, learned embeddings, chunking, vector store and retriever tool | Core restored: current handbook PDF -> cited chunks -> same-space vectors -> tool -> inspected answer; lecture70-115/tutorial60-100; actual source/model proof still blocked |
| W10 pp59-64; PFAD `word2vec_example.py` | Learned neighbour/analogy intuition | Updated: brief word-neighbour intuition and real local text-vector probe; no huge fastText download in class |
| PFAD `qdrant_store.py`, `qdrant_add_pdf.py` | Shared encoder/space, chunk metadata, real semantic query | Updated: bounded local cosine index carries weight/tokenizer hashes, dimension and source IDs; full ingestion prepared before class; real current PDF bundle pending |
| PFAD `pdf_bot.py` | Retriever exposed as agent tool | Restored and corrected: actual model tool request dispatched; prior ordered messages loaded and passed; ID alone not called memory; live model proof pending |
| W11 pp14-17,p22 | Reuse the same handbook embedding space | Retained in handbook retriever/agent; no unrelated corpus substituted |
| W11 pp18-30 | Orange/t-SNE/matrix exploration | **Removed by explicit instructor decision** to give Blender/Godot more time; not a missing prerequisite or quiz requirement |
| W11 pp31-39 and creative-app examples | Python controls creative applications | Moved/retained in W11 Blender/Godot; this week ends with retrieval as a reusable tool |
| W6 speech material | Input/output surrounding a bot | Retained/updated: typed input core, live offline TTS, recorded-audio fallback explicitly labeled; microphone optional |

## Implementation choices and evidence boundary

Peewee **4.5.3** is the latest upstream release checked 29 October (published
7 October). It is a real ORM, not a course imitation. `models.py` uses enforced
SQLite foreign keys, role/nonempty constraints, a compound history index and
atomic user/assistant writes. Exact row queries and ordered history reload are
verified, including a separate process. Fictional local profiles are not secure
accounts; no real passwords or personal student data belong in the examples.

The cached CLIP text encoder produces normalized 768-dimensional vectors on
CPU. Two small synthetic sanity queries ranked the intended passages first,
which proves learned inference and the similarity mechanism only. It does not
prove retrieval from the actual handbook. This encoder's 77-token limit and
image/text training objective must be considered when evaluating the real
passages. Encoder weights/tokenizer/pooling identity travels with the bundle.
No fabricated numbers are shipped as handbook embeddings.

The instructor supplied the exact official 2026-27 PDF URL. DNS prevents its
retrieval in this environment. The pipeline therefore refuses missing assets;
no fake page numbers or invented policy extracts fill the gap. `prepare_index.py`
can process selected pages once the actual PDF is available. At least two
prepared query vectors are required for its no-download fixture.

The local-only Ollama adapter follows current tool-calling/embed documentation,
but this environment cannot access a local model endpoint on port11434. Scripted protocol tests establish
request/history/dispatch/citation-ID validation and no-write-on-failure, not
model reasoning or live contextual memory. The bounded loop allows at most
three retrieval calls/four model requests. No package causes model downloads,
new accounts or paid API calls.

Real eSpeak NG synthesis creates PCM WAV files, including an explicitly
prepared refusal fallback. Audio opening is denied here, so audible playback
and stopping remain unverified. Speech is not a persistent source/index and
synthesis cannot establish the truth of the answer.

## Authoring gate and next handoff

The long replacement deck waits for real PDF/source/vector results, the actual
conversation-aware model/tool loop, and spoken output checks. When the gate
passes, use the approved run sheet, incumbent course fonts/palette/layouts,
`deckgen.CODE`, >=40-design-pixel primary labels, full-slide relationship diagrams,
rich notes, dated source links and pinned companion examples. Inspect actual
HTML/PDF and both PowerPoints with overflow warnings enabled. Do not claim
those renders or the current incumbent source establish the new endpoint.

No shared navigation/registration, root environment, official presenter,
classes or assessment policy was changed. Reviewers should inspect the new
companion implementation, test evidence and explicit gaps before authorizing
replacement slide production. Keep both PRs open; no merge or release is implied.
