#!/usr/bin/env python3
"""Fail-closed audit for Performance Log inbox evidence.

The Skill Evolution unlock should move only from real, verifier-backed work.
This auditor classifies registrar inbox drafts without mutating the inbox or
the committed performance log.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AGENT_DIR = ROOT / ".agent"
DEFAULT_INBOX = AGENT_DIR / "performance-log-inbox.jsonl"
DEFAULT_LOG = AGENT_DIR / "performance-log.jsonl"

PROMOTABLE = "promotable"
NEEDS_HUMAN_RATING = "needs-human-rating"
DUPLICATE_CLOSEOUT_ONLY = "duplicate/closeout-only"
INSUFFICIENT_PROOF = "insufficient-proof"

SCORING_FIELDS = (
    "quality_score",
    "intent_alignment",
    "expert_standard",
    "adversarial_resilience",
)
COMMITTED_SCORING_FIELDS = (
    "Quality Score",
    "Intent Alignment",
    "Expert Standard",
    "Adversarial Resilience",
)
CLOSEOUT_TITLES = (
    "session closeout intelligence",
    "weekly system pulse",
    "daily antigravity health",
    "activation governor plan",
)
PROOF_TERMS = (
    "implemented",
    "added",
    "fixed",
    "verified",
    "passed",
    "validation",
    "verifier",
    "regression",
    "proof",
    "created",
    "wired",
    "repaired",
)


@dataclass
class EvidenceVerdict:
    draft_id: str
    title: str
    classification: str
    reason: str
    source_artifact: str = ""
    workflow: str = ""

    def as_dict(self) -> dict[str, str]:
        return {
            "draft_id": self.draft_id,
            "title": self.title,
            "classification": self.classification,
            "reason": self.reason,
            "source_artifact": self.source_artifact,
            "workflow": self.workflow,
        }


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


def normalize(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def source_path(value: Any, root: Path = ROOT) -> Path | None:
    raw = str(value or "").strip()
    if not raw:
        return None
    path = Path(raw)
    return path if path.is_absolute() else root / path


def has_existing_duplicate(row: dict[str, Any], committed: list[dict[str, Any]]) -> bool:
    title = normalize(row.get("title"))
    workflow = normalize(row.get("workflow"))
    source = str(row.get("source_artifact") or "")
    for entry in committed:
        entry_source = str(entry.get("Source Artifact") or "")
        if source and source == entry_source:
            return True
        entry_title = normalize(entry.get("Output"))
        entry_workflow = normalize(entry.get("Workflow"))
        if title and workflow and title == entry_title and workflow == entry_workflow:
            return True
    return False


def is_closeout_only(row: dict[str, Any]) -> bool:
    title = normalize(row.get("title"))
    workflow = normalize(row.get("workflow"))
    source = str(row.get("source_artifact") or "")
    if any(name in title for name in CLOSEOUT_TITLES):
        return True
    if workflow in {"autopilot", "performance log", "report"} and source.startswith(".agent/recurring-reports/"):
        return True
    return False


def missing_scoring_fields(row: dict[str, Any]) -> list[str]:
    return [field for field in SCORING_FIELDS if not is_number(row.get(field))]


def scoring_is_complete(row: dict[str, Any]) -> bool:
    return not missing_scoring_fields(row)


def has_local_source_proof(row: dict[str, Any], root: Path = ROOT) -> bool:
    path = source_path(row.get("source_artifact"), root=root)
    return bool(path and path.exists() and path.is_file())


def notes_have_proof(row: dict[str, Any]) -> bool:
    haystack = normalize(" ".join(str(row.get(key) or "") for key in ("title", "notes", "reason")))
    return any(term in haystack for term in PROOF_TERMS)


def classify_row(
    row: dict[str, Any],
    committed: list[dict[str, Any]] | None = None,
    root: Path = ROOT,
) -> EvidenceVerdict:
    committed = committed or []
    title = str(row.get("title") or "")
    draft_id = str(row.get("draft_id") or row.get("fingerprint") or "")
    workflow = str(row.get("workflow") or "")
    source = str(row.get("source_artifact") or "")

    if has_existing_duplicate(row, committed) or is_closeout_only(row):
        return EvidenceVerdict(
            draft_id=draft_id,
            title=title,
            classification=DUPLICATE_CLOSEOUT_ONLY,
            reason="draft is a duplicate, recurring closeout, or report wrapper rather than a distinct performance outcome",
            source_artifact=source,
            workflow=workflow,
        )

    if not has_local_source_proof(row, root=root):
        return EvidenceVerdict(
            draft_id=draft_id,
            title=title,
            classification=INSUFFICIENT_PROOF,
            reason="source_artifact is missing or does not point to a local proof file",
            source_artifact=source,
            workflow=workflow,
        )

    if not notes_have_proof(row):
        return EvidenceVerdict(
            draft_id=draft_id,
            title=title,
            classification=INSUFFICIENT_PROOF,
            reason="notes do not describe an implemented, verified, or otherwise concrete outcome",
            source_artifact=source,
            workflow=workflow,
        )

    missing = missing_scoring_fields(row)
    if missing:
        return EvidenceVerdict(
            draft_id=draft_id,
            title=title,
            classification=NEEDS_HUMAN_RATING,
            reason="local proof exists, but scoring fields are missing: " + ", ".join(missing),
            source_artifact=source,
            workflow=workflow,
        )

    quality = float(row.get("quality_score"))
    if quality < 7:
        return EvidenceVerdict(
            draft_id=draft_id,
            title=title,
            classification=INSUFFICIENT_PROOF,
            reason=f"quality_score {quality:g} is below the Skill Evolution evidence floor",
            source_artifact=source,
            workflow=workflow,
        )

    return EvidenceVerdict(
        draft_id=draft_id,
        title=title,
        classification=PROMOTABLE,
        reason="distinct local proof file and complete scoring fields passed the evidence gate",
        source_artifact=source,
        workflow=workflow,
    )


def audit_rows(
    inbox_rows: list[dict[str, Any]],
    committed_rows: list[dict[str, Any]],
    root: Path = ROOT,
) -> list[EvidenceVerdict]:
    return [classify_row(row, committed_rows, root=root) for row in inbox_rows]


def count_by_class(verdicts: list[EvidenceVerdict]) -> dict[str, int]:
    counts = {
        PROMOTABLE: 0,
        NEEDS_HUMAN_RATING: 0,
        DUPLICATE_CLOSEOUT_ONLY: 0,
        INSUFFICIENT_PROOF: 0,
    }
    for verdict in verdicts:
        counts[verdict.classification] = counts.get(verdict.classification, 0) + 1
    return counts


def render_markdown(verdicts: list[EvidenceVerdict], limit: int = 40) -> str:
    counts = count_by_class(verdicts)
    lines = [
        "# Performance Evidence Audit",
        "",
        "## Summary",
        "",
        f"- Inbox drafts audited: {len(verdicts)}",
        f"- Promotable: {counts.get(PROMOTABLE, 0)}",
        f"- Needs human rating: {counts.get(NEEDS_HUMAN_RATING, 0)}",
        f"- Duplicate/closeout-only: {counts.get(DUPLICATE_CLOSEOUT_ONLY, 0)}",
        f"- Insufficient proof: {counts.get(INSUFFICIENT_PROOF, 0)}",
        "",
        "## Drafts",
        "",
        "| Draft | Classification | Workflow | Title | Reason |",
        "|---|---|---|---|---|",
    ]
    for verdict in verdicts[:limit]:
        title = re.sub(r"\s+", " ", verdict.title).replace("|", "\\|")[:90]
        reason = re.sub(r"\s+", " ", verdict.reason).replace("|", "\\|")[:130]
        lines.append(
            f"| `{verdict.draft_id}` | {verdict.classification} | "
            f"{verdict.workflow or '-'} | {title} | {reason} |"
        )
    if len(verdicts) > limit:
        lines.append(f"| ... | ... | ... | {len(verdicts) - limit} more drafts omitted | ... |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Performance Log inbox evidence without mutating logs.")
    parser.add_argument("--inbox", default=str(DEFAULT_INBOX), help="Path to performance-log inbox JSONL.")
    parser.add_argument("--performance-log", default=str(DEFAULT_LOG), help="Path to committed performance log JSONL.")
    parser.add_argument("--limit", type=int, default=40, help="Rows to show in markdown output.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable audit JSON.")
    args = parser.parse_args()

    inbox_path = Path(args.inbox)
    log_path = Path(args.performance_log)
    inbox_rows = read_jsonl(inbox_path if inbox_path.is_absolute() else ROOT / inbox_path)
    committed_rows = read_jsonl(log_path if log_path.is_absolute() else ROOT / log_path)
    verdicts = audit_rows(inbox_rows, committed_rows)
    if args.json:
        print(json.dumps({
            "counts": count_by_class(verdicts),
            "verdicts": [verdict.as_dict() for verdict in verdicts],
        }, indent=2))
    else:
        print(render_markdown(verdicts, limit=args.limit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
