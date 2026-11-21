---
name: yc-launch-copy-references
description: "YC Launch Copy: use when the owner asks \"show me an example\", a blank template, a worked example; for reference material: templates, the prompt set, the worked example and filled examples. Not for doing the step itself (load that step's skill)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "show me an example", a blank template, a worked example; this skill covers reference material: templates, the prompt set, the worked example and filled examples. WHEN NOT: doing the step itself (load that step's skill). One-off asks can load this skill directly; a full run reaches it through yc-launch-copy-workflow.
# YC Launch Copy: references

Templates, examples and reference tables for the YC Launch Copy steps. Everything here is invented and labelled as an example, or is a method, not a result. Copy the shape, never the facts. Never present an example number as the owner's. Checks named here are in yc-launch-copy-checks: each has a script in this bot's `scripts/` folder, with the written checklist as the fallback when code cannot run.

## Where each part lives (repo edition)
The material is split into files in this bot's `references/` folder so each one stays short. When another skill points here by section name (for example "Templates" or "Worked example"), open the file listed for that section. Inside a Grok Bot template, where only the skills are installed, the template edition of this skill keeps the sections inline.
- **Worked example: raw thoughts to a LinkedIn launch post (fictional)**: `references/worked-example.md`
- **Fill-in templates: YC Launch Copy**: `references/templates.md`
- **Prompt set: YC Launch Copy**: `references/prompt-set.md`
- **Examples (invented)**: `references/examples.md`

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
