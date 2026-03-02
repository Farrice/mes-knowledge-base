---
name: "Nate B Jones Intent Engineering"
description: "Design AI agents that reliably understand and execute user intent through explicit intent documentation, disambiguation protocols, and interpretation-execution separation"
version: "2.0"
format: "completion-engine"
workflows: 3
---

# Nate B Jones Intent Engineering

> Intent is not in the text the way context is. Intent is latent—priorities, tradeoffs, what done looks like, what's risky. This is the central failure mode of agentic systems.
Nate B Jones identified that the central failure mode of AI agents isn't hallucination, context, or tool calling—it's the **intent gap**. His breakthrough: separate interpretation from execution, treat intent as a first-class architectural object, and build disambiguation loops for high-stakes actions.
**Core Insight**: W

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| agent | [Agent Intent Diagnostic & Optimization](workflows/agent-intent-diagnostic-and-optimization.md) | Agent Reliability Audit & Remediation Plan | An existing AI agent is failing, behaving unpredictably, or producing 'answer-shaped' but incorrect results |
| intent | [Intent-Centric Agent Architecture](workflows/intent-centric-agent-architecture.md) | Comprehensive Agent Intent Specification | Designing a new agent from scratch for high-stakes tasks where hidden constraints and priorities are critical |
| operational | [Operational Safety & Communication Design](workflows/operational-safety-and-communication-design.md) | Agent Safety & Handover Protocol | Defining how an agent should handle uncertainty, ask for clarification, and transfer context between different stages of execution |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Legacy Prompts**: [references/_legacy-prompts/](references/_legacy-prompts/) — archived atomic prompts
