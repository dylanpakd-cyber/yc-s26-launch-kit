<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
# Sample campaign (invented)

Every fact in this folder is invented for an example meal-planning app called "Example Planner". It shows a finished campaign folder that passes every script. Copy the shape, never the lines.

Files: `brief.md` (step 1), `plan.md` (step 2), `drafts/email-01.md` to `drafts/email-08.md` (steps 3 to 6).

Run from this bot's folder:
```
python3 scripts/check_brief.py references/sample-campaign/brief.md
python3 scripts/check_run.py references/sample-campaign/plan.md
python3 scripts/check_email.py --facts references/sample-campaign/brief.md references/sample-campaign/drafts/*.md
```
All three exit 0. The email check still lists MANUAL items (13 and 14) for a person to tick.


---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
