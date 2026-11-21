---
name: outlier-idea-archive
description: "YC S26 Launch Kit, shared: use when the owner says \"log this post\", \"swipe file\", \"archive this outlier\", or asks which first lines are working before a draft. Keeps a swipe log of posts that spread and names the first-line wording move. Not for drafting the post itself."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# Outlier idea archive

## When
You are collecting posts that actually spread, or you are about to draft and need proven first lines.

## Add
1. Confirm the post is real (you opened it). No invented metrics.
2. Append one JSON line to the owner's swipe log: handle, url, date, lane, views, likes, bookmarks, hook (verbatim first 1 to 3 sentences), why_it_works, steal (the wording move, not just the article shape), asset (what they gave away, or null).
3. Skip duplicates by URL. Skip empty motivation.

Example line (fictional account, invented numbers):
```
{"handle": "@example", "url": "{POST_URL}", "date": "{DATE}", "lane": "build in public", "views": 41000, "likes": 900, "bookmarks": 310, "hook": "6:40am. I shipped the onboarding rewrite. 212 sign-ups by lunch.", "why_it_works": "a receipt in the first eight words", "steal": "time + I did + number", "asset": null}
```

## Study the wording first
Do not draft until you can name which of these the first 6 to 8 words are:
- Receipt: time + I did + number + machine
- Crowd split: everyone [behavior]. the ones [exception]: [one word]
- Offer: price or deliverable first
- Named quote or quit: a [role] told me why he [quit verb] [named system]

Ban: "people keep asking", announcing "I have N things", invented friend-on-a-train scenes, category nouns (the minute, the crew, the system), manifesto parallelisms.

## Write from it (only after study)
1. Read recent entries in the same lane.
2. Steal the first-line wording move. Structure is secondary.
3. Never copy their story, clients, or numbers.
4. If `asset` is null, do not draft a take with a fake gate.
5. If we do not have a real receipt, do not fake the skeleton.

## Anti-pattern
A post that is only an opinion plus "reply X for my 3 tips" does not go in as a winner. Tag it as a miss if it is the owner's own.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
