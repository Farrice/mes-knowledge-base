# Agent Memory Protocol

How agents maintain persistent context across conversations.

## Memory Location

Each agent stores memory in `agents/[agent-name]/memory/context.md`

## What to Remember

### Always Store
- **Brand/Project Details**: Names, positioning, voice, constraints
- **User Preferences**: Style preferences, approval patterns, working style
- **Past Work Summary**: What was created, what performed well
- **Key Decisions**: Significant choices made and reasoning

### Never Store
- Sensitive credentials or API keys
- Full content of generated deliverables (reference them instead)
- Temporary working notes
- Information already in the skill's reference files

## Memory File Format

```markdown
# [Agent Name] Memory

## Active Projects
- [Project 1]: [Brief context, last action, next steps]
- [Project 2]: [Brief context, last action, next steps]

## User/Brand Context
- Brand: [Name, positioning, voice]
- Preferences: [Known user preferences]
- Constraints: [Things to avoid]

## Learnings
- [Date]: [What was learned, how to apply it]
- [Date]: [What was learned, how to apply it]

## Past Work Reference
- [Date]: [What was created, outcome if known]
```

## When to Update Memory

✅ **Do update** when:
- Completing significant work
- Learning user preferences
- Discovering project constraints
- Receiving feedback on deliverables

❌ **Don't update** after:
- Simple questions
- Small quick tasks
- Information already captured

## Memory Maintenance

Periodically consolidate and prune:
- Remove outdated project references
- Consolidate repeated learnings
- Archive completed project context
