<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
# Sample research folder (invented)

Everything here is invented for an example family planner app. No real person, review or post is quoted. It shows a finished research folder that passes all five scripts. Copy the shape, never the content.

Run from this bot's folder:
```
python3 scripts/check_redaction.py references/sample-research/*.md references/sample-research/raw/*.md
python3 scripts/check_cards.py --kind index references/sample-research/index.md
python3 scripts/check_quote_bank.py references/sample-research/quote-bank.md
python3 scripts/check_evidence.py --bank references/sample-research/quote-bank.md --doc references/sample-research/research-doc.md
python3 scripts/check_cards.py --kind avatar --bank references/sample-research/quote-bank.md references/sample-research/avatars.md
python3 scripts/check_cards.py --kind objection references/sample-research/objections.md
python3 scripts/check_cards.py --kind locks --bank references/sample-research/quote-bank.md references/sample-research/locks.md
python3 scripts/check_pack.py .
```
Every command exits 0.


---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
