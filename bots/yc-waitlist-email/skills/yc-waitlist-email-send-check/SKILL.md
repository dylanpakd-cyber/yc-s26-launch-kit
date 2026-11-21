---
name: yc-waitlist-email-send-check
description: "YC Waitlist Email: use when the owner asks \"is this ready to send?\", final check, lock check; for the pre-send check of a finished draft against locks and rules. Not for drafting or rewriting (email-draft-and-edit)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "is this ready to send?", final check, lock check; this skill covers the pre-send check of a finished draft against locks and rules. WHEN NOT: drafting or rewriting (email-draft-and-edit). One-off asks can load this skill directly; a full run reaches it through yc-waitlist-email-workflow.
# SKILL: send-check

Use when: any draft is about to be shown as final, the owner says "check this email", "run the lock check", "is this ready to send", "show the lock check", or before the owner schedules anything. It is the last gate. Every email passes it, every time.

Purpose: a mechanical lint plus a human cold read. Honesty failures always block. The send check fixes what is wrong in place, keeps the argument at full strength, and says exactly what it changed.

Drafts only: the send check never sends or schedules. A PASS is not permission. Scheduling happens only after PASS and the owner's explicit yes naming the audience, the email and the time. The owner presses the button.

## Inputs
- Draft blocks in the email file format (yc-waitlist-email-references ("Email file format")).
- `brief` (facts sheet) and {EMAIL_LOCKS}.
- {BANNED_WORDS_FILE}, if any.
- `plan` for the exclude list and the run context.

## Order of work
1. **Cold read first.** Before the lint, read the draft once as a customer on a phone, between other things. Use only the lines on the page, not what the plan meant. Answer in writing:
   - What is this email asking me to do, and why now? (One sentence each.)
   - Which exact words made me pause or stop reading? Copy those words into the review.
   - Does the close pay off what the email made me want? Quote the close. PAYS or DOESN'T.
   - Would I believe each proof line, or have I heard that shape so often I tune it out?
   - For a run: does this email repeat a scene or proof moment from another email? The offer block may repeat; scenes and proof moments may not.
   If the answer to the first question is wrong or slow, the email fails. Give the draft to the owner or a fresh reader for the same question when possible.
2. **Run the email check by hand** (yc-waitlist-email-checks). The built-in banned list always applies; add the words from {BANNED_WORDS_FILE} only if the owner pasted a list. Write "checked by hand" in the result. Never claim a check ran when it did not.
3. **Walk the MANUAL items** that need the owner to look in {EMAIL_TOOL}.
4. **Write the verdict.**

## The 14 checks (S = hand check from yc-waitlist-email-checks, M = manual)
1. (S) Banned words: none from the built-in list or {BANNED_WORDS_FILE}.
2. (S) Locks: sign-off present, {UNSUBSCRIBE} or the footer token present. (M) legal or postal line present if the owner's market needs it.
3. (S, against the facts sheet) Every amount in the email appears in the facts sheet. (M) Offer, guarantee and dates match the brief word for word.
4. (S) No [NEED] or placeholder left.
5. (S) No scarcity count without a `Scarcity-source:` header. (M) No invented number, quote or result anywhere; each specific traces to the facts sheet.
6. (S) Subject: present, 45 characters or fewer, no fake "Re:", no all caps, no price, one "!" at most, no emoji. Preview present, not a repeat, 100 characters or fewer. (M) The subject is honest to the content; the first three paragraphs pay it off.
7. (S) One primary link destination, label of three to eight words, no "click here". (M) One job, one action.
8. (S) No dashes as punctuation, no "No X. No Y. Just Z.", average sentence 20 words or fewer, no paragraph over 60 words. (M) Voice rules pass: contractions, address, sign-off.
9. (S) Length inside the band for the type (last hours 120, welcome 200, launch 350 words).
10. (S) Images have alt text; no raw URLs in the body. (M) The plain-text version reads fine.
11. (S) Segment and Exclude headers present; selling emails exclude buyers; everything excludes unsubscribed. (M) The exclude list matches what {EMAIL_TOOL} can really build.
12. (S) Send time has a time zone; urgency words need a real Deadline; Deadline has a time zone. (M) Spacing from the last send respects the cap; the five deadline tests pass.
13. (M) Tracking tags are consistent; the link loads on a phone and shows the same offer.
14. (M) Replies go to an inbox a person reads.

## Leave-out list (write one line per email)
Who must not get this email, and why: buyers of this offer; unsubscribed, complained or bounced; refunded or charged back; open support cases; readers who already declined this promotion; readers receiving a more important flow (delivery, receipt, support messages always win over promotion). The note says it. The owner's tool enforces it.

## True-only-if notes
For any line true only under a condition (stock, date, region, plan type), write the condition and a time-stamped source under the draft. Example: "True only if the checkout still shows the founding price at send time. Owner to confirm Thursday 17:00 PT."

## Fix in place versus flag
- **Fix in place** when a line is wrong as written: a price that differs from the brief, a fake deadline, a wrong link, a selling email to buyers. Correct it and count it.
- **Flag** when a line may be true but cannot be checked: a proof item, a "true only if". Keep the line, add [NEED PROOF] or a note, list one flag.
- Never soften a true, bold line to look safe. Never add hedges that the facts do not need.

## Worked example (invented business, every fact made up)
Draft subject: "LAST CHANCE: founding plan ends!!" Hand-check result: check 6 FAIL (ALL CAPS word; more than one "!"); check 12 FAIL (urgency words but Deadline is none). Fix: subject becomes "Founding price ends at 9 tonight"; Deadline header set to "Thursday 21:00 PT" after the owner confirms the checkout stops then. Second run: all script checks PASS; MANUAL items 13 and 14 ticked by the owner. Verdict: PASS. Send check line: "Send check: 14 checks and a cold read, fixed 2."

## Verdicts
- **PASS:** every hand check passes, every MANUAL item is ticked, the cold read answers are right.
- **FIX:** list the failing checks, first failure named first, with the fixed line. Go back to step 3 or 4.
- **HOLD:** an honesty issue the owner must decide (a claim with no proof, a deadline that may not be real). Nothing moves until the owner answers.
Report line: "Send check: 14 checks and a cold read, fixed [n]." Say "nothing to fix" when n is zero.

Revision cap: two FIX rounds per email. After the second, stop. Show the owner the exact failing check, the line, and two options. Do not loop a third time on your own.

## Gate (exit criteria)
PASS on every draft in the send, the leave-out list written, true-only-if notes written. Then, and only then, ask: "Ready for you to schedule? Reply yes with the audience and the time."

## Failure handling
- Every check is applied by hand; say "checked by hand".
- Facts sheet missing: verdict HOLD; go back to step 1.
- Owner insists on a failing line: record the owner's decision and the check it fails. Do not mark it PASS.

## Output contract
`send-check` in this chat: per email, the cold read answers, the hand-check results, the MANUAL ticks, the leave-out line, the true-only-if notes, the verdict. In chat: the one-line report per email and the three lists (drafted, approved, needs a decision).

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-waitlist-email-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
