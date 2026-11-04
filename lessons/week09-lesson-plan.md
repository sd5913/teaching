# Week 9 instructor run sheet

Thursday 5 November 2026: **120-minute theory-first lecture**, including a
10-minute break, followed by a **separate 120-minute PFAD tutorial**.
Revised 4 November for clarity and presentation, following the instructor's
2 November correction. The 53-slide sequence splits crowded explanations;
the lecture and tutorial budgets stay at 120 minutes each.
The concepts support the **final-course quiz later**. There is no new quiz at
the end of this lecture and no new graded submission.

## Opening and connection to previous weeks

Start with **one group-project AMA**. Use the deck's existing ClassPoint Short
Answer activity so students can post their questions. Group related questions,
answer the shared ones, and carry project-specific follow-ups to tutorial
support. If the add-in is unavailable, collect the same questions verbally or
on paper, not through a new external form. Do not publish student questions
with names or other private details in the public repository.

The bridge follows the actual Week 8 lesson: Agile/Scrum, GitHub Projects,
branches/pull requests/review, and MediaPipe landmarks mapped to actions.
A team now wants to send a sensing/control result to another program or device.
The lecture explains how a client talks to an app through APIs/WebSocket. The tutorial implements that boundary. Next week the app talks to databases and other resources: commonly a network socket plus a database protocol, with embedded SQLite as an exception. Do not teach database implementation details this week.
The former disconnected opening questions and dated release-news detour are
removed from the live sequence; their historical source note is unchanged.
Networking remains optional for the group project.

## Lecture: exact 0-120 route

| Minutes | Teach, represent and check |
| --- | --- |
| 0-8 | Group-project AMA using Short Answer (5). Connect Agile/Scrum, GitHub PRs/Projects and MediaPipe to a sensing/control boundary (2). Establish the network/API journey (1). |
| 8-15 | Introduce Metcalfe's law and the growing number of possible links (2), then question how participation affects value (1). Client/server as process roles on one laptop (1). Simplex/half/full duplex and agreed message rules (3); return to reachability, routing and acknowledgement in their later examples. |
| 15-29 | Seven OSI layers, their jobs and approximate four-layer TCP/IP mapping (6). Trace JSON/WebSocket/TCP/IP/link encapsulation, including segmentation (2). Wired/wireless and sensor-bus choices (2). IPv4/IPv6, prefix/netmask, DHCP and gateway (2). Work same-subnet versus gateway routing example (2). |
| 29-40 | Separate diagrams for unicast, scoped broadcast and group multicast (2 each). Explain TCP SYN/SYN+ACK/ACK and later ordered bytes (3). Compare TCP stream and UDP datagram guarantees and application choices (2). |
| 40-49 | Many connections share one listening port (3). Decompose a URL and distinguish scheme/host/port/path (3). Trace localhost versus a remote server and distinguish bind address from client destination (3). |
| 49-60 | Interface/route/socket tools: ipconfig, ifconfig, ip, netstat/ss and an HTTP probe (3). Nmap versus Wireshark, permissions and privacy (2). Wrong route versus absent listener (2). Paired diagnostic reasoning and discussion (4). No graded quiz. |
| 60-70 | Full ten-minute break. No new material or tutorial implementation. |
| 70-80 | Locate DNS, HTTP/HTTPS, WebSocket and WebRTC by purpose (1). Name resolution, local overrides/cache and numeric IP (2). HTTP versus HTTPS, connection reuse and HTTP/3 caveat (3). WebSocket control messages versus WebRTC media/data/signaling (4). |
| 80-94 | API request/response and examples (3). Trace GET /state into a status/body response, optionally with a two-minute prepared curl observation (3). REST, resources and GET/POST/PUT/PATCH/DELETE semantics (3). Interpret HTTP status/optional body and the actual integer x=0..100 validation rule (3). Separate stateless requests, shared RAM state and durable storage (2). |
| 94-103 | WebSocket full-duplex capability and framed messages (1). Read the actual historical client send/recv loop (2), echo handler (2), and independent periodic server text push (4). Predict why a single recv after each send can mistake an unsolicited message for the reply. These are short excerpts, not a second installation/demo stack. |
| 103-115 | TCP byte-stream framing versus WebSocket messages (3). Local input, authoritative state, state snapshot, correlated app ack and per-connection fanout (3). Missing reply and retry uncertainty (3). Reconnect snapshot versus automatic resend (2). Choose protocol by interaction needs (1). |
| 115-120 | Teams name a useful boundary and an observable failure (2). Separate tutorial outcome, setup/fallback and tutor-review handoff (3). Preserve time for unresolved AMA questions in tutorial support. |

