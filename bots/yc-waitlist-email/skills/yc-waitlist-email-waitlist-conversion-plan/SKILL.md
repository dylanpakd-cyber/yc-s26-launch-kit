---
name: yc-waitlist-email-waitlist-conversion-plan
description: "YC Waitlist Email: use when the owner asks \"turn the waitlist into buyers\", the launch email plan, segments; for planning how the waitlist converts: segments, email jobs, objection matrix, and the run plan the owner approves before any email past email 1. Not for writing one email (email-draft-and-edit)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "turn the waitlist into buyers", the launch email plan, segments; this skill covers planning how the waitlist converts: segments, email jobs, objection matrix, and the run plan the owner approves before any email past email 1. WHEN NOT: writing one email (email-draft-and-edit). One-off asks can load this skill directly; a full run reaches it through yc-waitlist-email-workflow.
# SKILL: waitlist-conversion-plan

Use when: the brief passes and the owner asks to "plan the launch emails", "map the run", "what should we send and when", "build the objection matrix", or wants to know who gets which email. Run it before any drafting. Do not use it to write email copy.

Purpose: design the whole run before writing it. Which email goes to whom, on which day, doing which job, answering which doubt. A launch is one sales argument spread over several emails. Plan it once so each email does its own part and no email repeats another.

Drafts only: the plan is a document for the owner. This skill never builds segments, tags or automations. Nothing goes out without the owner's explicit yes.

## Inputs
- `brief` and {EMAIL_LOCKS} from step 1 (must pass the brief check).
- {LIST_SEGMENTS}: only segments {EMAIL_TOOL} can really build.
- The objection list: from replies, support tickets, survey answers, call notes or a customer research document. Never invented.
- Past open and click patterns, if the owner has them. Not required.

## Steps
1. **Decide if this needs a full sale plan.** It does if the window has a real start date and readers need several emails for the purchase to make sense. If the owner only wants one announcement, write a one-row plan and skip to drafting.
2. **Write the argument once.** One line each: who it is for and what they want (in their words), the promise, the one fresh way of seeing the problem, how it works in plain steps, the proof and its order, the doubts with an email assigned to each (lead with the emotional block; cover cost after desire), the exact offer, when the price first appears, how the last email asks.
3. **Segment by behaviour.** Use what the tool can see: opened recently, clicked, never opened, bought, late joiner. Buyers leave every selling email. Unsubscribed and complained people leave everything. If the tool cannot build a segment, do not plan around it.
4. **Name the top five doubts** in the readers' own words, ranked by how many readers hold them. If there is no data, write "assumed" beside each and plan a reply ask in the first email to learn the real ones.
5. **Build the objection matrix:** doubt, honest answer, proof, the email that answers it, what the answer does not claim. Missing proof is [NEED PROOF]. An objection with no honest answer is a product note for the owner, not an email.
6. **Draw the day map.** Start from yc-waitlist-email-references ("Send timing defaults"). Three rows do not move: the day-before announcement, the offer on day one, and the last-hours email on the final day. The middle is a menu: proof, one objection, one big question answered fully, who it is not for, a founder story, outside validation, the price set against a real alternative. Pick by the real objections.
7. **One job per email.** Remind, announce, offer, show, answer, admit, name the deadline, thank. If a job needs "and", split it.
8. **Real deadline check.** Apply the five deadline tests in yc-waitlist-email-knowledge. A date that fails all five tests is struck from the plan. Then the run uses the cost of waiting instead.
9. **Exit rules.** A purchase removes the person before the next selling email. Recompute buyers right before each send, including each send on the final day. A reply moves the person to the owner. Someone who asked a question gets an answer before the next scripted email. Cap selling sends to people who never engage.
10. **SMS, if used.** Only to people who opted in to texts. Shorter. No more than two across the run. Same honesty rules.
11. **Measurement plan.** Primary metric: purchases from the list. Secondary: clicks and replies. Opens are a rough signal only. Decide before the first send what result would change the plan (for example, "if the proof email gets no clicks, swap the order of emails 5 and 6"). Never report a number the owner did not give you.
12. **Hand off** the run plan table. One row per email with these columns: Email, Day, Segment, Type, Job, Doubt, Subject angle, Link, Deadline, Exclude, Status. Status starts as "planned".

