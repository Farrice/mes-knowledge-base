# Research Layer Rebuild — Walkthrough

## What Was Done

The entire research infrastructure was rebuilt to fix a systemic grounding problem: 30+ workflows were referencing Perplexity MCP as if it performed deep research, but it only fires basic Sonar queries. The result was LLM-generated speculation disguised as research.

### New Infrastructure (4 files)

| File | Purpose |
|------|---------|
| [deep_research_engine.py](file:///Users/farricecain/Google%20Antigravity/execution/deep_research_engine.py) | Universal research module with Quick/Standard/Deep depth levels |
| [research_quality_gate.py](file:///Users/farricecain/Google%20Antigravity/execution/research_quality_gate.py) | 6-check quality validator for any research output |
| [research-protocol.md](file:///Users/farricecain/Google%20Antigravity/directives/research-protocol.md) | Central research protocol for all workflows |
| [mcp-research-setup.md](file:///Users/farricecain/Google%20Antigravity/directives/mcp-research-setup.md) | MCP setup guide for upgraded Perplexity + Tavily |

### 19 Workflows Upgraded

- **Tier 1** (6): `/deep-research`, `/research-sprint`, `/parallel-research`, `/research-topic`, `/research-landscape`, `/grounding-pass`
- **Tier 2** (8): `/council`, `/roundtable`, `/swarm`, `/parallel-swarm`, `/generate-brief`, `/mini-brief`, `/icp-research`, `/competitor-intel`, `/hunt-trends`, `/flywheel-ideas`, `/betting-edge`
- **Tier 3** (5): `/weekly-pulse`, `/content-sprint`, `/authority-flywheel`, `/draft-proposal`, `/atomize`, `/watch-and-remix`
- **Zero** residual `WebSearch`, `WebFetch`, `perplexity_research` references remain

### Bugs Found & Fixed

1. **Per-task cap was warn-only** → `perplexity_client.py` now raises `BudgetExhaustedError` BEFORE the API call
2. **All research queries shared one task context** → `deep_research_engine.py` now uses angle-specific contexts (`research-engine-market`, `research-engine-competitive`, etc.)

---

## Test Results

### Research Engine Depth Tests

| Test | Result | Key Data |
|------|--------|----------|
| Decompose-only | ✅ | 5 sub-questions, 15 search queries, correct market intent detection |
| Quick depth | ✅ | 30+ findings, 10 unique source domains (McKinsey, Technavio, etc.) |
| Standard depth | ✅ | Specific pricing data ($1-4K, $4-6K, $6-10K+), 10 unique domains, 86% claim sourcing |

### Quality Gate: Old vs New

| File | Score | Claim Sourcing | Verdict |
|------|-------|---------------|---------|
| **New** Standard output | 70/100 | **86%** | ✅ PASS |
| **New** Quick output | 60/100 | **85%** | ✅ PASS |
| **Old** Samuel Thompson | 65/100 | **0%** | ❌ FAIL |

> [!IMPORTANT]
> The old research file scored **0% claim sourcing** — every data claim was unsourced speculation. The quality gate correctly flagged this. New engine outputs show 85-86% sourced claims with real URLs.

### Budget Impact

- Queries used during testing: 16 (Quick: 4, Standard: ~12)
- Cost: **$0.32** for tests
- Total month spend: $1.22 of $30.00 budget (**$28.78 remaining**)

---

## Remaining Items (User-Dependent)

1. **MCP Install**: Follow [mcp-research-setup.md](file:///Users/farricecain/Google%20Antigravity/directives/mcp-research-setup.md) to upgrade Perplexity MCP + add Tavily (optional)
2. **Manual workflow test**: Run `/deep-research "AI consulting for solopreneurs"` and verify grounded output
3. **Manual workflow test**: Run `/council` on a strategic question and verify research grounding
