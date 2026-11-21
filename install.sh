#!/usr/bin/env bash
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
#
# YC S26 Launch Kit installer: copies bots into a coding agent's skills folder as flat SKILL.md folders.
#
# Usage:
#   ./install.sh [--target claude|cursor|codex|DIR] [--bot <slug>|--all] [--project] [--dry-run] [--agents-md] [--list]
#
#   --target   claude  -> ~/.claude/skills   (with --project: ./.claude/skills)
#              cursor  -> ~/.cursor/skills   (with --project: ./.cursor/skills)
#              codex   -> ~/.agents/skills   (with --project: ./.agents/skills)
#              DIR     -> any folder you name
#              Default: claude.
#   --bot      one bot, for example --bot yc-launch-copy (repeatable). --all installs all six (the default).
#   --project  install into the current folder's project skills folder instead of your home folder.
#   --dry-run  print what would happen and change nothing.
#   --agents-md  also add (or refresh) a short marked block in ./AGENTS.md that points the agent at the kit.
#   --list     list the bots and exit.
#
# What it installs, per bot:
#   <slug>-operating-rules/   the bot's system prompt as a skill, plus the bot's references/ and scripts/
#   <slug>-<skill>/           one folder per skill
#   <shared-skill>/           the shared kit skills that bot uses (installed once even with --all)
#   yc-s26-launch-kit-router/ a small skill that routes a request to the right bot
# Paths: every installed skill gets one line saying its bot folder is ../<slug>-operating-rules/, so
# references/... and scripts/... resolve from there. The byte-locked yc-x-launch-desk-test-of-300 skill is copied unchanged.
# Safe to re-run: each folder it owns is replaced, nothing else in the target is touched.
# Needs only bash and the usual file tools. The check scripts need python3 (standard library only).
set -euo pipefail

KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="claude"; PROJECT=0; DRY=0; AGENTS_MD=0; BOTS=(); ALL=0

die() { echo "install.sh: $*" >&2; exit 2; }
all_bots() { for d in "$KIT"/bots/*/; do basename "$d"; done; }

while [ $# -gt 0 ]; do
  case "$1" in
    --target) [ $# -ge 2 ] || die "--target needs a value"; TARGET="$2"; shift 2 ;;
    --target=*) TARGET="${1#*=}"; shift ;;
    --bot) [ $# -ge 2 ] || die "--bot needs a slug"; BOTS+=("$2"); shift 2 ;;
    --bot=*) BOTS+=("${1#*=}"); shift ;;
    --all) ALL=1; shift ;;
    --project) PROJECT=1; shift ;;
    --dry-run) DRY=1; shift ;;
    --agents-md) AGENTS_MD=1; shift ;;
    --list) all_bots; exit 0 ;;
    -h|--help) sed -n '3,30p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) die "unknown option: $1 (see --help)" ;;
  esac
done

if [ "$ALL" = 1 ] || [ ${#BOTS[@]} -eq 0 ]; then BOTS=(); while read -r b; do BOTS+=("$b"); done < <(all_bots); fi
for b in "${BOTS[@]}"; do [ -d "$KIT/bots/$b" ] || die "no such bot: $b (try --list)"; done

if [ "$PROJECT" = 1 ]; then BASE="$(pwd)"; else BASE="${HOME:?HOME is not set}"; fi
case "$TARGET" in
  claude) DEST="$BASE/.claude/skills" ;;
  cursor) DEST="$BASE/.cursor/skills" ;;
  codex)  DEST="$BASE/.agents/skills" ;;
  *)      [ "$PROJECT" = 1 ] && die "--project only works with claude, cursor or codex"; DEST="$TARGET" ;;
esac

run() { if [ "$DRY" = 1 ]; then echo "  [dry-run] $*"; else "$@"; fi; }
COUNT=0

# copy a folder into DEST/<name>, replacing any earlier copy
put_dir() { # src name
  local src="$1" name="$2"
  echo "install $name"
  run rm -rf "$DEST/$name"
  run cp -R "$src" "$DEST/$name"
  COUNT=$((COUNT+1))
}

# add the "installed edition" line after the credit header and rewrite repo paths (never on the locked skill)
fix_skill() { # file slug
  local f="$1" slug="$2"
  [ "$DRY" = 1 ] && return 0
  case "$f" in *test-of-300*) return 0 ;; esac
  local note=""
  if [ -n "$slug" ]; then
    note="Installed edition: this bot's folder is ../$slug-operating-rules/ (next to this skill). Paths starting with references/ or scripts/ are inside it; run scripts from there, for example: cd ../$slug-operating-rules && python3 scripts/<check>.py --selftest"
  fi
  awk -v note="$note" '
    { line=$0
      while (match(line, /bots\/yc-[a-z-]+\//)) { s=substr(line, RSTART+5, RLENGTH-6); line=substr(line,1,RSTART-1) "../" s "-operating-rules/" substr(line, RSTART+RLENGTH) }
      gsub(/from `shared\/`/, "from the skills folder (they are installed next to this skill)", line)
      gsub(/\(\.\.\/\.\.\/shared\//, "(../", line)
      print line
      if (!done && note != "" && line ~ /^<!-- dylan-pak-credit/) { print ""; print note; done=1 }
    }' "$f" > "$f.tmp" && mv "$f.tmp" "$f"
}

shared_for() { # slug -> shared skill names from its card
  grep -o 'shared/[a-z0-9-]*/SKILL.md' "$KIT/bots/$1/card.md" | cut -d/ -f2 | sort -u
}

