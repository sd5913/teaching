# Week 9: connected interactions

Production planning, 29 October 2026. The instructor-approved course design
fixes **Thursday 5 November, 120-minute lecture plus separate 120-minute
tutorial**. This supersedes the 21 October draft's duration-unconfirmed and
paper-only core assumptions. Existing teaching/PFAD PR #12 remain the review pair.

## Status and feasibility gate

The runnable core and complete tutorial are in PFAD commit
[`cba28cba31826b9e798eca9740a537ff7af993ca`](https://github.com/sd5913/pfad/tree/cba28cba31826b9e798eca9740a537ff7af993ca/week09).
It provides one Python service, two browser views, HTTP snapshots/actions,
WebSocket broadcasts, validation, reconnect snapshots and an explicit
unobserved-ack demonstration. Port 8009 is separate from the presenter's 8765;
the retained raw TCP observation uses 8010.

Four rule tests and four real FastAPI ASGI handler tests pass in memory on the
cached environment. The host refuses socket creation/binding. Real loopback
tests therefore report explicit host-policy skips, and the attempted browser
check exits at server bind, before browser launch. No live/two-browser proof
is claimed. The coordinator will run the prepared independent socket/browser
checks in normal CI and inspect retained screenshots/trace before the long
replacement deck is authored. **The incumbent deck is deliberately preserved
until that gate passes; its obsolete paper-only/MCP sections are not the final
approved lesson.** This planning/run sheet is concrete preparation, not a claim
that the incumbent slides already teach the approved 120-minute route.

## Outcomes and prior-knowledge ledger

Students will trace a control message through client, server state and two
views; distinguish HTTP request/response, WebSocket messages and a TCP byte
stream; change a Python validation boundary and verify rejected input; and
explain disconnect/reconnect plus uncertainty when an acknowledgement is absent.

| Already taught | Reused here | New this week |
| --- | --- | --- |
| W4 HTTP tide API, JSON and browser chart | One request, one returned resource | Address/port/route diagnosis and separate processes |
| W7 classes and state | `Scene` instance owns position and revision | Authoritative shared state and multiple clients |
| W8 coordinate/gesture-to-action mapping | Supplied slider; MediaPipe bridge | Defined control-message schema and validation |
| W8 Git, environments and CI | Inspect the diff and run checks | Continuing updates, framing, ack and reconnect |

No repeated basic class lesson, MCP permission role-play, Docker setup,
microphone installation or compulsory camera/network project feature is added.
The exact lecture and tutorial blocks are in [the run sheet](week09-lesson-plan.md).

## System and acceptance contract

From the supplied PFAD `week09` directory, `uv run python server.py` starts a
loopback service on 8009. Open its HTTP address in two tabs. An action is
`{"id":"a-1","action":"set_x","x":25}`. `Scene.apply()` accepts exactly
these fields, a bounded string ID, the named action and an integer 0-100.
Only accepted actions change position and revision. Both transports use that
same Python method. Both clients receive the same state revision; only the
sender receives its matching acknowledgement. The lock orders state changes
and announcements in this one-process demonstration.

Reject malformed JSON, missing/extra fields, unknown action, booleans, strings
and out-of-range positions without mutation. Disconnect one client while the
other continues; reconnect for a fresh snapshot without replaying commands.
Stop/restart the process and observe RAM reset. The client-side fault button
deliberately ignores replies after send: another client may show processing,
while the sender must show Unknown. This is missing observation, not a claim
that a packet was lost. IDs correlate acknowledgements but are not stored for
deduplication. Absolute assignment limits the effect of a repeated position;
incrementing a score or spending a coin needs an explicit retry design.

The student edit changes the allowed right edge from 100 to 80, predicts
0/80/81/101, restarts and checks both tabs, then restores baseline. Baseline
tests intentionally fail while 100 remains disallowed. This connects code,
specification, observation and recovery rather than testing prose or slide counts.

## Source-to-lesson crosswalk

Historical references are **PDF page numbers counted from page 1**, from
`reference/2025/SD5913 - PFAD - Week 9.pdf`. The old examples were read at PFAD
`origin/2025`, commit `512edb07927c5d77cacc7279ba6be601b33dc601`; that unrelated
history is evidence, not a branch to merge or a current installation guide.

| 2025 source | Status | 2026 destination and correction |
| --- | --- | --- |
| PDF p23-25, networks/network effects/communication questions | Retained, focused | Opening asks which program must communicate; acknowledgements and agreed message language become concrete. Network-effect claim remains optional discussion, not a universal measured law. |
| PDF p26-28, link/network layers | Updated | 10-30 model distinguishes physical link, IP destination, transport and application message; loopback core needs no DHCP/netmask configuration exercise. |
| PDF p29, packet distribution | Retained as comparison | 70-95 one sender, server broadcast, two recipients; no claim this application broadcast is an IP multicast packet. |
| PDF p30-31, UDP/TCP | Updated | 50-60 ordered byte-stream/framing observation; 110-120 reliable events versus latency-sensitive snapshots. TCP may fail, has no fixed three-times packet count, and does not prove application processing. |
| PDF p32-35, application protocols/ports/debugging | Updated | 10-30 URL decomposition and 95-110 route versus listener failure; many connections can share a listening port. No scans of other people's machines. |
| PDF p36-42, APIs/REST/WebSockets/examples | Retained, updated | 30-50 real GET/POST/JSON/status trace and 70-95 two-way updates; HTTP may reuse TCP, server data can persist, PATCH/PUT rather than invented UPDATE verb. |
| PDF p43-45 and archived fastapi/websocket examples | Updated | One FastAPI app owns HTTP and WS boundaries; supplied browser keeps attention on readable Python rules instead of an echo-only endpoint. |
| PDF p46, p53-58 speech service/audio queues | Moved | Speech was taught in current W6 and is reused for W10's talking handbook agent. No GPU/microphone stack is silently required in networking. A short await excerpt explains cooperation without a second async course. |
| PDF p47-52 historical tutorial/setup/friend connection | Updated | Complete 120-minute README with uv, two tabs on one laptop, edit/failure/recovery and tutor support. LAN/mobile is an optional separately rehearsed extension. |
| W11 creative-app/OSC examples; current W8 hand coordinates | Retained bridge | 110-120 maps fingertip coordinate to bounded `set_x`, or OSC address/value to JSON through an adapter; neither a new camera requirement nor a pretend working OSC implementation. |
| 2026 incumbent MCP permission block | Moved out of W9 core | Later creative-tool/agent weeks teach useful tool boundaries; do not repeat a generic permission role-play here. |
| 2025 assessment/project pages | Superseded policy | Preserve current 40%, 25/50/25, public sd5913 team repository, Canvas and 6 December 2026 23:59 HKT. |
| Historical Orange/t-SNE destination | Removed by instructor | W11 uses the reallocated time for Blender/Godot. No W9 exercise or quiz dependency is created. |

## Current sources and version evidence

Context7 resolve + focused query, 29 October: official FastAPI WebSockets
(`https://fastapi.tiangolo.com/advanced/websockets/`), websockets synchronous
client (`https://websockets.readthedocs.io/en/stable/reference/sync/client.html`),
uv project/cache guidance (`https://docs.astral.sh/uv/guides/projects/`), and
Playwright browser tracing/page APIs (`https://playwright.dev/docs/api/class-tracing`).
FastAPI explicitly limits the in-memory connection-manager example to one
process. OSC comparison: `https://opensoundcontrol.stanford.edu/spec-1_0.html`.

Live GitHub primary-release checks on 29 October establish latest direct targets:
FastAPI **0.162.0**, published 23 October; uvicorn **0.54.0**, 25 September;
websockets **17.3**, 19 October. These replace older cache-only pins and await
online CI resolution, lock capture and runtime verification. Cached tests used
Python 3.13.16, FastAPI 0.142.2, Starlette 1.7.0, uvicorn 0.54.0, websockets
17.2 and Pydantic 2.10.6; they do not prove the new target versions.

Read current official W7/W8 material and the reviewed authoring contracts at
teaching `b943695a9b6b40e0340d1153361b3aaf695222dc` and PFAD
`2119e1cfcfd023a4e1864dc9f92b0205bc0e6ec5`. W8 is now merged into official
teaching `2d57def692d97f686850f6ffab3d144036e162f4` and PFAD
`a4370bec4be29d5f4a37b1a8ecd477e25a73fc3d`; shared registration integration
belongs to the coordinator. Dated opening source and limits are in
[the news note](week09-news-20261029.md).

## Next production gate

Independent code/teaching review, online latest-pin installation and lock,
live `test_scene` on 8009, TCP checks, and `check_browser.cjs` must pass before
replacement slides are described as runnable. Then author the full sequence
with large numbered message diagrams, actual CODE excerpts, rich notes,
precisely pinned PFAD links and explicit quiz/news separation. Build with
overflow checking and inspect all slide renders plus actual PDF and both
PowerPoints. Local host restrictions are recorded rather than bypassed.
