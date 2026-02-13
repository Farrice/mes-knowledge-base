# Perplexity API Usage Policy

> **Monthly Budget Limit: $10**
> This directive applies to ALL agents, workflows, and research tasks.

## Purpose

Perplexity provides higher-quality, citation-backed research than basic web search. It should be the **primary tool for market intelligence and deep research**. However, API costs must be managed carefully.

## Usage Guidelines

### When to Use Perplexity (PREFERRED)
- Market intelligence research
- Competitor analysis
- Deep research tasks (`/research-topic`, `/generate-brief`, `/spy-market`)
- Fact-checking with citations needed
- Any research where accuracy and sources matter

### When to Use Basic Web Search (FALLBACK)
- Quick factual lookups (dates, simple facts)
- General browsing/exploration
- When Perplexity budget is exhausted
- Non-critical background context

## Cost Tracking

| Metric | Value |
|--------|-------|
| **Monthly Budget** | $10.00 |
| **Est. Queries Available** | ~300-500 (standard), ~100-200 (deep research) |
| **Reset Date** | 1st of each month |

### Tracking File
Usage is tracked in: `/Users/farricecain/Google Antigravity/.agent/perplexity-usage.json`

## Agent/Workflow Rules

1. **Before using Perplexity**, check current usage against limit
2. **Batch queries** when possible—combine related questions into single requests
3. **Use Sonar (standard)** for most queries, reserve Sonar Pro/Deep Research for critical tasks
4. **Log each query** to the usage tracker
5. **If budget is exhausted**, notify user and fall back to basic web search

## Swarm/Multi-Agent Protocol

When spawning sub-agents or running swarms:
- **Do NOT give unrestricted Perplexity access**
- Allocate a per-task query budget (suggest: 5-10 queries max per swarm task)
- Central orchestrator should track cumulative usage

## Override

User can adjust the monthly limit by updating this file or verbally authorizing a temporary increase.

---

*Last updated: 2026-02-05*
