<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

# YC Launch Ads: Worked example

Everything here is invented to show the shape of each output. No real company, person, price or result. Use it to see what "done" looks like at each step.

The product: a fictional meal-plan app that keeps one shared weekly plan on every phone in a household. Offer: a free first week of shared plans. Price: kept off the ad ({PRICE_RULE} says "price on the page only").

### Step S: sizing
The owner states a launch goal and their own page-to-sign-up rate. Sign-up-to-buyer is [NEED] (no history), so the bot sizes a message test only and says so.

### Step 0: brand truth pack
The owner pastes twelve support emails and fifteen app-store reviews. The bot fills the BRAND-PACK template. Three never-claims: "saves money" (no data), "healthier meals" (health claim), "used by nutritionists" (no endorsement). Customer phrases include invented examples like "the plan dies by Wednesday" and "I'm the only one who knows what's for dinner", each with "source: example review, {DATE}". See references/examples/brand-pack.example.md. `python3 scripts/check_brand_pack.py references/examples/brand-pack.example.md` prints PASS.

### Step 1: mining
Quick depth. The own-offer teardown finds that the page never answers "does my partner need to pay too". That goes on the objection list. The mechanism sentence: "The plan lives where everyone in the house already looks, so nobody has to ask." The ladder ranks "failed past solution: the notes-app plan" first because it has the most customer phrases and a demo proof.

### Step 2: concept spec
See references/examples/concept-card.example.md. The insight lock settles the promise after three rounds of "so what?": shared plan, then fewer dinner questions, then "the parent stops being the household's dinner help desk". `python3 scripts/check_fields.py concept references/examples/concept-card.example.md` prints PASS.

### Step 3 and 4: brief, script, hooks
See references/examples/brief.example.md (`python3 scripts/check_fields.py brief references/examples/brief.example.md` PASS). Body format: story with "but" and "therefore" turns. See references/examples/script.example.txt and references/examples/hooks.example.txt. `python3 scripts/check_hooks.py references/examples/hooks.example.txt` prints PASS for all three. The third hook also carries a grader line that computes to 7.4. The ads harsh read is six of six. 

### Step 5: claims
`python3 scripts/check_facts_ledger.py references/examples/script.example.txt references/examples/ledger.example.md` prints PASS: "seven" in the script is a word, and "2 phones" and "7 dinners" are in the ledger. The honesty bar is 5 of 5. The honest admission ("not because I gave up") makes the main claim land harder. One Yellow flag: "plan once" is fine only if the plan does not need weekly re-entry. Rewrite kept as is with the condition confirmed by the owner.

### Step 6: creative QA
The first cut has a 0.6 second black lead-in. FAIL with timecode. Whoever built the file trims it. Round two: PASS.

### Step 7: preflight
Preflight (yc-launch-ads-claims-and-preflight Part B) checks the test card the owner pasted from the companion YC Ad Test Desk (its example is `bots/yc-ad-test-desk/references/examples/test-card.example.md`). Result: READY WITH FIXES (UTM tag missing on cut C). The owner fixes the tag and types "yes, launch the test" in chat. The owner launches. The bot does not.

### After step 7
Test design, the read and the winner decode for this same example are in the companion YC Ad Test Desk's worked example (`bots/yc-ad-test-desk/references/worked-example.md`).

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
