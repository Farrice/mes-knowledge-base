---
description: Maintain the selected content idea queue with visible state transitions
---

# /content-queue: Human-Curated Content Queue

Show or mutate a persistent content queue through one explicit operation.

## Usage

```text
/content-queue show --state-root [path]
/content-queue add-selected [idea IDs] --state-root [path]
/content-queue kill [item IDs] --reason "[decision]"
```

## Steps

### 1. Load Skills

Read:

1. `skills/kieran-flanagan-content-ops/SKILL.md`
2. `skills/kieran-flanagan-content-ops/genius.md`
3. `skills/kieran-flanagan-content-ops/workflows/04-content-queue.md`
4. `skills/kieran-flanagan-content-ops/references/prompts-v2/content-queue-session.md`

### 2. Resolve State

Load `[STATE_ROOT]/queues/content-queue.md`. Create it only for an approved `add-selected` operation.

### 3. Execute One Operation

Run exactly one requested operation and show the mutation delta before the resulting state.

### 4. Save Output

Persist the updated queue to `[STATE_ROOT]/queues/content-queue.md`.

Killed items remain as tombstones. Never generate finished content.
