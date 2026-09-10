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
| **1** | **Codex-native Deep Research** (`/deep-research-os --mode auto|codex-native`) | $0 provider API spend | Primary: adaptive questions, native web search/page reads, claim ledger, two gap rounds, counterevidence, and citation verification. |
| 2 | Native ChatGPT/Gemini subscription export + `benchmark-import` | $0 incremental API cost | Use when the consumer Deep Research UI is preferable; import preserves citations and runs the Research OS audit. |
| 3 | Gemini Deep Research standard API (`--mode gemini`) | Typically ~$1-$3; API billing separate | Explicit calibration challenger only, with one call, no retry, and a machine-verified provider ceiling. |
| 4 | Tavily Search/Extract | Account-dependent | Bounded source-recovery leg only after its zero-dollar boundary is verified. |
| 5 | Other paid research providers | Provider-dependent | Explicit escalation only; never an automatic fallback. |

*Tavily free tier: 1,000 calls/month.

### Speed-first (Quick fact checks, single-claim verification)

| Priority | Tool | Cost | When to Use |
|----------|------|------|-------------|
| 1 | `search_web` | Free | Always first for quick checks. 1-3 calls. |
| 2 | `perplexity_ask` (Sonar MCP) | ~$0.01 | Single fact-check with citation, quick synthesis of a narrow question. |
| 3 | Tavily MCP | Free | Structured alternative to Perplexity ask. |

**Rule**: Standard and Deep research default to Codex-native. Provider research is never activated by generic routing and never silently falls through to another paid provider.

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
- **Tools**: `/deep-research-os` Codex-native loop; provider challengers or subscription imports only when explicitly selected
- **Cost**: $0 provider API spend by default; any provider escalation receives its own receipt and fail-closed cap
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

For any research deeper than Quick, use the decompose-gather-gap-close-verify-synthesize pattern. Parallel workers are optional and still require explicit authorization:

1. **Decompose**: Break the question into 4-6 sub-questions using `deep_research_engine.py --decompose-only`
2. **Gather**: Each sub-question gets its own research track with native web search + full-page reads, never snippet-only. Inaccessible sources are logged as evidence gaps rather than silently dropped.
3. **Gap-fill**: a completeness critic names material gaps; follow-up agents close them (rounds per the depth contract — standard 1, deep 2, max 3)
4. **Verify**: every load-bearing claim is reopened and checked against its cited page; a separate agent may do this only when explicitly authorized
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

- **Default allocation**: 100% Codex-native provider-free execution.
- **Provider calls**: explicit mode only; no background accelerator and no automatic fallback.
- **$10 bakeoff**: `$8` application authorization ceiling plus `$2` reporting-lag reserve; unknown or unbounded provider cost means do not run.
- **Gemini bakeoff**: one standard interaction maximum, no Max and no paid retry.
- **Subscription exports**: record `incremental API cost: $0`; do not call the subscription universally free.

---

## Quality Gate

Every Standard and Deep research output is validated by `execution/research_quality_gate.py`:

- Source count meets depth minimum
- 80%+ of data claims have source URLs
- Contrarian perspectives present (no echo chamber)
- Time-sensitive data from 2024+
- No unsourced superlatives or absolutes

**Gate failure**: Fix specific issues identified, then re-validate.
