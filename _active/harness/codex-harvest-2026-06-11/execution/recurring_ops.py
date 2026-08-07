#!/usr/bin/env python3
"""Recurring Antigravity ops runner.

Local-first scheduled routines for health, system pulse, hygiene/evolution
review, and the supervised System Governor queue.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / ".agent" / "recurring-reports"
GOVERNOR_QUEUE = ROOT / ".agent" / "system-governor-queue.md"
LOCAL_PERFORMANCE_LOG = ROOT / ".agent" / "performance-log.jsonl"
ROUTING_LOG = ROOT / ".agent" / "routing-intelligence.json"
ACTIVATION_GOVERNOR = ROOT / "execution" / "activation_governor.py"
SYSTEM_COHESION_PLATTER = ROOT / "execution" / "system_cohesion_platter.py"
AUTOMATION_COHESION_VERIFIER = ROOT / "execution" / "verify_automation_cohesion_standard.py"
INTENT_MEMORY = ROOT / ".agent" / "intent-memory" / "current.json"
SYSTEM_COHESION_STATE = ROOT / ".agent" / "system-cohesion-state.json"


@dataclass
class CommandResult:
    label: str
    command: list[str]
    returncode: int
    stdout: str
    stderr: str

    @property
    def ok(self) -> bool:
        return self.returncode == 0


def run_command(label: str, args: list[str], timeout: int = 90) -> CommandResult:
    try:
        proc = subprocess.run(
            args,
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode("utf-8", errors="ignore") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = exc.stderr.decode("utf-8", errors="ignore") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        timeout_note = f"Timed out after {timeout}s."
        return CommandResult(label, args, 124, str(stdout).strip(), (str(stderr).strip() + "\n" + timeout_note).strip())
    return CommandResult(label, args, proc.returncode, proc.stdout.strip(), proc.stderr.strip())


def section(title: str, body: str) -> str:
    body = body.strip() or "No output."
    return f"## {title}\n\n{body}\n"


def render_command(result: CommandResult, max_chars: int = 6000) -> str:
    status = "PASS" if result.ok else "FAIL"
    text = result.stdout if result.stdout else result.stderr
    if len(text) > max_chars:
        text = text[:max_chars].rstrip() + "\n\n[truncated]"
    return f"**Status**: {status}\n\n```text\n{text}\n```"


def read_existing_report(label: str, path: Path, missing: str) -> CommandResult:
    if not path.exists():
        return CommandResult(label, ["read", str(path)], 0, missing, "")
    text = path.read_text(encoding="utf-8", errors="ignore").strip()
    if len(text) > 6000:
        text = text[:6000].rstrip() + "\n\n[truncated]"
    return CommandResult(label, ["read", str(path)], 0, text, "")


def read_json_file(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def compact(value: object, limit: int = 180) -> str:
    text = str(value or "").strip()
    if not text:
        return "Not recorded"
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "..."


def join_compact(values: object, limit: int = 5) -> str:
    if not isinstance(values, list) or not values:
        return "None recorded"
    shown = [str(value) for value in values[:limit] if str(value).strip()]
    suffix = f" (+{len(values) - limit} more)" if len(values) > limit else ""
    return ", ".join(shown) + suffix if shown else "None recorded"


def verifier_snapshot(verifier_status: dict) -> str:
    if not verifier_status:
        return "No verifier snapshot recorded."
    pass_count = sum(1 for value in verifier_status.values() if str(value).lower() == "pass")
    not_pass = [
        f"{key}={value}"
        for key, value in sorted(verifier_status.items())
        if str(value).lower() != "pass" and key != "last_checked_at"
    ]
    last_checked = verifier_status.get("last_checked_at", "unknown")
    if not_pass:
        return f"{pass_count} pass; attention: {', '.join(not_pass)}; last checked {last_checked}"
    return f"{pass_count} pass; last checked {last_checked}"


def latest_system_cohesion_platter() -> str:
    report_dir = ROOT / "docs" / "pulse-reports" / "system-cohesion"
    reports = sorted(report_dir.glob("*-system-cohesion-platter.md"))
    if not reports:
        return "Not written yet"
    return f"`{reports[-1].relative_to(ROOT)}`"


def optional_script_result(
    label: str,
    script: Path,
    args: list[str],
    missing: str,
    timeout: int = 180,
) -> CommandResult:
    if not script.exists():
        return CommandResult(label, ["read", str(script)], 0, missing, "")
    return run_command(label, [sys.executable, str(script.relative_to(ROOT)), *args], timeout=timeout)


def automation_cohesion_status() -> str:
    intent_memory = read_json_file(INTENT_MEMORY)
    cohesion = read_json_file(SYSTEM_COHESION_STATE)
    active_intent = cohesion.get("active_intent") or intent_memory.get("active_intent", {})
    chosen_route = cohesion.get("chosen_route", {})
    mission = cohesion.get("mission", {})
    next_move = cohesion.get("next_move", {})
    weekly_platter = cohesion.get("weekly_platter", {})
    activation_queue = cohesion.get("activation_queue", [])
    verifier_status = cohesion.get("verifier_status", {})
    automation_standard = optional_script_result(
        "Automation Cohesion Standard",
        AUTOMATION_COHESION_VERIFIER,
        [],
        "Automation cohesion verifier not installed yet.",
    )
    automation_drift = "PASS" if automation_standard.ok else "FAIL"
    weekly_path = weekly_platter.get("path") or latest_system_cohesion_platter()

    return "\n".join(
        [
            "| Surface | Current Standard |",
            "|---|---|",
            f"| Intent memory | {compact(active_intent.get('goal'))} |",
            f"| Clarity / confidence | {active_intent.get('clarity_score', 'unknown')} / {compact(active_intent.get('confidence'), 40)} |",
            f"| Mission | `{compact(mission.get('slug'), 80)}` ({compact(mission.get('status'), 40)}) |",
            f"| Chosen route | `/{compact(chosen_route.get('route'), 80).lstrip('/')}` via {compact(chosen_route.get('mode'), 60)} |",
            f"| Support gates | {join_compact(cohesion.get('support_gates'))} |",
            f"| Verifier snapshot | {compact(verifier_snapshot(verifier_status), 260)} |",
            f"| Activation queue | {join_compact(activation_queue, limit=3)} |",
            f"| Weekly platter | {compact(weekly_platter.get('status'), 60)} at {weekly_path} |",
            f"| Automation drift | {automation_drift}: {compact(automation_standard.stdout or automation_standard.stderr, 260)} |",
            f"| Next move | {compact(next_move.get('action'), 260)} |",
        ]
    )


def write_report(kind: str, content: str, dry_run: bool) -> Path:
    path = REPORT_DIR / f"{datetime.now().strftime('%Y-%m-%d')}-{kind}.md"
    if not dry_run:
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return path


def count_local_performance() -> tuple[int, str]:
    if not LOCAL_PERFORMANCE_LOG.exists():
        return 0, "Never"
    entries = []
    for line in LOCAL_PERFORMANCE_LOG.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    if not entries:
        return 0, "Never"
    entries.sort(key=lambda e: (e.get("Date", ""), e.get("Timestamp", "")), reverse=True)
    return len(entries), entries[0].get("Date", "Unknown")


def count_routing_decisions() -> int:
    if not ROUTING_LOG.exists():
        return 0
    try:
        data = json.loads(ROUTING_LOG.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return 0
    if isinstance(data, list):
        return len(data)
    return len(data.get("routing_decisions", []))


def routing_feedback_queue_items(limit: int = 5) -> list[str]:
    if not ROUTING_LOG.exists():
        return []
    try:
        data = json.loads(ROUTING_LOG.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    decisions = {
        row.get("routing_id"): row
        for row in data.get("routing_decisions", [])
        if row.get("routing_id")
    }
    items = []
    for feedback in data.get("feedback_log", []):
        if feedback.get("rating") not in {"negative", "mixed"}:
            continue
        decision = decisions.get(feedback.get("routing_id"), {})
        wrong = decision.get("workflow_used") or "unknown-route"
        correction = feedback.get("correction") or "needs correction"
        request = decision.get("request_summary") or "unknown request"
        items.append(
            f"[HIGH] Routing fix: `{wrong}` received {feedback.get('rating')} feedback for \"{request}\"; review correction `{correction}`."
        )
    return items[-limit:]


def evidence_status() -> str:
    perf_count, perf_last = count_local_performance()
    routing_count = count_routing_decisions()
    return "\n".join(
        [
            "| Evidence | Count | Last/Status |",
            "|----------|-------|-------------|",
            f"| Local performance log | {perf_count} | {perf_last} |",
            f"| Routing decisions | {routing_count} | {'active' if routing_count else 'not yet logged'} |",
            f"| Performance path | - | `{LOCAL_PERFORMANCE_LOG.relative_to(ROOT)}` |",
            f"| Routing path | - | `{ROUTING_LOG.relative_to(ROOT)}` |",
        ]
    )


def log_ops_routing(request: str, workflow: str, domain: str = "system") -> None:
    try:
        from routing_intelligence import log_routing_decision

        log_routing_decision(
            request_summary=request,
            intent_score=5,
            domain_detected=domain,
            experts_deployed=["antigravity-orchestrator", "evolution-agent"],
            tier_loaded=1,
            mode="output",
            workflow_used=workflow,
            session_id="recurring-ops",
        )
    except Exception:
        pass


def report_header(title: str) -> str:
    return f"# {title}\n\n**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"


def daily_health(args: argparse.Namespace) -> str:
    if not args.dry_run:
        log_ops_routing("daily recurring Antigravity health check", "health-check")
    registrar = run_command(
        "Session Registrar Backfill",
        [sys.executable, "execution/session_log_registrar.py", "--source", "daily-backfill", "register"] + (["--dry-run"] if args.dry_run else []),
    )
    results = [
        registrar,
        run_command("Health Check", [sys.executable, "execution/system_health.py", "--quick"]),
        run_command("Harness Smoke Check", [sys.executable, "execution/codex_harness_check.py"]),
        run_command("Routing Scoreboard", [sys.executable, "execution/routing_intelligence.py", "scoreboard"]),
        optional_script_result(
            "Activation Governor Plan",
            ACTIVATION_GOVERNOR,
            ["plan"] + (["--dry-run"] if args.dry_run else []),
            "Activation governor not installed yet.",
        ),
    ]
    failures = [r.label for r in results if not r.ok]
    next_action = "Fix failing checks first." if failures else "Keep collecting performance and routing evidence."
    content = report_header("Daily Antigravity Health")
    content += section("Evidence Status", evidence_status())
    content += section("Automation Cohesion", automation_cohesion_status())
    content += section("Critical Failures", ", ".join(failures) if failures else "None.")
    for result in results:
        content += section(result.label, render_command(result))
    content += section("Recommended Next Action", next_action)
    path = write_report("daily-health", content, args.dry_run)
    print(content)
    print(f"\nReport {'would be written' if args.dry_run else 'written'}: {path}")
    return content


def weekly_system_pulse(args: argparse.Namespace) -> str:
    if not args.dry_run:
        log_ops_routing("weekly recurring Antigravity system pulse", "system-pulse")
    briefing_result = (
        read_existing_report(
            "Knowledge Briefing",
            ROOT / "knowledge" / "compiled" / "briefing.md",
            "Dry run: briefing generation skipped. Existing briefing not found.",
        )
        if args.dry_run
        else run_command("Knowledge Briefing", [sys.executable, "execution/knowledge_compiler.py", "briefing"])
    )
    results = [
        run_command("Session Registrar Status", [sys.executable, "execution/session_log_registrar.py", "status"]),
        run_command("Health Check", [sys.executable, "execution/system_health.py", "--quick"]),
        run_command("Knowledge Stats", [sys.executable, "execution/knowledge_compiler.py", "stats"]),
        briefing_result,
        run_command("Unused Experts", [sys.executable, "execution/routing_intelligence.py", "unused"]),
        run_command("Gap Recommendations", [sys.executable, "execution/gap_analysis.py", "recommendations"]),
        optional_script_result(
            "System Cohesion Platter",
            SYSTEM_COHESION_PLATTER,
            ["run"] + (["--dry-run"] if args.dry_run else []),
            "System cohesion platter not installed yet.",
            timeout=120 if args.dry_run else 420,
        ),
    ]
    content = report_header("Weekly System Pulse")
    content += section("Evidence Status", evidence_status())
    content += section("Automation Cohesion", automation_cohesion_status())
    content += section(
        "Top Three System Priorities",
        "1. Keep local performance evidence moving toward 20 entries.\n"
        "2. Use routing evidence to identify sleeping experts and weak routes.\n"
        "3. Review gap recommendations before approving any evolution work.",
    )
    for result in results:
        content += section(result.label, render_command(result))
    path = write_report("weekly-system-pulse", content, args.dry_run)
    print(content)
    print(f"\nReport {'would be written' if args.dry_run else 'written'}: {path}")
    return content


def is_first_monday(today: date) -> bool:
    return today.weekday() == 0 and 1 <= today.day <= 7


def monthly_hygiene_review(args: argparse.Namespace) -> str:
    due = args.force or is_first_monday(date.today())
    title = "Monthly Hygiene/Evolution Review" if due else "Monthly Hygiene Due Check"
    if not args.dry_run:
        log_ops_routing("monthly recurring Antigravity hygiene and evolution review", "system-hygiene")

    if not due:
        content = report_header(title)
        content += section("Due Status", "Full review skipped because today is not the first Monday.")
        content += section("Evidence Status", evidence_status())
        content += section("Automation Cohesion", automation_cohesion_status())
        path = write_report("monthly-hygiene-due-check", content, args.dry_run)
        print(content)
        print(f"\nReport {'would be written' if args.dry_run else 'written'}: {path}")
        return content

    stale_result = (
        read_existing_report(
            "Knowledge Stale Report",
            ROOT / "knowledge" / "compiled" / "stale-report.md",
            "Dry run: stale report generation skipped. Existing stale report not found.",
        )
        if args.dry_run
        else run_command("Knowledge Stale Report", [sys.executable, "execution/knowledge_compiler.py", "stale"])
    )
    overlap_result = (
        read_existing_report(
            "Knowledge Overlap Report",
            ROOT / "knowledge" / "compiled" / "overlap-report.md",
            "Dry run: overlap report generation skipped. Existing overlap report not found.",
        )
        if args.dry_run
        else run_command("Knowledge Overlap Report", [sys.executable, "execution/knowledge_compiler.py", "overlap"])
    )
    results = [
        optional_script_result(
            "Automation Cohesion Standard",
            AUTOMATION_COHESION_VERIFIER,
            [],
            "Automation cohesion verifier not installed yet.",
        ),
        run_command("Description Audit", [sys.executable, "execution/trim_workflow_descriptions.py", "--audit"]),
        run_command("Gap Analysis", [sys.executable, "execution/gap_analysis.py", "analyze"]),
        stale_result,
        overlap_result,
        run_command("Evolution Status", [sys.executable, "execution/routing_intelligence.py", "underperforming"]),
    ]
    content = report_header(title)
    content += section("Evidence Status", evidence_status())
    content += section("Automation Cohesion", automation_cohesion_status())
    content += section("Autonomy Boundary", "Queue-only. This review does not apply repo changes.")
    for result in results:
        content += section(result.label, render_command(result))
    path = write_report("monthly-hygiene-review", content, args.dry_run)
    print(content)
    print(f"\nReport {'would be written' if args.dry_run else 'written'}: {path}")
    return content


def recent_reports(limit: int = 6) -> list[Path]:
    if not REPORT_DIR.exists():
        return []
    reports = sorted(REPORT_DIR.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    return reports[:limit]


def system_governor(args: argparse.Namespace) -> str:
    if not args.dry_run:
        log_ops_routing("weekly recurring System Governor queue review", "system-governor")
    reports = recent_reports()
    registrar_status = run_command("Session Registrar Status", [sys.executable, "execution/session_log_registrar.py", "status"])
    activation_plan = optional_script_result(
        "Activation Governor Plan",
        ACTIVATION_GOVERNOR,
        ["plan"] + (["--dry-run"] if args.dry_run else []),
        "Activation governor not installed yet.",
    )
    perf_count, _ = count_local_performance()
    routing_count = count_routing_decisions()
    queue_items = []
    if perf_count < 20:
        queue_items.append(f"[HIGH] Build performance evidence: {perf_count}/20 entries toward skill evolution readiness.")
    if routing_count == 0:
        queue_items.append("[HIGH] Start routing evidence capture from Autopilot and recurring ops runs.")
    queue_items.extend(routing_feedback_queue_items())
    queue_items.append("[MEDIUM] Review latest weekly pulse for sleeping assets worth activating.")
    queue_items.append("[LOW] Consolidate recurring report patterns after two full weekly cycles.")

    content = report_header("System Governor Queue")
    content += section("Autonomy Boundary", "Queue-only. Diagnose and prioritize; do not apply upgrades automatically.")
    content += section("Automation Cohesion", automation_cohesion_status())
    content += section("Registrar Status", render_command(registrar_status, max_chars=2000))
    content += section("Activation Governor", render_command(activation_plan, max_chars=3000))
    content += section("Reports Reviewed", "\n".join(f"- `{p.relative_to(ROOT)}`" for p in reports) if reports else "No recurring reports found yet.")
    content += section("Supervised Upgrade Queue", "\n".join(f"{i}. {item}" for i, item in enumerate(queue_items, 1)))
    content += section("Approval Rule", "Every queued upgrade needs explicit user approval before repo edits, external actions, or destructive changes.")

    if not args.dry_run:
        GOVERNOR_QUEUE.parent.mkdir(parents=True, exist_ok=True)
        with GOVERNOR_QUEUE.open("a", encoding="utf-8") as f:
            f.write("\n\n" + content.strip() + "\n")
    print(content)
    print(f"\nQueue {'would be appended' if args.dry_run else 'appended'}: {GOVERNOR_QUEUE}")
    return content


def main() -> int:
    parser = argparse.ArgumentParser(description="Run recurring Antigravity health and governance routines.")
    parser.add_argument("--dry-run", dest="global_dry_run", action="store_true", help="Print the report without writing report/queue files.")
    sub = parser.add_subparsers(dest="command", required=True)

    def add_dry_run(p: argparse.ArgumentParser) -> argparse.ArgumentParser:
        p.add_argument("--dry-run", action="store_true", default=False, help="Print the report without writing report/queue files.")
        return p

    add_dry_run(sub.add_parser("daily-health", help="Run the daily health routine."))
    add_dry_run(sub.add_parser("weekly-system-pulse", help="Run the weekly system pulse."))
    monthly = sub.add_parser("monthly-hygiene-review", help="Run monthly hygiene/evolution review when due.")
    monthly.add_argument("--dry-run", action="store_true", default=False, help="Print the report without writing report/queue files.")
    monthly.add_argument("--force", action="store_true", help="Run the full monthly review even if today is not the first Monday.")
    add_dry_run(sub.add_parser("system-governor", help="Review latest reports and queue supervised upgrades."))

    args = parser.parse_args()
    args.dry_run = bool(getattr(args, "global_dry_run", False) or getattr(args, "dry_run", False))
    if args.command == "daily-health":
        daily_health(args)
    elif args.command == "weekly-system-pulse":
        weekly_system_pulse(args)
    elif args.command == "monthly-hygiene-review":
        monthly_hygiene_review(args)
    elif args.command == "system-governor":
        system_governor(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
