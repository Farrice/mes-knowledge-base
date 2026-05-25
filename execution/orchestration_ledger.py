#!/usr/bin/env python3
"""
Orchestration Ledger — Post-run trace emitter (Autopilot Wave 4 / 2026-05-21).
Phase B (2026-05-25): Ledger learning loop. Suggestions now carry stable
suggestion_ids so accept/ignore/reject signals can flow back via
record_outcome() and influence future suggestions via weight_suggestions().

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
    - evolution_store/ledger_feedback.jsonl (Phase B — written by record_outcome)

Public functions:
    emit_ledger(session_id, project=None, since_ts=None) -> str
        Returns markdown ledger string. Also saves to
        _active/_ledgers/autopilot-<session_id>.md and writes a sidecar
        .agent/pending-suggestions.jsonl entry per suggestion (so
        chain_runner.finalize can auto-log invocation matches).

    record_outcome(suggestion_id, action, workflow=None, notes=None) -> None
        Append a feedback row to evolution_store/ledger_feedback.jsonl.
        action ∈ {"invoked", "ignored", "modified", "rejected"}.

    weight_suggestions(candidates: List[dict]) -> List[dict]
        Reorder + downweight a candidate suggestion list based on the
        user's historical accept rate per pattern (Phase B v1: simple
        threshold rule, room for ML later).
"""

from __future__ import annotations

import argparse
import hashlib
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

# Phase B (2026-05-25) — Ledger learning loop
LEDGER_FEEDBACK = ROOT / "evolution_store" / "ledger_feedback.jsonl"
PENDING_SUGGESTIONS = ROOT / ".agent" / "pending-suggestions.jsonl"

VALID_ACTIONS = {"invoked", "ignored", "modified", "rejected"}


def _parse_ts_to_naive_local(ts: str) -> Optional[datetime]:
    """Parse an ISO-8601 timestamp string into a naive local datetime.

    - Naive input (no tz info) is assumed to be local time, returned as-is.
    - Aware input (e.g. ends in 'Z' or '+00:00') is converted to local time
      and stripped of tzinfo so it can be compared against naive timestamps.
    - Returns None on parse failure so callers can skip the entry.

    Rationale: chain_runner writes traces with `datetime.now().isoformat()`
    (naive local). Callers passing UTC-aware `--since` (e.g. from `date -u`)
    previously failed string lex-compare against local-naive timestamps,
    silently filtering out the entire session. This normalizer fixes that.
    """
    if not ts:
        return None
    try:
        # Accept the 'Z' suffix that strict ISO-8601 uses for UTC.
        normalized = ts.replace("Z", "+00:00") if ts.endswith("Z") else ts
        dt = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if dt.tzinfo is not None:
        # Convert aware → local naive so we can compare against trace writes.
        dt = dt.astimezone().replace(tzinfo=None)
    return dt


def _load_traces_since(since_ts: str) -> List[Dict[str, Any]]:
    """Load v2 traces with timestamp >= since_ts (timezone-aware)."""
    if not TRACES_V2.exists():
        return []
    cutoff = _parse_ts_to_naive_local(since_ts)
    out = []
    for p in TRACES_V2.glob("trace_*.json"):
        try:
            d = json.loads(p.read_text())
            trace_dt = _parse_ts_to_naive_local(d.get("timestamp", ""))
            if cutoff is None or (trace_dt is not None and trace_dt >= cutoff):
                out.append(d)
        except Exception:
            continue
    out.sort(key=lambda t: t.get("timestamp", ""))
    return out


def _load_jsonl_since(path: Path, since_ts: str) -> List[Dict[str, Any]]:
    """Load JSONL entries with timestamp >= since_ts (timezone-aware)."""
    if not path.exists():
        return []
    cutoff = _parse_ts_to_naive_local(since_ts)
    out = []
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    d = json.loads(line)
                    entry_dt = _parse_ts_to_naive_local(d.get("timestamp", ""))
                    if cutoff is None or (entry_dt is not None and entry_dt >= cutoff):
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


