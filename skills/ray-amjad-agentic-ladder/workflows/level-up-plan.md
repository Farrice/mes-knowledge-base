---
description: Produce the specific climb plan from a diagnosed level to the next — transition mechanics + Ray's implementations, trust-gated
---

# Level-Up Plan — One Rung, Fully Built

Given a diagnosed level (run `ladder-diagnostic` first if absent), builds the climb plan for exactly ONE transition. Never plans two rungs at once — each level's loop must earn trust before the next (Boris's L3 trap).

## Pre-Flight Gate

Load `genius.md` + `references/boris-ladder-source.md` transitions. Require: diagnosed level with its missing mechanism. No diagnosis → run `ladder-diagnostic` inline first.

## Skill Acquisition

- `references/boris-ladder-source.md` — the relevant "how to get from N to N+1" row + tooling column
- `genius.md` — the implementation patterns for that transition

## Execution

1. **Anchor on the transition row** for the diagnosed level, then map each clause to its Ray implementation:
   - **0→1**: exec/buyer alignment memo; secure-launch framework; first supervised wins.
   - **1→2**: task-lifecycle forge (→ `task-lifecycle-forge`); verification environment (→ `verification-environment`); auto mode on; automated code+security review with severity routing; session management surface (agent view / tabs / desktop / chat).
   - **2→3**: context pull-in lines (wiki/discussion connectors + contradiction rule); loops and routines (→ `loop-hunter`); chat-native harness (→ `chat-native-harness`); first Claude-kicks-off-Claude experiment (→ `fanout-mission`).
   - **3→4**: pick ONE domain-specific task class to fully close (bug-fixing first — "the easiest one"); monitor-by-exception channel; vision doc as autonomy filter; guardrails per work type.
2. **Sequence into a 3-phase plan**: (a) build the mechanism, (b) run it manually 2-3× and refine (trust ledger), (c) widen autonomy + add the Manual-Once rule so refinements persist.
3. **Define the trust exit-test**: the observable condition proving the new loop is trusted (e.g. "5 consecutive lifecycles shipped from recording review alone, zero diff-reading") — the gate to ever planning the next rung.
4. **Name the level's bottleneck** from the source table so the operator knows what pain is *expected* (L2: reviewing six streams) vs what pain means *broken* (babysitting = loop not trusted).

## Content Type Adaptations

| Situation | Adaptation |
|---|---|
| Solo builder | Compress org clauses (cross-team review) to N/A; chat harness optional at 2→3 |
| Org/team | 0→1 and 2→3 org clauses (exec alignment, cross-team agency) become primary workstreams |
| Feature-heavy product work | At 3→4, flag the taste ceiling: feature-building resists full automation; vision doc partially substitutes |
| Client engagement | Wrap output in `adoption-brief` form |

## Output Requirements

One-transition plan: transition quote · mechanism build list (each mapped to a sibling workflow where one exists) · 3-phase sequence · trust exit-test · expected-vs-broken pain note.
Execution prompt: `references/prompts-v2/level-up-plan.md` — honor its Output Contract.

## Quality Gate

Reject if: plans >1 rung; skips the manual trust-run phase; exit-test unobservable; transition clauses invented rather than quoted; bottleneck omitted.
