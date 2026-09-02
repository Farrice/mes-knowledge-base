# Mood Board Orchestrator Cold-Start Proof

> Historical baseline: this proof predates the Brand Direction Decision Spine
> added on main. The integrated authority routes discovery-backed brand direction
> to Andrew Lane and standalone visual-board construction to `/mood-board`.

## Test Input

> Build a high-taste mood board from this discovery brief, with three materially different visual territories, real references, a blind taste choice, and one proving surface.

## Before Repair

| Surface | First route | `/mood-board` position | Behavior consequence |
|---|---|---:|---|
| `command_menu.py` | `/creative-brief-gen` | 6 | A generic brief owner beat the explicit moodboard front door. |
| `workflow_router.py` | `/moodboard-conversation-system` | 7 | One sign-off component beat the missing end-to-end conductor. |
| `/mood-board` output contract | Five-layer written brief plus three image prompts | N/A | The route could finish without actual boards, reference research, a proving surface, or a human taste decision. |

## After Repair

| Surface | Result | Evidence |
|---|---|---|
| `command_menu.py` | `/mood-board` ranks first | score exceeds 50,000 through the narrow `mood_board_orchestrator` binding |
| `workflow_router.py` | `/mood-board` ranks first | output carries `[BINDING — mandatory route]` |
| Routing enforcer | `/mood-board` accepted; `/creative-brief-gen` rejected | checked across eight positive fixtures, including natural discovery-to-moodboard word orders |
| Negative controls | no moodboard binding fires | existing moodboard library, approved-board-to-DESIGN.md, production-from-approved-board, and full BOS requests |
| Runtime contract | connected behavior | reference ledger → three actual visual boards → same proving surface A/B/C → blind choice → selected-direction handoff |
| False-green boundary | explicit | text-only output is `PARTIAL`; proving-surface prose is `UNBUILT`; human taste and market outcomes remain `UNTESTED` |

## Behavior Delta

The repaired route cannot successfully terminate at the artifact shape that
failed the user test. It must either produce inspectable visual evidence and
actual boards, or disclose the missing evidence/tool state as `PARTIAL`. It
also prevents Andrew Lane's decision-documentation method and Oren's
conversation component from becoming accidental front-door owners.

## Validation

```text
PASS — mood-board orchestrator: 8 positive routes, 4 negative controls, 101 structure/proof assertions
PASS — Renaissance audit: 3,953 v2 prompts, 0 failures
PASS — Skill-system contract verification
PASS — Peer-constitution authority verification
PASS — Autopilot runtime preflight
PASS — Subagent approval language
PASS — Platform compiler lint: failures=[]
PASS — Codex harness check
```

Current unrelated baseline failures are not attributed to this repair:

- Google Operator Core verification reports stale global end-session and
  steering-compass language.
- System Control Plane reaches the global sync check and reports the same
  pre-existing global `~/.codex` alignment gaps.
- Legacy `validate_skill.py` expects obsolete skill layouts and is not used as
  acceptance evidence for this command bridge.

## Remaining Proof Gap

Human taste preference and reduction in revision/approval drift remain
`UNTESTED`. The first real `/mood-board` run must produce three viewable boards
and receive a blind `Choose / Keep / Kill / Reason` verdict before this system
can be called taste-proven.

## Integrated Reconciliation Proof

The current acceptance gate is the union of
`verify_mood_board_orchestrator.py` and
`verify_brand_direction_decision_spine.py`: discovery-backed brand queries must
resolve to Andrew Lane, campaign/product/standalone board queries must resolve to
`/mood-board`, and both retain the same actual-board and proving-surface contract.
