#!/usr/bin/env python3
"""
Context Ethics Gate — deterministic backstop for the Context Engineering
Operating System (skills/chase-hughes-context-engineering).

WHY THIS EXISTS
---------------
The Defense/Ethics Gate inside /ce-design and /ce-build is a *persona-run*
judgment: the model names the technique it is deploying, runs the defensive
mirror, the surface test ("would I defend this if the target saw the full
design?"), the outcome-on-merits check, and the destabilization check
(reducing chaos = help; manufacturing chaos to sell the cure = the line).

Per the system's banned-pattern rule — "AI-Memory-Dependent Observability is
BANNED: never ship infra requiring Claude manual invocation; always pair with
a deterministic backstop" — that judgment MUST be paired with a deterministic
mechanism that (a) runs structural checks regardless of model memory and
(b) logs every verdict so the gate cannot silently no-op.

This module is that backstop. It does NOT replace the persona judgment — the
persona catches nuance this never could. This floors it: it catches the
structural red flags (manufactured urgency/scarcity that is then "cured,"
a context design shipped with NO defensive read, coercive power-asymmetry
markers around the honesty protocol) and guarantees a log entry for every
context-engineering deliverable.

The dual-use ethic Chase Hughes states it for, verbatim: every technique is
taught with its defense; intent is the only difference between control and
help. This gate is that ethic made deterministic.

MODES
-----
  check   Run structural heuristics on a context-design spec / copy and emit
          a verdict (PASS / REVIEW / BLOCK) + log it.
            python3 execution/context_ethics_gate.py check --file spec.md
            python3 execution/context_ethics_gate.py check --text "..." --kind honesty
  log     Record an explicit persona verdict (technique named + verdict).
            python3 execution/context_ethics_gate.py log --verdict PASS \
                --technique "PCP recipient-build" --workflow ce-design --note "..."
  report  Summarize recent verdicts.
            python3 execution/context_ethics_gate.py report --days 7

LOG: .agent/context-ethics-log.jsonl
"""

import sys
import json
import re
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional

ROOT = Path(__file__).resolve().parent.parent
LOG_PATH = ROOT / ".agent" / "context-ethics-log.jsonl"

# Workflows that produce context-engineering output and MUST pass the gate.
# Mirror of the SKILL.md workflow table; update both together.
CONTEXT_ENGINEERING_WORKFLOWS = {
    "ce-design", "ce-build", "ce-pcp", "ce-followability",
    "ce-honesty", "ce-read", "ce-source-code", "ce-defend",
}

# ── Structural red-flag patterns (deterministic) ──────────────────────────
# These are heuristics, not a conscience. They flag the SHAPE of an
# exploitative design so a human (or the persona's deeper judgment) looks again.

# Manufactured destabilization: fabricated urgency/scarcity/fear that the
# design then positions itself as the relief for. This is the FEAR/fractionation
# mechanic turned predatory — the exact line Hughes names.
_MANUFACTURED_DESTABILIZATION = [
    r"\bonly\s+\d+\s+(left|spots|seats|remaining)\b",
    r"\bact now\b", r"\bbefore (it'?s )?too late\b",
    r"\bdoors clos(e|ing)\b", r"\blast chance\b",
    r"\bthey don'?t want you to know\b",
    r"\bwhat (they|the \w+) (are )?hiding from you\b",
    r"\byou'?re (already )?(falling behind|being left behind)\b",
    r"\bif you don'?t .{0,40}\b(you'?ll|you will) (lose|miss|fail|regret)\b",
    r"\bfear of missing out\b", r"\bscarcity\b.{0,30}\b(manufactur|fake|artificial)",
]

