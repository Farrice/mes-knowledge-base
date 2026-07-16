# Approve Path Silently Drops Memories on Invalid Category

**Date**: 2026-07-16
**Problem solved**: `memory_review.py approve` printed "✓ Approved … → memory None (pinned: True)" and marked the review row `approved` — while writing **nothing** to sovereign.db. Human-approved lessons vanished at the exact moment the operator believed they were banked. 9 of 19 items in the July queue were exposed.

**Context**: Draining the pending review queue (the one stale lane found by the 2026-07-16 second-brain wiring audit). Two of three approvals reported `memory None`; a direct sovereign.db query confirmed only one row landed.

---

## Root cause (two defects compounding)

1. **Vocabulary drift between producers and the store**: the weekly distiller judge emits `proposed_category: principle`, but `memory_store.VALID_CATEGORIES["semantic"]` is `preference|pattern|rule|insight|error_pattern`. `store_memory()` handles the mismatch by **returning None** (prints an error, no raise).
2. **The caller trusted the return blindly**: `approve()` took the `None`, pinned it, stamped the review row `approved` with `promoted_memory_id=NULL`, and reported success. The failure was visible only as the word "None" inside a ✓-prefixed success line.

## The fix (execution/memory_review.py, approve())

1. **Normalize known aliases** before storing: `{"principle": "insight", "lesson": "insight", "heuristic": "pattern"}` — the distiller's vocabulary is stable, so mapping beats rejecting.
2. **Fail loudly on None**: if `store_memory` returns None, `raise SystemExit` BEFORE the status update — the row stays `pending`, nothing is marked done that didn't happen.

## Recovery recipe (for rows already burned)

```sql
UPDATE flagged_review SET status='pending', reviewed_at=NULL, promoted_memory_id=NULL
WHERE id IN (...) AND promoted_memory_id IS NULL;
```
then re-run `approve` through the fixed path — which doubles as the fix's cold-start proof.

## The generalizable rule

**A ✓ that carries a None is a silent write failure wearing a success costume.** Any promote/approve/publish path that (a) accepts a foreign producer's enum and (b) commits its own status separately from the actual write MUST verify the write's return value before stamping status — and the deterministic check is one `sqlite3` SELECT away. Same family as `feedback_ai-memory-dependent-observability` (never trust the report; verify the substrate) and the 2026-07-15 EMPTY-ABSORB detector (status flipped, content missing).

## Deploy when
- Any reviewer/promoter tool reports success with a null/empty artifact ID.
- Wiring any new producer (distiller, harvester, judge) whose output categories feed `store_memory` — check its vocabulary against `VALID_CATEGORIES` first.
