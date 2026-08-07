# Solution Capture: Expert Composition Standard

Created: 2026-05-10
Mission: expert-composition-standard

Use this while context is fresh. If the learning is generalizable, copy or convert it into `docs/solutions/`.

## Track
- Type: workflow / architecture

## Symptoms Or Context
- The user repeatedly saw the system name many experts, commands, and gates while the final deliverable still felt generic, flat, or stitched together.
- Autopilot and related routes could surface the right ingredients without proving that they were interwoven.
- The underlying problem was not missing expertise; it was missing composition.

## What Did Not Work
- Adding more expert names.
- Saying a copy gate or expert stack was used without showing what changed.
- Letting broad Autopilot, Mission, or Orchestrate routes stop at strategy when the user needed owner-led integration.
- Treating local routing hits as sufficient proof of quality.

## Working Solution Or Durable Guidance
- Create `/expert-composition-governor` as a system-wide route.
- Use one owner and bounded specialists.
- Assign specialists to contribution slots: Spine, Differentiator, Mechanism, Craft, Risk Gate.
- Require specialist handoffs to name top changes, affected section/line/decision, preservation notes, and downstream risk.
- Require the integration owner to merge accepted changes into one coherent output.
- For high-stakes work, include a Composition Ledger with evidence of change and skipped-expert reasons.

## Why This Works
- It converts the expert library from a list of possible influences into a controlled production system.
- It prevents role overlap by forcing slot decisions before execution.
- It makes hidden routing observable through the Composition Ledger.
- It avoids false quality scores by tying improvement to changed artifacts, not expert count.

## Prevention Or Reuse
- Route "expert soup," "too many agents," "not interwoven," "hammer instead of scalpel," "full arsenal," and related intent through `/expert-composition-governor`.
- Run `python3 execution/verify_expert_composition_standard.py` after system routing changes.
- Reuse the contract for any task where more than three experts/skills/workflows are plausible.

## Generalization Decision
- Keep mission-local: no.
- Promote to `docs/solutions/`: yes, `docs/solutions/expert-composition-standard.md`.
