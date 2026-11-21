#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""check_brief.py: gate for step 1. Checks the facts sheet plus voice profile file.

The file uses "Key: value" lines (see references/brief-and-voice-template.md).
Required keys and rules:
  Offer, Price rule, Guarantee, Launch date, Close date, Time zone, Segments,
  Signup promise, Primary action, Support route    -> present, not blank, not [NEED]
  Never claims                                    -> at least 3 items, separated by ";"
  Voice source                                    -> "approved samples" or "default starter voice"
  Avg sentence words                              -> a number from 5 to 25
  Contractions                                    -> yes or no
  Sign-off                                        -> present
  Banned words                                    -> present (may say "built-in list only")
  Links per email                                 -> a number, 1 or 2
Usage: python3 check_brief.py BRIEF.md
       python3 check_brief.py --selftest
Exit: 0 pass, 1 fail, 2 usage error.
"""
import re
import sys

HARD = ['offer', 'price rule', 'guarantee', 'launch date', 'close date', 'time zone', 'segments',
        'signup promise', 'primary action', 'support route']


def parse(text):
    kv = {}
    for line in text.splitlines():
        m = re.match(r'^\s*[-*]?\s*([A-Za-z][A-Za-z -]+?)\s*:\s*(.*)$', line)
        if m:
            kv[m.group(1).strip().lower()] = m.group(2).strip()
    return kv


def check(text):
    kv = parse(text)
    p = []
    for k in HARD:
        v = kv.get(k, '')
        if not v:
            p.append('missing: %s' % k)
        elif re.search(r'\[(NEED|placeholder)', v, re.I) or re.fullmatch(r'\{[A-Z_]+\}', v):
            p.append('not filled: %s (stop and ask the owner)' % k)
    nc = [x for x in kv.get('never claims', '').split(';') if x.strip()]
    if len(nc) < 3:
        p.append('never claims needs 3 or more items separated by ";"')
    vs = kv.get('voice source', '').lower()
    if vs not in ('approved samples', 'default starter voice'):
        p.append('voice source must be "approved samples" or "default starter voice"')
    try:
        a = float(kv.get('avg sentence words', 'x'))
        if not 5 <= a <= 25:
            p.append('avg sentence words out of range 5 to 25')
    except ValueError:
        p.append('avg sentence words must be a number')
    if kv.get('contractions', '').lower() not in ('yes', 'no'):
        p.append('contractions must be yes or no')
    for k in ('sign-off', 'banned words'):
        if not kv.get(k):
            p.append('missing: %s' % k)
    if kv.get('links per email', '') not in ('1', '2'):
        p.append('links per email must be 1 or 2')
    return p


GOOD = """Offer: Founding plan with a 30-day refund (example)
Price rule: copy the price from the checkout page on the day; never round
Guarantee: 30-day refund, no questions (example wording)
Launch date: Tuesday, March 10
Close date: Thursday, March 12, 21:00
Time zone: PT (example)
Segments: waitlist; early testers; buyers
Signup promise: one email when it is ready, then a short launch run
Primary action: buy the founding plan
Support route: reply to this email
Never claims: medical results; income results; works for everyone
Voice source: default starter voice
Avg sentence words: 12
Contractions: yes
Sign-off: {SENDER_NAME}
Banned words: built-in list only
Links per email: 1
"""


def selftest():
    ok = check(GOOD) == []
    bad = GOOD.replace('Tuesday, March 10', '[NEED: launch date]').replace('Contractions: yes', 'Contractions: often')
    bad = bad.replace('medical results; income results; works for everyone', 'medical results')
    ok = ok and len(check(bad)) == 3
    print('selftest: ok' if ok else 'selftest: FAILED')
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
    return 1 if p else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
