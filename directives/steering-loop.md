# Steering Loop — Per-Exchange Co-Creation Protocol

> Farrice 2026-07-07: "The follow-up prompting that fires at the end of our session
> should be firing as an exchange after every single time I interact with you."
> This directive makes that global. It is the missing global wiring for the spec
> that already lived in `/go` Stage 3, `/autopilot`'s Operator Core Closeout, and
> `/steering-compass` — but only fired when those workflows were invoked.

**Enforcement is physical, not advisory**: `execution/hooks/steering_loop_hook.py`
(UserPromptSubmit) injects this contract every exchange on every model, and its
Stop mode logs misses to `.agent/sessions/steering-observe.jsonl` (observe mode,
never blocks). Toggle off: `touch .agent/steering-loop.off` or `STEERING_LOOP_OFF=1`.

## 1. The Next Moves block (every substantive exchange)

Close every substantive reply with exactly this shape:

```
**Next Moves**
1. Deepen — <copy-paste prompt that goes further on what was just delivered>
2. Adjacent — <copy-paste prompt for the opportunity this unlocked that wasn't the ask>
3. Act — <copy-paste prompt for the next concrete step toward an active goal — name the goal>

Operator Lesson: <one line teaching the move behind the work, or the harness
capability Farrice didn't know he had for exactly this situation>
```

Rules:

- Every option is a **real copy-paste prompt**, not a category. "Want me to go
  deeper?" is banned; "Run `/depth-stack` on section 2 — the proof is thinner than
  the claim" is the standard.
- **Act** names the specific active goal it advances (read `.agent/cos/goals.json`
  when in doubt) — never a generic "next step."
- At least one option per session should reveal a capability Farrice hasn't used
  (a skill, workflow, subagent pattern, or script from his own arsenal). The
  hook's rotating "Harness tip" is the floor; genuine contextual matches beat it.
- Frontier bar (from `/steering-compass`): preserve thread context, bridge real
  information gaps, no engagement-bait options that don't earn their slot.
- **Skip** only for: terse asks, pure system commands, mid-mission mechanical
  turns ("continue", "yes"), or when Farrice asks for quiet. A skipped block is
  fine; a padded block is a failure.
- Deep closeouts (builds, strategy, extractions, client work, major decisions)
  still use the full `/steering-compass` Insightful Momentum format (Use Now /
  Harden / Expand). This block is the per-exchange floor, not a replacement.

## 2. Forge Radar (opportunity-to-build scanner)

While working, watch for leverage signals:

| Signal | Example |
|---|---|
| Repeated problem | Same class of fix twice in one session, or a PRIOR SOLUTION card keeps almost-matching |
| Manual loop | Farrice (or Claude) runs the same 3+ step sequence by hand more than once |
| Re-explaining | Farrice restates a preference/constraint the system should already know |
| Missing tool | A deterministic script would replace judgment-free grunt work |
| Blind spot | The session's shape reveals an asset the arsenal doesn't have |

When a signal fires: **flag it in ONE line** — name the build and the tradeoff —
inside or beside the Next Moves block. Never halt the current deliverable to
build it (COS rule: compass, never cage). If Farrice says go (or the build is
<5 min and doesn't derail the mission), build it in-session.

**PoC gate (non-negotiable)**: a new skill/workflow/script ships only with a
worked proof-of-concept — run it once on the real case from this session and
show the output. No empty scaffolds, no "should work" (this is the
plugin-packaging ladder rule: prove the helper before packaging). If it can't
be proven in-session, it becomes a `/dump` capture or a Next Moves option, not
a shipped artifact.

Solved a non-trivial problem along the way? The Solution Recorder binding still
applies: `/extract-approach` → card in `docs/solutions/` before moving on.

## 3. Ownership map (don't duplicate)

- Per-exchange floor (this directive) — global, hook-enforced.
- `/go` Stage 3 Next-Prompts — same spec at the conductor level; unchanged.
- `/autopilot` Operator Core Closeout — deep closeout for system runs; unchanged.
- `/steering-compass` — full Insightful Momentum coaching; the ceiling.
- `execution/contextual_next_prompts.py` — deterministic renderer when a
  status/receipt-grounded set is wanted.

## 4. Telemetry

`python3 execution/hooks/steering_loop_hook.py status` — one-line health check.
Misses accumulate in `.agent/sessions/steering-observe.jsonl`; review at
`/weekly-closeout`. If misses trend up, the fix is prompt-side (this directive's
wording in the hook), not more blocking — observe mode is deliberate, matching
the session-ledger precedent.
