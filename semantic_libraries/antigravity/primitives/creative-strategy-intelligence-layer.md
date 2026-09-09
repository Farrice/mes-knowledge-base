# Creative Strategy Intelligence Layer

## Purpose

Make creative strategy improve across cold-start Claude and Codex sessions without allowing a persona, one campaign, or unreviewed feedback to rewrite durable doctrine.

This is a shared companion layer. Alex Cooper is the first consumer; Dara Denney and other approved creative strategists may consume the same reviewed learning while retaining their own craft, voice, and workflow ownership.

## Authority Order

1. Source evidence and real outcome records
2. Human-approved semantic memory
3. Stable skill and agent doctrine
4. Pending candidates, descriptive signals, and source opinions

Pending evidence may influence a labeled hypothesis. It may not present itself as a durable rule.

## Compounding Loop

```text
creative finalize
  -> NO_EVENT evidence record
  -> due outcome or explicit feedback
  -> bounded proof state
  -> deterministic synthesis candidate
  -> existing memory-review queue
  -> human approval
  -> sovereign semantic memory
  -> Claude/Codex recall on the next relevant task
```

The append-only evidence ledger is an audit surface, not a second memory database. Approved recall remains owned by `.memory/sovereign.db` and the existing `skill_router_hook.py` path.

## Proof States

| State | Meaning | Allowed use |
|---|---|---|
| `NO_EVENT` | Artifact shipped; no later result exists | Follow-up only |
| `HUMAN_TASTE` | Explicit human preference or judgment | Project-scoped review candidate |
| `DESCRIPTIVE_SIGNAL` | Result exists without a valid comparison | Hypothesis only |
| `COMPARATIVE_RESULT` | Result has a baseline or comparison | Project lesson after two independent results |
| `CAUSAL_TEST` | Controlled test with baseline | Project lesson candidate after one test |

Shared promotion requires eligible evidence from three independent projects or campaigns, no unresolved contradiction, and human approval. Skill or agent doctrine still requires three production receipts, a blind before/after comparison, and explicit approval.

## Interfaces

`execution/creative_intelligence.py` owns:

- `capture`: append a creative event with `NO_EVENT`;
- `outcome`: attach metrics, baseline, window, and test design;
- `feedback`: attach an explicit human verdict;
- `synthesize`: preview or queue qualified lessons for existing human review;
- `recall`: return only approved creative semantic memories;
- `status`: report evidence states and due outcomes.

`chain_runner.py finalize` calls `capture` non-fatally for passed `Creative` and `Strategy` work. It never auto-promotes or edits expertise.

## Context Policy

- **Hot:** this contract, approved recalled lessons, current project scope.
- **On demand:** append-only evidence rows, source ledgers, outcome records.
- **Cold:** full transcripts, frames, commercial demonstrations, rejected and superseded candidates.
- **Never injected as truth:** promotional claims, single descriptive results, or unreviewed taste notes.

## Failure and Recovery

- Unknown event IDs refuse outcome or feedback attachment.
- Duplicate captures return the existing event ID.
- Contradictions block promotion and preserve both records.
- Queue or memory failure never blocks creative finalization; the result reports the exact error.
- Rollback removes the additive finalize hook and shared interfaces while preserving the append-only ledger for audit.

## Validation

Run:

```bash
python3 -m pytest tests/test_creative_intelligence.py
python3 execution/verify_creative_strategy_intelligence.py
python3 execution/creative_intelligence.py status
```
