# Higgsfield Creative Studio — Genius Context

> Load this before any routing decision. This is not a person-extraction skill — it is a **routing and stacking layer** that sequences two locked prompt directors (`gpt-image-2-director`, `marketing-studio-director`) plus a real-money credit guard (`execution/higgsfield_budget_guard.py`, gated per `directives/higgsfield-usage-policy.md`). Grounded in this skill's own `SKILL.md` (7,745 bytes), its existing `references/genius-patterns.md` and `references/hidden-knowledge.md`, and real Higgsfield platform documentation captured in `extractions/creative-direction/` (5 files, 30,166 bytes combined, `wc -c` verified). Every claim below is anchored — see `references/source-ledger.md` for VERIFIED/LIKELY/UNCONFIRMED labels claim-by-claim.

---

## How to Use This Skill (Model Calibration)

This is an intuition primitive for a routing skill, not a checklist to stamp. The job is sequencing and protecting two other skills' output formats — never rewriting them, never narrating the sequencing out loud. The test: would a Higgsfield production lead — or Rus Syzdykov's own Nov 21, 2025 prompt-engineering guide, "NANO BANANA PRO: Expert Use Cases with Prompts" — recognize this as production-grade routing discipline, or as an AI assistant reciting "I'll now load the strategy layer" narration over the top of a prompt stack? If it's the second, rebuild toward silent execution.

Specifically:
- Do NOT narrate the stacking order ("Loading Strategy layer... now Copy layer... now Visual Direction...") into the delivered output. `SKILL.md`'s own Combined Asset Package format (line 61-76) is five headers and nothing else — the sequencing happens before the response, invisibly.
- Do NOT wrap a single-prompt request in the five-section package. `SKILL.md` line 78 is explicit: "Do not add the package wrapper when the user asked only for a single GPT Image 2.0 prompt or a single Marketing Studio prompt. In those cases, follow the source skill's output format exactly." Over-delivering structure the user didn't ask for is the polish tell for this skill specifically — it reads as the orchestrator protecting its own machinery rather than serving the request.
- This skill's specific texture is restraint at the seam between two systems: the still "locks the visual world" (per `references/hidden-knowledge.md`, "A strong key visual can lock the product world before the motion prompt adds pacing and camera grammar") and the video inherits it — never the reverse, and never both prompts re-explaining the same product description from scratch.
- Photoreal fidelity and exact product/brand facts are the floor, not a stretch goal — `SKILL.md` line 86-87 is explicit that images must "preserve the Marketing Studio fidelity rules: exact product packaging, color, logo placement, proportions, avatar face/build" and "not infer unsupported product claims from images."

---

## Anti-Patterns (Sourced)

