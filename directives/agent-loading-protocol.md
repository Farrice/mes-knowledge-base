# Agent Loading Protocol

> **Purpose**: Authoritative source for how expert agents and skills are loaded into context. Defines the tiered loading chain that balances depth with context efficiency.
> **Referenced from**: CLAUDE.md Context Engine section, expert_auto_routing.md, content_creation_gate.md

---

## The Loading Chain (MANDATORY ORDER)

### Tier 0: Card Check (ALWAYS FIRST)

Read `agents/_framework/invocation-cards.md`. Find the relevant expert(s).

- **Sufficient for**: Routing decisions, recommendations, ensemble selection, `/recommend` output
- **Token cost**: ~50-80 per expert
- **When to stop here**: You're deciding WHICH expert to use, not executing their methodology

### Tier 1: Standard Load (Single expert, clear task)

Read `skills/[skill]/SKILL.md` + the specific `prompts/[prompt].md` needed.

- **Skip genius-patterns.md** unless the task requires creative application of principles
- **Token cost**: ~1,350
- **When to use**: Straightforward tasks where the prompt file gives you everything you need

### Tier 2: Deep Load (Creative work, complex analysis)

Read all 3: `SKILL.md` + `genius-patterns.md` + `prompts/[prompt].md`

- **Token cost**: ~2,550
- **When to use**: The task requires taste, creative judgment, or novel application of the expert's principles
- Optionally also read `AGENT.md` + `memory/context.md` for persona embodiment

### Tier 3: Sub-Agent Load (Multi-expert or extended work)

Spawn a SkillExecutor sub-agent. Sub-agent reads all files in fresh context. Returns compressed result.

- **Main context cost**: ~300 tokens (handoff summary only)
- **Sub-agent context**: Full Tier 2 files (~2,550+)
- **When to use**: 2+ experts needed, or session has already loaded 10+ files

---

## Decision Matrix

| Task Complexity | Expert Count | Load Tier |
|---|---|---|
| Quick recommendation / routing | 1-5 | Tier 0 (cards only) |
| Single expert, clear task | 1 | Tier 1 |
| Single expert, creative/complex | 1 | Tier 2 |
| Multi-expert, any complexity | 2+ | Tier 3 (sub-agents) |
| Council / Roundtable | 3-5 | Tier 0 (cards) + sub-agents for execution |

---

## The 9-Step Agent Loading Sequence (Full)

When doing a Tier 1+ load, follow this sequence:

1. **Check** `agents/_framework/invocation-cards.md` for quick expert summary (~50 tokens vs ~500+)
2. If deeper application needed, **read** `agents/[agent-name]/AGENT.md` for full persona
3. **Read** `agents/[agent-name]/memory/context.md` for persistent project context
4. **Read** `skills/[skill-name]/SKILL.md` for skill overview
5. **Read** `skills/[skill-name]/references/genius-patterns.md` for expert patterns (Tier 2+ only)
6. **Read** relevant prompt from `skills/[skill-name]/references/prompts/[prompt].md`
7. **Execute** using the prompt's framework
8. **Embody** the expert persona throughout the response
9. **Update** `memory/context.md` when you learn project-specific details

---

## Agent-to-Agent Handoffs

When your current task enters another agent's domain:

1. Summarize what you accomplished
2. Identify what the other agent should handle
3. Ask user for approval to handoff
4. Read receiving agent's files (starting at Tier 0) and switch personas

---

## Sub-Agent Prompt Template (For Tier 3)

When spawning sub-agents, **never describe frameworks — require direct file reading.**

```
## PHASE 1: SKILL ACQUISITION (Do this FIRST)

Read these files in order:
1. /Users/farricecain/Google Antigravity/skills/[skill-name]/SKILL.md
2. /Users/farricecain/Google Antigravity/skills/[skill-name]/references/genius-patterns.md
3. /Users/farricecain/Google Antigravity/skills/[skill-name]/references/prompts/[specific-prompt].md

After reading, confirm: What are the 3 most important patterns? What is the output structure? What would the expert say is WRONG?

## PHASE 2: EXPERT-DRIVEN EXECUTION
Apply the methodology to: [Task description]

## PHASE 3: OUTPUT
Embody principles (not templates). Reference patterns by name. Pass the skill's quality test.

## PHASE 4: RECURSIVE REFLECTION
Would the expert be proud? Is this creative application or mechanical copy? Remarkable or merely competent?

## VERIFICATION
SKILL FILES READ: [list] | PATTERNS APPLIED: [list] | QUALITY CHECK: [test, pass/fail]
```

**Creative Latitude Mandate**: Skill files transfer principles, taste, and intuition — NOT templates. Absorb principles, create something original.

---

## Missing Card Protocol

If you need an expert who doesn't have an invocation card:
1. Fall back to Tier 1 (read SKILL.md directly)
2. After the session, add a card to `agents/_framework/invocation-cards.md`

---

*Created: 2026-02-27 | Context Engine v1.0*
