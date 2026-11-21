---
name: yc-customer-voice-references
description: "YC Customer Voice: use when the owner asks \"show me an example\", a blank template, a worked example; for reference material: templates, mining methods, redaction rules, the no-data path and the sample research set. Not for doing the step itself (load that step's skill)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "show me an example", a blank template, a worked example; this skill covers reference material: templates, mining methods, redaction rules, the no-data path and the sample research set. WHEN NOT: doing the step itself (load that step's skill). One-off asks can load this skill directly; a full run reaches it through yc-customer-voice-workflow.
# YC Customer Voice: references

Templates, examples and reference tables for the YC Customer Voice steps. Everything here is invented and labelled as an example, or is a method, not a result. Copy the shape, never the facts. Never present an example number as the owner's. The checks named here are written checklists in yc-customer-voice-checks, applied by hand.

## Templates

Copy these blocks exactly. The hand checks read the field names. Every value in braces is filled from evidence or marked [NEED] or "inferred". All examples in the skills are invented.

### Index card (one per call or source) -> `index`
```
## Call {NN}
Source: {C-NN, owner notes | transcript | ticket T-NN | survey S-NN}
Date: {as given}
Segment: {early tester | waitlist | churned | buyer | unknown}
Speaker role: {role label, never a name}
Topic: {one line}
Tags: {three of: pain, desire, doubt, workaround, buying signal, failed solution, trigger, question}
Summary: {two lines}
Quote IDs: {Q-numbers pulled from this source}
Decision moment: {when they decided or hesitated, or n/a}
Redaction: done
```

### Quote bank -> `quote-bank`
```
| ID | Quote | Verbatim | Source type | Source ref | Date | Speakers | Label | Tier | Theme | Use | Consent |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | {exact redacted words} | yes | review | R-01 | {date} | 3 | stated | A | {theme} | internal | none |
```
Verbatim: yes or no. Label: stated, observed or claimed. Tier: A (verbatim and 3 or more speakers), B (2 or more speakers), C (the rest; every claimed row). Use: internal, copy (A or B only) or public (needs Consent "written"). Consent: none or written.

### Research document -> `research-doc`
Sixteen "## " sections in this order: Top pain points; Failed solutions; Desired outcomes; Objections; Misconceptions; Golden nuggets; Words to borrow and avoid; Triggers; What changed their mind; Alternatives; Necessity test; Strategy implications; Language analysis; Key personas; Open questions; Concepts. Each section cites two or more bank IDs or says "thin". Concepts says "Left empty."

### Avatar card -> `avatars`
```
## Avatar {N}: {nickname}
Nickname: {role-based nickname}
Age band: {range} (estimate)
Core problem: {one sentence plus emotional context}
Moment it bites: {time, place, who else}
Top fears: {1}; {2}; {3}; {4}; {5}
Emotional drivers: {two dominant}
Failed solutions: {what, why it failed, IDs}
Soundbites: {three or more Tier A or B IDs}
Desired transformation: {a concrete ordinary day}
Market beliefs: {belief about products like this}
Emotional blockers: {what stops them}
Relationship impact: {how it touches others}
Objections: {ranked, with IDs}
Awareness level: {unaware | problem | solution | product | most aware}
Where they spend time: {sources}
Proof that persuades: {proof and format}
Inferred: {every inferred field}
```
If fewer than three avatars, add:
```
## Avatar count note
Avatar count note: {n} avatars, because the evidence shows {n} distinct core problems ({IDs}). Needed to find a third: {what}.
```

### Five-layer objection stack -> `objections`
```
## Objection {N}: {short name}
Objection: "{their words}" ({ID})
Count: {number of independent people}
Sources: {IDs and refs}
Belief: {layer 2}
Fear: {layer 3}
Identity: {layer 4}
Defuse: {layer 5, one line}
Proof: {source or ID, or [NEED PROOF: what]}
Does not claim: {one line}
Avatar: {which}
Asset: {ad | email | landing page FAQ | post | onboarding}
```

### Lock page -> `locks`
```
## Lock page {N}: {avatar} x {objection}
People: {who}
Not for: {who not}
Empathy: {Tier A or B ID}
Doing: {from bank}
Frustrations: {from bank}
Heaven: {best day, from bank}
Hell: {worst day, from bank}
Positioning: {vs real alternatives}
How it works: {mechanism in buyer words}
Promise: {checkable outcome}
So what: {last true answer of the drill}
Proof: {IDs and owner proof}
Priority: {the one first job}
Honesty check: PASS
```

