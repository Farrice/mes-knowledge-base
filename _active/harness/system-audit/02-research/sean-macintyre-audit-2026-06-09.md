# Sean Macintyre — Persuasion Philosophy: 6-Week Deployment Audit
**Audit window:** 2026-04-28 → 2026-06-09  
**Skill shipped:** 2026-04-28 (commit 05bf7e62)  
**Audit date:** 2026-06-09  
**Skill location:** `skills/sean-macintyre-persuasion-philosophy/`  
**Workflows:** 17 across 4 tiers (4 Foundation / 5 Practitioner / 3 Stacking / 5 Apex)

---

## Step 1 — Trace Inventory

**Sources checked:**
- `evolution_store/traces/` — 3 files total, zero containing `sean-macintyre`
- `evolution_store/skill_audit_*.jsonl` — 8 audit runs (2026-04-29 through 2026-06-08)
- `knowledge/log.md` — full scan for sean-related finalize entries
- `deliverables/` and `projects/` — no Sean workflow invocation artifacts
- `_active/` — system audit references (file-size checks only, not deployments)

**Findings:**

The skill auditor JSONL files show two data states across the 8 audit runs:

| Date | trace_count | trace_avg | tier |
|------|------------|-----------|------|
| 2026-04-29 | 2 | 8.7 | A |
| 2026-05-03 | 2 | 8.7 | A |
| 2026-05-05 | 2 | 8.7 | A |
| 2026-05-24 | null | — | REVIEW |
| 2026-05-25 | null | — | REVIEW |
| 2026-05-28 | 2 | 8.7 | A |
| 2026-05-29 | null | — | REVIEW |
| 2026-06-08 | 2 | 8.7 | A |

The 2 traces are **both from the forge build day (2026-04-28)**. They are `extract-forge` finalize records, not production workflow invocations. The intermittent `REVIEW / null` state in May audits appears to reflect changes in the trace-detection logic between auditor versions.

**Workflow-level invocation count during audit window: ZERO.**

---

## Step 2 — Notion Performance Log Query

Database ID: `31f49875a89781dbb599dee5e7961b5c`  
Queried: full database (200 entries across 2 pages), filtered for sean-macintyre.

**Results:**

