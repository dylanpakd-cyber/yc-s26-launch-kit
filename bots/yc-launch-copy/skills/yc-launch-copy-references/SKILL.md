---
name: yc-launch-copy-references
description: "YC Launch Copy: use when the owner asks \"show me an example\", a blank template, a worked example; for reference material: templates, the prompt set, the worked example and filled examples. Not for doing the step itself (load that step's skill)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "show me an example", a blank template, a worked example; this skill covers reference material: templates, the prompt set, the worked example and filled examples. WHEN NOT: doing the step itself (load that step's skill). One-off asks can load this skill directly; a full run reaches it through yc-launch-copy-workflow.
# YC Launch Copy: references

Templates, examples and reference tables for the YC Launch Copy steps. Everything here is invented and labelled as an example, or is a method, not a result. Copy the shape, never the facts. Never present an example number as the owner's. The checks named here are written checklists in yc-launch-copy-checks, applied by hand.

## Worked example: raw thoughts to a LinkedIn launch post (fictional)

Everything here is invented to show the shape of each step. No real person, clinic, price or result.

### Raw thoughts the owner sends
"we keep missing calls at night, people book elsewhere, I built a text-back thing, pilot soon, idk how to say it without sounding salesy"

### Step 1: clarity interview
The bot asks one question at a time: who is it for, what do they try today, what made you build it, what can you prove. The owner pastes a week of the clinic's call log. Ledger rows go in with sources (see the ledger example in yc-launch-copy-references). Five pinpoint candidates. The chosen one passes the stranger and two-year tests (see the pinpoint-card example in yc-launch-copy-references).

Play-back:
1. Pinpoint: small clinics lose bookings at night because nobody answers after six.
2. For: owners of small clinics who check missed calls every morning.
3. Proof: 31 missed after-hours calls in one week; texts go out within 60 seconds.
The owner replies "yes".

### Step 1b: writing room (optional)
The owner uses an outside writing tool. The bot prepares the "six openers" prompt from yc-launch-copy-references ("Prompt set"), strips the clinic's name, and shows it. The owner says "ok to share". The owner pastes the reply back. See the room-log example in yc-launch-copy-references. The bot shows it unedited and flags one line: "most clinics lose a fifth of bookings" is not in the ledger.

### Step 2: outline
See the outline example in yc-launch-copy-references (the fields check (outline) PASS). Shape: story. Opening: the missed-call number. Beats: people booked elsewhere; the fix; the pilot. Teach before pitch: N/A (under 150 words).

### Step 3: hooks
Eleven lines written (six openers, five antithesis), the weakest dropped, ten gated, eight killed (two failed "fresh", three failed the length cut, three had no ledger number). See the hooks example in yc-launch-copy-references. The hook check passes both finalists.

### Step 4 and 5: draft and edit
See the draft example in yc-launch-copy-references (LinkedIn) and the x-post example in yc-launch-copy-references (X); the channel check passes both. The edit cut an opening line ("I've been thinking a lot about clinics lately") and moved the number to line one. Words: 71 to 52.

### Step 6: honesty gate
The facts-ledger check passes: 31, 60 and 20 all have sourced rows. Honesty bar 5 of 5. The honest admission is "we never knew their names". Draft score in the draft-score example in yc-launch-copy-references passes the ship rule.

### Step 7 and 8: hand-off
1. LinkedIn post (recommended), link in the first comment.
2. X version: same first line, link above "Show more".
3. Satellite: "Why voicemail is a booking leak" for day two.
The owner posts by hand.

## Fill-in templates: YC Launch Copy

Fill every field, then run the check named under it. Leave [NEED] for missing facts. The checks fail on [NEED], so nothing half-filled moves on.

### 1. Pinpoint card
Check: The fields check (pinpoint)
```
Pinpoint:
Reader:
Problem:
Benefit:
Emotion:
Action:
Stranger test: YES | NO
Two-year test: YES | NO
Proof 1:
Proof 2:
```

### 2. Facts ledger
Check: The facts-ledger check, then the facts-ledger check
```
- <fact with its number> | source: <where, {DATE}>
- <fact not yet proven> [NEED]
```

### 3. Room log
Check: The fields check (room-log)
```
Room: {WRITING_ROOM} | in-house
Prompt: <exact prompt, or a pointer to the block below>
Reply: <unedited, or a pointer to the block below>
Owner approved sharing: YES
Fact flags: <list, or none>
```

