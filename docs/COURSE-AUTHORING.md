# Course authoring guide

This guide records the teaching standard established by the 2026 lessons,
especially the Week 7 classes demonstration and the Week 8 teamwork, delivery
and computer-vision lesson. It is a reusable brief for authors and reviewers,
not a fixed slide count or a requirement to repeat their subject matter.

The audience is artists, designers and game-design students learning to
understand and verify software, including software produced with AI tools.
Use games, apps, installations and creative workflows as concrete contexts.
Explain the computing ideas that let students make decisions about those tools.

## 1. Establish the lesson before authoring it

Read the instructor's current request, accepted course plan, actual earlier
decks, relevant PFAD READMEs and the existing draft PR pair. Inspect what was
taught, rather than relying on a future draft's recap. Read the corresponding
2025 slides and examples if available. Maintain a concept crosswalk recording
the original slide/page or example, its 2026 destination, and whether it is
retained, updated, moved or removed. Read adjacent weeks for dependencies.
Current instructor decisions override historical scheduling.

Preserve the planned progression, not just isolated topics. In the later-week
sequence, objects/classes lead to persistent relational models; handbook PDF
embeddings lead to source-backed retrieval/RAG; an agent combines that knowledge
with conversation memory and tool use, then produces a spoken reply. Indexed
handbook knowledge and the history of a conversation are different sources of
context; explain what each contributes.

Preserve the approved concepts, not every original framework or visualization.
Record instructor-approved removals or redistribution in the source crosswalk.
Orange is deliberately removed to give Blender/Godot more time; do not restore
visual exploration as a mandatory dependency of embeddings or agents. Replacing
an outdated installation does not authorize other conceptual deletions. Include
proposed substantive scope changes in the outline for agreement; an audit's
recommendation or an omission in a draft is not approval to remove a concept.

Prepare an outline for agreement containing:

1. Three or four learning outcomes expressed as things students can explain,
   predict, inspect or build.
2. The new computing concepts and the earlier knowledge they build on.
3. A 120-minute lecture run sheet and a separate 120-minute tutorial route.
4. A concrete live demonstration, its source and command, and its failure case.
5. A student tutorial outcome that can be observed and checked.
6. Prerequisites, external services, costs and a fallback that retains learning.
7. Explicit quiz scope, optional inspiration and links to the group project.

Get agreement on substantive changes to the teaching arc before producing the
replacement decks. Do not use that checkpoint to repeatedly reopen already
approved details. When several weeks are authorized together, use one agreed
sequence with a named author for each week and cross-week review.

Maintain a small knowledge ledger in the planning material: **already taught /
reused now / new this week**. Classes and methods can explain a camera, network
client or persistence object without repeating the original Ball lesson.

## 2. Plan time for teaching, not only slides

A normal lecture lasts 120 minutes including its break. This is an adaptable
starting allocation, not a script to impose on every topic:

| Minutes | Purpose |
| --- | --- |
| 0-10 | Project-facing opening question, short sourced news and relevant recap |
| 10-30 | First concept sequence with diagrams and a code prediction |
| 30-50 | Worked code and live demonstration |
| 50-60 | Inspect a failure and check understanding |
| 60-70 | Break |
| 70-90 | Second concept sequence and deeper demonstration |
| 90-110 | Apply, compare and verify; discuss project possibilities |
| 110-120 | Questions, key ideas and PFAD tutorial handoff |

Budget actual terminal/UI work and questions. Repeating six bullets about
planning does not fill a missing half-hour. Conversely, do not add ten libraries
to occupy two hours. Prefer a small system explained in depth.

The separate tutorial has its own setup, break, exercises, recovery time and
tutor-review/project-support allocation. Show that allocation in its README.
Coordinate weekly tutor deliveries with the allocated tutorial slot; do not
invent extra appointments or crowd out the advertised hands-on material.

Week 13 has a different job: final quiz/revision and final tutorial/project
support, including recovery for unfinished work. Confirm actual Canvas quiz
timing with the instructor; do not infer it from the 2025 archive or add a new
defence, graded presentation or software stack.

## 3. Teach concepts through a system students can trace

