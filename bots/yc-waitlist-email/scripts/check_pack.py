#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""check_pack.py: hygiene check for a template pack folder.

Checks every .md and .py file under the folder:
  1. credit header on the first line (after a shebang for .py)
  2. credit footer as the last two non-empty lines
  3. no em dash or en dash in .md files
  4. each SKILL-*.md body is 600 to 1,800 words (credit lines excluded)
  5. each SKILL-*.md has a "Use when" line, a drafts-only line ("explicit yes")
     and a revision cap line ("Revision cap")

  6. with --source-dir: no run of 12 or more words copied from any source .md file
     (catches method text pasted instead of rewritten in fresh words)

Usage: python3 check_pack.py <pack-folder> [--source-dir DIR]
       python3 check_pack.py --selftest
Exit: 0 pass, 1 fail, 2 usage error.
"""
import os
import re
import sys
import tempfile

HEADER = ('<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file '
          '(including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->')
FOOT1 = 'Created and curated by Dylan Pak.'
FOOT2 = ('License note: free to use and adapt. If you copy, fork, or republish this file anywhere '
         '(including GitHub), keep the credit "Created and curated by Dylan Pak."')
DASHES = ('\u2014', '\u2013')


def check_file(path):
    errs = []
    with open(path, encoding='utf-8') as fh:
        lines = fh.read().splitlines()
    is_py = path.endswith('.py')
    body = [l for l in lines]
    if is_py:
        start = 1 if body and body[0].startswith('#!') else 0
        first = body[start] if len(body) > start else ''
        if first != '# ' + HEADER:
            errs.append('credit header missing on first line')
        tail = [l for l in body if l.strip()][-2:]
        if tail != ['# ' + FOOT1, '# ' + FOOT2]:
            errs.append('credit footer missing as last two lines')
    else:
        if not body or body[0] != HEADER:
            errs.append('credit header missing on first line')
        tail = [l.rstrip() for l in body if l.strip()][-2:]
        if tail != [FOOT1, FOOT2]:
            errs.append('credit footer missing as last two lines')
        text = '\n'.join(body)
        for d in DASHES:
            if d in text:
                n = [i + 1 for i, l in enumerate(body) if d in l]
                errs.append('dash character found on lines %s' % n[:10])
        name = os.path.basename(path)
        if name.startswith('SKILL-'):
            core = [l for l in body if l not in (HEADER, FOOT1, FOOT2) and l.strip() != '---']
            words = len(' '.join(core).split())
            if not 600 <= words <= 1800:
                errs.append('skill body is %d words, want 600 to 1,800' % words)
            low = text.lower()
            if 'use when' not in low:
                errs.append('no "Use when" line')
            if 'explicit yes' not in low:
                errs.append('no drafts-only line naming the owner\'s explicit yes')
            if 'revision cap' not in low:
                errs.append('no "Revision cap" line')
    return errs


SHINGLE = 12


def words_of(text):
    return re.findall(r"[a-z0-9']+", text.lower())


def source_shingles(src_dir):
    sh = set()
    for root, _d, files in os.walk(src_dir):
        for f in files:
            if f.endswith('.md'):
                with open(os.path.join(root, f), encoding='utf-8', errors='replace') as fh:
                    w = words_of(fh.read())
                sh.update(' '.join(w[i:i + SHINGLE]) for i in range(len(w) - SHINGLE + 1))
    return sh


def overlaps(text, sh):
    w = words_of(text)
    return [' '.join(w[i:i + SHINGLE]) for i in range(len(w) - SHINGLE + 1) if ' '.join(w[i:i + SHINGLE]) in sh]


def run(folder, src=None):
    if not os.path.isdir(folder):
        print('usage error: not a folder: %s' % folder)
        return 2
    bad = 0
    count = 0
    for root, _dirs, files in os.walk(folder):
        for f in sorted(files):
            if not (f.endswith('.md') or f.endswith('.py')):
                continue
            count += 1
            p = os.path.join(root, f)
            errs = check_file(p)
            if src is not None and f.endswith('.md'):
                with open(p, encoding='utf-8') as fh:
                    ov = overlaps(fh.read(), src)
                if ov:
                    errs.append('%d copied 12-word run(s), first: "%s"' % (len(ov), ov[0]))
            rel = os.path.relpath(p, folder)
            if errs:
                bad += 1
                for e in errs:
                    print('FAIL %s: %s' % (rel, e))
            else:
                print('PASS %s' % rel)
    print('checked %d files, %d failed' % (count, bad))
    return 1 if bad else 0


def selftest():
    good_md = '\n'.join([HEADER, '# x', 'text', '', '---', FOOT1, FOOT2, ''])
    words = ' '.join(['word'] * 700)
    good_skill = '\n'.join([HEADER, '# SKILL', 'Use when: a test.', 'Drafts only. Nothing goes out without the owner\'s explicit yes.',
                            'Revision cap: two rounds.', words, '---', FOOT1, FOOT2])
    good_py = '\n'.join(['#!/usr/bin/env python3', '# ' + HEADER, 'x = 1', '# ' + FOOT1, '# ' + FOOT2, ''])
    bad_md = '\n'.join(['# no header', 'a \u2014 b'])
    with tempfile.TemporaryDirectory() as d:
        for name, txt in (('A.md', good_md), ('SKILL-a.md', good_skill), ('a.py', good_py)):
            with open(os.path.join(d, name), 'w', encoding='utf-8') as fh:
                fh.write(txt)
        ok = check_file(os.path.join(d, 'A.md')) == [] and check_file(os.path.join(d, 'SKILL-a.md')) == [] \
            and check_file(os.path.join(d, 'a.py')) == []
        with open(os.path.join(d, 'B.md'), 'w', encoding='utf-8') as fh:
            fh.write(bad_md)
        errs = check_file(os.path.join(d, 'B.md'))
        ok = ok and len(errs) == 3
        with open(os.path.join(d, 'SKILL-short.md'), 'w', encoding='utf-8') as fh:
            fh.write('\n'.join([HEADER, 'short', FOOT1, FOOT2]))
        ok = ok and any('words' in e for e in check_file(os.path.join(d, 'SKILL-short.md')))
        src_dir = os.path.join(d, 'src')
        os.mkdir(src_dir)
        with open(os.path.join(src_dir, 'lesson.md'), 'w', encoding='utf-8') as fh:
            fh.write('a deadline counts only if the checkout really stops the offer at that exact time and the email says so')
        sh = source_shingles(src_dir)
        ok = ok and overlaps('note: a deadline counts only if the checkout really stops the offer at that exact time today', sh)
        ok = ok and not overlaps('Confirm the exact cutoff is set in the checkout before a time limit appears.', sh)
    print('selftest: ok' if ok else 'selftest: FAILED')
    return 0 if ok else 1


def main(argv):
    if len(argv) == 2 and argv[1] == '--selftest':
        return selftest()
    src = None
    if len(argv) == 4 and argv[2] == '--source-dir':
        if not os.path.isdir(argv[3]):
            print('usage error: not a folder: %s' % argv[3])
            return 2
        src = source_shingles(argv[3])
    elif len(argv) != 2:
        print(__doc__)
        return 2
    if argv[1].startswith('-'):
        print(__doc__)
        return 2
    return run(argv[1], src)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
