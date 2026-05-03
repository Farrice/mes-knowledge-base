---
description: Diagnose any AI context system across the 5 CDLC stages and prescribe upgrades
---

# Workflow 1 — CDLC Audit

Diagnose any AI context system (skills + agents + directives) using Patrick Debois's Context Development Life Cycle. Score each of the 5 stages, identify the bottleneck stage (the one rate-limiting the whole loop), and prescribe specific upgrades.

## Pre-Flight Gate

Run this audit ONLY when:
- The target system has 5+ context artifacts (skills, agents, prompts, directives) — below this, CDLC is overkill
- Artifacts are being authored, deployed, AND improved over time (loops, not one-shots)
- The user wants a *systems* diagnosis, not a single-artifact review

**Skip if**: The user wants you to fix one prompt. Use a targeted skill review instead.

## Skill Acquisition

Load `skills/patrick-debois-cdlc/genius.md` if not already in context. Anchor to:
- **Pattern 2** (Lifecycle Loop Reflex) — the audit IS the loop, applied recursively
- **Pattern 3** (Lint → Grammarly → Eval ladder) — used to grade Test stage
- **Pattern 6** (Library → Registry → Marketplace arc) — used to grade Distribute stage
- **Signature Move 2** (Demand the Test Tier) — primary diagnostic move
- **Signature Move 5** ("Crap Until Proven Otherwise") — baseline classification rule

## Input Required

- **Target system name**: What you're auditing (e.g., "Antigravity skills+agents+directives", "team-X prompt library")
- **Artifact inventory**: List of skills/agents/directives/prompts (counts + paths). If unavailable, run a discovery pass first.
- **Existing instrumentation**: Any current evals, logs, registries, scanners (or "none")
- **Constraint**: What the user can change vs. inherit (full control / shared with team / locked)

## Execution

### Step 1: Inventory & Stage Mapping

For each artifact, tag which CDLC stages currently have ANY tooling:

| Stage | Has tooling? | Evidence |
|---|---|---|
| Generate | Y/N | (e.g., "AGENT.md template, prompt scaffolds") |
| Test | Y/N | (e.g., "ZERO evals" or "lint-only via skill_validator.py") |
| Distribute | Y/N | (e.g., "git checkin only — no version pins, no registry") |
| Observe | Y/N | (e.g., "performance log fires, but no log → context-improvement loop") |
| Adapt | Y/N | (e.g., "evolution_orchestrator.py exists but unfired") |

### Step 2: Stage Scoring (1-10 per stage)

Use the rubric anchors from `genius.md`. Score each stage:

**Generate** — How systematic is context creation?
- 1-3: Ad-hoc copy-paste. No templates, no scaffolds.
- 4-6: Templates exist but inconsistent application. Voice-coded or handwritten.
- 7-9: Templates + skill-spec format + spec-driven prompts → planning mode.
- 10: Generate-stage tooling produces context that consistently passes Test-stage on first try.

**Test** — Test tier coverage?
- 1-3: Nothing. Or vibes-based review only.
- 4-6: Lint-tier only (syntax/format validation).
- 7-9: Lint + Grammarly + LLM-as-judge unit tests.
- 10: Full ladder including e2e with tools, all with N-run error budgets.

**Distribute** — Distribution maturity?
- 1-3: Copy-paste over Slack/DM.
- 4-6: Checked into repo, no versioning.
- 7-9: Versioned packages with discoverability index.
- 10: Registry with semver, deps, security scan, SBOM.

**Observe** — Feedback loop closure?
- 1-3: No feedback channel. Or feedback exists but discarded.
- 4-6: Manual log reading. Performance metrics tracked but not acted on.
- 7-9: Standardized log schema consumed by tooling. Recurring-failure detection.
- 10: Production failures auto-generate test cases. PR comments auto-trigger context upgrades.

**Adapt** — Loop closure & cadence?
- 1-3: No formal adaptation cycle. Improvements happen ad-hoc when remembered.
- 4-6: Manual review cadence (monthly retro), inconsistent execution.
- 7-9: Automated cadence (weekly/daily orchestrator) with logged decisions.
- 10: Auto-generated improvement candidates from Observe stage flow into Generate stage with human approval gate.

### Step 3: Bottleneck Identification

The **bottleneck stage** is the lowest-scored stage (ties broken by upstream-first: Generate < Test < Distribute < Observe < Adapt).

**Why**: A loop is paced by its weakest stage. Improving any stage other than the bottleneck wastes effort. This is Goldratt's Theory of Constraints applied to context engineering.

### Step 4: Upgrade Prescription

For the bottleneck stage AND the second-weakest stage, prescribe:

- **Specific tools/files to create or modify**
- **Tier target** (move from current tier → next tier, not all the way to savant)
- **Estimated effort** (hours / days / sprints)
- **Success criterion** (how you'll know the upgrade worked)
- **Anti-pattern to avoid** (the lazy version of this upgrade that won't actually help)

For the other 3 stages, document briefly: "current tier acceptable" or "deferred — upgrade after bottleneck resolved."

### Step 5: Reflexive Application Check

If the audited system is itself an extraction/skill system (like Antigravity), explicitly note:
- Does the audited system have a CDLC for ITS OWN context artifacts?
- If the system creates skills but has no Test stage for those skills, that's a recursive bottleneck.

## Content Type Adaptations

| If auditing... | Emphasize | De-emphasize |
|---|---|---|
| Personal solo system | Generate + Test stages | Distribute (no team to share with) |
| Team library (10-100 artifacts) | Distribute + Observe | Adapt (cadence emerges later) |
| Org-wide platform (100+ artifacts, multi-team) | All 5 stages, with extra weight on Distribute (registry tier) and Observe (multi-team feedback) | Generate (likely already mature) |
| Antigravity itself | All 5 stages explicitly + reflexive application check | None |

## Output Schema

```markdown
# CDLC Audit — [Target System Name]

## Inventory
- Artifact counts: [skills: X, agents: Y, directives: Z, etc.]
- Existing instrumentation: [list]
- Constraints: [list]

## Stage Scores

| Stage | Score | Evidence |
|---|---|---|
| Generate | X/10 | [1 sentence] |
| Test | X/10 | [1 sentence] |
| Distribute | X/10 | [1 sentence] |
| Observe | X/10 | [1 sentence] |
| Adapt | X/10 | [1 sentence] |

## Bottleneck

**[Stage name]** — Score: X/10

**Why this is the bottleneck**: [2-3 sentences citing specific evidence]

## Upgrade Prescription

### Bottleneck: [Stage] → Target tier [N+1]
- **Specific changes**: [bulleted list of files/tools to create or modify]
- **Effort estimate**: [hours/days/sprints]
- **Success criterion**: [measurable outcome]
- **Anti-pattern to avoid**: [the lazy version that won't help]

### Second priority: [Stage] → Target tier [N+1]
[Same format]

### Deferred (acceptable current tier)
- [Stage 1]: [1-line justification]
- [Stage 2]: [1-line justification]
- [Stage 3]: [1-line justification]

## Reflexive Application Check
[If applicable: does the audited system have a CDLC for its own artifacts?]

## 30-Day Success Metric
After implementing the bottleneck upgrade, the lowest-scored stage should move from [current score] to ≥[target score]. Re-run this audit on day 30 to confirm.
```

## Example Output

**Context**: Audit of Antigravity itself (210 skills, 117 agents, 58 directives, audit infrastructure already in place per 2026-04-24 system audit).

**THE DELIVERABLE:**

```markdown
# CDLC Audit — Antigravity Context System

## Inventory
- Artifact counts: 210 skills, 117 agents, 58 directives, ~800 workflow files
- Existing instrumentation: skill_auditor.py (tier classification), eval_harness.py (rubric anchoring), routing_enforcer.py (binding enforcement), recall_logger.py (grounding observability), evolution_orchestrator.py (loop closure)
- Constraints: Full control. Solo operator. ~$30/mo Perplexity, $20 Fal wallet, 100/mo NotebookLM.

## Stage Scores

| Stage | Score | Evidence |
|---|---|---|
| Generate | 8/10 | MES 3.0 extract directive, AGENT_TEMPLATE, completion-engine skill format, spec-driven /extract → /extract-forge ladder. Voice-coded directives are unusually elaborate. |
| Test | 4/10 | Lint-tier exists (skill format validators). LLM-as-judge tests EXIST as a concept (eval_harness.py rubric anchors, finalize() scoring) but only 16 ground-truth benchmarks across 7 domains for 210 skills. Single-run evals (no error budgets). |
| Distribute | 5/10 | Git-checkin only. No version pins per skill. Indexed (AGENT_INDEX.md, SKILL_INDEX.md) but no semver, no dependency declarations, no security scan. |
| Observe | 6/10 | Performance log fires (chain_runner.finalize), recall_logger now auto-fires (post-2026-05-03 fix), routing_decisions.jsonl exists. PR feedback → context upgrade loop is informal. Production failure → eval-case loop is absent. |
| Adapt | 6/10 | evolution_orchestrator.py exists with daily/weekly/monthly cadences. /skill-evolution must be triggered manually (Phase 2 activation gap from 2026-04-06). |

## Bottleneck

**Test** — Score: 4/10

**Why this is the bottleneck**: 210 skills exist; only 16 ground-truth benchmarks exist. The 2026-04-24 calibration check found 94-99% of finalize scores were 8+ — empirical proof of grade inflation, which is the symptom of a missing Test stage. Without unfakeable evals (Patrick's awesome-prefix test), the Generate stage produces artifacts that LOOK quality without proof. Every other stage is paced by this gap because Distribute can't filter quality, Observe has no signal to threshold against, and Adapt has no calibration anchor.

## Upgrade Prescription

### Bottleneck: Test → Target tier 7 (Lint + Grammarly + unit tests with budgets)
- **Specific changes**:
  - Create `evolution_store/eval_suites/[skill-name]/` directory pattern. Each contains: `lint.json` (skill format spec), `grammarly.md` (semantic completeness criteria), `unit_tests.jsonl` (LLM-as-judge tests, ≥3 per skill).
  - Author unit tests for top 20 skills first (by usage from performance log). Patrick's unfakeability rule: each test must include input/output that ONLY a context-loaded agent could produce.
  - Extend `eval_harness.py` with `run --skill X --runs 5` to execute N-run evals with success-rate output.
  - Add error budget field to skill frontmatter: `error_budget: { critical: 0.95, normal: 0.80 }`.
  - Wire `chain_runner.finalize()` to consult eval results when Expert Standard score is claimed ≥8 — if no recent eval, downgrade to ≤7.
- **Effort estimate**: 3 sprints (1 sprint = framework + 5 skills; 2 sprints = next 15 skills).
- **Success criterion**: Top 20 skills have ≥3 unit tests each, all running on a 5-run + budget basis. Calibration drift report shows finalize-score distribution matches eval-success-rate distribution within ±10%.
- **Anti-pattern to avoid**: Authoring tests that ANY model would pass (e.g., "output is valid markdown"). Every test must satisfy Patrick's awesome-prefix rule — passing PROVES context loaded.

### Second priority: Distribute → Target tier 6 (versioned packages)
- **Specific changes**:
  - Add `version: X.Y.Z` to all SKILL.md frontmatter; semver bump rules: major = breaking workflow signature change, minor = new workflow added, patch = content/prompt refinement.
  - Add `depends_on: [skill-name@version]` for cross-skill stacking guides.
  - Create `evolution_store/skill_versions.jsonl` log of every version bump with diff summary.
- **Effort estimate**: 1 sprint.
- **Success criterion**: Skill audit report shows 100% version-pin coverage. Cross-skill stacking calls reference specific versions.
- **Anti-pattern to avoid**: Bumping versions cosmetically without diff justification. Version bumps are commitments to backward compat.

### Deferred (acceptable current tier)
- Generate (8/10): Already strong. Don't optimize until Test catches up — improving Generate while Test is broken just produces more uncalibrated output faster.
- Observe (6/10): Recent fixes (recall_logger, routing_decisions) brought this above acceptable. Production-failure → eval-case loop is the next upgrade, but it's unbuildable without a Test stage to absorb the cases.
- Adapt (6/10): evolution_orchestrator infrastructure is in place; cadence enforcement via `loop`/`schedule` skills exists. Phase 2 activation gap closes automatically once Test stage produces signal worth adapting on.

## Reflexive Application Check

Antigravity creates skills and has no Test stage for those skills. The 2026-04-24 system audit found this empirically. The recursive bottleneck is: the *system that authors context* has no CDLC Test stage for *the context it authors*. This audit applied to itself produces the same finding — which is the strongest possible evidence the diagnosis is correct.

## 30-Day Success Metric
After implementing the Test stage upgrade for the top 20 skills, finalize-score distribution should normalize from "94-99% scoring 8+" to a realistic distribution (rough target: 30% at 8+, 50% at 6-7, 20% below 6). Re-run this audit on 2026-06-03.
```

**What elevates this**:
- Identifies the bottleneck using *evidence already in the system* (the 2026-04-24 audit's calibration finding) rather than fresh speculation
- Prescription is specific to specific tools (eval_harness.py, chain_runner.finalize) — actionable in this session
- Reflexive application check is brutal: the system that audits skills has no audit for the skills it audits. The finding is recursive, which is the strongest validation
- Anti-patterns named explicitly (especially "tests that ANY model would pass" — Patrick's core insight)
- Deferred stages have justified deferrals, not generic "good enough"

## Quality Gate

Before delivering, verify:
- [ ] All 5 stages scored 1-10 with specific evidence (not vibes)
- [ ] Bottleneck identified using upstream-first tiebreaker
- [ ] Upgrade prescription names specific files/tools (not abstractions)
- [ ] Each prescription has effort estimate + success criterion + anti-pattern
- [ ] Deferred stages have justified deferrals, not omissions
- [ ] If target system is itself a context system, reflexive application check fires
- [ ] No prescription claims tier 10 — always next-tier-up, not aspirational

## Stacks With

- **`/system-audit`** — System audit gives the empirical baseline; CDLC audit gives the lifecycle frame to organize the findings
- **`/skill_auditor.py`** — Use auditor classification (A/B/C/REVIEW) as the empirical input to Test stage scoring
- **`/eval_harness.py status`** — Calibration coverage feeds directly into Test stage score
- **Patrick's `/context-evals`** (next workflow) — Audit identifies which stage to upgrade; `/context-evals` builds the actual eval suite
