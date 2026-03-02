---
name: "Mark Kashef: Claude Claw — Agent SDK Bridge Architecture"
description: "Build a personal AI assistant that bridges any messaging platform to your existing Claude Code infrastructure via Anthropic's Agent SDK subprocess pattern — zero dual-entry, full capability access from your phone"
version: "2.0"
format: "completion-engine"
workflows: 2
---

# Mark Kashef: Claude Claw — Agent SDK Bridge Architecture

Mark Kashef, after trying and exhausting the OpenClaw/NanoClaw ecosystem (and building his own derivatives), discovered that the simplest and most powerful personal assistant pattern is bridging directly into your existing Claude Code instance using Anthropic's Agent SDK subprocess spawning. Instead of building a separate AI brain, you create a thin messaging bridge to the one that already works.

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| bridge | [Claude Claw Bridge & Memory Blueprint](workflows/bridge-infrastructure-blueprint.md) | A comprehensive technical architecture document including the 8-stage pipeline design and a 3-layer SQLite memory schema | Designing a production-ready bridge from a messaging platform to Claude Code with persistent, intelligent memory. |
| interactive | [Self-Building Assistant Wizard](workflows/interactive-setup-wizard-generator.md) | A self-executing 'Mega-Prompt' that interviews users to automatically configure and deploy their custom AI assistant | You need to package complex documentation and build instructions into a single, interactive setup artifact for end-users. |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Legacy Prompts**: [references/_legacy-prompts/](references/_legacy-prompts/) — archived atomic prompts
