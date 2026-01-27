# Multi-Agent Orchestration Protocol

Guidelines for coordinating expert agents.

## Invoking an Agent

When the user mentions an agent by name or describes a task matching an agent's domain:

1. Read the agent's `AGENT.md` for persona and capabilities
2. Read `memory/context.md` for persistent context
3. Embody the expert persona throughout the response
4. Use the agent's decision framework for approach
5. Reference available skills when executing deliverables

**Syntax**: User says "@seena-rez" or "ask Seena Rez to..." or describes viral content work.

## Agent-to-Agent Handoffs

When one agent's task enters another's domain:

### Handoff Initiation
1. Current agent identifies handoff trigger (per their Handoff Protocol)
2. Current agent summarizes:
   - What was accomplished
   - What needs to happen next
   - Relevant context to pass
3. Request user approval for handoff

### Handoff Execution
1. Read receiving agent's `AGENT.md`
2. Update receiving agent's `memory/context.md` with passed context
3. Switch to receiving agent's persona
4. Continue work

## Parallel Agent Work

When multiple agents should work on different aspects:

1. Identify if tasks are truly independent
2. Create separate work streams
3. Synthesize outputs at completion
4. User reviews combined deliverable

## Conflict Resolution

When agents have different approaches:

1. Present both perspectives to user
2. User decides direction
3. Update agent memory with decision for future reference

## Memory Sharing

Agents can reference each other's memory when relevant:
- Read-only access to other agent's context
- Only update your own memory directory
- Core project context belongs in user's project files, not agent memory
