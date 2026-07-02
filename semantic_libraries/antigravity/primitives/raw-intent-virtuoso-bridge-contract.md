# Raw Intent Virtuoso Bridge Contract

## Purpose

Use this primitive when Farrice gives rough context, raw intent, or a weak first
prompt and needs Codex to turn it into an executable operating packet before
normal routing.

The bridge is a companion layer over `/autopilot`, `/virtuoso`, and
`/source-to-skill-system`. It is not a new hot command, a global mirror, a plugin
first, or a competing router.

## Packet Shape

Every packet must include:

| Field | Requirement |
|---|---|
| `raw_intent` | The exact user intent being compiled. |
| `predicted_need` | The likely underlying need before interrogation. |
| `center` | The outcome the run should optimize for. |
| `success_standard` | Observable criteria for a good result. |
| `constraints` | Explicit and inferred boundaries, including risk gates. |
| `missing_inputs` | Inputs that would materially change execution. |
| `questions_that_change_execution` | Only questions that change route, scope, risk, taste, or proof. |
| `chosen_route` | One owner route selected for the run. |
| `support_gates` | Bounded support workflows or skills, not an expert pile. |
| `composition_slots` | Spine, Differentiator, Mechanism, Craft, and Risk Gate. |
| `context_plan` | What stays hot, cold, on demand, and skipped. |
| `execution_decision` | Running now, needs judgment, blocked, plan only, or trace status. |
| `first_safe_action` | The next local action or exact run prompt. |
| `verification_plan` | Commands/checks that prove the packet behavior. |
| `operator_run_prompt` | Copy-paste prompt for continuing from the packet. |
| `plugin_packaging_verdict` | Deferred until local cold-start proof passes. |

## Trigger Standard

Trigger the bridge when the request says or implies:

- raw intent, rough intent, messy context, messy notes
- "I do not know how to ask Codex"
- "be my prompt engineer" or "translate this for Codex"
- "get the full capabilities" or "use the full arsenal"
- "bridge," "layer," "run packet," or "companion layer"
- broad entrepreneurial work where the user is asking Codex to select the route

## Route Rules

- Revenue raw intent should route toward `/first-10k`,
  `/revenue-offer-agent`, `/client-acquire`, or their support gates.
- Creative raw intent may pause for taste criteria, but it must surface
  `high-taste-writing-os`, `publishable-copy-gate`, or `excellence-gate` as
  support when relevant.
- System or bridge-building raw intent routes to `/source-to-skill-system` with
  `/autopilot`, `/virtuoso`, `/extraction-governor-agent`, and
  `/expert-composition-governor` as bounded support.
- Plugin language inside a raw bridge request does not make plugin packaging the
  v1 owner. Plugin packaging is deferred until cold-start proof passes.

## Boundaries

- No global `~/.codex` writes in v1.
- No plugin marketplace edits in v1.
- No new standalone plugin in v1.
- No real Codex subagents without explicit authorization.
- No external writes, publishing, paid/quota-heavy tools, or destructive
  cleanup.
- Do not replace the existing routers; compile their evidence.

## Proof

Behavior is proven only when:

- revenue, creative, and system raw-intent fixtures produce useful packets,
- "prompt engineer," "virtuoso," or "world-class" wording does not capture the
  request into unrelated creative-writing routes,
- `/autopilot` and `/virtuoso` expose the bridge in their trace,
- `execution/verify_raw_intent_run_packet.py` passes,
- the existing Autopilot, Virtuoso, and Google operator-core verifiers still
  pass.
