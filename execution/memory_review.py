#!/usr/bin/env python3
"""
Memory Review — Human-in-loop CLI for distilled flagged_review queue.

Sprint 6 (2026-05-25): the only way to promote distilled rules from
`flagged_review` into the semantic memory tier. Auto-promotion is
explicitly off — see feedback rule "auto-evolution-cant-substitute-for-ground-truth".

Usage:
    python3 execution/memory_review.py list                   # pending queue
    python3 execution/memory_review.py list --status all      # all (pending/approved/rejected)
    python3 execution/memory_review.py show <id>              # full detail
    python3 execution/memory_review.py approve <id>           # promote to semantic memory (pinned)
    python3 execution/memory_review.py approve <id> --no-pin  # promote unpinned
    python3 execution/memory_review.py reject <id> [--reason "..."]
    python3 execution/memory_review.py purge --rejected --older-than 30  # housekeeping
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))

from memory_store import DB_PATH, store_memory, pin_memory  # noqa: E402


def list_pending(status: str = "pending", limit: int = 50) -> List[dict]:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    if status == "all":
        rows = conn.execute("""
            SELECT id, proposed_tier, proposed_category, judge_score, status,
                   created_at, reviewed_at, promoted_memory_id, proposed_content
            FROM flagged_review
            ORDER BY created_at DESC
            LIMIT ?
        """, (limit,)).fetchall()
    else:
        rows = conn.execute("""
            SELECT id, proposed_tier, proposed_category, judge_score, status,
                   created_at, reviewed_at, promoted_memory_id, proposed_content
            FROM flagged_review
            WHERE status = ?
            ORDER BY judge_score DESC, created_at DESC
            LIMIT ?
        """, (status, limit)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_one(fid: str) -> Optional[dict]:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    row = conn.execute("SELECT * FROM flagged_review WHERE id = ?", (fid,)).fetchone()
    conn.close()
    return dict(row) if row else None


def approve(fid: str, pin: bool = True) -> dict:
    """Promote a flagged_review row into the semantic memory tier."""
    fr = get_one(fid)
    if not fr:
        raise SystemExit(f"Not found: {fid}")
    if fr["status"] != "pending":
        raise SystemExit(f"Already {fr['status']}: {fid} (reviewed {fr.get('reviewed_at')})")

    metadata = {}
    if fr.get("proposed_metadata"):
        try:
            metadata = json.loads(fr["proposed_metadata"])
        except json.JSONDecodeError:
            pass
    metadata.update({
        "promoted_from": fid,
        "judge_score": fr["judge_score"],
        "judge_rationale": fr.get("judge_rationale"),
        "source_memory_ids": json.loads(fr.get("source_memory_ids") or "[]"),
    })

    # The distiller judge emits categories outside memory_store.VALID_CATEGORIES
    # (e.g. 'principle'); normalize instead of dropping the approved memory.
    CATEGORY_ALIASES = {"principle": "insight", "lesson": "insight", "heuristic": "pattern"}
    category = CATEGORY_ALIASES.get(fr["proposed_category"], fr["proposed_category"])

    memory_id = store_memory(
        tier=fr["proposed_tier"],
        category=category,
        content=fr["proposed_content"],
        metadata=metadata,
    )
    if memory_id is None:
        raise SystemExit(
            f"store_memory rejected tier={fr['proposed_tier']!r} category={category!r} "
            f"for {fid} — row left pending, nothing written"
        )

    if pin:
        pin_memory(memory_id)

    now = datetime.now(timezone.utc).isoformat()
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("""
        UPDATE flagged_review
        SET status = 'approved', reviewed_at = ?, promoted_memory_id = ?
        WHERE id = ?
    """, (now, memory_id, fid))
    conn.commit()
    conn.close()

    return {"flagged_id": fid, "memory_id": memory_id, "pinned": pin}


TASTE_GUARD = ("voice", "tone", "taste", "brand", "content style", "writing style",
               "persona", "farrice's voice", "linkedin post", "substack", "parallax")


def auto_promote(threshold: float = 9.0) -> list:
    """Act-then-veto lane (Farrice decision 2026-07-24): pending rules scored
    >= threshold auto-promote to a PROVISIONAL memory (labeled in content,
    unpinned) unless any taste-guard keyword appears — taste/voice/content
    rules NEVER auto-promote. Veto with `veto <id>`; bless with `bless <id>`."""
    promoted = []
    for fr in list_pending("pending", limit=100):
        if (fr.get("judge_score") or 0) < threshold:
            continue
        body = (fr.get("proposed_content") or "").lower()
        if any(k in body for k in TASTE_GUARD):
            continue
        full = get_one(fr["id"])
        full["proposed_content"] = ("[PROVISIONAL — auto-promoted, unreviewed; "
                                    f"veto: memory_review.py veto {fr['id']}]\n"
                                    + (full["proposed_content"] or ""))
        # reuse approve()'s promote path via a temporary in-place content swap
        conn = sqlite3.connect(str(DB_PATH))
        conn.execute("UPDATE flagged_review SET proposed_content = ? WHERE id = ?",
                     (full["proposed_content"], fr["id"]))
        conn.commit(); conn.close()
        # Provisionality marker lives in the content prefix (the table's CHECK
        # constraint allows only pending/approved/rejected statuses).
        res = approve(fr["id"], pin=False)
        promoted.append(res)
    return promoted


def _get_provisional(fid: str) -> dict:
    fr = get_one(fid)
    if not fr:
        raise SystemExit(f"Not found: {fid}")
    if fr["status"] != "approved" or not (fr.get("proposed_content") or "").startswith("[PROVISIONAL"):
        raise SystemExit(f"Not a provisional promotion (status={fr['status']}): {fid}")
    return fr


def veto(fid: str) -> dict:
    """Retro-veto a provisional auto-promotion: delete the promoted memory,
    mark the review row rejected."""
    fr = _get_provisional(fid)
    mid = fr.get("promoted_memory_id")
    conn = sqlite3.connect(str(DB_PATH))
    if mid:
        conn.execute("DELETE FROM memories WHERE id = ?", (mid,))
    conn.execute("UPDATE flagged_review SET status = 'rejected', reviewed_at = ?, "
                 "judge_rationale = COALESCE(judge_rationale,'') || ' | VETOED provisional' "
                 "WHERE id = ?", (datetime.now(timezone.utc).isoformat(), fid))
    conn.commit(); conn.close()
    return {"flagged_id": fid, "deleted_memory": mid}


def bless(fid: str) -> dict:
    """Confirm a provisional auto-promotion: strip the provisional label, pin."""
    fr = _get_provisional(fid)
    mid = fr.get("promoted_memory_id")
    conn = sqlite3.connect(str(DB_PATH))
    if mid:
        row = conn.execute("SELECT content FROM memories WHERE id = ?", (mid,)).fetchone()
        if row and row[0]:
            cleaned = row[0].split("]\n", 1)[-1] if row[0].startswith("[PROVISIONAL") else row[0]
            conn.execute("UPDATE memories SET content = ? WHERE id = ?", (cleaned, mid))
    cleaned_row = (fr.get("proposed_content") or "").split("]\n", 1)[-1]
    conn.execute("UPDATE flagged_review SET proposed_content = ? WHERE id = ?", (cleaned_row, fid))
    conn.commit(); conn.close()
    if mid:
        pin_memory(mid)
    return {"flagged_id": fid, "memory_id": mid, "pinned": True}


def reject(fid: str, reason: Optional[str] = None) -> dict:
    fr = get_one(fid)
    if not fr:
        raise SystemExit(f"Not found: {fid}")
    if fr["status"] != "pending":
        raise SystemExit(f"Already {fr['status']}: {fid}")

    now = datetime.now(timezone.utc).isoformat()
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("""
        UPDATE flagged_review
        SET status = 'rejected',
            reviewed_at = ?,
            judge_rationale = COALESCE(?, judge_rationale)
        WHERE id = ?
    """, (now, f"REJECTED: {reason}" if reason else None, fid))
    conn.commit()
    conn.close()
    return {"flagged_id": fid, "status": "rejected", "reason": reason}


def purge(rejected: bool = False, older_than_days: int = 30) -> int:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=older_than_days)).isoformat()
    conn = sqlite3.connect(str(DB_PATH))
    if rejected:
        cur = conn.execute("""
            DELETE FROM flagged_review
            WHERE status = 'rejected' AND reviewed_at < ?
        """, (cutoff,))
    else:
        cur = conn.execute("""
            DELETE FROM flagged_review
            WHERE status IN ('rejected', 'approved') AND reviewed_at < ?
        """, (cutoff,))
    deleted = cur.rowcount
    conn.commit()
    conn.close()
    return deleted


def render_list(rows: List[dict]) -> None:
    if not rows:
        print("(empty)")
        return
    print(f"\n{'ID':20s} {'score':>6s} {'status':10s} {'category':12s} {'created':30s}")
    print("─" * 100)
    for r in rows:
        excerpt = r["proposed_content"].split("\n", 1)[0][:80]
        print(f"{r['id']:20s} {r['judge_score']:>6.1f} {r['status']:10s} "
              f"{r['proposed_category']:12s} {r['created_at']:30s}")
        print(f"  → {excerpt}")
    print(f"\n({len(rows)} rows)")


def render_one(fr: dict) -> None:
    print("─" * 70)
    print(f"FLAGGED REVIEW: {fr['id']}")
    print("─" * 70)
    print(f"Status:           {fr['status']}")
    print(f"Judge score:      {fr['judge_score']}/10")
    print(f"Judge rationale:  {fr.get('judge_rationale')}")
    print(f"Proposed tier:    {fr['proposed_tier']}")
    print(f"Proposed cat:     {fr['proposed_category']}")
    print(f"Created:          {fr['created_at']}")
    if fr.get("reviewed_at"):
        print(f"Reviewed:         {fr['reviewed_at']}")
    if fr.get("promoted_memory_id"):
        print(f"Promoted as:      {fr['promoted_memory_id']}")
    print()
    print("PROPOSED CONTENT:")
    print(fr["proposed_content"])
    print()
    src = json.loads(fr.get("source_memory_ids") or "[]")
    print(f"Source memories ({len(src)}):")
    for sid in src[:10]:
        print(f"  - {sid}")
    if len(src) > 10:
        print(f"  ... and {len(src) - 10} more")


def main() -> int:
    parser = argparse.ArgumentParser(description="Memory Review — human approval queue")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="List flagged proposals")
    p_list.add_argument("--status", default="pending",
                       choices=["pending", "approved", "rejected", "all"])
    p_list.add_argument("--limit", type=int, default=50)

    p_show = sub.add_parser("show", help="Show full detail for a proposal")
    p_show.add_argument("id")

    p_approve = sub.add_parser("approve", help="Promote to semantic memory")
    p_approve.add_argument("id")
    p_approve.add_argument("--no-pin", action="store_true",
                          help="Don't pin the promoted memory (default: pin)")

    p_reject = sub.add_parser("reject", help="Reject (won't be promoted)")
    p_reject.add_argument("id")
    p_reject.add_argument("--reason", help="Optional rejection rationale")

    p_auto = sub.add_parser("auto-promote", help="Provisionally promote pending rules ≥9.0 (taste-guarded)")
    p_auto.add_argument("--threshold", type=float, default=9.0)

    p_veto = sub.add_parser("veto", help="Retro-veto a provisional auto-promotion")
    p_veto.add_argument("id")

    p_bless = sub.add_parser("bless", help="Confirm a provisional auto-promotion (strip label, pin)")
    p_bless.add_argument("id")

    p_purge = sub.add_parser("purge", help="Delete old reviewed entries")
    p_purge.add_argument("--rejected", action="store_true",
                        help="Only purge rejected (default: both approved+rejected)")
    p_purge.add_argument("--older-than", type=int, default=30,
                        help="Days threshold (default 30)")

    args = parser.parse_args()

    if args.command == "list":
        render_list(list_pending(args.status, args.limit))
        return 0

    if args.command == "show":
        fr = get_one(args.id)
        if not fr:
            print(f"Not found: {args.id}", file=sys.stderr)
            return 1
        render_one(fr)
        return 0

    if args.command == "approve":
        result = approve(args.id, pin=not args.no_pin)
        print(f"✓ Approved {result['flagged_id']} → memory {result['memory_id']} "
              f"(pinned: {result['pinned']})")
        return 0

    if args.command == "reject":
        result = reject(args.id, args.reason)
        print(f"✓ Rejected {result['flagged_id']}")
        return 0

    if args.command == "auto-promote":
        results = auto_promote(threshold=args.threshold)
        for r in results:
            print(f"✓ PROVISIONAL {r['flagged_id']} → memory {r['memory_id']} (unpinned; veto/bless available)")
        print(f"{len(results)} auto-promoted")
        return 0

    if args.command == "veto":
        r = veto(args.id)
        print(f"✓ Vetoed {r['flagged_id']} (deleted memory {r['deleted_memory']})")
        return 0

    if args.command == "bless":
        r = bless(args.id)
        print(f"✓ Blessed {r['flagged_id']} → memory {r['memory_id']} pinned")
        return 0

    if args.command == "purge":
        deleted = purge(rejected=args.rejected, older_than_days=args.older_than)
        print(f"Purged {deleted} rows (>{args.older_than}d old)")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