Use the diagrams at the established classroom scale. The networking figures
have primary labels at least 40 design pixels on a 1680 x 640 figure canvas.
Speaker notes carry explanations, sources and expected reasoning. Ask students
to predict or justify the observation, not merely repeat an acronym.

## Presentation and explanation order

- Explain Metcalfe's law on slide 5 before asking about its limits on slide 6.
  The exact possible-pair count motivates the proposed quadratic value model;
  the follow-up compares equally sized silent and active groups.
- Compare equivalent ideas at the same height on the same white surface.
  Use the numbered diagrams only when order matters, such as sending a message
  or reconnecting. Keep each slide to one question or relationship.
- Read the bold URL as a whole, then its labeled parts: blue host, dark teal
  port, burnt-orange path. Labels accompany color so the meaning does not
  depend on color perception. The DNS mapping is an illustrative example.
- After the break, introduce DNS, HTTP and WebSocket by their different jobs.
  Explain REST through an artwork address, read/create, then change/remove;
  status and validation have separate slides. State and action acknowledgement
  also have separate explanations. Transport-version details, DNS record types,
  authentication qualifications and implementation limits remain in notes.
- Highlight the operative lines of the three historical code excerpts. The
  examples remain read-only sources on the old port; the tutorial uses 8009.

The local draft can be reviewed as ordinary HTML without starting the presenter
or a remote ClassPoint session. Export and classroom evidence are recorded
separately from this explanation plan.

### Multiboxes tutorial reference

