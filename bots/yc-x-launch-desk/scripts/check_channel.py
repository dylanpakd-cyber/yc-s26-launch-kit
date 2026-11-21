#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""Channel gate for drafts: X length, link position, and one idea per post.

Usage:
  python3 check_channel.py <x|linkedin> <draft file>
  python3 check_channel.py --selftest

Draft file layout: metadata lines first, then a blank line, then the post body.
  Idea: <the one idea, one sentence>
  Link placement: in post | reply | first comment | none
For an X thread, split posts with a line holding only "---".

Rules (all mechanical):
  idea      an "Idea:" line exists and is one sentence (one end mark, no ";").
  one idea  the body has no add-on openers ("also,", "one more thing", "p.s.", "ps:", "bonus:", "oh and").
  x length  each post is 280 characters or fewer. A link counts as 23 characters, as X shortens links.
  x link    "in post": the link appears once, in the first post. "reply" or "none": no link in the body.
  linkedin  the first two lines fit in 210 characters (before the fold). "Link placement" must be
            "first comment" or "none", and the body holds no link.
A link is any http(s) address or the {CAMPAIGN_URL} placeholder.
Exit: 0 pass, 1 fail, 2 usage error.
"""
import re
import sys
import tempfile
from pathlib import Path

LINK = re.compile(r"https?://\S+|\{CAMPAIGN_URL\}")
ADDON = re.compile(r"^\s*(also,|one more thing|p\.?s\.?[:\s]|bonus:|oh and\b)", re.I | re.M)


def split(text):
    lines = [l for l in text.splitlines() if not l.startswith(("<!-- dylan-pak-credit", "Created and curated by Dylan Pak",
                                                                "License note: free to use"))]
    meta, body, in_body = {}, [], False
    for l in lines:
        if not in_body:
            m = re.match(r"^(Idea|Link placement)\s*:\s*(.*)$", l.strip(), re.I)
            if m:
                meta[m.group(1).lower()] = m.group(2).strip()
                continue
            if not l.strip() and meta:
                in_body = True
            continue
        body.append(l)
    while body and body[-1].strip() in ("", "---"):
        body.pop()
    return meta, "\n".join(body).strip()


def x_len(post):
    return len(LINK.sub("x" * 23, post))


def check(platform, text):
    meta, body = split(text)
    fails = []
    idea = meta.get("idea", "")
    if not idea:
        fails.append("missing 'Idea:' line")
    elif len(re.findall(r"[.!?](\s|$)", idea)) > 1 or ";" in idea:
        fails.append("Idea line holds more than one sentence")
    if not body:
        fails.append("no post body after the metadata and a blank line")
    if ADDON.search(body):
        fails.append("add-on opener found (also, one more thing, P.S., bonus): one idea per post")
    place = meta.get("link placement", "").lower()
    if place not in ("in post", "reply", "first comment", "none"):
        fails.append("Link placement must be: in post, reply, first comment or none")
    links = LINK.findall(body)
    if platform == "x":
        posts = [p.strip() for p in re.split(r"^\s*---\s*$", body, flags=re.M) if p.strip()]
        for i, p in enumerate(posts, 1):
            n = x_len(p)
            if n > 280:
                fails.append(f"post {i} is {n} characters, over 280")
        if place == "in post":
            if len(links) != 1:
                fails.append(f"'in post' needs exactly one link, found {len(links)}")
            elif posts and not LINK.search(posts[0]):
                fails.append("the link must sit in the first post")
        elif place in ("reply", "none", "first comment") and links:
            fails.append("link found in the body but placement says it is not in the post")
    elif platform == "linkedin":
        first_two = " ".join([l for l in body.splitlines() if l.strip()][:2])
        if len(first_two) > 210:
            fails.append(f"first two lines are {len(first_two)} characters, over 210 (the fold)")
        if place not in ("first comment", "none"):
            fails.append("LinkedIn link placement must be 'first comment' or 'none'")
        if links:
            fails.append("LinkedIn body holds a link; move it to the first comment")
    return fails


def run(platform, path):
    fails = check(platform, Path(path).read_text(encoding="utf-8"))
    for f in fails:
        print("FAIL  " + f)
    print(f"PASS  {platform} channel gate" if not fails else f"\n{len(fails)} problems")
    return 1 if fails else 0


def selftest():
    good_x = "Idea: Clinics lose bookings after six.\nLink placement: in post\n\nWe missed calls after six. Fix: {CAMPAIGN_URL}\n"
    assert check("x", good_x) == []
    assert check("x", good_x.replace("Fix:", "a" * 300))
    assert check("x", good_x.replace("in post", "reply"))
    assert check("x", good_x + "\nAlso, we hired.\n")
    assert check("x", good_x.replace("Idea: Clinics lose bookings after six.", "Idea: One. Two."))
    thread = "Idea: One point.\nLink placement: in post\n\nPost one {CAMPAIGN_URL}\n---\nPost two\n"
    assert check("x", thread) == []
    late = "Idea: One point.\nLink placement: in post\n\nPost one\n---\nPost two {CAMPAIGN_URL}\n"
    assert check("x", late)
    li = "Idea: One point.\nLink placement: first comment\n\nShort first line.\nSecond line.\n\nBody.\n"
    assert check("linkedin", li) == []
    assert check("linkedin", li.replace("Body.", "Body https://example.com"))
    with tempfile.TemporaryDirectory() as d:
        p = Path(d, "x.md")
        p.write_text(good_x)
        assert run("x", p) == 0
    print("SELFTEST PASS")
    return 0


def main(argv):
    if argv[1:2] == ["--selftest"]:
        return selftest()
    if len(argv) != 3 or argv[1] not in ("x", "linkedin") or not Path(argv[2]).is_file():
        print(__doc__)
        return 2
    return run(argv[1], argv[2])


if __name__ == "__main__":
    sys.exit(main(sys.argv))

# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
