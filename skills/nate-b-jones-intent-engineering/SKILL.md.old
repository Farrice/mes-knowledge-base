---
name: nate-b-jones-intent-engineering
description: "Design AI agents that reliably understand and execute user intent through explicit intent documentation, disambiguation protocols, and interpretation-execution separation"
---

# Nate B Jones Intent Engineering

> Intent is not in the text the way context is. Intent is latent—priorities, tradeoffs, what done looks like, what's risky. This is the central failure mode of agentic systems.

## Overview

Nate B Jones identified that the central failure mode of AI agents isn't hallucination, context, or tool calling—it's the **intent gap**. His breakthrough: separate interpretation from execution, treat intent as a first-class architectural object, and build disambiguation loops for high-stakes actions.

**Core Insight**: While everyone obsesses over context engineering, intent is *latent*—our priorities, what "done" looks like, what we'd regret if the agent guessed wrong.

## Core Concepts

| Concept | Definition |
|---------|------------|
| **Intent vs Context** | Context is IN the text; intent is BEHIND the text |
| **Invisible Guardrails** | Constraints humans assume but never state |
| **Reversibility Gradient** | Actions range from fully reversible to catastrophically permanent |
| **Answer-Shaped Text** | Outputs that LOOK correct but aren't validated against intent |

## Deployable Capabilities

| Prompt | Use When |
|--------|----------|
| [Intent Document Generator](references/prompts/intent-document-generator.md) | Creating explicit intent specifications for agents |
| [Disambiguation Protocol](references/prompts/disambiguation-protocol.md) | Designing when/how agents ask for clarification |
| [Guardrails Extractor](references/prompts/guardrails-extractor.md) | Surfacing unstated constraints |
| [Intent Gap Analyzer](references/prompts/intent-gap-analyzer.md) | Evaluating existing agents for intent failures |

## Key Principles

1. **Interpretation-Execution Separation**: Understand BEFORE doing—inspect agent's interpretation before tools fire
2. **Selective Disambiguation**: Ask when stakes are high, proceed when confident—not every breath
3. **Intent as First-Class Object**: Version and document intent separately from code
4. **Reversibility Mapping**: Higher intent confidence required for lower reversibility actions
5. **Production Pragmatism**: Ship reliable agents NOW while research catches up

## Quick Start

1. **Analyze one agent** for intent gaps (list assumptions, invisible guardrails)
2. **Create first Intent Document** (goals, failure conditions, tradeoffs, priorities)
3. **Add assumption-surfacing** to agent prompt
4. **Test with ambiguous inputs** (where real failures occur)

## Resources

- [Genius Patterns](references/genius-patterns.md) - 14 unconscious mastery behaviors
- [Hidden Knowledge](references/hidden-knowledge.md) - 4 tacit insights
- [Implementation Pathway](references/implementation.md) - 30-day mastery
