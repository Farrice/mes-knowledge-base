# Joey (Noisy Group / Control World) — Unified Genius Context

> Extraction: 2026-07-13 forge from 3 videos + Notion v3 doc + Joey's Skill Files v3.0.
> Full report: `extractions/joey-cinema-os/extraction-report.md` · deep skill-file analysis: `extractions/joey-cinema/skill-files-analysis.md` · real published artifacts: `extractions/joey-cinema-os/reference-corpus/`
> The three production skills install as siblings and carry the LOCKED verbatim grammar — this file carries the judgment layer. Never re-implement their blocks here; load them: `skills/banana-pro-director/SKILL.md`, `skills/cinema-worldbuilder-pro/SKILL.md`, `skills/story-bible-builder/SKILL.md`.

## Who

Joey — professional filmmaker (brand/ad work) who built **Control (CTRL)**, a fully AI-generated K-pop group with published music videos, and gave away the entire production pipeline as free Claude skills ("the pipeline is the actual product, the video is just a demo"). 40 → ~25k subs in months, unmonetized, anti-gatekeeping, anti-slop ("momma didn't raise AI slop"). Collaborator **KY** — formally trained fashion designer who imports real fashion-industry documentation (spec sheets, Adobe technical flats, measurements) into the AI pipeline.

## Core Genius

**Consistency is an asset discipline, not a model feature.** Move every load-bearing decision OUT of the prompt and INTO locked upstream artifacts — bibles (who), face locks + canonical sheets (what they look like), flat reference plates (what carries into the frame), block-structured video prompts (what happens on screen). Each generation becomes a cheap, disposable read of expensive, permanent context. The layers never do each other's jobs: the bible refuses cinematography, Banana Pro refuses to bake lighting, the worldbuilder refuses to re-describe what a reference shows.

## The Pipeline (strict order — CANON → STILLS → MOTION)

```
story-bible-builder        once per world: identity, voice, movement/stillness,
      │                    era palettes, production rules, "never" clauses
      ▼
banana-pro-director        per asset, strict order: Mode 0 face lock → Mode 1 outfit
      │                    base → Mode 2A 3-panel sheet → Mode 3 scene plates
      ▼                    (Modes 4 GPT-2 detail / 5 outfit swap = gated utilities)
cinema-worldbuilder-pro    per shot: block-structured Seedance prompts consuming
                           canonical refs as @tags + bible descriptors as payloads
```

Don't skip steps. Don't combine steps. Unbuilt character in a video request → kick back to Banana Pro. No bible on a multi-scene world → build one first or accept drift knowingly (say so).

## Genius Patterns (the 24 — compressed; full versions in extraction report + analysis §3)

**Reference/asset physics**
1. **References carry identity; prompts carry framing.** One visual handle per subject; a 2,500-char prompt with strong refs beats 5,000. If a sentence re-describes what a reference shows, cut it unless load-bearing for composition.
2. **Reference plates carry ZERO lighting information.** Baked shadows are "inherited and amplified" downstream and fight the scene's light. Identity assets are catalogue-flat; lighting is applied exactly once, at the final render.
3. **Lower subject-background contrast for downstream edge stability.** 18% gray beats white: video models amplify mistakes at high-contrast edges (halo, edge breathing). Choose asset defaults for the NEXT stage's failure modes.
4. **Face size controls drift.** One face per reference, as large as the format allows; garments get a face-free (headless) panel; competing faces deleted. 3-panel beats 6 on pixel-budget math (~2× resolution per cell).
5. **Canonical-over-plate.** Plates carry world; canonical refs carry identity — every named subject gets its own reference even when visible in the plate.
6. **Real documentation beats vibe prompts (KY).** Technical flats, measurements, all angles, per-character/product palette sheets WITH colors-to-avoid. Budget ~50 gens for the hardest garment, knowingly.

