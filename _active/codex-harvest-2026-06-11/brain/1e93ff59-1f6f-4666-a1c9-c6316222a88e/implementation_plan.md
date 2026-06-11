# Antigravity System Evolution Plan

## System Inventory (Current State)

| Component | Count | Status |
|-----------|-------|--------|
| Skills (with SKILL.md) | 192 | Active |
| Skills with genius.md | 161 | 149 uncompressed |
| Skill workflow files | 812 | Active |
| Slash-command workflows | 479 | Many overlapping |
| Execution scripts | 62 | Mostly functional |
| Directives | 46 | Some dormant |
| Performance Log entries | 87 | Healthy |
| Quality Gate activations | 71 | Active |
| Feedback Ratchet activations | 83 | Active |
| AGENTS.md | V002 deployed | 68% compressed |

### Performance Baselines

| Metric | Value |
|--------|-------|
| Avg Quality Score | 8.8 |
| Avg Intent Alignment | 9.4 |
| Avg Expert Standard | 8.7 |
| Avg Adversarial Resilience | 8.3 |
| Keep Rate | 100% |

### Evolution Pipeline Status

```
Phase 1: Feedback Ratchet    → ACTIVE (87 entries, threshold: 20) ✓
Phase 2: Skill Evolution     → READY but NEVER ACTIVATED (0 cycles)
Phase 3: Cross-Pollination   → BLOCKED by Phase 2
Phase 4: Gap Detection       → READY but DORMANT
```

---

## The Problem

You have a powerful system with 192 skills, 812 workflows, and 62 execution scripts — but the improvement loop has never turned. Phase 1 (data collection) has been running for months. Phase 2 (evolution) is unlocked but has 0 cycles. Phase 3 (cross-pollination) is structurally impossible without Phase 2 output. The system accumulates skill but doesn't compound it.

Meanwhile:
- **149 genius files** are uncompressed, meaning Tier 2 loads burn 25-50K tokens instead of 3-5K
- **479 workflows** have significant overlap and redundancy (multiple ad, content, brand workflows doing similar things)
- **Ground truth** has major gaps — 0% coverage in brand-strategy, partial in SEO and LinkedIn
- **Routing Intelligence** is dormant — 0 entries

---

## Five Workstreams (Priority Order)

### WS1: Activate Phase 2 — First Skill Evolution Cycle

> [!IMPORTANT]
> This is the most important system improvement. Everything downstream depends on it. One successful cycle proves the loop works.

**What**: Run the first skill evolution cycle end-to-end on the highest-traffic skill.

**Target**: `lara-acosta-linkedin-mastery` (8 deployments, highest traffic per phase3_targets.json)

**Steps**:
1. Run `python execution/skill_benchmark.py benchmark lara-acosta-linkedin-mastery`
2. Identify weakest dimension from the benchmark report
3. Write evolution hypothesis (one target only)
4. Generate variant workflow
5. Test variant vs current on 3 benchmark tasks (10 min max each)
6. Score blind, decide binary (≥7 KEEP, <7 DISCARD)
7. Git commit if KEPT
8. Log result to Performance Log + update `evolution-direction.md`

**Success**: One cycle completed. Evolution History table in `evolution-direction.md` has its first entry. Phase 3 unblocks.

**Estimated effort**: 1 focused session (~45 min)

---

### WS2: Genius Compression Sprint

**What**: Compress the remaining 149 genius files from 15-50K bytes down to 3-5K structured format (patterns, hidden knowledge, signature moves, quality rubric).

**Why**: At Tier 2, loading a 49K genius.md (Kallaway) consumes context that should go to the actual work. Compressed format maintains all expert intelligence at ~80% reduction.

**Approach**: Batch 10 files per session, prioritizing by deployment frequency:

| Priority | Skills | Reason |
|----------|--------|--------|
| **Batch 1** | nicolas-cole (×3 skills), luke-iha (×7 skills), lara-acosta (×3 skills) | Top 3 most-deployed experts |
| **Batch 2** | dai-media, grace-andrews, donald-miller, caleb-ralston | High-frequency experts |
| **Batch 3** | kallaway (×2), eric-roth (×2), joanna-wiebe (×2) | Largest files (29-50K) |
| **Batch 4-15** | Remaining 120+ skills | Alphabetical sweep |

> [!WARNING]
> This is a large volume task. 149 files × ~15 min each = ~37 hours of compression work across multiple sessions. Consider whether we want to compress ALL or only the top 30-40 most-used skills.

**Decision needed**: Compress all 149 or just top 40?

---

### WS3: Ground Truth Calibration

**What**: Fill the gaps in the ground truth comparison system so quality scores are grounded against real expert output, not AI self-evaluation.

**Current coverage**:

