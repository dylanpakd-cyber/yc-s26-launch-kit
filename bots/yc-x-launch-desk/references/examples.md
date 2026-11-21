<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC X Launch Desk: Examples (invented)

### Brief example

### Example brief (fictional product, invented for illustration)

Product: a browser add-on that turns any recipe page into a shopping list in one click
Buyer: home cooks who plan the week's meals on Sunday and shop on Monday
Claim: Recipe sites were built for ads, not for cooking. One click strips a recipe to the list you need.
Proof: demo of a long recipe page becoming a 9-item list in under 3 seconds
Offer: free add-on; paid sync plan later, price on the page only
Destination: {CAMPAIGN_URL}
KPI: installs counted from the add-on store dashboard
KPI target: 150 installs by T+24h, set by the owner
Counted from: owner's add-on store dashboard at T+24h
T0: {LAUNCH_DATE} 09:30
Time zone: {LAUNCH_TZ}
Launch owner: {FOUNDER}
Replies owner: {FOUNDER}
Backup: a cofounder or friend named by the owner in chat
Quiet window hours: 3 before, 6 after (default)
Network path: LINEUP
Ranking claims re-checked on: {DATE}, against the current public X help pages

### Freeze example

### Example freeze record (fictional scores from a Test of 300 run)

Scroll stop: 8
Comprehension: 9
Comment trigger: 7
Quotability: 8
Owner accepts risk: no
Frozen at: T-24h

### Gates example

### Example gates file at T-12h (fictional)

G1: PASS | store page loads on a phone, free offer matches the post | evidence: owner checked on two phones
G2: PASS | test install shows in the dashboard | evidence: owner logged one test install
G3: PASS | post frozen after harsh read | evidence: freeze record, all four signals 7 or more
G4: PASS | lineup logged | evidence: `scripts/check_lineup_log.py` PASS
G5: RISK | two quote drafts still waiting on owner review | owner: {FOUNDER} | accepted: yes
G6: PASS | quiet window agreed | evidence: owner confirmed in chat
G7: PASS | replies owner and backup named | evidence: both confirmed online
G8: PASS | rollback plan written | evidence: reply with mirror link drafted
Verdict: GO WITH RISKS

### Hooks example

```
# Example first line (fictional)
Recipe sites were built for ads. Not for cooking. | score: 4 5 5 5 4 | claimed: PASS
```

### Ledger example

### Example facts ledger (fictional)

- recipe page to a 9-item list in under 3 seconds | source: example demo recording, {DATE}
- 150 installs target by T+24h | source: owner's written target in the brief, {DATE}

### Lineup 30 example

### Example lineup log, 34 rows, 30 in the lineup (fictional placeholders, not real accounts; scores invented)

Rows 7, 15 and 23 failed the two-minute check and are skipped. Row 27 is stale and on watch.

