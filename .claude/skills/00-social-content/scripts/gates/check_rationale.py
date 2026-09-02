#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check A — the rationale gatekeeper (AIOS-190 W2, the reasoning spine).

Sibling of measure_text_contrast.py / dead_space.py. A SCRIPT-measured, non-negotiable
LOCK the builder MUST pass at the TOP of Step 3 (generation), BEFORE it generates anything.

WHAT IT VERIFIES (presence + completeness ONLY — NOT quality):
  - rationale.md exists.
  - All 4 required sections are present (by header) AND non-empty.
  - The ambiguity section (#4) is non-empty AND not a forbidden filler ("n/a", "none",
    "no ambiguity" with no following reasoning, "tbd", "-", etc.).

WHY (the test-09-06 lesson): prompt-discipline is the FIRST thing the model drops under
pressure — "writing the rationale IS the thinking" only holds if a scripted lock refuses to
let generation start without it. This gate does NOT judge whether the reasoning is GOOD
(that is vision/expensive/subjective and lives in the gabarito + the by-eye golden set). It
only refuses to proceed when the thinking artifact is absent or hollow.

The 4 required sections (matched case-insensitively, header text may carry a leading
number/marker like "1." / "①" / "## "):
  1. Form + tree-path-with-why
  2. Per-block breakdown
  3. Pipeline
  4. Ambiguity (examined)

Exit codes:
  0  -> all 4 sections present + non-empty (incl. ambiguity) -> generation may proceed.
  1  -> usage / file-not-found error.
  2  -> a section is missing or empty (incl. an empty/filler ambiguity section) -> BLOCK.

Usage:
    uv run check_rationale.py --rationale <template_dir>/rationale.md
"""
import argparse
import re
import sys
from pathlib import Path


def _force_utf8_streams() -> None:
    """UTF-8 stdout/stderr so reason glyphs never crash a cp1252 Windows console."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


# Each required section: a stable key + the substrings (any one) that identify its header.
# Matched against the header text with markers/numbering stripped, case-insensitive.
REQUIRED_SECTIONS = [
    ("form", ("form",)),                 # "Form + tree-path-with-why"
    ("blocks", ("per-block", "per block", "block breakdown")),
    ("pipeline", ("pipeline",)),
    ("ambiguity", ("ambiguity",)),
]

# Filler that makes the ambiguity section worthless. The test is "did it weigh
# alternatives?" — "no ambiguity BECAUSE <reason>" is VALID and passes (it has real
# content); a bare "n/a" / "none" / "no ambiguity" with nothing else is FORBIDDEN.
FORBIDDEN_AMBIGUITY = {
    "", "n/a", "na", "none", "no ambiguity", "no ambiguity.", "tbd", "todo",
    "-", "--", "—", "n/a.", "none.", "n.a.", "not applicable", "no",
}

HEADER_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.*\S)\s*$")


def strip_marker(header_text: str) -> str:
    """Drop a leading numbering/marker (1. / 1) / ① / - / *) from a header's text."""
    t = header_text.strip()
    # circled digits ①..⑨ and similar
    t = re.sub(r"^[①-⑳⓪]\s*", "", t)
    # "1." / "1)" / "1 -" leading number
    t = re.sub(r"^\d+\s*[.)\-:]\s*", "", t)
    # leading bullet
    t = re.sub(r"^[-*]\s+", "", t)
    return t.strip()


def parse_sections(text: str) -> list[tuple[str, str]]:
    """Split markdown into (header_text_normalized, body) pairs by ATX (#) headers.

    Returns the normalized header text (marker/numbering stripped, lowercased) and the
    body content (everything until the next header), stripped.
    """
    lines = text.splitlines()
    sections: list[tuple[str, list[str]]] = []
    current: tuple[str, list[str]] | None = None
    for line in lines:
        m = HEADER_RE.match(line)
        if m:
            if current is not None:
                sections.append(current)
            header = strip_marker(m.group(2)).lower()
            current = (header, [])
        elif current is not None:
            current[1].append(line)
    if current is not None:
        sections.append(current)
    return [(h, "\n".join(body).strip()) for h, body in sections]


def find_section(sections: list[tuple[str, str]], needles: tuple[str, ...]) -> str | None:
    """Return the body of the first section whose header contains any needle; None if absent."""
    for header, body in sections:
        if any(n in header for n in needles):
            return body
    return None


def ambiguity_is_filler(body: str) -> bool:
    """True when the ambiguity body is empty or a forbidden bare filler."""
    norm = body.strip().lower()
    if norm in FORBIDDEN_AMBIGUITY:
        return True
    # A body that is ONLY punctuation/whitespace is filler too.
    if not re.search(r"[a-z0-9]", norm):
        return True
    return False


def evaluate(text: str) -> dict:
    """Combine section presence/completeness into a verdict dict (pure, unit-tested)."""
    sections = parse_sections(text)
    missing: list[str] = []
    empty: list[str] = []
    for key, needles in REQUIRED_SECTIONS:
        body = find_section(sections, needles)
        if body is None:
            missing.append(key)
        elif not body.strip():
            empty.append(key)

    ambiguity_filler = False
    amb_body = find_section(sections, ("ambiguity",))
    if amb_body is not None and amb_body.strip() and ambiguity_is_filler(amb_body):
        ambiguity_filler = True

    ok = not missing and not empty and not ambiguity_filler
    reasons = []
    if missing:
        reasons.append(f"missing section(s): {', '.join(missing)}")
    if empty:
        reasons.append(f"empty section(s): {', '.join(empty)}")
    if ambiguity_filler:
        reasons.append("ambiguity section is filler (n/a/none/empty) — it must show "
                       "the alternatives were weighed (ruling one out WITH a reason is valid)")
    return {
        "ok": ok,
        "missing": missing,
        "empty": empty,
        "ambiguity_filler": ambiguity_filler,
        "reason": "; ".join(reasons) if reasons else "all 4 sections present and non-empty",
    }


def main() -> int:
    _force_utf8_streams()
    ap = argparse.ArgumentParser(description="Check A — rationale.md presence + completeness gate.")
    ap.add_argument("--rationale", required=True, type=Path)
    args = ap.parse_args()

    if not args.rationale.exists():
        print(f"[block] rationale.md not found: {args.rationale}", file=sys.stderr)
        print("  Step 3 (generation) is LOCKED until rationale.md is written FIRST "
              "(the reasoning IS the thinking).", file=sys.stderr)
        return 2

    text = args.rationale.read_text(encoding="utf-8")
    res = evaluate(text)

    print(f"Check A — rationale gate on {args.rationale.name}:")
    print(f"  verdict = {'PASS' if res['ok'] else 'BLOCK'} — {res['reason']}")
    if res["ok"]:
        return 0
    print(f"[block] {res['reason']}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
