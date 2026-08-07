#!/usr/bin/env python3
"""Flag public/revenue copy artifacts missing a Copy Gate Result.

The active written artifact surface should not treat LinkedIn, outreach,
marketplace, checkout, offer, or other revenue-critical copy as publishable
unless it includes the publishable copy gate result or an explicit sidecar skip.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable


DEFAULT_PATHS = (
    "brain",
    "deliverables",
    "research_outputs",
    "strategy_briefs",
)

ARCHIVE_DIR_NAMES = {
    "archive",
    "_archive",
    "archived",
    "deprecated",
}

PUBLIC_REVENUE_MARKERS = {
    "linkedin",
    "public-facing",
    "client-facing",
    "publishable",
    "revenue-critical",
    "marketplace",
    "upwork",
    "contra",
    "fiverr",
    "wellfound",
    "outreach",
    "dm flow",
    "contextual dm",
    "paid bridge",
    "checkout",
    "payment page",
    "sales page",
    "offer page",
    "proposal opener",
    "first comment",
    "comment bank",
    "comment strategy",
}

COPY_MARKERS = {
    "copy",
    "post",
    "hook",
    "cta",
    "dm",
    "comment",
    "proposal",
    "opener",
    "rewrite",
    "publish",
    "send it",
    "buyer language",
    "brand-jack",
    "voice",
    "tension",
    "punch",
}

ROUTING_MARKERS = {
    "copywriting agent",
    "lara acosta",
    "josh sanders",
    "kallaway",
    "erica mallet",
    "publishable-copy-gate",
    "social gate",
}

GATE_RE = re.compile(r"(^|\n)##\s+Copy Gate Result\b", re.IGNORECASE)
ACTIVE_INTENT = "2026-05-10-full-revenue-suite-rebuild"


def iter_markdown(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if path.is_file() and path.suffix.lower() == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(p for p in path.rglob("*.md") if p.is_file())
    return sorted(files)


def is_written_artifact_area(path: Path) -> bool:
    parts = {part.lower() for part in path.parts}
    return "document-artifacts" in parts or "readable-artifacts" in parts


def is_archived(path: Path) -> bool:
    return any(part.lower() in ARCHIVE_DIR_NAMES for part in path.parts)


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def sidecar_paths(path: Path) -> list[Path]:
    return [
        path.with_name(path.name + ".metadata.json"),
        path.with_suffix(path.suffix + ".metadata.json"),
        path.with_suffix(".metadata.json"),
    ]


def has_skip_approval(path: Path) -> bool:
    for sidecar in sidecar_paths(path):
        if not sidecar.exists():
            continue
        data = read_json(sidecar)
        reason = str(data.get("skipReason", "")).strip()
        if data.get("skipCopyGate") is True and reason:
            return True
    return False


def active_intent_metadata(path: Path) -> dict:
    for sidecar in sidecar_paths(path):
        if not sidecar.exists():
            continue
        data = read_json(sidecar)
        if data.get("activeIntent"):
            return data
    return {}


def marker_hits(text: str, markers: Iterable[str]) -> list[str]:
    lowered = text.lower()
    return sorted(marker for marker in markers if marker in lowered)


def requires_copy_gate(path: Path, text: str) -> tuple[bool, list[str]]:
    if path.name.lower() == "readme.md":
        return False, []

    public_hits = marker_hits(text, PUBLIC_REVENUE_MARKERS)
    copy_hits = marker_hits(text, COPY_MARKERS)
    routing_hits = marker_hits(text, ROUTING_MARKERS)

    if routing_hits:
        return True, routing_hits
    if public_hits and copy_hits:
        return True, sorted(set(public_hits + copy_hits))
    return False, []


def scan(paths: list[Path]) -> list[dict]:
    flagged: list[dict] = []
    for path in iter_markdown(paths):
        if is_archived(path) or not is_written_artifact_area(path):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        requires_gate, hits = requires_copy_gate(path, text)
        if not requires_gate:
            continue
        if GATE_RE.search(text):
            metadata = active_intent_metadata(path)
            if metadata.get("activeIntent") == ACTIVE_INTENT:
                missing = strict_copy_gate_issues(text)
                if missing:
                    flagged.append(
                        {
                            "path": str(path),
                            "markers": hits,
                            "reason": "Current AI Misfire revenue-suite copy gate is ceremonial or incomplete.",
                            "missing": missing,
                        }
                    )
            continue
        if has_skip_approval(path):
            continue
        flagged.append(
            {
                "path": str(path),
                "markers": hits,
                "reason": "Public/revenue copy markers found without Copy Gate Result or sidecar skip.",
            }
        )
    return flagged


def strict_copy_gate_issues(text: str) -> list[str]:
    issues: list[str] = []
    checks = [
        ("Verdict: PASS", re.compile(r"\*\*Verdict:\*\*\s*PASS\b", re.IGNORECASE)),
        (
            "Current intent marker",
            re.compile(r"\*\*Current intent marker:\*\*\s*`?2026-05-10-full-revenue-suite-rebuild`?", re.IGNORECASE),
        ),
        (
            "Expert deployment evidence",
            re.compile(r"\*\*Expert deployment evidence:\*\*\s*\S", re.IGNORECASE),
        ),
        (
            "Prose/slop review",
            re.compile(r"\*\*Prose/slop review:\*\*\s*\S", re.IGNORECASE),
        ),
        (
            "User-calibrated baseline",
            re.compile(r"\*\*User-calibrated baseline:\*\*\s*\S", re.IGNORECASE),
        ),
        (
            "Failure addressed",
            re.compile(r"\*\*Failure addressed:\*\*\s*\S", re.IGNORECASE),
        ),
        (
            "Score discipline",
            re.compile(r"\*\*Score discipline:\*\*\s*\S", re.IGNORECASE),
        ),
        ("Revision Applied column", re.compile(r"\|\s*Revision Applied\s*\|", re.IGNORECASE)),
    ]
    for label, regex in checks:
        if not regex.search(text):
            issues.append(label)
    if re.search(r"\b(TBD|TODO|none applied|no revision)\b", text, re.IGNORECASE):
        issues.append("No placeholder or no-revision language in current Copy Gate Result")
    prose_match = re.search(r"\*\*Prose/slop review:\*\*\s*(.+)", text, re.IGNORECASE)
    if prose_match:
        prose_line = prose_match.group(1).strip().lower()
        if "prose_classifier.py" in prose_line and not any(
            marker in prose_line
            for marker in (
                "manual",
                "anti-slop",
                "specificity",
                "classifier is not sufficient",
                "not sufficient",
            )
        ):
            issues.append("Prose/slop review cannot be classifier-only")
    scores = extract_copy_gate_scores(text)
    baseline = extract_user_baseline_score(text)
    verdict_pass = bool(re.search(r"\*\*Verdict:\*\*\s*PASS\b", text, re.IGNORECASE))
    if verdict_pass and baseline is not None and baseline <= 4.5:
        issues.append("PASS despite user-calibrated baseline <= 4.5/10 (must revise/rework and show delta)")
    if scores:
        average = sum(scores) / len(scores)
        if average >= 8.8:
            issues.append("Score inflation: average Copy Gate score >= 8.8")
        if baseline is not None and baseline <= 4.5 and average >= 8.0:
            issues.append("Score inflation: high average score conflicts with low user-calibrated baseline")
        if any(score >= 9.0 for score in scores) and not re.search(
            r"\*\*(Live|Market|User) proof:\*\*\s*\S", text, re.IGNORECASE
        ):
            issues.append("Score inflation: 9+ scores need live market/user proof")
    return issues


def extract_user_baseline_score(text: str) -> float | None:
    match = re.search(r"\*\*User-calibrated baseline:\*\*\s*(.+)", text, re.IGNORECASE)
    if not match:
        return None
    baseline = match.group(1).strip().lower()
    if baseline in {"none", "none available", "n/a", "na"}:
        return None
    # Handle common forms: "3/10", "3-4/10", "rated 3-4", "3 to 4"
    range_match = re.search(r"\b([0-9]+(?:\.[0-9]+)?)\s*(?:-|to)\s*([0-9]+(?:\.[0-9]+)?)\b", baseline)
    if range_match:
        try:
            return float(range_match.group(1))
        except ValueError:
            return None
    num_match = re.search(r"\b([0-9]+(?:\.[0-9]+)?)\b", baseline)
    if not num_match:
        return None
    try:
        return float(num_match.group(1))
    except ValueError:
        return None


def extract_copy_gate_scores(text: str) -> list[float]:
    scores: list[float] = []
    in_gate = False
    for line in text.splitlines():
        if re.match(r"##\s+Copy Gate Result\b", line, re.IGNORECASE):
            in_gate = True
            continue
        if in_gate and line.startswith("## "):
            break
        if not in_gate or not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        if cells[0].lower() in {"dimension", "---"} or set(cells[1]) <= {"-", ":"}:
            continue
        match = re.search(r"\b([0-9]+(?:\.[0-9]+)?)\b", cells[1])
        if not match:
            continue
        try:
            scores.append(float(match.group(1)))
        except ValueError:
            continue
    return scores


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Flag public/revenue copy artifacts missing Copy Gate Result."
    )
    parser.add_argument("paths", nargs="*", help="Files or directories to scan.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    paths = [Path(p) for p in args.paths] if args.paths else [Path(p) for p in DEFAULT_PATHS]
    flagged = scan(paths)

    result = {
        "status": "fail" if flagged else "pass",
        "flagged": flagged,
        "rule": "Active public/revenue copy artifacts need Copy Gate Result unless sidecar skipCopyGate is true with skipReason.",
    }

    if args.json:
        print(json.dumps(result, indent=2))
    elif not flagged:
        print("No ungated public/revenue copy artifacts found.")
    else:
        print(f"Found {len(flagged)} ungated public/revenue copy artifact(s):")
        for item in flagged:
            print(f"- {item['path']}: {', '.join(item['markers'][:10])}")
        print('\nAdd a real "## Copy Gate Result" or sidecar skip:')
        print('  {"skipCopyGate": true, "skipReason": "internal reference only"}')

    return 1 if flagged else 0


if __name__ == "__main__":
    raise SystemExit(main())
