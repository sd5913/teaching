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
#   None      the exercise deliberately has no check (the starter is the lesson)
#   FREE      the starter passes as given, on purpose — the one drill whose job is the
#             green tick itself (and the Pyodide download), not the thinking
#   callable  takes the deck module and returns the code, for a solution the deck
#             already holds (the Nake drills are a broken copy of the deck's NAKE)
FREE = 'passes as given, by design'
SOLUTIONS = {
    # 04 · six types
    'does-the-box-work': FREE,
    'ask-python-what-it-is':
        'print(type(3))\nprint(type(3.14))\nprint(type("3"))\nprint(type([]))',
    'the-quotes-change-the-answer':
        'a = "6"\nb = "6"\n\nprint(int(a) + int(b))',
    'everything-is-looked-up-the-same-way':
        'word = "design"\n'
        'colours = ["red", "green", "blue"]\n'
        'student = {"name": "Ada", "year": 2026}\n\n'
        'print(len(word))\nprint(word[0])\nprint(student["name"])\n'
        'print(colours[-1])\nprint(student["year"])',
    'put-a-value-inside-a-sentence':
        'name = "Ada"\nyears = 36\n\nprint(f"{name} is {years}")',
    # 05 · reading a rule
    'run-the-rule': None,
    'half-the-picture-is-solid': lambda mod: mod.NAKE,
    'does-this-still-meet-the-spec': lambda mod: mod.NAKE,
    # 06 · surprises
    'make-the-comparison-true':
        'total = 0.1 + 0.1 + 0.1\n\nprint(abs(total - 0.3) < 1e-9)',
    'make-b-a-real-copy':
        'a = [1, 2, 3]\nb = a.copy()\nb.append(4)\n\nprint(a)',
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
            if SOLUTIONS[e.eid] is FREE:
                if given['ok'] is True:
                    print(f'  ok   {e.eid}: passes as given, by design')
                else:
                    print(f'  FAIL {e.eid}: meant to pass as given, but does not — '
                          f'out={given["out"]!r} err={given["err"][-60:]!r}')
                    fails.append(e.eid)
                continue
            if e.expect is None and not e.check:
                what = (given['err'].splitlines()[-1][:44] if given['err']
                        else 'prints ' + repr(given['out']))
                print(f'  ok   {e.eid}: no check by design — starter {what}')
                continue
            if given['ok'] is True:
                print(f'  FAIL {e.eid}: the starter code already passes')
                fails.append(e.eid)
                continue
            solution = SOLUTIONS[e.eid](mod) if callable(SOLUTIONS[e.eid]) else SOLUTIONS[e.eid]
            got = json.loads(run(solution, e.check or '', e.expect))
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
