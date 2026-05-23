---
name: nate-b-jones-context-engineering
description: 'Architects memory and context systems for agentic systems using Nate B. Jones''s TurboQuant-informed methodology — PolarQuant + QJL compression, H2O/SnapKV eviction strategies, sovereign persistent memory, and self-decaying context. Treats the context window as a KV cache where every byte must earn its place. Use when the agent hits context-window limits or "lost in the middle" failures, token costs scale faster than value delivered, agents reload full context every conversation instead of persisting state, 50+ tool definitions create prompt bloat, or moving from static file loading to dynamic semantic retrieval. Trigger proactively whenever the user mentions "memory crisis", "context bloat", "agent forgets", or "compression". For production-deployment harness design (action-space, sandbox, KV-cache benchmarks) use lance-yichao-context-engineering; for the auto-improvement loop layer use nate-b-jones-auto-improvement-loops.'
expert: Nate B. Jones
domain: AI/Automation — Context & Memory Architecture
version: 1.0
format: completion-engine
workflows: 6
source: '"TurboQuant — Google''s Breakthrough That Changes Everything About AI Memory" (YouTube, 2026) + Parallel Swarm Research Synthesis'
---

# Nate B. Jones — Context Engineering

> Memory is a software problem, not a hardware problem. Compression moves at the speed of software — months. Hardware fabrication moves at the speed of physics — half a decade. Engineer your context. Don't wait for larger windows.

## Core Capability

Design, audit, and optimize how agentic systems manage memory and context. Treat context as an engineered resource — not a passive container. Apply compression principles from TurboQuant (PolarQuant + QJL), eviction strategies from H2O/SnapKV, and sovereign memory architecture to build systems that are token-efficient, persistent, and self-decaying. This skill treats the context window as a KV cache — every byte must earn its place.

## What This Skill Produces

| Workflow | Output |
|----------|--------|
| Context Bloat Diagnostic | Full audit with compression prescriptions for any agentic system |
| Context Compression Sprint | Deduplicated, restructured, distilled system reaching ≥30% token reduction |
| Sovereign Memory Architecture Blueprint | Complete persistent memory design with episodic/semantic/procedural tiers + decay |
| Tool Router Agent Blueprint | Dynamic tool selection architecture loading only task-relevant definitions |
| Semantic Context Retrieval System | Vector-based skill/genius chunk retrieval replacing static file loading |
| Memory Crisis Strategic Intelligence | Market/technology brief on AI memory optimization landscape |

## When to Deploy

- System hitting context window limits or showing "lost in the middle" failures
- Token costs scaling faster than value delivered
- Agents reloading full context every conversation instead of persisting state
- 50+ tool definitions creating prompt bloat
- Moving from static file loading to dynamic semantic retrieval
- Need strategic intelligence on memory optimization landscape for investment/architecture decisions

## Stacking Opportunities

- **+ Nate B. Jones (Orchestration Intelligence)**: Context engineering + DPVI = memory-efficient multi-agent systems with clean context per iteration
- **+ Nick Saraev (Agentic Workflows)**: Self-annealing + memory decay = self-healing context systems that improve without oversight
- **+ Nate B. Jones (Intent Engineering)**: Intent-driven context prioritization = load only what matters for the task's actual specification width
- **+ Nate B. Jones (Trust Architecture)**: Sovereign memory + zero-trust = memory systems with provenance, audit trails, and tamper resistance
- **+ Nate B. Jones (Agent Deployment Strategy)**: Deployment + context engineering = agents that start fast with minimal context bootstrapping

## Key Principles

1. **Software speed beats hardware speed** — Compress algorithmically before buying bigger windows
2. **Every token must earn its place** — Context is a KV cache; low-value tokens get evicted
3. **Own your memory** — Sovereign, portable, queryable stores you control
4. **Compress in stages** — Transform representation first, correct residuals second (Polarity-Quantization)
5. **Decay prevents rot** — Memory without expiry becomes bloat; frequency-weighted decay keeps context fresh
6. **Five vectors, not one silver bullet** — Attack context bloat from quantization, eviction, architecture, tiering, and attention simultaneously

## Load Order

1. Load `genius.md` (required — all frameworks + synthesis research)
2. Load specific workflow for task
3. Cross-reference `orchestration-intelligence/genius.md` for multi-agent context patterns
