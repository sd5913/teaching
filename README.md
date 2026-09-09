# SD5913 · Programming for Artists and Designers — teaching repo

Slides and class planning for PolyU School of Design, Semester 1 2026/27.
Lecturer Giovanni Lion (giovanni.lion@polyu.edu.hk).

This repo holds **sources only**. The slide toolchain is not in here — it is
[`ait4x/deckgen`](https://github.com/ait4x/deckgen), pinned by tag in `requirements.txt`
and shared with `venetanji/sd2112-teaching`. A fix to the PowerPoint or ClassPoint
plumbing lands in both courses at once.

Two GitHub Actions workflows run on every push to `main` (and on demand):

| Workflow | What it makes | Where it goes |
|---|---|---|
| **Publish site** (`.github/workflows/site.yml`) | The html decks, a PDF of each without the ClassPoint buttons, the landing page. | GitHub Pages (Week 2: `/week02/`). |
| **Build PowerPoints** (`.github/workflows/pptx.yml`) | `week02.pptx` (plain), `week02-classpoint.pptx` (ait4x master, animations, live ClassPoint buttons), the activity manifest, `.docx` of anything in `syllabus/` and `lessons/`, preview sheets. | One artifact per deck, `sd5913-week02` and so on, plus `sd5913-documents` for the `.docx`, kept 90 days. A deck whose inputs did not change is restored from the Actions cache, not rebuilt. Not published. |

## Layout

| Path | What |
|---|---|
| `deckgen.toml` | The course: code, name, year, footer, which decks, what gets published. |
| `deck/week02.py` | **Week 2 as one Python spec**: text, speaker notes, ClassPoint activities, in the order the class runs. Edit here; every output updates. |
| `deck/assets/` | Images. `deck/assets/generated/` is drawn at build time and git-ignored. |
| `lessons/` | Instructor run sheets. Built to `.docx` in the artifact, **not published**. |
| `syllabus/` | Published only if listed under `[[publish]]` in `deckgen.toml`. |
| `site/index.html` | The landing page. The reveal.js vendor bundle is added by the build. |
| `archive/` | The PowerPoint actually shown in class, per week, where it was not generated from `deck/`. Week 1 lives here — it was built by hand. |

Generated and git-ignored: `_site/`, `export/`, `deck/assets/generated/`, `node_modules/`.

## Build locally

```bash
uv venv && uv pip install -r requirements.txt
deckgen build --pptx          # export/: PowerPoints, manifest, docx, previews (no node needed)
deckgen build --site          # _site/: html decks, PDFs — needs node + playwright
deckgen build                 # both
deckgen build --no-pdf        # skip the Chromium step
```

The PDF step needs node 18+ and Playwright's Chromium:
`npm install --no-save playwright@1.56.1 && npx playwright install chromium`.
The html deck: arrow keys, `S` speaker notes, `O` overview, `F` full screen.

`deckgen build` **exits non-zero if any text overflows its box**, so a broken slide fails
the workflow rather than reaching the projector. Previews land in `export/preview/`.

## Classroom checklist

1. Download that week from the latest *Build PowerPoints* run (Actions → Artifacts → `sd5913-weekNN`), or from a terminal:
   ```bash
   gh run download -R sd5913/teaching -n sd5913-week02 \
     $(gh run list -R sd5913/teaching -w "Build PowerPoints" -L1 --json databaseId -q '.[0].databaseId')
   ```
2. Install Inter and JetBrains Mono on the classroom PC — they ship inside the `deckgen` package (`python -c "import deckgen, pathlib; print(pathlib.Path(deckgen.__file__).parent / 'fonts')"`). Restart PowerPoint. Slide 1 should show *Inter Black* in the font box; Arial substitutes automatically if not.
3. Open the deck with the ClassPoint add-in and fire one activity before class — a malformed tag fails silently.
4. Import the roster as the saved class. Students join with the last four digits and the letter of their ID.
5. Keep the html deck or the PDF open on a laptop as backup.

## After the class: publish the answers

ClassPoint keeps every activity on a **public** page at
`app.classpoint.io/activity/<activityId>` — no login, all the responses on it. Once a week
those links go into the deck, so a student can find their own work again in week 12.

1. Open [the ClassPoint activities dashboard](https://app.classpoint.io/cp/reports/activities).
   It is behind the login and has no API, so save the page: devtools → copy the cards
   element → paste into a file.
2. Run the routine from [`classpoint.py`](https://github.com/venetanji/classpoint.py):

   ```bash
   python3 weekly.py --repo ~/dev/sd5913/teaching --week weekNN \
           --on YYYY-MM-DD --from-html ~/Downloads/activities.html
   ```

   `--on` is the date the class ran, and it matters: it is what separates this course's
   activities from SD2112's, which are on the same dashboard a day apart. The runner
   fetches each activity, reads `deck/weekNN.py` with `ast` to get the question text, and
   writes `deck/weekNN-reports.json` and [`ANSWERS.md`](ANSWERS.md). Both are rewritten in
   place, so running it twice is running it once.
3. `deckgen build` — the eyebrow of every question slide gains a **YOUR ANSWERS** link, and
   the build fails if the deck and the mapping have drifted apart.
4. Commit both files and open a PR.

Each `deck/weekNN.py` calls `attach_reports(S, …)` just before `DECK = …`. It is a no-op
until the mapping file exists, so a week authored today picks its links up the week it is
taught, with no edit.

**Week 1 has no deck here yet**, so there are no slides to hang links on and nothing for
`ast` to read. Its five questions were typed into `deck/week01-reports.json` by hand, off
each activity's own slide image — the only surviving record of what was asked — and
`ANSWERS.md` plus the site footer are where students find them. Any later run keeps that
typing.

When `deck/week01.py` does exist, the one `attach_reports(S, …)` line is all week 1 needs:
the mapping is already in place, and because it carries the question text, **deckgen checks
the regenerated deck against what the room was actually asked** and fails the build if they
disagree.

**Activities run with names hidden are not linked.** ClassPoint's page honours
`isNamesHidden`, but the payload behind it still carries `participantName` for every
response — so linking one would hand out a way to undo the anonymity the room was
promised. `weekly.py` records those with a null id and no link, and `ANSWERS.md` says so.
None of week 1's five were run that way. The same null id also withholds a link by
choice: week 1's fifth activity was a poll on moving tutorial group, which is
administrative rather than course material, so it is recorded but not linked.

## Keeping the repository public

Nothing in the sources identifies a student. Keep it that way:

- Student IDs, rosters and ClassPoint exports stay local — `roster/`, `ids.csv` and
  `classpoint/*.csv` are git-ignored. The roster lives in `~/dev/sd5913/roster/`, which is
  a different directory on purpose.
- Grades, gradebooks and submissions never enter the repository, not even in a branch:
  the history is public too.
- Workflow artifacts on a public repo are downloadable by anyone with a GitHub account.
  The PowerPoint artifact is fine; a roster would not be.

## Related

- [`sd5913/pfad`](https://github.com/sd5913/pfad) — the course repo students clone. Branch `2026` is this year, `2025` is the archive.
- [`sd5913/github-student-registry`](https://github.com/sd5913/github-student-registry) — the ID ↔ GitHub matcher at <https://pfad.ait4x.org>.
- [`ait4x/deckgen`](https://github.com/ait4x/deckgen) — the slide toolchain this repo uses.
- `~/dev/sd5913/` — the private admin workspace: course plan, deck reviews, roster, org scripts.
