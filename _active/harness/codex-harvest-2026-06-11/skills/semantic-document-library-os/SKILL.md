---
name: "Semantic Document Library OS"
description: "Agent-readable semantic libraries for work primitives"
expert: Semantic Document Library
domain: AI/Automation - semantic work primitives, agent-readable knowledge systems, document architecture, client productization
version: 1.2
format: completion-engine
workflows: 6
source: "Nate B. Jones - The Work Primitive: What Every AI Product Leader Gets Wrong (YouTube, 2026-05) + existing Nate B. Jones Antigravity skills"
---

# Semantic Document Library OS

Build knowledge libraries that agents can execute from, not merely read. This skill turns business processes, workflows, SOPs, product specs, and strategy knowledge into semantic work primitives: described, permissioned, reviewable, reversible where possible, and validated by task-specific quality tests.

## Core Capability

Most documents assume a human supplies the missing meaning. A semantic document library makes that meaning explicit so an agent knows what work is being done, what the action means, who owns it, what can go wrong, what authority is required, and how the outcome should be checked.

This layer sits beside `SKILL.md`, workflows, and agent files. It does not replace them. It gives agents a richer operating substrate for non-code knowledge work.

## What This Skill Produces

| Workflow | Output |
|---|---|
| Semantic Document Audit | Scored audit of existing docs for agent usability, authority clarity, validation strength, and execution risk |
| Semantic Document Generator | One agent-executable semantic document from a transcript, SOP, article, workflow, or messy source |
| Semantic Document Library Builder | Full semantic library architecture for a business, agent, product, or knowledge domain |
| Semantic Document Validator | Execution tests that prove whether an agent can perform the task from the document alone |
| Semantic Document Productizer | Client-facing offer, sales angle, delivery workflow, audit checklist, and first deliverables |
| Steering Compass | Operator Coach steering prompts for kickoff, midpoint, and closeout so the user can move faster without knowing every command |

## When to Deploy

- A workflow works only when the human keeps explaining unstated context.
- An agent can access tools but does not understand what the action means.
- A business has docs, SOPs, or references that are human-readable but not agent-operable.
- A client wants "AI readiness" but does not have agent-readable operating knowledge.
- A system needs a step above generic markdown: source-of-truth documents that encode permissions, failure modes, examples, tests, and maintenance.

## Stacking Guide

- **Nate B. Jones Context Engineering**: use for retrieval, memory, and context-load architecture.
- **Nate B. Jones Intent Engineering**: use for hidden intent, invisible guardrails, and disambiguation triggers.
- **Nate B. Jones Trust Architecture**: use for permissions, approval gates, and high-consequence actions.
- **Nate B. Jones Orchestration Intelligence**: use for multi-agent work graphs and validation loops.
- **Nate B. Jones Agent Deployment Strategy**: use for rollout, containment, progressive delegation, and client implementation.
- **Liam Mley AI Brain Builder**: use when the semantic library becomes a full business context layer.
- **Rachel Woods Playbook OS**: use when the semantic docs become SOPs, delegation playbooks, and team operating systems.

## Required Load Order

1. `genius.md`
2. `references/semantic-document-schema.md`
3. `semantic_libraries/antigravity/primitives/high-floor-operator-os.md` for operating depth decisions
4. The specific workflow file
5. Optional: `references/productized-service-blueprint.md` for client delivery

## Core Rule

Do not stop at a clean article or prompt. A semantic document is complete only when an agent can use it to decide, act, check, and know when not to act.

## High-Floor Rule

Default to Standard depth unless the task is clearly Light. Use Deep for revenue-critical, client-facing, system-changing, ambiguous, or best/world-class/savant-level work. True Codex subagents require explicit delegated/parallel agent request and a briefing packet.
