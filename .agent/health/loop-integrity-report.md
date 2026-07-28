# Loop Integrity Audit Report
**Generated**: 2026-07-28T09:23:38.408674

## Summary

- **PROVEN** (wiring is live): 15
- **FLAGGED** (attention needed): 4
- **AUTO_FIX** (mechanical, reversible): 0

## 🚨 Flagged Issues

**[MEDIUM]** Launchd job declared but .plist missing: /Users/farricecain/Library/LaunchAgents/com.antigravity.health-check.plist
  - Job: com.antigravity.health-check

**[MEDIUM]** Launchd job declared but .plist missing: /Users/farricecain/Library/LaunchAgents/com.antigravity.harbor-launchd.plist
  - Job: com.antigravity.harbor-launchd

**[MEDIUM]** Launchd job declared but .plist missing: /Users/farricecain/Library/LaunchAgents/com.antigravity.memory-harvest.plist
  - Job: com.antigravity.memory-harvest

**[MEDIUM]** Launchd job declared but .plist missing: /Users/farricecain/Library/LaunchAgents/com.antigravity.memory-mirror.plist
  - Job: com.antigravity.memory-mirror

## ✅ Proven Wiring

### Launchd

- Launchd job com.antigravity.evolution-auto: loaded
- Launchd job com.antigravity.cos-prep: loaded

### Spine

- Spine step step_archive_session_state declared and defined
- Spine step step_artifact_sweep declared and defined
- Spine step step_closeout_intelligence declared and defined
- Spine step step_commit_gate declared and defined
- Spine step step_cos_journal declared and defined
- Spine step step_finalize_debt_nudge declared and defined
- Spine step step_friction_nudge declared and defined
- Spine step step_memory_bridge declared and defined
- Spine step step_menu_parity declared and defined
- Spine step step_resolve_handoff declared and defined
- Spine step step_self_heal declared and defined
- Spine step step_session_guide declared and defined
- Spine step step_solution_cards declared and defined
