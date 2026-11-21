---
name: yc-ad-test-desk-test-design-and-reads
description: "YC Ad Test Desk: use when the owner asks \"how should we test this?\", \"is this test result real?\", budget split for a test; for designing a test card with gates set before spend, then reading the result into a verdict packet. Not for decoding an existing winner (winner-decode-and-iteration)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: as in the description. WHEN NOT: decoding an existing winner (winner-decode-and-iteration).
# SKILL: test-design-and-reads

Part 1 designs the test before any spend (chain step T1). Part 2 reads the result into a verdict packet (chain step T3). The bot reports evidence; the owner approves, launches and decides what lives, dies or scales. The bot never sets "Owner yes".

## Part 1: test design
A test is a question with a budget attached. If you cannot write the question, the one variable, the success gate and the stop gate first, it is spend with a diary.

Use when assets passed claims (Part A) and creative QA, the owner asks what to test next, how much to spend to learn, or for a test plan or card, or names one uncertainty ("does the pain angle beat the proof angle?").

Inputs: passing concept cards and QA-passed assets (from the companion YC Launch Ads template or the owner's own); the owner's economics or the labeled defaults in yc-ad-test-desk-references ("Testing math"): break-even cost per result, {TARGET_COST_PER_RESULT}, {WINNER_SPEND_FLOOR}; the most the owner will lose on learning this cycle (ask, never assume); {AD_PLATFORM}, account structure in the owner's words, naming code.

### Steps
1. **Restate the uncertainty** in one sentence, in the owner's words.
2. **List two to four ways to reduce it,** including one with no ad spend (ask ten buyers, a landing-page headline test). Compare on what you would learn, how much it matters, cost, time, how easy it is to undo and evidence strength. Pick one.
3. **One variable** per concept cell. Ten ads testing everything test nothing.
4. **Set the gates now** from the owner's numbers or the defaults (Testing math sections 4 and 5): success gate (the result that justifies iteration; default cost per result at or below target after the spend floor), stop gate (ends the test without debate), evidence floor per cell (what a readable answer costs). Gates written after seeing results are storytelling.
5. **Precommit outcome bands** (upgrade, ambiguous, downgrade), each with an observable count or rate, never "good".
6. **Clean or blended read.** Clean: a dedicated cell, protected budget, no winners in the pool; costs more, can be trusted. Blended: new ads in a working library; cheaper, and the answer is "what delivery picked", not a comparison. Write which one you are buying.
7. **Launch surface:** working library, test cell, sandbox or sibling set, in the owner's account terms. If a working library hits its target, test beside it, not inside it.
8. **Statics: force the spend** (one concept per ad set with equal budgets, or a cell big enough for every ad to reach its floor), or accept the delivery-weighted read and say so on the card.
9. **Discovery envelope** (template 2 in yc-ad-test-desk-references). If it can fund four readable answers, do not open twelve questions.
10. **Design out mid-flight edits.** Editing targeting or structure mid-test resets learning and splits the history.
11. **Fill the test card** (template 1) and run the fields check (test-card). By hand: cells x evidence floor is at or under the envelope; if not, cut cells.
12. **Hand to preflight:** the companion YC Launch Ads template runs it (claims-and-preflight Part B) when the owner has it installed; otherwise run the launch preflight check in yc-ad-test-desk-checks here and say the claims and message review was not run. Then to the owner for a typed yes.

Gate: the fields check (test-card) passes, with "Owner yes: PENDING".
Output: the filled test card headed `TEST CARD #<n>`.

### If things go wrong
- **No economics:** use the default derivation (Testing math) with the owner's price and margin. If they will not share them, run a message test on leading indicators only and write "purchase direction unresolved" in advance.
- **Envelope too small for one clean cell:** say so; offer a blended read or a no-spend test.
- **Five things at once:** split into one-variable cells, rank them, fund the top ones the envelope affords.
- **Round cap:** two drafts of the card, then the owner decides with the open fields shown.

## Part 2: test reads and verdicts
Use when a test hit a gate, used its allocation or reached its read window, the owner asks whether a test won, for a weekly account read or to grade top and bottom ads, or a test ran past its window unread (a zombie test).

Inputs: the test card with gates written before launch; ad-level numbers the owner pastes or exports (spend, results, cost per result, clicks, thumb-stop and hold for video, initiated checkouts or sign-ups; the bot does not log into the ad account); the owner's own count of real sales or sign-ups; dates of any live edits.

### Steps
1. **Check the read is due:** a gate, the allocation or the window. Not because a day looked bad or a new idea arrived. Platform numbers restate for a day or two; never conclude on today's read of today.
2. **Coverage line:** dates, cells, ad count, total spend, edits and their dates. Split any history at an edit date.
3. **Read in order, always:** spend allocation (what delivery chose to buy), then business truth (the owner's real results and costs), then platform diagnostics.
4. **Compare to the gates as written.** Which gate was hit, and when. Never move a gate.
5. **Read quality:** clean or blended; forced or delivery-weighted; contaminants (a winner in the pool, a page change, a price change).
6. **Early image and static tests:** judge on leading indicators that fit the spend (Testing math section 7). Upper-funnel wins in a pocket that never bought do not prove purchase: write "purchase direction unresolved".
7. **Great clicks, no results:** check message match on the page, then traffic quality, then the offer, before blaming the creative.
8. **Cheap-format results** prove the variable only in that format. A richer format of the same idea is a new test with better odds, not a proven transfer.
9. **Weekly account read:** grade top-spend and bottom-spend ads WORKING, SOFT or BROKEN against {TARGET_COST_PER_RESULT} and name the leak (hook, body or page). An ad that spent 4 x target with no results is a red flag for the owner.
10. **Package the verdict packet** (template 3) headed `VERDICT-READINESS PACKET: TEST #<n>`, plus a learning log row (template 6). Run the fields check (verdict-packet).
11. **One-page retro** after each test (template 7). Facts only; opinions marked.

Gate: the fields check (verdict-packet) passes, with gates as declared at launch. The packet holds no recommendation verbs (scale, kill, pause); those are the owner's call. The owner's numbers stay in the owner's chat.

### If things go wrong
- **Gates never written:** say "no pre-set gates, this is not a test read". Report observation only, and write gates for the next run.
- **Too little spend:** "No read" is a valid, first-class result. Say what a read would cost.
- **Owner wants to call it early:** show where it stands against the gates and name the risk. The owner decides.
- **Data does not add up** (platform results far above the owner's count): trust the owner's count; flag tracking for preflight.
- **Round cap:** one read per test per window. Re-reading the same data with new gates is not allowed.

## Never
- Never launch, pause, scale, set budgets or edit campaigns.
- Never set or move gates after results arrive.
- Never call zero spend a loss, or a single failed execution a dead concept.
- Never fill "Owner yes" with YES yourself.
- Never copy the owner's numbers outside their chat.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the fields check: `python3 scripts/check_fields.py <kind> <filled file>`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-ad-test-desk-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
