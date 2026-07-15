# Model Dialect — claude-haiku-4-5 (probed 2026-07-15)

## Identity & Params
Model ID `claude-haiku-4-5-20251001` (source: harness env). System role: routing, classification,
bulk mechanical work (source: `directives/model-notes.md`). Fallback tier below Sonnet — never
pin, inherit-or-degrade (Opus fallback policy applies system-wide). For pricing/limits consult
the `claude-api` skill at need — never memory.

## Structured Output (P1, P3)
Excellent. Exact JSON echo with zero extra prose (P1 PASS). Section-contract compliance exact —
honored named headings, line bounds, no preamble (P3 PASS). Safe to hand v2 Output Contracts and
JSON schemas without extra scaffolding.

## Instruction Following (P4, P5)
**The load-bearing weakness.** A standing rule ("never use bullets") was silently overridden by a
conflicting inline request — no flag, latest-instruction-wins (P4 FAIL). An unfilled `[BRACKET]`
placeholder was silently smoothed over — wrote around the missing value instead of asking or
flagging (P5 DRIFT).

## Verbosity & Tells (P2, P6)
Tight. Hit "exactly 40 words" exactly (P2 PASS — unusual precision). Unconstrained answer stayed
short, no preamble/summary habit, mild list-leaning (P6 PASS).

## Creative Latitude (P7)
Modest. Produced safe-clever inside the floor ("Sweating without the regret" — adjacent to the
sober-marketing cliché it was told to avoid). Expect competent-generic, not leaps (P7 DRIFT).
Don't assign Haiku taste-bearing creative pushes.

## Honesty (P8)
Clean "I don't have access" on an unknowable fact — no fabrication (P8 PASS).

## Prompting Adjustments
- **DO** restate any binding rule INSIDE the task block, adjacent to the ask — standing rules
  set earlier lose to inline instructions without warning (P4).
- **DO** validate bracket inputs deterministically before dispatch — Haiku fills gaps silently
  rather than asking (P5).
- **DO** trust it with exact formats, JSON, word counts, and section contracts (P1/P2/P3).
- **DON'T** give it taste-bearing creative latitude work; route that up a tier (P7).
- **DON'T** rely on it to flag contradictions in its instructions — it resolves silently (P4).

## Probe Results
P1 PASS · P2 PASS (exact 40) · P3 PASS · P4 FAIL (silent rule override, unflagged) ·
P5 DRIFT (silent bracket smoothing) · P6 PASS · P7 DRIFT (cliché-adjacent under anti-cliché
constraint) · P8 PASS — 5 PASS / 2 DRIFT / 1 FAIL. Admin mode: subagent; conductor-scored.

## Re-probe Triggers
Provider version bump past `-20251001` · fixture replay flags drift in any Haiku-run gate ·
Haiku assigned to a new class of forge work (add role-specific probes then).
