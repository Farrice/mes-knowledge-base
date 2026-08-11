#!/usr/bin/env python3
"""End-session intelligence capture for Codex Antigravity.

This script turns the user's existing /end-session habit into a local-first
feedback loop. It coordinates the existing performance registrar, captures
routing decisions, commits explicit route feedback, inboxes ambiguous signals,
and writes a concise closeout report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


sys.path.insert(0, str(Path(__file__).resolve().parent))
from degrade import degraded  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
AGENT_DIR = ROOT / ".agent"
SESSION_STATE = AGENT_DIR / "session-state.md"
AUTOPILOT_STATE = AGENT_DIR / "autopilot-state.md"
DEFAULT_FEEDBACK_INBOX = AGENT_DIR / "routing-feedback-inbox.jsonl"
DEFAULT_REPORT_DIR = AGENT_DIR / "recurring-reports"
DEFAULT_ROUTING_DATA = AGENT_DIR / "routing-intelligence.json"
DEFAULT_PERFORMANCE_LOG = AGENT_DIR / "performance-log.jsonl"
DEFAULT_PERFORMANCE_INBOX = AGENT_DIR / "performance-log-inbox.jsonl"
DEFAULT_GUARD_LEDGER = AGENT_DIR / "sessions" / "closeout-intelligence-guard.jsonl"
REPORT_RETENTION = 10

CONTROL_ROUTES = {
    "autopilot",
    "system-audit",
    "routing-intelligence",
    "health-check",
    "mission",
    "orchestrate",
    "self-evolve",
    "skill-anneal",
    "source-to-skill-system",
    "knowledge-librarian",
}


@dataclass
class RoutingCandidate:
    request: str
    workflow: str
    confidence: float
    source: str
    evidence: str
    review_state: str = "candidate"
    reason: str = ""
    routing_id: str = ""
    feedback_id: str = ""
    fingerprint: str = ""


@dataclass
class FeedbackCandidate:
    request: str
    wrong_workflow: str
    correct_workflow: str
    rating: str
    confidence: float
    source: str
    evidence: str
    review_state: str = "candidate"
    reason: str = ""
    routing_id: str = ""
    feedback_id: str = ""
    fingerprint: str = ""


@dataclass
class CloseoutResult:
    registrar_output: str = ""
    routing_candidates: list[RoutingCandidate] | None = None
    feedback_candidates: list[FeedbackCandidate] | None = None
    ambiguous_feedback: list[dict] | None = None
    snapshots: dict[str, str] | None = None
    report_path: str = ""
    guard_skipped: bool = False


def read_text(path: Path, max_chars: int = 50000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:max_chars]
    except OSError as e:
        return degraded("", f"session artifact unreadable at {path} — closeout sees it as empty", e)


def append_jsonl(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except json.JSONDecodeError as e:
        return degraded({}, f"corrupt JSON at {path} — treated as empty store", e)


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def stable_fingerprint(*parts: str) -> str:
    normalized = "|".join(normalize(part) for part in parts if part)
    return hashlib.sha1(normalized.encode("utf-8")).hexdigest()[:16]


def section(text: str, name: str) -> str:
    pattern = rf"^## {re.escape(name)}\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else ""


def verification_passed(text: str) -> bool:
    low = text.lower()
    return (
        "-> pass" in low
        or "verification pass" in low
        or "verification\n" in low and "pass" in low
        or "validation passed" in low
        or "golden query" in low and "pass" in low
    )


def active_task(text: str) -> str:
    active = section(text, "Active Task")
    if active:
        return active.splitlines()[0].strip("- ").strip()
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else "Session closeout"


def route_domain(route: str, text: str) -> str:
    low = f"{route} {text}".lower()
    if route in CONTROL_ROUTES or any(term in low for term in ["system", "routing", "autopilot", "control plane"]):
        return "system"
    if any(term in low for term in ["client", "revenue", "sales", "offer"]):
        return "revenue"
    if any(term in low for term in ["content", "post", "newsletter", "copy"]):
        return "content"
    return "unknown"


def parse_current_behavior_routes(text: str, source: str) -> list[RoutingCandidate]:
    candidates: list[RoutingCandidate] = []
    pattern = re.compile(
        r"^\s*[-*]\s*`([^`]+)`\s*(?:->|=>|routes?\s+to)\s*`?/([a-z0-9][a-z0-9-]+)`?",
        re.MULTILINE | re.IGNORECASE,
    )
    for match in pattern.finditer(text):
        request = match.group(1).strip()
        workflow = match.group(2).strip().lstrip("/")
        candidate = RoutingCandidate(
            request=request,
            workflow=workflow,
            confidence=0.92 if verification_passed(text) else 0.72,
            source=source,
            evidence="current behavior route mapping",
            reason="verified route mapping" if verification_passed(text) else "route mapping needs feedback review",
        )
        candidate.fingerprint = stable_fingerprint(candidate.request, candidate.workflow)
        candidates.append(candidate)
    return candidates


def parse_primary_route(text: str, source: str) -> list[RoutingCandidate]:
    patterns = [
        r"\*\*Primary route\*\*:\s*`?/([a-z0-9][a-z0-9-]+)`?",
        r"\*\*Chosen route\*\*:\s*`?/([a-z0-9][a-z0-9-]+)`?",
        r"\*\*Workflow\*\*:\s*`?/([a-z0-9][a-z0-9-]+)`?",
    ]
    candidates: list[RoutingCandidate] = []
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            continue
        workflow = match.group(1).strip().lstrip("/")
        request = active_task(text)
        candidate = RoutingCandidate(
            request=request,
            workflow=workflow,
            confidence=0.86 if verification_passed(text) else 0.66,
            source=source,
            evidence="primary route declaration",
            reason="primary route with verification" if verification_passed(text) else "primary route without explicit verifier",
        )
        candidate.fingerprint = stable_fingerprint(candidate.request, candidate.workflow)
        candidates.append(candidate)
        break
    return candidates


def parse_explicit_misroutes(text: str, source: str) -> list[FeedbackCandidate]:
    candidates: list[FeedbackCandidate] = []
    patterns = [
        re.compile(
            r"Misroute:\s*`([^`]+)`\s+wrong\s+`?/([a-z0-9][a-z0-9-]+)`?\s+correct\s+`?/([a-z0-9][a-z0-9-]+)`?",
            re.IGNORECASE,
        ),
        re.compile(
            r"Wrong route:\s*`([^`]+)`\s+from\s+`?/([a-z0-9][a-z0-9-]+)`?\s+to\s+`?/([a-z0-9][a-z0-9-]+)`?",
            re.IGNORECASE,
        ),
    ]
    for pattern in patterns:
        for match in pattern.finditer(text):
            candidate = FeedbackCandidate(
                request=match.group(1).strip(),
                wrong_workflow=match.group(2).strip().lstrip("/"),
                correct_workflow=match.group(3).strip().lstrip("/"),
                rating="negative",
                confidence=0.96,
                source=source,
                evidence="explicit misroute correction",
                reason="explicit wrong/correct route pair",
            )
            candidate.fingerprint = stable_fingerprint(
                candidate.request,
                candidate.wrong_workflow,
                candidate.correct_workflow,
                candidate.rating,
            )
            candidates.append(candidate)
    return candidates


AMBIGUOUS_FAILURE_TERMS = [
    "not firing",
    "not working",
    "feels broken",
    "felt broken",
    "is broken",
    "are broken",
    "system broke",
    "misroute",
    "misrouted",
    "wrong route",
    "repeating myself",
    "manually put",
    "manual logging",
    "manual feedback",
    "manual routing",
    "remember it",
    "failure mode",
    "failed to",
    "verifier failed",
    "check failed",
    "guard failed",
]

AMBIGUOUS_META_EXCLUSIONS = [
    "ambiguous failure",
    "ambiguous feedback",
    "ambiguous routing failure",
    "failure signal",
    "failure signals",
    "routing feedback needed",
    "explicit route feedback",
    "feedback loop collects",
    "feedback loop",
    "does not auto-evolve",
]


def line_has_ambiguous_failure(line: str) -> bool:
    low = line.lower()
    if any(exclusion in low for exclusion in AMBIGUOUS_META_EXCLUSIONS):
        return False
    return any(term in low for term in AMBIGUOUS_FAILURE_TERMS)


def ambiguous_signal_text(text: str) -> str:
    narrative_sections = [
        "Active Task",
        "Key Findings",
        "Symptoms",
        "Issue Ledger",
        "Remaining Watch Items",
        "Open Questions",
    ]
    chunks = [section(text, name) for name in narrative_sections]
    chunks = [chunk for chunk in chunks if chunk]
    return "\n".join(chunks) if chunks else text


def ambiguous_failure_signal(text: str, source: str) -> list[dict]:
    signal_text = ambiguous_signal_text(text)
    if not any(line_has_ambiguous_failure(line) for line in signal_text.splitlines()):
        return []
    if parse_explicit_misroutes(text, source):
        return []
    excerpt = ""
    for line in signal_text.splitlines():
        if line_has_ambiguous_failure(line):
            excerpt = line.strip("- ").strip()
            break
    request = active_task(text)
    record = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source": source,
        "request": request[:200],
        "rating": "mixed",
        "confidence": 0.48,
        "evidence": excerpt[:500] if excerpt else "failure-like language without explicit route correction",
        "review_state": "inbox",
        "reason": "ambiguous failure signal needs human review before becoming routing feedback",
    }
    record["fingerprint"] = stable_fingerprint(record["request"], record["evidence"], record["source"])
    return [record]


def load_existing_routing(args: argparse.Namespace) -> dict:
    path = Path(args.routing_data_file) if args.routing_data_file else DEFAULT_ROUTING_DATA
    if not path.is_absolute():
        path = ROOT / path
    return read_json(path)


def routing_duplicate(data: dict, request: str, workflow: str) -> str:
    request_norm = normalize(request)
    workflow_norm = workflow.strip().lstrip("/")
    for row in data.get("routing_decisions", []):
        if normalize(row.get("request_summary", "")) == request_norm and row.get("workflow_used") == workflow_norm:
            return row.get("routing_id", "existing routing decision")
    return ""


def feedback_duplicate(data: dict, request: str, wrong: str, correct: str, rating: str) -> str:
    request_norm = normalize(request)
    for feedback in data.get("feedback_log", []):
        if feedback.get("rating") != rating:
            continue
        if feedback.get("correction") != correct:
            continue
        routing_id = feedback.get("routing_id")
        decision = next((row for row in data.get("routing_decisions", []) if row.get("routing_id") == routing_id), {})
        if decision.get("workflow_used") == wrong and normalize(decision.get("request_summary", "")) == request_norm:
            return feedback.get("feedback_id", "existing feedback")
    return ""


def inbox_duplicate(path: Path, fingerprint: str) -> bool:
    return any(row.get("fingerprint") == fingerprint for row in read_jsonl(path))


def routing_module(args: argparse.Namespace):
    if args.routing_data_file:
        os.environ["ANTIGRAVITY_ROUTING_DATA_FILE"] = str(Path(args.routing_data_file))
    import routing_intelligence  # noqa: PLC0415

    return routing_intelligence


def collect_routing_candidates(args: argparse.Namespace) -> tuple[list[RoutingCandidate], list[FeedbackCandidate], list[dict]]:
    state_path = Path(args.state_file) if args.state_file else SESSION_STATE
    autopilot_path = Path(args.autopilot_state_file) if args.autopilot_state_file else AUTOPILOT_STATE
    if not state_path.is_absolute():
        state_path = ROOT / state_path
    if not autopilot_path.is_absolute():
        autopilot_path = ROOT / autopilot_path

    session_text = read_text(state_path)
    # Autopilot state is a per-session enhancement, not a required closeout
    # artifact. Fresh worktree lanes intentionally may not have it.
    autopilot_text = (
        read_text(autopilot_path, max_chars=25000) if autopilot_path.exists() else ""
    )
    combined = "\n\n".join(part for part in [session_text, autopilot_text] if part)

    routing_candidates = []
    routing_candidates.extend(parse_current_behavior_routes(session_text, str(state_path.relative_to(ROOT)) if state_path.is_relative_to(ROOT) else str(state_path)))
    routing_candidates.extend(parse_primary_route(session_text, str(state_path.relative_to(ROOT)) if state_path.is_relative_to(ROOT) else str(state_path)))
    if not routing_candidates:
        routing_candidates.extend(parse_primary_route(autopilot_text, str(autopilot_path.relative_to(ROOT)) if autopilot_path.is_relative_to(ROOT) else str(autopilot_path)))

    feedback_candidates = parse_explicit_misroutes(combined, str(state_path.relative_to(ROOT)) if state_path.is_relative_to(ROOT) else str(state_path))
    ambiguous = ambiguous_failure_signal(combined, str(state_path.relative_to(ROOT)) if state_path.is_relative_to(ROOT) else str(state_path))
    return routing_candidates, feedback_candidates, ambiguous


def commit_routing_candidates(args: argparse.Namespace, candidates: list[RoutingCandidate], dry_run: bool) -> list[RoutingCandidate]:
    data = load_existing_routing(args)
    router = None if dry_run else routing_module(args)
    for candidate in candidates:
        duplicate = routing_duplicate(data, candidate.request, candidate.workflow)
        if duplicate:
            candidate.review_state = "skipped"
            candidate.reason = f"duplicate of {duplicate}"
            continue
        if candidate.confidence < 0.75:
            candidate.review_state = "inbox"
            candidate.reason = "routing candidate lacks verifier-strength confidence"
            continue
        if dry_run:
            candidate.review_state = "would-commit"
            candidate.reason = "dry-run route capture"
            continue
        routing_id = router.log_routing_decision(
            request_summary=candidate.request,
            intent_score=5 if candidate.confidence >= 0.9 else 4,
            domain_detected=route_domain(candidate.workflow, candidate.request),
            experts_deployed=["antigravity-orchestrator"],
            tier_loaded=1,
            mode="output",
            workflow_used=candidate.workflow,
            session_id=args.source,
        )
        candidate.routing_id = routing_id
        if candidate.confidence >= 0.9:
            candidate.feedback_id = router.log_feedback(
                routing_id=routing_id,
                rating="positive",
                session_id=args.source,
                correction="",
                notes=f"End-session auto-feedback: verified route /{candidate.workflow} matched `{candidate.request}`.",
            )
        candidate.review_state = "committed"
        candidate.reason = "route decision captured from end-session evidence"
    return candidates


def commit_feedback_candidates(args: argparse.Namespace, candidates: list[FeedbackCandidate], dry_run: bool) -> list[FeedbackCandidate]:
    data = load_existing_routing(args)
    router = None if dry_run else routing_module(args)
    for candidate in candidates:
        duplicate = feedback_duplicate(
            data,
            candidate.request,
            candidate.wrong_workflow,
            candidate.correct_workflow,
            candidate.rating,
        )
        if duplicate:
            candidate.review_state = "skipped"
            candidate.reason = f"duplicate of {duplicate}"
            continue
        if candidate.confidence < 0.85:
            candidate.review_state = "inbox"
            candidate.reason = "feedback candidate below explicit-confidence threshold"
            continue
        if dry_run:
            candidate.review_state = "would-commit"
            candidate.reason = "dry-run explicit feedback capture"
            continue
        # 2026-07-21: aligned to the reworked routing_intelligence.log_misroute
        # signature (request_summary, wrong_route, correct_route, notes,
        # session_id) — the old kwargs crashed every explicit misroute capture
        # at closeout (found by verify_end_session_intelligence triage).
        routing_id, feedback_id = router.log_misroute(
            request_summary=candidate.request,
            wrong_route=candidate.wrong_workflow,
            correct_route=candidate.correct_workflow,
            notes=f"End-session explicit route correction (rating: {candidate.rating}).",
            session_id=args.source,
        )
        candidate.routing_id = routing_id
        candidate.feedback_id = feedback_id
        candidate.review_state = "committed"
        candidate.reason = "explicit route correction captured"
    return candidates


def commit_ambiguous_feedback(args: argparse.Namespace, rows: list[dict], dry_run: bool) -> list[dict]:
    inbox_path = Path(args.feedback_inbox) if args.feedback_inbox else DEFAULT_FEEDBACK_INBOX
    if not inbox_path.is_absolute():
        inbox_path = ROOT / inbox_path
    for row in rows:
        if inbox_duplicate(inbox_path, row["fingerprint"]):
            row["review_state"] = "skipped"
            row["reason"] = "duplicate inbox item"
            continue
        if dry_run:
            row["review_state"] = "would-inbox"
            continue
        append_jsonl(inbox_path, row)
    return rows


def run_command(label: str, command: list[str], timeout: int = 90) -> tuple[str, str]:
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
        output = completed.stdout.strip()
        prefix = "PASS" if completed.returncode == 0 else f"FAIL ({completed.returncode})"
        return label, f"{prefix}\n{output}"
    except Exception as exc:  # noqa: BLE001
        return label, f"FAIL\n{exc}"


def guard_ledger_path(args: argparse.Namespace) -> Path:
    path = Path(args.guard_file) if getattr(args, "guard_file", "") else DEFAULT_GUARD_LEDGER
    if not path.is_absolute():
        path = ROOT / path
    return path


def closeout_session_id(args: argparse.Namespace) -> str:
    """Stable per-session id for the run guard, mirroring the closeout spine's
    ledger-flag dedup pattern (end_session_closeout.py memory-ledger keys):
    harness session id when provided, else a fingerprint of session-state
    content + date — the same close re-run produces the same id."""
    env_id = os.environ.get("CLAUDE_SESSION_ID", "").strip()
    if env_id:
        return env_id
    state_path = Path(args.state_file) if args.state_file else SESSION_STATE
    if not state_path.is_absolute():
        state_path = ROOT / state_path
    state_text = read_text(state_path, max_chars=20000)
    return stable_fingerprint(state_text or args.source, datetime.now().date().isoformat())


def guard_already_ran(args: argparse.Namespace, session_id: str) -> bool:
    return any(row.get("session_id") == session_id for row in read_jsonl(guard_ledger_path(args)))


def guard_record(args: argparse.Namespace, session_id: str) -> None:
    try:
        append_jsonl(
            guard_ledger_path(args),
            {"session_id": session_id, "ts": datetime.now(timezone.utc).isoformat(), "source": args.source},
        )
    except Exception as e:  # noqa: BLE001 — guard bookkeeping must never break closeout
        degraded(None, "guard-ledger append failed — same session may re-run closeout undetected", e)


def run_registrar(args: argparse.Namespace, dry_run: bool) -> str:
    if args.skip_registrar:
        return "SKIPPED by flag."
    command = [
        sys.executable,
        "execution/session_log_registrar.py",
        "--source",
        args.source,
        "register",
    ]
    if dry_run:
        command.append("--dry-run")
    _, output = run_command("Session Registrar", command)
    return output


def collect_snapshots(args: argparse.Namespace) -> dict[str, str]:
    if args.skip_snapshots:
        return {"Snapshots": "SKIPPED by flag."}
    commands = [
        ("Health Check", [sys.executable, "execution/system_health.py", "--quick"]),
        ("Skill Evolution Candidates", [sys.executable, "execution/skill_evolution_candidates.py", "status"]),
        ("Protocol Audit", [sys.executable, "execution/protocol_tracker.py", "audit"]),
        ("Routing Scoreboard", [sys.executable, "execution/routing_intelligence.py", "scoreboard"]),
        ("Registrar Status", [sys.executable, "execution/session_log_registrar.py", "status"]),
        ("Conversation Index Stats", [sys.executable, "execution/conversation_index.py", "stats"]),
    ]
    return dict(run_command(label, command) for label, command in commands)


def count_performance(path: Path = DEFAULT_PERFORMANCE_LOG) -> int:
    return len(read_jsonl(path))


def count_performance_inbox(path: Path = DEFAULT_PERFORMANCE_INBOX) -> int:
    return len(read_jsonl(path))


def routing_counts(path: Path = DEFAULT_ROUTING_DATA) -> tuple[int, int]:
    data = read_json(path)
    return len(data.get("routing_decisions", [])), len(data.get("feedback_log", []))


def latest_report(report_dir: Path = DEFAULT_REPORT_DIR) -> str:
    if not report_dir.exists():
        return ""
    reports = sorted(report_dir.glob("*session-closeout-intelligence.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not reports:
        return ""
    try:
        return str(reports[0].relative_to(ROOT))
    except ValueError:
        return str(reports[0])


def render_table_routing(candidates: Iterable[RoutingCandidate]) -> str:
    rows = list(candidates)
    if not rows:
        return "No routing candidates found."
    lines = ["| State | Confidence | Workflow | Request | Reason |", "|---|---:|---|---|---|"]
    for row in rows:
        lines.append(f"| {row.review_state} | {row.confidence:.2f} | /{row.workflow} | {row.request[:80]} | {row.reason} |")
    return "\n".join(lines)


def render_table_feedback(candidates: Iterable[FeedbackCandidate]) -> str:
    rows = list(candidates)
    if not rows:
        return "No explicit route feedback candidates found."
    lines = ["| State | Rating | Wrong | Correct | Request | Reason |", "|---|---|---|---|---|---|"]
    for row in rows:
        lines.append(
            f"| {row.review_state} | {row.rating} | /{row.wrong_workflow} | /{row.correct_workflow} | {row.request[:80]} | {row.reason} |"
        )
    return "\n".join(lines)


def render_ambiguous(rows: Iterable[dict]) -> str:
    values = list(rows)
    if not values:
        return "No ambiguous feedback signals found."
    lines = ["| State | Confidence | Request | Evidence | Reason |", "|---|---:|---|---|---|"]
    for row in values:
        lines.append(
            f"| {row.get('review_state')} | {row.get('confidence', 0):.2f} | {row.get('request', '')[:80]} | {row.get('evidence', '')[:100]} | {row.get('reason', '')} |"
        )
    return "\n".join(lines)


def render_report(result: CloseoutResult, dry_run: bool) -> str:
    snapshots = result.snapshots or {}
    content = [
        "# Session Closeout Intelligence",
        "",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Mode**: {'dry-run' if dry_run else 'write'}",
        "",
        "## Performance Registrar",
        "",
        f"```text\n{result.registrar_output.strip() or 'No output.'}\n```",
        "",
        "## Routing Decisions",
        "",
        render_table_routing(result.routing_candidates or []),
        "",
        "## Explicit Route Feedback",
        "",
        render_table_feedback(result.feedback_candidates or []),
        "",
        "## Ambiguous Feedback Inbox",
        "",
        render_ambiguous(result.ambiguous_feedback or []),
        "",
        "## Snapshots",
        "",
    ]
    for label, output in snapshots.items():
        # 2026-07-21 report-bloat fix: one 200-char summary line per tool
        # instead of six 4000-char embedded outputs.
        lines = [ln.strip() for ln in output.splitlines() if ln.strip()]
        status = lines[0] if lines else "(no output)"
        detail = next((ln for ln in lines[1:] if not ln.startswith("#")), "")
        summary = f"{status} — {detail}" if detail else status
        content.append(f"- **{label}**: {summary[:200]}")
    content.append("")
    return "\n".join(content).strip() + "\n"


def write_report(content: str, args: argparse.Namespace, dry_run: bool) -> str:
    report_dir = Path(args.report_dir) if args.report_dir else DEFAULT_REPORT_DIR
    if not report_dir.is_absolute():
        report_dir = ROOT / report_dir
    path = report_dir / f"{datetime.now().strftime('%Y-%m-%dT%H%M%S')}-session-closeout-intelligence.md"
    if dry_run:
        return str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path)
    report_dir.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path)


def prune_reports(args: argparse.Namespace, keep: int = REPORT_RETENTION) -> None:
    """Retention sweep: keep the newest `keep` closeout reports, move older
    ones to `<report-dir>/archive/`. Deterministic and fail-soft — a pruning
    error must never break closeout."""
    try:
        report_dir = Path(args.report_dir) if args.report_dir else DEFAULT_REPORT_DIR
        if not report_dir.is_absolute():
            report_dir = ROOT / report_dir
        reports = sorted(
            report_dir.glob("*-session-closeout-intelligence.md"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )
        if len(reports) <= keep:
            return
        archive_dir = report_dir / "archive"
        archive_dir.mkdir(parents=True, exist_ok=True)
        for old in reports[keep:]:
            try:
                old.rename(archive_dir / old.name)
            except OSError:
                continue
    except Exception as e:  # noqa: BLE001 — fail-soft by design
        degraded(None, "report pruning failed — old closeout reports left unarchived", e)


def perform_closeout(args: argparse.Namespace, dry_run: bool) -> CloseoutResult:
    session_id = closeout_session_id(args)
    force = bool(getattr(args, "force", False))
    guard_hit = (not force) and guard_already_ran(args, session_id)

    routing_candidates, feedback_candidates, ambiguous = collect_routing_candidates(args)
    registrar_output = run_registrar(args, dry_run)
    routing_results = commit_routing_candidates(args, routing_candidates, dry_run)
    feedback_results = commit_feedback_candidates(args, feedback_candidates, dry_run)
    ambiguous_results = commit_ambiguous_feedback(args, ambiguous, dry_run)

    if guard_hit:
        # Per-session run guard (2026-07-21): the same close re-invoked must not
        # regenerate 6 snapshots + a fresh report every time. Capture above is
        # already idempotent; snapshots + report are skipped here.
        print(
            f"Closeout intelligence already ran this session (guard: {session_id}) — "
            "skipping snapshots + report. Use --force to regenerate."
        )
        return CloseoutResult(
            registrar_output=registrar_output,
            routing_candidates=routing_results,
            feedback_candidates=feedback_results,
            ambiguous_feedback=ambiguous_results,
            snapshots={"Snapshots": f"SKIPPED — already ran this session (guard: {session_id})."},
            guard_skipped=True,
        )

    snapshots = collect_snapshots(args)
    result = CloseoutResult(
        registrar_output=registrar_output,
        routing_candidates=routing_results,
        feedback_candidates=feedback_results,
        ambiguous_feedback=ambiguous_results,
        snapshots=snapshots,
    )
    report = render_report(result, dry_run)
    result.report_path = write_report(report, args, dry_run)
    if not dry_run:
        guard_record(args, session_id)
        if not getattr(args, "no_prune", False):
            prune_reports(args)
    return result


def cmd_scan(args: argparse.Namespace) -> int:
    routing_candidates, feedback_candidates, ambiguous = collect_routing_candidates(args)
    print("# Session Closeout Intelligence Scan\n")
    print("## Routing Decisions\n")
    print(render_table_routing(routing_candidates))
    print("\n## Explicit Route Feedback\n")
    print(render_table_feedback(feedback_candidates))
    print("\n## Ambiguous Feedback\n")
    print(render_ambiguous(ambiguous))
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    result = perform_closeout(args, args.dry_run)
    if result.guard_skipped:
        return 0  # guard line already printed by perform_closeout
    report = render_report(result, args.dry_run)
    print(report)
    print(f"Report {'would be written' if args.dry_run else 'written'}: {result.report_path}")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    routing_path = Path(args.routing_data_file) if args.routing_data_file else DEFAULT_ROUTING_DATA
    feedback_inbox = Path(args.feedback_inbox) if args.feedback_inbox else DEFAULT_FEEDBACK_INBOX
    report_dir = Path(args.report_dir) if args.report_dir else DEFAULT_REPORT_DIR
    if not routing_path.is_absolute():
        routing_path = ROOT / routing_path
    if not feedback_inbox.is_absolute():
        feedback_inbox = ROOT / feedback_inbox
    if not report_dir.is_absolute():
        report_dir = ROOT / report_dir
    decisions, feedback = routing_counts(routing_path)
    print("# Session Closeout Intelligence Status\n")
    print(f"- Performance entries: {count_performance()}")
    print(f"- Performance inbox drafts: {count_performance_inbox()}")
    print(f"- Routing decisions: {decisions}")
    print(f"- Routing feedback entries: {feedback}")
    print(f"- Routing feedback inbox: {len(read_jsonl(feedback_inbox))}")
    print(f"- Latest closeout report: {latest_report(report_dir) or 'None'}")
    return 0


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--source", default="end-session", choices=["end-session", "daily-backfill", "system-governor", "manual"])
    parser.add_argument("--state-file", default="", help="Optional session-state file override for tests.")
    parser.add_argument("--autopilot-state-file", default="", help="Optional autopilot-state file override for tests.")
    parser.add_argument("--routing-data-file", default="", help="Optional routing intelligence JSON override.")
    parser.add_argument("--feedback-inbox", default="", help="Optional routing feedback inbox JSONL override.")
    parser.add_argument("--report-dir", default="", help="Optional report directory override.")
    parser.add_argument("--skip-registrar", action="store_true", help="Skip session_log_registrar; useful for isolated tests.")
    parser.add_argument("--skip-snapshots", action="store_true", help="Skip health/protocol/routing snapshots; useful for isolated tests.")
    parser.add_argument(
        "--no-prune",
        action="store_true",
        help="Write the current report without moving older reports; used by manifest-scoped Codex closeout.",
    )
    parser.add_argument("--guard-file", default="", help="Optional run-guard ledger JSONL override (tests).")


def main() -> int:
    parser = argparse.ArgumentParser(description="End-session intelligence capture loop.")
    sub = parser.add_subparsers(dest="command", required=True)

    scan = sub.add_parser("scan", help="Discover closeout intelligence candidates without writing.")
    add_common_args(scan)

    run = sub.add_parser("run", help="Capture closeout intelligence.")
    add_common_args(run)
    run.add_argument("--dry-run", action="store_true", help="Show capture actions without writing.")
    run.add_argument("--force", action="store_true", help="Bypass the per-session run guard and regenerate snapshots + report.")

    status = sub.add_parser("status", help="Show closeout intelligence counts.")
    add_common_args(status)

    args = parser.parse_args()
    if args.command == "scan":
        return cmd_scan(args)
    if args.command == "run":
        return cmd_run(args)
    if args.command == "status":
        return cmd_status(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
