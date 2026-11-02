# Week 9 instructor run sheet

Thursday 5 November 2026: **120-minute theory-first lecture**, including a
10-minute break, followed by a **separate 120-minute PFAD tutorial**.
Revised 2 November from the instructor's correction of the Week 9 draft.
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
| 8-15 | Possible network connections and the limits of a Metcalfe-style value claim (1). Client/server as process roles, including two programs on one laptop (2). Simplex/half/full duplex, compatible protocols, reachability, routing and transport versus application acknowledgement (4). |
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

## Small lecture illustrations, not the full tutorial

The core lecture can run without starting an application server. If the
current companion has completed its separate review and is ready, the optional
HTTP observation uses its documented source:
[`6e5637f56c1179f64d170dc29eecbf312bb41a2f/week09`](https://github.com/sd5913/pfad/tree/6e5637f56c1179f64d170dc29eecbf312bb41a2f/week09).
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

## Separate tutorial: preserved 120-minute allocation

The existing student/TA README is the starting implementation. Its current
example needs a separate review/fix under the instructor's latest request;
this lecture correction does not certify that repair or edit PFAD code.
Preserve this independent budget while that review is completed:

| Minutes | Tutorial work and observed outcome |
| --- | --- |
| 0-15 | Setup, read the readiness line, open two loopback views. At minute 15, move blocked setup to a prepared partner machine and alternate roles. |
| 15-35 | Trace one accepted action, authoritative Scene, two state observations and sender acknowledgement. Distinguish unsent local slider input. |
| 35-55 | Read `Scene.apply`, predict acceptance boundaries, change maximum 100 to 80, restart/check both transports, then restore baseline. Invalid input must not mutate position/revision. |
| 55-65 | Break. |
| 65-85 | Compare HTTP polling and continuing WebSocket updates. Read `updates()`, receive, validation, lock, broadcast and acknowledgement. Predict two-client ordering and inspect revisions. |
| 85-100 | Disconnect/reconnect, unknown acknowledgement, stop/restart and recovery. Distinguish observed state from an action outcome; do not automatically replay uncertain commands. |
| 100-120 | Tutor review / project support, including unresolved opening AMA questions and the next usable increment. |

The previously lengthy lecture demonstration moves here: JSON parsing and exact
field checks; bool/int distinction; accepted/rejected states; revision order;
`await` and the one-process lock; slow-client fanout limitation; delayed replies;
HTTP-only restart recovery; and the 100-to-80 code edit. Keep the raw TCP
red/blue/orange framing example as optional tutor-led support, not a second
mandatory setup. The conceptual framing distinction remains in the lecture.

The tutorial's known example uses IDs for correlation, not deduplication.
Repeating set_x can retain the same position while advancing revision;
repeating spend_coin could charge again. Ignore-replies deliberately suppresses
observation and does not prove random packet loss. Restart resets RAM, not
persistent storage. These are behaviors to recheck during the separate fix.

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
verification in the PR handoff, not as an unsupported assertion here. Earlier
29 October companion test/browser evidence is historical evidence for its
pinned commit, not proof that the newly requested tutorial repair is complete.
Physical classroom/add-in and Windows/macOS runtime rehearsals are separate
checks from Linux source/build validation.
