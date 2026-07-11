#!/usr/bin/env python3
"""Renaissance v2 quality gate — deterministic audit of structure-pure v2 files.

Every v2 file must have: the 3 required sections (Output Contract, Output
Skeleton, Quality Gate), >= 20 lines, no stub markers, and structure-pure-v2
frontmatter. Files that fail are exactly the ones the resume mechanism
(renaissance_queue.py skip-if-exists) would wrongly treat as done.

Usage:
  python3 execution/renaissance_audit.py            # report failures
  python3 execution/renaissance_audit.py --delete   # delete failures so the
                                                    # queue re-includes their originals
"""
import argparse
import glob
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED_SECTIONS = ["## Output Contract", "## Output Skeleton", "## Quality Gate"]
STUB_MARKERS = [
    "[Refactored to v2 structure]",
    "[Define expected output format]",
    # 2026-07-11 dual-session incident: template-slop fingerprints from the
    # rogue Haiku fleet — generic boilerplate pasted identically across files
    # while the actual methodology was amputated.
    'fidelity: "standard"',
    'refactored: "20',
    "Structured framework/system responding to input requirements",
    "├─ Layer 1:",
    "Captures the real practitioner system from source material",
]
MIN_LINES = 20


def v2_files():
    return sorted(
        glob.glob(os.path.join(ROOT, "skills", "*", "references", "prompts-v2", "*.md"))
        + glob.glob(os.path.join(ROOT, "extractions", "*", "prompts-v2", "*.md"))
    )


def audit_file(path):
    """Return list of failure reasons (empty = pass)."""
    text = open(path, encoding="utf-8", errors="replace").read()
    reasons = []
    if any(m in text for m in STUB_MARKERS):
        reasons.append("stub-marker")
    if len(text.splitlines()) < MIN_LINES:
        reasons.append(f"under-{MIN_LINES}-lines")
    lower = text.lower()
    missing = [s for s in REQUIRED_SECTIONS if s.lower() not in lower]
    if missing:
        reasons.append("missing:" + ",".join(s.replace("## ", "") for s in missing))
    if "standard: structure-pure-v2" not in text:
        reasons.append("bad-frontmatter")
    return reasons


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--delete", action="store_true", help="delete failing v2 files")
    ap.add_argument("--quiet", action="store_true", help="only print counts")
    args = ap.parse_args()

    files = v2_files()
    failures = {}
    for f in files:
        reasons = audit_file(f)
        if reasons:
            failures[f] = reasons

    rel = lambda p: os.path.relpath(p, ROOT)
    if not args.quiet:
        for f, reasons in sorted(failures.items()):
            print(f"FAIL  {rel(f)}  [{'; '.join(reasons)}]")
    print(f"\naudited: {len(files)} v2 files · pass: {len(files) - len(failures)} · fail: {len(failures)}")

    if args.delete and failures:
        for f in failures:
            os.remove(f)
        print(f"deleted {len(failures)} failing v2 files — rebuild the wave to re-include their originals")

    sys.exit(1 if failures and not args.delete else 0)


if __name__ == "__main__":
    main()
