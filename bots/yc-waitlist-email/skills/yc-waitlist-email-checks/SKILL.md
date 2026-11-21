---
name: yc-waitlist-email-checks
description: "YC Waitlist Email: use when the owner asks \"lint this email\", check the run plan, check the brief, banned words or subject length; for the written hand checks the steps apply: brief, run plan and the 14-point email check. Not for the full pre-send verdict with the cold read (send-check)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "lint this email", check the run plan, check the brief, banned words or subject length; this skill covers the written hand checks the steps apply: brief, run plan and the 14-point email check. WHEN NOT: the full pre-send verdict with the cold read (send-check). One-off asks can load this skill directly; a full run reaches it through yc-waitlist-email-workflow.
# YC Waitlist Email: hand checks

This bot has no scripts and runs no code. Every check named in the other skills ("the style check", "the email check" and so on) is one of the written checklists below. Apply it by hand, line by line, on the text in this chat. Then print each check as PASS or FAIL with the line that failed, and add the words "checked by hand" to the result. Never edit a draft only to make a check pass; fix the real problem or report it.

Every check gives one of three results: PASS, FAIL (list each failing line and why), or CANNOT CHECK (the input is missing; ask the owner for it).

## Brief check (step 1)
The facts sheet and voice profile are "Key: value" lines.
1. Present, not blank, not [NEED]: Offer, Price rule, Guarantee, Launch date, Close date, Time zone, Segments, Signup promise, Primary action, Support route.
2. Never claims: 3 or more items separated by ";".
3. Voice source: "approved samples" or "default starter voice".
4. Avg sentence words: a number from 5 to 25.
5. Contractions: yes or no.
6. Sign-off: present.
7. Banned words: present (it may say "built-in list only").
8. Links per email: 1 or 2.

## Run-plan check (step 2, before any email past email 1 is drafted)
The run plan is a table: Email | Day | Segment | Type | Job | Doubt | Subject angle | Link | Deadline | Exclude | Status.
1. Every column present and every cell filled ("none" or "n/a", never blank).
2. One job per email: no "and", "&", "+", ";" or "/" in Job.
3. Every selling email (launch, resend, reminder, answer, demo, proof, objection, story, founder-note, deadline, last-hours, announcement) excludes buyers and unsubscribed people.
4. One deadline for the whole run: every Deadline that is not "none" is identical and names a time zone.
5. A run with a deadline has a last-hours email and a close email.
6. No two emails of the same type back to back.
7. A run of five or more has at least one proof or demo email and one answer or objection email.
8. Answer and objection rows name the doubt.
9. One link per row.
10. Persuasive sends to the main segment are at or under the cap (default 9).
11. Status is planned, draft or owner-approved. This bot never writes sent or scheduled.
12. Plan-approval gate: Status reads owner-approved only after the owner says yes to the plan in chat.

## Email check (the hand-check half of the 14-point send check)
Each draft has a header (Email, Type, Segment, Exclude, Send, Deadline, Subject, Preview) above the body. Mark each point PASS, FAIL or MANUAL (a person must look in {EMAIL_TOOL}).
1. Banned words: none of delve, tapestry, crucial, pivotal, testament, underscore, showcase, foster, harness, unlock, elevate, empower, seamless, effortless, holistic, transformative, unparalleled, vibrant, robust, streamline, game-changer, game changing, supercharge, leverage, groundbreaking, world-class, best-in-class, "we're thrilled", "excited to share", "I hope this finds you", "let's dive in", "click here", "learn more", "read more", "just checking in", "act now", "once in a lifetime", "lowest price ever", "selling fast", "don't miss out", or any word from {BANNED_WORDS_FILE}. Check every form of each word (seamlessly, unlocks, leverages).
2. Locks: {UNSUBSCRIBE} and a sign-off ({SENDER_NAME} or the brief's sign-off) are present.
3. Offer facts: every money amount in the subject or body appears in the facts sheet; terms match it.
4. No [NEED] or placeholder note left open.
5. No unverified scarcity ("only 3 left", "spots left", "almost gone") unless a Scarcity-source header names the system and time it was read.
6. Subject and preview: a subject exists, 45 characters or fewer; no fake "Re:" or "Fwd:"; no ALL CAPS word of 4 or more letters; at most one "!"; no price in the subject; no emoji in the subject; a preview exists, 100 characters or fewer, and does not repeat the subject.
7. One job, one primary link (one destination; close, note and bridge emails may have none), and each link label is 3 to 8 words naming what the reader gets.
8. Voice basics: no em or en dash and no double hyphen; no "No X. No Y. Just Z." flip; average sentence 20 words or fewer; no paragraph over 60 words.
9. Length band for the type: last-hours 120 words, close 150, welcome 200, announcement 200, thank-you 200, deadline 250, resend 300, reminder 300, launch 350, anything else 400.
10. Accessibility: every image has alt text; no raw web address in the body.
11. Segment and suppression: Segment and Exclude headers exist; Exclude names unsubscribed; a selling email also excludes buyers.
12. Timing and a real deadline: a Send header with day, time and time zone; urgency words ("ends", "closes", "last chance", "until Thursday", "open through", "by Friday") need a real Deadline with a time zone, never "none".
13. Tracking and mobile load: MANUAL. The owner opens the link on a phone and checks tags in {EMAIL_TOOL}.
14. Replies reach a human: MANUAL. The owner confirms the reply-to inbox is read by a person.
Result: FIX if any point fails; otherwise PASS, then do the MANUAL items and the cold read.

## Leak check
Run on every draft and on anything the owner may share or export. FAIL on any of these:
1. A file path from a computer (a home folder, a workspace folder, a path starting with a tilde).
2. A social handle (an at-sign followed by a name).
3. A money amount written as a currency sign followed by digits that did not come from the owner's sourced facts in this chat.
4. An email address.
5. The name of an outside writer, creator, coach or paid course, unless the owner asked for a credited quote.
6. Any private word the owner listed (their company, product, people or customers) appearing where the text will be shared outside the owner's chat.

## Export check (only when the owner asks to export or copy a skill)
1. The first line of every exported skill is the dylan-pak-credit comment.
2. The last two lines are "Created and curated by Dylan Pak." and the license note.
3. The leak check passes on every exported file.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
