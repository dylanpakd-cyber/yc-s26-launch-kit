---
name: reference-teardown
description: "YC S26 Launch Kit, shared: use when the owner hands over one reference video, ad, launch film or short and asks to break it down, clone its format, say why it works, or turn it into a shot list. Produces a measured teardown (cut map, style spec, per-cut motion, transferable format). Not for writing the brief itself (the owning bot's brief or script skill)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# Reference teardown

The law: never invent a concept from nothing. Every concept, scene, frame or script starts from a named reference whose beat order is measured first. This skill produces that measurement.

Tools: phases 1 and 2 need a shell with ffmpeg. If the agent cannot run commands (a Grok Bot template runs no scripts), ask the owner for stills at each cut and the transcript, do phases 1 and 2 by eye, and mark every number "estimated, not measured".

## The split of instruments
- ffmpeg says WHERE the cuts are. Never take shot boundaries from a model; models over- and under-segment.
- Extracted frames measure the PIXELS: palette hexes, type size in px, composition.
- A video-capable model reads MOTION, pacing, audio and the slop verdict. Never grade motion, pacing or slop from a still.
- Where they disagree: pixels win on look, the video model wins on motion.

## Phase 0: intake
1. Get the file (a local path, or a download the owner is allowed to make). If no reference was given, ask for one. That is the one question worth blocking on.
2. `ffprobe` for duration, fps, resolution, aspect, audio stream.
3. Ask, or infer and state, what we plan to BUILD from it (the target beat).

## Phase 1: cut map
```bash
ffmpeg -v error -i REF.mp4 -vf "select='gt(scene,0.15)',metadata=print:file=-" -f null - 2>/dev/null \
  | grep -oE 'pts_time:[0-9.]+'
```
- Report the raw cut count AND a burst-collapsed count (absorb any sub-0.2 s shot into the one before it). Strobe-cut films over-count at threshold 0.15.
- Make a 1 fps contact strip per 30 s: `ffmpeg -ss T -t 30 -i REF.mp4 -vf "fps=1,scale=256:-1,tile=10x3" strip_T.jpg`.
- Write the CUT MAP, one row per beat: time range, framing, subject and action, on-screen text verbatim, camera, cut type, one palette note.

## Phase 2: style spec (from real frames)
Palette as sampled hexes; typography (family style, weight, colour, shadow, placement, per-word animation); look (grain, contrast, saturation, black level, aspect); composition and light model. Numbers and hexes, never adjectives. "Retro" is banned; give the hex and the px.

## Phase 3: motion, pacing, audio (video model)
Send the clip plus the true cut list plus the contact strips. Ask for: hook mechanism, pacing (average shot length, cut rhythm, energy curve), camera behaviour, voice-over tone, music shape, sync to cuts, authenticity markers. Raise the output cap for long answers. Frame-verify every beat timestamp against the strips; models drift several seconds late in long clips even with pinned cuts.

## Phase 4: per-cut transcription
For every cut: duration in frames, each element, enter frame and mechanism, settle frame, exit, camera move, transition into the next cut, micro-motion. Numbers only.

## Phase 5: the record
1. Visual-system spec. 2. Cut map. 3. Per-cut transcription.
4. THE TRANSFERABLE FORMAT: strip the subject, keep the recipe (hook type, beat count and cadence, caption system, colour-to-emotion map, audio bed shape, escalation curve).
5. What each reference line SELLS (its job), so a rewrite keeps the job, not just the shape.
6. A shot list ready for production, one row per beat.
7. Tags: platform, format, hook type, one line "why this is the bar".

## Laws
- One reference per teardown, end to end. Study material only; never reuse its footage or a creator's voice in shipped work.
- Take the reference's APPROACH, not a line-for-line copy. Source concept rounds from a wide spread (film, TV, animation, ads); at most one card per source. Tech launch films are for clarity, not ideas.
- Done means a fresh agent can rebuild the format without re-watching. Adjectives mean not done.
- Outside view counts are attention signals about the reference, never proof for the owner's product.
- No em dashes in any copy.

## Where it plugs in
- YC Launch Ads: before yc-launch-ads-reference-to-brief, so the brief rests on a measured cut map.
- YC X Launch Desk: before yc-x-launch-desk-founder-post-and-video-script when the owner wants a launch video "like this one".
- YC Ad Test Desk: step 4 of yc-ad-test-desk-winner-decode-and-iteration (storyboard each winner) when the agent can run ffmpeg.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