### 4. Outline
Check: The fields check (outline)
```
Pinpoint:
Promise:
Opening:
Beat 1:
Beat 2:
Beat 3:
Turn:
Action:
Teach before pitch: YES | N/A
```

### 5. Hooks file
Check: The hook check
```
<first line> | gate: Y Y Y Y Y Y Y Y | score: q1 q2 q3 q4 q5 | claimed: PASS
```
Gate order: context, curiosity gap, concrete, voice, honest payoff, fresh, survives the 130-character cut, sayable in one breath.

### 6. Draft score
Check: The fields check (draft-score)
```
Channel:
Pinpoint:
Clarity:
Specificity:
Voice:
Honesty:
Payoff:
Reason for lowest score:
```

### 7. Post skeleton (X or LinkedIn)
```
Line 1: the hook (works alone, under 130 characters)
Line 2: does a paragraph's work: what it is, for whom, why now
Lines 3 to 6: proof, a scene, one number from the ledger
Quotable line: one sentence worth reposting
Close: the strongest sentence, or one genuine question
Link: above "Show more" on X | first comment on LinkedIn
```

### 8. Draft file header (for the channel gate)
Check: The channel check (x) (or linkedin)
```
Idea: <one sentence>
Link placement: in post | reply | first comment | none

<post body; for an X thread, split posts with a line holding only --->
```

### 9. Review output
```
Top problems (3 to 5), each naming the rule it breaks:
1. ...
Full rewrite:
...
Cut and why (one line):
Word count: before <n>, after <n>
```

## Prompt set: YC Launch Copy

Plain-language prompts for yc-launch-copy-writing-room. Fill every slot in braces or angle brackets. Always state platform, reader and goal. Strip private data before sharing any prompt with an outside tool.

### 1. Pinpoint session (no draft yet)
"Act as my editor, not my writer. Do not draft anything. Ask me one question at a time and wait for my answer. Push back when I am vague. Keep going until we have five clear answers: the exact problem, whose problem it is, the concrete benefit, the feeling the reader should leave with, and the one action I want. Topic to start from: <topic>. Ask your first question."

### 2. Two-year lessons
"Two years ago I was <then>. Today I am <now>. List five specific lessons I learned between those points that I could teach my past self. Use only what I told you. Mark any lesson you had to assume."

### 3. Six openers
"My core point is <pinpoint>. Reader: <reader>. Platform: <platform>. Write six first lines, one of each: a flat declaration, a question that makes them think, a vulnerable admission, a contrarian opinion, a number (only from these facts: <ledger facts>), and a moment in time."

### 4. Antithesis openers
"Main idea: <idea>. Write five first lines that state the obvious view and then flip it to the less obvious truth. Keep each under 130 characters."

### 5. Four-angle headlines (4A)
"Topic: <topic>. Reader: <reader>. Write twelve headlines, three of each kind: actionable (how to do it), analytical (why it works), aspirational (you can do this too), and human nature (the psychology underneath)."

### 6. Clear headline, five parts
"Write ten clear headlines for <topic>. Each holds a number, the specific reader, a concrete noun, a measurable outcome, and what the reader loses by skipping it. Clear beats clever. Use only these facts for numbers: <ledger facts>."

### 7. Short essay outline
"Topic <topic>, points <a, b, c>. Outline it as: hook, a one-sentence promise, three points of one or two sentences each, and a final takeaway that answers the hook."

### 8. Pain, dream, fix
"Teach <reader> how to get <outcome>. Describe the painful now, the better state, and three steps between them. No product mention until the last line."

### 9. What, how, why
"Concept: <concept>. Give a plain definition, three concrete steps, and three reasons it matters to <reader>."

### 10. Ten expansions
"Expand this point ten ways: a tip, a data angle (only my data: <ledger facts>), step by step, a lesson learned, a benefit, a reason why, a common mistake, a real example, a provoking question, and a personal story prompt for me to fill in."

### 11. Atomize long form
"From this section, write five standalone short posts: a one-line declaration, an antithesis, a three-bullet list, a mistake and its fix, and a question that starts a conversation. Section: <text>."

### 12. Sentence polish
"Rewrite this sentence three times, each tighter than the last. Put the strongest word last. Cut a third to a half of the words. Two commas at most. Drop tiny-word clusters and -ly adverbs. Say why for each. Sentence: <text>."

