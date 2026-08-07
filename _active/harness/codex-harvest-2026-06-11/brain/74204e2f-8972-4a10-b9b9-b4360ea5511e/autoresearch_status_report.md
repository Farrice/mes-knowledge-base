# Karpathy Autoresearch Loop — Status Report

*Generated: 2026-03-30*

---

## Executive Summary

The autoresearch loop is a **4-phase self-improvement engine** inspired by Andrej Karpathy's autoresearch concept — where agents modify their own training code, test variants, and keep winning changes. In Antigravity, this translates to skills that benchmark, evolve, and cross-pollinate improvements automatically.

**Current state: Phase 1 is data-rich and ready to unlock Phase 2. Phases 2-4 are built but dormant.**

---

## Phase Status Dashboard

| Phase | Name | Directive | Status | Activations |
|-------|------|-----------|--------|-------------|
| **1** | Feedback Ratchet | [feedback-ratchet.md](file:///Users/farricecain/Google%20Antigravity/directives/feedback-ratchet.md) | ✅ **ACTIVE** | 47 |
| **2** | Skill Evolution | [skill-evolution-protocol.md](file:///Users/farricecain/Google%20Antigravity/directives/skill-evolution-protocol.md) | 🔒 **READY TO UNLOCK** | 0 |
| **3** | Cross-Pollination | [cross-pollination.md](file:///Users/farricecain/Google%20Antigravity/directives/cross-pollination.md) | 🔒 Locked (needs Phase 2 data) | 0 |
| **4** | Intelligence Gap Detector | [expertise-gap-protocol.md](file:///Users/farricecain/Google%20Antigravity/directives/expertise-gap-protocol.md) | 🔒 Locked (needs Phase 2 data) | 0 |

---

## Phase 1: Feedback Ratchet — ✅ ACTIVE

**What it does**: Logs quality scores after every expert output, building per-skill baselines that detect regression and improvement.

**Current metrics** (from Notion Performance Log `31f49875a89781dbb599dee5e7961b5c`):

| Metric | Value |
|--------|-------|
| Total log entries | **44** |
| Unique skills logged | **26** |
| Rolling avg quality | **8.9/10** |
| Avg intent alignment | **9.5/10** |
| Avg expert standard | **8.7/10** |
| Avg adversarial resilience | **8.5/10** |
| Keep rate | **100%** |
| Protocol activations | 47 |

**Skills with logged performance data**: `andreessen-horowitz-new-media`, `caleb-ralston-personal-brand`, `dai-media-consumer-posture`, `dan-martell-business-scaling`, `david-placek-naming`, `donald-miller-storybrand`, `grace-andrews-media-company`, `josh-sanders-linkedin-growth`, `kieran-flanagan-content-engine`, `lara-acosta-linkedin-mastery`, `luke-iha-proof-ladder`, `luke-iha-vicious-hooks`, `nicolas-cole-client-acquisition`, `nicolas-cole-newsletter-flywheel`, + 12 more.

**Execution engine**: [chain_runner.py](file:///Users/farricecain/Google%20Antigravity/execution/chain_runner.py) — deterministic enforcement of Steps 6-7 of The Chain (quality gate + performance log + regression check + session state).

> [!IMPORTANT]
> The feedback ratchet directive says "13 entries, 7 more to unlock Phase 2" — but the **actual Notion DB has 44 entries**. The directive's count is stale. Phase 2's unlock threshold (20 entries) has been **exceeded by 2x**.

---

## Phase 2: Skill Evolution — 🔒 READY TO UNLOCK

**What it does**: Systematic variant testing. Picks the weakest dimension of a skill, generates a variant workflow, benchmarks both versions head-to-head, and keeps the winner.

**The evolution loop**:
1. **Benchmark** current state → `python execution/skill_benchmark.py benchmark <skill>`
2. **Identify** the weakest workflow/dimension
3. **Hypothesize** a fix (documented before any code change)
4. **Generate** variant workflow (`workflows/<name>.variant.md`)
5. **Test** variant vs current on 3 domain-matched benchmark tasks
6. **Decide** — variant wins by 1+ avg → KEEP, else DISCARD
7. **Log** to `genius.md` Evolution Log + Performance DB

**Infrastructure status**:

| Component | Status |
|-----------|--------|
| [skill_benchmark.py](file:///Users/farricecain/Google%20Antigravity/execution/skill_benchmark.py) | ✅ Built (469 lines) |
| Benchmark task library | ✅ 6 domains × 3 tasks each |
| Domain auto-detection | ✅ Keyword-based classifier |
| Performance history pull | ✅ Queries Notion DB |
| Variant comparison | ✅ Structural diff analysis |
| Evolution Log format | ✅ Defined in `genius.md` |

**Why it hasn't fired**: The unlock condition is 20+ Performance Log entries for **any single skill**. While the system has 44 total entries, they're spread across 26 skills — most skills have only 1-2 entries. No single skill has hit the 20-entry threshold yet.

---

## Phase 3: Cross-Pollination — 🔒 Locked

**What it does**: When Phase 2 produces a KEPT improvement, it scans related skills that share pattern families and transfers the winning change.

**Pattern families defined**: Persuasion, Hooks, Structure, Voice, Research, Conversion, Storytelling, Positioning, Systems.

**Infrastructure status**:

| Component | Status |
|-----------|--------|
| [pattern_propagation.py](file:///Users/farricecain/Google%20Antigravity/execution/pattern_propagation.py) | ✅ Built (372 lines) |
| Pattern family classifier | ✅ Keyword-based, multi-family |
| Related skill finder | ✅ Overlap scoring |
| Propagation report generator | ✅ Monthly/on-demand |

**Blocked by**: Phase 2 producing its first KEPT evolution.

---

## Phase 4: Intelligence Gap Detector — 🔒 Locked

**What it does**: Analyzes the gap log for recurring domain gaps (3+ occurrences of the same missing expertise) and surfaces them as high-priority extraction candidates.

**Infrastructure**: Defined in [expertise-gap-protocol.md](file:///Users/farricecain/Google%20Antigravity/directives/expertise-gap-protocol.md) §Autoresearch Integration. References `execution/gap_analysis.py` (not yet built) and `/gap-report` workflow.

**Blocked by**: Phase 2 performance data + gap log accumulation.

---

## The Bottleneck

```
Phase 1 (Data) ──── 44 entries, 26 skills ──── ✅ Threshold exceeded
     │
     ▼
Phase 2 (Evolution) ─── 0 activations ────── 🔒 READY but never triggered
     │
     ▼
Phase 3 (Cross-Pollination) ──────────────── 🔒 Waiting for Phase 2 KEEPs
     │
     ▼
Phase 4 (Gap Intelligence) ───────────────── 🔒 Waiting for Phase 2 data
```

> [!CAUTION]
> **Phase 2 has never been triggered.** The data threshold is met, but no one has run `/skill-evolution <skill>` or detected a regression. The loop is stuck at the Phase 1→2 transition because:
> 1. The directive's stale counter (says "13") makes it look like Phase 2 isn't ready
> 2. No regression has been detected (avg quality is 8.9 — everything passes)
> 3. No one has manually triggered `/skill-evolution` to start the first cycle

---

## What It Would Take to Activate

### Immediate (unlock Phase 2 now):
1. **Update the stale counter** in `feedback-ratchet.md` (line 204) from "13" to "44"
2. **Run the first skill evolution cycle**: pick a high-traffic skill with 3+ entries and run `/skill-evolution <skill-name>`
3. **The benchmark will produce** a report showing weakest dimension → generate a variant → test → keep or discard

### Near-term (feed the flywheel):
- Continue running `chain_runner.py finalize` after every expert output (this is already happening)
- Concentrate usage on a few key skills to build per-skill depth (currently spread thin across 26 skills)
- Look for skills scoring < 8 in any dimension — these are ideal evolution candidates

### Full loop activation:
- Phase 2 produces first KEPT evolution → triggers Phase 3 scan
- Phase 3 transfers pattern to related skill → tested via Phase 2
- Gap log accumulates → Phase 4 surfaces extraction priorities
- **The system becomes genuinely self-improving**
