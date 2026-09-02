#!/usr/bin/env python3
"""Bulk task/lane audit and guarded closeout shorthand.

This is a deterministic, stdlib-only control surface. It never talks to the
Codex app, sends messages, commits, merges, pushes, archives, unpins, deletes,
or writes outside explicit report paths. Native task data is supplied as a
JSON snapshot by the Codex app conductor; Git facts are refreshed locally.

Commands:
  audit       Match pinned tasks to live worktree lanes and classify state.
  wave        Select up to eight evidence-backed closeout candidates.
  interpret   Parse the exact guarded phrases used by the global skill.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AUDIT_SCHEMA = "bulk-closeout-audit/v1"
WAVE_SCHEMA = "bulk-closeout-wave/v1"
SHORTHAND_SCHEMA = "closeout-shorthand/v1"

LANE_STATES = {
    "active",
    "awaiting-merge",
    "stale-dirty",
    "conflicted",
    "safely-reclaimable",
}
SAFE_MATCH_CONFIDENCE = {"exact-cwd", "branch-evidence", "high-title-match"}
WORD_RE = re.compile(r"[a-z0-9]+")
CONFLICT_RE = re.compile(
    r"(?im)^(?:changed in both|added in both|removed in (?:local|remote))$|"
    r"\bCONFLICT\b|^<<<<<<< "
)
STOP_TOKENS = {
    "active", "antigravity", "archive", "blocked", "build", "closeout",
    "codex", "content", "creative", "done", "extraction", "google",
    "main", "mid", "ready", "research", "revenue", "session", "system",
    "task", "worktree",
}


class AuditError(RuntimeError):
    pass


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def run(command: list[str], cwd: Path, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    # A worktree can be removed after `git worktree list` but before its lane is
    # inspected. Keep the subprocess launch alive so `git -C <missing-path>`
    # can return an ordinary non-zero result that the audit classifies.
    launch_cwd = cwd if cwd.is_dir() else ROOT
    return subprocess.run(
        command,
        cwd=str(launch_cwd),
        text=True,
        errors="replace",
        capture_output=True,
        timeout=timeout,
    )


def git(cwd: Path, *args: str, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    return run(["git", "-C", str(cwd), *args], cwd, timeout)


def git_text(cwd: Path, *args: str, timeout: int = 60) -> str:
    result = git(cwd, *args, timeout=timeout)
    return result.stdout.strip() if result.returncode == 0 else ""


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AuditError(f"unreadable JSON {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise AuditError(f"JSON root must be an object: {path}")
    return data


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def parse_worktrees(main: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    result = git(main, "worktree", "list", "--porcelain")
    if result.returncode != 0:
        raise AuditError(f"git worktree list failed: {result.stderr.strip()}")
    rows: list[dict[str, str]] = []
    current: dict[str, str] = {}
    for raw in result.stdout.splitlines() + [""]:
        if raw.startswith("worktree "):
            if current:
                rows.append(current)
            current = {"path": raw[len("worktree ") :]}
        elif raw.startswith("branch refs/heads/"):
            current["branch"] = raw[len("branch refs/heads/") :]
        elif raw == "detached":
            current["branch"] = "(detached)"
        elif not raw.strip() and current:
            rows.append(current)
            current = {}
    main_resolved = main.resolve()
    linked = [
        {**row, "worktree_linked": True, "registry_status": None}
        for row in rows
        if row.get("branch") and Path(row["path"]).resolve() != main_resolved
    ]
    by_branch = {row["branch"]: row for row in linked}
    registry_path = main / ".agent" / "lanes.json"
    registry_orphans: list[dict[str, Any]] = []
    try:
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        registry = {}
    if isinstance(registry, dict):
        for branch, metadata in registry.items():
            metadata = metadata if isinstance(metadata, dict) else {}
            if not branch or branch == "?":
                registry_orphans.append({"branch": branch or "?", **metadata})
                continue
            if branch in by_branch:
                by_branch[branch]["registry_status"] = metadata.get("status")
                continue
            if git(main, "show-ref", "--verify", f"refs/heads/{branch}").returncode != 0:
                registry_orphans.append({"branch": branch, **metadata, "reason": "branch ref missing"})
                continue
            row = {
                "branch": branch,
                "path": str(metadata.get("path") or ""),
                "worktree_linked": False,
                "registry_status": metadata.get("status"),
            }
            linked.append(row)
            by_branch[branch] = row
    return linked, registry_orphans


def dirty_paths(path: Path) -> list[str]:
    output = git_text(path, "status", "--porcelain", "--untracked-files=all")
    paths: list[str] = []
    for line in output.splitlines():
        if len(line) < 4:
            continue
        value = line[3:].strip()
        if " -> " in value:
            value = value.split(" -> ", 1)[1]
        paths.append(value)
    return paths


def merge_conflicts(main: Path, branch: str, ahead: int) -> tuple[bool | None, str]:
    if ahead <= 0:
        return False, "no branch-only commits"
    base = git_text(main, "merge-base", "main", branch)
    if not base:
        return None, "merge base unavailable"
    result = git(main, "merge-tree", base, "main", branch, timeout=120)
    if result.returncode != 0:
        return None, f"merge-tree probe failed: {result.stderr.strip() or result.returncode}"
    conflict = bool(CONFLICT_RE.search(result.stdout))
    return conflict, "fresh merge-tree conflict signal" if conflict else "fresh merge-tree clean"


def lane_fact(main: Path, row: dict[str, Any], stale_days: int) -> dict[str, Any]:
    raw_path = str(row.get("path") or "")
    path = Path(raw_path).resolve() if raw_path else None
    branch = row["branch"]
    linked = bool(row.get("worktree_linked"))
    dirty = dirty_paths(path) if linked and path else []
    counts = git_text(main, "rev-list", "--left-right", "--count", f"main...{branch}")
    try:
        behind, ahead = (int(value) for value in counts.split())
    except (TypeError, ValueError):
        behind, ahead = -1, -1
    merged = git(main, "merge-base", "--is-ancestor", branch, "main").returncode == 0
    head = git_text(main, "rev-parse", branch)
    last_epoch_text = git_text(main, "log", "-1", "--format=%ct", branch)
    try:
        last_epoch = int(last_epoch_text)
        age_days = round(max(0.0, (time.time() - last_epoch) / 86400), 1)
    except ValueError:
        last_epoch, age_days = 0, None
    conflict, conflict_reason = merge_conflicts(main, branch, max(ahead, 0))

    if conflict is True:
        state = "conflicted"
    elif linked and dirty and age_days is not None and age_days >= stale_days:
        state = "stale-dirty"
    elif linked and dirty:
        state = "active"
    elif merged or ahead == 0:
        state = "safely-reclaimable"
    else:
        state = "awaiting-merge"

    return {
        "branch": branch,
        "path": str(path) if path else "",
        "worktree_linked": linked,
        "registry_status": row.get("registry_status"),
        "head": head,
        "dirty_count": len(dirty) if linked else None,
        "dirty_paths": dirty[:20],
        "ahead_of_main": ahead,
        "behind_main": behind,
        "merged_into_main": merged,
        "merge_conflict": conflict,
        "merge_probe": conflict_reason,
        "last_commit_epoch": last_epoch,
        "age_days": age_days,
        "state": state,
    }


def tokens(value: str) -> set[str]:
    return {
        token for token in WORD_RE.findall((value or "").lower())
        if len(token) >= 3 and token not in STOP_TOKENS
    }


def branch_tokens(branch: str) -> set[str]:
    value = re.sub(r"^(?:codex/|claude/|worktree-)", "", branch)
    return tokens(value)


def task_match(task: dict[str, Any], lanes: list[dict[str, Any]]) -> dict[str, Any]:
    cwd = str(task.get("cwd") or "")
    mentions = {str(value).lower() for value in task.get("branch_mentions", [])}
    evidence = " ".join(
        str(task.get(key) or "") for key in ("title", "summary", "last_agent_excerpt")
    )
    evidence_tokens = tokens(evidence)

    exact = [
        lane for lane in lanes
        if cwd and lane.get("path") and Path(cwd).resolve() == Path(lane["path"]).resolve()
    ]
    if len(exact) == 1:
        return {"branch": exact[0]["branch"], "confidence": "exact-cwd", "reason": "task cwd equals lane path"}
    mentioned = [lane for lane in lanes if lane["branch"].lower() in mentions]
    if len(mentioned) == 1:
        return {"branch": mentioned[0]["branch"], "confidence": "branch-evidence", "reason": "task history names branch"}

    scored: list[tuple[float, int, dict[str, Any]]] = []
    for lane in lanes:
        bt = branch_tokens(lane["branch"])
        if not bt:
            continue
        shared = len(bt & evidence_tokens)
        coverage = shared / len(bt)
        if shared >= 2:
            scored.append((coverage, shared, lane))
    scored.sort(key=lambda item: (item[0], item[1]), reverse=True)
    if not scored:
        return {"branch": None, "confidence": "unmatched", "reason": "no exact or two-token lane evidence"}
    best_coverage, best_shared, best_lane = scored[0]
    tied = [row for row in scored if row[0] == best_coverage and row[1] == best_shared]
    if len(tied) > 1:
        return {
            "branch": None,
            "confidence": "ambiguous",
            "reason": "multiple lanes share the same title-token score",
            "candidates": [row[2]["branch"] for row in tied[:6]],
        }
    confidence = "high-title-match" if best_coverage >= 0.75 else "probable-title-match"
    return {
        "branch": best_lane["branch"],
        "confidence": confidence,
        "reason": f"title/history covers {best_shared}/{len(branch_tokens(best_lane['branch']))} lane tokens",
    }


def requested_status_for(state: str) -> str:
    return {
        "active": "active",
        "stale-dirty": "mid-build",
        "conflicted": "blocked",
        "awaiting-merge": "ready",
        "safely-reclaimable": "done-candidate",
    }[state]


def build_audit(main: Path, snapshot: dict[str, Any], stale_days: int) -> dict[str, Any]:
    tasks = snapshot.get("tasks")
    if not isinstance(tasks, list):
        raise AuditError("task snapshot requires a tasks list")
    lane_rows, registry_orphans = parse_worktrees(main)
    lanes = [lane_fact(main, row, stale_days) for row in lane_rows]
    lane_by_branch = {lane["branch"]: lane for lane in lanes}
    mapped_tasks: list[dict[str, Any]] = []
    claimed: dict[str, list[str]] = {}
    for task in tasks:
        match = task_match(task, lanes)
        lane = lane_by_branch.get(match.get("branch"))
        state = lane["state"] if lane else "unconfirmed"
        if lane:
            claimed.setdefault(lane["branch"], []).append(str(task.get("id")))
        mapped_tasks.append({
            **task,
            "match": match,
            "lane_state": state,
            "requested_closeout_status": requested_status_for(state) if state in LANE_STATES else "unconfirmed",
        })
    for lane in lanes:
        lane["task_ids"] = claimed.get(lane["branch"], [])
        lane["task_count"] = len(lane["task_ids"])

    task_counts: dict[str, int] = {}
    for task in mapped_tasks:
        task_counts[task["lane_state"]] = task_counts.get(task["lane_state"], 0) + 1
    lane_counts: dict[str, int] = {}
    for lane in lanes:
        lane_counts[lane["state"]] = lane_counts.get(lane["state"], 0) + 1

    return {
        "schema_version": AUDIT_SCHEMA,
        "generated_at": now_iso(),
        "main": str(main),
        "main_head": git_text(main, "rev-parse", "main"),
        "origin_main": git_text(main, "rev-parse", "origin/main"),
        "main_status": git_text(main, "status", "--short", "--branch"),
        "safety": {
            "read_only_source_scan": True,
            "messages_sent": 0,
            "commits": 0,
            "merges": 0,
            "pushes": 0,
            "archives": 0,
            "deletions": 0,
        },
        "summary": {
            "tasks": len(mapped_tasks),
            "lanes": len(lanes),
            "task_states": dict(sorted(task_counts.items())),
            "lane_states": dict(sorted(lane_counts.items())),
            "tasks_unconfirmed": task_counts.get("unconfirmed", 0),
            "lanes_without_task_match": sum(1 for lane in lanes if not lane["task_ids"]),
            "linked_worktrees": sum(1 for lane in lanes if lane["worktree_linked"]),
            "registry_only_lanes": sum(1 for lane in lanes if not lane["worktree_linked"]),
            "registry_orphans": len(registry_orphans),
        },
        "tasks": mapped_tasks,
        "lanes": lanes,
        "registry_orphans": registry_orphans,
    }


def markdown_report(audit: dict[str, Any]) -> str:
    summary = audit["summary"]
    lines = [
        "# Bulk Closeout Audit",
        "",
        f"Generated: `{audit['generated_at']}`",
        "",
        "This is a read-only evidence map. `done-candidate` is not permission to archive; only a valid end-session coordinator receipt can authorize that action.",
        "",
        "## Summary",
        "",
        f"- Pinned Antigravity Codex tasks: **{summary['tasks']}**",
        f"- Lane records with valid branch identity: **{summary['lanes']}**",
        f"- Linked worktrees: **{summary['linked_worktrees']}**; registry-only lanes: **{summary['registry_only_lanes']}**",
        f"- Registry entries without a valid branch identity: **{summary['registry_orphans']}**",
        f"- Tasks without a defensible lane match: **{summary['tasks_unconfirmed']}**",
        f"- Lanes without a pinned-task match: **{summary['lanes_without_task_match']}**",
        f"- Main: `{audit['main_status']}`",
        "",
        "### Lane states",
        "",
    ]
    for state, count in summary["lane_states"].items():
        lines.append(f"- `{state}`: {count}")
    lines += [
        "",
        "## Task-to-lane map",
        "",
        "| Task | Match | Lane | State | Closeout status |",
        "|---|---|---|---|---|",
    ]
    for task in audit["tasks"]:
        title = str(task.get("title") or "Untitled").replace("|", "\\|")
        match = task["match"]
        lines.append(
            f"| {title} | {match['confidence']} | `{match.get('branch') or 'UNCONFIRMED'}` | "
            f"{task['lane_state']} | {task['requested_closeout_status']} |"
        )
    lines += [
        "",
        "## Lane inventory",
        "",
        "| Lane | Linked | State | Dirty | Ahead | Behind | Conflict | Matched tasks |",
        "|---|---|---|---:|---:|---:|---|---:|",
    ]
    for lane in audit["lanes"]:
        conflict = "UNKNOWN" if lane["merge_conflict"] is None else ("yes" if lane["merge_conflict"] else "no")
        lines.append(
            f"| `{lane['branch']}` | {'yes' if lane['worktree_linked'] else 'registry-only'} | {lane['state']} | {lane['dirty_count'] if lane['dirty_count'] is not None else '?'} | "
            f"{lane['ahead_of_main']} | {lane['behind_main']} | {conflict} | {lane['task_count']} |"
        )
    lines += [
        "",
        "## Safety boundary",
        "",
        "- No task message, commit, merge, push, archive, unpin, deletion, or global write occurred during this audit.",
        "- `close ready` preserves and closes as `ready`; it never archives or merges main.",
        "- `close done` requests proof. If integration or coordinator proof is absent, it must remain unarchived and downgrade to `ready`, `blocked`, or `mid-build`.",
        "- `bulk closeout audit` is read-only. Dispatch requires a separate approved wave action.",
        "- Bare `ready` and `done` are status words, never commands.",
        "",
    ]
    return "\n".join(lines)


def build_wave(audit: dict[str, Any], limit: int) -> dict[str, Any]:
    if audit.get("schema_version") != AUDIT_SCHEMA:
        raise AuditError("wave requires a bulk-closeout-audit/v1 report")
    state_rank = {"safely-reclaimable": 0, "awaiting-merge": 1, "conflicted": 2, "stale-dirty": 3}
    candidates = []
    for task in audit["tasks"]:
        confidence = task.get("match", {}).get("confidence")
        state = task.get("lane_state")
        if confidence not in SAFE_MATCH_CONFIDENCE or state not in state_rank:
            continue
        candidates.append(task)
    candidates.sort(key=lambda task: (
        state_rank[task["lane_state"]],
        0 if task.get("closeout_receipt_seen") else 1,
        0 if task.get("end_session_invoked") else 1,
        task.get("updated_at") or 0,
        task.get("title") or "",
    ))
    selected = candidates[:limit]
    prompt = (
        "Run the guarded closeout for this existing task. Inspect its exact lane and preserve all unfinished work. "
        "Do not merge or push main; do not archive, unpin, delete, or edit global files. Run the canonical /end-session "
        "handoff and verification path only when safe. Report task status (active, blocked, ready, mid-build, or done), "
        "lane/branch, dirty paths, unique commits, handoff verification, coordinator receipt, and requested native task actions. "
        "A title or prior claim is not proof. If done is not proven, keep the task unarchived."
    )
    return {
        "schema_version": WAVE_SCHEMA,
        "generated_at": now_iso(),
        "limit": limit,
        "selected_count": len(selected),
        "selection_rule": "exact/evidence/high-title match; non-active lane; safest states first",
        "dispatch_prompt": prompt,
        "safety": {
            "merge_main": False,
            "push_main": False,
            "archive": False,
            "unpin": False,
            "delete": False,
            "global_write": False,
        },
        "tasks": [
            {
                "id": task["id"],
                "title": task["title"],
                "branch": task["match"]["branch"],
                "match_confidence": task["match"]["confidence"],
                "lane_state": task["lane_state"],
                "requested_closeout_status": task["requested_closeout_status"],
            }
            for task in selected
        ],
    }


def interpret_phrase(raw: str) -> dict[str, Any]:
    phrase = re.sub(r"\s+", " ", raw.strip().lower()).rstrip(".!?")
    common = {
        "schema_version": SHORTHAND_SCHEMA,
        "input": raw,
        "normalized": phrase,
        "recognized": True,
        "bare_status_words_are_commands": False,
    }
    if phrase == "close ready":
        return {
            **common,
            "action": "end-session",
            "requested_status": "ready",
            "read_only": False,
            "require_handoff_verify": True,
            "require_coordinator_receipt": True,
            "merge_main": False,
            "archive": False,
            "fail_closed_status": "ready",
        }
    if phrase == "close done":
        return {
            **common,
            "action": "end-session-verify-done",
            "requested_status": "done",
            "read_only": False,
            "require_handoff_verify": True,
            "require_coordinator_receipt": True,
            "require_integration_proof": True,
            "merge_main": False,
            "archive": "only when task_actions.archive is true",
            "fail_closed_status": "ready-or-blocked",
        }
    if phrase == "bulk closeout audit":
        return {
            **common,
            "action": "bulk-audit",
            "requested_status": None,
            "read_only": True,
            "messages": 0,
            "commits": 0,
            "merges": 0,
            "pushes": 0,
            "archives": 0,
            "deletions": 0,
        }
    return {
        **common,
        "recognized": False,
        "action": None,
        "reason": "only the exact guarded phrases trigger lifecycle behavior; bare ready/done remain ordinary language",
    }


def cmd_audit(args: argparse.Namespace) -> int:
    main = Path(args.main).expanduser().resolve()
    snapshot = load_json(Path(args.tasks).expanduser().resolve())
    audit = build_audit(main, snapshot, args.stale_days)
    if args.output_json:
        write_json(Path(args.output_json).expanduser().resolve(), audit)
    if args.output_md:
        path = Path(args.output_md).expanduser().resolve()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown_report(audit), encoding="utf-8")
    print(json.dumps(audit if args.json else audit["summary"], indent=2, sort_keys=True))
    return 0


def cmd_wave(args: argparse.Namespace) -> int:
    audit = load_json(Path(args.audit).expanduser().resolve())
    wave = build_wave(audit, args.limit)
    if args.output:
        write_json(Path(args.output).expanduser().resolve(), wave)
    print(json.dumps(wave, indent=2, sort_keys=True))
    return 0 if wave["selected_count"] == args.limit else 3


def cmd_interpret(args: argparse.Namespace) -> int:
    result = interpret_phrase(args.phrase)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["recognized"] else 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    audit = sub.add_parser("audit", help="Build a fresh read-only task/lane map.")
    audit.add_argument("--tasks", required=True, help="Codex app task snapshot JSON.")
    audit.add_argument("--main", default=str(ROOT), help="Main checkout path.")
    audit.add_argument("--stale-days", type=int, default=7)
    audit.add_argument("--output-json")
    audit.add_argument("--output-md")
    audit.add_argument("--json", action="store_true", help="Print the full audit instead of summary.")
    audit.set_defaults(func=cmd_audit)

    wave = sub.add_parser("wave", help="Select a receipt-safe closeout wave.")
    wave.add_argument("--audit", required=True)
    wave.add_argument("--limit", type=int, default=8, choices=range(1, 9))
    wave.add_argument("--output")
    wave.set_defaults(func=cmd_wave)

    interpret = sub.add_parser("interpret", help="Interpret an exact guarded closeout phrase.")
    interpret.add_argument("phrase")
    interpret.set_defaults(func=cmd_interpret)

    args = parser.parse_args()
    try:
        return args.func(args)
    except AuditError as exc:
        print(f"BULK CLOSEOUT CONTROL FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
