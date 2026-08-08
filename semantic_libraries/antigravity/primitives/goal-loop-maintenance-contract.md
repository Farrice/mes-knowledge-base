# Goal-Loop Maintenance Contract

## Purpose

Use this primitive when Codex Antigravity is improving itself: workflows,
skills, routing rules, command bridges, maintenance queues, or recurring
health loops. The goal is to turn "make the system better" into a bounded
goal-loop with a target, proof, stop condition, evaluator, and safety cap.

This contract is adapted from Mark Kashef's self-improving OS source package:

- YouTube: `https://www.youtube.com/watch?v=5xrjO38WUYY`
- Local PDF: `/Users/farricecain/Downloads/Mark Kashef-goal_cookbook.pdf`
- Local prompt zip: `/Users/farricecain/Downloads/Mark Kashef-Raw Text Prompts.zip`

## When To Use

- `/self-evolve`, `/skill-anneal`, or `/skill-evolution` would change a skill,
  workflow, router, prompt, or verifier.
- `/autopilot` or `/system-audit` identifies a self-improvement or maintenance
  path.
- `/repeatability-spine` turns a failed route, failed revision, or regression
  into an evolution search set.
- A maintenance automation proposes cleanup, forge, archive, or queue updates.

Do not use this for ordinary one-off answers, simple local tests, or read-only
inspection that does not produce an improvement recommendation.

## Goal Packet

Every mutation-capable self-improvement run must define this packet before
editing files or deploying variants:

The plain-language checks are: proof artifact, measurable stop, turn cap,
evaluator, wake-up check, and rollback/archive rule.

| Field | Requirement |
|---|---|
| `target` | Exact file, workflow, skill, queue, route, or system surface. |
| `scope` | Items included and excluded. |
| `per_item_criteria` | Concrete decision rule for each item in scope. |
| `permitted_side_effect` | What may change: edit, archive, queue, report, or no-op. |
| `proof_artifact` | File, report, log, verifier output, or queue entry the evaluator can inspect. |
| `measurable_stop` | Checkable stop condition, not "good enough". |
| `turn_cap` | Safety limit for loops or iterative runs. |
| `evaluator` | Rubric, verifier, test inputs, or external judge rule. |
| `wake_up_check` | Exact command or review surface for future resumption. |
| `human_checkpoint` | Where the chain pauses for approval or why approval is already satisfied. |
| `rollback_or_archive_rule` | How to recover: archive-never-delete, revert, discard variant, or queue-only. |

If any field is missing, the run can still produce a diagnosis or draft packet,
but it cannot deploy a mutation.

## Retro Before Rule (SHADOW)

Use the `Learn` decision from
`systems-thinking-expertise-intelligence-overlay.md` when a failure creates
pressure to add permanent process. First run a blameless reflection on the
assumption, decision, source truth, handoff, owner, and changed behavior. Add a
durable gate only for a demonstrated recurring need or a hard truth, proof,
privacy, safety, or permission veto. This advisory check must not weaken those
vetoes or block the nearest safe continuation.

## Evolution Council Preflight

Before `/self-evolve`, `/skill-anneal`, or `/skill-evolution` mutates a target,
run a compact Mark Kashef-style council locally unless the user explicitly
authorized real Codex subagents for that run.

| Role | Mandate | Output |
|---|---|---|
| Forager | Must compress source evidence, failure logs, and current target into a digest. | `Forager Digest` |
| Architect | Must propose the smallest change that could satisfy the goal packet. | `Build Hypothesis` |
| Skeptic | Must identify failure modes, overfitting risks, and missing proof. | `Risk Review` |
| Implementer | Must name touched files and preserve existing contracts. | `Change Scope` |
| Evaluator | Must define stop checks, no-regression checks, and wake-up checks. | `Evaluation Plan` |

The preflight must produce a single **Evolution Council Verdict**:

```markdown
## Evolution Council Verdict
- **Target**:
- **Goal packet complete**: yes/no
- **Recommended path**: queue-only / anneal / self-evolve / skill-evolution / no-op
- **Permitted side effect**:
- **Proof artifact**:
- **Stop condition**:
- **No-regression check**:
- **Human checkpoint**:
- **Open risk**:
```

Unanimous agreement is not enough. The Skeptic must name at least one plausible
failure mode, or the verdict is incomplete.

## Safety Rules

- Queue-first by default: candidates and variants are proposed before they are
  applied.
- Archive, quarantine, or cold-store before delete.
- Do not change global `~/.codex` or external workspaces until local proof is
  clean and the user explicitly approves the broader mutation.
- Do not claim freshness from manually edited reports. Freshness comes from a
  real run, verifier output, or current source scan.
- Do not let a live status command rebuild fresh counts in memory while the
  persisted queue remains stale without flagging the mismatch.
- Do not generate new skills from session history directly into the hot surface.
  Forge outputs are draft candidates until reviewed.

## Source Pattern Mapping

| Mark Kashef source pattern | Codex Antigravity translation |
|---|---|
| Clean | Audit hot/cold skill surface, archive-never-delete, manifest every move. |
| Sharpen | Rubric and test inputs before skill edits, fix lowest failing criterion without regression. |
| Revive | Give dormant projects/workflows verdicts: keep, queue, retire, blocked. |
| Forge | Detect recurring prompt patterns and propose draft skills with smoke tests. |
| Maintain | Run heartbeat reports that converge toward small diffs, never fake freshness. |

## Validation

Goal-loop changes should be verified with:

```bash
python3 execution/verify_goal_loop_maintenance_contract.py
python3 execution/verify_skill_evolution_candidates.py
python3 execution/verify_skill_evolution_local_first.py
python3 execution/verify_system_control_plane.py
python3 execution/verify_autopilot_routing.py
```

If candidate freshness is involved, also run:

```bash
python3 execution/verify_skill_evolution_candidate_freshness.py
```

## Last Updated

2026-08-08
