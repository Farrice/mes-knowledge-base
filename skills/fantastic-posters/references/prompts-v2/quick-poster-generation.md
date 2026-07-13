---
name: "Fantastic Posters — Quick Poster / Image Generation"
source_prompt: born-v2
skill: fantastic-posters
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running the fantastic-posters generator's direct path: read the brief, identify its mood and
subject, pick the single best-matching visual style from the 38-style catalog, build the prompt, and
render via GPT Image 2 (through Fal). This is the lightweight path — a quick draft, a template
replicate, or a single client brief that doesn't need the full Studio's divergence/critique
ceremony. Real client work is the primary use case here: use real brand names when supplied, only
anonymize for generic demos.

## Input Required

- **[BRIEF]** — the subject and intent (event / product / album / movie / listing / retreat) plus mood (calm / vibrant / nostalgic / mystical / luxury / corporate / playful).
- **[STYLE_OVERRIDE]** — a specific `styles.js` id if the user names one, or AUTO (use the Style Picker).
- **[BRAND_GUARDRAILS]** — optional: palette (hex list), typography mood, subject types allowed, cultural register, an explicit avoid-list — supply when the brief belongs to a recurring brand identity.
- **[REFERENCE_ASSETS]** — optional: hero photo / brand-book PDF / logo paths for `--refs`, in order (hero, then brand book, then logos), or NONE.
- **[LOGO_PATH]** — optional exact wordmark to anchor via `--logo=`, or NONE.
- **[VARIATION_COUNT]** — default 1; N if the user asks for "more designs" or "variations."
- **[SIZE]** — portrait (default) | landscape | square | banner-3to1 | hero-2to1 | poster-xl | WxH.
- **[QUALITY]** — low ($0.011, drafts) | medium ($0.04, client review) | high ($0.17, final delivery).

## Execution Protocol

1. **Read the brief and identify mood + subject.** Mood: calm / vibrant / nostalgic / mystical / luxury / corporate / playful. Subject: event / product / album / movie / listing / retreat.
2. **Pick the style.** Match the brief's intent against the Style Picker below (first confident match wins). If a `[BRAND_GUARDRAILS]` set is supplied, weight the picker toward styles that carry the brand's stated register (e.g., neon/PLUR guardrails point at `vaporwave-synth`, `neon-noir-cyberpunk`, `streetwear-lookbook`, `brutalist-broadcast`, `cinematic-neonoir`, `album-cover-portrait`). If nothing matches confidently, offer the user a 3-option shortlist rather than guessing.

   | Brief is about... | Style |
   |---|---|
   | moody crime / thriller / dark cinematic | `cinematic-neonoir` |
   | travel / destination / vintage tourism | `vintage-travel` |
   | design lecture / minimal swiss / typography | `swiss-minimal-typo` |
   | tech conference / agentic web / dev event | `tech-conf-darkmode` |
   | annual report / executive / finance | `corporate-report` |
   | live music / DIY gig / underground band | `indie-gig-riso` |
   | home listing / open house with photo | `luxury-real-estate` |
   | luxury estate brochure / architectural retreat | `luxury-estate-cover` |
   | art deco / Gatsby / 1920s glam | `art-deco` |
   | Bauhaus / primary geometric / design school | `bauhaus-geometric` |
   | Japanese woodblock / Edo / classical Japan | `ukiyo-e` |
   | sixties rock / Fillmore / hippie concert | `psychedelic-60s` |
   | synthwave / retro futurism / 80s sunset | `vaporwave-synth` |
   | minimalist film / cut-paper / Hitchcock vibe | `saul-bass-minimal` |
   | 80s postmodern / playful clashing patterns | `memphis-80s` |
   | high fashion magazine / editorial cover | `editorial-fashion` |
   | symmetric pastel / dollhouse / storybook film | `symmetric-storybook` |
   | comic / Ben-Day dots / pop art | `pop-art-comic` |
   | wellness / meditation / retreat / soft calm | `pastel-mindful` |
   | zen / Japanese ink / monastic minimal | `sumi-e-zen` |
   | Día de los Muertos / Mexican folk / festival | `loteria-folk` |
   | surreal / Magritte / dreamlike | `surreal-dreamscape` |
   | documentary / Magnum reportage / photo essay | `documentary-portrait` |
   | stadium / race / athletic event campaign | `sports-action-hero` |
   | album cover / vinyl / soul-funk debut | `album-cover-portrait` |
   | post-apocalyptic action game key art | `post-apoc-sword` |
   | melancholic sci-fi wanderer / cargo / Iceland | `lone-traveler-cargo` |
   | cyberpunk / neon noir / dystopian megacity | `neon-noir-cyberpunk` |
   | streetwear lookbook / drop / collection | `streetwear-lookbook` |
   | tech product reveal / keynote / Apple-style | `minimal-tech-keynote` |
   | brutalist / broadcast / jersey-number / HYROX-style | `brutalist-broadcast` |
   | restaurant / wine bar / jazz lounge / brasserie | `emerald-nocturne` |
   | absurd transit map / mood diagram (experimental) | `absurd-transit-map` |

