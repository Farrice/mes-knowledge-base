# Mark Kashef (Agent Orchestration) — Genius Context

> Load before executing any workflow. Full extraction intelligence.

## Core Operating System

Kashef treats multi-agent orchestration as intentional cognitive division of labor — splitting tasks across specialized agents with explicit communication protocols, forced divergence, and human checkpoints. The core insight: a single LLM attempting multiple cognitive roles simultaneously produces shallow output across all of them; dedicated agents with pure context windows produce deep output in each.

---

## Genius Patterns (Compressed)

### GP1: The Directed Assembly Line (Sequential Handoff)
Break massive tasks into distinct agent roles (Researcher → Slide Writer → Designer). Program the prompt to refuse advancement until the previous actor passes the payload. This prevents context dilution — each agent focuses its entire context window on one cognitive function.

### GP2: The Forced Consensus Protocol (Parallel Synthesis)
Spawn 3-5 parallel agents on mutually exclusive tasks with a mandate to share top findings before writing. A Synthesis Lead normalizes and aggregates. The orchestrator acts as arbiter, reassigning angles if agents pick the same data point. Solves the AI "yes-man" problem through structural friction.

### GP3: The Human Tollbooth
Insert explicit halts: `require plan approval from the user before proceeding to the final build stage`. Correcting a bad outline takes seconds; correcting a fully built artifact takes thousands of tokens. Protects against compounding errors in long-running processes.

### GP4: The Hybrid Grunt-to-Architect Pipeline
Use a fast sub-agent to read, summarize, and compress source material. Feed condensed summary to the Agent Team. Avoids 5 premium agents all individually reading the same material, wasting context window capacity.

---

## Hidden Knowledge

| # | Principle | Deploy |
|---|-----------|--------|
| HK1 | Must explicitly say "create an agent team" or "spawn an agent team" — "spawn agents" defaults to sub-agents lacking inter-agent communication | Any multi-agent invocation |
| HK2 | 3-to-5 Rule — team of 3-5 agents is the sweet spot; 8+ agents plummets ROI through over-engineering and token burn | Sizing any agent team |
| HK3 | The Omniscient Observer — the orchestrator takes 3rd-person perspective and independently intervenes if it detects overlap, re-assigning topics to agents | Building prompts that trust the arbiter |

---

## Signature Moves

1. **Explicit Team Instantiation** — Always starts with "create an agent team" to ensure inter-agent communication protocols are active, not siloed sub-agents.
2. **Strategic Tollbooth Insertion** — Inserts `require plan approval` at critical junctures to prevent compounding errors and token waste on misaligned paths.
3. **Forced Perspective Divergence** — Programs parallel agents with mandates to share findings and wait for group submission to prevent homogeneous outputs.
4. **Context Compression with Grunts** — Deploys cheap sub-agents to pre-process large datasets before feeding condensed summaries to premium agent teams.
5. **3-to-5 Team Sizing Rule** — Limits agent teams to 3-5 members, resisting the urge to add more, optimizing for efficiency and cost.

---

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|-----------|----------------|----------|-------------|
| Role Specialization | Single LLM handles multiple roles with context dilution | Agents have distinct roles but some overlap | Each agent has pure context window focused on one cognitive function with zero role bleed |
| Sequential Integrity | Tasks run in parallel when they should be sequential | Most dependencies respected but some premature advancement | Strict handoff protocol — no agent advances until payload received from predecessor |
| Divergence Quality | Parallel agents produce complementary/agreeable outputs | Some genuine divergence with mild structural friction | Mandated conflict produces genuinely distinct perspectives; omniscient observer intervenes on overlap |
| Human Checkpoint Placement | No human checkpoints in multi-step workflows | Checkpoints exist but at suboptimal positions | Tollbooths placed at maximum-leverage points (after outline, before expensive build phases) |
| Token Efficiency | Premium agents all read same source material | Some compression but still redundant context loading | Grunt agents compress; premium agents receive distilled summaries; 3-5 team size enforced |
