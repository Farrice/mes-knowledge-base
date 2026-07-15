---
description: "(alias) → /weekly-closeout"
status: superseded
superseded_by: weekly-closeout
---

# /maintenance — superseded alias

Superseded 2026-07-15 (health-loop consolidation: three overlapping weekly rituals → one spine).

**Read and execute `.agent/workflows/weekly-closeout.md`** with this invocation's arguments — its Step 1.5 (System Health Review) carries this workflow's unique steps (skill benchmark regression check, cross-pollination scan, gap analysis, agent-health spot check), now fed by the daily `health_metrics.py` snapshots.

Rationale: /system-pulse, /maintenance, and /weekly-closeout all ran overlapping weekly checks; the deterministic health collector (launchd `com.antigravity.health-metrics`, daily 06:15) plus the hook-nudged /weekly-closeout replaces all three surfaces. Original content: `git show d3067dff8:.agent/workflows/maintenance.md`.
