<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Waitlist Email: Email file format

Every draft is a plain-text block. The header is for the owner and the checks; it is not pasted into the email tool. A blank line ends the header. Everything below it is the email body. Use the email check on these files, not on a whole report.

### Required header
```
Email: 1
Type: launch
Segment: waitlist, has not bought
Exclude: buyers, unsubscribed, complained, open support case
Send: Tuesday 09:00 {LAUNCH_TZ}
Deadline: Thursday 21:00 {LAUNCH_TZ}
Subject: It is ready. Here's what happens next
Preview: The founding plan is open until Thursday.

Hi {FIRST_NAME|there},

[body]

[Get your founding plan today]({CAMPAIGN_URL})

{SENDER_NAME}

P.S. [optional, same offer, new angle]

{UNSUBSCRIBE}
```
This is an example shell. All facts are placeholders.

Types the checks know: announcement, launch, resend, story, answer, proof, demo, founder-note, deadline, last-hours, close, thank-you, welcome, bridge, nurture, note.

`Deadline: none` is valid if the email has no urgency words. `Send:` must always name the audience time zone. For relative triggers use "on signup, {LAUNCH_TZ}".

If using a scarcity count add `Scarcity-source: {SYSTEM}, read {DAY} {TIME} {LAUNCH_TZ}`. A count without that header fails check 5.

### Body rules checked by script (`scripts/check_email.py`) or by hand
- No [NEED: ...] or [placeholder: ...] marks left by the send check.
- A sign-off: {SENDER_NAME}, or add `Sign-off: your sign-off text` in the header.
- An unsubscribe line: {UNSUBSCRIBE} or the word "unsubscribe" linked to the tool's token.
- One primary link destination (repeating the same link in the P.S. is fine). Unsubscribe does not count.
- Link labels: three to eight words, naming what they get.
- Subject at most 45 characters, preview at most 100. No price in the subject.

### Body rules checked by a person
Every amount, term, guarantee and date matches the brief. The email sits inside what people signed up for. The link loads on a phone and shows the same offer. The reply-to inbox is read by a person.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
