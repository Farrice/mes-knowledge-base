---
description: Design isolated parallel workers plus the dedicated merge infrastructure that reconciles their outputs — the two-tier scale architecture that avoids coordination collapse
---

# Worker Isolation + Merge Infrastructure Design

> Load `genius.md` first — especially Patterns 11-14 (Worker Isolation + Merge Infrastructure, Coordination Overhead Math, Scale Threshold Prediction, Episodic Sessions + Non-Deterministic Idempotence) and the Human-Team Metaphor Trap.

## When to Use
- Adding agents made the system WORSE, not better (quality drops or costs balloon as worker count grows)
- Designing a system intended to run at >5 parallel workers
- Workers currently share state, message each other, or "hand off" to peers
- Parallel outputs are being combined ad hoc (or by a human) with no dedicated merge layer
- Architecture docs use human-team language: meetings, handoffs, collaboration

## Core Insight

Peer-to-peer coordination grows O(n²); hub-and-spoke grows O(n). Past a small worker count, flat/chatty structures convert compute into coordination overhead instead of capability. The architecture that scales: fully isolated workers (share nothing at runtime) + a first-class merge layer (the "refinery") that reconciles their outputs. Isolation without merge infrastructure just moves the coordination failure downstream.

## Input Required
- **System objective + current architecture** (or greenfield design brief)
- **Worker count** — current and target
- **Failure evidence** (if retrofit): where quality degrades, duplicated work, conflicting outputs, blocked workers
- **Output type** per worker (code, prose, research findings, structured data)

## Execution

### Phase 1 — Topology Audit
1. Map every communication path between agents. Classify: orchestrator→worker (fine) vs. worker→worker (flag).
2. Count paths under current topology; project the count at target worker count. If growth is superlinear, restructure before scaling.
3. Grep the design for human-team metaphors (meetings, handoffs, collaboration, standups). Each is a candidate O(n²) path — replace with orchestrator-mediated assignment. Keep hierarchy; kill meetings.

### Phase 2 — Worker Isolation Specification
For each worker type, write a prompt-as-contract:
- **Fixed input schema** — everything the worker needs, provided at spawn; no runtime requests to peers
- **Fixed output schema** — structured so merging is mechanical, not interpretive
- **Zero shared mutable state** — worker reads its inputs, writes its own output location, touches nothing else
- **Explicit termination condition** — what "done" means; workers end, they don't linger
- **Tool catalog audit** — hold each worker's tool count well below the selection-degradation cliff (~30-50 tools); prefer narrow catalogs per worker type
- **Context minimalism** — only task-relevant context; no sibling outputs, no global project state

### Phase 3 — Merge Infrastructure (the Refinery)
Design the merge layer as a first-class component, not an afterthought:
1. **Merge owner**: single component (orchestrator or dedicated judge) owns all reconciliation decisions.
2. **Conflict taxonomy**: enumerate how worker outputs can conflict (overlapping edits, contradictory findings, duplicate coverage) and write a mechanical resolution rule for each.
3. **Deduplication pass**: detect >70% overlap between worker outputs; feed overlap patterns back into decomposition (overlap = decomposition failure signal).
4. **Escalation rule**: conflicts with no mechanical resolution route to the judge with both outputs + the decision criteria — never to an ad-hoc human arbitration.

### Phase 4 — Episodic State Design
1. Every worker writes external state before terminating (what was completed, where outputs live).
2. Make tasks idempotent against that state: a re-run first reads external state, detects completed work, and does only what remains — path unpredictable, outcome guaranteed.
3. Verify the kill test: any worker can be killed mid-run and restarted with zero lost progress and zero duplicated side effects.

### Phase 5 — Scale Validation
Before promoting the architecture:
- Run at 2x current worker count on a cheap-failure task; measure compute-to-capability conversion (useful output per token) vs. baseline
- Confirm coordination cost stays a bounded fraction of pipeline spend as workers are added
- Confirm failures trace to declared thresholds (tool cliff, spec ambiguity), not to surprise coordination behavior

## Output Schema
1. **Topology diagram** — before/after, with path counts at current and target scale
2. **Worker contract specs** — one per worker type (input schema, output schema, termination, tool catalog)
3. **Merge layer design** — owner, conflict taxonomy + resolution rules, dedup + escalation
4. **External state schema** + idempotence rules
5. **Scale validation plan** with pass/fail thresholds

## Quality Gate
- No worker→worker communication paths survive the design
- Every conflict class has a written mechanical resolution before first run
- Kill test passes for every worker type
- Human-team metaphor count in the final architecture doc: zero
