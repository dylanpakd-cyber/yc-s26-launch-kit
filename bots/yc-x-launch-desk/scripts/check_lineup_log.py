#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""Lineup log check: every account was checked, scored in range, and every draft is distinct and unsent by the desk.

Usage:
  python3 check_lineup_log.py <lineup log .md>
  python3 check_lineup_log.py --selftest

The log is a markdown table with this header (see references/templates.md):
| Account | Fit | Reach | Relationship | Last ten checked | Check result | Decision | Draft | Status |

Rules:
  Fit and Reach are whole numbers 0 to 3.
  Relationship is one of: cold, seen, replied, friend.
  Last ten checked is filled (a date placeholder or date) for every row.
  Check result is pass or fail. A fail row must have Decision skip or watch.
  Decision is one of: core, bench, skip, watch.
  Status is one of: drafted, approved by owner, creator wrote own, sent by owner, replied, skipped.
  No two Draft cells are the same text (identical quotes read as a scripted wave).
  Row count for core plus bench is reported. Under 30 prints a WARN, not a fail (use the no-network path).
Exit: 0 pass, 1 fail, 2 usage error.
"""
import re
import sys
import tempfile
from pathlib import Path

HEAD = ["account", "fit", "reach", "relationship", "last ten checked", "check result", "decision", "draft", "status"]
REL = {"cold", "seen", "replied", "friend"}
DEC = {"core", "bench", "skip", "watch"}
STATUS = {"drafted", "approved by owner", "creator wrote own", "sent by owner", "replied", "skipped"}


def rows(text):
    table = [l for l in text.splitlines() if l.strip().startswith("|")]
    if len(table) < 2:
        return None, []
    head = [c.strip().lower() for c in table[0].strip().strip("|").split("|")]
    body = []
    for l in table[1:]:
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", c) for c in cells):
            continue
        body.append(dict(zip(head, cells)))
    return head, body


def check(text):
    head, body = rows(text)
    if head is None or head != HEAD:
        return ["table header must be: | " + " | ".join(h.title() for h in HEAD) + " |"], [], 0
    fails, warns, seen = [], [], {}
    for i, r in enumerate(body, 1):
        tag = f"row {i} ({r.get('account', '?')})"
        for k in ("fit", "reach"):
            if not re.fullmatch(r"[0-3]", r.get(k, "")):
                fails.append(f"{tag}: {k} must be 0 to 3")
        if r.get("relationship", "").lower() not in REL:
            fails.append(f"{tag}: relationship must be one of {sorted(REL)}")
        if not r.get("last ten checked"):
            fails.append(f"{tag}: last ten posts not checked")
        cr = r.get("check result", "").lower()
        dec = r.get("decision", "").lower()
        if cr not in ("pass", "fail"):
            fails.append(f"{tag}: check result must be pass or fail")
        if dec not in DEC:
            fails.append(f"{tag}: decision must be one of {sorted(DEC)}")
        if cr == "fail" and dec in ("core", "bench"):
            fails.append(f"{tag}: failed the check but is in the lineup")
        st = r.get("status", "").lower()
        if st not in STATUS:
            fails.append(f"{tag}: status must be one of {sorted(STATUS)}")
        d = re.sub(r"\W+", " ", r.get("draft", "").lower()).strip()
        if d and d not in ("n a", "none"):
            if d in seen:
                fails.append(f"{tag}: draft is identical to row {seen[d]}")
            seen.setdefault(d, i)
    n = sum(1 for r in body if r.get("decision", "").lower() in ("core", "bench"))
    if n < 30:
        warns.append(f"lineup has {n} core plus bench accounts (plan says 30 to 60; under 10 means use the no-network path)")
    return fails, warns, n


def run(path):
    fails, warns, n = check(Path(path).read_text(encoding="utf-8"))
    for f in fails:
        print("FAIL  " + f)
    for w in warns:
        print("WARN  " + w)
    print(f"PASS  lineup log clean ({n} in lineup)" if not fails else f"\n{len(fails)} problems")
    return 1 if fails else 0


def selftest():
    h = "| Account | Fit | Reach | Relationship | Last ten checked | Check result | Decision | Draft | Status |\n|---|---|---|---|---|---|---|---|---|\n"
    ok = h + "| {ACCOUNT_1} | 3 | 1 | replied | {DATE} | pass | core | example take one | drafted |\n" \
             "| {ACCOUNT_2} | 2 | 2 | seen | {DATE} | fail | skip | n/a | skipped |\n"
    assert not check(ok)[0]
    dup = ok + "| {ACCOUNT_3} | 2 | 2 | seen | {DATE} | pass | bench | Example take one. | drafted |\n"
    assert check(dup)[0]
    bad = h + "| {ACCOUNT_4} | 5 | 1 | stranger | | fail | core | x | sent by desk |\n"
    assert len(check(bad)[0]) >= 4
    assert check("no table")[0]
    with tempfile.TemporaryDirectory() as d:
        p = Path(d, "l.md")
        p.write_text(ok)
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