def _pattern_key(text: str) -> str:
    """Pattern hash for cross-session suggestion matching.

    Two suggestions for the same underlying recommendation (e.g., both
    suggesting /aar) should share a pattern_key so accept rates aggregate.
    Uses first non-comment, non-whitespace 60 chars after the # header line.
    """
    # Strip the leading '# <comment>\n' header to focus on the actual prompt body
    body = text
    if text.startswith("#"):
        body = text.split("\n", 1)[-1] if "\n" in text else text
    canonical = " ".join(body.split())[:60].lower()
    return hashlib.sha1(canonical.encode()).hexdigest()[:8]


def _make_suggestion_id(session_id: str, idx: int, text: str) -> str:
    """Stable per-session-per-position suggestion id.

    Returns 8 hex chars — short enough to render in markdown without
    bloating, long enough to be collision-safe across a single session.
    Cross-session collisions don't matter because record_outcome scopes
    by session_id too.
    """
    canonical = f"{session_id}|{idx}|{_pattern_key(text)}"
    return hashlib.sha1(canonical.encode()).hexdigest()[:8]


def _extract_workflow_hint(text: str) -> Optional[str]:
    """Best-effort extraction of the slash command this suggestion proposes.

    Used by chain_runner.finalize backstop to auto-match a workflow
    invocation to a pending suggestion (within 24h window).
    """
    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("/"):
            # Take the first token after the leading slash
            return line.split()[0]
    # Python execution scripts don't have a slash; return None
    return None


def _refinement_prompts(traces: List[Dict[str, Any]], session_id: str = "anon") -> List[Dict[str, str]]:
    """Build 3-5 copy-pasteable refinement prompts from the session.

    Phase B (2026-05-25): returns list of dicts, not bare strings.
    Each dict has {id, text, workflow_hint, pattern_key}. Weighted
    by user's historical accept rate per pattern.
    """
    prompts: List[Dict[str, str]] = []

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
            prompts.append({
                "text": (
                    f"# Refine the below-threshold deliverable:\n"
                    f"/writers-room\n"
                    f"\"Diagnose the {workflow} output by {expert} that scored {comp}. "
                    f"Run the adversarial pass and rewrite the weakest section.\""
                ),
            })

    # Always offer the atomize prompt if there's any strong content
    strong = [
        t for t in traces
        if t.get("quality", {}).get("composite", 0) >= 8 and t.get("context", {}).get("task_type") in ("Content", "Strategy")
    ]
    if strong:
        prompts.append({
            "text": (
                "# Atomize the strongest deliverable into platform-native variants:\n"
                "/atomize <deliverable-path> --formats linkedin-carousel,linkedin-post,note,thread"
            ),
        })

    # Offer the Notion ship prompt if we have any Content task type
    content_traces = [t for t in traces if t.get("context", {}).get("task_type") == "Content"]
    if content_traces:
        prompts.append({
            "text": (
                "# Ship the deliverable to Notion content pipeline:\n"
                "python execution/notion_api.py capture \"<title>\" \"<body>\" --type Content"
            ),
        })

    # Always offer the /aar after-action prompt
    prompts.append({
        "text": (
            "# Capture lessons + update calibration for next session:\n"
            "/aar"
        ),
    })

    # Annotate each with stable id + workflow hint + pattern key
    for i, p in enumerate(prompts):
        p["id"] = _make_suggestion_id(session_id, i, p["text"])
        p["pattern_key"] = _pattern_key(p["text"])
        hint = _extract_workflow_hint(p["text"])
        if hint:
            p["workflow_hint"] = hint

    # Phase B: weight by historical accept rate
    weighted = weight_suggestions(prompts)
    return weighted[:5]


def _suggested_next_moves(traces: List[Dict[str, Any]], session_id: str = "anon") -> List[Dict[str, str]]:
    """Build the 'not gates, just options' next-moves list.

    Phase B: same dict shape as _refinement_prompts so feedback can flow.
    """
    moves: List[Dict[str, str]] = []
    weak = [t for t in traces if t.get("quality", {}).get("composite", 10) < 7.5]
    strong = [t for t in traces if t.get("quality", {}).get("composite", 0) >= 8]
    blocked = [t for t in traces if "BLOCKED" in (t.get("notes") or "")]

    if blocked:
        moves.append({"text": f"Re-verify factual claims on {len(blocked)} BLOCKED deliverable(s) — facts > polish."})
    if weak:
        moves.append({"text": f"Refine {len(weak)} below-threshold deliverable(s) before shipping."})
    if strong:
        moves.append({"text": f"Ship {len(strong)} ready deliverable(s) — they cleared the bimodal PASS bar."})
    if not (weak or strong or blocked):
        moves.append({"text": "All session deliverables clean — proceed to next session."})

    for i, m in enumerate(moves):
        # Use a different idx-namespace so move-ids don't collide with prompt-ids
        m["id"] = _make_suggestion_id(session_id, 100 + i, m["text"])
        m["pattern_key"] = _pattern_key(m["text"])
    return moves