**Prompt physics**
7. **Write the visible.** km/h not "fast"; % haze + meter visibility; scale in stacked humans; emotion in muscle ("knuckles blanch"). "If a word doesn't produce a visible pixel, cut it."
8. **The prompt bell curve.** More ≠ better; less ≠ control. Past ~3 failed iterations: cut it, reset it, let it breathe, re-add only what's necessary.
9. **Position in the prompt is instruction.** Composition loads the front (Banana Pro reads the front heaviest); camera/FOV lock sits at the bottom; style distributes to home blocks — a style prefix "scatters the model's attention."
10. **Discrete anchors beat continuous suggestions.** FOV in degrees not mm ("47° holds, 50mm drifts" — degrees read as instruction, mm as suggestion); timed cuts; hex palettes; contrast stated three ways. Quantized instructions hold; analog ones decay.
11. **Positive phrasing except sanctioned end-position negations.** "The model sees the noun and rounds toward it" — prohibitions become descriptions of what IS; known-failure suppression lists go at the END where they read as quality filters.
12. **Resolution-aware detail.** Describe what THIS camera at THIS distance can physically resolve, not what's "true" about the subject.
13. **Absence is not a directive — name the null.** "Nothing else moves" is stated per motion layer; "the camera does not add any additional cuts" closes the door.
14. **Timestamped beats inside one generation.** "Heels hit the ledge at 7.0s... again at 11.0s" + per-beat speed treatment; hard cut at every speed change.

**Canon/context discipline**
15. **Names drift; descriptions survive.** No character names, brands, ages, or platform names in any prompt — models don't know names; visual descriptors survive across prompts.
16. **Locks exclude as much as they include.** "Warm fair skin — never pale porcelain, never tan." Name the wrong-answer drift inside the lock or it won't hold over hundreds of renders.
17. **Never invent — [TBD] beats plausible.** "Invented canon becomes locked canon becomes prompt drift."
18. **Prompt-ready quoted payloads.** Bible descriptors must paste verbatim into their downstream slot (Speech → Sound Bed, Movement/Stillness → Subject Lock) or they're written wrong.
19. **The stranger test.** "Could a stranger who has never heard of this story write a scene in it, using only this bible, and get it right?"

**Taste/economics**
20. **The flattering-realism ceiling.** Matte fights plastic; fine-and-even fights ugly; both always on; ties resolve toward flattering. Realism without the ceiling = dermatology photo.
21. **Credit economy as design constraint.** Duration declared per prompt; shot plans costed before generation; the honest win is 8-10 takes → 2-3, never "one-shot magic."
22. **Confirmation gates scale with blast radius.** Pre-prompt check (references listed FIRST) before every expensive prompt; minor iterations skip it — "re-confirming on tiny deltas creates friction."
23. **Silent structure, prose surface.** Checklists and coordinate grids stay internal; output is confident DP prose — "the model responds to confident scene description, not coordinate grids."
24. **Fake-BTS worldbuilding.** Behind-the-scenes-that-never-happened, domestic slice-of-life, era emulation — a synthetic world reads real through mundane *context*, not just render fidelity.

## Hidden Knowledge

- **3-shot/15-second story test:** grab → emotional payoff → unresolved questions. Judge by question count ("why does he back down?" ×4 = winner). Resolution is not the win condition.
- **Voice consistency is a context problem** — bible voice/timbre/cadence descriptors into every prompt; don't wait for model features.
- **Native 4K ≠ 720p upscaled** — resolution is a generation-time decision.
- **Register flip for video-to-video (Omni):** ≤10s real footage, plain imperative prompts ("keep me exactly the same, change X"). Generation prompts are dense; edit prompts are simple.
- **Economics:** ~117 credits/13s 1080p Seedance gen; 200-300 credits per studio piece; 5-6k per music video.

## Signature Moves

- **Reset Ritual** — bloated prompt → cut, breathe, re-add minimum. *Deploy: iteration ≥3 failing.*
- **References First** — pre-prompt check lists refs before anything; missing ref caught before ship. *Deploy: any multi-ref composition.*
- **The Existence Question** — "does this character/product already exist, or are we developing it?" *Deploy: session start.*
- **Cost Before Generate** — declared durations, costed shot plans. *Deploy: any paid generation.*
- **One Variable Per Shot** — reference series vary exactly one parameter; identity stays locked. *Deploy: asset libraries.*
- **Kick to the Right Layer** — never do another layer's job. *Deploy: cross-layer temptation.*

## Quality Rubric (anchor before shipping any pipeline output)

