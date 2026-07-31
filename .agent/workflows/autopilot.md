---
description: Google-local Codex front door for intent lock, route choice, safe execution, proof, and closeout
---

# /autopilot - Codex Intent-To-Outcome Front Door

Autopilot is the Google Antigravity front door for raw intent. It turns a messy
request into one owner route, bounded support gates, the first safe local action,
verification, and a run receipt. It is not a competing router and not the older
gate-suppressed mission dispatcher.

## Co-Creative Launchpad

Autopilot owns the Co-Creative Launchpad: raw context becomes an intent lock,
route trace, execution decision, and safe local next action when risk permits.

For substantial operator/system work, start with the local preflight:

```bash
python3 execution/codex_operator_preflight.py "<raw intent>" --plain
```

Follow the `local_next_action` when it is safe, local, and verifier-backed.
Pause only for external writes, destructive cleanup, paid/quota-heavy tools,
global `~/.codex` edits, Codex Antigravity mutation, publishing/outreach,
connector writes, or real Codex subagents.

`/go` is the front door that stages this engine: when intent arrives raw or
messy, run `/go "<messy thought>"` first. Its Stage 0 RUN PACKET (assumptions,
outcomes, constraints, taste refs, budget note) is what Autopilot's Intent Lock
consumes — Autopilot itself stays a gate-suppressed dispatcher, not a second
intent-sharpening pass.

## Usage

```bash
/autopilot [raw context]
/autopilot --plan [raw context]
/autopilot --menu [raw context]
```

Default behavior is execute-safe-local-work. `--plan` stops at a
decision-complete plan. `--menu` is for cases where Farrice explicitly wants
ranked options.

## Execution Decision

Every Autopilot run must name one execution status before work starts:

| Status | Meaning |
|---|---|
| `Running now` | safe workspace-local execution can start after the trace. |
| `Needs judgment` | Farrice must decide a taste, scope, or intent point before execution. |
| `Blocked by risk` | External, paid, destructive, global, Google Antigravity, publishing, connector-write, or real-subagent action is present. |
| `Plan only` | The user asked for `--plan`, `--menu`, or another explicit no-execution posture. |

When blocked, include a copy-paste **Run Prompt** so the work has a clean
resume path instead of dying as a recommendation.

## Capability Graph

Use the capability graph to expose the available routes, support gates, tools,
and proof surfaces before choosing a path:

```bash
python3 execution/capability_graph.py --json
```

## Outcome Recipes

Use outcome recipes to keep Autopilot from becoming a generic planner. The
chosen route should map to the smallest executable recipe that can produce the
requested outcome, proof, and handoff:

```bash
python3 execution/outcome_recipes.py "[raw context]" --json
```

The classifier resolves to one of these outcome classes (source of truth:
`execution/outcome_recipes.py` — this table mirrors it, never extends it):

| Outcome class | Primary route |
|---|---|
| kishotenketsu-contrast-storytelling | `/kishotenketsu-contrast-storytelling` |
| system-repair | `/system-audit` |
| source-to-skill | `/source-to-skill-system` |
| plugin-packaging | `/plugin-readiness-audit` |
| revenue-sprint | `/first-10k` |
| content-package | `/content-media-agent` |
| research-synthesis | `/research-intelligence-agent` |
| deep-research-os | `/deep-research-os` |
| client-audit | `/client-delivery-agent` |
| design-build | `/creative-design-agent` |
| mission-continuation | `/mission` |
| repeatability-repair | `/repeatability-spine` |
| general-operator (fallback) | `/autopilot` |

## Friction Ledger And Run Receipt

When routing, hook, retrieval, proof, or operator-friction issues appear, log
them locally and close with proof:

```bash
python3 execution/friction_ledger.py log --kind failed-route --summary "[what happened]" --next-action "[repair route]"
python3 execution/friction_ledger.py verify
python3 execution/run_receipt.py --query "[raw context]" --route "[route]" --status "[Running now|Needs judgment|Blocked by risk|Plan only]" --changed "[what changed]" --passed "[checks]" --failed "[failures]" --judgment "[judgment needed]" --next-action "[next]"
```

## Plugin Packaging Ladder

Do not jump from a useful local workflow to plugin packaging. First prove the
helper, workflow, command bridge, live use, and repeatability. Packaging checks
route through:

```bash
python3 execution/plugin_readiness_audit.py --stdout [candidate routes]
```

Hard stops before mutation: No global mirror, Google Antigravity edit, publishing, paid tool, destructive cleanup, external write, connector write, or real Codex subagent without explicit approval.

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

## Capability Stewardship Lifecycle

