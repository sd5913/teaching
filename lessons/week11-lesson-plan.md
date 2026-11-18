# Week 11: identity, deployment and creative tools

Thursday 19 November 2026. **120-minute lecture and separate 120-minute PFAD tutorial.**
The instructor's 18 November revision puts substantial authentication theory
first, followed by a real GitHub deployment walkthrough. After the break,
follow one Blender object through agent-assisted editing and into Godot.
Compare Week 9/10's concept -> diagram -> data/code -> demo/check teaching
pattern. Do not lead with protocol plumbing or a generic PR workflow.

## Lecture run sheet

| Minutes | Teaching work and observable result |
| --- | --- |
| 0-5 | Title; four dated news items 1-5, one minute each; brief agenda transition. Keep vendor claims attributed. |
| 5-14 | W10 stored User ID versus proof of caller; authentication versus authorization; registration versus login; password/passkey/session credentials. |
| 14-22 | Encryption versus password hashing; salted slow password verification; registration and login diagrams. Explain why the historical unsalted hash must not be copied. |
| 22-30 | Separate HTTP requests; session lifecycle; opaque versus signed sessions; readable signed payload; verified identity drives owner queries. |
| 30-38 | OAuth redirects/state/code, server exchange/PKCE/profile and our app session; browser/Worker/D1 topology. |
| 38-49 | Local/remote environment; real template and GitHub UI screenshots; create exercise repo, register OAuth App callback, configure eight repository secrets, inspect workflow and Run workflow. |
| 49-55 | Build/migrate/deploy distinctions; actual CI screenshot; save/reload/restart, two accounts and signed-out refusal; diagnose identity, permission and deployment failures. |
| 55-65 | Full break. |
| 65-74 | Actual Blender render; scene/object/mesh/material; transforms, centre/pivot and dimensions; calculate floor contact. |
| 74-85 | Embedded Blender Python; named collection lookup, property assignment, camera position/aim; save versus render; missing-object failure and recovery. |
| 85-97 | Give an agent a bounded visual goal; first proportion change; actual before/after; action/observation/revision versus a fixed script; API/CLI/MCP as interfaces. |
| 97-103 | Focused reviewer request on the same PR; rerender less width with everything else fixed; accept/revise/stop. |
| 103-115 | SAME saved Sculpture -> GLB -> Godot PackedScene/Node3D instance; axes, dimensions, pivot, material; actual two-application images; rendering versus collision. |
| 115-120 | Choose one tutorial route; 100-120 tutor/project support; project policy, then AMA at 118-120. |

Speaker notes supply explanations, predictions and exact sources. Primary diagram
labels remain at least 40 design pixels on a 1920x1080 canvas. Protect discussion
and application observations inside their blocks rather than adding demos later.

## Authentication: concepts before configuration

Week 10's local User/Conversation/Message rows were selected by a local operator.
A browser-supplied user ID is not proof of the caller. Authentication establishes
an identity; authorization checks its access to a resource on EVERY request.
The same handbook embedding index, retrieval, conversation memory and spoken
reply remain the accepted W10 dependency; login does not replace that work.

Explain local registration using a modern password library: a random per-password
salt, an expensive supported algorithm such as Argon2id, and stored verifier plus
parameters. A salt is not secret. A fast unsalted SHA-256 digest is unsuitable.
Login verifies a candidate; password reset does not recover the old plaintext.
The practical delegates credentials to GitHub instead of implementing passwords.

Compare opaque server-held sessions with the template's signed expiring payload.
Signing protects integrity, not confidentiality. The template verifies shape,
signature and expiry. Logout clears this browser's cookie; a copied valid cookie
remains usable until expiry without additional revocation. Do not claim a D1
session table or that signing encrypts the user fields.

Template pinned for this walkthrough:
https://github.com/sd5913/github-oauth-d1-template/tree/69cbed7363412daa4a7e8c2c8fc4ed02a3f1afa5 .
Reuse registry-derived implementation and its notices unchanged. Personal GitHub
OAuth App, not GitHub App/PAT/repo scope. Callback is APP_URL plus
`/api/auth/github/callback`; local origin is `http://127.0.0.1:3000`.
Use separate local/deployed Apps for clear environments; GitHub currently supports
multiple callbacks. Never project credential values.

Trace state -> callback validation -> server code/PKCE exchange -> GET /user ->
immutable numeric GitHub ID -> signed app session. Token is discarded after profile
verification. GET/POST `/api/note` uses session.githubId to filter notes.github_id;
POST accepts only a body string, max 2000 characters, and checks Origin. It cannot
accept an owner chosen by the browser. Inspect lib/handlers.ts and lib/session.ts.

## GitHub deployment walkthrough

1. Open the actual course template. Sign in, Use this template > Create a new
   repository under the student's personal exercise owner. This is separate
   from the required sd5913-owned group-project repository.
2. Register the personal OAuth App, exact local/deployed origin and callback.
   Follow the template README to prepare the student's Cloudflare Worker and D1.
3. Repository Settings > Secrets and variables > Actions > New repository secret.
   Enter the eight exact names below without projecting their filled values.
