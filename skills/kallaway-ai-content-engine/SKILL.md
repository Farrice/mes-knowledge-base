---
name: kallaway-ai-content-engine
description: Accelerates content production 3-5x using Kallaway's Transactional-Creative Split — automate transactional work (research, outlier mining, hook clustering, scripting structure, analytics) while preserving creative work (unique take, perspective choice, voice, emotional calibration) for humans. Governing metric is Research-to-Reaction Ratio (target 80% AI research / 20% human reaction). Use when scaling content output without losing authenticity, when content production feels like grunt work, when AI is producing technically-correct-but-flavorless content, or when the user mentions "scale content with AI", "AI content engine", "use AI without sounding AI". Trigger proactively when the user describes manual research bottlenecking creative output OR when AI-generated drafts are losing the "sauce" — the Transactional-Creative Split diagnoses both failure modes.
expert: Kallaway
domain: AI-Augmented Content Production Infrastructure
workflows: 5
---

# Kallaway AI-Enabled Content Engine — SKILL.md

## Domain
AI-Augmented Production Infrastructure — the toolchain layer that accelerates every other Kallaway skill 3-5x without sacrificing creative authenticity.

## Expert
Kallaway — Production substrate beneath Content Psychology ("what to build"), Word Mastery ("how to write it"), Audience Obsession ("what to implant"), and Addictive Storytelling ("how to keep them watching"). This domain answers: **"How do you use AI to create more, faster, without losing the sauce?"**

## Core Thesis
AI eliminates **transactional tasks** so humans can spend more time on **creative thinking**. The Transactional-Creative Split is the master filter: automate research, mining, and pattern extraction. Keep human judgment for creative reaction — the authentic take, the unique perspective, the sauce layer. The moment you outsource perspective to AI, content gets stale. The moment you DON'T automate research, you waste creative energy on grunt work.

## Governing Metric
**Research-to-Reaction Ratio** — time spent on AI-powered data mining vs. time spent on human creative response. Target: 80% AI research / 20% human reaction. If a creator spends more time researching than reacting, the pipeline is broken.

For business-facing content, the outcome hierarchy is **email conversions or qualified leads > relevant followers gained > views**. Competitor views are a public discovery proxy, not proof of trust or demand. Once 10-20 owned posts exist, first-party performance should increasingly replace competitor proxies.

## The Decision: Automate vs. Preserve
Every content task falls into one of two categories:
- **Transactional** (→ AI): Topic research, outlier identification, hook format clustering, data analysis, scripting structure, caption generation, analytics compilation
- **Creative** (→ Human): Your unique take, perspective selection, hook angle choice, creative reaction, voice and personality, emotional calibration, strategic interpretation

All workflows in this domain automate the transactional while protecting the creative.

## Signal Producer Contract

`execution/outlier_radar.py` is the default $0 public-data producer. Its versioned pack contract is `execution/specs/outlier-radar-pack.schema.md`. The producer may calculate outlier, engagement, freshness, and confidence; it must not invent cohort fit or promote a topic into production. This skill owns those judgments and passes accepted rows downstream to Growth Blueprint OS or the Kallaway Content Operating System.

Required boundary fields: `evidence_class`, `data_maturity_state`, `cohort_role`, `engagement_rate`, `signal_hygiene`, and `rejection_reasons`. `PUBLIC_PROXY` can discover candidates; it cannot prove demand, conversion, or revenue.

## Workflows (5)

### Tier 1 — Foundation
| Workflow | Slash Command | What It Does |
|----------|--------------|-------------|
| `ai-topic-mining-engine` | `/ai-topic-mining` | Full Sandcastles → Claude topic validation pipeline with ranked categories and idea seeds |
| `ai-hook-pattern-extractor` | `/ai-hook-extractor` | Data-driven hook format clustering, performance ranking, and template generation |

### Tier 2 — Practitioner
| Workflow | Slash Command | What It Does |
|----------|--------------|-------------|
| `ai-creative-reaction-sprint` | `/ai-creative-sprint` | Human-in-the-loop creative process using AI-validated topics — the sauce layer |

