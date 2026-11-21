#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""Brand truth minimum bar: is the brand pack strong enough to write ads from?

Usage:
  python3 check_brand_pack.py <BRAND-PACK.md>
  python3 check_brand_pack.py --selftest

The pack is one markdown file with these level-2 sections (see references/templates.md):
  Offer, Never claims, Customer phrases, Avatars, Competitors, Voice, Thin spots
Hard bar (fail = exit 1):
  1. Offer holds a real offer line or the words "no offer".
  2. Never claims has 3 or more bullets.
  3. Customer phrases has 10 or more bullets, each with "source:" on the same line.
Soft checks (WARN, no fail): Avatars has 3 to 5 bullets, Competitors has 3 or more, Voice has
"Words we use" and "Words we never use".
Lines with [NEED], TBD or TODO never count.
Exit: 0 pass, 1 below the bar, 2 usage error or file missing.
"""
import re
import sys
import tempfile
from pathlib import Path

OPEN = re.compile(r"\[NEED|\bTBD\b|\bTODO\b", re.I)


def sections(text):
    out, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            cur = m.group(1).strip().lower()
            out[cur] = []
        elif cur is not None:
            out[cur].append(line)
    return out


def bullets(lines):
    return [l for l in lines if re.match(r"^\s*[-*]\s+\S", l) and not OPEN.search(l)]


def check(text):
    s = sections(text)
    fails, warns = [], []
    offer = [l for l in s.get("offer", []) if l.strip() and not OPEN.search(l)]
    if not offer:
        fails.append("Offer: state the real offer and price rule, or write 'no offer' (scripts invent offers otherwise)")
    never = bullets(s.get("never claims", []))
    if len(never) < 3:
        fails.append(f"Never claims: {len(never)} of 3 (rewrites copy promises your product may not keep)")
    phrases = bullets(s.get("customer phrases", []))
    sourced = [p for p in phrases if re.search(r"source:\s*\S", p, re.I)]
    if len(sourced) < 10:
        fails.append(f"Customer phrases: {len(sourced)} sourced of 10 (hooks turn into generic ad-speak)")
    av = len(bullets(s.get("avatars", [])))
    if not 3 <= av <= 5:
        warns.append(f"Avatars: {av} (aim for 3 to 5)")
    if len(bullets(s.get("competitors", []))) < 3:
        warns.append("Competitors: fewer than 3 (nobody knows which angles are worn out)")
    voice = "\n".join(s.get("voice", [])).lower()
    if "words we use" not in voice or "words we never use" not in voice:
        warns.append("Voice: add 'Words we use' and 'Words we never use'")
    return fails, warns


def run(path):
    fails, warns = check(Path(path).read_text(encoding="utf-8"))
    for f in fails:
        print("FAIL  " + f)
    for w in warns:
        print("WARN  " + w)
    print("PASS  brand pack meets the minimum bar" if not fails else "\nBelow the bar. Fill these before any script.")
    return 1 if fails else 0


def selftest():
    full = ["## Offer", "Example offer: founding member plan at {PRICE}, {PRICE_RULE}", "## Never claims",
            "- cures anything", "- guaranteed results", "- used by a named brand", "## Customer phrases"]
    full += [f"- \"example phrase {i}\" source: example review {i}" for i in range(10)]
    full += ["## Avatars", "- a", "- b", "- c", "## Competitors", "- x", "- y", "- z",
             "## Voice", "Words we use: plain", "Words we never use: hype"]
    assert check("\n".join(full)) == ([], [])
    thin = "\n".join(full).replace("source: example review 3", "")
    assert check(thin)[0]
    assert check("## Offer\n[NEED]\n")[0]
    with tempfile.TemporaryDirectory() as d:
        p = Path(d, "b.md")
        p.write_text("\n".join(full))
        assert run(p) == 0
    print("SELFTEST PASS")
    return 0


def main(argv):
    if argv[1:2] == ["--selftest"]:
        return selftest()
    if len(argv) != 2 or not Path(argv[1]).is_file():
        print(__doc__)
        return 2
    return run(argv[1])


if __name__ == "__main__":
    sys.exit(main(sys.argv))

# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
