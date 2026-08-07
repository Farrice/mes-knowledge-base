# Context Optimization Sprint

## Objective
Reduce token overhead by 40-60% without degrading system depth, nuance, or output quality.

## Tasks

### Phase 1: Immediate Wins
- [x] Merge AGENTS.md + GEMINI.md — deduplicate, preserve all unique instructions
- [x] Backup originals before any modification
- [x] Validate merged file preserves every unique rule

### Phase 2: Workflow Consolidation
- [x] Audit all 524 workflows for duplicates and near-duplicates
- [x] Identify consolidation candidates — found 4 exact duplicate pairs
- [x] Build consolidation script (`execution/workflow_consolidator.py`)
- [x] Execute consolidation: 4 pairs merged (deprecated → redirect stubs)
  - `competitor-content-spy` → `/competitor-intel`
  - `design-offer` → `/design-digital-product-offer`
  - `swarm-research` → `/research-swarm`
  - `content-series` → `/content-series-plan`
- [x] Backups saved to `.tmp/consolidated_backups/`

### Phase 3: Genius Compression Sprint
- [x] Identify the 7 biggest genius files (35-50K chars)
- [x] Compress each below 15K chars using pattern extraction
- [x] Verify compressed files preserve all expert-specific insights

### Phase 4: Loading Protocol Enhancement
- [x] Split hot-path directives into section-specific files
  - `directives/qa/anti_patterns.md` (1.2KB vs 13.7KB full) — 91% reduction
  - `directives/qa/mandates.md` (1.2KB vs 13.7KB full) — 91% reduction
- [x] Build workflow router script (`execution/workflow_router.py`) — 19 domains, keyword search
- [x] Update GEMINI.md with modular directive references + context budget rules
- [x] Enhance session-state.md usage (protocol documented, GEMINI.md references it)

## Results

| Optimization | Before | After | Savings |
|---|---|---|---|
| System instructions (AGENTS+GEMINI) | ~2,100 tokens | ~1,800 tokens | ~300 tokens/conversation |
| Workflow listing (per conversation) | ~13,500 tokens | 0 (router replaces) | ~13,500 tokens/conversation |
| QA directive (per load) | ~3,425 tokens | ~308 tokens | ~3,117 tokens/load |
| Genius files (Tier 2 loads) | 35-50K chars each | <15K chars each | ~60% per load |
| Duplicate workflows eliminated | 4 pairs | Redirect stubs | Cleaner routing |

**Estimated total per-conversation savings: ~17,000+ tokens static overhead**

### Phase 5: Expert Auto-Routing
- [x] Build `execution/expert_router.py` — 106 experts, 15 domains, 26 compounds
- [x] 3-tier signal matching: exact substring > bigram stem overlap > fractional word
- [x] Tightened compound matching (60%+ trigger coverage)
- [x] Enriched mindset expert signals (Dr. K, Pressfield) for creative block routing
- [x] Updated GEMINI.md Step 3 to mandate `expert_router.py` for all routing
- [x] Verified: correct routing for sales pages, creative blocks, newsletters, identity
- [x] Committed and pushed

### Phase 6: Remaining Hygiene & Hardening
- [x] Reduce noise in positions 3-5 of routing results — raised min score to 2.0, lowered `use` weight to 0.5
- [x] Tier 0 Expert Cards: `directives/tier0-cards.md` — 8 most-used experts (Cardinal Mason, Lara Acosta, Pressfield, Oren, Dr. K, Shaan Puri, Kallaway, Harry Dry)
- [x] `.tmp/` cleanup — purged 2MB of stale backups (14+ days), down from 2.7MB to 624KB
- [x] Committed and pushed all changes

## Rules
- **NO deletion** of any knowledge, methodology, or expert insight ✅
- **Backup everything** before modifying ✅
- **Test after each phase** — verify system still operates correctly ✅
