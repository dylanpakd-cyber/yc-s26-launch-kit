#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""T-12h launch check: the eight GO / NO-GO gates, computed, not guessed.

Usage:
  python3 check_gates.py <gates file>
  python3 check_gates.py --selftest

Gates file: one line per gate, G1 to G8, then a status and evidence:
  G1: PASS | destination loads on a phone, offer matches the post | evidence: owner checked at {TIME}
  G2: RISK | KPI counter works on desktop only | owner: {LAUNCH_OWNER} | accepted: yes
  G3: FAIL | post not frozen | owner: {LAUNCH_OWNER} | deadline: T-6h
Optional last line: "Verdict: GO" (or GO WITH RISKS, NO-GO). If present it must match the arithmetic.

Gates: G1 destination and offer match, G2 tracking and KPI count, G3 post frozen after the harsh read,
G4 people plan logged (lineup log, or the no-network plan), G5 every quote or note draft approved by the owner,
G6 quiet window agreed, G7 replies owner and backup named, G8 rollback plan written.

Rules:
  every gate G1 to G8 appears once with PASS, RISK or FAIL.
  PASS needs an "evidence:" part. RISK needs "accepted: yes" from the owner, else it counts as FAIL.
  FAIL needs "owner:" and "deadline:" so the blocker has a name and a time.
  Verdict: any FAIL is NO-GO; else any RISK is GO WITH RISKS; else GO.
Exit: 0 GO or GO WITH RISKS, 1 NO-GO or a malformed gate, 2 usage error.
"""
import re
import sys
import tempfile
from pathlib import Path


def evaluate(text):
    gates, problems, declared = {}, [], None
    for line in text.splitlines():
        m = re.match(r"^\s*G([1-8])\s*:\s*(PASS|RISK|FAIL)\b(.*)$", line.strip(), re.I)
        if m:
            n = int(m.group(1))
            if n in gates:
                problems.append(f"G{n} listed twice")
            gates[n] = (m.group(2).upper(), m.group(3).lower())
        v = re.match(r"^\s*verdict\s*:\s*(GO WITH RISKS|NO-GO|GO)\b", line.strip(), re.I)
        if v:
            declared = v.group(1).upper()
    status = {}
    for n in range(1, 9):
        if n not in gates:
            problems.append(f"G{n} missing")
            status[n] = "FAIL"
            continue
        s, rest = gates[n]
        if s == "PASS" and "evidence:" not in rest:
            problems.append(f"G{n} PASS has no evidence")
            s = "FAIL"
        if s == "RISK" and not re.search(r"accepted:\s*yes", rest):
            problems.append(f"G{n} RISK not accepted by the owner, counted as FAIL")
            s = "FAIL"
        if gates[n][0] == "FAIL" and not ("owner:" in rest and "deadline:" in rest):
            problems.append(f"G{n} FAIL needs owner: and deadline:")
        status[n] = s
    vals = status.values()
    verdict = "NO-GO" if "FAIL" in vals else ("GO WITH RISKS" if "RISK" in vals else "GO")
    if declared and declared != verdict:
        problems.append(f"declared verdict {declared} but the gates say {verdict}")
    return verdict, status, problems


def run(path):
    verdict, status, problems = evaluate(Path(path).read_text(encoding="utf-8"))
    for n in range(1, 9):
        print(f"G{n}: {status[n]}")
    for p in problems:
        print("PROBLEM  " + p)
    print(f"\nVERDICT: {verdict}")
    return 0 if verdict != "NO-GO" and not problems else 1


def selftest():
    good = "\n".join(f"G{i}: PASS | ok | evidence: example check" for i in range(1, 9))
    assert evaluate(good)[0] == "GO" and not evaluate(good)[2]
    risky = good.replace("G2: PASS | ok | evidence: example check", "G2: RISK | desktop only | accepted: yes")
    assert evaluate(risky)[0] == "GO WITH RISKS"
    unacc = good.replace("G2: PASS | ok | evidence: example check", "G2: RISK | desktop only")
    assert evaluate(unacc)[0] == "NO-GO"
    missing = "\n".join(good.splitlines()[:7])
    assert evaluate(missing)[0] == "NO-GO"
    lie = good + "\nVerdict: NO-GO"
    assert evaluate(lie)[2]
    with tempfile.TemporaryDirectory() as d:
        p = Path(d, "g.md")
        p.write_text(good)
        assert run(p) == 0
        p.write_text(unacc)
        assert run(p) == 1
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