### Hand-off pack -> `handoff`
Per desk (ads, email, copy, X): the lock page, passing angles, the quote pack (Tier A and B rows with Use "copy", redacted, with IDs), the do-not-use list, and the line "Evidence status: {PASS | INSUFFICIENT}". The owner says yes before any other bot reads it.

## Claims and honesty lanes for hand-offs

The research bot does not write copy, but its hand-off decides what other bots believe is true. Tag every strategy implication and angle with a lane.

| Lane | Meaning | Hand-off rule |
|---|---|---|
| Green | Felt, specific, backed by Tier A or B evidence and owner facts | Hand off as is |
| Yellow | True only in context (a segment, a condition) | Hand off with the condition written beside it |
| Owner-approved | The owner cleared it with conditions | Hand off only with every condition met and listed |
| Red | Health, money or safety outcomes, "guaranteed", "the only", "number one", competitor comparisons, before and after results | Do not hand off. Flag it to the owner |

Back each claim up to the highest lane the evidence reaches. Never invent proof to reach a higher one. A participant's belief ("this would help my anxiety") is customer language, not proof of a health claim; keep everyday words and drop the clinical label.

### Honesty pre-check (used in the lock page)
1. Every fact checkable and true today.
2. No scarcity or deadline that is not real.
3. No promise bigger than the product does today.
4. One honest admission, true and slightly costly, that makes the main claim stronger.
5. If a buyer got exactly what this says, a complaint would not be fair.
All five clear means PASS.

## Mining methods (full steps)

All methods are read-only and public data or owner material only.

### Comment mining
1. Open the post, video or product page. Write down what it claims; comments answer it.
2. Collect comments and replies. Keep text, like count if shown, date and source ref. Never collect personal profile details.
3. Clean lightly: drop spam, bots, duplicates, giveaway entries.
4. Sort each useful comment: question, objection, complaint or pain, praise, confusion, request, buying intent, debate, joke or culture signal.
5. Cluster. Score each theme by frequency (independent people) and intensity (how strong the words are).
6. Quote the best three per theme with source refs.
7. Report how much material was read and how much to trust the sample. Do not let an intense single reply stand in for a trend. Note moderation or platform bias.
8. Turn insights into actions for other bots: FAQ, objection answer, product note, angle to test.

### Social listening
1. Define the topic, aliases, misspellings, competitor names and the date window.
2. Search two or three relevant platforms, not every platform.
3. Keep URLs, dates, platform and exact quotes.
4. Cluster into themes. Split positive, negative, neutral and mixed.
5. For each theme: count, two verbatim examples, recommended action.
6. Say what was not available. This is public-data research, not full monitoring.

### Demand research
1. Turn the idea into search terms and synonyms.
2. Search for unmet needs in the buyer's language. Useful signals include a recurring complaint, a request for help, a handmade workaround, an alternative under review, and a specific purchase question.
3. Score demand on frequency, intensity, recency and willingness-to-pay hints.
4. Never claim validation from a handful of comments. Never ignore negative evidence or existing alternatives.

### Transcript mining (videos, podcasts, recorded interviews the owner provides as text)
1. Keep the source ref and timestamps.
2. Segment: opening, setup, main claim, evidence, payoff, ask.
3. Pull stories, objections addressed, emotional language and quotable lines that a buyer said (not the host).
4. If no transcript exists, say so; never guess captions.

### Scoring engagers against the buyer
For each source: do the people talking match {AUDIENCE} by role, situation and problem? Mark each item buyer-like or not our buyer. Only buyer-like items count toward themes. Report the split, because a topic popular with non-buyers can mislead a launch.

## No-data path: a pre-launch founder with little or no customer material

Use this when the evidence check prints INSUFFICIENT EVIDENCE, or the owner says "we have no customers yet". The goal is 10 or more real, independent sources across at least two source types. Everything here is public data or material the owner already has. Never log in as anyone, never message strangers, never scrape behind a login. The owner does any outreach themselves.

### Step 1: what the owner already has (ask one at a time)
1. Waitlist signup answers (a "why did you join" field)?
2. Replies to any email or post you sent?
3. Notes from conversations with friends, testers or early users?
4. Support or contact-form messages?
5. Your own reasons for building it? (Brand context only. Never customer evidence.)

### Step 2: public sources (pick the ones where the buyer talks)
| Source type | What to look for | Target |
|---|---|---|
| Reviews of the closest alternatives (app stores, shops, review sites) | one-, two- and three-star reviews for objections; five-star for desired outcomes | 10 to 30 |
| Forum threads (community forums, Q and A sites) | "how do I", "is there a tool", "I wish"; read the whole thread | 3 to 10 threads |
| Comments under posts or videos about the problem | questions, complaints, workarounds | 2 to 5 posts |
| Long video or podcast transcripts where buyers describe the problem | stories, triggers, words | 1 to 3 |
| Public job posts, templates or guides people share | workarounds that prove the need | optional |

