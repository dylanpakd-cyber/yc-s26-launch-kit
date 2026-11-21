<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Waitlist Email: Brief and voice template

Copy this into `brief`. Fill every line from the owner or a page the owner provides. Add a source in parentheses to each fact. Do not infer facts from a page's tone. Run the brief check on the filled file.

```
Offer: [NEED: exact offer and terms]
Price rule: copy the price from the checkout page on the day; never round
Guarantee: [NEED: exact wording, or "none"]
Launch date: [NEED: weekday, month, day]
Close date: [NEED: weekday, month, day, time, or "no deadline"]
Time zone: [NEED: audience time zone]
Segments: [NEED: segments the tool can really build]
Signup promise: [NEED: exact words of the signup page and consent line]
Primary action: [NEED: the single thing the reader does]
Support route: reply to this email
Never claims: [NEED: first]; [NEED: second]; [NEED: third]
Voice source: default starter voice
Avg sentence words: 12
Contractions: yes
Sign-off: {SENDER_NAME}
Banned words: built-in list only
Links per email: 1
```

### Default starter voice (for a founder with no past emails)
- First person. Talk to one reader as "you".
- Plain, warm, direct. A true scene beats a clever line.
- Average twelve words per sentence. One to three sentences per paragraph.
- Contractions yes. No dashes as punctuation, no emoji, at most one exclamation mark.
- Open on the point. A welcome or a reply may open with "Hi {FIRST_NAME|there}, it's {SENDER_NAME}."
- Sign off with the first name.
- One primary link. Label names what they get in three to eight words.
- Subject: 45 characters or fewer. Preview: 100 or fewer.
- No hype, no fake urgency, no apology for writing.
- Provisional until the owner approves three drafts. Then run the voice profile on those three and replace the defaults with observed rules.

### Locks file template ({EMAIL_LOCKS})
```
Required: {SENDER_NAME}, {UNSUBSCRIBE}, support route
Primary links: 1
Subject limit: 45 characters
Length bands: last-hours 120; welcome 200; launch 350; all others 400 words
Banned: built-in list plus {BANNED_WORDS_FILE}
Never claims: copied from `brief`
Offer block: copied exactly from `brief`
```

### Per-email brief (one block per plan row)
```
Email number:
Type:
Segment and state:
One job:
Question this answers:
Doubt:
Proof to use (source):
Offer block (copied from brief):
Primary action and link:
Deadline (exact wording or none):
Exclude:
Voice source and special locks:
Length band:
What happens after the click:
```

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
