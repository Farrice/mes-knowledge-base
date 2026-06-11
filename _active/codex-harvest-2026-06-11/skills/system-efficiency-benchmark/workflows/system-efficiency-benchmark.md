# System Efficiency Benchmark Workflow

## Goal

Benchmark Antigravity before restructuring so the system can choose the smallest optimization that improves route quality, reduces reconstruction burden, or lowers context load.

## Steps

1. Run `python3 execution/system_efficiency_benchmark.py`.
2. Run `python3 execution/plugin_readiness_audit.py --all-bundles` when package expansion is being evaluated.
3. Compare current routing, cleanup-only projection, and plugin-packaged projection.
4. Recommend one next move: route metadata cleanup, workflow hardening, selective plugin packaging, feedback logging, or no change.

## Quality Bar

The recommendation must be grounded in measured routing results, not vibes. No archive, deletion, or whole-library plugin conversion should happen from this workflow alone.

