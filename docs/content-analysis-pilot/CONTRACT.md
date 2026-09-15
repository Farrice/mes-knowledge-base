# Content analyst pilot contract

Farrice confirmed this scope on 2026-09-14: one on-demand content analyst for
Codex and Claude Code, initially a local pilot with paid execution disabled.
This milestone does not authorize paid trials, uploads, global installs or jobs.

## Skill system contract

- **Objective:** discover promising references, learn declared taste, extract
  timestamped lessons and propose original adaptations with explicit spending.
- **Owner:** main Codex task builds and integrates; Farrice owns taste and budget.
- **Sources:** Google video/pricing/billing docs, Riley's published video skill,
  existing watch, execution/cost_gate.py, existing video-context-ledger discipline.
- **Components:** additive content_analysis_pilot.py, existing video analysis
  skill and watch; existing analytics tools only after access is verified.
- **Order:** classify sources → immutable preview → exact batch approval →
  transactional reservation → bounded simulation → durable receipt → synthesis.
- **Inputs:** exact URLs/files, duration, goal, model, output limit and available
  performance evidence/taste decisions. A link alone does not prove success.
- **Outputs/handoff:** batch hash, cost assumptions, per-item state and source
  evidence references. Synthesis distinguishes performance, taste and hypotheses.
- **Composition:** one evidence-analysis owner. Gemini is a future perception
  backend, not the strategist. Existing content workflows own final production.
- **Human checkpoint:** no spending is implied by a key, confirmation of this
  build, or simulation approval. Live transport is absent and hard-disabled.
- **Validation:** isolated stdlib tests for approval, hash, expiry, budgets,
  concurrency, deduplication, cache, deadlines, interruption and unknown charges;
  cold CLI preview/approve/simulate/status example. No external API calls.
- **Behavior proof:** simulator state transitions only; real video quality and
  actual billed usage remain UNTESTED pending a separately authorized trial.
- **Result surface:** concise conversation receipt; local readable operator guide.
- **Context/reuse:** extend the existing creative-reference workflow with an
  opt-in reference. No new hot skill, global mirror, discovery daemon or agent.

## Engineering packet

Use one SQLite ledger for the two harnesses, reserve before dispatch and retain
unknown liability across restarts. Bounded requests/tokens/time, no paid retries,
no model fallback. Never treat a static estimate as a proven agentic cost cap.
A child timeout cannot establish that a real remote job stopped charging.
Approval records capture user decisions; they are not an OS security boundary.
Do not change other services' cost policy or the generic Gemini quota entry.

Chunks: guard → adversarial tests → analyst workflow → offline example. No new
dependencies. Stop after targeted checks pass; reassess after two failed repair
passes. Rollback removes additive code/docs and the opt-in link, keeps receipts.
No monthly paid allowance has been granted: effective live allowance is $0.

## Source and preservation references

- https://ai.google.dev/gemini-api/docs/video-understanding
- https://ai.google.dev/gemini-api/docs/pricing
- https://ai.google.dev/gemini-api/docs/billing
- https://agentnative.inc/resources/give-agents-video-analysis-skill
- skills/youtube-video-context-analysis/references/prompts-v2/multi-video-comparison.md

Existing watch and extraction routes remain the approved primary. State machines
and shared spending are the only new common foundation; domain judgment remains
with the existing owner. Controls cover this workflow, not unrelated processes.
