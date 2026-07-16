---
name: approve-path-silent-drop-invalid-category
problem_signature: "memory_review.py approve prints '✓ Approved → memory None' and stamps the review row approved while store_memory silently rejected the proposed category and wrote nothing — human-approved lessons vanish at the exact moment the operator believes they were banked"
domain: system
tags: [memory, sovereign-db, silent-failure, review-queue, distiller]
date: 2026-07-16
status: active
session: "a9d8e93d-78e2-4cff-8c3e-c2547b1e4070"
---

## Problem

Draining the 19-item pending review queue (the one stale lane found by the 2026-07-16 second-brain wiring audit), two of three approvals reported `✓ Approved fr_… → memory None (pinned: True)` and the queue showed them resolved — but a direct sovereign.db query found only one of the three memories actually existed. Human-approved lessons were being destroyed by the act of approving them. 9 of the 19 queue items carried the exposed category and would all have vanished the same way.

## Root Cause

Two defects compounding:
1. **Vocabulary drift between producer and store**: the weekly distiller judge emits `proposed_category: principle`, but `memory_store.VALID_CATEGORIES["semantic"]` is `preference|pattern|rule|insight|error_pattern`. `store_memory()` handles the mismatch by printing an error and **returning None** — no raise.
2. **Caller trusted the return blindly**: `approve()` in `execution/memory_review.py` took the None, called `pin_memory(None)`, stamped the review row `status='approved', promoted_memory_id=NULL`, and printed a ✓ success line. The only visible symptom was the word "None" inside a success message.

## Approach That Worked

1. **Verify the substrate, not the report**: `sqlite3 .memory/sovereign.db "SELECT id, content FROM memories WHERE …"` for each approved item — confirmed 1 of 3 landed. This single SELECT is what converted "looks done" into "data loss."
2. **Alias-map the producer's vocabulary** in `approve()` before `store_memory`: `{"principle": "insight", "lesson": "insight", "heuristic": "pattern"}` — the distiller's category set is stable, so mapping beats rejecting.
3. **Fail loudly on None**: after `store_memory`, `if memory_id is None: raise SystemExit(...)` BEFORE the status UPDATE — the row stays `pending`; nothing gets marked done that didn't happen.
4. **Recover burned rows**: `UPDATE flagged_review SET status='pending', reviewed_at=NULL, promoted_memory_id=NULL WHERE id IN (…) AND promoted_memory_id IS NULL;` then re-run `approve` through the fixed path — the re-approval doubles as the fix's cold-start proof (both minted real IDs: ab591027, 508b76dc).

## Dead Ends

- Reading only the CLI output to judge success — `tail -1` on the approve loop kept the ✓ line and discarded the store_memory error printed above it; the failure was invisible until the substrate query.
- Considering a `VALID_CATEGORIES` expansion first (adding `principle` as a real category) — viable, but it patches one producer; the alias map + loud-fail guard protects against every future producer's vocabulary drift.

## Verification

`sqlite3 .memory/sovereign.db "SELECT id, category, pinned, substr(content,1,70) FROM memories WHERE json_extract(metadata,'$.promoted_from') IN ('fr_652ee354c05052b4','fr_cd15ebf312bad5a6','fr_faf1cbf8dccaa18e');"` → 3 rows (bce6dbe6 rule, ab591027 insight, 508b76dc insight), all pinned=1. Queue list returns `(empty)`.

## Weaker-Model Trap

A weaker model sees `✓ Approved` and moves on — the success glyph plus a plausible ID-shaped word ("None") pattern-matches to done. It also fixes the symptom by hand-inserting the missing rows without patching `approve()`, leaving the next approval to silently drop again. The trap is trusting a tool's self-report over a one-line substrate query, and repairing data without repairing the path that lost it.

## Pointers

- `execution/memory_review.py` (approve(), the alias map + None guard)
- `execution/memory_store.py:244` (store_memory returns None on invalid tier/category — the contract every caller must check)
- `feedback_ai-memory-dependent-observability.md` (same family: deterministic backstops over self-reports)
- `docs/solutions/2026-07-15-ours-merge-absorbs-silently-drop-branch-content.md` (sibling: status flipped, content missing)
