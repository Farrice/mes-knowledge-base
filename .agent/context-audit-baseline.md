# Context Injection Baseline Audit

> Measured: 2026-04-11 06:18:17 UTC
> Branch: context-optimization
> Script: `execution/measure_injection.py`

## Summary

| Source | Files | Chars | Est. Tokens |
|---|---|---|---|
| `.agent/workflows/` (top-level, auto-injected) | 524 | 37,862 | ~9,465 |
| `.agent/workflows/_library/` (deferred) | 0 | 0 | ~0 |
| `CLAUDE.md` | 1 | 14,911 | ~3,727 |
| `MEMORY.md` | 1 | 17,556 | ~4,389 |
| **Total fixed injection per turn** | | **70,329** | **~17,582** |

Top-level workflow scan: 524 `.md` files, 517 with a `description:` frontmatter field.

## Top 20 Heaviest Top-Level Workflows (by injection line length)

| Slug | Chars | Description |
|---|---|---|
| `haunt-story` | 276 | "Full narrative haunting architecture — write scenes, stories, and long-form pie… |
| `etymology-engine` | 241 | "Etymological depth deployment — take the 5 most important words in any piece, t… |
| `literary-edging` | 233 | "Strategic denial as standalone composition tool — map where readers predict you… |
| `haunt-social` | 229 | "Platform-specific haunting deployment. Residue-first (not hook-first) social me… |
| `daring-disobedience` | 221 | "Deploy Pattern 13 — the Skater's Mindset. Diagnose where you're self-censoring,… |
| `anti-homogenization-audit` | 218 | Audit any content against Ocean Vuong's 7-dimension anti-homogenization protocol… |
| `perception-lab` | 216 | "Language R&D laboratory — dedicated space for sentence experimentation without … |
| `haunt-audit` | 213 | "Post-completion quality gate scoring any finished piece on haunting potential. … |
| `haunt` | 198 | "The master Haunting Engine — take ANY piece of writing and elevate it from atte… |
| `haunt-copy` | 196 | "Marketing copy that doesn't just convert — it HAUNTS. The prospect can't stop t… |
| `species-test` | 192 | Run Ocean Vuong's Species Test on any content — "Has the species had this senten… |
| `estrangement-engine` | 185 | Transform mimetic writing into estranged prose using Ocean Vuong's behavioral di… |
| `parallax` | 173 | Produce Parallax Substack editions — trending research, briefing, drafting, prom… |
| `offer-stack` | 158 | Make any digital product offer irresistible with question-to-asset mapping, cong… |
| `diandra-first-50` | 120 | Audit + rewrite the first 50 words of any LinkedIn post for AI retrieval + human… |
| `diandra-save-architect` | 119 | Transform any content idea into a save-optimized format (1 save ≈ 5x reach of 1 … |
| `diandra-headline-engineer` | 116 | LinkedIn headline optimized for both AI retrieval matching AND human conversion |
| `taste-declare` | 116 | Declare your taste identity — what you want to say, why, and the cultural lineag… |
| `taste-stage` | 115 | Diagnose whether you are at good taste (follow rules) or great taste (break rule… |
| `belief-dissolution-engine` | 114 | Dissolve hardened audience beliefs using backward-dissolution proof sequences |

## Notes on Methodology

- Token counts use the 4-chars-per-token approximation (accurate within ~5% for English markdown).
- Only the `description:` frontmatter field is counted for workflows — full bodies only load on invocation.
- Injection format simulated: `- /<slug> (path): <description>` (matches observed system-reminder output).
- MEMORY.md is loaded by the auto-memory system on every turn; CLAUDE.md by the harness project-instructions loader.
- This report is regenerated after each Phase 1 batch to track lossless deferral progress.
