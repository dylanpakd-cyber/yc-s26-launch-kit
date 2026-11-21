---
name: yc-launch-copy-writing-room
description: "YC Launch Copy: use when the owner asks \"use my writing room\", give me the exact prompt, run this through my AI writer; for preparing the exact prompt for an outside AI writing tool after the owner's yes, then returning its unedited reply with fact flags. Not for drafting in-house, which is the default (channel-drafting)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "use my writing room", give me the exact prompt, run this through my AI writer; this skill covers preparing the exact prompt for an outside AI writing tool after the owner's yes, then returning its unedited reply with fact flags. WHEN NOT: drafting in-house, which is the default (channel-drafting). One-off asks can load this skill directly; a full run reaches it through yc-launch-copy-workflow.
# SKILL: writing-room

Purpose: run the clarity-first prompt set, either inside an outside AI writing tool the owner already uses ({WRITING_ROOM}) or by the bot itself. When a room is used, the bot returns the exact prompt it prepared and the room's reply unedited, and flags only fact problems. The prompts are written in this pack's own words.

## Use when
- The owner says "use my writing room", "run it through the room", "send this to the AI writer", "give me the exact prompt", "unedited reply".
- The owner wants a specific prompt from the set below: pinpoint session, two-year lessons, six openers, five antithesis openers, 4A headlines, clear headline, short essay outline, pain-dream-fix, what-how-why, ten expansions, atomize, sentence polish, revelation audit, throat-clearing cut, one-three-one rhythm, long-form diagnosis.

Not for: replacing the bot's own gates. Every room output still goes through hooks, line edit and the honesty gate.

## Inputs
- A passing or draft pinpoint card from yc-launch-copy-clarity-interview.
- {WRITING_ROOM}: the tool's name, and whether the owner pastes prompts themselves or has connected it.
- The owner's approval of what may be shared with the outside tool.

## Data-sharing caution (read before every room run)
An outside writing tool is a third party. Before any text leaves the chat:
1. Strip unreleased numbers, customer names, private plans, prices not yet public, and anything under a claim lock.
2. Show the owner the exact prompt.
3. Ask: "OK to share this with {WRITING_ROOM}?" Only a yes moves on.
4. Log the yes in the room log ("Owner approved sharing: YES").
Default when there is no yes: the bot runs the same prompt itself and labels the result "run in-house".

The bot never creates an account, buys a plan, connects socials or schedules posts in a writing tool.

## Steps
1. **Pick the prompt** from the set in yc-launch-copy-references ("Prompt set") that fits the need. One prompt per run.
2. **Fill it** with the pinpoint, reader, platform and goal. Be specific: always name the platform, the reader and the goal.
3. **Strip private data** per the caution above.
4. **Show the exact prompt** to the owner and get a yes to share.
5. **Run it.** If the owner pastes it into the room, wait for them to paste the reply back. If the room is connected and the owner said yes, send that one prompt only.
6. **Return the reply unedited.** Do not fix style, trim or reorder. Quote it whole.
7. **Flag facts only.** Under the reply, list every number, name, claim or story the reply added that is not in the ledger. Each flag: quoted phrase, "not in ledger", what would source it.
8. **Fill the room log** from yc-launch-copy-references ("Templates"). Run the fields check (room-log).
9. **Hand on.** The owner picks which parts to keep. Those parts enter the normal chain at the right step (outline, hooks, or draft).

## Owner yes and the in-house default
- In-house drafting is the default. The writing room is optional.
- Nothing goes to {WRITING_ROOM} until the owner has seen the exact prompt and said yes in chat. No yes: run the prompt in-house and label it "run in-house".
- In-house runs follow the no-room rule: only the owner's facts plus [NEED] marks. No invented scenes, details, people, quotes or outcomes.

## Gate
- The fields check (room-log) passes: room, prompt, reply, "Owner approved sharing: YES", fact flags (write "none" if none).
- The reply shown is byte for byte what the room returned.
- Every fact the room added is flagged or found in the ledger.

## Output
```
ROOM RUN: <prompt name> in {WRITING_ROOM} | or: run in-house
PROMPT (exact):
<prompt>
REPLY (unedited):
<reply>
FACT FLAGS:
1. "<phrase>" | not in ledger | needs: <source>
Next: <step this feeds>
```

## If things go wrong
- **Owner says no to sharing.** Run in-house. Never send a trimmed version without asking again.
- **The room invents facts.** That is expected. Flag every one. Do not delete them from the reply; the reply stays unedited.
- **The room is down or the owner cannot paste.** Run in-house and label it.
- **The reply ignores the prompt.** Run the same prompt once more with the platform, reader and goal stated first. Round cap: two runs per prompt.
- **Owner wants the bot's own edit of the reply.** That is yc-launch-copy-line-edit-and-rhythm, run on a copy. The room log keeps the original.

## Never
- Never share private data with an outside tool without the owner's yes.
- Never edit the room's reply before showing it.
- Never connect socials, publish, schedule or buy plans in the room.
- Never present the room's invented facts as the owner's.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the fields check: `python3 scripts/check_fields.py <kind> <filled file>`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-launch-copy-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
