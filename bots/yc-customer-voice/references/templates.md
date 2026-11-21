<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Customer Voice: Templates

Copy these blocks exactly. The check scripts read the field names. Every value in braces is filled from evidence or marked [NEED] or "inferred". All examples in the skills are invented.

### Index card (one per call or source) -> `index`
```
## Call {NN}
Source: {C-NN, owner notes | transcript | ticket T-NN | survey S-NN}
Date: {as given}
Segment: {early tester | waitlist | churned | buyer | unknown}
Speaker role: {role label, never a name}
Topic: {one line}
Tags: {three of: pain, desire, doubt, workaround, buying signal, failed solution, trigger, question}
Summary: {two lines}
Quote IDs: {Q-numbers pulled from this source}
Decision moment: {when they decided or hesitated, or n/a}
Redaction: done
```

### Quote bank -> `quote-bank`
```
| ID | Quote | Verbatim | Source type | Source ref | Date | Speakers | Label | Tier | Theme | Use | Consent |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | {exact redacted words} | yes | review | R-01 | {date} | 3 | stated | A | {theme} | internal | none |
```
Verbatim: yes or no. Label: stated, observed or claimed. Tier: A (verbatim and 3 or more speakers), B (2 or more speakers), C (the rest; every claimed row). Use: internal, copy (A or B only) or public (needs Consent "written"). Consent: none or written.

### Research document -> `research-doc`
Sixteen "## " sections in this order: Top pain points; Failed solutions; Desired outcomes; Objections; Misconceptions; Golden nuggets; Words to borrow and avoid; Triggers; What changed their mind; Alternatives; Necessity test; Strategy implications; Language analysis; Key personas; Open questions; Concepts. Each section cites two or more bank IDs or says "thin". Concepts says "Left empty."

### Avatar card -> `avatars`
```
## Avatar {N}: {nickname}
Nickname: {role-based nickname}
Age band: {range} (estimate)
Core problem: {one sentence plus emotional context}
Moment it bites: {time, place, who else}
Top fears: {1}; {2}; {3}; {4}; {5}
Emotional drivers: {two dominant}
Failed solutions: {what, why it failed, IDs}
Soundbites: {three or more Tier A or B IDs}
Desired transformation: {a concrete ordinary day}
Market beliefs: {belief about products like this}
Emotional blockers: {what stops them}
Relationship impact: {how it touches others}
Objections: {ranked, with IDs}
Awareness level: {unaware | problem | solution | product | most aware}
Where they spend time: {sources}
Proof that persuades: {proof and format}
Inferred: {every inferred field}
```
If fewer than three avatars, add:
```
## Avatar count note
Avatar count note: {n} avatars, because the evidence shows {n} distinct core problems ({IDs}). Needed to find a third: {what}.
```

### Five-layer objection stack -> `objections`
```
## Objection {N}: {short name}
Objection: "{their words}" ({ID})
Count: {number of independent people}
Sources: {IDs and refs}
Belief: {layer 2}
Fear: {layer 3}
Identity: {layer 4}
Defuse: {layer 5, one line}
Proof: {source or ID, or [NEED PROOF: what]}
Does not claim: {one line}
Avatar: {which}
Asset: {ad | email | landing page FAQ | post | onboarding}
```

### Lock page -> `locks`
```
## Lock page {N}: {avatar} x {objection}
People: {who}
Not for: {who not}
Empathy: {Tier A or B ID}
Doing: {from bank}
Frustrations: {from bank}
Heaven: {best day, from bank}
Hell: {worst day, from bank}
Positioning: {vs real alternatives}
How it works: {mechanism in buyer words}
Promise: {checkable outcome}
So what: {last true answer of the drill}
Proof: {IDs and owner proof}
Priority: {the one first job}
Honesty check: PASS
```

### Hand-off pack -> `handoff`
Per desk (ads, email, copy, X): the lock page, passing angles, the quote pack (Tier A and B rows with Use "copy", redacted, with IDs), the do-not-use list, and the line "Evidence status: {PASS | INSUFFICIENT}". The owner says yes before any other bot reads it.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
