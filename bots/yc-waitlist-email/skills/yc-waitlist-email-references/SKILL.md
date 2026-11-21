---
name: yc-waitlist-email-references
description: "YC Waitlist Email: use when the owner asks \"show me an example\", a blank template, a worked example; for reference material: templates, the email file format, email shells, the subject-line bank, send-timing defaults and the sample campaign. Not for doing the step itself (load that step's skill)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "show me an example", a blank template, a worked example; this skill covers reference material: templates, the email file format, email shells, the subject-line bank, send-timing defaults and the sample campaign. WHEN NOT: doing the step itself (load that step's skill). One-off asks can load this skill directly; a full run reaches it through yc-waitlist-email-workflow.
# YC Waitlist Email: references

Templates, examples and reference tables for the YC Waitlist Email steps. Everything here is invented and labelled as an example, or is a method, not a result. Copy the shape, never the facts. Never present an example number as the owner's. The checks named here are written checklists in yc-waitlist-email-checks, applied by hand.

## Brief and voice template

Copy this into `brief`. Fill every line from the owner or a page the owner provides. Add a source in parentheses to each fact. Do not infer facts from a page's tone. Run the brief check on the filled file.

```
Offer: [NEED: exact offer and terms]
Price rule: copy the price from the checkout page on the day; never round
Guarantee: [NEED: exact wording, or "none"]
Launch date: [NEED: weekday, month, day]
Close date: [NEED: weekday, month, day, time, or "no deadline"]
Time zone: [NEED: audience time zone]
Segments: [NEED: segments the tool can really build]
Signup promise: [NEED: exact words of the signup page and consent line]
Primary action: [NEED: the single thing the reader does]
Support route: reply to this email
Never claims: [NEED: first]; [NEED: second]; [NEED: third]
Voice source: default starter voice
Avg sentence words: 12
Contractions: yes
Sign-off: {SENDER_NAME}
Banned words: built-in list only
Links per email: 1
```

### Default starter voice (for a founder with no past emails)
- First person. Talk to one reader as "you".
- Plain, warm, direct. A true scene beats a clever line.
- Average twelve words per sentence. One to three sentences per paragraph.
- Contractions yes. No dashes as punctuation, no emoji, at most one exclamation mark.
- Open on the point. A welcome or a reply may open with "Hi {FIRST_NAME|there}, it's {SENDER_NAME}."
- Sign off with the first name.
- One primary link. Label names what they get in three to eight words.
- Subject: 45 characters or fewer. Preview: 100 or fewer.
- No hype, no fake urgency, no apology for writing.
- Provisional until the owner approves three drafts. Then run the voice profile on those three and replace the defaults with observed rules.

### Locks file template ({EMAIL_LOCKS})
```
Required: {SENDER_NAME}, {UNSUBSCRIBE}, support route
Primary links: 1
Subject limit: 45 characters
Length bands: last-hours 120; welcome 200; launch 350; all others 400 words
Banned: built-in list plus {BANNED_WORDS_FILE}
Never claims: copied from `brief`
Offer block: copied exactly from `brief`
```

### Per-email brief (one block per plan row)
```
Email number:
Type:
Segment and state:
One job:
Question this answers:
Doubt:
Proof to use (source):
Offer block (copied from brief):
Primary action and link:
Deadline (exact wording or none):
Exclude:
Voice source and special locks:
Length band:
What happens after the click:
```

## Claims and honesty lanes

Use this in the draft step and the send check. Sort every claim into a lane before it goes in an email. Derive lanes from the owner's own facts and never-claims. Never invent a lane to make a claim louder.

| Lane | What it means | What to do |
|---|---|---|
| Green | Felt, specific, supportable from the brief or a demo | Use at full strength |
| Yellow | True only with context (a condition, a region, a plan type) | Use with the condition in the same sentence and a true-only-if note |
| Owner-approved | The owner cleared it with conditions | Check every condition is met; flag any that is missing |
| Red | Health, money or safety outcomes, "guaranteed", "the only", "number one", named competitor comparisons, before and after results | Do not draft it. Flag it for the owner and suggest the strongest Green version |

Rule: back each claim up to the highest lane you can prove. Do not stretch the evidence to move up a lane. When more support is missing, write [NEED PROOF: what] and one flag.

