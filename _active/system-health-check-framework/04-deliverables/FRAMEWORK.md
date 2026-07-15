---
title: Antigravity Recurring Health-Check Framework
created: 2026-07-15
updated: 2026-07-15
status: v1-active
owner: orchestrator
---

# System Health-Check & Debt-Prevention Framework

## Mission

Establish a deterministic, recurring system health-check process that:
1. Detects context bloat, engineering debt, and routing drift before they cascade
2. Prevents toxic waste accumulation (finalize debts, zombie protocols, stale telemetry)
3. Maintains maximum efficiency and capabilities without constant operator cognitive overhead
4. Keeps the operator fully informed of system state changes without drift or silent removal

## Baseline Findings (2026-07-15 09:00)

### P1 Issues (Critical — Fix Immediately)

| Issue | Impact | Root Cause | Fix |
|-------|--------|-----------|-----|
| **Control-plane routing conflict** | health-check queries route to `/system-audit` instead of `/health-check` | Golden routing matrix mismatch in workflow_router | Reconcile workflow_router against control_plane_golden_queries.json; re-verify with verify_system_control_plane.py |
| **Routing telemetry broken** | routing_intelligence.py scoreboard fails (KeyError: 'auto_miss') | Rating enum mismatch in routing_intelligence.py line 438 | Fix enum/data model in routing_intelligence.py; validate with verification scripts |

### P2 Issues (Important — Backlog with Timeline)

| Issue | Volume | Impact | Root Cause | Fix Timeline |
|-------|--------|--------|-----------|--------------|
| **Zombie protocols** | 32 never activated | Context bloat; wasted context when loaded | Protocols written but not wired to any trigger or gate | Audit each; decommission or resurrect within 7d |
| **Overdue protocols** | 39 stale activations | Activation gaps; systems that should fire don't | Protocol window exceeded but not refreshed | Review cadence + enforcement within 7d |
| **Finalize debts** | 135 unenforced | Toxic waste accumulation; quality violations slipping through | Finalize gate in observe=True; system NOT blocking | Decide: enforce (LEDGER_ENFORCE=1) or fix root issues within 14d |

### P3 Issues (Maintenance)

| Issue | Backlog | Fix Timeline |
|-------|---------|--------------|
| **Memory review pending** | 18 items | Batch approve/reject within 3d |

---

## Framework Architecture

### Layer 1: Automated Detection (runs daily @ 07:00 via launchd)

**File**: `execution/system_health_monitor.py`

```bash
# Daily health snapshot
python3 execution/system_health.py --quick           # activation status
python3 execution/protocol_tracker.py audit          # protocol compliance
python3 execution/routing_intelligence.py scoreboard # routing parity
python3 execution/verify_system_control_plane.py    # golden query matrix
python3 execution/verify_autopilot_runtime_preflight.py # Autopilot firing
```

**Output**: `.agent/health-checks/health-snapshot-YYYY-MM-DD.json`

**Data Captured**:
- System activation status (active/dormant/blocked/stale/unmeasured)
- Protocol compliance (never-fired, overdue, active count)
- Routing parity (golden queries pass/fail)
- Autopilot runtime status
- Finalize debt count + trend
- Memory review backlog

### Layer 2: Issue Triage & Severity Ranking

**File**: `execution/system_debt_ledger.py` (reads daily snapshots)

**Process**:
1. Load baseline from previous week's snapshot
2. Detect NEW issues (regression → P0), GROWING issues (P1 escalation)
3. Classify by severity per `/system-audit` rubric:
   - **P0**: Autopilot/front-door failure, unsafe routing, approval-boundary break
   - **P1**: Router parity, routing mismatch, authority conflict, broken-system misrouting
   - **P2**: Dormant telemetry, stale protocols, missing closeout proof, weak activation
   - **P3**: Cleanup, documentation, hygiene

**Output**: `.agent/health-checks/issue-ledger-YYYY-MM-DD.json`

```json
{
  "timestamp": "2026-07-15T07:00:00Z",
  "baseline_date": "2026-07-08",
  "issues": [
    {
      "id": "routing-conflict-health-check",
      "severity": "P1",
      "is_new": true,
      "detected_date": "2026-07-15",
      "symptom": "health-check queries route to /system-audit",
      "root_cause": "Golden routing matrix mismatch",
      "fix_boundary": "workspace-only",
      "fix_estimate_hours": 0.5,
      "blocker": false
    }
  ],
  "summary": {
    "p0_count": 0,
    "p1_count": 2,
    "p2_count": 3,
    "p3_count": 1,
    "regression_items": 0,
    "new_items": 2,
    "trend": "stable"
  }
}
```

