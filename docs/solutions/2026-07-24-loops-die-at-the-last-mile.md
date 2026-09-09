---
date: 2026-07-24
session: loop-engineering integration (wayfinder)
name: loops-die-at-the-last-mile
problem_class: harness / compound loops / unclosed loop
domain: harness
status: proven
problem_signature: "a feedback loop was built and its capture side runs (logs grow, queues fill, cards generate) but behavior never changes — signal produced, never consumed; ritual closers never run"
tags: [loops, compounding, closers, launchd, audit, telemetry]
---
# Loops die at the last mile — audit the closing arm, not the capture arm

**Date**: 2026-07-24 · **Session**: loop-engineering integration (wayfinder) · **Domain**: system / compound loops / self-improvement

problem_signature: "a feedback loop was built and its capture side runs (logs grow, queues fill, cards generate) but behavior never changes — signal produced, never consumed; ritual closers never run"

## Problem

Audit of all 12 compound loops in the system (2026-07-24): 4 compounding, 7 open, 1 dead. Every failure was the same shape — the **capture arm worked, the closing arm didn't**: 817 would-block events with zero readers, 130-item Phase-2 queue consumed once ever, 9 distilled memory rules stuck pending, 19 calibration seeds unpromoted, wargame failure-maps with no reader code, launchd jobs silently missing fires when the Mac slept, and `/weekly-closeout` — the designed closer for four loops — never run once. A loop whose closing step is "a human remembers a ritual" isn't a loop yet.

## Solution

1. **Audit by evidence on BOTH arms**: for each loop record (a) input signal, (b) where learning lands, (c) proof later behavior changed — file mtimes, log tails, launchd state, git. Verdict COMPOUNDING / OPEN / DEAD. (Full method: `_active/harness/loop-engineering-integration/research/2026-07-24-loop-inventory-audit.md`.)
2. **Repair closers, don't add producers**: every fix wires a deterministic consumer — `RunAtLoad` catch-up keys on sleep-lossy plists, a report script over the unread log, a mission-card emitter over the unconsumed queue, a /cos brief line over the invisible review queue, banking artifacts where an existing reader already resurfaces them (docs/solutions/).
3. **Never trust a stale metrics snapshot**: the audit's "30/86 fleet red" was an old state file; the live run was 68/1/4. Re-run the checker before fixing what it reports.
4. **Refuse producer-side "compounding"**: append-to-CLAUDE.md loops, new cron producers without named consumers, and ratcheting a green metric are the anti-patterns (canon receipts in `research/2026-07-24-canon-proven-vs-hype.md`).

Decision record: `_active/harness/loop-engineering-integration/04-deliverables/LOOP-ENGINEERING-INTEGRATION-BRIEF.md` (12 candidates, all shipped 2026-07-24).
