#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""check_email.py: the mechanical half of the 14-point send check.

Reads one or more email draft files in the pack's email file format
(see references/email-file-format.md). Each check prints PASS, FAIL or MANUAL.
MANUAL means a person must look (the script cannot see the email tool).

Usage:
  python3 check_email.py [--banned FILE] [--facts FILE] [--max-subject N] DRAFT.md [DRAFT.md ...]
  python3 check_email.py --selftest

  --banned FILE   extra banned words or phrases, one per line ({BANNED_WORDS_FILE})
  --facts FILE    the facts sheet; every price-like amount in the email must appear in it
  --max-subject N subject length limit in characters (default 45)

Exit: 0 all pass, 1 any FAIL, 2 usage error.
"""
import os
import re
import sys

SELLING = {'launch', 'resend', 'reminder', 'answer', 'demo', 'proof', 'objection', 'story',
           'founder-note', 'deadline', 'last-hours', 'warm-up', 'announcement'}
LENGTH = {'last-hours': 120, 'welcome': 200, 'resend': 300, 'reminder': 300, 'deadline': 250,
          'announcement': 200, 'thank-you': 200, 'close': 150, 'launch': 350}
DEFAULT_LEN = 400
BUILTIN_BANNED = ['delve', 'tapestry', 'crucial', 'pivotal', 'testament', 'underscore', 'showcase', 'foster',
                  'harness', 'unlock', 'elevate', 'empower', 'seamless', 'effortless', 'holistic', 'transformative',
                  'unparalleled', 'vibrant', 'robust', 'streamline', 'game-changer', 'game changer', 'game changing', 'supercharge',
                  'leverage', 'groundbreaking', 'world-class', 'best-in-class', "we're thrilled", 'excited to share',
                  'i hope this finds you', 'let\'s dive in', 'click here', 'learn more', 'read more', 'just checking in',
                  'act now', 'once in a lifetime', 'lowest price ever', 'selling fast', 'don\'t miss out']
DAYS = r'(monday|tuesday|wednesday|thursday|friday|saturday|sunday|mon|tue|tues|wed|thu|thur|thurs|fri|sat|sun|tonight|midnight|tomorrow|noon|the end of|end of|[0-9]{1,2}(st|nd|rd|th)?\b|january|february|march|april|june|july|august|september|october|november|december)'
URGENCY = re.compile(r'\b(ends?|ending|closes?|closing|tonight at|last chance|deadline|final hours|hours left|last call|'
                     r'expires?|expiring|while (it|they|stocks?) lasts?|limited time|today only|only today|this week only|'
                     r'ends soon|won\'t last|before it\'s gone|price goes up|doors close|'
                     r'(open|available|on sale|valid|runs?|holds?|lasts?|good)\s+(until|till|til|through|thru)|'
                     r'(until|till|til|through|thru|by|before)\s+' + DAYS + r')(?![a-z])', re.I)
SCARCITY = re.compile(r'\b(only \d+ (left|spots|seats|places)|\d+ (spots|seats|places) left|limited spots|almost gone)\b', re.I)
TZ = re.compile(r'(\{LAUNCH_TZ\}|\b(UTC|GMT|[A-Z]{2,4}T|PT|ET|CT|MT)\b)')
MONEY = re.compile(r'[$\u20ac\u00a3]\s?\d[\d,.]*|\b\d[\d,.]*\s?(usd|eur|gbp|dollars|euros|pounds)\b', re.I)
LINK = re.compile(r'\[([^\]]+)\]\(([^)\s]+)\)')
RAW_URL = re.compile(r'(?<!\()\bhttps?://\S+')
IMG = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
NEED = re.compile(r'\[(NEED|placeholder)[^\]]*\]', re.I)
DASH = re.compile('[\u2014\u2013]|--')
FLIP_END = re.compile(r'\bNo [^.]{1,30}\.\s+No [^.]{1,30}\.\s+(Just|Only) ', re.I)
WEAK_LABEL = {'here', 'click here', 'learn more', 'read more', 'this link', 'link', 'more'}


SUFFIXES = r'(s|es|d|ed|ing|ingly|ly|ness|ment|ments|r|rs|er|ers|able)?'


def stem_rx(w):
    """Match a banned word with common endings: unlock -> unlocks, seamless -> seamlessly, leverage -> leveraging."""
    w = w.strip().lower()
    if ' ' in w or "'" in w:
        return re.compile(r'(?<![a-z])' + re.escape(w) + r'(?![a-z])')
    base = w[:-1] if w.endswith('e') and len(w) > 3 else w
    tail = r'(e|es|ed|ing|ingly|ely|ement|ements|er|ers|able)?' if base != w else SUFFIXES
    if w.endswith('-changer') or w.endswith(' changer'):
        base, tail = w[:-2], r'(er|ers|ing)'
    return re.compile(r'(?<![a-z])' + re.escape(base) + tail + r'(?![a-z])')


CREDIT_LINE = re.compile(r'^(<!-- dylan-pak-credit:.*-->|Created and curated by Dylan Pak\.|License note: free to use and adapt\..*)$')


def strip_credit(text):
    """Remove the pack credit header and footer (and the --- line before the footer) before checking."""
    lines = text.splitlines()
    out = [l for l in lines if not CREDIT_LINE.match(l.strip())]
    while out and out[-1].strip() in ('', '---'):
        out.pop()
    return '\n'.join(out) + '\n'


def parse(text):
    head, body_lines, in_body = {}, [], False
    for line in text.splitlines():
        if not in_body:
            m = re.match(r'^([A-Za-z-]+):\s*(.*)$', line)
            if m and m.group(1).lower() not in ('p.s', 'ps'):
                head[m.group(1).lower()] = m.group(2).strip()
                continue
            if line.strip() == '' and head:
                in_body = True
                continue
            if line.strip().startswith('<!--'):
                continue
            in_body = True
        body_lines.append(line)
    return head, '\n'.join(body_lines)


def words(s):
    return re.findall(r"[A-Za-z0-9'\u2019]+", s)


def check(text, banned_extra=(), facts_text=None, max_subject=45):
    text = strip_credit(text)
    head, body = parse(text)
    full = text
    res = []

    def add(n, name, ok, detail=''):
        res.append((n, name, 'PASS' if ok is True else ('MANUAL' if ok is None else 'FAIL'), detail))

    etype = head.get('type', '').lower()
    low = (head.get('subject', '') + '\n' + head.get('preview', '') + '\n' + body).lower()
    hits = [w for w in list(BUILTIN_BANNED) + [b.lower() for b in banned_extra if b.strip()]
            if stem_rx(w).search(low)]
    add(1, 'banned words', not hits, ', '.join(hits))

    has_unsub = '{unsubscribe}' in low or 'unsubscribe' in low
    has_sign = '{sender_name}' in low or bool(head.get('sign-off')) and head.get('sign-off', '').lower() in low
    add(2, 'locks: sign-off and unsubscribe', has_unsub and has_sign,
        '' if has_unsub and has_sign else 'need {UNSUBSCRIBE} and a sign-off ({SENDER_NAME} or the Sign-off header text)')

    if facts_text is not None:
        flow = facts_text.lower()
        amounts = [m.group(0) for m in MONEY.finditer(head.get('subject', '') + ' ' + body)]
        missing = [a for a in amounts if a.lower().replace(' ', '') not in flow.replace(' ', '')]
        add(3, 'offer facts match facts sheet', not missing, 'not in facts sheet: ' + ', '.join(missing))
    else:
        add(3, 'offer facts match facts sheet', None, 'run with --facts to check amounts; check terms by eye')

    needs = NEED.findall(full)
    add(4, 'no [NEED] or placeholder left', not needs, '%d open' % len(needs) if needs else '')

    sc = SCARCITY.search(body)
    add(5, 'no unverified scarcity', not sc or bool(head.get('scarcity-source')),
        'scarcity line needs a Scarcity-source header with the system and time read' if sc and not head.get('scarcity-source') else '')

    subj, prev = head.get('subject', ''), head.get('preview', '')
    sp = []
    if not subj:
        sp.append('no subject')
    if len(subj) > max_subject:
        sp.append('subject is %d chars (max %d)' % (len(subj), max_subject))
    if re.match(r'^\s*(re|fwd?)\s*:', subj, re.I):
        sp.append('fake Re:/Fwd:')
    if any(len(w) >= 4 and w.isupper() for w in words(subj)):
        sp.append('ALL CAPS word')
    if subj.count('!') > 1:
        sp.append('more than one !')
    if MONEY.search(subj):
        sp.append('price in subject')
    if not prev:
        sp.append('no preview text')
    elif prev.strip().lower() == subj.strip().lower() or prev.lower().startswith(' '.join(words(subj)[:3]).lower() + ' ') and len(words(subj)) >= 3:
        sp.append('preview repeats subject')
    if len(prev) > 100:
        sp.append('preview over 100 chars')
    if re.search('[\U0001F300-\U0001FAFF]', subj):
        sp.append('emoji in subject')
    add(6, 'subject and preview', not sp, '; '.join(sp))

    links = [(l, u) for l, u in LINK.findall(body) if not body[body.find('](' + u) - len(l) - 2:].startswith('![')]
    links = [(l, u) for l, u in links if '{unsubscribe}' not in u.lower() and 'unsubscribe' not in l.lower()]
    dests = sorted(set(u for _l, u in links))
    lp = []
    need_links = 0 if etype in ('close', 'note', 'bridge') else 1
    if len(dests) > 1:
        lp.append('%d different destinations (want 1): %s' % (len(dests), ', '.join(dests)))
    if len(dests) < need_links:
        lp.append('no primary link')
    for l, _u in links:
        n = len(words(l))
        if l.strip().lower() in WEAK_LABEL or not 3 <= n <= 8:
            lp.append('link label "%s" should be 3 to 8 words naming what they get' % l)
    add(7, 'one job, one primary link, clear label', not lp, '; '.join(lp))

    vp = []
    if DASH.search(full):
        vp.append('dash used as punctuation')
    if FLIP_END.search(body):
        vp.append('"No X. No Y. Just Z." pattern')
    sents = [s for s in re.split(r'[.!?]+\s', body) if words(s)]
    if sents:
        avg = sum(len(words(s)) for s in sents) / len(sents)
        if avg > 20:
            vp.append('average sentence %.1f words (max 20)' % avg)
    long_paras = [p for p in body.split('\n\n') if len(words(p)) > 60]
    if long_paras:
        vp.append('%d paragraph(s) over 60 words' % len(long_paras))
    add(8, 'voice basics (dashes, flips, sentence length)', not vp, '; '.join(vp))

    limit = LENGTH.get(etype, DEFAULT_LEN)
    n = len(words(body))
    add(9, 'length band for type', n <= limit, '%d words (limit %d for %s)' % (n, limit, etype or 'untyped'))

    ap = []
    for alt, _src in IMG.findall(body):
        if not alt.strip():
            ap.append('image without alt text')
    stripped = LINK.sub('', body)
    if RAW_URL.search(stripped):
        ap.append('raw URL in body')
    add(10, 'accessibility: alt text, no raw URLs', not ap, '; '.join(ap))

    ex = head.get('exclude', '').lower()
    sg = []
    if not head.get('segment'):
        sg.append('no Segment header')
    if not ex:
        sg.append('no Exclude header')
    elif etype in SELLING and 'buyer' not in ex:
        sg.append('selling email must exclude buyers')
    if ex and 'unsubscrib' not in ex:
        sg.append('Exclude must name unsubscribed')
    add(11, 'segment and suppression', not sg, '; '.join(sg))

    tp = []
    send = head.get('send', '')
    if not send:
        tp.append('no Send header (day and time in the audience zone)')
    elif not TZ.search(send):
        tp.append('Send header has no time zone')
    dl = head.get('deadline', '')
    if URGENCY.search(body) and (not dl or dl.lower() == 'none'):
        tp.append('urgency words but Deadline is none')
    if dl and dl.lower() != 'none' and not TZ.search(dl):
        tp.append('Deadline has no time zone')
    add(12, 'timing and real deadline', not tp, '; '.join(tp))

    add(13, 'tracking and mobile load', None, 'open the link on a phone; check tags in {EMAIL_TOOL}')
    add(14, 'replies reach a human', None, 'confirm the reply-to inbox is read by a person')
    if not etype:
        res.append((0, 'type header', 'FAIL', 'no Type header'))
    return res


def report(name, res):
    print('== %s' % name)
    for n, nm, st, d in res:
        print('%-6s %2d %s%s' % (st, n, nm, (': ' + d) if d else ''))
    return any(st == 'FAIL' for _n, _nm, st, _d in res)


GOOD = """Email: 3
Type: reminder
Segment: opened the launch email, has not bought
Exclude: buyers, unsubscribed, complained, open support case
Send: Tuesday 09:00 {LAUNCH_TZ}
Deadline: Thursday 21:00 {LAUNCH_TZ}
Subject: The question three of you asked
Preview: Yes, it works offline. Here is how.

