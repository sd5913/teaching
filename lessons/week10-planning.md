# Week 10 production design and source crosswalk

Status: **concept-led first hour revised with instructor approval, 11 November
2026**. The 2025 conceptual progression is taught visibly before implementation:
persistence/identity, relationships, database families, schema/keys, SQL and ORM.
The 65-slide deck keeps one saved conversation as its running
example. Six numbered dividers mark Persistence, Relationships, Database types,
SQL, Retrieval and Pip without adding time to the 120-minute lecture. SQL starts
with clause meanings, followed immediately by a foreign-key filter and its
source/result rows. Python ORM and generated SQL are paired for the foreign-key
SELECT, JOIN and UPDATE. A prediction checkpoint makes translation, execution
and unsaved instance state explicit quiz/revision scope.
The second half now opens with the instructor's Semantle example, defining
word embeddings before extending to short-text/question/passage embeddings.
Numeric vectors come after those explanations. The 70-83 concept block and
83-95 prepared retrieval block retain the 95-115 Pip demonstration.
Repeated introductions are merged; three relationship
cases share one discussion slide. Qdrant/Pip and the 120-minute lecture remain.
The PFAD README adds conceptual revision alongside its separate 120-minute
practical. Physical room audibility, the actual loaded model and non-Linux
platforms remain explicit rehearsal checks. See the paired run sheet for timing.

## Prior knowledge and new ideas

| Already taught | Use here | New contribution |
| --- | --- | --- |
| W7 Ball class/attributes/methods/instances | Distinguish class behavior from instance state | Persistent identity/values/references; reconstruction, cardinality and inherited ORM operations |
| W8 inspected code, dependencies, testing, teamwork | Run a small local environment and check a purposeful change | Owner-scoped queries, keys/references/indexes, constraints and transactions |
| W9 requests/messages/process lifetimes | Observe a model request/tool response | Source-backed retrieval plus persisted conversation context |
| W6 speech input/output | Keep typed input and visible answer | Synthesis/playback/stop as separate checked outputs; microphone optional |

The design/game scenario is one returning user's handbook conversation, not a
second login app or a generic SQL worksheet. SaveFile, Membership and reply-to
relationships transfer the modelling idea without adding application builds.

## Source-to-lesson crosswalk

Page numbers are PDF positions, read from the actual archived 2025 Week 10 PDF
and checked against the matching PPTX. Both contain 67 pages/slides (PDF page
33 is image-only). The 11 November revision restores explanations and practice
that the earlier compressed walkthrough did not adequately teach.
The archived PFAD source was inspected at `512edb07927c5d77cacc7279ba6be601b33dc601`.
Week 11 PDF and PPTX numbering differ; do not silently substitute slide numbers.

| Historical source | Purpose | Current destination and status |
| --- | --- | --- |
| W10 p14; PFAD `login_app/model.py` | Object attributes and types | Updated: live/stored comparison and concrete saved ID/owner/title at 10-17; class methods remain code; model excerpt/ORM at 48-50, unsaved-change checkpoint at 52-53 |
| W10 pp15-16 | One-to-many | Retained: User → several Conversations at 20-23, then one-to-one contrast at 23-25; count in both directions and discuss optionality |
| W10 pp17-18 | Many-to-many and junction models | Visual sequence at 25-28: crossing links, then the same three links as Membership rows with per-membership roles |
| W10 p19 | Self-reference | Restored explicitly: Message reply-to diagram at 28-30; distinguish record type, direction and cardinality |
| W10 pp20-24 | Five active cardinality questions | Streamlined: Player/Score, Player/Team and Tag/Post share one slide at 30-34; all five case pairs including User/Group and Conversation/Message remain in the PFAD revision guide |
| W10 p25 | IDs, references and ordinary indexes | Restored explicitly: separate PK/FK/index diagram at 43-45 and conceptual checkpoint at 45-46; ordinary indexes do not imply uniqueness or authentication |
| W10 p26 | Schema | Restored explicitly: schema versus actual rows diagram at 41-43; distinguish field/types/constraints from ORM translation and database enforcement |
| W10 pp27-31 | SQL, inherited ORM persistence/query methods | Keywords at 46-47, foreign-key SELECT at 47-48, operations/models at 48-49, ORM definition and Python/generated SELECT at 49-50, owner-ID diagram/Python JOIN at 50-51, Python/generated UPDATE at 51-52, prediction checkpoint at 52-53, transaction at 53-54, SQLite/D1 evidence at 54-58 |
| W10 pp32-35 | Databases, SQL and NoSQL | Clarified at instructor request: a taxonomy map at 34-35; key-value/document/wide-column/graph under NoSQL at 35-37; specialist vector databases versus vector features in other databases at 37-39. SQL is a language; models and search capabilities overlap |
| W10 pp36-37 | Persistent storage and volumes | Updated: memory/disk/file/database distinction at 10-20; local/hosted is separate from data model; Qdrant restart-with-volume evidence remains in second half |
| W10 p38 | Choose storage by data/retrieval needs | Retained: accounts/messages, scene saves and semantic handbook retrieval checkpoint at 39-41, recap at 58-60 and PFAD revision; final recap distinguishes knowledge/history/prompt/audio |
| W10 pp39-43 | Account records, registration/login operations | Updated: user ownership of conversations/messages; no separate auth UI and no unsafe bare SHA-256 password hashing |
| W10 pp44-54 | RAG, word vectors, learned embeddings, chunking, vector store and retriever tool | Concept-led: Semantle/word vectors -> text embeddings at 70-79, real vectors/ranking at 79-83, current PDF/cited chunks/Qdrant/tool at 83-95, Pip at 95-115; tutorial60-100 unchanged |
| W10 pp59-64; PFAD `word2vec_example.py` | Learned neighbour/analogy intuition | Expanded at instructor request: live Semantle at 70-73, learned numeric word representation at 73-75, word-versus-text comparison at 75-77, question/passage encoder diagram at 77-79; actual vector probe follows; no huge fastText download in class |
| PFAD `qdrant_store.py`, `qdrant_add_pdf.py` | Shared encoder/space, chunk metadata, real semantic query | Updated: current Qdrant API/dashboard route plus bounded in-process reference; same encoder identity, dimension and source IDs; full ingestion prepared before class; six-extract/current PDF fixture supplied |
| PFAD `pdf_bot.py` | Retriever exposed as agent tool | Restored and corrected: actual model tool request dispatched; prior ordered messages loaded and passed; ID alone not called memory; actual model/follow-up/reload/isolation recorded |
| W11 pp14-17,p22 | Reuse the same handbook embedding space | Retained in handbook retriever/agent; no unrelated corpus substituted |
| W11 pp18-30 | Orange/t-SNE/matrix exploration | **Removed by explicit instructor decision** to give Blender/Godot more time; not a missing prerequisite or quiz requirement |
| W11 pp31-39 and creative-app examples | Python controls creative applications | Moved/retained in W11 Blender/Godot; this week ends with retrieval as a reusable tool |
| W6 speech material | Input/output surrounding a bot | Retained/updated: typed input core, live offline TTS, recorded-audio fallback explicitly labeled; microphone optional |

