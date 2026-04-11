# Context Injection Baseline Audit (Corrected)

> Measured: 2026-04-11 06:35:54 UTC
> Branch: context-optimization
> Script: `execution/measure_injection.py`

## What This Measures

The Antigravity / Claude Code harness injects three things into the system prompt on every turn:

1. **`.claude/commands/*.md`** — slash command registrations. Each file is a single-line delegator. Listed in the system reminder as the available skills/workflows. **THIS is the actual workflow injection source**, not `.agent/workflows/`.
2. **`CLAUDE.md`** — project instructions, loaded as part of the system prompt.
3. **`MEMORY.md`** — auto-memory index, loaded by the auto-memory system every turn.

Files in `.agent/workflows/` are workflow CONTENT — they load on invocation, not every turn. They cost zero per-turn injection.

## Summary (per-turn fixed injection)

| Source | Files | Chars (truncated) | Est. Tokens | Notes |
|---|---|---|---|---|
| `.claude/commands/` slash command registrations | 199 | 20,099 | ~5,024 | each entry capped ~100 chars in actual injection |
| `CLAUDE.md` | 1 | 14,911 | ~3,727 | full file always loaded |
| `MEMORY.md` | 1 | 17,556 | ~4,389 | full file always loaded |
| **Total fixed injection per turn** | | **52,566** | **~13,141** | |

### For reference (NOT injected, no per-turn cost)

| Source | Files | Total Chars | Notes |
|---|---|---|---|
| `.claude/commands/` untruncated | 199 | 31,574 | ~7,893 tokens if no truncation |
| `.agent/workflows/` (workflow content) | 524 | 1,150,412 | content store — loads on invocation only |

## Registration vs Content Mismatch

- Slash commands registered in `.claude/commands/`: **199**
- Workflow files present in `.agent/workflows/`: **524**
- Workflows with NO slash command registration (dormant on disk): **325**
- Slash commands pointing to MISSING workflow files (broken delegators): **0**

### Dormant workflows (file exists but no slash command — zero injection cost)

First 30 of 325:

- `aar`
- `accommodation-audit`
- `affiliate-select`
- `affiliate-traffic`
- `ai-ad-production`
- `ai-affiliate-site`
- `ai-app-revenue`
- `ai-lead-scraper`
- `algorithmic-reach`
- `analogy-engine`
- `anti-homogenization-audit`
- `archetype-build`
- `authority-flywheel`
- `authority-manufacturing`
- `auto-experiment`
- `belief-creative-brief`
- `belief-dissolution-engine`
- `belief-dissolve-copy`
- `belief-first-audience-intelligence`
- `belief-gap-sprint`
- `betting-edge`
- `bitter-lesson-check`
- `blue-chip-client`
- `book-atomize`
- `book-never-ends`
- `caleb-4c-intro`
- `caleb-brand-audit`
- `caleb-brand-build`
- `caleb-content-sprint`
- `caleb-format-strategy`
- ... and 295 more

## Top 20 Heaviest Slash Commands (by untruncated injection length)

| Slug | Untruncated Chars | Content (first 80 chars) |
|---|---|---|
| `/check-picks` | 275 | Read and execute the workflow at `.agent/workflows/check-picks.md` — Fast-path N… |
| `/picks-tonight` | 243 | Read and execute the workflow at `.agent/workflows/picks-tonight.md` — Tonight's… |
| `/build` | 242 | Read and execute the workflow at `.agent/workflows/build.md` — System Improvemen… |
| `/maintenance` | 238 | Read and execute the workflow at `.agent/workflows/maintenance.md` — Weekly Inte… |
| `/deep-work` | 236 | Read and execute the workflow at `.agent/workflows/deep-work.md` — Full Chain St… |
| `/parallax` | 234 | Read and execute the workflow at `.agent/workflows/parallax.md` — Produce Parall… |
| `/picks-status` | 225 | Read and execute the workflow at `.agent/workflows/picks-status.md` — Full track… |
| `/picks-review` | 211 | Read and execute the workflow at `.agent/workflows/picks-review.md` — Morning re… |
| `/roth-content` | 199 | Read and execute the workflow at `.agent/workflows/roth-content.md` — Long-form … |
| `/roth-ghostwrite` | 196 | Read and execute the workflow at `.agent/workflows/roth-ghostwrite.md` — Premium… |
| `/design-digital-product-offer` | 194 | Read and execute the workflow at `.agent/workflows/design-digital-product-offer.… |
| `/research-landscape` | 191 | Read and execute the workflow at `.agent/workflows/research-landscape.md` — Univ… |
| `/roth-visual-prose` | 191 | Read and execute the workflow at `.agent/workflows/roth-visual-prose.md` — Visua… |
| `/ship` | 191 | Read and execute the workflow at `.agent/workflows/ship.md` — Quick Content Spri… |
| `/roth-social` | 187 | Read and execute the workflow at `.agent/workflows/roth-social.md` — Social medi… |
| `/domain-verifiability-map` | 185 | Read and execute the workflow at `.agent/workflows/domain-verifiability-map.md` … |
| `/evolution-sprint` | 184 | Read and execute the workflow at `.agent/workflows/evolution-sprint.md` — Backgr… |
| `/roth-email` | 184 | Read and execute the workflow at `.agent/workflows/roth-email.md` — Cinematic em… |
| `/connelly-detail` | 183 | Read and execute the workflow at `.agent/workflows/connelly-detail.md` — Deploy … |
| `/connelly-conflict` | 182 | Read and execute the workflow at `.agent/workflows/connelly-conflict.md` — Run t… |

## Notes on Methodology

- Token counts use the 4-chars-per-token approximation (accurate within ~5% for English markdown).
- Each `.claude/commands/X.md` file is a single-line delegator: `Read and execute the workflow at .agent/workflows/X.md — <desc>`.
- The system reminder displays each entry as `- <slug>: <content>` truncated at ~100 chars with `…`. We use a 100-char cap for the realistic injection cost.
- Files in `.agent/workflows/` are workflow content. They load on invocation, not every turn. Zero per-turn cost. The historical '524 workflows' count is real but only ~199 of those have a `.claude/commands/` registration.
- This report is regenerated after each optimization step to track progress losslessly.
