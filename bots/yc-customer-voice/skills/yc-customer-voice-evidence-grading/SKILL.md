---
name: yc-customer-voice-evidence-grading
description: "YC Customer Voice: use when the owner asks \"is this real or wishful?\", grade quotes, build a quote bank; for grading evidence as stated, observed or claimed. Not for writing the research doc (research-document)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "is this real or wishful?", grade quotes, build a quote bank; this skill covers grading evidence as stated, observed or claimed. WHEN NOT: writing the research doc (research-document). One-off asks can load this skill directly; a full run reaches it through yc-customer-voice-workflow.
# SKILL: evidence-grading

Use when: findings exist and the owner asks to "grade the evidence", "build the quote bank", "which quotes can we use", "how sure are we", "stated vs observed", or before any research document, avatar or objection map is written. It is the gate between raw findings and anything other bots will read.

Purpose: separate what customers really said from what we wish they said, and build the quote bank that copy may use. Every later step cites quote-bank IDs, so nothing reaches a launch bot without a grade.

Drafts only: the bank is an internal file. No quote is used in public copy without written permission on file. Nothing leaves the owner's chat without the owner's explicit yes.

## Inputs
- `findings` (step 2) and pulled items from `index` (step 1).
- The consent record, if the owner has any written permission from customers.

## Steps
1. **One row per item** in the quote bank table (template in yc-customer-voice-references ("Templates")): ID, Quote, Verbatim (yes or no), Source type, Source ref, Date, Speakers, Label, Tier, Theme, Use, Consent.
2. **Count speakers honestly.** Speakers is the number of independent people who said the same thing in substance. Two comments by one person count as one. A thread that quotes a review is not a second person.
3. **Label** each row: stated (the person about their own life), observed (behaviour seen), claimed (about others, the market, or the brand's own words). A claimed row is never above Tier C. A brand's own claim is never customer evidence.
4. **Tier** each row by the rule, never by how good it sounds:
   - A: Verbatim yes, and Speakers 3 or more.
   - B: Speakers 2 or more (verbatim or close paraphrase).
   - C: everything else (single mention, inferred, claimed).
   You may grade lower than the rule allows when the source is weak. You may never grade higher.
5. **Theme confidence.** High: Tier A rows from three or more different sources. Medium: Tier A from fewer, or several Tier B. Low: Tier C only.
6. **Set Use.** internal (research only), copy (other bots may borrow the words or the idea; Tier A or B only), public (shown as a customer quote; needs Consent "written"). Default for every row: internal. The owner upgrades Use, not the bot.
7. **Contradictions.** List findings that disagree (some say it is too simple, others too complex) and what could explain it (different segments, different products). Do not average them away.
8. **Negative evidence.** List what people dislike about the category or the product, with tiers. A launch that ignores it loses trust.
9. **Do-not-use list.** Quotes that are identifying even after redaction, sensitive (health, money, family conflict), or unverifiable. They stay internal and are never handed off.
10. **Run the checks.** Apply the quote-bank check then the evidence check.

## The minimum-evidence bar
At least 10 distinct sources, at least two source types, and either one Tier A theme or three Tier B themes. Below the bar the evidence check prints INSUFFICIENT EVIDENCE. Then:
- head every later output with "INSUFFICIENT EVIDENCE: n sources, n types";
- do not build avatars or locks as if they were real; draft them only if the owner asks, marked "provisional";
- give the owner the no-data path list (yc-customer-voice-references ("No data path")) to close the gap.

## Worked example (invented, every detail made up)
| ID | Quote | Verbatim | Source type | Source ref | Date | Speakers | Label | Tier | Theme | Use | Consent |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | found out about the bake sale at 8am | yes | review | R-04 | 2026-02-03 | 7 | stated | A | missed events | copy | none |
| Q2 | the second app nobody in the house opens | no | forum | F-02 | 2026-02-10 | 5 | observed | B | failed solution | copy | none |
| Q3 | every parent at school would buy this | yes | call | C-05 | as given | 1 | claimed | C | demand | internal | none |

Q1 is A: verbatim and seven people said the same thing in substance. Q2 is B: a paraphrase of five people. Q3 is C: one person's claim about others. Q3 can hint at a question for the owner; it can never appear as "parents love it".

## Gate (exit criteria)
- The quote-bank check PASS.
- The evidence check PASS, or INSUFFICIENT reported to the owner.
- No Tier C item is marked copy or public.

## Failure handling
- Everything is Tier C: report it plainly. The research has leads, not evidence. Run the no-data path.
- The owner wants a Tier C quote in an ad: say no in one line; offer to look for two more independent sources that would lift it to B.
- Two items conflict on a count: use the lower count and note why.
- Revision cap: two grading rounds. After the second fail, show the failing rows and stop.

## Rules
No Tier C item appears as a fact in later documents. Never upgrade a paraphrase to verbatim. Never add speakers you did not see. Consent defaults to "none".

## Output contract
`quote-bank` (the table), plus in the same block: theme confidence table, contradictions, negative evidence, do-not-use list. In chat: counts by tier, the bar result, and the top three Tier A rows. Report: Done, Blocked, Next.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the quote-bank check: `python3 scripts/check_quote_bank.py BANK.md`; the evidence check: `python3 scripts/check_evidence.py --bank BANK.md [--doc DOC.md] [--min-sources N]`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-customer-voice-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