For each major concept, provide a representation, a concrete code path, an
observable result and a useful question or failure. For example, a networking
block should let a student follow a message through client/server roles and
explain what happens when the server stops. A relational database block should
build on meaningful classes such as User, Account, Message or SaveFile. Trace
model methods to stored fields/relationships, SQL and a fresh-process reload.
Clarify that values and relationships persist; Python methods remain code.

An embeddings block needs real model-derived numerical vectors and observable
similarity-search results. Link handbook chunks to source IDs/text/page metadata,
distinguish similarity from exact database lookup, and inspect retrieval before
generation. Preserve corpus/encoder identity, dimension and provenance across
the retrieval handoff. A sourced vector fixture can support an honest fallback;
keyword matching cannot stand in for embeddings.

For the handbook agent, distinguish the indexed PDF knowledge from conversation
history. Show which previous turns are retained or recalled, then trace retrieved
sources, conversation context and tool results into the answer and spoken reply.
Conversation memory is not automatically another embedding index, and audio
playback is a separate result to verify from the answer's correctness.

Introduce terminology in plain language, then use the correct technical term.
Ask students to predict outputs, distinguish two mechanisms, locate a fault,
or decide whether a result meets the stated behavior. Explain the relevant
objects, method calls, data shapes, state and boundaries as they occur.

Keep these distinctions clear:

- A framework/tool versus the computing concept it implements.
- A deterministic workflow versus an agent choosing actions from observations.
- Source code, running process, stored state and displayed result.
- A successful unit test versus a working integrated experience.
- Core concepts for revision versus dated news and optional frontier examples.

The project connection is a question such as "Could this help your project?"
rather than a new requirement to integrate this week's library.

## 4. Preserve the visual language

Use existing course fonts, colors, spacing and Deckgen layouts. Give one
relationship or action the slide wherever possible. Primary node/arrow labels
should be at least 40 design pixels on the 1920 x 1080 canvas. Number sequences
1, 2, 3 with arrows and maintain geometry as a diagram develops across slides.

Do not replace concrete diagrams with repeated generic boxes labeled input,
process and output. Show the actual message, record, object or tool request.
Use legible code excerpts with `deckgen.CODE`; split an example when needed.
Some existing Week 7/8 helpers manually enlarge code. Treat those as local
exceptions, not a second font standard to propagate into every new lesson.
The slide is what the room can read quickly; speaker notes carry the argument,
definitions, demo instructions, questions, sources and expected observations.
Every slide needs useful notes.

Screenshots are useful for actual UI steps and observed results. Capture the
real current interface, cite its source/date, crop irrelevant space and enlarge
the relevant control. Surrounding explanatory labels must remain readable.
Link the screenshot or a visible label to the actual page. Avoid rebuilding a
fictional UI when a real public example is available. Refresh screenshots when
an instructor's changes make the instruction inaccurate.

## 5. Produce the complete material set

| Material | Job |
| --- | --- |
| `deck/weekNN.py` and focused helpers | Lecture concepts, diagrams, questions and notes |
| `lessons/weekNN-lesson-plan.md` | Timed instructor run sheet, commands, preflight and fallback |
| `lessons/weekNN-planning.md` | Outcomes, prerequisites, prior-knowledge ledger and decisions |
| `lessons/weekNN-news-YYYYMMDD.md`, when news is used | Dated sources, claim limits and discussion prompt |
| PFAD `weekNN/README.md` | Complete timed two-hour student/TA tutorial |
| PFAD examples, assets and dependency files, for technical teaching weeks | Runnable exercises and meaningful behavior checks |
| PR descriptions | Paired links, outcomes, validation and remaining rehearsal needs |

Use separate helpers when they make a concept or diagram easier to maintain.
Do not duplicate the renderer. Keep staff run sheets out of public site
navigation, and keep private assessment keys out of the public repo entirely.
For Week 13, supply a revision/quiz run sheet and a timed final-support README
that refers to existing examples. It does not need a new demo, dependency
environment or feature exercise to satisfy this material list.