# ═══════════════════════════════════════════════════════════════
# Phase B — Ledger learning loop
# ═══════════════════════════════════════════════════════════════

def _lookup_pending(suggestion_id: str) -> Optional[Dict[str, Any]]:
    """Find the pending-suggestions row for this suggestion_id."""
    if not PENDING_SUGGESTIONS.exists():
        return None
    try:
        with open(PENDING_SUGGESTIONS) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    d = json.loads(line)
                    if d.get("suggestion_id") == suggestion_id:
                        return d
                except Exception:
                    continue
    except Exception:
        return None
    return None


def record_outcome(
    suggestion_id: str,
    action: str,
    workflow: Optional[str] = None,
    session_id: Optional[str] = None,
    notes: Optional[str] = None,
) -> None:
    """Append a feedback row to evolution_store/ledger_feedback.jsonl.

    Called when the user accepts/ignores/modifies/rejects a ledger
    suggestion. The chain_runner.finalize backstop auto-fires this with
    action='invoked' when a workflow matches a pending suggestion within
    24h — that's the AI-Memory-Dependent-Observability fix.

    Looks up the pending-suggestions sidecar by suggestion_id to enrich
    the row with pattern_key and (if not provided) session_id — this
    lets weight_suggestions() aggregate accept rates across sessions.

    Args:
        suggestion_id: 8-hex id from the ledger markdown
        action: one of VALID_ACTIONS
        workflow: optional slash command actually invoked
        session_id: optional autopilot session
        notes: free-form annotation
    """
    if action not in VALID_ACTIONS:
        raise ValueError(
            f"action must be one of {sorted(VALID_ACTIONS)}, got {action!r}"
        )

    LEDGER_FEEDBACK.parent.mkdir(parents=True, exist_ok=True)

    row = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "suggestion_id": suggestion_id,
        "action": action,
    }

    # Enrich from pending-suggestions sidecar (pattern_key is required for
    # weight_suggestions to count this signal)
    pending = _lookup_pending(suggestion_id)
    if pending:
        if pending.get("pattern_key"):
            row["pattern_key"] = pending["pattern_key"]
        # Pick up session_id from sidecar if caller didn't supply
        if not session_id and pending.get("session_id"):
            session_id = pending["session_id"]

    if workflow:
        row["workflow"] = workflow
    if session_id:
        row["session_id"] = session_id
    if notes:
        row["notes"] = notes

    with open(LEDGER_FEEDBACK, "a") as f:
        f.write(json.dumps(row) + "\n")


def _load_feedback(max_age_days: int = 90) -> List[Dict[str, Any]]:
    """Load ledger feedback rows from the last N days."""
    if not LEDGER_FEEDBACK.exists():
        return []
    cutoff = datetime.now() - timedelta(days=max_age_days)
    out = []
    try:
        with open(LEDGER_FEEDBACK) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    d = json.loads(line)
                    ts = _parse_ts_to_naive_local(d.get("timestamp", ""))
                    if ts is not None and ts >= cutoff:
                        out.append(d)
                except Exception:
                    continue
    except Exception:
        return []
    return out


