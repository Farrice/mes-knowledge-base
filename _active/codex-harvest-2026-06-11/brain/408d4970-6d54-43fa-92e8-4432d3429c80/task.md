# Research Layer Rebuild — Task Tracker

## Phase 1: Build Universal Research Engine
- [x] Audit all research-dependent workflows (30+ identified)
- [x] Research external MCP tools and GitHub repos for better alternatives
- [x] Write implementation plan
- [x] Build `execution/deep_research_engine.py` (Quick/Standard/Deep depths)
- [x] Test research engine at all 3 depth levels

## Phase 2: Upgrade MCP Tools
- [x] Evaluate MCP Option A (replace Perplexity MCP + add Tavily) vs Option B — chose A
- [x] Write setup guide: `directives/mcp-research-setup.md`
- [ ] User follows setup guide to install Perplexity Sonar + Tavily MCP servers (USER ACTION)
- [ ] Verify new MCP tools work correctly (BLOCKED ON USER)

## Phase 3: Rebuild Research-Dependent Workflows

### Core Infrastructure (NEW)
- [x] `execution/deep_research_engine.py` — universal research module
- [x] `execution/research_quality_gate.py` — 6-check quality validator
- [x] `.agent/workflows/swarm-research.md` — Manus/Kimi-style parallel research
- [x] `directives/research-protocol.md` — central research protocol
- [x] `directives/mcp-research-setup.md` — MCP setup guide

### Tier 1 — Core Research Workflows
- [x] `/deep-research` — fixed MCP refs, added tiered tools, quality gate
- [x] `/research-sprint` — increased research call volume, fixed tool refs, added quality gate
- [x] `/parallel-research` — wired to research engine, fixed tool refs, added quality gate
- [x] `/research-topic` — wired to engine, fixed tool refs, added quality gate
- [x] `/research-landscape` — wired to engine, fixed tool refs, added quality gate
- [x] `/grounding-pass` — wired claim verification to search_web + read_url_content

### Tier 2 — Workflows With Research Phases
- [x] `/council` — added tiered tool strategy for research grounding
- [x] `/roundtable` — added tiered tool strategy for research grounding
- [x] `/swarm` — added read_url_content + quality gate
- [x] `/parallel-swarm` — fixed WebSearch → search_web + read_url_content
- [x] `/generate-brief` — added read_url_content + quality gate + research engine
- [x] `/mini-brief` — added tiered tool strategy to Phase 1 research
- [x] `/icp-research`, `/icp-deep-dive` — upgraded VOC mining with tiered tools
- [x] `/competitor-intel` — added research phase with tiered tools
- [x] `/hunt-trends` — added read_url_content for deep reads
- [x] `/flywheel-ideas` — added read_url_content for deep reads
- [x] `/betting-edge` — fixed WebSearch → search_web + read_url_content

### Tier 3 — Light Research Dependencies
- [x] `/deep-research` — cleaned 4 residual WebSearch/WebFetch references
- [x] `/weekly-pulse` — fixed WebSearch → `search_web` in Agent 1 scanner
- [x] `/content-sprint` — fixed WebSearch → `search_web` in trending signals
- [x] `/authority-flywheel` — fixed WebSearch + Perplexity → tiered tool strategy
- [x] `/draft-proposal` — fixed WebFetch → `read_url_content`
- [x] `/atomize` — fixed WebFetch → `read_url_content`
- [x] `/watch-and-remix` — fixed 3x WebFetch → `read_url_content`
- [x] **Verification**: Zero `WebSearch`, `WebFetch`, `perplexity_research`, or `mcp__perplexity` references remain

## Phase 4: Research Quality Gate
- [x] Build `execution/research_quality_gate.py`
- [x] Integrate quality gate into `/deep-research` workflow
- [x] Test quality gate on old vs. new research outputs

## Phase 5: Bug Fixes (discovered during testing)
- [x] Fixed per-task cap in `perplexity_client.py` — cap was warn-only, now blocks pre-call
- [x] Fixed task context isolation in `deep_research_engine.py` — angle-specific contexts prevent cap collision
- [x] Raised research-engine cap from 10 → 20 queries per task context

## Verification
- [x] Run decompose-only test → 5 sub-questions, 15 queries, correct intent detection
- [x] Run Quick depth test → 30+ findings, 10 unique domains, real source URLs
- [x] Run Standard depth test → specific pricing data, 10 unique domains, 86% claim sourcing
- [x] Run quality gate on new output (Standard) → 70/100, ✅ PASS
- [x] Run quality gate on new output (Quick) → 60/100, ✅ PASS
- [x] Run quality gate on OLD output (Samuel Thompson) → 65/100, ❌ FAIL (0% claim sourcing!)
- [x] Verify Perplexity budget intact → $1.22 spent, $28.78 remaining
- [ ] Run `/deep-research` on test topic via workflow (REQUIRES MANUAL TEST)
- [ ] Run `/council` on strategic question via workflow (REQUIRES MANUAL TEST)
