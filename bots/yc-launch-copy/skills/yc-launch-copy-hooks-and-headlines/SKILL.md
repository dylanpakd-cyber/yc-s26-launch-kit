---
name: yc-launch-copy-hooks-and-headlines
description: "YC Launch Copy: use when the owner asks \"give me opening lines\", headlines, first lines, hooks; for writing openers, antithesis lines and headlines. Not for full post drafting for a channel (channel-drafting)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "give me opening lines", headlines, first lines, hooks; this skill covers writing openers, antithesis lines and headlines. WHEN NOT: full post drafting for a channel (channel-drafting). One-off asks can load this skill directly; a full run reaches it through yc-launch-copy-workflow.
# SKILL: hooks-and-headlines

Purpose: write ten first lines, kill most, keep three. Then write three full posts from the best three when the owner asks. Covers post hooks, article openers, headlines and short-video hooks. The gate defaults to KILL.

## Use when
- An outline exists and needs a first line.
- The owner says "hooks", "first lines", "openers", "6 openers", "antithesis", "4A headlines", "headline options", "vet the hook", "grill my hook", "which hook is stronger", "ten first lines".
- A post underperformed and needs a re-hook.

Not for: video ad hooks for paid campaigns (that is the ads bot's job).

## Inputs
- The outline and pinpoint.
- The facts ledger (numbers in hooks come only from here).
- Voice rules.
- Platform. Default: X (130-character cut).

## Steps
1. **Write eleven, keep ten for the gate.** Use the six opener types (flat declaration, thought-provoking question, vulnerable admission, contrarian opinion, a number from the ledger, a moment in time) plus five antithesis openers (the obvious view, then the less obvious truth). Drop the weakest one so ten go to the gate. Concrete nouns. A short first sentence.
2. **Hook gate, eight tests, default KILL.** Each test is Y or N:
   1. Context: a stranger knows the topic.
   2. Curiosity gap: one specific open question.
   3. Concrete: nouns, numbers, scenes.
   4. Voice: sounds like the owner's samples.
   5. Honest: the piece pays it off.
   6. Fresh: not the phrase every account uses.
   7. Survives the cut: under 130 characters.
   8. One breath: sayable aloud without a pause.
   A line survives only with eight Y.
3. **Score survivors, 1 to 5 each:** callout or open loop; would the owner say it to a friend; a stranger understands; no insider words; easy to picture. PASS: every score 3 or more, the first 4 or more, average 4.0 or more.
4. **Video hooks only.** Mute test: picture and text carry it with no sound. Eyes-closed test: audio carries it. All three (text, voice, picture) say the same thing.
5. **Run the arithmetic.** Write each surviving line to hooks in the format in yc-launch-copy-references ("Templates"). Run the hook check. It checks length, dashes, the gate and the score math.
6. **Headlines (articles, newsletters, long posts).** Write twelve with the four-angle set (three actionable, three analytical, three aspirational, three human nature). Add three five-part clear headlines (a number from the ledger, the reader, a concrete noun, a measurable outcome, the cost of skipping). Keep three. Clear beats clever.
7. **Pick three finalists** with a one-line reason each. Recommend one.
8. **Ten lines, then three posts.** If the owner asks, write three full posts, one from each finalist, using the post skeleton in yc-launch-copy-references ("Templates"). The second line does a paragraph's work: what it is, for whom, why now.
9. **Hook bank.** Save the killed lines with the test they failed. They are raw material for satellites.

## Gate
- The hook check passes for the three finalists.
- Every number in a hook is in the ledger.
- No finalist the piece does not pay off.

## Output
```
TEN LINES (gate result per line): 1. ... [Y Y Y Y Y N Y Y] KILL: not fresh
FINALISTS:
1. <line> | score 5 4 4 5 4 = 4.4 | why: ...
2. ...
3. ...
Recommended: 1
HEADLINES (if asked): 12 + 3, three kept
Next: yc-launch-copy-channel-drafting
```

## If things go wrong
- **Nothing passes the gate.** Go back to the pinpoint and the bank. The best first line is often a real moment from the bank, cut down. Round cap: two rounds of ten. Then show the three closest with their failed tests.
- **Strong line, no proof.** Keep it in the bank with [NEED]. Never ship it.
- **Question hooks keep failing.** Use a question only when the answer is surprising.
- **Owner loves a hook that fails.** Show the failed test once. The owner decides. Log the choice.

## Never
- Never put a number in a hook that is not in the ledger.
- Never write a hook the piece does not pay off.
- Never borrow a phrase everyone uses.
- Never present a hook score as a prediction. It is a rubric read.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-launch-copy-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
