---
name: humanizer
description: "YC S26 Launch Kit, shared: use when the owner says \"humanizer\", \"run the humanizer\", \"humanize this\", \"slop check\", \"de-slop this\", \"sounds like ai\" or \"too corporate\", or asks to strip machine tells or run the 7-pass scorecard. Quick mode strips tells without rebuilding; full mode runs all 7 passes. Also run quick mode on every draft before showing it. Used by YC Waitlist Email (quick mode only, before the send check) and YC Launch Copy. Full rebuilds go to edit-a-draft rewrite mode."
---

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# Humanizer

Strip machine tells from text. Not by running it through another rephraser, but by finding and removing the specific word, structure and style patterns that make a human reader stop trusting the writing. The goal is writing a person wants to read. This skill is never used to disguise who wrote something.

## Mode pick

- **Quick (anti-slop):** the owner says "slop check", "de-slop this", "sounds like ai", "too corporate", or you are about to show any draft. Strip machine tells without rebuilding the piece. Default for every outbound draft.
- **Full (7-pass):** the owner says "humanizer", "humanize this", or wants the scorecard. Run all 7 passes and present the clean version with a changelog.

If the draft is already close and mostly theirs, prefer edit-a-draft (edit mode) after the quick pass rather than a full rebuild.

## Quick mode (anti-slop)

Run this on anything before it leaves your hands, including a draft the owner says is already fine.

Cut on sight:
- Em dashes, en dashes, and semicolons. A period or a comma does the job.
- Banned words: Opener theater: "In today's fast-paced world", "I hope this finds you well", "I'm excited to announce", "Let's dive in".
- Announced structure: "Here's the breakdown", "Two things:", "To summarize", "At its core".
- Banned words: Corporate verbs and adjectives: leverage, streamline, seamless, robust, empower, elevate, unlock, supercharge, cutting-edge, best-in-class, game-changing, revolutionary, world-class.
- Copula dodging: "serves as", "stands as", "boasts", "acts as". Write "is" and "has".
- Fake-depth wrappers: highlighting, underscoring, showcasing, reflecting, ensuring, delivering.
- Definition by negation: "it's not X, it's Y", "more than just a".
- Padded triples where only one word is doing work: "fast, simple, and powerful".
- Stacked hedges: "could potentially help". Pick one hedge or drop it.
- Filler: "in order to" becomes "to", "due to the fact that" becomes "because", "at this point in time" becomes "now", "it is important to note that" gets deleted.
- Adjective claims with no number behind them. Either the number goes in or the claim comes out.
- Sentences whose only job is to reassure the reader. Question closers on a deliverable.

Then do the four rewrites that make prose sound spoken:
1. One idea per sentence. Break anything that needs a comma to stay standing.
2. Vary the length. Two long sentences in a row get one of them cut in half.
3. Active voice and a real subject. Somebody does something.
4. Read it aloud in your head. Anything you would not say to the person, rewrite.

Banned words: used on purpose in this before line. Before: "Our platform leverages best-in-class automation to seamlessly streamline your workflow, empowering teams to do more."
After: "It does the repeat work for you, so your team stops doing it by hand."

Before: "I wanted to reach out regarding our Q3 partnership opportunity and was wondering if you might have some time to connect."
After: "Checking in on the Q3 partnership. Got 20 minutes this week?"

The hard rule: this pass changes wording, never meaning. A fact, a name, a number, a price, or a claim that goes in comes out unchanged, or comes out marked as a gap.

When you run this inside edit-a-draft, be stricter about the owner's own phrasing. Cut the slop, leave the quirks.

## Full mode (7-pass scorecard)

When the owner provides text, run it through all 7 passes below. For each pattern found, rewrite the flagged segment. Then present the clean version with a brief scorecard showing what was changed and why.

## The 7 passes

### Pass 1: Banned Words and Phrases

Scan for and remove these words. They show up far more in machine-written drafts than in the way people actually write.

