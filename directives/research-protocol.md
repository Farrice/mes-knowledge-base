# Research Protocol — Grounded Intelligence Standard

**Version**: 2.0 (rebuilt)
**Status**: Active

---

## Core Rule

**No research output may contain data claims, statistics, or factual assertions without source URLs.** Period.

If a finding cannot be sourced, it is labeled as "unverified inference" and treated accordingly.

---

## Research Tools — Priority Order

Two orderings: **depth-first** (for insight-grade research, the default for Standard and Deep tasks) and **speed-first** (for quick fact-checks and sanity checks).

### Depth-first (Standard + Deep research — DEFAULT)

| Priority | Tool | Cost | When to Use |
|----------|------|------|-------------|
| **1** | **Gemini Deep Research** (`deep_research_client.py`, via `/deep-research-gemini`) | $0 under Ultra; ~$0.25-1.50/query on prepaid | **Primary** for foundation research, strategic intelligence, any research feeding downstream decisions. 93.3% DeepSearchQA accuracy. Budget-gated via 3-layer defense. |
| 2 | Gemini Deep Research Max (same client, `--mode max`) | $0 under Ultra; ~$0.50-1.50/query | When maximum comprehensiveness matters over speed. |
| 3 | `perplexity_client.py` (sonar-deep-research) | ~$0.25/query | **Fallback only** — when Gemini Deep Research is rate-limited, errors, or budget-exhausted. Tag output as "Perplexity fallback." |
| 4 | Tavily MCP (`tavily_search`) | Free* | Structured search supplementation. Unlimited within plan. |
| 5 | `search_web` + `read_url_content` | Free | Supplementation when Deep Research results need URL-level verification. |

*Tavily free tier: 1,000 calls/month.

### Speed-first (Quick fact checks, single-claim verification)

| Priority | Tool | Cost | When to Use |
|----------|------|------|-------------|
| 1 | `search_web` | Free | Always first for quick checks. 1-3 calls. |
| 2 | `perplexity_ask` (Sonar MCP) | ~$0.01 | Single fact-check with citation, quick synthesis of a narrow question. |
| 3 | Tavily MCP | Free | Structured alternative to Perplexity ask. |

**Rule**: If the task is Standard or Deep depth, default to Gemini Deep Research. Do NOT start with Perplexity for foundation work — it has historically produced shallower synthesis that misses the insight layer.

---

## Depth Levels

> **SINGLE SOURCE OF TRUTH: `execution/research_depth.py`** (2026-07-26). The
> floors below are a human-readable mirror of that contract — if they ever
> disagree, the code wins and this file is stale. The contract also carries
> what this table historically omitted, which is how "deep" runs shipped as
> six snippets: **gap-fill rounds** (standard=1, deep=2, max=3), **full-page
> extracts per subtopic** (snippets count HALF toward the source floor), and
> **independent verification of ALL load-bearing claims** (cap 20; the finder
> never verifies its own claim). Any research artifact — including ad-hoc
> Workflow swarms, which previously bypassed every floor — is validated with
> `python3 execution/research_quality_gate.py validate <report> --depth <tier> --receipt`;
> a Research-type finalize without that PASSING receipt gets Factual Grounding
> capped at 6 by `chain_runner.py` (deterministic). Unvalidated research ships
> with a `⚠️ RECON-GRADE — not decision-grade` banner.

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
- **Tools**: Full deep-research workflow (see `.agent/workflows/deep-research.md`; the multi-wave engine is `.agent/workflows/deep-research-swarm.workflow.js`)
- **Cost**: $0 — Gemini Deep Research is Ultra-quota-covered (fire it as a background accelerator on every deep/max run via `research.py gemini-start`); Perplexity is DEAD, never propose paid credits
- **Time**: 15-40 minutes (2 gap-fill waves + independent verification — single-pass "deep" is a contradiction)
- **Source minimum**: 15 across 6+ domains, full-page reads (snippets count half)

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
2. **Research in parallel**: Each sub-question gets its own research track with `search_web` + `read_url_content` — full-page reads, never snippet-only. JS-rendered/login-gated primary sources route to the Playwright lane, never dropped silently.
3. **Gap-fill**: a completeness critic names material gaps; follow-up agents close them (rounds per the depth contract — standard 1, deep 2, max 3)
4. **Verify**: every load-bearing claim attacked by an agent that did NOT find it (refute-default; REFUTED claims dropped)
5. **Synthesize**: cross-reference findings across all tracks, flag contradictions
6. **Quality gate**: `research_quality_gate.py validate <report> --depth <tier> --receipt` — the receipt feeds `chain_runner.py finalize --depth-receipt`

Full protocol: `.agent/workflows/deep-research.md` (note: `swarm-research.md` is a superseded stub — do not cite it as the protocol)

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
