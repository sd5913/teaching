# Week 11: agents, Blender and authenticated applications

Approved direction: 15 November 2026, for 19 November. The instructor has
approved exactly two cases: Blender through the existing PFAD examples, and
authentication/deployment through `sd5913/github-oauth-d1-template`, adapted
from the existing registry. Personal GitHub OAuth Apps are confirmed. This
supersedes the earlier Week 11 Blender/Godot allocation. The lecture lasts
120 minutes; the separate 120-minute tutorial completes one selected case.
Godot practical work remains supplied as Week 12 preparation.

## Outcomes and knowledge ledger

Students should be able to:

1. Explain a goal, available actions, observation, revision and stopping rule;
   distinguish a fixed tool script from an agent choosing the next action.
2. Trace a Blender property change through API/CLI/MCP boundaries to a saved
   scene and actual render, then review a focused camera change in one PR.
3. Trace browser redirects, state validation, server code exchange and a signed
   session into a server-derived owner filter on a persistent D1 note.
4. Distinguish repository setup values, runtime bindings, credential-free PR
   checks, deployment and credential-dependent live acceptance.

| Already taught | Reused here | New this week |
| --- | --- | --- |
| W7 objects, methods, state and multiple views | Named scene object/property; code versus stored values | Application-owned scene state, saved scene and camera render |
| W8 focused changes, branch/PR/check/review | A criterion, diff, evidence, reviewer request and revision | Actual Blender evidence; same workflow applied to deployment |
| W9 processes/messages and server authority | CLI/stdio/socket/request/result | API/CLI/MCP boundaries in a creative application |
| W10 fictional local User/Conversation/Message rows | Parameterized owner filters and persistence/restart | Authenticated GitHub identity, signed session and per-request authorization |
| W10 handbook embeddings/retriever/memory/spoken reply | Same source-backed knowledge path; tool result as context | An external creative action is a different kind of tool; login does not replace retrieval |

## Lecture and separate tutorial

| Lecture minutes | Work |
| --- | --- |
| 0-10 | Agent goal/action/observation/stop; fixed workflow distinction; W10 handoff |
| 10-35 | Existing Blender scale/camera scene, API/process/save/render; failure; concise MCP trace |
| 35-55 | Concrete camera PR: acceptance, branch, initial renders, reviewer request, revision, checks and human merge |
| 55-65 | Break |
| 65-90 | Private-note brief; local rows versus identity; OAuth redirect/state/server exchange/session; personal OAuth App; credential locations |
| 90-110 | D1 owner key/query, reload/restart, PR CI versus deployment, failures and second-account isolation |
| 110-120 | Choose one tutorial route, Week 12 preparation, project support/policy and questions |

The PFAD tutorial has its own 120-minute allocation and 55-65 break. Students
choose Blender or authentication; 100-120 remains scheduled tutor/project
support. A student does not need both applications or the instructor's login.
Blender uses existing scene/variants/tool examples. Authentication uses the
separate template, students' personal OAuth Apps and Cloudflare accounts. If
setup fails, preserve useful code/test tracing and use a prepared partner or
choose Blender; mock OAuth does not establish working GitHub sign-in.

## Worked PR and concrete evidence

The supplied `blender_variants.py` already renders `(7,-9,6)` and `(9,-7,6)` at
scale 1.25. The first branch task asks an agent to inspect/render the existing
code and add a small credential-free evidence note, not to recreate the same
function. The first PR diff is that note. Acceptance: keep scale, sculpture,
material, light and look target fixed; output two uncropped camera views in
separate folders. The reviewer asks the second view to show more front and less
side; increasing the angular separation between the two cameras is not the goal.

Worked reviewer request: keep the first pose and scene unchanged; try second
camera `(5,-10,6)` aimed at the same target; rerender and attach the comparison
to the same PR. The revision changes only the second coordinate pair. The
reviewer inspects diff, recorded camera coordinates and actual images, then a
human approves/merges after relevant checks. The source/images are real; the
brief/reviewer wording is an instructional example, not an invented public PR
or a claimed live autonomous episode. New render provenance is in
`deck/assets/week11/camera-revision-source.md`.

## Authentication case and exact contract

Template: https://github.com/sd5913/github-oauth-d1-template . Reuse source:
registry `531980151fd4aa1e37baacdc9223e4f69d61721c`, retaining its
Vinext/React/Vite, Worker/D1 and Web Crypto session approach while removing
roster/assessment/admin features. Preserve provenance and upstream notices.
Week 10's fictional local profile IDs were database identities, not login.
The template confirms a GitHub numeric ID and uses it as the note owner key.
It never trusts an owner ID from the browser or stores a GitHub access token.

Local app: `http://127.0.0.1:3000`. Callback:
`APP_URL` plus `/api/auth/github/callback`. Use the exact configured URL for
each demonstrated environment; separate local and deployed personal OAuth Apps
make environment ownership clear. No PAT, repo scope or installable GitHub App.

