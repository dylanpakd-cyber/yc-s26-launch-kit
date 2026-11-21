<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Launch Copy

> Sharpened our LinkedIn and X posts for launch. Turns your messy launch thoughts into clear posts and essays in your own voice.

Import into Grok Bot: TEMPLATE_LINK (yc-launch-copy)

## Skills in this bot

- `yc-launch-copy-channel-drafting`
- `yc-launch-copy-checks`
- `yc-launch-copy-clarity-interview`
- `yc-launch-copy-getting-started`
- `yc-launch-copy-honesty-and-fact-gate`
- `yc-launch-copy-hooks-and-headlines`
- `yc-launch-copy-idea-map-and-outline`
- `yc-launch-copy-knowledge`
- `yc-launch-copy-line-edit-and-rhythm`
- `yc-launch-copy-references`
- `yc-launch-copy-workflow`
- `yc-launch-copy-writing-room`

## Shared kit skills it can use

- [`launch-kit-handoffs`](../../shared/launch-kit-handoffs/SKILL.md): who owns what across the six bots, run order, and the hand-off packet
- [`hook-library-keeper`](../../shared/hook-library-keeper/SKILL.md): keeps a verbal and visual hook library fresh, with an evidence gate
- [`x-source-scan`](../../shared/x-source-scan/SKILL.md): 5 to 8 proven X posts on a topic, ranked by how repackageable they are
- [`outlier-idea-archive`](../../shared/outlier-idea-archive/SKILL.md): swipe log of posts that spread, with the first-line wording move named
- [`meeting-transcripts-to-copy-desk`](../../shared/meeting-transcripts-to-copy-desk/SKILL.md): turns meeting transcripts into redacted pull-quotes for the copy bots

## Folders in this bot

- `persona/operating-rules.md`: the system prompt.
- `skills/`: one folder per skill.
- `references/`: templates, worked example and filled examples the skills point to (`examples.md`, `prompt-set.md`, `step-table.md`, `templates.md`, `worked-example.md`).
- `scripts/`: 8 check scripts (Python 3, standard library only): `check_channel.py`, `check_credit.py`, `check_facts_ledger.py`, `check_fields.py`, `check_hooks.py`, `check_leak.py`, `check_sections.py`, `check_style.py`. Run from this folder, for example `python3 scripts/check_channel.py --selftest`.

## Start here

1. Put `persona/operating-rules.md` in the agent's instructions.
2. Install the whole bot folder: copy the folders in `skills/` (and the shared ones above) where your agent loads skills, and keep `references/` and `scripts/` together in one place the agent can read (skills point at `references/<file>.md` and run `python3 scripts/<check>.py` from the bot folder).
3. Say "start". The bot runs `yc-launch-copy-getting-started`: setup questions one at a time, then the first run.

---

By Dylan Pak · Moonshot (YC S26)

Created and curated by Dylan Pak. Independent template, not an official accelerator product. License: any copy, fork or republication (including on GitHub) must keep this credit.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
