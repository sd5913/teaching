# Week 9: clients, applications and network boundaries

Lecture correction, **2 November 2026**, based on teaching main
`da0e86c67172c765ab5d7de9c5dfe1f625370667`.
Thursday 5 November remains a **120-minute lecture plus separate 120-minute
tutorial**. Preserve the existing Deckgen Python/figure architecture and course
styling. No shared renderer, registration, navigation or Week 10 files change.

**4 November clarity pass:** introduce Metcalfe's law before objections. Replace
the uneven text/panel layout with aligned comparisons, annotated addresses,
short method/status rows and ordered message sequences. Use bold for addresses
and key terms, and distinguish address parts with labels and semantic colors.
Split crowded explanations rather than add concepts: the draft has 53 slides
within the same 120-minute lecture. Technical qualifications remain in speaker
notes. The instructor is reviewing this pass through a local HTML preview.

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
  separate tutorial now uses **30 minutes of WebSockets, 30 minutes observing
  Multiboxes, and 40 minutes for group work and TA feedback**, plus ten minutes
  each for setup and a break. Advanced implementation details are optional.
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
its independent 0-120 allocation and final 40 minutes for group work and TA feedback.
The slide count follows the concepts, not a fixed production target.

| Concept family | Taught representation and reasoning check | Location in lecture |
| --- | --- | --- |
| Network roles and network effects | Metcalfe's law, then its participation/value qualification; process roles and communication directions | Slides 5-8, 8-15 min |
| OSI / TCP-IP and encapsulation | Seven names mapped into four groups; JSON/WebSocket/TCP/IP/link nesting; change links without changing JSON | Slides 9-11, 15-25 min |
| IP configuration and routing | Address examples; separate prefix/gateway/DNS jobs; DHCP; local versus routed destination | Slides 12-14, 25-29 min |
| Packet distribution | Successive diagrams for one recipient, local scope and joined group | Slides 15-17, 29-35 min |
| Transport | TCP handshake and ordered bytes; UDP datagrams; freshness versus ordered delivery | Slides 18-19, 35-40 min |
| Endpoints | Shared listener; bold, color-labeled URL; localhost and remote destination | Slides 20-22, 40-49 min |
| Diagnostic evidence | Address, listener and reply questions; probing versus capture; paired fault reasoning | Slides 23-26, 49-60 min |
| Application protocols | Ordered jobs, illustrative DNS lookup, HTTPS, WebRTC versus WebSocket; qualifications in notes | Slides 28-31, 70-80 min |
| APIs and REST | Request/response; artwork address; read/create; change/remove; separate status and validation; request/data lifetimes | Slides 32-39, 80-94 min |
| WebSocket code | Connection/message sequence and highlighted client, echo and server-push excerpts | Slides 40-43, 94-103 min |
| Message and state boundaries | Framing; shared scene; state versus ack; uncertainty; reconnect | Slides 44-49, 103-115 min |
| Project and next-week connection | One state/command/failure; PFAD handoff and pinned Multiboxes game/tutorial/protocol references; app becomes a resource client | Slides 50-53, 115-120 min |

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
| Slide 24, network effects / Metcalfe | Retained with qualification | Slides 5-6: introduce the proposed value model using 2/3/4 nodes and 1/3/6 possible pairs, then compare equally sized silent and active groups. |
| Slide 25, duplex/reachability/protocol/routing/ACK | Restored | Slides 7-8, 14 and 46: process roles, direction capability, agreed rules, next hop and TCP ACK versus application result. |
| Slide 26, OSI/TCP-IP diagram | Restored substantially | Slides 9-10: all seven OSI layers, approximate grouping into four Internet layers, concrete encapsulation and segmentation. No “not a full OSI course” substitution. |
| Slide 27, wired/wireless links | Restored | Slide 11: Ethernet, Wi-Fi/5G, Bluetooth, LoRa, USB, I2C and 1-Wire; rate/range/power tradeoffs without fictional fixed specifications. Sensor buses are not all IP networks. |
| Slide 28, IPv4/v6, DHCP, netmask, gateway | Restored | Slides 12-14: address sizes/examples, prefix, gateway, DHCP and IPv6 auto-configuration; local versus routed destination. |
| Slide 29, unicast/broadcast/multicast diagram | Restored as separate diagrams | Slides 15-17: unicast one destination, scoped broadcast, multicast group. IPv6 has no broadcast. WebSocket fanout is a different application mechanism. |
| Slides 30-31, TCP/UDP | Restored/corrected | Slides 18-19 and 44: handshake, ordered stream, retransmission/failure, UDP datagrams and framing. No claim of error immunity or a universal three-times packet count. |
| Slides 32-33, DNS/HTTP/HTTPS/WS/WebRTC | Restored/expanded | Slides 28-31 and 40: distinct protocol purposes, DNS resolution/cache, TLS protections, HTTP/3 caveat, live media versus control messages. |
| Slide 34, ports | Restored/corrected | Slides 20-22: many connections share a listener, source/destination endpoint pairs, URL path and server binding. A port is not limited to one connection. |
| Slide 35, commands and tools | Restored | Slides 23-26: ipconfig, ifconfig, ip, netstat/ss, curl, Nmap and Wireshark; own-lab authorization, packet privacy and evidence-based diagnosis. |
| Slides 36-37, API requests/responses | Restored | Slides 32-33: method/path/headers/body into an app, status/body back; a concrete GET /state trace and creative-service examples. |
| Slide 38, REST | Restored/corrected | Slides 34-39: resources, representations, GET/POST/PUT/PATCH/DELETE, stateless request context versus stored data; /action is a command API, not advertised as full REST. |
| Slide 39, persistent bidirectional WebSocket | Restored | Slides 40-43: full-duplex capability contrasted with chosen send/recv loop and independent server push. Persistence of a connection differs from durable data. |
| Slide 40, API examples | Retained with relevant examples | Slide 32 uses the current scene; notes retain weather/gallery examples; earlier tide and MediaPipe supply the course connection, without adding accounts or paid services. |
| Slides 43-45 and actual historical WebSocket files | Retained as code, corrected context | Slides 41-43 quote pinned client, echo and push excerpts. Old slide/README paths are not an installation guide. `Ping!` is text data, not a Ping control frame. No old unpinned server is run on presenter port 8765. |
| Earlier draft's detailed Scene/validation/await/lock/retry walkthrough | Simplified by instructor, with optional references | Lecture retains framing, local/shared state, state/ack, uncertainty and reconnect concepts. Tutorial core is one action, a `Scene.apply` boundary edit and reconnect in 30 minutes. Locking, fanout limits, exact JSON checks and uncertain replies remain optional code references. Multiboxes observation takes 30 minutes; the final 40 are for group work and TA feedback. |
| Slides 46, 53-58, speech/audio queues | Remain moved | Current W6 already taught speech; later handbook-agent work can reuse it. No audio/GPU stack is restored to networking. |
| Slides 47-52, setup/friend connection | Updated | Existing two-hour tutorial uses uv/two local views with setup fallback and project support. LAN/mobile is an optional authorized/rehearsed extension, not required exposure. |
| W8 MediaPipe and historical OSC creative control | Retained bridge / optional | Opening links sensing to a message. OSC address/value-to-JSON remains an optional tutor explanation, not a pretend running adapter or required setup. |
| 2026 former MCP block | Remain outside W9 core | No generic permission role-play replaces networking theory. |
| Historical project/assessment pages | Superseded policy | Preserve current 40%, 25/50/25, public sd5913 repository, Canvas and 6 December 2026 23:59 HKT. No new quiz/submission. |
| Historical Orange/t-SNE material | Remain removed by instructor | W11 time stays reallocated to Blender/Godot; no new dependency here. |

