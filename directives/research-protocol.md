# Research Protocol — Grounded Intelligence Standard

**Version**: 2.0 (rebuilt)
**Status**: Active

---

## Core Rule

**No research output may contain data claims, statistics, or factual assertions without source URLs.** Period.

If a finding cannot be sourced, it is labeled as "unverified inference" and treated accordingly.

---

## Research Tools — Priority Order

Use tools in this order, starting with the cheapest:

| Priority | Tool | Cost | When to Use |
|----------|------|------|-------------|
| 1 | `search_web` | Free | Always. First line of research. 3-15 calls per topic. |
| 2 | `read_url_content` | Free | Read full pages from search results. 2-6 per topic. |
| 3 | `perplexity_ask` (sonar MCP) | ~$0.01 | Quick synthesis or when you need AI-structured summaries |
| 4 | Tavily MCP (`tavily_search`) | Free* | High-quality structured search. Unlimited within plan. |
| 5 | `perplexity_client.py` (sonar-deep-research) | ~$0.25 | Strategic intelligence only. Budget-gated. |

*Tavily free tier: 1,000 calls/month. Paid: unlimited.

---

## Depth Levels

### Quick (Sanity Check)
- **When**: Fact-checking a single claim, quick context gathering
- **Tools**: 3-5 `search_web` calls
- **Cost**: Free
- **Time**: 15-30 seconds
- **Source minimum**: 3

### Standard (Decision-Grade)
- **When**: Content research, council prep, competitor analysis, audience research
- **Tools**: 10-15 `search_web` + 3-5 `read_url_content`
- **Cost**: Free (add $0.04 if Perplexity synthesis used)
- **Time**: 2-5 minutes
- **Source minimum**: 8

### Deep (Strategic Intelligence)
- **When**: User explicitly requests deep research, strategy briefs, critical decisions
- **Tools**: Full swarm-research workflow (see `.agent/workflows/swarm-research.md`)
- **Cost**: $0.50-0.75 (if Perplexity premium used; $0 if free-tier only)
- **Time**: 8-15 minutes
- **Source minimum**: 15

---

## Research Triggers — When Research MUST Fire

Research is NOT optional in these scenarios:

| Trigger | Minimum Depth |
|---------|---------------|
| Any claim about market size, pricing, or revenue | Quick |
| Any claim about what "research shows" or "experts say" | Quick |
| Council/roundtable deliberation | Standard (BEFORE deliberation) |
| Strategy brief or analysis | Standard |
| User asks "research X for me" | Standard |
| `/deep-research` or `/generate-brief` | Deep |
| `/icp-research` or `/icp-deep-dive` | Deep |
| `/betting-edge` | Standard (stat-specific queries) |
| Any deliverable containing data assertions | Quick (verification pass) |

---

## Research MUST NOT Fire

Save resources — don't research when:

- User asks a pure opinion question ("what do you think?")
- Task is applying a known framework (e.g., StoryBrand structure)
- Content is creative writing (hooks, copy, scripts)
- User says "just do it" or "go ahead" on a plan already approved
- System/administrative tasks (file management, agent config)

---

## Swarm Research Protocol

For any research deeper than Quick, use the decompose-parallel-synthesize pattern:

1. **Decompose**: Break the question into 4-6 sub-questions using `deep_research_engine.py --decompose-only`
2. **Research in parallel**: Each sub-question gets its own research track with `search_web` + `read_url_content`
3. **Synthesize**: Cross-reference findings across all tracks, flag contradictions
4. **Quality gate**: Run `research_quality_gate.py validate` on the output

Full protocol: `.agent/workflows/swarm-research.md`

---

## Anti-Patterns (DO NOT)

1. **DO NOT** fire a single `perplexity_ask` call and call it "research"
2. **DO NOT** tell sub-agents to "research this topic" without specifying search queries
3. **DO NOT** present LLM training data as research findings
4. **DO NOT** use phrases like "research shows" without a linked source URL
5. **DO NOT** use `sonar-deep-research` for simple fact checks (use `search_web`)
6. **DO NOT** skip the quality gate on Standard or Deep research

---

## Budget Management

- **Monthly Perplexity budget**: $30 (tracked in `.agent/perplexity-usage.json`)
- **Deep research calls**: ~$0.25 each via `sonar-deep-research`
- **Target allocation**: 80% free tier (`search_web` + `read_url_content`), 20% premium
- **Budget check before premium calls**: Always run `perplexity_client.budget_remaining()`
- **When budget is low**: Fall back to free-tier-only using swarm research workflow

---

## Quality Gate

Every Standard and Deep research output is validated by `execution/research_quality_gate.py`:

- Source count meets depth minimum
- 80%+ of data claims have source URLs
- Contrarian perspectives present (no echo chamber)
- Time-sensitive data from 2024+
- No unsourced superlatives or absolutes

**Gate failure**: Fix specific issues identified, then re-validate.
