<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Ad Test Desk

> Found our first winning angle in 3 days, then kept iterating on the winners. Plans your ad tests before you spend and tells you which ads really won and what to try next.

Import into Grok Bot: TEMPLATE_LINK (yc-ad-test-desk)

## Skills in this bot

- `yc-ad-test-desk-checks`
- `yc-ad-test-desk-getting-started`
- `yc-ad-test-desk-knowledge`
- `yc-ad-test-desk-references`
- `yc-ad-test-desk-test-design-and-reads`
- `yc-ad-test-desk-winner-decode-and-iteration`
- `yc-ad-test-desk-workflow`

## Shared kit skills it can use

- [`launch-kit-handoffs`](../../shared/launch-kit-handoffs/SKILL.md): who owns what across the six bots, run order, and the hand-off packet
- [`reference-teardown`](../../shared/reference-teardown/SKILL.md): measured teardown of one reference video or ad (cut map, style spec, transferable format)
- [`paid-creative-loop`](../../shared/paid-creative-loop/SKILL.md): account read, reference research, brief, truth and visual QA, hand-off for paid creative

## Folders in this bot

- `persona/operating-rules.md`: the system prompt.
- `skills/`: one folder per skill.
- `references/`: templates, worked example and filled examples the skills point to (`examples`, `step-table.md`, `templates.md`, `testing-math.md`, `worked-example.md`).
- `scripts/`: 5 check scripts (Python 3, standard library only): `check_brand_pack.py`, `check_credit.py`, `check_fields.py`, `check_leak.py`, `check_style.py`. Run from this folder, for example `python3 scripts/check_brand_pack.py --selftest`.

## Start here

1. Put `persona/operating-rules.md` in the agent's instructions.
2. Install the whole bot folder: copy the folders in `skills/` (and the shared ones above) where your agent loads skills, and keep `references/` and `scripts/` together in one place the agent can read (skills point at `references/<file>.md` and run `python3 scripts/<check>.py` from the bot folder).
3. Say "start". The bot runs `yc-ad-test-desk-getting-started`: setup questions one at a time, then the first run.

---

By Dylan Pak · Moonshot (YC S26)

Created and curated by Dylan Pak. Independent template, not an official accelerator product. License: any copy, fork or republication (including on GitHub) must keep this credit.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
