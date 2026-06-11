---
description: Benchmark routing quality, latency, performance, context footprint, command bloat, overengineering risk, plugin readiness, and feedback coverage before broad restructuring or packaging Antigravity
---

# /system-efficiency-benchmark - Measure Before Packaging

Decide whether Antigravity needs router cleanup, workflow hardening, selective plugin packaging, or no broad restructuring.

## Usage

```bash
/system-efficiency-benchmark
/system-efficiency-benchmark --compare-packaging
```

## Pre-Flight

Read:

1. `skills/system-efficiency-benchmark/SKILL.md`
2. `skills/system-efficiency-benchmark/references/genius-patterns.md`
3. `semantic_libraries/antigravity/primitives/workflow-packaging-ladder.md`
4. `deliverables/plugin-readiness/operator-core-scorecard.md` if present

## Execution

Run:

```bash
python3 execution/system_efficiency_benchmark.py
python3 execution/plugin_readiness_audit.py --all-bundles --out deliverables/plugin-readiness/family-bundle-matrix.md
```

## Output

Return:

- benchmark report path
- route quality and latency summary
- current vs cleanup-only vs plugin-packaged comparison
- full-family plugin-readiness summary
- hot/cold tier recommendation
- next optimization order

## Quality Gate

Do not recommend whole-system packaging. Package only if a bundle beats cleanup-only or solves a fresh-thread reliability problem that routing metadata cannot solve.
