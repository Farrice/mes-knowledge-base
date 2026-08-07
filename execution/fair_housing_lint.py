#!/usr/bin/env python3
"""
Fair Housing Lint — the deterministic backstop that keeps steering language out
of real-estate marketing copy (reel scripts, captions, listing packages).

WHY THIS EXISTS
---------------
Fair Housing Act steering language is a compliance risk that no self-score or
finalize pass mechanically checks for. The client policy is explicit —
`_active/clients/jen-listings/CLAUDE.md` (Override List): "Still never: ... fair-housing
steering language (safe/family/great-for-kids, schools on camera)." Schools are
allowed as DATA in captions; spoken on camera they read as targeting.

Per the standing rule — "never ship infra that depends on the model REMEMBERING;
pair it with a deterministic backstop" — this module is that backstop. It is a
pure regex scanner (no AI judgment) that catches protected-class steering moves
and returns a non-zero exit on FAIL so a gate halts. HARD-FAIL rules cover
familial-status steering, safety code words, explicit protected-class targeting,
exclusive+people pairings, and religion landmarks sold as buyer fit. WARN rules
cover context leaks (schools on camera, persona labels in captions) and
unverifiable environment absolutes.

MODES
-----
  check     Scan a file/text; emit findings + verdict (PASS/FAIL); exit 2 on FAIL.
              python3 execution/fair_housing_lint.py check --file reel.md --context script
              python3 execution/fair_housing_lint.py check --text "..." [--strict]
  rules     Print the rule table.
  selftest  Run the built-in known-bad/known-good corpus; exit 0/1.
LOG: .agent/fair-housing-lint.jsonl
"""

import sys
import re
import json
import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any, Optional

ROOT = Path(__file__).resolve().parent.parent
LOG_PATH = ROOT / ".agent" / "fair-housing-lint.jsonl"

RELIGION_PLACES = r"(?:church(?:es)?|temple|mosque|synagogue|parish|chapel)"