### Tier 3 — Stacking
| Workflow | Slash Command | What It Does |
|----------|--------------|-------------|
| `ai-content-operations` | `/ai-content-ops` | AI workflows integrated into team/pod content operations at scale |
| `trend-hook-radar` | `/kallaway-trend-hook-engine` | Compliant signal intake, outlier scoring, hook-pattern clustering, and creative-reaction handoff |

## Stacking Chains
This domain is designed to power every other Kallaway skill:

1. **AI Content Engine** (this domain) = the TOOLCHAIN (how to find and validate faster)
2. **Content Psychology** = the STRATEGY (what to build and why)
3. **Word Mastery** = the CRAFT (how to write it)
4. **Addictive Storytelling** = the RETENTION (how to keep them watching)
5. **Audience Obsession** = the PAYLOAD (what to implant)

**Common stacking sequences**:
- `/ai-topic-mining` → `/ai-hook-extractor` → `/ai-creative-sprint` (full research-to-reaction pipeline)
- `/ai-topic-mining` → `/dopamine-ladder-architect` → `/loop-chain-scripting` (AI research → psychology → retention)
- `/ai-hook-extractor` → `/vicious-hook` → `/obsession-level-architect` (AI patterns → human craft → obsession injection)
- `/ai-content-ops` → `/content-orchestrate` (AI operations → full content orchestration)

## Quality Rubric
All outputs from this domain are evaluated on:
1. **Data Validation %** — every topic/hook backed by outlier evidence? Target: 100%
2. **Human-AI Balance** — did a human make every creative decision? AI did research only?
3. **Workflow Reusability** — is the output a reusable skill, not a one-off prompt?
4. **Speed** — research phase under 10 minutes? Creative reaction time unlimited?
5. **Input Curation** — source channel list hand-curated by taste, not algorithm-suggested?
6. **Output Specificity** — individual idea seeds with source links and performance data?
7. **Metric-Class Discipline** — is each signal labeled private outcome, owned proxy, or public proxy rather than flattened into views?
8. **Cohort Integrity** — are topic comparisons scale-matched, while cross-niche or celebrity examples are used only for transferable formats?
9. **Data Maturity** — does the workflow declare COLD_START, HYBRID, or OWNED_LEARNING and change the research mix accordingly?
10. **Creative Ownership** — does AI stop at evidence and reaction questions rather than inventing the creator's angle or substance?

## File Map
```
skills/kallaway-ai-content-engine/
├── SKILL.md                           ← You are here
├── genius.md                          ← Core intelligence (12 patterns; Patterns 1-6 verified against `ImzoNTrgvFg`; Pattern 7 source UNCONFIRMED; Patterns 8-12 verified/source-stated against `extractions/video-context/GmIn1W9V8Rs/`)
├── references/
│   └── source-ledger.md               ← Claim-by-claim VERIFIED/LIKELY/UNCONFIRMED provenance
└── workflows/
    ├── ai-topic-mining-engine.md      ← Tier 1
    ├── ai-hook-pattern-extractor.md   ← Tier 1
    ├── ai-creative-reaction-sprint.md ← Tier 2
    └── ai-content-operations.md      ← Tier 3
```

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

5 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **AI Content Operations System — [TEAM SIZE], [CONTENT VOLUME]/week** — `skills/kallaway-ai-content-engine/references/prompts-v2/ai-content-operations-system.md`
- **AI Hook Pattern Report — [NICHE/INDUSTRY]** — `skills/kallaway-ai-content-engine/references/prompts-v2/ai-hook-pattern-report.md`
- **AI Topic Mining Report — [NICHE/INDUSTRY]** — `skills/kallaway-ai-content-engine/references/prompts-v2/ai-topic-mining-report.md`
- **Creative Reaction Sprint Package — [BATCH SIZE] seeds** — `skills/kallaway-ai-content-engine/references/prompts-v2/creative-reaction-sprint-package.md`
- **Trend Hook Radar Briefing — [RUN_ID]** — `skills/kallaway-ai-content-engine/references/prompts-v2/trend-hook-radar-briefing.md`

<!-- END:execution-prompts -->
