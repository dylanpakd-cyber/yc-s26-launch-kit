<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Waitlist Email

> Helped us turn 1,000+ reservations into 100 backers in the first 24 hours. Writes the emails that turn your waitlist into customers.

Import into Grok Bot: TEMPLATE_LINK (yc-waitlist-email)

## Skills in this bot

- `yc-waitlist-email-checks`
- `yc-waitlist-email-email-brief-and-voice`
- `yc-waitlist-email-email-draft-and-edit`
- `yc-waitlist-email-getting-started`
- `yc-waitlist-email-knowledge`
- `yc-waitlist-email-launch-close-sequence`
- `yc-waitlist-email-references`
- `yc-waitlist-email-send-check`
- `yc-waitlist-email-waitlist-conversion-plan`
- `yc-waitlist-email-welcome-and-nurture`
- `yc-waitlist-email-workflow`

## Shared kit skills it can use

- [`launch-kit-handoffs`](../../shared/launch-kit-handoffs/SKILL.md): who owns what across the six bots, run order, and the hand-off packet

## Folders in this bot

- `persona/operating-rules.md`: the system prompt.
- `skills/`: one folder per skill.
- `references/`: templates, worked example and filled examples the skills point to (`brief-and-voice-template.md`, `claims-and-honesty-lanes.md`, `email-file-format.md`, `email-shells.md`, `sample-campaign`, `send-timing-defaults.md`, `step-table.md`, `subject-line-bank.md`).
- `scripts/`: 6 check scripts (Python 3, standard library only): `check_brief.py`, `check_credit.py`, `check_email.py`, `check_leak.py`, `check_pack.py`, `check_run.py`. Run from this folder, for example `python3 scripts/check_brief.py --selftest`.

## Start here

1. Put `persona/operating-rules.md` in the agent's instructions.
2. Install the whole bot folder: copy the folders in `skills/` (and the shared ones above) where your agent loads skills, and keep `references/` and `scripts/` together in one place the agent can read (skills point at `references/<file>.md` and run `python3 scripts/<check>.py` from the bot folder).
3. Say "start". The bot runs `yc-waitlist-email-getting-started`: setup questions one at a time, then the first run.

---

By Dylan Pak · Moonshot (YC S26)

Created and curated by Dylan Pak. Independent template, not an official accelerator product. License: any copy, fork or republication (including on GitHub) must keep this credit.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
