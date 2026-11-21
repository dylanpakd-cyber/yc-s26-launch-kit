<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Ad Test Desk: Worked example

One fictional product, picking up where the creative work ends (the companion YC Launch Ads carries the earlier steps of the same example in `bots/yc-launch-ads/references/worked-example.md`). No real company, person, price or result. Product: a meal-plan app that keeps one shared weekly plan on every phone in a household. Offer: a free first week of shared plans. Three cuts (A, B, C) passed claims review and creative QA.

### S: sizing
The owner states a launch goal and their own page-to-sign-up rate. Sign-up-to-buyer is [NEED] (no history), so the test is sized as a message test only, and the card says so.

### T1: test design
See `references/examples/test-card.example.md`. One variable (the first three seconds); defaults labeled "(default)"; "Owner yes: PENDING". `python3 scripts/check_fields.py test-card references/examples/test-card.example.md` prints PASS.

### T2: preflight
READY WITH FIXES (UTM tag missing on cut C). The owner fixes the tag and types "yes, launch the test" in chat. The owner launches. The bot does not.

### T3: read
After the window, one cut crossed the evidence floor and hit the success gate. Two did not reach the floor. See `references/examples/verdict-packet.example.md` (`python3 scripts/check_fields.py verdict-packet references/examples/verdict-packet.example.md` PASS). The packet says: "Gate hit: success gate on cut A. Unresolved: whether starts become paid plans." No recommendation verbs. A one-page retro is filed. The owner decides to iterate on cut A.

### T4: decode
Keep: the confession open and the two-phone demo. Flex: speaker, format. Next rung: same words, new speaker. Labeled "iteration" because cut A is spend-proven. The weekly report is `references/examples/winner-read.example.md` (`python3 scripts/check_fields.py winner-read references/examples/winner-read.example.md` PASS).

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
