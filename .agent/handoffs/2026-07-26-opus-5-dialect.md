---
thread: opus-5-dialect
status: ready
resume_hint: Add the negative-scoping exclusion block to directives/sub_agent_protocol.md, then prove it with one throwaway model:opus dispatch
unfinished: Fleet-wide dispatch templates not yet scoped; raw probe outputs not persisted to disk; P2/P6/P9 need a cross-tier re-score from a Fable seat
branch: main
pin: true
---

# Model Dialects — Opus 5 Probe Battery + Card (subagent scope containment)

## Purpose
- **Next session should do:** apply the P9 finding across the fleet — add the negative-scoping exclusion block to `directives/sub_agent_protocol.md` and the Workflow dispatch templates, so no future subagent runs the Chain or writes to Notion from a task brief.
- **Not in scope:** re-running the probe battery; editing routing, seating, or the Executor Model Registry (all verified untouched and correct); building `jsonl_surgery.py` (flagged, not approved).

## Load First
- `directives/model-dialects/claude-opus-5.md` — the card this session produced; P9 section is the whole reason for the next task
- `docs/solutions/2026-07-26-subagent-inherits-claude-md-and-runs-the-chain.md` — the exact exclusion block to paste, plus the cleanup recipe
- `directives/sub_agent_protocol.md` — the edit target; it specifies what to *give* a subagent, never what to *forbid*
- `directives/orchestration-doctrine.md` §Executor Model Registry (L68-84) — already correct for Opus 5 / Sonnet 5; read, don't edit

## Current State
- **Objective:** close the gap between "Opus 5 is seated correctly" (true since 2026-07-24) and "Opus 5 dispatches are scoped safely" (not yet true).
- **What is already done:**
  - `/forge dialect claude-opus-5` run end-to-end in subagent admin mode; 8 isolated `model: opus` probes, conductor-scored: **6 PASS / 2 DRIFT / 0 FAIL** on P1–P8, plus a **P9 extension probe scored FAIL**.
  - Card written + `model-notes.md` pointer updated → commit `ce81208ed`, pushed to main.
  - Two solution cards banked (subagent side-effects; jsonl purge by fingerprint).
  - Phantom telemetry purged: row removed from `.agent/performance-log.jsonl` (115→114) and Notion page `3a949875-a897-8129-ac86-cbdbbd1990c3` archived. Sibling session's rows verified intact.
  - Chain finalize PASS, composite **8.33**, learning debt cleared.
- **What is uncertain or stale:**
  - **Independence caveat** — conductor and target were the same tier (Opus 5 scoring Opus 5). Contexts were isolated; scoring was not cross-tier. P2, P6, and P9 deserve a re-score from a Fable seat.
  - **Engine Quality Gate is PARTIAL** — the 8 raw probe outputs live in this session's agent transcripts, never persisted to disk. Deliberate (avoiding the unrequested-artifact failure the card documents), but the gate is not fully satisfied.
  - Haiku 4.5 and Sonnet 5 cards still assert the restate-binding-rules tax is "family-level." P4 falsifies that at the Opus tier only — the two older cards are still correct for their own tiers and need no edit.
- **Latest proof/receipt:** commit `ce81208ed` (2 files, 104 insertions); finalize composite 8.33 logged to Notion; `grep -c 'CLIENT NAME' .agent/performance-log.jsonl` → 0.

## Suggested Skills / Workflows
- `/forge dialect <model>` — the lane that produced this; engine at `skills/forge-os/references/prompts-v2/dialect-probe.md`
- `/extract-approach` — if the protocol edit surfaces a second reusable recipe
- `/fixture-replay` — the drift detector that triggers a re-probe on this card
- `/cos` — 3 questions + 5 check-ins due; outer loop 25 check-ins stale

## Exact Next Prompt
```text
Read directives/model-dialects/claude-opus-5.md (P9 section) and
docs/solutions/2026-07-26-subagent-inherits-claude-md-and-runs-the-chain.md.

Add the negative-scoping exclusion block to directives/sub_agent_protocol.md as a
required element of every non-deliverable dispatch brief, and to the Workflow
dispatch templates. Exclusion text is verbatim in the solution card.

Then prove it: dispatch one throwaway model:opus subagent with a one-line copy task
under the new brief, and confirm from its return text that it produced ONLY the
artifact — no Chain, no finalize, no score, no Notion write, no Next Moves.
Show me the before/after brief diff and the proof output. Do not edit routing,
seating, or the Executor Model Registry.
```

## Acceptance Criteria
- `directives/sub_agent_protocol.md` contains the exclusion block as a required element, not a suggestion.
- A live throwaway `model: opus` dispatch under the new brief returns the artifact only — verified from its actual return text, not asserted.
- `.agent/performance-log.jsonl` line count unchanged by that test dispatch (the deterministic proof it didn't finalize).
- Routing, seating, and the Executor Model Registry are untouched (`git show --name-only` shows no such files).

## Risk Notes
- **Concurrent sessions are live on this tree.** A sibling session appended to `.agent/performance-log.jsonl` mid-task this session and nearly caused a wrong-row delete. Claim `session_lock.py` before any multi-file work; address telemetry rows by content fingerprint, never by line position.
- **`--from-temp` collision:** the shared OS temp dir accumulates `handoff-*.md` from every session and from phantom subagent finalizes (one was removed this session before it could poison this handoff). Always read the `from-temp:` line and confirm the basename matches the intended work.
- **Over-correction risk:** the exclusion block must not leak into dispatches that *are* meant to produce logged deliverables — scope it to non-deliverable briefs (probes, scouts, drafts-for-inspection, verification passes).
- No secrets, credentials, or client PII in this handoff.
