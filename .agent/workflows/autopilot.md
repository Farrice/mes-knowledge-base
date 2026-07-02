---
description: Google-local Codex front door for intent lock, route choice, safe execution, proof, and closeout
---

# /autopilot - Codex Intent-To-Outcome Front Door

Autopilot is the Google Antigravity front door for raw intent. It turns a messy
request into one owner route, bounded support gates, the first safe local action,
verification, and a run receipt. It is not a competing router and not the older
gate-suppressed mission dispatcher.

For substantial operator/system work, start with the local preflight:

```bash
python3 execution/codex_operator_preflight.py "<raw intent>" --plain
```

Follow the `local_next_action` when it is safe, local, and verifier-backed.
Pause only for external writes, destructive cleanup, paid/quota-heavy tools,
global `~/.codex` edits, Codex Antigravity mutation, publishing/outreach,
connector writes, or real Codex subagents.

## Usage

```bash
/autopilot [raw context]
/autopilot --plan [raw context]
/autopilot --menu [raw context]
```

Default behavior is execute-safe-local-work. `--plan` stops at a
decision-complete plan. `--menu` is for cases where Farrice explicitly wants
ranked options.

## Routing Owner Rules

- Broken, drifted, noisy, not-firing, route/hook/default/wiring, Codex/Claude
  parity, or execution-bias complaints route to `/system-audit`.
- Prior-session, golden-run, caliber drift, or "lost the good part" complaints
  route to `/repeatability-spine`.
- More than three plausible experts/routes route through
  `/expert-composition-governor` as a support gate, not an expert soup default.
- Council, deliberate cross-domain judgment, and collective-genius requests route
  to `/convene`.
- Steering and next-prompt coaching route to `/steering-compass`; persistent
  closeout behavior is global and should not hijack system repair.
- `source-command-jcc-refine` is an intent-refinement support path only. It can
  sharpen ambiguity, but it does not own system repair, route wiring, hooks, or
  Claude-parity complaints.

## Execution Sequence

1. Capture the raw intent.
2. When Farrice says he does not know how to ask Codex, gives messy context, or
   asks for a prompt-engineering bridge, compile the raw-intent run packet:
   `python3 execution/raw_intent_run_packet.py "<raw intent>" --plain`.
3. Build the preflight packet with `execution/codex_operator_preflight.py`.
4. Confirm the chosen owner with the workflow router and routing enforcer. Use
   `routing_enforcer.py check --no-log` for probes and verifier checks.
5. If the owner is `/system-audit`, run proof-first local diagnosis before
   patching: route probes, hook probes, bridge checks, registry/index health,
   and the relevant verifier.
6. Patch only the Google-local owner surface needed to change behavior.
7. Rerun the targeted verifier set.
8. Write or update a run receipt for meaningful system work.
9. Close with proof, remaining risks, and concrete next prompts.

## Raw Intent Virtuoso Bridge

The Raw Intent Virtuoso Bridge is the local companion layer for under-specified
operator starts. It is not a new hot command and not a plugin-first path.

Use it when the request contains rough intent, messy context, "I do not know how
to ask Codex," prompt-engineering bridge language, or broad entrepreneurial work
where the system should translate the first attempt into an executable packet.

```bash
python3 execution/raw_intent_run_packet.py "<raw intent>" --mode auto --plain
python3 execution/raw_intent_run_packet.py "<raw intent>" --mode revenue --plain
python3 execution/raw_intent_run_packet.py "<raw intent>" --mode creative --plain
python3 execution/raw_intent_run_packet.py "<raw intent>" --mode system --plain
```

The bridge must output predicted need, center, quality bar, chosen route,
support gates, composition slots, context plan, execution decision, first safe
action, verification plan, operator run prompt, and deferred plugin verdict.
Plugin packaging remains deferred until local cold-start proof passes.

## Safety Boundaries

- Do not edit `.claude/` for Codex parity repairs.
- Do not edit `~/.codex` without explicit approval.
- Do not mutate `/Users/farricecain/Codex Antigravity` from this workspace.
- Do not spawn real Codex subagents without explicit run-specific authorization.
- Real Codex subagents, when authorized, are read-only diagnostics by default:
  no further subagents, and the main thread owns all edits, synthesis, and
  integration.
- For research fan-out, add to fan-out list only if Farrice has explicitly authorized it for this run; otherwise run the research angles sequentially in the main thread.
- Any authorization packet must name worker count, read-only scope, deny list, halt condition, and no further subagents.
- Treat "without breaking my workspace" as a safety constraint: keep the first
  action local, reversible, and verifier-backed.

## Proof Standard

Autopilot work counts as repaired only when the route, hook, verifier, and
visible behavior agree. For routing/wiring repair, the minimum proof set is:

```bash
python3 execution/verify_codex_claude_parity.py
python3 execution/verify_google_operator_core.py
python3 execution/verify_system.py --errors-only
python3 execution/run_receipt.py --verify
```

Use narrower checks first while patching, but finish with the full proof set
when the work changes control-plane behavior.

## Operator Core Closeout

Every meaningful Autopilot run closes with persistent per-exchange steering, not
just a run receipt. For substantial work — builds, repairs, audits, or any run
with a real next decision — include **3 Next Prompts** under the Insightful
Momentum standard, keeping the Use Now / Harden / Expand frame and making each
option context-rich and capability-revealing.

Always end with an **Operator Lesson** that teaches the move behind the work, not
just the result, plus:

- **Next-time prompt:** the copy-paste continuation that gets a better result on
  the next run.
- **Subagent worth it?** — would isolated parallel agents have done this better or
  faster, and is that worth invoking next time? Note that real Codex subagents
  require explicit authorization and default to read-only diagnostics.
- **Reuse hook:** the part of this run worth turning into a repeatable skill,
  workflow, or saved prompt.

Skip the full closeout only when Farrice explicitly asks for a terse answer or a
special tool action requires silence.
