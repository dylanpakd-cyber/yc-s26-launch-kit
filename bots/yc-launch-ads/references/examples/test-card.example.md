<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
# Example test card (fictional, defaults labeled)

Question: Which opening line gets problem-aware parents to start the free week at the lowest cost?
Test variable: hook
Cells: 3 cuts, same body, hooks A, B, C
Read type: CLEAN
Surface: dedicated cold test cell, equal budgets per cut
Success gate: cost per free-week start at or under {TARGET_COST_PER_RESULT} after 3x target spent per cut (default)
Stop gate: 2x {TARGET_COST_PER_RESULT} spent on a cut with zero starts (default)
Evidence floor: 3x {TARGET_COST_PER_RESULT} per cut (default)
Read window days: 7 plus the owner's conversion lag
Max loss: {MAX_LOSS} stated by the owner in chat
Naming code: C01_failedfix_sundayplanner_vid_A_v1
Log row: added before launch, row 1
Owner yes: PENDING
Outcome bands: upgrade = under target after floor / ambiguous = between target and break-even or under floor / downgrade = over break-even after floor
What this cannot tell us: whether a static would beat video, or whether starts turn into paid plans

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