# Each rule: name, pattern, severity ("fail"/"warn"), why, fix_hint,
# optional contexts (rule fires only in these contexts),
# optional sections (rule fires only inside these labeled sections).
# Adding a rule = appending one dict here.
RULES: List[Dict[str, Any]] = [
    {"rule": "familial-status-steering",
     "pattern": r"\b(?:safe|perfect|great|ideal|wonderful)\s+"
                r"(?:(?:neighborhood|area|community|street|home|place)\s+)?"
                r"(?:for|to\s+raise)\s+(?:families|a\s+family|kids|children)\b"
                r"|\bfamily[- ]friendly\b|\bfamily\s+neighborhood\b"
                r"|\bkid[- ]friendly(?:\s+(?:neighborhood|area|community))?\b",
     "severity": "fail",
     "why": "Familial-status steering under the Fair Housing Act — describes who the home is FOR, not what it IS.",
     "fix_hint": "Describe the property fact instead: bedroom count, yard size, layout. Let the buyer self-select."},
    {"rule": "safety-code-words",
     "pattern": r"\bsafe\s+(?:neighborhood|area|street)\b|\blow[- ]crime\b|\bcrime[- ]free\b",
     "severity": "fail",
     "why": "'Safe'/'low crime' is documented code language for racial steering — HARD ban regardless of intent.",
     "fix_hint": "Cut it. Point to verifiable location facts (cul-de-sac, gated entry as a feature, HOA) if relevant."},
    {"rule": "protected-class-targeting",
     "pattern": r"\b(?:christian|jewish|muslim|catholic|hindu|buddhist|white|black|asian|hispanic|latino)\s+"
                r"(?:famil(?:y|ies)|buyers?|couples?|neighborhood|community)\b"
                r"|\bno\s+wheelchairs?\b|\bable[- ]bodied\b"
                r"|\b(?:perfect|great|ideal|wonderful)\s+for\s+(?:young|older|mature|single|married|retired)\s+"
                r"(?:couples?|professionals?|famil(?:y|ies)|buyers?)\b"
                r"|\bempty\s+nesters?\s+only\b|\badults?[- ]only\b|\badult\s+community\b"
                r"|\bno\s+section\s*8\b|\benglish[- ]speaking\b",
     "severity": "fail",
     "why": "Explicit protected-class buyer descriptor (race/religion/national origin/disability/familial status/age).",
     "fix_hint": "Remove the buyer descriptor entirely. ('Adult community' is legal only with a verified HOPA exemption — flag to Farrice, never assume.)"},
    {"rule": "exclusive-plus-people",
     "pattern": r"\bexclusive\s+(?:neighborhood|community|enclave)\b"
                r"|\bexclusive\b[^.!?\n]{0,40}\b(?:famil(?:y|ies)|buyers?|residents?|clientele)\b",
     "severity": "fail",
     "why": "'Exclusive' + people-words signals who is excluded. (Bare 'exclusive listing' is a fine industry term — not flagged.)",
     "fix_hint": "Say what's scarce about the PROPERTY (one of three units, off-market), never about the people."},
    {"rule": "religion-landmark-selling",
     "pattern": rf"\b{RELIGION_PLACES}\b[^.!?\n]{{0,80}}\b(?:perfect|ideal|great|wonderful)\s+for\b"
                rf"|\b(?:perfect|ideal|great|wonderful)\s+for\b[^.!?\n]{{0,80}}\b{RELIGION_PLACES}\b",
     "severity": "fail",
     "why": "Religious landmark tied to buyer fit = religion-based steering. Bare distance facts are fine.",
     "fix_hint": "State the distance fact alone, or cut the landmark; never attach it to who should buy."},
    {"rule": "schools-on-camera",
     "pattern": r"\bschools?\b",
     "severity": "warn",
     "contexts": {"script"},
     "why": "Schools belong in caption data, not spoken targeting (policy: _active/clients/jen-listings/CLAUDE.md — schools off camera).",
     "fix_hint": "Move school names/ratings to the caption as a labeled data point; cut from the spoken script."},
    {"rule": "persona-label-leak",
     "pattern": r"^\s*for:\s*\S",
     "severity": "warn",
     "sections": {"CAPTION", "SAY"},
     "why": "'For: the ...' buyer-persona labels are internal targeting notes — never publishable copy.",
     "fix_hint": "Strip the label before the caption ships; keep persona targeting in the internal brief only."},
    {"rule": "worship-walking-distance",
     "pattern": rf"\bwalking\s+distance\s+(?:to|from)\s+(?:the\s+)?{RELIGION_PLACES}\b",
     "severity": "warn",
     "why": "Proximity to a place of worship as a selling point drifts toward religious steering.",
     "fix_hint": "Prefer neutral anchors (park, main street, transit) unless the landmark is a pure location fact."},
    {"rule": "absolute-environment-claims",
     "pattern": r"\bzero\s+street\s+noise\b|\bno\s+crime\b|\bquiet\s+(?:neighborhood|area)\b",
     "severity": "warn",
     "why": "Unverifiable environment absolute stated as fact ('quiet cul-de-sac' is a location fact — not flagged).",
     "fix_hint": "Anchor to a verifiable feature (end of a cul-de-sac, double-pane windows) or soften to observation."},
]
for _r in RULES:
    _r["rx"] = re.compile(_r["pattern"], re.I)

SECTION_RX = re.compile(r"^\s*(HOOK|SAY|CAPTION|SHOT|B-?ROLL|CTA|SCENE|VO|ON[- ]SCREEN)\b[:\s]", re.I)
SCRIPT_MARKER_RX = re.compile(r"\bHOOK\b|SAY:", re.I)


def detect_context(text: str, explicit: str = "") -> str:
    """Explicit --context wins; else sniff script markers; else 'package'."""
    if explicit:
        return explicit
    return "script" if SCRIPT_MARKER_RX.search(text) else "package"


def evaluate(text: str, context: str = "") -> Dict[str, Any]:
    """Deterministic fair-housing scan. Returns {verdict, context, findings}."""
    ctx = detect_context(text, context)
    findings: List[Dict[str, Any]] = []
    section = ""
    for line_no, line in enumerate(text.splitlines(), start=1):
        m = SECTION_RX.match(line)
        if m:
            section = m.group(1).upper().replace("-", "").replace(" ", "")
            section = {"BROLL": "B-ROLL", "ONSCREEN": "ON-SCREEN"}.get(section, section)
        for rule in RULES:
            if rule.get("contexts") and ctx not in rule["contexts"]:
                continue
            if rule.get("sections") and section not in rule["sections"]:
                continue
            hit = rule["rx"].search(line)
            if hit:
                findings.append({
                    "rule": rule["rule"], "severity": rule["severity"],
                    "match": hit.group(0), "line_no": line_no,
                    "why": rule["why"], "fix_hint": rule["fix_hint"],
                })
    fails = [f for f in findings if f["severity"] == "fail"]
    return {"verdict": "FAIL" if fails else "PASS", "context": ctx, "findings": findings}


