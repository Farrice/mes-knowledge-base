---
description: Replay a skill's golden fixtures against the current model and report drift deterministically
---

# /fixture-replay — Golden-Fixture Drift Detection

Use when a new model ships, a skill's v2 engine prompt changes, or a dialect card flags a re-probe
trigger — anywhere "did this prompt degrade?" is currently answered by feel. Replays the `## Fixtures`
sections of v2 prompts (input values → expected output SHAPE) through fresh-context probe agents and
diffs the results against the recorded shapes. Do NOT use it to grade output quality or taste (that is
the Chain's quality gate), to fix systematic skill weaknesses (that is `/skill-anneal`, which needs the
documented failures this workflow produces), or to characterize a brand-new model from zero (that is
`/dialect-probe` — replay assumes the prompt was once known-good).

**Honesty split** — deterministic: fixture discovery, fixture parsing, the structural pre-gate, log
appends, verification counts. Model-dependent: executing fixtures (probe agents) and judging shape
(conductor, bound by the rules in Stage 4). The log is the backstop: no run exists unless its lines do.

## Invocation

- `/fixture-replay <skill-name>` — replay all fixture-bearing v2 prompts in one skill
- `/fixture-replay <skill-name> --prompt <prompt-name>` — one prompt only
- `/fixture-replay --all` — full sweep (new-model day, engine-prompt refactor day)
- `/fixture-replay <skill-name> --model <model-id>` — pin the probe model; default is the harness default

## Stage 1 — Discover & Pre-Gate (deterministic)

1. Resolve targets: `grep -rl "^## Fixtures" skills/<skill>/references/prompts-v2/*.md`
   (or `skills/*/references/prompts-v2/*.md` for `--all`).
2. **Gate — structural audit first**: run `python3 execution/renaissance_audit.py --quiet`. Any FAIL in
   a targeted file = stop for that file; a structurally broken v2 makes fixture verdicts meaningless.
   Fix structure (or exclude the file, stating so) before replaying it.
3. If a named dialect card exists at `directives/model-dialects/<model-id>.md`, read it — it informs
   judging context in Stage 4 (known quirks), never excuses a FAIL.

**Failure behavior**: zero fixture-bearing prompts found → stop-and-surface. Append one
`NO_FIXTURES` line to the log (Stage 5 schema), report that the skill is not born-instrumented, and
point at the prompts-v2 backfill (`## Fixtures` per `skills/forge-os/references/prompts-v2/prompt-forge.md`).
Never invent fixtures to have something to run.

## Stage 2 — Parse Fixtures (deterministic)

For each target file, extract each numbered fixture: its **input values** and its **expected output
shape** (components that must be present, numeric bounds, prohibitions). A fixture missing either half
is marked `UNREPLAYABLE`, logged, and skipped — never guess the missing half.

**Gate**: none beyond well-formedness. **Failure behavior**: `UNREPLAYABLE` fixtures continue the run;
they still get a log line.

## Stage 3 — Execute Blind (model-dependent)

Dispatch **one fresh-context probe agent per fixture** (Agent tool). The probe receives ONLY the v2
prompt body plus the fixture's input values — **never the expected shape, never sibling fixtures'
outputs**. The conductor holds the answer key; a probe that can see the target can teach to the test.

**Gate — cost**: if executing a fixture would call a paid, cost-gated API (Fal, Seedance, deep-research
etc.), do not dispatch — log the fixture as `SKIPPED_COST` and move on. Replay must stay free to run.

**Failure behavior**: probe error or non-response → one retry with the identical payload; second
failure → log `ERROR` with the error text, continue to the next fixture. No fixture blocks the run.

## Stage 4 — Judge Shape (conductor; rule-bound)

The conductor — never the probe — diffs each output against its expected shape:

- **Components**: each named section/element scored present/absent, binary, with the evidence quoted.
- **Bounds**: every numeric constraint (≤N, ≥N, "exactly N", "one decision not two") **counted**, not
  eyeballed. State the measured number next to the bound.
- **Prohibitions**: "not both", "no X" clauses checked explicitly.
- **Never exact wording.** Phrasing, style, and word choice are out of scope; two wildly different
  texts with the same components and bounds both PASS.