Hi {FIRST_NAME|there},

Three readers asked the same thing this week. Does the planner work without a signal?

It does. Your week saves to the phone. It syncs when you are back online.

The launch offer ends Thursday at 21:00 {LAUNCH_TZ}.

[See the offline planner in action]({CAMPAIGN_URL})

{SENDER_NAME}

P.S. Reply with any other question. I read every one.

{UNSUBSCRIBE}
"""

BAD = """Type: last-hours
Segment: everyone
Subject: RE: LAST CHANCE!!! Only \u00a320 today
Preview: RE: LAST CHANCE!!! Only \u00a320 today

Only 3 spots left \u2014 act now. [NEED: proof]
[click here](https://a.example) and [here](https://b.example)
"""


def selftest():
    g = check(GOOD)
    b = check(BAD)
    ok = not any(st == 'FAIL' for _n, _nm, st, _d in g)
    fails = {n for n, _nm, st, _d in b if st == 'FAIL'}
    ok = ok and {1, 2, 4, 5, 6, 7, 8, 11, 12}.issubset(fails)
    f = check(GOOD.replace('ends Thursday', 'costs \u00a320 and ends Thursday'), facts_text='price: \u00a325')
    ok = ok and any(n == 3 and st == 'FAIL' for n, _nm, st, _d in f)
    # stem-aware banned words
    for w in ('It works seamlessly.', 'It unlocks your week.', 'It leverages your list.', 'Game-changing.'):
        r = check(GOOD.replace('It does.', w))
        ok = ok and any(n == 1 and st == 'FAIL' for n, _nm, st, _d in r)
    # urgency without a real deadline
    nodl = GOOD.replace('Deadline: Thursday 21:00 {LAUNCH_TZ}', 'Deadline: none').replace(
        'The launch offer ends Thursday at 21:00 {LAUNCH_TZ}.', 'PHRASE')
    for ph in ('The founding plan is open until Thursday.', 'The price holds through Thursday.',
               'You can join until Friday.', 'Available till midnight.', 'Get it before Sunday.'):
        r = check(nodl.replace('PHRASE', ph))
        ok = ok and any(n == 12 and st == 'FAIL' for n, _nm, st, _d in r)
    r = check(nodl.replace('PHRASE', "I'll write about once a week until launch. The plan is closed now."))
    ok = ok and not any(n == 12 and st == 'FAIL' for n, _nm, st, _d in r)
    # credit header and footer do not trip the checks
    credited = ('<!-- dylan-pak-credit: Created and curated by Dylan Pak. -->\n' + GOOD +
                '\n\n---\nCreated and curated by Dylan Pak.\nLicense note: free to use and adapt. Keep the credit.\n')
    ok = ok and not any(st == 'FAIL' for _n, _nm, st, _d in check(credited))
    # an unfilled {BANNED_WORDS_FILE} falls back to the built-in list
    import contextlib, io, os, tempfile
    with tempfile.TemporaryDirectory() as d:
        f = os.path.join(d, 'email-01.md')
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(GOOD)
        with contextlib.redirect_stdout(io.StringIO()):
            ok = ok and main(['x', '--banned', '{BANNED_WORDS_FILE}', f]) == 0
    # the shipped sample campaign must pass (fix: sample folder)
    import glob
    here = os.path.dirname(os.path.abspath(__file__))
    sample = os.path.join(here, '..', 'references', 'sample-campaign')
    drafts = sorted(glob.glob(os.path.join(sample, 'drafts', '*.md')))
    if drafts:
        with open(os.path.join(sample, 'brief.md'), encoding='utf-8') as fh:
            facts = fh.read()
        for d in drafts:
            with open(d, encoding='utf-8') as fh:
                ok = ok and not any(st == 'FAIL' for _n, _nm, st, _d in check(fh.read(), facts_text=facts))
    print('selftest: ok' if ok else 'selftest: FAILED')
    if not ok:
        report('good', g)
        report('bad', b)
    return 0 if ok else 1


def main(argv):
    args = argv[1:]
    if args == ['--selftest']:
        return selftest()
    banned, facts, maxs, files = [], None, 45, []
    try:
        while args:
            a = args.pop(0)
            if a == '--banned':
                bf = args.pop(0)
                if re.fullmatch(r'\{[A-Z_]+\}', bf) or bf.lower() in ('none', 'builtin', 'built-in'):
                    print('note: no banned-words file given (%s); using the built-in list only' % bf)
                else:
                    with open(bf, encoding='utf-8') as fh:
                        banned = [l.strip() for l in fh if l.strip() and not l.startswith('#')]
            elif a == '--facts':
                with open(args.pop(0), encoding='utf-8') as fh:
                    facts = fh.read()
            elif a == '--max-subject':
                maxs = int(args.pop(0))
            elif a.startswith('-'):
                raise ValueError('unknown flag ' + a)
            else:
                files.append(a)
        if not files:
            raise ValueError('no draft files given')
        texts = []
        for f in files:
            with open(f, encoding='utf-8') as fh:
                texts.append((f, fh.read()))
    except (IndexError, ValueError, OSError) as e:
        print('usage error: %s' % e)
        print(__doc__)
        return 2
    failed = False
    for f, t in texts:
        failed = report(f, check(t, banned, facts, maxs)) or failed
    print('RESULT: %s' % ('FIX' if failed else 'PASS (now do the MANUAL items and the cold read)'))
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