### Layer 3: Operator Briefing & Dashboard

**Daily Briefing** (runs @ 07:15, displayed at session start)

**File**: `execution/health_briefing_render.py`

**Output**: CLI table + action links

```markdown
╔════════════════════════════════════════════════╗
║     ANTIGRAVITY SYSTEM HEALTH — 2026-07-15     ║
║              BRIEFING @ 07:15 UTC               ║
╚════════════════════════════════════════════════╝

🔴 P1 ALERTS (Action Required)
  1. Routing: health-check → /system-audit (not /health-check)
     └─ fix_link: `/system-health-fix-routing`
     
  2. Telemetry: routing_intelligence.py KeyError
     └─ fix_link: `/system-health-fix-telemetry`

🟡 P2 BACKLOG (Next 7 Days)
  • 32 zombie protocols (context bloat)
  • 39 overdue protocols
  • 135 finalize debts
  
  👉 Review: `/health-check` or `/pulse-board`

✅ HEALTHY SYSTEMS
  • Autopilot runtime: PASS
  • Skill system contract: PASS
  • Google Operator Core: PASS
  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ℹ️ Last full audit: 2026-07-15 09:00
Next scheduled audit: 2026-07-22 07:00
```

**Session Start Hook**: Display briefing if P1 issues exist or trend changed

### Layer 4: Automated Repair (with Approval)

**File**: `execution/system_health_auto_repair.py`

**Workspace-local repairs** (run automatically):
1. Fix routing conflicts via workflow_router rebuild + re-verify
2. Fix telemetry enum mismatches
3. Decommission zombie protocols (mark `status: archived`)
4. Refresh overdue protocol windows

**Approval-required repairs** (surface for decision):
1. Decide: enforce finalize gate (LEDGER_ENFORCE=1) or fix root debt issues
2. Delete vs. resurrect zombie protocols
3. Global `~/.codex` writes (if Phase 5 active)

**Output**: `.agent/health-checks/repairs-applied-YYYY-MM-DD.json`

### Layer 5: Debt Prevention Rules

**Embedded in Hooks** (file: `execution/hooks/health_debt_prevention_hook.py`)

| Rule | Trigger | Action | Boundary |
|------|---------|--------|----------|
| **Dead Protocol Block** | New protocol written but no activation wired within 48h | Warn at SessionStart; auto-retire if untouched after 30d | Workspace-only |
| **Finalize Debt Cap** | Unenforced finalize debts exceed 50 (observe mode) | Warn; offer `/enforce-finalize-gate` | Workspace-only |
| **Routing Drift Detection** | Routing matrix fails 2+ golden queries | Auto-repair attempt + re-verify; escalate if still fails | Workspace-only |
| **Telemetry Stale** | Health snapshot older than 8d | Re-run automated detection; alert if failures | Workspace-only |
| **Context Bloat** | Loaded skills/agents exceed 200 in conversation | Warn; suggest context compaction | Workspace-only |

---

## Recurring Operations

### Daily (@ 07:00 UTC via launchd: `com.antigravity.system-health-daily`)

```bash
python3 execution/system_health_monitor.py capture
python3 execution/system_debt_ledger.py ingest-daily
python3 execution/health_briefing_render.py brief --session-start
```

**Output**: Health snapshot + briefing text

### Weekly (Sundays @ 04:00 UTC via launchd: `com.antigravity.system-health-weekly`)

```bash
python3 execution/system_health_monitor.py capture
python3 execution/system_debt_ledger.py analyze
python3 execution/system_health_auto_repair.py repair --dry-run
python3 execution/health_dashboard_render.py board --week
```

**Output**: Weekly dashboard + repair recommendations

### Monthly (1st of month @ 08:00 UTC)

```bash
python3 execution/verify_system_control_plane.py         # full control-plane audit
python3 execution/protocol_tracker.py audit --deep
python3 execution/skill_audit.py
python3 execution/evolution_orchestrator.py calibrate
```

**Output**: Monthly audit report + calibration recommendations

---

## Operator Workflows

### `/health-check`
Read-only status. Shows current health, recent issues, trending.

### `/system-health-fix-<issue>`
Specific repair workflows (auto-generated based on current issues).
- `/system-health-fix-routing` — Reconcile routing + re-verify
- `/system-health-fix-telemetry` — Fix enum + validate
- `/system-health-fix-zombies` — Audit protocols
- `/system-health-fix-finalize` — Enforce or resolve debt

### `/system-audit`
Comprehensive control-plane audit (existing workflow — now with weekly scheduling).

### `/pulse-board`
Abbreviated dashboard (trending + action items).

---

## Prevention Rules (Applied at Submission)

### Protocol Creation

