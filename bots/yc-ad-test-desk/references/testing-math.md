<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Ad Test Desk: Testing math

All numbers are formulas or labeled starting defaults, never benchmarks or promises. Replace each default with the owner's own number after the first readable test. Print "(default)" beside any default you use.

### 0. Sizing step zero (before any test)
Size from the owner's own funnel numbers, never anyone else's.
1. Launch goal: buyers or sign-ups wanted by {LAUNCH_DATE}.
2. The owner's own rates: page visit to sign-up, sign-up to buyer. No history: write [NEED] and size a message test only.
3. Results needed from ads = launch goal minus what other channels will bring (owner's estimate).
4. Spend range = results needed x target cost per result (low) to results needed x break-even cost per result (high).
5. Cells fundable = maximum loss / evidence floor (section 5).
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

### 3. Winner spend floor
{WINNER_SPEND_FLOOR} default: 3 x target cost per result. An ad under the floor is a rumour no matter how good its return looks.

### 4. Stop gate
Default: a cell has spent 2 x target cost per result with zero results, or the read window ended, whichever comes first.

### 5. Evidence floor per cell
Default: 3 x target cost per result per cell: the cost of a readable answer, not a guarantee of one. Cells the envelope can fund = maximum loss / evidence floor, rounded down. Never open more.

### 6. Read window
Default: 7 days plus the owner's conversion lag (click to purchase). Never read on today's data for today.

### 7. Leading indicators for cheap message tests
When spend is too small for purchase reads: cost per qualified click, thumb-stop rate (3-second views over impressions), hold rate (views to the end of the hook over 3-second views), cost per initiated checkout or sign-up. Write "purchase direction unresolved" on every such read.

### 8. Outcome bands (write before launch)
- Upgrade: cost per result at or under target after the floor is spent.
- Ambiguous: between target and break-even, or under the floor.
- Downgrade: over break-even after the floor, or stop gate hit.

### 9. Worked arithmetic (fictional)
A fictional app keeps a fixed amount per first order, K. Break-even = K. Target = 0.7K. Spend floor = 2.1K. Stop gate = 1.4K with zero results. Evidence floor = 2.1K per cell. A maximum loss of 10K funds 4 cells (10 / 2.1 = 4.7, rounded down).

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
