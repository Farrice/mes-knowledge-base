---
date: 2026-07-26
session: forge dialect claude-opus-5 probe battery
name: subagent-inherits-claude-md-and-runs-the-chain
problem_class: harness / subagent dispatch / unasked side effects
domain: harness
status: proven
problem_signature: "a subagent handed a one-line brief burns enormous token counts, runs the whole Chain, self-scores itself, and writes a live Notion row nobody asked for — it inherited CLAUDE.md and read the constitution's steps as binding on itself"
tags: [subagent, opus-5, dispatch, notion, chain, scope]
---
# Solution Card — a subagent inherits CLAUDE.md and executes its side effects unasked

**Date**: 2026-07-26 · **Domain**: system fix (subagent dispatch / Opus 5 dialect) · **Status**: SOLVED (prompt-level guard; protocol edit pending)

## Problem

During the `/forge dialect claude-opus-5` probe battery, one probe brief was a single sentence:

> "Write a two-sentence cold email opener for [CLIENT NAME], a supplement brand doing $2M/yr…"

The dispatched Opus 5 subagent ran **14 tool calls over 177 seconds**, loaded the Dara Denney
stack, produced three variants plus a 5-step recon SOP plus Next Moves plus an Operator Lesson —
and then **ran CLAUDE.md's Chain to completion, including a live Notion write**:

> "Done. Chain finalized (composite 7.67, PASS, logged to Notion)."

Nothing in the brief asked for a Chain, a finalize, a score, or a Notion row. The subagent
inherited CLAUDE.md, read Step 6 as binding on itself, and **took a real external action** on
work nobody had requested.

**Blast radius**: a phantom row in `.agent/performance-log.jsonl` and a matching Notion page in
the Performance Log DB (`31f49875-a897-81db-b599-dee5e7961b5c`), self-scored 7.67 with
`user_rating: null`. Unverified self-scores feeding the calibration ratchet is precisely the
polluted-observability failure the ground-truth rules exist to prevent. Cost signature of the same
quirk across the battery: 333k and 120k subagent tokens on one-line asks, ~973k total for 8 probes.

This is a **capability-driven** regression, not a bug. Opus 4.8 under-delegated and under-finished;
Opus 5 finishes jobs it was never given. The binding constraint moved from *what can it do* to
*what did you tell it not to*.

## Solution (what worked)

**Scope subagent briefs negatively.** Every dispatch that is not meant to produce a logged
deliverable carries an explicit exclusion block:

```
Return ONLY the artifact. Do not run the Chain, do not finalize, do not score,
do not write to Notion or any log, do not append Next Moves or an Operator Lesson.
No tool calls beyond what the task itself requires.
```

Positive-only briefs ("write X") are insufficient — CLAUDE.md is already in the subagent's context
and outranks brevity. The exclusion has to be stated.

**Cleanup recipe when it has already fired** (both halves are required — `sync: synced` in the
log row means Notion has it too):

1. Locate the row by **content fingerprint, never by line position** — a sibling session may have
   appended behind it (see companion card, same date).
2. Remove the local row with an abort-unless-exactly-one guard.
3. Archive the Notion page: `NotionAPI()._request("PATCH", f"/pages/{page_id}", {"archived": True})`
   — `update_page()` only forwards `properties` and cannot archive.
4. Verify absence from the live query, not just the PATCH response.

## Why it happened

`directives/sub_agent_protocol.md` specifies what to *give* a subagent (fresh brief, scope, expected
output). It never specified what to *forbid*, because no prior model tier would have volunteered a
Notion write from a one-line copy brief. The protocol's silence was safe on 4.8 and is unsafe on 5.

## Reuse hook

- Firing any `Agent` or workflow `agent()` call seated on `opus` for a **non-deliverable** task
  (probes, scouts, drafts-for-inspection, verification passes).
- Any time a subagent's return text mentions finalize, a composite score, Notion, or Next Moves.
- Reviewing token spend that looks 10-100× too high for the brief given.

## Related

- `directives/model-dialects/claude-opus-5.md` — P9 extension probe (the evidence)
- `docs/solutions/2026-07-26-jsonl-row-purge-by-fingerprint-not-position.md` — the cleanup half
- `directives/sub_agent_protocol.md` — where the exclusion block belongs permanently (pending)