<banned_words>
TIER 1, strongest tells (remove on sight):
- Banned words: delve, tapestry (figurative), landscape (figurative), intricate/intricacies, meticulous/meticulously
- pivotal, crucial, vibrant, profound, showcasing, underscoring, highlighting, emphasizing
- foster/fostering, garner, bolstered, testament, enduring, interplay
- nestled, in the heart of, groundbreaking (figurative), renowned
- rich (figurative, as in "rich cultural heritage"), diverse array
- serves as, stands as, marks a, represents a (when substituting for "is")
- not just X but also Y, it's not about X it's about Y, it's not X it's Y
- here's the thing, here's why, here's what, here's how (AI opener crutch)
- let's dive in, let's explore, let's break it down, let's take a look
- the reality is, the truth is, the fact is, the bottom line is
- think about it, consider this, imagine this, picture this (when used as hollow rhetorical pivots)
- Banned words: game-changer, game-changing, next-level, level up, unlock (figurative)
- boasts (meaning "has"), enhancing, exemplifies, commitment to
- aligns with, resonates with, valuable insights, natural beauty

TIER 2, moderate tells (replace when they cluster with other tells):
- Additionally (starting a sentence), Moreover, Furthermore, In conclusion
- It is worth noting, It is important to note, Notably
- plays a vital/significant/crucial/pivotal/key role
- setting the stage for, marking/shaping the, reflects broader
- evolving landscape, focal point, indelible mark, deeply rooted
- encompassing, cultivating, ensuring (participial phrases at end of sentences)
- a diverse range of, a wide array of, myriad of
- Banned words: navigate (figurative), leverage (as verb), facilitate, utilize (when "use" works)
- Banned words: comprehensive, robust (for non-engineering contexts), seamless
- straightforward, certainly, palpable, nuanced (when used as filler praise)

TIER 3, context tells (flag only when 3 or more appear together):
- key (as adjective), significant, enhance, contributing to
- offering, providing, featuring, exploring
- Banned words: dynamic, innovative, cutting-edge, transformative

TRANSITION CRUTCHES: remove these filler transitions:
- "That said," "With that in mind," "On the flip side," "That being said," "Having said that," "When it comes to," "At the end of the day," "In terms of"

ADVERB PADDING: kill when they add nothing:
- significantly, effectively, particularly, essentially, fundamentally, increasingly, ultimately

EXPLANATORY PATTERN: kill the "This means" pattern where AI states something then immediately explains what it means. Trust the reader.

OVER-SIGNPOSTING: kill "First... Second... Third...", "Now let's move on to...", "Let's look at..." AI narrates its own structure. Just write the next section.

INCLUSIVE HEDGING: kill "Whether X or Y" constructions: "Whether you're a beginner or an expert," "Whether it's for personal or professional use." These try to address everyone and address no one.
</banned_words>

Banned words: Replacement strategy: Do not just swap synonyms. Restructure the sentence entirely. A sentence built around "delve into the intricate tapestry" cannot be saved by replacing three words. It needs to be rewritten from scratch with a specific, concrete claim.

### Pass 2: Structural Patterns

<structural_patterns>
ELIMINATE these structural tells:

1. PARTICIPIAL PHRASE ENDINGS: Sentences ending with "-ing" phrases that add superficial analysis.
   - BAD: "The mosque was built in 1492, reflecting the enduring influence of Ottoman architecture."
   - GOOD: "The mosque was built in 1492. Its design borrows directly from Ottoman models."

2. RULE OF THREE: Adjective triplets or three-item lists used to sound comprehensive.
   - BAD: "The conference features keynote sessions, panel discussions, and networking opportunities."
   - GOOD: "The conference runs keynotes and panels. There's time to meet people between sessions."

3. ELEGANT VARIATION: Using different words for the same thing to avoid repetition (protagonist, key player, eponymous character, all meaning the main character).
   - FIX: Pick one term and repeat it. Humans repeat words. AI avoids repetition artificially.

4. NEGATIVE PARALLELISMS: "Not just X, but also Y" and "It's not about X, it's about Y" and "It's not X. It's Y." constructions. These are the most performative, cringe AI patterns. They sound like a TED talk written by committee.
   - FIX: State the point directly. Cut the theatrical contrast. Say what the thing IS, not what it isn't-then-is.