### Honesty pre-check (five questions)
1. Is every fact checkable and true today?
2. Is any scarcity or deadline not real? Cut it.
3. Does the email promise more than the product does today?
4. Is there one honest admission that makes the main claim land harder? It must be true and slightly costly to say. Never fake one.
5. If a buyer got exactly what the email says, would their complaint be fair? If yes, rewrite.
PASS means all five are clear.

### Testimonials and customer words
Only with the person's permission, recorded in the brief with the date. Quote exactly. Add one honest line about scope ("That's one tester, not an average."). No permission means no quote; describe the pattern instead, with a source.

### Consumer-law line (add once per run in the hand-off)
"Deadlines, discounts and claims must be true in your market. Rules differ by country. This is not legal advice."

## Email file format

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

### Body rules checked by hand
- No [NEED: ...] or [placeholder: ...] marks left by the send check.
- A sign-off: {SENDER_NAME}, or add `Sign-off: your sign-off text` in the header.
- An unsubscribe line: {UNSUBSCRIBE} or the word "unsubscribe" linked to the tool's token.
- One primary link destination (repeating the same link in the P.S. is fine). Unsubscribe does not count.
- Link labels: three to eight words, naming what they get.
- Subject at most 45 characters, preview at most 100. No price in the subject.

### Body rules checked by a person
Every amount, term, guarantee and date matches the brief. The email sits inside what people signed up for. The link loads on a phone and shows the same offer. The reply-to inbox is read by a person.

## Five worked email shells

All examples here are invented for an example meal-planning app. Every fact is made up to show shape. Never reuse the lines. Use the owner's facts and voice. Header fields omitted for space; use the format in `email-file-format`.

### 1. Launch (direct, full offer)
Subject: It is ready. Here's what happens next
Preview: The founding plan is open until Thursday.

Hi {FIRST_NAME|there},

You asked to hear when Example Planner was ready. It is.

It builds a week of dinners and the shopping list in about five minutes. Each person gets their own swaps.

The founding plan is open until Thursday at 21:00 PT. It comes with a 30-day refund. After Thursday the price moves to the standard plan.

If you want next week sorted before Sunday, here's where to start.

[Start your founding plan today]({CAMPAIGN_URL})

{SENDER_NAME}

P.S. If you already plan every meal on Sunday, you may not need this. I'd love to hear how you do it.

{UNSUBSCRIBE}

Why it works: ready first, what it is second, terms third, one action. No story before the offer.

### 2. Answer (one doubt, proof, same offer)
Subject: Does it work for a picky family?
Preview: Here's how the swaps work.

Hi {FIRST_NAME|there},

Three of you asked the same thing. Does it work if everyone eats different things?

Each dinner has swaps per person. The shopping list merges them, so you still make one trip. This clip shows a family of four planning a week.

The founding plan is open until Thursday at 21:00 PT, with the 30-day refund.

[See the family swaps in action]({CAMPAIGN_URL})

{SENDER_NAME}

{UNSUBSCRIBE}

Why it works: the reader's question in the first line; one mechanism; one proof; same offer block. "Three" and "family of four" need sources in a real brief.

### 3. Founder note (true scene, honest limit)
Subject: Sunday kept winning
Preview: Why I built this, and who it won't help.

Hi {FIRST_NAME|there},

Last winter I spent more time planning dinner than cooking it.

I'd build a list on Sunday, change it on Tuesday, and end up back at the shop on Thursday. That's why Example Planner merges the swaps into one list.

It won't make you a better cook. It just gets the week out of your head.

The founding plan is open until Thursday at 21:00 PT, with the 30-day refund.

[Plan your first week today]({CAMPAIGN_URL})

{SENDER_NAME}

{UNSUBSCRIBE}

Why it works: a true scene (the owner must supply it), a mechanism, a slightly costly admission, then the one thing it does best.

### 4. Last hours (short, no new argument)
Subject: Founding price ends at 9 tonight
Preview: After that it moves to the standard plan.

Hi {FIRST_NAME|there},

The founding price ends tonight at 21:00 PT.

After that, new plans start at the standard price. The 30-day refund stays the same.

If you want next week planned before Sunday comes, this is the moment.

[Lock in the founding price]({CAMPAIGN_URL})

{SENDER_NAME}

{UNSUBSCRIBE}

Why it works: under 120 words, deadline first, consequence named, no new argument, one link. To non-buyers only.

### 5. Welcome (give first, no pitch)
Subject: You're on the list. Here's your week
Preview: The starter plan you asked for.

