# Week 9: clients, applications and network boundaries

Lecture correction, **2 November 2026**, based on teaching main
`da0e86c67172c765ab5d7de9c5dfe1f625370667`.
Thursday 5 November remains a **120-minute lecture plus separate 120-minute
tutorial**. Preserve the existing Deckgen Python/figure architecture and course
styling. No shared renderer, registration, navigation or Week 10 files change.

## Current instructor decisions

- Open with one **group-project AMA** so students can post questions using the
  established ClassPoint Short Answer activity. Do not begin with unrelated
  cold questions or a release-news detour.
- Connect the actual prior work: **Agile/Scrum, GitHub PRs/Projects and
  MediaPipe**. A team can now send a sensing/control result across a process or
  device boundary and test that integration together.
- Restore substantial networking theory from the supplied 2025 Week 9 slides
  24-40: layers, links, addressing, delivery modes, transport, application
  protocols, ports, commands and APIs. The old compact four-row slide did not
  preserve this teaching coverage.
- The **final-course quiz is later**. Teach assessable concepts now; do not add
  a Week 9 end quiz, a new assessment or public private-question material.
- Keep the lecture theory-first with short concrete code illustrations. The
  detailed shared-scene example belongs to the **two-hour tutorial** and needs
  its own review/fix, which this lecture source correction does not certify.
- Progression: **this week, a client talks to an app through APIs/WebSocket;
  next week, the app talks to databases and other resources**. A network
  database commonly uses a TCP socket and database protocol. A socket endpoint
  is not an application protocol, and embedded SQLite needs no network server.
  Do not teach or edit Week 10's implementation here.

## Outcomes and prior-knowledge ledger

After the lecture, students should be able to:

1. Trace a control message through protocol, host resolution, IP, transport
   port and application route, using OSI/TCP-IP responsibilities to explain
   which part changes when the network or application changes.
2. Compare unicast/broadcast/multicast and TCP/UDP guarantees, then justify a
   delivery/transport choice for a creative interaction.
3. Explain HTTP/HTTPS, REST operations, WebSocket and WebRTC by purpose, and
   predict the behavior of the actual echo and unsolicited-push examples.
4. Select a diagnostic observation, distinguish connection/status/data/state
   failures, and explain what missing application acknowledgement does and
   does not prove.

| Already taught | Reused now | New focus |
| --- | --- | --- |
| W8 Agile/Scrum and visible increments | One testable integration goal | A message boundary that two team members can agree and verify |
| W8 GitHub Projects, branches, PRs and review | Coordinate sender/receiver changes and evidence | Interface contracts and failures across processes |
| W8 MediaPipe landmarks and action mapping | Fingertip x becomes a bounded control value; slider fallback | How a client sends that value to an application |
| W4 HTTP tide API, JSON and browser chart | Request, representation and browser rendering | Layered protocols, methods/status, REST and continuing messages |
| W7 classes and state | One Scene object in the tutorial | Shared state versus local input, correlation and recovery |

Networking, a camera, AI and a particular engine are not project requirements.
No repeated basic class lesson, MCP permission role-play, Docker setup or
microphone installation is added.

## Teaching route and revision coverage

The detailed timed route is in [the run sheet](week09-lesson-plan.md).
The lecture totals 120 minutes, including the 60-70 break. The tutorial keeps
its independent 0-120 allocation and final 20 minutes for tutor/project support.
The slide count follows the concepts, not a fixed production target.

| Concept family | Taught representation and reasoning check | Location in lecture |
| --- | --- | --- |
| Network roles and network effects | Possible pair connections; client/server process roles; why more participants need not add value | Slides 5-7, 8-15 min |
| OSI / TCP-IP and encapsulation | All seven names mapped into four groups; actual JSON/WebSocket/TCP/IP/link nesting; change Wi-Fi to Ethernet without changing JSON | Slides 8-10, 15-25 min |
| IP configuration and routing | IPv4/IPv6; DHCP/prefix/gateway; decide whether an illustrated destination is on-link | Slides 11-12, 25-29 min |
| Packet distribution | Three successive diagrams; distinguish one recipient, local scope and joined group | Slides 13-15, 29-35 min |
| Transport | TCP three-way setup, ordered bytes, UDP datagrams; freshness versus ordered delivery | Slides 16-17, 35-40 min |
| Endpoints | Two client ports share one server listener; URL and bind/destination distinction | Slides 18-20, 40-49 min |
| Diagnostic evidence | Configuration, routes, listener, HTTP response; Nmap probes versus Wireshark capture; paired fault reasoning | Slides 21-24, 49-60 min |
| Application protocols | DNS/cache, HTTPS security, HTTP transport caveat, WebRTC versus WebSocket purpose | Slides 26-29, 70-80 min |
| APIs and REST | Request/response diagram, resource methods, status/optional body, x=0..100 validation, stateless request versus durable resource | Slides 30-34, 80-94 min |
| WebSocket code | Persistent client loop, echo handler, concurrent unsolicited text push; predict a recv mismatch | Slides 35-38, 94-103 min |
| Message and state boundaries | TCP framing, state versus ack, per-connection fanout, uncertainty and reconnect | Slides 39-43, 103-115 min |
| Project and next-week connection | Choose a useful boundary; tutorial owns implementation; next the app becomes a database/resource client | Slides 44-46, 115-120 min |

