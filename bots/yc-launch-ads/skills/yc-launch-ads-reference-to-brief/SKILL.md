---
name: yc-launch-ads-reference-to-brief
description: "YC Launch Ads: use when the owner asks \"here's a competitor/reference ad, what should we make?\", swipe or remake an ad; for turning one reference ad into a numbered concept brief. Not for scoring hooks alone (ad-script-and-hooks) or judging live results (the companion YC Ad Test Desk)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "here's a competitor/reference ad, what should we make?", swipe or remake an ad; this skill covers turning one reference ad into a numbered concept brief. WHEN NOT: scoring hooks alone (ad-script-and-hooks) or judging live results (the companion YC Ad Test Desk). One-off asks can load this skill directly; a full run reaches it through yc-launch-ads-workflow.
# SKILL: reference-to-brief

Purpose: turn an ad worth learning from, or a passing concept card, into one complete brief that a creator, editor or generation desk can build without asking questions. Borrow structure. Make the concept your own.

## Use when
- The owner shares a reference ad and says "make one like this", "swipe this", "brief this", "turn this into an ad".
- A concept card passed and needs a buildable brief.
- The format desk asks for a brief, a shot list or plates.

Not for: generating or rendering media, or spending. Hand the brief to the format owner.

## Inputs
- A passing concept card (yc-launch-ads-concept-spec), or a reference ad plus an owner note on what to keep and change.
- brand pack.
- Target format and length in seconds. Default: vertical video, 30 seconds.

## Front door (when the output is unclear)
Ask at most two questions: "What are we starting from: an idea, a finished piece, a product or offer, a reference video, or footage?" and "Where should it end up: social post, creator-style ad, launch film, vertical cut-downs, or stills?" Never ask a third. Pick the closest route and say why. Run one route at a time and note the other as Next.

## Steps
1. **Find or confirm the reference.** Prefer long-running public ads with many duplicates, a sign of spend. Save it with a readable name. If the owner left a note (keep, change, hooks, offer), use it as the brief's instruction word for word.
2. **Score swipeability, yes or no for each:** the mechanism transfers to our product; there is one clear problem and payoff; it does not depend on a person, claim or trend we cannot match. Two or more "no": pick another reference.
3. **Break down both tracks.** Words: a transcript. Frames: one still per cut and a beat sheet with timecodes.
4. **Pick the lane.** One to one (swap only the problem and product), swap the mechanism, or keep the structure and rewrite the content.
5. **Audit each element:** keep, translate, or drop. Write one line of why for each.
6. **Translate four things:** problem, mechanism, person, proof. Add language and culture if the market changes.
7. **Payoff check.** Does the new ad deliver what its hook promises, with our real product? Yes or no. No means rework before writing.
8. **Brand check.** Re-run the brand-pack check. If it fails, stop and run the brand pack first.
9. **Script and three hooks.** Hand to yc-launch-ads-ad-script-and-hooks, or write them in place using that skill's rules.
10. **Storyboard.** Mirror the reference shot by shot, with plates: product shots, locations, props, on-screen text.
11. **Fill the brief** from yc-launch-ads-references ("Templates") and run the fields check (brief).
12. **Internal analysis.** Keep the reference breakdown and lane choice in a separate note that is not sent to creators.
13. **Queue discipline for teams.** Give each brief the next free number, never reused. Keep a status: queued, working, done, failed.

## Gate
- The fields check (brief) passes: concept, format, length, avatar, awareness, three hooks, body format, proof, objection, offer, CTA, destination, claim sources and money gates are all filled.
- Payoff check is yes.
- Swipeability has at most one "no".

## Output
```
CREATIVE BRIEF #<n>
Start: <given>   End: <format + surface>
Route: <route> | Lane: <one to one | mechanism swap | structure only>
Concept: <one line> | Avatar: ... | Awareness: ...
Hook A / B / C: ...
Body format: ... | Proof: ... | Objection handled: ...
Offer: ... | CTA: <per {CTA_RULE}> | Destination: {CAMPAIGN_URL}
Claim sources: <ledger rows>
Plates and shot list: ...
Money gates: <steps that need a typed yes>
Next: yc-launch-ads-claims-and-preflight Part A
```

## If things go wrong
- **Reference depends on a celebrity or a trend we cannot match.** Not swipeable. Keep only the beat structure, or pick another.
- **No reference, only an idea.** Skip steps 1 to 5. Build the beat sheet from the concept card and the body format.
- **Payoff check fails twice.** The concept does not fit this product. Return it to backlog.
- **Owner wants a one to one copy of a competitor.** Allowed only for beat structure. Words, footage and claims are never copied.
- **Round cap.** Two drafts of the brief. Then hand over the best with open fields named.

## Never
- Never copy a reference's words, footage, claims or brand assets.
- Never add beats the reference lacked in a one to one remake.
- Never skip the payoff check.
- Never spend, render or publish from this skill.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-launch-ads-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
