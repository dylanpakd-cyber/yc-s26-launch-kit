---
name: yc-launch-ads-brand-truth-pack
description: "YC Launch Ads: use when the owner asks \"set up our brand facts\", what we can and can't say about the product; for building the one-page brand truth pack every brief draws from. Not for checking a specific line (claims-and-preflight)."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

WHEN TO USE: the owner asks "set up our brand facts", what we can and can't say about the product; this skill covers building the one-page brand truth pack every brief draws from. WHEN NOT: checking a specific line (claims-and-preflight). One-off asks can load this skill directly; a full run reaches it through yc-launch-ads-workflow.
# SKILL: brand-truth-pack

Purpose: build the one block every other skill reads, so ads talk about the real product to the real buyer in the buyer's own words. Without it, every script could be for any product.

## Use when
- First run for a product, before any concept, brief or script.
- The owner says "set up the brand", "brand pack", "brand truth", "what do we know about the buyer".
- The brand-pack check fails, or any later skill finds a thin spot (no offer, no never-claims, no customer words).
- The offer, price rule or destination changed. Re-run the Offer section only.

Not for: brand look, logo or positioning strategy. The owner owns those.

## Inputs
Ask in one message, then fill gaps one question at a time:
1. {PRODUCT} in one line, and the product page or a paste of it.
2. {OFFER} and {PRICE_RULE}: what the buyer gets today, its terms, the guarantee word for word. "No offer" is a valid answer.
3. {AUDIENCE} in one line.
4. Where customer words live: reviews, support emails, sales calls, forum threads, survey answers. The owner pastes them.
5. Competitors the owner knows of. Three is enough to start.
6. Anything the product must never claim. Ask for at least three.
7. {BANNED_WORDS_FILE} and {CLAIM_LOCKS}, pasted in chat.

Defaults when an input is missing: no offer means "no offer" in the Offer section and no price on any ad. No competitor list means you ask once, then mark Competitors thin.

## Steps
1. **Open the template.** Copy the BRAND-PACK template from yc-launch-ads-references ("Templates") into the owner's chat. Nothing is saved outside its sections: Offer, Never claims, Customer phrases, Avatars, Competitors, Voice, Thin spots.
2. **Read the sources in two waves.** Wave one: the product page and offer, then the customer words the owner pasted, then the competitors' longest-running public ads. Wave two, only when the owner wants depth: comments under those ads, and the mechanism work in yc-launch-ads-mechanism-and-market-mining.
3. **One writer fills the file.** Read every source before writing any section. Patterns only show when one reader sees them all: the same pain in a review, in an ad comment and in a competitor's hook.
4. **Offer.** The offer and guarantee word for word, the price rule, where ads link. If the destination page says something different from the owner, flag it. That mismatch is the first thing to fix.
5. **Never claims.** What the product does not do, results it cannot promise, comparisons it cannot back, regulated words. At least three bullets.
6. **Customer phrases.** Exact words only, kept with their misspellings and slang, each with "source:" on the same line (for example "source: review site, {DATE}" or "source: support email, {DATE}"). Sort them under pain, desire, doubt. At least ten.
7. **Avatars.** Three to five buyer types. Each one is a person with a moment, not a demographic: the trigger moment, the failed past fix, the awareness level, the proof they need, and two of their own phrases.
8. **Competitors.** Who runs long ads to this buyer, which angles everyone has already heard, which nobody runs.
9. **Voice.** "Words we use" (from customers) and "Words we never use" (ad-speak and the owner's banned list).
10. **Feature to objection table** inside Avatars or Offer: each real feature next to the doubt it answers.
11. **Slop sweep.** Remove invented numbers, filler, empty sections and unsourced quotes. Run the style check and the leak check.
12. **Run the bar.** Apply the brand-pack check by hand. Read each FAIL line to the owner with why it makes ads worse.
13. **Thin spots.** List what is weak, and ask the owner at most three questions only they can answer.

## Gate
The brand-pack check passes. That means: an offer line or "no offer"; 3 or more never-claims; 10 or more customer phrases, each with a source. Never edit the pack just to pass the check. A phrase without a real source does not count.

WARN lines (avatars, competitors, voice) do not block the next step, but list them under Thin spots.

## Output
Lands in the owner's chat as one block:
```
BRAND PACK STATUS: PASS | THIN
Solid: <three bullets>
Thin: <bullets from WARN and FAIL lines>
Owner questions (max 3):
1. ...
Next: yc-launch-ads-mechanism-and-market-mining
```
Then the filled brand pack.

## If things go wrong
- **No customer words at all.** Do not write any. Ask the owner for one of: ten support emails, ten reviews, three call notes, or permission to read public reviews of the category. Until then, the status is THIN and no script is written.
- **Fewer than ten phrases after reading everything.** Keep the real ones. Status THIN. Scripts may still be written for the one avatar that has five or more phrases; mark them "thin pack".
- **Owner and page disagree on the offer.** Use the page as truth for ads (that is what the buyer sees) and flag the gap at the top of the report.
- **Owner pushes to skip the pack.** Say once what breaks without it (invented offers, generic hooks, copied promises). Then do the smallest version: Offer, Never claims, five phrases. Mark it THIN.
- **A check is unclear.** Apply the three hard-bar rules by hand and say "checked by hand".
- **Round cap.** Two rounds of owner questions. After that, ship the THIN pack with its gaps named.

## Never
- Never invent a customer phrase, review, testimonial or number.
- Never read files, other bots or shared memory to find the owner's facts. Ask.
- Never copy the owner's customer words, spend or results into anything that leaves the owner's chat.
- Never claim affiliation with any accelerator or brand.

Revision cap: two revision rounds per piece of work. After round 2, stop, show the best version with its open flags, and ask the owner how to go on.
Hand checks: this bot runs no scripts. Every check named in this skill is a written checklist in yc-launch-ads-checks. Apply it by hand, line by line, and write "checked by hand" next to the result.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