### 13. Revelation audit
"Mark every sentence in this draft that tells the reader nothing new. Then cut a third of the draft so every sentence moves forward. Then rewrite it to lead with the punchline. Draft: <text>."

### 14. Throat-clearing cut
"Audit this opening. Cut the warm-up so the core point lands in the first two sentences. Explain each cut. Opening: <text>."

### 15. One, three, one
"Rewrite this as one short declarative line, three lines of explanation, and one punchy closing line. Text: <text>."

### 16. Long-form diagnosis (diagnose, do not rewrite)
"Score this piece 1 to 5 on: throat-clearing, one-sentence openers for the piece and each section, rate of revelation, rhythm and white space, and whether the last line closes the headline's loop. Quote the worst line for each. Do not rewrite. Piece: <text>."

### Hook rewriter
"Platform: <platform>. Draft hook: <hook>. Where does it sound generic? Give three rewrites that keep my facts."

## Examples (invented)

### Draft score example

### Example draft score (fictional)

Channel: LinkedIn
Pinpoint: Small clinics lose bookings at night because nobody answers the phone after six.
Clarity: 5
Specificity: 5
Voice: 4
Honesty: 5
Payoff: 4
Reason for lowest score: voice rules are tentative, only three samples so far

### Draft example

Idea: Small clinics lose bookings at night because nobody answers after six.
Link placement: first comment

Last month our clinic missed 31 calls in one week. All after six.

Most of those people booked somewhere else. We never knew their names.

So we built a tiny fix. Miss a call after hours, and the caller gets a booking link by text within 60 seconds.

The pilot opens to 20 clinics. Link in the first comment.

### Hooks example

```
# Example first lines (fictional). Gate order: context, gap, concrete, voice, honest, fresh, length, one breath.
Last month our clinic missed 31 calls in one week. All after six. | gate: Y Y Y Y Y Y Y Y | score: 4 5 5 5 5 | claimed: PASS
Your clinic closes at six. Your phone does not. | gate: Y Y Y Y Y Y Y Y | score: 4 4 4 4 4 | claimed: PASS
```

### Ledger example

### Example facts ledger (fictional)

- 31 missed after-hours calls in one week | source: example clinic call log, {DATE}
- booking link texted within 60 seconds | source: example demo recording, {DATE}
- pilot opens to 20 clinics | source: example founder note, {DATE}

### Outline example

### Example outline (fictional)

Pinpoint: Small clinics lose bookings at night because nobody answers the phone after six.
Promise: You will see where after-hours bookings leak and one way to stop it.
Opening: our clinic missed 31 calls in one week, all after six
Beat 1: most of those callers booked somewhere else, and we never knew their names
Beat 2: voicemail feels like a safety net but works like a leak
Beat 3: the fix: a missed call after hours gets a booking link by text within 60 seconds
Turn: the problem was never staff effort; it was the hours
Action: join the pilot waitlist, link in the first comment
Teach before pitch: N/A

### Pinpoint card example

### Example pinpoint card (fictional founder and product, invented for illustration)

Pinpoint: Small clinics lose bookings at night because nobody answers the phone after six.
Reader: The owner of a two-room physio clinic who checks missed calls every morning and winces.
Problem: Calls after closing go to voicemail and most callers book elsewhere.
Benefit: Every after-hours caller gets a booking link by text within a minute.
Emotion: relief that the phone stops being a nightly leak
Action: join the waitlist for the pilot
Stranger test: YES
Two-year test: YES
Proof 1: 31 missed after-hours calls in one example week from the founder's own clinic log
Proof 2: pilot texts sent within 60 seconds in the example demo

### Room log example

### Example room log (fictional)

Room: the owner's outside writing tool
Prompt: prompt 3 (six openers) from yc-launch-copy-references ("Prompt set"), filled with the pinpoint and reader; clinic name removed before sharing
Reply: pasted back by the owner and shown unedited in chat (six lines, not repeated here)
Owner approved sharing: YES
Fact flags: 1. "most clinics lose a fifth of their bookings" not in ledger, needs a source or removal

### X post example

Idea: Small clinics lose bookings at night because nobody answers after six.
Link placement: in post

Last month our clinic missed 31 calls in one week. All after six.

So we built a fix: miss a call after hours, and the caller gets a booking link by text within 60 seconds.

The pilot opens to 20 clinics: {CAMPAIGN_URL}

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
