---
name: yc-customer-voice-objection-map
description: "YC Customer Voice: use when the owner asks \"why aren't people buying?\", what's holding them back, doubts; for mapping objections and honest answers. Not for describing who the buyer is (buyer-avatars)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "why aren't people buying?", what's holding them back, doubts; this skill covers mapping objections and honest answers. WHEN NOT: describing who the buyer is (buyer-avatars). One-off asks can load this skill directly; a full run reaches it through yc-customer-voice-workflow.
# SKILL: objection-map

Use when: the owner asks "why don't people buy", "map the objections", "objection list", "what stops them", "answer the objections", or the email, ad or copy bots need objection answers with proof. Run after the research document and avatars.

Purpose: find why people hesitate and what honestly answers each doubt, in five layers, ranked by how many people hold it, each with its evidence count and proof status.

Drafts only: internal map for the owner and the launch bots. Nothing is published without the owner's explicit yes.

## Inputs
- `research-doc` (Objections section) and `quote-bank`.
- `avatars`.
- Owner facts for proof: guarantee terms, demos, specs, real customer stories with permission.

## Steps
1. **Collect and rank.** List every objection from the bank with its count of independent people and its IDs. Rank by count. Every objection is tagged with where it came from: comment, call, review, survey, or "owner's guess" (which stays Tier C and is marked as a guess).
2. **Pick the top five** (or all, if fewer). For each build the five-layer stack (template in yc-customer-voice-references ("Templates")):
   - Layer 1, surface: the objection in their words, with an ID.
   - Layer 2, belief: what they must believe for that objection to make sense.
   - Layer 3, fear: what they are afraid will happen.
   - Layer 4, identity: what saying yes would say about them ("I'm the kind of person who needs an app to remember my own kids").
   - Layer 5, defuse: the honest proof or reframe that answers the deepest layer it can reach.
3. **One-line defusing statement** in plain words, aimed at the deepest layer the proof can honestly reach.
4. **Name the proof.** A fact, a demo, a guarantee term, a spec, a customer story with permission. Cite the source or bank ID. No proof yet: [NEED PROOF: what would prove it].
5. **What the answer does not claim.** One line. This protects the copy bots from stretching it.
6. **Map** each objection to the avatar who holds it most and the asset where it should be answered: ad, email, landing page FAQ, post, or onboarding.
7. **Honesty check.** Would the answer be fair if the buyer got exactly what it says? Remove guilt, manipulation and fake urgency. An objection with no honest answer is a product note for the owner, not copy.
8. **Run** the cards check (objection).

## Worked example (invented, every detail made up)
```
## Objection 1: the other parent won't use it
Objection: "my husband never checks it" (Q2)
Count: 5
Sources: Q2, Q9, F-02, R-07
Belief: any shared tool only works if both people open it
Fear: I'll pay for another thing that only I use
Identity: I'm the nagging one, again
Defuse: the reminder reaches the other parent as a plain text, no app needed
Proof: [NEED PROOF: a demo of the text reminder; owner to confirm the feature ships at launch]
Does not claim: that the other parent will act on it
Avatar: 1 (The Calendar Keeper)
Asset: email answer, landing page FAQ
```
This defuse reaches layer 2 (the belief) with a mechanism. It does not reach the identity layer; a real customer story with permission might.

## Gate (exit criteria)
- The cards check (objection) PASS: every field filled, Count is a number, Proof cites a source or says [NEED PROOF].
- Every defuse passes the honesty check.

## Failure handling
- No objections in the evidence: the evidence is thin. Ask the owner for replies, support tickets or refund reasons; mark guesses as guesses.
- The only answer is a promise the product cannot keep: write it as a product note for the owner and leave the copy answer [NEED PROOF].
- Revision cap: two rounds. Then show the failing stacks and stop.

## Rules
Never invent an objection or a count. Never write an answer that needs a fake deadline or guilt to work. Mark guesses as guesses.

## Output contract
`objections` with one stack per objection, ranked, plus a summary table in chat: objection, count, avatar, proof status, asset. Report: Done, Blocked, Next.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-customer-voice-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
