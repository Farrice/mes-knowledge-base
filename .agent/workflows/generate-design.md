# Generate Design

End-to-end creative design generation — from concept to actual image. Chains the Creative Director's art direction intelligence through Gemini's Nano Banana 2 image model to produce world-class AI-generated visual assets.

## Expert Loading

Load `skills/creative-direction/SKILL.md` at Tier 1. For complex briefs, load `genius.md` for deep reference on visual language, art movements, and platform prompting.

## Two Modes

### Mode 1: Full Pipeline (Claude Code orchestrated)

When the user provides a concept and wants an actual generated image:

1. **Art Direct** — Apply the Creative Director's decision framework to the concept:
   - Establish Three Anchors (Visual Hook, Emotional Core, Cultural Anchor)
   - Choose aesthetic (specific art movement, cultural reference)
   - Define visual language (composition, color, lighting, typography)
   - Apply the Virgil Test to the direction

2. **Generate the Prompt** — Write a production-ready prompt using the Nano Banana 2 formula:
   ```
   [DETAILED SUBJECT], [PRECISE ENVIRONMENT], [SPECIFIC LIGHTING with direction],
   [CAMERA: lens, aperture], [COLOR TEMPERATURE], [MOOD], [STYLE REFERENCE]
   ```
   Rules: no vague words, front-load subject, describe light not mood, include technical specs.

3. **Execute Generation** — Run the Python pipeline:
   ```bash
   python execution/generate_design.py "concept description"
   python execution/generate_design.py --type apparel --style streetwear "concept"
   python execution/generate_design.py --iterate 3 "concept"  # with creative review loop
   ```

4. **Review Output** — View the generated image and apply the Virgil Test:
   - Tension? Cultural anchor? One-sentence concept? Subtraction test?
   - If score < 8, revise prompt and regenerate

### Mode 2: Prompt Only (for external platforms)

When the user wants prompts for Higgsfield, Kittl, Midjourney, or Flux (not Nano Banana):

```bash
python execution/generate_design.py --prompt-only "concept"
```

Or generate manually using the platform-specific formulas from SKILL.md/genius.md.

## CLI Reference

```bash
# Basic generation
python execution/generate_design.py "streetwear tee for My.BPM EDM brand"

# With type and style
python execution/generate_design.py --type logo --style swiss "AI agency mark"
python execution/generate_design.py --type apparel --style vintage-bootleg "DJ collective tee"
python execution/generate_design.py --type campaign --style cyberpunk "product launch hero"

# Control output
python execution/generate_design.py --aspect 16:9 --resolution 2K "LinkedIn banner"
python execution/generate_design.py --output deliverables/brand/logo.png "gravity logo"

# Iterate with creative review
python execution/generate_design.py --iterate 3 "album cover"

# Prompt only (no image gen)
python execution/generate_design.py --prompt-only "luxury streetwear lookbook"

# With reference image for style consistency
python execution/generate_design.py --reference prev_design.png "matching set piece"
```

## Design Types

| Type | What It Optimizes For |
|---|---|
| `general` | Any creative asset (default) |
| `logo` | Brand marks, icons, wordmarks |
| `apparel` | T-shirt, hoodie, hat graphics (streetwear archetypes) |
| `campaign` | Campaign hero images, key visuals |
| `social` | Social posts, stories, banners |
| `product` | Product photography, mockups |
| `editorial` | Fashion/editorial photography |
| `pattern` | Repeating patterns, all-over prints |
| `poster` | Posters, print art, wall art |

## Style Presets

| Preset | Aesthetic |
|---|---|
| `auto` | Creative director decides (default) |
| `cyberpunk` | Neon noir, tech dystopian |
| `swiss` | Clean grids, Helvetica, minimal |
| `streetwear` | Bold, high-contrast, edge |
| `vintage-bootleg` | Distressed, nostalgic |
| `brutalist` | Raw, anti-beauty |
| `luxury` | Elegant, restrained, premium |
| `vaporwave` | Retro-futurism, pastels |
| `afrofuturism` | African heritage + sci-fi |

## Output

Images saved to `deliverables/designs/` with companion `.json` metadata (creative direction, prompt, cost, tokens).

## Connection to Other Workflows

- `/art-direct` — Full 3-direction creative brief (manual, no generation)
- `/creative-prompt` — 3-variant prompts for any platform (Higgsfield, Kittl, MJ, Flux)
- `/design-spec` — Production specs for apparel/print (no generation)
- `/creative-review` — Critique existing work against Virgil Test
- `/generate-design` — THIS: concept -> art direction -> actual image

## Cost Notes

Each generation: ~$0.01-0.05 (creative direction via Flash + image via Nano Banana 2).
With `--iterate 3`: ~$0.03-0.15 (adds review + regeneration cycles).
Prompt-only mode: ~$0.001 (text generation only, no image cost).
