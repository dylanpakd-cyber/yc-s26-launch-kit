---
name: yc-launch-ads-references
description: "YC Launch Ads: use when the owner asks \"show me an example\", a blank template, a worked example; for reference material: templates, the worked example, sizing math, claim lanes and the hook library. Not for doing the step itself (load that step's skill)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: as in the description. WHEN NOT: doing the step itself (load that step's skill).
# YC Launch Ads: references

Templates, the worked example and reference tables for the YC Launch Ads steps. Everything here is invented and labelled as an example, or is a method, not a result. Copy the shape, never the facts. Never present an example number as the owner's. Checks named here are written checklists in yc-launch-ads-checks, applied by hand.

## Worked example
One fictional product through the chain, to show "done" at each step. No real company, person, price or result. Product: a meal-plan app that keeps one shared weekly plan on every phone in a household. Offer: a free first week of shared plans. Price off the ad ({PRICE_RULE}: "price on the page only").
- **S:** sign-up-to-buyer is [NEED], so the bot sizes a message test only and says so.
- **0:** twelve support emails and fifteen reviews fill template 1. Never-claims: "saves money" (no data), "healthier meals" (health claim), "used by nutritionists" (no endorsement). Phrases like "the plan dies by Wednesday", each with "source: example review, {DATE}". Brand-pack check PASS.
- **1:** the page never answers "does my partner need to pay too" (objection list). Mechanism: "The plan lives where everyone in the house already looks, so nobody has to ask." Ladder row 1: "failed past solution: the notes-app plan".
- **2:** three rounds of "so what?" end at "the parent stops being the household's dinner help desk". Fields check (concept) PASS.
- **3 and 4:** fields check (brief) PASS; story body with "but" and "therefore" turns; hook check PASS on three hooks (one grader line computes to 7.4); harsh read six of six.
- **5:** facts-ledger PASS ("seven" is a word; "2 phones" and "7 dinners" are ledger rows). Honesty bar 5 of 5; the admission "not because I gave up" lands the claim harder. One Yellow ("plan once" holds only if no weekly re-entry) kept with the owner's confirmation.
- **6:** a 0.6 second black lead-in is a FAIL with timecode; trimmed; round two PASS.
- **7:** preflight READY WITH FIXES (UTM tag missing on cut C). The owner fixes it, types "yes, launch the test" and launches. The bot does not.
- **After 7:** the test design, read and winner decode for this example are in the companion YC Ad Test Desk template's worked example.

## Templates
Copy a template into the owner's chat, fill every field, then run the check named under it. Braces are the owner's facts, collected in chat. Leave [NEED] where a fact is missing; the checks fail on [NEED], so nothing half-filled moves on.

### 1. Brand pack (check: the brand-pack check)
```
# Brand pack: {PRODUCT}

## Offer
Offer today: {OFFER}
Price rule: {PRICE_RULE}
Guarantee, word for word: [NEED]
Ads link to: {CAMPAIGN_URL}

## Never claims
- [NEED]
- [NEED]
- [NEED]

## Customer phrases
Pain:
- "<exact words>" source: <where, {DATE}>
Desire:
- "<exact words>" source: <where, {DATE}>
Doubt:
- "<exact words>" source: <where, {DATE}>

## Avatars
- <name the moment, not the demographic>: trigger, failed fix, awareness, proof needed, two phrases

## Competitors
- <competitor>: long-running angle, what everyone says, what nobody says

## Voice
Words we use: ...
Words we never use: ...

## Thin spots
- ...
```

### 2. Concept card (check: the fields check (concept))
One "Field: value" line per concept field, in the order the fields check (concept) lists them. Awareness: unaware | problem-aware | solution-aware | product-aware | most-aware. Destination match: YES | NO.

### 3. Creative brief (check: the fields check (brief))
One "Field: value" line per brief field, in the order the fields check (brief) lists them.

### 4. Hooks file (check: the hook check)
```
<hook text> | score: q1 q2 q3 q4 q5 | claimed: PASS
<hook text> | score: q1 q2 q3 q4 q5 | grade: C1 C2 K1 K2 K3 K4 K5 K6 K7 K8 O1 O2 | claimed: PASS
```

### 5. Facts ledger (check: the facts-ledger check)
```
- <fact with its number> | source: <where it came from, {DATE}>
- <fact still unproven> [NEED]
```

### 6. Test card (check: the fields check (test-card))
Kept here so preflight (claims-and-preflight Part B) can check a pasted card. Designing the test is the companion YC Ad Test Desk's job.
```
Question:
Test variable:
Cells:
Read type: CLEAN | BLENDED
Surface:
Success gate:
Stop gate:
Evidence floor:
Read window days:
Max loss:
Naming code:
Log row:
Owner yes: PENDING
Outcome bands: upgrade ... / ambiguous ... / downgrade ...
What this cannot tell us:
```