These are teaching/revision targets, **not new quiz questions or a private key**.
Expect explanation and prediction rather than command-flag/version memorization.
Metcalfe's law is a qualified model, not an economic fact to prove. Optional
LAN/OSC setup, old library imports and dated release details are outside core
revision. The opening AMA is ungraded.

## Source-to-lesson crosswalk

The supplied `SD5913 - PFAD - Week 9(1).pdf` and `SD5913 - PFAD - Week 9.pptx`
each contain 60 slides. **PDF page number equals slide number**, counted from 1.
The table restores the missing concepts, correcting inaccurate claims rather
than copying them. Current lecture slide numbers below refer to this correction.

| Original source | Status | Current destination and correction |
| --- | --- | --- |
| Slide 24, network effects / Metcalfe | Retained with qualification | Slide 5: 2/3/4 nodes and 1/3/6 possible undirected pairs; possible connections are not guaranteed economic value. |
| Slide 25, duplex/reachability/protocol/routing/ACK | Restored | Slides 6-7 and 12: process roles, direction capability, agreed rules, next hop and TCP ACK versus application result. |
| Slide 26, OSI/TCP-IP diagram | Restored substantially | Slides 8-9: all seven OSI layers, approximate grouping into four Internet layers, concrete encapsulation and segmentation. No “not a full OSI course” substitution. |
| Slide 27, wired/wireless links | Restored | Slide 10: Ethernet, Wi-Fi/5G, Bluetooth, LoRa, USB, I2C and 1-Wire; rate/range/power tradeoffs without fictional fixed specifications. Sensor buses are not all IP networks. |
| Slide 28, IPv4/v6, DHCP, netmask, gateway | Restored | Slides 11-12: address sizes/examples, prefix, gateway, DHCP and IPv6 auto-configuration; local versus routed destination. |
| Slide 29, unicast/broadcast/multicast diagram | Restored as separate diagrams | Slides 13-15: unicast one destination, scoped broadcast, multicast group. IPv6 has no broadcast. WebSocket fanout is a different application mechanism. |
| Slides 30-31, TCP/UDP | Restored/corrected | Slides 16-17 and 39: handshake, ordered stream, retransmission/failure, UDP datagrams and framing. No claim of error immunity or a universal three-times packet count. |
| Slides 32-33, DNS/HTTP/HTTPS/WS/WebRTC | Restored/expanded | Slides 26-29 and 35: distinct protocol purposes, DNS resolution/cache, TLS protections, HTTP/3 caveat, live media versus control messages. |
| Slide 34, ports | Restored/corrected | Slides 18-20: many connections share a listener, source/destination endpoint pairs, URL path and server binding. A port is not limited to one connection. |
| Slide 35, commands and tools | Restored | Slides 21-24: ipconfig, ifconfig, ip, netstat/ss, curl, Nmap and Wireshark; own-lab authorization, packet privacy and evidence-based diagnosis. |
| Slides 36-37, API requests/responses | Restored | Slides 30-31: method/path/headers/body into an app, status/body back; a concrete GET /state trace and creative-service examples. |
| Slide 38, REST | Restored/corrected | Slides 32-34: resources, representations, GET/POST/PUT/PATCH/DELETE, stateless request context versus stored data; /action is a command API, not advertised as full REST. |
| Slide 39, persistent bidirectional WebSocket | Restored | Slides 35-38: full-duplex capability contrasted with chosen send/recv loop and independent server push. Persistence of a connection differs from durable data. |
| Slide 40, API examples | Retained with relevant examples | Slide 30 uses weather/gallery plus the current scene; earlier tide and MediaPipe supply the course connection, without adding accounts or paid services. |
| Slides 43-45 and actual historical WebSocket files | Retained as code, corrected context | Slides 36-38 quote pinned client, echo and push excerpts. Old slide/README paths are not an installation guide. `Ping!` is text data, not a Ping control frame. No old unpinned server is run on presenter port 8765. |
| Current 36-slide draft's detailed Scene/validation/await/lock/retry walkthrough | Moved to separate tutorial, not deleted | Lecture retains framing, local/shared state, state/ack, uncertainty and reconnect concepts. Tutorial/run sheet owns actual `Scene.apply`, JSON checks, revisions, receive loop, lock, fanout limits, delayed reply/restart checks and the boundary edit. |
| Slides 46, 53-58, speech/audio queues | Remain moved | Current W6 already taught speech; later handbook-agent work can reuse it. No audio/GPU stack is restored to networking. |
| Slides 47-52, setup/friend connection | Updated | Existing two-hour tutorial uses uv/two local views with setup fallback and project support. LAN/mobile is an optional authorized/rehearsed extension, not required exposure. |
| W8 MediaPipe and historical OSC creative control | Retained bridge / optional | Opening links sensing to a message. OSC address/value-to-JSON remains an optional tutor explanation, not a pretend running adapter or required setup. |
| 2026 former MCP block | Remain outside W9 core | No generic permission role-play replaces networking theory. |
| Historical project/assessment pages | Superseded policy | Preserve current 40%, 25/50/25, public sd5913 repository, Canvas and 6 December 2026 23:59 HKT. No new quiz/submission. |
| Historical Orange/t-SNE material | Remain removed by instructor | W11 time stays reallocated to Blender/Godot; no new dependency here. |

