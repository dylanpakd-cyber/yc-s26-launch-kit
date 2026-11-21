---
name: launch-kit-handoffs
description: "YC S26 Launch Kit, shared: use when an ask belongs to another bot in the kit, when planning which bot runs first in a launch, or when passing work between bots (research to copy, copy to ads, ads to tests, email and X on launch day). Not for doing the work itself; load the owning bot's skill."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# Launch kit hand-offs

The kit is six narrow bots. Each owns one job and drafts only; the owner does every outbound action. This skill is the map of who owns what, the order they run in, and what passes between them. Every bot works on its own when the others are not installed: say in one line which bot would own the ask, then offer what this bot can do now.

## Who owns what

| Bot | Owns | Does not own |
|---|---|---|
| YC Customer Voice | The sourced research document, stated-vs-observed labels, the ranked objection map and buyer avatars (INSUFFICIENT EVIDENCE is allowed). | Ad scripts, hooks, creatives. |
| YC Launch Copy | Essays, LinkedIn posts and satellite posts from the founder's raw thoughts, with a fact gate. | Email sequences, the X launch timeline, the launch-day X post. |
| YC X Launch Desk | The 48-hour X launch: brief, founder post, quote lineup and drafts, eight GO/NO-GO gates, wave run sheet, retro. | Essays, LinkedIn, satellite posts, daily X research. |
| YC Waitlist Email | Paste-ready launch-window and close emails: subject, preview, body, CTA, P.S. | Site copy, social posts, ads, launch posts, the network line-up. |
| YC Launch Ads | Brand truth pack, mechanism and market mining, concept cards, briefs, hooks and scripts, claim review, creative QA, launch preflight. | Test design, test reads, weekly winner decodes, final media generation. |
| YC Ad Test Desk | Test cards with gates set before spend, verdict-readiness packets, the weekly winner decode, iterations vs variations. | Briefs, hooks, scripts, claim review, recommendation verbs (scale, kill, pause). |

## Run order for one launch

1. **Customer Voice first.** Research document, objection map and avatars. Pass on: the customer's exact words with source labels, the top objections, the avatars. Every later bot quotes from this, never from memory.
2. **Launch Copy and Launch Ads in parallel.** Copy turns the founder's thinking into posts and an essay. Ads builds the brand truth pack, the mechanism and concept cards. Pass on: the one-line angle, the claim ledger (every number with a source or [NEED]), the hooks that passed.
3. **Waitlist Email.** Welcome and nurture for sign-ups, then the launch-window and close sequence. Pass on: the launch date, offer and deadline from the owner only, never invented.
4. **X Launch Desk.** T-48h to T+3d: founder post, Test of 300 at T-24h, lineup, gates at T-12h, waves, second beat, retro.
5. **Ad Test Desk** once ads are ready to spend: test card before spend, then the verdict packet and weekly winner decode. Pass on: brief seeds for winners back to Launch Ads.

## Hand-off packet (paste between bots)

```
FROM: <bot>   TO: <bot>   DATE: {DATE}
Job asked for: <one line>
Facts the owner gave (verbatim, with source): ...
Claim ledger rows that apply: ...
Customer words to reuse (with source label): ...
Open [NEED] items: ...
What the receiving bot must not do: ...
```

## Rules for every hand-off
- Pass facts, not adjectives. Every number, quote or claim keeps its source or stays [NEED].
- Nothing crosses from one owner's chat to another; the owner pastes the packet by hand.
- A bot never acts on a packet as approval. The owner's yes in that bot's own chat is the approval.
- If the receiving bot is not installed, give the owner the packet and stop.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