Hi {FIRST_NAME|there}, it's {SENDER_NAME}.

Here's the starter week you asked for.

[Get your starter meal plan]({CAMPAIGN_URL})

I made it for the nights you get home late and the fridge looks empty. Try the Tuesday dinner first. It uses five things.

I'll write about once a week until launch. Some emails will include an offer. Leaving is one click, and that's fine.

What made you join? Hit reply and tell me in a line. I read every one.

{SENDER_NAME}

{UNSUBSCRIBE}

Why it works: the thing in the first two lines, one human sentence, one first use, expectations, reply ask. No buy link.

## Send-timing defaults

These are starting guesses, not measured results. Check them against the owner's list. The owner chooses the dates. Never imply this cadence guarantees a result.

### Five-day launch window (default)
| When | Email | Job | Segment |
|---|---|---|---|
| Weeks before | P.S. in normal emails | why you are building it, rough date | normal list |
| Day before | announcement | tomorrow it opens, plainly | waitlist |
| Day 1 morning | launch | the full offer and the ask | waitlist |
| Day 2 morning | resend of launch | new subject, new first line | non-openers of launch, not bought |
| Day 3 | proof or demo | show it working | not bought |
| Day 4 | answer | top doubt, fully answered | not bought |
| Day 5 morning | deadline day | today is the last day, what changes | not bought |
| Day 5, a few hours before close | last hours | shortest sales email, one link | clickers, not bought |
| Day 6 | close and thank-you | buyers: onboarding; non-buyers: closed | split buyers from non-buyers |

The three fixed pieces: announcement, launch, last hours. The middle is a menu. At least one proof and one answer. Never two of the same type back to back. Never add an email without a job of its own.

### Other windows
- One-day window: announcement, launch, last hours, close. Proof and doubt answers live on the sales page.
- Eight-day window: add founder note, who it is not for, and price against a real alternative in the middle.
- No real deadline: no last-hours email. End the run with a "still deciding?" answer email and return to the normal newsletter.

### Tiny or unengaged lists
Below 20 reachable, consented people, use a short launch, one doubt answer and a close note. Skip resends and rate-based A/B tests. A real cutoff and fresh interest may justify a last-hours draft, but the owner decides. Report counts and denominators, never a prediction.

When there is no recent human signal, put the launch on HOLD. Draft a single relevance check, inside the original signup promise. The owner reviews replies before a sale run resumes. No response ends the attempt; it does not justify more mail.

### Caps and exits
Default cap: nine selling emails per window. Readers who never engage get fewer: launch, one answer, deadline day. One resend per email at most. People who clicked but did not buy get at most two short notes inside the window.

Recompute buyers before every send, including the final-day cluster. A purchase exits the selling run before the next email. A reply goes to the owner. Delivery and support emails always win over promotion. Welcome email 1 still sends during a launch; the rest of nurture waits until the window closes.

### Flow audit (at the start of every return visit)
Ask the owner what actually happened, then update the table. Never assume something sent because it was drafted.

| Email | Planned | Drafted | Owner-approved | Scheduled (owner reports) | Sent (owner reports) | Missing |
|---|---|---|---|---|---|---|
| {NUMBER} | {DAY TIME ZONE} | yes/no | yes/no | yes/no | yes/no | {WHAT} |

Report: sent, drafted, missing. Then the next beat only. No extra lecture.

## Subject-line bank

Patterns, not swipe copy. Every example below is invented for an example meal-planning app. Write fresh lines from the owner's facts. Write five, pick one. Name the pattern for each.

| Pattern | Example (invented) | Best for |
|---|---|---|
| Ready | It is ready. Here's the plan | launch |
| Plain date | Founding price ends at 9 tonight | last hours |
| Their question | Does it work without a signal? | answer |
| Their action | You asked to be first. You are | launch |
| Honest limit | Who this planner is not for | middle |
| Small surprise | The meal nobody planned | story |
| Behind the scenes | I almost cut this feature | founder note |
| Proof tease | One week. One shopping trip | demo |
| Direct ask | Try it before Sunday | launch |
| One word changed | Why I stopped saying "diet" | story |
| What happens next | You're on the list. Here's what's next | welcome |
| Thanks | You made the first week possible | close to buyers |

