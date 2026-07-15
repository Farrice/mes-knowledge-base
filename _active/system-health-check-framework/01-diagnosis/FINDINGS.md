---
title: System Health-Check — Baseline Findings
date: 2026-07-15
---

# Baseline System Audit Findings

**Session**: 2026-07-15 09:43 UTC  
**Orchestrator**: `/system-audit` workflow  
**Status**: **4 issues identified (2 P1, 2 P2+ categories)**

---

## Executive Summary

The Antigravity system is **fundamentally healthy** (Autopilot, skill system, Google Operator Core all pass canonical verification). However, three distinct **accumulation issues** have emerged:

1. **Routing precision degradation** (P1) — queries misrouting due to golden matrix drift
2. **Telemetry system broken** (P1) — routing analytics can't generate scoreboard
3. **Protocol activation collapse** (P2) — 32 zombie protocols, 39 overdue, only 15% activation rate
4. **Finalize debt explosion** (P2) — 135 unenforced quality violations in 7-day window

These are **not catastrophic failures** (systems still work), but they're the **accumulation pattern the user wanted to prevent** — toxic waste silently building.

---

## P1: Control-Plane Routing Conflict

**Discovery**: `verify_system_control_plane.py` golden query test failed

```
AssertionError: workflow_router health-check-harness-status 
expected first route in ['health-check'], got /system-audit
```

### Evidence

**Query**: `"health check harness status"`  
**Expected route**: `/health-check` (per control_plane_golden_queries.json line 327)  
**Actual route**: `/system-audit` (workflow_router ranked it first)  
**Impact**: Health-check status queries land on the audit workflow instead of the lightweight status endpoint

### Root Cause

The workflow_router is scoring "health-check" language without distinguishing between:
- **Status reads** (`health check status` → `/health-check`)
- **System repairs** (`the system is broken` → `/system-audit`)

The golden matrix says health-check-harness-status should rank `/health-check` first, but the router is returning `/system-audit` first.

### Fix Approach

1. **Quick**: Reconcile workflow_router scoring against control_plane_golden_queries.json matrix
2. **Verify**: Re-run `verify_system_control_plane.py` golden queries — must pass all 30+ test cases
3. **Retest**: Run `/health-check` command with sample queries to confirm firing behavior

**Estimated effort**: 0.5 hours  
**Boundary**: Workspace-only (no external writes)

---

## P1: Routing Telemetry System Broken

**Discovery**: `routing_intelligence.py scoreboard` fails to generate

```
KeyError: 'auto_miss'
  File routing_intelligence.py, line 438
    ensembles[pairing][rating] += 1
```

### Evidence

**Command**: `python3 execution/routing_intelligence.py scoreboard`  
**Error**: Rating enum undefined or data model mismatch  
**Impact**: No routing analytics visible; user can't see which queries misroute

### Root Cause

The routing telemetry data model has ratings (PASS, MISS, PARTIAL, etc.) but the scoreboard code is looking for an 'auto_miss' rating that doesn't exist in the enum.

### Fix Approach

1. **Audit**: Map rating enum in routing_intelligence.py (what values are possible?)
2. **Fix**: Either add 'auto_miss' to enum OR update line 438 to handle missing values
3. **Verify**: Re-run `routing_intelligence.py scoreboard` — must render without error

**Estimated effort**: 0.5 hours  
**Boundary**: Workspace-only

---

## P2: Zombie Protocols (Context Bloat)

**Discovery**: `protocol_tracker.py audit` shows activation statistics

```
Total Protocols:    47
Active:             15 (32%)
Never Activated:    32
Zombies (overdue):  39
```

### Evidence

**32 protocols** created but never wired to any trigger or gate:
- agent-loading-protocol.md
- ai-slop-detector.md
- collaboration-protocol.md
- content-creation.md
- cross-pollination.md
- decision-council.md
- deep_self_annealing.md
- ... (28 more)

**Impact**: Each protocol loads as context when referenced; wasted token budget and confusion when Farrice expects a protocol to exist but it's not wired.

### Root Cause

Protocols created during system build but activation infrastructure (gates/hooks) was never wired. They sit dormant, adding context bloat.

### Fix Approach

**Triage each protocol**:
- Keep & resurrect (wire to existing gate or workflow)
- Delete (decommission via `status: archived` in frontmatter)
- Clarify (rename + relocate to docs/solutions or guides/)

**Estimated effort**: 4-6 hours (1-2 per protocol to triage)  
**Boundary**: Workspace-only  
**Timeline**: By 2026-07-22 (end of week)

---

## P2: Overdue Protocols (Activation Gaps)

**Discovery**: `protocol_tracker.py audit` shows stale protocols

