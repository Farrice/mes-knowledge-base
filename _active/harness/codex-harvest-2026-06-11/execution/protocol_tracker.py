#!/usr/bin/env python3
"""
Protocol Tracker — Automated directive activation tracking for Antigravity.

Updates the "Usage Tracking" section in directive Markdown files. Replaces
manual AI tracking with deterministic code that can't be forgotten.

Usage:
    # Activate a protocol (update Last Activated + increment count)
    python execution/protocol_tracker.py activate directives/quality_gate.md

    # Audit all protocols (list activation lifecycle status)
    python execution/protocol_tracker.py audit

    # From Python:
    from execution.protocol_tracker import activate_protocol, audit_protocols
    activate_protocol("directives/quality_gate.md")
    report = audit_protocols()
"""

import re
import argparse
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

# Project root: two levels up from execution/
PROJECT_ROOT = Path(__file__).parent.parent
DIRECTIVES_DIR = PROJECT_ROOT / "directives"

# Regex patterns for the Usage Tracking table fields
LAST_ACTIVATED_PATTERN = re.compile(
    r'(\| \*\*Last Activated\*\* \| )(.+?)( \|)',
    re.MULTILINE
)
ACTIVATION_COUNT_PATTERN = re.compile(
    r'(\| \*\*Activation Count\*\* \| )(\d+|\*Not yet activated\*)( \|)',
    re.MULTILINE
)
REVIEW_DATE_PATTERN = re.compile(
    r'(\| \*\*30-Day Review Date\*\* \| )(.+?)( \|)',
    re.MULTILINE
)

DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}")
RECENT_ACTIVE_DAYS = 14
COLD_SOURCE_ONLY_HINTS = (
    "guide",
    "policy",
    "playbook",
    "reference",
    "cheat",
    "paths",
    "principles",
    "usage",
    "setup",
)


def activate_protocol(directive_path: str, note: str = "") -> Dict:
    """
    Update the Usage Tracking section of a directive file.

    Args:
        directive_path: Relative or absolute path to the directive .md file.
        note: Optional note to append (e.g., which tier was triggered).

    Returns:
        Dict with old/new values and success status.
    """
    # Resolve path relative to project root if not absolute
    path = Path(directive_path)
    if not path.is_absolute():
        path = PROJECT_ROOT / path

    if not path.exists():
        return {"success": False, "error": f"File not found: {path}"}

    content = path.read_text(encoding="utf-8")

    if "## Usage Tracking" not in content:
        return {"success": False, "error": f"No Usage Tracking section in {path.name}"}

    today = date.today().isoformat()
    result = {"success": True, "file": path.name, "date": today}

    # Update Last Activated
    match = LAST_ACTIVATED_PATTERN.search(content)
    if match:
        old_val = match.group(2).strip()
        result["old_last_activated"] = old_val
        note_suffix = f" ({note})" if note else ""
        content = LAST_ACTIVATED_PATTERN.sub(
            rf'\g<1>{today}{note_suffix}\g<3>', content
        )

    # Update Activation Count
    match = ACTIVATION_COUNT_PATTERN.search(content)
    if match:
        old_count = match.group(2).strip()
        if old_count == "*Not yet activated*" or not old_count.isdigit():
            new_count = 1
        else:
            new_count = int(old_count) + 1
        result["old_count"] = old_count
        result["new_count"] = new_count
        content = ACTIVATION_COUNT_PATTERN.sub(
            rf'\g<1>{new_count}\g<3>', content
        )

    # Reset the review window when a protocol is deliberately activated.
    match = REVIEW_DATE_PATTERN.search(content)
    if match:
        old_review = match.group(2).strip()
        new_review = (date.today() + timedelta(days=30)).isoformat()
        result["old_review_date"] = old_review
        result["new_review_date"] = new_review
        content = REVIEW_DATE_PATTERN.sub(
            rf'\g<1>{new_review}\g<3>', content
        )

    # Write back
    path.write_text(content, encoding="utf-8")
    return result


