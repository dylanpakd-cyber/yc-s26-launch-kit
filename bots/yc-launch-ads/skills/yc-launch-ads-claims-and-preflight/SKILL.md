---
name: yc-launch-ads-claims-and-preflight
description: "YC Launch Ads: use when the owner asks \"can we say this?\", \"check this line/claim before it runs\", compliance; for checking a line, claim or ad against the claim locks and banned words before it runs. Not for visual or format QA of a finished asset (creative-qa)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "can we say this?", "check this line/claim before it runs", compliance; this skill covers checking a line, claim or ad against the claim locks and banned words before it runs. WHEN NOT: visual or format QA of a finished asset (creative-qa). One-off asks can load this skill directly; a full run reaches it through yc-launch-ads-workflow.
# SKILL: claims-and-preflight

Purpose: two gates. Part A checks every claim and the honesty bar at the script step. Part B is the last check before anything goes live. Both keep the line strong. The job is to find proof or the strongest compliant rewrite, never to sand the copy down.

## Use when
- Part A: right after a script, a static or any copy is drafted. Triggers: "can we say this", "where's the proof", "will this get rejected", "claims check".
- Part B: right before the owner launches. Triggers: "is this ready", "preflight", "can we launch", "final check".

## Inputs
- The asset (script cuts, static copy, headline, primary text).
- brand pack (never-claims) and {CLAIM_LOCKS}.
- The facts ledger: one fact per line with "source:" (template in yc-launch-ads-references ("Templates")).
- {AD_PLATFORM} and the surface (feed, stories, search).
- For Part B: {CAMPAIGN_URL}, the test card, tracking setup notes from the owner.

## Steps: Part A, claims and honesty gate
1. **List every claim verbatim:** numbers, results, comparisons, mechanisms, testimonials, guarantees, time frames, "only", "first", "best".
2. **Lane each claim** (detail in yc-launch-ads-references ("Claims lanes and policy")):
   - Green: supported by a ledger row. Ships at full strength.
   - Yellow: true only with a condition. Add the condition in the wording.
   - Owner-approved: cleared by the owner with conditions. Flag a missing condition.
   - Red: cannot be supported, health or money fear bait, fake or implied expert endorsement, regulated outcome.
3. **Run the ledger check.** Apply the facts-ledger check. Every number in the asset must match a sourced row.
4. **Platform risk.** Name the surface. Platform rules change, so say "checked against current rules on {DATE}" or "dated snapshot, verify before launch". If a line is likely rejected, name the rule and give an alternative route: a different framing with the same pressure, a different proof, or a different surface.
5. **Rewrite every non-Green claim** to its strongest compliant version, with the ledger row it rests on or the placeholder that would fill it (for example "[your real sign-up count]"). Never weaken a claim you can prove. Find the proof instead.
6. **Honesty bar, all five yes:**
   1. Every fact is checkable and true today.
   2. No scarcity or deadline that is not real.
   3. No promise bigger than the real offer.
   4. One honest damaging admission if it fits naturally (never faked; if it costs nothing to say, it is not one).
   5. The line is fair if the buyer gets exactly what was said.
7. **AI or "smart" products:** scope claims to what works today. No mind-reading implications.

## Steps: Part B, launch preflight
Mark each item pass, should-fix, or fix-before-launch.
- **A. Fix before launch:** no made-up specifics or unfilled placeholders; no Red claim or surface-policy clash; tracking intact (right destination, consistent campaign tags, the result event fires, offer and price on the asset match the page); specs valid (format, aspect, length, character limits, captions).
- **B. Concept complete:** the concept card passed the fields check (concept) and the test card passed the fields check (test-card). The test card comes from the companion YC Ad Test Desk, which the owner may install, or the owner pastes their own; with no test card, item B does not pass.
- **C. Message:** hook matches awareness; the six jobs (attention, awareness, education, desire, justification, action) are covered in proportion; the first screen of the asset carries the hook.
- **D. Language and brand:** native market language; copy and picture point at the same proof.
- **E. Offer:** offer, price and guarantee the same on ad, page and checkout.

## Gate
- Part A passes when the facts-ledger check passes, there are no Red claims, and the honesty bar is 5 of 5.
- Part B returns READY (all pass), READY WITH FIXES (only should-fix items), or FIX FIRST (any fix-before-launch item). Only READY or READY WITH FIXES goes to the owner for a yes.

## Output
Part A, after the asset:
```
Flags:
"<quoted line>" | lane | what it needs or what is likely to happen | strongest rewrite (loud flags only)
Honesty bar: 5/5 | Ledger check: PASS
```
Green claims get no line. Nothing to flag, no list.

Part B:
```
PREFLIGHT: READY | READY WITH FIXES | FIX FIRST
Fix before launch: <#: what, where, the fix>
Should fix: <#: what, the fix>
Passed: <short list>
Launch responsibility: owner. Nothing goes live without your typed yes.
```

## If things go wrong
- **No ledger exists.** Build it now from the brand pack and the owner's answers. Every number without a source becomes a placeholder.
- **Owner insists on a Red claim.** State once what is likely to happen (rejection, account risk, legal exposure) and give the alternative route. The owner decides. Log their decision.
- **Unsure of current platform rule.** Say so. Label it a dated snapshot. Recommend the owner check the platform's policy page.
- **Round cap.** Two rounds of Part A rewrites. Still Red: the asset goes back to the brief.

## Never
- Never add hedging, generic disclaimers or a "safe" low-pressure version of an honest line.
- Never treat reviews or comments as proof a mechanism works. They are buyer language.
- Never let a made-up specific pass, in any mode.
- Never launch, publish or edit a campaign. The owner does.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-launch-ads-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
