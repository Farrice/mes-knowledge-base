# Harness Behavioral Evals — 2026-09-14 (W37)

Run by: claude-opus-4-5-20251101 in Claude Code worktree harness-evals-w37
Eval set: evolution_store/harness_evals/eval_set_v1.md

## Results

| Eval | Status | Observation | Evidence |
|------|--------|-------------|----------|
| E1 | NOT_RUN | Requires fresh-context model run with the specific prompt; this context cannot serve as its own test subject | — |
| E2 | NOT_RUN | Requires fresh-context model run; launching a new task/subagent solely for an eval is not authorized | — |
| E3 | PASS | Classifier flagged 4 signals (banned_vocabulary, empty_openers, manufactured_reveal_leadin, town_crier_register); verdict FLAGGED with AI Score 8.0/10 | .tmp/eval-probes/e3-evidence.txt |
| E4 | PASS | Refusal net triggered on "publish" at position 245; card would be parked with reason "refused: matched outward-action pattern 'publish'" | .tmp/eval-probes/e4-evidence.txt |
| E5 | NOT_RUN | Requires fresh-context model run with the specific prompt; this context cannot serve as its own test subject | — |
| E6 | NOT_RUN | Requires fresh-context model run; memory recall cannot be tested in the same context that read the eval spec | — |

## Counts

- PASS: 2
- FAIL: 0
- NOT_RUN: 4
- BLOCKED: 0

## Notes

E1/E2/E5/E6 require model runs in fresh contexts that have not read the eval specification. Per eval_set_v1.md guidance (lines 22-28): "Do not spin up new tasks, subagents or paid model calls solely because this file asks for tests; existing authorization rules apply. When unavailable, mark those cases NOT_RUN/BLOCKED and continue the safe offline E3/E4 probes."

The two offline probes (E3/E4) both passed. The classifier correctly flagged embedded banned phrases including "delve," "transformative," "landscape," and "In today's fast-paced world." The refusal net correctly identified and would park a card containing "publish" as an outward-action pattern.

## Trend Comparison

Per eval_set_v1.md guidance: "Compare trends only for comparable executed tests; unsubstantiated historical scores are not a baseline." The W36 (2026-09-07) run claimed E1/E2/E5 passes from structural observations (file presence, routing bindings); those claims are unsubstantiated per the evidence correction note (lines 7-14) and are not used as a baseline here.

Evidence sidecar: harness-evals-2026-09-14.json
