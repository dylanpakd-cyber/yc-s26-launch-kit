#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""check_cards.py: validate templated cards (see references/templates.md).

Each card starts with a "## " heading and holds "Field: value" lines.
Kinds:
  index      call or source index cards
  avatar     buyer avatar cards (exactly 3, or fewer with an "Avatar count note:" line)
  objection  five-layer objection stacks
  locks      insight-to-truth lock pages
Usage: python3 check_cards.py --kind KIND [--bank BANK.md] FILE
       python3 check_cards.py --selftest
  --bank  quote bank; soundbite and empathy IDs must exist there at Tier A or B
Exit: 0 pass, 1 fail, 2 usage error.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_quote_bank import table  # noqa: E402
from check_redaction import scan  # noqa: E402

FIELDS = {
    'index': ['source', 'date', 'segment', 'speaker role', 'topic', 'tags', 'summary', 'quote ids',
              'decision moment', 'redaction'],
    'avatar': ['nickname', 'age band', 'core problem', 'moment it bites', 'top fears', 'emotional drivers',
               'failed solutions', 'soundbites', 'desired transformation', 'market beliefs', 'emotional blockers',
               'relationship impact', 'objections', 'awareness level', 'where they spend time', 'proof that persuades',
               'inferred'],
    'objection': ['objection', 'count', 'sources', 'belief', 'fear', 'identity', 'defuse', 'proof',
                  'does not claim', 'avatar', 'asset'],
    'locks': ['people', 'not for', 'empathy', 'doing', 'frustrations', 'heaven', 'hell', 'positioning',
              'how it works', 'promise', 'so what', 'proof', 'priority', 'honesty check'],
}
TAGS = {'pain', 'desire', 'doubt', 'workaround', 'buying signal', 'failed solution', 'trigger', 'question'}
IDS = re.compile(r'\b[A-Z]{1,2}\d{1,4}\b')


def cards(text):
    out = []
    for part in re.split(r'^##\s+', text, flags=re.M)[1:]:
        title, _, body = part.partition('\n')
        kv = {}
        for line in body.splitlines():
            m = re.match(r'^\s*[-*]?\s*([A-Za-z][A-Za-z -]+?)\s*:\s*(.*)$', line)
            if m:
                kv[m.group(1).strip().lower()] = m.group(2).strip()
        out.append((title.strip(), kv, body))
    return out


def check(kind, text, bank_text=None):
    cs = cards(text)
    p = []
    tiers = None
    if bank_text:
        _h, rows = table(bank_text)
        tiers = {r['id']: r.get('tier', '').upper() for r in rows}
    if not cs:
        return ['no cards found (each card starts with "## ")']
    real = [c for c in cs if not c[0].lower().startswith('avatar count note')]
    for title, kv, body in real:
        for f in FIELDS[kind]:
            if not kv.get(f):
                p.append('%s: missing %s' % (title, f))
        for _i, n, v in scan(body):
            p.append('%s: identifier (%s: %s)' % (title, n, v))
        if kind == 'index':
            tags = [t.strip().lower() for t in kv.get('tags', '').split(',') if t.strip()]
            if len(tags) != 3 or any(t not in TAGS for t in tags):
                p.append('%s: Tags must be 3 of %s' % (title, ', '.join(sorted(TAGS))))
            if kv.get('redaction', '').lower() not in ('done', 'checked'):
                p.append('%s: Redaction must be done' % title)
        if kind == 'avatar':
            fears = [x for x in kv.get('top fears', '').split(';') if x.strip()]
            if len(fears) != 5:
                p.append('%s: Top fears needs 5 items separated by ";"' % title)
            sb = IDS.findall(kv.get('soundbites', ''))
            if len(sb) < 3:
                p.append('%s: Soundbites need 3 or more quote-bank IDs' % title)
            if tiers is not None:
                for i in sb:
                    if tiers.get(i) not in ('A', 'B'):
                        p.append('%s: soundbite %s is not a Tier A or B bank item' % (title, i))
        if kind == 'objection':
            pr = kv.get('proof', '')
            if not pr:
                pass
            elif '[need proof' not in pr.lower() and not IDS.search(pr) and 'source' not in pr.lower():
                p.append('%s: Proof must cite a source or say [NEED PROOF]' % title)
            if not re.fullmatch(r'\d+', kv.get('count', '')):
                p.append('%s: Count must be a number' % title)
        if kind == 'locks':
            for f in FIELDS['locks']:
                if re.search(r'\[need', kv.get(f, ''), re.I):
                    p.append('%s: lock open (%s is [NEED])' % (title, f))
            if not IDS.search(kv.get('empathy', '')):
                p.append('%s: Empathy must cite a quote-bank ID' % title)
            if tiers is not None:
                for i in IDS.findall(kv.get('empathy', '')):
                    if tiers.get(i) not in ('A', 'B'):
                        p.append('%s: empathy quote %s is not Tier A or B' % (title, i))
            if kv.get('honesty check', '').upper() != 'PASS':
                p.append('%s: Honesty check must be PASS' % title)
    if kind == 'avatar':
        note = any(c[0].lower().startswith('avatar count note') for c in cs) or 'avatar count note' in text.lower()
        if len(real) != 3 and not note:
            p.append('%d avatars; need exactly 3, or an "Avatar count note:" saying why fewer' % len(real))
        if len(real) > 3:
            p.append('more than 3 avatars')
        probs = [re.sub(r'\W+', ' ', kv.get('core problem', '').lower()).strip() for _t, kv, _b in real]
        if len(set(probs)) != len(probs):
            p.append('two avatars share a core problem; they are the same person')
    return p


