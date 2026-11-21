---
name: yc-customer-voice-research-document
description: "YC Customer Voice: use when the owner asks \"write up the research\", one doc for the team, brand sheet; for the research document and brand-information sheet. Not for grading single quotes (evidence-grading)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "write up the research", one doc for the team, brand sheet; this skill covers the research document and brand-information sheet. WHEN NOT: grading single quotes (evidence-grading). One-off asks can load this skill directly; a full run reaches it through yc-customer-voice-workflow.
# SKILL: research-document

Use when: the quote bank passes and the owner asks for "the research document", "a research doc", "brand info sheet", "what should the launch say", "summarise the research", or another bot needs a single file to read. Run after step 3. It writes the one document every other bot reads.

Purpose: convert graded findings into one structured research document plus a short brand information sheet. Every cell traces to a quote-bank ID. No ad ideas.

Drafts only: an internal document for the owner. Nothing is published or shared without the owner's explicit yes.

## Inputs
- Passing `quote-bank` (Tier A and B rows drive every section).
- Owner facts for the brand sheet: what the product is, the real offer, real proof assets, never-claims.

## Pipeline order (do not skip)
1. Raw material in, redacted (step 1).
2. Public sources gathered with full threads (step 2).
3. Reviews and comments graded into the bank (step 3).
4. This document.
5. The brand sheet.
6. Avatars (step 5) paste into Key personas.
Concepts stays empty. This bot never writes ads.

## Sections (each a "## " heading, in this order)
1. **Top pain points:** table of pain, description, count, best quote ID.
2. **Failed solutions:** attempt, why it failed, IDs.
3. **Desired outcomes:** outcome in their words, explanation, IDs.
4. **Objections:** ranked by count; each row says quote or paraphrase, with IDs.
5. **Misconceptions:** only where a source shows the belief, with the clarification from the owner's facts.
6. **Golden nuggets:** the best real lines grouped by emotion (relief, frustration, pride, fear, embarrassment), with IDs and dates.
7. **Words to borrow and avoid:** their words for the problem, the category and the outcome; words they dislike or that sound like marketing to them.
8. **Triggers:** events that start a search or a purchase.
9. **What changed their mind:** from reviews and calls.
10. **Alternatives:** what they use now and what they say about it.
11. **Necessity test:** why this product and not the free or existing option, answered only from evidence. If not shown, write "necessity not shown" and say what evidence would show it.
12. **Strategy implications:** opportunity and how the brand could win, directional only, each tied to IDs. Not ad scripts.
13. **Language analysis:** tone, emotional style, vocabulary clusters, reading level, and tips grounded in observed language.
14. **Key personas:** placeholder until step 5 lands; then a one-line summary per avatar.
15. **Open questions:** where evidence is thin, with Tier C leads that need checking.
16. **Concepts:** left empty.

## Steps
1. Fill sections from Tier A and B rows only. Each section cites at least two IDs, or is marked "thin" with the reason.
2. Keep separate motive families separate. If some buy for family and some for work, show both; do not blend them.
3. Run a slop sweep: remove invented numbers, filler, marketer words, unsourced quotes and claims the bank does not support.
4. Write the one-page summary: five things the launch should say and five it should avoid, each with IDs.
5. Write the brand sheet: product in one sentence, real offer and terms, real proof assets, never-claims, tone notes, links the copy may use. Every line sourced from the owner or [NEED]. Brand facts are context, never customer evidence.
6. Run the evidence check.

## Worked example: two sections (invented, every detail made up)
```
## Top pain points
| Pain | Description | Count | Best quote |
|---|---|---|---|
| Missed school events | Learns about events too late to act | 7 | Q1 |
| One parent carries the calendar | The other parent never checks shared tools | 5 | Q2 |

## Necessity test
Thin. Evidence shows the shared phone calendar fails because one parent never opens it (Q2, Q7). No source yet shows why this product would be opened when the calendar is not. Next: ask testers what made them open it on day three.
```

## Gate (exit criteria)
- The evidence check PASS: every section present, two IDs or "thin", no Tier C cited outside open questions, Concepts empty.
- Brand sheet has no unsourced line.

## Failure handling
- INSUFFICIENT EVIDENCE: write the document only if the owner asks, headed "INSUFFICIENT EVIDENCE", every section marked thin.
- A section has nothing: write "thin: no source yet" and add it to open questions. Never pad.
- The owner asks for ad ideas in Concepts: say this bot leaves it empty and hands the locks to the ad bot.
- Revision cap: two rounds. Then list the failing sections for the owner.

## Output contract
`research-doc` (sixteen sections), `brand-sheet`, and a one-page summary in chat (five to say, five to avoid, with IDs). Report: Done, Blocked, Next.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the evidence check: `python3 scripts/check_evidence.py --bank BANK.md [--doc DOC.md] [--min-sources N]`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-customer-voice-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
