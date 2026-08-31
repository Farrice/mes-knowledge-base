---
date: 2026-07-26
session: telemetry surgery under concurrent sessions
name: jsonl-row-purge-by-fingerprint-not-position
problem_class: harness / telemetry surgery / positional delete
domain: harness
status: proven
problem_signature: "a bad row has to be removed from an append-only .agent jsonl log and the obvious positional delete (the last line, the most recent entry, the top row) would silently destroy a genuine record a sibling session appended in the meantime"
tags: [jsonl, telemetry, concurrency, surgery, backup, fingerprint]
---
# Solution Card — purge a `.agent/*.jsonl` row by fingerprint, never by position

**Date**: 2026-07-26 · **Domain**: system fix (telemetry surgery under concurrent sessions) · **Status**: SOLVED (recipe; helper script not built)

## Problem

A phantom row had to be removed from `.agent/performance-log.jsonl`. When the plan was agreed it
was **the last line**, and the obvious command was `head -n -1` / `sed '$d'`.

Ninety seconds later it was **line 113 of 115**. A sibling session on the same working tree had
appended two real entries behind it. A positional delete would have silently destroyed a genuine
offer-validation record instead of the junk one — and the shell would have reported success.

This is the same class as `2026-07-25-handoff-from-temp-cross-session-collision`: an operation that
identifies a record by *where it sits* rather than *what it is*, on a tree with more than one writer.

## Solution (what worked)

Identify by content fingerprint, refuse to act unless the match is unique, back up first:

```python
import json, pathlib
p = pathlib.Path(".agent/performance-log.jsonl")
FP = "<a distinctive substring unique to the target row>"
lines = p.read_text().splitlines(keepends=True)
hits = [i for i, l in enumerate(lines) if FP in l]
if len(hits) != 1:
    raise SystemExit("ABORT — expected exactly 1 match, refusing to delete")
removed = json.loads(lines[hits[0]])
p.write_text("".join(l for i, l in enumerate(lines) if i != hits[0]))
print(f"REMOVED -> {removed['date']} {removed['agent']} {removed['workflow']} {removed['quality_score']}")
```

Non-negotiables:

1. **`cp` the file to the scratchpad before touching it** — reversibility beats confidence.
2. **Abort unless exactly one match.** Zero means the fingerprint is wrong; two means it isn't a
   fingerprint. Both are stop conditions, not warnings.
3. **Print the parsed row you removed**, not just a count — that is the proof it was the right one.
4. **Verify the sibling's rows survived**: `grep -c "<their distinctive string>"` after the write.
5. If the row carries `"sync": "synced"`, the mirror (usually Notion) needs its own purge.

## Why it happened

Every `.agent/*.jsonl` is append-only telemetry written by hooks, daemons, launchd jobs, **and any
concurrent session**. The GOLDEN RULE prevents two *tools* on one tree; it does not prevent two
Claude Code sessions, and the alarm at session start is a warning, never a block. Any read→decide→
write gap is a race, and positional addressing turns that race into silent data loss.

## Reuse hook

- Any edit to `.agent/*.jsonl`, `.agent/*.json`, or `docs/solutions/index.md` that removes or
  rewrites an existing entry.
- The concurrent-session alarm fired at SessionStart (it fired this session).
- Any plan sentence containing "the last line", "the most recent entry", or "the top row".

## Forge candidate

`execution/jsonl_surgery.py` (not yet built — forge candidate only) `remove --file <f> --fingerprint <s>` wrapping the guard above
(auto-backup + abort-unless-one + parsed-row receipt). Tradeoff: one more script to maintain for an
operation run maybe monthly — worth it only if this recurs a third time.

## Related

- `docs/solutions/2026-07-25-handoff-from-temp-cross-session-collision.md` — same class, handoff lane
- `docs/solutions/2026-07-26-subagent-inherits-claude-md-and-runs-the-chain.md` — what created the row