| Criterion | 4 | 7 | 10 |
|---|---|---|---|
| Identity persistence | 3 shots | full scene, no re-rolls | full video incl. wardrobe/action/era |
| Reference discipline | refs attached | refs carry identity, prompt carries framing | zero re-description, flat plates, canonical-over-plate |
| Anti-AI-render physics | no plastic skin | matte + grain + rolled highlights | full stack + flattering ceiling + "photographed not generated" |
| Write-the-visible | some measurables | km/h, %, meters, muscle emotion | every word = visible pixel, resolution-aware |
| Prompt economy | under limits | bell-curve tuned, front-loaded | lean prompt + strong refs; reset reflexive |
| Credit economy | costs tracked | durations declared, plan costed | 2-3 takes; hard assets budgeted knowingly |
| Story grip | coherent | timestamped beats | 15s: grab → payoff → unresolved "why"s |
| World believability | consistent look | era/palette locks | fake-BTS/mundane texture reads documentary-real |

## Anti-Patterns (Joey would reject — each sourced; ledger: `references/source-ledger.md`)

- Style-keyword slop ("8k, masterpiece, cinematic") — fails write-the-visible: "If a word doesn't produce a visible pixel, cut it" (cinema-worldbuilder SKILL.md, 2026-07-13 install).
- Names, brands, or ages in prompt output — "Higgsfield does not know names. Visual descriptors survive across prompts; names do not" (banana-pro-director SKILL.md, Naming rule).
- Style header at the top of a prompt — "Putting a style prefix on the prompt scatters the model's attention" (cinema-worldbuilder, DISTRIBUTED STYLE).
- Re-describing what an attached reference shows — "double-weight prompts that dilute the photographic direction" (banana-pro-director, reference-reading doctrine).
- Baking lighting/shadow into a reference plate — baked shadows get "inherited and amplified by every downstream generation" (banana-pro-director, flat-grade rationale); white seamless for video-bound assets — "video models amplify small mistakes most at high-contrast edges" (same section).
- 6-panel sheets by default — "Six cells splits that budget six ways" (banana-pro-director, Mode 2A rationale); more than one face on an identity reference — "where did bird head go?... one face on the reference sheet instead of two" (video x5nP-3t6R9o transcript).
- Patching a bloated prompt instead of resetting it — "cut it, reset it, let the prompt breathe" (video x5nP-3t6R9o, bell-curve doctrine).
- Generating before the shot plan is costed — durations declared per prompt, ~117 credits/13s 1080p observed (video 0YhhPQVXA7c UI frame); skipping the existence question (banana-pro-director, Step 0).
- Inventing canon to fill a gap — "Invented canon becomes locked canon becomes prompt drift" (story-bible-builder); locks without "never" clauses — "'Warm fair skin — never pale porcelain, never tan'" (same).
- "Fixing" the sanctioned end-position negation blocks into positive phrasing or scattering them upward — negations at the end read "as a quality filter rather than a conflicting instruction" (banana-pro-director, Mode 3).

## Recognition Test

Before shipping any output from this skill, ask: **would Joey recognize this as his — a prompt he'd hit Copy on and paste into Higgsfield without edits?** Concretely: does it read like the amber-PVC-raincoat sheet prompt or the '33'-jersey character prompt (`extractions/joey-cinema-os/reference-corpus/`) — construction-language wardrobe, one visual handle per subject, measurables not moods, the locked closes intact, nothing a reference already carries? If a stranger comparing it against those two corpus pieces could pick out yours as the imitation, it fails — find the tell (usually: re-described references, a mood word, a missing "never" clause) and fix it.

## System Fit (this workspace)

- **Execution surfaces:** Higgsfield MCP (`generate_image`, `generate_video`, `show_characters`, `show_reference_elements`) = Joey's native surface, @tags work here. Fal wrappers (`fal_video_seedance.py` etc.) = no @tags; strip to prose descriptors. All generation stays behind the existing cost gates — these skills are prompt-only ("the skill's job ends at the code block").
- **Disambiguation (critical):** Joey's "GPT-2" = **Higgsfield GPT-2** (face-fidelity king, credit-heavy). The system's `gpt-image-2-director` = **OpenAI GPT Image 2** (layout/typography king, weak faces). Opposite verdicts; never conflate.
- **Division vs existing lanes:** fantastic-posters = stylized/typographic Fal lane (keep); gpt-image-2-director = layout/text density (keep); joey pipeline = photoreal persistent-world/character/product lane. Fantastic-studio stages 04-05 route photoreal-people and Seedance work into these grammars.
- **Product transfer (Farrice's core use):** face lock ≈ hero-angle lock; 3-panel sheet ≈ product turnaround; bible ≈ brand canon; KY method ≈ client product documentation. This is how "product-grade output" happens for MyBPM, Jen, TrendScale.
