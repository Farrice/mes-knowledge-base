#!/usr/bin/env python3
"""Automatic session performance registrar.

Turns meaningful Antigravity session outcomes into local-first Performance Log
evidence. High-confidence candidates are committed; uncertain candidates go to
an inbox for review.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, asdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[1]
AGENT_DIR = ROOT / ".agent"
SESSION_STATE = AGENT_DIR / "session-state.md"
REPORT_DIR = AGENT_DIR / "recurring-reports"
INBOX_PATH = AGENT_DIR / "performance-log-inbox.jsonl"
SKIPPED_PATH = AGENT_DIR / "performance-log-skipped.jsonl"
INBOX_ARCHIVE_PATH = AGENT_DIR / "performance-log-inbox-archive.jsonl"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from log_performance import get_local_performance_entries, log_output
from performance_evidence_audit import (
    DUPLICATE_CLOSEOUT_ONLY,
    PROMOTABLE,
    classify_row,
    read_jsonl as read_evidence_jsonl,
)


TASK_TYPES = {"Content", "Strategy", "Extraction", "Research", "Client Work", "System", "Creative", "Analysis"}
LANES = {"Client", "Personal", "System", "Creative", "Research", "Unknown"}


@dataclass
class Candidate:
    title: str
    agent: str = ""
    skill: str = ""
    workflow: str = ""
    task_type: str = "System"
    lane: str = "Unknown"
    quality_score: Optional[float] = None
    intent_alignment: Optional[float] = None
    expert_standard: Optional[float] = None
    adversarial_resilience: Optional[float] = None
    status: str = "Keep"
    notes: str = ""
    source_artifact: str = ""
    registration_source: str = "daily-backfill"
    auto_confidence: float = 0.0
    review_state: str = "inbox"
    reason: str = ""
    fingerprint: str = ""


def read_text(path: Path, max_chars: int = 30000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:max_chars]
    except OSError:
        return ""


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def source_hash(path: str) -> str:
    p = ROOT / path if not Path(path).is_absolute() else Path(path)
    if not p.exists():
        return ""
    digest = hashlib.sha1()
    try:
        digest.update(p.read_bytes()[:50000])
    except OSError:
        return ""
    return digest.hexdigest()[:12]


def fingerprint(candidate: Candidate) -> str:
    parts = [
        date.today().isoformat(),
        normalize(candidate.title),
        normalize(candidate.workflow),
        normalize(candidate.skill),
        source_hash(candidate.source_artifact),
    ]
    return hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()[:16]


def append_jsonl(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


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


def recent(path: Path, since_days: int) -> bool:
    if not path.exists():
        return False
    cutoff = datetime.now().timestamp() - (since_days * 86400)
    return path.stat().st_mtime >= cutoff


def section(content: str, name: str) -> str:
    pattern = rf"^## {re.escape(name)}\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_quality(text: str) -> tuple[Optional[float], Optional[float], Optional[float], Optional[float]]:
    quality = None
    intent = None
    expert = None
    adversarial = None
    q_match = re.search(r"Quality(?: Score)?:\s*(\d+(?:\.\d+)?)\s*/?\s*10?", text, re.IGNORECASE)
    if q_match:
        quality = float(q_match.group(1))
    labels = {
        "Intent Alignment": "intent",
        "Expert Standard": "expert",
        "Adversarial Resilience": "adversarial",
    }
    for label, target in labels.items():
        match = re.search(rf"{label}:\s*(\d+(?:\.\d+)?)", text, re.IGNORECASE)
        if match and target == "intent":
            intent = float(match.group(1))
        elif match and target == "expert":
            expert = float(match.group(1))
        elif match and target == "adversarial":
            adversarial = float(match.group(1))
    return quality, intent, expert, adversarial


def infer_lane(text: str) -> str:
    low = text.lower()
    if any(term in low for term in ["registrar", "automation", "health", "governor", "workflow", "skill", "system"]):
        return "System"
    if any(term in low for term in ["client", "proposal", "deliverable", "outreach", "buyer", "revenue"]):
        return "Client"
    if any(term in low for term in ["creative", "design", "video", "image", "carousel"]):
        return "Creative"
    if any(term in low for term in ["research", "ground truth", "market", "citation"]):
        return "Research"
    if any(term in low for term in ["personal", "journal", "voice", "farrice"]):
        return "Personal"
    return "Unknown"


def infer_task_type(text: str) -> str:
    low = text.lower()
    if "system" in low or "automation" in low or "registrar" in low or "health" in low:
        return "System"
    if "extraction" in low or "extract-forge" in low:
        return "Extraction"
    if "client" in low or "proposal" in low or "deliverable" in low:
        return "Client Work"
    if "research" in low or "ground truth" in low:
        return "Research"
    if "content" in low or "post" in low or "newsletter" in low:
        return "Content"
    if "creative" in low or "design" in low or "video" in low:
        return "Creative"
    if "strategy" in low or "brief" in low:
        return "Strategy"
    return "Analysis"


def infer_workflow(text: str) -> str:
    low = text.lower()
    explicit = re.search(r"`([^`]+)`", text)
    if explicit and "/" not in explicit.group(1):
        value = explicit.group(1)
        if value.endswith(".py"):
            return Path(value).stem
    for name in ["recurring-ops", "session-log-registrar", "extract-forge", "autopilot", "end-session", "system-governor", "daily-health"]:
        if name in low:
            return name
    match = re.search(r"/([a-z0-9][a-z0-9-]+)", text)
    return match.group(1) if match else ""


def infer_agent(text: str) -> str:
    experts = section(text, "Experts Deployed")
    match = re.search(r"\*\*([^*]+)\*\*", experts)
    if match:
        return match.group(1).strip()
    if "evolution-agent" in text:
        return "evolution-agent"
    if "knowledge-librarian" in text:
        return "knowledge-librarian"
    return ""


def infer_skill(text: str) -> str:
    match = re.search(r"Skill[`: ]+([a-z0-9][a-z0-9-]+)", text, re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r"`([a-z0-9][a-z0-9-]+)`", text)
    if match and "source-command" in match.group(1):
        return match.group(1)
    return ""


def session_state_candidate(registration_source: str) -> Optional[Candidate]:
    text = read_text(SESSION_STATE)
    if not text:
        return None
    active = section(text, "Active Task")
    key_findings = section(text, "Key Findings (Compressed)")
    completed = section(text, "Completed")
    full = "\n".join([active, key_findings, completed, text])
    if not is_evolution_worthy(full):
        return None

    title = active.splitlines()[0].strip("- ").strip() if active.strip() else "Session outcome"
    title = title[:120]
    quality, intent, expert, adversarial = extract_quality(full)
    workflow = infer_workflow(full)
    task_type = infer_task_type(full)
    lane = infer_lane(full)
    agent = infer_agent(full)
    skill = infer_skill(full)

    validation_evidence = any(term in full.lower() for term in ["validation", "verified", "passed", "health now shows", "created active", "implemented"])
    if quality is None and validation_evidence:
        quality = 8.0
        intent = intent or 8.0
        expert = expert or 8.0
        adversarial = adversarial or 7.0
        notes_suffix = "Auto-estimated scores from validation evidence; review if this should be human-rated."
    else:
        notes_suffix = ""

    confidence = 0.35
    if title and len(title) > 10:
        confidence += 0.15
    if workflow or skill or agent:
        confidence += 0.2
    if quality is not None:
        confidence += 0.2
    if lane != "Unknown" and task_type in TASK_TYPES:
        confidence += 0.1
    if "conversation index update" in full.lower() or "git checkpoint unavailable" in full.lower():
        confidence -= 0.05

    candidate = Candidate(
        title=title,
        agent=agent,
        skill=skill,
        workflow=workflow,
        task_type=task_type,
        lane=lane,
        quality_score=quality,
        intent_alignment=intent,
        expert_standard=expert,
        adversarial_resilience=adversarial,
        status="Keep" if quality and quality >= 7 else "Baseline",
        notes="; ".join(x for x in [summarize_notes(key_findings or full), notes_suffix] if x),
        source_artifact=str(SESSION_STATE.relative_to(ROOT)),
        registration_source=registration_source,
        auto_confidence=round(min(confidence, 0.98), 2),
    )
    candidate.fingerprint = fingerprint(candidate)
    candidate.review_state = "committed" if candidate.auto_confidence >= 0.85 else "inbox"
    candidate.reason = "clear meaningful session outcome" if candidate.review_state == "committed" else "missing one or more scoring fields"
    return candidate


def report_candidates(registration_source: str, since_days: int) -> list[Candidate]:
    candidates: list[Candidate] = []
    if not REPORT_DIR.exists():
        return candidates
    for path in sorted(REPORT_DIR.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)[:10]:
        if not recent(path, since_days):
            continue
        text = read_text(path)
        if not is_evolution_worthy(text):
            continue
        title = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        name = title.group(1).strip() if title else path.stem
        if "Daily Antigravity Health" in name:
            continue
        quality, intent, expert, adversarial = extract_quality(text)
        workflow = infer_workflow(text) or path.stem
        candidate = Candidate(
            title=name,
            workflow=workflow,
            task_type=infer_task_type(text),
            lane=infer_lane(text),
            quality_score=quality,
            intent_alignment=intent,
            expert_standard=expert,
            adversarial_resilience=adversarial,
            status="Keep" if quality and quality >= 7 else "Baseline",
            notes=summarize_notes(text),
            source_artifact=str(path.relative_to(ROOT)),
            registration_source=registration_source,
            auto_confidence=0.62 if quality is None else 0.82,
            review_state="inbox",
            reason="recurring report needs review before becoming performance evidence",
        )
        candidate.fingerprint = fingerprint(candidate)
        candidates.append(candidate)
    return candidates


def fixture_candidate(path: Path, registration_source: str) -> Candidate:
    data = json.loads(path.read_text(encoding="utf-8"))
    candidate = Candidate(
        title=data.get("title") or data.get("output") or "Fixture session outcome",
        agent=data.get("agent", ""),
        skill=data.get("skill", ""),
        workflow=data.get("workflow", ""),
        task_type=data.get("task_type", infer_task_type(json.dumps(data))),
        lane=data.get("lane", infer_lane(json.dumps(data))),
        quality_score=data.get("quality_score"),
        intent_alignment=data.get("intent_alignment"),
        expert_standard=data.get("expert_standard"),
        adversarial_resilience=data.get("adversarial_resilience"),
        status=data.get("status", "Keep"),
        notes=data.get("notes", ""),
        source_artifact=str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
        registration_source=registration_source,
    )
    fields = [candidate.title, candidate.workflow, candidate.skill, candidate.task_type, candidate.lane, candidate.quality_score]
    present = sum(1 for f in fields if f not in ("", None, "Unknown"))
    candidate.auto_confidence = round(min(0.35 + present * 0.11, 0.97), 2)
    candidate.review_state = "committed" if candidate.auto_confidence >= 0.85 else "inbox"
    candidate.reason = "fixture explicit enough to commit" if candidate.review_state == "committed" else "fixture missing registration fields"
    candidate.fingerprint = fingerprint(candidate)
    return candidate


def is_evolution_worthy(text: str) -> bool:
    low = text.lower()
    skip_terms = ["trivial question", "routing only", "debugging only", "pure file ops"]
    if any(term in low for term in skip_terms):
        return False
    signals = [
        "implemented", "built", "created", "delivered", "produced", "extraction",
        "client", "system", "workflow", "skill", "research", "strategy", "creative",
        "validation", "health", "automation", "governor", "registrar",
    ]
    return sum(1 for signal in signals if signal in low) >= 2


def summarize_notes(text: str) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    clean = re.sub(r"`", "", clean)
    return clean[:450]


def collect_candidates(args: argparse.Namespace) -> list[Candidate]:
    candidates: list[Candidate] = []
    if getattr(args, "fixture", None):
        candidates.append(fixture_candidate(Path(args.fixture), args.source))
        return candidates
    session_candidate = session_state_candidate(args.source)
    if session_candidate:
        candidates.append(session_candidate)
    candidates.extend(report_candidates(args.source, args.since_days))
    return candidates


def duplicate_reason(candidate: Candidate) -> str:
    entries = get_local_performance_entries()
    candidate_title = normalize(candidate.title)
    for entry in entries:
        entry_title = normalize(str(entry.get("Output", "")))
        same_title = candidate_title and (candidate_title == entry_title or candidate_title in entry_title or entry_title in candidate_title)
        same_workflow = candidate.workflow and candidate.workflow == entry.get("Workflow")
        same_skill = candidate.skill and candidate.skill == entry.get("Skill")
        same_source = candidate.source_artifact and candidate.source_artifact == entry.get("Source Artifact")
        if same_source or (same_title and (same_workflow or same_skill)):
            return f"duplicate of {entry.get('Local ID', 'existing entry')}"
        if same_workflow and entry.get("Date") >= (date.today() - timedelta(days=3)).isoformat():
            return f"recent workflow already logged as {entry.get('Local ID', 'existing entry')}"
    for row in read_jsonl(INBOX_PATH):
        if row.get("fingerprint") == candidate.fingerprint:
            return f"already in inbox as {row.get('draft_id', candidate.fingerprint)}"
    return ""


def to_record(candidate: Candidate) -> dict:
    record = asdict(candidate)
    record["draft_id"] = f"draft_{candidate.fingerprint}"
    record["created_at"] = datetime.now().isoformat(timespec="seconds")
    return record


def commit_candidate(candidate: Candidate, dry_run: bool) -> dict:
    if dry_run:
        return {"url": "dry-run://commit", "local_id": "dry-run"}
    return log_output(
        output=candidate.title,
        agent=candidate.agent,
        skill=candidate.skill,
        workflow=candidate.workflow,
        task_type=candidate.task_type,
        quality_score=candidate.quality_score,
        intent_alignment=candidate.intent_alignment,
        expert_standard=candidate.expert_standard,
        adversarial_resilience=candidate.adversarial_resilience,
        status=candidate.status,
        notes=candidate.notes,
        lane=candidate.lane,
        source_artifact=candidate.source_artifact,
        registration_source=candidate.registration_source,
        auto_confidence=candidate.auto_confidence,
        review_state="committed",
    )


def route_candidate(candidate: Candidate, dry_run: bool) -> tuple[str, str]:
    duplicate = duplicate_reason(candidate)
    if duplicate:
        candidate.review_state = "skipped"
        candidate.reason = duplicate
        if not dry_run:
            append_jsonl(SKIPPED_PATH, to_record(candidate))
        return "skipped", duplicate
    if candidate.auto_confidence >= 0.85:
        commit_candidate(candidate, dry_run)
        return "committed", candidate.reason
    if candidate.auto_confidence >= 0.55:
        candidate.review_state = "inbox"
        if not dry_run:
            append_jsonl(INBOX_PATH, to_record(candidate))
        return "inbox", candidate.reason
    candidate.review_state = "skipped"
    candidate.reason = "below confidence threshold"
    if not dry_run:
        append_jsonl(SKIPPED_PATH, to_record(candidate))
    return "skipped", candidate.reason


def render_candidates(candidates: list[Candidate], include_routing: bool = False) -> str:
    if not candidates:
        return "No registrar candidates found."
    lines = ["| State | Confidence | Lane | Type | Workflow | Title | Reason |", "|---|---:|---|---|---|---|---|"]
    for c in candidates:
        state = c.review_state
        if include_routing:
            dup = duplicate_reason(c)
            state = "skipped" if dup else ("committed" if c.auto_confidence >= 0.85 else "inbox" if c.auto_confidence >= 0.55 else "skipped")
            reason = dup or c.reason
        else:
            reason = c.reason
        lines.append(f"| {state} | {c.auto_confidence:.2f} | {c.lane} | {c.task_type} | {c.workflow or '-'} | {c.title[:80]} | {reason} |")
    return "\n".join(lines)


def cmd_scan(args: argparse.Namespace) -> int:
    candidates = collect_candidates(args)
    print(render_candidates(candidates, include_routing=True))
    return 0


def cmd_register(args: argparse.Namespace) -> int:
    candidates = collect_candidates(args)
    results = []
    for candidate in candidates:
        state, reason = route_candidate(candidate, args.dry_run)
        candidate.review_state = state
        candidate.reason = reason
        results.append(candidate)
    print(render_candidates(results))
    print(f"\nSummary: committed={sum(1 for c in results if c.review_state == 'committed')} inbox={sum(1 for c in results if c.review_state == 'inbox')} skipped={sum(1 for c in results if c.review_state == 'skipped')}")
    return 0


def cmd_inbox(args: argparse.Namespace) -> int:
    rows = read_jsonl(INBOX_PATH)
    if not rows:
        print("Registrar inbox is empty.")
        return 0
    print("| Draft ID | Confidence | Lane | Type | Workflow | Title |")
    print("|---|---:|---|---|---|---|")
    for row in rows[-args.limit:]:
        print(f"| {row.get('draft_id')} | {row.get('auto_confidence', 0):.2f} | {row.get('lane', 'Unknown')} | {row.get('task_type', '')} | {row.get('workflow', '-')} | {row.get('title', '')[:80]} |")
    return 0


def cmd_promote(args: argparse.Namespace) -> int:
    rows = read_jsonl(INBOX_PATH)
    selected = next((row for row in rows if row.get("draft_id") == args.draft_id), None)
    if not selected:
        print(f"Draft not found: {args.draft_id}")
        return 1
    committed = read_evidence_jsonl(AGENT_DIR / "performance-log.jsonl")
    verdict = classify_row(selected, committed)
    if verdict.classification != PROMOTABLE:
        print(f"Promotion blocked: {args.draft_id}")
        print(f"Classification: {verdict.classification}")
        print(f"Reason: {verdict.reason}")
        print("Use `python3 execution/performance_evidence_audit.py` to review inbox evidence.")
        return 2
    candidate = Candidate(**{k: selected.get(k) for k in Candidate.__dataclass_fields__.keys()})
    candidate.review_state = "promoted"
    candidate.registration_source = "manual-promote"
    commit_candidate(candidate, args.dry_run)
    if not args.dry_run:
        remaining = [row for row in rows if row.get("draft_id") != args.draft_id]
        INBOX_PATH.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in remaining), encoding="utf-8")
    print(f"Promoted: {args.draft_id}")
    return 0


def archive_inbox_record(row: dict, verdict) -> dict:
    record = dict(row)
    record["archive_state"] = "archived"
    record["archive_classification"] = verdict.classification
    record["archive_reason"] = verdict.reason
    record["archived_at"] = datetime.now().isoformat(timespec="seconds")
    return record


def cmd_archive_duplicates(args: argparse.Namespace) -> int:
    rows = read_jsonl(INBOX_PATH)
    if not rows:
        print("Registrar inbox is empty.")
        return 0

    committed = read_evidence_jsonl(AGENT_DIR / "performance-log.jsonl")
    archived: list[dict] = []
    remaining: list[dict] = []
    for row in rows:
        verdict = classify_row(row, committed)
        if verdict.classification == DUPLICATE_CLOSEOUT_ONLY:
            archived.append(archive_inbox_record(row, verdict))
        else:
            remaining.append(row)

    if not args.dry_run and archived:
        INBOX_ARCHIVE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with INBOX_ARCHIVE_PATH.open("a", encoding="utf-8") as archive_file:
            for record in archived:
                archive_file.write(json.dumps(record, ensure_ascii=False) + "\n")
        INBOX_PATH.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in remaining), encoding="utf-8")

    mode = "dry-run" if args.dry_run else "write"
    print("# Registrar Inbox Duplicate Archive")
    print("")
    print(f"- Mode: {mode}")
    print(f"- Inbox before: {len(rows)}")
    print(f"- Archived duplicate/closeout-only: {len(archived)}")
    print(f"- Remaining inbox drafts: {len(remaining)}")
    print(f"- Archive path: {INBOX_ARCHIVE_PATH.relative_to(ROOT)}")
    if archived:
        print("")
        print("| Draft ID | Title | Source |")
        print("|---|---|---|")
        for record in archived[: args.limit]:
            title = re.sub(r"\s+", " ", str(record.get("title") or "")).replace("|", "\\|")[:80]
            source = str(record.get("source_artifact") or "").replace("|", "\\|")[:90]
            print(f"| `{record.get('draft_id')}` | {title} | {source} |")
        if len(archived) > args.limit:
            print(f"| ... | {len(archived) - args.limit} more archived drafts omitted | ... |")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    entries = get_local_performance_entries()
    inbox = read_jsonl(INBOX_PATH)
    skipped = read_jsonl(SKIPPED_PATH)
    auto_entries = [e for e in entries if e.get("Registration Source") in {"end-session", "daily-backfill", "system-governor", "manual-promote"}]
    print("# Session Log Registrar Status\n")
    print(f"- Committed local performance entries: {len(entries)}")
    print(f"- Auto/promoted registrar entries: {len(auto_entries)}")
    print(f"- Inbox drafts: {len(inbox)}")
    print(f"- Skipped duplicate/low-confidence candidates: {len(skipped)}")
    if inbox:
        print(f"- Next review: `python3 execution/session_log_registrar.py inbox`")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Automatic session performance registrar.")
    parser.add_argument("--source", default="daily-backfill", choices=["manual", "end-session", "daily-backfill", "system-governor"], help="Registration source label.")
    parser.add_argument("--since-days", type=int, default=3, help="How many days of local reports to scan.")
    parser.add_argument("--fixture", default="", help="Optional JSON fixture/session summary to scan instead of live state.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("scan", help="Scan for candidate entries without writing.")
    register = sub.add_parser("register", help="Register high-confidence entries and inbox uncertain ones.")
    register.add_argument("--dry-run", action="store_true", help="Show routing without writing log or inbox files.")
    inbox = sub.add_parser("inbox", help="List registrar inbox drafts.")
    inbox.add_argument("--limit", type=int, default=20)
    promote = sub.add_parser("promote", help="Promote an inbox draft to committed performance evidence.")
    promote.add_argument("draft_id")
    promote.add_argument("--dry-run", action="store_true")
    archive_duplicates = sub.add_parser("archive-duplicates", help="Archive duplicate/closeout-only inbox drafts.")
    archive_duplicates.add_argument("--dry-run", action="store_true")
    archive_duplicates.add_argument("--limit", type=int, default=20, help="Archived rows to show.")
    sub.add_parser("status", help="Show registrar counts.")

    args = parser.parse_args()
    if args.command == "scan":
        return cmd_scan(args)
    if args.command == "register":
        return cmd_register(args)
    if args.command == "inbox":
        return cmd_inbox(args)
    if args.command == "promote":
        return cmd_promote(args)
    if args.command == "archive-duplicates":
        return cmd_archive_duplicates(args)
    if args.command == "status":
        return cmd_status(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
