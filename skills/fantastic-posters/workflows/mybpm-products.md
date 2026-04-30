# Workflow: My.BPM Streetwear Posters

> **Brand**: My.BPM (mybpm.store) — EDM/PLUR streetwear
> **Use**: Product posters, drop announcements, festival-ready imagery
> **Default quality**: `medium` ($0.04/image) — social-grade, allows 2-3 variants per product
> **Bound to**: My.BPM ecommerce content pipeline

## Native-Fit Styles (auto-picker recommended)

| Style ID | When |
|---|---|
| `vaporwave-synth` | Retro-future drops, neon palette, summer launches |
| `neon-noir-cyberpunk` | Premium cyber/PLUR aesthetic, night-event tees |
| `streetwear-lookbook` | Editorial product photography vibe, model + product focus |
| `brutalist-broadcast` | Loud, high-contrast typographic drops, manifesto pieces |
| `cinematic-neonoir` | Atmospheric mood pieces, story-driven product launches |
| `album-cover-portrait` | Artist-collab merch, named drops |

## Brand Guardrails (always include in brief)

- **Color palette**: neon magenta, electric cyan, ultraviolet, deep black — cite hex if known: `--palette="#FF00FF,#00FFFF,#7B2FFF,#0A0A0F"`
- **Typography mood**: heavy sans-serif, condensed, rave-flyer aesthetics
- **Subject types allowed**: product (apparel), abstract logos/marks, abstract figures (avoid recognizable people)
- **Cultural register**: PLUR (Peace, Love, Unity, Respect) — never aggressive, never violent imagery
- **Avoid**: corporate clean, minimalism that reads "Apple keynote," country/folk aesthetics

## Standard Brief Template

```
"My.BPM streetwear poster for [PRODUCT NAME]. [PRODUCT TYPE: tee / hoodie / accessory] in [COLOR].
[MOOD: night festival / summer rave / underground warehouse / sunset]. EDM/PLUR aesthetic.
Neon palette, heavy condensed typography, atmospheric. No people's faces."
```

## Standard Run

```bash
# 1. Pre-flight
python3 execution/fal_budget_guard.py check --quality=medium --n=3

# 2. Generate 3 variants for selection
cd "/Users/farricecain/Google Antigravity/skills/fantastic-posters/" && \
  ./gen.sh "<brief from template above>" \
    --n=3 \
    --quality=medium \
    --palette="#FF00FF,#00FFFF,#7B2FFF,#0A0A0F"

# 3. Log
python3 execution/fal_budget_guard.py log --quality=medium --n=3 --status=success
# Cost: ~$0.12
```

## Final-Render Pattern (after picking the winner from variants)

```bash
# Re-render the winning style at high quality
python3 execution/fal_budget_guard.py check --quality=high --n=1
./gen.sh "<same brief>" --style=<winning-style> --quality=high
python3 execution/fal_budget_guard.py log --quality=high --n=1 --status=success
# Cost: $0.17
```

## Output Pipeline

1. Posters land in `skills/fantastic-posters/out/`
2. Move to `_active/mybpm/poster-drops/[date]/[product-slug]/`
3. Open in Canva via MCP for text edits / mockup placement
4. Export final to `mybpm-store/products/[product-slug]/poster.png`

## Cost Envelope per Product

- **Exploration phase**: 3 medium variants = $0.12
- **Final render**: 1 high quality = $0.17
- **Total per product**: ~$0.29
- **Budget for 30 products**: ~$8.70 (well under $20 wallet)

## Notes

- Logo placement: pass `--logo=path/to/mybpm-logo.png` to anchor the logo. Generator places it in upper-right by default.
- Reference brand book: when a PDF brand guide exists, pass `--refs=brand.pdf` (auto-renders page 1 to PNG at 2x DPI). Requires `npm install pdfjs-dist canvas` once.
- Avoid recognizable celebrity faces in briefs — Fal/GPT Image 2 will refuse or distort.
