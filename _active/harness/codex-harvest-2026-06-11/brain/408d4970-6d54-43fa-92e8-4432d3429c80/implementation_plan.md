# Research Layer Rebuild — Implementation Plan

## The Problem

Our entire research infrastructure has been running on a shallow foundation. The Perplexity MCP tool (`perplexity_ask`) is a single-turn Sonar API call, but 30+ workflows reference it as if it performs deep research. The result: workflows that claim to produce "grounded research" are actually producing LLM-generated speculation dressed up as data.

> [!CAUTION]
> This affects ~30 workflows that depend on research as a foundation. Any past deliverable that relied on council/roundtable/swarm research phases — without explicit `search_web` or `read_url_content` calls — should be treated as potentially ungrounded.

## What Already Works (Don't Break These)

1. **`perplexity_client.py`** — Python client that DOES support `sonar-deep-research` model with budget tracking. This is real deep research capability, just underused.
2. **`search_web`** — Free web search tool with citations. Works well when used properly (as proven in Samuel Thompson research).
3. **`read_url_content`** — Free full-page content extraction. Essential for going beyond search snippets.
4. **`/deep-research` workflow** — Already correctly designed to use `sonar-deep-research` via Python client. Just needs the MCP tool references fixed and research call volume increased.

## What's Broken

| Layer | Issue | Impact |
|-------|-------|--------|
| **Perplexity MCP** | `perplexity_ask` only does basic Sonar, not deep research | Every workflow calling this gets shallow results |
| **Workflow design** | Most workflows fire 3-5 research queries and call it done | Insufficient depth for decision-grade intelligence |
| **Agent research phases** | Sub-agents told to "use WebSearch" get 1-3 generic searches | Agents produce LLM confabulation, not research |
| **No research chaining** | No standard for "search → read → follow-up → synthesize" | Each workflow reinvents (badly) the research process |

---

## Proposed Changes

### Phase 1: Build the Universal Research Engine

Create a single Python module that all workflows call for research. This replaces ad-hoc tool calls with a standardized, depth-controlled research pipeline.

#### [NEW] [deep_research_engine.py](file:///Users/farricecain/Google%20Antigravity/execution/deep_research_engine.py)

A new execution script that provides three research depth levels:

| Depth | What It Does | Tools Used | Est. Time | Cost |
|-------|-------------|-----------|-----------|------|
| **Quick** (sanity check) | 3-5 `search_web` calls, summarize | `search_web` | 15-30s | Free |
| **Standard** (decision-grade) | 10-15 `search_web` → follow best 3-5 with `read_url_content` → 1-2 `perplexity_ask` for synthesis | `search_web` + `read_url_content` + `perplexity_ask` | 1-3 min | ~$0.04 |
| **Deep** (strategic intelligence) | 2-3 `sonar-deep-research` via Python client + 10-15 `search_web` + 5-8 `read_url_content` | Full stack | 3-8 min | ~$0.50-0.75 |

**Key design principle**: Every finding MUST have a source URL. No source = not grounded = gets flagged.

Features:
- Query decomposition (splits one broad question into 5-10 specific queries)
- Source quality scoring (primary vs. secondary, recency, domain authority)
- Contradiction detection (flags when sources disagree)
- Citation tracking (every data point linked to its source URL)
- Budget-aware routing (auto-downgrades depth if Perplexity budget low)
- Output as structured markdown with provenance metadata

---

### Phase 2: Upgrade Research MCP Tools

#### Option A: Replace Perplexity MCP with a better one (RECOMMENDED)

There are several open-source Perplexity MCP servers on GitHub that expose `sonar-deep-research`:

| MCP Server | What It Does | Why Consider |
|-----------|-------------|--------------|
| **Perplexity Sonar MCP Server** (GitHub) | Exposes all Sonar models including `sonar-deep-research` via MCP | Drop-in replacement for our current weak Perplexity MCP |
| **pinkpixel-dev/deep-research-mcp** | Uses Tavily Search + Crawl for multi-step research | Free alternative, doesn't consume Perplexity budget |
| **GPT Researcher MCP** (`gptr-mcp`) | Full deep research agent as MCP server | Most capable but heaviest |

> [!IMPORTANT]
> **Recommendation**: Replace the current `perplexity-ask` MCP with a Perplexity Sonar MCP that supports `sonar-deep-research`. Additionally, ADD a Tavily-based MCP for free high-quality search that doesn't consume the Perplexity budget. This gives us two research MCP tools — one premium (Perplexity deep) and one workhorse (Tavily).

#### Option B: Keep current MCP, route everything through Python client

If changing MCP servers is too complex, we can route all deep research through `perplexity_client.py` and use the MCP only for quick checks.

---

### Phase 3: Rebuild All Research-Dependent Workflows

#### Tier 1 — Core Research Workflows (fix first)

These workflows ARE the research layer. Fix these and everything downstream improves.

| Workflow | Current Problem | Fix |
|----------|----------------|-----|
| `/deep-research` | References `mcp__perplexity-ask__perplexity_research` which doesn't exist | Route through `deep_research_engine.py` at "Deep" level |
| `/research-sprint` | Agents use "5 web searches" each = 15 shallow searches total | Bump to 15 searches per agent + 3 `read_url_content` each |
| `/parallel-research` | Same as research-sprint but without follow-up capability | Replace research phase with `deep_research_engine.py` at "Standard" level |
| `/research-topic` | Quick research that needs to actually be quick AND grounded | Use "Quick" depth from engine |
| `/research-landscape` | Domain mapping with no real research foundation | Use "Standard" or "Deep" depth |
| `/grounding-pass` | Validates claims against... what? Currently unclear | Wire to `search_web` + `read_url_content` for each claim |