Record a source ref, URL and date for each. Redact before saving.

### Step 3: what the owner can collect (the owner does this, not the bot)
Draft for the owner, never sent by the bot:
- A one-question reply ask for the waitlist: "What made you join? Reply in a line."
- Five interview questions: tell me about the last time this happened; what did you try; what happened next; what would have to be true for you to pay for a fix; what almost stopped you trying the last thing.
- A note to self: ask about the past, not about hypothetical futures. People are poor predictors of what they will buy.

### Step 4: re-check
Grade the new items and re-run the evidence check. If it still prints INSUFFICIENT EVIDENCE after this path, stop and report:
- sources found, by type;
- the strongest themes so far (all marked provisional);
- the exact sources the owner should collect next.
Revision cap: one no-data run per session. Do not loop.

### What counts as independent
Different people. Two reviews by the same account count once. A thread that quotes a review is not a new person. The owner's friends count, marked "friend" in the source type, and cannot make a theme Tier A on their own.

## Redaction rules

Default level: strict. {REDACTION_RULES} may add more, never fewer.

### Always remove
| Item | Replace with |
|---|---|
| Personal names (first, last, nicknames) | role label: [BUYER-3], [PARENT-1], [TEACHER-2] |
| Social handles and profile links | [HANDLE REMOVED] |
| Emails and phone numbers | [CONTACT REMOVED] |
| Street addresses, small towns tied to a person | region only ("a small town") or remove |
| Employer or school tied to a person | "a school", "a mid-size company" |
| Order, account, ticket, invoice numbers | [ORDER REMOVED] |
| Health, money or legal detail that could identify | summary in general words |
| Faces or names in screenshots | describe the screenshot instead |

### Keep
The problem, the emotion and the exact words around it. Misspellings. Times and situations ("at 8am on a school day").

### Summarise instead of quoting when
The words would identify the person even after removal (a rare job plus a place, a public story). Mark it "summary, not quote". It can be Tier B at most.

### The check
The redaction check flags emails, phone numbers, handles, profile URLs, street addresses, order or account numbers, "Name:" style fields with a value, and likely names after cues like "said", "my name is", "my husband". Keep non-person words (product names, brands, places) on an allow list. The name check is a judgment call: a CLEAN result does not replace one human read of the quote bank before hand-off.

### Never
Never keep the unredacted original in the research. Never re-identify a person. Never quote a minor. Never publish a customer quote without written permission on file.

## Sample research (invented)

### README

### Sample research set (invented)

Everything here is invented for an example family planner app. No real person, review or post is quoted. It shows a finished research set that passes every hand check. Copy the shape, never the content.

```
```
Every block passes every hand check in yc-customer-voice-checks.

### Avatars

### Buyer avatars (invented)

#### Avatar 1: The Calendar Keeper
Nickname: The Calendar Keeper
Age band: 35 to 45 (estimate)
Core problem: carries the family schedule alone and still misses school events
Moment it bites: 8am on a school day, reading about an event that is today
Top fears: my kid is the only one left out; the other parent says I should have known; teachers think we do not care; I miss something bigger; I never get a break from tracking it
Emotional drivers: guilt, wanting to be seen as capable
Failed solutions: shared calendar nobody else opens (Q2); paper on the fridge (Q7)
Soundbites: Q1, Q3, Q8
Desired transformation: a weekday where both adults got the reminder the night before
Market beliefs: family apps are built for people who are already organized
Emotional blockers: embarrassment at needing help with something basic
Relationship impact: small arguments about who forgot
Objections: one more app (Q5); price (Q9)
Awareness level: solution aware
Where they spend time: app store reviews, parenting forums
Proof that persuades: a demo of the other adult receiving the reminder
Inferred: age band; the left-out fear is inferred from Q1

#### Avatar 2: The Stretched Worker
Nickname: The Stretched Worker
Age band: 30 to 50 (estimate)
Core problem: work deadlines and school forms collide in the same week
Moment it bites: late evening, after work, when the forms are finally read
Top fears: missing a form during a busy work week; looking unreliable at work; looking absent at school; falling behind on both; being too tired to check
Emotional drivers: stress, wanting control
Failed solutions: reading everything at night and copying it by hand (Q3)
Soundbites: Q6, Q10, Q5
Desired transformation: forms and work dates in one calm evening check
Market beliefs: another tool means more setup time
Emotional blockers: fatigue
Relationship impact: less patience at home in busy weeks
Objections: one more app (Q5)
Awareness level: problem aware
Where they spend time: forums, social posts about school notices
Proof that persuades: a short demo of a two-minute evening check
Inferred: age band; the work fear is inferred from Q6

