---
name: yc-x-launch-desk-network-and-lineup
description: "YC X Launch Desk: use when the owner asks \"who should quote/share the post?\", lineup, who to tell, \"I don't have a network\"; for building the quote lineup and note list, or the no-network plan. Not for the live window itself (wave-and-replies)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "who should quote/share the post?", lineup, who to tell, "I don't have a network"; this skill covers building the quote lineup and note list, or the no-network plan. WHEN NOT: the live window itself (wave-and-replies). One-off asks can load this skill directly; a full run reaches it through yc-x-launch-desk-workflow.
# SKILL: network-and-lineup

Purpose: build the people plan for the launch. Who might honestly care, who gets a hand-written note from the founder, and who might quote the launch in their own voice. Two paths: LINEUP for founders with a network, NO-NETWORK for founders without one. Everything is a draft. The owner sends.

## Use when
- The brief passed. Runs in parallel with the post draft at T-48h.
- The owner says "who should quote this", "lineup", "lineup log", "creator scout", "score my followers", "quote drafts", "notes to send", "I don't have a network".

## Inputs
- {LINEUP_SOURCE}: the owner's own follower and following export, read only. Default: none; ask.
- {AUDIENCE} and the brief's claim.
- {CREATOR_BUDGET_APPROVED_BY_OWNER}. Default: no paid placements.
- The post draft (for Part C).

## Steps: Part A, score the network
1. Read the export. Do not scrape private data or log into anyone's account.
2. Score each account from evidence only: **fit** 0 to 3 (posts about the topic), **reach** 0 to 3, **relationship** (cold, seen, replied, friend). Follower count alone never earns reach points.
3. Shortlist up to 200 by fit, then relationship, then reach.
4. Draft one short note per shortlisted person for the owner to send by hand. Each note is different and names something real that person did. Never bulk messages.

## Steps: Part B, the lineup (30 to 60 accounts)
1. Candidates: the shortlist, accounts whose audience overlaps {AUDIENCE}, accounts that already talked about the problem.
2. **Two-minute check each.** Last ten posts, pinned one left out. Date span. How many are on topic. Does the audience engage with posts like this? Daily sponsored content? Recent controversy? Fit for the claim? Stale (newest post older than about 30 days) goes to watch.
3. **Decision:** core, bench, skip or watch. A failed check is never core or bench.
4. Prefer small and fresh over big and tired.
5. Paid placements only with {CREATOR_BUDGET_APPROVED_BY_OWNER}. Otherwise skip them.
6. **Log it** in the lineup log template (yc-x-launch-desk-references ("Templates")). The log is the single source of truth: who, scores, check date, result, decision, draft, status.
7. Run the lineup-log check.

## Steps: Part C, quote drafts
1. One draft per core or bench account, in that person's own voice (sentence length, humour, topics from their last ten posts). Never identical. The lineup-log check fails identical drafts.
2. Each draft says something the person could honestly say, with an opinion attached. Not a copy of the founder's line.
3. Status per draft: drafted, approved by owner, creator wrote own, sent by owner, replied, skipped. The desk never sets "sent by owner"; the owner reports it.
4. Drop any draft that makes someone claim an experience they did not have.

## Steps: NO-NETWORK path (under 10 accounts pass the check)
1. **Ten real notes.** Find up to ten people who publicly asked about this problem. Draft one personal note each. The owner sends or skips.
2. **Reply plan.** List five live conversations on the topic where the founder can add a useful reply in the week before launch, without linking the product. Drafts only.
3. **Communities.** Name up to three places the buyer already gathers where a launch post is allowed by the rules. The owner checks each rule.
4. **Built for strangers.** Lean harder on the first line and the video, because no network will carry it. Re-run the harsh read with that in mind.
5. **Log it.** Write the plan as the people plan for gate G4.

## Gate
- LINEUP path: The lineup-log check passes (scores in range, every account checked, failed checks not in lineup, statuses valid, no identical drafts).
- NO-NETWORK path: the plan has notes, reply plan and communities sections filled.
- Every draft is true and distinct.

## Output
```
PATH: LINEUP | NO-NETWORK
SHORTLIST: <n> with notes
LINEUP LOG: <table>, <n> core, <n> bench, check: PASS
QUOTE DRAFTS: <n>, all distinct
Next: owner review at T-36h, then yc-x-launch-desk-test-of-300
```

## If things go wrong
- **No export.** Ask once. Without it, run the NO-NETWORK path.
- **Fewer than 30 pass.** Fine. Launch with who passed. Under 10: NO-NETWORK path.
- **A big account wants payment.** Skip unless the owner approved a budget in writing.
- **Someone asks for the exact words to post.** Give them the draft as a suggestion and say they should change it to their own words.
- **Round cap.** Two drafts per account. Then mark it skipped.

## Never
- Never send, DM, follow, like or quote for the owner.
- Never automate sends to a network.
- Never pay or promise payment.
- Never write a quote that puts false words in someone's mouth.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the lineup-log check: `python3 scripts/check_lineup_log.py <lineup log .md>`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-x-launch-desk-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
