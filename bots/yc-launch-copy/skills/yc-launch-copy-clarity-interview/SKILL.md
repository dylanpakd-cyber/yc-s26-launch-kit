---
name: yc-launch-copy-clarity-interview
description: "YC Launch Copy: use when the owner asks \"help me figure out what I'm saying\", messy thoughts, why I built this; for the clarity interview that turns raw thoughts into one clear idea. Not for writing openers (hooks-and-headlines) or polishing a draft (line-edit-and-rhythm)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "help me figure out what I'm saying", messy thoughts, why I built this; this skill covers the clarity interview that turns raw thoughts into one clear idea. WHEN NOT: writing openers (hooks-and-headlines) or polishing a draft (line-edit-and-rhythm). One-off asks can load this skill directly; a full run reaches it through yc-launch-copy-workflow.
# SKILL: clarity-interview

Purpose: pull one clear, true idea out of raw notes, voice memos and half-formed thoughts before any drafting. Most weak launch copy is a clarity problem, not a writing problem. This skill also starts the facts ledger and the voice rules every later step uses.

## Use when
- The owner sends raw thoughts, a voice memo transcript, bullet notes or "I want to write about X".
- The owner says "pinpoint", "Pinpoint Writing", "2-Year Test", "two-year test", "help me figure out what I'm saying", "what's my angle".
- First run of the bot (intake), or a new launch.

Not for: editing a finished draft (yc-launch-copy-line-edit-and-rhythm).

## Inputs
- Raw notes in any form.
- Intake answers, asked one at a time on first run: name and handle; the reader in one sentence ({READER_ONE_LINE}); two years ago versus today ({TWO_YEARS_AGO_VS_TODAY}); claim locks and banned words; which writing room, if any ({WRITING_ROOM}).
- {VOICE_SAMPLES}: five or more pieces the owner wrote. Fewer is fine; rules become tentative.
- Launch facts if the piece mentions them: {PRODUCT}, {LAUNCH_DATE}, {PRICE_RULE}, {CAMPAIGN_URL}.

## Steps
1. **Intake, one question at a time.** What are you launching; who is it for; what does that person try today; what happened that made you build this; what is the strongest fact you can prove; what must never be said. Save each answer as a memory before asking the next.
2. **Experience bank.** Pull concrete material out of the notes: scenes (who, where, what happened), numbers with sources, named facts, objections heard, mistakes made. Tag each: scene, number, objection, mistake, lesson.
3. **Facts ledger.** Every number and named fact goes in the ledger as "- <fact> | source: <where>". No source means "[NEED]". Run the facts-ledger check.
4. **Two-year test.** From {TWO_YEARS_AGO_VS_TODAY}, list five hard lessons the founder could teach their former self. Only lessons the notes or the owner confirm.
5. **Pinpoint questions.** Answer, from the notes: what exact problem; whose problem (one specific person); what concrete benefit; what feeling the reader should leave with; what one action.
6. **Pinpoint candidates.** Draft five one-sentence takeaways. Choose with three tests: a stranger understands it; it is still true in two years; the bank holds proof for it.
7. **Reader sentence.** One sentence about the exact reader: who they are, what they own, what keeps them up.
8. **Proof list.** Two to four ledger facts that make the pinpoint believable.
9. **Voice rules.** From {VOICE_SAMPLES}, measure: average sentence length, share of fragments, contractions, how the reader is addressed, words always used, words never used, how pieces open and close, punctuation habits. Mark any rule backed by fewer than three samples "tentative".
10. **Play-back.** Say back what you heard in three lines: the pinpoint, who it is for, the proof. Ask: "Is that it?" Do not draft until the owner says yes or corrects it.
11. **Fill the pinpoint card** from yc-launch-copy-references ("Templates") and run the fields check (pinpoint).
12. **Gaps.** At most three questions for the owner.

## Gate
- The fields check (pinpoint) passes: pinpoint, reader, problem, benefit, emotion, action, "Stranger test: YES", "Two-year test: YES", two proof lines.
- The facts-ledger check passes: every ledger row has a source or is marked [NEED].
- The owner confirmed the three-line play-back.

## Output
```
PLAY-BACK
1. Pinpoint: ...
2. For: ...
3. Proof: ...
Is that it? (reply yes, or correct a number)

PINPOINT CARD: <filled template>
LEDGER: <rows>
VOICE RULES: <rules, tentative ones marked>
OPEN QUESTIONS (max 3): ...
Next: yc-launch-copy-idea-map-and-outline (or yc-launch-copy-writing-room if the owner uses one)
```

## If things go wrong
- **Notes hold two or three ideas.** That is two or three posts. Pick the one with the most proof. Save the others in the bank as future pinpoints.
- **No proof for the best pinpoint.** Keep it as a candidate, ask the owner for the fact, and draft from the next best pinpoint meanwhile.
- **No voice samples.** Use house style (short sentences, plain words) and say so in every output until samples arrive.
- **Owner skips the play-back.** Ask once more in one line. If they still skip, draft and label the draft "pinpoint unconfirmed".
- **Round cap.** Two rounds of pinpoint candidates. If none passes, show the best two and let the owner choose.

## Never
- Never invent a scene, lesson, number or quote.
- Never search files or other bots for the owner's facts. Ask.
- Never draft before a pinpoint exists.
- Never store passwords, keys or private customer details in the bank.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-launch-copy-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
