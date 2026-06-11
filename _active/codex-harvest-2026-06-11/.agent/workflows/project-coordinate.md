---
description: Create or update a shared project context home so multiple sessions and agents can coordinate on the same work
---

# /project-coordinate - Shared Project Context Home

Use this command when a project needs durable context, session logs, open threads, handoff notes, and a single place future sessions can read before acting.

## Usage

```text
/project-coordinate <project name or slug>
/project-coordinate <project name or slug> --light
```

## Pre-Flight

Read:

1. `semantic_libraries/antigravity/primitives/daily-operator-command-kit.md`
2. `CODEX.md` for artifact organization rules
3. Existing `_active/<project-slug>/INDEX.md` if present

Do not modify `/Users/farricecain/Google Antigravity`.

## Behavior

1. Resolve a project slug from the user request.
2. Prefer an existing `_active/<project-slug>/` home when one matches.
3. If no home exists, create the standard project structure:
   - `INDEX.md`
   - `00-start-here/handoff.md`
   - `06-system/project-context.md`
   - `06-system/session-log.md`
   - `06-system/open-threads.md`
4. Capture only durable context:
   - project objective
   - current status
   - active constraints
   - important paths
   - open decisions
   - latest session note
5. Keep raw brainstorming out of the hot context unless it is needed for future action.

## `--light`

Create or update only `INDEX.md` and `06-system/project-context.md`.

## Output

```markdown
# Project Coordinate

## Project Home
- Path:

## Context Captured
1. ...

## Next Session Start
Use `/project-onboard <project>` to reload this context.
```