### Nine tests for each candidate
1. 45 characters or fewer (hook in the first 40).
2. Fourteen words or fewer.
3. One idea. One question mark at most.
4. No price, fake "Re:", all caps, emoji or more than one "!".
5. Every number on record. Deadline words match a real deadline.
6. The reader can tell what the email is about from the subject and preview together.
7. The first three paragraphs pay off the promise.
8. For a curiosity subject, test whether it leaves a real unanswered question. Logistics subjects can simply state the news.
9. Not the same shape as the last email in the run.

### Preview text
About 40 to 100 characters. Completes the thought, never repeats the subject. Put the useful bit first so a phone cut-off still makes sense.

Example pair (invented):
- Subject: Does it work without a signal?
- Preview: Yes. Your week saves to the phone. Here's how.

Weak pair (invented):
- Subject: Does it work without a signal?
- Preview: Does it work without a signal? Read on to find out.

The weak preview repeats the subject and says nothing new.

## Sample campaign (invented)

### README

### Sample campaign (invented)

Every fact in this sample is invented for an example meal-planning app called "Example Planner". It shows a finished chat that passes every script. Copy the shape, never the lines.

Files: `brief` (step 1), `plan` (step 2), `email-01` to `email-08` (steps 3 to 6).

```
```
All three passes. The email check still lists MANUAL items (13 and 14) for a person to tick.

### Brief

### Brief: Example Planner launch (invented)

Offer: Founding plan, first year at the founding price, with a 30-day refund (owner)
Price rule: copy the price from the checkout page on the day; never round (owner)
Guarantee: 30-day refund, no questions asked (owner)
Launch date: Tuesday, March 10 (owner)
Close date: Thursday, March 12, 21:00 (owner; checkout stops the founding price then)
Time zone: PT (owner)
Segments: waitlist; non-openers; clickers; buyers; unsubscribed (email tool)
Signup promise: one email when it is ready, then a short launch run (signup page)
Primary action: start the founding plan (owner)
Support route: reply to this email
Never claims: weight loss; medical advice; works for every diet
Voice source: default starter voice
Avg sentence words: 12
Contractions: yes
Sign-off: {SENDER_NAME}
Banned words: built-in list only
Links per email: 1

Proof on file (owner): testers planned a week in about five minutes (tester notes, owner); offline mode ships at launch (owner).

### Email 01

Email: 1
Type: announcement
Segment: waitlist
Exclude: buyers, unsubscribed, complained
Send: Monday 09:00 PT
Deadline: Thursday 21:00 PT
Subject: Example Planner opens tomorrow
Preview: Here's what you'll get, and when.

Hi {FIRST_NAME|there},

Tomorrow morning the founding plan opens.

Example Planner builds your week of dinners and the shopping list in one go. You asked to hear first, so you will.

The founding plan runs from Tuesday morning to Thursday at 21:00 PT.

[Preview the founding plan now]({CAMPAIGN_URL})

{SENDER_NAME}

{UNSUBSCRIBE}

### Email 02

Email: 2
Type: launch
Segment: waitlist
Exclude: buyers, unsubscribed, complained
Send: Tuesday 08:00 PT
Deadline: Thursday 21:00 PT
Subject: It's ready. Here's what happens next
Preview: The founding plan is open now.

Hi {FIRST_NAME|there},

You asked to hear when Example Planner was ready. It is.

It plans a week of dinners and the shopping list in about five minutes. Each person gets their own swaps.

The founding plan closes Thursday at 21:00 PT. It comes with a 30-day refund. After Thursday, new plans start at the standard price.

If you want next week sorted before Sunday, here's where to start.

[Start your founding plan today]({CAMPAIGN_URL})

{SENDER_NAME}

P.S. If you already plan every meal on Sunday, you may not need this.

{UNSUBSCRIBE}

### Email 03

Email: 3
Type: resend
Segment: did not open email 2
Exclude: buyers, unsubscribed, complained, opened email 2
Send: Wednesday 08:00 PT
Deadline: Thursday 21:00 PT
Subject: In case Tuesday got busy
Preview: The founding plan is open for two more days.

Hi {FIRST_NAME|there},

Tuesday was busy for a lot of people, so here's the short version.

Example Planner is live. It turns a week of dinners into one shopping list.

The founding plan closes Thursday at 21:00 PT, with a 30-day refund.

[See the founding plan details]({CAMPAIGN_URL})

{SENDER_NAME}

{UNSUBSCRIBE}

