# Executable Flywheel Workflows — Diandra Escobar LinkedIn Growth System

Turn Diandra Escobar's expert-prompt workflows into end-to-end executable flywheels that **research, produce, and assemble deliverables** — matching the quality bar of `/mini-brief` and `/ip-flywheel`.

## Problem

Current Diandra workflows (01-14) are **prompt templates** — they describe what to produce but don't orchestrate:
- Live research (Perplexity, `search_web`, `read_url_content`)
- Parallel sub-agent execution
- File I/O (`.tmp/` intermediates, assembled outputs)
- Multi-variant generation
- Approval checkpoints

They're blueprints. We need engines.

## Proposed Changes

### 5 New Slash Commands

All created in `.agent/workflows/` for system-wide invocation.

---

### 1. `/diandra-growth-sprint` — The Growth Post Engine (LinkedIn-specific)

#### [NEW] [diandra-growth-sprint.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/diandra-growth-sprint.md)

**What it does**: Takes any brand, person, or news event → auto-detects jack type → researches the entity → produces 3 angle variations → writes publish-ready posts with boomerang strategy.

**Pipeline**:
```
Input (brand/person/news) or "find me something"
  ↓
Phase 1: Auto-Detect (brandjack vs newsjack vs namejack vs hot take)
  ↓
Phase 2: Research Gate (search_web → entity news, ICP overlap, boomerang viability)
  ↓
Phase 3: Angle Mining (3 angles per Diandra's angle framework)
  ↓  [USER PICKS ANGLE]
Phase 4: Parallel Post Production (3 sub-agents write body-first variations)
  ↓
Phase 5: Hook Mining + Boomerang Strategy
  ↓
Phase 6: Quality Gate + Deliver
```

**Produces**: 3 post variations + hook alternatives + boomerang playbook + visual briefs. Saves to `.tmp/diandra-growth-sprint/`.

---

### 2. `/diandra-content-engine` — The Daily Content Production Line (LinkedIn-specific)

#### [NEW] [diandra-content-engine.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/diandra-content-engine.md)

**What it does**: Takes topic + bucket → runs the full body-first pipeline → produces finished post with 5 hook candidates, visual brief, CTA, and cross-platform adaptations.

**Pipeline**:
```
Input (topic + bucket) or "what should I write today?"
  ↓
Phase 1: Calendar Check (where are we in the 4-bucket ratio?)
  ↓
Phase 2: Topic Enrichment (search_web for fresh data, quotes, stats to ground claims)
  ↓
Phase 3: Body-First Production (write substance → mine for hooks → CTA match)
  ↓
Phase 4: Multi-Variant Assembly (3 format variations: text post, carousel outline, image+text)
  ↓
Phase 5: Cross-Platform Adaptation (Substack-ready, X thread, universal text)
  ↓
Phase 6: Quality Gate + Deliver
```

**Produces**: Publish-ready LinkedIn post + 5 hook candidates + 3 format variations + cross-platform adaptations. Saves to `.tmp/diandra-content-engine/`.

---

### 3. `/diandra-steal-and-remix` — The Content Sourcing Flywheel (LinkedIn-specific)

#### [NEW] [diandra-steal-and-remix.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/diandra-steal-and-remix.md)

**What it does**: Finds viral LinkedIn posts in your niche → extracts structural patterns → produces 3 original remixes in your voice. Diandra's "steal like an artist" methodology operationalized.

**Pipeline**:
```
Input (niche/topic) or (specific URL to study)
  ↓
Phase 1: Outlier Discovery (search_web for top LinkedIn posts in niche, read 5-8 posts)
  ↓
Phase 2: Pattern Extraction (parallel sub-agents: hook analyst, framework analyst, engagement analyst)
  ↓
Phase 3: Mechanic Blueprint (synthesize the structural template)
  ↓  [USER APPROVES OR PICKS FAVORITES]
Phase 4: Remix Sprint (3 parallel agents remix using Farrice's voice + Diandra's body-first method)
  ↓
Phase 5: Content Bank Deposit (save patterns to reusable mechanic library)
  ↓
Phase 6: Quality Gate + Deliver
```

**Produces**: 3-5 outlier breakdowns + mechanic blueprints + 3 original remixes + content bank entries. Saves to `.tmp/diandra-steal-and-remix/`.

---

### 4. `/jackpost` — Universal Borrowed-Attention Engine (platform-agnostic)

#### [NEW] [jackpost.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/jackpost.md)

**What it does**: Platform-agnostic version of the growth sprint. Auto-detects jack type, researches, produces content for ANY platform (LinkedIn, X, Substack, email newsletter), with platform-native formatting.

**Pipeline**:
```
Input (entity + platform) or "find me something trending for [platform]"
  ↓
Phase 1: Entity Research + Jack Type Detection
  ↓
Phase 2: Angle Mining (3 angles, scored by platform fit)
  ↓  [USER PICKS]
Phase 3: Platform-Native Production (routes to platform-appropriate expert alongside Diandra)
  ↓
Phase 4: Multi-Platform Bundle (same angle → LinkedIn + X + newsletter versions)
  ↓
Phase 5: Quality Gate + Deliver
```

**Produces**: Multi-platform content package (3+ platforms) from one entity/angle. Universal usage — not LinkedIn-locked.

---

### 5. `/growth-format-sprint` — Batch Growth Format Production (universal)

#### [NEW] [growth-format-sprint.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/growth-format-sprint.md)

**What it does**: Batch-produces 3-5 growth posts across ALL jack types in a single session. Researches trending brands, people, AND news simultaneously → produces a full week's growth content in one sprint.

**Pipeline**:
```
Input (niche/domain + target platform) or "fill my growth bucket for the week"
  ↓
Phase 1: Trend Scan (parallel research: trending brands, notable people, breaking news in niche)
  ↓
Phase 2: Opportunity Ranking (score each entity by recognition × recency × boomerang potential)
  ↓  [USER PICKS TOP 3-5]
Phase 3: Parallel Production (each post produced by dedicated sub-agent with Diandra + platform expert)
  ↓
Phase 4: Calendar Integration (tag each post by bucket, suggest posting order)
  ↓
Phase 5: Quality Gate + Deliver
```

**Produces**: 3-5 publish-ready growth posts across jack types + posting calendar + boomerang strategies. One-sprint week of growth content.

---

## Architecture Notes

Each flywheel follows the established pattern from `/mini-brief`:
- **Research gates** use `search_web` (free, unlimited) as workhorse + Perplexity (budget-gated)
- **Parallel agents** spawn via Task tool sub-agents in single messages
- **Approval checkpoints** halt at angle selection and production review
- **File I/O** saves intermediates to `.tmp/[workflow-name]/` and presents assembled output
- **Quality gates** run Diandra's rubric (genius.md Quality Rubric) + voice check + anti-pattern scan

## Verification Plan

### Automated
- Verify all 5 `.md` files exist in `.agent/workflows/`
- Verify SLASH_COMMANDS.md entries
- Verify SKILL.md references

### Manual
- Run `/diandra-growth-sprint` with a real brand to test end-to-end execution
