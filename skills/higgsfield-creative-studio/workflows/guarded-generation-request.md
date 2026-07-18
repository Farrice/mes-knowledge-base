---
name: "Higgsfield Creative Studio — Guarded Generation Request"
slug: "guarded-generation-request"
produces: "A guard-checked generation decision (clear / approval-required / denied / circuit-tripped) plus the post-generation log plan"
skill: "higgsfield-creative-studio"
load_context: "genius.md"
---

# Higgsfield Creative Studio — Guarded Generation Request Workflow

## Role

You are running the real-money dispatch path: the only place in this skill where a prompt turns
into an actual Higgsfield (or GPT Image) generation call. This workflow is a thin, additive wrapper
around the deterministic protocol already locked in
`skills/higgsfield-creative-studio/references/prompts-v2/guarded-generation-request.md` — read that
file for the full seven-step Execution Protocol (determine channel/preflight cost, run the guard,
apply the Balanced Defaults thresholds, branch on the result, generate only what cleared, log after
generation, sequence the wider creative workflow). This workflow file exists so the skill has an
auditable `workflows/` entry point; it changes none of that protocol's cost thresholds, model names,
or routing rules.

**Before executing:** confirm this actually fires. Per `SKILL.md`'s Credit Guard section:
"Prompt-only Creative Capsules are free and do not need user approval." This workflow only runs
when the user asks to actually render, generate, or show a real result — not for prompt-only
ideation.

## Input Required

1. **Operation** — e.g. `marketing_studio_video`, `image_generation`, `product_photoshoot`,
   `soul_id_training`, `marketplace_card`.
2. **Channel** — `cli` or `mcp`.
3. **Estimated credits** — from `higgsfield generate cost <model> --prompt "..."` when CLI cost is
   knowable preflight, otherwise the conservative estimate in `.agent/higgsfield-usage.json`.
4. **Client or personal work** — governs default variant/duration/resolution per
   `directives/higgsfield-usage-policy.md`.
5. **Prior approval status** — none, requested, or already granted this session.

## Workflow

### Step 1 — Determine channel and preflight cost
CLI with knowable cost: run `higgsfield generate cost` first. CLI without one (product photoshoot,
marketplace cards): use the conservative `.agent/higgsfield-usage.json` estimate. MCP: the guard
must be called manually before any `mcp__higgsfield__generate_image` /
`mcp__higgsfield__generate_video` / Soul-ID tool call — MCP does not auto-route through it.

### Step 2 — Run the guard
```bash
python3 execution/higgsfield_budget_guard.py check \
  --operation <operation> --channel <cli|mcp> --estimated-credits <credits>
```

### Step 3 — Branch on the result
Clear → proceed. Approval required → stop, ask the user explicitly, then re-run with `--approved`
before generating. Denied → do not generate; offer a cheaper route (fewer variants, shorter video,
prompt-only package, next-day run). Circuit tripped → stop all generation, diagnose the underlying
auth/param/media/network issue before any reset.

### Step 4 — Generate only the approved scope, then log
Call the cleared tool at exactly the checked scope — never a larger batch. Log with
`python3 execution/higgsfield_budget_guard.py log --operation <operation> --channel <cli|mcp>
--status <success|failure> --estimated-credits <estimate> --actual-credits <actual>`.

## Output Schema

The response states, in order, matching
`references/prompts-v2/guarded-generation-request.md`'s own Output Skeleton:

```markdown
## Request
Operation: [operation]
Channel: [cli | mcp]
Estimated credits: [number, and how it was derived]

## Guard Check
Command: [exact command run]
Result: [clear | approval required | denied | circuit tripped]

## Decision
[Plain-language reasoning. If approval required: the explicit ask. If denied: the
blocking reason plus the cheaper alternative offered. If circuit tripped: the
diagnosis step before any reset.]

## Generation Plan
[Tool/command to call, scope (variants/duration/resolution), and confirmation this
matches what was checked/approved — or "withheld pending approval / cheaper route"]

## Post-Generation Log
[Exact log command plan, including job-id/output-url placeholders if not yet known]
```

Never state or imply generation happened without the guard check having actually run first.

## Quality Gate

1. **Guard ran before any call.** Was `higgsfield_budget_guard.py check` actually executed before
   any generation tool was invoked — no speculative generation while approval was pending?
2. **Approval, not assumption.** If approval was required, was explicit user approval obtained
   before re-running the check `--approved` and before generating?
3. **Denied means denied, with an alternative.** If the guard denied the request, was a concrete
   cheaper route offered rather than a bare refusal?
4. **Scope discipline.** Does the generation call match exactly what was checked and approved
   (variants, duration, resolution) — not a larger unapproved batch?
5. **Log plan exists, including the failure path.** Is there a post-generation log command plan,
   with the failure-status branch covered if generation fails or the 2-consecutive-failure circuit
   trips per `directives/higgsfield-usage-policy.md`'s Balanced Defaults?
