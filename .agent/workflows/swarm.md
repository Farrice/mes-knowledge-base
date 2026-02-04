---
description: Deploy an agent swarm to execute complex tasks with 10-50 experts working in orchestrated parallel
---

# /swarm Workflow

Orchestrate multiple expert agents to tackle complex objectives using the Swarm Commander skill.

// turbo-all

---

## Usage

```
/swarm [Your objective here]
/swarm --verbose [Your objective here]
```

### Flags

| Flag | Effect |
|------|--------|
| `--verbose` | Show each agent's FULL output inline before synthesis (learning mode) |
| (default) | Show only final synthesis with drill-down access to agent files |

## Steps

### 1. Read Swarm Commander Skill

Read the core methodology:
```
/Users/farricecain/Google Antigravity/skills/swarm-commander/SKILL.md
```

### 2. Read Genius Patterns

Internalize the 18 orchestration patterns:
```
/Users/farricecain/Google Antigravity/skills/swarm-commander/references/genius-patterns.md
```

### 3. Execute Phase 1: Swarm Planning

Read and apply:
```
/Users/farricecain/Google Antigravity/skills/swarm-commander/references/prompts/swarm-planning.md
```

Produce:
- `execution_plan.md` with dependency graph
- `work_orders/[agent_name].md` for each agent

### 4. Execute Phase 2: Agent Constellation

Read and apply:
```
/Users/farricecain/Google Antigravity/skills/swarm-commander/references/prompts/agent-constellation.md
```

Produce:
- `agent_constellation.md` with selection justification and tension map

**CHECKPOINT**: Present constellation to user for approval before execution.

### 5. Execute Phase 3: Batch Execution

Read and apply:
```
/Users/farricecain/Google Antigravity/skills/swarm-commander/references/prompts/batch-execution.md
```

For each batch:
- Embody each expert's methodology
- Execute their work order
- Write output to `agent_outputs/[agent_name].md`

### 6. Execute Phase 4: Swarm Synthesis

Read and apply:
```
/Users/farricecain/Google Antigravity/skills/swarm-commander/references/prompts/swarm-synthesis.md
```

Produce:
- `final_synthesis.md` with unified findings, provenance, and minority positions

### 7. Deliver to User

Present:
- Executive summary
- Key recommendations with confidence
- Minority report (if applicable)
- Links to detailed agent outputs for deep dives

---

## Example Invocations

```
/swarm Research my top 5 competitors in AI copywriting
/swarm Plan a product launch for my new course
/swarm Analyze 10 different positioning strategies for my brand
/swarm Write a comprehensive content strategy with multiple expert perspectives
```

## Swarm Sizes

- **Squad (3-5)**: Quick, focused tasks
- **Team (6-12)**: Standard complexity
- **Platoon (13-25)**: Deep research
- **Army (26-50)**: Enterprise initiatives

## Notes

- User approves constellation before execution begins
- All intermediate outputs saved to files for later review
- Minority positions always preserved
- Provenance tracked for every finding
