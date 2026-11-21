#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""Style lint for drafts and pack files: no em or en dashes, no machine-sounding words, no "not just X, it is Y".

Usage:
  python3 check_style.py <file or folder> [--banned FILE] [--exempt NAME ...]
  python3 check_style.py --selftest

--banned FILE adds the owner's banned words (one per line, # comments allowed).
Lines that start with "Banned words:" (after an optional "1." or "-" list marker) are skipped, so a skill can list the words it bans.
Long sentences (over 30 words) print as WARN and do not fail.
Exit: 0 pass, 1 fail, 2 usage error.
Files named in LOCKED (byte-locked owner files) are skipped automatically and reported.
"""
import re
import sys
import tempfile
from pathlib import Path

LOCKED = {"SKILL-test-of-300.md"}  # byte-locked owner files, skipped automatically and reported


def _locked(p):
    """Byte-locked owner file: SKILL-test-of-300.md in a pack, or the test-of-300 skill folder in the repo."""
    return p.name in LOCKED or "test-of-300" in p.as_posix()


DASHES = re.compile("[\u2014\u2013]")
BANNED = ["leverage", "seamless", "seamlessly", "robust", "elevate", "unlock", "unlocks", "delve", "game-changer",
          "game changer", "revolutionary", "empower", "supercharge", "unleash", "cutting-edge", "next level",
          "in today's world", "in today's fast-paced", "look no further", "say goodbye to", "transform your",
          "we're excited to announce", "we are excited to announce"]
NOT_JUST = re.compile(r"\b(it'?s|is|isn'?t|was) not just\b[^.]{0,60}\b(it'?s|it is)\b", re.I)


def lint_text(text, extra):
    words = BANNED + extra
    fails, warns = [], []
    in_code = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            in_code = not in_code
        if re.sub(r"^(\d+\.|-)\s*", "", line.strip()).lower().startswith("banned words:"):
            continue
        if DASHES.search(line):
            fails.append(f"line {n}: em or en dash")
        low = line.lower()
        for w in words:
            if re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", low):
                fails.append(f"line {n}: banned word '{w}'")
        if NOT_JUST.search(line):
            fails.append(f"line {n}: 'not just X, it is Y' pattern")
        if not in_code and not line.lstrip().startswith(("|", "#")):
            for s in re.split(r"(?<=[.!?])\s+", line):
                if len(s.split()) > 30:
                    warns.append(f"line {n}: sentence over 30 words")
    return fails, warns


def load_extra(path):
    if not path:
        return []
    return [l.strip().lower() for l in Path(path).read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.startswith("#")]


def run(target, extra, exempt):
    t = Path(target)
    files = [t] if t.is_file() else sorted(p for p in t.rglob("*.md") if p.is_file())
    total = 0
    for p in files:
        if p.name in exempt or _locked(p):
            print(f"SKIP  {p.name} (exempt)")
            continue
        fails, warns = lint_text(p.read_text(encoding="utf-8"), extra)
        total += len(fails)
        print(f"{'FAIL' if fails else 'PASS'}  {p.name}" + (f" ({len(warns)} warn)" if warns else ""))
        for f in fails:
            print("      " + f)
    print(f"\n{len(files)} files, {total} failures")
    return 1 if total else 0


def selftest():
    f, _ = lint_text("Short line. Plain words.", [])
    assert not f
    f, _ = lint_text("This will unlock growth \u2014 fast.", [])
    assert len(f) == 2, f
    f, _ = lint_text("Banned words: leverage, seamless", [])
    assert not f
    f, _ = lint_text("It is not just a tool, it is a habit.", [])
    assert f
    f, _ = lint_text("We ship synergy.", ["synergy"])
    assert f
    with tempfile.TemporaryDirectory() as d:
        Path(d, "a.md").write_text("Fine text.\n")
        assert run(d, [], set()) == 0
        Path(d, "b.md").write_text("A seamless flow.\n")
        assert run(d, [], set()) == 1
    print("SELFTEST PASS")
    return 0


def main(argv):
    if argv[1:2] == ["--selftest"]:
        return selftest()
    if len(argv) < 2 or not Path(argv[1]).exists():
        print(__doc__)
        return 2
    banned = None
    exempt = set()
    args = argv[2:]
    if "--banned" in args:
        i = args.index("--banned")
        if i + 1 >= len(args) or not Path(args[i + 1]).is_file():
            print("--banned needs a readable file")
            return 2
        banned = args[i + 1]
    if "--exempt" in args:
        exempt = set(a for a in args[args.index("--exempt") + 1:] if not a.startswith("--"))
    return run(argv[1], load_extra(banned), exempt)


if __name__ == "__main__":
    sys.exit(main(sys.argv))

# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
