---
name: "Mark Kashef — Banana Squad Image Agent Team"
description: "AI-powered image generation via multi-agent orchestration using the PaperBanana framework + Gemini 3 Pro API"
version: "2.0"
format: "completion-engine"
workflows: 2
---

# Mark Kashef — Banana Squad Image Agent Team

A deployable Claude Code agent team ("Banana Squad") that generates professional-grade images through a 5-agent pipeline: Research → Prompt Architect → Generator → Critic → Lead. Built on the PaperBanana agentic framework and powered by the Gemini 3 Pro Image API.

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| banana | [Banana Squad System Deployment & Quality Tuning](workflows/banana-squad-system-deployment.md) | A fully configured multi-agent image generation environment with calibrated quality thresholds | Initializing the agentic pipeline in Claude Code and setting the performance benchmarks for the Critic agent |
| style | [Style-Driven Visual Asset Production](workflows/style-driven-visual-production.md) | A set of high-fidelity images or infographics matching a specific visual DNA | Recreating a specific aesthetic from reference images or producing editorial-grade data visualizations |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Legacy Prompts**: [references/_legacy-prompts/](references/_legacy-prompts/) — archived atomic prompts
