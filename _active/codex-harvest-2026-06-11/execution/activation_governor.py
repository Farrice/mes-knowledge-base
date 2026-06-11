#!/usr/bin/env python3
"""Activation Governor for supervised Antigravity system activation.

The governor reads existing local evidence, proposes activation work, and
records only supervised queue/report outputs. It deliberately does not activate
protocols, mark agents as used, or write performance/routing evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXECUTION_DIR = ROOT / "execution"
AGENT_DIR = ROOT / ".agent"
DEFAULT_QUEUE = AGENT_DIR / "activation-governor-queue.jsonl"
DEFAULT_APPLIED = AGENT_DIR / "activation-governor-applied.jsonl"
DEFAULT_REPORT_DIR = AGENT_DIR / "recurring-reports"
PERFORMANCE_TARGET = 20

sys.path.insert(0, str(EXECUTION_DIR))

try:
    import protocol_tracker  # type: ignore
    import routing_intelligence  # type: ignore
    import session_log_registrar  # type: ignore
    import system_health  # type: ignore
    from log_performance import get_local_performance_entries, get_sync_summary  # type: ignore
except Exception as exc:  # noqa: BLE001
    protocol_tracker = None
    routing_intelligence = None
    session_log_registrar = None
    system_health = None
    get_local_performance_entries = None
    get_sync_summary = None
    IMPORT_ERROR = str(exc)
else:
    IMPORT_ERROR = ""


PRIORITY_ORDER = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
FORBIDDEN_AUTOMATION_TERMS = (
    "activate all",
    "mass activate",
    "mark all",
    "mass-mark",
    "auto-commit",
    "auto commit",
    "pretend activated",
)

PROTOCOL_ACTIVATION_CANDIDATES = {
    "agent-loading-protocol.md": {
        "rank": 0,
        "trigger": "selecting or loading expert/skill context",
    },
    "expert_auto_routing.md": {
        "rank": 1,
        "trigger": "domain, ensemble, or expert selection affects the route",
    },
    "slash-command-playbook.md": {
        "rank": 2,
        "trigger": "command/workflow discoverability or what-to-use prompts",
    },
    "verification-agent-protocol.md": {
        "rank": 3,
        "trigger": "finalizing code, system changes, public claims, or factual deliverables",
    },
    "session-end-commit.md": {
        "rank": 4,
        "trigger": "end-session commit checkpoint or explicit commit/wrap-up request",
    },
}


@dataclass
class ActivationItem:
    id: str
    priority: str
    title: str
    source: str
    signal: str
    evidence: str
    proposed_action: str
    risk: str
    command_hint: str = ""
    approval_required: bool = True
    status: str = "queued"
    fingerprint: str = ""


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def now_stamp() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H%M%S")


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def stable_hash(*parts: str, length: int = 12) -> str:
    joined = "|".join(normalize(part) for part in parts if part)
    return hashlib.sha1(joined.encode("utf-8")).hexdigest()[:length]


def safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def resolve_path(value: str | Path, default: Path) -> Path:
    path = Path(value) if value else default
    return path if path.is_absolute() else ROOT / path


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line.strip():
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict):
            rows.append(data)
    return rows


def append_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")


def safe_call(label: str, func: Any, fallback: Any) -> Any:
    try:
        return func()
    except Exception as exc:  # noqa: BLE001
        if isinstance(fallback, dict):
            data = dict(fallback)
            data["error"] = f"{label}: {exc}"
            return data
        return fallback


def local_performance_entries() -> list[dict[str, Any]]:
    if get_local_performance_entries:
        return list(get_local_performance_entries())
    return read_jsonl(AGENT_DIR / "performance-log.jsonl")


def local_sync_summary() -> dict[str, int]:
    if get_sync_summary:
        return dict(get_sync_summary())
    entries = local_performance_entries()
    return {
        "total": len(entries),
        "remote_synced": 0,
        "pending": 0,
        "sync_failed": 0,
        "local_first": len(entries),
    }


def collect_system_health() -> dict[str, Any]:
    if not system_health:
        return {
            "session_state": {"status": "UNKNOWN", "health": "Unknown", "message": IMPORT_ERROR},
            "routing": {"status": "UNKNOWN", "health": "Unknown", "count": 0, "message": IMPORT_ERROR},
            "gap_log": {"status": "UNKNOWN", "health": "Unknown", "count": 0, "message": IMPORT_ERROR},
        }
    return {
        "session_state": safe_call("session state", system_health.check_session_state, {}),
        "routing": safe_call("routing intelligence health", system_health.check_routing_intelligence, {}),
        "gap_log": safe_call("gap log", system_health.check_gap_log, {}),
    }


def collect_protocols() -> dict[str, Any]:
    if not protocol_tracker:
        return {
            "total_protocols": 0,
            "active_protocols": 0,
            "zombie_protocols": 0,
            "never_activated": 0,
            "total_activations": 0,
            "activation_rate": "0%",
            "protocols": [],
            "error": IMPORT_ERROR,
        }
    report = safe_call("protocol audit", protocol_tracker.audit_protocols, {})
    return report if isinstance(report, dict) else {}


def collect_routing() -> dict[str, Any]:
    if routing_intelligence and hasattr(routing_intelligence, "_read_data"):
        data = safe_call("routing data", routing_intelligence._read_data, {})
    else:
        data = read_json(AGENT_DIR / "routing-intelligence.json")
    if not isinstance(data, dict):
        data = {}

    decisions = data.get("routing_decisions", [])
    feedback = data.get("feedback_log", [])
    if not isinstance(decisions, list):
        decisions = []
    if not isinstance(feedback, list):
        feedback = []

    decision_by_id = {
        row.get("routing_id"): row
        for row in decisions
        if isinstance(row, dict) and row.get("routing_id")
    }
    negative_feedback = []
    for row in feedback:
        if not isinstance(row, dict) or row.get("rating") not in {"negative", "mixed"}:
            continue
        decision = decision_by_id.get(row.get("routing_id"), {})
        negative_feedback.append(
            {
                "feedback_id": row.get("feedback_id", ""),
                "routing_id": row.get("routing_id", ""),
                "rating": row.get("rating", ""),
                "correction": row.get("correction") or "",
                "notes": row.get("notes") or "",
                "request": decision.get("request_summary") or "",
                "wrong_workflow": decision.get("workflow_used") or "",
                "domain": decision.get("domain_detected") or "",
            }
        )

    return {
        "decisions": len(decisions),
        "feedback": len(feedback),
        "negative_or_mixed_feedback": negative_feedback,
        "current_month": data.get("current_month", ""),
    }


def collect_registrar() -> dict[str, Any]:
    inbox_path = getattr(session_log_registrar, "INBOX_PATH", AGENT_DIR / "performance-log-inbox.jsonl")
    skipped_path = getattr(session_log_registrar, "SKIPPED_PATH", AGENT_DIR / "performance-log-skipped.jsonl")
    return {
        "inbox_path": safe_rel(Path(inbox_path)),
        "skipped_path": safe_rel(Path(skipped_path)),
        "inbox_count": len(read_jsonl(Path(inbox_path))),
        "skipped_count": len(read_jsonl(Path(skipped_path))),
    }


def collect_signals() -> dict[str, Any]:
    entries = local_performance_entries()
    last_entry = entries[0] if entries else {}
    return {
        "generated_at": now_iso(),
        "performance": {
            "count": len(entries),
            "target": PERFORMANCE_TARGET,
            "last_date": last_entry.get("Date", "Never"),
            "last_output": last_entry.get("Output", ""),
            "sync": local_sync_summary(),
        },
        "system_health": collect_system_health(),
        "protocols": collect_protocols(),
        "routing": collect_routing(),
        "registrar": collect_registrar(),
    }


def item(
    priority: str,
    title: str,
    source: str,
    signal: str,
    evidence: str,
    proposed_action: str,
    risk: str,
    command_hint: str = "",
    id_override: str = "",
) -> ActivationItem:
    fingerprint = stable_hash(title, source, signal, proposed_action)
    return ActivationItem(
        id=id_override or f"ag_{fingerprint}",
        priority=priority,
        title=title,
        source=source,
        signal=signal,
        evidence=evidence,
        proposed_action=proposed_action,
        risk=risk,
        command_hint=command_hint,
        fingerprint=fingerprint,
    )


def top_protocol_attention(protocols: dict[str, Any], limit: int = 5) -> list[dict[str, Any]]:
    rows = protocols.get("protocols", [])
    if not isinstance(rows, list):
        return []
    candidates = [
        row
        for row in rows
        if isinstance(row, dict) and row.get("lifecycle") in {"overdue", "dormant"}
    ]
    candidates.sort(
        key=lambda row: (
            PROTOCOL_ACTIVATION_CANDIDATES.get(str(row.get("file") or ""), {}).get("rank", 99),
            0 if row.get("lifecycle") == "overdue" else 1,
            int(row.get("activation_count") or 0),
            str(row.get("file") or ""),
        )
    )
    return candidates[:limit]


def protocol_activation_summary(rows: list[dict[str, Any]]) -> str:
    parts = []
    for row in rows:
        name = str(row.get("file") or "")
        trigger = PROTOCOL_ACTIVATION_CANDIDATES.get(name, {}).get("trigger", "explicit trigger required")
        parts.append(f"{name} ({trigger})")
    return ", ".join(parts) or "none"


def build_items(signals: dict[str, Any]) -> list[ActivationItem]:
    items: list[ActivationItem] = []
    performance = signals.get("performance", {})
    registrar = signals.get("registrar", {})
    protocols = signals.get("protocols", {})
    routing = signals.get("routing", {})
    health = signals.get("system_health", {})

    perf_count = int(performance.get("count") or 0)
    if perf_count < PERFORMANCE_TARGET:
        remaining = PERFORMANCE_TARGET - perf_count
        inbox_count = int(registrar.get("inbox_count") or 0)
        items.append(
            item(
                "HIGH" if remaining <= 5 else "MEDIUM",
                "Unblock Skill Evolution performance evidence",
                "system_health + session_log_registrar",
                f"{perf_count}/{PERFORMANCE_TARGET} performance entries",
                f"{remaining} more high-signal entries needed; registrar inbox has {inbox_count} drafts.",
                "Review only concrete, outcome-tied registrar drafts or capture the next real session outcome. Use `.agent/templates/performance-log-3-entry-sprint.md` to avoid filler entries.",
                "Low if review stays evidence-based; high if low-signal entries are logged just to hit the threshold.",
                "python3 execution/session_log_registrar.py inbox",
            )
        )

    inbox_count = int(registrar.get("inbox_count") or 0)
    if inbox_count:
        items.append(
            item(
                "MEDIUM",
                "Review registrar inbox before new automation",
                "session_log_registrar inbox",
                f"{inbox_count} inbox drafts",
                f"Uncertain performance candidates are waiting in {registrar.get('inbox_path')}.",
                "Approve, revise, or discard inbox drafts one by one. Keep ambiguous candidates out of committed performance evidence.",
                "Low. This is review work, not automatic logging.",
                "python3 execution/session_log_registrar.py inbox",
            )
        )

    sync = performance.get("sync", {})
    pending = int(sync.get("pending", 0)) + int(sync.get("local_first", 0))
    failed = int(sync.get("sync_failed", 0))
    if pending or failed:
        items.append(
            item(
                "LOW" if not failed else "MEDIUM",
                "Clarify local-first performance sync status",
                "log_performance sync summary",
                f"{pending} pending/local-first, {failed} sync failed",
                "Local JSONL remains the source of truth while remote sync is unavailable or unapproved.",
                "Run a sync dry-run and record whether blockers are network, API, or approval-related. Do not auto-sync external systems.",
                "Medium if external sync is attempted without approval; low for dry-run diagnostics.",
                "python3 execution/log_performance.py sync-pending --dry-run",
            )
        )

    overdue_count = int(protocols.get("overdue_protocols") or protocols.get("zombie_protocols") or 0)
    dormant_count = int(protocols.get("dormant_protocols") or 0)
    attention_count = overdue_count + dormant_count
    if attention_count:
        top = top_protocol_attention(protocols)
        names = protocol_activation_summary(top)
        items.append(
            item(
                "MEDIUM",
                "Triage dormant protocols into a top-five activation plan",
                "protocol_tracker audit",
                f"{overdue_count} overdue and {dormant_count} dormant protocols",
                f"Leverage-ranked candidates: {names}.",
                "Use `.agent/protocol-activation-plan.md` as the supervised trigger list. Do not activate every dormant protocol.",
                "Medium. Wrong trigger wiring adds ceremony and false confidence.",
                "python3 execution/protocol_tracker.py audit",
                id_override="ag_0d77e021d9f1",
            )
        )

    negative_feedback = routing.get("negative_or_mixed_feedback", [])
    if isinstance(negative_feedback, list):
        for row in negative_feedback[-5:]:
            wrong = str(row.get("wrong_workflow") or "unknown-route").strip("/")
            correction = str(row.get("correction") or "needs correction")
            request = str(row.get("request") or row.get("notes") or "unknown request")
            items.append(
                item(
                    "HIGH",
                    f"Repair routed failure: /{wrong}",
                    "routing_intelligence feedback",
                    f"{row.get('rating')} feedback -> {correction}",
                    f"Request: {request[:180]}",
                    "Approve a targeted routing fix or regression guard for this failure class only. Do not change broad defaults without regression proof.",
                    "Medium. Routing fixes can over-correct broad intent if they are not regression tested.",
                    "python3 execution/routing_intelligence.py underperforming",
                )
            )

    if int(routing.get("decisions") or 0) == 0:
        items.append(
            item(
                "HIGH",
                "Start routing evidence capture",
                "routing_intelligence",
                "0 routing decisions",
                "The router has no local evidence to learn from.",
                "Add explicit capture at approved lifecycle points. Do not backfill guessed route decisions.",
                "Medium. Invented routing data would pollute future decisions.",
                "python3 execution/routing_intelligence.py scoreboard",
            )
        )

    session_state = health.get("session_state", {})
    if session_state.get("status") in {"DORMANT", "STALE"}:
        items.append(
            item(
                "MEDIUM",
                "Refresh session state capture",
                "system_health session_state",
                str(session_state.get("status", "UNKNOWN")),
                str(session_state.get("message", "No session state detail.")),
                "Use the next real closeout to refresh session state and verify the registrar sees it.",
                "Low. This is evidence freshness, not repo mutation.",
                "python3 execution/session_log_registrar.py scan",
            )
        )

    routing_health = health.get("routing", {})
    if routing_health.get("status") in {"DORMANT", "ERROR"}:
        items.append(
            item(
                "HIGH",
                "Restore routing intelligence health",
                "system_health routing",
                str(routing_health.get("status", "UNKNOWN")),
                str(routing_health.get("message", "No routing health detail.")),
                "Diagnose the routing evidence file and capture the next explicit route decision after approval.",
                "Medium. Do not manufacture historical routing decisions.",
                "python3 execution/routing_intelligence.py scoreboard",
            )
        )

    gap_health = health.get("gap_log", {})
    if gap_health.get("status") == "DORMANT" and perf_count >= 5:
        items.append(
            item(
                "LOW",
                "Queue gap detection review from real evidence",
                "system_health gap_log",
                str(gap_health.get("status", "UNKNOWN")),
                str(gap_health.get("message", "No gap-log detail.")),
                "Run a gap review only against existing performance/routing evidence; do not invent gaps.",
                "Low. Useful after evidence has accumulated.",
                "python3 execution/gap_analysis.py recommendations",
            )
        )

    items.sort(key=lambda row: (PRIORITY_ORDER.get(row.priority, 9), row.title))
    return items


def item_record(row: ActivationItem, status: str = "queued") -> dict[str, Any]:
    data = asdict(row)
    data["status"] = status
    data["created_at"] = now_iso()
    data["autonomy_boundary"] = (
        "supervised queue/report only; no protocol activation, agent usage marking, "
        "or performance/routing evidence writes"
    )
    return data


def queue_ids(path: Path) -> set[str]:
    return {str(row.get("id")) for row in read_jsonl(path) if row.get("id")}


def applied_ids(path: Path) -> set[str]:
    return {str(row.get("id")) for row in read_jsonl(path) if row.get("id")}


def md_cell(value: Any, limit: int = 140) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    text = text.replace("|", "\\|")
    if len(text) > limit:
        text = text[: limit - 3].rstrip() + "..."
    return text


def render_signal_summary(signals: dict[str, Any]) -> str:
    performance = signals.get("performance", {})
    protocols = signals.get("protocols", {})
    routing = signals.get("routing", {})
    registrar = signals.get("registrar", {})
    health = signals.get("system_health", {})
    sync = performance.get("sync", {})
    return "\n".join(
        [
            "| Signal | Value | Source |",
            "|---|---:|---|",
            f"| Performance entries | {performance.get('count', 0)}/{performance.get('target', PERFORMANCE_TARGET)} | local performance log |",
            f"| Registrar inbox drafts | {registrar.get('inbox_count', 0)} | session_log_registrar |",
            f"| Registrar skipped candidates | {registrar.get('skipped_count', 0)} | session_log_registrar |",
            f"| Pending/local-first sync | {int(sync.get('pending', 0)) + int(sync.get('local_first', 0))} | log_performance |",
            f"| Sync failed | {sync.get('sync_failed', 0)} | log_performance |",
            f"| Protocol lifecycle attention | {protocols.get('overdue_protocols', protocols.get('zombie_protocols', 0))} overdue / {protocols.get('dormant_protocols', 0)} dormant / {protocols.get('cold_source_only_protocols', 0)} cold-source | protocol_tracker |",
            f"| Routing decisions | {routing.get('decisions', 0)} | routing_intelligence |",
            f"| Negative/mixed route feedback | {len(routing.get('negative_or_mixed_feedback', []))} | routing_intelligence |",
            f"| Session state | {md_cell(health.get('session_state', {}).get('status', 'UNKNOWN'))} | system_health |",
            f"| Gap log | {md_cell(health.get('gap_log', {}).get('status', 'UNKNOWN'))} | system_health |",
        ]
    )


def render_items(items: list[ActivationItem], existing: set[str] | None = None) -> str:
    existing = existing or set()
    if not items:
        return "No activation items found."
    lines = [
        "| ID | Priority | Queue State | Title | Evidence | Proposed Action |",
        "|---|---|---|---|---|---|",
    ]
    for row in items:
        state = "already-queued" if row.id in existing else row.status
        lines.append(
            f"| `{row.id}` | {row.priority} | {state} | {md_cell(row.title, 80)} | "
            f"{md_cell(row.evidence, 120)} | {md_cell(row.proposed_action, 160)} |"
        )
    return "\n".join(lines)


def render_report(signals: dict[str, Any], items: list[ActivationItem], existing: set[str] | None = None) -> str:
    return "\n".join(
        [
            "# Activation Governor Plan",
            "",
            f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "",
            "## Autonomy Boundary",
            "",
            "Supervised queue/report only. This worker does not activate protocols, mark agents as used, commit performance entries, or write routing evidence.",
            "",
            "## Local Signals",
            "",
            render_signal_summary(signals),
            "",
            "## Supervised Activation Queue",
            "",
            render_items(items, existing=existing),
            "",
            "## Approval Rule",
            "",
            "Use `apply-approved --approval-id <id>` only after the user approves a specific queued item. Approval records create handoff evidence; the implementation work still stays explicit and reviewable.",
            "",
        ]
    ).strip() + "\n"


def write_plan_outputs(
    signals: dict[str, Any],
    items: list[ActivationItem],
    queue_path: Path,
    report_dir: Path,
) -> tuple[int, int, Path]:
    existing = queue_ids(queue_path)
    new_records = [item_record(row) for row in items if row.id not in existing]
    if new_records:
        append_jsonl(queue_path, new_records)
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"{now_stamp()}-activation-governor-plan.md"
    report_path.write_text(render_report(signals, items, existing=existing), encoding="utf-8")
    return len(new_records), len(items) - len(new_records), report_path


def parse_approval_file(path: Path) -> set[str]:
    if not path.exists():
        raise FileNotFoundError(f"Approval file not found: {path}")
    text = path.read_text(encoding="utf-8", errors="ignore").strip()
    if not text:
        return set()
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return {line.strip() for line in text.splitlines() if line.strip() and not line.strip().startswith("#")}
    if isinstance(data, list):
        ids = set()
        for row in data:
            if isinstance(row, str):
                ids.add(row)
            elif isinstance(row, dict) and row.get("approved", True):
                value = row.get("id") or row.get("approval_id")
                if value:
                    ids.add(str(value))
        return ids
    if isinstance(data, dict):
        values = data.get("approved_ids") or data.get("approval_ids") or data.get("ids") or []
        if isinstance(values, str):
            return {values}
        if isinstance(values, list):
            return {str(value) for value in values}
    return set()


def approval_ids_from_args(args: argparse.Namespace) -> set[str]:
    ids = set(args.approval_id or [])
    if args.approval_file:
        ids.update(parse_approval_file(resolve_path(args.approval_file, Path(args.approval_file))))
    return ids


def render_apply_report(results: list[dict[str, Any]], dry_run: bool) -> str:
    lines = [
        "# Activation Governor Approved Handoff",
        "",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Mode**: {'dry-run' if dry_run else 'write'}",
        "",
        "## Autonomy Boundary",
        "",
        "Approved handoff only. No protocols, agents, routing logs, or performance entries were marked active by this command.",
        "",
        "## Results",
        "",
        "| ID | State | Title | Next Action |",
        "|---|---|---|---|",
    ]
    for row in results:
        lines.append(
            f"| `{row.get('id', '')}` | {row.get('apply_state', '')} | "
            f"{md_cell(row.get('title', ''), 80)} | {md_cell(row.get('proposed_action', ''), 160)} |"
        )
    return "\n".join(lines).strip() + "\n"


def apply_approved(
    approval_ids: set[str],
    queue_path: Path,
    applied_path: Path,
    report_dir: Path,
    dry_run: bool,
) -> tuple[list[dict[str, Any]], Path]:
    queue = read_jsonl(queue_path)
    by_id = {str(row.get("id")): row for row in queue if row.get("id")}
    already = applied_ids(applied_path)
    results: list[dict[str, Any]] = []
    for approval_id in sorted(approval_ids):
        row = dict(by_id.get(approval_id, {"id": approval_id, "title": "Missing queue item"}))
        if approval_id not in by_id:
            row["apply_state"] = "missing"
        elif approval_id in already:
            row["apply_state"] = "already-applied"
        else:
            row["apply_state"] = "would-apply" if dry_run else "applied"
            row["applied_at"] = now_iso()
            row["approval_source"] = "apply-approved"
        results.append(row)

    report_path = report_dir / f"{now_stamp()}-activation-governor-apply.md"
    if not dry_run:
        applied_records = [
            row
            for row in results
            if row.get("apply_state") == "applied"
        ]
        if applied_records:
            append_jsonl(applied_path, applied_records)
        report_dir.mkdir(parents=True, exist_ok=True)
        report_path.write_text(render_apply_report(results, dry_run=False), encoding="utf-8")
    return results, report_path


def verify_items(items: list[ActivationItem]) -> list[str]:
    failures = []
    for row in items:
        if not row.approval_required:
            failures.append(f"{row.id} does not require approval")
        haystack = " ".join([row.title, row.signal, row.evidence, row.proposed_action]).lower()
        for term in FORBIDDEN_AUTOMATION_TERMS:
            if term in haystack:
                failures.append(f"{row.id} contains forbidden automation term: {term}")
        if "do not" not in row.proposed_action.lower() and row.source in {
            "protocol_tracker audit",
            "routing_intelligence feedback",
        }:
            failures.append(f"{row.id} lacks explicit conservative boundary in proposed action")
    return failures


def cmd_scan(args: argparse.Namespace) -> int:
    signals = collect_signals()
    items = build_items(signals)
    print("# Activation Governor Scan\n")
    print("## Local Signals\n")
    print(render_signal_summary(signals))
    print("\n## Candidate Activation Items\n")
    print(render_items(items))
    print("\nNo files were written.")
    return 0


def cmd_plan(args: argparse.Namespace) -> int:
    queue_path = resolve_path(args.queue_path, DEFAULT_QUEUE)
    report_dir = resolve_path(args.report_dir, DEFAULT_REPORT_DIR)
    signals = collect_signals()
    items = build_items(signals)
    existing = queue_ids(queue_path)
    report = render_report(signals, items, existing=existing)
    print(report)
    if args.dry_run:
        print(f"Queue would be appended: {safe_rel(queue_path)}")
        print(f"Report would be written under: {safe_rel(report_dir)}")
        return 0
    new_count, existing_count, report_path = write_plan_outputs(signals, items, queue_path, report_dir)
    print(f"Queued new items: {new_count}")
    print(f"Already queued: {existing_count}")
    print(f"Queue written: {safe_rel(queue_path)}")
    print(f"Report written: {safe_rel(report_path)}")
    return 0


def cmd_apply_approved(args: argparse.Namespace) -> int:
    queue_path = resolve_path(args.queue_path, DEFAULT_QUEUE)
    applied_path = resolve_path(args.applied_path, DEFAULT_APPLIED)
    report_dir = resolve_path(args.report_dir, DEFAULT_REPORT_DIR)
    approvals = approval_ids_from_args(args)
    if not approvals:
        print("No approval IDs supplied. Use --approval-id or --approval-file.")
        return 2
    results, report_path = apply_approved(
        approval_ids=approvals,
        queue_path=queue_path,
        applied_path=applied_path,
        report_dir=report_dir,
        dry_run=args.dry_run,
    )
    print(render_apply_report(results, dry_run=args.dry_run))
    if args.dry_run:
        print(f"Applied log would be appended: {safe_rel(applied_path)}")
        print(f"Report would be written: {safe_rel(report_path)}")
    else:
        print(f"Applied log written: {safe_rel(applied_path)}")
        print(f"Report written: {safe_rel(report_path)}")
    missing = [row for row in results if row.get("apply_state") == "missing"]
    return 1 if missing else 0


def cmd_verify(args: argparse.Namespace) -> int:
    signals = collect_signals()
    items = build_items(signals)
    failures = verify_items(items)
    report = render_report(signals, items)
    required_text = [
        "does not activate protocols",
        "mark agents as used",
        "commit performance entries",
        "write routing evidence",
        "Use `apply-approved --approval-id <id>`",
    ]
    for text in required_text:
        if text not in report:
            failures.append(f"rendered report missing boundary text: {text}")
    if IMPORT_ERROR:
        failures.append(f"dependency import failed: {IMPORT_ERROR}")

    if failures:
        print("ACTIVATION GOVERNOR VERIFICATION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("ACTIVATION GOVERNOR VERIFICATION PASS")
    print(f"- signals collected: performance={signals.get('performance', {}).get('count', 0)} routing={signals.get('routing', {}).get('decisions', 0)}")
    print(f"- activation candidates: {len(items)}")
    print("- dry-run report boundary present")
    print("- no automatic protocol/agent/performance/routing activation paths detected")
    return 0


def add_output_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--queue-path", default=str(DEFAULT_QUEUE), help="Supervised queue JSONL path.")
    parser.add_argument("--report-dir", default=str(DEFAULT_REPORT_DIR), help="Report output directory.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Supervised Activation Governor.")
    sub = parser.add_subparsers(dest="command", required=True)

    scan = sub.add_parser("scan", help="Read local signals and show activation candidates without writing.")
    add_output_args(scan)

    plan = sub.add_parser("plan", help="Create a supervised activation plan.")
    add_output_args(plan)
    plan.add_argument("--dry-run", action="store_true", help="Show plan without writing queue/report outputs.")

    verify = sub.add_parser("verify", help="Verify governor boundaries and candidate safety.")
    add_output_args(verify)

    apply = sub.add_parser("apply-approved", help="Record handoff for explicitly approved queue items.")
    add_output_args(apply)
    apply.add_argument("--applied-path", default=str(DEFAULT_APPLIED), help="Approved handoff JSONL path.")
    apply.add_argument("--approval-id", action="append", default=[], help="Approved activation item ID.")
    apply.add_argument("--approval-file", default="", help="JSON, JSONL, or line-delimited approval IDs.")
    apply.add_argument("--dry-run", action="store_true", help="Show approval handoff without writing.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "scan":
        return cmd_scan(args)
    if args.command == "plan":
        return cmd_plan(args)
    if args.command == "verify":
        return cmd_verify(args)
    if args.command == "apply-approved":
        return cmd_apply_approved(args)
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
