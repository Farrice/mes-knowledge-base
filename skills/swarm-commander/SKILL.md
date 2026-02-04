---
name: swarm-commander
description: "Orchestrate 10-50 expert agents in parallel-style execution with intelligent task decomposition, file-based coordination, and unified synthesis"
---

# Swarm Commander

> Transform from single-agent interaction to commanding an expert army. You become the CEO reviewing synthesized outputs while specialized agents execute in orchestrated swarms.

## Overview

Swarm Commander is the Tier 1.5 implementation of agent swarm orchestration—achieving 80-95% of true parallelism benefits using sophisticated prompt engineering, file-based coordination, and the Agent-as-Tool pattern. Built on three foundational methodologies:

| Source Expert | Pattern Borrowed |
|---------------|-----------------|
| **Boris** | Batch processing, work orders, multi-instance orchestration |
| **Lance & Yichao** | Agent-as-Tool isolation, file system coordination, context engineering |
| **Mark Kashef** | Intelligent agent selection, tension design, deliberation protocols |

**Core Insight**: True parallel execution isn't required when you architect *minimal-context work orders* and *file-based aggregation*. The speed gains come from eliminating redundant context loading, not from simultaneous API calls.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    YOUR REQUEST                                  │
└───────────────────────────┬─────────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│         PHASE 1: SWARM PLANNING                                  │
│  • Decompose task into parallelizable work units                │
│  • Select optimal agents from 44+ expert registry               │
│  • Map dependency graph (parallel vs sequential)                │
│  • Generate work orders with rigid output schemas               │
│  → Output: execution_plan.md + work_orders/                     │
└───────────────────────────┬─────────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│         PHASE 2: SWARM EXECUTION                                 │
│  • Each agent receives ONLY their work order (isolated context) │
│  • Agent embodies expert persona + methodology                  │
│  • Output written to structured file (not conversation)         │
│  • Parallel-compatible agents batched together                  │
│  → Output: agent_outputs/[agent_name].md                        │
└───────────────────────────┬─────────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│         PHASE 3: SWARM SYNTHESIS                                 │
│  • Fresh context reads ONLY file outputs                        │
│  • Identifies agreements, conflicts, and minority positions     │
│  • Applies quality verification from source experts             │
│  • Produces unified deliverable with provenance                 │
│  → Output: final_synthesis.md                                   │
└─────────────────────────────────────────────────────────────────┘
```

## Deployable Prompts

| Prompt | Use When |
|--------|----------|
| [Swarm Planning](references/prompts/swarm-planning.md) | Decompose any task into a multi-agent execution plan |
| [Agent Constellation](references/prompts/agent-constellation.md) | Select optimal experts based on task requirements |
| [Batch Execution](references/prompts/batch-execution.md) | Execute work orders with Agent-as-Tool isolation |
| [Swarm Synthesis](references/prompts/swarm-synthesis.md) | Aggregate outputs into unified deliverable |

## Key Principles

1. **Work Orders > Conversations**: Agents receive minimal context + schema, not full history
2. **Files > Messages**: Coordination happens through file system, not context passing
3. **Batching > Looping**: Conceptually parallel agents execute in optimized batches
4. **Schemas > Prose**: Rigid output formats enable fast synthesis
5. **Provenance > Anonymity**: Track which expert said what for accountability

## Swarm Sizes

| Size | Agents | Best For |
|------|--------|----------|
| **Squad** | 3-5 | Focused tasks, quick turnaround |
| **Team** | 6-12 | Comprehensive analysis, multi-perspective |
| **Platoon** | 13-25 | Large-scale research, complex projects |
| **Army** | 26-50 | Enterprise initiatives, exhaustive coverage |

## Quick Start

1. Describe your objective to Swarm Commander
2. Review the proposed agent constellation
3. Approve the execution plan
4. Receive synthesized output with full provenance
5. Iterate on specific agent outputs if needed

## Example Use Cases

- **Competitive Analysis**: 10 research agents analyze different competitors in parallel
- **Content Campaign**: Writers, SEO, design, psychology experts contribute simultaneously
- **Product Launch**: Market research, pricing, positioning, copy experts coordinate
- **Strategic Decision**: Multiple domain experts deliberate with structured synthesis

## Resources

- [Genius Patterns](references/genius-patterns.md) - Core patterns from Boris, Lance/Yichao, Kashef
- [Expert Registry](references/expert-registry.md) - Reference to available 44+ agents
