# Handoff: Capability Stewardship Default - Phase 1

## Purpose

- **Next session should do:** run a fresh-session Google-local smoke test and review the visible recommendation quality.
- **Not in scope:** Phase 2 global `~/.codex` writes, task creation, real subagents, external actions, or Angle Map / LinkedIn work.

## Load First

- `semantic_libraries/antigravity/primitives/operating-alignment-contract.md` - lifecycle source of truth.
- `semantic_libraries/antigravity/primitives/co-creative-launchpad-contract.md` - packet and visible recommendation fields.
- `.agent/workflows/autopilot.md` - start, mid-session, and closeout behavior.
- `.agent/run-receipts/latest.md` - latest proof boundary and remaining red items.

## What Changed

- Persistent capability/session-lifecycle language now routes to `/system-audit`; mentioning closeout as one lifecycle phase no longer invokes `/end-session`.
- Genuine current-session wrap requests still route to `/end-session`.
- Raw Intent, the Co-Creative Launchpad, Google preflight, Autopilot preflight, Orchestration Receipt, and persisted Run Receipt now carry `container_decision`, `capability_move`, `why_now`, and `approval_boundary`.
- Mid-session signals choose one of: continue, bounded support, verify, handoff, fresh pen, recommend new task, preserve, or monitor.
- Tiny mechanical turns stay quiet. User-owned tasks and real subagents are never created automatically.
- Existing `/handoff`, `/fresh-pen`, steering, and Operator Lesson surfaces remain the transfer and closeout owners.

## Regression Proof

| Behavior | Result |
|---|---|
| Exact lifecycle/default request -> `/system-audit` | PASS |
| Natural capability-awareness request -> `/system-audit` | PASS |
| Genuine wrap/closeout request -> `/end-session` | PASS |
| Tiny mechanical edit remains quiet | PASS |
| Distinct branch -> focused handoff; no task creation | PASS |
| Durable branch -> new-task recommendation; no task creation | PASS |
| Two rejected taste revisions + heavy context -> `/fresh-pen` | PASS |
| More than three experts -> one owner + bounded support | PASS |
| Safe local verifier -> execute verifier | PASS |
| External publish/send -> prepare, then request approval | PASS |
| Repeating one-off -> preserve smallest reusable system | PASS |
| Raw Intent lifecycle packet | PASS |
| System integrity (`verify_system.py --errors-only`) | PASS - all clear |
| Google Operator Core | PARTIAL - implementation checks pass; current worktree hook trust is absent in global Codex config |
| Wider control-plane verifier | PARTIAL - reaches and passes the new Autopilot suite, then stops on a pre-existing intent-memory/cohesion-state mismatch |

## Remaining Boundary

- Do not edit global Codex hook trust or install a global Capability Stewardship bridge without new explicit approval.
- The archived Agentic Engineering verifier has a stale internal path and was not revived to force a green result.
- Preserve the unrelated pre-existing `.agent/sessions/solution-injections.jsonl` change.

## Exact Fresh-Session Smoke Prompt

```text
I want you to help naturally without making me remember commands. Start by choosing one owner and the best work container. If a distinct branch, context fatigue, a useful verifier, too many experts, an external action, or a reusable-system opportunity appears, surface one plain-English recommendation with why now, what you can do, and any approval boundary. Keep tiny turns quiet and do not create another task or deploy real subagents automatically.
```

## Acceptance Criteria

- A meaningful fresh session exposes one capability move only at a material fork.
- A five-minute mechanical turn has no capability lecture or forced steering.
- No global write, task creation, subagent deployment, publish/send action, or connector write occurs without its existing approval.
