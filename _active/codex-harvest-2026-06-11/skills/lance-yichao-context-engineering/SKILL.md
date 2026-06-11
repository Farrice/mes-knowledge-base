---
name: "Lance Martin & Yichao "Peak" Ji - Context Engineering"
description: "Context engineering methodology for production AI agents from Lance Martin (LangChain) and Yichao "Peak" Ji (Manus)"
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