def weight_suggestions(candidates: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Reorder + filter candidates based on historical accept rate.

    Phase B v1 — simple threshold rules. Room for ML later.

    Rules:
    - If a pattern has been suggested >= 5 times with accept rate < 0.15,
      mark it `cold=True` (kept but ranked last; could be hidden later).
    - If accept rate >= 0.5 with N>=3, mark `hot=True` (ranked first).
    - Otherwise: leave untouched.

    Returns the same list with optional `hot` / `cold` / `accept_rate`
    / `samples` annotations + stable sort: hot → neutral → cold.
    """
    feedback = _load_feedback()
    if not feedback:
        return candidates

    # Tally per pattern_key
    counts: Dict[str, Dict[str, int]] = {}
    for row in feedback:
        # Older rows from before Phase B won't have pattern_key — skip them.
        # We could lookup by suggestion_id but it's session-scoped, so we'd
        # need a separate suggestion_id → pattern_key index. Skip is fine.
        key = row.get("pattern_key")
        if not key:
            continue
        c = counts.setdefault(key, {"samples": 0, "invoked": 0})
        c["samples"] += 1
        if row.get("action") == "invoked":
            c["invoked"] += 1

    for c in candidates:
        key = c.get("pattern_key")
        if not key or key not in counts:
            continue
        samples = counts[key]["samples"]
        invoked = counts[key]["invoked"]
        rate = invoked / samples if samples else 0.0
        c["samples"] = samples
        c["accept_rate"] = round(rate, 3)
        if samples >= 5 and rate < 0.15:
            c["cold"] = True
        elif samples >= 3 and rate >= 0.5:
            c["hot"] = True

    # Stable sort: hot first, neutral middle, cold last
    def _rank(c: Dict[str, Any]) -> int:
        if c.get("hot"):
            return 0
        if c.get("cold"):
            return 2
        return 1

    return sorted(candidates, key=_rank)


def _write_pending_suggestions(
    session_id: str,
    refinement_prompts: List[Dict[str, str]],
    next_moves: List[Dict[str, str]],
) -> None:
    """Sidecar registry for chain_runner.finalize backstop.

    For 24h after a ledger emits, chain_runner can match an invoked
    workflow to a pending suggestion_id and auto-fire record_outcome.
    Closes the AI-Memory-Dependent-Observability failure class.
    """
    PENDING_SUGGESTIONS.parent.mkdir(parents=True, exist_ok=True)
    now_iso = datetime.now().isoformat(timespec="seconds")
    rows = []
    for p in refinement_prompts + next_moves:
        rows.append({
            "timestamp": now_iso,
            "session_id": session_id,
            "suggestion_id": p["id"],
            "pattern_key": p.get("pattern_key", ""),
            "workflow_hint": p.get("workflow_hint", ""),
        })
    if not rows:
        return
    try:
        with open(PENDING_SUGGESTIONS, "a") as f:
            for r in rows:
                f.write(json.dumps(r) + "\n")
    except Exception:
        pass  # sidecar is nice-to-have, never blocks ledger emit


def find_pending_match(workflow: str, max_age_hours: int = 24) -> Optional[Dict[str, Any]]:
    """Find a recent pending suggestion that matches an invoked workflow.

    Used by chain_runner.finalize. Returns the most-recent matching row
    (suggestion_id + pattern_key + session_id) or None.
    """
    if not PENDING_SUGGESTIONS.exists():
        return None
    cutoff = datetime.now() - timedelta(hours=max_age_hours)
    matches = []
    try:
        with open(PENDING_SUGGESTIONS) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    d = json.loads(line)
                    hint = d.get("workflow_hint", "")
                    if not hint:
                        continue
                    if hint != workflow and hint.lstrip("/") != workflow.lstrip("/"):
                        continue
                    ts = _parse_ts_to_naive_local(d.get("timestamp", ""))
                    if ts is not None and ts >= cutoff:
                        matches.append(d)
                except Exception:
                    continue
    except Exception:
        return None
    if not matches:
        return None
    matches.sort(key=lambda r: r.get("timestamp", ""), reverse=True)
    return matches[0]


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

    refinement_prompts = _refinement_prompts(traces, session_id=session_id)
    next_moves = _suggested_next_moves(traces, session_id=session_id)

    # Phase B: write pending-suggestions sidecar for chain_runner.finalize backstop
    _write_pending_suggestions(session_id, refinement_prompts, next_moves)

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
            sid = p.get("id", "")
            marker = ""
            if p.get("hot"):
                rate = p.get("accept_rate", 0)
                marker = f"  [hot · accept_rate {rate}]"
            elif p.get("cold"):
                rate = p.get("accept_rate", 0)
                marker = f"  [cold · accept_rate {rate} — rarely fired]"
            lines.append(f"\n{i}.  [id: {sid}]{marker}")
            lines.append(p["text"])
    else:
        lines.append("  (no refinement prompts — clean session)")
    lines.append("")
    lines.append("─" * 60)
    lines.append("SUGGESTED NEXT MOVES (not gates — options)")
    lines.append("─" * 60)
    for m in next_moves:
        sid = m.get("id", "")
        lines.append(f"  • [id: {sid}] {m['text']}")
    lines.append("")
    # Phase B: explain the [id: ...] suffixes the first time they appear
    lines.append(
        "  (Suggestion ids let the system learn what you fire vs ignore. "
        "Auto-tracked when you run the suggested workflow within 24h; "
        "manual: `python3 execution/orchestration_ledger.py record "
        "--suggestion-id <id> --action invoked|ignored|modified|rejected`.)"
    )
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
def _cmd_emit(args) -> None:
    print(emit_ledger(args.session_id, args.project, args.since))


def _cmd_record(args) -> None:
    record_outcome(
        suggestion_id=args.suggestion_id,
        action=args.action,
        workflow=args.workflow,
        session_id=args.session_id,
        notes=args.notes,
    )
    print(
        f"Recorded: suggestion_id={args.suggestion_id} action={args.action}"
        + (f" workflow={args.workflow}" if args.workflow else "")
    )


def _cmd_feedback_report(args) -> None:
    """Show acceptance rates per pattern over the last N days."""
    feedback = _load_feedback(max_age_days=args.days)
    if not feedback:
        print(f"No ledger feedback in the last {args.days} days.")
        return

    # Tally per pattern_key
    counts: Dict[str, Dict[str, int]] = {}
    for row in feedback:
        key = row.get("pattern_key") or "(unkeyed)"
        c = counts.setdefault(key, {"samples": 0, "invoked": 0, "ignored": 0,
                                     "modified": 0, "rejected": 0})
        c["samples"] += 1
        action = row.get("action", "")
        if action in c:
            c[action] += 1

    print(f"Ledger feedback report — last {args.days} days, {len(feedback)} signals total")
    print("=" * 70)
    print(f"{'pattern':12s} {'samples':>8s} {'invoked':>8s} {'rate':>6s}  status")
    print("-" * 70)
    for key in sorted(counts.keys(), key=lambda k: -counts[k]["samples"]):
        c = counts[key]
        rate = c["invoked"] / c["samples"] if c["samples"] else 0.0
        if c["samples"] >= 5 and rate < 0.15:
            status = "cold"
        elif c["samples"] >= 3 and rate >= 0.5:
            status = "hot"
        else:
            status = "neutral"
        print(f"{key:12s} {c['samples']:>8d} {c['invoked']:>8d} {rate:>6.2f}  {status}")


def main():
    parser = argparse.ArgumentParser(
        description="Orchestration Ledger — emit, record feedback, report rates",
    )
    sub = parser.add_subparsers(dest="cmd")

    # emit (default behavior)
    p_emit = sub.add_parser("emit", help="Emit a session ledger")
    p_emit.add_argument("--session-id", required=True)
    p_emit.add_argument("--project", default=None)
    p_emit.add_argument("--since", default=None, help="ISO timestamp; defaults to 1 hour ago")
    p_emit.set_defaults(func=_cmd_emit)

    # record (Phase B — accept/ignore/modify/reject a suggestion)
    p_rec = sub.add_parser("record", help="Record feedback on a ledger suggestion")
    p_rec.add_argument("--suggestion-id", required=True, help="8-hex id from ledger markdown")
    p_rec.add_argument("--action", required=True, choices=sorted(VALID_ACTIONS))
    p_rec.add_argument("--workflow", default=None, help="Slash command actually invoked, if any")
    p_rec.add_argument("--session-id", default=None)
    p_rec.add_argument("--notes", default=None)
    p_rec.set_defaults(func=_cmd_record)

    # feedback-report
    p_rep = sub.add_parser("feedback-report", help="Show acceptance rates per pattern")
    p_rep.add_argument("--days", type=int, default=30)
    p_rep.set_defaults(func=_cmd_feedback_report)

    # Backwards-compat: bare `--session-id X` (no subcommand) still works as emit.
    # If --session-id is the FIRST positional arg, dispatch to emit.
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--session-id":
        # Reroute: prepend "emit"
        sys.argv.insert(1, "emit")

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        return
    args.func(args)


if __name__ == "__main__":
    main()
