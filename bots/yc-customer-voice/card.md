<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Customer Voice

> Found the real reason people bought our product. Turns your customer calls, reviews and comments into a sourced research doc, a ranked objection list and buyer profiles.

Import into Grok Bot: TEMPLATE_LINK (yc-customer-voice)

## Skills in this bot

- `yc-customer-voice-buyer-avatars`
- `yc-customer-voice-call-index-and-redaction`
- `yc-customer-voice-checks`
- `yc-customer-voice-evidence-grading`
- `yc-customer-voice-getting-started`
- `yc-customer-voice-insight-to-truth`
- `yc-customer-voice-knowledge`
- `yc-customer-voice-objection-map`
- `yc-customer-voice-references`
- `yc-customer-voice-research-document`
- `yc-customer-voice-voice-mining`
- `yc-customer-voice-workflow`

## Shared kit skills it can use

- [`launch-kit-handoffs`](../../shared/launch-kit-handoffs/SKILL.md): who owns what across the six bots, run order, and the hand-off packet
- [`meeting-transcripts-to-copy-desk`](../../shared/meeting-transcripts-to-copy-desk/SKILL.md): turns meeting transcripts into redacted pull-quotes for the copy bots

## Folders in this bot

- `persona/operating-rules.md`: the system prompt.
- `skills/`: one folder per skill.
- `references/`: templates, worked example and filled examples the skills point to (`claims-and-honesty-lanes.md`, `mining-methods.md`, `no-data-path.md`, `redaction-rules.md`, `sample-research`, `step-table.md`, `templates.md`).
- `scripts/`: 8 check scripts (Python 3, standard library only): `check_cards.py`, `check_credit.py`, `check_evidence.py`, `check_leak.py`, `check_pack.py`, `check_quote_bank.py`, `check_redaction.py`, `check_style.py`. Run from this folder, for example `python3 scripts/check_cards.py --selftest`.

## Start here

1. Put `persona/operating-rules.md` in the agent's instructions.
2. Install the whole bot folder: copy the folders in `skills/` (and the shared ones above) where your agent loads skills, and keep `references/` and `scripts/` together in one place the agent can read (skills point at `references/<file>.md` and run `python3 scripts/<check>.py` from the bot folder).
3. Say "start". The bot runs `yc-customer-voice-getting-started`: setup questions one at a time, then the first run.

---

By Dylan Pak · Moonshot (YC S26)

Created and curated by Dylan Pak. Independent template, not an official accelerator product. License: any copy, fork or republication (including on GitHub) must keep this credit.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
