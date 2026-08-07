# Walkthrough: Diandra Escobar Flywheel Workflows

## What Was Built

5 executable flywheel workflows that operationalize Diandra Escobar's LinkedIn growth system into repeatable slash commands.

### LinkedIn-Specific (3)

| Command | Purpose | Parallel Sub-Agents |
|---------|---------|-------------------|
| `/diandra-growth-sprint` | Entity → research → 3 angles → 3 post variations + boomerang | 3 (one per angle) |
| `/diandra-content-engine` | Topic + bucket → enrichment → body-first → 5 hooks + 3 formats | 3 (hook, format, cross-platform) |
| `/diandra-steal-and-remix` | Viral post → pattern extraction → 3 original remixes | 6 (3 analysts + 3 remixers) |

### Universal (2)

| Command | Purpose | Key Difference |
|---------|---------|---------------|
| `/jackpost` | Borrowed attention adapted to ANY platform (LinkedIn, X, Substack, email) | Routes to platform-specific experts |
| `/growth-format-sprint` | Batch 3-5 growth posts from trending entities in one session | Entity scoring + calendar integration |

## Architecture Pattern

All 5 follow the established flywheel architecture from `/mini-brief`:

```
Research gate → Approval checkpoint → Parallel sub-agents → Quality gate → Assembled deliverable
```

**Key features:**
- Sub-agents load skill files fresh (no context bleed)
- Research is mandatory and grounded (real `search_web` + `read_url_content`)
- Approval checkpoints between phases
- Body-first writing method enforced throughout
- Anti-pattern checks against genius.md exemplars

## Files Created

```
.agent/workflows/
  diandra-growth-sprint.md
  diandra-content-engine.md
  diandra-steal-and-remix.md
  jackpost.md
  growth-format-sprint.md
```

## Registrations Updated

- [SLASH_COMMANDS.md](file:///Users/farricecain/Google%20Antigravity/SLASH_COMMANDS.md) — New "LinkedIn Growth Flywheels" section (5 entries) + 5 natural language triggers
- Command count updated: 355 → 360

## Natural Language Triggers

| Say This | Gets You |
|----------|---------|
| "growth post" / "brandjack" / "newsjack" | `/diandra-growth-sprint` |
| "daily content engine" / "body-first writing" | `/diandra-content-engine` |
| "steal and remix" / "study viral posts" | `/diandra-steal-and-remix` |
| "jackpost" / "cross-platform post" | `/jackpost` |
| "growth sprint" / "batch growth posts" | `/growth-format-sprint` |
