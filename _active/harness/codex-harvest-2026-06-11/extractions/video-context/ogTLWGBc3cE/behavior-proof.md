# Co-Creative Launchpad Behavior Proof

## Source Boundary

This proof uses the public YouTube extraction package for `ogTLWGBc3cE`, including transcript-backed evidence and local Nate B. Jones intent/orchestration skill surfaces. Private Substack or member examples were not used or claimed.

## Behavior Target

Raw intent such as "co creative launching pad intent alignment apex before build raw intent" should route into the shared front-door intent layer, not an unrelated creative-intent workflow. Source-system requests such as "turn this video source into a co-creative launchpad OS for the harness" should route into `/source-to-skill-system`.

## Implementation Delta

The harness now has a shared `co-creative-launchpad-contract.md` primitive and deterministic `co_creative_launchpad.py` helper. Autopilot and Virtuoso render the same Launchpad Packet before route/execution decisions, while `/align`, `/validate-intent`, `/refine-intent`, `/jcc-refine`, and `/source-to-skill-system` reference the same contract rather than maintaining separate intent logic.

## Routing Proof

Test query:

```text
co creative launching pad intent alignment apex before build raw intent
```

Observed result:

- Routing governor lane: `front-door-choice`
- Chosen route: `/autopilot`
- Command menu winners start with `/autopilot`
- Workflow router winners start with `/autopilot`
- `/nijhof-intent-creative` is flagged/skipped instead of winning

Source-system test query:

```text
turn this video source into a co-creative launchpad OS for the harness
```

Observed result:

- Routing governor lane: `skill-system`
- Chosen route: `/source-to-skill-system`
- Required candidates include `/source-to-skill-system`, `/extraction-governor-agent`, and `/autopilot`

## Launchpad Proof

The Autopilot preflight now renders `## Co-Creative Launchpad` before `## Autopilot Trace` and includes:

- `predicted_need`
- `center`
- `edges`
- `success_standard`
- `missing_inputs`
- `questions_that_change_execution`
- `route_bias`
- `pause_or_run`
- `handoff`

For the raw launchpad query, the packet runs with assumptions instead of pausing just because the phrase contains "co-creative." Taste-heavy requests still pause when the quality bar is execution-changing.

## Proof Standard

This change is behavior-changing only if future raw-intent starts produce a better launchpad, clearer route, sharper questions, and faster local execution without requiring Farrice to memorize another command. Current proof covers route choice, output sections, helper schema, workflow references, and verifier coverage.

## Validation Run

Passed:

- `python3 execution/verify_autopilot_runtime_preflight.py`
- `python3 execution/verify_autopilot_routing.py`
- `python3 execution/verify_virtuoso_orchestration.py`
- `python3 execution/verify_skill_system_contract.py`
- `python3 execution/verify_behavior_changing_extraction_contract.py`
- `python3 execution/verify_system_control_plane.py`
- `python3 execution/codex_live_surface_audit.py --strict`
- `python3 execution/codex_harness_check.py`
- `python3 execution/artifact_surface_guard.py semantic_libraries/antigravity/primitives/co-creative-launchpad-contract.md`
- `python3 execution/export_format_guard.py semantic_libraries/antigravity/primitives/co-creative-launchpad-contract.md`
- `python3 execution/artifact_frontmatter_guard.py semantic_libraries/antigravity/primitives/co-creative-launchpad-contract.md`
- `python3 execution/artifact_router.py enforce semantic_libraries/antigravity/primitives/co-creative-launchpad-contract.md`
- `python3 execution/artifact_router.py enforce extractions/video-context/ogTLWGBc3cE/behavior-proof.md`

## Remaining Risk

The deterministic helper is heuristic. It should be tuned from real sessions after repeated examples show a specific class of false pause, false run, weak center, or weak question.
