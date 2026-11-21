---
name: yc-x-launch-desk-founder-post-and-video-script
description: "YC X Launch Desk: use when the owner asks \"write/fix my launch post\", the launch video script; for drafting the launch-day founder post on X and the video script. Not for the readiness gate on a finished post (test-of-300), or essays and LinkedIn posts (YC Launch Copy owns those)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "write/fix my launch post", the launch video script; this skill covers drafting the launch-day founder post on X and the video script. WHEN NOT: the readiness gate on a finished post (test-of-300), or essays and LinkedIn posts (YC Launch Copy owns those). One-off asks can load this skill directly; a full run reaches it through yc-x-launch-desk-workflow.
# SKILL: founder-post-and-video-script

Purpose: draft the founder's launch post and a retention-first video script so the first small audience stops, understands and reacts. Drafts only. The founder posts.

## Use when
- The brief passed (yc-x-launch-desk-launch-playbook Part A).
- The owner says "write the launch post", "first line", "ten first lines", "launch video script", "first five seconds", "link above Show more", "harsh read", "pressure-test this launch script".
- A Test of 300 run sent rewrites back.

## Inputs
- The brief, chosen angle, market card and facts ledger.
- What can be shown on screen: real product, a demo path, one to three moments a viewer would call surprising.
- Length target for the video. Default: 45 to 90 seconds, plus a 15-second cut for the second beat.
- {CAMPAIGN_URL} and link placement decided in the brief.

## Steps: Part A, the post
1. **Ten first lines.** Types: the claim; the named incident; the number; the contrarian truth; the demonstration; the stake; the confession; the question a stranger already has; the contrast; the promise. Rules: a short first sentence; concrete nouns; a question only if the answer surprises; under about 130 characters so it fits before "Show more"; no emoji openers.
2. **Mute and stranger test.** With no context, does a stranger know what this is about? Pick one. Keep the other nine for the second beat.
3. **Score the chosen line.** Five questions, 1 to 5: callout or open loop; would the founder say it aloud to a friend; a stranger understands; no insider words; easy to picture. Write it to hooks and run the hook check.
4. **Body.** Line two says what it is and for whom. Then proof (a ledger number or named fact). One quotable line built to be reposted with an opinion. The link where the brief says.
5. **Teach before pitch (long posts).** Teach a small complete skill first and name the product after.
6. **Plain language pass.** Vary sentence length. Start with concrete nouns and real numbers. End on the strongest sentence. Remove throat-clearing and filler. Run the style check.
7. **Harsh read, six questions:** (1) a stranger gets it in one read; (2) the first line stops a thumb; (3) the claim is true and checkable; (4) the visual proves the claim; (5) a line is worth quoting; (6) the link is placed on purpose. Any no: rewrite.

## Steps: Part B, the video script
1. **Launch spine.** Introduction (the bold claim inside an argument the timeline already cares about), problem (plain, no context jumps), agitate (cost, embarrassment, status; leave room to disagree), solution (the mechanism shown, not described; the strongest outcome).
2. **Five hook variants,** each answering within seven seconds: what is launching; why it matters; why it never existed before, or why now. Pick one primary and two alternates. The primary puts the most surprising moment or hardest proof first.
3. **Banned openings:** logo sting, cinematic establishing shot, long founder talk, slow story setup, the "excited to announce" opener.
4. **Script card, beat by beat.** Fields per beat: time, on screen, spoken line, on-screen text, camera move, which doubt it answers (is this what I clicked; is this for me; is it worth staying). Template in yc-x-launch-desk-references ("Templates").
5. **Four elements, or kill the draft:** a bold claim bigger than the product; an early payoff or proof in the open; no context gaps in the first ten seconds; the strongest outcome (money or status over "saves time" when true).
6. **Retention checks.** Something changes on screen every couple of seconds in the open. One idea per scene. Captions large and on. The payoff lands before a viewer would leave. Talking head alone in only a few shots. The close shows the product working, not a logo card.
7. **Mute and eyes-closed tests.** Sound off: picture and text carry the idea. Eyes closed: audio carries it.
8. **Same claim.** The post and the video make the same claim with the same facts.
9. **Ledger check.** Apply the facts-ledger check on the post and the script card.
10. **Second-beat cut.** Mark the strongest 15 seconds for a short version.

## Lanes
This desk owns the launch-day X post and its video script. Essays, LinkedIn posts and satellite posts belong to YC Launch Copy; if the owner asks for those here, say so and keep to the launch post.

## Gate
- The hook check passes on the chosen first line.
- The facts-ledger check passes on the post and the script.
- The channel check (x) passes on the post (280 limit, link position, one idea).
- Harsh read is six of six yes.
- All four video elements present. Then hand to yc-x-launch-desk-test-of-300.

## Output
```
TEN FIRST LINES: 1 to 10, chosen: <n>, score 5 4 4 5 4
POST DRAFT: <ready to copy>
HARSH READ: 6/6
VIDEO: primary hook + 2 alternates
SCRIPT CARD: [0-5s] ... [5-15s] ... [proof window] ... [destination] ... [close] ...
Mute test: PASS | Eyes-closed test: PASS | Four elements: 4/4
Next: yc-x-launch-desk-test-of-300
```

## If things go wrong
- **No surprising moment to show.** Use the hardest real number or a side-by-side of old way and new way. If neither exists, run a text-and-screenshot post instead of video and say so.
- **The claim needs insider knowledge.** Bridge the gap in line two, or pick a wider angle from the angle sheet.
- **Owner wants the founder story first.** Put one line of it after the proof, not before.
- **Round cap.** Two rewrite rounds before Test of 300. Then run it on the best version.

## Never
- Never invent a number, user, quote or result.
- Never use sales adjectives in place of a demo.
- Never post or schedule.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the style check: `python3 scripts/check_style.py <file or folder> [--banned FILE] [--exempt NAME ...]`; the hook check: `python3 scripts/check_hooks.py <hooks file> [--max-chars 130]`; the facts-ledger check: `python3 scripts/check_facts_ledger.py <draft file> <ledger file>`; the channel check: `python3 scripts/check_channel.py <x|linkedin> <draft file>`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-x-launch-desk-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
