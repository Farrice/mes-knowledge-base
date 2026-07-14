# Higgsfield Usage Policy

> Applies to all Higgsfield CLI and MCP generation: images, videos, Marketing Studio, product photoshoots, marketplace cards, Soul-ID training, and job display.

## Hard Rule

Every real Higgsfield generation must pass through `execution/higgsfield_budget_guard.py check` before generation and `execution/higgsfield_budget_guard.py log` after completion.

Prompt-only ideation, creative briefs, and prompt packages are free and do not need approval.

The Joey cinema skills (`banana-pro-director`, `cinema-worldbuilder-pro`, `story-bible-builder`, `joey-cinema-os`) are prompt-only — their job ends at the code block and they are never gated. Executing their prompts through Higgsfield MCP/CLI or Fal wrappers remains guarded unchanged.

## Current Baseline

- Account: `farrice.cain@gmail.com`
- Plan: ultimate
- Starting tracked balance: `1200` credits
- Tracker: `.agent/higgsfield-usage.json`
- Guard: `execution/higgsfield_budget_guard.py`

## Balanced Defaults

| Layer | Rule |
|---|---|
| Per-call approval | Estimated spend above 3% of current credits requires explicit approval |
| Session soft cap | Projected session spend above 8% requires explicit approval |
| Daily hard cap | Projected daily spend above 15% is blocked unless explicitly overridden |
| Failure circuit | 2 consecutive generation failures halt all generation |
| Retry limit | 1 automatic retry max |
| Video defaults | 1 variant, 720p max, 8-10s preview; 15s final only when requested |
| Image defaults | 1-3 preview variants; final render after a winner is selected |

## Tool Routing

Use MCP when:

- The user benefits from in-app widgets.
- Showing Marketing Studio libraries, product/webproduct fetch, avatars, or previous jobs.
- Training/listing/checking Soul-ID through the guided flow.
- Direct image/video generation is being run from the app context.

Use CLI when:

- Local files need auto-upload.
- Account status, transactions, or credit checks are needed.
- `higgsfield generate cost ...` can estimate credits before generation.
- Product photoshoot backend enhancement is needed.
- Marketplace card generation is needed.
- Repeatable batch or dry-run workflows are needed.

## Preflight Patterns

### Prompt-only package

```bash
python3 execution/higgsfield_budget_guard.py check --operation prompt_only --channel prompt
```

### CLI generation with known cost

```bash
higgsfield generate cost <model> --prompt "..." [flags]
python3 execution/higgsfield_budget_guard.py check \
  --operation <operation> \
  --channel cli \
  --estimated-credits <credits_from_cost_command>
```

If the guard returns approval required, ask the user before running. After approval:

```bash
python3 execution/higgsfield_budget_guard.py check \
  --operation <operation> \
  --channel cli \
  --estimated-credits <credits_from_cost_command> \
  --approved
```

### MCP generation

MCP calls do not automatically pass through the local guard, so the agent must call the guard first:

```bash
python3 execution/higgsfield_budget_guard.py check \
  --operation marketing_studio_video \
  --channel mcp \
  --estimated-credits <conservative_estimate>
```

Only then call `mcp__higgsfield__generate_image`, `mcp__higgsfield__generate_video`, `mcp__higgsfield__show_marketing_studio`, or Soul-ID tools.

### Log after generation

```bash
python3 execution/higgsfield_budget_guard.py log \
  --operation <operation> \
  --channel <cli|mcp> \
  --status success \
  --estimated-credits <estimate> \
  --actual-credits <actual_or_estimate> \
  --job-id <id_if_known> \
  --output-url <url_if_known>
```

If the account balance is known before and after:

```bash
python3 execution/higgsfield_budget_guard.py log \
  --operation <operation> \
  --status success \
  --before-credits <before> \
  --after-credits <after>
```

## Creative Workflow

1. Create a prompt-only Creative Capsule first: strategy spine, visual direction, still prompt, video prompt, recommended preview.
2. Generate a low-cost preview only when approved or clearly requested.
3. Ask the user to pick a winner before final render.
4. Use final renders for client-facing assets, not broad unselected batches.
5. Log selected and rejected outputs where useful so future work starts from taste history.

## Refusal / Halt Behavior

If the guard denies a run:

- Do not generate.
- Explain the blocking reason in plain language.
- Offer a cheaper alternative: fewer variants, shorter video, lower-risk prompt-only package, or wait until the next day.

If the failure circuit trips:

- Stop all generation.
- Diagnose auth, model params, media roles, or network issues.
- Reset only after the issue is fixed:

```bash
python3 execution/higgsfield_budget_guard.py reset-failures
```
