# Agent Template

> Copy this template to create a new agent. Replace all [BRACKETED] content.

---
name: [agent-name]
expert: [expert-name]
domain: [domain-description]
skills:
  - [linked-skill-name]
source: "[extraction source — e.g., MES 3.0 Expert Interview Part 1-3, YouTube masterclass, course module]"
credentials: "[1-line expert credential — e.g., $500K/year AI copywriter, 7-figure creator business]"
last_updated: [YYYY-MM-DD]
---

# [EXPERT NAME] Agent

[One paragraph describing who this agent embodies and their unique expertise. Should feel like introducing a trusted advisor.]

## Core Competencies

What this agent excels at (drawn from the skill's genius patterns):

1. **[Competency 1]**: [Brief description]
2. **[Competency 2]**: [Brief description]
3. **[Competency 3]**: [Brief description]
4. **[Competency 4]**: [Brief description]
5. **[Competency 5]**: [Brief description]

## Available Skills

Prompts this agent can invoke (linked from skill):

| Capability | Workflow | When Used |
|------------|--------|-----------| 
| [Capability 1] | [workflow-1.md] | [When this agent uses it] |
| [Capability 2] | [workflow-2.md] | [When this agent uses it] |
| [Capability 3] | [workflow-3.md] | [When this agent uses it] |

## Decision Framework

How this agent approaches problems:

1. **First**: [What they assess first]
2. **Then**: [What they do next]
3. **Finally**: [How they deliver]

## Activation Triggers

When to invoke this agent (vs. using skills directly):

- ✅ [Situation where agent is appropriate]
- ✅ [Another appropriate situation]
- ❌ [Situation where just use the skill instead]

## Approval Gates

Actions requiring user confirmation before proceeding:

- [ ] **High-stakes execution**: [Example requiring approval]
- [ ] **External publishing**: [Example requiring approval]
- [ ] **Budget allocation**: [Example requiring approval]

## Handoff Protocol

When this agent should delegate to another expert:

| Situation | Hand off to | What to transfer |
|-----------|-------------|------------------|
| [Situation 1] | [Other Agent] | [Context to pass] |
| [Situation 2] | [Other Agent] | [Context to pass] |

## Memory Reference

This agent's persistent context is stored in `memory/context.md`. Update it when:
- Learning user brand/project details
- Completing significant work
- Discovering preferences

---

## Workflow File Standards

When creating workflow files for this agent's skill, each workflow MUST include:

### Output Schema
Define the exact structure of the deliverable so output follows a predictable format:

```yaml
## Output Schema
final_deliverable:
  component_1: "[what this contains]"
  component_2: "[what this contains]"
  component_3: "[what this contains]"
```

### Example Output
Include at least one worked input → output example per workflow:

```markdown
## Example Output

**Scenario**: [Specific, realistic input context]

**Result**:
[The actual deliverable — complete enough to demonstrate quality standard.
Not a description. The thing itself.]

**What makes this excellent**: [1-2 lines on why this meets the expert's standard]
```

**Sources for examples** (in priority order):
1. Expert demonstrations from the source transcript
2. Legacy v1.0 prompt examples (check `references/prompts/`)
3. Real-world exemplars of the expert's published work
