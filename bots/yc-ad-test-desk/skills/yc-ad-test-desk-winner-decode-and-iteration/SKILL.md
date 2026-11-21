---
name: yc-ad-test-desk-winner-decode-and-iteration
description: "YC Ad Test Desk: use when the owner asks \"our best ad is tired\", \"get more like our winner\", weekly read of what's working; for decoding winners from ad-level numbers and writing variations and iterations. Not for designing a fresh test from scratch (test-design-and-reads)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: as in the description. WHEN NOT: designing a fresh test from scratch (test-design-and-reads).
# SKILL: winner-decode-and-iteration

Purpose: once ads have run at least one full week, turn the week's ad-level numbers into real winners, learn why they sell, and write next week's versions so each result teaches something; also when a winner is fading and needs its next rung. Spend decides how much you believe a return. Reading a designed test against its gates is yc-ad-test-desk-test-design-and-reads.

Inputs: ad-level results for the last full week, the week before and lifetime, pasted or exported by the owner (ad name, spend, results, cost per result, return if tracked); {TARGET_COST_PER_RESULT} or {BREAK_EVEN_RETURN}, and {WINNER_SPEND_FLOOR} (defaults: yc-ad-test-desk-references, "Testing math"); the naming code, so copies can be merged; ad files, or transcripts and stills, for the winners; brand pack (pasted by the owner, or from the companion YC Launch Ads template).

## Steps
1. **Coverage line:** dates, campaigns, ad count. Merge copies of the same ad across ad sets.
2. **Proof tiers:** sort by spend first. Tier each ad by spend (under the floor, at the floor, 3 x the floor and up) and band it by cost per result or return against break-even. Under the floor is a rumour, whatever its return. Four short tables: Winners (at or over the floor, inside target); Promising (under the floor, inside target: rumours); Spend leaks (over the floor, outside break-even); Re-hook list (strong hold or click after the open, weak first three seconds).
3. **Weekly delta:** this week against last, ad by ad and concept by concept: new, rising, falling, faded, crossed a tier.
4. **Storyboard each winner:** every spoken word and shot, with timecodes.
5. **Decode each winner:** why it sells (one paragraph pointing at moments in the video); keep and flex (keep: the few parts that make it work, each with proof from the ad; flex: everything free to change); copy slots (hook, problem, belief, proof, objection, offer, call to action) with the winner's line in each.
6. **Study losers too:** one line per big spend leak: which slot failed.
7. **Gap map:** angle by awareness grid; mark covered cells, empty cells and ladders in progress.
8. **Next rung:** each new version changes one flex part, in this order: hook, speaker, format, awareness level, a static version, a new angle.
9. **Variation or iteration?** A new hook, rewritten script, new first five seconds, font polish, or the same ad in a new ad set is a variation; label it so. An iteration keeps the keep-parts of a spend-proven winner and changes one meaningful thing.
10. **Winner matrix:** per winner: concept type, angle, avatar (a person with a problem), hook style, message, pain, dream outcome. Change one column, usually concept type or format; hold the rest.
11. **Words stay, picture changes:** when words and voice carry the sale and the picture wears out, keep the audio and rebuild the visuals two ways: the speaker cut out over fresh footage, or the winning story as large on-screen text over silent fresh footage. Check edges, safe zones and legibility before delivery.
12. **Brand check before briefs:** run the brand-pack check (yc-ad-test-desk-checks); a thin brand pack holds back the briefs only, not the numbers.
13. **Next week's briefs:** each next-rung line names the winner, its keep-parts, the one flex part to change and the proof it rests on. Full concept cards and briefs are written in the companion YC Launch Ads template (concept-spec, then reference-to-brief) when the owner has it installed; otherwise hand the owner these brief seeds as the output.
14. **Report** with the weekly report (template 5 in yc-ad-test-desk-references) and run the fields check (winner-read).

## Gate
The weekly report passes the fields check (winner-read). Every ad is tiered by spend before its return is discussed. No ad under {WINNER_SPEND_FLOOR} is called a winner. Every next-rung brief changes exactly one flex part and says which. Each "iteration" label rests on a spend-proven winner; otherwise it is relabeled "variation".

## Output
```
WEEK <dates> | ads <n> | merged copies <n>
WINNERS | PROMISING (rumours) | SPEND LEAKS | RE-HOOK
DELTA: new / rising / falling / faded
DECODE: <winner>: why, keep, flex, copy slots
GAP MAP: angle x awareness grid
NEXT RUNG: 1. <winner> -> change <flex part> -> brief #<n>
Next: brief seeds to the companion YC Launch Ads template (concept-spec), or to the owner
```
The owner's numbers stay in the owner's chat.

## If things go wrong
- **Nothing reached the spend floor:** say "no read this week", list the rumours and the spend each would need for a read. That is the owner's decision.
- **No naming code:** merge by matching creative text and thumbnail; ask the owner to adopt template 4.
- **Winner's files missing:** decode from transcript and stills; mark visual keep-parts "unconfirmed".
- **Everything is a spend leak:** check destination and tracking first. A broken page makes every ad look bad.
- **Round cap:** one decode per winner per week. If it fades again, move one step down the next-rung order.

## Never
Never invent results or fill missing weeks. Never pause, scale, duplicate or edit ads. Never call a variation an iteration. Never paste the owner's numbers outside their chat.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the brand-pack check: `python3 scripts/check_brand_pack.py <BRAND-PACK.md>`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-ad-test-desk-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
