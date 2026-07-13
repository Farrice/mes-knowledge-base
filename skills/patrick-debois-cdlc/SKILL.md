---
name: patrick-debois-cdlc
description: Treat AI context as code with a full development lifecycle — Generate, Test, Distribute, Observe, Adapt. From the founder of DevOps applied to AI engineering.
version: "2.0"
format: "completion-engine"
workflows: 4
expert: "Patrick Debois"
domain: "AI-augmented engineering / context engineering"
source: "AI Engineering Summit keynote, 2026 — 'Context is the new code'"
source_url: "https://www.youtube.com/watch?v=bSG9wUYaHWU"
extracted: "2026-05-03"
extracted_with: "claude-opus-4-7[1m]"
---

# Patrick Debois — Context Development Life Cycle (CDLC)

The founder of DevOps applied his 2009 question (*"what if ops looked more like dev?"*) to AI engineering in 2025: **"what if context is the code?"** Result: the **CDLC** — a 5-stage lifecycle (Generate → Test → Distribute → Observe → Adapt) that treats AI context as code with full systems-engineering discipline.

Use this skill when you need to **diagnose, build, or evolve any AI context system** — skills, agents, directives, prompts, multi-agent orchestrations.

## Expert Context

Patrick Debois is the only practitioner with the credentials to extend the DevOps mental model into AI-augmented engineering at the lifecycle level. His insight: AI engineering teams in 2025 are 3-5 years behind where DevOps was in 2014. He's reapplying the exact maturity arc DevOps traveled (2009-2015) to context engineering (2025-2028) — and the entire upcoming tooling wave is predictable from this analog: context linters, context eval frameworks, context registries with semver, context security scanners, context observability platforms.

**Direct relevance to Antigravity**: The system operates at registry-tier complexity (210 skills, 117 agents, 58 directives) but at copy-paste-tier hygiene. The 2026-04-24 system audit identified this gap empirically. CDLC provides the lifecycle vocabulary to organize what's already being built (`eval_harness.py`, `routing_enforcer.py`, `skill_auditor.py`, `evolution_orchestrator.py`) and what needs to be built next.

---

## Workflows

| # | Slash Command | What It Produces | When to Deploy |
|---|---------------|------------------|----------------|
| 1 | `/cdlc-audit` | Diagnostic scoring of any AI context system across 5 CDLC stages with bottleneck identification + per-stage upgrade prescriptions | When a system has 5+ context artifacts and the user wants a *systems* diagnosis (not a single-artifact review) |
| 2 | `/context-evals` | Complete eval suite for one target artifact: lint + Grammarly + LLM-as-judge unit tests + e2e tests, all with N-run success rates and calibrated error budgets | When a load-bearing artifact has no eval coverage or only lint-tier |
| 3 | `/context-library` | Migration plan from current distribution tier to next: version pins, dependency declarations, security scans, SBOMs, predicted failure modes | When a collection has 10+ artifacts being shared across projects/teammates and the user is hitting version-drift or dependency friction |
| 4 | `/context-observe` | Observability loop closure: three feedback channels (agent logs / PR comments / prod failures) wired to context-improvement candidates with explicit trust budget and review cadence | When the system has ≥2 weeks of operational data, recurring failures are appearing, and existing context is mature enough to diagnose vs rebuild |

---

## Stacking Guide

### Within this skill
The 4 workflows form a sequence:
1. **`/cdlc-audit`** identifies which stage is the bottleneck
2. **`/context-evals`** upgrades the Test stage (most common bottleneck)
3. **`/context-library`** upgrades the Distribute stage
4. **`/context-observe`** upgrades the Observe + Adapt stages

Run `/cdlc-audit` first. The other 3 are prescriptions tied to specific stage scores.

### With existing Antigravity infrastructure

| Patrick's Workflow | Stacks With | Why |
|---|---|---|
| `/cdlc-audit` | `/system-audit`, `skill_auditor.py audit`, `eval_harness.py status` | Patrick's audit gives the lifecycle frame; existing tools give empirical evidence to score against |
| `/context-evals` | `eval_harness.py` (runner), `chain_runner.finalize` (production-failure feed) | This workflow produces the suite; the harness executes it; finalize feeds prod failures into pending tests |
| `/context-library` | `skill_auditor.py`, `evolution_orchestrator.py` | Auditor's A/B/C/REVIEW classification feeds quality gating; orchestrator can monitor version drift |
| `/context-observe` | `recall_logger.py`, `routing_enforcer.py`, `evolution_orchestrator.py` | Existing loggers ARE Patrick's Channel 1; orchestrator's daily/weekly/monthly cadence IS Patrick's review loop |

