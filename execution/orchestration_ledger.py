#!/usr/bin/env python3
"""
Orchestration Ledger — Post-run trace emitter (Autopilot Wave 4 / 2026-05-21).

This is what /autopilot prints when a session ends. NO interrogative —
the run ends, the ledger surfaces what happened, the user reads it.
Refinement is opt-in (via copy-pasteable prompts), never gated.

Reads from existing artifacts (no new tracking infrastructure):
    - evolution_store/traces/routing_decisions.jsonl
    - evolution_store/v2_traces/*.json
    - .agent/cost-gate-log.jsonl (if present)
    - projects/<slug>/state.yaml (if --project set)
    - evolution_store/sub_agent_misses.jsonl
    - evolution_store/predictions/*.json (post-Wave-3)

Skinny version (Wave 4) — populates RAN, LOADED, DELIVERABLES, GATES,
REFINEMENT PROMPTS. Wave 5 adds the full SUB-AGENT FAN-OUT section,
ROUTING VERIFIED detail, deeper SUGGESTED NEXT MOVES intelligence.

Function:
    emit_ledger(session_id, project=None, since_ts=None) -> str
        Returns markdown ledger string. Also saves to
        _active/_ledgers/autopilot-<session_id>.md.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).parent.parent
TRACES_V2 = ROOT / "evolution_store" / "v2_traces"
ROUTING_LOG = ROOT / "evolution_store" / "traces" / "routing_decisions.jsonl"
COST_LOG = ROOT / ".agent" / "cost-gate-log.jsonl"
SUBAGENT_MISSES = ROOT / "evolution_store" / "sub_agent_misses.jsonl"
PREDICTIONS = ROOT / "evolution_store" / "predictions"
LEDGER_OUT_DIR = ROOT / "_active" / "_ledgers"


def _load_traces_since(since_ts: str) -> List[Dict[str, Any]]:
    """Load v2 traces with timestamp >= since_ts (ISO format)."""
    if not TRACES_V2.exists():
        return []
    out = []
    for p in TRACES_V2.glob("trace_*.json"):
        try:
            d = json.loads(p.read_text())
            if d.get("timestamp", "") >= since_ts:
                out.append(d)
        except Exception:
            continue
    out.sort(key=lambda t: t.get("timestamp", ""))
    return out


def _load_jsonl_since(path: Path, since_ts: str) -> List[Dict[str, Any]]:
    """Load JSONL entries with timestamp >= since_ts."""
    if not path.exists():
        return []
    out = []
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    d = json.loads(line)
                    if d.get("timestamp", "") >= since_ts:
                        out.append(d)
                except Exception:
                    continue
    except Exception:
        return []
    return out


def _verdict_marker(verdict: str) -> str:
    return {
        "PASS": "Keep",
        "MARGINAL": "Marginal",
        "FAIL": "Needs Improvement",
    }.get(verdict, verdict or "?")


def _refinement_prompts(traces: List[Dict[str, Any]]) -> List[str]:
    """Build 3-5 copy-pasteable refinement prompts from the session."""
    prompts: List[str] = []

    # Find any deliverable that landed below PASS — auto-suggest /writers-room
    weak = [
        t for t in traces
        if t.get("quality", {}).get("composite", 10) < 7.5
    ]
    if weak:
        for w in weak[:2]:
            comp = w.get("quality", {}).get("composite", "?")
            expert = w.get("expert") or "(unknown)"
            workflow = w.get("workflow") or "(unknown)"
            prompts.append(
                f"# Refine the below-threshold deliverable:\n"
                f"/writers-room\n"
                f"\"Diagnose the {workflow} output by {expert} that scored {comp}. "
                f"Run the adversarial pass and rewrite the weakest section.\""
            )

    # Always offer the atomize prompt if there's any strong content
    strong = [
        t for t in traces
        if t.get("quality", {}).get("composite", 0) >= 8 and t.get("context", {}).get("task_type") in ("Content", "Strategy")
    ]
    if strong:
        prompts.append(
            "# Atomize the strongest deliverable into platform-native variants:\n"
            "/atomize <deliverable-path> --formats linkedin-carousel,linkedin-post,note,thread"
        )

    # Offer the Notion ship prompt if we have any Content task type
    content_traces = [t for t in traces if t.get("context", {}).get("task_type") == "Content"]
    if content_traces:
        prompts.append(
            "# Ship the deliverable to Notion content pipeline:\n"
            "python execution/notion_api.py capture \"<title>\" \"<body>\" --type Content"
        )

    # Always offer the /aar after-action prompt
    prompts.append(
        "# Capture lessons + update calibration for next session:\n"
        "/aar"
    )

    return prompts[:5]


def _suggested_next_moves(traces: List[Dict[str, Any]]) -> List[str]:
    """Build the 'not gates, just options' next-moves list."""
    moves = []
    weak = [t for t in traces if t.get("quality", {}).get("composite", 10) < 7.5]
    strong = [t for t in traces if t.get("quality", {}).get("composite", 0) >= 8]
    blocked = [t for t in traces if "BLOCKED" in (t.get("notes") or "")]

    if blocked:
        moves.append(f"Re-verify factual claims on {len(blocked)} BLOCKED deliverable(s) — facts > polish.")
    if weak:
        moves.append(f"Refine {len(weak)} below-threshold deliverable(s) before shipping.")
    if strong:
        moves.append(f"Ship {len(strong)} ready deliverable(s) — they cleared the bimodal PASS bar.")
    if not (weak or strong or blocked):
        moves.append("All session deliverables clean — proceed to next session.")
    return moves


def emit_ledger(
    session_id: str,
    project: Optional[str] = None,
    since_ts: Optional[str] = None,
) -> str:
    """Generate the markdown ledger for an autopilot session.

    Args:
        session_id: autopilot session id (e.g., 'ap-20260521-115500-research')
        project: optional project slug for state.yaml lookup
        since_ts: ISO timestamp; defaults to 1 hour ago

    Returns:
        Markdown string. Also writes to _active/_ledgers/autopilot-<id>.md
    """
    if since_ts is None:
        since_ts = (datetime.now() - timedelta(hours=1)).isoformat()

    traces = _load_traces_since(since_ts)
    routing = _load_jsonl_since(ROUTING_LOG, since_ts)
    cost = _load_jsonl_since(COST_LOG, since_ts)
    misses = _load_jsonl_since(SUBAGENT_MISSES, since_ts)

    total_cost = sum(c.get("actual_cost") or 0 for c in cost) or 0
    estimated_cost = sum(c.get("estimated_cost") or 0 for c in cost) or 0

    composites = [t.get("quality", {}).get("composite") for t in traces if t.get("quality")]
    composites = [c for c in composites if c is not None]

    deliverables_lines = []
    for t in traces:
        q = t.get("quality") or {}
        comp = q.get("composite", "?")
        verdict = t.get("notes", "").split("|")[0].strip() if t.get("notes") else ""
        expert = t.get("expert") or ""
        workflow = t.get("workflow") or ""
        operation = t.get("operation") or ""
        deliverables_lines.append(
            f"  • [{operation}] {workflow} via {expert} — composite {comp}/10"
        )

    refinement_prompts = _refinement_prompts(traces)
    next_moves = _suggested_next_moves(traces)

    # Build the ledger
    lines: List[str] = []
    lines.append("═" * 60)
    lines.append(f"ORCHESTRATION LEDGER — autopilot session {session_id}")
    lines.append("═" * 60)
    lines.append("")
    lines.append(f"Project:        {project or '(none)'}")
    lines.append(f"Window:         since {since_ts}")
    lines.append(f"Deliverables:   {len(traces)}")
    lines.append(f"Median composite: {sorted(composites)[len(composites)//2] if composites else 'n/a'}")
    lines.append(f"Total paid cost: ${total_cost:.4f}  (estimated ${estimated_cost:.4f})")
    lines.append("")
    lines.append("─" * 60)
    lines.append("RAN")
    lines.append("─" * 60)
    if deliverables_lines:
        lines.extend(deliverables_lines)
    else:
        lines.append("  (no traces in window)")
    lines.append("")
    lines.append("─" * 60)
    lines.append("ROUTING VERIFIED")
    lines.append("─" * 60)
    if routing:
        lines.append(f"  Routing decisions logged: {len(routing)}")
        violations = [r for r in routing if r.get("violation")]
        lines.append(f"  Violations: {len(violations)}")
    else:
        lines.append("  (no routing decisions in window)")
    lines.append("")
    lines.append("─" * 60)
    lines.append("SUB-AGENT FAN-OUT")
    lines.append("─" * 60)
    if misses:
        lines.append(f"  Misses logged (qualifying workflows that didn't spawn): {len(misses)}")
        for m in misses[-3:]:
            lines.append(f"    - {m.get('workflow')} / {m.get('skill')}")
    else:
        lines.append("  (no qualifying-workflow misses in window)")
    lines.append("")
    lines.append("─" * 60)
    lines.append("COPY-PASTE REFINEMENT PROMPTS")
    lines.append("─" * 60)
    if refinement_prompts:
        for i, p in enumerate(refinement_prompts, 1):
            lines.append(f"\n{i}.")
            lines.append(p)
    else:
        lines.append("  (no refinement prompts — clean session)")
    lines.append("")
    lines.append("─" * 60)
    lines.append("SUGGESTED NEXT MOVES (not gates — options)")
    lines.append("─" * 60)
    for m in next_moves:
        lines.append(f"  • {m}")
    lines.append("")
    if project:
        lines.append(f"State persisted: projects/{project}/state.yaml")
    lines.append(f"Ledger archived: _active/_ledgers/autopilot-{session_id}.md")
    lines.append("═" * 60)

    ledger_md = "\n".join(lines)

    # Save to disk
    try:
        LEDGER_OUT_DIR.mkdir(parents=True, exist_ok=True)
        out_path = LEDGER_OUT_DIR / f"autopilot-{session_id}.md"
        out_path.write_text(ledger_md)
    except Exception:
        pass  # archiving is nice-to-have, never blocks

    return ledger_md


# ─── CLI ────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Orchestration Ledger emitter")
    parser.add_argument("--session-id", required=True)
    parser.add_argument("--project", default=None)
    parser.add_argument("--since", default=None, help="ISO timestamp; defaults to 1 hour ago")

    args = parser.parse_args()
    print(emit_ledger(args.session_id, args.project, args.since))


if __name__ == "__main__":
    main()
