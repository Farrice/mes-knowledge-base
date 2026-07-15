#!/usr/bin/env python3
"""
COS Primer Gate — the deterministic quality bar for the Operator Primer
(COS v3, Farrice 2026-07-14: "work checked against a standard; if it doesn't
meet the bar it gets redone until the goal is hit, with a capped number of
runs").

The gate is $0 Python so retries are cheap; the RETRY protocol lives in the
workflow (compose → gate → on fail recompose WITH the failure JSON injected →
max 2 retries → ship best attempt with a DEGRADED banner naming the failures).

Checks (each maps to a failure mode Farrice named — regression-pinned by
execution/verify_cos_primer_gate.py):
  structure     — required primer sections present
  actionability — every move carries a startable `→ next:` line
  echo          — primer must not be his journal fed back (8-word shingle
                  overlap vs recent journals above threshold = FAIL)
  attribution   — every board advisory names its seat + expert
  question_ctx  — every question carries inline context/provenance (↳)
  url           — no truncated (`...`) links; live-check http(s) URLs
                  (network errors / --offline downgrade to WARN — never
                  block the morning on wifi)
  recency       — world-pulse lines must read current-year, ≤14 days
  prose         — prose_classifier FLAGGED = fail

Exit codes (matches gates.py convention): 0 = pass · 2 = fail (JSON on
stdout) · 1 = usage error.

CLI:
    python3 execution/cos_primer_gate.py check --file <primer.md> [--offline]
    python3 execution/cos_primer_gate.py check --text "..." [--journal-dir DIR]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JOURNAL_DIR = ROOT / ".agent" / "cos" / "journal"

# ── tunable constants (one block, per plan) ──────────────────────────
ECHO_SHINGLE_WORDS = 8
ECHO_THRESHOLD = 0.15          # >15% of primer shingles found in journals = echo
                               # (a real primer SYNTHESIZES — overlap should be ~0)
ECHO_JOURNAL_FILES = 3         # compare against the last N journal files
URL_TIMEOUT_S = 5
PULSE_MAX_AGE_DAYS = 14
REQUIRED_SECTIONS = ("## Today's 3 moves", "## Board advisories", "## Your questions")
ADVISORY_RE = re.compile(
    r"^\s*-\s*\[(CEO|CFO|COO|Chairman|Mentor|Specialist|Wildcard):\s*[^\]]+\]",
)


def _words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", text.lower())


def _shingles(text: str, n: int = ECHO_SHINGLE_WORDS) -> set:
    w = _words(text)
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def _strip_quoted_data(text: str) -> str:
    """Remove code spans, command lines, and ↳ provenance lines before the
    echo check — quoting a close-command or a goal target verbatim is fine;
    echoing his own prose back is not."""
    out = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("↳") or s.startswith("```") or "`python3" in s:
            continue
        out.append(re.sub(r"`[^`]*`", " ", line))
    return "\n".join(out)


# ── individual checks: each returns (failures, warnings) lists of dicts ──


def check_structure(text: str):
    missing = [s for s in REQUIRED_SECTIONS if s not in text]
    return ([{"code": "structure", "detail": f"missing section(s): {missing}"}]
            if missing else []), []


def check_actionability(text: str):
    m = re.search(r"## Today's 3 moves\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
    if not m:
        return [], []  # structure check owns the missing-section failure
    block = m.group(1)
    moves = re.findall(r"^\s*\d+\.\s+.*(?:\n(?!\s*\d+\.\s|\s*##).*)*", block,
                       re.MULTILINE)
    bad = [i + 1 for i, mv in enumerate(moves) if "→ next:" not in mv]
    if not moves:
        return [{"code": "actionability", "detail": "no numbered moves found"}], []
    return ([{"code": "actionability",
              "detail": f"move(s) {bad} missing a '→ next:' startable step"}]
            if bad else []), []


def check_echo(text: str, journal_dir: Path):
    body = _strip_quoted_data(text)
    primer_shingles = _shingles(body)
    if not primer_shingles:
        return [], []
    journal_shingles: set = set()
    try:
        for jf in sorted(journal_dir.glob("*.md"), reverse=True)[:ECHO_JOURNAL_FILES]:
            journal_shingles |= _shingles(jf.read_text(encoding="utf-8"))
    except Exception:
        return [], [{"code": "echo", "detail": "journal dir unreadable — echo check skipped"}]
    if not journal_shingles:
        return [], []
    overlap = primer_shingles & journal_shingles
    ratio = len(overlap) / len(primer_shingles)
    if ratio > ECHO_THRESHOLD:
        sample = sorted(overlap)[:5]
        return [{"code": "echo",
                 "detail": f"journal-echo ratio {ratio:.2f} > {ECHO_THRESHOLD} "
                           f"— the primer is feeding his own words back. "
                           f"Offending runs (sample): {sample}"}], []
    return [], []


def check_attribution(text: str):
    m = re.search(r"## Board advisories\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
    if not m:
        return [], []
    bad = []
    for line in m.group(1).splitlines():
        s = line.rstrip()
        if re.match(r"^\s*-\s+", s) and not re.match(r"^\s{2,}-", line):
            if not ADVISORY_RE.match(s):
                bad.append(s[:60])
    return ([{"code": "attribution",
              "detail": f"unattributed advisory line(s): {bad} — every advisory "
                        f"must open '[Seat: Name]' (composition standard)"}]
            if bad else []), []


def check_question_context(text: str):
    m = re.search(r"## Your questions\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
    if not m:
        return [], []
    lines = m.group(1).splitlines()
    bad = []
    for i, line in enumerate(lines):
        if re.match(r"^\s*\d+\.\s+", line):
            follow_lines = []
            for nxt in lines[i + 1:]:
                if re.match(r"^\s*\d+\.\s+", nxt):
                    break  # next question owns its own context line
                follow_lines.append(nxt)
            if "↳" not in "\n".join(follow_lines):
                bad.append(line.strip()[:60])
    return ([{"code": "question_ctx",
              "detail": f"question(s) without inline ↳ context: {bad}"}]
            if bad else []), []


def check_urls(text: str, offline: bool):
    failures, warnings = [], []
    urls = re.findall(r"https?://[^\s)>\]]+", text)
    truncated = [u for u in urls if u.rstrip(").,;").endswith("...")
                 or "..." in u]
    if truncated:
        failures.append({"code": "url",
                         "detail": f"truncated link(s): {truncated}"})
    if offline:
        if urls:
            warnings.append({"code": "url", "detail": "offline — liveness not checked"})
        return failures, warnings
    import urllib.request
    for u in [u.rstrip(").,;") for u in urls if "..." not in u][:10]:
        try:
            req = urllib.request.Request(u, method="HEAD",
                                         headers={"User-Agent": "cos-primer-gate/1.0"})
            with urllib.request.urlopen(req, timeout=URL_TIMEOUT_S) as resp:
                if resp.status >= 400:
                    failures.append({"code": "url",
                                     "detail": f"{u} → HTTP {resp.status}"})
        except Exception as e:
            code = getattr(e, "code", None)
            if code and int(code) >= 400 and int(code) not in (403, 405, 429):
                failures.append({"code": "url", "detail": f"{u} → HTTP {code}"})
            else:
                # network flake / bot-blocking / no wifi: warn, never block
                warnings.append({"code": "url",
                                 "detail": f"{u} unverifiable ({type(e).__name__})"})
    return failures, warnings


def check_recency(text: str):
    m = re.search(r"## 🌍? ?World pulse[^\n]*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
    if not m:
        return [], []
    block = m.group(1)
    current_year = datetime.now().year
    stale = []
    for line in block.splitlines():
        years = {int(y) for y in re.findall(r"\b(20[12]\d)\b", line)}
        if years and max(years) < current_year:
            stale.append(line.strip()[:70])
    return ([{"code": "recency",
              "detail": f"world-pulse line(s) dated pre-{current_year}: {stale} "
                        f"(bar: ≤{PULSE_MAX_AGE_DAYS} days, current-year)"}]
            if stale else []), []


def _prose_body(text: str) -> str:
    """Composed prose only — headers, provenance lines, and URLs are document
    STRUCTURE, not prose, and must not trip the classifier."""
    out = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith(("#", "↳", "<!--")):
            continue
        out.append(re.sub(r"https?://\S+", "", line))
    return "\n".join(out)


def check_prose(text: str):
    text = _prose_body(text)
    if not text.strip():
        return [], []
    try:
        r = subprocess.run(
            [sys.executable, str(ROOT / "execution" / "prose_classifier.py"),
             "check", "--text", text],
            capture_output=True, text=True, timeout=30, cwd=ROOT,
        )
        out = r.stdout + r.stderr
        if "FLAGGED" in out:
            return [{"code": "prose", "detail": "prose_classifier verdict: FLAGGED"}], []
        if "WARNING" in out:
            return [], [{"code": "prose", "detail": "prose_classifier verdict: WARNING"}]
    except Exception as e:
        return [], [{"code": "prose",
                     "detail": f"prose_classifier unavailable ({type(e).__name__})"}]
    return [], []


def run_gate(text: str, journal_dir: Path = JOURNAL_DIR,
             offline: bool = False) -> dict:
    failures, warnings = [], []
    for fn in (check_structure, check_actionability, check_attribution,
               check_question_context, check_recency):
        f, w = fn(text)
        failures += f
        warnings += w
    f, w = check_echo(text, journal_dir)
    failures += f
    warnings += w
    f, w = check_urls(text, offline)
    failures += f
    warnings += w
    f, w = check_prose(text)
    failures += f
    warnings += w
    return {"verdict": "PASS" if not failures else "FAIL",
            "failures": failures, "warnings": warnings}


def main() -> int:
    p = argparse.ArgumentParser(prog="cos_primer_gate.py")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("--file", help="primer markdown file")
    c.add_argument("--text", help="primer text inline")
    c.add_argument("--journal-dir", default=str(JOURNAL_DIR))
    c.add_argument("--offline", action="store_true")
    a = p.parse_args()
    if not a.file and not a.text:
        print("usage error: --file or --text required", file=sys.stderr)
        return 1
    text = a.text if a.text else Path(a.file).read_text(encoding="utf-8")
    result = run_gate(text, Path(a.journal_dir), offline=a.offline)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["verdict"] == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
