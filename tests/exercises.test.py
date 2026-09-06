#!/usr/bin/env python3
"""
Every in-slide exercise must start unsolved and be solvable.

    python tests/exercises.test.py

Two ways an exercise fails a class of 112, both silent:

  the starter code already passes  — the drill teaches nothing, and they learn that
                                     pressing Run is what makes the box go green
  the expected output is wrong     — a correct answer is marked wrong, in public,
                                     and you cannot fix it from the lectern

So each exercise is run twice: once as the student first sees it, which must NOT pass,
and once with the intended solution from SOLUTIONS below, which must. Add the solution
here when you add an exercise; a missing one fails the test rather than being skipped.

Pyodide runs the same CPython this does, so a pass here is a pass in the browser.
"""
import importlib.util
import json
import pathlib
import sys

import deckgen
from deckgen import configure
from deckgen.project import Project

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUNTIME = pathlib.Path(deckgen.__file__).parent / 'js' / 'pyodide-runtime.py'

# eid -> the code a student who understood it would end up with.
# None means the exercise deliberately has no check (the starter is the lesson).
SOLUTIONS = {
    'run-it-and-see': None,
    'now-make-it-survive':
        'rows = [{"year": 2024, "height": 2.1}]\n\n'
        'def mean_height(rows, year):\n'
        '    out = [r["height"] for r in rows if r["year"] == year]\n'
        '    if not out: return None\n'
        '    return sum(out) / len(out)\n\n'
        'print(mean_height(rows, 2025))',
    'make-the-comparison-true':
        'total = 0.1 + 0.1 + 0.1\n\nprint(abs(total - 0.3) < 1e-9)',
    'stop-the-aliasing':
        'a = [1, 2, 3]\nb = a.copy()\nb.append(4)\n\nprint(a)',
    'two-different-questions':
        'def describe(rows):\n'
        '    if rows is None:\n        return "missing"\n'
        '    if rows:\n        return "got data"\n'
        '    return "empty"\n\n'
        'print(describe([1, 2]))\nprint(describe([]))\nprint(describe(None))',
    'the-list-that-remembers':
        'def collect(item, seen=None):\n'
        '    if seen is None:\n        seen = []\n'
        '    seen.append(item)\n    return seen\n\n'
        'print(collect("a"))\nprint(collect("b"))',
    'it-gives-you-none':
        'def double(x):\n    return x * 2\n\nprint(double(21))',
}


def load_deck(proj, name):
    spec = importlib.util.spec_from_file_location(f'deck_{name}', proj.decks_dir / f'{name}.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    proj = configure(Project.load(ROOT))
    g = {}
    exec(RUNTIME.read_text(), g)
    run = g['_dg_run']

    fails, n = [], 0
    for name in proj.decks:
        mod = load_deck(proj, name)
        exes = [e for s in mod.DECK['slides'] for e in s.els if e.kind == 'exercise']
        print(f'{name}: {len(exes)} exercises')
        for e in exes:
            n += 1
            if e.eid not in SOLUTIONS:
                print(f'  FAIL {e.eid}: add its solution to SOLUTIONS in this file')
                fails.append(e.eid)
                continue
            given = json.loads(run(e.code, e.check or '', e.expect))
            if e.expect is None and not e.check:
                what = (given['err'].splitlines()[-1][:44] if given['err']
                        else 'prints ' + repr(given['out']))
                print(f'  ok   {e.eid}: no check by design — starter {what}')
                continue
            if given['ok'] is True:
                print(f'  FAIL {e.eid}: the starter code already passes')
                fails.append(e.eid)
                continue
            got = json.loads(run(SOLUTIONS[e.eid], e.check or '', e.expect))
            if got['ok'] is not True:
                print(f'  FAIL {e.eid}: intended solution does not pass — '
                      f'out={got["out"]!r} err={got["err"][-60:]!r} msg={got["msg"][:60]!r}')
                fails.append(e.eid)
            else:
                print(f'  ok   {e.eid}: starts failing, solution passes')
    print(f'\n{len(fails)} of {n} FAILED: {fails}' if fails else
          f'\nall {n} exercises start unsolved and are solvable')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
