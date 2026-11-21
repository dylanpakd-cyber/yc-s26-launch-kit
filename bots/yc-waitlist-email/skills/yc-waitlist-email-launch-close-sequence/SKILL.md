---
name: yc-waitlist-email-launch-close-sequence
description: "YC Waitlist Email: use when the owner asks \"campaign ends Friday\", last days, deadline and close emails; for the close run: deadline, last hours and after-close emails. Not for the welcome flow (welcome-and-nurture)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "campaign ends Friday", last days, deadline and close emails; this skill covers the close run: deadline, last hours and after-close emails. WHEN NOT: the welcome flow (welcome-and-nurture). One-off asks can load this skill directly; a full run reaches it through yc-waitlist-email-workflow.
# SKILL: launch-close-sequence

Use when: the plan is approved and the owner says "write the launch emails", "cart closes Friday", "last call email", "write the close", "the deadline emails", or "what do we send on launch day". Run after step 2. It drafts every selling email from the day before launch to the close note, then hands each one to the send check.

Purpose: write the emails from launch day to the end of the offer, with real scarcity and a clean close. The list is the cheapest source of customers, so the window converts the people who are ready and answers the ones who are not. It does not repeat the warm-up.

Drafts only: this skill writes drafts and a calendar. It never schedules, never sends, never changes the offer. Nothing goes out without the owner's explicit yes naming the audience, the email and the time.

## Inputs
- Approved `plan` (run table, objection matrix, exit rules).
- `brief`: offer block, price rule, guarantee, the real close date and time zone.
- Stock or capacity only if the owner read it from the source system today. Logged with the time.

## The three fixed emails
1. **Announcement, the day before.** Tomorrow it opens; what it is in one line; the date and time. The subject says so plainly. No story wrapper. No link needed, or a link to a preview page if one exists.
2. **The offer, day one.** Lead with what the reader asked for and that it is ready. One paragraph of what it is. The offer block. One button. People who are ready buy at once; do not make them wait through more warm-up.
3. **Last hours, the final day.** Under 120 words. The deadline in the first line. One link. No new arguments; fresh proof at most. Only to people who did not buy. Clickers who did not buy are the best segment.

## The middle (pick from the menu by real objections)
- **Resend to non-openers, next day.** Same job, new subject, new first line. Never a copy and paste. Remove buyers first.
- **Proof.** A sourced outcome from a buyer whose earlier situation matches this reader's, with permission. If none is on file: a demo of the product working.
- **Answer.** One doubt, said once, answered fully, with proof. Strongest feeling first. Price late.
- **One big question.** "Do I need X?" The subject is the question.
- **Who it is not for.** A short list. The right readers recognise themselves.
- **Founder note.** Why this exists and one honest limit. No invented hardship, no guilt, no pressure. Midway, never on launch day.
- **Price against something real.** Only after desire exists. Set the price against what the reader already spends or loses. No invented anchors, no inflated value stacks.

Check the middle has both evidence and an answered doubt. Alternate formats rather than repeating a type. Each sales draft must stand alone, with enough offer detail for a reader who missed the others. As the cutoff nears, cut the body and bring the time into focus. A slow response halfway through is not a reason to add volume. An extra row needs a distinct purpose.

## Deadline day and the close
- **Deadline day (morning).** The real date and time in the first line, what changes after it, and one line on what to do with a last question (reply or the support route).
- **Close note.** Buyers get a thank-you and what happens next. Non-buyers get one gracious line: "It's closed." Add "the next window is [date]" only if a next window is real. Then they go back to normal emails. Do not chase. Do not guilt.

## Scarcity and deadline rules
- Run the five deadline tests (yc-waitlist-email-knowledge) on every deadline line. If any test fails, remove the deadline line and use the cost of waiting or desire instead.
- Consequence beats countdown: say what changes at the deadline.
- A count ("only 40 left") is allowed only if read from the source on the send day, logged with time, and written in the draft header as `Scarcity-source:`. The email check fails a count without it.
- The deadline is stated the same way in every email. It never moves quietly. Reopening needs a new, real reason and the owner's yes.

## The close of each email (the ask)
Each selling email ends with: a turn from the point to the offer; one reason to act (the ongoing problem, the wanted outcome, supporting evidence, self-image, a lighter load, or an enforced cutoff); what it is and who it is for in a clause; the price when price decides it; one conditional invitation ("If you want X without Y, here's where to start."); the link line. Use one reason per email, and never the same reason as the email before. Rotate the shape of the invitation. Never end on "No X. No Y. Just Z."

## Resend, cap and exit rules
- One resend per email at most, to non-openers only.
- Stop selling to a reader after the last-hours email.
- Suppress buyers, unsubscribed, complained and open-support people at every send. Ask the owner to recompute buyers right before each send on the final day. A last call to someone who paid this morning loses trust fast.
- People who clicked and did not buy get at most two short notes inside the window, each answering the likeliest question.
- Replies go to the owner. Draft answers to common replies in the voice. Escalate refund, legal and complaint replies to the owner untouched.

## Worked example: last-hours email (invented business, every fact made up)
```
Email: 6
Type: last-hours
Segment: clicked a launch email, has not bought
Exclude: buyers, unsubscribed, complained, open support case
Send: Thursday 17:00 PT
Deadline: Thursday 21:00 PT
Subject: Founding price ends at 9 tonight
Preview: After that it moves to the standard plan.

Hi {FIRST_NAME|there},

The founding price ends tonight at 21:00 PT.

After that, new plans start at the standard price. The 30-day refund stays the same.

If you want next week planned before Sunday comes, this is the moment.

[Lock in the founding price]({CAMPAIGN_URL})

{SENDER_NAME}

{UNSUBSCRIBE}
```

## Gates (exit criteria)
- Every selling email: real scarcity only, one primary link, offer and price identical to the brief, buyers excluded.
- The run-plan check still passes after any change to the run.
- The email check passes on every draft, then the send check skill runs the manual items and the cold read.
- Scheduling happens only after PASS and the owner's explicit yes naming audience and time. The owner schedules it.

## Failure handling
- Tiny or unengaged list: use the short-run or HOLD path in yc-waitlist-email-waitlist-conversion-plan instead of the default calendar. Never force the full launch sequence onto a quiet list.
- No real deadline: no deadline, no last-hours email. Replace it with a "still deciding?" answer email and a plain close note.
- Owner asks for a fake countdown or a moving deadline: say no in one line, explain the five tests, offer the strongest true version.
- Owner changes the price mid-window: that is a new window. Re-run step 1 and step 2.
- Send check fails: fix in place. Revision cap: two rounds per email; then show the owner the failing check.

## Output contract
All selling drafts in this chat in the email file format, plus a calendar table in chat: day, time with zone, segment, email, chosen subject, resend rule, exclude list. Then three lists: drafted, approved, needs a decision.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-waitlist-email-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