def log(result: Dict[str, Any], file_label: str = "") -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a") as fh:
        fh.write(json.dumps({
            "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "file": file_label, "verdict": result["verdict"],
            "findings": result["findings"],
        }) + "\n")


def run_check(text: str, context: str = "", strict: bool = False,
              file_label: str = "", quiet: bool = False, do_log: bool = True) -> int:
    r = evaluate(text, context)
    if strict and r["verdict"] == "PASS" and r["findings"]:
        r["verdict"] = "FAIL"
    if do_log:
        log(r, file_label)
    if not quiet:
        icon = {"PASS": "✅", "FAIL": "⛔"}[r["verdict"]]
        print(f"{icon} FAIR HOUSING LINT — {r['verdict']} · context={r['context']}"
              + (f" · {file_label}" if file_label else ""))
        for f in r["findings"]:
            mark = "⛔" if f["severity"] == "fail" else "⚠️ "
            print(f"   {mark} L{f['line_no']} [{f['rule']}] \"{f['match']}\"")
            print(f"        why: {f['why']}")
            print(f"        fix: {f['fix_hint']}")
        if not r["findings"]:
            print("   no steering language · no protected-class targeting · no context leaks")
    return 2 if r["verdict"] == "FAIL" else 0


def print_rules() -> int:
    for r in RULES:
        gates = []
        if r.get("contexts"):
            gates.append("context=" + "|".join(sorted(r["contexts"])))
        if r.get("sections"):
            gates.append("section=" + "|".join(sorted(r["sections"])))
        gate = f" ({', '.join(gates)})" if gates else ""
        print(f"[{r['severity'].upper():4}] {r['rule']}{gate}")
        print(f"       why: {r['why']}")
        print(f"       fix: {r['fix_hint']}")
    return 0


def selftest() -> int:
    ok = True

    def check(label: str, cond: bool) -> None:
        nonlocal ok
        print(f"{'PASS' if cond else 'FAIL'}  {label}")
        if not cond:
            ok = False

    # Known-bad: must FAIL (exit 2).
    for bad in [
        "this safe neighborhood is perfect for families",
        "great for kids and just minutes from the best schools",
        "ideal for young couples starting out",
        "low crime area",
    ]:
        code = run_check(bad, quiet=True, do_log=False)
        check(f"known-bad fails (exit 2): {bad!r}", code == 2)

    # Schools: WARN in script context, silent in caption context; both exit 0.
    school = "a nine-out-of-ten high school… four tenths of a mile away"
    r_script = evaluate(school, "script")
    r_caption = evaluate(school, "caption")
    check("schools in script context yields WARN finding",
          any(f["rule"] == "schools-on-camera" and f["severity"] == "warn"
              for f in r_script["findings"]))
    check("schools in script context still exits 0 (warn only)",
          run_check(school, "script", quiet=True, do_log=False) == 0)
    check("schools in caption context yields no findings",
          r_caption["findings"] == [] and r_caption["verdict"] == "PASS")

    # Known-good: must PASS clean (no findings, exit 0).
    for good in [
        "the second one's in a guest house… a parent moving closer, an adult kid coming home",
        "exclusive listing — call for details",
        "end of a quiet cul-de-sac",
    ]:
        r = evaluate(good, "caption")
        code = run_check(good, "caption", quiet=True, do_log=False)
        check(f"known-good passes clean (0 findings, exit 0): {good!r}",
              r["findings"] == [] and code == 0)

    # --strict promotes warns to FAIL.
    check("--strict promotes script-context schools warn to exit 2",
          run_check(school, "script", strict=True, quiet=True, do_log=False) == 2)

    # Context auto-detect: SAY: marker → script.
    check("context sniff: 'SAY:' marker detects script",
          detect_context("SAY: welcome to this listing") == "script")

    print("SELFTEST " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main() -> int:
    p = argparse.ArgumentParser(prog="fair_housing_lint.py")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("--file", default="")
    c.add_argument("--text", default="")
    c.add_argument("--context", default="", choices=["", "script", "caption", "package"])
    c.add_argument("--strict", action="store_true")
    c.add_argument("--quiet", action="store_true")
    sub.add_parser("rules")
    sub.add_parser("selftest")
    args = p.parse_args()
    if args.cmd == "rules":
        return print_rules()
    if args.cmd == "selftest":
        return selftest()
    text = Path(args.file).read_text() if args.file and Path(args.file).exists() else (args.text or "")
    if not text.strip():
        print("fair_housing_lint: no input.", file=sys.stderr)
        return 2
    return run_check(text, args.context, args.strict, args.file, args.quiet)


if __name__ == "__main__":
    sys.exit(main())
