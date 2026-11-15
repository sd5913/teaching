# Week 11: agents, tools and evidence

Thursday 19 November 2026. **120-minute lecture and separate 120-minute PFAD
tutorial.** Teach exactly two cases, Blender and authenticated deployment.
Students choose one tutorial route. Godot sources are retained as Week 12 prep;
do not add a third Week 11 installation or change the Week 12 lesson.

## Lecture run sheet

| Minutes | Teaching work and observable evidence |
| --- | --- |
| 0-10 | Ask which result students would accept. Explain agent goal/action/observation/stop versus fixed script. Keep W10 handbook sources, conversation history, prompt and spoken reply distinct. |
| 10-35 | Actual Blender scale/camera renders, named object/property, CLI/API/process boundary and save/render distinction. Run one short render/failure; trace MCP discovery/call/result. Optional live bridge is preflight/tutorial work, not another unbudgeted lecture demo. |
| 35-55 | Worked camera PR: criterion, `agent/camera-study`, existing first-attempt renders/evidence note, reviewer request, second-camera revision, current comparison, relevant checks and human review/merge in same PR. |
| 55-65 | Full break. Close disposable Blender/bridge first. |
| 65-90 | Private project note: W10 local row is not login. Trace browser redirects/state, server code exchange/profile, signed session. Show personal OAuth App callback and eight repository setup names, including Actions-to-runtime aliases. |
| 90-110 | Session-derived `notes.github_id` owner filter; parameterized SQL; save/reload/restart; local versus remote D1; PR CI versus main/manual migration/deploy/runtime secrets; diagnose failures and second-account acceptance. |
| 110-120 | Complete PFAD tutorial handoff, one selected route, W12 prep, 100-120 tutor support, project boundaries and questions. |

Use substantive notes for explanations; keep diagrams visible while tracing.
Primary diagram labels stay at least 40 design pixels on the 1920x1080 canvas.
The prepared PR wording is a worked example, not a claimed public PR or live
agent episode. The actual rendered images retain source/date provenance.

## Sources and preflight

While companion PR #14 is unmerged, use its verified source revision:
https://github.com/sd5913/pfad/tree/e02fd99bc51c5df2b46c89eb4491b9da591b843d/week11 .
The integration owner refreshes this pin after reviewing the revised tutorial.
Template: https://github.com/sd5913/github-oauth-d1-template . Open its README
and real configuration UI; do not invent screenshots or project secret values.

Existing Blender environment checked 29 October: Blender 5.2.3 LTS,
`mcp-for-blender` 2.2.6, pinned community add-on `8782963`. The 15 November
camera revision rerendered with the same Blender version and unchanged course
scene. Windows/macOS and classroom projected display remain separate checks.

From the PFAD checkout, `cd week11`:

```bash
blender --background --factory-startup -noaudio --python-exit-code 1 --python blender_scene.py -- --scale 1
blender --background --factory-startup -noaudio --python-exit-code 1 --python blender_scene.py -- --scale 1.5
uv run python blender_variants.py
```

Inspect actual PNGs, `.blend` and `inspect.json`, not only a success message.
The script raises the cube center with scale to keep floor contact. Variants
use scale 1.25 and cameras `(7,-9,6)` and `(9,-7,6)`, both aimed at the same
target. Each folder has current camera coordinates and its own render.
A scene edit, saving a scene and rendering a PNG are separate operations.

Useful failure, expected nonzero before a new save/render:

```bash
blender --background --factory-startup -noaudio --python-exit-code 1 --python blender_scene.py -- --target MissingObject
```

Read `Missing object: MissingObject; use Sculpture`. Restore the target and
rerender; an old PNG does not establish that the failed run succeeded.

## Concrete PR sequence, 35-55

1. State the fixed acceptance criterion: two useful distinct views, no cropped
   sculpture; keep scale 1.25, sculpture/material/light/look target unchanged.
2. Create `agent/camera-study`. Ask the agent to inspect and render the supplied
   variants, then write a small credential-free evidence note. The first code
   already exists; do not ask the agent to recreate it. The note is the first
   PR diff. Retain exact source/command/current coordinate and render evidence.