Finish the existing 117-120 handoff with the concrete
[Multiboxes source](https://github.com/venetanji/multiboxes/tree/2977be17b35790dd7b31f1f242b0dc86113d5350),
[two-hour study guide](https://github.com/venetanji/multiboxes/blob/2977be17b35790dd7b31f1f242b0dc86113d5350/STUDY_GUIDE.md)
and [setup](https://github.com/venetanji/multiboxes/blob/2977be17b35790dd7b31f1f242b0dc86113d5350/README.md).
Two tabs share a Python/Pymunk physics and territory-painting world; the browser
renders server-owned state. Trace controls, validation, physics, snapshots and
rendering, then distinguish a Python rule from local drawing in
[simulation.py](https://github.com/venetanji/multiboxes/blob/2977be17b35790dd7b31f1f242b0dc86113d5350/src/multibox/simulation.py).

The current [protocol](https://github.com/venetanji/multiboxes/blob/2977be17b35790dd7b31f1f242b0dc86113d5350/docs/protocol.md)
uses JSON controls/metadata and complete binary gameplay snapshots, with a
supplied decoder. It is distinct from the minimal Scene's JSON state messages.
Use the PFAD README's **30-minute observation**: two players (10), input to
shared physics and a snapshot (10), rules versus rendering (10). The external
two-hour study guide is further reading. Prepare the instance before class;
students observe two local tabs, pair at a prepared machine or follow the
demonstration. No second installation or code edit is required. Stop at tutorial
minute 80 to protect group/TA time. Shared-campus play requires its own prepared
endpoint and device/network rehearsal.

## Small lecture illustrations, not the full tutorial

The core lecture can run without starting an application server. A prepared
optional HTTP observation uses the companion's documented source:
[`66067e191bd1c58b9c8d530dbc3fa8b50d69657a/week09`](https://github.com/sd5913/pfad/tree/66067e191bd1c58b9c8d530dbc3fa8b50d69657a/week09).
From that folder:

```bash
uv run python server.py
# In a separate terminal:
curl -i http://127.0.0.1:8009/state
```

Inspect status, Content-Type and body. A fresh process's example snapshot is
`{"type":"state","x":50,"revision":0}`. Stop with Ctrl+C. If the service is
not ready, read the documented trace and call it a trace, not a successful
live demonstration. Do not spend lecture time repairing its environment.

The historical WebSocket excerpts are pinned to
[`venetanji/pfad@7eb4077d508866ce0d95bbbd489ee64e9badb78b/week09`](https://github.com/venetanji/pfad/tree/7eb4077d508866ce0d95bbbd489ee64e9badb78b/week09):

- `websocket_client_example.py`: one persistent connection, send/recv/sleep loop.
- `websocket_server_echo.py`: one text response for each incoming message.
- `websocket_server_echo_ping.py`: `asyncio.gather` runs `respond` alongside a
  five-second ordinary text `"Ping!"` push. This is **not** a WebSocket Ping
  control frame or ICMP ping. The client can receive this unsolicited message
  before its echo, motivating message types and an independent receive path.

These sources are inspected examples, **not** the current installation guide.
Do not run them: their port 8765 conflicts with the presenter, the push variant
binds all IPv4 interfaces, and the old dependencies are not the tested tutorial
pins. The modern scene uses 127.0.0.1:8009; optional raw TCP uses 8010.

## Diagnostic demonstration and safety

Use only the instructor's own prepared loopback service. Interface commands
are platform-specific. `ipconfig /all` is Windows, `ifconfig` shows macOS interfaces; `route -n get default` shows its default gateway. On Linux, `ip addr`, `ip route`, `ss -ltn` are modern Linux tools. `netstat -an`
exists on Windows/macOS, with platform-dependent output. No installation is
required just to learn the purpose of each tool.

The only shown scan target is `nmap -sT -p 8009 127.0.0.1`. Do not scan campus,
classmates or remote hosts without explicit owner permission and scope.
Wireshark's `tcp.port == 8009` is a **display filter**, not a capture filter.
Capture only synthetic own-demo traffic; protect credentials, cookies, personal
content and identifiers. Encrypted traffic does not expose application bodies
without authorized decryption. A prepared capture is an observation fallback,
not a claim that live capture ran. No captures enter the public repository.

## Separate tutorial: 30 minutes, 30 minutes, 40 minutes

The [complete PFAD tutorial](https://github.com/sd5913/pfad/blob/66067e191bd1c58b9c8d530dbc3fa8b50d69657a/week09/README.md)
uses the instructor's revised allocation. Keep setup and break to ten minutes
each and protect the final 40 minutes for project work and TA feedback.

| Minutes | Tutorial work and observed outcome |
| --- | --- |
| 0-10 | Setup two loopback tabs. Move blocked setup to a prepared partner machine at minute 10 and alternate roles. |
| 10-40 | WebSockets: send 25 and trace state/ack (10); change the maximum 100 to 80, restart, test 80/81 and restore 100 (10); disconnect A, send 35 from B and reconnect A (10). |
| 40-50 | Full ten-minute break. |
| 50-80 | Observe prepared Multiboxes: two players and shared scores (10); input -> Python physics -> snapshot -> drawing (10); shared rules versus local rendering (10). |
| 80-120 | Group work and TA feedback: show a runnable increment or blocker, get focused advice, make a small fix, and record the next owner/action/check. Include unresolved opening AMA questions and teams still getting started. |

WebSocket work has one small Python edit and one recovery sequence. Advanced
JSON checks, `await`, locking, slow-client fanout, uncertain replies and raw TCP
remain optional code references. Do not let them consume the protected group/TA
block. The lecture retains the conceptual framing and acknowledgement limits.

IDs correlate replies; they do not deduplicate commands. A fresh process resets
RAM. Multiboxes uses binary state snapshots with a supplied decoder, unlike
the small Scene's JSON messages. Observe those distinctions without adding
another implementation exercise or database setup.

## Core revision scope and policy

Students should be able to reason about roles, duplex/protocol/reachability,
OSI and TCP/IP jobs, IP/subnet/gateway/DHCP, delivery modes, TCP/UDP, names and
ports, diagnostic evidence, HTTP/HTTPS/WebRTC/WebSocket, request/response and
REST methods, framing, app acknowledgements, shared/local state and recovery.
The planning file maps those outcomes to taught representations.

Do not assess command-flag or library-version memorization, economic proof of
Metcalfe's law, optional LAN/OSC configuration or the deprecated API imports.
No private final-quiz questions or answer keys belong in these public sources.
Networking, AI and a camera are not group-project requirements. Preserve the
existing 40% weight, 25/50/25 rubric, public sd5913 team repository, Canvas
submission and 6 December 2026 23:59 HKT deadline. Tutor timing remains
confirmed by tutors within allocated tutorial slots; no new upload or defence.

## Preflight and validation boundaries

Rehearse the ClassPoint AMA on the classroom add-in without publishing student
responses. Keep a non-add-in fallback. Confirm fonts, projector readability and
presenter port 8765. Do not expose a loopback service just to enable a LAN demo.

Deckgen HTML, PDF and plain/ClassPoint PowerPoints must build with overflow
checks enabled and actual slides must be visually inspected. Record that
verification in the PR handoff. The revised PFAD README changes allocation,
instructions and references; its runtime code is unchanged. Earlier 29 October
companion test/browser evidence remains dated runtime evidence. Link/source and
timetable checks on 4 November verify this documentation revision, not a fresh
Multiboxes runtime or classroom rehearsal.
Physical classroom/add-in and Windows/macOS runtime rehearsals are separate
checks from Linux source/build validation.