Verdict per fixture: **PASS** (all components present, all bounds hold, no prohibition violated) ·
**DRIFT** (all components present but ≥1 bound violated or a component materially thinner than the
shape demands) · **FAIL** (≥1 component absent or a prohibition violated). Every non-PASS verdict must
quote the specific deviation. **Failure behavior**: if the conductor cannot decide a verdict from the
rules above, the verdict is `DRIFT` with reason "shape underspecified" — ambiguity is drift in the
fixture, and the fix routes to the fixture text, not to a generous PASS.

## Stage 5 — Log (deterministic)

Append one JSON line per fixture (including `NO_FIXTURES`, `UNREPLAYABLE`, `SKIPPED_COST`, `ERROR`) to
**`.agent/fixture-replay-log.jsonl`**:

```json
{"ts": "<ISO-8601>", "run_id": "<skill>-<date>-<n>", "skill": "<skill>", "prompt": "<v2 filename>",
 "fixture": <n>, "model": "<model-id>", "verdict": "PASS|DRIFT|FAIL|NO_FIXTURES|UNREPLAYABLE|SKIPPED_COST|ERROR",
 "deviation": "<quoted specific deviation, or null for PASS>"}
```

**Gate — completeness**: lines appended must equal fixtures discovered (plus one for `NO_FIXTURES`
runs). **Failure behavior**: a fixture that was judged but cannot be logged blocks closeout —
stop-and-surface; an unlogged verdict is the AI-memory-dependent observability this workflow exists
to kill.

## Stage 6 — Route Drift

- **All PASS** → report clean, one-line summary per prompt, done.
- **DRIFT/FAIL, cause is obvious prompt text** → fix same-session, re-run that fixture once (new log
  line, same run_id), report before/after.
- **DRIFT/FAIL, cause not obvious** → count this skill's documented non-PASS lines in the log:
  `grep '"skill": "<skill>"' .agent/fixture-replay-log.jsonl | grep -cv '"PASS"'`. **≥3** → route to
  `/skill-anneal` with those log lines as its required failure examples. **<3** → surface the finding;
  the log line stands as documented failure #N toward the anneal threshold.
- **Same drift pattern across many skills on a new model** → the prompt isn't broken, the model
  dialect is unmapped: route to `/dialect-probe` (re-probe, diff the card) before touching prompts.

**Failure behavior**: never leave a non-PASS verdict unrouted — every one ends in a fix, an anneal
dispatch, a dialect re-probe, or an explicit "documented, below threshold" statement.

## Boundaries

- Never edit a fixture's expected shape to make a run pass; shape changes ride prompt changes, stated.
- Never let a probe agent see the expected shape, sibling outputs, or score itself.
- Never judge by exact wording — components, bounds, prohibitions only.
- Never delete or rewrite existing lines in `.agent/fixture-replay-log.jsonl`; append-only.
- Never trigger cost-gated paid APIs during replay; `SKIPPED_COST` instead.
- Never substitute conversational memory of a past replay for the log — the log is the record.

## Verification

Deterministic proofs a run completed honestly:

1. **Log completeness**: `tail -n <N> .agent/fixture-replay-log.jsonl | grep -c '"run_id": "<run_id>"'`
   equals the fixture count discovered in Stage 1.
2. **Pre-gate ran**: the report states the `renaissance_audit.py --quiet` counts for this run.
3. **No naked verdicts**: every non-PASS line has non-null `deviation`:
   `grep '"<run_id>"' .agent/fixture-replay-log.jsonl | grep -v '"PASS"' | grep -c '"deviation": null'` → 0.
4. **Routing stated**: the report names the Stage 6 outcome for each non-PASS fixture.

## Fixtures

1. Input: `/fixture-replay forge-os --model claude-haiku-4-5` (7 v2 prompts, 6 fixture-bearing) →
   Expected shape: audit counts stated; one probe agent per fixture, dispatched blind; per-fixture
   verdict table with counted bounds; every non-PASS quotes its deviation; log lines appended ==
   fixtures discovered, all carrying the same run_id; Stage 6 routing named for each non-PASS.
2. Input: `/fixture-replay some-skill` where the skill has no `## Fixtures` sections → Expected shape:
   NO probe agents dispatched; exactly one `NO_FIXTURES` log line; report says not-born-instrumented
   and points to the prompts-v2 fixture backfill; no invented fixtures anywhere.
