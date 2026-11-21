---
name: yc-launch-copy-line-edit-and-rhythm
description: "YC Launch Copy: use when the owner asks \"tighten this\", \"this feels clunky\", edit a paragraph; for line editing an existing draft for clarity and rhythm. Not for checking claims (honesty-and-fact-gate)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "tighten this", "this feels clunky", edit a paragraph; this skill covers line editing an existing draft for clarity and rhythm. WHEN NOT: checking claims (honesty-and-fact-gate). One-off asks can load this skill directly; a full run reaches it through yc-launch-copy-workflow.
# SKILL: line-edit-and-rhythm

Purpose: make a draft clean, short and in the owner's voice without changing a fact. Edit mode keeps the owner's draft. Rewrite mode rebuilds it from the pinpoint. Both end with a change list the owner can reverse.

## Use when
- A draft exists (the bot's, the owner's, or a room reply the owner kept).
- Edit triggers: "tighten this", "clean this up", "make it shorter", "fix the tone but keep it me", "hemingway this", "grade 3", "too hard to read", "make it simpler".
- Rewrite triggers: "rewrite this", "start over", "redo it", "make it sound human".
- Review triggers: "review this", "what's wrong with this".

## Inputs
- The draft and its channel.
- Voice rules. Default when missing: edit lightly and say so.
- Facts ledger.
- How hard to go: light (typos, small swaps), tighten (cut and sharpen, the default), heavy (reorder). Ask once only if the owner did not say.

## Steps: edit mode
1. **Name the job** in one line: what this copy must get the reader to do. Every edit serves that.
2. **Inventory the facts:** names, numbers, dates, claims, links, the ask. All survive. Nothing new joins.
3. **Cut.** Throat-clearing openers, repeated points, hedges, stacked adjectives, "in order to". Most drafts lose their first paragraph and their last.
4. **Clarity.** Move the sentence that states the point up. One idea per sentence. A real subject doing something. Swap jargon for the plain word. Fix vague pronouns.
5. **Sentence rules.** Strongest word last (avoid ending on "is" or "was"). Two commas at most. Cut tiny-word clusters. Delete most -ly adverbs. Active voice.
6. **Rhythm.** Mix long and short sentences. No three of the same length in a row. One, three, one for short pieces. One-sentence openers and closers. White space.
7. **Tangible swap.** Replace abstractions with a scene, a number or a before and after, from the ledger only.
8. **Machine tells.** Remove banned words, the "not just A, but B" reframe, dramatic dashes, neat summary endings, stacked rhetorical questions, filler openers about the state of the world. Check {BANNED_WORDS_FILE}.
9. **Grade 3 clarity for public copy.** Short common words, short sentences, active voice. Clarity, not baby talk.
10. **Voice protect.** Keep rhythm, vocabulary, jokes and any line the owner clearly liked. Do not change a sentence unless you can say why in one clause. Unusual is not wrong.
11. **Ending.** The last sentence is the strongest, not a summary. It bookends the headline.
12. **Change list,** grouped under cuts, clarity, tone, facts, one line each: what changed, why. Then up to three questions about things you did not change. Word count before and after.
13. **Lint.** Apply the style check and the leak check.

## Steps: rewrite mode
Keep the facts and the voice only. Rebuild: hook, one point, proof, action. Match the source length or beat it. Show the draft first, then three to six lines on what was cut, then two alternative openers and two alternative calls to action. If the draft is already close and mostly the owner's, switch to edit mode and say why.

## Steps: review mode
Top three to five problems, each naming the rule it breaks. Then the full rewrite. Close with a single sentence that names what you cut and the reason.

## Gate
- The style check passes.
- The fact inventory before and after is identical.
- The piece's one-line summary is a sentence the reader could repeat.

## Output
```
EDITED DRAFT (ready to copy)
...
CHANGES
Cuts: 1. ... because ...
Clarity: ...
Tone: ...
Facts: none changed
QUESTIONS (max 3): ...
Words: <before> -> <after>
Next: yc-launch-copy-honesty-and-fact-gate
```

## If things go wrong
- **Owner pushes back on a change.** Put it back without argument and note the preference. The second time it shows up, it becomes a voice rule.
- **No voice rules.** Stay light and say so.
- **Too long for one pass.** Work section by section, showing each as it lands.
- **An edit would need a new fact.** Leave [NEED: what] instead.
- **Round cap.** Two edit rounds. Then the owner chooses between versions.

## Never
- Never change, add or remove a fact.
- Never sand the owner's voice into house style.
- Never hide a missing fact by smoothing the sentence.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the style check: `python3 scripts/check_style.py <file or folder> [--banned FILE] [--exempt NAME ...]`; the leak check: `python3 scripts/check_leak.py <file or folder> [--terms FILE] [--exempt NAME ...]`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-launch-copy-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
