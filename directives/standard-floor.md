# The Standard Floor

> **Machine source:** `execution/standard_floor.py` (`FLOORS` dict) — update BOTH together,
> same contract as `directives/routing-bindings.md`. The dict is authority; this file is the
> human mirror.
> **Consumed by:** `execution/homework_binder.py` → the `Homework:` line in every session's
> Stop receipt (`execution/execution_receipt.py`).

## What a floor is

A floor answers, per artifact class: *what must be true of this file's own bytes before a
session may count it as done?* Not "did a gate run" (a gate can run against stale bytes) and
never "did the assistant say so" (prose is the label; the floor opens the box).

Every floor is a triple — `roots` (where the class lives) · `predicate` (~10 deterministic
lines over content) · `fixture` (a known-bad file the predicate MUST reject, plus a
known-good twin it MUST accept). **No fixture, no floor** — an unexercised predicate
refuses to grade (`UNKNOWN`), never passes. The fleet's weekly self-test re-proves every
fixture in both directions.

## The classes (2026-08-09)

| Class | Scope | Floor |
|---|---|---|
| `rendered` | `.html` under `.agent/`, `deliverables/`, `_active/` | No wall of raw markdown (`##`, `**`, `\|---\|`, fences) surviving into the visible text layer — trip at 5 tokens. The 2026-08-08 mdview specimen is the bad fixture. |
| `content` | `.md` under `deliverables/`, `_active/farrice-brand/content/`, `_active/clients/` | Bytes floor: ≥300 body bytes, zero placeholders (`TODO:`/`FIXME`/`[TK]`/lorem) and zero conflict markers. Second layer, honestly labeled either way: `prose_classifier.py` ban-bank check — detail says "bytes + ban-bank" when it ran, "bytes only — classifier NOT run" when it couldn't. |
| `code` | `.py` under `execution/` | Parses (`compile()` only — **never import**: a verifier must not run side effects in what it grades), zero merge-conflict markers, ≥3 real code lines. The bad fixture is shaped like the real 2026-08-08 find: a lane-seal merge that clobbered `control_intent.py`. |

## Verdicts

`PROVEN` (floor met) · `PARTIAL` (artifact real, floor unmet — names the missing piece) ·
`UNPROVEN` (claim with nothing bound) · `UNKNOWN` (no fixture / no claims / lane artifact /
unreadable). None is called "failed"; nothing blocks, ever (Compass Doctrine).
**Empty window = UNKNOWN, never green. Lane work = UNKNOWN, never UNPROVEN.**

## Adding a class

1. Write the predicate (~10 lines, bytes in → `(ok, detail)` out, deterministic, no imports
   of the graded artifact).
2. Write BOTH fixtures. The self-test loops the dict — a new class with fixtures is tested
   automatically; without them it refuses to grade.
3. Add the row above and the dict entry in the same commit.
