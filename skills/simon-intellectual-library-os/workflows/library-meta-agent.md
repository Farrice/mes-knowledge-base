---
description: "Deploy the meta-agent pattern — a prompt-engineering specialist, itself grounded in an agentic-design-patterns KB, that scaffolds new advisors/KBs/skills via plan-lock."
---

# Library Meta-Agent

The agent that builds agents. Never scaffold a specialist by hand: a meta-agent grounded in its own KB of agent-design patterns does it better, faster, and consistently.

## Pre-Flight Gate
- Load `genius.md` §Decision Framework #1-2.
- Eat-your-own-dogfood check: the meta-agent must ITSELF pass the grounding gate — it consults its design-patterns KB before proposing any build. A meta-agent without a KB is generic-with-a-process.

## Skill Acquisition
Read `genius.md` + `references/kb-schema.md`.

## Execution
1. **Build (or audit) the meta-agent's own KB**: agentic design patterns, prompt-engineering principles, instruction-writing standards, the 6-property schema itself, platform mechanics (what the host platform's agents can/can't do). Source candidates: the Agentic Design Patterns document, platform docs, this skill's references. Ingest via `/library-ingest`.
2. **Write the meta-agent instructions** (job-description form): mission = scaffold new specialists; mandatory KB-read gate; its working method = plan-lock protocol: (a) restate the goal, (b) propose KB design + instruction outline + 2 launch skills, (c) surface platform affordances ("there's a new-KB button/template — use it?"), (d) ask scoping questions (standalone vs integrated? boundaries with existing modes?), (e) BUILD ONLY AFTER LOCK.
3. **Bake in the standards**: every artifact it produces gets token-slimmed; every advisor it builds gets the grounding gate + refusal test; every KB follows the 6-property schema; it registers new advisors in the global instructions.
4. **Bake in teach-forward**: when the user corrects it mid-build, it updates its OWN instructions/KB before continuing.
5. **Live test**: have it scaffold a small specialist end-to-end; verify plan-lock happened, gate installed, refusal test run.

## Content Type Adaptations
| Platform | Adaptation |
|---|---|
| Notion | Meta-agent = instruction page + design-patterns DB; uses native buttons/templates for new KBs |
| Claude Code / this repo | The /extract pipeline IS a meta-agent — this workflow adds: grounding extractions in a design-patterns KB + plan-lock checkpoints |
| Claude Cowork | Meta-agent = skill + KB folder; scaffolds new KB folders per the parent CLAUDE.md |
| Client handoff | Ship the meta-agent WITH the system so the client can grow it without you |

## Output Requirements
Meta-agent instructions (slimmed) + its seeded KB + one scaffold-run transcript demonstrating plan-lock → build → gate → test. The meta-agent passes its own refusal test.

## Quality Gate
`genius.md` §Anti-Patterns: a meta-agent that builds without plan-lock, or whose products skip the grounding gate, fails. Rubric: Groundedness + Token Economy ≥7 on the meta-agent itself.
