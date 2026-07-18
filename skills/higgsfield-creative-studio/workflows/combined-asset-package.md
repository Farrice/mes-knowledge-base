---
name: "Higgsfield Creative Studio — Combined Asset Package"
slug: "combined-asset-package"
produces: "One still-to-video campaign package: Strategy Spine, Key Visual Prompt, Marketing Studio Prompt, QA Pass, Preview Recommendation"
skill: "higgsfield-creative-studio"
load_context: "genius.md"
---

# Higgsfield Creative Studio — Combined Asset Package Workflow

## Role

You are running the full-system path of the Higgsfield Creative Studio router: the case where a
user wants a still and a video that read as one campaign, not two disconnected prompts. This
workflow is a thin, additive wrapper around the deterministic protocol already locked in
`skills/higgsfield-creative-studio/references/prompts-v2/combined-asset-package.md` — read that
file for the full Execution Protocol (Strategy → Copy → Visual Direction → still → video → image
references → Design QA → Preview Recommendation) and follow it exactly. This workflow file exists
so the skill has an auditable `workflows/` entry point; it does not redefine or loosen anything
that file already locks.

**Before executing:** confirm this is genuinely a full-system request per
`skills/higgsfield-creative-studio/SKILL.md`, line 78 — "Do not add the package wrapper when the
user asked only for a single GPT Image 2.0 prompt or a single Marketing Studio prompt." A
single-format ask routes straight to `gpt-image-2-director` or `marketing-studio-director` instead.

## Input Required

1. **Product / brand / offer** and **audience** — what is being sold and to whom.
2. **Angle or emotional target** — user-supplied, or established during this session.
3. **Product or avatar images**, if attached — carried through with fidelity rules intact.
4. **Marketing Studio preset**, if the user has one — otherwise mapped by job (UGC/Tutorial/
   Unboxing/Hyper Motion/TV Spot/Try On) per `SKILL.md`'s Stacking Order step 4.
5. **Client or personal work** — governs preview defaults per the Credit Guard section.

## Workflow

### Step 1 — Load the Strategy layer
Per `SKILL.md` Stacking Order step 1: `skills/luke-iha-creative-strategy/SKILL.md` by default, or
`skills/greg-hoffman-brand-mastery/SKILL.md` for campaign-/brand-level requests. Land on the
Strategy Spine before either prompt is drafted.

### Step 2 — Produce the still, then the video
Load `gpt-image-2-director` for the Key Visual Prompt first (locks product placement, mood,
palette, hierarchy), then `marketing-studio-director` for the Marketing Studio Prompt second, so
the video inherits the still's world rather than re-deriving it. Preserve each source skill's own
output format exactly — this workflow never rewrites their syntax.

### Step 3 — Run Design QA
Load `skills/satori-graphics-design-mastery/SKILL.md` (or `skills/jack-roberts-design-mastery/SKILL.md`
for reusable design-system work) to check hierarchy, AI tells, fidelity, and brand drift. QA
recommendations flag problems; they do not overwrite the prompt-director outputs.

### Step 4 — Recommend, never generate, the lowest useful preview
State the guarded first-render recommendation only. Real generation is a separate, gated step —
route it through `skills/higgsfield-creative-studio/workflows/guarded-generation-request.md`
(or the deterministic `references/prompts-v2/guarded-generation-request.md` it wraps) if and when
the user asks to actually render.

## Output Schema

Exactly five markdown sections, in this order, using the headers verbatim — matching
`references/prompts-v2/combined-asset-package.md`'s own Output Skeleton so the two never drift:

```markdown
## Strategy Spine
[1-3 bullets: audience, angle, emotional target]

## Key Visual Prompt
[GPT Image 2.0 prompt in gpt-image-2-director's native format — fenced code block]

## Marketing Studio Prompt
[One flowing paragraph in marketing-studio-director's native format]

[Generate link exactly as that skill requires]

## QA Pass
[3-5 checks: product fidelity, avatar fidelity if applicable, visual hierarchy,
brand consistency, ad clarity]

## Preview Recommendation
[One guarded first-render recommendation: operation, count, duration/resolution
if video, and why this is the lowest useful preview]
```

No section is dropped for a full-system request; no section is added beyond these five. The still
prompt stays in a fenced code block; the video prompt stays a flowing paragraph plus Generate link.

## Quality Gate

1. **Full-system confirmed.** Was this genuinely a multi-format ask, not a single-prompt request
   that should have bypassed the package (`SKILL.md`, line 78)?
2. **One strategy spine, not two.** Do the still and video share the same audience/angle/emotional
   target rather than reading as disconnected assets (`references/hidden-knowledge.md`,
   "Orchestration Bias")?
3. **Source format fidelity.** Are `gpt-image-2-director`'s and `marketing-studio-director`'s own
   output formats preserved exactly, with zero orchestrator rewriting
   (`references/genius-patterns.md` § "1. Source Skill Sovereignty")?
4. **Concrete QA, not restated brief.** Does the QA Pass name real hierarchy/AI-tell/fidelity risks
   specific to this product and preset, not a generic checklist?
5. **Preview stays guarded.** Is the Preview Recommendation the lowest-cost useful render, never a
   full/final-render default — with actual generation deferred to the guarded generation workflow?