5. PERFORMATIVE OPENERS: "Here's the thing." "Here's why." "Here's what most people get wrong." "Let's dive in." These are AI crutches that mimic human casualness but land as fake because they're empty. A real writer just starts talking.
   - FIX: Delete the opener. Start with the actual point. The sentence after "Here's the thing:" is always the real sentence.

6. TOPIC-SENTENCE PARAGRAPHS: Every paragraph opening with a clear topic sentence, followed by supporting evidence, concluded with a summary. Real writing is messier.
   - FIX: Vary paragraph openers. Start some with evidence, examples, or transitions. Let some paragraphs just... end.

7. COPULA AVOIDANCE: AI replaces "is" and "are" with "serves as," "stands as," "marks," "represents," "holds the distinction of being."
   - FIX: Use "is." Use "are." Simple copulatives are human.

8. SIGNIFICANCE INFLATION: Sentences claiming something "played a pivotal role," "marked a turning point," "set the stage for," or "shaped the landscape of."
   - FIX: State the specific impact or cut the sentence. If you cannot name the specific impact, the sentence is filler.

9. PERFORMATIVE DEPTH: Phrases designed to SOUND thoughtful without saying anything. "The implications are far-reaching." "This raises important questions." "The landscape is shifting." "This changes everything." These are the written equivalent of nodding sagely while saying nothing.
   - FIX: Either state the specific implication, the specific question, or cut it entirely.

10. REPETITIVE SENTENCE STARTERS: If 3+ consecutive sentences start with the same word ("The," "This," "It"), break the pattern. Humans naturally vary their sentence openings.

11. UNSOLICITED POSITIVE SPIN: AI can't stay neutral, it defaults to positive framing. If the original text doesn't call for cheerleading, remove it. State facts, not praise.
</structural_patterns>

### Pass 3: Punctuation and Typography

<punctuation_rules>
1. EM DASHES: Never use em dashes or en dashes. Replace every one with a comma, period, colon, or parentheses depending on context. Em dashes are the single most discussed AI punctuation tell. Do not use them anywhere in the output.

2. CURLY QUOTES: Replace all curly quotation marks with straight quotes. Curly quotes pasted in from a chat window are a common tell.

3. EXCESSIVE COMMAS: AI uses more commas per sentence than human writers. Cut unnecessary commas, especially before participial phrases.

4. SEMICOLONS: AI overuses semicolons to connect related clauses. Use periods instead. Shorter sentences read more human.

5. ELLIPSIS FOR FLOW: Use "..." to create breathing room and natural flow. Drop them mid-sentence where a speaker would trail off before finishing a thought, or between ideas where the connection is implied rather than stated. "The article ranked on page one within a week... and we hadn't even built backlinks yet." Not at the end of every paragraph. Not as a substitute for periods. Treat them like a pause in a conversation where the reader fills in the gap themselves.
</punctuation_rules>

### Pass 4: Sentence length and flow

AI text has uniform sentence length. Human text doesn't. But the fix isn't to alternate short-long-short mechanically.

<rhythm_rules>
1. Default to medium and long sentences. Let ideas build and connect through natural clauses, commas, and continuation. Very short sentences (under 6 words) should be rare, maybe one every few paragraphs, and only when something genuinely needs to land hard.

2. Three short sentences in a row sounds like a robot making bullet points. One short sentence after a long one sounds like a human making a point.

3. When in doubt, let the sentence keep going... most real writers do.

4. Break any sequence of 3+ sentences with similar word counts.

5. Start some sentences with "And" or "But." AI avoids this. Humans do it constantly.

6. Vary paragraph length. Some paragraphs should be a single line. Others run to 4-5 sentences. AI defaults to uniform 3-sentence blocks. That uniformity is a tell.
</rhythm_rules>

### Pass 5: Specificity Over Generality

AI writing is vague because LLMs regress to the statistical mean. The most common, generic description wins over the specific, unusual one.

<specificity_rules>
1. Replace every abstract claim with a concrete detail. "A significant contribution to the field" tells the reader nothing. "Reduced processing time from 4 hours to 11 minutes" tells them everything.

