---
description: Run deterministic session sweep and update mission briefs
---

# /sweep

> **Command**: `python3 execution/session_sweep.py`

Run a deterministic sweep of recent sessions (Claude Code + Codex) and generate living mission briefs.

## Usage

```bash
# Sweep last 14 days and build briefs
/sweep

# Sweep since a specific date
/sweep --since 2026-08-01

# Sweep N days back
/sweep --days 7

# Dry-run (no writes)
/sweep --dry-run
```

## What it does

1. **Collects** session records from `.claude/projects/` and `.codex/`
2. **Applies promotion bar** — threads with real deliverables, files, assets, open missions, or active handoffs get a card
3. **Builds fact bundles** → `.agent/sweep/sweep-<date>.json` (durable, never pruned)
4. **Generates mission briefs** → `deliverables/research-briefs/mission-<slug>/`
5. **Updates mission-board** → the digest of all live missions

## Living briefs

Each mission brief is updated in place so sessions append to the timeline. All facts are pre-filled deterministically; meaning-bearing slots (summary, decision, caveats) are filled by an LLM judge in the nightly synthesis pass.

## Nightly automation

Runs at 02:45 UTC via `com.antigravity.session-sweep.plist`. Reads the lock; skips cleanly if another session is working.