| Account | Fit | Reach | Relationship | Last ten checked | Check result | Decision | Draft | Status |
|---|---|---|---|---|---|---|---|---|
| [Account 1] | 3 | 1 | friend | {DATE} | pass | core | the list showed up before the ads finished loading | drafted |
| [Account 2] | 2 | 0 | replied | {DATE} | pass | core | creator wrote own (2) | creator wrote own |
| [Account 3] | 2 | 1 | cold | {DATE} | pass | core | I timed it on a stew recipe and it was faster than scrolling | drafted |
| [Account 4] | 3 | 3 | cold | {DATE} | pass | core | recipes read like instructions again | approved by owner |
| [Account 5] | 2 | 3 | cold | {DATE} | pass | core | creator wrote own (5) | creator wrote own |
| [Account 6] | 2 | 1 | cold | {DATE} | pass | core | creator wrote own (6) | creator wrote own |
| [Account 7] | 3 | 0 | seen | {DATE} | fail | skip | n/a | skipped |
| [Account 8] | 2 | 1 | replied | {DATE} | pass | core | this fixes the worst part of cooking from a website | approved by owner |
| [Account 9] | 2 | 0 | replied | {DATE} | pass | core | creator wrote own (9) | creator wrote own |
| [Account 10] | 2 | 0 | seen | {DATE} | pass | core | one click and my Monday shop list was done | approved by owner |
| [Account 11] | 2 | 0 | cold | {DATE} | pass | core | creator wrote own (11) | creator wrote own |
| [Account 12] | 2 | 3 | friend | {DATE} | pass | core | I stopped screenshotting ingredient lists | approved by owner |
| [Account 13] | 3 | 3 | replied | {DATE} | pass | core | finally a tool that cuts the life story out of recipes | approved by owner |
| [Account 14] | 2 | 1 | seen | {DATE} | pass | core | my partner used it without asking me how | drafted |
| [Account 15] | 3 | 3 | replied | {DATE} | fail | skip | n/a | skipped |
| [Account 16] | 3 | 2 | cold | {DATE} | pass | core | good for anyone who meal-preps on Sunday | drafted |
| [Account 17] | 3 | 1 | replied | {DATE} | pass | core | the shopping list is the only part of a recipe page I need | approved by owner |
| [Account 18] | 3 | 3 | cold | {DATE} | pass | core | tried it on three sites and it held up | drafted |
| [Account 19] | 3 | 2 | replied | {DATE} | pass | core | creator wrote own (19) | creator wrote own |
| [Account 20] | 3 | 3 | cold | {DATE} | pass | core | this is what recipe sites should have shipped years ago | drafted |
| [Account 21] | 3 | 3 | cold | {DATE} | pass | bench | small tool, big relief on a weeknight | drafted |
| [Account 22] | 3 | 3 | replied | {DATE} | pass | bench | the demo is the whole pitch and it works | approved by owner |
| [Account 23] | 3 | 0 | friend | {DATE} | fail | skip | n/a | skipped |
| [Account 24] | 3 | 1 | cold | {DATE} | pass | bench | I cook more when the list is ready | approved by owner |
| [Account 25] | 2 | 1 | replied | {DATE} | pass | bench | less scrolling, more cooking, that is the trade | approved by owner |
| [Account 26] | 2 | 3 | friend | {DATE} | pass | bench | quick win for anyone who batch cooks | approved by owner |
| [Account 27] | 2 | 1 | friend | {DATE} | pass | watch | n/a | skipped |
| [Account 28] | 3 | 2 | seen | {DATE} | pass | bench | it pulled a clean list from a messy page | approved by owner |
| [Account 29] | 3 | 3 | replied | {DATE} | pass | bench | useful for students cooking on a budget | approved by owner |
| [Account 30] | 2 | 1 | cold | {DATE} | pass | bench | it handles long ingredient lists well | approved by owner |
| [Account 31] | 2 | 1 | seen | {DATE} | pass | bench | I like that it does one thing | drafted |
| [Account 32] | 3 | 1 | replied | {DATE} | pass | bench | the best part is it lives in the browser | approved by owner |
| [Account 33] | 2 | 1 | friend | {DATE} | pass | bench | creator wrote own (33) | creator wrote own |
| [Account 34] | 3 | 2 | seen | {DATE} | pass | bench | creator wrote own (34) | creator wrote own |

### Lineup example

### Example lineup log (fictional placeholders, not real accounts)

| Account | Fit | Reach | Relationship | Last ten checked | Check result | Decision | Draft | Status |
|---|---|---|---|---|---|---|---|---|
| [Account 1] | 3 | 1 | replied | {DATE} | pass | core | I tried this on a long stew recipe and got my list before the ads loaded | approved by owner |
| [Account 2] | 2 | 2 | seen | {DATE} | pass | bench | Finally a tool that treats recipes like instructions, not content | drafted |
| [Account 3] | 3 | 3 | cold | {DATE} | fail | skip | n/a | skipped |
| [Account 4] | 2 | 1 | friend | {DATE} | pass | core | creator wrote own | creator wrote own |

### Post example

Idea: Recipe pages bury the shopping list, and this tool pulls it out in one click.
Link placement: reply

Recipe sites were built for ads. Not for cooking.

So I made a one-click fix. Any recipe page becomes the shopping list you need.

Here it is turning a long recipe page into 9 items in under 3 seconds.

Cook more. Scroll less.

### Retro example

### Example retro at T+3d (fictional numbers, invented for illustration)

KPI planned: 150 installs by T+24h
KPI counted: 118 at T+24h, 171 at T+3d
Counted when: T+24h and T+3d from the owner's dashboard
First 300: owner saw strong replies in the first hour; most asked which sites work
Lines that travelled: "built for ads, not for cooking" was quoted the most
People who moved it: two core accounts with cooking audiences; the large bench account did nothing
What broke: nothing on the page; the FAQ did not list supported sites
Keep: the contrast first line; the 3-second demo; the clarifier reply
Cut: the bench account with a tired audience; the long video; posting the clip at +60 without new info
Try: a supported-sites list on the page; a second beat built on the top question; a NO-NETWORK note set for cooks who asked
Verdict: PARTIAL
Log row: | {DATE} | category stance | Recipe sites were built for ads | text + demo | LINEUP | 150 | PARTIAL | answer "which sites" before launch |

### Run sheet example

### Example run sheet (fictional)

T0: {LAUNCH_DATE} 09:30 {LAUNCH_TZ}
Plus 5: owner confirms the post is live and the store link opens on a phone; reply to first real comments from prepared drafts
Plus 15: owner reports whether comments are about the idea or confusion; post clarifier if confusion
Plus 60: decide second beat; if people quote the "built for ads" line, post the 15-second clip
Second beat: 15-second clip of the demo, drafted and ready
Clarifier reply: "It runs on the recipe page you already have open. No new app."
Replies owner: {FOUNDER}
Escalation owner: {FOUNDER}
Stay online until: T0 plus 6 hours, then check in at T+24h

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
