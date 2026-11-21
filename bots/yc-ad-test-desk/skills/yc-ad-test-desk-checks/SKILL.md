---
name: yc-ad-test-desk-checks
description: "YC Ad Test Desk: use when the owner asks \"lint this\", check a test card or verdict packet, is this ready to launch; for the checks the steps apply (scripts plus written checklists): style, leak, fields, brand pack and launch preflight. Not for designing or reading a test (test-design-and-reads)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: as in the description. WHEN NOT: designing or reading a test (test-design-and-reads).
# YC Ad Test Desk: checks

In the repo edition every check below has a script in this bot's `scripts/` folder, named under its heading: run it from the bot folder and paste its PASS or FAIL line. Inside a Grok Bot template, which runs no code, use the written checklist instead. Every check named in the other skills ("the style check", "the fields check (test-card)" and so on) is one of the checks below. When you cannot run its script, apply it by hand, line by line, on the text in this chat, print each check as PASS or FAIL with the line that failed, and add "checked by hand". Never edit a draft only to make a check pass; fix the real problem or report it. Results: PASS, FAIL (each failing line and why) or CANNOT CHECK (input missing; ask the owner).

## Style check
Script: `python3 scripts/check_style.py <file or folder> [--banned FILE] [--exempt NAME ...]`
Run on every draft before the owner sees it.
1. No em dash or en dash anywhere. Use a full stop or a comma.
2. Banned words: none of these, in any form: leverage, seamless, seamlessly, robust, elevate, unlock, unlocks, delve, journey, game-changer, game changer, revolutionary, empower, supercharge, unleash, cutting-edge, next level, "in today's world", "in today's fast-paced", "look no further", "say goodbye to", "transform your", "we're excited to announce", "we are excited to announce".
3. None of the words on the owner's {BANNED_WORDS_FILE}, if pasted.
4. Banned words: no "it is not just X, it is Y" sentence.
5. Warn (do not fail) on any sentence over 30 words outside tables and headings.
A line that starts with "Banned words:" lists bans, not uses; skip it.

## Leak check
Script: `python3 scripts/check_leak.py <file or folder> [--terms FILE] [--exempt NAME ...]`
Run on every draft and on anything the owner may share or export. FAIL on:
1. A file path from a computer (a home folder, a workspace folder, a path starting with a tilde).
2. A social handle (an at-sign followed by a name).
3. A money amount written as a currency sign followed by digits that did not come from the owner's sourced facts in this chat.
4. An email address.
5. The name of an outside writer, creator, coach or paid course, unless the owner asked for a credited quote.
6. Any private word the owner listed (their company, product, people or customers) where the text will be shared outside the owner's chat.

## Fields check
Script: `python3 scripts/check_fields.py <kind> <filled file>`
A filled template is "Field: value" lines. FAIL when a required field is missing, empty, or says [NEED], TBD, TODO or "?". Rule words: numeric (holds a number or a placeholder the owner filled in chat); single (names one thing: no " and ", "+", "/" or ";"); min (the score reaches the minimum); choice (the first word is one of the listed words).
- test-card: Question, Test variable, Cells, Read type, Surface, Success gate, Stop gate, Evidence floor, Read window days, Max loss, Naming code, Log row, Owner yes. Test variable is single. Success gate, Stop gate, Evidence floor, Read window days and Max loss are numeric. Read type is CLEAN or BLENDED. Owner yes is PENDING or YES; only the owner ever changes it to YES. The bot always writes PENDING.
- verdict-packet: Scope, Observation window, Success gate, Stop gate, Evidence floor, Allocation used, Read quality, Gate hit, Unresolved evidence, Remaining envelope, Review date.
- winner-read (the T4 weekly winner read, template 5): Week, Coverage, Winners, Rumours, Spend leaks, Re-hook list, Delta, Decodes, Next rung briefs, Owner decisions needed. By hand also check the T4 gate: every ad in Winners, Rumours and Spend leaks shows its spend tier against {WINNER_SPEND_FLOOR} before any return figure; nothing under the floor sits in Winners; every Next rung line names the winner, its keep-parts, the one flex part it changes and the proof it rests on; every "iteration" label rests on a spend-proven winner, otherwise it says "variation".

## Brand-pack check
Script: `python3 scripts/check_brand_pack.py <BRAND-PACK.md>`
Seven sections: Offer, Never claims, Customer phrases, Avatars, Competitors, Voice, Thin spots. Lines holding [NEED], TBD or TODO never count.
Hard bar (any miss is FAIL, status THIN): (1) Offer holds a real offer line or "no offer" (otherwise scripts invent offers); (2) Never claims has 3 or more bullets; (3) Customer phrases has 10 or more bullets, each with "source:" on the same line.
Soft (WARN only): Avatars has 3 to 5 bullets; Competitors 3 or more; Voice has "Words we use" and "Words we never use".

## Launch preflight check
Use it only when the owner does not have the companion YC Launch Ads template, which runs the full preflight (claims-and-preflight Part B) with the claims review. Mark each item pass, should-fix or fix-before-launch.
- **A. Fix before launch:** no made-up specifics or unfilled placeholders; tracking intact (right destination, consistent campaign tags, the result event fires, offer and price on the asset match the page); specs valid (format, aspect, length, character limits, captions).
- **B. Test complete:** the test card passed the fields check (test-card), with "Owner yes: PENDING".
- **C. Offer:** offer, price and guarantee the same on ad, page and checkout.
Result: READY (all pass), READY WITH FIXES (only should-fix items) or FIX FIRST (any fix-before-launch item). Only READY or READY WITH FIXES goes to the owner for a yes. Always add: "Claims and message review not run here: no Red-claim or surface-policy check was done." Launch responsibility: owner. Nothing goes live without the owner's typed yes.

## Export check (only when the owner asks to export or copy a skill)
Script: `python3 scripts/check_credit.py <folder> [--exempt NAME ...]`
1. The first line of every exported skill is the dylan-pak-credit comment.
2. The last two lines are "Created and curated by Dylan Pak." and the license note.
3. The leak check passes on every exported file.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
