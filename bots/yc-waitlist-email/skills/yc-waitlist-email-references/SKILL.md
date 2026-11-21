---
name: yc-waitlist-email-references
description: "YC Waitlist Email: use when the owner asks \"show me an example\", a blank template, a worked example; for reference material: templates, the email file format, email shells, the subject-line bank, send-timing defaults and the sample campaign. Not for doing the step itself (load that step's skill)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "show me an example", a blank template, a worked example; this skill covers reference material: templates, the email file format, email shells, the subject-line bank, send-timing defaults and the sample campaign. WHEN NOT: doing the step itself (load that step's skill). One-off asks can load this skill directly; a full run reaches it through yc-waitlist-email-workflow.
# YC Waitlist Email: references

Templates, examples and reference tables for the YC Waitlist Email steps. Everything here is invented and labelled as an example, or is a method, not a result. Copy the shape, never the facts. Never present an example number as the owner's. Checks named here are in yc-waitlist-email-checks: each has a script in this bot's `scripts/` folder, with the written checklist as the fallback when code cannot run.

## Where each part lives (repo edition)
The material is split into files in this bot's `references/` folder so each one stays short. When another skill points here by section name (for example "Templates" or "Worked example"), open the file listed for that section. Inside a Grok Bot template, where only the skills are installed, the template edition of this skill keeps the sections inline.
- **Brief and voice template**: `references/brief-and-voice-template.md`
- **Claims and honesty lanes**: `references/claims-and-honesty-lanes.md`
- **Email file format**: `references/email-file-format.md`
- **Five worked email shells**: `references/email-shells.md`
- **Send-timing defaults**: `references/send-timing-defaults.md`
- **Subject-line bank**: `references/subject-line-bank.md`
- **Sample campaign (invented)**: `references/sample-campaign/` (11 files, start with `references/sample-campaign/README.md`). An invented brief, run plan and all eight sample emails. Every check script passes on it; use it for a practice run.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
