---
name: lance-yichao-context-engineering
description: 'Designs production-grade context-engineering infrastructure for AI agents using Lance Martin (LangChain) and Yichao "Peak" Ji (Manus) methodologies — action-space layering, sandbox configurations, security guardrails, reversible compaction, structured summarization, KV-cache optimization, and pre-rot benchmarking. Use when designing a new agentic system from scratch, migrating a prototype to production, hitting performance degradation across long sessions, token costs scaling faster than value delivered, benchmarking agent reliability, selecting models per task, or simplifying a bloated harness. Trigger proactively whenever the user asks "why is my agent slower after 100 tool calls" or "how do I deploy this to production" — the Lance/Yichao surface is the production-deployment lane. For memory-crisis architecture, sovereign persistent memory, or TurboQuant compression theory, use nate-b-jones-context-engineering instead.'
version: "2.0"
format: "completion-engine"
workflows: 3
---

# Lance Martin & Yichao "Peak" Ji - Context Engineering

Production-grade context engineering methodology for building AI agents that maintain performance across hundreds of tool calls without degradation.

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| production | [Production Agent Infrastructure Blueprint](workflows/production-agent-infrastructure-blueprint.md) | A comprehensive architectural specification including action-space layers, sandbox configurations, and security guardrails. | You are designing a new agentic system from scratch or migrating a prototype to a production-grade environment. |
| context | [Context Management & Efficiency Engine](workflows/context-management-efficiency-engine.md) | A technical implementation plan for reversible compaction, structured summarization, and KV-cache optimization. | The agent is suffering from performance degradation due to long-running sessions or high token costs. |
| performance | [Performance Discovery & Optimization Protocol](workflows/performance-discovery-optimization-protocol.md) | An evaluation report detailing the pre-rot threshold, model routing logic, and a simplified architecture roadmap. | You need to benchmark agent reliability, select the right models for specific tasks, or simplify a bloated system. |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Legacy Prompts**: [references/_legacy-prompts/](references/_legacy-prompts/) — archived atomic prompts