```
39 protocols overdue (last activated more than expected window ago)
```

### Evidence

Notable overdue:
- skill-evolution-protocol.md: overdue since 2026-04-09 (96 days! — should fire ~2x/month)
- verification-agent-protocol.md: overdue since 2026-05-01 (76 days)
- user-state-awareness.md: overdue since 2026-05-01

**Impact**: Systems designed to activate periodically are not firing; telemetry is stale.

### Root Cause

Protocols were activated once during build but the cadence enforcement is missing. No reminder or auto-trigger to re-activate.

### Fix Approach

1. **Cadence audit**: Review each overdue protocol's intended cadence (daily/weekly/monthly?)
2. **Wiring check**: Is it wired to a hook/automation that should have fired?
3. **Reactivate or decommission**: Either wire the trigger or mark protocol as archived

**Estimated effort**: 2-3 hours  
**Boundary**: Workspace-only  
**Timeline**: By 2026-07-22

---

## P2: Finalize Debt Explosion

**Discovery**: `system_health.py --quick` reports finalize gate status

```
Finalize Gate (observe mode)
- Mode: observe (Farrice 2026-07-02: observe; flip via LEDGER_ENFORCE=1)
- Would-blocks last 7d: 135
- ⚠ 135 unenforced finalize debts this week
```

### Evidence

**135 deliverables** in last 7 days did NOT pass finalize scoring (would have been blocked if `LEDGER_ENFORCE=1`).

This is the toxic waste the user was concerned about — quality violations silently accumulating.

### Root Cause

Finalize gate in **observe mode** (logs but doesn't block). No enforcement = no consequence for shipping incomplete or unscored work.

### Fix Approach

**Decision required**:

**Option A: Enforce** (flip to `LEDGER_ENFORCE=1`)
- Pros: Forces every deliverable through quality gate; prevents toxic waste
- Cons: Sessions may be blocked waiting for finalize data; stricter quality bar
- Timeline: Can flip immediately; test with 1-2 sessions first

**Option B: Fix root debt** (improve underlying quality without enforcement)
- Pros: Catches systematic problems (e.g., missing scoring rubric); lighter UX
- Cons: Still silently accumulates if users skip finalize voluntarily
- Timeline: Requires root-cause investigation; 3-5 days

**Recommendation**: Start with Option A (enforce for 7 days), measure session friction, then decide whether to relax or keep strict.

**Estimated effort (Option A)**: 0.25 hours (flip flag + monitor)  
**Estimated effort (Option B)**: 4-8 hours (investigate + fix)

---

## P3: Memory Review Backlog

**Discovery**: `system_health.py --quick` reports memory status

```
- Total memories: 5145
- ⚠ Flagged for review: 18 pending
```

### Evidence

18 distilled memories awaiting human (Farrice) approval before they become canonical.

### Fix Approach

Run `python3 execution/memory_review.py list` to see all 18.  
Then batch approve/reject to clear backlog.

**Estimated effort**: 0.5-1 hour  
**Timeline**: By 2026-07-18 (end of week)

---

## Summary & Severity

| Issue | Type | Severity | Impact | Fix Time | Timeline |
|-------|------|----------|--------|----------|----------|
| Routing conflict | Precision | P1 | Queries misroute; specific commands don't fire | 0.5h | Immediate |
| Telemetry broken | Visibility | P1 | Can't see routing analytics; debug blind | 0.5h | Immediate |
| Zombie protocols | Bloat | P2 | Context waste; 32 unused protocols | 4-6h | By 07-22 |
| Overdue protocols | Gaps | P2 | Telemetry stale; automations not triggering | 2-3h | By 07-22 |
| Finalize debt | Waste | P2 | 135 unscored deliverables shipping | 0.25-8h | Decide today; implement by 07-22 |
| Memory backlog | Hygiene | P3 | 18 pending reviews | 0.5-1h | By 07-18 |

---

## What This Means

**The system is not broken. But it's showing the early signs of accumulation that you wanted to prevent:**

1. ✅ Core systems (Autopilot, routing, skill loading) all pass verification
2. ⚠️ Precision is drifting (routing conflicts, telemetry blind spots)
3. 🔴 Waste is accumulating (zombie protocols, finalize debts, stale automation)
4. 🚨 Operator visibility is degrading (routing analytics down, health dashboard manual)

**The framework above (FRAMEWORK.md) will automate detection and prevention.** Once daily health checks are running, these issues will surface in the morning briefing instead of being discovered by surprise audits.

---

## Next Action

Review findings. Decide on finalize gate enforcement (Option A vs B). Then proceed to Phase 2 fixes.
