<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Ad Test Desk: Templates

Copy a template into the owner's chat, fill every field, then run the check named under it. Braces are the owner's facts, collected in chat. Leave [NEED] where a fact is missing; the checks fail on [NEED], so nothing half-filled moves on.

### 1. Test card (check: the fields check (test-card))
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

### 2. Discovery envelope
```
Target cost per result:
Break-even cost per result:
Maximum acceptable loss this cycle:
Cells funded (initial allocation, max top-up):
Evidence floor per cell:
Conversion lag assumption:
Replacement rule / expansion rule / stop rule:
Owner / review date / what happens to anything unresolved at expiry:
```

### 3. Verdict-readiness packet (check: the fields check (verdict-packet))
```
Scope:
Observation window:
Success gate:
Stop gate:
Evidence floor:
Allocation used:
Read quality:
Gate hit:
Unresolved evidence:
Remaining envelope:
Review date:
```

### 4. Naming code
`<concept number>_<angle>_<avatar>_<format>_<hook letter>_<version>`, for example `C03_proof_nightshift_vid_A_v1` (fictional).

### 5. Weekly report (one page) (check: the fields check (winner-read))
```
Week: {DATE} to {DATE}
Coverage: <campaigns, ads, merged copies>
Winners: <at or over the floor, inside target: ad, spend tier, cost per result>
Rumours: <under the floor: ad, spend tier, cost per result>
Spend leaks: ...
Re-hook list: ...
Delta: new / rising / falling / faded
Decodes: <winner>: keep / flex
Next rung briefs: 1. ... 2. ... 3. ...
Owner decisions needed: 1. ...
```

### 6. Learning log row
`| Date | Test # | Question | Variable | Read type | Gate hit | One-line lesson |`

### 7. One-page test retro
```
Test #: | Question:
Declared: variable / success gate / stop gate / read type
What happened against the gates:
First broken link: destination | hook | body | offer | none
Keep (3): | Cut (3): | Try (3):
Next test's question:
```

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