| Date | Skill | Workflow | Composite | URL |
|------|-------|----------|-----------|-----|
| 2026-04-28 | sean-macintyre-persuasion-philosophy | extract-forge | 8.7 | [link](https://app.notion.com/p/35049875a89781f78daed564d29bbcd3) |
| 2026-04-28 | sean-macintyre-persuasion-philosophy | extract-forge | 8.7 | [link](https://app.notion.com/p/35049875a89781848a28cbc2cb9cad38) |
| 2026-05-02 | writers-room | v5-coach-cooz-clean-handoff-with-winning-mechanisms | 8.3 | [link](https://app.notion.com/p/35549875a89781e796d6c86785794fa9) |

**Finding:** The two April 28 entries are forge extraction finalizes — the skill build itself, not deployment. The May 2 entry is an ensemble deployment (13 experts as Tier 2 thinking lenses, `Skill='writers-room'`). Sean appeared as one voice among thirteen; no dedicated workflow was invoked.

**There are zero Notion Performance Log entries where any specific Sean Macintyre workflow was the primary mechanism.**

---

## Step 3 — Per-Workflow Report

> All 17 workflows: zero post-ship invocations. The table below records the structural audit.

### Tier 1 — Foundation

| # | Workflow | Tier | Invocations | Avg Composite | Best | Worst <7 | Notes |
|---|---------|------|-------------|--------------|------|----------|-------|
| 01 | Armor Diagnose | Foundation | 0 | — | — | — | UNUSED |
| 02 | Mechanism Test | Foundation | 0 | — | — | — | UNUSED |
| 03 | Cross-Pollinate | Foundation | 0 | — | — | — | UNUSED |
| 04 | Genealogy Attack | Foundation | 0 | — | — | — | UNUSED |

### Tier 2 — Practitioner

| # | Workflow | Tier | Invocations | Avg Composite | Best | Worst <7 | Notes |
|---|---------|------|-------------|--------------|------|----------|-------|
| 05 | Bullet From Winner | Practitioner | 0 | — | — | — | UNUSED |
| 06 | Litotes Line | Practitioner | 0 | — | — | — | UNUSED |
| 07 | Adherence Protocol | Practitioner | 0 | — | — | — | UNUSED |
| 08 | Guru Audit | Practitioner | 0 | — | — | — | UNUSED |
| 09 | Hole Frame | Practitioner | 0 | — | — | — | UNUSED |

### Tier 3 — Stacking

| # | Workflow | Tier | Invocations | Avg Composite | Best | Worst <7 | Notes |
|---|---------|------|-------------|--------------|------|----------|-------|
| 10 | Armor + Iha Proof | Stacking | 0 | — | — | — | UNUSED |
| 11 | Deutsch + Wright Residue | Stacking | 0 | — | — | — | UNUSED |
| 12 | Local Maxima Flywheel | Stacking | 0 | — | — | — | UNUSED |

### Tier 4 — Apex / Mastery

| # | Workflow | Tier | Invocations | Avg Composite | Best | Worst <7 | Notes |
|---|---------|------|-------------|--------------|------|----------|-------|
| 13 | Three-Vector Idea Forge | Apex | 0 | — | — | — | UNUSED |
| 14 | Classical Rhetoric Deploy | Apex | 0 | — | — | — | UNUSED |
| 15 | Post-Hook Architecture | Apex | 0 | — | — | — | UNUSED |
| 16 | Shiny Prediction Engine | Apex | 0 | — | — | — | UNUSED |
| 17 | Fifty-Year Architecture | Apex | 0 | — | — | — | UNUSED |

---

## Step 4 — Strongest Performers

**None.** No workflows reached the minimum threshold of ≥2 invocations during the audit window. There is no performance data to amplify.

The only meaningful score signal is the forge build (composite 8.7 on both extraction finalizes), which speaks to skill architecture quality, not deployment performance.

---

## Step 5 — Weakest / Unused

**Category: Never Tried (all 17 workflows)**

All 17 workflows were zero-deployment during the 6-week window. This is not underperformance when used — it is non-deployment. The distinction matters: underperforming workflows need structural revision; non-deployed workflows need routing and discoverability work.

The 3 most likely activation candidates that were never invoked despite relevant work in the window:

1. **Mechanism Test (02)** — The Coach Cooz V5 project involved evaluating whether Cooz's "total transformation through disciplined choices" mechanism was substantive or hollow. This is textbook Mechanism Test territory. It was handled by the ensemble instead.

2. **Armor Diagnose (01)** — Multiple copy deliverables in the window (VSL lead for Invisible Expert, SFV first-time-homebuyer copy, Coach Cooz profile). Each started with audience-state assumptions rather than a formal armor diagnostic. The Invisible Expert VSL work in particular (May 31) was exactly the problem Armor Diagnose was built for — the audience has "I'm not a marketer" identity armor.

3. **Hole Frame (09)** — The aspirational-permission market (Cooz's fitness coaching, Invisible Expert positioning) is precisely where this workflow applies. Not invoked.

---

## Step 6 — Apex Tier Strategic Verdict

**Aggregate:**
- Total apex (workflows 13-17) invocations: **0**
- Total non-apex (workflows 1-12) invocations: **0**
- Apex-to-non-apex ratio: N/A (both zero)
- Average composite — apex: N/A
- Average composite — non-apex: N/A (forge build only: 8.7)

**Did the apex tier pay for itself?**

No. But neither did the non-apex tier. The failure isn't in the apex architecture — the failure is that the base skill never got deployed first. Apex tiers need a deployment funnel: Foundation workflows get used → deployer builds fluency → Stacking + Apex become natural. That funnel never started.

The 5-workflow apex investment (Three-Vector Idea Forge, Classical Rhetoric Deploy, Post-Hook Architecture, Shiny Prediction Engine, Fifty-Year Architecture) represents the highest conceptual sophistication in the skill roster. These workflows address problems that most copywriters never reach (65 pages past the hook, classical rhetorical figures, meta-trend prediction). Their non-use is not evidence of bloat — it's evidence that the access path to them was never established.

**Recommendation: Keep all 5 apex workflows.** Do not consolidate or archive. The workflows are structurally sound (verified in forge audit at 8.7). The problem is upstream: the Foundation tier needs to get used first.

If the skill remains at zero deployment 6 weeks after the next cycle, revisit the apex consolidation question.

---

## Step 7 — `/skill-evolution` Recommendation

**Do not run `python3 execution/skill_benchmark.py` at this time.**

Rationale: `skill_benchmark.py` compares skill output against ground-truth benchmarks. Running it on a skill with zero production deployments produces benchmark scores that reflect forge quality, not battle-tested performance. The feedback-ratchet protocol (Phase 2) is designed to refine based on observed failure modes — and there are no observed failure modes yet because the skill hasn't run.

**What to do instead:**

1. **Prioritize 3 first deployments.** Route the next relevant copywriting tasks explicitly through Sean:
   - Any new copy project where audience state is unknown → **Armor Diagnose (01)** first
   - Any project where the mechanism is borrowed or inherited → **Mechanism Test (02)** 
   - Any aspirational/info-product audience frame → **Hole Frame (09)**

2. **Add Sean to CLAUDE.md routing internalization.** The current routing table has no Sean signal. Proposed addition:
   ```
   mechanism testing / "does this claim survive scrutiny" / audience-state unknown → Sean Macintyre armor-diagnose + mechanism-test
   ```

3. **After 3-5 production deployments**, run `skill_benchmark.py` to compare outputs against ground-truth persuasion benchmarks. Then re-evaluate apex tier ROI with actual failure mode data.

4. **Evolution cycle recommendation (per `directives/feedback-ratchet.md`):** This skill is in **Phase 1 (Deployment)** — not yet eligible for Phase 2 (Refinement) or Phase 3 (Consolidation). The evolution protocol should be invoked only after meaningful production use, not on forge quality alone.

**Specific workflows to prioritize for first deployment cycle:**
- Workflow 01 (Armor Diagnose) — the gateway; every other workflow runs better with this first
- Workflow 02 (Mechanism Test) — highest re-use across any persuasion/copy context
- Workflow 09 (Hole Frame) — directly relevant to Farrice's Parallax audience and client work

---

## Step 8 — Calibration Verdict

**No calibration changes warranted.**

The skill files are architecturally sound. The 8.7 forge score reflects quality construction. There are no observed failure modes to calibrate against — the workflows have never failed in production because they've never been in production.

Calibration would be premature correction of a hypothesis that hasn't been tested. The workflows stay as-built until production data creates a falsifiable case for revision.

---

## Root Cause Analysis

**Why zero deployments in 6 weeks?**

1. **No routing hook.** Sean isn't in the CLAUDE.md internalized routing table. The routing only fires when the user explicitly invokes Sean or when a workflow's description matches a routing signal the system has been trained to recognize. Sean's signals (armor diagnosis, mechanism testing, genealogy attacks) aren't wired into any automatic dispatch path.

2. **Work volume mismatch.** The 6-week window was dominated by: Jen Santulan real estate copy (not Sean territory), Andrea DJ project (brand/music, not copy persuasion), Coach Cooz (used an ensemble instead of dedicated Sean workflows), Parallax editions (Nicolas Cole + Rory Sutherland are the primary experts), Luke Iha expansion work. None of these were copy projects with the specific character that triggers Sean's specialty — long-form financial/info-product persuasion where the audience's armor is the core problem.

3. **Ensemble substitution.** The Coach Cooz V5 work (May 2) was close to Sean territory. It used him, but as 1 of 13 thinking lenses in a writers-room-style ensemble. The specific diagnostic workflows (Armor Diagnose, Mechanism Test) were subsumed into the ensemble output.

4. **Discovery friction.** The 17 `.agent/workflows/sean-*.md` wrapper files exist but invoke skills that require deliberate loading. Without a pre-flight check that asks "is there a mechanism claim here that needs testing?", the workflow never fires.

---

## Summary

| Metric | Value |
|--------|-------|
| Total invocations (any workflow) | 0 |
| Forge build score | 8.7 composite |
| Notion Performance Log entries (dedicated) | 0 |
| Ensemble appearances | 1 (Coach Cooz V5, May 2) |
| Apex tier invocations | 0 |
| Non-apex tier invocations | 0 |
| Skill auditor tier | A (based on forge quality) / REVIEW (when trace logic changes) |
| Calibration changes needed | None |
| Next action | 3 intentional first deployments → then benchmark |

**The skill is well-built and unproven. The architecture is right. The deployment path needs to be opened.**