3. Open one PR. Show the actual two supplied renders. Human review asks:
   “Keep the first pose and scene unchanged. Try second camera `(5,-10,6)`,
   aimed at the same target. Rerender both; attach the comparison to this PR.”
4. Revise only the second tuple in `blender_variants.py`. Commit to the same
   branch, rerun the helper, inspect both outputs/current JSON and review the
   updated diff. The new lecture image is actual CPU-rendered evidence; its
   provenance is `deck/assets/week11/camera-revision-source.md`.
5. Review relevant checks and the visual criterion. A human approves/merges;
   no agent/tool success message substitutes for that acceptance.

A configured coding agent is optional. A human-directed edit follows the same
observable workflow. Do not label the deterministic helper a live autonomous
run. For a live tool preflight/tutorial extension:

```bash
uv run python setup_blender.py
uv run python blender_live.py --verify
```

The community server/add-on drives a disposable window over stdio plus a
loopback socket; it is not an official Blender Foundation feature. Expect live
scale `[1.5,1.5,1.5]`, `blender_exit: 0`, `socket_closed: true` and actual
scene/image output. Interactive `uv run python blender_live.py` waits for
Enter before cleanup. No personal scene, model call or asset service is used.
The course-owned bounded CLI adapter is different:

```bash
uv run python mcp_client.py --blender list
uv run python mcp_client.py --blender render_scene '{"scale":1.25}'
uv run python mcp_client.py --blender inspect_scene
uv run python mcp_client.py --blender render_scene '{"scale":5}'
```

The last request must return `isError: true` before launch. `inspect_scene`
reads saved JSON; community `get_scene_info` reads a live scene. Process exit,
current state and visible composition supply different evidence.

## Personal OAuth App and configuration, 65-90

The student owns a personal GitHub OAuth App and Cloudflare account. This is
sign-in, with no PAT, `repo` scope or installable GitHub App. Week 10 fictional
User IDs were local database identity, not proof of the requesting person.

Open https://github.com/settings/applications/new in the real UI. For local
work set Homepage URL `http://127.0.0.1:3000` and callback
`http://127.0.0.1:3000/api/auth/github/callback`. For deployed work use the exact
HTTPS `APP_URL` and same path. Separate local/deployed apps are an easy teaching
route; do not claim only one callback is supported by GitHub.

The app starts at GET `/api/auth/github`: create random state, remember it in
a protected short-lived cookie, redirect to GitHub. Callback state must match
before server exchange; wrong/missing/expired state or denied authorization
must not create a session. The template also uses PKCE: a verifier remains in
the protected flow state, a challenge goes to GitHub, and exchange proves the
verifier. Teach its purpose briefly; detailed crypto is not quiz syntax.

The Worker exchanges the temporary code, verifies the authenticated GitHub
profile and issues its own signed expiring HttpOnly/SameSite session cookie
(Secure under HTTPS). A signature detects tampering; it is not encryption.
Do not put access tokens/private note text in cookies. The GitHub token is used
for identity, then discarded. Later requests verify our session on every API
call; POST mutation also checks Origin. Logout clears the cookie.

All **eight** repository secret names go in Settings > Secrets and variables >
Actions > Repository secrets:

```text
CLOUDFLARE_API_TOKEN
CLOUDFLARE_ACCOUNT_ID
CLOUDFLARE_D1_DATABASE_ID
CLOUDFLARE_WORKER_NAME
APP_URL
OAUTH_CLIENT_ID
OAUTH_CLIENT_SECRET
SESSION_SECRET
```

Some are public identifiers, but the classroom uses one setup location.
GitHub reserves names starting `GITHUB_`. The deployment workflow maps
`OAUTH_CLIENT_ID` to runtime `GITHUB_CLIENT_ID` and `OAUTH_CLIENT_SECRET` to
runtime `GITHUB_CLIENT_SECRET`; `SESSION_SECRET` keeps its name. It writes the
three values to an unlogged temporary file and deploys with Wrangler
`--secrets-file`. A repository secret alone is not a Worker runtime binding.
The deployment token remains in Actions; the browser receives none of these
secret values. Never project or paste filled values into prompts/source/logs.

