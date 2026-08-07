# Artifact-Only Blind Replay Protocol

## Separation Rule

Each replay worker may read:

1. `skills/shaan-puri-storytelling/SKILL.md`;
2. `skills/shaan-puri-storytelling/references/story-deployment-map.md`;
3. `skills/shaan-puri-storytelling/workflows/shaan-story-deploy.md`;
4. `skills/shaan-puri-storytelling/references/prompts-v2/shaan-story-deploy.md`;
5. exactly one normalized case `brief.md`.

After the worker chooses a dosage, it may read only:

- `genius.md` when a Shaan production route was selected;
- the one selected workflow;
- that workflow's exact v2 prompt;
- Farrice's voice card only when the brief names Farrice as voice owner.

The worker must not read:

- any case `reference.md` or `evaluation.md`;
- another case brief or replay;
- the source video transcript, behavior proof, architecture plan, or earlier synthetic fixtures;
- this protocol's manifest fields that reveal the expected decision;
- any prior worker output, evaluator note, regression fixture, or repair.

## Worker Contract

- Read only the paths explicitly supplied in the delegation packet.
- Do not inspect the surrounding repository for hints.
- Do not write files, finalize, log, score, or mutate the skill.
- Return the complete Final Asset and Story Deployment Receipt in the response.
- Stop after one output; do not self-revise unless the brief itself requires a factual correction.
- State every extra file read. An undeclared read invalidates the blind replay.

## Conductor Contract

1. Seal `reference.md` before dispatch.
2. Save the worker response verbatim under `replays/<case-id>-pass-1.md`.
3. Judge it against the local brief sources, held-out reference, and `rubric.md`.
4. Record `evaluations/<case-id>.json` against `evaluation-schema.json`, with explicit evidence preserved in `judgeNotes`; synthesize the human-readable comparison in `blind-pass-report.md`.
5. For every failure, create `regressions/<case-id>-<failure-slug>.md` before editing any skill file.
6. Make the smallest repair tied to that fixture; do not add a route or load another expert.
7. Run one fresh replay using the same blind boundary and save it as pass 2.
8. If pass 2 fails, leave the case pending and stop broadening.

## Valid Blind Receipt

A blind result is valid only when its delegation receipt names:

- worker;
- exact case slice;
- context read;
- reference paths withheld;
- accepted and rejected output portions;
- risk notes;
- main-thread integration owner.

Self-graded outputs, verdicts without generated/reference paths, and workers exposed to the expected route do not count.
