---
name: yc-launch-ads-concept-spec
description: "YC Launch Ads: use when the owner asks \"turn this idea into a concept\", what exactly are we testing, persona, angle and offer for one idea; for locking one idea into a concept card (insight lock, four sentences, one test variable) before any brief. Not for turning a reference ad into a brief (reference-to-brief) or writing hooks (ad-script-and-hooks)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "turn this idea into a concept", what exactly are we testing, persona, angle and offer for one idea; this skill covers locking one idea into a concept card (insight lock, four sentences, one test variable) before any brief. WHEN NOT: turning a reference ad into a brief (reference-to-brief) or writing hooks (ad-script-and-hooks). One-off asks can load this skill directly; a full run reaches it through yc-launch-ads-workflow.
# SKILL: concept-spec

Purpose: turn a ladder idea into a concept card that can be tested and read. It locks the customer insight into true statements first, then writes four falsifiable sentences and the seven-field concept cell. If the card cannot be filled, the idea is backlog, not a brief.

## Use when
- After the concept ladder exists, for each idea you plan to brief.
- The owner says "is this idea ready", "spec this concept", "lock the insight", "what are we actually testing".
- A batch of ads looks different but may test the same thing.
- Before any spend on a new idea.

Not for: writing the script (yc-launch-ads-ad-script-and-hooks) or choosing the budget (the companion YC Ad Test Desk, which the owner may install).

## Inputs
- One row from the concept ladder.
- brand pack: avatars, customer phrases, never-claims, offer.
- The proof ledger from mining.
- {CAMPAIGN_URL} and what that page promises in its first screen.

## Steps
1. **Insight-to-truth lock.** Fill six lines, in order, each from customer words in the brand pack. Do not move to the next line until the current one is true and specific.
   - People: who gets the most value, one thing they believe, one thing you can see about them.
   - Position: why this and not the old way, said as a mechanism, not as "we are better".
   - Promise: who they become. Ask "so what?" of the answer until it stops changing. Keep the result personal and concrete.
   - Proof: only what the owner can show (demo, owned testimonial, real number in the ledger).
   - Priority: the cost of doing nothing, as a moment the buyer knows. Use soft or deadline language only when it is real.
   - Process: how it works, in the buyer's words.
2. **Empathy check.** From customer words only: what the buyer is doing, what frustrates them, what good looks like, what bad looks like. If any of the four has no source, mark it [NEED] and say which avatar is thin.
3. **Four sentences.** Write each as a full sentence that could be proven wrong by a test.
   - Persona sentence: this is for a buyer who recognizes a specific trigger, has a specific failed fix or belief, and needs specific proof before buying.
   - Angle sentence: the ad argues one belief shift, contradiction, problem, proof or comparison for that buyer.
   - Offer sentence: the offer frames the product, value or risk reversal as the reason this buyer acts now.
   - Hook promise sentence: the first three seconds promise specific relevance through picture, sound or words, without bait and without an abrupt pitch.
4. **Seven-field concept cell.** Persona, angle, offer, proof path, format, surface (cold, warm, retargeting, test cell), test variable. Format is chosen last, to serve the concept.
5. **One variable.** Name the single thing this launch is built to learn. If two things changed, it is two concepts.
6. **Awareness.** Pick one level. Cold and low-awareness concepts open on a concrete fact, proof or contrast.
7. **Destination match.** Write the page's first-screen promise next to the hook promise sentence. They must say the same thing. If not, the fix is the page or the concept, not a better hook.
8. **Distinctness check.** Compare against existing cards. A concept is new only if persona, angle or offer changed. A new background, face or font is the same concept.
9. **Fill the card** from yc-launch-ads-references ("Templates") and run the fields check (concept).

## Gate
The fields check (concept) passes. That requires all four sentences, all seven cell fields, a mechanism line, an awareness level from the allowed list, one test variable (no "and", "+", "/" or ";"), and "Destination match: YES".

Also by hand: every proof line exists in the ledger, and each sentence is specific enough that a result could prove it wrong.

## Output
One concept card per idea, numbered, in the owner's chat:
```
CONCEPT 1: <angle in one line>
Persona sentence: ...
Angle sentence: ...
Offer sentence: ...
Hook promise sentence: ...
Persona: ... | Angle: ... | Offer: ... | Proof path: ... | Format: ... | Surface: ... | Test variable: ...
Awareness: ... | Mechanism: ... | Destination promise: ... | Destination match: YES
Status: READY FOR BRIEF | BACKLOG (reason)
```
Backlog ideas go to a list at the end with the missing field named.

## If things go wrong
- **Cannot write the persona sentence.** The avatar is thin. Go back to the brand pack for that buyer, or pick a ladder row with more customer words.
- **Destination match is NO.** Stop. Tell the owner the page and the ad promise different things, and give two options: change the page headline (owner's job) or change the concept to fit the page.
- **The "so what?" drill never settles.** Use the third answer and mark the promise "tentative". Test it as the variable.
- **Proof path is empty.** The concept can only run as a message test (statics, leading indicators). Say so on the card.
- **Round cap.** Two rewrites per card. Still failing: backlog it with the reason.

## Never
- Never fill a field with a guess to pass the check.
- Never write a medical, money or legal outcome as a promise.
- Never call a cosmetic change a new concept.
- Never send a card to a brief without a passing check.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-launch-ads-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
