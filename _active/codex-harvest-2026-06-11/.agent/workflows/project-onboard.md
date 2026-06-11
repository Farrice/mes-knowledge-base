---
description: Load a project context home and brief the current session with constraints, latest state, route, and first action
---

# /project-onboard - Project Session Brief

Use this command at the start of a new session or branch when the work already has a project home.

## Usage

```text
/project-onboard <project name or slug>
/project-onboard <project name or slug> [task]
```

## Pre-Flight

Read:

1. `semantic_libraries/antigravity/primitives/daily-operator-command-kit.md`
2. `_active/<project-slug>/INDEX.md`
3. `_active/<project-slug>/06-system/project-context.md`
4. `_active/<project-slug>/06-system/session-log.md`
5. `_active/<project-slug>/06-system/open-threads.md`
6. `_active/<project-slug>/00-start-here/handoff.md` if present

If multiple project homes match, list the candidates and recommend the best match before proceeding.

## Behavior

Produce a compact onboarding brief, not a full context dump:

- project objective
- latest known state
- active constraints and boundaries
- relevant files to load next
- open decisions
- likely route/workflow for the requested task
- first action

Do not edit files unless the user explicitly asks to log or update the project.

## Output

```markdown
# Project Onboard

## Brief
...

## Active Constraints
...

## Likely Route
...

## First Action
...

## Missing Context
...
```