New protocol must have:
- [ ] Defined trigger (workflow, gate, hook, or explicit invocation)
- [ ] Activation wired (linked in a conductor workflow or gate)
- [ ] Telemetry capture (logged to protocol_tracker.py)
- [ ] 30-day decommission timeout if untouched

→ **Enforce**: automation/hooks/protocol_creation_gate.py

### Finalize Debt

No deliverable without finalize call:
- [ ] Intent alignment scored (1-10)
- [ ] Expert standard scored (1-10)
- [ ] Adversarial resilience scored (1-10)
- [ ] Factual grounding scored (1-10)
- [ ] Composite ≥ 7 or retry weakest section

→ **Enforce**: LEDGER_ENFORCE=1 (currently observe=True; recommendation: flip to enforce by 2026-07-22)

### Routing Drift

Golden query matrix must match workflow_router output:
- [ ] Verify against control_plane_golden_queries.json before commit
- [ ] Automated re-check daily @ 07:00
- [ ] Escalate to P1 if 2+ queries misroute

→ **Enforce**: verify_system_control_plane.py (daily + pre-push hook)

### Context Bloat

No conversation shall load >200 files without explicit justification:
- [ ] Skill loading audited in Tier 1.5 (memory facade)
- [ ] Cold-load context cached for reuse
- [ ] Session state tracks cumulative context cost

→ **Enforce**: context_size_gate.py (warn at 150, block at 200 unless override)

---

## Dashboards & Telemetry

### `.agent/health-checks/` — Daily Snapshots
```
health-snapshot-2026-07-15.json        # daily capture
issue-ledger-2026-07-15.json           # triaged issues
repairs-applied-2026-07-15.json        # automated fixes
protocol-audit-2026-07-15.json         # detailed protocol status
```

### `.agent/health-trends/` — Weekly Aggregates
```
health-trend-week-2026-07-08.json      # week summary
protocol-trend-week-2026-07-08.json    # protocol compliance trend
routing-parity-week-2026-07-08.json    # golden query pass rate
```

### Operator Visible (SessionStart)
- P1/P2 alerts in briefing
- Action links to workflows
- Trend arrow (↑ degrading / → stable / ↓ improving)

---

## Success Criteria

### Immediate (By 2026-07-22)

- [ ] P1 routing conflict fixed + verified
- [ ] P1 telemetry bug fixed + verified  
- [ ] Daily health-check automation wired (launchd)
- [ ] Operator receives morning briefing with P1/P2 alerts

### Short-term (By 2026-08-01)

- [ ] All zombie protocols triaged (keep/delete decision made)
- [ ] Finalize gate decision (enforce or fix root debt)
- [ ] Memory review backlog cleared (<3 items)
- [ ] Issue ledger dashboard live

### Long-term (Ongoing)

- [ ] Zero new regressions in routing parity
- [ ] Zombie protocol creation < 5 per month
- [ ] Protocol activation rate ≥ 85%
- [ ] Context bloat stays ≤ 150 files/conversation
- [ ] Finalize debt trend → 0 (if enforced) or stable (if observe)

---

## Implementation Roadmap

### Phase 1: Diagnostics (This Session)
- ✅ Baseline audit complete
- ✅ Issue ledger drafted
- ⏳ [Daily health-check automation wired to launchd]

### Phase 2: Fixes (Next Session)
- [ ] Fix P1 routing conflict
- [ ] Fix P1 telemetry bug
- [ ] Operator briefing displayed
- [ ] Weekly dashboard live

### Phase 3: Prevention (End of Week)
- [ ] Zombie protocol decommissioning rule wired
- [ ] Finalize debt decision enforced
- [ ] Protocol creation gate active
- [ ] Routing drift detection automated

### Phase 4: Scaling (Ongoing)
- [ ] Extend detection to multi-session patterns (e.g., repeated manual loops → missing tool)
- [ ] Add self-healing for common issues
- [ ] Integrate with evolution_orchestrator.py feedback loops

---

## References

- System audit workflow: `.agent/workflows/system-audit.md`
- Health-check workflow: `.agent/workflows/health-check.md`
- Autopilot control-plane: `.agent/workflows/autopilot.md`
- Golden routing matrix: `execution/control_plane_golden_queries.json`
- System health script: `execution/system_health.py`
- Protocol tracker: `execution/protocol_tracker.py`
- Routing intelligence: `execution/routing_intelligence.py`

---

## Next Steps

**Immediate (Now)**: 
1. Review this framework
2. Approve P1 fix approaches
3. Decide: enforce finalize gate?

**Short-term (Next Session)**:
1. Implement daily health automation
2. Fix P1 issues
3. Launch operator briefing