AV = """## Avatar {n}: The {nick}
Nickname: The {nick}
Age band: 30 to 45 (estimate)
Core problem: {prob}
Moment it bites: {prob} at the worst time
Top fears: a; b; c; d; e
Emotional drivers: relief, pride
Failed solutions: notes app (Q2)
Soundbites: Q1, Q2, Q4
Desired transformation: a calm Tuesday
Market beliefs: tools like this are toys
Emotional blockers: embarrassment
Relationship impact: partner notices
Objections: price (Q4)
Awareness level: problem aware
Where they spend time: forums (Q2)
Proof that persuades: a demo
Inferred: age band
"""


def selftest():
    good = ''.join(AV.format(n=i, nick=k, prob=pr) for i, k, pr in
                   ((1, 'Juggler', 'forgets promises made in meetings'), (2, 'Carer', 'misses family dates'),
                    (3, 'Rebuilder', 'lost trust after a missed handoff')))
    bank = ('| ID | Quote | Verbatim | Source type | Source ref | Date | Speakers | Label | Tier | Theme | Use | Consent |\n'
            '|---|---|---|---|---|---|---|---|---|---|---|---|\n'
            '| Q1 | a | yes | review | R1 | d | 3 | stated | A | t | copy | none |\n'
            '| Q2 | b | yes | forum | F1 | d | 2 | observed | B | t | internal | none |\n'
            '| Q4 | c | yes | call | C1 | d | 1 | stated | C | t | internal | none |\n')
    ok = check('avatar', good) == []
    p = check('avatar', good, bank)
    ok = ok and any('Q4' in x for x in p)
    two = ''.join(AV.format(n=i, nick='Same', prob='same problem') for i in (1, 2))
    p = check('avatar', two)
    ok = ok and any('need exactly 3' in x for x in p) and any('same person' in x for x in p)
    lock = ('## Lock page 1\nPeople: x\nNot for: y\nEmpathy: Q1\nDoing: a\nFrustrations: b\nHeaven: c\nHell: d\n'
            'Positioning: e\nHow it works: f\nPromise: [NEED: outcome]\nSo what: g\nProof: Q1\nPriority: h\nHonesty check: PASS\n')
    ok = ok and any('lock open' in x for x in check('locks', lock))
    obj = ('## Objection 1\nObjection: too pricey\nCount: 7\nSources: Q1, Q2\nBelief: b\nFear: f\nIdentity: i\n'
           'Defuse: d\nProof: [NEED PROOF: refund terms]\nDoes not claim: n\nAvatar: 1\nAsset: email\n')
    ok = ok and check('objection', obj) == []
    idx = ('## Call 03\nSource: owner notes\nDate: as given\nSegment: early tester\nSpeaker role: parent\nTopic: setup\n'
           'Tags: pain, doubt, workaround\nSummary: s\nQuote IDs: Q1\nDecision moment: n/a\nRedaction: done\n')
    ok = ok and check('index', idx) == [] and check('index', idx.replace('pain, doubt', 'pain, vibes')) != []
    here = os.path.dirname(os.path.abspath(__file__))
    sample = os.path.join(here, '..', 'references', 'sample-research')
    if os.path.isdir(sample):
        rd = lambda n: open(os.path.join(sample, n), encoding='utf-8').read()
        sb = rd('quote-bank.md')
        for kind, f in (('index', 'index.md'), ('avatar', 'avatars.md'), ('objection', 'objections.md'), ('locks', 'locks.md')):
            ok = ok and check(kind, rd(f), sb if kind in ('avatar', 'locks') else None) == []
    print('selftest: ok' if ok else 'selftest: FAILED')
    return 0 if ok else 1


def main(argv):
    args = argv[1:]
    if args == ['--selftest']:
        return selftest()
    kind = bank = None
    files = []
    try:
        while args:
            a = args.pop(0)
            if a == '--kind':
                kind = args.pop(0)
            elif a == '--bank':
                bank = args.pop(0)
            elif a.startswith('-'):
                raise ValueError('unknown flag ' + a)
            else:
                files.append(a)
        if kind not in FIELDS or len(files) != 1:
            raise ValueError('need --kind index|avatar|objection|locks and one file')
        with open(files[0], encoding='utf-8') as fh:
            text = fh.read()
        bt = None
        if bank:
            with open(bank, encoding='utf-8') as fh:
                bt = fh.read()
    except (IndexError, ValueError, OSError) as e:
        print('usage error: %s' % e)
        print(__doc__)
        return 2
    p = check(kind, text, bt)
    for x in p:
        print('FAIL %s' % x)
    print('RESULT: %s' % ('FIX' if p else 'PASS'))
    return 1 if p else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