4. Actions > Deploy to Cloudflare. Inspect the source trigger and selected branch.
   The workflow supports push to main and manual workflow_dispatch. Run workflow
   is demonstrated by an attributed GitHub Docs screenshot; its illustrative
   Browser Tests title is explicitly different from our Deploy to Cloudflare.
5. Open jobs/steps for the actual run. Build creates an artifact, remote migrations
   prepare D1 schema, and deploy installs code/config/runtime secrets. Open APP_URL
   after success; check callback, storage persistence and ownership separately.

| Repository secret | Role |
| --- | --- |
| CLOUDFLARE_API_TOKEN | Actions deployment authority |
| CLOUDFLARE_ACCOUNT_ID | Deployment account |
| CLOUDFLARE_D1_DATABASE_ID | Remote DB binding ID |
| CLOUDFLARE_WORKER_NAME | Worker target name |
| APP_URL | Fixed application origin/callback |
| OAUTH_CLIENT_ID | Maps to runtime GITHUB_CLIENT_ID |
| OAUTH_CLIENT_SECRET | Maps to runtime GITHUB_CLIENT_SECRET |
| SESSION_SECRET | Runtime signing secret |

GitHub reserves the GITHUB_ prefix for Actions secrets; aliases are intentional.
The script uses an unlogged temporary secrets file and Wrangler --secrets-file.
Repository secrets do not automatically become runtime bindings. Local .dev.vars
and local D1 are separate from remote state. No live cloud deployment was run in
this authoring session. The actual template Checks run passed; its deployment is
unconfigured and skipped. Captures must not imply otherwise. Sources/licence:
`deck/assets/week11/github-screenshots-source.md`.

Acceptance on a configured app: A signs in, saves, reloads and restarts the same
server/storage; B in another profile sees only B's note and cannot change A's;
signed-out API requests fail. Mock provider/fixture checks are labelled local
checks and do not establish actual OAuth, connectivity or cloud permissions.
Diagnose callback mismatch, invalid state, missing runtime secret, wrong D1
binding/migration and missing owner filter as different boundaries.

## Blender and the same object in Godot

From PFAD/week11 create the unchanged baseline:

```bash
blender --background --factory-startup -noaudio --python-exit-code 1 --python blender_scene.py -- --scale 1.25 --output .output/blender/before
```

Read object/mesh/material and location/rotation/scale before the agent prompt.
The base cube side is 2; scale 1.25 gives side 2.5. Centre z1.25 means bottom 0.
The script runs inside Blender's Python, not uv's interpreter; do not pip-install
bpy. Camera aim is derived from target minus position. Saving .blend and rendering
PNG are distinct. --target MissingObject must fail nonzero before a new save/render;
restore Sculpture. An old PNG cannot establish a successful new run.

Give the full prompt in agent-pr-workflow.md. First proposed scale is
(1.6*s, .75*s, s); dimensions at s = 1.25 are (4,1.875,2.5). Let the agent inspect,
edit, run Blender, view JSON/PNG and revise from observations. Open a practice PR.
Human review requests x1.3*s with everything else fixed; revised dimensions are
(3.25,1.875,2.5). Update the SAME PR, rerender and judge. Actual lecture images
are author rehearsal from temporary source copies, not a model-session transcript.
Students retain their own real action/observation record or label partner fallback.
MCP is an optional tool interface; CLI also lets an agent use the application.

```bash
uv run python asset_handoff.py export .output/blender/revised/sculpture.blend
uv run python asset_handoff.py check
uv run python asset_handoff.py play
```

Export reads the saved revised scene, selects only Sculpture, preserves mesh/material,
normalizes bottom pivot and bakes scale in export memory without rewriting .blend.
GLB axis conversion maps Z-up to Y-up; no second manual 90-degree rotation. Godot
imports the GLB as a PackedScene and instantiates it under Node3D, with its own
camera/light/floor. Actual dimensions (3.25,2.5,1.875), bottom y = 0, identity instance
transform. Existing Node2D world is retained separately. Lighting differs; do not
claim pixel parity. Rendering does not create collision. Missing-source command
must fail clearly; recover with the actual saved source. Lecture capture provenance:
`deck/assets/week11/blender-godot-source.md`.

## Tutorial and course boundary

PFAD README provides a complete separate 120-minute route, auth first then Blender/
Godot. Students choose ONE, keep 55-65 break and 100-120 tutor/project support.
No ClassPoint/instructor login is needed. With setup blocked, use a prepared partner
and take turns; recording alone is not hands-on work. Linux Blender 5.3.0/Godot 4.7.2
were tested; Windows/macOS, classroom projection and actual student agent behavior
remain rehearsal checks. Week 12 retains its full bounded agent/check/revise/film
lesson; today's small asset import prepares it.

Group project stays 40%, rubric 25% idea/50% code/25% execution, due 6 December 2026
23:59 HKT. Public sd5913-owned group repo, teammates Write; GitHub Projects or an
equivalent accessible progress record. Canvas submission rules remain authoritative.
No new graded task or requirement to use today's tools.