| Domain | Samples | Coverage | Missing |
|--------|---------|----------|---------|
| Copywriting | 5 | 33% | cardinal-mason, stefan-georgi, ad-copy, email-sequence |
| LinkedIn | 2 | 50% | nicolas-cole, headline, about-section, carousel |
| Brand Strategy | 0 | 0% | oren-john, grace-beverley, david-placek |
| SEO | 1 | 50% | ethan-smith, meta-titles, technical-audit |

**Steps**:
1. Source real expert samples for the top 3 domains (LinkedIn, copywriting, brand-strategy)
2. Add 2-3 samples per domain using `python execution/ground_truth.py`
3. Run blind comparisons on the most-deployed skills
4. If AI scores diverge >2 points from expert baseline → recalibrate scoring rubric

**Decision needed**: Where do we source expert samples? Published work, client examples, or commissioned benchmarks?

---

### WS4: Workflow Consolidation Audit

**What**: Audit the 479 slash-command workflows for overlap, redundancy, and dead commands.

**Symptoms**:
- Multiple ad workflows: `/ad-script`, `/full-stack-ad`, `/cash-method`, `/mechanism-sprint`, `/unaware-ad`, `/proof-stacked-ad-builder`
- Multiple content workflows: `/content-bundle`, `/content-cluster`, `/content-enrich`, `/content-orchestrate`, `/content-remix`, `/content-series`, `/content-series-plan`, `/content-style-card`, `/parallel-content`, `/quantity-sprint`
- Multiple hook workflows: `/hook-bank`, `/hook-forge`, `/hook-formula-extract`, `/hook-viciousness-audit`, `/vicious-hook`, `/vicious-hook-sprint`, `/vicious-rewrite`
- Multiple brand workflows: `/brand-arena`, `/zero-to-brand`, `/caleb-brand-audit`, `/caleb-brand-build`, `/junyuh-brandbook`, `/junyuh-identity`

**Approach**:
1. Categorize all 479 workflows by domain
2. Identify true duplicates (different name, same output)
3. Identify complementary workflows that should chain, not coexist
4. Propose merges, deprecations, and a routing index
5. Build a decision tree: "I want to make an ad" → which workflow?

**Not proposing deletion** — proposing a routing layer so the system knows which workflow to pick. This directly feeds Routing Intelligence (currently dormant at 0 entries).

---

### WS5: Directive Modernization

**What**: Review the 46 directives for staleness, conflict, and activation gaps.

**Known issues**:
- `evolution-direction.md` says "Phase 2 activating 2026-04-06" but 3 days later, still 0 cycles
- `skill-evolution-protocol.md` 30-Day Review Date is TODAY (2026-04-09)
- Routing Intelligence has 0 entries despite being marked READY
- Several directives reference features that may have evolved since creation

**Approach**:
1. Run `python execution/system_health.py` (already done — see results)
2. Tag each directive: ACTIVE / STALE / CONFLICTING / DORMANT
3. Update stale dates and cross-references
4. Archive truly dead directives to `directives/_archived/`

---

## Proposed Execution Order

| Phase | Workstream | Sessions | Dependencies |
|-------|-----------|----------|--------------|
| **Now** | WS1: First Evolution Cycle | 1 session | None — this unblocks everything |
| **Next** | WS2: Genius Compression (Batch 1 — top experts) | 2-3 sessions | None |
| **Then** | WS3: Ground Truth (top 3 domains) | 1-2 sessions | Expert samples needed |
| **After** | WS4: Workflow Consolidation Audit | 2 sessions | None |
| **Ongoing** | WS5: Directive Modernization | 1 session | After WS1 completes |
| **Background** | WS2: Genius Compression (remaining batches) | 10+ sessions | Batch as you go |

---

## Open Questions

> [!IMPORTANT]
> **Q1**: Genius compression scope — all 149 files, or just the top 30-40 most-deployed? Full run = ~37 hours. Top 40 = ~10 hours. The long tail of rarely-used skills may not justify the investment.

> [!IMPORTANT]
> **Q2**: Do you want to run the first evolution cycle (WS1) right now in this session? It would take ~45 minutes and would be the single highest-leverage system improvement — it turns the loop on for the first time.

> [!WARNING]
> **Q3**: Workflow consolidation (WS4) — are you open to deprecating workflows, or do you want to keep all 479 and just add a routing layer? Some of these may have been created speculatively and never used.

---

## Verification Plan

### Automated
- `python execution/system_health.py` — before and after each workstream
- `python execution/skill_benchmark.py benchmark <skill>` — before and after WS1
- `python execution/ground_truth.py gap-report` — before and after WS3
- Git diff on all modified files

### Manual
- You review the first evolution cycle result (WS1) before KEEP/DISCARD
- You approve any workflow deprecations (WS4)
- You spot-check compressed genius files against originals for intelligence loss
