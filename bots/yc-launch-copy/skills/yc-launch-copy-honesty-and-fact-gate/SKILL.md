---
name: yc-launch-copy-honesty-and-fact-gate
description: "YC Launch Copy: use when the owner asks \"is this true?\", fact-check, can I say this; for checking a draft for invented facts, metrics and over-claims. Not for editing style (line-edit-and-rhythm)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "is this true?", fact-check, can I say this; this skill covers checking a draft for invented facts, metrics and over-claims. WHEN NOT: editing style (line-edit-and-rhythm). One-off asks can load this skill directly; a full run reaches it through yc-launch-copy-workflow.
# SKILL: honesty-and-fact-gate

Purpose: nothing leaves the desk with a claim the owner cannot defend in the replies. Every number in the draft must be in the facts ledger with a source. Every claim gets a lane. The draft gets a 1 to 5 score with a mechanical ship rule.

## Use when
- After line edit, before any hand-off, on every version including adapted ones.
- The owner says "fact check", "can I say this", "is this true", "where's the proof", "check claims", "score this draft".
- A room reply or outside draft enters the chain.

## Inputs
- The edited draft and its channel.
- The facts ledger.
- Claim locks and {BANNED_WORDS_FILE}.
- The pinpoint card.

## Steps
1. **List every claim** in the draft verbatim: numbers, results, comparisons, quotes, named facts, time frames, "first", "only", "best".
2. **Run the ledger check.** Apply the facts-ledger check. Every number, percent, money figure and date must match a sourced ledger row. Open [NEED] marks fail.
3. **Lane each claim:**
   - Green: backed by a ledger row.
   - Yellow: true only under a condition. Add a "true only if" note, and put the condition in the wording.
   - Red: cannot be supported, health or money fear bait, implied endorsement, regulated outcome.
4. **Rewrite Yellow and Red** to the strongest honest version that keeps force, or name the proof that would make it Green. Never weaken a claim you can prove.
5. **Honesty bar, all five yes:**
   1. Facts true today and checkable.
   2. No fake scarcity or deadline.
   3. No promise bigger than the real offer.
   4. One honest damaging admission where it fits naturally (never faked).
   5. Fair if the reader got exactly what was said.
6. **Banned tactics:** invented testimonials, fake timers, false "last chance", posts that pretend to be unpaid when they are paid, guilt, naming a competitor without evidence.
7. **Platform check.** If a claim touches a regulated area or a platform rule, label the check "dated snapshot" and recommend the owner check the current rule.
8. **Draft score.** Score clarity, specificity, voice, honesty and payoff with the rubric in yc-launch-copy-knowledge. Write the reason for the lowest score. Fill the draft-score template and run the fields check (draft-score).
9. **Verdict:** PASS, FIX (list) or HOLD (the owner must decide).

## Gate
- The facts-ledger check passes.
- No Red claims.
- Honesty bar 5 of 5.
- The fields check (draft-score) passes: clarity, specificity, voice and payoff 4 or more; honesty 5.

## Output
```
VERDICT: PASS | FIX | HOLD
Flags:
"<quoted line>" | lane | rewrite or source needed
Ledger check: PASS | <failing tokens>
Honesty bar: 5/5
Draft score: clarity 5, specificity 4, voice 4, honesty 5, payoff 4 | lowest: ... because ...
Next: hand-off (numbered options, one recommendation), or back to step 4 or 5
```
Green claims get no line.

## If things go wrong
- **A number fails the ledger check.** Ask the owner for the source, or replace it with [NEED: what] and send it back to line edit. Never guess.
- **The owner insists on a Red claim.** State once what could happen (a public correction, a platform flag, legal risk) and offer the strongest honest rewrite. The owner decides. Log it.
- **Score 3 on voice twice.** The voice rules are thin. Ask for more samples.
- **The room or an outside draft added facts.** Treat each as unsourced until the owner confirms it. Flag it with the quoted phrase and what would source it.
- **A claim is true but old** (a past count, an ended offer). Mark it expired in the ledger and ask for the current figure. Expired rows never ship.
- **Round cap.** Two rounds back to drafting or editing. Then HOLD with the open flags and let the owner choose.

## Never
- Never pass a number that is not in the ledger.
- Never invent customers, quotes or results.
- Never add timid hedging to an honest line.
- Never publish. The owner posts by hand.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the facts-ledger check: `python3 scripts/check_facts_ledger.py <draft file> <ledger file>`; the fields check: `python3 scripts/check_fields.py <kind> <filled file>`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-launch-copy-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
