---
name: lance-yichao-context-engineering
version: 1.0.0
description: Context engineering methodology for production AI agents from Lance Martin (LangChain) and Yichao "Peak" Ji (Manus)
expert: Lance Martin & Yichao "Peak" Ji
domain: AI Agent Architecture, Context Engineering, Production Agent Systems
---

# Lance Martin & Yichao "Peak" Ji - Context Engineering

Production-grade context engineering methodology for building AI agents that maintain performance across hundreds of tool calls without degradation.

## Core Genius

Context engineering is the science and art of filling the context window with precisely the right information for the next step—combating the paradox that agents need extensive context (from tool calls) while model performance degrades as context grows. The solution isn't adding more sophisticated layers but finding the minimal effective architecture that lets model intelligence shine.

## Key Frameworks

### The Context Paradox
Agents need tool context, but performance drops as context grows. Solution: precise context management through offloading, reducing, retrieving, isolating, and caching.

### Three-Layer Action Space
1. **Function Calling** (10-20 atomic tools) - Schema-safe, cache-friendly
2. **Sandbox Utilities** - Extensible CLI tools via shell
3. **Packages/APIs** - Computation-heavy operations in code

### Compaction vs. Summarization
- **Compaction** (reversible): Replace full payload with unique identifier
- **Summarization** (irreversible): Reduce information content
- Always compact first, summarize only when compaction insufficient

### Pre-Rot Threshold
Model performance degrades at 128K-200K tokens (varies by model/task). Find YOUR threshold through evaluation, not documentation.

## Available Prompts

| # | Prompt | Purpose |
|---|--------|---------|
| 1 | context-architecture-design | Design context-aware agent architectures |
| 2 | compaction-system-generator | Create reversible compaction schemas |
| 3 | action-space-design | Structure capabilities across 3 layers |
| 4 | agent-as-tool-orchestrator | Wrap complex operations as sub-agents |
| 5 | summarization-schema-designer | Structured summarization with schema contracts |
| 6 | future-proof-validator | Test if architecture benefits from model upgrades |
| 7 | context-management-pipeline | Complete context reduction pipeline |
| 8 | mcp-integration-architecture | Model Context Protocol integration patterns |
| 9 | evaluation-system-designer | User ratings + automated tests + human eval |
| 10 | model-routing-strategy | Select models based on task characteristics |
| 11 | collective-feedback-mining | Extract system improvements from user corrections |
| 12 | agentic-map-reduce | Parallel sub-agent orchestration patterns |
| 13 | prerot-threshold-discovery | Find your model's actual working context limit |
| 14 | agent-security-guardrails | Multi-layer security architecture |
| 15 | kv-cache-optimization | Maximize cache efficiency and reduce costs |
| 16 | architecture-simplification | Remove complexity while improving performance |
| 17 | sandbox-environment-designer | Design agent execution environments |

## Quick Start

1. **Start with**: `13-prerot-threshold-discovery.md` to find your model's limits
2. **Then**: `01-context-architecture-design.md` for overall design
3. **Add**: `02-compaction-system-generator.md` for context management
4. **Scale with**: `04-agent-as-tool-orchestrator.md` for complex operations

## File Structure

```
lance-yichao-context-engineering/
├── SKILL.md (this file)
├── LICENSE.txt
└── references/
    ├── genius-patterns.md
    ├── hidden-knowledge.md
    └── prompts/
        ├── 01-context-architecture-design.md
        ├── 02-compaction-system-generator.md
        └── ... (17 prompts total)
```

## Deployment Triggers

- Building production AI agents
- Debugging agent performance degradation
- Designing multi-agent systems
- Optimizing context usage and costs
- Implementing agent security
