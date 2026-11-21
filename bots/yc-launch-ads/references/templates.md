<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Launch Ads: Templates

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

### 7. Naming code
`<concept number>_<angle>_<avatar>_<format>_<hook letter>_<version>`, for example `C03_proof_nightshift_vid_A_v1` (fictional).

### 8. Research pack sections
Summary; own offer teardown (15 points); competitor teardowns; changes over time; customer phrases by pain, desire, doubt; proof ledger; ad library heat map; keep or flex per long runner; mechanism mine; avatars; concept ladder; hook bank; open questions.


Test design, the discovery envelope, verdict-readiness packets, weekly reports, the learning log and test retros are templates of the companion YC Ad Test Desk (`bots/yc-ad-test-desk/references/templates.md`).

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