#### Tier 2 — Workflows With Research Phases (fix second)

These workflows have research as one step among many. The research step needs upgrading.

| Workflow | Fix |
|----------|-----|
| `/council` | Add mandatory research phase BEFORE expert deliberation |
| `/roundtable` | Same — research first, interpret second |
| `/swarm` | Each swarm agent's research step → `deep_research_engine.py` |
| `/parallel-swarm` | Same |
| `/generate-brief` | Foundation research → "Deep" level engine |
| `/mini-brief` | Research phase → "Standard" level engine |
| `/icp-research` | VOC mining → chain `search_web` for Reddit/forums + `read_url_content` |
| `/icp-deep-dive` | Full pipeline → "Deep" level engine |
| `/competitor-intel` | Competitive research → "Standard" with specific competitor queries |
| `/hunt-trends` | Trend scanning → "Standard" with recency filter |
| `/flywheel-ideas` | Multi-expert ideation → "Standard" research per expert |
| `/betting-edge` | NBA data → specific targeted queries for player stats |

#### Tier 3 — Workflows With Light Research Dependencies (fix last)

These need a "Quick" research check but aren't primarily research workflows:

`/authority-flywheel`, `/comedy`, `/consumer-gap-diagnostic`, `/consumer-posture-profile`, `/content-orchestrate`, `/cold-outreach-gen`, `/outreach-and-follow-up-engine`, `/design-digital-product-offer`, `/design-offer`, `/listing-content`, `/placek-hooks`, `/daily-flywheel`

---

### Phase 4: Research Quality Gate

#### [NEW] [research_quality_gate.py](file:///Users/farricecain/Google%20Antigravity/execution/research_quality_gate.py)

A validation script that runs on any research output before it's used downstream:

- **Source count check**: Minimum 5 unique sources for Standard, 15 for Deep
- **Provenance audit**: Every claim must have a source URL
- **Recency check**: Flags data older than 12 months for time-sensitive topics
- **Echo chamber detection**: Flags when all sources say the same thing (may indicate shallow research)
- **Confidence scoring**: High (5+ corroborating sources), Medium (2-4), Low (1 or unverified)

---

## Verification Plan

### Automated Tests

Since this system doesn't have a test suite, we'll verify through structured integration tests:

1. **Research Engine Smoke Test**:
   ```bash
   cd "/Users/farricecain/Google Antigravity"
   python3 execution/deep_research_engine.py --depth quick "AI consulting market size 2025"
   # Verify: Output has 3+ sources with URLs, structured markdown, takes <30s
   ```

2. **Research Engine Standard Test**:
   ```bash
   python3 execution/deep_research_engine.py --depth standard "ghostwriting retainer pricing for coaches 2025"
   # Verify: Output has 8+ sources, includes read_url_content results, takes <3min
   ```

3. **Quality Gate Test**:
   ```bash
   python3 execution/research_quality_gate.py validate .tmp/test-research-output.md
   # Verify: Reports source count, provenance, recency, confidence scores
   ```

### Manual Verification

After building the engine and updating workflows:

1. **Run `/deep-research "AI consulting for solopreneurs"`** — verify the output contains real data with real URLs that you can click and verify
2. **Run `/council` on a strategic question** — verify the council's deliberation references actual research findings, not LLM-generated claims
3. **Compare old vs. new**: Take a past council/roundtable output and compare the data quality to a new run with the rebuilt research layer

> [!IMPORTANT]
> **User action required**: Farrice should pick 2-3 past deliverables that relied on council/roundtable research and spot-check the claims against reality. This tells us how much damage the weak research layer caused.

---

## Implementation Order

1. **Phase 1**: `deep_research_engine.py` (core module — everything else depends on this)
2. **Phase 2**: MCP tool evaluation and upgrade (needs your decision on Option A vs B)
3. **Phase 3 Tier 1**: Fix 6 core research workflows
4. **Phase 4**: `research_quality_gate.py`
5. **Phase 3 Tier 2**: Fix 12 workflows with research phases
6. **Phase 3 Tier 3**: Fix ~12 workflows with light research dependencies

**Estimated total effort**: Phase 1-2 can be done this session. Phase 3 Tier 1 + Phase 4 can be done this session. Tier 2 and 3 are follow-up sessions.

## User Review Required

> [!IMPORTANT]
> **Decision needed on MCP tools**: Do you want us to (A) replace the Perplexity MCP with a better one that supports `sonar-deep-research` + add Tavily MCP, or (B) keep current MCP and route all deep research through the Python client? Option A is more powerful but requires MCP configuration changes. Option B is simpler and faster to implement.

> [!WARNING]
> **Budget reality check**: Deep research via `sonar-deep-research` costs ~$0.25 per query. At 3 queries per deep research run, that's $0.75/run. With a $30/month budget, that's ~40 deep research runs per month. The free `search_web` + `read_url_content` chain gives you unlimited "Standard" depth research at zero cost — this is where the real volume should happen.
