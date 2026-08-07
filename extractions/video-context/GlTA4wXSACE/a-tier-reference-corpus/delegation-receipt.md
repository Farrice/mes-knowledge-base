# Blind Replay Delegation Receipt

## Integration Owner

The main Codex thread owns source selection, held-out references, judging, all file edits, regression conversion, and final validation.

## Worker Boundary

Six fresh-context, read-only workers each receive one normalized brief. Every worker is prohibited from reading:

- `corpus-manifest.json`, `reference-seal.json`, `router-scope-seal.json`, and `rubric.md`;
- any `reference.md`, replay, evaluation, regression, transcript, or prior fixture;
- the source paths named inside the brief;
- any other case brief;
- the parent conversation or another worker's output.

Workers may read only the shipped router surface, their assigned brief, and—after dosage selection—the selected existing production-owner files. They may load Farrice's voice card only when the brief names Farrice as the voice owner. Workers do not write files, change state, score their own work, or finalize the run.

## Dispatch Plan

| Packet | Case | Domain | Wave | Expected return |
|---|---|---|---|---|
| BR-FND-01 | FND-01 | Founder | 1 | One complete asset and Story Deployment Receipt |
| BR-SAL-01 | SAL-01 | Sales | 1 | One complete asset and Story Deployment Receipt |
| BR-HLT-01 | HLT-01 | Health | 1 | One complete asset and Story Deployment Receipt |
| BR-TEC-01 | TEC-01 | Technical | 2 | One complete asset and Story Deployment Receipt |
| BR-EDU-01 | EDU-01 | Educational | 2 | One complete asset and Story Deployment Receipt |
| BR-OPS-01 | OPS-01 | Operational | 2 | One complete asset and Story Deployment Receipt |

## Acceptance and Rejection Policy

- Worker output is evidence, not a verdict.
- The main thread saves the returned text verbatim before evaluation.
- Any context-boundary breach makes the replay `INVALID` and becomes a protocol regression fixture.
- Any dosage, fidelity, domain-fit, restraint, usefulness, or recognition failure becomes a case-specific regression fixture before a repair.
- Repairs may strengthen an existing router or production-owner contract but may not add a route, expert, decision label, or second body owner.

## Dispatch Results

| Worker | Case | Accepted output | Rejected output | Risk/result |
|---|---|---|---|---|
| `/root/blind_fnd_01` | FND-01 | Full asset and receipt | None | Valid blind PASS |
| `/root/blind_sal_01` | SAL-01 | Dosage, HVC proof boundary, offer facts, CTA | Unsupported ICP Tell process; silent owner-contract override | Two fixtures; repair dispatched |
| `/root/blind_hlt_01` | HLT-01 | Dosage, evidence spine, dated metrics, trial boundary | Invented narrator attitude; silent owner-contract override | Two fixtures; repair dispatched |
| `/root/blind_tec_01` | TEC-01 | Full direct memo and receipt | None | Valid blind PASS |
| `/root/blind_edu_01` | EDU-01 | Full educational asset and receipt | None | Valid blind PASS |
| `/root/blind_ops_01` | OPS-01 | Full direct handoff and receipt | None | Valid blind PASS |
| `/root/repair_hlt_01` | HLT-01 repair | Full bounded post and receipt | None | Both fixtures repaired; final PASS |
| `/root/repair_sal_01` | SAL-01 repair | Process trace, bounded subset, offer and proof fidelity | `FULL STORY` upgrade | Original fixtures repaired; new dosage fixture pending |

No worker edited files, read a held-out reference, followed a source path from a brief, saw another case, or scored its own output. The main thread saved every response verbatim and owns all verdicts.