def get_protocol_status(directive_path: Path) -> Optional[Dict]:
    """
    Read the Usage Tracking section from a directive file.

    Returns:
        Dict with last_activated, activation_count, review_date, lifecycle.
        None if no Usage Tracking section exists.
    """
    if not directive_path.exists():
        return None

    content = directive_path.read_text(encoding="utf-8")
    if "## Usage Tracking" not in content:
        return None

    status = {"file": directive_path.name, "path": str(directive_path.relative_to(PROJECT_ROOT))}

    # Extract Last Activated
    match = LAST_ACTIVATED_PATTERN.search(content)
    if match:
        raw = match.group(2).strip()
        status["last_activated"] = raw
        status["never_activated"] = raw.startswith("*Not yet") or raw == ""
    else:
        status["last_activated"] = "unknown"
        status["never_activated"] = True

    # Extract Activation Count
    match = ACTIVATION_COUNT_PATTERN.search(content)
    if match:
        raw = match.group(2).strip()
        status["activation_count"] = 0 if raw == "*Not yet activated*" or not raw.isdigit() else int(raw)
    else:
        status["activation_count"] = 0

    # Extract 30-Day Review Date
    match = REVIEW_DATE_PATTERN.search(content)
    if match:
        raw = match.group(2).strip()
        status["review_date"] = raw
        # Check if review date has passed
        try:
            review = datetime.strptime(raw, "%Y-%m-%d").date()
            status["is_overdue"] = date.today() > review
        except ValueError:
            status["is_overdue"] = False
    else:
        status["review_date"] = "none"
        status["is_overdue"] = False

    status["lifecycle"] = classify_lifecycle(status, content)
    status["is_zombie"] = status["lifecycle"] == "overdue"

    return status


def first_date(raw: str) -> Optional[date]:
    match = DATE_PATTERN.search(str(raw or ""))
    if not match:
        return None
    try:
        return datetime.strptime(match.group(0), "%Y-%m-%d").date()
    except ValueError:
        return None


def classify_lifecycle(status: Dict, content: str) -> str:
    """Classify protocol health without pretending unused protocols fired."""
    filename = str(status.get("file") or "").lower()
    early_text = content[:2500].lower()
    if "deprecated" in filename or re.search(r"\bdeprecated\b", early_text):
        return "deprecated"

    if status.get("never_activated"):
        if (
            any(hint in filename for hint in COLD_SOURCE_ONLY_HINTS)
            or "source-only" in early_text
            or "source only" in early_text
            or "reference material" in early_text
        ):
            return "cold/source-only"
        return "dormant"

    if status.get("is_overdue"):
        return "overdue"

    last = first_date(str(status.get("last_activated") or ""))
    if last and (date.today() - last).days <= RECENT_ACTIVE_DAYS:
        return "active"
    return "healthy"


def audit_protocols(include_archived: bool = False) -> Dict:
    """
    Audit all directive files for protocol activation status.

    Returns:
        Dict with summary stats and per-protocol details.
    """
    results = []
    search_dir = DIRECTIVES_DIR

    for md_file in sorted(search_dir.glob("*.md")):
        if not include_archived and "_archived" in str(md_file):
            continue
        status = get_protocol_status(md_file)
        if status:
            results.append(status)

    # Summary
    total = len(results)
    activated = sum(1 for r in results if not r["never_activated"])
    lifecycle_counts = {
        "active": sum(1 for r in results if r.get("lifecycle") == "active"),
        "healthy": sum(1 for r in results if r.get("lifecycle") == "healthy"),
        "dormant": sum(1 for r in results if r.get("lifecycle") == "dormant"),
        "cold/source-only": sum(1 for r in results if r.get("lifecycle") == "cold/source-only"),
        "overdue": sum(1 for r in results if r.get("lifecycle") == "overdue"),
        "deprecated": sum(1 for r in results if r.get("lifecycle") == "deprecated"),
    }
    healthy = lifecycle_counts["active"] + lifecycle_counts["healthy"]
    never_activated = sum(1 for r in results if r["never_activated"])
    total_activations = sum(r["activation_count"] for r in results)

    return {
        "total_protocols": total,
        "active_protocols": lifecycle_counts["active"],
        "activated_protocols": activated,
        "healthy_protocols": healthy,
        "dormant_protocols": lifecycle_counts["dormant"],
        "cold_source_only_protocols": lifecycle_counts["cold/source-only"],
        "overdue_protocols": lifecycle_counts["overdue"],
        "deprecated_protocols": lifecycle_counts["deprecated"],
        "zombie_protocols": lifecycle_counts["overdue"],
        "never_activated": never_activated,
        "total_activations": total_activations,
        "activation_rate": f"{(activated / total * 100):.0f}%" if total else "0%",
        "lifecycle_counts": lifecycle_counts,
        "protocols": results,
    }


