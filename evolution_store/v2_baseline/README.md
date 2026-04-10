# Evolution Store v2 — Baseline

> **Created:** 2026-04-09
> **Save Point:** `e615c301` (git commit)
> **Rollback:** `git reset --hard e615c301`

## What This Is

This is the v2 evolution baseline. The v1 evolution store (`baseline/`, `variant_001-003/`) evolved a modular-pointer GEMINI.md architecture that was abandoned in production. This v2 baseline captures the **actually deployed** system state.

## Files

- `AGENTS.md` — 10,187 bytes, the Claude harness (never evolved)
- `GEMINI.md` — 2,119 bytes, the Gemini harness (self-contained rewrite)
- `score.json` — Baseline metrics and system stats

## Rules

1. **Never modify baseline files.** They are the rollback reference.
2. **All variants go in `evolution_store/v2_variants/`.**
3. **All traces go in `evolution_store/v2_traces/`.**
4. **A variant only deploys if it passes blind comparison against ground truth.**
