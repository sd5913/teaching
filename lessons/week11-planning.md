# Week 11 redesign and source crosswalk

Current instructor direction:18 November 2026, for19 November. Authentication theory
and visible GitHub deployment first; Blender Python and asking an agent to operate
the application second; SAME saved object imported into Godot. This supersedes the
15 November tool-first draft and its blanket deferral of Godot. The new Godot work
is a small asset handoff within Blender, not a third tutorial or replacement for W12.

See [the run sheet](week11-lesson-plan.md) for timing, exact config, demos and limits.
Follow the accepted W9/W10 pattern: define -> diagram -> data/code -> demo/check.
Full120-minute lecture and separate 120-minute tutorial;55-65 break in both, 100-120
tutorial project/tutor support. Four dated news items stay inside the opening 1-5.

## Outcomes and progression

1. Separate stored record identity from authentication and authorization.
2. Explain registration, salted slow password hashing, login verification and
   session lifecycle; compare opaque and signed sessions accurately.
3. Trace GitHub state/code/PKCE/profile into an app session and server-derived
   D1 owner query; follow the actual GitHub configuration/Actions deployment path.
4. Explain Blender object/mesh/material/transform/camera/save/render concepts;
   ask an agent to inspect, edit, use Blender, observe and revise with a clear stop.
5. Export the SAME saved Sculpture to GLB, instantiate it in Godot and check
   axes/dimensions/pivot/material while separating visible mesh from collision.

| Prior learning | Reuse and extension |
| --- | --- |
| W7 classes, objects, methods, state/views | Named scene objects and transforms versus mesh/material; same object in different views/apps |
| W8 branch/PR/check/review and cloud dev | Focused visual goal, same-PR revision; deployment is separate from a prepared coding workspace |
| W9 processes/requests/server authority | Blender embedded Python/CLI/tool boundaries; browser/Worker/GitHub/D1 roles |
| W10 User/Conversation/Message persistence | User row is not caller proof; verify session then scope owner queries; fresh-process persistence |
| W10 handbook embedding retrieval/memory/spoken reply | Same corpus/index and knowledge path retained; identity and creative tool action extend the agent |

## Reuse and sources

- Course layout: existing week09_layouts and Week 10 concept/diagram/code/demo sequence.
- PFAD: existing blender_scene.py, variants, bounded tools and pinned community bridge;
  reuse world.engine() for a separate small Godot3D preview. No replacement 2D world.
- Template pinned69cbed7363412daa4a7e8c2c8fc4ed02a3f1afa5. Registry-derived session/
  owner-query implementation and notices retained; no new credentials subsystem.
- Actual GitHub public repository captures and attributed GitHub Docs control images.
  Production deployment is unconfigured/skipped; screenshots never claim otherwise.
- Actual Blender/Godot renders18 November; temporary source variants label author rehearsal,
  not a model transcript. Student agent prompt permits real CLI operation and image review.
- Password concepts restore2025 Week 10 slides39-43 and Week11 slides13-14, modernized
  to a per-password salt and slow supported password library; never copy old unsalted code.

## Source-to-lesson crosswalk

Historical references are 1-based PDF pages of the 78-page 2025 Week 11 PDF.
Its PPTX has 79 slides; numbering differs after the extra slide 31. The accepted
crosswalk is retained, with the instructor-approved redistribution recorded.

| Historical/accepted source | Status | 2026 destination |
| --- | --- | --- |
| W11 pp4-17 objects/storage recap | Reused, shortened | Scene/property/save/render; W10 owner-query and restart concepts reused in D1 |
| W11 p22; W10 retrieval/Pip | Retained dependency | Same handbook embedding space, source-backed retriever, conversation history and spoken reply; opening handoff, no replacement corpus |
| W11 pp18-30 Orange/t-SNE/projection | Removed by instructor | No Orange/matrix/projection requirement; explicit scope decision retained |
| W11 pp31-33 Python-enabled Blender | Updated | Scene/object/mesh/material and transforms, actual bpy inspect/change/save/render, API/process boundaries |
| W11 pp34-39 multi-angle dataset | Retained/updated | Camera position/aim, optional two-view loop; main task is agent-assisted proportions/review, then same asset to Godot |
| W11 pp40-44 TouchDesigner/Python | Retained as extension | Linked archive; operators/data mapping, no extra install |
| W11 pp45-48 NDI | Retained as extension | Networked audio/video contrasted with named tools/control messages |
| W11 pp49-55 MediaPipe/OSC | Moved/retained | W9 vision-to-message bridge; optional W11 archive extension |
| W11 pp56-60 physics server/clients/async | Moved/retained | W9 server-owned state; creative application owns its scene, Worker owns authorization |
| W11 pp61-78 tutorial/project update | Updated | Complete two-route timed PFAD README; 19 November tutor support; no new assessment |
| Accepted W11 Godot world/bridge/check/failure/capture | Moved by instructor, 15 November | Existing2D world preserved for W12; instructor18 November adds small Blender GLB -> Node3D preview in W11; W12 full agent/check/revise/film unchanged |
| W10 local account rows / registry auth architecture | Extended with approval | Personal OAuth App, server session, D1 private note, CI/deploy/credential boundaries; no roster features |

Archive source inspected in the accepted plan: PFAD `origin/2025` at
`512edb07927c5d77cacc7279ba6be601b33dc601`, Week 11 README/ARCHITECTURE,
OSC demo and Blender datasetbuilder inventory. The archive has no standalone
Python file for its embedded Blender script. Current W10 and W12 planning/decks
were read before this revision. No W12 source is modified here.

## Current evidence and boundaries

Current primary documentation checked through Context718 November: OWASP password/
session guidance, GitHub OAuth/App creation/Secrets/workflow_dispatch, Cloudflare
runtime secrets/D1 deployment, Blender Python and Godot GLB/scene instantiation.
Exact URLs and attribution are in notes and asset manifests. The verified companion
pin in deck/week11.py is refreshed after integration; no floating-branch claim.

Linux Blender 5.3.0/Godot 4.7.2 outputs, actual engine import/instantiation, source
preservation and size/material/floor checks support the new handoff. Bridge earlier
acceptance used 5.2.3. No live model episode, live OAuth/cloud deployment, private
account capture or student data is claimed. Classroom projection/Windows/macOS
remain manual checks. Mock OAuth and local fixtures are clearly labelled.

Orange/t-SNE remains removed by instructor. Public sd5913 group repo,40% project,
25/50/25 rubric and 6 December 2026 23:59HKT deadline remain. Canvas is submission;
GitHub Projects recommended or equivalent accessible progress record.
