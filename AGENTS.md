# SD5913 Content Authoring

Read [the course authoring guide](docs/COURSE-AUTHORING.md) before planning,
creating or reviewing a lesson. These instructions apply to the whole repo.

## Teaching contract

- Teach programming to artists, designers and game-design students. Python is
  the main language for explaining computing concepts; connect other tools to
  concepts students can inspect in code.
- Each normal teaching week has a **120-minute lecture and a separate
  120-minute PFAD tutorial**. Include breaks, setup, live demos, questions and
  transitions in those budgets. Week 13 is final quiz/revision and final
  tutorial/project support; do not add another content week.
- Agree the outline before producing a replacement lesson. Read the actual
  delivered material and its PFAD companion first. Check the 2025 archive for
  useful content and omissions; it does not determine current policy or APIs.
- Preserve verification over memorization: predict a result, trace the code,
  try a change, inspect a failure, explain the evidence. A tool tour and repeated
  project-planning prompts do not substitute for computing concepts.
- Build on what has already been taught. Do not spend another block teaching
  basic classes, two independent objects or generic MCP permission cards when
  the week's new subject is networks, databases or creative-tool integration.

## Materials and presentation

- Use the established course typography, palette and layouts. On the
  1920 x 1080 canvas, target at least **40 design pixels for primary diagram
  labels**. Make diagrams fill the slide; use consistent successive diagrams
  for complex explanations. Mark ordered workflows **1, 2, 3 with arrows**.
- Use short visible text and substantive speaker notes on every slide. Keep
  technical explanations in notes or separate slides. Use `deckgen.CODE` for
  code panels; do not shrink text to force a dense example onto one slide.
- Link runnable PFAD sources and show the exact launch command for live demos.
  Include expected output, the code being explained and a useful failure case.
  Capture real screenshots for UI instructions, identify the source/date, and
  enlarge the relevant action when needed.
- `pfad/weekNN/README.md` is the complete student/TA tutorial. It must work
  without the instructor's login or ClassPoint account. Tutorials explain setup,
  timed tasks, expected observations, edits, verification and troubleshooting.
- Keep news brief, dated, sourced and relevant to creative practice. News and
  frontier demos are refreshed near class, and are separate from quiz scope.
- Use current documentation for API/tool instructions and compatible pinned
  dependencies. Prefer simple `uv` commands. Never invent release versions,
  working integrations, measured results or classroom rehearsal evidence.

## Assessment and course boundaries

- Canvas is the submission system. Do not introduce new graded submissions,
  attendance/role requirements or assessment logistics without instructor
  approval. Group project: **40% of the course; 25% idea / 50% code / 25%
  execution; 6 December 2026, 23:59 HKT**.
- Each group uses a shared **public repository owned by `sd5913`**, with teammate
  write access. The [Project template](https://github.com/orgs/sd5913/projects/1)
  starts with **Use this template**. Check its actual title/UI before authoring;
  repository and Project permissions are separate.
  This is the recommended tracking route; an equivalent accessible shared
  planning/progress record remains valid under the project brief.
- Review weeks: 5, 12, 19 and 26 November, then 3 December. Tutors confirm exact
  times within allocated tutorial slots. These records support the existing
  execution criterion. Do not invent a compulsory project defence.
- Project connections are inspiration. Do not require camera input, AI,
  a specific engine, app-store publication, paid APIs, a GPU or robot hardware
  merely because a weekly demo uses them. State actual exercise prerequisites
  and supply a meaningful fallback.

## Working and review

- Work in an isolated feature checkout. Preserve other authors' changes and the
  union of accepted weekly registrations/navigation. Keep renderer fixes in
  Deckgen and student examples in PFAD; do not patch the engine into this repo.
- Keep a teaching/PFAD PR pair for each week, with precise cross-links. While
  the companion is unmerged, pin runnable-source links to its verified commit.
  An unmerged PR URL alone is not a student run instruction.
- Build HTML, PDF, plain and ClassPoint PowerPoint with overflow checking
  enabled; inspect renders at presentation size and rehearse real demos. Green
  tests and screenshots do not establish live camera, tool or classroom access.
- Review against the approved outline and
  [weekly integration rules](docs/WEEKLY-PR-INTEGRATION.md). Report what was
  tested, what was inspected and what still needs instructor rehearsal.
- Do not merge, publish course releases, change the official presenter, run a
  remote class or contact students/tutors as part of authoring draft content.
  Rosters, credentials, private answer keys and identifiable activity exports
  stay outside public repositories, PRs, artifacts and logs.
