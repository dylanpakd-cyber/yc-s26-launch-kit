---
name: yc-customer-voice-call-index-and-redaction
description: "YC Customer Voice: use when the owner asks \"here are call notes/transcripts\", log or redact a call; for indexing and redacting customer calls. Not for mining public reviews (voice-mining)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "here are call notes/transcripts", log or redact a call; this skill covers indexing and redacting customer calls. WHEN NOT: mining public reviews (voice-mining). One-off asks can load this skill directly; a full run reaches it through yc-customer-voice-workflow.
# SKILL: call-index-and-redaction

Use when: the owner pastes call notes, transcripts, interview summaries, support tickets or survey answers and says "index these calls", "save these notes", "redact this", "what did people say on calls", "pull quotes from the calls", or runs the test prompt with five call notes. Run it before any mining or grading. It never records or joins a call.

Purpose: store customer call material safely, in a form other steps can search and count. Redaction happens before anything is saved. Each source gets an index card.

Drafts only: the library lives in the owner's chat. Nothing is shared, posted or sent. Nothing leaves the owner's chat without the owner's explicit yes.

## Inputs
- Transcripts, summaries or notes from {CALL_SOURCE}, pasted by the owner.
- {REDACTION_LEVEL} and {REDACTION_RULES}. Default: strict.
- Optional: the segment each call came from (early tester, waitlist, churned user).

## Steps
1. **Accept, do not fetch.** Take only what the owner pastes in this chat. Never join, record or transcribe a live call. Never ask for logins.
2. **Number each source.** Calls are C-01, C-02. Support tickets T-01. Surveys S-01. Keep the owner's date "as given"; do not guess dates.
3. **Redact before saving.** Replace every name, handle, email, phone, address, profile link, employer tied to a person, order or account number, and identifying medical or financial detail with a role label: [BUYER-1], [PARENT-2], [MANAGER-1]. Keep the problem and the exact words around it. If the words themselves would identify the person, write a summary instead and mark it "summary, not quote".
4. **Run the redaction check** by hand. Fix every hit and re-run until CLEAN. Product, brand and place names that are not people go on an allow list the owner confirms in chat. Read line by line for the patterns in yc-customer-voice-checks and yc-customer-voice-references ("Redaction rules"), and say "checked by hand".
5. **Write an index card per source** (template in yc-customer-voice-references ("Templates")): source, date as given, segment, speaker role, topic, exactly three tags (pain, desire, doubt, workaround, buying signal, failed solution, trigger, question), a two-line summary, the IDs of quotes pulled, the decision moment, and "Redaction: done".
6. **Extract.** From each source pull: the best exact quotes (redacted), questions the person asked, objections, failed solutions, the moment they decided or hesitated. Give each pulled item an ID (Q-numbers) so step 3 can grade it.
7. **Separate verified from claimed.** "I tried three apps and quit each in a week" is stated. "My whole team wants one" is claimed: it is a claim about other people. "Showed me the sticky notes on their screen" is observed. Write the label beside each item.
8. **Keep a running tally** per theme across calls: theme, number of calls, call IDs. One call mentioning a theme twice still counts as one.
9. **Retrieval.** When asked "what did people say about X", return matching cards and quotes with their IDs. Never invent a call. If nothing matches, say "no source says this yet".
10. **Call-notes-to-brief.** On request, turn the tally into a one-page digest for the creative bots: top recurring themes with counts and IDs, the best three quotes per theme (Tier A or B only, after step 3), open questions. No hooks, no scripts.

## Worked example (invented, every detail made up)
Raw note pasted by the owner: "Call with a teacher who uses our planner. She said she forgets what she promised parents by lunch. Tried a notes app, never opened it. Asked if it works offline."

Redacted and indexed:
```
## Call 03
Source: C-03, owner notes
Date: as given (owner says last week)
Segment: early tester
Speaker role: teacher
Topic: remembering promises
Tags: pain, failed solution, question
Summary: Forgets promises made to parents by midday. A notes app failed because it was never opened.
Quote IDs: Q11, Q12, Q13
Decision moment: n/a (already a tester)
Redaction: done
```
Pulled items: Q11 "forgets what she promised parents by lunch" (paraphrase, stated), Q12 "tried a notes app, never opened it" (paraphrase, stated, failed solution), Q13 "does it work offline?" (question, stated). All three are paraphrases because the owner's notes are not verbatim. Step 3 will grade them B at best.

## Gate (exit criteria)
- The redaction check is CLEAN on every saved source.
- The cards check (index) prints PASS.
- Every pulled item has an ID, a source ref and a label.

## Failure handling
- Notes are summaries, not transcripts: accept them, mark every pulled item "paraphrase". They can reach Tier B, never A.
- An item cannot be redacted without losing its meaning: leave it out and note "removed for privacy" on the card.
- The owner pastes a recording link: say you only work from text the owner provides, and ask for notes or a transcript.
- Fewer than five sources: index them anyway, and tell the owner the minimum-evidence bar (10 sources) is not met yet.
- Revision cap: two redaction rounds per source. If hits remain after the second, quarantine the source (do not use it) and tell the owner which lines need a human look.

## Rules
Never record or join calls. Never store contact details. Never guess who a speaker is. Never upgrade a paraphrase to a quote.

## Output contract
`research/raw/` (redacted sources), `index` (cards in the template format), a theme tally table in chat (theme, calls, IDs), and the redaction result line. Report: Done, Blocked, Next.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-customer-voice-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
