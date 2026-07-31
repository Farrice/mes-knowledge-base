# Co-Creative Launchpad Contract

## Purpose

Use this primitive before meaningful execution when raw intent, creative
direction, system work, source harvesting, strategy, or ambiguous operator
judgment should become a better shared starting point.

The launchpad is not a slower planning mode and not a separate expert skill. It
is the shared intent layer that Autopilot, Virtuoso, Align, Validate Intent,
Refine Intent, JCC Refine, and Source-to-skill-system use before they route,
ask, or execute.

## Source Boundary

This contract is grounded in:

- Public YouTube source: `https://www.youtube.com/watch?v=ogTLWGBc3cE`
- Local evidence package: `extractions/video-context/ogTLWGBc3cE/`
- Existing local Nate B. Jones skills for intent, context, and orchestration
  engineering.

Do not claim access to Nate B. Jones paid membership, Substack prompts, private
examples, or unavailable source material unless Farrice supplies them in the
current workspace. Mark those as unavailable rather than enriching from
inference.

## Launchpad Packet

Every launchpad pass should produce these fields:

| Field | Requirement |
|---|---|
| `predicted_need` | What the user probably needs, stated before interrogation. |
| `center` | The flashlight center: the main outcome the work should optimize for. |
| `edges` | The boundaries, tradeoffs, and nearby risks that change execution. |
| `success_standard` | What good looks like in observable terms. |
| `constraints` | Explicit and inferred constraints, including risk and source limits. |
| `missing_inputs` | Inputs that would materially change execution if absent. |
| `questions_that_change_execution` | Only questions whose answers alter route, scope, risk, taste, or proof. |
| `route_bias` | The front door or support route the launchpad is leaning toward. |
| `pause_or_run` | Whether to run with assumptions, pause for judgment, or block for risk. |
| `container_decision` | One move: continue, bounded-support, verify, handoff, fresh-pen, recommend-new-task, preserve, or monitor. |
| `capability_move` | One plain-English recommendation plus the concrete action Codex can take; quiet when no leverage fork exists. |
| `why_now` | The outcome, context, speed, proof, or compounding reason the move matters now. |
| `approval_boundary` | The exact boundary if task creation, subagents, external writes, paid tools, destructive action, connectors, publishing, automation, or global writes are involved. |
| `handoff` | Compact packet the next route receives; do not pass full transcript dumps. |

## Operating Standard

1. Predict first. State the likely underlying need before asking questions.
2. Name the center. Make the desired outcome sharper than the raw request.
3. Name the edges. Surface constraints, taste calls, risks, source boundaries,
   and what should not be optimized.
4. Define "good." Turn vague excellence into acceptance criteria, proof, or a
   review surface.
5. Separate data, opinion, and source truth. Data/files are evidence; Farrice's
   judgment and taste are operator signal; unavailable sources stay unavailable.
6. Ask only execution-changing questions. Do not ask questions merely because
   the request could be clearer.
7. Push back like a senior partner. If the likely path is weaker than another
   route, say so and select the stronger route.
8. Preserve speed. If the ambiguity affects polish but not execution, state the
   assumption and run.
9. Steward capabilities quietly. Surface one recommendation only when a better
   container, bounded support gate, verifier, transfer, monitor, or reusable
   asset materially changes the outcome.
10. Do not auto-split tasks. A handoff or new-task packet may be prepared
    locally, but a user-owned task is created or opened only after explicit
    approval.

## Pause Rules

Pause for judgment when:

- the deliverable, audience, success standard, or source boundary would change
  the chosen route,
- the request asks for a taste-heavy or high-stakes decision and the standard is
  not inferable,
- multiple routes would produce materially different artifacts,
- the next action is external, paid, destructive, global, public-facing,
  connector-writing, or real-subagent work,
- private source material would be needed but is unavailable.

Run with assumptions when:

- the goal, route, and reversible first action are clear enough,
- missing details affect refinement more than execution,
- the work is workspace-local, additive, reversible, and verifiable,
- the launchpad can produce a proof plan before touching risky surfaces.

## Route Integration

- `/autopilot` owns raw intent, route choice, safe local action, and run
  receipts.
- `/virtuoso` inherits the same Launchpad Packet and composes owner, stack,
  gates, delegation packets, and proof around it.
- `/align`, `/validate-intent`, `/refine-intent`, and `/jcc-refine` use this
  same contract for question selection and intent sharpening.
- `/source-to-skill-system` uses this contract when source material should
  improve the harness, prompt layer, agent behavior, or reusable operating
  surface.
- `/extraction-governor-agent` remains the read-only source-to-capability triage
  lane before build decisions.

## Behavior Proof

This contract changes behavior only if a future run shows:

- a raw or vague prompt produces a Launchpad Packet,
- routing improves toward `/autopilot` or `/source-to-skill-system` when
  launchpad/source-to-system intent is present,
- only execution-changing questions are asked,
- safe local work still runs when ambiguity is not execution-changing,
- the final handoff includes proof, route, and source limits.
- a tiny mechanical turn keeps `capability_move.visible` false,
- a material fork produces one container decision, one reason, one action, and
  the applicable approval boundary.

## Last Updated

2026-05-29
