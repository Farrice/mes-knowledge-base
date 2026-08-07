# Walkthrough: Antigravity Harness Audit & Evolution

## What Changed

### 1. AGENTS.md — Full Directive Index
**Before**: 13 of 42 directives were listed in a "Supporting Protocols" table. The other 29 were invisible to the orchestration loop.

**After**: All 42 directives indexed across 7 categories (Chain, Routing, Research, Extraction, Session, Domain, Setup) with 1-line trigger conditions.

Also fixed:
- Title: `# CLAUDE.md` → `# AGENTS.md — Antigravity System Harness`
- Removed stale `/sync-instructions` comment

render_diffs(file:///Users/farricecain/Google%20Antigravity/AGENTS.md)

---

### 2. chain_runner.py — Trace Logging
**Before**: `finalize` logged to Notion only. No local structured data for the `/self-evolve` loop.

**After**: Optional `--trace` flag writes a JSON trace to `evolution_store/traces/` with timestamp, scores, regression data, and notes. Existing behavior 100% unchanged.

render_diffs(file:///Users/farricecain/Google%20Antigravity/execution/chain_runner.py)

---

## Verification Results

| Test | Result |
|------|--------|
| All 42 directives in AGENTS.md | ✅ 0 missing |
| Title fixed | ✅ `# AGENTS.md — Antigravity System Harness` |
| Sync comment removed | ✅ |
| evolution_store/traces/ exists | ✅ |
| `--trace` flag in chain_runner.py | ✅ |
| Live trace test (9.0/10 composite) | ✅ JSON written |

## How to Use

The `--trace` flag is opt-in. Use it when you want trace data for evolution:

```bash
python3 execution/chain_runner.py finalize "output" \
    --expert lara-acosta --skill lara-acosta-linkedin --workflow high-dwell \
    --type Content --intent 8 --expert-score 7 --adversarial 8 \
    --trace --notes "what worked"
```

Traces accumulate in `evolution_store/traces/` and feed `/self-evolve` and `/harness-evolve` workflows.