- Rewriting or "improving" `gpt-image-2-director`'s or `marketing-studio-director`'s own delivered prompt syntax instead of passing their output through untouched. Sourced to `references/genius-patterns.md` § "1. Source Skill Sovereignty" (2026-07-13 refactor date on this skill's own `references/prompts-v2/combined-asset-package.md` frontmatter): "Use the orchestrator for routing and stacking, but let `gpt-image-2-director` and `marketing-studio-director` control their own final prompt formats."
- Wrapping every request — including a single GPT Image 2 prompt ask — in the full five-section Combined Asset Package. Directly contradicted by `skills/higgsfield-creative-studio/SKILL.md`, line 78: "Do not add the package wrapper when the user asked only for a single GPT Image 2.0 prompt or a single Marketing Studio prompt. In those cases, follow the source skill's output format exactly."
- Calling `mcp__higgsfield__generate_image`, `mcp__higgsfield__generate_video`, or any CLI `higgsfield generate create` without running the guard first. Per `directives/higgsfield-usage-policy.md`, "Hard Rule" section: "Every real Higgsfield generation must pass through `execution/higgsfield_budget_guard.py check` before generation and `execution/higgsfield_budget_guard.py log` after completion."
- Confusing Higgsfield's internal "GPT-2" face-fidelity escalation tool with OpenAI's separate GPT Image 2 model that `gpt-image-2-director` targets. `SKILL.md` line 38 draws the line explicitly: "Disambiguation: Higgsfield GPT-2 (face-fidelity image model, credit-heavy — banana-pro-director's escalation path) ≠ OpenAI GPT Image 2 (`gpt-image-2-director` — layout/typography king, weak faces)."
- Generating the still and video prompts from two separate, un-synced briefs instead of one shared Strategy Spine. Per `references/hidden-knowledge.md`, "Orchestration Bias": "The still image and video prompt should share one strategy spine." Skipping this reverses `references/genius-patterns.md` § "2. Strategy Spine Before Asset Stack": "Still and video prompts feel like one campaign, not two disconnected assets" is the stated success metric, not a suggestion.
- Treating Sora 2 Trends' pacing guidance as license to imitate a specific competitor clip rather than absorb structural timing. Per Mariam Barova, higgsfield.ai blog, Nov 26, 2025 ("Best Ways to Organize Your Workflow on HiggsfieldAI"): "Unlike generic trend tools, it provides creative structure rather than imitation, guiding how pacing, composition, and tone can adapt to what audiences currently engage with."
- Over-explaining the routing decision to the user before delivering the asset. Per `references/hidden-knowledge.md`, "Failure Mode": "The orchestrator can accidentally break source-skill output formats by over-explaining. Single-prompt requests must be passed through to the relevant source director."

---

## Verbatim Exemplars

> "Nano Banana Pro represents a fundamental shift in diffusion technology. The model prioritizes comprehension and logical interpretation of the prompt." — Rus Syzdykov, Head of Prompt Engineering, Higgsfield, Nov 21, 2025 (`extractions/creative-direction/higgsfield.ai_blog_Nano-Banana-Pro-Expert-Use-Cases.md`, lines 46-56; https://higgsfield.ai/blog/Nano-Banana-Pro-Expert-Use-Cases).

> "Do not add the package wrapper when the user asked only for a single GPT Image 2.0 prompt or a single Marketing Studio prompt. In those cases, follow the source skill's output format exactly." — `skills/higgsfield-creative-studio/SKILL.md`, line 78 (this skill's own single-prompt bypass rule).

> "Unlike generic trend tools, it provides creative structure rather than imitation, guiding how pacing, composition, and tone can adapt to what audiences currently engage with." — Mariam Barova, higgsfield.ai blog, Nov 26, 2025 (`extractions/creative-direction/higgsfield.ai_blog_Best-Ways-to-Organize-Your-Workflow-on-Higgsfield-AI.md`, line 96).

> "Your scene comes together when each tool does one job well: Higgsfield Popcorn locks tone and composition, Seedream or Seedance refine identity and micro-motion, Veo 3.1 or Sora 2 carry the performance, and Recast replaces characters without breaking light, framing, or atmosphere." — `extractions/creative-direction/higgsfield.ai_blog_Prompt-Guide-to-Cinematic-AI-Videos.md`, lines 25-27 (the same one-job-per-tool discipline this skill's Stacking Order applies to the strategy/copy/visual/production/QA layer split).

---

## Real Tool Ecosystem (Grounding)

Real Higgsfield tools this orchestrator routes across, confirmed against platform documentation captured in `extractions/creative-direction/` (not invented for this repair): Nano Banana Pro, Nano Banana 2, Soul 2.0 / Soul Cinema / Soul Cast, Soul ID Character, GPT Image 1.5, Higgsfield Popcorn, Recast, Seedance 2.0, Kling 3.0, WAN 2.6, Cinema Studio 3.0, Sora 2 / Sora 2 Max, Google Veo 3.1 (per `extractions/creative-direction/higgsfield_notes.md`, lines 9-48, and `higgsfield_pipeline.md`, lines 5-44). Higgsfield is headquartered at 535 Mission St, 14th floor, San Francisco, CA, 94105 (per `extractions/creative-direction/higgsfield.ai_blog_Prompt-Guide-to-Cinematic-AI-Videos.md`, line 117, footer capture, © 2026 Higgsfield AI™).

**Byline spelling gap worth flagging (not silently resolved):** the "Best Ways to Organize Your Workflow" article credits the byline "Mariam Barova" at the top (line 48) but the same site's "Hot and trending" footer block credits "Mairam Bairova" for the same and adjacent articles (lines 125, 129, 133) — two different spellings of what is presumably one author, both present in the same captured page. Which spelling is correct is UNCONFIRMED from this source alone; both are quoted as they literally appear rather than silently normalized. See `references/source-ledger.md`.

---

## Credit Guard Physics (Grounding)

The numbers this skill's Credit Guard section defers to are not this repair's invention — they are `directives/higgsfield-usage-policy.md`'s own "Balanced Defaults" table: per-call approval required above 3% of current credits, session soft cap at 8% projected spend, daily hard cap at 15% (blocked unless explicitly overridden), a 2-consecutive-failure circuit breaker, and a 1-retry max. Starting tracked balance on the account of record (`farrice.cain@gmail.com`, "ultimate" plan) is 1,200 credits, tracked in `.agent/higgsfield-usage.json`. Video defaults cap at 1 variant / 720p / 8-10s preview (15s final only when explicitly requested); image defaults cap at 1-3 preview variants before any final render. These are the guard's actual rules, not a paraphrase — this repair changes zero cost thresholds, per the additive-first, never-alter-cost-references constraint on this repair pass.

---

## Source Ledger Pointer

Full claim-by-claim VERIFIED / LIKELY / UNCONFIRMED breakdown lives in `references/source-ledger.md` — every source consulted for this repair pass (this skill's own `SKILL.md`, `references/genius-patterns.md`, `references/hidden-knowledge.md`, `references/prompts-v2/*.md`; `directives/higgsfield-usage-policy.md`; 5 Higgsfield platform captures in `extractions/creative-direction/`, 30,166 bytes combined; and a negative-result check against `extractions/` for any dedicated "higgsfield-creative-studio" extraction folder, confirmed absent by directory listing, not assumed) is logged there with file path, byte size, and verification status.
