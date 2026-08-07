---
description: "Deploy Virtuoso orchestration for any objective: visible route, owner, stack, gates, delegation packets, dynamic workflow manifests, verification, and first safe local action"
---

# /virtuoso - Virtuoso Orchestration Front Door

Use this when Farrice wants the full Antigravity harness applied to any domain
without remembering individual commands, agents, workflows, or plugins.

`/virtuoso` is a composer over the existing control plane. It does not replace
Autopilot, Orchestrate, Mission, System Audit, Expert Composition Governor,
Source-to-skill-system, or Routing Intelligence. It inherits Autopilot's shared
Co-Creative Launchpad Packet, chooses the owner, shows the blend, labels what
was considered versus actually executed, and then runs the first safe
workspace-local action by default.

For operating-alignment requests, Virtuoso must preserve `/system-audit` as the
owner and use itself, Expert Composition Governor, Routing Intelligence,
Health Check, Repeatability Spine, and Self-Evolve as support gates. It should
not promote a domain expert stack to owner just because the prompt asks for the
full arsenal.

## Usage

```text
/virtuoso [goal]
/virtuoso --trace-only [goal]
/virtuoso --delegate [goal]
/virtuoso --log [goal]
/virtuoso --workflow [goal]
/virtuoso --mode revenue|creative|research|build|audit|repair [goal]
```

## Options

- `--trace-only`: render the trace and stop.
- `--delegate`: prepare subagent-first packets and Delegation Receipt fields;
  never spawn real Codex subagents without explicit approval.
- `--log`: log the routing decision only when the chosen route is actually used.
- `--workflow`: attach a Codex Dynamic Workflow manifest trace for large,
  multi-phase, cross-checked, or resumable work. This prepares phases and worker
  packets but does not spawn real Codex subagents.
- `--mode revenue|creative|research|build|audit|repair`: bias routing without
  bypassing the owner, support-gate, or approval system.
  Research-heavy objectives should route into `/deep-research-os` when they
  need source-ledger planning, social listening, wide decomposition, or claim
  verification.

## Steps

### 1. Normalize Objective

Strip the `/virtuoso` command name and option flags from the user's request.
If no meaningful objective remains, ask for the smallest missing goal. If the
objective is clear enough to route, state assumptions and continue.

### 2. Run Composer

From the project root, run the matching command:

```bash
python3 execution/virtuoso_orchestration.py "[goal]" [--trace-only] [--delegate] [--log] [--mode revenue|creative|research|build|audit|repair]
```

For manifest-held multi-phase work, add:

```bash
python3 execution/virtuoso_orchestration.py "[goal]" --workflow
```

Use JSON only when another script needs the result:

```bash
python3 execution/virtuoso_orchestration.py "[goal]" --json
```

### 3. Show Virtuoso Trace

Return the trace with these sections:

- Co-Creative Launchpad Packet inherited from Autopilot
- primary route and owner
- support gates considered
- recommended stack or skip reason
- Composition Ledger
- Delegation Matrix
- Dynamic Workflow Trace when `--workflow` is used
- plugin/tool surface
- verification plan
- Orchestration Receipt with meta_intent, composition_owner, support gates,
  expert lenses, subagent boundary, verifier status, and feedback hook
- Execution Receipt

The receipt must distinguish:

- considered gates
- loaded context
- selected workflow
- executed workflows
- executed scripts
- skipped gates
- expert lenses applied
- subagent packets prepared
- real subagents spawned
- dynamic workflow manifest planned or saved
- external actions

### 4. Execute First Safe Local Action

If `--trace-only` is present, stop after the trace.

If `--workflow` is present, stop after the manifest trace unless Farrice
explicitly asks to save, resume, or run the manifest. Real Codex subagents still
require explicit authorization and a Delegation Receipt.

If the execution decision is safe for local work, execute the first safe local
action in the main Codex thread. Update the Execution Receipt after the action
so the user can see what actually ran.

If the next action needs external/public/paid/destructive/global/connector
access, Google Antigravity edits, Mission/system memory mutation, or real Codex subagents,
stop at an approval checkpoint with a copy-pasteable continuation prompt.

### 5. Verify

Run the smallest relevant verifier set. At minimum after command-surface
changes, run:

```bash
python3 execution/verify_virtuoso_orchestration.py
python3 execution/verify_codex_dynamic_workflow.py
python3 execution/codex_live_surface_audit.py --strict
python3 execution/codex_harness_check.py
```

For ordinary `/virtuoso` runs, use the verifier plan from the trace and add
domain-specific checks only when they materially reduce risk.

### 6. Report

Close with:

- what route owned the work
- what was considered
- what actually executed
- whether routing was logged
- what remains approval-gated
- the next concrete prompt or action

## Behavior Rules

- Support gates in the trace are considered, not deployed, unless listed under
  executed workflows or executed scripts.
- Expert names are lenses unless a real worker or subagent was explicitly
  spawned.
- Real Codex subagents require explicit authorization.
- No publishing, DMs, connector writes, paid/API usage, destructive cleanup,
  global mirrors, or `/Users/farricecain/Google Antigravity` edits without
  explicit approval.
- Mission remains untouched unless its verifier fails and Farrice approves
  Mission repair.
- If the command creates an artifact, use the workspace artifact guards before
  closeout.
