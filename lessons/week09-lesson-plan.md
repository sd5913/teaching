# Week 9 instructor run sheet

Thursday 5 November 2026: **120-minute lecture**, followed by a separate
**120-minute PFAD tutorial**. Approved production route, prepared 29 October.
The existing long deck is retained pending real network/browser acceptance;
do not mistake its older paper-only/MCP sequence for this final run sheet.

## Preflight and materials

Use the paired PFAD source at
[`cba28cba31826b9e798eca9740a537ff7af993ca/week09`](https://github.com/sd5913/pfad/tree/cba28cba31826b9e798eca9740a537ff7af993ca/week09).
From that folder, `uv run python server.py`, then open
`http://127.0.0.1:8009` twice. Read the server readiness line before showing a
view. No login, camera, microphone, GPU or remote class is necessary. Stop with
Ctrl+C. Leave the presenter's 8765 untouched; raw TCP uses 8010.

Before classroom use, independently check latest pinned install and two views,
HTTP and WS accepted/rejected inputs, disconnect/reconnect, unobserved ack,
stopped-server recovery and simultaneous presenter use. Run the real socket
suite and supplied Playwright check. A free-port test or ASGI-only test does
not establish default-port/browser acceptance. Local sandbox EPERM is recorded;
do not bypass it or claim a paper trace passed the actual gate.

Prepare a clean `scene.py` copy/diff to restore the 100 boundary. Keep a
second working machine or printed message cards for failure recovery. A
fallback must be called a paper simulation if no real process runs. Do not
start a ClassPoint session for automated validation; lecture questions can use
hands/discussion. The tutorial never depends on an instructor login.

## Lecture: exact 0-120 route

| Minutes | Teach, demonstrate and check |
| --- | --- |
| 0-10 | Ask what other program/person/device the project might talk to (2). Dated software news and claim limits (3). Recall W4 tide request and ask who initiates it (3). Outcomes and route (2). |
| 10-30 | Draw two processes on one laptop (4). Decompose http://127.0.0.1:8009/state into protocol/host/port/route (5). Distinguish link/IP/transport/application message with the same journey (5). Predict wrong route versus no listener, then reveal concrete failure evidence (6). |
| 30-50 | Start the actual server, GET /state and identify JSON/status (5). Send HTTP action and follow id/action/x into Scene.apply (5). Compare accepted 0/100 with invalid 101 and unchanged revision (5). Students trace browser, route, Python state and response on one numbered diagram; discuss their prediction (5). |
| 50-60 | Compact raw TCP observation on 8010: start echo server/client and identify newline framing (4). Show combined red/blue and split orange writes from the test (3). Predict why recv is not one complete application message; distinguish byte stream from WS frames (3). Stop extra listener. |
| 60-70 | Break. Keep the main scene available; no new material. |
| 70-95 | Two tabs: first snapshot, A sends25, B observes same revision (7). B sends80; map authoritative server state and local unsent slider (5). GET snapshot/polling versus server push; HTTP may reuse transport connections (5). Read await receive and one-process event-loop/lock excerpt; compare handler wait with another client's work (5). Predict competing actions; use server order/revisions rather than wall-clock assumptions (3). |
| 95-110 | Reject invalid101 and compare state (3). Disconnect A, change B, reconnect A for current snapshot without resend (4). Deliberately ignore replies after sending; observer and sender have different evidence, so Unknown is honest (4). Stop/restart: disconnected UI and reset RAM, not persistent storage (4). |
| 110-120 | Reliable coin event versus frequent position snapshots/UDP comparison (2). MediaPipe fingertip or OSC address/value to bounded control message; no camera/OSC setup (2). Teams choose local/HTTP/live boundary and name one failure (3). Recap, quiz scope and exact PFAD tutorial handoff/tutor review (3). |

Each major diagram should occupy its slide at the established course scale:
numbered arrows, real action/state/ack labels, primary text at least 40 design
pixels. Maintain geometry as the message travels. Use deckgen.CODE for the
short runnable excerpts; explain validation/state/await and source links in
speaker notes. Do not turn this into an installation or framework survey.

## Demo trace and useful questions

Fresh process: x50/revision0. A sends
`{"id":"a-1","action":"set_x","x":25}`. Accepted: both see
state x25/revision1; A also sees ack a-1/revision1. Invalid101 gets rejected;
position/revision stay unchanged. Moving a slider without Send changes local
input only. IDs match acknowledgements but this service stores no dedup table.

Ask students to point to which line validates, which mutates state, and which
announces it. In `updates()`, `await client.receive()` lets another handler run
while this one waits. The in-memory list/Scene belongs to one process; it is
not a distributed persistence or scalable multiplayer system. Slow-client
backpressure is a limitation of the deliberately small broadcast loop.

Disconnect A, update B, Connect A: snapshot recovers the view. The explicit
ignore-replies button demonstrates unavailable acknowledgement observation,
not proven packet loss. An absolute set position may be safe to repeat in one
sense, but a second command still advances the revision. Ask what duplicate
spend/increment commands would do before prescribing retries. No reply alone
establishes neither definite success nor definite failure.

## Separate tutorial and tutor time

The complete student/TA instructions are the pinned PFAD README. Preserve
their exact allocations: 0-15 setup; 15-35 trace; 35-55 edit/check; 55-65 break;
65-85 two clients; 85-100 failure/recovery; 100-120 first-working-interaction
tutor review/project support. At minute15, move blocked setup to a prepared
partner machine and alternate roles. The 100-to-80 boundary edit includes
explicit predicted acceptance cases, restart, verification and baseline restore.

The tutor's 5 November first-working-interaction delivery uses the allocated
tutorial slot; exact team time is tutor-confirmed. Networking, AI or a camera
is not a project requirement. Keep accessible progress/run/test evidence and
the next goal in the existing team record, with GitHub Projects recommended
and an equivalent accessible record valid. No new upload/attendance score or
compulsory defence. Preserve public sd5913 repository/teammate Write access,
Canvas submission, 40% weighting, 25/50/25 rubric and 6 December 2026,
23:59 HKT deadline.

## Quiz scope and evidence limits

Core revision: roles/processes/address/port/route; JSON validation; HTTP
methods/status versus connection failure; TCP framing; continuing WS updates;
shared versus local state; ack uncertainty/reconnect; brief await/event-loop
meaning and protocol choice. Dated release news, specific version numbers,
OSC installation, optional LAN configuration and library memorization are
outside the quiz. No private graded questions or keys are published here.

Before final handoff replace this preparation status with actual live version,
command, browser/render and CI evidence. Physical classroom screens/audio,
presenter coexistence and learner platform checks remain separate from CI.