### With other expert skills

| Patrick's Workflow | Pairs With | Compound Output |
|---|---|---|
| `/cdlc-audit` | `/system-hygiene` | Lifecycle diagnosis + tactical hygiene fixes |
| `/context-evals` | Lara Acosta / Luke Iha / Sean Macintyre voice skills | Author voice-specific unfakeability tests (Pattern 20 detection, AI-tells-banned tests, etc.) |
| `/context-library` | `evolution-direction.md` | Library curation aligned with current evolution priorities |
| `/context-observe` | `/skill-evolution`, `/evolution-status` | Observe loop feeds skill-evolution review queue |

---

## Quick Reference — Patrick's 5 Signature Moves

| # | Move | Trigger |
|---|------|---------|
| 1 | **Force the Parallel First** — name the established discipline this resembles before proposing anything new | Introducing infrastructure for an emerging domain |
| 2 | **Demand the Test Tier** — "what tier is your eval — lint, Grammarly, unit, or e2e?" | Auditing any context artifact |
| 3 | **Run-It-Five-Times Reflex** — never single-run an LLM eval; always N-run with error budget | Any LLM-as-judge evaluation |
| 4 | **Convert PR Argument to Context Upgrade** — instead of arguing the comment, ask what context would have prevented it | PR review friction with AI-generated code |
| 5 | **Default to "Crap Until Proven Otherwise"** — baseline classification is REVIEW, eval evidence required to elevate | Auditing third-party or legacy context library |

---

## Quality Standard

Every output from this skill should pass Patrick's unfakeability test:
> *"If this artifact were not loaded, would the output still pass the test?"*
> If yes → the test is theatre. Re-author so passing PROVES context loaded.

---

## Anti-Patterns Rejected by This Skill

- **Single-run eval theatre** — Treating LLM-as-judge results as deterministic
- **Lint-only confidence** — Skill that passes format validation but has no semantic or behavioral tests
- **Default-A skill classification** — 90%+ A-tier without eval evidence is inflation
- **Sandbox-as-only-defense** — Sandboxes don't filter what's loaded; context filter is separate, required
- **Static eval suites** — Suites that don't grow from production failures rot
- **Generate-only thinking** — All attention on prompts while Test/Distribute/Observe stages are unstaffed
- **Argue-the-PR reflex** — Every PR comment that could be solved by better context but instead becomes a turf war
- **Tier-skipping in distribution** — Tier 1 → Tier 3 fails because Tier 2 forcing functions weren't internalized

---

## Reference: The CDLC Loop

```
            ┌─────────────────────────────────┐
            │                                 │
        ▼   │                                 │   ▲
    GENERATE → TEST → DISTRIBUTE → OBSERVE → ADAPT
        ▲                                     │   ▼
            │                                 │
            └─────────────────────────────────┘
```

Loops are paced by their weakest stage. Improving any stage other than the bottleneck wastes effort. (Goldratt's Theory of Constraints, applied to context engineering.)

---

## Source Attribution

All extraction from: Patrick Debois, "Context is the new code / Context Development Life Cycle" — AI Engineering Summit architect track keynote, ~25 minutes, 4,276 words. Source URL: https://www.youtube.com/watch?v=bSG9wUYaHWU

Patrick is currently founder/CTO at **Tessl**, building tooling for the CDLC he describes. His next conference: **AI DevCon London**, June 1-2, 2026 (he curates the content).

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

4 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **CDLC Audit — [TARGET_SYSTEM]** — `skills/patrick-debois-cdlc/references/prompts-v2/cdlc-audit.md`
- **Eval Suite — [TARGET_ARTIFACT]** — `skills/patrick-debois-cdlc/references/prompts-v2/context-eval-suite.md`
- **Context Library Curation — [TARGET_COLLECTION]** — `skills/patrick-debois-cdlc/references/prompts-v2/context-library-migration.md`
- **Observability Loop — [TARGET_SYSTEM]** — `skills/patrick-debois-cdlc/references/prompts-v2/observability-loop-closure.md`

<!-- END:execution-prompts -->
