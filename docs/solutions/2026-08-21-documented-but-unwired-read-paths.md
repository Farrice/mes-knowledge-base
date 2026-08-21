---
date: 2026-08-21
session: second-brain-awakening
problem_class: harness / memory / retrieval-dormancy
problem_signature: "a memory or knowledge store writes perfectly on launchd schedule yet 'feels dormant' — its retrieval side exists only as a markdown instruction ('always run memory_facade first'), so it fires at model discretion under 5% of prompts while every hook-wired injection path fires on all of them"
tags: [memory, hooks, second-brain, retrieval, sovereign-db, session-brief, dormancy]
---

# Documented-but-unwired read paths: why a healthy memory stack feels dormant

## Problem

The second brain wrote flawlessly (episodic capture minutes-fresh, nightly harvest green for weeks) but Farrice felt it was "dormant and not enhancing execution." Audit receipts proved him right: `memory_facade.py` — declared mandatory in three constitution files — fired ~2.5×/day, while the one hook-wired path (solution-card injection) fired ~55×/day. Same repo, same period.

## Root Cause

Every writer was wired to launchd; every reader was wired to prose. Instructions do not execute; hooks do. Three compounding leaks: (1) no hook ever queried sovereign.db back into a session; (2) the per-exchange Operator Lesson had no sink — 676 lessons evaporated in chat over 3.5 months; (3) the one live injector had no per-session dedupe, so one card became 89% of all injections and trained the model to ignore the banner.

## Approach That Worked

1. Wire reads into hooks, not docs: `_memory_recall_lines()` in `execution/skill_router_hook.py` — sovereign FTS on every routed prompt, firing even when routing abstains.
2. Calibrate precision on the LIVE store, then sabotage-test: floor = ≥3 word-boundary token hits, ≥2 from tokens len≥5, bm25 ≤ −9.0 (junk prompts return nothing; topic prompts recall the right row).
3. Per-session dedupe (`.agent/sessions/seen-injections-<sid>.json`) so no card/memory repeats within one session.
4. Give the high-frequency signal a sink: `execution/operator_ledger.py` scans episodic assistant turns nightly for `Operator Lesson:` lines → `knowledge/lessons/LEDGER.jsonl` + sovereign mirror (`metadata.source='operator-ledger'`, reversible), backfilled 676 lessons.
5. Make dormancy measurable: injections and facade reads bump `access_count`/`last_accessed`.
6. Surface state where eyes are: `execution/memory_pulse.py` one-liner in the SessionStart digest (the review-queue alarm had lived unseen in a launchd log for 26 days).

## Dead Ends

- bm25-only relevance floor: OR-matching let junk prompts ("what time is it") pull strong-looking scores off long rows.
- Substring token hits: 'main' matched inside 'remains' and surfaced an unrelated personal row on a worktree question — word boundaries are mandatory.
- Counting short-token hits equally: 'does'/'back'/'end' co-occur by accident; require ≥2 content-bearing (len≥5) hits.

## Verification

7-prompt precision suite (junk → silent, topic → correct row, including a backfilled Operator Lesson surfacing on a LinkedIn prompt); dedupe re-run injects nothing twice; access_count before/after diff shows only returned rows moved; ledger backfill idempotent (second run +0).

## Weaker-Model Trap

A weaker model will "fix" dormancy by adding MORE capture (new inboxes, new stores) or by strengthening the instruction text. Neither executes. The diagnostic is a fires-per-day diff between hook-wired and documented paths; a 20×+ gap means install a hook, not write more prose.

## Pointers

- `execution/skill_router_hook.py` — `_memory_recall_lines`, `_load_seen`/`_mark_seen`
- `execution/operator_ledger.py`, `knowledge/lessons/LEDGER.jsonl`
- `execution/memory_pulse.py`, `execution/hooks/session_brief.py`
- Plan + full audit receipts: `~/.claude/plans/https-www-youtube-com-watch-v-teyaltxi-e-fluffy-cascade.md`
