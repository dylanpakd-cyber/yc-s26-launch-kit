#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""Check hooks and first lines: length, the yes/no hook gate, the five-question score, and the weighted grader.

Usage:
  python3 check_hooks.py <hooks file> [--max-chars 130]
  python3 check_hooks.py --selftest

One hook per line, fields split by " | ". Only the text field is required:
  <hook text> | gate: Y Y Y Y Y Y Y Y | score: 4 3 5 4 4 | grade: C1 C2 K1 K2 K3 K4 K5 K6 K7 K8 O1 O2 | claimed: PASS
Blank lines and lines starting with # are skipped.

Rules (all mechanical):
  length    the hook fits in --max-chars characters (default 130, the feed cut before "Show more").
  dashes    no em or en dash.
  gate      every answer is Y. Default verdict is KILL until all are Y.
  score     five scores 1 to 5. PASS when every score is 3 or more, the first is 4 or more, and the average is 4.0 or more.
  grade     twelve scores 0 to 10: context and curiosity count double. Weighted average =
            (2*C1 + 2*C2 + sum of the other ten) / 14. If C1 or C2 is 3 or less, the result is capped at 5.0.
            PASS at 7.0 or more.
  claimed   if a verdict is written on the line, it must match the arithmetic.
Exit: 0 every hook passes, 1 any hook fails, 2 usage error.
"""
import re
import sys
import tempfile
from pathlib import Path


def nums(s):
    return [float(x) for x in re.findall(r"\d+(?:\.\d+)?", s)]


def score_bar(vals):
    if len(vals) != 5 or any(v < 1 or v > 5 for v in vals):
        return None, "score needs five numbers from 1 to 5"
    avg = sum(vals) / 5
    ok = min(vals) >= 3 and vals[0] >= 4 and avg >= 4.0
    return ok, f"score avg {avg:.1f}, min {min(vals):g}, first {vals[0]:g}"


def grade(vals):
    if len(vals) != 12 or any(v < 0 or v > 10 for v in vals):
        return None, "grade needs twelve numbers from 0 to 10"
    total = (2 * vals[0] + 2 * vals[1] + sum(vals[2:])) / 14
    if vals[0] <= 3 or vals[1] <= 3:
        total = min(total, 5.0)
    return total >= 7.0, f"grade {total:.1f}/10"


def check_line(line, max_chars):
    parts = [p.strip() for p in line.split(" | ")]
    text = parts[0]
    fails, notes = [], []
    if len(text) > max_chars:
        fails.append(f"{len(text)} chars, over {max_chars}")
    if re.search("[\u2014\u2013]", text):
        fails.append("em or en dash")
    verdict_ok = True
    claimed = None
    for p in parts[1:]:
        key, _, val = p.partition(":")
        key = key.strip().lower()
        if key == "gate":
            answers = val.split()
            if not answers or any(a.upper() not in ("Y", "N") for a in answers):
                return None, ["gate answers must be Y or N"]
            if any(a.upper() == "N" for a in answers):
                fails.append("gate: KILL (a test failed)")
        elif key == "score":
            ok, msg = score_bar(nums(val))
            if ok is None:
                return None, [msg]
            notes.append(msg)
            if not ok:
                fails.append("score below bar")
        elif key == "grade":
            ok, msg = grade(nums(val))
            if ok is None:
                return None, [msg]
            notes.append(msg)
            if not ok:
                fails.append("grade below 7.0")
        elif key == "claimed":
            claimed = val.strip().upper()
    computed = "FAIL" if fails else "PASS"
    if claimed and claimed not in (computed, "KILL" if computed == "FAIL" else "SHIP"):
        fails.append(f"claimed {claimed} but the arithmetic says {computed}")
    return (not fails), fails + notes


def run(path, max_chars):
    lines = [l.rstrip("\n") for l in Path(path).read_text(encoding="utf-8").splitlines()]
    lines = [l for l in lines if l.strip() and not l.startswith("#")]
    if not lines:
        print("no hooks found")
        return 2
    bad = 0
    for i, l in enumerate(lines, 1):
        ok, info = check_line(l, max_chars)
        if ok is None:
            print(f"USAGE line {i}: {info[0]}")
            return 2
        bad += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {i}. {l.split(' | ')[0][:70]}  " + "; ".join(info))
    print(f"\n{len(lines)} hooks, {bad} failing")
    return 1 if bad else 0


def selftest():
    good = "You lost the meeting notes again. | gate: Y Y Y Y Y Y Y Y | score: 4 4 4 5 4 | claimed: PASS"
    assert check_line(good, 130)[0] is True
    assert check_line("x | score: 3 5 5 5 5", 130)[0] is False      # first question under 4
    assert check_line("x | score: 4 4 4 4 3", 130)[0] is False      # average 3.8
    assert check_line("x | gate: Y N Y", 130)[0] is False
    assert check_line("a" * 140, 130)[0] is False
    assert check_line("x | grade: 3 10 10 10 10 10 10 10 10 10 10 10", 130)[0] is False  # cap at 5.0
    assert check_line("x | grade: 8 8 7 7 7 7 7 7 7 7 7 7", 130)[0] is True
    assert check_line("x | score: 3 3 3 3 3 | claimed: PASS", 130)[0] is False      # wrong claim
    with tempfile.TemporaryDirectory() as d:
        p = Path(d, "h.txt")
        p.write_text(good + "\n")
        assert run(p, 130) == 0
        p.write_text("x | score: 9 9\n")
        assert run(p, 130) == 2
    print("SELFTEST PASS")
    return 0


def main(argv):
    if argv[1:2] == ["--selftest"]:
        return selftest()
    if len(argv) < 2 or not Path(argv[1]).is_file():
        print(__doc__)
        return 2
    mc = 130
    if "--max-chars" in argv:
        try:
            mc = int(argv[argv.index("--max-chars") + 1])
        except (IndexError, ValueError):
            print("--max-chars needs a number")
            return 2
    return run(argv[1], mc)


if __name__ == "__main__":
    sys.exit(main(sys.argv))

# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
