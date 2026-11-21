#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""Leak scan (allowlist: the fictional test handles @example and @alexsample_99, and addresses at example.com or example.org): no private paths, handles, money amounts, emails or named outside creators in a template.

Usage:
  python3 check_leak.py <file or folder> [--terms FILE] [--exempt NAME ...]
  python3 check_leak.py --selftest

--terms FILE adds the owner's own private words, one per line: company, product, people,
and any outside creator, course or source the owner does not want named.
Run it on every draft before you show it, and on the pack before you share it.
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


PATTERNS = [
    ("private path", r"/h[o]me/|/w[o]rkspace|~[/]"),
    ("handle", r"(?<![\w.])@[a-z0-9_]{3,}"),
    ("money amount", r"\x24[0-9]"),
    ("email address", r"[\w.+-]+@[\w-]+\.[a-z]{2,}"),
]
COMPILED = [(n, re.compile(p, re.I)) for n, p in PATTERNS]
# Fictional test data used in examples and self-tests; never a real account.
ALLOW_RX = re.compile(r"(?<![\w.])@(example|alexsample_99)\b|[\w.+-]+@example\.(com|org)\b", re.I)


def scan_text(text, extra):
    hits = []
    for n, line in enumerate(text.splitlines(), 1):
        clean = ALLOW_RX.sub("", line)
        for name, rx in COMPILED:
            if rx.search(clean):
                hits.append(f"line {n}: {name}: {line.strip()[:90]}")
        low = line.lower()
        for t in extra:
            if t and t in low:
                hits.append(f"line {n}: owner private term '{t}'")
    return hits


def run(target, extra, exempt):
    t = Path(target)
    files = [t] if t.is_file() else sorted(p for p in t.rglob("*") if p.is_file() and p.suffix in (".md", ".py", ".txt", ".json", ".csv"))
    total = 0
    for p in files:
        if p.name in exempt or _locked(p):
            print(f"SKIP  {p.name} (exempt)")
            continue
        hits = scan_text(p.read_text(encoding="utf-8"), extra)
        total += len(hits)
        if hits:
            print(f"FAIL  {p.name}")
            for h in hits:
                print("      " + h)
    print(f"{len(files)} files scanned, {total} hits")
    return 1 if total else 0


def selftest():
    assert not scan_text("Use {FOUNDER_HANDLE} and {PRICE}.", [])
    assert scan_text("ping " + "@" + "someone", [])
    assert scan_text("costs " + chr(36) + "49", [])
    assert scan_text("saved in " + "/h" + "ome/user", [])
    assert scan_text("acme corp", ["acme"])
    with tempfile.TemporaryDirectory() as d:
        Path(d, "ok.md").write_text("Placeholders only: {COMPANY}.\n")
        assert run(d, [], set()) == 0
        Path(d, "bad.md").write_text("Write to " + "x" + "@" + "y.com\n")
        assert run(d, [], set()) == 1
    print("SELFTEST PASS")
    return 0


def main(argv):
    if argv[1:2] == ["--selftest"]:
        return selftest()
    if len(argv) < 2 or not Path(argv[1]).exists():
        print(__doc__)
        return 2
    args = argv[2:]
    extra, exempt = [], set()
    if "--terms" in args:
        i = args.index("--terms")
        if i + 1 >= len(args) or not Path(args[i + 1]).is_file():
            print("--terms needs a readable file")
            return 2
        extra = [l.strip().lower() for l in Path(args[i + 1]).read_text().splitlines() if l.strip()]
    if "--exempt" in args:
        exempt = set(a for a in args[args.index("--exempt") + 1:] if not a.startswith("--"))
    return run(argv[1], extra, exempt)


if __name__ == "__main__":
    sys.exit(main(sys.argv))

# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
