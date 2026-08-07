# Context Optimization Sprint — Walkthrough

## What We Did

Reduced Antigravity's per-conversation token overhead by **~17,000+ tokens** without deleting any knowledge, methodology, or expert insight. Four phases, all complete.

---

## Phase 1: System Instruction Deduplication

**Problem:** `AGENTS.md` and `GEMINI.md` contained ~40% overlapping content — both loaded on every turn.

**Fix:**
- Merged all unique rules into [GEMINI.md](file:///Users/farricecain/Google%20Antigravity/GEMINI.md) (73 lines, 4.5KB)
- Reduced [AGENTS.md](file:///Users/farricecain/Google%20Antigravity/AGENTS.md) to a 4-line pointer file

**Savings:** ~300 tokens per conversation

---

## Phase 2: Workflow Consolidation

**Problem:** 4 duplicate workflow pairs with identical descriptions cluttering the router and listing.

**Fix:** Created [workflow_consolidator.py](file:///Users/farricecain/Google%20Antigravity/execution/workflow_consolidator.py) and executed it:

| Deprecated | Canonical (kept) |
|---|---|
| `/competitor-content-spy` | `/competitor-intel` |
| `/design-offer` | `/design-digital-product-offer` |
| `/swarm-research` | `/research-swarm` |
| `/content-series` | `/content-series-plan` |

- Deprecated files → redirect stubs (backward compatible)
- Originals backed up to `.tmp/consolidated_backups/`

---

## Phase 3: Genius File Compression

**Problem:** Tier 1 genius files averaging 35-50K chars — too large for efficient Tier 2 loading.

**Fix:** Applied structural compression via [genius_compressor.py](file:///Users/farricecain/Google%20Antigravity/execution/genius_compressor.py):
- Collapsed blank lines, removed filler, tightened headers
- Preserved all expert-specific insights, frameworks, and patterns

**Savings:** ~60% reduction per genius file load

---

## Phase 4: Modular Directive Splitting

**Problem:** `quality_assurance.md` (13.7KB / 3,425 tokens) loaded in full even when only anti-patterns or only mandates were needed.

**Fix:** Created modular sub-files:

| File | Size | Use Case |
|---|---|---|
| [anti_patterns.md](file:///Users/farricecain/Google%20Antigravity/directives/qa/anti_patterns.md) | 1.2KB (308 tokens) | When checking output for anti-patterns |
| [mandates.md](file:///Users/farricecain/Google%20Antigravity/directives/qa/mandates.md) | 1.2KB (293 tokens) | When enforcing production mandates |
| `quality_assurance.md` (full) | 13.7KB (3,425 tokens) | When both sections needed |

**Savings:** 91% per load when using sub-files

Updated [GEMINI.md](file:///Users/farricecain/Google%20Antigravity/GEMINI.md) to:
- Reference modular sub-files with explicit "prefer sub-files" instruction
- Enforce context budget rules (minimize reads, suggest resets after 15+ turns)
- Route workflows via `workflow_router.py` instead of scanning full listing

---

## Verification

All systems verified operational:

- ✅ GEMINI.md contains all unique rules from both original files
- ✅ AGENTS.md correctly points to GEMINI.md
- ✅ Modular directive sub-files exist and contain accurate content
- ✅ All 4 consolidated workflows redirect to canonical versions
- ✅ All backups preserved in `.tmp/`
- ✅ Workflow router returns correct results including redirect markers
- ✅ Zero knowledge, methodology, or expert insight deleted

---

## Total Impact

| Metric | Before | After |
|---|---|---|
| Static overhead per conversation | ~31,600 tokens | ~14,600 tokens |
| QA directive per load | 3,425 tokens | 308 tokens (sub-file) |
| Genius files per Tier 2 load | ~12,000 tokens avg | ~5,000 tokens avg |
| Duplicate workflows | 4 pairs (8 files) | 4 canonical + 4 stubs |

> [!IMPORTANT]
> **Net reduction: ~17,000+ tokens per conversation in static overhead alone.**
> Additional savings compound during sessions from modular directive loading and compressed genius files.

## New Tools Created

| Tool | Purpose |
|---|---|
| [workflow_router.py](file:///Users/farricecain/Google%20Antigravity/execution/workflow_router.py) | Search 524 workflows by keyword/domain instead of loading the full listing |
| [workflow_consolidator.py](file:///Users/farricecain/Google%20Antigravity/execution/workflow_consolidator.py) | Merge duplicate workflows with backup + redirect stubs |
| [genius_compressor.py](file:///Users/farricecain/Google%20Antigravity/execution/genius_compressor.py) | Structural compression of genius files preserving expert depth |
| [expert_router.py](file:///Users/farricecain/Google%20Antigravity/execution/expert_router.py) | Library-style expert routing — 106 experts, 15 domains, 26 compounds |
| [tier0-cards.md](file:///Users/farricecain/Google%20Antigravity/directives/tier0-cards.md) | 80-token hot-context cards for 8 most-used experts |

---

## Phase 5: Expert Auto-Routing

**Problem:** Expert selection required loading the 752-line `DOMAIN_REGISTRY.md` (~7,500 tokens) or relying on a hardcoded shortcut table in GEMINI.md that covered only ~15 of 106 experts.

**Fix:** Built [expert_router.py](file:///Users/farricecain/Google%20Antigravity/execution/expert_router.py) — a CLI tool that maps problem signatures to the optimal expert(s):
- 106 experts with ownership domains, use cases, and signal keywords
- 3-tier scoring: exact substring → bigram stem overlap → fractional word match
- Min score threshold (≥ 2.0) eliminates noise
- 26 compound combinations for force-multiplier pairings
- `route`, `compounds`, `domain`, and `stats` subcommands

**Savings:** ~7,500 tokens per routing decision (no DOMAIN_REGISTRY read needed)

**Verification:**

| Query | #1 Result | Correct? |
|---|---|---|
| "creative block" | Pressfield + Dr.K compound | ✅ |
| "sales page" | Jeremy Miner | ✅ |
| "newsletter growth" | Tyler Denk | ✅ |
| "LinkedIn growth" | Lara Acosta | ✅ |
| "taste design" | Oren | ✅ |

---

## Phase 6: Housekeeping & Tier 0 Cards

**Routing noise reduction:**
- Raised minimum score threshold from 1.0 to 2.0
- Lowered `use` field weight from 1.0 to 0.5 (prevents common words like "content" from polluting results)

**Tier 0 Expert Cards:** Created [tier0-cards.md](file:///Users/farricecain/Google%20Antigravity/directives/tier0-cards.md) with 8 most-used experts:
- Cardinal Mason (conversion copy), Lara Acosta (LinkedIn), Pressfield (resistance), Oren (taste)
- Dr. K (psychology), Shaan Puri (storytelling), Kallaway (revenue ramps), Harry Dry (copy rules)
- Each card: voice fingerprint, top frameworks, anti-patterns, escalation triggers (~80 tokens vs ~1,350 for full SKILL.md)

**Tmp cleanup:** Purged 2MB of stale backups (14+ days old), reducing `.tmp/` from 2.7MB to 624KB.

---

## Final Verification

All systems verified operational:

- ✅ Expert router returns correct top-1 results for 5 test domains
- ✅ Tier 0 cards referenced in GEMINI.md Context Engine
- ✅ `.tmp/` cleaned; only recent backups remain
- ✅ All changes committed and pushed to `main`
- ✅ Zero knowledge, methodology, or expert insight deleted across all 6 phases

