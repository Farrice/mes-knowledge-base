# Knowledge Librarian Solution Surfacing

Use this pattern when a durable solution folder exists but future missions are not guaranteed to consult it.

## Problem

A solved-problem library can become shelfware if it is not surfaced during planning. The system may keep creating new plans even when reusable guidance already exists.

## Trigger

- A mission may reuse a previous solved problem.
- A workflow now produces reusable `solution-capture.md` files.
- A new durable docs folder exists outside the main knowledge manifest.
- Farrice wants fewer things to remember manually.

## Working Solution

Give Knowledge Librarian a deterministic solution-search step and require Mission OS to cite relevant solution docs in the Library Decision.

Use:

```bash
python3 execution/knowledge_compiler.py solutions "[mission focus]" --top 8
```

The Library Decision should say one of:

- apply directly
- adapt into this mission's plan
- ignore with reason
- promote a new solution after completion

## Why It Works

It moves reusable solution docs from passive storage into active mission preflight. The user does not need to remember the folder exists; the librarian checks it before new work is invented.

## Prevention Rule

Before substantial mission planning, run solution search alongside knowledge briefing and command routing. If a new reusable lesson appears, capture it in the mission's `solution-capture.md` and promote it to `docs/solutions/` only when it generalizes.
