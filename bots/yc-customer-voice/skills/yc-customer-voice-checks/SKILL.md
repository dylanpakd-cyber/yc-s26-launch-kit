---
name: yc-customer-voice-checks
description: "YC Customer Voice: use when the owner asks \"is this redacted?\", check the quote bank, do we have enough evidence; for the written hand checks the steps apply: redaction, quote bank, evidence bar and cards. Not for grading new quotes (evidence-grading)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "is this redacted?", check the quote bank, do we have enough evidence; this skill covers the written hand checks the steps apply: redaction, quote bank, evidence bar and cards. WHEN NOT: grading new quotes (evidence-grading). One-off asks can load this skill directly; a full run reaches it through yc-customer-voice-workflow.
# YC Customer Voice: hand checks

This bot has no scripts and runs no code. Every check named in the other skills ("the style check", "the redaction check" and so on) is one of the written checklists below. Apply it by hand, line by line, on the text in this chat. Then print each check as PASS or FAIL with the line that failed, and add the words "checked by hand" to the result. Never edit a draft only to make a check pass; fix the real problem or report it.

Every check gives one of three results: PASS, FAIL (list each failing line and why), or CANNOT CHECK (the input is missing; ask the owner for it).

## Redaction check
Run on every source before it is saved in the research and on every quote before it is shown.
Find and remove: email addresses; phone numbers; social handles; profile links (any link to a person's page on a social site or a link with /u/, /user/, /profile or /in/); street addresses; order, account, ticket or invoice numbers; card-like numbers; and likely personal names. Names hide behind cues such as "my name is", "I'm", "I am", "this is", "named", "called", "said", "told me", "husband", "wife", "son", "daughter", "boss", "Mr", "Mrs", "Ms", "Dr", and before "said", "wrote", "asked", "mentioned". Check cues at the start of a sentence and in any case. A Name, Customer, Speaker, Interviewee, Reviewer or Author field must hold a role label, not a name.
Role labels such as [BUYER-3] are fine. Product, brand and place names the owner lists are fine. Result: CLEAN, or each hit with its line.

## Quote-bank check
The bank is a table: ID | Quote | Verbatim | Source type | Source ref | Date | Speakers | Label | Tier | Theme | Use | Consent.
1. Every column present; IDs unique; no blank cells (use "n/a" or "unknown").
2. Verbatim is yes or no. Label is stated, observed or claimed.
3. Source ref is filled and not [NEED]. Speakers is a whole number, 1 or more. Speakers is counted by hand, so keep the source refs so a person can recount.
4. Tier is A, B or C and never higher than the evidence allows: A needs Verbatim yes and 3 or more speakers; B needs 2 or more speakers; everything else is C. A claimed row is at most C. A row whose Source type is friend (friends, family, the owner's own circle) is at most B, so a friends-only theme never reaches Tier A.
5. Use is internal, copy or public. Tier C is internal only. Copy needs Tier A or B. Public needs Consent "written" (a permission on file).
6. Quote text passes the redaction check.

## Evidence check
Part 1, the minimum-evidence bar (always):
1. 10 or more distinct source refs.
2. 2 or more source types, at least one of them not friend.
3. At least one theme with a Tier A row, or at least three themes with Tier B rows.
Below the bar, head every output "INSUFFICIENT EVIDENCE". That is an allowed, honest outcome, not a failure of the bot. Say what is missing and run the no-data path.
Part 2, the research document:
1. Every required section is present: Top pain points, Failed solutions, Desired outcomes, Objections, Misconceptions, Golden nuggets, Words to borrow and avoid, Triggers, What changed their mind, Alternatives, Necessity test, Strategy implications, Language analysis, Key personas, Open questions, Concepts.
2. Each section cites 2 or more quote-bank IDs or says "thin" (Open questions, Concepts and Key personas are exempt).
3. Every cited ID exists in the bank. Tier C IDs are cited only under Open questions.
4. Concepts is empty or says "left empty". This bot writes no ads.

## Cards check
Each card starts with a "## " heading and holds "Field: value" lines. No field may hold a personal identifier.
- index: Source, Date, Segment, Speaker role, Topic, Tags, Summary, Quote IDs, Decision moment, Redaction. Tags are 3 of: pain, desire, doubt, workaround, buying signal, failed solution, trigger, question. Redaction must be done.
- avatar: Nickname, Age band, Core problem, Moment it bites, Top fears, Emotional drivers, Failed solutions, Soundbites, Desired transformation, Market beliefs, Emotional blockers, Relationship impact, Objections, Awareness level, Where they spend time, Proof that persuades, Inferred. Top fears has 5 items separated by ";". Soundbites cite 3 or more quote-bank IDs at Tier A or B. Three avatars when the evidence shows three distinct core problems; fewer with an "Avatar count note:" that gives the evidence; never more than 3. Two avatars with the same core problem are the same person.
- objection: Objection, Count, Sources, Belief, Fear, Identity, Defuse, Proof, Does not claim, Avatar, Asset. Count is a number. Proof cites a source or says [NEED PROOF].
- locks: People, Not for, Empathy, Doing, Frustrations, Heaven, Hell, Positioning, How it works, Promise, So what, Proof, Priority, Honesty check. No lock field is [NEED]. Empathy cites a Tier A or B quote-bank ID. Honesty check must be PASS.

## Leak check
Run on every draft and on anything the owner may share or export. FAIL on any of these:
1. A file path from a computer (a home folder, a workspace folder, a path starting with a tilde).
2. A social handle (an at-sign followed by a name).
3. A money amount written as a currency sign followed by digits that did not come from the owner's sourced facts in this chat.
4. An email address.
5. The name of an outside writer, creator, coach or paid course, unless the owner asked for a credited quote.
6. Any private word the owner listed (their company, product, people or customers) appearing where the text will be shared outside the owner's chat.

## Export check (only when the owner asks to export or copy a skill)
1. The first line of every exported skill is the dylan-pak-credit comment.
2. The last two lines are "Created and curated by Dylan Pak." and the license note.
3. The leak check passes on every exported file.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