## Source pins and corrections

The revised modern tutorial is pinned to
[`sd5913/pfad@66067e191bd1c58b9c8d530dbc3fa8b50d69657a/week09`](https://github.com/sd5913/pfad/tree/66067e191bd1c58b9c8d530dbc3fa8b50d69657a/week09).
This documentation revision uses the existing small scene without runtime
changes. Its timetable, relative links and pinned Multiboxes source paths were
checked on 4 November. The earlier runtime evidence remains dated; no new
Multiboxes or classroom-device run is claimed.

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
Keep earlier companion runtime evidence dated and distinguish documentation
checks from a fresh runtime or classroom rehearsal.

### Local clarity-pass evidence, 4 November

The focused Week 9 suite passes all six checks. The final 53-slide HTML,
Chromium PDF and both PowerPoint variants build with overflow checking and no
overflow warnings. Both PowerPoint packages contain 53 slides and 53 notes,
including the pinned PFAD and Multiboxes hyperlinks. All HTML slides were
inspected at 1920x1080 across the clarity and final handoff passes. The DNS,
code, revised timetable and Multiboxes slides were also checked in actual PDF
page renders. A 390x844 browser check preserves the address composition and
working keyboard navigation. The browser reported no page errors, and the
address host renders at weight 700 with its blue role color. The Impeccable
mechanical scan reported no findings.

The 53rd slide links the current source, selected PFAD observation and protocol
at verified Multiboxes commit
`2977be17b35790dd7b31f1f242b0dc86113d5350`. The game uses Python/Pymunk authority,
browser rendering, JSON controls and complete binary state snapshots. This
supports the selected 30-minute observation. The external full study guide is
further reading. The PFAD README and lecture handoff share the revised
0-10 setup / 10-40 WebSockets / 40-50 break / 50-80 Multiboxes / 80-120 group
work and TA feedback route.

This pass is a local instructor-review draft on an isolated branch. It adds no
PFAD runtime or assessment change. Native PowerPoint/ClassPoint rehearsal is
still distinct from export/package verification.
