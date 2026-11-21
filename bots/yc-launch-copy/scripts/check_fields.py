#!/usr/bin/env python3
# <!-- dylan-pak-credit: Created and curated by Dylan Pak. Any copy, fork, or republication of this file (including on GitHub) must keep this credit: "Created and curated by Dylan Pak." -->
"""Completeness check for this pack's fill-in templates.

Usage:
  python3 check_fields.py <kind> <filled file>
  python3 check_fields.py --list
  python3 check_fields.py --selftest

Reads "Field: value" lines (also "- Field: value" and "**Field:** value").
Fails when a required field is missing, empty, or still says [NEED], TBD, TODO or "?".
Some kinds add mechanical rules:
  numeric  the value must hold a number or a {PLACEHOLDER} the owner filled in chat.
  single   the value names one thing (no " and ", "+", "/" or ";").
  min      the value is a score that must reach the minimum.
  choice   the value must be one of the listed words (first word counts).
  override a kind may name one field; when the owner writes "yes" there, the minimum scores are waived
           and the waiver is printed so it stays visible.
Exit: 0 pass, 1 fail, 2 usage error.
"""
import re
import sys
import tempfile
from pathlib import Path

KINDS = {
    "pinpoint": {"required": ["Pinpoint", "Reader", "Problem", "Benefit", "Emotion", "Action", "Stranger test",
                              "Two-year test", "Proof 1", "Proof 2"],
                 "choice": {"Stranger test": ["YES"], "Two-year test": ["YES"]}},
    "outline": {"required": ["Pinpoint", "Promise", "Opening", "Beat 1", "Beat 2", "Beat 3", "Turn", "Action",
                             "Teach before pitch"],
                "choice": {"Teach before pitch": ["YES", "N/A"]}},
    "draft-score": {"required": ["Channel", "Pinpoint", "Clarity", "Specificity", "Voice", "Honesty", "Payoff"],
                    "min": {"Clarity": 4, "Specificity": 4, "Voice": 4, "Honesty": 5, "Payoff": 4}},
    "room-log": {"required": ["Room", "Prompt", "Reply", "Owner approved sharing", "Fact flags"],
                 "choice": {"Owner approved sharing": ["YES"]}},
}

OPEN = re.compile(r"^\s*$|\[NEED|\bTBD\b|\bTODO\b|^\?$", re.I)


def parse(text):
    fields = {}
    for line in text.splitlines():
        m = re.match(r"^\s*[-*]?\s*\**([A-Za-z][A-Za-z0-9 /()'+-]{1,60}?)\**\s*:\**\s*(.*)$", line)
        if m:
            fields.setdefault(m.group(1).strip().lower(), m.group(2).strip())
    return fields


def check(kind, text):
    spec = KINDS[kind]
    f = parse(text)
    fails = []
    ov = spec.get("override")
    overridden = bool(ov) and f.get(ov.lower(), "").lower().startswith("yes")
    for name in spec["required"]:
        val = f.get(name.lower())
        if val is None:
            fails.append(f"missing field: {name}")
            continue
        if OPEN.search(val):
            fails.append(f"open field: {name} = '{val}'")
            continue
        if name in spec.get("numeric", []) and not re.search(r"\d|\{[A-Z0-9_]+\}", val):
            fails.append(f"{name} needs a number or a filled placeholder")
        if name in spec.get("single", []) and re.search(r"\band\b|\+|/|;", val, re.I):
            fails.append(f"{name} must name one thing only")
        if name in spec.get("min", {}) and not overridden:
            m = re.search(r"\d+(?:\.\d+)?", val)
            if not m or float(m.group(0)) < spec["min"][name]:
                fails.append(f"{name} must be {spec['min'][name]} or more")
        if name in spec.get("choice", {}):
            if val.split()[0].strip(".,").upper() not in [c.upper() for c in spec["choice"][name]]:
                fails.append(f"{name} must be one of: " + ", ".join(spec["choice"][name]))
    return fails


def run(kind, path):
    fails = check(kind, Path(path).read_text(encoding="utf-8"))
    for x in fails:
        print("FAIL  " + x)
    spec = KINDS[kind]
    if spec.get("override") and parse(Path(path).read_text(encoding="utf-8")).get(spec["override"].lower(), "").lower().startswith("yes"):
        print(f"NOTE  owner waived the minimum scores in '{spec['override']}'")
    print(f"PASS  {kind} complete" if not fails else f"\n{kind}: {len(fails)} problems")
    return 1 if fails else 0


def selftest():
    for kind, spec in KINDS.items():
        lines = []
        for name in spec["required"]:
            if name in spec.get("choice", {}):
                v = spec["choice"][name][0]
            elif name in spec.get("min", {}):
                v = str(spec["min"][name])
            else:
                v = "example value 3"
            lines.append(f"{name}: {v}")
        good = "\n".join(lines)
        assert check(kind, good) == [], (kind, check(kind, good))
        assert check(kind, good.replace(lines[0], spec["required"][0] + ": [NEED]")), kind
        assert check(kind, "\n".join(lines[1:])), kind
    with tempfile.TemporaryDirectory() as d:
        k = next(iter(KINDS))
        p = Path(d, "t.md")
        p.write_text("nothing\n")
        assert run(k, p) == 1
    print("SELFTEST PASS")
    return 0


def main(argv):
    if argv[1:2] == ["--selftest"]:
        return selftest()
    if argv[1:2] == ["--list"]:
        for k, s in KINDS.items():
            print(f"{k}: " + ", ".join(s["required"]))
        return 0
    if len(argv) != 3 or argv[1] not in KINDS or not Path(argv[2]).is_file():
        print(__doc__)
        print("kinds: " + ", ".join(KINDS))
        return 2
    return run(argv[1], argv[2])


if __name__ == "__main__":
    sys.exit(main(sys.argv))

# Created and curated by Dylan Pak.
# License note: free to use and adapt. If you copy, fork, or republish this file anywhere (including GitHub), keep the credit "Created and curated by Dylan Pak."
