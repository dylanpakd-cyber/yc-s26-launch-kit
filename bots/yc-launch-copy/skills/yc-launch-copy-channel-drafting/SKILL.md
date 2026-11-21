---
name: yc-launch-copy-channel-drafting
description: "YC Launch Copy: use when the owner asks \"write the LinkedIn post\", turn this into an essay, a thread or follow-up posts; for drafting essays, LinkedIn posts and satellite posts, in-house by default. Not for checking facts (honesty-and-fact-gate) or the launch-day X post (YC X Launch Desk owns it)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "write the LinkedIn post", turn this into an essay, a thread or follow-up posts; this skill covers drafting essays, LinkedIn posts and satellite posts, in-house by default. WHEN NOT: checking facts (honesty-and-fact-gate) or the launch-day X post (YC X Launch Desk owns it). One-off asks can load this skill directly; a full run reaches it through yc-launch-copy-workflow.
# SKILL: channel-drafting

Purpose: write the piece natively for each platform in {PLATFORMS} from the same outline and facts, then adapt approved pieces to other platforms without pasting. Each version stands alone and states the same claim.

## Use when
- Draft mode: a finalist hook and outline exist. Triggers: "write the post", "draft it", "LinkedIn version", "X post", "thread", "article", "newsletter blurb", "launch post".
- Adapt mode: a draft was approved. Triggers: "repurpose", "turn this into a thread", "make a LinkedIn version", "atomize this".
- The owner shares a public video or transcript and wants posts from it.

Not for: email sequences or the X launch timeline (other bots own those).

## Inputs
- Outline, finalist hook, facts ledger, voice rules.
- {PLATFORMS}. Default: X and LinkedIn.
- {CAMPAIGN_URL} and where the link should sit.
- Launch facts if mentioned: {LAUNCH_DATE}, {LAUNCH_TZ}, {PRICE_RULE}.

## Steps: draft mode
1. **Fact inventory first.** List the ledger facts this piece may use. Anything else becomes [NEED].
2. **One version per platform,** not several. Say in one line why this shape fits.
3. **X post.** Line one: the hook, under 130 characters, works alone. Line two does a paragraph's work: what it is, for whom, why now. Then proof (one ledger number or a named fact), one quotable line, the link above "Show more" or in the planned reply. One idea.
4. **X thread** (only when each post stands alone): post one is the hook and promise; each next post is one point; the last post closes the hook's loop and holds the link or the action.
5. **LinkedIn post.** The first two lines carry the hook before the fold. Short paragraphs with white space. One story and one lesson. A concrete close. Link in the first comment by default. No hashtag wall. A closing question only if genuine.
6. **Essay or article.** Headline from the finalists. Opening scene or claim. Sections with headings that make sense alone. Teach a complete skill before naming the product. End with the action. Last line bookends the headline.
7. **Short follow-ups.** One satellite post per question from the idea map.
8. **DM or note.** Two to four sentences, specific to one reader, one ask. The owner sends it.
9. **Newsletter blurb or release note.** What changed, who it helps, how to try it.
10. **Short video script** (if asked). Open on the strongest true moment in the first few seconds. Captions on. Show the product doing the thing. One quotable line. End on the strongest sentence. A new visual every few seconds.
11. **Channel gate.** Start each X or LinkedIn draft with two metadata lines, "Idea:" (one sentence) and "Link placement:" (in post, reply, first comment or none), then a blank line, then the post. Run the channel check (x) or the channel check (linkedin). It checks the 280-character X limit per post (links count as 23), that the link sits where the placement line says (first post on X; never in a LinkedIn body), the 210-character LinkedIn fold, and one idea per post.
12. **Lint.** Run the style check and the leak check on each version.

## Steps: adapt mode
1. Keep the pinpoint and the facts identical.
2. Rebuild the opening, length and structure for how people read on the target platform. Never paste.
3. Atomize a long piece into five short posts: a one-line declaration, an antithesis, a three-bullet list, a mistake and its fix, a conversation question.
4. Re-run the honesty gate on every new version.

## Public video or transcript to posts
Extract the pinpoint, the best three quotes (exact, with time stamps), and the claims (checked later). Credit the source in the draft. Never present another person's words as the owner's.

## Lanes
This bot owns essays, LinkedIn posts and satellite posts (short follow-ups, threads that expand one point). YC X Launch Desk owns the launch-day X post. If the owner asks for the launch-day X post, say that desk owns it and offer a satellite post instead.

## No writing room set
When {WRITING_ROOM} is empty or the owner said no to sharing, draft in-house from the owner's facts only. Every missing detail is a [NEED: what] mark. Never fill a gap with an invented scene, detail, person, quote or outcome, even to make a draft read better.

## Gate
- Each version stands alone and states the same claim.
- Each version passes the launch-post checklist in yc-launch-copy-knowledge.
- The channel check passes on each X and LinkedIn version.
- The style check and the leak check pass on each version.
- Every number traces to the ledger (checked again at step 6).

## Output
```
PLATFORM: X
<draft>
Why this shape: ...
Facts used: <ledger rows> | Open [NEED]: ...
Link placement: ...

PLATFORM: LinkedIn
<draft>
...
Next: yc-launch-copy-line-edit-and-rhythm
```

## If things go wrong
- **The piece needs a fact the ledger lacks.** Write the line with [NEED: what]. Never smooth the sentence so the gap hides.
- **Too long for the platform.** Cut beats from the end of the outline, not the proof.
- **Owner wants five versions of one post.** Give one per platform plus up to two alternative openers. More options slow the owner down.
- **Thread posts depend on each other.** Rewrite so each stands alone, or make it a single post.
- **Round cap.** Two drafts per platform. Then the owner picks.

## Never
- Never publish, schedule, reply or DM.
- Never paste one format into another.
- Never use another writer's text as the owner's.
- Never add a hashtag wall or a fake question.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Checks (repo edition): each check named in this skill has a script in this bot's `scripts/` folder. Run it from the bot folder and paste its PASS or FAIL line: the style check: `python3 scripts/check_style.py <file or folder> [--banned FILE] [--exempt NAME ...]`; the leak check: `python3 scripts/check_leak.py <file or folder> [--terms FILE] [--exempt NAME ...]`; the channel check: `python3 scripts/check_channel.py <x|linkedin> <draft file>`. If you cannot run code (for example inside a Grok Bot template), apply the same written checklist from yc-launch-copy-checks by hand and write "checked by hand".

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
