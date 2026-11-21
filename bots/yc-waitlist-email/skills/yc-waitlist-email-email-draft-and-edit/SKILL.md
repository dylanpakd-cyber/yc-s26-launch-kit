---
name: yc-waitlist-email-email-draft-and-edit
description: "YC Waitlist Email: use when the owner asks \"write/edit/tighten this email\", subject lines, one email; for drafting or editing a single email or subject line. Not for planning the whole sequence (waitlist-conversion-plan)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "write/edit/tighten this email", subject lines, one email; this skill covers drafting or editing a single email or subject line. WHEN NOT: planning the whole sequence (waitlist-conversion-plan). One-off asks can load this skill directly; a full run reaches it through yc-waitlist-email-workflow.
# SKILL: email-draft-and-edit

Use when: a plan row is approved and the owner says "draft email 3", "write the launch email", "tighten this email", "rewrite this", "make it sound like me", or pastes an email to fix. Email only. This bot does not write site copy, landing pages, social posts or DMs; say so in one line and stop if asked.

Purpose: draft, tighten or rebuild one email in the owner's voice from a plan row. One skill, three modes: Draft, Edit, Rewrite.

Drafts only: the output is a draft file. Never paste it into {EMAIL_TOOL}, never schedule it. Nothing goes out without the owner's explicit yes.

## Inputs
- The approved plan row (job, segment, doubt, subject angle, link, deadline, exclude).
- `brief` and {EMAIL_LOCKS}.
- For Edit and Rewrite: the existing draft.

## Draft mode
1. **Pinpoint first.** Before any prose, answer five lines: the exact reader (segment and state), the one question this email answers for them, the one concrete thing they get from reading it, the feeling it should leave, the single action. If any line is blank, the plan row is not ready. Go back to step 2.
2. **Fact inventory.** List every fact you may use, each with its source line in the brief. List every fact you are missing. Missing facts become [NEED: what]. Never invent a number, a quote, a customer, a date or a feature.
3. **Pick the shape** from the plan row's type: announcement, launch, resend, story, answer, proof or demo, founder note, deadline day, last hours, close, thank-you. Shapes are in yc-waitlist-email-knowledge. Worked shells are in yc-waitlist-email-references ("Email shells"). Use the shells for structure only; write fresh sentences.
4. **One version only.** Do not offer three drafts. Pick the best approach and say why in one line.
5. **Write the body.**
   - First line: why this reader is getting this, now.
   - One idea per paragraph. Paragraphs of one to three sentences, under about 45 words.
   - The lead changes per email. The offer block stays the same, copied from the brief. Only the deadline line changes.
   - One action, one primary link. The link label uses three to eight words to name the benefit of the click. Never "click here".
   - The close is one sentence that pays off what the email made the reader want, right before the link.
   - Sign-off from the locks. Then an optional P.S. that adds a new angle (a second doubt answered, the guarantee, an honest "skip this if"). Never a second offer.
   - End with {UNSUBSCRIBE} or the tool's footer token.
6. **Subject and preview.** Write five subject lines using different patterns from yc-waitlist-email-references ("Subject line bank"). Recommend one. Each is 45 characters or fewer, no price, no fake "Re:". The preview text finishes the subject's thought and does not repeat it.
7. **Fill the header** in the email file format (yc-waitlist-email-references ("Email file format")): Email, Type, Segment, Exclude, Send, Deadline, Subject, Preview.
8. **Self-check** against {EMAIL_LOCKS}. Then apply the email check by hand.

## Edit mode (tighten and clean)
1. Inventory the facts. They do not change. Not one word of the offer block changes.
2. Fix clarity: unclear pronouns, a buried point, two jobs in one email.
3. Cut throat-clearing and repeated points. Every sentence must reveal something new; cut the ones that do not.
4. Sentence polish: strongest word near the end, two commas at most, no "-ly" filler, contractions where a person would contract.
5. Fix tone drift against the voice profile. Protect quirks the profile marks as voice.
6. Remove machine tells: dashes as punctuation, "not X, but Y" flips (one per email at most, none in the subject), three-beat drumrolls, staged questions ("The result?"), polished last lines, "No X. No Y. Just Z." endings.
7. Show a short change list: what was cut, moved, and kept on purpose.

## Rewrite mode (rebuild)
Use when the structure fails: two jobs, no clear action, or the cold read in step 7 says a stranger would drop it. Keep only the facts and the voice. Rebuild from the one job: opening, one point, proof, the close, the action. State what was lost on purpose.

## Revision loop
Read it aloud. Remove any sentence that could appear in any brand's email. Replace a vague claim with the concrete fact from the brief, or delete it. Re-run the locks. Ship to the send check only when the one-line summary of the email is a sentence the reader could repeat to a friend.

Revision cap: two rounds per email inside this skill. After two, hand it to the send check with the open issues listed. Do not loop a third time without the owner.

## Worked example (invented business, every fact made up)
Plan row: Email 5, answer, doubt "is it worth it", close Thursday 21:00 PT.

```
Email: 5
Type: answer
Segment: waitlist, has not bought
Exclude: buyers, unsubscribed, complained, open support case
Send: Thursday 08:00 PT
Deadline: Thursday 21:00 PT
Subject: Is it worth it? Fair question
Preview: Here's the math I'd do in your seat.

Hi {FIRST_NAME|there},

A few of you replied with the same question. Is the founding plan worth it?

Here's how I'd check. Count the nights you stand at the fridge with no plan. For most of our testers it was four a week.

Example Planner builds the week and the shopping list in about five minutes. If it doesn't save you time in the first month, the 30-day refund covers you.

The founding price ends tonight at 21:00 PT. After that it moves to the standard price.

[Start your founding plan today]({CAMPAIGN_URL})

{SENDER_NAME}

P.S. If you already plan every meal on Sunday, you may not need this. Hit reply and tell me how you do it.

{UNSUBSCRIBE}
```
Note: "four a week" and "about five minutes" are allowed only because the invented brief lists them with a source. In a real draft, any number not in the brief is [NEED].

## Rules
- Never change a fact in Edit mode. Never include a claim not in the brief.
- Avoid filler words (the built-in banned list in the email check), the "it is not just X, it is Y" pattern and neat summary endings.
- Never imitate a real person's writing beyond the owner's approved samples.

## Plan-approval gate and scope
- Email 1 may be drafted on request. No email past email 1 is drafted until the owner has approved the run plan in chat (yc-waitlist-email-waitlist-conversion-plan).
- Email only: no site copy, social posts or ads. If the owner asks for those, say which other desk owns them.
- A first email to the waitlist carries no buy link unless the approved plan puts one there.

## Gate (exit criteria)
Fact inventory matches the brief. No invented claims. Five subject lines with one picked. Header complete. The email check has no FAIL other than check 4 ([NEED] left), which the owner must fill before the send check.

## Failure handling
- Plan row unclear: go back to step 2 with the exact question.
- Fact missing: [NEED: fact] in the body, listed once in a fill-in list under the draft.
- Owner hates the draft: ask which line feels wrong, then Rewrite mode. Still within the revision cap.

## Output contract
One block per email, headed `email-nn`, in the email file format. In chat: the draft, the five subject lines with the pick, the fact line ("facts used: n, [NEED]: list"), the lock-check result and the five scores from yc-waitlist-email-workflow.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-waitlist-email-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