### Email 04

Email: 4
Type: proof
Segment: waitlist, has not bought
Exclude: buyers, unsubscribed, complained
Send: Wednesday 17:00 PT
Deadline: Thursday 21:00 PT
Subject: Five minutes, one week of dinners
Preview: Watch a tester plan the whole week.

Hi {FIRST_NAME|there},

Our testers planned a full week in about five minutes. This short clip shows one of them doing it, start to finish.

Watch the swaps. One person skips meat, another skips dairy. The list still comes out as one trip.

The founding plan closes Thursday at 21:00 PT, with a 30-day refund.

[Watch a week get planned]({CAMPAIGN_URL})

{SENDER_NAME}

{UNSUBSCRIBE}

### Email 05

Email: 5
Type: answer
Segment: waitlist, has not bought
Exclude: buyers, unsubscribed, complained, open support case
Send: Thursday 08:00 PT
Deadline: Thursday 21:00 PT
Subject: Is it worth it? Fair question
Preview: Here's the check I'd do in your seat.

Hi {FIRST_NAME|there},

A few of you replied with the same question. Is the founding plan worth it?

Here's how I'd check. Count the nights this week you stood at the fridge with no plan.

Example Planner builds the week and the list in about five minutes. If it doesn't save you time in the first month, the 30-day refund covers you.

The founding plan closes tonight at 21:00 PT.

[Start your founding plan today]({CAMPAIGN_URL})

{SENDER_NAME}

{UNSUBSCRIBE}

### Email 06

Email: 6
Type: last-hours
Segment: clicked a launch email, has not bought
Exclude: buyers, unsubscribed, complained
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

### Email 07

Email: 7
Type: thank-you
Segment: bought the founding plan
Exclude: unsubscribed
Send: Friday 09:00 PT
Deadline: none
Subject: You're in. Start with one dinner
Preview: Your first week takes about five minutes.

Hi {FIRST_NAME|there},

Thank you for joining as a founding member.

Your plan is active now. Open the app, add who eats with you, and pick one dinner for tonight.

If anything is unclear, reply to this email. A person reads every reply.

[Open your Example Planner account]({APP_URL})

{SENDER_NAME}

{UNSUBSCRIBE}

### Email 08

Email: 8
Type: close
Segment: did not buy
Exclude: buyers, unsubscribed, complained
Send: Friday 10:00 PT
Deadline: none
Subject: The founding plan is closed
Preview: Thanks for reading along this week.

Hi {FIRST_NAME|there},

The founding plan is closed now. Thanks for reading along this week.

You'll keep getting the regular weekly note. If you have a question about the app, just hit reply.

{SENDER_NAME}

{UNSUBSCRIBE}

### Plan

### Run plan: Example Planner launch (invented)

| Email | Day | Segment | Type | Job | Doubt | Subject angle | Link | Deadline | Exclude | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Mon | waitlist | announcement | say it opens tomorrow | none | the date | {CAMPAIGN_URL} | Thu 21:00 PT | buyers, unsubscribed | draft |
| 2 | Tue AM | waitlist | launch | ask for the sale | none | it is ready | {CAMPAIGN_URL} | Thu 21:00 PT | buyers, unsubscribed | draft |
| 3 | Wed AM | non-openers of 2 | resend | reach non-openers | none | new angle | {CAMPAIGN_URL} | Thu 21:00 PT | buyers, unsubscribed, openers of 2 | draft |
| 4 | Wed PM | waitlist | proof | show a week planned fast | will it work for my family | demo | {CAMPAIGN_URL} | Thu 21:00 PT | buyers, unsubscribed | draft |
| 5 | Thu AM | waitlist | answer | settle the cost doubt | is it worth it | the question | {CAMPAIGN_URL} | Thu 21:00 PT | buyers, unsubscribed | draft |
| 6 | Thu PM | clickers, not bought | last-hours | wake the deadline | none | hours left | {CAMPAIGN_URL} | Thu 21:00 PT | buyers, unsubscribed | draft |
| 7 | Fri | buyers | thank-you | start onboarding | none | welcome in | {APP_URL} | none | unsubscribed | draft |
| 8 | Fri | non-buyers | close | say it closed | none | closed | none | none | buyers, unsubscribed | draft |

Exit rules: a purchase removes the person before the next selling email; the owner recomputes buyers before each Thursday send; replies go to the owner.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
