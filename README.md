# YC S26 Launch Kit

<!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this repo or any file in it (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->

**By Dylan Pak · Moonshot (YC S26)**

Six narrow AI agents that run a startup launch end to end: customer research, launch copy, the X launch, waitlist email, paid-social ads and ad testing. Each one does one job, drafts only, and leaves every outbound action (posting, sending, spending) to you.

They ship as Grok Bot templates. This repo is the full, open edition: every skill as a plain `SKILL.md` folder, the full operating rules for each bot, the long-form references (templates, worked examples, filled examples) and the check scripts that a template cannot carry. Use them in Grok Bot, Claude Code, Cursor, or any agent that can load markdown skills.

## Two ways to use it

### Path A: as Grok Bots

Each bot is a Grok Bot template. Import it, then say "start". The bots carry their own skills, so there is nothing else to install.

| Bot | Import |
|---|---|
| YC X Launch Desk | TEMPLATE_LINK |
| YC Launch Ads | TEMPLATE_LINK |
| YC Ad Test Desk | TEMPLATE_LINK |
| YC Waitlist Email | TEMPLATE_LINK |
| YC Customer Voice | TEMPLATE_LINK |
| YC Launch Copy | TEMPLATE_LINK |

Templates have a size limit and run no code, so the template edition is slimmer and its checks are written checklists applied by hand. This repo has the long form.

### Path B: as skills in your coding agent

Install the whole kit, or one bot, with the installer (bash only; the check scripts need `python3`, standard library only):

```bash
git clone https://github.com/dylanpakd-cyber/yc-s26-launch-kit.git && cd yc-s26-launch-kit && ./install.sh --target claude --all
```

| Agent | Command | Installs into |
|---|---|---|
| Claude Code | `./install.sh --target claude --all` | `~/.claude/skills/` (add `--project` for `./.claude/skills/`) |
| Cursor | `./install.sh --target cursor --all` | `~/.cursor/skills/` (add `--project` for `./.cursor/skills/`) |
| Codex and other agents that read `AGENTS.md` | `./install.sh --target codex --all --agents-md` | `~/.agents/skills/` (add `--project` for `./.agents/skills/`); `--agents-md` adds a short marked block to `./AGENTS.md` |
| Anything else | `./install.sh --target path/to/skills --all` | the folder you name |

One bot instead of six: `./install.sh --target claude --bot yc-launch-copy` (see `./install.sh --list`). Preview first with `--dry-run`. Re-running is safe: it replaces only the folders it owns.

What lands in the skills folder, as flat `SKILL.md` folders:
- `<bot>-operating-rules/`: the bot's system prompt as a skill, with the bot's `references/` and `scripts/` beside it.
- one folder per skill (`<bot>-workflow`, `<bot>-getting-started`, the step skills, `<bot>-checks`, `<bot>-references`), each with a line pointing at its bot folder so `references/...` and `scripts/...` paths keep working.
- the shared kit skills that bot uses, once each.
- `yc-s26-launch-kit-router/`: picks the right bot for a request.

Then tell the agent to load `<bot>-operating-rules` first (or the router skill), and say "start" or ask for one job ("write the welcome email").

Rather work from the clone? Open the repo in your agent: [AGENTS.md](AGENTS.md) (and [CLAUDE.md](CLAUDE.md), which points to it) tell any coding agent how to route a request to the right bot, load `persona/operating-rules.md` first, then `<bot>-workflow`. For Cursor rules or another agent's system prompt, paste the bot's `persona/operating-rules.md`.

## The six bots

| Bot | What it did for us | Skills | Check scripts | Grok Bot template |
|---|---|---|---|---|
| [YC X Launch Desk](bots/yc-x-launch-desk/card.md) | The Grok Bot we used to hit 1.4M views on X in 3 days. Runs your 48-hour launch on X: the founder post, quote-post drafts for your network and a launch-day plan. It drafts; you post. | 11 | 10 | TEMPLATE_LINK |
| [YC Launch Ads](bots/yc-launch-ads/card.md) | Studied over $3.3B in ad spend. Turns a competitor ad or your product notes into ready-to-film briefs, hooks and scripts, and checks every claim before you ship. | 12 | 8 | TEMPLATE_LINK |
| [YC Ad Test Desk](bots/yc-ad-test-desk/card.md) | Found our first winning angle in 3 days, then kept iterating on the winners. Plans your ad tests before you spend and tells you which ads really won and what to try next. | 7 | 5 | TEMPLATE_LINK |
| [YC Waitlist Email](bots/yc-waitlist-email/card.md) | Helped us turn 1,000+ reservations into 100 backers in the first 24 hours. Writes the emails that turn your waitlist into customers. | 11 | 6 | TEMPLATE_LINK |
| [YC Customer Voice](bots/yc-customer-voice/card.md) | Found the real reason people bought our product. Turns your customer calls, reviews and comments into a sourced research doc, a ranked objection list and buyer profiles. | 12 | 8 | TEMPLATE_LINK |
| [YC Launch Copy](bots/yc-launch-copy/card.md) | Sharpened our LinkedIn and X posts for launch. Turns your messy launch thoughts into clear posts and essays in your own voice. | 12 | 8 | TEMPLATE_LINK |

Suggested order for one launch: Customer Voice, then Launch Copy and Launch Ads, then Waitlist Email, then X Launch Desk on launch day, then Ad Test Desk once ads are ready to spend. The shared skill [`launch-kit-handoffs`](shared/launch-kit-handoffs/SKILL.md) has the full map and a hand-off packet to paste between bots. Every bot also works on its own.

## What is in the repo

```
README.md
AGENTS.md, CLAUDE.md          routing instructions for coding agents
install.sh                    installs bots as skills for Claude Code, Cursor, Codex or any folder
LICENSE                       credit requirement + CC BY 4.0 for the prose
bots/<bot>/
  card.md                     the bot's card: proof line, what it does, skills, folders, how to start
  persona/operating-rules.md  the bot's system prompt (persona, one job, router, house rules)
  skills/<skill>/SKILL.md     one folder per skill
  references/                 templates, worked example, step table, filled examples (the skills point here)
  scripts/                    check scripts (Python 3, standard library only, each with --selftest)
shared/<skill>/SKILL.md       skills several bots can use
```

Each bot has the same skill shape:
- `<bot>-getting-started`: the first conversation (setup questions one at a time).
- `<bot>-workflow`: the operating rules, the router and the chain. Load it before every reply. The full step table is in `bots/<bot>/references/step-table.md`.
- Step skills: one per job the bot does.
- `<bot>-knowledge`: rubrics and definitions. `<bot>-checks`: every check, with the script that runs it. `<bot>-references`: an index of the files in `references/`.

## Shared skills

| Skill | Used by |
|---|---|
| [`launch-kit-handoffs`](shared/launch-kit-handoffs/SKILL.md) | all six bots |
| [`reference-teardown`](shared/reference-teardown/SKILL.md) | Launch Ads, X Launch Desk, Ad Test Desk |
| [`quote-lineup-scout`](shared/quote-lineup-scout/SKILL.md) | X Launch Desk |
| [`hook-library-keeper`](shared/hook-library-keeper/SKILL.md) | Launch Ads, X Launch Desk, Launch Copy |
| [`x-source-scan`](shared/x-source-scan/SKILL.md) | X Launch Desk, Launch Copy |
| [`outlier-idea-archive`](shared/outlier-idea-archive/SKILL.md) | X Launch Desk, Launch Copy |
| [`meeting-transcripts-to-copy-desk`](shared/meeting-transcripts-to-copy-desk/SKILL.md) | Customer Voice, Launch Copy |
| [`paid-creative-loop`](shared/paid-creative-loop/SKILL.md) | Ad Test Desk (all sections), Launch Ads (sections 3 to 5) |
| [`edit-a-draft`](shared/edit-a-draft/SKILL.md) | Launch Copy |
| [`draft-for-a-channel`](shared/draft-for-a-channel/SKILL.md) | Launch Copy (post, blog, landing page, DM, release notes), Waitlist Email (email shape only) |
| [`build-the-voice-profile`](shared/build-the-voice-profile/SKILL.md) | Launch Copy, Waitlist Email |
| [`humanizer`](shared/humanizer/SKILL.md) | Waitlist Email (quick mode only), Launch Copy (quick mode on every draft, full mode on request) |

## Check scripts

Every check a skill names ("the style check", "the gates check", "the redaction check") has a script in that bot's `scripts/` folder; `<bot>-checks` names it under each heading. In the repo the scripts are the default and the written checklists are the fallback when the agent cannot run code.

```bash
cd bots/yc-launch-ads
python3 scripts/check_hooks.py --selftest                      # every script has a self-test
python3 scripts/check_brand_pack.py references/examples/brand-pack.example.md
python3 scripts/check_style.py .                                 # whole bot folder
```

Each script prints PASS or FAIL with the failing line, and exits 0 on pass, 1 on fail, 2 on a usage error. Python 3 standard library only. The invented examples in `references/` (Launch Ads and Ad Test Desk examples, the Waitlist Email sample campaign, the Customer Voice sample research) all pass their scripts, so you can do a practice run before using your own material.

The leak check ships with generic patterns only (paths, handles, emails, money). Add your own private words (company, product, people, customers) in a `--terms` file before sharing anything outside your chat.

## Notes for coding agents

- The ISOLATION rule was written for a shared Grok Bot computer: it tells the bot to work only from its own skills and what you paste, and never to go looking through your files for brand or claim documents. In a code agent, loading the kit's own files (skills, references, scripts) is fine; keep the spirit (paste your facts, don't let it guess them).
- "Save each answer as a memory" means: keep the setup answers somewhere the agent will see next session (for example a notes file you control).
- Placeholders in braces such as `{PRODUCT}`, `{AUDIENCE}` or `{BANNED_WORDS_FILE}` are yours to fill on the first run. The bots never guess them.
- `yc-x-launch-desk-test-of-300` is kept byte for byte on purpose, including its em dashes and its shorter credit line. Don't restyle it. Every kit-wide script (style, leak, credit, sections) skips it automatically and reports it as exempt.

## House rules every bot follows

- Drafts and plans only. Never posts, sends, schedules, publishes, spends or changes an account setting.
- Never invents metrics, quotes, testimonials, caps, deadlines or proof. Cites a source or writes [NEED].
- Never asks for or stores passwords, API keys, tokens or card numbers.
- Asks for missing context one question at a time.
- Examples are invented and labelled as examples. Outside benchmarks are never presented as your numbers.

## Credit and license

Created and curated by Dylan Pak. Independent project, not an official accelerator product.

Any copy, fork or republication of this repo or any file in it (including on GitHub) must keep the credit line "Created and curated by Dylan Pak." See [LICENSE](LICENSE).

---
Created and curated by Dylan Pak.
License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
