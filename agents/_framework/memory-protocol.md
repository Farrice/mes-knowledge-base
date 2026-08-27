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

## Council Sessions (the Mailroom, 2026-08-27)

Council engines now READ `memory/context.md` at seat time (capped excerpt via
`execution/persona_team.py`) and APPEND one entry per session at close — this is the persona's
"private notes": accumulated positions, verdicts, and open predictions. Entry format (written by
`persona_team.py close-session`, never hand-formatted):

```markdown
## Council session — YYYY-MM-DD
- **Question:** …
- **My position:** …
- **Council verdict:** …
- **Session digest:** knowledge/council-sessions/<date>-<slug>.md
```

A persona seated twice on related questions must recognize its own prior position. Trust
calibration (`councils/README.md`) runs on these entries.

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
