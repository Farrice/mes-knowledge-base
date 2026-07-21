---
description: Diagnose the ACTUAL agentic-coding level (0-4) of a setup — perceived vs real, with the specific missing mechanism
---

# Ladder Diagnostic — Where You Actually Are

Applies Boris Cherny's 5-level ladder with Ray's trap-detection: level is set by **loop trust**, never by agent count or tool inventory. Most setups that feel like Level 2-3 are Level 1 with extra windows.

## Pre-Flight Gate

Load `genius.md` (patterns 1, 2, 8) + `references/boris-ladder-source.md`. If the subject's setup details are unknown, interview before scoring — never diagnose from vibes.

## Skill Acquisition

- `genius.md` — the 12 patterns, especially Parallel ≠ Progress
- `references/boris-ladder-source.md` — canonical levels, bottlenecks, transitions

## Execution

1. **Inventory the setup**: sessions run in parallel; where agents run (terminal/desktop/cloud/chat); what happens after an agent claims "done"; review process; any routines/proactive kickoffs.
2. **Run the two-test challenge** (this overrides self-reported level):
   - Does the agent verify its own work **end-to-end on the change's surface** (GUI → pixels, API → request/response, agent → run it) before the human sees it — and is that loop *trusted*?
   - Is automated code review + security review running by default, with severity-routed fixes?
   - Both no → Level 1, regardless of parallel sessions.
3. **Score against the ladder**: assign 0-4 using the source table's descriptions and bottlenecks. Check L3+ claims against: context pull-in (wikis/discussions), loops and routines running, Claude kicking off Claude. Check L4 claims against: most agents machine-kicked, monitor-by-exception.
4. **Name the gap**: perceived level vs actual level, and the *single missing mechanism* that sets the actual level (e.g. "no trusted verification loop — everything else is Level 2 theater").
5. **Prescribe the next unlock**: quote the relevant "how to get from N to N+1" transition and Ray's concrete implementation of it (task lifecycle / verification environment / routines / fan-out).

## Content Type Adaptations

| Subject | Adaptation |
|---|---|
| Solo developer | Score personal workflow; attention is the L1 bottleneck to name |
| Team/org | Score the org mode, note the 10x-individual-vs-org gap (Boris's opening observation); L0 gating questions first |
| This system (Antigravity) | Route to `system-ladder-audit` workflow instead |
| Client audit (consulting) | Pair with `adoption-brief` for the deliverable form |

## Output Requirements

Diagnostic card: **Actual level (0-4)** + perceived level · two-test results · the missing mechanism (one sentence) · bottleneck (from source table) · next unlock with its transition quote · 3 first actions.
Execution prompt: `references/prompts-v2/ladder-diagnostic.md` — honor its Output Contract.

## Quality Gate

Reject if: level justified by session count or tools owned; two-test challenge skipped; missing mechanism not named; next unlock not tied to a source transition; any invented level or cell (genius.md anti-patterns).
