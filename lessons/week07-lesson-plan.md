# SD5913 Week 7 · 22 October 2026

## Flow

Twenty selected concept slides from the taught Weeks 1–6, then an Ask Me Anything
ClassPoint inbox. Reserve fifteen minutes for each before the fixed **10:00–10:30
HKT** Canvas midterm. If opening at 09:30, use 09:30–09:45 and 09:45–10:00;
otherwise adapt the recap to the actual timetable without moving the test.

After the test, use the following schedule. **Class finishes at 11:20 HKT.**

| Time | Activity |
| --- | --- |
| 10:30–10:35 | Break after confirming test submission. |
| 10:35–10:42 | Short classes explanation and the shared-ball laptop demo. |
| 10:42–10:44 | Brief app/game inspiration. |
| 10:44–10:45 | Demonstrate the actual Canvas team-registration route; one minute maximum. |
| 10:45–11:00 | Team formation, registration, idea discussion and one ClassPoint text response. |
| 11:00–11:15 | One image mock-up and ClassPoint upload. |
| 11:15–11:20 | Check both submissions, help ungrouped students, Assignment 3 reminder, finish. |

The first fifteen-minute activity includes team formation and registration. The
text contains the team name, intended user/player, action, program response,
what is reinvented/combined and the first interaction to test. Suggested split:
four minutes team setup, eight minutes choosing/describing, three minutes
submission/check.

The second fifteen-minute activity includes making and checking the image
upload. The same representative uses the same team name. Show a screen or
moment of use with action/response, not just a logo. Photographing a paper
sketch is sufficient.

No extra prototype, video, pitch deck or critique submission today. Use remaining
time for feedback and helping ungrouped students. Team size follows existing
instructor arrangements; no SD2112 team-size rule is imported.

## After the break: classes through one moving ball model

Classes are the only new theory in this short section. Demonstrate from the
laptop; watching is enough and students have no extra submission. Use the real
[PFAD Week 7 example](https://github.com/sd5913/pfad/tree/2026/week07), merged
through PFAD PR #17.

1. Show `Ball.__init__`: a class defines attributes and methods; `red` and `blue`
   are separate instances with their own `x`, `y`, `vx`, `vy` and `radius`.
   `self` means the object receiving the method call.
2. Trace the first three lines of `Ball.update(seconds)`: gravity changes
   velocity, then velocity changes position. The rest of the method handles
   bounces. Predict whether `red.update(0.1)` also moves blue, then run
   `uv run week07/ball.py` from `~/Work/sd5913/pfad` to check.
3. Run `uv run week07/ball_both.py`. Keep the ASCII terminal and Pygame window
   visible together: the same ball objects and simulation ticks feed both
   renderers. ASCII has a coarser grid; it does not have different physics.
4. Edit `week07/ball.py`: change `GRAVITY = 28` to `GRAVITY = 56`, predict the
   result and save. Both views stay open and reset using the edited class.
   Restore 28 and save after comparing. Space pauses/resumes; R resets;
   closing Pygame stops both.

Keep `ball_live.py`, file watching and renderer internals as optional tutorial
reading. Saving resets the simulation; it does not migrate existing objects.
Warm up the launcher before class so dependency downloads do not use demo time.

## Framing and assessment

Build something amazing with your team. Ambitious useful apps, creative tools and
game mashups are welcome. AI may help development but need not be inside the final
product. Independently implement ideas using original/licensed code and assets;
use permitted targets for software inspection. REA is the reference found in the
taught slides, not a verified Hera reference. Do not claim Melty uses REA.

The midterm remains 40 multiple-choice questions, 30 minutes, open book, 10% of the
course. Announce tool/collaboration permissions; open book alone does not settle
AI use. No exam questions or keys are present in this repository.

Group project stays 40%: shared GitHub repository, everyone's commits, original
code, multimedia, scope agreed by Week 8. Today's two submissions are provisional
idea-development work. Do not invent further final deliverables or rubric rules.

Individual Assignment 3 stays separate: 15%, due 1 November 2026 23:59 HKT, own
GitHub URL submitted on Canvas, existing brief and documentation requirements.

## Before class

- Verify Canvas availability, timer, accommodations and hidden answers.
- Check actual group set and registration permissions; demonstrate without exposing
  unrelated student records.
- Open the AMA, team text and team image activities; ensure upload works.
- Open `pfad/week07/ball.py` and warm up `uv run week07/ball_both.py`; restore
  the starting source after any rehearsal edits.
- Use the HTML deck for links; no new accounts or paid generation are required.
- Importing old slides must not import their old ClassPoint response links.

## Sources

Recap imports current deck/week01.py through week06.py by exact title, with old
chrome/collection metadata removed. Week 1 establishes assessment weights and
Week 8 scope agreement. Week 6 establishes quiz format/date. Assignment 3 uses
syllabus/03-interactive-experience.md. Workshop flow adapts SD2112 Week 7, without
its AI + X framing or course-specific assessment deliverables. The classes demo
uses the current PFAD Week 7 `Ball` example rather than the older catch game.
