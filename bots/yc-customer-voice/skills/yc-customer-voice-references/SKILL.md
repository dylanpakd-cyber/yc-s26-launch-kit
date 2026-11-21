---
name: yc-customer-voice-references
description: "YC Customer Voice: use when the owner asks \"show me an example\", a blank template, a worked example; for reference material: templates, mining methods, redaction rules, the no-data path and the sample research set. Not for doing the step itself (load that step's skill)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "show me an example", a blank template, a worked example; this skill covers reference material: templates, mining methods, redaction rules, the no-data path and the sample research set. WHEN NOT: doing the step itself (load that step's skill). One-off asks can load this skill directly; a full run reaches it through yc-customer-voice-workflow.
# YC Customer Voice: references

Templates, examples and reference tables for the YC Customer Voice steps. Everything here is invented and labelled as an example, or is a method, not a result. Copy the shape, never the facts. Never present an example number as the owner's. Checks named here are in yc-customer-voice-checks: each has a script in this bot's `scripts/` folder, with the written checklist as the fallback when code cannot run.

## Where each part lives (repo edition)
The material is split into files in this bot's `references/` folder so each one stays short. When another skill points here by section name (for example "Templates" or "Worked example"), open the file listed for that section. Inside a Grok Bot template, where only the skills are installed, the template edition of this skill keeps the sections inline.
- **Templates**: `references/templates.md`
- **Claims and honesty lanes for hand-offs**: `references/claims-and-honesty-lanes.md`
- **Mining methods (full steps)**: `references/mining-methods.md`
- **No-data path: a pre-launch founder with little or no customer material**: `references/no-data-path.md`
- **Redaction rules**: `references/redaction-rules.md`
- **Sample research (invented)**: `references/sample-research/` (9 files, start with `references/sample-research/README.md`). An invented research set (index cards, quote bank, research doc, three avatars, objection stacks, a lock page, a hand-off pack and one redacted call). Every check script passes on it; use it for a practice run.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
