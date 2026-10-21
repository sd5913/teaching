# Week 10 · One class, two objects, and saved records

Teaching date and class duration are not confirmed. This run sheet orders the core work; the instructor should allocate actual minutes once the timetable is confirmed. Content number `week10` is not a calendar-week assertion. The slides use fictional artworks throughout and add no new assessment rules.

## Outcome and preparation

Students should be able to create two instances of one small Python class, explain their independent attributes and a method, then relate those objects to records that can be saved and loaded. Bring a Python 3 interpreter and a writable disposable directory for `artworks.json`. No package install, account, network, Docker or real credentials. Use the two-object trace and a drawn JSON table if the computer setup is unavailable. The proposed student companion [PFAD Week 10 PR #13](https://github.com/sd5913/pfad/pull/13) contains planning activities only; it does **not** yet supply runnable files.

## Teaching route

1. **Opening and prediction (slides 1–10).** Invite a familiar project thing, show the class and two separate artwork instances, then pause before slide 8 for a paired prediction: after `amber.view()`, what happens to `blue.views`? Expected values are 3 and 7. Run the self-contained code on slide 9 or trace it on paper. Have students produce and explain two fictional instances of their own. Keep constructor, attribute and method distinct; don't teach inheritance as the first step.
2. **Link records (slides 11–14).** Follow `e1` from the exhibition into two artworks; ask what `exhibition_id` means and what happens with `e99`. JSON does not enforce foreign keys, so a successful parse is not evidence the reference exists. Many-to-many is recognition only, not a required implementation.
3. **Save and restart (slides 15–22).** Contrast live objects with the file. Run slide 18 in a disposable working directory, close Python, and run slide 19 in a new process in the same directory. Slide 20 is an excerpt that needs the class definition and loaded records in scope. Pause at slide 21: missing file raises `FileNotFoundError`; malformed JSON raises `JSONDecodeError`; a missing referenced ID is not caught by JSON. Re-running slide 18 overwrites its example file, so do not use a student's existing file. Never enter a real password.
4. **Project application (slides 23–24, 28).** Partner sketch: two objects, one method, two saved records and an optional link. Which values need to survive closing the program, and which can be recalculated? Treat this as working evidence, not an assessed submission. If no state needs persistence, accept that answer with an explanation.
5. **Only if time remains (slides 25–27).** Search three fictional/public exhibition passages for support and also ask an unanswerable question. Retrieval is a candidate source, not proof. Show a read-only agent → MCP server → tool pathway without executing a tool or granting permissions. The Git/Scrum/Docker/network map indicates related topics without setting dates or requirements. Cut this block first to protect core explanation and practice.

Close with a short Q&A and the exit prompt on slide 28. No verified Week 10 news item is included; any future opening news needs a primary source, event/publication dates, a supported claim and an explicit testing caveat, and should be cut before core practice.

## Historical-to-current mapping

Historical source: `SD5913 - PFAD - Week 10.pdf`, 67 PDF pages, archived outside this public repository. Page numbers below are PDF positions. Archive README and manifest identify it as 2025 source evidence, not the 2026 timetable.

| Historical PDF | This draft | Change |
|---|---|---|
| pp. 13–24: object attributes, relation types and prompts | slides 4–14 | Retain the prediction/relationship format; first teach a plain class and two instances. |
| pp. 25–31: IDs, SQL and Peewee | slides 12–13, 16–20 | Retain stable IDs and records; replace ORM inheritance with standard-library JSON; SQL remains a later option. |
| pp. 32–38: database types and persistence | slides 16–22 | Retain the storage decision and restart test; no database container required. |
| pp. 39–43: login and hashing | slide 22 safety note only | Omit the historical login implementation: bare SHA-256 is unsuitable for password storage. |
| pp. 44–55: retrieval/RAG | slide 25 | Move to optional evidence-inspection discussion; no model, handbook corpus or vector service. |
| pp. 56–67: tutorial/setup and prototype | slides 10, 24, 28 | Retain project reflection; omit historical setup commands and any obsolete date/team/assessment instructions. |

The current 2026 student companion is a proposed planning README; do not claim the course repository supplies a tested script or executable storage starter. Individual Assignment 3 and the group project remain separate; no new deadline, mark or format is established here.
