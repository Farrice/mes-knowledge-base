---
name: "AI Carousel Content Engine — GPT Image 2 Design Prompt"
source_prompt: born-v2
skill: ai-carousel-content-engine
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are building the structured GPT Image 2 design prompt for a carousel — the stage the AI Carousel Content Engine treats as the durable asset. Hidden Knowledge (references/hidden-knowledge.md) is explicit: "The durable asset is the prompt package. Generated images are useful, but the reusable system is what compounds." Genius Pattern 2 states the operating rule directly: GPT Image 2 performs best when the design prompt has explicit regions, text, counts, and slide instructions — structured prompts beat vibes.

**Scope boundary**: this prompt produces the structured JSON design prompt only. Any actual image generation must flow through the cost-gated visual route (`creative_router.py` pre-flight, e.g. `skills/fantastic-posters/`) — this prompt does not generate images itself.

## Input Required

- `[CAROUSEL_SCRIPT]` — the finished slide-by-slide script (title, body, visual direction per slide) this prompt is built from. The design prompt must carry this text exactly, never paraphrase it at generation time.
- `[TITLE]` — carousel topic.
- `[AUDIENCE]` — target audience for the design system.
- `[STYLE_DIRECTION]` — optional custom style/brand reference. If absent, use the default premium-operator style system below.
- `[PLATFORM]` — Instagram, LinkedIn, or both (affects aspect ratio framing).
- `[SLIDE_COUNT]` — must match `[CAROUSEL_SCRIPT]` exactly, 7-10.

## Execution Protocol

**Step 1 — Resolve the style system before touching the prompt.** A vague style paragraph is the failure mode this stage exists to prevent (Hidden Knowledge: "Style Matching Is A Taste Shortcut" — a single strong reference or style board communicates more design intent than a mood word). If `[STYLE_DIRECTION]` is supplied, resolve it into the same four fields the default system uses: visual style description, palette, typography, composition. If not supplied, use the default premium-operator system: clean editorial social carousel, premium consulting brand, high-contrast typography, generous whitespace, structured visual hierarchy, subtle abstract illustrations, no clutter; palette anchored on near-black/navy ground, off-white, one violet accent, one green accent, neutral gray line; bold geometric sans headlines with a readable modern sans body and small uppercase labels; composition rule of one core idea per slide, one visual anchor, short supporting copy, consistent slide numbering.

**Step 2 — Build the prompt as a JSON layout spec, not prose.** The prompt must specify, at minimum:
- `type`: N-slide social media carousel design system.
- `output`: format (single image containing all slides as separate panels), platform, aspect ratio (4:5 portrait is the default for Instagram/LinkedIn), slide count.
- `style`: the resolved visual style description.
- `brand_system`: palette (hex list), typography, composition.
- `audience` and `topic`.
- `layout_rules`: the non-negotiable list — one clearly separated portrait panel per slide; keep all text exactly as supplied in the slide list (do not let the image model paraphrase copy); one hero line per slide, supporting text visibly smaller; consistent margins, slide numbers, and visual motif across all panels; new visuals generated per slide must match the same visual style; when copy runs long, prioritize hierarchy and line breaks over cramming.
- `slides`: an array carrying, per slide, the slide number, label, exact headline, exact body, and visual direction — pulled verbatim from `[CAROUSEL_SCRIPT]`.
- `human_review_note`: an explicit instruction that generated output still needs review for text accuracy, visual cohesion, brand fit, and whether each slide earns the next swipe — the prompt hands off design, not final judgment (Genius Pattern 4: Human-In-The-Loop Taste).

**Step 3 — Verify text fidelity.** Every headline and body string in the `slides` array must match `[CAROUSEL_SCRIPT]` exactly — this stage is not where copy gets rewritten. If a line is too long to fit a panel, that is a signal to return to the copy stage, not to silently truncate inside the design prompt.

## Output Contract

A single structured (JSON-shaped) design prompt containing: type/output block, resolved style block, brand_system block (palette/typography/composition), audience, topic, a complete layout_rules list, a full per-slide array matching the carousel script exactly, and a human_review_note. No prose-only design brief — the structure is the point.

## Output Skeleton

```
{
  "type": "[N]-slide social media carousel design system",
  "output": {
    "format": "single image containing all carousel slides as separate panels",
    "platform": "[PLATFORM]",
    "aspect_ratio": "[e.g. 4:5 portrait]",
    "slide_count": [N]
  },
  "style": "[resolved visual style description]",
  "brand_system": {
    "palette": ["[hex]", "[hex]", "[hex]", "..."],
    "typography": "[headline treatment + body treatment + label treatment]",
    "composition": "[core composition rule set]"
  },
  "audience": "[AUDIENCE]",
  "topic": "[TITLE]",
  "layout_rules": [
    "[panel separation rule]",
    "[text-fidelity rule]",
    "[hero-line-hierarchy rule]",
    "[consistency rule: margins/numbering/motif]",
    "[new-visual-style-match rule]",
    "[overcrowding/line-break priority rule]"
  ],
  "slides": [
    {
      "slide": [number],
      "label": "[Cover / Retention Bridge / Step N / Transformation / CTA]",
      "headline": "[exact headline from carousel script]",
      "body": "[exact body from carousel script]",
      "visual_direction": "[exact visual instruction from carousel script]"
    }
  ],
  "human_review_note": "[explicit reminder: review for text accuracy, visual cohesion, brand fit, swipe-earning before publish]"
}
```

## Quality Gate

- Does every slide's headline and body match `[CAROUSEL_SCRIPT]` exactly, with no paraphrasing introduced at this stage?
- Does the prompt specify exact slide count, layout rules, palette, and typography — not a vague style paragraph?
- Is `slide_count` in the output block identical to the number of entries in the `slides` array?
- Does `layout_rules` include an explicit hierarchy rule for when copy runs long, rather than assuming everything fits?
- Is the `human_review_note` present and substantive, not a placeholder?

## Creative Latitude

The JSON shape and the mandatory field list are the floor. Inside that: the visual_direction lines are where real design thinking lives — push past generic "supporting illustration" language into visual metaphors specific to each claim (the skill's own logic — article-becomes-cards, prompt-becomes-grid, brand-becomes-board — is a starting point, not a ceiling). When resolving a vague `[STYLE_DIRECTION]` into a concrete system, make genuine taste calls on palette and typography rather than defaulting to the premium-operator preset if the brand or audience calls for something else entirely.

## Deploy When

- A carousel script is finished and ready to become a structured design prompt for GPT Image 2 — before any actual image generation is triggered through the cost-gated visual route.
