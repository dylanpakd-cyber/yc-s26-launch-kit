---
name: yc-waitlist-email-email-brief-and-voice
description: "YC Waitlist Email: use when the owner asks \"set up our voice\", style guide, what this email should do; for the email brief and voice guide before drafting. Not for the final check before a send (send-check)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "set up our voice", style guide, what this email should do; this skill covers the email brief and voice guide before drafting. WHEN NOT: the final check before a send (send-check). One-off asks can load this skill directly; a full run reaches it through yc-waitlist-email-workflow.
# SKILL: email-brief-and-voice

Use when: the owner starts a new launch, asks to "set up the emails", "lock the voice", "build the email brief", "read my locks", or any later step finds a fact missing. Run it first on every new campaign. Do not use it to write emails; it only locks facts and voice.

Purpose: lock the facts and the voice before a single email is drafted. This merges brand facts, voice profiling and the email brief into one pass. Every later step reads its output and nothing else.

Drafts only: this skill writes files for the owner. It never sends, schedules or touches {EMAIL_TOOL}. Nothing goes out without the owner's explicit yes.

## Inputs
- Owner answers to the first-run questions (below).
- The signup page and the sales page at {CAMPAIGN_URL}, pasted or described by the owner.
- Approved past emails or newsletters, if any. Only ones the owner says are "us".
- {BANNED_WORDS_FILE}, if the owner has one.

## First-run questions (one at a time, save each answer)
1. What is the product, in one line a stranger would understand? ({PRODUCT})
2. What exactly is the offer today: what buyers get, the terms, the guarantee wording? ({OFFER})
3. How may the price be stated? Default: copy it from the checkout page on the day. ({PRICE_RULE})
4. When does the window open and close, with the time zone? ({LAUNCH_DATE}, {CLOSE_DATE}, {LAUNCH_TZ})
5. Does the checkout really stop or change the price at the close? (If no, there is no deadline.)
6. What email tool do you use, and which segments can it build? ({EMAIL_TOOL}, {LIST_SEGMENTS})
7. What did the signup page promise people? Paste the exact words.
8. Who sends the emails and how do they sign off? ({SENDER_NAME})
9. Why did you build it, in one true line? ({FOUNDER_STORY_ONE_LINE})
10. What must the product never claim? Give at least three.
11. Do you have past emails you are proud of? Paste up to five, or say "none".

If an answer is "I don't know", write [NEED: that fact] and move to the next question. Never fill it from the site's tone.

## Part A: facts sheet
Build a facts sheet in "Key: value" lines so the brief check can read it. Template: yc-waitlist-email-references ("Brief and voice template"). Every line is tagged with its source ("owner", "checkout page", "signup page") or [NEED]. Copy the guarantee and the offer word for word. Do not round prices. Do not shorten terms.

Rules for facts:
1. A fact is something the owner said, or the page says in plain words. Tone is not a fact.
2. If the page and the owner disagree, ask which is current. Do not pick.
3. A number with no source is [NEED: source for this number].
4. Customer quotes need the owner's permission to appear in an email. Default: no permission.

## Part B: the voice profile
**Path 1, the owner has approved samples (three or more).** Pull measurable rules, not adjectives:
- Average sentence length and range. Share of fragments. Paragraph length.
- Contractions: yes or no, and how often.
- How the reader is addressed, and the sign-off.
- Opening and closing habits. How humour shows up, if at all.
- Words always used. Words never used. Punctuation habits (exclamation marks, emoji). Dashes are never used, whatever the samples do.
- Formatting: bullets, bold, links per email, length per email type.
Include three short excerpts as "this is us" examples. Mark any rule backed by fewer than three samples as tentative.

**Path 2, the owner has no past emails.** Use the default starter voice from yc-waitlist-email-references ("Brief and voice template"): plain, warm, first person, average twelve words per sentence, contractions yes, one link, signed with the first name. Write "Voice source: default starter voice" in the brief. After the owner approves the first three drafts, re-run Part B on those three as the samples and update the profile. Tell the owner this will happen.

**Path 3, one or two samples.** Start from the default starter voice and change only the rules the samples clearly show. Mark those rules tentative.

## Part C: style guide and locks
Turn the profile into a one-page guide: tone, structure, content per email type, language rules, formatting, audience, and a do and don't list. Then write the locks. Locks are hard rules a script or a careful reader can check without judgment:
- banned words (the built-in list plus {BANNED_WORDS_FILE});
- the sign-off line;
- the required legal or footer line, and the unsubscribe token {UNSUBSCRIBE};
- links per email (default one primary link);
- subject length limit (default 45 characters);
- length bands per email type (yc-waitlist-email-knowledge and the email check use the same bands);
- never-claims.
Save the locks as {EMAIL_LOCKS}. Every later step reads it. If {EMAIL_LOCKS} already exists from an earlier run, read it first and only update what changed.

## Part D: the per-email brief template
One block the drafting step fills for each email: offer, price rule, guarantee, dates, segment, the job of this email, the single action, facts allowed, facts forbidden, voice rules, locks, length band, what happens after the click.

## Worked example (invented business, every fact made up)
A founder sells a meal-planning app called "Example Planner". No past emails.
- Offer: founding plan, first year at the founding price, 30-day refund (owner's words).
- Price rule: copy from the checkout page on the day.
- Launch: Tuesday, March 10. Close: Thursday, March 12, 21:00 PT. Checkout stops the founding price at the close: yes.
- Segments: waitlist, early testers, buyers. Signup promise: "One email when it is ready, then a short launch run."
- Never claims: weight loss; medical advice; "works for every diet".
- Voice source: default starter voice. Sign-off: first name.
Result: The brief check passes. Locks: built-in banned list, one link, 45-character subjects, sign-off, {UNSUBSCRIBE}.

## Gate (exit criteria)
- The brief check passes. Walk the same list by hand; this bot runs no scripts.
- The brief has the offer, real dates with a time zone, at least three never-claims, segments, the signup promise and measurable voice rules.
- If the offer or a date is [NEED], stop. Ask the owner one question at a time. Do not move to step 2.

## Failure handling
- Thin inputs (no site, no samples): use Path 2 and mark every unknown [NEED]. Keep going on everything else.
- Owner contradicts the page: ask which is current; record the answer with today's date.
- Owner wants to skip the brief: explain in one line that every later check reads it, then build the shortest version that passes the gate.
- Revision cap: two rounds of brief changes per session. After that, save what exists and list the open items.

## Output contract
Paste in chat:
1. `brief`: facts sheet plus voice profile in "Key: value" lines, then the style guide.
2. `{EMAIL_LOCKS}`: the locks list.
3. A numbered summary in chat: what is locked, what is [NEED], and the next step.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-waitlist-email-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
