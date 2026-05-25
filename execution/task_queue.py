#!/usr/bin/env python3
"""
Task Queue — per-project phase persistence for agent_tick (Phase D / 2026-05-25).

Persistence layer for multi-day autonomous agent work. Each project that
opts into agent_tick has its phase plan stored as JSONL files under
`.agent/queue/<slug>/`. agent_tick.py reads from `pending.jsonl`, executes
ONE phase, and moves it to either `done.jsonl` or `blocked.jsonl`.

Why JSONL not state.yaml: state.yaml (anchor_memory) is the project's
identity + key decisions + anchored deliverables. The task queue is the
operational stack of work-in-flight. Two different concerns, two different
files. anchor_memory.state.yaml is the WHO/WHAT/WHY; task_queue is the
WHEN-NEXT.

Layout:
    .agent/queue/<slug>/
        pending.jsonl    — phases not yet executed (FIFO)
        blocked.jsonl    — phases halted on user input (taste calls, etc.)
        done.jsonl       — completed phases with outcome summaries

Each row schema:
    {
        "phase_id": "<slug>-<n>-<short-name>",
        "title": "<one-line>",
        "instructions": "<what to do on this tick>",
        "expected_outputs": ["path-1", "path-2", ...],
        "depends_on": ["<phase_id>", ...],          # must be in done.jsonl
        "blocked_reason": "<reason>",               # only on blocked.jsonl
        "outcome": {                                # only on done.jsonl
            "files": [...],
            "summary": "...",
            "composite_score": <float>,
            "timestamp": "<iso>",
        },
        "enqueued_at": "<iso>",
    }

Public functions:
    enqueue(slug, phase_dict)
    next_pending(slug) -> dict or None
    mark_done(slug, phase_id, outcome)
    mark_blocked(slug, phase_id, reason)
    unblock(slug, phase_id)            # move back to pending
    list_queue(slug) -> {"pending": [...], "blocked": [...], "done": [...]}

CLI:
    python3 execution/task_queue.py enqueue <slug> --title "..." --instructions "..."
    python3 execution/task_queue.py next <slug>
    python3 execution/task_queue.py list <slug>
    python3 execution/task_queue.py done <slug> <phase_id> --summary "..."
    python3 execution/task_queue.py block <slug> <phase_id> --reason "..."
    python3 execution/task_queue.py unblock <slug> <phase_id>
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).parent.parent
QUEUE_DIR = ROOT / ".agent" / "queue"


def _project_dir(slug: str) -> Path:
    """Resolve project queue dir; create if missing."""
    if not re.match(r"^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", slug):
        raise ValueError(
            f"slug must be lowercase, alphanumeric + hyphens. Got: {slug!r}"
        )
    d = QUEUE_DIR / slug
    d.mkdir(parents=True, exist_ok=True)
    return d


def _read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    out = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except Exception:
                continue
    return out


def _write_jsonl(path: Path, rows: List[Dict[str, Any]]) -> None:
    """Atomic-ish replace: write to .tmp then rename."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    tmp.replace(path)


def _append_jsonl(path: Path, row: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(row) + "\n")


def _make_phase_id(slug: str, title: str, existing_ids: List[str]) -> str:
    """Generate a stable phase_id from slug + title + index."""
    n = len(existing_ids) + 1
    short = re.sub(r"[^a-z0-9]+", "-", title.lower())[:40].strip("-")
    return f"{slug}-{n:03d}-{short or 'phase'}"


