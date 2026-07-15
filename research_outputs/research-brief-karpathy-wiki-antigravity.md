# Research Brief: Karpathy LLM Wiki + Notion Integration for Antigravity

**Date**: 2026-04-13
**Angles Covered**: Karpathy Architecture, Notion AI Second Brain, Deployment Patterns
**Confidence**: High (all 3 agents, 30+ sources, primary + secondary)

---

## Executive Summary

Karpathy's LLM Wiki is a persistent, LLM-maintained markdown knowledge base that replaces RAG with "compile-time knowledge assembly" — the LLM reads sources once, synthesizes them into structured wiki pages, and maintains them incrementally via three operations (ingest, query, lint). This compounds knowledge across sessions instead of re-deriving it from scratch every time. Combined with autoresearch (constrained ratcheting loops: one file, one metric, 5-minute experiments, auto-revert on failure), it creates a self-improving system where humans curate sources and write directives while LLMs handle all mechanical bookkeeping.

Antigravity already implements a PRIMITIVE version of both patterns — the knowledge compiler is Karpathy-inspired, the evolution engine runs the autoresearch loop, and the file-based architecture is correct. But 5 critical loops are open:

1. **No query-writes-back** — queries retrieve knowledge but don't enrich the wiki
2. **No lint cycle** — only stale/overlap detection, no contradiction/orphan/cross-reference checks
3. **No living index** — manifest.json exists but isn't updated on every ingest
4. **No reflection pass** — no second-order synthesis articles from cross-source patterns
5. **Notion is dormant** — 2 entries in Knowledge Vault vs 217 files locally

Notion is NOT the right primary knowledge store (5K record wall, 3 req/sec throttle, proprietary format). But Notion 3.0's Custom Agents, Autofill, and MCP server can ACTIVATE the structured databases we already have — auto-triaging, auto-tagging, and serving as a collaboration/tracking layer while local markdown remains the knowledge backbone.

---

## Key Findings

### Karpathy LLM Wiki Architecture
- **Three layers**: Raw sources (immutable) → Wiki (LLM-maintained markdown) → Schema (CLAUDE.md)
- **Three operations**: Ingest (one source cascades 10-15 page updates), Query (synthesize + write back), Lint (contradictions, staleness, orphans)
- **Key infrastructure**: index.md (living catalog), log.md (append-only chronological record)
- **Autoresearch complement**: 700 experiments in 48 hours, 20 improvements, 11% speedup. Binary keep/discard ratchet via git. program.md = natural-language directive.
- **Critical quote**: "The LLM is rediscovering knowledge from scratch on every question. There's no accumulation." The wiki fixes this.

### Notion as AI Platform (2026)
- **Notion 3.0 agents**: Run autonomously for 20 minutes, Custom Agents trigger on schedules/events
- **Autofill**: Databases self-maintain with auto-generated summaries, tags, action items
- **Official MCP server**: `mcp.notion.com/mcp` — OAuth 2.1, LLM-optimized, production-ready
- **Scale limits**: 5K record perf wall, 10K row cap, 3 req/sec API throttle
- **Verdict**: Hybrid is optimal. Local markdown for knowledge. Notion for structured tracking + collaboration.
- **4-layer memory pattern**: Short-term (session), Episodic (performance log), Semantic (knowledge vault), Procedural (directives)

### Deployment Patterns
- **Zero infrastructure**: Obsidian + Claude Code sharing a directory. No server needed at our scale.
- **Reflection pass**: Second-order knowledge articles from cross-source patterns become "the most useful things in the wiki"
- **Wiki vs RAG**: Compile-time vs query-time. 95% token reduction at small scale. Scale ceiling ~200 pages.
- **Results**: 61% reduction in knowledge management overhead, 85% improvement in findability
- **Failure modes**: Model drift (rewrite instead of update), structural decay, stub explosion, scale wall
- **Schema document (CLAUDE.md) is highest leverage** — it's the institutional knowledge about how to maintain institutional knowledge

---

## Cross-Cutting Insights

1. **We're 60% there.** The architecture is correct (file-based, directive-driven, tiered loading). The missing piece is the COMPOUNDING LOOP — knowledge goes in but doesn't come back enriched.

2. **Notion's role is activator, not store.** Don't migrate 217 files to Notion. Instead, leverage Custom Agents to auto-triage Performance Log, Autofill to auto-tag Content Pipeline, and MCP server for bidirectional access.

3. **The reflection pass is the highest-ROI new feature.** Cross-source synthesis articles that identify patterns, contradictions, and connections nobody manually made. This is where the 10x knowledge compounding lives.

4. **Evolution engine needs volume.** 6 KEPT cycles vs Karpathy's 700 experiments. The ratchet works — it just needs to run 100x more often with harder constraints (auto-revert, single file, binary decisions).

5. **Scale wall is real but manageable.** 217 files / 1.7M words exceeds flat-index viability (~200 pages). Per-domain index files + search tooling (qmd-style BM25/vector hybrid) solves this without infrastructure.

---

## Gap Analysis: Current State vs Karpathy Wiki

| Karpathy Component | Antigravity Equivalent | Status | Gap |
|---|---|---|---|
| Raw sources (immutable) | `extractions/` | Exists | None — architecture correct |
| Wiki pages (LLM-maintained) | `knowledge/` | Partial | No cascade updates, no write-back |
| Schema (CLAUDE.md) | `CLAUDE.md` | Exists | Already serves this role |
| index.md (living catalog) | `knowledge/compiled/manifest.json` | Partial | Not updated on every ingest |
| log.md (chronological record) | `.agent/session-state.md` | Partial | Not a unified knowledge log |
| Ingest (cascade 10-15 pages) | `/extract` workflow | Partial | No cascade across existing pages |
| Query (write-back) | `/knowledge-search` | Missing | Retrieves but doesn't enrich |
| Lint (contradictions, orphans) | `knowledge_compiler.py stale/overlap` | Partial | No contradictions, no orphans |
| Reflection (second-order) | None | Missing | Highest-ROI new feature |
| Auto-revert ratchet | `/skill-evolution` | Partial | Manual keep/discard, no auto-revert |
| program.md | `evolution-direction.md` | Exists | Already modeled on this |
| Notion as agent platform | 6 databases, mostly dormant | Dormant | Custom Agents + Autofill not activated |
| MCP knowledge server | None | Missing | Would enable universal tool access |

---

## Sources
All URLs cited in individual research files:
- `.tmp/research-karpathy-wiki-architecture.md`
- `.tmp/research-notion-second-brain.md`
- `.tmp/research-llm-wiki-deployment.md`
