# Claude Design Adapter

## Attach in this order

1. `00-READ-ME-FIRST.md`
2. `01-BRAND-FOUNDATION.md`
3. `02-DESIGN-CONTRACT.md`
4. `03-ASSET-STATE-LEDGER.md`
5. `tokens/design-tokens.json`
6. `tokens/asset-recipes.json`
7. `ai/UNIVERSAL-AI-BRAND-DIRECTOR-PROMPT.md`
8. `ai/REQUEST-BRIEF-TEMPLATE.md`
9. the closest editable SVG or PPTX template
10. the relevant contact-sheet example

Attach the private identity add-on only when the requested asset genuinely needs Farrice's portrait.

## Claude-specific working instruction

Use the supplied editable source as the structural parent. Preserve the existing grid, hierarchy, typography roles, and relative linked assets. Replace only the content or component explicitly named in the request.

Return one recommended design first. Do not generate a stylistic mood-board spread unless Farrice asks for exploration.

### For SVG work

- Keep linked image files beside the SVG or embed them deliberately.
- Preserve a 1584 × 396, 1920 × 1080, or 1080 × 1350 viewBox exactly when working from those templates.
- Use live editable text when Helvetica Neue is available.
- If Helvetica Neue is unavailable, keep the asset in `review` and report the substitution.
- Export a PNG at the native canvas dimensions.

### For PPTX work

- Preserve slide size and safe areas.
- Do not convert body text to screenshots unless the supplied source already uses flattened page artwork.
- The supplied carousel PPTX is a presentation container built from flattened page art; edit the page SVGs first, then replace the slide images.
- The supplied field-guide PPTX is the editable source for its typography and layout.

### For image-generation work

Use image generation only for nonrepresentational texture or atmospheric background fields. Generate a typography-free background, then place exact copy in the editable layout source.

## Delivery receipt

Claude should return:

- editable source;
- native-size export;
- font report;
- linked-file report;
- claim and identity report;
- thumbnail screenshot; and
- `draft` or `review` state.