## Implementation and evidence boundary

This revision changes teaching content and diagrams, not student application
behavior. It does not claim a new live model, D1, Qdrant or audio rehearsal.
Current operational commands are in the run sheet and PFAD `QDRANT-PIP.md` /
`VALIDATION.md`. The first hour now budgets two minutes for prepared
SQLite evidence and two for the D1 demonstration; longer edits and failure
experiments remain in the separate tutorial.

Peewee 4.5.3 maps the real User/Conversation/Message classes to SQLite, with
explicit FK enforcement, role/nonempty checks, compound history lookup index
and atomic two-row writes. Method→SQL→rows→fresh-process reload, ownership,
rollback and bounded chronological history are tested. No unsafe login scheme
or second app is introduced; local profile names are fictional, not authentication.

The official 2026/27 handbook was refreshed and re-embedded on 11 November
after its 10 November update: 137 pages, SHA-256
`43ac3a6a7697b2ce78f1964f673dae0aa2ccf79ba7c58fb310b469dc2b380a1b`.
Six short verbatim whitespace-normalized extracts from PDF 20, 25, 76 retain
section/printed-page mapping. A pinned MiniLM sentence encoder replaces the
short-context CLIP feasibility candidate:384D,masked-mean,L2-normalized,max 256tokens.
Real compatible passage/query fixtures rank all three inspected queries.
The fee row was shortened after a noisy table excerpt missed retrieval; ambiguous
leave-table columns were excluded rather than inventing their relationship.

The classroom route reuses Week 6 Pip, tool-capable LM Studio on loopback 1234,
the Qdrant service on 6333 and Kokoro. The earlier CPU CLI recordings below
are evidence for the alternate route only, not proof of a fresh Pip run.

Historical October route: local CPU Qwen3.5-2B Q4_K_M through llama.cpp b11972 on loopback 11440.
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

The revised deck uses the approved 120-minute run sheet, incumbent course
fonts/palette/layouts, reused Week 9 native comparison/rows/steps compositions,
deckgen.CODE, large primary diagram labels and substantive notes. An embedded
restart prediction, three discussion slides and a first-half recap keep the
conceptual quiz scope explicit. Repeated slides are merged/removed; shorter
titles keep the diagrams central. The latest requested additions replace the
text-only cardinality contrast with a one-to-one diagram, show many-to-many
links before junction rows, and follow related table IDs into SELECT/JOIN/UPDATE
examples with concrete results. The subsequent instructor refinement explains
query keywords immediately before the foreign-key example, and adds consistent
numbered section boundaries. These signposts and explanations bring the deck
to 59 slides. The subsequent ORM refinement pairs Python and generated SQL for
the three query forms and adds a prediction checkpoint, bringing the total to
61 while preserving the first-hour conceptual scope. The subsequent Semantle
refinement adds four introductory slides before the original numeric vector:
live word-similarity example, embedding definition, word-to-text comparison and
question/passage encoding diagram. Total: 65 slides; the first half is unchanged.
Detailed caveats stay
in speaker notes.
The second half connects the current PDF/compatible vectors/tool/
selected history/spoken output without repeating Week 7 constructors or Week 9
boundaries. The PFAD README budgets its own 120 minutes with break/recovery/tutor
support and supplies a conceptual revision section. Render/build/review evidence belongs in the private report;
source alone is not proof of visual readability.

No shared navigation/registration,root environment,official presenter,classes
or assessment policy was changed. Keep both PRs open; no merge/release is implied.
