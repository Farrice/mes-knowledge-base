#!/usr/bin/env python3
"""
forge_gate.py — Extraction usage TELEMETRY (never a gate).

STANDING DECISION (Farrice, 2026-06-09): extractions are NEVER gated. The
freeze concept shipped in the rebuild and was reversed the same day at his
explicit direction. This script survives purely as telemetry: it counts
PRODUCTION uses of the most recent extraction (finalize traces where workflow
is not a build workflow) for the monthly /weekly-closeout report.

Usage:
    python3 execution/forge_gate.py status                    # JSON usage report
    python3 execution/forge_gate.py record <skill-dir> [--expert <name>]
    python3 execution/forge_gate.py check                     # ALWAYS exit 0 (kept
                                                              # for compatibility;
                                                              # prints usage info)
"""

import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent
TRACES_DIR = ROOT / "evolution_store" / "v2_traces"
STATE_FILE = ROOT / ".agent" / "forge-state.json"
OVERRIDE_LOG = ROOT / "evolution_store" / "forge_gate_overrides.jsonl"

REQUIRED_USES = 3

try:
    sys.path.insert(0, str(ROOT / "execution"))
    from skill_auditor import BUILD_WORKFLOWS  # single source of truth
except Exception:
    BUILD_WORKFLOWS = {"extract-forge", "extract"}


def _load_traces():
    if not TRACES_DIR.exists():
        return []
    out = []
    for tf in sorted(TRACES_DIR.glob("trace_*.json")):
        try:
            with open(tf) as f:
                out.append(json.load(f))
        except Exception:
            continue
    return out


def _last_extraction(traces):
    """Most recent extraction: forge-state.json first, else latest build trace."""
    if STATE_FILE.exists():
        try:
            state = json.loads(STATE_FILE.read_text())
            if state.get("last_extraction"):
                return state
        except Exception:
            pass
    build = [t for t in traces
             if (t.get("workflow") or "") in BUILD_WORKFLOWS and t.get("component")]
    if not build:
        return None
    latest = max(build, key=lambda t: t.get("timestamp", ""))
    return {
        "last_extraction": latest.get("component"),
        "expert": latest.get("expert", ""),
        "shipped": latest.get("timestamp", ""),
        "source": "inferred_from_traces",
    }


def _production_uses(traces, skill, expert, shipped):
    """Traces for this skill AFTER ship date, excluding build workflows."""
    uses = []
    for t in traces:
        if (t.get("workflow") or "") in BUILD_WORKFLOWS:
            continue
        comp = t.get("component") or t.get("skill") or ""
        exp = t.get("expert") or ""
        if comp != skill and not (expert and exp == expert):
            continue
        if shipped and (t.get("timestamp", "") <= shipped):
            continue
        uses.append({"timestamp": t.get("timestamp"), "workflow": t.get("workflow"),
                     "composite": (t.get("quality") or {}).get("composite")})
    return uses


def cmd_check(args):
    """Compatibility shim — ALWAYS exits 0. Extractions are never gated
    (standing decision 2026-06-09). Prints the usage count as information."""
    traces = _load_traces()
    state = _last_extraction(traces)
    if state is None:
        print("EXTRACTION TELEMETRY — no prior extraction on record. Proceed.")
        return 0
    skill = state["last_extraction"]
    uses = _production_uses(traces, skill, state.get("expert", ""), state.get("shipped", ""))
    print(f"EXTRACTION TELEMETRY (informational, never blocks) — last extraction "
          f"{skill}: {len(uses)} production use(s) since ship. Proceed.")
    return 0


def cmd_record(args):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state = {
        "last_extraction": args.skill,
        "expert": args.expert or "",
        "shipped": datetime.now().isoformat(),
        "source": "forge_gate record",
    }
    STATE_FILE.write_text(json.dumps(state, indent=2))
    print(f"Recorded extraction: {args.skill} (shipped {state['shipped']})")
    return 0


def cmd_status(args):
    traces = _load_traces()
    state = _last_extraction(traces)
    if state is None:
        print(json.dumps({"mode": "telemetry-only", "last_extraction": None}, indent=2))
        return 0
    skill = state["last_extraction"]
    uses = _production_uses(traces, skill, state.get("expert", ""), state.get("shipped", ""))
    print(json.dumps({
        "mode": "telemetry-only (extractions are never gated)",
        "last_extraction": skill,
        "shipped": state.get("shipped"),
        "production_uses": len(uses),
        "uses": uses,
    }, indent=2))
    return 0


def main():
    p = argparse.ArgumentParser(description="Extraction freeze gate")
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("check", help="Exit 0 if gate open, 2 if closed")
    c.add_argument("--force", action="store_true", help="Override (logged)")
    c.add_argument("--reason", default="", help="Why the override is needed")

    r = sub.add_parser("record", help="Record a completed extraction")
    r.add_argument("skill", help="Skill directory name")
    r.add_argument("--expert", default="", help="Expert name")

    sub.add_parser("status", help="Show gate state as JSON")

    args = p.parse_args()
    return {"check": cmd_check, "record": cmd_record, "status": cmd_status}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
