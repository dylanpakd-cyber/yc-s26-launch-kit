<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Launch Ads: Hook and script library

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

### 5. The five-question hook score
1. Callout or open loop? 2. Would the buyer say it to a friend? 3. Would a stranger understand it? 4. Free of insider words? 5. Concrete enough to picture?
Each 1 to 5. PASS: every score 3 or more, question one 4 or more, average 4.0 or more. `scripts/check_hooks.py` computes it from the "score:" field on each hook line.
Heuristic for ranking passing hooks: how big the benefit is, times how relevant it is to this buyer, times how believable it is, divided by how much effort it seems to ask. Use it to order hooks, never as a score you report as data.

### 6. The twelve-check video hook grader
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

### 7. Idea gate for a whole video concept (0, 1 or 2 each)
Familiar format; no product in the hook; curiosity gap within two seconds; identity (the viewer sees who they want to be); a credential within two seconds; what the sharer gets to say; hook, problem, story, payoff in order; no dead space; captions on everything. The story beat and identity count double. A zero on the story beat, or on any of the first four, fails the concept.

### 8. Rewrite order for a failing hook
Use a strong existing visual if there is one. Put context and contrast in one or two spoken sentences. Let the visual finish the sentence. Add a short text hook. Make sure sound agrees. Pick a spoken structure only when it fits the facts: experiment, tutorial, reveal, case, problem and fix, contrarian, warning, comparison, question, list, ranking, scenario, proof, personal experience.

### 9. Delete-on-sight words
The banned list is the style check in yc-launch-ads-checks.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
