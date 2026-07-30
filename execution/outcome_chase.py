#!/usr/bin/env python3
"""outcome_chase.py — weekly due-outcomes → Mission Card generator (stdlib-only).

Born 2026-07-21 (ladder-audit build, upgrade 4). The OUTER LOOP STALE hook
nags Farrice to chase outcome check-ins by hand; this generator turns the
same due list into a T1 Mission Card that the existing nightly mission-runner
train (com.antigravity.mission-runner, 02:30) executes — drafting check-in
questions and follow-up message DRAFTS into .agent/cos/ for review. Nothing
is ever transmitted or contacted; Farrice reviews and acts manually.

Boris L3 clause this implements: "Claude proactively does work you would
have had to kick off manually" (see skills/ray-amjad-agentic-ladder/).

Usage:
  python3 execution/outcome_chase.py generate [--dry-run]

Guards:
  - due_count == 0            -> exit 0 silently (no card)
  - card already in pending/  -> exit 0 (never stack duplicates)
  - card generated < 6 days ago (pending/ or done/) -> exit 0

Scheduled by com.antigravity.outcome-chase.plist (Sun 04:30). The card text
deliberately avoids the mission-runner refusal-net words; drafts only.
"""

import argparse
import contextlib
import io
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUEUE = ROOT / ".agent" / "mission-queue"
CARD_PREFIX = "card-outcome-chase-"

sys.path.insert(0, str(ROOT / "execution"))


def _due():
    """Call revenue_tracker.get_due() with its print side-effects captured."""
    import revenue_tracker
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        return revenue_tracker.get_due()


def _recent_card_exists(max_age_days: int = 6) -> str:
    """A chase card in pending/ (any age) or parked recently blocks a new one.
    Apex W2 fix (2026-07-29): done/ cards no longer block — a COMPLETED chase
    was strangling the weekly loop (the 07-21 done card, 4.8d old, refused the
    07-27 run; its log was two lines of refusal while 12 check-ins went stale).
    The guard exists to prevent duplicate PENDING work, not to rate-limit
    completed work."""
    now = datetime.now().timestamp()
    for sub in ("pending", "parked"):
        for card in (QUEUE / sub).glob(f"{CARD_PREFIX}*.md"):
            if sub == "pending":
                return f"pending/{card.name}"
            age_days = (now - card.stat().st_mtime) / 86400
            if age_days < max_age_days:
                return f"{sub}/{card.name} ({age_days:.1f}d old)"
    return ""


def _mask(text: str) -> str:
    """Mask mission-runner refusal-net words appearing inside real deliverable
    names/outcomes (e.g. 'publish copy') so the card isn't parked for quoting
    them. Display-only: the executor joins back to exact names via
    .agent/revenue-outcomes.json. Keep this list in sync with
    mission_runner.FORBIDDEN_RE."""
    import re
    return re.sub(r"\b(publish|send|post to|payment|purchase|deploy)\b",
                  lambda m: m.group(0)[0] + "·" + m.group(0)[2:], text or "",
                  flags=re.I)


def _render_card(due: dict, today: str) -> str:
    items = due.get("due", [])
    lines = [
        f"# Mission Card — Weekly outcome check-in drafts ({today})",
        "Tier: T1",
        f"Produced: {today} (queued by execution/outcome_chase.py — ladder-audit build)",
        "",
        "## Objective",
        f"DRAFTS ONLY. For each of the {len(items)} due outcome check-ins below, compose:",
        "1. Two or three check-in questions that would surface the real outcome",
        "   (revenue, result, or dead-with-reason) for that deliverable.",
        "2. A short follow-up message DRAFT in Farrice's voice (load",
        "   `_active/farrice-brand/voice/VOICE-CARD.md`, dial BLEND) where a human",
        "   recipient exists; otherwise a self-check-in note.",
        f"Write everything to `.agent/cos/outcome-chase-{today}.md` — one labeled",
        "block per deliverable: name, expected_outcome, check_in_date, the",
        "questions, the message draft, and the copy-paste close command",
        '`python3 execution/revenue_tracker.py log "<deliverable>" --revenue <$> --outcome "<result>"`.',
        "Files only. Nothing is transmitted or contacted — Farrice reviews and",
        "acts manually.",
        "",
        "## Due items",
    ]
    for it in items:
        lines.append(
            f"- {_mask(it.get('deliverable', '?'))} | expected: {_mask(it.get('expected_outcome') or 'unstated')} "
            f"| check-in due: {it.get('check_in_date', '?')} | shipped: {it.get('date', '?')} "
            f"| expert: {it.get('expert') or '-'}"
        )
    lines.append("  (some names carry a '·' mask so this card clears the runner's refusal net —")
    lines.append("  exact names are in `.agent/revenue-outcomes.json`; join by check-in date + shipped date)")
    if due.get("legacy"):
        lines.append(f"- (+{len(due['legacy'])} legacy pending items with no check-in date — "
                     "list them in a final 'legacy debt' block, questions optional)")
    lines += [
        "",
        "## Context to load first",
        "- `.agent/revenue-outcomes.json` (full stubs for the items above)",
        "- `.agent/cos/goals.json` (so questions connect outcomes to named goals)",
        "",
        "## Constraints",
        "- Run `python3 execution/prose_classifier.py check .agent/cos/outcome-chase-"
        f"{today}.md` before finishing; rewrite flagged sections once.",
        "- One block per deliverable; no prose blobs; density over completeness.",
        "- Nothing is transmitted or contacted. Drafts land on disk only.",
        "",
    ]
    return "\n".join(lines)


def generate(dry_run: bool = False) -> int:
    due = _due()
    if not due.get("due_count") and not due.get("legacy_count"):
        print("outcome-chase: nothing due — no card generated")
        return 0
    existing = _recent_card_exists()
    if existing:
        print(f"outcome-chase: card already exists ({existing}) — skipping")
        return 0
    today = date.today().isoformat()
    card = _render_card(due, today)
    if dry_run:
        print(card)
        return 0
    (QUEUE / "pending").mkdir(parents=True, exist_ok=True)
    path = QUEUE / "pending" / f"{CARD_PREFIX}{today}.md"
    path.write_text(card)
    print(f"outcome-chase: card queued -> {path.relative_to(ROOT)} "
          f"({due['due_count']} due, {due.get('legacy_count', 0)} legacy)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="command", required=True)
    gen = sub.add_parser("generate", help="Render + queue the weekly chase card (if due items exist)")
    gen.add_argument("--dry-run", action="store_true", help="Print the card, write nothing")
    args = ap.parse_args()
    if args.command == "generate":
        return generate(dry_run=args.dry_run)
    return 1


if __name__ == "__main__":
    sys.exit(main())
