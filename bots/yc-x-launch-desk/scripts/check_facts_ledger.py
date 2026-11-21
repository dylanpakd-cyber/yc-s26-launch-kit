#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""Claim-has-proof check: every number, percent, money figure and date in a draft must be in the facts ledger,
and every ledger row must carry a source.

Usage:
  python3 check_facts_ledger.py <draft file> <ledger file>
  python3 check_facts_ledger.py --ledger-only <ledger file>
  python3 check_facts_ledger.py --selftest

Ledger format: one fact per line, "- <fact> | source: <where it came from>".
A row marked [NEED] has no proof yet. Any draft token that only matches a [NEED] row fails.
Draft tokens in {BRACES} are placeholders and are ignored. A draft line holding [NEED] fails, because it is not ready.
Exit: 0 pass, 1 fail, 2 usage error.
"""
import re
import sys
import tempfile
from pathlib import Path

TOKEN = re.compile(r"(?<![\w{])[^\s\w{]?\d[\d,.:/]*\s?(?:%|x\b|k\b|m\b|percent\b)?", re.I)


def tokens(text):
    clean = re.sub(r"\{[A-Z0-9_]+\}", " ", text)
    out = []
    for m in TOKEN.finditer(clean):
        t = m.group(0).strip().rstrip(".,:")
        if re.search(r"\d", t):
            out.append(t.lower().replace(" ", ""))
    return out


def load_ledger(path):
    good, need, bad_rows = set(), set(), []
    for n, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        s = line.strip()
        if not s.startswith("- "):
            continue
        has_source = re.search(r"source:\s*\S", s, re.I) is not None
        is_need = "[NEED" in s.upper()
        if not has_source and not is_need:
            bad_rows.append(f"ledger line {n}: no source and not marked [NEED]")
        target = need if (is_need or not has_source) else good
        for t in tokens(s.split("|")[0]):
            target.add(t)
    return good, need, bad_rows


def run(draft, ledger):
    good, need, bad_rows = load_ledger(ledger)
    fails = list(bad_rows)
    if draft:
        for n, line in enumerate(Path(draft).read_text(encoding="utf-8").splitlines(), 1):
            if "[NEED" in line.upper():
                fails.append(f"draft line {n}: open [NEED] mark")
            for t in tokens(line):
                if t in good:
                    continue
                why = "only a [NEED] row backs it" if t in need else "not in the ledger"
                fails.append(f"draft line {n}: '{t}' {why}")
    for f in fails:
        print("FAIL  " + f)
    print("PASS  every number traces to a sourced ledger row" if not fails else f"\n{len(fails)} problems")
    return 1 if fails else 0


def selftest():
    with tempfile.TemporaryDirectory() as d:
        led = Path(d, "ledger.md")
        led.write_text("- 412 people joined the waitlist | source: signup export, {DATE}\n- 30% open rate [NEED]\n")
        dr = Path(d, "draft.md")
        dr.write_text("412 people joined. Price is {PRICE}.\n")
        assert run(dr, led) == 0
        dr.write_text("412 people joined and 30% opened.\n")
        assert run(dr, led) == 1
        dr.write_text("We grew 3x.\n")
        assert run(dr, led) == 1
        led.write_text("- 10 beta users\n")
        assert run(None, led) == 1
        led.write_text("- 10 beta users | source: example\n\n---\nfooter\n")
        assert run(None, led) == 0
        led.write_text("- 10 beta users\n")
        assert run(None, led) == 1
    print("SELFTEST PASS")
    return 0


def main(argv):
    if argv[1:2] == ["--selftest"]:
        return selftest()
    if argv[1:2] == ["--ledger-only"] and len(argv) == 3 and Path(argv[2]).is_file():
        return run(None, argv[2])
    if len(argv) != 3 or not Path(argv[1]).is_file() or not Path(argv[2]).is_file():
        print(__doc__)
        return 2
    return run(argv[1], argv[2])


if __name__ == "__main__":
    sys.exit(main(sys.argv))

# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
