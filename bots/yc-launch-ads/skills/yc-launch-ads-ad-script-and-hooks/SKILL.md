---
name: yc-launch-ads-ad-script-and-hooks
description: "YC Launch Ads: use when the owner asks \"write/score hooks\", \"write the ad script\", spoken lines, first three seconds; for writing or grading hooks and ad scripts. Not for checking claims (claims-and-preflight) or full concept briefs from a reference (reference-to-brief)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "write/score hooks", "write the ad script", spoken lines, first three seconds; this skill covers writing or grading hooks and ad scripts. WHEN NOT: checking claims (claims-and-preflight) or full concept briefs from a reference (reference-to-brief). One-off asks can load this skill directly; a full run reaches it through yc-launch-ads-workflow.
# SKILL: ad-script-and-hooks

Purpose: write ad scripts that sound spoken, built from real customer language, as three cuts that differ only in the first three seconds. Then score the hooks with arithmetic, not taste, and audit the script.

## Use when
- A brief or concept card is ready and needs words.
- The owner says "write the script", "give me hooks", "three cuts", "score this hook", "grade my hook", "is this hook good".
- A winner needs new hooks (the re-hook list from the companion YC Ad Test Desk's winner read, or the owner's own numbers).

Not for: claim review (Part A of yc-launch-ads-claims-and-preflight runs after this) or final media.

## Inputs
- One avatar with at least five exact phrases from brand pack.
- Awareness level, angle lens, proof available, the objection to handle (from the concept card).
- Format and target length in seconds. Default: 30 seconds.
- {BANNED_WORDS_FILE}.
- Market and language. Default: English, about 2.5 spoken words per second.

## Steps
1. **Read the avatar.** One buyer and their exact words. Mode: broad (rank several concepts) or focused (one buyer). Default focused.
2. **Entry point.** Awareness level and how often the market has heard this claim.
3. **Angle.** One lens: pain moment, failed solutions, identity, comparison without naming a brand, proof, myth-busting, honest admission, desired-outcome day.
4. **Hooks.** Write ten, one per hook type (see yc-launch-ads-knowledge). Keep three. Save the rest to the hook bank with their source phrase.
5. **Framework.** Pick one script structure by awareness, length and format (see yc-launch-ads-references ("Hook and script library")). Cold and short: problem first. Warm: proof or offer first.
6. **Body in seven beats,** filled from customer words: hook, problem, belief shift, proof, objection, offer, call to action. Pick one body format: story, analogy, steps, maxim, whiteboard, interview turn, qualifiers.
7. **Three cuts.** Same body. Only the hook changes. Each cut has a target length in seconds.
8. **Voice pass.** Read aloud with a timer. Targets: a quarter or more of sentences under eight words; at least one long sentence in a 30 second ad; some fragments; some sentences that start with "and", "but" or "so"; contractions; no essay connectors. The spoken estimate must land within two seconds of the target length.
9. **Quality audit.** Trace every number and quote to the ledger or delete it. Remove filler that sounds machine-made. Check the seven beats are all present.
10. **Hook score (five questions, 1 to 5 each):**
    1. Is it a callout or an open loop?
    2. Would the buyer say it out loud to a friend?
    3. Would a stranger with no context understand it?
    4. Is it free of insider words?
    5. Is it concrete enough to picture?
    PASS when every score is 3 or more, question one is 4 or more, and the average is 4.0 or more.
11. **Video hook grader** (for video cuts). Score twelve checks 0 to 10: context on mute within about two seconds (counts double); one specific curiosity gap about a topic already recognized (counts double); words, voice and picture agree (mute pass, eyes-closed pass, sound-on pass); proof or stake right behind the claim; contrast between old belief and new reality; a specific turn, not a generic lesson; stakes for the speaker and desire for the viewer; the next line raises the stakes; proof is owned, not borrowed; a fingerprint (if any brand could say it, score low); payoff honesty; format fit (opens inside a real moment). Weighted average = (2 x context + 2 x curiosity + the other ten) / 14. If context or curiosity is 3 or less, the score caps at 5.0. PASS at 7.0.
12. **Run the arithmetic.** Put the three hooks in a list, one per line, in the format shown in the hook check. Run the hook check. Fix any hook whose written verdict disagrees with the math.
13. **Ads harsh read, six yes/no.** The hook score passes; the honesty bar is 5 of 5; the first three seconds pass the mute test; a stranger gets the point in one view; the payoff matches what the destination promises; there is one line a viewer would repeat. Any no: rewrite that part.
14. **Lint.** Apply the style check and the leak check on the script.
15. **Save** the script, an index line, and grow the hook bank.

## Gate
- The hook check passes for all three hooks.
- Voice pass length lands within two seconds of target.
- Every number and quote is in the ledger.
- Ads harsh read is six of six yes.
- The style check passes.

## Output
```
SCRIPT: <concept> | <format> | <length>s | Avatar: ...
CUT A hook: ... | score: q1 q2 q3 q4 q5 = avg | grade: x.x
CUT B hook: ...
CUT C hook: ...
BODY (shared):
[0-3s] HOOK (varies by cut)
[3-8s] PROBLEM ...
[8-14s] BELIEF SHIFT ...
[14-20s] PROOF ...
[20-25s] OBJECTION ...
[25-30s] OFFER + CTA ...
Voice pass: <PASS/FIX with numbers> | Audit: <PASS/FIX>
Next: yc-launch-ads-claims-and-preflight Part A
```

## If things go wrong
- **No hook passes.** Go back to customer phrases. The best hooks are usually a buyer's own sentence, trimmed.
- **Context fights "no product in the hook".** Show the situation without a pitch in the first two seconds. Show the product later. Name the tradeoff.
- **Script runs long.** Cut the belief-shift beat first, then the objection. Never cut the proof.
- **Thin avatar (under five phrases).** Write one cut, not three, and label it "thin pack".
- **Round cap.** Two rewrite rounds. Then hand over the best three with their scores and the owner chooses.

## Never
- Never invent proof, quotes or numbers.
- Never open on a slogan. Open on a spoken moment or a visible problem.
- Never put captions over a face.
- Never show the product first unless the owner asks or the audience is warm.
- Never present a hook score as a performance prediction. It is a rubric read, not a forecast.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-launch-ads-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
