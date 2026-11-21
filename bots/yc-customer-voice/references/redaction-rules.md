<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Customer Voice: Redaction rules

Default level: strict. {REDACTION_RULES} may add more, never fewer.

### Always remove
| Item | Replace with |
|---|---|
| Personal names (first, last, nicknames) | role label: [BUYER-3], [PARENT-1], [TEACHER-2] |
| Social handles and profile links | [HANDLE REMOVED] |
| Emails and phone numbers | [CONTACT REMOVED] |
| Street addresses, small towns tied to a person | region only ("a small town") or remove |
| Employer or school tied to a person | "a school", "a mid-size company" |
| Order, account, ticket, invoice numbers | [ORDER REMOVED] |
| Health, money or legal detail that could identify | summary in general words |
| Faces or names in screenshots | describe the screenshot instead |

### Keep
The problem, the emotion and the exact words around it. Misspellings. Times and situations ("at 8am on a school day").

### Summarise instead of quoting when
The words would identify the person even after removal (a rare job plus a place, a public story). Mark it "summary, not quote". It can be Tier B at most.

### The check
The redaction check flags emails, phone numbers, handles, profile URLs, street addresses, order or account numbers, "Name:" style fields with a value, and likely names after cues like "said", "my name is", "my husband". Keep non-person words (product names, brands, places) on an allow list. The name check is a judgment call: a CLEAN result does not replace one human read of the quote bank before hand-off.

### Never
Never keep the unredacted original in the research. Never re-identify a person. Never quote a minor. Never publish a customer quote without written permission on file.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
