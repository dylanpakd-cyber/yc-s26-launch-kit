---
name: yc-x-launch-desk-retro-and-angles
description: "YC X Launch Desk: use when the owner asks \"we launched, what did we learn?\", retro, what's next; for the T+3d retro and the next-angle backlog. Not for the live window (wave-and-replies)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "we launched, what did we learn?", retro, what's next; this skill covers the T+3d retro and the next-angle backlog. WHEN NOT: the live window (wave-and-replies). One-off asks can load this skill directly; a full run reaches it through yc-x-launch-desk-workflow.
# SKILL: retro-and-angles

Purpose: turn the launch into learning and a backlog of better angles. Runs at T+3d, after the KPI was counted. A one-page retro, one learning log row, and five ranked next angles. Facts only. Opinions are marked as opinions.

## Use when
- T+3d after a launch, or any time the owner says "retro", "what worked", "post-mortem", "did the launch work", "learning log", "what next", "angle backlog", "next launch".
- Before planning the next launch, to read past log rows.

## Inputs
- The brief with the KPI target written at step 1.
- The KPI count at T+24h and at T+3d, from the owner's own dashboard.
- What the owner reports from post analytics: impressions, profile visits, link clicks, replies, quotes, reposts, video watch time if any.
- The run sheet notes, the lineup log, the reply list, the second beat decision.
- Past learning log rows.

## Steps
1. **KPI against plan.** The target written at step 1 versus what was counted at T+24h and T+3d. HIT (at or over target), PARTIAL (above half of target), or MISSED. Write the numbers in the owner's chat only.
2. **Read the diagnosis in order.** Stop at the first broken link and say so:
   1. Destination and tracking: did the page load, keep the post's promise, and count correctly?
   2. First line and first five seconds: did people stop? Use the owner's numbers (for example clicks on "Show more" or video holds) where they exist.
   3. The claim: did comments argue with the idea, or ask what it was? Confusion means a context gap.
   4. The people plan: who quoted, whose audience responded, who did nothing, what the two-minute check missed.
   5. Timing and the quiet window: did anything else compete?
3. **The first 300.** What did the early viewers do: stop, watch, comment, leave? Evidence is the owner's own reading of analytics. Mark guesses as opinions.
4. **Lines that travelled.** Which sentences were quoted or repeated, by whom (described, not named in shared files). These become future first lines.
5. **People.** Who moved it, who did not. One lesson for the next lineup.
6. **What broke.** Destination, tracking, replies, timing, gates that passed but should not have.
7. **Gate review.** For each of the eight gates: did its PASS hold up on launch day? A gate that passed and still broke gets a stricter check next time.
8. **Keep, cut, try.** Three of each, specific enough to act on.
9. **Verdict.** Did the launch do the job it was designed for? Views are context, not the verdict.
10. **Learning log row.** One row: date, angle, first line, format, path (LINEUP or NO-NETWORK), KPI target, KPI result band, one lesson.
11. **Angle backlog.** From unused first lines and angles, the replies, the questions people asked, and lines that travelled, propose five next angles. Each with the "so what?" test, the proof it needs, and how many real people asked. Rank by that count.
12. **Fill the retro template** (yc-x-launch-desk-references ("Templates")) and run the fields check (retro).

## Gate
- The fields check (retro) passes: KPI planned, KPI counted, when counted, first 300, lines that travelled, people who moved it, what broke, keep, cut, try, verdict (HIT, PARTIAL or MISSED), log row.
- The diagnosis checked the destination before the creative.
- Every number in the retro is the owner's, with when it was counted.

## Output
```
RETRO: <launch> | T+3d
KPI: target <n> | counted <n> at T+24h, <n> at T+3d | VERDICT: HIT | PARTIAL | MISSED
First broken link: <destination | first line | claim | people | timing | none>
First 300: ...
Lines that travelled: ...
People who moved it: ...
What broke: ...
Gate review: G1 held ... G8 held
Keep: 1. 2. 3. | Cut: 1. 2. 3. | Try: 1. 2. 3.
LEARNING LOG ROW: | date | angle | first line | format | path | target | band | lesson |
ANGLE BACKLOG (ranked): 1. <angle> | so what: ... | proof: ... | asked by: <count>
```

## If things go wrong
- **KPI not counted yet.** Wait up to 24 hours. Then run the retro with "KPI counted: [NEED]" and a reminder. The fields check fails until it is filled. That is on purpose.
- **Owner has no analytics access.** Use what is visible on the post (replies, quotes) and mark the first-300 section "visible signals only".
- **The launch missed and the owner blames the post.** Walk the diagnosis order first. Most misses break at the destination or the claim.
- **No past log rows.** This is row one. Say so.
- **Round cap.** One retro per launch. Corrections are added as a dated note, not a rewrite.

## Never
- Never judge the launch by views alone.
- Never invent numbers or fill a missing count.
- Never copy the owner's numbers or people's names into a shared or public file.
- Never blame the creative before checking the destination.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the fields check: `python3 scripts/check_fields.py <kind> <filled file>`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-x-launch-desk-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