2. Kill hedging language: "It is worth noting," "It is important to consider," "One might argue." State the thing directly.

3. Remove vague attributions: "Experts say," "Observers have noted," "Industry reports suggest." Either name the expert and cite the report, or cut the claim.

4. Remove legacy/significance filler: "Contributing to the broader landscape of," "playing a vital role in the evolution of," "marking a pivotal moment in the history of." If it could describe anything, it describes nothing.

5. Preserve and amplify specifics from the original text. If the input contains a real number, a name, a date, a location, keep it. Those are the human fingerprints. Build sentences around them.
</specificity_rules>

### Pass 6: Tone and Voice

<tone_rules>
1. REMOVE PROMOTIONAL LANGUAGE: "Boasts a vibrant community," "showcasing its commitment to excellence," "a testament to innovation." Cut anything that sounds like a press release or travel brochure.

2. ALLOW IMPERFECTION: Human writing has rough edges. Not every transition is smooth. Not every paragraph connects perfectly to the next. A little friction is authentic.

3. USE CONTRACTIONS: "It's" not "It is." "Don't" not "Do not." "Can't" not "Cannot." Unless the register is genuinely formal (legal, academic), contractions make text read human.

4. FIRST AND SECOND PERSON WHERE APPROPRIATE: If the text is a blog post, email, or social content, use "I" and "you." AI defaults to third person and passive voice.

5. CUT THE SUMMARY: AI loves to end with a summary paragraph restating everything it just said. "In conclusion, we have explored..." Delete it. Humans end when they're done making their point.

6. REMOVE OUTLINE-LIKE CONCLUSIONS: Sentences about "challenges and future prospects" or "ongoing research and development" are AI padding. Cut them unless they contain specific, sourced claims.
</tone_rules>

### Pass 7: Formatting Tells

<formatting_rules>
1. NO BOLD FOR EMPHASIS in prose. Bold keywords in a paragraph is an AI tell inherited from listicles and READMEs. Use italics sparingly or rely on sentence structure for emphasis.

2. NO INLINE-HEADER LISTS: Bulleted lists where each item starts with a bold term followed by a colon and description. Rewrite as prose or use a simpler list format.

3. HEADING CASE: Use sentence case for headings, not Title Case. "How the system works" not "How The System Works."

4. NO EMOJI in professional/editorial content unless the brand voice explicitly uses them.

5. MARKDOWN ARTIFACTS: Remove stray asterisks (**bold**), hashtags (### Heading), or other Markdown syntax that got pasted into non-Markdown contexts.
</formatting_rules>

## Output Format

After rewriting, present:

```
[The rewritten text]

---

Changes made:
- [Category]: [specific change and why] (x N instances)
- [Category]: [specific change and why] (x N instances)
...
Machine-tell level: before [LOW / MEDIUM / HIGH], after [LOW / MEDIUM / HIGH]
```

Keep the changelog concise. Group similar changes. The owner wants to see what was fixed, not read a dissertation about it.

## Rules

- Never add em dashes or en dashes to the output. This is absolute. Use commas, periods, colons, or parentheses instead.
- Never invent facts. The rewrite must preserve every factual claim from the input. You are changing HOW things are said, not WHAT is said.
- Never make the text longer. Humanized text should be the same length or shorter than the input. AI pads; humans cut.
- If the owner provides a voice profile (from build-the-voice-profile), match that profile's patterns instead of generic "human" patterns.
- If the text is already human-sounding, say so. Do not rewrite for the sake of rewriting.
- The goal is to make the writing good for the person reading it. Never aim the rewrite at a tool score, and never use it to hide who wrote something.

## Kit fit
- **YC Waitlist Email** uses quick mode only, as a machine-tell strip on each draft before yc-waitlist-email-send-check. The send check still runs in full.
- **YC Launch Copy** runs quick mode on every draft (edit-a-draft and draft-for-a-channel call it) and full mode when the owner asks for the scorecard.
- Neither mode changes a fact, a number, a name or a claim. The kit's own style check (the bot's checks skill) still has the final word on dashes and banned words.

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