def print_audit_report(report: Dict) -> None:
    """Pretty-print the audit report."""
    print("=" * 60)
    print("  PROTOCOL ACTIVATION AUDIT")
    print("=" * 60)
    print(f"  Total Protocols:    {report['total_protocols']}")
    print(f"  Activated Ever:     {report.get('activated_protocols', report['active_protocols'])}")
    print(f"  Active Recent:      {report.get('active_protocols', 'unknown')}")
    print(f"  Healthy Total:      {report.get('healthy_protocols', 'unknown')}")
    print(f"  Dormant:            {report.get('dormant_protocols', 'unknown')}")
    print(f"  Cold/Source-Only:   {report.get('cold_source_only_protocols', 'unknown')}")
    print(f"  Overdue:            {report.get('overdue_protocols', 'unknown')}")
    print(f"  Deprecated:         {report.get('deprecated_protocols', 'unknown')}")
    print(f"  Never Activated:    {report['never_activated']}")
    print(f"  Total Activations:  {report['total_activations']}")
    print(f"  Activation Rate:    {report['activation_rate']}")
    print("-" * 60)

    groups = {
        "OVERDUE (review required)": [p for p in report["protocols"] if p.get("lifecycle") == "overdue"],
        "DORMANT (never activated)": [p for p in report["protocols"] if p.get("lifecycle") == "dormant"],
        "COLD/SOURCE-ONLY": [p for p in report["protocols"] if p.get("lifecycle") == "cold/source-only"],
        "ACTIVE RECENT": [p for p in report["protocols"] if p.get("lifecycle") == "active"],
        "HEALTHY": [p for p in report["protocols"] if p.get("lifecycle") == "healthy"],
        "DEPRECATED": [p for p in report["protocols"] if p.get("lifecycle") == "deprecated"],
    }

    for label, protocols in groups.items():
        if not protocols:
            continue
        print(f"\n  {label} ({len(protocols)}):")
        for p in sorted(protocols, key=lambda x: (x.get("activation_count", 0), x.get("file", "")), reverse=label in {"ACTIVE RECENT", "HEALTHY"}):
            detail = (
                f"overdue since {p['review_date']}"
                if p.get("lifecycle") == "overdue"
                else str(p.get("last_activated") or "not activated")
            )
            print(f"    - {p['file']}: {detail} (count: {p['activation_count']})")

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Protocol Tracker CLI")
    sub = parser.add_subparsers(dest="command")

    # activate
    act = sub.add_parser("activate", help="Activate a protocol (update tracking)")
    act.add_argument("path", help="Path to directive .md file")
    act.add_argument("--note", default="", help="Activation note")

    # audit
    sub.add_parser("audit", help="Audit all protocols for activation status")

    args = parser.parse_args()

    if args.command == "activate":
        result = activate_protocol(args.path, note=args.note)
        if result["success"]:
            print(f"  Activated: {result['file']}")
            print(f"     Date: {result['date']}")
            print(f"     Count: {result.get('old_count', '?')} -> {result.get('new_count', '?')}")
        else:
            print(f"  Failed: {result['error']}")

    elif args.command == "audit":
        report = audit_protocols()
        print_audit_report(report)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
