#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""Check that every SKILL-*.md in a pack has the required sections and a body of 600 to 1,800 words.

Usage:
  python3 check_sections.py <pack folder> [--exempt NAME ...]
  python3 check_sections.py --selftest

Required headings (level 2, in any order): Use when, Inputs, Steps, Gate, Output, If things go wrong, Never.
The body count leaves out the credit header and footer and fenced code blocks still count.
Exit: 0 pass, 1 fail, 2 usage error.
Files named in LOCKED (byte-locked owner files) are skipped automatically and reported.
"""
import re
import sys
import tempfile
from pathlib import Path

LOCKED = {"SKILL-test-of-300.md"}  # byte-locked owner files, skipped automatically and reported


def _label(p):
    return p.parent.name if p.name == "SKILL.md" else p.name


def _locked(p):
    """Byte-locked owner file: SKILL-test-of-300.md in a pack, or the test-of-300 skill folder in the repo."""
    return p.name in LOCKED or "test-of-300" in p.as_posix()


# Repo layout: support skills (workflow, getting-started, knowledge, checks, references) are not step skills.
SUPPORT = ("-workflow", "-getting-started", "-knowledge", "-checks", "-references")
REQUIRED = ["use when", "inputs", "steps", "gate", "output", "if things go wrong", "never"]
LOW, HIGH = 600, 1800


def body_words(text):
    lines = [l for l in text.splitlines() if not l.startswith("<!-- dylan-pak-credit")
             and not l.startswith("Created and curated by Dylan Pak") and not l.startswith("License note: free to use")]
    return len(re.findall(r"[A-Za-z0-9{}_'/-]+", "\n".join(lines)))


def check_file(path):
    text = path.read_text(encoding="utf-8")
    heads = [h.strip().lower() for h in re.findall(r"^##\s+(.+)$", text, flags=re.M)]
    missing = [r for r in REQUIRED if not any(h.startswith(r) for h in heads)]
    n = body_words(text)
    out = []
    if missing:
        out.append("missing sections: " + ", ".join(missing))
    if not LOW <= n <= HIGH:
        out.append(f"body is {n} words (want {LOW} to {HIGH})")
    return out, n


def run(folder, exempt):
    files = sorted(Path(folder).glob("SKILL-*.md")) + sorted(p for p in Path(folder).rglob("SKILL.md") if not p.parent.name.endswith(SUPPORT))
    if not files:
        print("no SKILL-*.md or */SKILL.md files found")
        return 1
    fails = 0
    for p in files:
        if p.name in exempt or _locked(p):
            print(f"SKIP  {_label(p)} (exempt)")
            continue
        bad, n = check_file(p)
        fails += bool(bad)
        print(f"{'FAIL' if bad else 'PASS'}  {_label(p)} ({n} words)" + ("" if not bad else ": " + "; ".join(bad)))
    return 1 if fails else 0


def selftest():
    body = "\n".join(f"## {h.title()}\n" + "word " * 100 for h in REQUIRED)
    with tempfile.TemporaryDirectory() as d:
        Path(d, "SKILL-a.md").write_text("# SKILL: a\n" + body)
        assert run(d, set()) == 0
        Path(d, "SKILL-b.md").write_text("# SKILL: b\n## Steps\nshort\n")
        assert run(d, set()) == 1
        assert run(d, {"SKILL-b.md"}) == 0
    print("SELFTEST PASS")
    return 0


def main(argv):
    if argv[1:2] == ["--selftest"]:
        return selftest()
    if len(argv) < 2 or not Path(argv[1]).is_dir():
        print(__doc__)
        return 2
    exempt = set(argv[argv.index("--exempt") + 1:]) if "--exempt" in argv else set()
    return run(Path(argv[1]), exempt)


if __name__ == "__main__":
    sys.exit(main(sys.argv))

# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
