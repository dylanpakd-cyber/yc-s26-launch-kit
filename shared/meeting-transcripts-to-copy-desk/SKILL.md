---
name: meeting-transcripts-to-copy-desk
description: "YC S26 Launch Kit, shared: use when the owner wants meeting or call transcripts turned into redacted, channel-ready source material: strip confidential content from founder meetings, pull quotes for posts, ads or emails. Works with any notetaker's transcript. Feeds yc-customer-voice-call-index-and-redaction and the copy bots."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# Meeting transcripts to copy desk

Turns raw founder meeting transcripts into plenty of channel-ready source material for the copy bots. Confidential and private content is stripped before anything reaches a writer.

## Inputs
- Meeting source: transcripts the owner pastes or exports from whatever notetaker they use. Use the full transcript, not just an AI summary.
- Time window: what the owner said, else the last 24 hours of meetings they attended.
- Destination: the owner's chat or the named copy bot, as a draft packet. Never post publicly.

## Steps
1. List meetings in the window. Skip cancelled, empty, or personal-only calendar blocks the owner did not ask to include.
2. For each meeting, take the full transcript.
3. Redact before any hand-off. Remove and replace with `[redacted]`:
   - Passwords, codes, API keys, wallet or seed phrases, card numbers
   - Exact amounts of fundraising, runway, salary, or deals unless the owner said to keep money talk
   - Health, family, relationship, or legal matters
   - Named people outside the company when the topic is sensitive (candidates, investors in closed talks, customers under NDA)
   - Anything the speakers marked off-record, confidential, or "don't put this in writing"
   - Private addresses, personal phone numbers, home details
4. Keep: product language, pains, stories, metaphors, objections, proof points, jokes that are on-brand, and how the founder actually talks.
5. Package one file per meeting:
   - Title, date, attendees (first names or roles only)
   - Redacted transcript
   - 5 to 12 pull-quotes that could become posts, ads, or newsletter lines (still redacted)
   - Tag each pull-quote with a channel hint: X, LinkedIn, newsletter, site, paid social ad, script
6. Deliver to the copy bot as a draft packet in chat. Do not publish, schedule, or send anywhere public.
7. Log what was redacted at category level only ("3 salary mentions, 1 investor name"). Never log the secret itself.

## Rules
- Drafts only. The founder approves before anything ships.
- Plenty over polish: raw usable lines beat rewritten corporate copy.
- If a transcript is mostly confidential, skip the meeting and say so in one line.
- Never invent quotes. Only lines that appear in the transcript.
- Customer calls go through yc-customer-voice-call-index-and-redaction as well, so the redaction check runs on them.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