Capability Stewardship is a companion layer inside Autopilot, not a new front
door. For every meaningful start, quietly check the owner, current context
container, one materially useful capability, the proof path, and what should
survive the session. If none changes the outcome, execute without mentioning
the scan.

Re-run the leverage check when a distinct branch appears, decisions circle,
two taste-bearing revisions are rejected, context fatigue appears, independent
workstreams emerge, more than three experts are plausible, a safe verifier or
research/monitoring/artifact capability becomes useful, or a one-off process is
becoming reusable.

Choose one move: continue, bounded support, verify, `/handoff`, `/fresh-pen`,
recommend a new user-owned task, preserve the method, or monitor. Reuse the
existing `/handoff` and `/fresh-pen` packet contracts; never duplicate their
transfer logic. At a material fork show only:

1. the recommended move in plain English;
2. why it matters now;
3. the concrete local action Codex can take;
4. the approval boundary, only when one exists.

Do not create or open user-owned tasks automatically. Do not deploy real
subagents, schedule automations, publish, send, write through connectors, use
paid tools, perform destructive action, or change global state without their
existing explicit approvals.

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

## Taste Gates (G1 / G2 / G3)

Autopilot is gate-*suppressed*, not gate-free: every other mid-flight halt
(routing ambiguity, format choice, model choice, minor scope calls) is
suppressed by design — see Execution Sequence above for the default path. Only
these three taste gates are allowed to interrupt, and their conditions are
code, not judgment. Run one check:

```bash
python3 execution/gates.py check --dice <1-5> [--est-cost <dollars>] \
    [--services <csv>] [--deliverable <path>] [--expert-score <n>]
```

Exit 0 = no gate fires, run end-to-end. Exit 2 = at least one fires; the
output names each firing gate with its reason and exact remediation command.
A gate whose inputs weren't provided reports "not evaluated (missing --x)" —
never a silent pass. DICE-score the raw intent per CLAUDE.md Step 1, or reuse
the `/go` Stage 0 RUN PACKET score if one was already produced upstream.

| Gate | Fires when | Remediation |
|---|---|---|
| **G1 — Intent** | DICE score <= 2 | One question round on the missing dimensions only, then proceed. Score >= 3: write the assumptions and proceed — no halt. |
| **G2 — Cost** | est-cost > $5, OR any listed service returns needs-approval/denied from `cost_gate.py check` (on Claude Code the deny is hook-enforced HARD BLOCK; on Codex the check is manual) | Ask Farrice once; after an explicit yes: `python3 execution/cost_gate.py approve --service <id>`, then continue without re-asking this run. Denied: surface, do not retry. |
| **G3 — Prose/taste** | Expert Standard trending >= 7 AND `prose_classifier.py check` FLAGGED on the deliverable | Surface exactly one taste call to Farrice — never re-litigate the whole draft. Companion factual gate when the deliverable carries real-world claims: `python3 execution/claim_audit.py check <path>`. |

Calibration for the G3 taste call (unchanged, binding): reference the
taste-calibration signature — bimodal: clear PASS/FAIL, narrow marginal band;
-1/dimension on a FAIL. Any dimension scored 8+ must name the matching anchor
in `evolution_store/ground_truth/rubric_v1.md` — if the anchor can't be named,
lower the score instead of asking.

If none of G1/G2/G3 fire, Autopilot runs end-to-end and closes with the
Friction Ledger + Run Receipt — no other approval loop.

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

Substantial Autopilot runs — builds, repairs, audits, or any run with a real
next decision — compose the Capability Stewardship reveal into the existing
steering closeout. Skip the full block for answers, diagnostics, corrections,
conversation, terse asks, and mechanical turns per `directives/steering-loop.md`;
a skipped block is better than padded capability education.

Use `execution/contextual_next_prompts.py` when it fits, or fill this compact
shape with context-rich prompts:

```
### Next Prompts (Insightful Momentum)
1. **Use Now:** <copy-paste immediate continuation; reveal the capability that makes it stronger>
2. **Harden:** <copy-paste verifier or reliability move; name the hidden gap it closes>
3. **Expand:** <copy-paste compounding move; name the reusable asset worth preserving>

### Operator Lesson
<one lesson that teaches the move behind the work, not just the result>

- **Next-time prompt:** <copy-paste continuation that gets a better result next run>
- **Subagent worth it?** <yes/no + why — real Codex subagents require explicit
  authorization and default to read-only diagnostics>
- **Reuse hook:** <the part of this run worth turning into a repeatable skill,
  workflow, or saved prompt>
```

Each Next Prompt must be context-rich and capability-revealing, not generic.
At most one capability recommendation interrupts the main answer before this
closeout; never dump the tool or expert menu.
