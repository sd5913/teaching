# SD5913 Week 11: Connecting creative tools

Instructor draft. Content number `week11` only; date and class length are **not confirmed**. The core route uses printed, synthetic values and standard Python. Do not present the companion planning PR as a released runnable tutorial.

## Outcome and evidence

A pair follows one value across a sender/receiver boundary, names its range and meaning, predicts a result and decides what a missing update should do. Collect an informal labelled input/output sketch, a mapping and a safe-stop explanation in discussion only. No new assessment, mandatory AI, paid service, camera or additional installation.

The optional opening news slot stays empty until a recent source is verified with event/publication dates, primary link, supported claim, classroom connection and test status. If none passes that filter, omit it.

## Preparation

- Open the targeted HTML/PDF deck and check both diagrams and notes. Have Python available for a scratch file, or use arithmetic and paper only.
- Trace `0.50 -> 50%`, then `0.75 -> 75%`; test `3` (clamped to 100) and `"oops"` (fallback 0). These are simulated messages: printing `receive ...` does **not** receive OSC.
- If demonstrating OSC, prepare and rehearse a *local* receiver independently: explicit address `/control`, matched port, known numeric mapping, receiver-side validation and timeout/reset. No receiver is shipped in the Week 11 PFAD companion draft. If anything is unverified, use printed trace; do not open a network port in class by default.
- If using the Blender alternative, start with a disposable prepared scene with `Cube`, camera and light. The `bpy` excerpt changes scale in Blender only; it does not create the scene or render. Keep students' project files out of reach of any old scene-clearing script.
- No camera, NDI, GPU or sign-up for the core lesson. If recording/transmitting images on an optional extension, check device permission and participants' consent and stop the stream before leaving the session. For any agent/MCP example, restrict to an explicit read-only capability first; human approval and a narrow target are required before a write.

## Pacing (adapt to the confirmed slot)

Suggested **70-minute core**, not a claim about the timetable. If a longer class is confirmed, use remaining time for project work and questions. If shorter, omit optional tools and the opening discussion, not the failure test.

| Minutes | Slides | Move |
|---|---|---|
| 0-8 | 1-4 | Ask what changes across programs; identify the goal. |
| 8-19 | 5-9 | Show name, attribute, method; predict the plain Python `print`. |
| 19-38 | 10-17 | Build sender/boundary/receiver in successive diagrams; run printed trace; predict 0.75; validate 3 and `"oops"`. |
| 38-53 | 18-21 | Ask what a silent sender means; run the pair lab (3 min sketch/predict, 5 min edit or calculate, 2 min absence, 2 min share). |
| 53-62 | 22-24 | Compare local Blender property, local HTTP request and OSC. Skip installs. |
| 62-70 | 25-29 | Explain optional MCP permission boundary briefly; close with project application and one pair's safe-stop explanation. |

If the room has no devices or Python, students calculate the exact trace on paper. If a local receiver disconnects, its last value may remain: do not claim it reset unless a tested timeout exists. Ask teams for a small independently testable increment rather than turning the old tutorial's team update into an assessed presentation.

## Historical-to-current decision

The supplied OneDrive 2025/2025-26 Week 11 PDF (78 pages; archive README/manifest verified, 1-based pages) shows object/storage recap on pp. 4-17; Orange on pp. 18-30; Blender on pp. 31-39; TouchDesigner on pp. 40-44; NDI/OSC and hand tracking on pp. 45-55; networked game/async on pp. 56-60; and tutorial on pp. 61-78. Retain the object's attribute bridge and broad tool map; replace the installation tour with one synthetic, finite input-to-output trace and a stop test. Blender is an alternative. Move Orange, NDI/camera, TouchDesigner and networked game into references or optional extensions; do not teach asyncio as a prerequisite. Historical slides are evidence of an earlier design, not evidence of a 2026 date, project policy or software readiness. The current PFAD Week 11 companion is [draft PR #14](https://github.com/sd5913/pfad/pull/14) at ca66f05: a planning README, not executable code. Site/slide publication awaits teaching review.

## Review limits

Rendered deck and tests verify slide generation only. No OSC packet/receiver, Blender render, actual MCP server, camera, network latency or classroom permission flow has been tested here. Confirm timetable, receiver choice and teaching machine before calling live demonstrations ready. No assessment policy or confirmed deadline is changed.