3. **Out-of-Left-Field mode** — if the request is "out of left field," "weird," "different," "surprise me," or "experimental," catalog defaults are forbidden. Vary palette and typography away from catalog norms, pull inspiration from less-obvious references via web research (Polish theatre posters — Lenica, Tomaszewski; Japanese book covers — Sugiura, Yokoo; Czech New Wave; AIGA annuals; Dribbble experimental), and propose 5+ one-line-vibe ideas before generating — never default to a safe catalog pick.
4. **Show the reference render.** Before generating, show `examples/<style-id>.png` — never regenerate the catalog showcase; the reference render is the baseline.
5. **State the pick.** Tell the user which style was chosen and why, in one sentence.
6. **Handle logos, if any.** Pass as base64 data URI via `--logo=<path>` (handled automatically); this routes to the edit endpoint and adds the "do NOT redraw, recolour, or modify proportions" clause automatically. For dual-wordmark layouts (client + partner), specify equal visual weight separated by a hairline rule — never combined into one lockup. Logo placement is imperfect even on the edit endpoint — flag for human review.
7. **Handle references, if any.** Order is load-bearing: image 1 = hero photo, image 2 = brand book (PDF auto-renders page 1 at 2x DPI), image 3+ = logos. For `--template` mode: template first, new hero photo second, optional logos after. With `--template` or any multi-ref edit, the shortest prompt naming ONLY what changes outperforms verbose specs — trust the reference to carry layout, typography, palette, and logo.
8. **Keep titles short.** GPT Image 2 is strong on typography but not perfect — a title over ~6 words risks typos. Footer line, if present, is always last: date · venue · price/credit.
9. **Set variations correctly.** If `[VARIATION_COUNT]` > 1, vary the subject slightly across variations rather than repeating the same prompt with a color nudge.
10. **Run the command** and state the estimated cost before confirming. The CLI always prompts for confirmation on ≥5 images or `--quality=high`, regardless of `--yes`.

```bash
cd <repo-root>
node generate.js "<brief>" [--style=<id>] [--n=<N>] [--variants=<1-4>] \
  [--refs=hero.jpg,brand.pdf,logo.png] [--logo=<path>] [--template=<existing.png>] \
  [--size=portrait|landscape|square|banner-3to1|hero-2to1|poster-xl|WxH] \
  [--quality=low|medium|high] [--palette="#hex,#hex"] [--rembg]
```

11. **Deliver.** Give the file path and remind: open in Canva and use Magic Layers to split foreground/background/text if editing is needed. PSD layering and upscaling are out of scope for this skill — route to `poster-to-layers` and Topaz/Real-ESRGAN respectively.

## Output Contract

The chosen style + one-sentence reasoning; the exact `generate.js` command with real flags only; the
pre-run cost estimate; the output file path(s) once rendered; the post-generation Canva reminder.

## Output Skeleton

```markdown
**Style picked**: [style-id] — [one-sentence why]
**Reference shown**: examples/[style-id].png
**Command**:
`node generate.js "[brief]" --style=[id] [--refs=...] [--logo=...] --size=[size] --quality=[tier] [--n=N | --variants=N]`
**Estimated cost**: $[n] ([tier] × [count] images)
**Output**: out/[filename].png [+ alpha variant if --rembg]
**Post-gen**: open in Canva → Magic/Smart Layers to split foreground/background/text if editing is needed.
```

## Quality Gate

- [ ] The style was matched to the brief's stated mood/subject (or the user's explicit override) — not forced onto the first keyword hit.
- [ ] Title (if any) is ≤6 words; footer (if present) is last and carries date/venue/price-credit.
- [ ] Reference image order follows the hero → brand-book → logo(s) convention when `--refs` is used.
- [ ] Cost was estimated and stated before the run; ≥5 images or `--quality=high` was never auto-fired past the confirmation prompt.
- [ ] Multiple variations vary the subject, not just a color/framing nudge on one prompt.
- [ ] Out-of-Left-Field requests did not fall back to a catalog default.

## Creative Latitude

Within the chosen style's frame, push on how the subject is depicted, not just what label is applied
— a "luxury-real-estate" pick still needs a genuinely considered composition and light quality, not
a generic fill-in. In Out-of-Left-Field mode, the latitude is explicit: research and name a real,
specific, less-obvious design lineage rather than defaulting to the 38-style catalog, and propose
several genuinely different one-line vibes before generating. When brand guardrails are supplied,
find the version of the style that honors the register (PLUR, luxury-restrained, etc.) without
reading as a template fill of the guardrail list.

## Deploy When

A quick draft or single client brief is needed without the Studio's full divergence/critique
ceremony; a proven layout is being replicated via `--template`; a recurring brand needs a fast,
guardrail-consistent poster; the user explicitly asks for "a poster," "an edit," "a transparent
logo," or names one of the 38 styles directly.