# Coercive power-asymmetry markers around the honesty/interrogation protocol —
# running SMRP on someone who cannot freely exit is coercive regardless of intent.
_POWER_ASYMMETRY = [
    r"\b(my|their|the) (employee|subordinate|direct report|intern|assistant)\b",
    r"\b(my|their) (kid|child|son|daughter)\b",
    r"\b(can'?t|cannot|unable to) (leave|exit|walk away|say no|refuse)\b",
    r"\b(has to|must|forced to|required to) (stay|answer|comply)\b",
    r"\bmid-?(fight|conflict|argument)\b",
    r"\b(power|status) (imbalance|asymmetry|differential)\b",
]

# Signals that a defensive read / ethics verdict IS present (the dual-use pairing).
_DEFENSE_PRESENT = [
    r"\bdefens(e|ive) (read|mirror|verdict|note)\b",
    r"\bif this were run on me\b", r"\bsurface test\b",
    r"\bwould i defend this\b", r"\bdestabilization check\b",
    r"\boutcome[- ]on[- ]merits\b", r"\bethics (gate|verdict|check)\b",
    r"\bresistance move\b", r"\bhow to detect\b",
]

# Honesty/interrogation-protocol signals (so power-asymmetry only flags in context).
_INTERROGATION_CONTEXT = [
    r"\bsmrp\b", r"\bsocialize.{0,20}minimize", r"\binterrogat",
    r"\bconfession\b", r"\bhonesty protocol\b", r"\balternative question\b",
    r"\bbait question\b", r"\bget (them|him|her) to (admit|confess|tell)\b",
]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _matches(patterns: List[str], text: str) -> List[str]:
    hits = []
    for p in patterns:
        m = re.search(p, text, re.IGNORECASE)
        if m:
            hits.append(m.group(0).strip())
    return hits


def evaluate(text: str, kind: str = "spec") -> Dict[str, Any]:
    """Run deterministic structural checks. Returns verdict + flags.

    kind: 'spec' (a context-design spec), 'copy' (deliverable copy/content),
          or 'honesty' (an honesty-protocol / interrogation design).
    Verdict logic:
      BLOCK  — manufactured destabilization present AND no defensive read present.
      REVIEW — any single red flag present, or honesty design touching a
               power-asymmetry target, or a spec with no defensive read at all.
      PASS   — defensive read present and no red flags.
    """
    text = text or ""
    destab = _matches(_MANUFACTURED_DESTABILIZATION, text)
    defense = _matches(_DEFENSE_PRESENT, text)
    is_interrogation = kind == "honesty" or bool(_matches(_INTERROGATION_CONTEXT, text))
    power = _matches(_POWER_ASYMMETRY, text) if is_interrogation else []

    flags: List[str] = []
    if destab:
        flags.append(f"manufactured_destabilization: {destab[:3]}")
    if power:
        flags.append(f"coercive_power_asymmetry: {power[:3]}")
    if kind == "spec" and not defense:
        flags.append("no_defensive_read_present")

    if destab and not defense:
        verdict = "BLOCK"
        reason = ("Manufactured urgency/scarcity/fear present with NO defensive "
                  "read — this is the fractionation mechanic turned predatory "
                  "(manufacturing chaos to sell the cure). Rewrite or add a "
                  "genuine destabilization-check verdict.")
    elif flags:
        verdict = "REVIEW"
        reason = ("Structural red flag(s) detected; the persona Defense/Ethics "
                  "Gate must explicitly clear these before shipping.")
    else:
        verdict = "PASS"
        reason = ("No structural red flags; defensive read present. "
                  "Persona judgment still governs nuance.")

    return {
        "verdict": verdict,
        "reason": reason,
        "flags": flags,
        "kind": kind,
        "defense_markers_found": len(defense),
        "checked_chars": len(text),
    }


