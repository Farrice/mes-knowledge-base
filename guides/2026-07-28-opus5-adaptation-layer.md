---
date: 2026-07-28
session: opus5-adaptation-layer
tier: operator-guide
status: enriched
---

# Self-Heal + Execution Receipt + Failure Learner — What We Built 2026-07-27/28 and How to Use It

> The session that answered "am I being fooled into thinking things ran?" with
> machinery instead of reassurance — then made the machinery repair, learn, and
> commit without you.

## ⚡ If you only read 10 lines

- **You don't run any of this.** Session close sweeps + heals; session open shows only what needs judgment; `/cos` reports the residue.
- `python3 execution/self_heal.py report` — classify every harness failure AUTO / EVIDENCE / JUDGMENT, read-only.
- `python3 execution/self_heal.py heal` — apply mechanical repairs; each verifies green or reports COULD NOT FIX; commits are scoped to the healer's declared files, never `git add -A`.
- `python3 execution/execution_receipt.py` — proof of what ACTUALLY ran this session (skills at T1/T2, gates, grounding) from the tool log, not from claims.
- `python3 execution/failure_learning.py` — recurrence → written rules in `evolution_store/failure-registry.md` (empty 115 days; now fills itself). Thresholds pinned: 3 fails = CHRONIC, 5 heals/5 days = RECURRING, 7 days unresolved = ROTTING.
- Doctrine line: **prose is not a mechanism — only hooks, launchd, and spine steps fire.**
- Handoffs: near-duplicate threads now AUTO-ADOPT (`--new-thread` to force separate); a missing Do-NOT-Rebuild section is scaffolded into the body.
- Escape hatches: `SELF_HEAL_NO_AUTOCOMMIT=1`, `heal --no-commit`.
- Verifiers: `verify_self_heal` 38 · `verify_failure_learning` 30 · `verify_execution_receipt` 34 — all on the Sunday fleet; every safety property has a negative control.
- First thing to run next session: nothing — read what `pending_decisions_hook` prints at open.

## Command table

| Command | What it does | When |
|---|---|---|
| `/self-heal` | report by default, heal on request | On demand; automatic at session close |
| `python3 execution/self_heal.py report` | classify only, read-only | Curious mid-session |
| `python3 execution/self_heal.py heal --no-commit` | repair, caller owns the commit | Inside spines/scripts |
| `python3 execution/execution_receipt.py --all` | receipts for every producing session, 7 days | "Did the machinery actually run?" |
| `python3 execution/failure_learning.py --report` | recurrence scan, writes nothing | Reviewing what the system learned |
| `python3 execution/handoff_store.py save … --new-thread` | force a genuinely separate thread past auto-adopt | Rare, deliberate |

## Mental model

One pipeline, four stations, all deterministic:

**Record** (session_ledger manifest: every skill/workflow/gate that fired) →
**Judge** (execution_receipt: claims vs tool log; self_heal: who fixes this?) →
**Repair** (session-close spine step, scoped commit, re-verify or admit failure) →
**Learn** (failure_learning: recurrence becomes a registry rule; JUDGMENT residue greets you at next session open).

The classification is the whole idea: AUTO = fix silently · EVIDENCE = git already proves deliberateness, fix and mention once · JUDGMENT = never auto-touched. Only the cost gate and factual veto block; everything here reports.

## Honest edges

- `generate_slash_commands.py` is broken (`--check` says 2,398 to append; `main()` writes ~6 lines) — self-heal correctly refuses to retry it; needs a real fix.
- `platform_compiler` drift is classify-only by decision — auto-write earns trust after a week of clean runs.
- `handoff_store.py` improvements are live-tested but have **no verifier suite** yet.
- The three suites cost real debugging: pinned thresholds (a test reading the constant it tests detects nothing), AST over string-matching (3 false REDs from matching docstrings), sandbox probes must redirect the audit log too.

## Pointers

Solution Cards: `docs/solutions/2026-07-27-verification-with-no-reader.md` · `2026-07-27-every-failure-defaults-to-the-human.md`. Handoff: `.agent/handoffs/2026-07-28-opus5-adaptation-layer.md` (next mission: bound injector + dead-channel detector, Fable seat).
