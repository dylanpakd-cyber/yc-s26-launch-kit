#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""check_run.py: checks a run plan table before any email is drafted.

The run plan is a markdown table with these columns (any order, case ignored):
  Email | Day | Segment | Type | Job | Doubt | Subject angle | Link | Deadline | Exclude | Status

Checks:
  1. all columns present and every row filled (use "none" or "n/a", never blank)
  2. one job per email (no "and", "&", "+", ";" or "/" in Job)
  3. every selling email excludes buyers and unsubscribed people
  4. one deadline for the whole run (every non-"none" Deadline is identical) and it names a time zone
  5. a run with a deadline has a last-hours email and a close email
  6. no two emails of the same type back to back
  7. a run of five or more has at least one proof or demo email and one answer or objection email
  8. answer and objection rows name the doubt
  9. one link per row
 10. persuasive sends to the main segment are at or under the cap (default 9)
 11. Status is planned, draft or owner-approved (this bot never sends or schedules)

Usage: python3 check_run.py [--cap N] PLAN.md
       python3 check_run.py --selftest
Exit: 0 pass, 1 fail, 2 usage error.
"""
import re
import sys

COLS = ['email', 'day', 'segment', 'type', 'job', 'doubt', 'subject angle', 'link', 'deadline', 'exclude', 'status']
SELLING = {'launch', 'resend', 'reminder', 'answer', 'demo', 'proof', 'objection', 'story', 'founder-note',
           'deadline', 'last-hours', 'announcement'}
TZ = re.compile(r'(\{LAUNCH_TZ\}|\b(UTC|GMT|[A-Z]{2,4}T|PT|ET|CT|MT)\b)')
STATUS = {'planned', 'draft', 'owner-approved'}


def parse_table(text):
    rows = [l.strip() for l in text.splitlines() if l.strip().startswith('|')]
    if len(rows) < 2:
        return None, []
    split = lambda l: [c.strip() for c in l.strip('|').split('|')]
    head = [h.lower() for h in split(rows[0])]
    data = []
    for l in rows[1:]:
        cells = split(l)
        if all(re.fullmatch(r':?-{2,}:?', c) for c in cells if c):
            continue
        data.append(dict(zip(head, cells + [''] * (len(head) - len(cells)))))
    return head, data


def check(text, cap=9):
    head, rows = parse_table(text)
    out = []

    def add(n, name, problems):
        out.append((n, name, not problems, '; '.join(problems)))

    if head is None:
        add(1, 'columns and filled rows', ['no table found'])
        return out
    p = ['missing column: ' + c for c in COLS if c not in head]
    for r in rows:
        for c in COLS:
            if c in head and not r.get(c, '').strip():
                p.append('email %s: blank %s' % (r.get('email', '?'), c))
    add(1, 'columns and filled rows', p)
    if any(x.startswith('missing column') for x in p):
        return out
    add(2, 'one job per email', ['email %s: job has two parts "%s"' % (r['email'], r['job'])
                                 for r in rows if re.search(r'\band\b|&|\+|;|/', r['job'], re.I)])
    p = []
    for r in rows:
        if r['type'].lower() in SELLING:
            ex = r['exclude'].lower()
            if 'buyer' not in ex or 'unsubscrib' not in ex:
                p.append('email %s: Exclude must name buyers and unsubscribed' % r['email'])
    add(3, 'buyers and unsubscribed excluded', p)
    dls = sorted(set(r['deadline'] for r in rows if r['deadline'].lower() not in ('none', 'n/a')))
    p = []
    if len(dls) > 1:
        p.append('more than one deadline: ' + ' | '.join(dls))
    for d in dls:
        if not TZ.search(d):
            p.append('deadline has no time zone: ' + d)
    add(4, 'one real deadline with time zone', p)
    types = [r['type'].lower() for r in rows]
    p = []
    if dls:
        if 'last-hours' not in types:
            p.append('no last-hours email')
        if 'close' not in types:
            p.append('no close email')
    add(5, 'last-hours and close present', p)
    add(6, 'no same type back to back', ['emails %s and %s are both %s' % (rows[i - 1]['email'], rows[i]['email'], types[i])
                                         for i in range(1, len(rows)) if types[i] == types[i - 1]])
    p = []
    if len(rows) >= 5:
        if not set(types) & {'proof', 'demo'}:
            p.append('no proof or demo email')
        if not set(types) & {'answer', 'objection'}:
            p.append('no answer or objection email')
    add(7, 'proof and objection coverage', p)
    add(8, 'doubt named', ['email %s: no doubt named' % r['email'] for r in rows
                           if r['type'].lower() in ('answer', 'objection') and r['doubt'].lower() in ('none', 'n/a', '')])
    add(9, 'one link per row', ['email %s: more than one link' % r['email'] for r in rows
                                if len(re.findall(r'https?://|\{[A-Z_]*URL[A-Z_]*\}', r['link'])) > 1 or ',' in r['link']])
    n = sum(1 for t in types if t in SELLING)
    add(10, 'persuasive send cap', ['%d selling emails, cap is %d' % (n, cap)] if n > cap else [])
    add(11, 'status is planned, draft or owner-approved', ['email %s: status "%s"' % (r['email'], r['status'])
                                                           for r in rows if r['status'].lower() not in STATUS])
    return out


GOOD = """| Email | Day | Segment | Type | Job | Doubt | Subject angle | Link | Deadline | Exclude | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | D-1 | waitlist | announcement | say it opens tomorrow | none | the date | {CAMPAIGN_URL} | Thu 21:00 {LAUNCH_TZ} | buyers, unsubscribed | planned |
| 2 | D1 | waitlist | launch | ask for the sale | none | it is ready | {CAMPAIGN_URL} | Thu 21:00 {LAUNCH_TZ} | buyers, unsubscribed | planned |
| 3 | D2 | non-openers | resend | reach non-openers | none | new angle | {CAMPAIGN_URL} | Thu 21:00 {LAUNCH_TZ} | buyers, unsubscribed, openers | planned |
| 4 | D3 | waitlist | proof | show it working | will it work for me | demo | {CAMPAIGN_URL} | Thu 21:00 {LAUNCH_TZ} | buyers, unsubscribed | planned |
| 5 | D4 | waitlist | answer | settle the price doubt | is it worth it | the question | {CAMPAIGN_URL} | Thu 21:00 {LAUNCH_TZ} | buyers, unsubscribed | planned |
| 6 | D5 AM | waitlist | deadline | name the last day | none | today | {CAMPAIGN_URL} | Thu 21:00 {LAUNCH_TZ} | buyers, unsubscribed | planned |
| 7 | D5 PM | clickers | last-hours | wake the deadline | none | hours left | {CAMPAIGN_URL} | Thu 21:00 {LAUNCH_TZ} | buyers, unsubscribed | planned |
| 8 | D6 | non-buyers | close | say it is closed | none | closed | none | none | buyers, unsubscribed | planned |
"""


def selftest():
    ok = all(r[2] for r in check(GOOD))
    bad = GOOD.replace('| 5 | D4 | waitlist | answer | settle the price doubt | is it worth it',
                       '| 5 | D4 | waitlist | proof | settle price and show proof | none')
    bad = bad.replace('buyers, unsubscribed | planned |\n| 7', 'everyone | sent |\n| 7')
    bad = bad.replace('| 7 | D5 PM | clickers | last-hours', '| 7 | D5 PM | clickers | deadline')
    fails = {n for n, _nm, good, _d in check(bad) if not good}
    ok = ok and {2, 3, 5, 6, 7, 11}.issubset(fails)
    ok = ok and not check('no table')[0][2]
    print('selftest: ok' if ok else 'selftest: FAILED %s' % sorted(fails))
    return 0 if ok else 1


def main(argv):
    args = argv[1:]
    if args == ['--selftest']:
        return selftest()
    cap = 9
    try:
        if args[:1] == ['--cap']:
            cap = int(args[1])
            args = args[2:]
        if len(args) != 1 or args[0].startswith('-'):
            raise ValueError('give one plan file')
        with open(args[0], encoding='utf-8') as fh:
            text = fh.read()
    except (IndexError, ValueError, OSError) as e:
        print('usage error: %s' % e)
        print(__doc__)
        return 2
    res = check(text, cap)
    for n, nm, good, d in res:
        print('%-4s %2d %s%s' % ('PASS' if good else 'FAIL', n, nm, (': ' + d) if d else ''))
    failed = any(not g for _n, _nm, g, _d in res)
    print('RESULT: %s' % ('FIX' if failed else 'PASS'))
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