## Template demo and failures, 90-110

From a fresh repository created with **Use this template**, follow its README.
Copy `.dev.vars.example` to ignored `.dev.vars` and fill the three runtime
names locally. Optional `.env.example`/ignored `.env` holds public configuration.

```bash
npm ci
npm test
npm run typecheck
npm run build
npm run db:migrate:local
npm run dev
```

Open `http://127.0.0.1:3000`. The documented `npm run deploy` path and
main/manual Actions deployment require the student's Cloudflare/config values.
PR checks use no deployment credentials. The Actions deploy job applies remote
D1 migrations, then deploys code plus OAuth/session runtime secrets. A local
migration/test does not establish the remote database or actual GitHub flow.

Trace `lib/handlers.ts`, `lib/session.ts` and `migrations/0001_notes.sql`:
GET/POST `/api/note` verifies session; POST accepts only `{ "body": "..." }`
(up to 2000 characters); owner comes from `session.githubId`. Parameterized D1
queries select/upsert `notes.github_id`; the client cannot choose an owner.
The SQL slide includes the required `updated_at`; inspect the full route and bindings.

Use a harmless invented note. Save, reload, stop/restart the same local server
without deleting local D1 state, and read again. D1 row persistence is distinct
from session lifetime and live server memory. Then use two separate browser
profiles/accounts: B gets its own empty/note state, B's save leaves A's note
unchanged, and sign-out makes the note API refuse anonymous access.

Diagnose by boundary:

| Observation | Inspect |
| --- | --- |
| Callback mismatch | Exact APP_URL, environment and personal OAuth App callback |
| Invalid state | Fresh initiating browser flow/cookie; begin again, do not disable state |
| Missing runtime credential | Actions alias mapping and deploy secrets file step |
| Missing table/binding | Local versus remote D1, configured ID and applied migration |
| Another user's note | Stop using real data; inspect server session-derived query filters |
| Green CI but failed sign-in | CI mocks versus real GitHub/Cloudflare configuration |

Template tests label mock OAuth and include state/session/ownership failures.
Its built-Worker/local-D1 check uses fixture sessions to verify actual local
storage and restart. That is not real GitHub acceptance. Actual OAuth,
Cloudflare deployment, two-account isolation and projected-browser rehearsal
need the student's configured services; record those gaps honestly.

## Separate tutorial and project boundary

The PFAD README is the complete timed student/TA guide, independent of instructor
login/ClassPoint. Choose Blender **or** authentication, keep its 55-65 break,
and reserve 100-120 for the 19 November tutor review/project support. If setup
blocks, use a prepared partner and take turns; a recording alone is not hands-on
practice. Godot remains supplied as Week 12 preparation, with existing first-time
setup/orientation at 0-20 and prepared partner handoff at minute 20.

No new upload/grade/defence. Group project: 40%, rubric 25% idea / 50% code /
25% execution, due 6 December 2026 at 23:59 HKT. Public sd5913-owned group
repository with teammate Write access; personal OAuth App ownership does not
change this. Projects is recommended or equivalent accessible progress record.
Canvas instructions govern submission. No requirement to use today's tools.

## Current documentation and verification boundary

Checked through Context7 and primary sources on 15 November 2026:

- https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps
- https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app
- https://docs.github.com/en/rest/users/users#get-the-authenticated-user
- https://docs.github.com/en/actions/reference/security/secrets#naming-your-secrets
- https://developers.cloudflare.com/workers/configuration/secrets/#upload-secrets-alongside-code
- https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/
- https://developers.cloudflare.com/d1/reference/migrations/
- https://developers.cloudflare.com/d1/worker-api/prepared-statements/
- https://docs.blender.org/api/current/info_quickstart.html

Preserve existing engine/bridge notices and licensing; Blender is GPL, the
community bridges and MCP SDK are MIT. No downloaded artwork. Crosswalk and
knowledge ledger: `week11-planning.md`. Detailed test/build/render evidence
and remaining classroom/live checks live in the private integration report.
