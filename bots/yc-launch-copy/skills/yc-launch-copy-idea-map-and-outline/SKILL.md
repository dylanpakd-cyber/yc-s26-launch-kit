---
name: yc-launch-copy-idea-map-and-outline
description: "YC Launch Copy: use when the owner asks \"outline this\", structure an essay or post, map the ideas; for turning a clear idea into an outline. Not for line-level polishing (line-edit-and-rhythm)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "outline this", structure an essay or post, map the ideas; this skill covers turning a clear idea into an outline. WHEN NOT: line-level polishing (line-edit-and-rhythm). One-off asks can load this skill directly; a full run reaches it through yc-launch-copy-workflow.
# SKILL: idea-map-and-outline

Purpose: turn the confirmed pinpoint into a set of ideas and one tight outline. The outline decides what the piece says before any sentence is polished, so the draft has one point and steady new information.

## Use when
- A pinpoint card passed and the owner confirmed the play-back.
- The owner says "outline this", "what should I write about", "give me angles", "expand this idea", "atomic essay", "short essay outline", "Pain-Dream-Fix", "What/How/Why", "content buckets".
- One strong post needs satellites for launch week.

Not for: first lines and headlines (yc-launch-copy-hooks-and-headlines).

## Inputs
- The pinpoint card and facts ledger.
- The experience bank.
- {CONTENT_BUCKETS}. Default: the product's problem, the founder's craft, lessons from building.
- {PLATFORMS} and the primary piece's format: post, thread, essay or article. Default: one LinkedIn post and one X post.

## Steps
1. **Question list.** Write twenty questions the reader would ask about the pinpoint. Pull them from the bank, from what the owner has been asked, and from objections. Rank by how many people would ask each.
2. **Bucket check.** Tag each question with a content bucket. Drop questions outside every bucket, or ask the owner whether to add a bucket.
3. **Expansion angles.** For the top three questions, apply two or three of the ten expansions: tip, data angle (ledger only), step by step, lesson learned, benefit, reason why, common mistake, real example, provoking question, personal story.
4. **Teaching shape.** Pick one for the primary piece:
   - Short essay: hook, one-sentence promise, three points of one or two sentences, a takeaway that answers the hook.
   - Pain, dream, fix: the painful now, the better state, three steps.
   - What, how, why: a definition, three steps, three reasons.
   - Story: a scene, the turn, what changed, the lesson for the reader.
5. **Primary and satellites.** One primary piece. Two to four satellites, each a short post answering one question from the list.
6. **Outline the primary.** Pinpoint at the top. Promise. Opening scene or claim. Three beats, each holding one fact from the ledger. The turn. The action.
7. **Rate of revelation.** Read the beats in order. Each must reveal something new. Put the best idea early, not last. Move or cut any beat that repeats.
8. **Cut test.** Remove any section that does not prove or show the pinpoint.
9. **Teach before pitch (long pieces).** The reader learns something usable before the product appears. If the product shows up first, move it down.
10. **Fill the outline** from yc-launch-copy-references ("Templates"). Run the fields check (outline).

## Gate
- The fields check (outline) passes: pinpoint, promise, opening, three beats, turn, action, and "Teach before pitch: YES" (or N/A for posts under 150 words).
- Every beat that holds a number points to a ledger row.
- Every section serves the pinpoint (cut test done).

## Output
```
QUESTIONS (top 10 of 20, ranked): 1. ...
ANGLES for Q1 to Q3: ...
PRIMARY: <format> | shape: <short essay | pain-dream-fix | what-how-why | story>
OUTLINE: <filled template>
SATELLITES:
1. <question> -> <one-line angle>
Next: yc-launch-copy-hooks-and-headlines
```

## If things go wrong
- **Fewer than ten real questions.** Ask the owner: "What do people ask you most about this?" Use their answers. Do not invent reader questions.
- **Every beat needs a fact the ledger lacks.** Mark [NEED] on those beats, show the owner the list, and write the beats that are covered first.
- **The outline has two points.** Split it. The second point becomes a satellite or a future primary.
- **The product must lead (a pure announcement).** Then the piece is short: what it is, who it is for, one proof, the link. Mark "Teach before pitch: N/A".
- **Round cap.** Two outline drafts. Then the owner picks.

## Never
- Never invent a reader question, data point or story.
- Never let the product appear before the reader gets value in a long piece.
- Never pad an outline to look thorough.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the fields check: `python3 scripts/check_fields.py <kind> <filled file>`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-launch-copy-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
