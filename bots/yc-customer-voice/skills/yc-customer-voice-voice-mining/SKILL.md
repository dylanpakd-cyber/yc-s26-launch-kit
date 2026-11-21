---
name: yc-customer-voice-voice-mining
description: "YC Customer Voice: use when the owner asks \"here are reviews/comments, what are people saying?\", mine a thread or survey; for mining reviews, comments and forums for buyer language. Not for ranking objections (objection-map)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "here are reviews/comments, what are people saying?", mine a thread or survey; this skill covers mining reviews, comments and forums for buyer language. WHEN NOT: ranking objections (objection-map). One-off asks can load this skill directly; a full run reaches it through yc-customer-voice-workflow.
# SKILL: voice-mining

Use when: the owner asks to "mine comments", "read the reviews", "what are people saying about this", "find buyer language", "is there demand for this", "social listening", or points at posts, review pages, forum threads or survey exports. Merges comment mining, social listening and demand research. Run after step 1 for owner material, or straight after the evidence check for public sources.

Purpose: mine public comments, reviews, forums and social posts (and owner-provided surveys) for the language and signals of real buyers, with a source and a count for every finding.

Drafts only: read-only research. Never comment, reply, message, follow, post or log in as anyone. Nothing leaves the owner's chat without the owner's explicit yes.

## Inputs
- {RESEARCH_QUESTION}: the decision this research must inform.
- {SOURCES} and {REVIEW_SOURCES}: links or pasted text. If none, use the no-data path (yc-customer-voice-references ("No data path")).
- Redacted owner material from step 1.
- Competitor and alternative names the owner knows, plus aliases for the category.

## Steps
1. **Scope.** Write: the research question, the platforms (two or three, chosen for where the buyer talks), the time window, the target sample size, the search terms (topic, aliases, misspellings, competitor names). State what is out of reach (private groups, login-walled pages, deleted posts).
2. **Collect.** For each source record: a source ref (R-01 for reviews, F-01 for forum threads, P-01 for posts, S-01 for surveys), the URL or "owner paste", the date, and the context. Read the original post or product page first; a comment means little without what it answers. For forums, read the whole thread, including follow-ups.
3. **Aim for balance.** Own reviews (10 to 30 if they exist), competitor or alternative reviews (10 to 30), and comments that surface questions and objections. Include negative and three-star reviews; they hold the best objection language.
4. **Clean lightly.** Drop spam, bots, duplicates and giveaway comments. Keep slang, misspellings and emotional wording. Do not tidy quotes.
5. **Score engagers against the buyer.** For each source, ask: do the people talking look like {AUDIENCE} (role, situation, problem)? Mark each item "buyer-like" or "not our buyer". Only buyer-like items count toward themes. Note the split in the limits section.
6. **Sort every item** into one bucket: pain, desire, failed solution, workaround, doubt, question, buying signal, trigger, praise, confusion, request, debate, joke. One item, one bucket. If it fits two, split it into two items.
7. **Label each item** stated, observed or claimed (yc-customer-voice-workflow rubric). Mark verbatim or paraphrase.
8. **Cluster into themes.** For each theme: count of independent people, share of the buyer-like sample, intensity (low, medium, high, judged by the words used), two verbatim examples redacted per {REDACTION_RULES}, and the strongest phrase.
9. **Repeated questions** go in their own list with counts. A question asked many times is an FAQ or a subject line for the launch bots.
10. **Demand rating.** Strong (many independent people, recent, specific, signs of willingness to pay), medium, or weak, with the reason. Weigh negative evidence: people who tried the category and left.
11. **Recommended action per theme:** hook idea for another bot, FAQ, objection answer, product note for the owner, or avoid. Directional only; no copy.
12. **Limits note.** What could not be seen, how the sample may be biased (platform moderation, a viral post skewing counts, mostly fans), and what would change the picture.

## Worked example (invented, every detail made up)
Question: "Why do busy parents want a shared family planner?" Sources: R-01 to R-12 (app store reviews of two alternatives), F-01 to F-03 (parenting forum threads), P-01 (a post about school calendars). Themes:

| Theme | Bucket | People | Intensity | Example (redacted) | Action |
|---|---|---|---|---|---|
| Missed school events | pain | 7 | high | "found out about the bake sale at 8am" (R-04) | hook idea for ad bot |
| Second app nobody opens | failed solution | 5 | medium | "my husband never checks it" (F-02) | objection answer |
| Works offline? | question | 4 | low | "does it sync without wifi" (R-09) | FAQ |

Limits: no private parenting groups; two of the twelve reviews were from the same long thread; the post skews toward one school district.

## Gate (exit criteria)
- Every finding has a source ref, a bucket, a label and a count. No source, no finding.
- Every count is a real count of independent people from the collected items.
- The limits note exists.

## Failure handling
- No sources given and the owner has none: run the no-data path. If still under the minimum, report "insufficient evidence" with what was found.
- A platform blocks access: say so in limits and move to the next source. Never log in or work around a block.
- A theme has one mention: keep it as a lead in the open questions, not a theme.
- Revision cap: two collection rounds. After the second, report what exists and the gaps.

## Rules
Public data only. Never log in as someone, never message anyone, never scrape behind a login. Keep exact words including misspellings. Counts must be real. Never claim broad market sentiment from one post's comments.

## Output contract
`findings`: scope block, item table (ID, words, verbatim yes or no, source ref, date, bucket, label, buyer-like), theme table, repeated-question list, demand rating, limits note. In chat: the top five themes with counts. Report: Done, Blocked, Next.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the evidence check: `python3 scripts/check_evidence.py --bank BANK.md [--doc DOC.md] [--min-sources N]`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-customer-voice-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
