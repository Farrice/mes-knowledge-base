# Walkthrough: Luke Iha Insight Vectors Skill Build

## What Was Built

A complete production skill at `skills/luke-iha-insight-vectors/` — Luke Iha's upstream idea engine that generates **insight vectors** (structural interventions in audience mental models) which feed ALL downstream copy, mechanism, and campaign workflows.

> [!IMPORTANT]
> This skill sits UPSTREAM of the existing `luke-iha-proof-mechanisms` skill. Insight Vectors generate the raw conceptual ammunition; Proof Mechanisms deploys it with proof architecture.

---

## Skill Architecture

```
skills/luke-iha-insight-vectors/
├── SKILL.md                          (7.5 KB — core skill file)
├── genius.md                         (14.5 KB — deep context)
├── references/
│   └── insight-vector-framework.md   (7.8 KB — taxonomy reference)
└── workflows/
    ├── mental-model-mapper.md        (6.5 KB — Tier 1)
    ├── insight-vector-generator.md   (6.2 KB — Tier 1)
    ├── insight-elaborator.md         (7.5 KB — Tier 1)
    ├── insight-vector-audit.md       (5.8 KB — Tier 1)
    ├── reverse-causation-engine.md   (5.2 KB — Tier 2)
    ├── archetype-factory.md          (6.3 KB — Tier 2)
    ├── insight-to-mechanism-bridge.md (6.1 KB — Tier 2)
    ├── insight-copy-injector.md      (5.6 KB — Tier 2)
    ├── social-media-insight-engine.md (8.0 KB — Tier 3)
    ├── creative-strategy-insight-brief.md (7.6 KB — Tier 3)
    ├── belief-gap-insight-sprint.md   (12.7 KB — Tier 4)
    └── insight-content-series.md      (9.8 KB — Tier 4)
```

**Total**: 16 files, ~105 KB of production-grade skill content.

---

## Workflow Tiers

### Tier 1 — Core (4 workflows)
| Workflow | Slash Command | Purpose |
|----------|--------------|---------|
| Mental Model Mapper | `/insight-vectors` (Phase 1) | Excavate audience belief architecture |
| Insight Vector Generator | `/insight-vectors` (Phase 2) | Systematic generation across 10 categories |
| Insight Elaborator | `/insight-elaborate` | 8-fold elaboration into copy ammunition |
| Insight Vector Audit | `/insight-audit` | Audit existing copy for vector coverage |

### Tier 2 — Practitioner (4 workflows)
| Workflow | Slash Command | Purpose |
|----------|--------------|---------|
| Reverse Causation Engine | `/reverse-cause` | Dedicated causal arrow flipping engine |
| Archetype Factory | `/archetype-build` | Build typing systems for any domain |
| Insight → Mechanism Bridge | `/insight-bridge` | Convert vectors to SIN-scored mechanisms |
| Insight Copy Injector | `/insight-inject` | Inject vectors into existing flat copy |

### Tier 3 — Applied Channels (2 workflows)
| Workflow | Slash Command | Purpose |
|----------|--------------|---------|
| Social Media Insight Engine | `/insight-social` | Platform-native social content from vectors |
| Creative Strategy Insight Brief | `/insight-brief` | Campaign brief built on vector architecture |

### Tier 4 — Cross-Expert Stacking (2 workflows)
| Workflow | Slash Command | Purpose |
|----------|--------------|---------|
| Belief Gap Sprint | `/belief-gap-sprint` | McRaney × Iha deep belief dissolution |
| Insight Content Series | `/insight-series` | Multi-part series with progressive stacking |

---

## Key Design Decisions

1. **Taxonomy**: 10 vector types across 4 categories (Causality, Pattern, Control Point, Structural) — based on systems thinking applied to audience mental models.

2. **SIN Filter**: Simple + Intuitive + New scoring (1-10 each, /30). Vectors ≥21 are deploy-ready. This quality gate is referenced across all workflows.

3. **8-Fold Elaboration**: The core expansion protocol that takes a raw vector → full copy block (paradoxical question → UMP → trigger → proof → intensifiers → myth busting → root cause → resolution).

4. **Cross-Expert Integration**: The Tier 4 belief-gap sprint includes a full McRaney framework (even if the McRaney skill doesn't exist yet) for belief diagnosis and dissolution.

5. **Genius Patterns**: 12 patterns + 8 hidden knowledge items covering when NOT to use vectors, density calibration, stack ordering, and the self-persuasion effect.

---

## System Integration

- **Skill paths reference**: Added `Luke Iha (Insight Vectors)` entry to `directives/skill-paths-reference.md`
- **Slash commands**: 11 entries created in `.agent/workflows/` — all discoverable via standard routing
- **Pipeline position**: This skill is the upstream SOURCE for insight vectors, mechanisms, hooks, and content across the Antigravity system

---

## How To Use

**Generate vectors**: `/insight-vectors` with a topic + audience
**Elaborate one vector**: `/insight-elaborate` with a specific vector
**Audit existing copy**: `/insight-audit` with the copy to analyze
**Mine reverse causation**: `/reverse-cause` with a market's causal beliefs
**Build types**: `/archetype-build` with a domain
**Bridge to mechanisms**: `/insight-bridge` with shortlisted vectors
**Inject into copy**: `/insight-inject` with existing copy
**Generate social**: `/insight-social` with vectors + platform
**Build campaign brief**: `/insight-brief` with product + objective
**Dissolve blocking beliefs**: `/belief-gap-sprint` with product + conversion block
**Design content series**: `/insight-series` with series theme + platform