Templates 7, 8 and 10 to 12 (discovery envelope, verdict-readiness packet, weekly report, learning log row, test retro) live in the companion YC Ad Test Desk template, which the owner may install.

### 9. Naming code
`<concept number>_<angle>_<avatar>_<format>_<hook letter>_<version>`, for example `C03_proof_nightshift_vid_A_v1` (fictional).

### 13. Research pack sections
Summary; own offer teardown (15 points); competitor teardowns; changes over time; customer phrases by pain, desire, doubt; proof ledger; ad library heat map; keep or flex per long runner; mechanism mine; avatars; concept ladder; hook bank; open questions.

## Claims lanes and policy
Posture: let the copy hit as hard as the truth allows, and say plainly where a line carries real risk. Flags, not lectures. The owner decides what ships.

### 1. Lanes
- **Green:** felt, local, specific, supportable, backed by a ledger row. Ships at full strength, no flag line.
- **Yellow:** usable with wording that carries its source or condition. One flag line with the strongest supported wording.
- **Owner-approved:** cleared by the owner with conditions (a dedicated page, a source list, no specific-metric promise). Flag when a condition is missing.
- **Red:** the loudest flag. Unsupportable outcome, health or money fear bait, fake or implied expert endorsement, regulated outcome, a current ban on the named surface.
Lanes are per product, read from the owner's {CLAIM_LOCKS}. Never invent a lane.

### 2. What is not a claim
A bold opinion in the seller's voice is register; only a specific presented as measured needs a receipt. A format choice (a chat-style frame, a notes-app look) is style; review the claims inside it.

### 3. Social signal is not proof
Reviews, comments, threads and survey answers are buyer language and objections, never evidence that a mechanism works or a result happened. A quoted customer is a testimonial only when it is a real quote the owner has permission to use.

### 4. Proof bank row
`claim or fact | value | evidence tier | source and date | market | lane | status (verified or expired) | usable as (hook, proof, FAQ)`
Evidence tiers, strongest first: owner's own measured data; third-party study about this product; documented customer result with permission; public category data; owner's statement. Expired rows (old counts, past offers) never ship.

### 5. Rewrite patterns that keep pressure
| Problem | Weak fix (do not) | Strong fix (do) |
|---|---|---|
| Unbacked number | Delete the line | Keep it with a named placeholder: "[your real count] people joined" |
| Outcome promise | Add "results may vary" | Describe the felt moment the buyer gets, which is Green |
| Fake urgency | Remove urgency entirely | The real reason to act now, or the cost of waiting, said as a moment |
| Implied expert | Soften to "experts say" | Show the mechanism working on screen |
| Health or money fear | Hedge it | Reframe to the everyday frustration the buyer named in their own words |

