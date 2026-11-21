<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC X Launch Desk

> The Grok Bot we used to hit 1.4M views on X in 3 days. Runs your 48-hour launch on X: the founder post, quote-post drafts for your network and a launch-day plan. It drafts; you post.

Import into Grok Bot: TEMPLATE_LINK (yc-x-launch-desk)

## Skills in this bot

- `yc-x-launch-desk-checks`
- `yc-x-launch-desk-founder-post-and-video-script`
- `yc-x-launch-desk-getting-started`
- `yc-x-launch-desk-knowledge`
- `yc-x-launch-desk-launch-playbook`
- `yc-x-launch-desk-network-and-lineup`
- `yc-x-launch-desk-references`
- `yc-x-launch-desk-retro-and-angles`
- `yc-x-launch-desk-test-of-300`
- `yc-x-launch-desk-wave-and-replies`
- `yc-x-launch-desk-workflow`

## Shared kit skills it can use

- [`launch-kit-handoffs`](../../shared/launch-kit-handoffs/SKILL.md): who owns what across the six bots, run order, and the hand-off packet
- [`reference-teardown`](../../shared/reference-teardown/SKILL.md): measured teardown of one reference video or ad (cut map, style spec, transferable format)
- [`quote-lineup-scout`](../../shared/quote-lineup-scout/SKILL.md): deeper research pass for the 30 to 60 person quote lineup
- [`hook-library-keeper`](../../shared/hook-library-keeper/SKILL.md): keeps a verbal and visual hook library fresh, with an evidence gate
- [`x-source-scan`](../../shared/x-source-scan/SKILL.md): 5 to 8 proven X posts on a topic, ranked by how repackageable they are
- [`outlier-idea-archive`](../../shared/outlier-idea-archive/SKILL.md): swipe log of posts that spread, with the first-line wording move named

## Folders in this bot

- `persona/operating-rules.md`: the system prompt.
- `skills/`: one folder per skill.
- `references/`: templates, worked example and filled examples the skills point to (`examples.md`, `step-table.md`, `templates.md`, `worked-example-48h.md`).
- `scripts/`: 10 check scripts (Python 3, standard library only): `check_channel.py`, `check_credit.py`, `check_facts_ledger.py`, `check_fields.py`, `check_gates.py`, `check_hooks.py`, `check_leak.py`, `check_lineup_log.py`, `check_sections.py`, `check_style.py`. Run from this folder, for example `python3 scripts/check_channel.py --selftest`.

## Start here

1. Put `persona/operating-rules.md` in the agent's instructions.
2. Install the whole bot folder: copy the folders in `skills/` (and the shared ones above) where your agent loads skills, and keep `references/` and `scripts/` together in one place the agent can read (skills point at `references/<file>.md` and run `python3 scripts/<check>.py` from the bot folder).
3. Say "start". The bot runs `yc-x-launch-desk-getting-started`: setup questions one at a time, then the first run.

---

By Dylan Pak · Moonshot (YC S26)

Created and curated by Dylan Pak. Independent template, not an official accelerator product. License: any copy, fork or republication (including on GitHub) must keep this credit.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
