---
name: yc-launch-ads-checks
description: "YC Launch Ads: use when the owner asks \"lint this\", check a draft for banned words, dashes or unsourced numbers, does the brand pack meet the bar; for the checks the steps apply (scripts plus written checklists): style, leak, hooks, facts ledger, fields and brand pack. Not for deciding whether a claim is allowed (claims-and-preflight)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: as in the description. WHEN NOT: deciding whether a claim is allowed (claims-and-preflight).
# YC Launch Ads: checks

In the repo edition every check below has a script in this bot's `scripts/` folder, named under its heading: run it from the bot folder and paste its PASS or FAIL line. Inside a Grok Bot template, which runs no code, use the written checklist instead. Every check named in the other skills ("the style check", "the brand-pack check" and so on) is one of the checks below. When you cannot run its script, apply it by hand, line by line, on the text in this chat, print each check as PASS or FAIL with the line that failed, and add "checked by hand". Never edit a draft only to make a check pass; fix the real problem or report it. Results: PASS, FAIL (each failing line and why) or CANNOT CHECK (input missing; ask the owner).

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

## Hook check
Script: `python3 scripts/check_hooks.py <hooks file> [--max-chars 130]`
One hook per line: the hook text, then optional gate answers, five scores and twelve grades.
1. Length: fits in 130 characters (the feed cut before "Show more").
2. No em or en dash.
3. Gate: every gate answer is Y; until all are Y the verdict is KILL.
4. Five-question score (questions in yc-launch-ads-ad-script-and-hooks step 10), each 1 to 5. PASS when every score is 3 or more, the first is 4 or more, and the average is 4.0 or more.
5. Weighted grade (video hooks; checks C1 C2 K1 to K8 O1 O2 defined in yc-launch-ads-references, "Hook and script library" 5), each 0 to 10. Weighted average = (2 x C1 + 2 x C2 + the other ten) / 14. If C1 or C2 is 3 or less, cap at 5.0. PASS at 7.0 or more.
6. A verdict written on the line must match the arithmetic. Show the arithmetic.

## Facts-ledger check
Script: `python3 scripts/check_facts_ledger.py <draft file> <ledger file>`
The ledger is one fact per line: "- <fact> | source: <where it came from>"; a row with no source yet is marked [NEED].
1. Every row has a source or is marked [NEED].
2. Every number, percent, money figure, multiplier and date in the draft matches a sourced row. Placeholders in braces, such as {PRICE}, are skipped.
3. A draft figure that only matches a [NEED] row fails.
4. A draft line that still holds [NEED] fails: it is not ready to ship.

## Fields check
Script: `python3 scripts/check_fields.py <kind> <filled file>`
A filled template is "Field: value" lines. FAIL when a required field is missing, empty, or says [NEED], TBD, TODO or "?". Rule words: numeric (holds a number or a placeholder the owner filled in chat); single (names one thing: no " and ", "+", "/" or ";"); min (the score reaches the minimum); choice (the first word is one of the listed words).
- concept: Persona sentence, Angle sentence, Offer sentence, Hook promise sentence, Persona, Angle, Offer, Proof path, Format, Surface, Test variable, Awareness, Mechanism, Destination promise, Destination match. Test variable is single. Awareness is one of unaware, problem-aware, solution-aware, product-aware, most-aware. Destination match must be YES.
- brief: Concept, Format, Length seconds, Avatar, Awareness, Hook A, Hook B, Hook C, Body format, Proof, Objection handled, Offer, CTA, Destination, Claim sources, Money gates. Length seconds is numeric.
- test-card: Question, Test variable, Cells, Read type, Surface, Success gate, Stop gate, Evidence floor, Read window days, Max loss, Naming code, Log row, Owner yes. Test variable is single. Success gate, Stop gate, Evidence floor, Read window days and Max loss are numeric. Read type is CLEAN or BLENDED. Owner yes is PENDING or YES; only the owner ever changes it to YES. The bot always writes PENDING.

## Brand-pack check
Script: `python3 scripts/check_brand_pack.py <BRAND-PACK.md>`
Seven sections: Offer, Never claims, Customer phrases, Avatars, Competitors, Voice, Thin spots. Lines holding [NEED], TBD or TODO never count.
Hard bar (any miss is FAIL, status THIN): (1) Offer holds a real offer line or "no offer" (otherwise scripts invent offers); (2) Never claims has 3 or more bullets; (3) Customer phrases has 10 or more bullets, each with "source:" on the same line.
Soft (WARN only): Avatars has 3 to 5 bullets; Competitors 3 or more; Voice has "Words we use" and "Words we never use".

## Export check (only when the owner asks to export or copy a skill)
Script: `python3 scripts/check_credit.py <folder> [--exempt NAME ...]`
1. The first line of every exported skill is the dylan-pak-credit comment.
2. The last two lines are "Created and curated by Dylan Pak." and the license note.
3. The leak check passes on every exported file.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
