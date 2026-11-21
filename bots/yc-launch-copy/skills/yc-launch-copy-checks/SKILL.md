---
name: yc-launch-copy-checks
description: "YC Launch Copy: use when the owner asks \"lint this\", check a draft for banned words, dashes, X length or link placement; for the written hand checks the steps apply: style, leak, hooks, facts ledger, channel and fields. Not for judging whether a claim is true (honesty-and-fact-gate)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "lint this", check a draft for banned words, dashes, X length or link placement; this skill covers the written hand checks the steps apply: style, leak, hooks, facts ledger, channel and fields. WHEN NOT: judging whether a claim is true (honesty-and-fact-gate). One-off asks can load this skill directly; a full run reaches it through yc-launch-copy-workflow.
# YC Launch Copy: hand checks

This bot has no scripts and runs no code. Every check named in the other skills ("the style check", "the channel check" and so on) is one of the written checklists below. Apply it by hand, line by line, on the text in this chat. Then print each check as PASS or FAIL with the line that failed, and add the words "checked by hand" to the result. Never edit a draft only to make a check pass; fix the real problem or report it.

Every check gives one of three results: PASS, FAIL (list each failing line and why), or CANNOT CHECK (the input is missing; ask the owner for it).

## Style check
Run on every draft before the owner sees it.
1. No em dash or en dash anywhere. Use a full stop or a comma.
2. None of these words or phrases, in any form: leverage, seamless, seamlessly, robust, elevate, unlock, unlocks, delve, game-changer, game changer, revolutionary, empower, supercharge, unleash, cutting-edge, next level, "in today's world", "in today's fast-paced", "look no further", "say goodbye to", "transform your", "we're excited to announce", "we are excited to announce".
3. None of the words on the owner's own list in {BANNED_WORDS_FILE}, if the owner pasted one.
4. No "it is not just X, it is Y" sentence.
5. Warn (do not fail) on any sentence over 30 words outside tables and headings.
A line that starts with "Banned words:" is a list of bans, not a use, so skip it.

## Leak check
Run on every draft and on anything the owner may share or export. FAIL on any of these:
1. A file path from a computer (a home folder, a workspace folder, a path starting with a tilde).
2. A social handle (an at-sign followed by a name).
3. A money amount written as a currency sign followed by digits that did not come from the owner's sourced facts in this chat.
4. An email address.
5. The name of an outside writer, creator, coach or paid course, unless the owner asked for a credited quote.
6. Any private word the owner listed (their company, product, people or customers) appearing where the text will be shared outside the owner's chat.

## Hook check
One hook per line. Fields: the hook text, then optional gate answers, five scores and twelve grades.
1. Length: the hook fits in 130 characters (the feed cut before "Show more").
2. No em or en dash.
3. Gate: every gate answer is Y. Until all are Y the verdict is KILL.
4. Five-question score, each 1 to 5. PASS when every score is 3 or more, the first is 4 or more, and the average is 4.0 or more.
5. Weighted grade (video hooks), twelve checks C1 C2 K1 to K8 O1 O2, each 0 to 10. Weighted average = (2 x C1 + 2 x C2 + the other ten) / 14. If C1 or C2 is 3 or less, cap the result at 5.0. PASS at 7.0 or more.
6. If a verdict is written on the line, it must match the arithmetic. Show the arithmetic.

## Facts-ledger check
The ledger is one fact per line: "- <fact> | source: <where it came from>". A row with no source yet is marked [NEED].
1. Every ledger row has a source or is marked [NEED].
2. Every number, percent, money figure, multiplier and date in the draft matches a sourced ledger row. Placeholders in braces, such as {PRICE}, are skipped.
3. A draft figure that only matches a [NEED] row fails.
4. A draft line that still holds [NEED] fails: it is not ready to ship.

## Channel check
Each X or LinkedIn draft starts with two lines, "Idea:" (one sentence) and "Link placement:" (in post, reply, first comment or none), then a blank line, then the post. Split thread posts with a line holding only "---".
1. An "Idea:" line exists and is one sentence (one end mark, no semicolon).
2. One idea: no add-on openers such as "also,", "one more thing", "P.S.", "bonus:", "oh and".
3. X: each post is 280 characters or fewer. A link counts as 23 characters.
4. X link: "in post" means exactly one link, in the first post. "reply" or "none" means no link in the body.
5. LinkedIn: the first two lines fit in 210 characters (the fold). Link placement is "first comment" or "none", and the body holds no link.
A link is any web address or {CAMPAIGN_URL}.

## Fields check
A filled template is a list of "Field: value" lines. FAIL when a required field is missing, empty, or still says [NEED], TBD, TODO or "?". Rule words:
- numeric: the value holds a number or a placeholder the owner filled in chat.
- single: the value names one thing (no " and ", "+", "/" or ";").
- min: the score reaches the minimum.
- choice: the first word is one of the listed words.

### Fields check kinds
- pinpoint: Pinpoint, Reader, Problem, Benefit, Emotion, Action, Stranger test, Two-year test, Proof 1, Proof 2. Stranger test and Two-year test must be YES.
- outline: Pinpoint, Promise, Opening, Beat 1, Beat 2, Beat 3, Turn, Action, Teach before pitch. Teach before pitch is YES or N/A.
- draft-score: Channel, Pinpoint, Clarity, Specificity, Voice, Honesty, Payoff. Minimums: Clarity 4, Specificity 4, Voice 4, Honesty 5, Payoff 4.
- room-log: Room, Prompt, Reply, Owner approved sharing, Fact flags. Owner approved sharing must be YES. With no yes there is no room run: the work is done in-house and labelled "run in-house".

## Export check (only when the owner asks to export or copy a skill)
1. The first line of every exported skill is the dylan-pak-credit comment.
2. The last two lines are "Created and curated by Dylan Pak." and the license note.
3. The leak check passes on every exported file.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