def log_verdict(
    verdict: str,
    *,
    technique: str = "",
    workflow: str = "",
    expert: str = "chase-hughes",
    kind: str = "spec",
    flags: Optional[List[str]] = None,
    note: str = "",
    source: str = "explicit",
) -> Dict[str, Any]:
    """Append a verdict to the JSONL log. Importable by chain_runner finalize."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "ts": _now(),
        "verdict": (verdict or "UNKNOWN").upper(),
        "technique": technique,
        "workflow": workflow,
        "expert": expert,
        "kind": kind,
        "flags": flags or [],
        "note": note,
        "source": source,
    }
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    return entry


def _read_log(days: Optional[int] = None) -> List[Dict[str, Any]]:
    if not LOG_PATH.exists():
        return []
    cutoff = None
    if days:
        cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    out = []
    for line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if cutoff:
            try:
                if datetime.fromisoformat(e["ts"]) < cutoff:
                    continue
            except (KeyError, ValueError):
                pass
        out.append(e)
    return out


def _cmd_check(args) -> int:
    text = args.text or ""
    if args.file:
        text = Path(args.file).read_text(encoding="utf-8")
    result = evaluate(text, kind=args.kind)
    log_verdict(
        result["verdict"],
        technique=args.technique or "",
        workflow=args.workflow or "",
        kind=args.kind,
        flags=result["flags"],
        note=(args.note or "") + " | " + result["reason"],
        source="structural_check",
    )
    print(json.dumps(result, indent=2))
    # Non-zero exit on BLOCK so a workflow `// turbo` gate can halt on it.
    return 2 if result["verdict"] == "BLOCK" else 0


def _cmd_log(args) -> int:
    entry = log_verdict(
        args.verdict,
        technique=args.technique or "",
        workflow=args.workflow or "",
        kind=args.kind,
        note=args.note or "",
        source="explicit",
    )
    print(json.dumps(entry, indent=2))
    return 0


def _cmd_report(args) -> int:
    entries = _read_log(days=args.days)
    counts: Dict[str, int] = {}
    for e in entries:
        counts[e.get("verdict", "UNKNOWN")] = counts.get(e.get("verdict", "UNKNOWN"), 0) + 1
    blocked = [e for e in entries if e.get("verdict") == "BLOCK"]
    review = [e for e in entries if e.get("verdict") == "REVIEW"]
    print(f"Context Ethics Gate — last {args.days or 'all'} days")
    print(f"  total verdicts : {len(entries)}")
    for v in ("PASS", "REVIEW", "BLOCK", "NOT_OBSERVED", "UNKNOWN"):
        if v in counts:
            print(f"  {v:<13}: {counts[v]}")
    if review:
        print(f"\n  {len(review)} REVIEW — flags to clear:")
        for e in review[-5:]:
            print(f"    [{e.get('workflow','?')}] {e.get('flags')}")
    if blocked:
        print(f"\n  ⚠ {len(blocked)} BLOCK — designs that failed the structural gate:")
        for e in blocked[-5:]:
            print(f"    [{e.get('workflow','?')}] {e.get('note','')[:100]}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Context Ethics Gate — deterministic backstop.")
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("check", help="Run structural checks on a spec/copy and log the verdict.")
    c.add_argument("--file", default=None, help="Path to the context-design spec / copy file.")
    c.add_argument("--text", default=None, help="Inline text to check.")
    c.add_argument("--kind", default="spec", choices=["spec", "copy", "honesty"])
    c.add_argument("--technique", default=None)
    c.add_argument("--workflow", default=None)
    c.add_argument("--note", default=None)
    c.set_defaults(func=_cmd_check)

    l = sub.add_parser("log", help="Record an explicit persona verdict.")
    l.add_argument("--verdict", required=True, choices=["PASS", "REVIEW", "BLOCK", "pass", "review", "block"])
    l.add_argument("--technique", default=None)
    l.add_argument("--workflow", default=None)
    l.add_argument("--kind", default="spec")
    l.add_argument("--note", default=None)
    l.set_defaults(func=_cmd_log)

    r = sub.add_parser("report", help="Summarize recent verdicts.")
    r.add_argument("--days", type=int, default=7)
    r.set_defaults(func=_cmd_report)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
