---
date: 2026-08-20
session: harness-opus5-diagnosis
tier: operator-guide
status: enriched
---

# System: Opus 5 Gap Diagnosis - Resolved, Defaults Installed — What We Built 2026-08-20 and How to Use It

> Measured the 4.8→5 gap instead of vibing it (Fable-seat probes + blind 3-seat taste A/B), wrote the seating ruling into the dialect cards, and installed the **Intent Brief Default** — raw intent → compiled brief → confirm → fresh-context executor — as a per-prompt hook injection. Also: SessionStart wall → 5-line digest; 7 false-positive "Stop says" nag rules disabled. Companions: `directives/model-dialects/claude-opus-5.md` § Fable-Seat Re-probe · handoff `.agent/handoffs/2026-08-20-harness-opus5-diagnosis.md` · plan `~/.claude/plans/i-don-t-know-i-recursive-eclipse.md`.

## ⚡ If you only read 10 lines

- Opus 5 pain = **interaction ergonomics, not taste**: blind test rated Opus's ghostwritten take GREAT, Fable's TERRIBLE (n=1, voice_ratchet rows 58-60).
- Seating ruling: **Fable/Sonnet 5 conduct interactive sessions; Opus 5 executes dispatched work — including creative prose** under "no Chain, no finalize, no Notion, no Next Moves, return only the artifact".
- After 2026-08-31 (Fable window closes): Sonnet 5 front seat. Its dialect card now HAS a machine block — the injector was silent for it before today.
- Raw ask in any session now auto-fires the **INTENT BRIEF card**: ≤10-line brief, your confirm, then fresh dispatch. "Just do it" skips the confirm, never the clean room.
- Rejected take → **fix the brief, dispatch fresh** — never iterate the same pen in-thread (composes with the spiral brake).
- Verbosity is harness-amplified, not Opus-specific: Sonnet ran ~380w on a bare question under injected context. Only dialect injection counteracts.
- `/fast` mode = Opus. Don't toggle it expecting a smaller, tamer model.
- Startup scroll: `execution/hooks/session_brief.py` digests 6 noisy hooks to one line each. Extend the digest; never re-add per-script dumps.
- New warn-hooks law: key on **receipts** (logs, commands), never transcript word-matching — 7 mention-based rules died today for nagging every session.
- First thing to run next session: one raw ask, watch the brief-confirm beat fire. Wrong feel = reshape the card in `steering_loop_hook.py`, one line.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| (automatic) raw ask in chat | INTENT BRIEF card → ≤10-line brief for confirm | every raw substantive ask — no invocation |
| (automatic) "write/draft a post/brief/doc…" | FRESH PEN card → clean-room dispatch | artifact-shaped asks |
| `echo '{"session_id":"t","prompt":"<p>"}' \| .venv/bin/python3 execution/hooks/steering_loop_hook.py prompt` | the exact injection for any prompt | debugging why a card did/didn't fire |
| `python3 execution/voice_ratchet.py add --verdict pass\|fail --line "…" --why "…" --source "…"` | felt-verdict row in calibration log | every gut verdict on prose |
| `python3 execution/platform_compiler.py check` | constitution drift report | before/after editing CLAUDE.md |
| `/resume harness-opus5-diagnosis` | this thread's handoff | continuing this work |

## The mental model

1. **Quality is working conditions, not model choice.** Take B won because its author had a settled brief, a clean head (zero conversation debris), and one shot judged from outside. Every in-thread draft lacks all three.
2. **Seat by disposition: conductor ≠ pen.** Fable/Sonnet compress and contain — good conductors, weak storytellers. Opus narrates and expands — bad conversationalist, strong pen. The same trait is the flaw in one seat and the virtue in the other.
3. **Opt-in tools die; injections fire.** `/refine-intent`, `/validate-intent`, intent-pipeline.md — all correct, all unused. The mirror injection fires every prompt. Defaults must live in the injector.

## Capability: Intent Brief Default

**What it is:** `steering_loop_hook.py` classifies every prompt. Raw dump (2+ vomit signals, ≥120 chars) → INTENT BRIEF card: compile Deliverable+size · Outcome/felt standard · Constraints · Sources · Taste bar · Pen seat · Open questions-that-change-execution; present for confirm; production only after. Sharp ask → one-line mirror, straight to work.

**When to reach for it:** never — it reaches for you. That's the point.

**When NOT to rely on it:** Codex sessions (hook is Claude-Code-only; doctrine reaches Codex via `feedback_fresh-pen-protocol` memory until platform sync). Mission-scale work → `/go` (full Mission Card + plan mode).

**How to invoke escape hatches:** "just do it" (skips confirm, keeps clean room) · `mode X` overrides the work-mode classifier.

**Worked example:** this session's Take B — the six-line brief (voice card + chosen angle + I-narrative rule + 150-220w + containment) dispatched to a fresh Opus seat produced the take Farrice rated "great" on first shot.

**Honest edges:** bench-tested (5-path sabotage battery), NOT yet live-fired in a real session. n=1 on the Opus-taste verdict. The raw-dump detector is regex — a calm, single-sentence-but-vague ask can slip past it to the compact mirror.

## Capability: Fresh Pen clean room (generalized)

**What it is:** artifact-shaped asks (write/draft/build × post/email/brief/report/doc/deck/…) get a card forbidding in-thread production: one fresh-context executor, seat per `directives/orchestration-doctrine.md` Executor Registry (creative prose: Opus 5; grind: Sonnet 5), negative brief verbatim.

**When NOT to:** diagnosis, debugging-with-context, decisions — the conversation IS the material; front seat handles those. Trivial mechanical edits stay front-seat.

**Honest edges:** dispatch adds ~30–90s per artifact. The suppression rule (INTENT BRIEF card present → fresh-pen card suppressed) is string-matched on the injected block.

## Capability: noise diet (startup digest + hookify law)

**What it is:** `session_brief.py` wraps 6 SessionStart hooks → one line each, alarms preserved, pointers to full views. Seven hookify `event: stop` warn rules disabled (they matched trigger words CLAUDE.md injects into every session). The three `event: bash` command-guards (fal/Notion/Perplexity budgets) stay live.

**When NOT to:** don't add a new stop/warn rule keyed on transcript text — receipts only (`feedback_no-mention-based-stop-warn-hooks`, BINDING).

**Honest edges:** the digest runs children with a 15s timeout each; a hung child reports one line rather than blocking startup. Real backstops these rules duplicated (routing/quality/grounding) still run in `chain_runner.py finalize`.

## Composition (options, not wiring)

| Stacks with | When it earns its cost |
|---|---|
| `/go` | mission-scale: multi-session, fleet, or contract-worthy work — full Mission Card replaces the light brief |
| `/fresh-pen` | explicit pen swap mid-thread after the spiral brake trips |
| `/jam` | taste-bearing forks where two takes + gut verdict beat one brief |
| blind A/B method (this session) | any "which seat writes X better" question — identical brief, `Agent` tool with model opus/sonnet/fable, unlabeled presentation, verdicts → voice_ratchet |