| Repository secret name | Destination/purpose |
| --- | --- |
| `CLOUDFLARE_API_TOKEN` | Actions deployment authorization |
| `CLOUDFLARE_ACCOUNT_ID` | Deployment account |
| `CLOUDFLARE_D1_DATABASE_ID` | Generated D1 binding configuration |
| `CLOUDFLARE_WORKER_NAME` | Worker configuration |
| `APP_URL` | Fixed public app origin/callback configuration |
| `OAUTH_CLIENT_ID` | Mapped to runtime `GITHUB_CLIENT_ID` |
| `OAUTH_CLIENT_SECRET` | Mapped to runtime `GITHUB_CLIENT_SECRET` |
| `SESSION_SECRET` | Runtime session/state signing secret |

All eight go in repository Settings > Secrets and variables > Actions.
GitHub reserves secret names beginning `GITHUB_`; the aliases are deliberate.
Some values are public identifiers, but one repository-secrets setup route is
the approved classroom flow. Actions writes an unlogged temporary secrets file;
`wrangler deploy --secrets-file` installs the three OAuth/session bindings in
the Worker. Storing a repository secret alone does not install a runtime secret.
Locally, copy `.dev.vars.example` to ignored `.dev.vars` for the runtime names;
optional `.env.example`/`.env` holds public build configuration.

Routes: GET `/api/auth/github`, GET `/api/auth/github/callback`, POST
`/api/auth/logout`, GET/POST `/api/note`. Notes accept only `{ "body": "..." }`,
at most 2000 characters. `lib/handlers.ts` verifies state/profile/session,
request origin and schema, and binds `session.githubId` in every note query.
`lib/session.ts` signs/verifies expiry; `migrations/0001_notes.sql` stores one
row per `notes.github_id`. The SQL panel includes the timestamp required by the schema; the surrounding
route handles session/origin checks and binds the verified owner ID.

## Source-to-lesson crosswalk

Historical references are 1-based PDF pages of the 78-page 2025 Week 11 PDF.
Its PPTX has 79 slides; numbering differs after the extra slide 31. The accepted
crosswalk is retained, with the instructor-approved redistribution recorded.

| Historical/accepted source | Status | 2026 destination |
| --- | --- | --- |
| W11 pp4-17 objects/storage recap | Reused, shortened | Scene/property/save/render; W10 owner-query and restart concepts reused in D1 |
| W11 p22; W10 retrieval/Pip | Retained dependency | Same handbook embedding space, source-backed retriever, conversation history and spoken reply; opening handoff, no replacement corpus |
| W11 pp18-30 Orange/t-SNE/projection | Removed by instructor | No Orange/matrix/projection requirement; explicit scope decision retained |
| W11 pp31-33 Python-enabled Blender | Updated | Actual bpy inspect/change/save/render, API/process boundaries |
| W11 pp34-39 multi-angle dataset | Retained/updated | Two controlled camera variants and concrete agent-assisted PR revision; no generated mesh requirement |
| W11 pp40-44 TouchDesigner/Python | Retained as extension | Linked archive; operators/data mapping, no extra install |
| W11 pp45-48 NDI | Retained as extension | Networked audio/video contrasted with named tools/control messages |
| W11 pp49-55 MediaPipe/OSC | Moved/retained | W9 vision-to-message bridge; optional W11 archive extension |
| W11 pp56-60 physics server/clients/async | Moved/retained | W9 server-owned state; creative application owns its scene, Worker owns authorization |
| W11 pp61-78 tutorial/project update | Updated | Complete two-route timed PFAD README; 19 November tutor support; no new assessment |
| Accepted W11 Godot world/bridge/check/failure/capture | Moved by instructor, 15 November | Existing PFAD files preserved as preparation; existing W12 0-20 first-time setup and prepared-partner handoff, then bounded agent/check/revise/film |
| W10 local account rows / registry auth architecture | Extended with approval | Personal OAuth App, server session, D1 private note, CI/deploy/credential boundaries; no roster features |

Archive source inspected in the accepted plan: PFAD `origin/2025` at
`512edb07927c5d77cacc7279ba6be601b33dc601`, Week 11 README/ARCHITECTURE,
OSC demo and Blender datasetbuilder inventory. The archive has no standalone
Python file for its embedded Blender script. Current W10 and W12 planning/decks
were read before this revision. No W12 source is modified here.

## Sources, versions and evidence limits

Current documentation fetched through Context7 on 15 November: GitHub OAuth
App web flow/state/code exchange; Cloudflare Wrangler remote D1 migrations;
`wrangler deploy --secrets-file` runtime installation. Exact primary URLs are
in the run sheet and relevant slide notes. GitHub repository-secret prefix
restriction was independently checked during integration; the template names
use `OAUTH_` aliases. No release-news claim is needed for this lesson.

Blender scene output was rerendered on 15 November with Blender 5.2.3 LTS.
The old verified community-bridge paths/pins remain supplied, accurately
labelled as previous checks; a fixed client is never called a live model loop.
The new template's tests use mock OAuth; built-Worker/local-D1 integration
and actual GitHub/Cloudflare acceptance are separate evidence categories.
No credentials, account captures or identifiable student notes are published.
Full build/render/test evidence belongs in the private author report.

The group project remains 40%, 25/50/25, due 6 December 2026 at 23:59 HKT.
Use a public sd5913-owned group repository; personal OAuth App ownership does
not change that policy. GitHub Projects or an equivalent accessible shared
progress record is valid. Canvas submission instructions remain authoritative.