### 6. Likely rejection on a surface
Say "Likely rejected on <surface>", name the rule category, and give one alternative route: a different framing with the same pressure, a different proof, or a surface where it can run as written. Never silently soften. Never refuse without a route. Categories to check on paid social: personal attributes (implying you know the viewer's health, money or identity), before and after images, sensational or shocking content, health and wellness claims, financial outcomes, misleading buttons or fake system notices. Rules change: label every policy check with the date or "dated snapshot".

### 7. Honesty bar
The five checks live in yc-launch-ads-claims-and-preflight (Part A, step 6). All five, or the asset goes back.

## Hook and script library
Depth for yc-launch-ads-ad-script-and-hooks. Methods, not promises of results.

### 1. Script structures by awareness and length
| Awareness | 15 seconds | 30 seconds | 60 seconds |
|---|---|---|---|
| Unaware | Moment, problem named, product glimpse | Moment, problem, belief shift, proof, offer | Story with but and therefore turns, proof, objection, offer |
| Problem-aware | Problem callout, proof | Problem, failed fix, mechanism, proof, offer | Problem, failed fixes, mechanism demo, two proofs, objection, offer |
| Solution-aware | Contrast with old way, demo | Contrast, demo, proof, offer | Comparison without naming a brand, demo, proof stack, offer |
| Product-aware | Proof, offer | Objection first, proof, offer | Objection set, proof, guarantee, offer |
| Most-aware | Offer and action | Offer, reason now (only if real), action | Rarely needed |

### 2. The seven beats
Hook, problem, belief shift, proof, objection, offer, call to action. Use customer words where you can. Proof is never cut to save time. Body formats: yc-launch-ads-knowledge.

### 3. Voice targets for spoken scripts
- A quarter or more of sentences under eight words; some fragments of four words or fewer.
- At least one sentence over twenty words in a 30 second script, so it does not sound like a list.
- One in ten sentences or more starts with "and", "but" or "so".
- Contractions by default; one emphatic uncontracted pair is fine. No essay connectors (furthermore, additionally, moreover, consequently).
- Spoken pace about 2.5 words per second in English, slower for languages with longer words.
- No three sentences of the same length in a row.

### 4. Ranking passing hooks
The five-question score is in yc-launch-ads-ad-script-and-hooks (step 10); the arithmetic is the hook check. To order hooks that pass: benefit size, times relevance to this buyer, times believability, divided by the effort it seems to ask. Use it to order, never as a score you report as data.

### 5. The twelve-check video hook grader
| Code | Check | Weight |
|---|---|---|
| C1 | Context on mute within about two seconds: who, what, where | 2 |
| C2 | One specific curiosity gap about a topic already recognized, usually opened by contrast | 2 |
| K1 | Words, voice and picture say the same thing (mute pass, eyes-closed pass, sound-on pass) | 1 |
| K2 | Proof or stake right behind the claim, real numbers only | 1 |
| K3 | Contrast: old belief and new reality in one breath | 1 |
| K4 | A specific turn: a day, a decision, a user moment | 1 |
| K5 | Stakes for the speaker and desire for the viewer | 1 |
| K6 | The second line raises the stakes, not backstory | 1 |
| K7 | Proof is owned (founder or real user), not borrowed fame | 1 |
| K8 | Fingerprint: if any brand could say it, score low | 1 |
| O1 | Payoff honesty: the ad delivers what the hook promises | 1 |
| O2 | Format fit: opens inside a real moment, not a lecture | 1 |
Arithmetic, cap and PASS line: the hook check. Always add: "Rubric read, not a performance prediction." When context fights "no product in the hook": show the situation without a pitch in the first two seconds, then the product.

### 6. Idea gate for a whole video concept (0, 1 or 2 each)
Familiar format; no product in the hook; curiosity gap within two seconds; identity (the viewer sees who they want to be); a credential within two seconds; what the sharer gets to say; hook, problem, story, payoff in order; no dead space; captions on everything. The story beat and identity count double. A zero on the story beat, or on any of the first four, fails the concept.

### 7. Rewrite order for a failing hook
Use a strong existing visual if there is one. Put context and contrast in one or two spoken sentences. Let the visual finish the sentence. Add a short text hook. Make sure sound agrees. Pick a spoken structure only when it fits the facts: experiment, tutorial, reveal, case, problem and fix, contrarian, warning, comparison, question, list, ranking, scenario, proof, personal experience.

### 8. Delete-on-sight words
The banned list is the style check in yc-launch-ads-checks.

## Sizing math
All numbers are formulas or labeled starting defaults, never benchmarks or promises. Replace each default with the owner's own number after the first readable test. Print "(default)" beside any default you use. The full testing math (spend floor, stop gate, read window, leading indicators, outcome bands) is in the companion YC Ad Test Desk template.

### 0. Sizing step zero (before the brand pack)
Size from the owner's own funnel numbers, never anyone else's.
1. Launch goal: buyers or sign-ups wanted by {LAUNCH_DATE}.
2. The owner's own rates: page visit to sign-up, sign-up to buyer. No history: write [NEED] and size a message test only.
3. Results needed from ads = launch goal minus what other channels will bring (owner's estimate).
4. Spend range = results needed x target cost per result (low) to results needed x break-even cost per result (high).
5. Cells fundable = maximum loss ({MAX_LOSS}) / evidence floor (section 3).
Output, in the owner's chat only:
```
SIZING: goal <n> | from ads <n> | spend range <low> to <high> | cells fundable <n>
Inputs: <each with "owner" or [NEED]>
```

### 1. Break-even cost per result
Purchase campaign: break-even cost per purchase = money kept from one first order after product cost, fees, shipping and refunds. Ask the owner for price, product or delivery cost per order, payment and platform fees, average refund rate. Do the arithmetic in chat. Never assume margins.
Waitlist or sign-up campaign: break-even cost per sign-up = share of sign-ups expected to buy at launch x money kept per first order. No conversion history: do not invent one; ask the most they would pay for one sign-up and label it "owner ceiling".
{BREAK_EVEN_RETURN} for return-on-spend accounts = 1 / gross margin share. Invented example: a business that keeps half of each sale breaks even at a return of 2.0.

### 2. Target cost per result
Default: 70% of break-even, so the account keeps a margin for error. Label "(default)".

### 3. Evidence floor per cell
Default: 3 x target cost per result per cell: the cost of a readable answer, not a guarantee of one. Cells the envelope can fund = maximum loss / evidence floor, rounded down. Never open more.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
