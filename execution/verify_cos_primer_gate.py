#!/usr/bin/env python3
"""
Golden-set regression gate for cos_primer_gate.py (pattern: verify_control_intent.py).

Every failure mode Farrice has named for the COS daily output is pinned here as
a fixture. If a future change to the gate lets one of these ship again, this
script exits 1 and says which. Add a golden case every time he names a new
failure mode — that is the regression loop he asked for (2026-07-14).

Run: python3 execution/verify_cos_primer_gate.py   (exit 0 = all pass)
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cos_primer_gate import run_gate  # noqa: E402

# A synthetic journal the echo fixture lifts from.
SYNTH_JOURNAL = """# Journal — 2026-07-01

## Raw
The thirty day money sprint means three to five thousand collected by mid
August or a reliable recurring stream with the Josh close in motion and the
TrendScale recruiter rescue finished render ready to ship plus warm intro asks
with the brief pack as the artifact for Michelle and Chris this month.

## Open loops
- Sprint lanes ranked and waiting on the Josh nudge
"""

# ── fixtures ─────────────────────────────────────────────────────────

GOOD_PRIMER = """# Operator Primer — 2026-07-14

## Today's 3 moves
1. Nudge Josh on the retainer. Silence is a decision being made without you.
   → next: say `draft the Josh nudge` and send before noon
2. Send the recruiter package. The render is done, only the send is missing.
   → next: `/resume ad-script`, attach sample, hit send
3. One warm referral ask.
   → next: text Michelle, with the brief pack as the artifact

## Delta since yesterday
Sprint day 2. Nothing shipped yet. The calendar trigger for move 1 fired today.

## Board advisories
- [CFO: Alex Hormozi] Track asks made, not revenue felt. Three asks before
  noon is fully in your control; collected cash is a lag measure.
- [Mentor: Robert Greene] Move 2 is finished work withheld — that is a
  confidence pattern, not a scheduling problem. Ship the imperfect artifact.

## Your questions
1. Goal "father-presence" review is due. Recommit as-is or renegotiate?
   ↳ registry target: "Present, engaged father for JJ; the business serves this"
2. What did sleep look like the last few nights?
   ↳ health-rebuild goal targets sleep QUALITY specifically; section 6d stale

## 🌍 World pulse
Nothing cleared the bar today. Stale items suppressed.
"""

ECHO_PRIMER = GOOD_PRIMER.replace(
    "## Delta since yesterday\nSprint day 2. Nothing shipped yet. The calendar trigger for move 1 fired today.",
    """## Delta since yesterday
The thirty day money sprint means three to five thousand collected by mid
August or a reliable recurring stream with the Josh close in motion and the
TrendScale recruiter rescue finished render ready to ship plus warm intro asks
with the brief pack as the artifact for Michelle and Chris this month. The
thirty day money sprint means three to five thousand collected by mid August
or a reliable recurring stream with the Josh close in motion and the TrendScale
recruiter rescue finished render ready to ship plus warm intro asks with the
brief pack as the artifact for Michelle and Chris this month and again the
thirty day money sprint means three to five thousand collected by mid August
or a reliable recurring stream with the Josh close in motion.""")

NO_NEXT_PRIMER = GOOD_PRIMER.replace(
    "   → next: say `draft the Josh nudge` and send before noon\n", "")

UNATTRIBUTED_PRIMER = GOOD_PRIMER.replace(
    "- [CFO: Alex Hormozi] Track asks made, not revenue felt.",
    "- Track asks made, not revenue felt.")

NO_CONTEXT_PRIMER = GOOD_PRIMER.replace(
    "   ↳ registry target: \"Present, engaged father for JJ; the business serves this\"\n",
    "")

TRUNCATED_URL_PRIMER = GOOD_PRIMER.replace(
    "Nothing cleared the bar today. Stale items suppressed.",
    "- **Framework news** — relevant (https://medium.com/@x/the-ai-agent-...)")

STALE_PULSE_PRIMER = GOOD_PRIMER.replace(
    "Nothing cleared the bar today. Stale items suppressed.",
    "- **The AI Agent Framework Landscape in 2025** — what changed and what matters")

MISSING_SECTION_PRIMER = GOOD_PRIMER.replace("## Board advisories", "## Notes")

# (name, fixture, expected_verdict, expected_failure_code or "")
GOLDEN = [
    ("good primer passes",            GOOD_PRIMER,            "PASS", ""),
    ("journal echo fails",            ECHO_PRIMER,            "FAIL", "echo"),
    ("move without next-step fails",  NO_NEXT_PRIMER,         "FAIL", "actionability"),
    ("unattributed advisory fails",   UNATTRIBUTED_PRIMER,    "FAIL", "attribution"),
    ("question without context fails", NO_CONTEXT_PRIMER,     "FAIL", "question_ctx"),
    ("truncated url fails",           TRUNCATED_URL_PRIMER,   "FAIL", "url"),
    ("2025-stale pulse fails",        STALE_PULSE_PRIMER,     "FAIL", "recency"),
    ("missing section fails",         MISSING_SECTION_PRIMER, "FAIL", "structure"),
]


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        jdir = Path(td)
        (jdir / "2026-07-01.md").write_text(SYNTH_JOURNAL, encoding="utf-8")
        failures = []
        for name, fixture, want_verdict, want_code in GOLDEN:
            result = run_gate(fixture, journal_dir=jdir, offline=True)
            got_verdict = result["verdict"]
            got_codes = {f["code"] for f in result["failures"]}
            if got_verdict != want_verdict:
                failures.append(f"{name}: verdict {got_verdict} != {want_verdict} "
                                f"(failures: {sorted(got_codes)})")
            elif want_code and want_code not in got_codes:
                failures.append(f"{name}: expected failure code '{want_code}' "
                                f"not in {sorted(got_codes)}")
        if failures:
            print("REGRESSIONS:")
            for f in failures:
                print(f"  ✗ {f}")
            return 1
        print(f"OK — {len(GOLDEN)} golden cases pass")
        return 0


if __name__ == "__main__":
    sys.exit(main())