def enqueue(
    slug: str,
    title: str,
    instructions: str,
    expected_outputs: Optional[List[str]] = None,
    depends_on: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Append a new phase to pending.jsonl."""
    pd = _project_dir(slug)
    pending_path = pd / "pending.jsonl"
    done_path = pd / "done.jsonl"
    blocked_path = pd / "blocked.jsonl"

    all_ids = (
        [r["phase_id"] for r in _read_jsonl(pending_path)]
        + [r["phase_id"] for r in _read_jsonl(done_path)]
        + [r["phase_id"] for r in _read_jsonl(blocked_path)]
    )

    row = {
        "phase_id": _make_phase_id(slug, title, all_ids),
        "title": title.strip(),
        "instructions": instructions.strip(),
        "expected_outputs": list(expected_outputs or []),
        "depends_on": list(depends_on or []),
        "enqueued_at": datetime.now().isoformat(timespec="seconds"),
    }
    _append_jsonl(pending_path, row)
    return row


def _dependencies_satisfied(phase: Dict[str, Any], done_ids: set) -> bool:
    deps = phase.get("depends_on") or []
    return all(d in done_ids for d in deps)


def next_pending(slug: str) -> Optional[Dict[str, Any]]:
    """Return the next phase whose dependencies are all done. FIFO within deps-satisfied."""
    pd = _project_dir(slug)
    pending = _read_jsonl(pd / "pending.jsonl")
    if not pending:
        return None
    done_ids = {r["phase_id"] for r in _read_jsonl(pd / "done.jsonl")}
    for row in pending:
        if _dependencies_satisfied(row, done_ids):
            return row
    # All pending phases are dep-blocked. agent_tick should report this.
    return None


def _remove_from_pending(slug: str, phase_id: str) -> Optional[Dict[str, Any]]:
    pd = _project_dir(slug)
    pending_path = pd / "pending.jsonl"
    pending = _read_jsonl(pending_path)
    removed: Optional[Dict[str, Any]] = None
    remaining = []
    for r in pending:
        if r["phase_id"] == phase_id and removed is None:
            removed = r
        else:
            remaining.append(r)
    if removed:
        _write_jsonl(pending_path, remaining)
    return removed


def mark_done(slug: str, phase_id: str, outcome: Dict[str, Any]) -> Dict[str, Any]:
    """Move a phase from pending → done with an outcome summary."""
    phase = _remove_from_pending(slug, phase_id)
    if not phase:
        raise ValueError(f"phase {phase_id!r} not in pending queue for {slug}")
    phase["outcome"] = {
        **outcome,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
    }
    _append_jsonl(_project_dir(slug) / "done.jsonl", phase)
    return phase


def mark_blocked(slug: str, phase_id: str, reason: str) -> Dict[str, Any]:
    """Move a phase from pending → blocked with a reason."""
    phase = _remove_from_pending(slug, phase_id)
    if not phase:
        raise ValueError(f"phase {phase_id!r} not in pending queue for {slug}")
    phase["blocked_reason"] = reason
    phase["blocked_at"] = datetime.now().isoformat(timespec="seconds")
    _append_jsonl(_project_dir(slug) / "blocked.jsonl", phase)
    return phase


def unblock(slug: str, phase_id: str) -> Dict[str, Any]:
    """Move a phase from blocked → pending (user resolved the ambiguity)."""
    pd = _project_dir(slug)
    blocked_path = pd / "blocked.jsonl"
    blocked = _read_jsonl(blocked_path)
    target: Optional[Dict[str, Any]] = None
    remaining = []
    for r in blocked:
        if r["phase_id"] == phase_id and target is None:
            target = r
        else:
            remaining.append(r)
    if not target:
        raise ValueError(f"phase {phase_id!r} not in blocked queue for {slug}")
    # Strip the block-specific fields before re-enqueueing
    target.pop("blocked_reason", None)
    target.pop("blocked_at", None)
    target["unblocked_at"] = datetime.now().isoformat(timespec="seconds")
    _write_jsonl(blocked_path, remaining)
    _append_jsonl(pd / "pending.jsonl", target)
    return target


def list_queue(slug: str) -> Dict[str, List[Dict[str, Any]]]:
    """Snapshot of all three queues for a project."""
    pd = _project_dir(slug)
    return {
        "pending": _read_jsonl(pd / "pending.jsonl"),
        "blocked": _read_jsonl(pd / "blocked.jsonl"),
        "done": _read_jsonl(pd / "done.jsonl"),
    }


# ─── CLI ────────────────────────────────────────────────────────
def _cmd_enqueue(args):
    row = enqueue(
        slug=args.slug,
        title=args.title,
        instructions=args.instructions,
        expected_outputs=args.expected_output,
        depends_on=args.depends_on,
    )
    print(f"Enqueued: {row['phase_id']}")
    print(f"  Title:        {row['title']}")
    print(f"  Instructions: {row['instructions']}")
    if row["expected_outputs"]:
        print(f"  Expected:     {row['expected_outputs']}")
    if row["depends_on"]:
        print(f"  Depends on:   {row['depends_on']}")


def _cmd_next(args):
    row = next_pending(args.slug)
    if row is None:
        # Check if blocked-on-deps vs empty queue
        all_pending = _read_jsonl(_project_dir(args.slug) / "pending.jsonl")
        if all_pending:
            print("(all pending phases are dep-blocked; nothing executable yet)")
        else:
            print("(pending queue is empty)")
        sys.exit(1)
    print(json.dumps(row, indent=2))


def _cmd_list(args):
    snap = list_queue(args.slug)
    print(f"Project: {args.slug}")
    print(f"  Pending:  {len(snap['pending'])}")
    print(f"  Blocked:  {len(snap['blocked'])}")
    print(f"  Done:     {len(snap['done'])}")
    if args.verbose:
        for state, rows in snap.items():
            print(f"\n── {state.upper()} ──")
            for r in rows:
                print(f"  • {r['phase_id']}  —  {r['title']}")


def _cmd_done(args):
    outcome = {
        "summary": args.summary or "",
        "files": args.file or [],
    }
    if args.composite is not None:
        outcome["composite_score"] = args.composite
    row = mark_done(args.slug, args.phase_id, outcome)
    print(f"Done: {row['phase_id']}")


def _cmd_block(args):
    row = mark_blocked(args.slug, args.phase_id, args.reason)
    print(f"Blocked: {row['phase_id']} — {args.reason}")


def _cmd_unblock(args):
    row = unblock(args.slug, args.phase_id)
    print(f"Unblocked → pending: {row['phase_id']}")


def main():
    parser = argparse.ArgumentParser(
        description="Task Queue — per-project phase persistence for agent_tick",
    )
    sub = parser.add_subparsers(dest="cmd")

    p_enq = sub.add_parser("enqueue", help="Append a new phase to pending")
    p_enq.add_argument("slug")
    p_enq.add_argument("--title", required=True)
    p_enq.add_argument("--instructions", required=True)
    p_enq.add_argument("--expected-output", action="append", default=[])
    p_enq.add_argument("--depends-on", action="append", default=[])
    p_enq.set_defaults(func=_cmd_enqueue)

    p_next = sub.add_parser("next", help="Show the next executable pending phase")
    p_next.add_argument("slug")
    p_next.set_defaults(func=_cmd_next)

    p_list = sub.add_parser("list", help="Show queue snapshot")
    p_list.add_argument("slug")
    p_list.add_argument("--verbose", "-v", action="store_true")
    p_list.set_defaults(func=_cmd_list)

    p_done = sub.add_parser("done", help="Mark a phase done with outcome")
    p_done.add_argument("slug")
    p_done.add_argument("phase_id")
    p_done.add_argument("--summary", default="")
    p_done.add_argument("--file", action="append", default=[])
    p_done.add_argument("--composite", type=float, default=None)
    p_done.set_defaults(func=_cmd_done)

    p_block = sub.add_parser("block", help="Mark a phase blocked on user input")
    p_block.add_argument("slug")
    p_block.add_argument("phase_id")
    p_block.add_argument("--reason", required=True)
    p_block.set_defaults(func=_cmd_block)

    p_unblock = sub.add_parser("unblock", help="Move a blocked phase back to pending")
    p_unblock.add_argument("slug")
    p_unblock.add_argument("phase_id")
    p_unblock.set_defaults(func=_cmd_unblock)

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        return
    try:
        args.func(args)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