## Source pins and corrections

The existing modern tutorial link remains
[`sd5913/pfad@6e5637f56c1179f64d170dc29eecbf312bb41a2f/week09`](https://github.com/sd5913/pfad/tree/6e5637f56c1179f64d170dc29eecbf312bb41a2f/week09).
This preserves verified source identity while its newly requested example fix
is handled separately. It is not evidence that this correction reran that app.
Only refresh the lecture pin after the revised tutorial has its own verified
commit and documented run commands.

Historical code is separately pinned to
[`venetanji/pfad@7eb4077d508866ce0d95bbbd489ee64e9badb78b/week09`](https://github.com/venetanji/pfad/tree/7eb4077d508866ce0d95bbbd489ee64e9badb78b/week09).
The basic echo binds localhost:8765. The text-push variant binds 0.0.0.0:8765
and gathers a response coroutine with a periodic send coroutine. Those sources
were read, not installed/run. Do not copy missing files from the old README or
confuse `venetanji/pfad` with the current `sd5913/pfad` tutorial repository.

Primary technical references, checked 2 November, are cited in slide notes:

- [ITU-T X.200](https://www.itu.int/rec/T-REC-X.200-199407-I/en) and
  [RFC 1122](https://www.rfc-editor.org/rfc/rfc1122): layer models and routing.
- [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293),
  [RFC 768](https://www.rfc-editor.org/rfc/rfc768),
  [RFC 1112](https://www.rfc-editor.org/rfc/rfc1112) and
  [RFC 4291](https://www.rfc-editor.org/rfc/rfc4291): TCP, UDP and IP delivery.
- [RFC 2131](https://www.rfc-editor.org/rfc/rfc2131),
  [RFC 8200](https://www.rfc-editor.org/rfc/rfc8200) and
  [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034): DHCP, IPv6 and DNS.
- [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110),
  [RFC 5789](https://www.rfc-editor.org/rfc/rfc5789),
  [Fielding chapter 5](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm),
  [RFC 6455](https://www.rfc-editor.org/rfc/rfc6455) and
  [W3C WebRTC](https://www.w3.org/TR/webrtc/): HTTP/REST, WebSocket and WebRTC.
- [Microsoft ipconfig](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig),
  [netstat](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netstat),
  [Nmap guide](https://nmap.org/book/man.html) and
  [Wireshark guide](https://www.wireshark.org/docs/wsug_html_chunked/ChapterIntroduction.html): diagnostics.

The cross-week bridge was checked against current main `deck/week08.py`.
The cited authoring contract is
[`b943695a9b6b40e0340d1153361b3aaf695222dc/docs/COURSE-AUTHORING.md`](https://github.com/sd5913/teaching/blob/b943695a9b6b40e0340d1153361b3aaf695222dc/docs/COURSE-AUTHORING.md),
which is absent from the current main tree but remains the referenced standard.

## Validation and handoff boundary

Preserve the unchanged `deckgen.toml`, requirements pin, site navigation,
existing assets and unrelated weekly files. Extend focused figure/export tests
for the added diagrams and AMA mechanism, not arbitrary slide-count assertions.

Build HTML, PDF and both PowerPoints with overflow checks. Inspect changed
slides/diagrams at presentation size and record exactly which output was
actually rendered. Native preview inspection is not a PowerPoint or PDF render.
Physical ClassPoint and presenter/classroom coexistence remain rehearsal gates.
Do not rewrite earlier companion runtime history as a fresh pass, or mark the
new tutorial repair complete from a lecture-source build.
