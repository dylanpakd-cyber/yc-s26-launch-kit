#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""check_redaction.py: scan saved research files for personal identifiers.

Finds: email addresses, phone numbers, social handles, profile URLs, street
addresses, order or account numbers, card-like numbers, and likely personal
names (name heuristic). Role labels like [BUYER-3] are fine.

Usage: python3 check_redaction.py [--allow WORDS_FILE] FILE [FILE ...]
       python3 check_redaction.py --selftest
  --allow  one word per line that is not a person (product, brand, place names)
Exit: 0 clean, 1 identifiers found, 2 usage error.
"""
import re
import sys

PATTERNS = [
    ('email', re.compile(r'\b[\w.+-]+@[\w-]+\.[\w.]+\b')),
    ('phone', re.compile(r'(?<!\w)(\+?\d[\d ().-]{7,}\d)(?!\w)')),
    ('handle', re.compile(r'(?<![\w.])@[A-Za-z0-9_]{2,}')),
    ('profile url', re.compile(r'(?:https?://\S*(/u/|/user/|/users/|/profile|/in/|/people/)\S*|'
                               r'(?<![\w.])(?:https?://)?(?:www\.)?(?:twitter\.com|x\.com|instagram\.com|'
                               r'facebook\.com|linkedin\.com|tiktok\.com)/[^\s)\]>]+)', re.I)),
    ('street address', re.compile(r'\b\d{1,5}\s+[A-Z][a-z]+(\s[A-Z][a-z]+)?\s(Street|St|Avenue|Ave|Road|Rd|Lane|Ln|Drive|Dr|Blvd)\b')),
    ('order or account number', re.compile(r'(#\s?\d{4,}|\b(order|account|ticket|invoice)\s*(no\.?|number|#)?\s*\d{4,})', re.I)),
]
NAME_CUES = re.compile(r"\b(?:my name is|i'm|i am|this is|named|called|said|asked|told me|husband|wife|son|daughter|"
                       r"boss|mr\.?|mrs\.?|ms\.?|dr\.?)\s+((?-i:[A-Z][a-z]{2,}))(?:\s+((?-i:[A-Z][a-z]{2,})))?", re.I)
NAME_BEFORE = re.compile(r"\b([A-Z][a-z]{2,})(?:\s+([A-Z][a-z]{2,}))?\s+(?:said|says|told|wrote|asked|mentioned|explained)\b")
NAME_FIELD = re.compile(r'^\s*[-*]?\s*(name|customer|speaker|interviewee|reviewer|author)\s*:\s*(?!\[|role|n/a|none|redacted|\{)(\S.*)$', re.I)
STOP = {'The', 'This', 'That', 'They', 'There', 'Then', 'When', 'What', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December', 'She', 'Her', 'His', 'Him', 'We', 'You', 'Our', 'One', 'Someone', 'Everyone', 'Nobody', 'Customer', 'Customers', 'Buyer', 'Buyers', 'Parent', 'User', 'Users', 'Reviewer', 'Founder', 'Owner', 'Support', 'Another', 'Most', 'Many', 'Some', 'Few', 'Three', 'Two', 'Five', 'Reddit', 'Google', 'Amazon', 'App', 'Store', 'Tier', 'Example', 'Use', 'Concepts', 'Verbatim', 'Label', 'Quote', 'Source', 'Consent', 'Theme', 'Speakers', 'Not', 'So', 'Just', 'Really', 'Going', 'Very', 'Also', 'Still', 'Happy', 'Glad', 'Sure', 'Sorry', 'Here', 'Done'}


def scan(text, allow=()):
    hits = []
    allow = set(allow) | STOP
    for i, line in enumerate(text.splitlines(), 1):
        for name, rx in PATTERNS:
            for m in rx.finditer(line):
                val = m.group(0)
                if name == 'phone' and len(re.sub(r'\D', '', val)) < 9:
                    continue
                if name == 'phone' and re.fullmatch(r'\d{4}-\d{2}-\d{2}', val.strip()):
                    continue
                hits.append((i, name, val))
        m = NAME_FIELD.match(line)
        if m:
            hits.append((i, 'name field', m.group(2).strip()))
        for m in list(NAME_CUES.finditer(line)) + list(NAME_BEFORE.finditer(line)):
            w = m.group(1)
            if w not in allow:
                hits.append((i, 'likely name', w + (' ' + m.group(2) if m.group(2) else '')))
    return hits


def selftest():
    # invented fixture data only: fake person, example.com domain, fake handle and numbers
    dirty = ("Alex Sample said it broke.\nReach me at alex.sample@example.com or +1 555 010 9999.\n"
             "Follow @alexsample_99. Order #48213. Lives at 12 Elm Street.\nName: Alex Sample\n"
             "https://social.example/user/alexsample\n")
    clean = ("[BUYER-3] said it broke after a week. Source: review R-14, 2026-03-02.\n"
             "Name: [redacted]\nSpeaker: role: parent of two\nOn Monday the app froze.\n")
    hd = {n for _i, n, _v in scan(dirty)}
    ok = {'email', 'phone', 'handle', 'order or account number', 'street address', 'name field', 'likely name',
          'profile url'}.issubset(hd)
    ok = ok and scan(clean) == []
    # invented name fixtures: mixed-case cues must work too
    for cue in ("My name is Fixture Person.", "Hi I'm Fixture Person", "MY NAME IS Fixture Person"):
        ok = ok and any(n == 'likely name' for _i, n, _v in scan(cue))
    for domain in ('twitter.com', 'x.com', 'instagram.com', 'facebook.com', 'linkedin.com', 'tiktok.com'):
        for prefix in ('', 'https://', 'www.', 'https://www.'):
            ok = ok and any(n == 'profile url' for _i, n, _v in scan(prefix + domain + '/example_profile'))
    print('selftest: ok' if ok else 'selftest: FAILED %s %s' % (sorted(hd), scan(clean)))
    return 0 if ok else 1


def main(argv):
    args = argv[1:]
    if args == ['--selftest']:
        return selftest()
    allow = []
    try:
        if args[:1] == ['--allow']:
            with open(args[1], encoding='utf-8') as fh:
                allow = [l.strip() for l in fh if l.strip()]
            args = args[2:]
        if not args or any(a.startswith('-') for a in args):
            raise ValueError('give one or more files')
        texts = []
        for f in args:
            with open(f, encoding='utf-8') as fh:
                texts.append((f, fh.read()))
    except (IndexError, ValueError, OSError) as e:
        print('usage error: %s' % e)
        print(__doc__)
        return 2
    total = 0
    for f, t in texts:
        for i, n, v in scan(t, allow):
            total += 1
            print('FAIL %s:%d %s: %s' % (f, i, n, v))
    print('RESULT: %s' % ('%d identifier(s) found, redact and re-run' % total if total else 'CLEAN'))
    return 1 if total else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
