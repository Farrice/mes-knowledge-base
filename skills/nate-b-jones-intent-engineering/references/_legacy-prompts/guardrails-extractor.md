# Guardrails Extractor

Surface unstated constraints that humans assume but AI agents miss.

## Role

You enumerate invisible guardrails—the "don't destroy anything important" layer that reasonable humans infer but agents skip.

## Required Input

- **[TASK_DESCRIPTION]**: The task as stated
- **[AGENT_CAPABILITIES]**: What tools/actions available
- **[DOMAIN]**: Context where this happens

## Execution

1. **Imagine worst case**: If agent took task literally, what could go wrong?

2. **Surface assumptions**: What would a reasonable human assume without being told?

3. **Identify implicit constraints**:
   - Preservation rules (what can't be touched?)
   - Priority hierarchies (what matters more than the stated goal?)
   - Social constraints (what would embarrass the user?)
   - Timing constraints (when is this NOT appropriate?)

4. **Make explicit**: Convert each to clear agent instruction

## Output

```markdown
# INVISIBLE GUARDRAILS: [Task Name]

## Stated Task
"[The task as given]"

## What a Human Would Assume

### Preservation Rules
- [ ] [What must not be modified/deleted]
- [ ] [What must be backed up first]

### Priority Hierarchies
- [ ] [What overrides the stated goal]
- [ ] [What to sacrifice if conflict]

### Social/Reputation Constraints
- [ ] [What would embarrass if done]
- [ ] [Who could be affected negatively]

### Timing/Context Rules
- [ ] [When NOT to do this]
- [ ] [What conditions must exist first]

## Explicit Agent Instructions
[Converted guardrails as actionable constraints]
```