While a companion PR is open, pin lecture source links to its verified commit.
Check both the link target and the command: a working file URL does not prove
the example runs. Once integration is authorized, preserve all accepted deck
registrations, navigation links and PFAD course-index entries.

## 6. Verify current tools and practical access

Check current primary documentation for library/API/CLI instructions. Pin a
compatible set of Python, dependencies and model/assets where needed. Record
the versions actually tested; do not substitute a plausible future version.
Use `uv` for Python environments and keep student commands simple. A weekly
environment can be isolated from an incompatible PFAD root project.

Core tutorial work should not depend on the instructor's accounts, a private
device, a real deployment token, paid generation or specialist hardware.
State any actual prerequisites. Provide deterministic fixtures, a local
simulation or another meaningful fallback, and distinguish its coverage from
the live system. Do not describe a trace replay as a live agent.
Rendering a film still requires a verified graphics path, even when no
dedicated GPU or model inference is required. Document that prerequisite and
the recorded-frame/partner-machine alternative honestly.

Rehearse network demos alongside the presenter and other required services;
check ports and bind addresses. Exercise disconnects, malformed/missing data,
stale state and timeouts where relevant. Never expose a local tool bridge to
the network merely to simplify a demo.

For new tool integrations, verify startup, discovery, a useful action, the
result in the target application, and cleanup. Check student-platform support.
State whether an MCP server is official or a third-party project. A server
import or protocol smoke test is not an acceptance test for Blender or Godot.

## 7. Preserve assessment and project policy

Use the [current reviewed PFAD group-project brief](https://github.com/sd5913/pfad/blob/4358b4e47b874ef40c120e63b2f6329acbe9b7d5/assignments/group-project.md).
This source is pinned while its PR is open. Refresh the link to the accepted
live-branch version after authorized integration. Do not silently derive policy
from older drafts.

The current group project is 40% of the course grade, with its mark divided
25% idea / 50% code / 25% execution. Final deadline: 6 December 2026, 23:59 HKT.
Groups use public repositories owned by `sd5913`, with teammate write access.
The course [GitHub Project template](https://github.com/orgs/sd5913/projects/1)
uses **Use this template**; check its current name rather than assuming a
previous screenshot's title is permanent. Project access is configured
separately from repository access.
GitHub tracking is recommended; an equivalent accessible shared planning and
progress record remains valid. Do not turn use of a particular board into a
grading requirement.

Tutor reviews cover the class weeks of 5, 12, 19 and 26 November and 3 December;
tutors confirm meeting times in allocated tutorial slots. Usable increments,
evidence, feedback and next goals support the existing execution criterion.
Raw card/commit counts, formal Scrum roles and ceremony attendance do not
determine it. No additional Canvas upload is introduced by this record.

## 8. Review and hand off

A week is ready for instructor review when:

- Its outline, core concepts and full 120 + 120 minute budgets match.
- All required tutorial examples have documented, checked commands and expected
  results, with meaningful failure/recovery paths.
- Current sources and versions support the technical claims.
- The relevant automated checks pass; new tests verify behavior rather than
  mirroring prose, slide counts or arbitrary keywords.
- HTML, PDF and both PowerPoints build with overflow checks enabled; changed
  slides and diagrams have been inspected at presentation size, including the
  actual PDF. Sources, hyperlinks and notes survive export.
- Demo evidence distinguishes offline tests, live tool checks and physical
  classroom rehearsal. Any remaining instructor-only checks are listed.
- The teaching/PFAD PR pair is cross-linked, conflicts and shared-file changes
  are reconciled, and the PR description explains the final material set.

Apply the new-concept/demo/example checks to technical teaching weeks. For
Week 13, check revision scope, the confirmed quiz schedule, support triage,
existing run instructions and the final delivery checklist instead. Its final
support tutorial still has a 120-minute allocation; do not invent a new
practical or publish private quiz questions/answers to satisfy this checklist.

Use [the integration checklist](WEEKLY-PR-INTEGRATION.md) for an authorized
combined build. Do not claim individual PR checks establish cross-week
integration. Do not merge or switch the official presenter while preparing
drafts. Leave the instructor one coherent, reviewable set.
