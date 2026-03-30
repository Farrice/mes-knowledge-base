---
name: "David McRaney: Belief Change Architecture"
description: "Complete belief change architecture — from psychological diagnosis through persuasion engineering to commercial application — based on David McRaney's How Minds Change + Spencer Greenberg interview synthesis"
version: "3.0"
format: "completion-engine"
workflows: 14
---

# David McRaney: Belief Change Architecture

The science of how minds actually change — translated from McRaney's synthesis of Street Epistemology, Deep Canvassing, Motivational Interviewing, Elaboration Likelihood Model, and cognitive psychology into deployable frameworks for audience research, persuasion, and conversion.

David McRaney's *How Minds Change* integrates previously siloed disciplines into a unified theory of belief modification. This skill converts that theory into deployable systems for:
1. **Belief Diagnosis & Research** — Map belief structures, processing routes (ELM), emotional sediment, and metacognitive profiles
2. **Threshold Calculation** — Quantify the exact social/identity cost of change using the 30% empirical calibration
3. **Intervention Design** — Match strategy to belief type, processing route, and rebuttal type

## Apex Workflows (v3.0)

These 10 workflows form a complete belief-change production system. The **Creative Brief** is the hub — all others accept its output.

| Slash Command | Workflow | Produces |
|--------------|---------|----------|
| `/belief-creative-brief` | [Belief-Layer Creative Brief](workflows/belief-layer-creative-brief.md) | Master intelligence document — feeds every downstream workflow |
| `/mcraney-deep-canvass` | [Deep Canvassing Research Sprint](workflows/deep-canvassing-research-sprint.md) | 5-phase Belief Architecture Document from Perplexity research |
| `/persuasion-copy` | [Persuasion-Engineered Copy Engine](workflows/persuasion-engineered-copy-engine.md) | McRaney × Luke Iha finished copy with ELM + proof + accommodation |
| `/accommodation-audit` | [Accommodation Audit](workflows/accommodation-audit.md) | 7-point quality gate — accommodation vs assimilation |
| `/belief-dissolve-copy` | [Belief Dissolution Copywriting](workflows/belief-dissolution-copywriting.md) | Copy that dissolves a specific blocking belief from within |
| `/resistance-proof-rx` | [Resistance-Matched Proof Rx](workflows/resistance-matched-proof-rx.md) | McRaney diagnosis → Luke Iha proof prescription |
| `/threshold-campaign` | [Threshold-Optimized Campaign](workflows/threshold-optimized-campaign.md) | Multi-touchpoint campaign targeting the binding constraint |
| `/metacognitive-content` | [Metacognitive Thought Leadership](workflows/metacognitive-thought-leadership.md) | Content that triggers genuine self-examination |
| `/elm-content-strategy` | [ELM Content Strategy](workflows/elm-content-strategy.md) | Platform × processing route matrix with matched prescriptions |
| `/social-permission-campaign` | [Social Permission Campaign](workflows/social-permission-campaign.md) | Campaign to reduce social cost of adoption |

### Workflow Hub Architecture

```
                    /belief-creative-brief
                    (master document — run ONCE)
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
  /mcraney-deep-canvass   Section 3         Section 2
  (feeds Section 1)     ┌───┴───┐         ┌───┴───┐
        │               ▼       ▼         ▼       ▼
        │    /elm-content   /resistance  /social-permission
        │    -strategy      -proof-rx    -campaign
        │
        ├──► /persuasion-copy
        ├──► /belief-dissolve-copy
        ├──► /threshold-campaign
        └──► /metacognitive-content
                    │
                    ▼
            /accommodation-audit
            (quality gate — run LAST)
```

## Legacy Workflows (v2.1)

| # | Workflow | Produces |
|---|---------|----------|
| strategic | [Strategic Persuasion Campaign Blueprint](workflows/strategic-persuasion-campaign-blueprint.md) | 1-on-1 or small-scale persuasion roadmap |
| social | [Social Influence & Norm-Shift Strategy](workflows/social-influence-norm-shift-strategy.md) | Group behavior shift and tribal bridge plan |
| high | [High-Resistance Intervention Protocol](workflows/high-resistance-intervention-protocol.md) | Emergency de-escalation for extreme beliefs |
| belief-intel | [Belief-First Audience Intelligence](workflows/belief-first-audience-intelligence.md) | Belief-aware consumer posture profile (Dai Media cross-stack) |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow (26 patterns, 13 hidden knowledge items)
- **Legacy Prompts**: [references/_legacy-prompts/](references/_legacy-prompts/) — archived atomic prompts
- **Source Material**: [references/spencer-greenberg-interview-notes.md](references/spencer-greenberg-interview-notes.md) — v2.1 extraction source
