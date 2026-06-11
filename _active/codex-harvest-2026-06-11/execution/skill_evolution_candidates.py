#!/usr/bin/env python3
"""Local-first Skill Evolution candidate helper.

This script ranks possible /skill-evolution targets without creating variants
or mutating skill workflows. It keeps the intelligence layer current so the
operator sees "ready", "watchlist", and "blocked" targets without manually
inspecting performance logs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AGENT_DIR = ROOT / ".agent"
SKILLS_DIR = ROOT / "skills"
LIVE_SKILLS_DIR = ROOT / ".agents" / "skills"
COLD_WRAPPERS_DIR = ROOT / ".agents" / "cold-skills" / "source-command-wrappers"
PERFORMANCE_LOG = AGENT_DIR / "performance-log.jsonl"
PERFORMANCE_INBOX = AGENT_DIR / "performance-log-inbox.jsonl"
GROUND_TRUTH_MANIFEST = ROOT / "evolution_store" / "ground_truth" / "manifest.json"
TRACE_DIR = ROOT / "evolution_store" / "v2_traces"
QUEUE_DIR = ROOT / "evolution_store" / "queue"
TRACE_REPORT_DIR = ROOT / "evolution_store" / "traces"
SNAPSHOT_PATH = QUEUE_DIR / "skill_evolution_candidates.json"

MIN_READY_ENTRIES = 3
WEAK_QUALITY_THRESHOLD = 7.0
WEAK_DIMENSION_THRESHOLD = 7.0
TRACE_WINDOW_DAYS = 7


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def stable_id(*parts: str) -> str:
    payload = "|".join(str(part).strip().lower() for part in parts if str(part).strip())
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()[:16]


def safe_float(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    try:
        if value in ("", None):
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except json.JSONDecodeError:
        return {}


def skill_names_from_field(value: str) -> list[str]:
    names = [part.strip() for part in str(value or "").split(",")]
    return [name for name in names if name]


def root_skill_inventory(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    skills_dir = root / "skills"
    inventory: dict[str, dict[str, Any]] = {}
    if not skills_dir.exists():
        return inventory
    for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        workflow_dir = skill_dir / "workflows"
        workflows = []
        if workflow_dir.exists():
            workflows = sorted(
                path.stem
                for path in workflow_dir.glob("*.md")
                if not path.name.endswith(".variant.md")
            )
        inventory[skill_dir.name] = {
            "skill": skill_dir.name,
            "root_exists": True,
            "has_skill_md": (skill_dir / "SKILL.md").exists(),
            "has_genius": (skill_dir / "genius.md").exists(),
            "workflow_count": len(workflows),
            "workflows": workflows,
        }
    return inventory


def load_grounded_skills(root: Path = ROOT) -> set[str]:
    manifest = read_json(root / "evolution_store" / "ground_truth" / "manifest.json")
    grounded: set[str] = set()
    for sample in manifest.get("samples", []):
        if sample.get("skill"):
            grounded.add(str(sample["skill"]))
    return grounded


def load_recent_trace_metrics(root: Path = ROOT, days: int = TRACE_WINDOW_DAYS) -> dict[str, dict[str, Any]]:
    trace_dir = root / "evolution_store" / "v2_traces"
    if not trace_dir.exists():
        return {}
    cutoff = datetime.now() - timedelta(days=days)
    grouped: dict[str, list[float]] = defaultdict(list)
    for path in trace_dir.glob("trace_*.json"):
        try:
            if datetime.fromtimestamp(path.stat().st_mtime) < cutoff:
                continue
            row = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        skill = str(row.get("component") or row.get("skill") or row.get("expert") or "")
        score = safe_float((row.get("quality") or {}).get("composite"))
        if skill and score is not None:
            grouped[skill].append(score)
    return {
        skill: {
            "trace_count_7d": len(scores),
            "trace_mean_7d": round(sum(scores) / len(scores), 2),
            "trace_low_count_7d": sum(1 for score in scores if score < WEAK_QUALITY_THRESHOLD),
        }
        for skill, scores in grouped.items()
    }


def local_performance_by_skill(root: Path = ROOT) -> tuple[dict[str, list[dict[str, Any]]], list[dict[str, Any]]]:
    entries = read_jsonl(root / ".agent" / "performance-log.jsonl")
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in entries:
        for skill in skill_names_from_field(str(row.get("Skill") or "")):
            grouped[skill].append(row)
    return grouped, entries


def performance_inbox_rows(root: Path = ROOT) -> list[dict[str, Any]]:
    return read_jsonl(root / ".agent" / "performance-log-inbox.jsonl")


def is_command_wrapper_only(skill: str, root: Path = ROOT) -> bool:
    return (
        skill.startswith("source-command-")
        or (root / ".agents" / "skills" / f"source-command-{skill}").exists()
        or (root / ".agents" / "cold-skills" / "source-command-wrappers" / f"source-command-{skill}").exists()
    )


def is_closeout_like(row: dict[str, Any]) -> bool:
    haystack = " ".join(
        str(row.get(key, ""))
        for key in ["Output", "output", "Title", "title", "Workflow", "workflow", "Notes", "notes", "Registration Source", "registration_source"]
    ).lower()
    return any(term in haystack for term in ["session closeout", "closeout intelligence", "activation governor plan", "recurring report"])


def verifier_backed_failure(rows: list[dict[str, Any]]) -> bool:
    for row in rows:
        source = str(row.get("Source Artifact") or row.get("source_artifact") or "")
        notes = str(row.get("Notes") or row.get("notes") or "").lower()
        status = str(row.get("Status") or row.get("status") or "").lower()
        quality = safe_float(row.get("Quality Score") or row.get("quality_score"))
        verifier_source = "execution/verify_" in source or "verify_" in source
        failure_language = any(term in notes for term in ["fail", "failure", "regression", "misroute", "blocked"])
        weak_score = quality is not None and quality < WEAK_QUALITY_THRESHOLD
        if verifier_source and (failure_language or weak_score or status in {"discard", "needs improvement"}):
            return True
    return False


def analyze_entries(rows: list[dict[str, Any]], valid_workflows: set[str]) -> dict[str, Any]:
    rows_sorted = sorted(rows, key=lambda row: (str(row.get("Date") or ""), str(row.get("Timestamp") or "")), reverse=True)
    quality = [score for score in (safe_float(row.get("Quality Score")) for row in rows_sorted) if score is not None]
    intent = [score for score in (safe_float(row.get("Intent Alignment")) for row in rows_sorted) if score is not None]
    expert = [score for score in (safe_float(row.get("Expert Standard")) for row in rows_sorted) if score is not None]
    adversarial = [score for score in (safe_float(row.get("Adversarial Resilience")) for row in rows_sorted) if score is not None]

    trend = "no_data"
    if len(quality) >= 4:
        mid = len(quality) // 2
        recent = sum(quality[:mid]) / mid
        older = sum(quality[mid:]) / (len(quality) - mid)
        delta = recent - older
        trend = "declining" if delta < -0.5 else "improving" if delta > 0.5 else "stable"
    elif quality:
        trend = "insufficient_data"

    workflow_scores: dict[str, list[float]] = defaultdict(list)
    for row in rows_sorted:
        workflow = str(row.get("Workflow") or "")
        score = safe_float(row.get("Quality Score"))
        if workflow in valid_workflows and score is not None:
            workflow_scores[workflow].append(score)

    weakest_workflow = ""
    weakest_workflow_score = 0.0
    if workflow_scores:
        weakest_workflow = min(workflow_scores, key=lambda name: sum(workflow_scores[name]) / len(workflow_scores[name]))
        weakest_workflow_score = round(sum(workflow_scores[weakest_workflow]) / len(workflow_scores[weakest_workflow]), 2)

    dimension_scores = {
        "Intent Alignment": round(sum(intent) / len(intent), 2) if intent else 0.0,
        "Expert Standard": round(sum(expert) / len(expert), 2) if expert else 0.0,
        "Adversarial Resilience": round(sum(adversarial) / len(adversarial), 2) if adversarial else 0.0,
    }
    nonzero_dimensions = {name: score for name, score in dimension_scores.items() if score > 0}
    weakest_dimension = min(nonzero_dimensions, key=nonzero_dimensions.get) if nonzero_dimensions else ""
    weakest_dimension_score = dimension_scores.get(weakest_dimension, 0.0)

    latest = rows_sorted[0] if rows_sorted else {}
    return {
        "entries": len(rows),
        "scored_entries": len(quality),
        "avg_quality": round(sum(quality) / len(quality), 2) if quality else 0.0,
        "avg_intent": dimension_scores["Intent Alignment"],
        "avg_expert": dimension_scores["Expert Standard"],
        "avg_adversarial": dimension_scores["Adversarial Resilience"],
        "trend": trend,
        "latest_date": str(latest.get("Date") or str(latest.get("Timestamp") or "")[:10] or ""),
        "weakest_dimension": weakest_dimension,
        "weakest_dimension_score": weakest_dimension_score,
        "weakest_workflow": weakest_workflow,
        "weakest_workflow_score": weakest_workflow_score,
        "verifier_backed_failure": verifier_backed_failure(rows),
    }


def priority_score(stats: dict[str, Any], grounded: bool) -> float:
    score = 0.0
    if stats.get("verifier_backed_failure"):
        score += 100.0
    avg_quality = safe_float(stats.get("avg_quality")) or 0.0
    weakest_dimension_score = safe_float(stats.get("weakest_dimension_score")) or 0.0
    if avg_quality:
        score += max(0.0, 10.0 - avg_quality) * 10.0
    if weakest_dimension_score:
        score += max(0.0, 10.0 - weakest_dimension_score) * 8.0
    if stats.get("trend") == "declining":
        score += 15.0
    score += min(int(stats.get("scored_entries") or 0), 10)
    if stats.get("latest_date") == date.today().isoformat():
        score += 3.0
    if grounded:
        score += 3.0
    return round(score, 2)


def candidate_for_skill(
    skill: str,
    inventory: dict[str, dict[str, Any]],
    grouped: dict[str, list[dict[str, Any]]],
    trace_metrics: dict[str, dict[str, Any]],
    grounded: set[str],
    root: Path = ROOT,
) -> dict[str, Any]:
    info = inventory.get(skill)
    rows = grouped.get(skill, [])
    trace = trace_metrics.get(skill, {})
    is_grounded = skill in grounded

    if not info:
        reason = "command-wrapper-only or missing root skill" if is_command_wrapper_only(skill, root) else "missing root skill"
        return {
            "candidate_id": stable_id("blocked", skill, reason),
            "state": "blocked",
            "skill": skill,
            "reason": reason,
            "priority_score": 0,
            "evidence_count": len(rows),
            "grounded": is_grounded,
            "recommended_action": "Keep as command/workflow evidence, or create a root skill before evolution.",
        }

    valid_workflows = set(info.get("workflows", []))
    if not valid_workflows:
        return {
            "candidate_id": stable_id("blocked", skill, "missing workflows"),
            "state": "blocked",
            "skill": skill,
            "reason": "root skill has no workflow files",
            "priority_score": 0,
            "evidence_count": len(rows),
            "grounded": is_grounded,
            "recommended_action": "Add a workflow before running a variant cycle.",
        }

    stats = analyze_entries(rows, valid_workflows)
    stats.update(trace)
    score = priority_score(stats, is_grounded)
    target = stats.get("weakest_workflow") or stats.get("weakest_dimension") or "collect-evidence"
    weakness = (
        stats.get("avg_quality", 0) and stats.get("avg_quality", 0) < WEAK_QUALITY_THRESHOLD
    ) or (
        stats.get("weakest_dimension_score", 0) and stats.get("weakest_dimension_score", 0) < WEAK_DIMENSION_THRESHOLD
    ) or stats.get("trend") == "declining" or bool(stats.get("verifier_backed_failure"))

    if (stats["scored_entries"] >= MIN_READY_ENTRIES or stats["verifier_backed_failure"]) and weakness:
        state = "ready"
        reason = "verifier-backed failure evidence" if stats["verifier_backed_failure"] else "local evidence shows weakness or regression"
        action = f"Run `/skill-evolution {skill}` targeting {target}."
    else:
        state = "watchlist"
        if stats["scored_entries"] == 0:
            reason = "needs scored local performance evidence"
        elif stats["scored_entries"] < MIN_READY_ENTRIES:
            reason = f"needs {MIN_READY_ENTRIES - stats['scored_entries']} more scored local entries"
        else:
            reason = "no actionable weakness detected"
        action = "Keep logging real outputs; do not mutate yet."

    return {
        "candidate_id": stable_id(state, skill, str(target)),
        "state": state,
        "skill": skill,
        "target": target,
        "reason": reason,
        "priority_score": score,
        "evidence_count": stats["entries"],
        "scored_entries": stats["scored_entries"],
        "grounded": is_grounded,
        "workflow_count": info.get("workflow_count", 0),
        "has_genius": bool(info.get("has_genius")),
        "metrics": stats,
        "recommended_action": action,
    }


def blocked_inbox_rows(root: Path = ROOT) -> list[dict[str, Any]]:
    blocked = []
    for row in performance_inbox_rows(root):
        draft_id = str(row.get("draft_id") or row.get("Local ID") or stable_id(json.dumps(row, sort_keys=True)))
        reason = "closeout-only inbox draft" if is_closeout_like(row) else "review-only inbox draft"
        blocked.append({
            "candidate_id": stable_id("blocked-inbox", draft_id),
            "state": "blocked",
            "skill": str(row.get("skill") or row.get("Skill") or row.get("workflow") or row.get("Workflow") or "inbox-draft"),
            "reason": reason,
            "priority_score": 0,
            "evidence_count": 0,
            "grounded": False,
            "draft_id": draft_id,
            "recommended_action": "Do not use inbox drafts as evolution evidence until promoted by the evidence gate.",
        })
    return blocked


def build_snapshot(root: Path = ROOT) -> dict[str, Any]:
    inventory = root_skill_inventory(root)
    grouped, perf_entries = local_performance_by_skill(root)
    traces = load_recent_trace_metrics(root)
    grounded = load_grounded_skills(root)

    skill_names = set(inventory) | set(grouped) | set(traces)
    candidates = [
        candidate_for_skill(skill, inventory, grouped, traces, grounded, root)
        for skill in sorted(skill_names)
    ]
    candidates.extend(blocked_inbox_rows(root))

    ready = sorted([row for row in candidates if row["state"] == "ready"], key=lambda row: (-row["priority_score"], row["skill"]))
    watchlist = sorted([row for row in candidates if row["state"] == "watchlist"], key=lambda row: (-row["priority_score"], row["skill"]))
    blocked = sorted([row for row in candidates if row["state"] == "blocked"], key=lambda row: (row["reason"], row["skill"]))

    summary = {
        "ready": len(ready),
        "watchlist": len(watchlist),
        "blocked": len(blocked),
        "total_candidates": len(candidates),
        "root_skills": len(inventory),
        "local_performance_entries": len(perf_entries),
        "grounded_skills": len(grounded),
        "inbox_drafts_excluded": len(performance_inbox_rows(root)),
    }

    return {
        "generated_at": now_iso(),
        "summary": summary,
        "ready_candidates": ready,
        "watchlist": watchlist,
        "blocked": blocked,
        "top_recommendation": ready[0] if ready else (watchlist[0] if watchlist else None),
        "source_counts": {
            "performance_log": len(perf_entries),
            "performance_inbox": len(performance_inbox_rows(root)),
            "root_skills": len(inventory),
            "trace_skills_7d": len(traces),
            "grounded_skills": len(grounded),
        },
    }


def render_snapshot(snapshot: dict[str, Any], limit: int = 10) -> str:
    summary = snapshot.get("summary", {})
    lines = [
        "# Skill Evolution Candidates",
        "",
        f"Generated: {snapshot.get('generated_at', '')}",
        "",
        "## Summary",
        "",
        f"- Ready: {summary.get('ready', 0)}",
        f"- Watchlist: {summary.get('watchlist', 0)}",
        f"- Blocked: {summary.get('blocked', 0)}",
        f"- Local performance entries: {summary.get('local_performance_entries', 0)}",
        f"- Inbox drafts excluded: {summary.get('inbox_drafts_excluded', 0)}",
        "",
    ]

    def table(title: str, rows: list[dict[str, Any]]) -> None:
        lines.extend([f"## {title}", ""])
        if not rows:
            lines.extend(["- none", ""])
            return
        lines.append("| Skill | Score | Evidence | Target | Reason |")
        lines.append("|---|---:|---:|---|---|")
        for row in rows[:limit]:
            lines.append(
                f"| `{row.get('skill', '')}` | {row.get('priority_score', 0)} | "
                f"{row.get('scored_entries', row.get('evidence_count', 0))} | "
                f"{row.get('target', '') or '-'} | {row.get('reason', '')} |"
            )
        if len(rows) > limit:
            lines.append(f"| ... | ... | ... | ... | {len(rows) - limit} more omitted |")
        lines.append("")

    table("Ready Candidates", snapshot.get("ready_candidates", []))
    table("Watchlist", snapshot.get("watchlist", []))

    blocked = snapshot.get("blocked", [])
    reason_counts = Counter(row.get("reason", "unknown") for row in blocked)
    lines.extend(["## Blocked Summary", ""])
    if reason_counts:
        for reason, count in reason_counts.most_common():
            lines.append(f"- {reason}: {count}")
    else:
        lines.append("- none")
    lines.append("")

    top = snapshot.get("top_recommendation")
    lines.extend(["## Top Recommendation", ""])
    if top:
        lines.append(f"- `{top.get('skill')}` ({top.get('state')}): {top.get('recommended_action')}")
    else:
        lines.append("- No candidates found.")
    lines.append("")
    return "\n".join(lines)


def write_outputs(snapshot: dict[str, Any], root: Path = ROOT) -> tuple[Path, Path]:
    snapshot_path = root / "evolution_store" / "queue" / "skill_evolution_candidates.json"
    report_path = root / "evolution_store" / "traces" / f"skill_evolution_candidates_{date.today().isoformat()}.md"
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    report_path.write_text(render_snapshot(snapshot), encoding="utf-8")
    return snapshot_path, report_path


def load_snapshot(root: Path = ROOT) -> dict[str, Any]:
    return read_json(root / "evolution_store" / "queue" / "skill_evolution_candidates.json")


def compact_status(snapshot: dict[str, Any]) -> str:
    if not snapshot:
        return "No skill evolution candidate snapshot found."
    summary = snapshot.get("summary", {})
    top = snapshot.get("top_recommendation") or {}
    top_text = f" top={top.get('skill')} ({top.get('state')})" if top else ""
    return (
        f"ready={summary.get('ready', 0)} watchlist={summary.get('watchlist', 0)} "
        f"blocked={summary.get('blocked', 0)}{top_text}"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Local-first Skill Evolution candidate helper")
    sub = parser.add_subparsers(dest="command")

    scan = sub.add_parser("scan", help="Scan local evidence and rank evolution candidates")
    scan.add_argument("--write", action="store_true", help="Write snapshot and daily candidate report")
    scan.add_argument("--json", action="store_true", help="Print JSON snapshot")
    scan.add_argument("--limit", type=int, default=10, help="Rows to show per rendered section")

    status = sub.add_parser("status", help="Show current candidate snapshot summary")
    status.add_argument("--json", action="store_true", help="Print JSON snapshot")

    args = parser.parse_args()

    if args.command == "scan":
        snapshot = build_snapshot()
        if args.write:
            snapshot_path, report_path = write_outputs(snapshot)
            snapshot["written"] = {"snapshot": str(snapshot_path), "report": str(report_path)}
        if args.json:
            print(json.dumps(snapshot, indent=2, ensure_ascii=False))
        else:
            print(render_snapshot(snapshot, limit=args.limit))
        return 0

    if args.command == "status":
        snapshot = load_snapshot()
        if not snapshot:
            snapshot = build_snapshot()
        if args.json:
            print(json.dumps(snapshot, indent=2, ensure_ascii=False))
        else:
            print("# Skill Evolution Candidate Status")
            print()
            print(compact_status(snapshot))
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
