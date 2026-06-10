#!/usr/bin/env python3
"""
forge_gate.py — Extraction freeze gate (deterministic).

Rule: no new /extract or /extract-forge until the most recent extraction has
≥3 PRODUCTION uses (finalize traces where workflow is not a build workflow).
Origin: audit 2026-04-24 ("growth curve flipped from accretive to dilutive")
+ Sean Macintyre audit 2026-06-09 (17 workflows, 0 uses in 6 weeks). New
domain knowledge enters as genius.md enrichment of A-tier skills instead.

Usage:
    python3 execution/forge_gate.py check [--force]
    python3 execution/forge_gate.py record <skill-dir-name> [--expert <name>]
    python3 execution/forge_gate.py status

Exit codes (check):
    0 = gate OPEN (last extraction has enough production uses, no prior
        extraction on record, or --force override logged)
    2 = gate CLOSED (last extraction under-used; message on stdout)

Soft gate by user decision 2026-06-09: --force is honored but logged to
evolution_store/forge_gate_overrides.jsonl.
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
    traces = _load_traces()
    state = _last_extraction(traces)
    if state is None:
        print("FORGE GATE OPEN — no prior extraction on record.")
        return 0

    skill = state["last_extraction"]
    uses = _production_uses(traces, skill, state.get("expert", ""), state.get("shipped", ""))

    if len(uses) >= REQUIRED_USES:
        print(f"FORGE GATE OPEN — {skill} has {len(uses)}/{REQUIRED_USES} production uses.")
        return 0

    if args.force:
        OVERRIDE_LOG.parent.mkdir(parents=True, exist_ok=True)
        with open(OVERRIDE_LOG, "a") as f:
            f.write(json.dumps({
                "timestamp": datetime.now().isoformat(),
                "skill": skill,
                "production_uses": len(uses),
                "required": REQUIRED_USES,
                "reason": args.reason or "unspecified",
            }) + "\n")
        print(f"FORGE GATE FORCED OPEN — {skill} has only {len(uses)}/{REQUIRED_USES} "
              f"production uses. Override logged to {OVERRIDE_LOG.name}.")
        return 0

    print(f"""FORGE GATE CLOSED — {skill} has {len(uses)}/{REQUIRED_USES} production uses since ship.

The last extraction hasn't earned its keep yet. Options (in order of preference):
  1. DEPLOY IT: route real work through {skill} ({REQUIRED_USES - len(uses)} more
     finalize traces with workflow != extract-forge opens the gate).
  2. ENRICH INSTEAD: add the new source material as genius.md enrichment to an
     existing A-tier skill (per audit-2026-04-24 — knowledge enters existing
     skills, not new SKILL.md files).
  3. OVERRIDE (logged): re-run with --force --reason "<why this can't wait>".
""")
    return 2


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
        print(json.dumps({"gate": "open", "last_extraction": None}, indent=2))
        return 0
    skill = state["last_extraction"]
    uses = _production_uses(traces, skill, state.get("expert", ""), state.get("shipped", ""))
    print(json.dumps({
        "gate": "open" if len(uses) >= REQUIRED_USES else "closed",
        "last_extraction": skill,
        "shipped": state.get("shipped"),
        "production_uses": len(uses),
        "required": REQUIRED_USES,
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
