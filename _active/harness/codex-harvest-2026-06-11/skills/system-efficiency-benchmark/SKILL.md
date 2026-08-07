---
name: "system-efficiency-benchmark"
description: "Benchmark Antigravity routing latency, top-route quality, command-surface size, context footprint, performance, command bloat, overengineering risk, plugin-readiness scores, and feedback coverage before packaging or restructuring workflows. Use when deciding whether plugin packaging, router cleanup, metadata tightening, workflow consolidation, or no change is the best efficiency move."
---

# System Efficiency Benchmark

Use this skill before broad system restructuring, whole-library plugin conversion, command-surface pruning, or claims that packaging will make Antigravity faster.

## Load Order

1. Read `.agent/workflows/system-efficiency-benchmark.md`.
2. Run `python3 execution/system_efficiency_benchmark.py`.
3. If plugin packaging is still being considered, run `python3 execution/plugin_readiness_audit.py --all-bundles`.
4. Read the generated benchmark report before recommending packaging, pruning, or archive work.

## Decision Rule

- If router/metadata cleanup beats plugin packaging, improve routing first.
- If plugin packaging beats cleanup for a tight bundle, package only that bundle.
- If neither beats the baseline, improve feedback coverage before restructuring.
- Never recommend whole-system plugin packaging from theory alone.

## Required Output

Return:

- benchmark report path
- current route quality and latency
- variant comparison: current, cleanup-only, plugin-packaged
- hot/cold tier recommendation
- plugin bundle readiness summary
- concrete next optimization move
