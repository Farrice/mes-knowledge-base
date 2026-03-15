#!/usr/bin/env python3
"""
Protocol Tracker — Automated directive activation tracking for Antigravity.

Updates the "Usage Tracking" section in directive Markdown files. Replaces
manual AI tracking with deterministic code that can't be forgotten.

Usage:
    # Activate a protocol (update Last Activated + increment count)
    python execution/protocol_tracker.py activate directives/quality_gate.md

    # Audit all protocols (list activation status, flag zombies)
    python execution/protocol_tracker.py audit

    # From Python:
    from execution.protocol_tracker import activate_protocol, audit_protocols
    activate_protocol("directives/quality_gate.md")
    report = audit_protocols()
"""

import os
import re
import argparse
from datetime import date, datetime
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

    # Write back
    path.write_text(content, encoding="utf-8")
    return result


def get_protocol_status(directive_path: Path) -> Optional[Dict]:
    """
    Read the Usage Tracking section from a directive file.

    Returns:
        Dict with last_activated, activation_count, review_date, is_zombie.
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

    # Zombie detection: never activated OR overdue for review
    status["is_zombie"] = status["never_activated"] or status["is_overdue"]

    return status


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
    active = sum(1 for r in results if not r["never_activated"])
    zombies = sum(1 for r in results if r["is_zombie"])
    never_activated = sum(1 for r in results if r["never_activated"])
    total_activations = sum(r["activation_count"] for r in results)

    return {
        "total_protocols": total,
        "active_protocols": active,
        "zombie_protocols": zombies,
        "never_activated": never_activated,
        "total_activations": total_activations,
        "activation_rate": f"{(active / total * 100):.0f}%" if total else "0%",
        "protocols": results,
    }


def print_audit_report(report: Dict) -> None:
    """Pretty-print the audit report."""
    print("=" * 60)
    print("  PROTOCOL ACTIVATION AUDIT")
    print("=" * 60)
    print(f"  Total Protocols:    {report['total_protocols']}")
    print(f"  Active:             {report['active_protocols']}")
    print(f"  Never Activated:    {report['never_activated']}")
    print(f"  Zombies (overdue):  {report['zombie_protocols']}")
    print(f"  Total Activations:  {report['total_activations']}")
    print(f"  Activation Rate:    {report['activation_rate']}")
    print("-" * 60)

    # Group by status
    zombies = [p for p in report["protocols"] if p["is_zombie"]]
    healthy = [p for p in report["protocols"] if not p["is_zombie"]]

    if zombies:
        print("\n  🔴 ZOMBIES (need attention):")
        for p in zombies:
            reason = "never activated" if p["never_activated"] else f"overdue since {p['review_date']}"
            print(f"    • {p['file']}: {reason} (count: {p['activation_count']})")

    if healthy:
        print(f"\n  ✅ ACTIVE ({len(healthy)}):")
        for p in sorted(healthy, key=lambda x: x["activation_count"], reverse=True):
            print(f"    • {p['file']}: {p['last_activated']} (count: {p['activation_count']})")

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
            print(f"  ✅ Activated: {result['file']}")
            print(f"     Date: {result['date']}")
            print(f"     Count: {result.get('old_count', '?')} → {result.get('new_count', '?')}")
        else:
            print(f"  ❌ Failed: {result['error']}")

    elif args.command == "audit":
        report = audit_protocols()
        print_audit_report(report)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
