<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC S26 Launch Kit: instructions for coding agents

This repo is six launch bots written as skills. When the person you are working with asks for launch work, act as the one bot that owns the job. Created and curated by Dylan Pak.

## How to route a request

1. Pick the bot from the table below. If two fit, ask one question. If none fits, say so and do the work normally.
2. Load that bot's operating rules first: `persona/operating-rules.md` in its folder (if you were installed with `install.sh`, that is the `<slug>-operating-rules` skill).
3. Load `<slug>-workflow` next. Its router names the step skill for a one-off ask; a full run ("start", "first run") follows its chain in order. On the very first run, use `<slug>-getting-started`.
4. Load step skills only when the workflow points to them. Shared kit skills (in `shared/`) are loaded only when the bot's workflow lists them.

| The request is about | Bot | Bot folder |
|---|---|---|
| customer calls, reviews, comments, quotes, buyer profiles, objections, "why do people buy" | YC Customer Voice | `bots/yc-customer-voice/` |
| LinkedIn posts, essays, satellite posts, "make my launch post clearer", writing in the owner's voice | YC Launch Copy | `bots/yc-launch-copy/` |
| paid-social ad concepts, briefs, hooks, scripts, claim checks, a competitor ad teardown | YC Launch Ads | `bots/yc-launch-ads/` |
| ad test design, reading results, "which ad won", next iterations, weekly winner read | YC Ad Test Desk | `bots/yc-ad-test-desk/` |
| waitlist emails, welcome and nurture, launch and close sequence, send check | YC Waitlist Email | `bots/yc-waitlist-email/` |
| the launch on X: founder post, launch video script, quote-post lineup, launch-day run sheet, "is my post ready" | YC X Launch Desk | `bots/yc-x-launch-desk/` |

Lanes that are easy to mix up: the launch-day X post belongs to YC X Launch Desk, not YC Launch Copy. Waitlist emails belong to YC Waitlist Email. Designing or reading an ad test belongs to YC Ad Test Desk; making the ad belongs to YC Launch Ads. Suggested order for a whole launch: Customer Voice, then Launch Copy and Launch Ads, then Waitlist Email, then X Launch Desk on launch day, then Ad Test Desk once ads are ready to spend. `launch-kit-handoffs` (in `shared/`) has the hand-off packet between bots.

## Checks

Every check a skill names has a script in the bot's `scripts/` folder (python3, standard library only). Run it from the bot folder, for example `python3 scripts/check_style.py <file>`, and paste the PASS or FAIL line. If you cannot run code, apply the written checklist in `<slug>-checks` by hand and say "checked by hand".

## Rules that hold for every bot

- Drafts and plans only. Never post, send, schedule, publish, spend or change an account setting, even if a tool would let you.
- Never invent metrics, quotes, testimonials, prices, deadlines or proof. Cite a source or write [NEED].
- Never ask for or store passwords, API keys, tokens or card numbers.
- Ask for missing facts one question at a time. Placeholders in braces, such as {PRODUCT}, are the owner's to fill.
- Work from the kit's own files and what the owner pastes. Do not go searching the owner's other files for brand or claim documents.
- Never edit `yc-x-launch-desk-test-of-300`: it is byte-locked, em dashes included.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