#### Avatar 3: The Two-Home Coordinator
Nickname: The Two-Home Coordinator
Age band: 30 to 50 (estimate)
Core problem: two households need one shared view of pickups and events
Moment it bites: a pickup time nobody confirmed
Top fears: a child waiting at school; conflict with the other house; looking like the unreliable parent; schedules diverging; the child carrying messages between homes
Emotional drivers: worry, wanting fairness
Failed solutions: shared calendar one side ignores (Q2); texting back and forth (Q14)
Soundbites: Q11, Q12, Q2
Desired transformation: both homes see the same confirmed pickup every week
Market beliefs: the other house will not use anything new
Emotional blockers: fear of starting a conflict by suggesting a tool
Relationship impact: tension over missed handoffs
Objections: the other side will not use it (Q2)
Awareness level: solution aware
Where they spend time: forums on shared parenting
Proof that persuades: the other house receives reminders without signing up
Inferred: age band; whether the other house needs an account is unknown

### Handoff

### Hand-off pack (invented, waiting for the owner's yes)

Evidence status: PASS

#### For the email bot
Lock page 1. Passing angle: "you stop being the family's reminder" (Q1, Q2, Q8). Quote pack: Q1, Q3, Q8, Q10. Do not use: Q13, Q14.

#### For the ad bot
Lock page 1. Open proof: the text reminder demo is [NEED PROOF]. Quote pack: Q1, Q2, Q5.

#### For the copy bot
Research document sections: Necessity test, Strategy implications. Quote pack: Q2, Q11, Q12.

#### For the X bot
Words to borrow: "the night before" (Q10). Repeated question for a post: Q4.

### Index

### Index cards (invented)

#### Call 01
Source: C-01, owner notes
Date: as given
Segment: early tester
Speaker role: parent of two school-age kids
Topic: missed school forms
Tags: pain, failed solution, question
Summary: Missed a field trip form. The shared calendar fails because the other parent never opens it.
Quote IDs: Q13
Decision moment: n/a
Redaction: done

#### Source R-01
Source: R-01, app store review of an alternative
Date: 2026-02-03
Segment: unknown
Speaker role: parent
Topic: late school notices
Tags: pain, trigger, desire
Summary: Learned about a school event the same morning. Wants notice the night before.
Quote IDs: Q1
Decision moment: left the alternative after the missed event
Redaction: done

### Locks

### Lock pages (invented)

#### Lock page 1: The Calendar Keeper x the other adult will not use it
People: the parent who carries the family schedule alone, solution aware
Not for: families who already share one calendar that both adults open daily
Empathy: Q8
Doing: copies school messages into a phone at night (Q3)
Frustrations: the shared calendar nobody else opens (Q2)
Heaven: both adults know about the event the night before (Q10)
Hell: learning about it at 8am the same day (Q1)
Positioning: a family planner that texts the other adult, so nobody needs to open an app
How it works: forward the school message; both adults get a plain text the night before
Promise: both adults hear about school events the night before
So what: nobody gets caught at 8am, and you stop being the reminder
Proof: Q1, Q2; text reminder demo from the owner before launch
Priority: remove the "only I will use it" doubt first
Honesty check: PASS

### Objections

### Objection stacks (invented)

#### Objection 1: one more app
Objection: "another app is the last thing i need" (Q5)
Count: 3
Sources: Q5, Q14
Belief: each app adds work instead of removing it
Fear: paying for something that becomes another unopened icon
Identity: the person who falls for every new tool
Defuse: it replaces the shared calendar and the copy job instead of adding a step
Proof: [NEED PROOF: owner demo of import from school messages]
Does not claim: that setup takes no time
Avatar: 2 (The Stretched Worker)
Asset: email answer, landing page FAQ

#### Objection 2: the other adult will not use it
Objection: "the shared calendar nobody else in the house opens" (Q2)
Count: 5
Sources: Q2, Q12
Belief: shared tools only work when both people open them
Fear: being the only one who uses it, again
Identity: the nagging one
Defuse: the reminder reaches the other adult as a plain text the night before
Proof: [NEED PROOF: owner confirms the text reminder ships at launch]
Does not claim: that the other adult will act on it
Avatar: 1 (The Calendar Keeper)
Asset: ad, email answer

### Quote bank

### Quote bank (invented)

