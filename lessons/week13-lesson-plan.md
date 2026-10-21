# Week 13: explain the loop, explain your work

Instructor draft for content `week13`; class date is Thursday 3 December 2026;
class duration and final-quiz time/format are not confirmed. This lesson is not an assessment announcement.

## Outcome and preparation

Students should explain a small program as input, state, control flow, output and
evidence, then identify a reproducibility gap. They can use their own work or a
previously taught example. No new file, tool, team arrangement or deliverable is
required. The matching student [Week 13 companion draft](https://github.com/sd5913/pfad/pull/16)
contains a short trace, runnable stdlib loop and another-computer check, not a new assessment.

Before class, confirm (1) class duration and final-quiz time/format with gio,
(2) which later-week concepts were actually taught, (3) the current project
brief and submission route, and (4) working links to whichever current weekly
examples are selected. The historical PDF is not evidence for 2026 timing or
policy. Prepare a short taught example and a safe small sample input; do not
bring private submissions or secrets to the projector. There is no live AI news
slot in this advance draft. If relevant news is added close to class, check the
primary-source event/publication dates, claim and classroom connection, and
omit it rather than displacing review or assessment time.

## Flexible run of show

| Slides | Move | Keep if time is short |
|---|---|---|
| 1–7 | Welcome; map Weeks 1–6 through one input-state-output example; optional peer comparison. | Ask for one prediction about a changed input. |
| 8–13 | Predict the loop output; trace all checks and a zero-limit case. | Show how step changes and why it stops. |
| 14–20 | Connect review vocabulary to work actually taught. Slides marked **IF TAUGHT** are optional. | Do not introduce untaught concepts as assessed content. |
| 21–26 | Explain repository-to-result; try an optional second-machine check or paper fallback; discuss a failure report. | Record one observed result and one limitation. |
| 27–29 | AMA, assessment boundary and closing reflection. | Leave space for real questions. |

Slide numbers should be checked against the rendered deck if slides are added.
Allocate minutes only after the instructor confirms the class duration and any
final-quiz slot. Keep the assessment slot separate; do not transfer the
midterm's question count or length. If time is tight, skip slides 16–20 and
shorten the three-clue discussion, not the trace and questions.

## Worked example and fallback

On slide 9, stop before advancing. Ask students to predict the printout of
`limit = 3; step = 0; while step < limit: print(step); step += 1; print("done")`
as laid out on separate lines. Slides 10–11 reveal 0, 1, 2, then done. For
`limit = 0`, the body does not run and only done prints. Ask what happens if
the increment is removed, but **do not run** that infinite version in class.
An incorrect prediction is useful if a student can locate the condition or
state update that explains it. A paper trace is enough; there is no install.

The diagram on slide 10 is a conceptual left-to-right map, not a literal
straight-line control-flow chart. On a true condition the body increments and
returns to the test; on false it exits to the final print.

For the reproducibility exercise, ask for a repository link and a short run
instruction only if the student is comfortable sharing. On a spare device,
follow the documented steps and compare one predicted and observed result.
Without a second machine, trace from a clean-start checklist on paper:
files, relative paths, dependencies, command, expected output. If anything is
missing, record the gap and improve one instruction. Do not publish personal
data or a secret to make the example work. No team presentation is required.

## Source decisions

The supplied 2025 Week 13 PDF (1-based pages) has recap/final/AMA/tutorial
on pp. 2, 3–26, 27 and 28 respectively. Retained: a synthesis structure,
a small conditional-loop question (p. 6), optional class/object vocabulary
(p. 8), a map of Scrum, Docker and networks (pp. 13–17), permission-aware
agent/MCP/tool discussion (pp. 25–26), questions and another-computer test
(pp. 27–28). Replaced: archive's assessment-simulation code with a finite
trace and current-course example; archived submission/Blackboard instructions
with current instructor guidance. Not copied: p. 5's misleading assignment
wording, p. 21's unsafe password screenshot, advanced asyncio (p. 12),
historical final timing or assumed group membership. None of the archive's
topic inventory establishes what was taught in later 2026 weeks.

Current anchors: teaching `deck/week01.py` (assessment weights and content-week
placement), `deck/week02.py` (values and control flow), `deck/week04.py` (interface
and tests), `deck/week05.py` (images), `deck/week06.py` (sound), and the student
[PFAD companion PR #16](https://github.com/sd5913/pfad/pull/16). The companion
now includes a runnable stdlib loop; its partner check and paper fallback align
with slides 23–24. The optional later-week cards must be reconfirmed before
teaching and should not be used as an assessment coverage list.

## Open decisions

- Confirm class duration and final-quiz time/format; class date is Thursday 3 December 2026.
- Confirm actually taught later-week concepts and remove irrelevant optional slides.
- Confirm project submission route and deadline against the current brief.
- Verify the selected taught practical on the teaching computer; no live service
  or student project has been run as part of this deck draft.
