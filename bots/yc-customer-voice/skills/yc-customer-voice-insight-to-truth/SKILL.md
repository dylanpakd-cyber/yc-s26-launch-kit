---
name: yc-customer-voice-insight-to-truth
description: "YC Customer Voice: use when the owner asks \"turn this insight into what we can say\", locked statements before copy; for the six locked statements before any copy is written. Not for writing the copy itself (this desk writes no ads)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "turn this insight into what we can say", locked statements before copy; this skill covers the six locked statements before any copy is written. WHEN NOT: writing the copy itself (this desk writes no ads). One-off asks can load this skill directly; a full run reaches it through yc-customer-voice-workflow.
# SKILL: insight-to-truth

Use when: avatars and objections exist and the owner asks to "lock the six", "insight to truth", "find the angle", "what is the true message", "pressure test this angle", or a copy, ad, email or X bot needs a brief. Run last, once per avatar and objection pair. It writes locks, not copy.

Purpose: turn customer insight into six locked statements before any hook, body or call to action is written by another bot. This stops clever copy that is not true. The locks open every brief the launch bots receive.

Drafts only: lock pages are internal. This bot writes no hooks, bodies, scripts or ads. Nothing is handed off or published without the owner's explicit yes.

## Inputs
- One avatar card and one objection stack.
- `quote-bank` and the brand sheet (for proof and never-claims).

## The six locks
1. **People:** exactly who this message is for (the avatar, their situation, the beliefs inside them and the cues you could see from outside) and who it is not for.
2. **Empathy:** what they feel and say, in their words, as a four-part map, each part from the bank:
   - Doing: what they do today about the problem.
   - Frustrations: what annoys them about it.
   - Heaven (best day): what life looks like when it works.
   - Hell (worst day): what it looks like when it fails.
   Plus one sourced quote (Tier A or B ID).
3. **Positioning:** what this product is, set against the alternatives they actually use, and how it works in buyer words. A plain mechanism read, not us-versus-them theatre. Use the owner's product noun; do not rename the category.
4. **Promise:** the one outcome, stated so a stranger could check it. Run the "so what" drill: write the feature, ask "so what?", write the answer, ask again, until the answer is who they get to be or what they get back. Keep the last answer that is still true.
5. **Proof:** the evidence that makes the promise believable: facts, demos, terms, specs, customer words with permission. Whose proof it is, and its source.
6. **Priority:** the single thing the message must do first (stop the scroll, remove one doubt, show the product). Name the cost of doing nothing in the avatar's words. Real dates only if real.

## Steps
1. **Select the pair:** one avatar, one objection. One lock page per pair.
2. **Fill the six locks**, each with a source ID or [NEED: what]. Template in yc-customer-voice-references ("Templates").
3. **Find the angle.** From the locks, write three directional angles in one line each (an angle is a way of seeing the problem, not a headline). Tie each to IDs.
4. **Angle pressure test.** For each angle ask:
   - Is it true for this avatar, from Tier A or B evidence?
   - Is it specific to this product, or could a competitor say it unchanged?
   - Does it pass the necessity test (why this, not the free option)?
   - Does it survive the objection, or walk into it?
   - Would a stranger understand it at about a third-grade reading level, without baby talk?
   Keep the angles that pass all five. Mark the rest "failed: reason".
5. **True-information test.** Read the six locks as one paragraph. Would the owner stand behind every word in front of a customer? Cut anything they would not.
6. **Honesty pre-check** (all five must be clear):
   - Every fact checkable and true today.
   - No scarcity or deadline that is not real.
   - No promise bigger than what the product does today.
   - One honest admission, true and slightly costly, that makes the main claim land harder. Never fake one.
   - If a buyer got exactly what this says, would their complaint be fair? If yes, rewrite.
   Write "Honesty check: PASS" only when all five are clear.
7. **Run** the cards check (locks).
8. **Hand off.** With the owner's yes, the locks open every brief to the copy, ads, email and X bots, followed by the quote pack for that desk (Tier A and B rows with Use "copy", redacted, with IDs).

## Worked example (invented, every detail made up)
```
## Lock page 1: Calendar Keeper x "the other parent won't use it"
People: the parent who carries the family schedule alone, solution aware
Not for: families who already share one calendar that both open daily
Empathy: Q2
Doing: copies school messages into a shared calendar at night (Q7)
Frustrations: the other parent never opens it (Q2)
Heaven: both parents know about the bake sale the night before (Q10)
Hell: learning about it at 8am the same day (Q1)
Positioning: a family planner that texts the reminder to the other parent, so nobody needs to open an app
How it works: forward the school message; the planner sends both parents a plain text the night before
Promise: both parents hear about school events the night before
So what: nobody gets caught at 8am, and you stop being the reminder
Proof: Q1, Q2; text reminder demo from the owner
Priority: remove the "only I will use it" doubt first
Honesty check: PASS
```
Angles: "You stop being the family's reminder" (passes); "Never miss anything again" (failed: over-promise, not checkable).

## Gate (exit criteria)
- The cards check (locks) PASS: every lock filled, no [NEED], an empathy ID at Tier A or B, Honesty check PASS.
- At least one angle passed the pressure test, or the page says "no angle passed" with reasons.

## Failure handling
- A lock is [NEED]: stop. Go back to research for that lock or ask the owner. Do not hand off.
- No angle passes: report it. That is a real finding; the launch should not proceed on that pair.
- The owner wants a claim the proof cannot support: offer the strongest true version and flag it.
- Revision cap: two rounds per lock page. Then show the open locks and stop.

## Rules
All six locked before any other bot drafts. No invented proof. No scarcity that is not real. No hooks, bodies or calls to action written here.

## Output contract
`locks`, one page per pair, plus `handoff`: per desk (ads, email, copy, X) the lock page, the passing angles, and the quote pack. In chat: pairs locked, angles passed, open locks. Report: Done, Blocked, Next.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the cards check: `python3 scripts/check_cards.py --kind KIND [--bank BANK.md] FILE`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-customer-voice-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
