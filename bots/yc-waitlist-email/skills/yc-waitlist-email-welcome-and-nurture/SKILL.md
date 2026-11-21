---
name: yc-waitlist-email-welcome-and-nurture
description: "YC Waitlist Email: use when the owner asks \"someone just joined, what do they get?\", welcome flow, first week; for the welcome and nurture flow for new joiners. Not for the final days of a campaign (launch-close-sequence)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "someone just joined, what do they get?", welcome flow, first week; this skill covers the welcome and nurture flow for new joiners. WHEN NOT: the final days of a campaign (launch-close-sequence). One-off asks can load this skill directly; a full run reaches it through yc-waitlist-email-workflow.
# SKILL: welcome-and-nurture

Use when: the owner asks for "a welcome flow", "the welcome email", "nurture emails for the waitlist", "a 5-email welcome flow for people who have not bought", "what do late joiners get", or "what do buyers get after they pay". Also use for the test prompt: draft email 1 of a five-email welcome flow, leading with the strongest objection.

Purpose: make the first emails after signup or purchase keep the promise the signup page made, then build trust at a gentle pace. It also routes late joiners into the close run and buyers into onboarding.

Drafts only: this skill writes drafts and the flow map. It never turns on an automation. Nothing goes out without the owner's explicit yes.

## Inputs
- The exact words of the signup page and form consent line (from `brief`).
- The freebie or first thing promised, if any.
- What buyers actually receive and when.
- The objection matrix from `plan`, if it exists.

## Steps
1. **Promise check.** Quote, word for word, what the signup page promised (what, when, how often) and the consent line. Where they differ, the narrower one binds. The welcome repeats that promise and nothing bigger. Every gap between promised and delivered costs unsubscribes and complaints at the most attentive moment a subscriber gives you.
2. **Welcome email (right away).** Five jobs, in order:
   - The thing they asked for in the first two lines, with its real name. Never behind a pitch.
   - One human sentence from the founder: why they made it. If none was given, [NEED: one true line from the founder].
   - The next step: one small first use, so it gets opened today.
   - What happens next: how often you write, what kind of emails, an honest notice that some notes sell something, plus a simple opt-out.
   - A reply ask: one question the reader can answer in a line ("What made you join?"). This is also how the owner learns the real objections.
   Under about 200 words. No selling.
3. **Bridge email (day two or three).** The single most common first question, answered. Say what you will not do (no daily spam, no fake urgency).
4. **Nurture set (three to five emails over the wait).** Each gives one real thing the reader did not get on the page: how it is made, a founder letter, a demo clip, a customer story with permission, an honest "what it is not for". The give comes first. If you cannot name the give, cut the email.
5. **Objection-led flow (when asked).** For a five-email flow to people who have not bought: order the emails by the objection matrix, strongest feeling first, price last. Each email answers one doubt with proof, then one soft action. The first clear offer appears around email three to five, never in email one of a pure welcome. If the owner explicitly asks email 1 to lead with the strongest objection, open with that doubt and its honest answer, keep the welcome's five jobs, and make the ask a reply, not a buy link.
6. **Late-joiner path.** Someone who joins during the launch window gets the welcome, then skips nurture and enters the close run with the real date. The welcome still sends during a launch; the rest of nurture waits until the window closes.
7. **Buyer path.** After purchase: what they bought and when they get it, how to get help, one thing to do while they wait. No upsell in the first message. Buyers leave every selling email at once.
8. **Stop rule.** Every nurture email carries an easy way to stop. Readers who have not opened or clicked after the planned set move to a quiet segment. They are not mailed harder.

## Pacing defaults
Start with two or three daily notes after signup, then the rhythm the welcome promised. A warm list can see an offer in email two or three; a cold list needs two or three value emails first. No urgency in nurture unless a real deadline exists outside the flow.

## Worked example: welcome email 1, objection-led (invented business, every fact made up)
```
Email: W1
Type: welcome
Segment: new waitlist signups
Exclude: unsubscribed, buyers
Send: on signup, {LAUNCH_TZ}
Deadline: none
Subject: You're on the list. One honest answer
Preview: The thing most people ask before they join.

Hi {FIRST_NAME|there}, it's {SENDER_NAME}.

You're on the Example Planner list. Here's the two-minute starter week you asked for.

[Get your starter meal plan]({CAMPAIGN_URL})

Most people ask me one thing first. Will this work if my family eats different things? Yes. Each person gets their own swaps, and the shopping list merges them.

I built this because Sunday planning kept eating my evenings.

Try one dinner from the starter week tonight. That's the best test.

I'll write about once a week until launch. Some emails will include an offer. Leaving is one click, and that's fine.

What made you join? Hit reply and tell me in a line. I read every one.

{SENDER_NAME}

{UNSUBSCRIBE}
```

## Gate (exit criteria)
- The welcome makes no claim the signup page did not make.
- Each email has one job and a plain subject. The email check passes on each draft.
- The flow map states the entry, the exits (purchase, unsubscribe, reply), the most emails anyone gets, and how a launch overlaps it.

## Failure handling
- No signup page text: ask for it. Without it, write the welcome as a draft marked "promise not checked".
- Freebie is weak or missing: say which check it fails (specific, close to the purchase, fast to a first result, honest about the bridge) and write the email anyway.
- Owner wants to sell in the welcome: explain the promise rule in one line and offer to put the offer in email three.
- Revision cap: two rounds per email. Then list the open issues for the owner.

## Output contract
Drafts in this chat (W1, W2, N1 to N5, B1 for buyers) in the email file format, and a flow map table in chat: email, trigger, delay, job, give, exit rule. Then three lists: drafted, approved, needs a decision.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-waitlist-email-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