## Worked example (invented business, every fact made up)
"Example Planner", eight emails, close Thursday 21:00 PT.

| Email | Day | Segment | Type | Job | Doubt | Subject angle | Link | Deadline | Exclude | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Mon | waitlist | announcement | say it opens tomorrow | none | the date | {CAMPAIGN_URL} | Thu 21:00 PT | buyers, unsubscribed | planned |
| 2 | Tue AM | waitlist | launch | ask for the sale | none | it is ready | {CAMPAIGN_URL} | Thu 21:00 PT | buyers, unsubscribed | planned |
| 3 | Wed AM | non-openers of 2 | resend | reach non-openers | none | new angle | {CAMPAIGN_URL} | Thu 21:00 PT | buyers, unsubscribed, openers of 2 | planned |
| 4 | Wed PM | waitlist | proof | show a week planned in five minutes | will it work for my family | demo | {CAMPAIGN_URL} | Thu 21:00 PT | buyers, unsubscribed | planned |
| 5 | Thu AM | waitlist | answer | settle the cost doubt | is it worth it | the question | {CAMPAIGN_URL} | Thu 21:00 PT | buyers, unsubscribed | planned |
| 6 | Thu PM | clickers, not bought | last-hours | wake the deadline | none | hours left | {CAMPAIGN_URL} | Thu 21:00 PT | buyers, unsubscribed | planned |
| 7 | Fri | buyers | thank-you | start onboarding | none | welcome in | app link | none | unsubscribed | planned |
| 8 | Fri | non-buyers | close | say it closed | none | closed | none | none | buyers, unsubscribed | planned |

This short window has no separate deadline-day email. A five-day window would add one.

## Plan-approval gate
Show the run plan as a numbered table and ask: "Approve this plan?" Only the owner's yes in chat moves the plan to owner-approved. Until then, draft nothing past email 1. If the owner changes a row, re-run the run-plan check and ask again.

## Gate (exit criteria)
- The run-plan check passes.
- Every email has one job, one reader, one action. Every deadline is true. Buyers are excluded.
- The owner says yes to the plan before step 3 writes more than email 1. Show the plan above any draft.

## Failure handling
- Tiny list: if fewer than 20 reachable, consented readers remain, do not infer a winning subject or segment from rates. Propose three drafts only: launch, one answer, a close note. Add a last-hours draft only for a real cutoff and fresh interest. No resend. The owner chooses whether the short run is worth doing.
- Unengaged list: if nobody has replied, bought or made a confirmed human visit recently, pause the sales plan. Propose one low-pressure relevance check to consented readers, with an easy opt-out. Let the owner review real replies before resuming. No reply is not permission to send more. Suppression and consent rules still apply.
- Tiny or unengaged lists have no fixed conversion forecast. Ask for qualitative feedback, report raw counts with the denominator, and cap this recovery attempt at one check-in. No response means HOLD, not a longer sequence.
- No objection data: mark doubts "assumed", add a reply ask to email 1, and re-rank after the first replies.
- No real deadline: remove the Deadline column values ("none"), drop the last-hours row, and lean on cost of waiting and desire.
- The tool cannot segment non-openers: replace the resend with a new email to everyone that has its own job.
- The run-plan check fails: fix the rows it names. Revision cap: two rounds. After the second fail, show the owner the table and the failing checks, and ask which to change.

## Output contract
Save `plan` in this chat: the argument block (step 2), the objection matrix, the run plan table, exit rules, the measurement plan. In chat: a numbered summary with one line per email and its job, and the question "Approve this plan?".

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the brief check: `python3 scripts/check_brief.py BRIEF.md`; the run-plan check: `python3 scripts/check_run.py [--cap N] PLAN.md`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-waitlist-email-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
