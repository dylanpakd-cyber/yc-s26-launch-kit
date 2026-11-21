---
name: yc-launch-ads-creative-qa
description: "YC Launch Ads: use when the owner asks \"review this ad/creative/video/static\", is this asset ready to hand off; for QA of a finished asset: truth, format, destination match. Not for checking a single line or claim (claims-and-preflight)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "review this ad/creative/video/static", is this asset ready to hand off; this skill covers QA of a finished asset: truth, format, destination match. WHEN NOT: checking a single line or claim (claims-and-preflight). One-off asks can load this skill directly; a full run reaches it through yc-launch-ads-workflow.
# SKILL: creative-qa

Purpose: check a finished video or static before any spend. Read the file only. Report each problem with a timecode or a position, so the format desk can fix it in one pass.

## Use when
- A built video or static comes back from the format desk or a creator.
- The owner says "QA this", "check the video", "is this ready to upload", "check the first three seconds", "safe zones".
- After any re-render.

Not for: claim review (yc-launch-ads-claims-and-preflight) or judging whether the idea is good (yc-launch-ads-concept-spec).

## Inputs
- The built file, or stills at each cut plus the transcript if the bot cannot open video.
- The brief it was built from.
- {AD_PLATFORM} and placements (feed, stories, reels). Default: vertical 9:16 with platform UI at top, bottom and right side.
- {BANNED_WORDS_FILE}.

## Steps
1. **Match to brief.** Same concept, same hook per cut, same CTA rule. A mismatch is a FAIL before anything else.
2. **First three seconds (vertical video), each pass or fail:**
   1. A picture is on screen at once. No black frames, no logo lead-in.
   2. Something moves in the first second. No frozen still as the opener.
   3. Sound starts at once, or on-screen text carries the hook with sound off.
   4. Captions read with sound off: large enough, high contrast, two short lines at most.
   5. Nothing important sits under platform UI: captions, badges, CTA, faces.
   6. The mute test: a stranger watching with no sound can say what this is about.
3. **Picture checks:** list of cuts with timecodes; push-ins; frozen stretches; colour outliers; black gaps; format, size, frame rate.
4. **Faces:** face size per shot; captions never cover a face; the same face in too many shots of a "many customers" ad is a WARN.
5. **Sound:** voice clear over music; no hum under pauses; no echo on word endings; loudness within platform norms; no clipped peaks.
6. **Motion in the open.** Something changes on screen every couple of seconds in the first ten. Flat screens under voice-over for long stretches are a WARN.
7. **Words on screen:** run the on-screen text and transcript through the style check and the leak check. Compare every number with the ledger using the facts-ledger check.
8. **Static checks:** text legible at phone size; product not cropped; price or terms correct or absent per {PRICE_RULE}; no generation artifacts, warped hands or banding; one to one with the reference if it is a remake.
9. **Grade:** PASS (no FAIL, no WARN), WATCH (WARN only), REJECT (any FAIL). REJECT blocks upload and any further paid generation.
10. **Review loop.** Collect notes on exact timestamps. Send the FAIL list to the format desk. When it returns, re-run every check, not only the fixed ones.

## Gate
No FAIL items. WATCH items are listed for the owner to accept or fix. Reused scenes across cuts count as one creative in the test plan.

## Output
```
CREATIVE QA: <file name> | <cut>
GRADE: PASS | WATCH | REJECT
FAIL (must fix):
1. 00:00.0-00:00.8 black lead-in. Fix: trim to first frame of the hook shot.
WARN (look at it):
1. 00:04.2 caption sits near the bottom UI band. Fix: raise it above the safe line.
First failing item: <the one to fix first>
Next: re-run QA after fixes, or if PASS, test design in the companion YC Ad Test Desk, then yc-launch-ads-claims-and-preflight Part B
```

## If things go wrong
- **Cannot open the file.** Ask the owner for stills at each cut and the transcript. Run every check you can and mark the rest "not checked".
- **Unsure of the safe zone for a placement.** Use the conservative default: keep key items out of the top 14%, the bottom 20% and the right 12% of a vertical frame. Say it is a default.
- **The fix changes the message.** That is a brief change, not a QA fix. Send it back to yc-launch-ads-reference-to-brief.
- **Same FAIL after two rounds.** Stop the loop. Show the owner the item and two options: accept the risk in writing, or rebrief.

## Never
- Never edit, render or upload the file.
- Never pass an asset with an unsourced number on screen.
- Never ignore captions covering a face, a CTA under UI, or a black open.
- Never trigger paid generation from QA.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-launch-ads-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
