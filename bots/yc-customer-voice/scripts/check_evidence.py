#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""check_evidence.py: minimum-evidence gate and research-document check.

Part 1 (always): reads the quote bank and applies the minimum-evidence bar:
  - at least --min-sources distinct Source refs (default 10)
  - at least 2 different Source types, at least one of them not "friend"
  - at least one theme with a Tier A row, or at least 3 themes with Tier B rows
  Below the bar prints "INSUFFICIENT EVIDENCE" and exits 1.
Part 2 (with --doc): checks the research document:
  - every required "## " section is present, in any order
  - each section cites 2 or more quote-bank IDs, or says "thin" (Open questions and Concepts exempt)
  - every cited ID exists in the bank
  - Tier C IDs are cited only under "Open questions"
  - "Concepts" is empty or says "left empty"
Usage: python3 check_evidence.py --bank BANK.md [--doc DOC.md] [--min-sources N]
       python3 check_evidence.py --selftest
Exit: 0 pass, 1 fail or insufficient evidence, 2 usage error.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_quote_bank import table  # noqa: E402

SECTIONS = ['top pain points', 'failed solutions', 'desired outcomes', 'objections', 'misconceptions',
            'golden nuggets', 'words to borrow and avoid', 'triggers', 'what changed their mind', 'alternatives',
            'necessity test', 'strategy implications', 'language analysis', 'key personas', 'open questions',
            'concepts']
EXEMPT = {'open questions', 'concepts', 'key personas'}


def bar(rows, min_sources):
    p = []
    refs = {r.get('source ref', '') for r in rows if r.get('source ref')}
    types = {r.get('source type', '').lower() for r in rows if r.get('source type')}
    a_themes = {r['theme'] for r in rows if r.get('tier', '').upper() == 'A'
                and 'friend' not in r.get('source type', '').lower()}
    b_themes = {r['theme'] for r in rows if r.get('tier', '').upper() == 'B'}
    if len(refs) < min_sources:
        p.append('%d distinct sources, need %d' % (len(refs), min_sources))
    if len(types) < 2:
        p.append('%d source type(s), need 2' % len(types))
    if types and all('friend' in x for x in types):
        p.append('only friend sources; need at least one source type that is not friend')
    if not a_themes and len(b_themes) < 3:
        p.append('no Tier A theme and only %d Tier B theme(s), need 3' % len(b_themes))
    return p


def doc_check(doc, rows):
    tiers = {r['id']: r.get('tier', '').upper() for r in rows}
    parts = re.split(r'^##\s+', doc, flags=re.M)
    secs = {}
    for part in parts[1:]:
        title, _, body = part.partition('\n')
        secs[title.strip().lower()] = body
    p = ['missing section: %s' % s for s in SECTIONS if s not in secs]
    for name, body in secs.items():
        ids = set(re.findall(r'\b[A-Z]{1,2}\d{1,4}\b', body))
        ids = {i for i in ids if i in tiers or re.fullmatch(r'Q\d+', i)}
        for i in ids:
            if i not in tiers:
                p.append('%s: cites %s, not in the bank' % (name, i))
            elif tiers[i] == 'C' and name != 'open questions':
                p.append('%s: cites Tier C item %s as evidence' % (name, i))
        if name in SECTIONS and name not in EXEMPT and len(ids) < 2 and 'thin' not in body.lower():
            p.append('%s: cites %d IDs and is not marked thin' % (name, len(ids)))
        if name == 'concepts':
            txt = re.sub(r'<!--.*?-->', '', body, flags=re.S).strip().lower()
            txt = txt.split('\n---')[0].strip()
            if txt and 'left empty' not in txt:
                p.append('concepts: must stay empty (this bot writes no ads)')
    return p


def run(bank_text, doc_text=None, min_sources=10):
    head, rows = table(bank_text)
    if head is None:
        return ['quote bank: no table found'], False
    p = bar(rows, min_sources)
    insufficient = bool(p)
    if doc_text is not None:
        p += doc_check(doc_text, rows)
    return p, insufficient


def _bank(n_sources, tier='A'):
    lines = ['| ID | Quote | Verbatim | Source type | Source ref | Date | Speakers | Label | Tier | Theme | Use | Consent |',
             '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for i in range(1, n_sources + 1):
        st = 'review' if i % 2 else 'forum'
        lines.append('| Q%d | example words %d | yes | %s | S-%02d | 2026-01-%02d | 3 | stated | %s | theme%d | internal | none |'
                     % (i, i, st, i, i, tier, i % 3))
    return '\n'.join(lines) + '\n'


def _doc(extra=''):
    out = []
    for s in SECTIONS:
        if s == 'concepts':
            body = 'Left empty.'
        elif s in EXEMPT:
            body = 'none yet'
        else:
            body = 'Finding (Q1, Q2).'
        out.append('## %s\n%s\n' % (s.capitalize(), body))
    return '\n'.join(out) + extra


def selftest():
    p, ins = run(_bank(12), _doc())
    ok = p == [] and not ins
    p, ins = run(_bank(4))
    ok = ok and ins and any('distinct sources' in x for x in p)
    bad_doc = _doc().replace('## Concepts\nLeft empty.', '## Concepts\nHook: an ad idea').replace('Finding (Q1, Q2).', 'Finding (Q1, Q99).', 1)
    p, _ins = run(_bank(12), bad_doc)
    ok = ok and any('Q99' in x for x in p) and any('concepts' in x for x in p)
    # friend-only evidence never clears the bar
    fb = _bank(12).replace('| review |', '| friend |').replace('| forum |', '| friend |')
    p, ins = run(fb)
    ok = ok and ins and any('friend' in x for x in p)
    here = os.path.dirname(os.path.abspath(__file__))
    sample = os.path.join(here, '..', 'references', 'sample-research')
    if os.path.isdir(sample):
        with open(os.path.join(sample, 'quote-bank.md'), encoding='utf-8') as fh:
            sb = fh.read()
        with open(os.path.join(sample, 'research-doc.md'), encoding='utf-8') as fh:
            sd = fh.read()
        sp, sins = run(sb, sd)
        ok = ok and sp == [] and not sins
    print('selftest: ok' if ok else 'selftest: FAILED %s' % p)
    return 0 if ok else 1


def main(argv):
    args = argv[1:]
    if args == ['--selftest']:
        return selftest()
    bank = doc = None
    mins = 10
    try:
        while args:
            a = args.pop(0)
            if a == '--bank':
                bank = args.pop(0)
            elif a == '--doc':
                doc = args.pop(0)
            elif a == '--min-sources':
                mins = int(args.pop(0))
            else:
                raise ValueError('unknown argument ' + a)
        if not bank:
            raise ValueError('--bank is required')
        with open(bank, encoding='utf-8') as fh:
            bt = fh.read()
        dt = None
        if doc:
            with open(doc, encoding='utf-8') as fh:
                dt = fh.read()
    except (IndexError, ValueError, OSError) as e:
        print('usage error: %s' % e)
        print(__doc__)
        return 2
    p, ins = run(bt, dt, mins)
    for x in p:
        print('FAIL %s' % x)
    if ins:
        print('RESULT: INSUFFICIENT EVIDENCE (run the no-data path in references/no-data-path.md)')
    else:
        print('RESULT: %s' % ('FIX' if p else 'PASS'))
    return 1 if p else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
