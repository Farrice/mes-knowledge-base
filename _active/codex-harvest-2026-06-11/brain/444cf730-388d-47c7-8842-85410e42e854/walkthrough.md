# Kieran Flanagan AI Content Team — Extraction Walkthrough

## What Was Built

A complete 3-skill expert with 15 workflows, implementing Kieran Flanagan's AI content team methodology. This is the system for building AI-powered content operations that produce genuinely human-sounding content at scale.

### Architecture: 3-Skill Hybrid

| Skill | Files | Workflows | Purpose |
|-------|-------|-----------|---------|
| `kieran-flanagan-audience-intelligence` | SKILL.md + genius.md | 4 | Research layer: audience profiles, style cards, voice cloning, topic clusters |
| `kieran-flanagan-content-engine` | SKILL.md + genius.md | 8 | Production layer: talking points, lookalike patterns, enrichment, bundling, adaptation, series planning, hooks, competitive intel |
| `kieran-flanagan-content-ops` | SKILL.md + genius.md | 3 | Management layer: session orchestration, performance feedback, monthly reviews |

### Files Created (38 total)

**Extraction** (1 file):
- [extraction-report.md](file:///Users/farricecain/Google%20Antigravity/extractions/kieran-flanagan/extraction-report.md)

**Skills** (21 files across 3 skills):
- [audience-intelligence/SKILL.md](file:///Users/farricecain/Google%20Antigravity/skills/kieran-flanagan-audience-intelligence/SKILL.md) + [genius.md](file:///Users/farricecain/Google%20Antigravity/skills/kieran-flanagan-audience-intelligence/genius.md) + 4 workflows
- [content-engine/SKILL.md](file:///Users/farricecain/Google%20Antigravity/skills/kieran-flanagan-content-engine/SKILL.md) + [genius.md](file:///Users/farricecain/Google%20Antigravity/skills/kieran-flanagan-content-engine/genius.md) + 8 workflows
- [content-ops/SKILL.md](file:///Users/farricecain/Google%20Antigravity/skills/kieran-flanagan-content-ops/SKILL.md) + [genius.md](file:///Users/farricecain/Google%20Antigravity/skills/kieran-flanagan-content-ops/genius.md) + 3 workflows

**Agent** (2 files):
- [AGENT.md](file:///Users/farricecain/Google%20Antigravity/agents/kieran-flanagan/AGENT.md) + [memory/context.md](file:///Users/farricecain/Google%20Antigravity/agents/kieran-flanagan/memory/context.md)

**Workflow Commands** (15 files in `.agent/workflows/`):
- `/content-audience-profile`, `/content-style-card`, `/style-from-creator`, `/content-cluster`
- `/talking-points`, `/lookalike-content`, `/content-enrich`, `/content-bundle`
- `/platform-adapt`, `/content-series-plan`, `/hook-formula-extract`, `/competitor-content-spy`
- `/content-orchestrate`, `/content-feedback`, `/content-review-cycle`

**Registry Updates**:
- Invocation card added to `agents/_framework/invocation-cards.md`
- `AGENT_INDEX.md` synced (106 agents)
- `SKILL_INDEX.md` synced (174 skills)

## Key Genius Patterns Extracted

8 patterns from the source, with the most distinctive being:

1. **Separation of Creation and Optimization** — Never ask the same AI to create AND judge content
2. **Style Cards as Voice DNA** — Structured documents that make AI content sound genuinely human
3. **The Enrichment Layer** — Dedicated AI role that adds data/stories AFTER creation, not during
4. **Invisible System Assets** — The infrastructure (profiles, cards, talking points) that compounds over time
5. **Feedback Loops as Self-Improvement** — Monthly reviews that update system assets based on performance data

## Verification

| Check | Status |
|-------|--------|
| All 21 skill files exist | ✅ |
| All 15 workflow commands exist | ✅ |
| Agent files exist | ✅ |
| Invocation card added | ✅ |
| AGENT_INDEX synced | ✅ (106 agents) |
| SKILL_INDEX synced | ✅ (174 skills) |
| No naming conflicts with existing workflows | ✅ |

## How to Use

**Starting from scratch**: `/content-audience-profile` → `/content-style-card` → `/talking-points` → `/content-orchestrate`

**Quick content production**: `/content-orchestrate full-sprint --platform LinkedIn`

**Improving existing system**: `/content-feedback` → `/content-review-cycle`

**Competitive analysis**: `/competitor-content-spy` → `/lookalike-content`

**Voice cloning**: `/style-from-creator [creator name]`
