---
name: futurepedia-prompt-engineering
description: "The Expert Anchor System - 3-step framework for transforming generic AI outputs into expert-level, personalized execution through systematic knowledge extraction and context synthesis"
---

# Futurepedia Prompt Engineering

> Transform every AI conversation from generic average to expert-level through systematic framework extraction, context capture, and meta-prompt synthesis.

## Overview

Futurepedia reverse-engineered WHY AI gives generic advice (prediction engines find the most likely/average response) and created a 3-step system that forces AI to operate from expert frameworks + personalized context, eliminating the "looks impressive but useless" phenomenon.

**Core Insight**: The problem isn't your prompt words—it's that AI lacks expert grounding and personal context. This system fixes both.

## The 3-Step Expert Anchor System

| Step | Purpose | Core Action |
|------|---------|-------------|
| **1. Expert Anchor** | Ground AI in proven frameworks | Upload expert source → Extract operating system |
| **2. Context Extraction** | Capture all relevant details | AI interviews YOU → Compiles context file |
| **3. Meta-Prompt Synthesis** | Combine framework + context | AI writes optimal prompt using RICECO |

## Deployable Capabilities

| Prompt | Use When |
|--------|----------|
| [Expert Extractor](references/prompts/expert-extractor.md) | Transforming any source into deployable system |
| [Expert Discovery](references/prompts/expert-discovery.md) | Finding experts and frameworks in any domain |
| [Context Interview](references/prompts/context-interview.md) | Extracting personal context through questioning |
| [Context Compiler](references/prompts/context-compiler.md) | Turning interview answers into structured brief |
| [Meta-Prompt Synthesizer](references/prompts/meta-prompt-synthesizer.md) | Creating optimal execution prompts |

## Workflow Decision Tree

```
Want expert-level AI output?
│
├─ Step 1: Get Expert Anchor
│  ├─ Have source material? → Use Expert Extractor
│  └─ Need to find sources? → Use Expert Discovery
│
├─ Step 2: Get Personal Context
│  ├─ Have time for interview? → Use Context Interview
│  └─ Have notes to compile? → Use Context Compiler
│
└─ Step 3: Synthesize & Execute
   └─ Use Meta-Prompt Synthesizer → Deploy in clean session
```

## Quick Start

1. **Expert Anchor** (new chat): Upload expert source, extract framework
2. **Context Interview** (new chat): Let AI interview you about project
3. **Synthesize** (new chat): Combine anchor + context into master prompt
4. **Execute** (new chat): Run master prompt in clean session

**Key Rules:**
- Each step = separate chat (prevents momentum contamination)
- "Reconstruct, don't summarize" (preserves operational detail)
- Use XML tags to separate information blocks

## Resources

- [Genius Patterns](references/genius-patterns.md) - 7 unconscious mastery behaviors
- [Hidden Knowledge](references/hidden-knowledge.md) - 5 tacit insights
- [Implementation Pathway](references/implementation.md) - 30-day mastery
