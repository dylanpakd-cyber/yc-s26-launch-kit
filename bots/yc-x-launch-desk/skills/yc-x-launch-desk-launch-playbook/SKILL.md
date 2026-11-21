---
name: yc-x-launch-desk-launch-playbook
description: "YC X Launch Desk: use when the owner asks \"plan our launch\", the 48-hour timeline, checklist, GO/NO-GO gates, the T-12h check; for the launch brief, timeline and the eight gates computed at T-12h. Not for writing the founder post (founder-post-and-video-script)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "plan our launch", the 48-hour timeline, checklist, GO/NO-GO gates, the T-12h check; this skill covers the launch brief, timeline and the eight gates computed at T-12h. WHEN NOT: writing the founder post (founder-post-and-video-script). One-off asks can load this skill directly; a full run reaches it through yc-x-launch-desk-workflow.
# SKILL: launch-playbook

Purpose: the spine of the launch. Part A writes the one-page brief and pressure-tests the angle. Part B runs the 48-hour clock. Part C runs the eight GO / NO-GO gates at T-12h with a script, so the verdict is computed, not felt.

## Use when
- A founder wants to launch on X and has a date, or wants help picking one.
- The owner says "plan my launch", "launch brief", "angle", "so what", "48-hour plan", "launch checklist", "GO/NO-GO", "eight gates", "are we ready to launch", "offer note".
- Every launch starts here.

Not for: daily X research or posting on the owner's behalf.

## Inputs
Ask one at a time, save each as a memory:
1. T0: date, minute and {LAUNCH_TZ}.
2. {LAUNCH_OWNER}. Default: the founder.
3. {KPI} and a target number. Default KPI: sign-ups or orders on {CAMPAIGN_URL} counted at T+24h. The target has no default.
4. {CAMPAIGN_URL} and what its first screen says.
5. {OFFER} and {PRICE_RULE}.
6. Replies owner and a backup.
7. {QUIET_WINDOW_HOURS}. Default: 3 hours before and 6 after.
8. {LINEUP_SOURCE} and whether the owner has a network. This sets the path: LINEUP or NO-NETWORK.
9. {BANNED_WORDS_FILE}.

## Steps: Part A, brief and angle (T-48h)
1. **Facts ledger.** Every number and named fact with "source:" or [NEED]. Run the facts-ledger check.
2. **Market card.** Fill it before thinking about features (see yc-x-launch-desk-knowledge, "The claim"). Print `market card: PASS` only when every field is filled from the owner's facts or public sources. Otherwise `FAIL (<field>)`.
3. **Angle sheet.** Five angles: category stance, named incident, contrarian truth, demonstration, number. For each: the "so what?" test (what is at stake for a stranger), the proof it needs, who will disagree and why. Pick one. Keep the rest for the second beat and the backlog.
4. **Offer note.** What the buyer gets, what it costs per {PRICE_RULE}, the guarantee wording, and the plain reason to act now, only if real.
5. **Ranking check.** Re-read the ranking hypotheses in yc-x-launch-desk-knowledge against current public X documentation. Note any that changed. Write the date in the brief's "Ranking claims re-checked on" field.
6. **One-page brief.** Fill the brief template in yc-x-launch-desk-references ("Templates"). Run the fields check (brief).
7. **Missing list** and the next three actions, each with an owner and a time.

## Steps: Part B, the 48-hour clock
- T-48h: brief, angle, owner, KPI. Start the post draft and the people plan in parallel.
- T-36h: quote and note drafts out for the owner's review.
- T-24h: harsh-read gate (yc-x-launch-desk-test-of-300). On pass, freeze the post. Any later change goes back through the gate.
- T-12h: eight gates (Part C).
- T-1h: final destination and tracking check on a phone. Remind the owner of the quiet window.
- T0: the owner posts. The desk delivers only the run sheet.
- T+1d: replies and repost list. T+3d: retro.
Every item has one owner and a time. Overdue items lead the next report.

## Steps: Part C, eight gates (T-12h)
1. Write the gates file from yc-x-launch-desk-references ("Templates"). One line per gate with PASS, RISK or FAIL:
   - G1 destination loads on a phone; offer and price match the post.
   - G2 tracking and the KPI count work (a test result was logged).
   - G3 the post is frozen after the harsh read.
   - G4 the people plan is logged (lineup log passes, or the no-network plan is written).
   - G5 every quote or note draft was approved by the owner, or the person wrote their own.
   - G6 the quiet window is agreed.
   - G7 replies owner and backup are named and will be online.
   - G8 the rollback plan is written (what the owner does if the page or offer breaks mid-launch).
2. PASS needs "evidence:". RISK needs "accepted: yes" from the owner. FAIL needs "owner:" and "deadline:".
3. Run the gates check (`scripts/check_gates.py`). It prints the verdict: GO, GO WITH RISKS, or NO-GO.

## Gate
- Part A: The fields check (brief) passes and the market card prints PASS.
- Part C: The gates check (`scripts/check_gates.py`) passes. Any FAIL, or any RISK the owner has not accepted, is NO-GO.

## Output
```
LAUNCH BRIEF: <filled template>
ANGLE SHEET: 1 to 5, chosen: <n>
OFFER NOTE: ...
CLOCK: T-48h ... T+3d, each with owner and time
GATES (T-12h): G1 PASS ... G8 PASS | VERDICT: GO
Next: <step>
```

## If things go wrong
- **No KPI the owner can count.** Stop. Offer three countable options (sign-ups, orders, qualified replies) and ask the owner to pick one and a target.
- **No T0.** Offer two slots the owner can make, both outside their other posting. The owner picks.
- **NO-GO at T-12h.** Name the blocker, owner and deadline. If it cannot clear by T-1h, recommend moving T0 and draft the move note for the owner.
- **The owner wants to skip the gates.** Show the failing gate once and what it risks. The owner decides. Log it.
- **Round cap.** Two passes of the angle sheet. Then the owner picks from the best three.

## Never
- Never post, schedule or change any account setting.
- Never soften a failed gate.
- Never set the KPI target for the owner.
- Never invent a deadline or cap to create urgency.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the facts-ledger check: `python3 scripts/check_facts_ledger.py <draft file> <ledger file>`; the fields check: `python3 scripts/check_fields.py <kind> <filled file>`; the gates check: `python3 scripts/check_gates.py <gates file>`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-x-launch-desk-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
