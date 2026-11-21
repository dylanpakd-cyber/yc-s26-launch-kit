#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""check_quote_bank.py: validate the graded quote bank (markdown table).

Columns (any order, case ignored):
  ID | Quote | Verbatim | Source type | Source ref | Date | Speakers | Label | Tier | Theme | Use | Consent

Rules:
  1. every column present; IDs unique; no blank cells (use "n/a" or "unknown")
  2. Verbatim is yes or no; Label is stated, observed or claimed
  3. Source ref is filled and not [NEED]; Speakers is a whole number of 1 or more
  4. Tier is A, B or C and never higher than the evidence allows:
       A needs Verbatim yes and Speakers >= 3
       B needs Speakers >= 2
       C is everything else (single mention, inferred, or a claim)
     A "claimed" row is at most C (a claim is not evidence of itself)
     A row whose Source type is "friend" (friends, family, the owner's own circle) is at most B,
     so a theme backed only by friends can never reach Tier A
  Note: Speakers is self-reported by whoever builds the bank. The script cannot verify it.
  The hand-off must keep the source refs so a person can recount.
  5. Use is internal, copy or public. Tier C may only be internal.
     public needs Consent "written" (a permission on file); copy needs Tier A or B
  6. Quote text has no personal identifiers (same scan as check_redaction.py)
Usage: python3 check_quote_bank.py BANK.md
       python3 check_quote_bank.py --selftest
Exit: 0 pass, 1 fail, 2 usage error.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_redaction import scan  # noqa: E402

COLS = ['id', 'quote', 'verbatim', 'source type', 'source ref', 'date', 'speakers', 'label', 'tier', 'theme', 'use',
        'consent']


def table(text):
    rows = [l.strip() for l in text.splitlines() if l.strip().startswith('|')]
    if len(rows) < 2:
        return None, []
    sp = lambda l: [c.strip() for c in l.strip('|').split('|')]
    head = [h.lower() for h in sp(rows[0])]
    data = []
    for l in rows[1:]:
        c = sp(l)
        if all(re.fullmatch(r':?-{2,}:?', x) for x in c if x):
            continue
        data.append(dict(zip(head, c + [''] * (len(head) - len(c)))))
    return head, data


def max_tier(r):
    try:
        n = int(r['speakers'])
    except ValueError:
        return None
    if r['label'].lower() == 'claimed':
        return 'C'
    friend = 'friend' in r.get('source type', '').lower()
    if r['verbatim'].lower() == 'yes' and n >= 3 and not friend:
        return 'A'
    if n >= 2:
        return 'B'
    return 'C'


def check(text):
    head, rows = table(text)
    if head is None:
        return ['no table found']
    p = ['missing column: %s' % c for c in COLS if c not in head]
    if p:
        return p
    seen = set()
    for r in rows:
        rid = r['id'] or '?'
        if rid in seen:
            p.append('%s: duplicate ID' % rid)
        seen.add(rid)
        for c in COLS:
            if not r[c]:
                p.append('%s: blank %s' % (rid, c))
        if r['verbatim'].lower() not in ('yes', 'no'):
            p.append('%s: Verbatim must be yes or no' % rid)
        if r['label'].lower() not in ('stated', 'observed', 'claimed'):
            p.append('%s: Label must be stated, observed or claimed' % rid)
        if not r['source ref'] or re.search(r'\[need', r['source ref'], re.I):
            p.append('%s: no source' % rid)
        mt = max_tier(r)
        if mt is None or int(r['speakers'] or 0) < 1:
            p.append('%s: Speakers must be a whole number of 1 or more' % rid)
        else:
            t = r['tier'].upper()
            if t not in ('A', 'B', 'C'):
                p.append('%s: Tier must be A, B or C' % rid)
            elif t < mt:
                p.append('%s: Tier %s is higher than the evidence allows (max %s)' % (rid, t, mt))
        use, tier = r['use'].lower(), r['tier'].upper()
        if use not in ('internal', 'copy', 'public'):
            p.append('%s: Use must be internal, copy or public' % rid)
        if tier == 'C' and use != 'internal':
            p.append('%s: Tier C may only be internal' % rid)
        if use == 'public' and r['consent'].lower() != 'written':
            p.append('%s: public use needs written consent on file' % rid)
        for _i, n, v in scan(r['quote']):
            p.append('%s: identifier in quote (%s: %s)' % (rid, n, v))
    return p


GOOD = """| ID | Quote | Verbatim | Source type | Source ref | Date | Speakers | Label | Tier | Theme | Use | Consent |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | i forget what i promised by lunch | yes | review | R-04 | 2026-02-11 | 4 | stated | A | forgetting | copy | none |
| Q2 | Buyers keep a notes app they never open | no | forum | F-02 | 2026-02-20 | 2 | observed | B | workaround | internal | none |
| Q3 | everyone in my office wants one | yes | call | C-07 | 2026-03-01 | 1 | claimed | C | demand | internal | none |
"""


def selftest():
    ok = check(GOOD) == []
    bad = GOOD.replace('| 4 | stated | A | forgetting | copy |', '| 1 | stated | A | forgetting | public |')
    bad = bad.replace('| C-07 |', '| [NEED] |').replace('| Q2 |', '| Q1 |')
    # invented fixture: example.com address
    bad = bad.replace('everyone in my office', 'email me at sam.sample@example.com, everyone in my office')
    p = check(bad)
    want = ['higher than', 'written consent', 'no source', 'duplicate', 'identifier']
    ok = ok and all(any(w in x for x in p) for w in want)
    # friend-sourced rows cap at Tier B
    fr = GOOD.splitlines()[:2] + ['| F%d | words %d | yes | friend | FR-%02d | 2026-01-01 | 3 | stated | A | theme | copy | none |'
                                  % (i, i, i) for i in range(1, 12)]
    fp = check('\n'.join(fr))
    ok = ok and len([x for x in fp if 'higher than' in x]) == 11
    ok = ok and check('\n'.join(fr).replace('| A |', '| B |')) == []
    print('selftest: ok' if ok else 'selftest: FAILED %s' % p)
    return 0 if ok else 1


def main(argv):
    if argv[1:] == ['--selftest']:
        return selftest()
    if len(argv) != 2 or argv[1].startswith('-'):
        print(__doc__)
        return 2
    try:
        with open(argv[1], encoding='utf-8') as fh:
            text = fh.read()
    except OSError as e:
        print('usage error: %s' % e)
        return 2
    p = check(text)
    for x in p:
        print('FAIL %s' % x)
    print('RESULT: %s' % ('FIX' if p else 'PASS'))
    print('note: Speakers counts are self-reported; recount from the source refs before hand-off.')
    return 1 if p else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