echo "YC S26 Launch Kit -> $DEST"
[ "$DRY" = 1 ] && echo "(dry run: nothing will be changed)"
run mkdir -p "$DEST"

SHARED_DONE=" "
for slug in "${BOTS[@]}"; do
  b="$KIT/bots/$slug"
  # 1. operating rules as a skill, with the bot's references and scripts beside it
  name="$slug-operating-rules"
  echo "install $name"
  run rm -rf "$DEST/$name"
  run mkdir -p "$DEST/$name"
  if [ "$DRY" = 0 ]; then
    title="$(grep -m1 '^# ' "$b/card.md" | sed 's/^# //')"
    {
      printf -- '---\nname: %s\ndescription: "%s: load this first, before any %s request. The bot'"'"'s system prompt (persona, one job, router, house rules) and its folder of references and check scripts. Then load %s-workflow."\n---\n\n' "$name" "$title" "$title" "$slug"
      awk 'NR==1 && /^<!-- dylan-pak-credit/ {print; print ""; print "Installed edition: this folder is the bot'"'"'s folder. references/ and scripts/ live here; run the check scripts from this folder (python3, standard library only)."; next} {print}' "$b/persona/operating-rules.md"
    } > "$DEST/$name/SKILL.md"
    cp -R "$b/references" "$DEST/$name/references"
    cp -R "$b/scripts" "$DEST/$name/scripts"
    cp "$b/card.md" "$DEST/$name/card.md"
    find "$DEST/$name" -name '__pycache__' -prune -exec rm -rf {} +
    while IFS= read -r -d '' f; do fix_skill "$f" ""; done < <(find "$DEST/$name" -name '*.md' -print0)
  fi
  COUNT=$((COUNT+1))
  # 2. the bot's skills
  for s in "$b"/skills/*/; do
    s="${s%/}"; sn="$(basename "$s")"
    put_dir "$s" "$sn"
    fix_skill "$DEST/$sn/SKILL.md" "$slug"
  done
  # 3. shared skills it uses
  for sh in $(shared_for "$slug"); do
    case "$SHARED_DONE" in *" $sh "*) continue ;; esac
    put_dir "$KIT/shared/$sh" "$sh"
    fix_skill "$DEST/$sh/SKILL.md" ""
    SHARED_DONE="$SHARED_DONE$sh "
  done
done

# 4. router skill built from AGENTS.md
echo "install yc-s26-launch-kit-router"
run rm -rf "$DEST/yc-s26-launch-kit-router"
run mkdir -p "$DEST/yc-s26-launch-kit-router"
if [ "$DRY" = 0 ]; then
  {
    printf -- '---\nname: yc-s26-launch-kit-router\ndescription: "YC S26 Launch Kit: use when a request is about a startup launch (customer research, launch copy, the X launch, waitlist email, paid-social ads, ad tests) and you need to pick which kit bot handles it. Routes to the right <bot>-operating-rules and <bot>-workflow skill."\n---\n\n'
    awk '{a[NR]=$0} END{for(i=1;i<=NR-3;i++) print a[i]}' "$KIT/AGENTS.md"
    missing=""
    for s in $(all_bots); do [ -d "$DEST/$s-operating-rules" ] || missing="$missing $s"; done
    if [ -n "$missing" ]; then
      printf 'Installed edition: not installed here:%s. If a request belongs to one of them, say so and point the owner to ./install.sh --bot <slug>.\n\n' "$missing"
    fi
    tail -n 3 "$KIT/AGENTS.md"
  } > "$DEST/yc-s26-launch-kit-router/SKILL.md"
  fix_skill "$DEST/yc-s26-launch-kit-router/SKILL.md" ""
fi
COUNT=$((COUNT+1))

if [ "$AGENTS_MD" = 1 ]; then
  BLOCK_START="<!-- yc-s26-launch-kit:start -->"; BLOCK_END="<!-- yc-s26-launch-kit:end -->"
  echo "update ./AGENTS.md (marked block)"
  if [ "$DRY" = 0 ]; then
    touch AGENTS.md
    awk -v s="$BLOCK_START" -v e="$BLOCK_END" '$0==s{skip=1} !skip{print} $0==e{skip=0}' AGENTS.md > AGENTS.md.tmp
    {
      cat AGENTS.md.tmp
      echo "$BLOCK_START"
      echo "## YC S26 Launch Kit (Created and curated by Dylan Pak)"
      echo "Skills are installed in $DEST. For any launch request, load yc-s26-launch-kit-router, then the chosen bot's <slug>-operating-rules and <slug>-workflow skills. Drafts only: never post, send, publish or spend."
      echo "$BLOCK_END"
    } > AGENTS.md
    rm -f AGENTS.md.tmp
  fi
fi

echo "done: $COUNT folders for ${#BOTS[@]} bot(s) in $DEST"
echo "next: tell your agent to load <bot>-operating-rules first (or the router skill), then say \"start\"."

# ---
# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
