#!/usr/bin/env python3
"""
Wraps `npx @google/design.md lint` with rich console output and structured logging.

Usage:
    python3 execution/design_md_validate.py <path-to-DESIGN.md>
    python3 execution/design_md_validate.py <path-to-DESIGN.md> --json
    python3 execution/design_md_validate.py <path-to-DESIGN.md> --quiet

Exit codes:
    0  — valid (0 errors, any number of warnings)
    1  — invalid (1+ errors)
    2  — usage / runtime error

Logs every run to .agent/design-md-validations.jsonl for evolution / observability.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG_PATH = ROOT / ".agent" / "design-md-validations.jsonl"

SEVERITY_COLOR = {
    "error": "\033[31m",     # red
    "warning": "\033[33m",   # yellow
    "info": "\033[36m",      # cyan
}
RESET = "\033[0m"
BOLD = "\033[1m"

FIX_HINTS = {
    "broken-ref": "Replace with the correct path or a literal value. Token references must point to a primitive value (e.g., colors.primary, not colors).",
    "missing-primary": "Promote the most-used or most-emotionally-loaded color to `colors.primary`.",
    "contrast-ratio": "Adjust the lighter color lighter or the darker darker until WCAG AA (4.5:1 normal, 3:1 large) is met. Or restrict the variant to large-text-only.",
    "orphaned-tokens": "Either delete the unused token, or document its reservation in `## Do's and Don'ts`.",
    "missing-sections": "Generate stubs from your YAML tokens for the missing sections (Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts).",
    "section-order": "Reorder canonical: Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts.",
    "token-summary": "Informational. Use to detect bloat: > 12 colors or > 18 type levels usually means the system isn't disciplined.",
}


def run_lint(path: Path) -> dict:
    """Run `npx @google/design.md lint <path> --format json` and parse output."""
    if not shutil.which("npx"):
        sys.stderr.write("ERROR: `npx` not found on PATH. Install Node.js to use this tool.\n")
        sys.exit(2)

    cmd = ["npx", "-y", "@google/design.md", "lint", str(path), "--format", "json"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        sys.stderr.write("ERROR: lint timed out after 60s.\n")
        sys.exit(2)

    # The CLI writes JSON to stdout. Stderr is the npx noise.
    stdout = (result.stdout or "").strip()
    if not stdout:
        sys.stderr.write(f"ERROR: empty output from lint. stderr was:\n{result.stderr}\n")
        sys.exit(2)

    # The JSON may be preceded by npx noise on first run; find the first { ... } block
    start = stdout.find("{")
    if start == -1:
        sys.stderr.write(f"ERROR: no JSON found in lint output:\n{stdout[:500]}\n")
        sys.exit(2)
    try:
        return json.loads(stdout[start:])
    except json.JSONDecodeError as e:
        sys.stderr.write(f"ERROR: failed to parse lint JSON: {e}\nFirst 500 chars:\n{stdout[:500]}\n")
        sys.exit(2)


def _infer_rule(message: str) -> str:
    """Infer rule name from message text — the CLI doesn't always emit rule IDs."""
    lower = message.lower()
    if "is defined but never referenced" in lower:
        return "orphaned-tokens"
    if "design system defines" in lower:
        return "token-summary"
    if "missing" in lower and "primary" in lower:
        return "missing-primary"
    if "contrast ratio" in lower or "wcag" in lower:
        return "contrast-ratio"
    if "broken" in lower or "could not resolve" in lower:
        return "broken-ref"
    if "section" in lower and "order" in lower:
        return "section-order"
    if "missing section" in lower or "section is absent" in lower:
        return "missing-sections"
    return "(unknown rule)"


def render_human(report: dict, path: Path) -> int:
    findings = report.get("findings", [])
    summary = report.get("summary", {})
    # CLI uses "infos" (plural) — accept both for forward compat
    info_count = summary.get("infos", summary.get("info", 0))
    error_count = summary.get("errors", 0)
    warning_count = summary.get("warnings", 0)

    print()
    print(f"{BOLD}DESIGN.md validation report{RESET}")
    print(f"  File: {path}")
    print()

    if not findings:
        print(f"  \033[32m✓ Clean.\033[0m No findings.")
    else:
        # Group by severity
        for sev in ("error", "warning", "info"):
            items = [f for f in findings if f.get("severity") == sev]
            if not items:
                continue
            color = SEVERITY_COLOR.get(sev, "")
            print(f"  {color}{BOLD}{sev.upper()}{RESET} ({len(items)})")
            for f in items:
                msg = f.get("message", "")
                rule = f.get("rule") or f.get("id") or _infer_rule(msg)
                ref = f.get("path", "")
                print(f"    • [{rule}] {msg}")
                if ref:
                    print(f"      at: {ref}")
                hint = FIX_HINTS.get(rule)
                if hint:
                    print(f"      \033[2m→ {hint}{RESET}")
            print()

    print(f"  Summary: {error_count} errors, {warning_count} warnings, {info_count} info")
    print()

    return 0 if error_count == 0 else 1


def append_log(path: Path, report: dict, exit_code: int) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "path": str(path),
        "exit_code": exit_code,
        "summary": report.get("summary", {}),
        "finding_count": len(report.get("findings", [])),
    }
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a DESIGN.md against the official spec.")
    parser.add_argument("path", type=Path, help="Path to the DESIGN.md file")
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of human-readable")
    parser.add_argument("--quiet", action="store_true", help="Suppress all output (exit code only)")
    args = parser.parse_args()

    if not args.path.exists():
        sys.stderr.write(f"ERROR: file not found: {args.path}\n")
        return 2
    if not args.path.is_file():
        sys.stderr.write(f"ERROR: not a file: {args.path}\n")
        return 2

    report = run_lint(args.path)

    summary = report.get("summary", {})
    exit_code = 0 if summary.get("errors", 0) == 0 else 1

    if args.json:
        print(json.dumps(report, indent=2))
    elif not args.quiet:
        render_human(report, args.path)

    append_log(args.path, report, exit_code)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
