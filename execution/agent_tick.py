#!/usr/bin/env python3
"""
Agent Tick — Multi-day autonomous wake handler (Phase D / 2026-05-25).

The wake-and-advance loop for long-running projects. Reads project state
+ task queue + sovereign memory; identifies the next executable phase;
writes a wake-report to `_active/_ledgers/`; (v1.1) optionally fires the
phase via autopilot.

CRITICAL safety rules (per directives/agent-tick-protocol.md):
1. ONE PHASE PER TICK. Never auto-execute multiple phases in a single wake.
2. BLOCK ON AMBIGUITY. If the next phase needs a taste call or branching
   choice, halt — write to blocked.jsonl, do not improvise.
3. EXPLICIT OPT-IN. A project does NOT get a launchd tick unless the user
   runs `agent_tick.py enable --project <slug>`.
4. STATE.YAML IS SOURCE OF TRUTH. Missing/corrupted → exit with error.
   Do not "recover" or guess.
5. NO SURPRISE COST. Per-project daily cost ceiling enforced (when paid
   APIs would be invoked; v1 just reports estimated cost without firing).

v1 scope (this file): the skeleton + dry-run mode + enable/disable
opt-in CLI. The wake-report tells the user (or v1.1 automation) what
WOULD execute on this tick; actual chain execution requires explicit
invocation.

v1.1 (deferred): --execute mode that fires the phase via autopilot,
captures outcome, calls task_queue.mark_done.

CLI:
    python3 execution/agent_tick.py enable --project <slug> [--schedule daily|hourly|<cron>]
    python3 execution/agent_tick.py disable --project <slug>
    python3 execution/agent_tick.py run --project <slug> [--execute]
    python3 execution/agent_tick.py status [--project <slug>]
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).parent.parent

# Make sibling execution/ modules importable whether this file is invoked
# as a script (`python3 execution/agent_tick.py ...`) or imported as a
# module from project root.
_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))

import task_queue as tq  # noqa: E402  (path tweak intentionally precedes)

PROJECTS_DIR = ROOT / "projects"
ENABLED_REGISTRY = ROOT / ".agent" / "agent-tick-enabled.json"
LEDGER_OUT_DIR = ROOT / "_active" / "_ledgers"
LAUNCHD_DIR = Path.home() / "Library" / "LaunchAgents"
LAUNCHD_TEMPLATE_NAME = "com.antigravity.agent-tick.{slug}.plist"


def _load_enabled() -> Dict[str, Any]:
    if not ENABLED_REGISTRY.exists():
        return {}
    try:
        return json.loads(ENABLED_REGISTRY.read_text())
    except Exception:
        return {}


def _save_enabled(data: Dict[str, Any]) -> None:
    ENABLED_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    ENABLED_REGISTRY.write_text(json.dumps(data, indent=2))


def _project_state_path(slug: str) -> Path:
    """state.yaml for the project (managed by anchor_memory.py)."""
    return PROJECTS_DIR / slug / "state.yaml"


def _load_state_yaml(slug: str) -> Optional[str]:
    """Read raw state.yaml text. Returns None if missing.

    We don't parse YAML here — anchor_memory owns the schema. agent_tick
    just needs to know IF state exists. Full parse happens via
    `anchor_memory.py load <slug>` (subprocess call in v1.1).
    """
    p = _project_state_path(slug)
    if not p.exists():
        return None
    try:
        return p.read_text()
    except Exception:
        return None


def _sovereign_memory_brief(slug: str, top_k: int = 5) -> str:
    """Best-effort one-line summary of sovereign memory hits for this project.

    Defers actual retrieval to memory_retrieve.py (subprocess). Returns a
    short string for the wake-report — full memory injection happens at
    execution time, not in the wake-report itself.
    """
    return (
        f"(sovereign memory will be loaded at execution time via "
        f"`python3 execution/memory_retrieve.py \"<phase-instructions>\" "
        f"--top {top_k}`; not pre-loaded into wake-report to save tokens)"
    )


def _write_wake_report(slug: str, content: str) -> Path:
    LEDGER_OUT_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_path = LEDGER_OUT_DIR / f"agent-tick-{slug}-{date_str}.md"
    out_path.write_text(content)
    return out_path


# ─── Public actions ─────────────────────────────────────────────

def enable_project(slug: str, schedule: str = "daily") -> Dict[str, Any]:
    """Register a project for autonomous ticks. Does NOT install launchd yet —
    that's a separate, more invasive step (writes to ~/Library/LaunchAgents).
    """
    if not _project_state_path(slug).exists():
        raise ValueError(
            f"projects/{slug}/state.yaml does not exist. "
            f"Initialize via `anchor_memory.py init <slug>` first."
        )

    enabled = _load_enabled()
    enabled[slug] = {
        "enabled_at": datetime.now().isoformat(timespec="seconds"),
        "schedule": schedule,
        "ticks_executed": 0,
        "last_tick_at": None,
        "last_tick_outcome": None,
    }
    _save_enabled(enabled)

    # Hint about launchd installation (do NOT auto-install — too invasive)
    plist_name = LAUNCHD_TEMPLATE_NAME.format(slug=slug)
    return {
        "slug": slug,
        "schedule": schedule,
        "registry": str(ENABLED_REGISTRY),
        "launchd_hint": (
            f"To install daily wake on macOS, copy the template at "
            f"`directives/agent-tick-protocol.md` (Appendix A) to "
            f"~/Library/LaunchAgents/{plist_name}, then "
            f"`launchctl load ~/Library/LaunchAgents/{plist_name}`. "
            f"This is intentionally manual — auto-installing launchd jobs "
            f"is too invasive for a default action."
        ),
    }


def disable_project(slug: str) -> Dict[str, Any]:
    enabled = _load_enabled()
    if slug not in enabled:
        return {"slug": slug, "was_enabled": False}
    removed = enabled.pop(slug)
    _save_enabled(enabled)

    plist_path = LAUNCHD_DIR / LAUNCHD_TEMPLATE_NAME.format(slug=slug)
    return {
        "slug": slug,
        "was_enabled": True,
        "previous_config": removed,
        "launchd_hint": (
            f"If you previously installed the launchd job, also run "
            f"`launchctl unload {plist_path}` and delete the plist."
        ),
    }


def run_tick(slug: str, execute: bool = False) -> Dict[str, Any]:
    """One tick = at most one phase advance.

    v1 default (execute=False): identify next phase, write wake-report,
    exit. User reviews and fires via autopilot manually.

    v1.1 (execute=True): NOT YET IMPLEMENTED. Will fire the phase via
    autopilot and call task_queue.mark_done. For now, --execute prints a
    deferred-implementation notice and exits.
    """
    # 1) State must exist
    state_text = _load_state_yaml(slug)
    if state_text is None:
        raise ValueError(
            f"projects/{slug}/state.yaml not found — tick aborted. "
            f"Initialize project state first (`anchor_memory.py init {slug}`)."
        )

    # 2) Project must be opted-in
    enabled = _load_enabled()
    if slug not in enabled:
        raise ValueError(
            f"Project {slug!r} is NOT opted in to agent_tick. "
            f"Enable first: `agent_tick.py enable --project {slug}`."
        )

    # 3) Find next phase
    next_phase = tq.next_pending(slug)
    queue_snap = tq.list_queue(slug)

    # 4) Build wake-report
    now = datetime.now().isoformat(timespec="seconds")
    tick_n = enabled[slug].get("ticks_executed", 0) + 1
    lines: List[str] = []
    lines.append(f"# Agent Tick — {slug} — tick #{tick_n}")
    lines.append("")
    lines.append(f"> Wake time: {now}")
    lines.append(f"> Mode:      {'EXECUTE (v1.1 deferred)' if execute else 'DRY-RUN (v1)'}")
    lines.append("")
    lines.append("## Queue snapshot")
    lines.append(f"- Pending: {len(queue_snap['pending'])}")
    lines.append(f"- Blocked: {len(queue_snap['blocked'])}")
    lines.append(f"- Done:    {len(queue_snap['done'])}")
    lines.append("")

    if next_phase is None:
        if queue_snap["pending"]:
            lines.append("## No executable phase")
            lines.append("All pending phases have unsatisfied dependencies. "
                          "Review depends_on chains:")
            for p in queue_snap["pending"]:
                lines.append(f"- `{p['phase_id']}` depends on: {p.get('depends_on') or '(none — should be next?)'}")
        elif queue_snap["blocked"]:
            lines.append("## All phases blocked")
            for b in queue_snap["blocked"]:
                lines.append(f"- `{b['phase_id']}` — reason: {b.get('blocked_reason', '(unknown)')}")
            lines.append("")
            lines.append("Resolve via `python3 execution/task_queue.py unblock {slug} <phase_id>`.")
        else:
            lines.append("## Project complete")
            lines.append("No pending or blocked phases. Either the project is done or "
                          "enqueue more phases via `task_queue.py enqueue`.")
        lines.append("")
        report_path = _write_wake_report(slug, "\n".join(lines))
        return {
            "slug": slug,
            "tick": tick_n,
            "next_phase": None,
            "wake_report": str(report_path),
            "action_taken": "none — no executable phase",
        }

    lines.append("## Next phase")
    lines.append(f"**ID**: `{next_phase['phase_id']}`")
    lines.append(f"**Title**: {next_phase['title']}")
    lines.append("")
    lines.append("**Instructions** (what to advance on this tick):")
    lines.append("")
    lines.append(next_phase["instructions"])
    lines.append("")
    if next_phase.get("expected_outputs"):
        lines.append("**Expected outputs**:")
        for o in next_phase["expected_outputs"]:
            lines.append(f"- `{o}`")
        lines.append("")
    lines.append("## Context to load at execution time")
    lines.append(f"- Project state: `projects/{slug}/state.yaml`")
    lines.append(f"- Sovereign memory: {_sovereign_memory_brief(slug)}")
    lines.append("")

    if execute:
        lines.append("## EXECUTE mode (v1.1) — DEFERRED")
        lines.append("Full chain execution is not yet implemented. To advance manually:")
        lines.append("")
        lines.append("```")
        lines.append(f"# 1) Load anchor context")
        lines.append(f"python3 execution/anchor_memory.py load {slug}")
        lines.append(f"")
        lines.append(f"# 2) Load sovereign memory for this phase")
        lines.append(f"python3 execution/memory_retrieve.py \"<phase instructions>\" --top 10")
        lines.append(f"")
        lines.append(f"# 3) Invoke autopilot with the phase instructions")
        lines.append(f"# (autopilot will resolve outcome class and run the right workflow)")
        lines.append(f"")
        lines.append(f"# 4) After completion, mark phase done with outcome")
        lines.append(f"python3 execution/task_queue.py done {slug} {next_phase['phase_id']} \\")
        lines.append(f"    --summary \"<one-line outcome>\" --composite <0-10>")
        lines.append("```")
        action = "wake-report-written (execute mode deferred to v1.1)"
    else:
        lines.append("## DRY-RUN")
        lines.append("This wake-report shows what WOULD execute. To proceed manually:")
        lines.append("")
        lines.append("```")
        lines.append("# Review the phase, then fire via autopilot:")
        lines.append(f"/autopilot \"{next_phase['title']}\"")
        lines.append("")
        lines.append("# After completion, mark done:")
        lines.append(f"python3 execution/task_queue.py done {slug} {next_phase['phase_id']} \\")
        lines.append(f"    --summary \"<outcome>\" --composite <0-10>")
        lines.append("```")
        action = "wake-report-written (dry-run)"

    # 5) Update enabled registry
    enabled[slug]["last_tick_at"] = now
    enabled[slug]["ticks_executed"] = tick_n
    enabled[slug]["last_tick_outcome"] = action
    _save_enabled(enabled)

    report_path = _write_wake_report(slug, "\n".join(lines))
    return {
        "slug": slug,
        "tick": tick_n,
        "next_phase": next_phase["phase_id"],
        "wake_report": str(report_path),
        "action_taken": action,
    }


def status(slug: Optional[str] = None) -> Dict[str, Any]:
    """Show opt-in registry status."""
    enabled = _load_enabled()
    if slug:
        if slug not in enabled:
            return {"slug": slug, "enabled": False}
        info = dict(enabled[slug])
        info["slug"] = slug
        info["enabled"] = True
        # Add queue snapshot if state exists
        try:
            snap = tq.list_queue(slug)
            info["queue"] = {k: len(v) for k, v in snap.items()}
        except Exception:
            info["queue"] = "(no queue dir)"
        return info
    return {
        "enabled_projects": sorted(enabled.keys()),
        "count": len(enabled),
        "registry": str(ENABLED_REGISTRY),
    }


# ─── CLI ────────────────────────────────────────────────────────
def _cmd_enable(args):
    info = enable_project(args.project, args.schedule)
    print(f"Enabled agent_tick for project: {info['slug']}")
    print(f"  Schedule: {info['schedule']}")
    print(f"  Registry: {info['registry']}")
    print("")
    print(info["launchd_hint"])


def _cmd_disable(args):
    info = disable_project(args.project)
    if not info["was_enabled"]:
        print(f"Project {args.project!r} was not in the agent_tick registry.")
        return
    print(f"Disabled agent_tick for project: {info['slug']}")
    print(f"  Ticks executed before disable: {info['previous_config'].get('ticks_executed', 0)}")
    print("")
    print(info["launchd_hint"])


def _cmd_run(args):
    out = run_tick(args.project, execute=args.execute)
    print(f"Tick #{out['tick']} for {out['slug']}")
    print(f"  Next phase:  {out['next_phase'] or '(none)'}")
    print(f"  Action:      {out['action_taken']}")
    print(f"  Wake report: {out['wake_report']}")


def _cmd_status(args):
    info = status(args.project)
    print(json.dumps(info, indent=2))


def main():
    parser = argparse.ArgumentParser(
        description="Agent Tick — multi-day autonomous wake handler",
    )
    sub = parser.add_subparsers(dest="cmd")

    p_en = sub.add_parser("enable", help="Opt a project in to autonomous ticks")
    p_en.add_argument("--project", required=True)
    p_en.add_argument("--schedule", default="daily", help="daily | hourly | <cron-string>")
    p_en.set_defaults(func=_cmd_enable)

    p_dis = sub.add_parser("disable", help="Opt a project out of autonomous ticks")
    p_dis.add_argument("--project", required=True)
    p_dis.set_defaults(func=_cmd_disable)

    p_run = sub.add_parser("run", help="Run ONE tick (default: dry-run)")
    p_run.add_argument("--project", required=True)
    p_run.add_argument(
        "--execute", action="store_true",
        help="(v1.1 deferred) Fire the phase via autopilot — currently writes a deferred-notice report",
    )
    p_run.set_defaults(func=_cmd_run)

    p_stat = sub.add_parser("status", help="Show opt-in registry + queue snapshots")
    p_stat.add_argument("--project", default=None)
    p_stat.set_defaults(func=_cmd_status)

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
