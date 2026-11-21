#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""Check that every .md, .py and .txt file in a folder carries the credit header and footer.

Usage:
  python3 check_credit.py <folder> [--exempt NAME ...]
  python3 check_credit.py --selftest

Rules:
  .md  first line is the exact credit comment; the last two non-empty lines are the credit and license note.
  .py  the credit comment sits on line 1, or line 2 after a shebang, prefixed with "# ";
       the last two non-empty lines are the credit and license note prefixed with "# ".
  .txt same as .py ("# " comment lines), so hook and script checks skip them.
Files named in LOCKED (byte-locked owner files) are skipped automatically and reported.
Exit: 0 pass, 1 fail, 2 usage error.
"""
import sys
import tempfile
from pathlib import Path

HEADER = ('<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file '
          '(including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->')
LOCKED = {"SKILL-test-of-300.md"}


def _locked(p):
    """Byte-locked owner file: SKILL-test-of-300.md in a pack, or the test-of-300 skill folder in the repo."""
    return p.name in LOCKED or "test-of-300" in p.as_posix()

FOOT1 = "Created and curated by Dylan Pak."
FOOT2 = ('License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), '
         'keep the credit "Created and curated by Dylan Pak."')


def _strip_frontmatter(lines):
    """SKILL.md files open with YAML frontmatter (---, name, description, ---); the credit header follows it."""
    if lines and lines[0].strip() == "---" and "---" in [l.strip() for l in lines[1:]]:
        k = [l.strip() for l in lines[1:]].index("---") + 2
        lines = lines[k:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    return lines


def problems(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    tail = [l for l in lines if l.strip()][-2:]
    out = []
    if path.suffix == ".md":
        lines = _strip_frontmatter(lines)
        if not lines or lines[0] != HEADER:
            out.append("first line is not the exact credit header")
        if tail != [FOOT1, FOOT2]:
            out.append("does not end with the credit and license note")
    elif path.suffix in (".py", ".txt"):
        head = lines[1] if lines and lines[0].startswith("#!") else (lines[0] if lines else "")
        if head != "# " + HEADER:
            out.append("credit header comment missing (line 1, or line 2 after a shebang)")
        if tail != ["# " + FOOT1, "# " + FOOT2]:
            out.append("does not end with the credit and license note comments")
    return out


def run(folder, exempt):
    files = sorted(p for p in Path(folder).rglob("*") if p.suffix in (".md", ".py", ".txt") and p.is_file())
    fails = 0
    for p in files:
        if p.name in exempt or _locked(p):
            print(f"SKIP  {p.relative_to(folder)} (locked or exempt)")
            continue
        bad = problems(p)
        if bad:
            fails += 1
            print(f"FAIL  {p.relative_to(folder)}: " + "; ".join(bad))
        else:
            print(f"PASS  {p.relative_to(folder)}")
    print(f"\n{len(files)} files, {fails} failing")
    return 1 if fails else 0


def selftest():
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        (d / "good.md").write_text(HEADER + "\n# Title\nbody\n\n---\n" + FOOT1 + "\n" + FOOT2 + "\n")
        (d / "good.py").write_text("#!/usr/bin/env python3\n# " + HEADER + "\nx = 1\n# " + FOOT1 + "\n# " + FOOT2 + "\n")
        (d / "locked.md").write_text("anything\n")
        (d / "good.txt").write_text("# " + HEADER + "\nhook line\n# " + FOOT1 + "\n# " + FOOT2 + "\n")
        (d / "SKILL-test-of-300.md").write_text("locked owner file\n")
        assert run(d, {"locked.md"}) == 0, "good files should pass"
        (d / "bad.txt").write_text("hook without credit\n")
        assert run(d, {"locked.md"}) == 1, "txt without credit should fail"
        (d / "bad.txt").unlink()
        (d / "bad.md").write_text("# Title\nno credit\n")
        assert run(d, {"locked.md"}) == 1, "missing credit should fail"
    print("SELFTEST PASS")
    return 0


def main(argv):
    if argv[1:2] == ["--selftest"]:
        return selftest()
    if len(argv) < 2 or not Path(argv[1]).is_dir():
        print(__doc__)
        return 2
    exempt = set()
    if "--exempt" in argv:
        exempt = set(argv[argv.index("--exempt") + 1:])
    return run(Path(argv[1]), exempt)


if __name__ == "__main__":
    sys.exit(main(sys.argv))

# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