| ID | Quote | Verbatim | Source type | Source ref | Date | Speakers | Label | Tier | Theme | Use | Consent |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | found out about the bake sale at 8am | yes | review | R-01 | 2026-02-03 | 4 | stated | A | missed events | copy | none |
| Q2 | the shared calendar nobody else in the house opens | no | forum | F-01 | 2026-02-05 | 5 | observed | B | failed solution | copy | none |
| Q3 | i copy every school message into my phone at night | yes | review | R-02 | 2026-02-06 | 3 | stated | A | workaround | copy | none |
| Q4 | does it work without wifi | yes | review | R-03 | 2026-02-07 | 3 | stated | A | offline question | copy | none |
| Q5 | another app is the last thing i need | yes | review | R-04 | 2026-02-08 | 3 | stated | A | app fatigue | copy | none |
| Q6 | work deadlines and school forms land in the same week | no | forum | F-02 | 2026-02-09 | 2 | stated | B | work and family clash | copy | none |
| Q7 | paper on the fridge until it falls off | yes | review | R-05 | 2026-02-10 | 2 | observed | B | failed solution | copy | none |
| Q8 | i feel like the only one who remembers anything | yes | forum | F-03 | 2026-02-11 | 3 | stated | A | mental load | copy | none |
| Q9 | is the price worth it for a calendar | yes | review | R-06 | 2026-02-12 | 2 | stated | B | price | copy | none |
| Q10 | the night before is when i actually read things | yes | post | P-01 | 2026-02-13 | 2 | stated | B | timing | copy | none |
| Q11 | two homes needed one place both of us could see | no | forum | F-04 | 2026-02-14 | 2 | stated | B | two households | copy | none |
| Q12 | the other house never confirms pickups | yes | forum | F-05 | 2026-02-15 | 2 | stated | B | two households | copy | none |
| Q13 | every parent at school would buy this | no | call | C-01 | as given | 1 | claimed | C | demand | internal | none |
| Q14 | we switched back to texting each other | yes | review | R-07 | 2026-02-16 | 2 | observed | B | negative evidence | internal | none |

Speakers counts are self-reported by the researcher. Recount from the source refs before hand-off.

### Call 01

### Call C-01, redacted owner notes (invented)

[PARENT-1], an early tester with two school-age kids, talked about the week a field trip form was missed. [PARENT-1] said the shared phone calendar did not help because the other parent never opens it. [PARENT-1] reads school messages late at night and copies them into a phone by hand. [PARENT-1] claimed every parent at school would buy this. Asked whether it works without wifi.

### Research doc

### Research document: example family planner (invented)

#### Top pain points
| Pain | Description | Count | Best quote |
|---|---|---|---|
| Missed school events | Notices arrive too late to act on | 4 | Q1 |
| Mental load on one parent | One person carries every date | 3 | Q8 |

#### Failed solutions
A shared calendar that only one parent opens (Q2). Paper on the fridge (Q7).

#### Desired outcomes
Notice the night before, when parents actually read (Q10). Both adults seeing the same dates (Q11).

#### Objections
Ranked: one more app (Q5, 3 people), price for a calendar (Q9, 2 people).

#### Misconceptions
Thin: no source yet shows a belief that is false. Q2 and Q7 show failed tools, not misconceptions.

#### Golden nuggets
Frustration: Q1, Q8. Relief wanted: Q10. Fatigue: Q5.

#### Words to borrow and avoid
Borrow: "the night before" (Q10), "remembers anything" (Q8). Avoid "productivity" and "optimize"; nobody used them (Q1, Q3 use plain words).

#### Triggers
A missed event starts the search (Q1). A pickup that nobody confirmed (Q12).

#### What changed their mind
Thin: the strongest evidence is negative. Q14 returned to texting, and Q2 shows the shared calendar was abandoned.

#### Alternatives
Shared phone calendars (Q2), paper (Q7), group texts (Q14).

#### Necessity test
Partly shown. Free calendars fail when the other adult never opens them (Q2, Q12). Evidence does not yet show this product gets opened when they do not. Q14 is a warning.

#### Strategy implications
| Opportunity | How the brand could win |
|---|---|
| Reach the second adult without an app | Lead with night-before reminders the other adult receives (Q2, Q10) |
| Answer app fatigue early | Show it replaces a tool rather than adding one (Q5, Q14) |

#### Language analysis
Plain, tired and specific. Lowercase, short sentences, concrete times (Q1, Q3). Reading level is simple; keep hand-offs plain.

#### Key personas
The Calendar Keeper (Q1, Q8); The Stretched Worker (Q6, Q10); The Two-Home Coordinator (Q11, Q12).

#### Open questions
Q13 claims school-wide demand from one call; treat it as a lead only. Does the product get opened on day three?

#### Concepts
Left empty.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
