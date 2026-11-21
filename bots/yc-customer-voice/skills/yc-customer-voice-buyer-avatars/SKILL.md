---
name: yc-customer-voice-buyer-avatars
description: "YC Customer Voice: use when the owner asks \"who is our customer?\", personas, buyer profiles; for building buyer avatars: three when the evidence shows three distinct core problems, fewer with an evidence note. Not for mining raw sources (voice-mining)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "who is our customer?", personas, buyer profiles; this skill covers building buyer avatars: three when the evidence shows three distinct core problems, fewer with an evidence note. WHEN NOT: mining raw sources (voice-mining). One-off asks can load this skill directly; a full run reaches it through yc-customer-voice-workflow.
# SKILL: buyer-avatars

Use when: the research document passes and the owner asks for "buyer avatars", "three avatars", "personas", "who is the buyer", "draft avatar 1 of 3", or another bot needs to know who it is talking to. Run after step 4. Avatars are built from research, never invented.

Purpose: three distinct buyer avatars drawn from the research document, so copy can speak to one person at a time. Each avatar reads like a real person with the inner thoughts buyers rarely say out loud, and every soundbite traces to the quote bank.

Drafts only: internal cards for the owner and the launch bots. Nothing is published without the owner's explicit yes.

## Inputs
- Passing `research-doc` and `quote-bank`.
- {AVATAR_COUNT}: default 3.

## The count rule
The default is exactly three avatars. Build three only when the evidence shows three different core problems (different situations and relationships to the problem, not three shades of one person). If the evidence shows only two, build two and add an "Avatar count note:" saying why, with the IDs that show the third does not exist yet. Never pad to three. Never build more than three; extra ones become sub-avatars on request.

## Steps
1. **Parse the research.** Extract: what the product does and how; market context (what they have seen before, how skeptical they are); the people with purchase evidence; their original language; their prior attempts.
2. **Find the core problems.** List every distinct core problem with its IDs. Pick the three with the strongest evidence. Different core problems, not different ages or jobs.
3. **Fill one card per avatar** (template in yc-customer-voice-references ("Templates")), in this order:
   - Nickname (a role, never a real person's name), age band marked as an estimate unless sourced.
   - Core problem in one sentence, plus the emotional context around it.
   - The moment it bites: time, place, who else is there.
   - Top five fears, ranked, in their inner voice ("If I miss one more, they'll think I don't care.").
   - Emotional drivers: name the two that dominate (stress, guilt, frustration, loneliness, pride, relief, wanting to be seen as capable).
   - Failed solutions: the attempted fix, the failure point, and any lasting distrust.
   - Soundbites: three or more quote-bank IDs at Tier A or B. Their words only. Mark paraphrases.
   - Desired transformation: a concrete ordinary day after the problem is gone, not a fantasy.
   - Market beliefs: what they believe about products like this.
   - Emotional blockers: what stops them even when they want it.
   - Relationship impact: how the problem touches the people around them.
   - Objections: ranked, in their words, with the fear under each.
   - Awareness level: unaware, problem aware, solution aware, product aware, most aware.
   - Where they spend time, from the sources.
   - Proof that persuades this avatar, and the format that suits them (short video, long post, email).
   - Inferred: list every attribute that is inferred rather than evidenced.
4. **Voice rule.** Raw and human, never marketer-speak. Use their words. Never turn everyday words into medical or clinical labels.
5. **Distinctness check.** Swap the nicknames. Would the copy still fit? If yes, the avatars are the same person; merge them and add a count note. The cards check also fails two cards with the same core problem.
6. **Sub-avatars (only on request).** Split one avatar by experience, behaviour or emotion, not demographics. For each: the angle, one proof point, the top objections, two or three directional hook ideas for the ad bot to test. Still no finished ads. Remind the owner that one failed ad does not kill an angle.
7. **Run** the cards check (avatar).

## Worked example: one card (invented, every detail made up)
```
## Avatar 1: The Calendar Keeper
Nickname: The Calendar Keeper
Age band: 35 to 45 (estimate)
Core problem: carries the whole family schedule alone and still misses things
Moment it bites: 8am on a school day, reading a message about an event that is today
Top fears: my kid will be the only one without a costume; the other parent will say I should have known; teachers think we don't care; I'll forget something that matters more; I'll never get a break from tracking it all
Emotional drivers: guilt, wanting to be seen as capable
Failed solutions: a shared phone calendar the other parent never opens (Q2); paper on the fridge (Q7)
Soundbites: Q1, Q2, Q8
Desired transformation: a Tuesday where the reminder arrived the night before and both parents saw it
Market beliefs: family apps are built for organised people, not for us
Emotional blockers: embarrassment at needing help with something basic
Relationship impact: small fights about who forgot
Objections: the other parent won't use it either (Q2), one more app (Q9)
Awareness level: solution aware
Where they spend time: parenting forums (F-01 to F-03), app store reviews
Proof that persuades: a demo of the other parent getting the reminder without opening the app
Inferred: age band; the costume fear is inferred from Q1 and Q8
```

## Avatar count rule
Three avatars when evidence shows three distinct core problems, fewer with an evidence note ("Avatar count note:" naming what the evidence shows). Never pad to reach three. INSUFFICIENT EVIDENCE is an allowed outcome when the evidence bar is not met.

## Gate (exit criteria)
- The cards check (avatar) PASS: every field filled, five fears, three or more Tier A or B soundbites, distinct core problems, three cards or a count note.
- No real person's name or identifying detail.

## Failure handling
- INSUFFICIENT EVIDENCE upstream: do not build avatars unless the owner asks; then mark every card "provisional" and list the gaps.
- A field has no evidence: write "inferred: reason" or "unknown"; never invent a life story.
- Only one core problem: one avatar plus a count note, and a list of questions that might reveal others.
- Revision cap: two rounds. Then show the failing fields and stop.

## Rules
Do not invent a life story. Do not use a real person's name or details. Do not stereotype by demographics. Soundbites come from the bank only.

## Output contract
`avatars` with the cards (and any count note). In chat: the avatar nicknames with one line each and the distinctness result. Then paste one-line summaries into the research document's Key personas section. Report: Done, Blocked, Next.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the cards check: `python3 scripts/check_cards.py --kind KIND [--bank BANK.md] FILE`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-customer-voice-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
