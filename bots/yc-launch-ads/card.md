<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Launch Ads

> Studied over $3.3B in ad spend. Turns a competitor ad or your product notes into ready-to-film briefs, hooks and scripts, and checks every claim before you ship.

Import into Grok Bot: TEMPLATE_LINK (yc-launch-ads)

## Skills in this bot

- `yc-launch-ads-ad-script-and-hooks`
- `yc-launch-ads-brand-truth-pack`
- `yc-launch-ads-checks`
- `yc-launch-ads-claims-and-preflight`
- `yc-launch-ads-concept-spec`
- `yc-launch-ads-creative-qa`
- `yc-launch-ads-getting-started`
- `yc-launch-ads-knowledge`
- `yc-launch-ads-mechanism-and-market-mining`
- `yc-launch-ads-reference-to-brief`
- `yc-launch-ads-references`
- `yc-launch-ads-workflow`

## Shared kit skills it can use

- [`launch-kit-handoffs`](../../shared/launch-kit-handoffs/SKILL.md): who owns what across the six bots, run order, and the hand-off packet
- [`reference-teardown`](../../shared/reference-teardown/SKILL.md): measured teardown of one reference video or ad (cut map, style spec, transferable format)
- [`hook-library-keeper`](../../shared/hook-library-keeper/SKILL.md): keeps a verbal and visual hook library fresh, with an evidence gate
- [`paid-creative-loop`](../../shared/paid-creative-loop/SKILL.md): sections 3 to 5 only: brief, truth and visual QA, hand-off (the account read belongs to YC Ad Test Desk)

## Folders in this bot

- `persona/operating-rules.md`: the system prompt.
- `skills/`: one folder per skill.
- `references/`: templates, worked example and filled examples the skills point to (`claims-lanes-and-policy.md`, `examples`, `hook-and-script-library.md`, `sizing-math.md`, `step-table.md`, `templates.md`, `worked-example.md`).
- `scripts/`: 8 check scripts (Python 3, standard library only): `check_brand_pack.py`, `check_credit.py`, `check_facts_ledger.py`, `check_fields.py`, `check_hooks.py`, `check_leak.py`, `check_sections.py`, `check_style.py`. Run from this folder, for example `python3 scripts/check_brand_pack.py --selftest`.

## Start here

1. Put `persona/operating-rules.md` in the agent's instructions.
2. Install the whole bot folder: copy the folders in `skills/` (and the shared ones above) where your agent loads skills, and keep `references/` and `scripts/` together in one place the agent can read (skills point at `references/<file>.md` and run `python3 scripts/<check>.py` from the bot folder).
3. Say "start". The bot runs `yc-launch-ads-getting-started`: setup questions one at a time, then the first run.

---

By Dylan Pak · Moonshot (YC S26)

Created and curated by Dylan Pak. Independent template, not an official accelerator product. License: any copy, fork or republication (including on GitHub) must keep this credit.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
