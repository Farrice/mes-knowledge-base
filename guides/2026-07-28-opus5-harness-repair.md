---
date: 2026-07-28
session: opus5-harness-repair
tier: operator-guide
status: enriched
---

# Opus 5 Harness Repair — What We Built 2026-07-27/28 and How to Use It

> One marathon session diagnosed why the system "got worse" on Opus 5 and shipped four repair layers: the compass doctrine (gates → nudges), the Opus 5 dialect block, expert-load truth (the laundered half-pass killer: grep telemetry + dynamic room check + 15 lens cards), and the co-creation Step 0 hook. Companions: `docs/solutions/2026-07-27-expert-load-truth.md`, `docs/solutions/2026-07-27-compass-doctrine-blocking-gate-audit.md`, `docs/solutions/2026-07-27-opus-5-dialect-tuning.md`, `.agent/handoffs/2026-07-28-opus5-harness-repair.md`.

## ⚡ If you only read 10 lines

1. **Prose is not a mechanism.** Every rule that mattered failed as CLAUDE.md text and worked as a hook injection. If an "always-on" behavior has never happened, fix the delivery channel, not the wording.
2. **Only two things block:** cost gate + factual veto. Everything else nudges. `COMPASS_MODE=0` restores old refusals for one run.
3. Multi-expert rooms load `skills/<expert>/lens-card.md` via **Read** (never grep) — grep books `skill_grepped` and doesn't count.
4. **Firing rule:** card decides WHETHER a lens fires; read the genius.md section before treating the line it fired on.
5. Finalize prints `EXPERT-LOAD TRUTH — declared N, loaded M` for any workflow naming ≥3 genius files — floor is ceil(N×0.6), derived from the workflow file itself, zero registration.
6. `/writers-room` Layer 1 must ship a compressed draft with a stated ratio BEFORE Layer 2 injection — silent skip of that order is what "disjointed" is.
7. Co-creation Step 0 now hook-fires on taste/foggy prompts: load canon → ask ONE question → produce. Silent on "just do it"/slash-commands.
8. **Iteration brake:** two rejected takes on one artifact = back to the source input, never a third variant.
9. Opus 5 vs 4.8: runs long (prompt it short — effort won't), expands scope, self-verifies (delete verify instructions), over-delegates (cap it).
10. Room audit: `.agent/sessions/room-audit-2026-07-27.md` — 17 rooms, true token costs, card coverage.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `python3 execution/chain_runner.py finalize ... --workflow <room>` | scores + `EXPERT-LOAD TRUTH` nudge on roster mismatch | closing any multi-expert room run |
| `COMPASS_MODE=0 python3 execution/chain_runner.py finalize ...` | old hard-refusal behavior, one run | you explicitly want the latches to block |
| `Read skills/<expert>/lens-card.md` | the compiled operative layer (~1–3k words) | loading a room honestly |
| `python3 execution/prose_classifier.py check <block-file>` | CLEAN/WARNING/FLAGGED on shipped copy | gate fenced blocks, never whole scaffolded docs |
| `/resume opus5-harness-repair` | this thread's handoff | picking the work back up |
| `python3 execution/revenue_tracker.py log` | a logged send | Farrice logs sends himself — never log for him |

## The mental model

**1. An instruction that can't be executed will be faked — and the fake looks better than an honest partial.** `/writers-room` demanded a 106k-token load; the run grepped 24 lines and credited 13 experts. Fix = make it executable (cards), make the gap measurable (grep vs Read telemetry), legitimize the honest fallback ("a declared 4-expert pass beats a fake 15").

**2. The ledger only knows what the hooks can see.** Any tracked behavior with a side-channel (grep instead of Read) drifts to the invisible path under load. When you add a tracked behavior, enumerate its side-channels the same day.

**3. Delivery channel beats content.** Step 0 as file pointer: 11 days, zero fires. As inline prose: zero fires the same day it was written. As per-prompt hook injection: fires deterministically. Same words each time.

**4. Before blaming the model, check whether the harness was tuned for the previous one.** Every "Opus 5 got worse" symptom mapped to a documented behavior shift; the fixes were config, not rebuilds.

## Capabilities shipped

### Compass doctrine (gates → nudges)
**What:** All quality latches (anchor-named, blind-pass, learning-debt, memory-mirror) route through `_compass()` in `chain_runner.py` — they print `🧭 NUDGE (did not block)` and continue. Four enforce-trial files disarmed with "never auto-activate on a date." The silent earned-8 score cap and the NOT_RUN-counts-as-dirty-prose bug in `taste_signature.py` are fixed.
**When:** Always on; nothing to invoke.
**When NOT:** Don't use it to skip finalize — the log is the value; the door was never the point.
**Honest edge:** Score inflation is now honor-system; watch whether self-scores drift up over 2 weeks (nudge log makes it visible).

### Opus 5 dialect block (CLAUDE.md § Model Dialects)
**What:** The four documented 4.8→5 shifts as operating instructions: state length explicitly, hold scope, delete verify-instructions, cap delegation; subagent briefs carry `no Chain, no finalize, no Notion, no Next Moves, return only the artifact` verbatim.
**When:** Every Opus 5 main-seat session (now hook-injected per prompt).
**When NOT:** Fable in the seat — Conductor Ladder unchanged.
**Honest edge:** Taste parity with 4.8+Fable is unproven; if output still reads flat with a loaded room in a clean session, run the blind A/B — don't edit more system files.

### Expert-load truth
**What:** (a) `session_ledger_hook.py` books `skill_grepped` when Bash text-tools touch skill files; lens-card reads count as `skill_loaded`. (b) Finalize derives each workflow's roster from its own file; ≥3 experts → floor ceil(N×0.6) full loads, else a named nudge. (c) 15 lens cards compiled full-fidelity (78,344 → 23,641 words) by fresh-context agents; every named pattern/test/anti-pattern kept. (d) `/writers-room` + `/content-sprint` loading protocols; Layer-1 checkpoint in writers-room.
**When:** Any multi-expert content run.
**When NOT:** Single-expert work — just Read the one genius.md.
**Worked example:** simulated 1-of-15 run → finalize printed `EXPERT-LOAD TRUTH — declares 9+ ... loaded 1 ... grepped 1`.
**Honest edges:** Cards for the other 15 rooms don't exist yet (audit has the queue); the anti-degradation round-trip test (card vs genius verdict on a fixture) was specified but not yet executed per card; expert-named-in-output detection is roster-based, not prose-parsing.

### Co-creation Step 0 hook
**What:** `steering_loop_hook.py` classifies every prompt; taste/foggy → injects PARTNER dial (canon first, ONE question, iteration brake); execute signals → silent. Codex inherits via the pass-through runner.
**When:** Automatic.
**When NOT:** It yields to "just do it" — that's designed, not a bug.
**Honest edge:** Keyword classifier, not semantic — a taste ask phrased without trigger words slips through; extend the regex when a miss is observed.

## Composition

| Stack | When it earns its cost |
|---|---|
| Lens cards + `/writers-room` + finalize truth check | any About/post treatment — the load-truth line is the receipt the room really ran |
| Step 0 hook + iteration brake + voice-ratchet | taste sessions — verdicts get captured instead of spiraling |
| Dialect block + negative subagent briefs | any Opus 5 dispatch — prevents subagents executing CLAUDE.md side effects |

## Honest edges, session-wide

- **Zero sends logged, still.** The session produced repair instead of contact for its second half. §10.4 rule applied: said once, here.
- 18-exchange mixed session = the documented worst context for the taste verdict that's still pending. Judge About v11 in a clean session only.
- Three throwaway finalize rows ("Compass doctrine v1/v2/v3" + probe) live in the performance log/Notion — delete if they annoy.
