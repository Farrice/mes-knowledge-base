# Fantastic Studio — Genius Context

> **Unified genius context for the fantastic-posters skill (v2 "Studio" elevation, 2026-07-04).**
> Load this before any Studio workflow. It is the operating system that turns a capable image generator into a **concept-first, multi-model, divergent, self-critiquing creative engine**.

**Domain**: AI image + video generation for brand/creative work — posters, identity, social, product, packaging, motion.

**What changed in v2**: v1 was a strong pair of hands (`generate.js`: 38 styles, edit/mask, refs, variants, rembg, sizes, video bridge) bolted to a thin brain (`pickStyle()` keyword-matches one template; `--n` nudges "shift colour accent"). v2 inserts a real creative-direction brain in front and opens the full model surface behind.

---

## How to Use This Skill (Model Calibration)

These eight stages are intuition primitives, not a checklist to march through out loud. Absorb the divergence discipline (real strangers, not tinted siblings) and the reference-lineage habit (a named designer, not "modern/clean"), then work from concept, not from template.

The test: would a working art director — the kind who names Müller-Brockmann or Saul Bass without reaching for Wikipedia — recognize this as theirs, a reference-grounded, orthogonally-diverged piece of design thinking? Or would they recognize it as generic keyword-template output wearing 38-style vocabulary? If it's the second, rebuild from Stage 1 (reference-ground), not from a palette override.

Specifically:
- Do NOT narrate "Stage 2: Art-Direct, Stage 3: Divergence" inside the delivered creative unless the user asked to see the pipeline itself. Execute the thinking; don't caption the machinery on the page.
- Do NOT label a compiled prompt "here's the anti-slop move" or "here's the leverage point." Land it in the scene description; naming it is the tell that a template filled the form instead of a concept driving it.
- This skill's texture is tool-honest, not tasteful-by-default — GPT Image 2 and Higgsfield are instruments a director points, not oracles that already have taste. A prompt that reads like a keyword stack ("moody, cinematic, professional, 4k") is the single-model, one-shot failure this build exists to kill; compile one fully-realised scene, never a tag list.
- Polish is the tell here too, inverted: an anti-slop pass that removes every imperfection re-produces the AI-perfect template lane this skill exists to escape. The ≥3 deliberate human-imperfection moves (WF-02 move 7) are load-bearing, not garnish — a "clean" render that skipped them has failed the anti-slop lens even if nothing else is wrong.

---

## The Underlying Belief

> **Satori decides. The router picks the instrument. The studio critiques its own work.**

Generation is abundant and cheap; *taste* is the moat. A model will happily render the generic version forever. The value is in the thinking *before* the prompt (concept, hierarchy, color, feeling) and the judgment *after* the render (critique, refine). The image model is an instrument, not the composer.

Three failure modes v2 exists to kill:

| Failure | Symptom | v2 fix |
|---|---|---|
| **Template brain** | keyword → 1 of 38 styles → fill blanks | Art-direction spec from the **satori brain** (WF-02) |
| **Tint divergence** | `--n` = "shift colour accent" → same idea 3× | **Divergence spread** on 6 orthogonal axes (WF-03) |
| **One model, one shot** | GPT Image 2 only, accept first output | **Model route** (WF-04) + **critique/refine loop** (WF-07) |

---

## The Pipeline (8 stages + front door)

`/fantastic-studio` (WF-00) orchestrates:

```
BRIEF
 → 1 REFERENCE-GROUND   real high-taste lineage, not model default        (WF-01)
 → 2 ART-DIRECT         satori brain → art-direction spec                  (WF-02)  ← the anti-generic move
 → 3 DIVERGENCE SPREAD  N orthogonally-distinct directions                 (WF-03)  ← the anti-redundancy move
 → 4 MODEL ROUTE        each direction → the right tool                    (WF-04)  ← take full advantage of the surface
 → 5 PROMPT COMPILE     spec → model-specific prompt (+ Fal --brief JSON)  (WF-05)
 → 6 GENERATE           cost-gated, human-triggered runbook                (WF-06)
 → 7 CRITIQUE + REFINE  Virgil × LIFT × type × anti-slop → mask edits       (WF-07)  ← first output → remarkable
 → 8 FORMAT PACK        one concept → feed/story/hero/print/cutout/motion  (WF-08)
```

Stages 1-5 and 7-8 are **free** (thinking). Only stage 6 spends money, and only behind the cost gate + a human yes.

---

## The Capability Map (use every lever ON PURPOSE)

The current skill under-uses its own hands. Here is the full surface; a Studio job should reach for the *right* lever, not default to plain text-to-image.

### `generate.js` (GPT Image 2 via Fal) — run from repo root with `FAL_KEY` in env
| Lever | Flag | Use it for |
|---|---|---|
| Style DNA | `--style=<id>` | Start from one of 38 lineage primitives (blend, don't keyword-lock) |
| **Distinct takes** | `--n=N` | N separate calls w/ diversity nudge — *only after* WF-03 gives distinct prompts; never as the divergence engine itself |
| **Cheap siblings** | `--variants=1..4` | N images, 1 API call — cheapest way to see siblings of a *chosen* direction |
| Multi-reference | `--refs=hero,brand.pdf,logo` | hero photo + brand book (PDF auto-renders) + logos |
| Exact wordmark | `--logo=<path>` | logo-anchored edit, no redraw |
| Replicate layout | `--template=<png>` | reuse a proven layout; shortest prompt naming ONLY changes |
| **Edit** | `--input=<url\|path>` | modify an existing image; describe only the change |
| **Surgical edit** | `--mask=<bw png>` | region edit (white=edit, black=preserve) — the refine-loop workhorse; fixes garbled text without re-rolling the whole image |
| **Transparency** | `--rembg` | logos, stickers, cutouts → `*_alpha.png` (+~$0.005) |
| Format | `--size=portrait\|landscape\|square\|banner-3to1\|hero-2to1\|poster-xl\|WxH` | one concept → many deployments (multiples of 16, ≤3:1, 655K–8.3MP) |
| Palette | `--palette="#hex,#hex"` | override with the satori color tokens |
| **Structured brief** | `--brief=spec.{md,yaml,json}` | **how the compiler hands a rich art-direction spec to the generator** (keys: style, subject, title, subtitle, body, footer, palette, logo) |
| Batch | `--batch=list.json` | many briefs at once |
| Quality | `--quality=low($0.011)\|medium($0.04)\|high($0.17)` | draft cheap → promote the winner |

### Beyond GPT Image 2 (the surface the v1 skill ignored)
- **Higgsfield Soul** — best **photoreal + PEOPLE / character consistency / product hero** (`creative_router` → `higgsfield-soul`, ~$0.10). MCP: `mcp__claude_ai_Higgsfield__generate_image`.
- **Higgsfield Nano Banana Pro** — fastest/cheapest **iteration + concept sketch** (`higgsfield-nano`).
- **Higgsfield models_explore** — `action:'recommend'` when unsure which Higgsfield model fits.
- **Video** — `fal-kling` (multi-shot narrative, $2 ceiling) · `higgsfield-cinema` (cinematic, $1.5) · `fal-seedance-720p` ($3 ceiling; **1080p HARD-BLOCKED**) · `veo-3` (premium, Ultra quota). Bridge: any still becomes a video start-frame.
- **Virality** — `higgsfield-virality` to pre-score a creative's engagement.

### The router is the pre-flight brain
`python3 execution/creative_router.py route --task "<direction>" --json` → service + reason + cost-gate command. First match wins; specific patterns first. Do not hand-pick a model without checking the router — it encodes Farrice's routing taste.

---

## The 6 Divergence Axes (the anti-redundancy engine — WF-03)

A "spread" that changes only colour is a **tint, not a divergence**. Real directions vary along ≥2–3 *orthogonal* axes:

| Axis | Vary by | Source |
|---|---|---|
| **A1 Concept angle** | different hidden-truth / technique per direction | satori concept engine (hidden-truth · one-big-idea · what-if · emotion-over-info · literal · tiny-detail) |
| **A2 Art lineage** | different movement/designer reference | reference library below |
| **A3 Composition** | type-dominant · image-dominant · negative-space · asymmetric-collage · symmetric | satori LIFT leverage strategy |
| **A4 Color strategy** | fit-in · stand-out · monochrome · high-contrast | satori 5-layer color |
| **A5 Medium / model** | GPT Image 2 · Higgsfield Soul · Nano · Flux · video | exploits the model surface AND diversifies |
| **A6 Register / feeling** | premium-restrained · loud · playful · eerie | satori feeling-calibrate |

**Rule**: 3–5 directions; any two collapsible into the same one-sentence concept → kill one and regenerate. The spread is graded on *distinctness*, not count.

---

## Model-Routing Decision Tree (WF-04)

```
Is it TYPE-led / stylized / text-in-image / a poster?      → fal-poster (GPT Image 2, 38 styles)
Is it PHOTOREAL + PEOPLE / product hero / needs a face?    → higgsfield-soul  (attach a character ref for consistency)
Just scouting cheaply / many quick concepts?               → higgsfield-nano
Editing an existing image?                                 → fal-edit  (--input [+ --mask])
Need transparency / a cutout / a logo on alpha?            → fal-rembg  (--rembg)
Motion?  multi-shot → fal-kling · single cinematic → higgsfield-cinema/seedance-720p · premium → veo-3
Unsure which Higgsfield model?                             → mcp Higgsfield models_explore action:'recommend'
```
Cheap-first always: draft at `--quality=low` / Nano → critique → promote the survivor to medium → high.

---

## Reference Lineage Library (the high-taste anchor — WF-01)

Anchor in real craft so output isn't generic-model-default. Blend the *transferable move*, never copy the artist.

| Lineage | Named references | Transferable move |
|---|---|---|
| **Swiss / International** | Müller-Brockmann, Josef Müller, Emil Ruder | grid discipline, one dominant element, ruthless hierarchy, type-as-structure |
| **Polish poster school** | Jan Lenica, Henryk Tomaszewski, Roman Cieślewicz | metaphor + hand, surreal concept, painterly type |
| **Japanese** | Tadanori Yokoo, Kohei Sugiura, Ikko Tanaka | dense collage OR extreme restraint, flat color planes, cultural symbol |
| **Saul Bass / mid-century** | Bass, Paul Rand, Herb Lubalin | cut-paper simplicity, one witty visual idea, expressive lettering |
| **Editorial / fashion** | Fabien Baron, Alexey Brodovitch, current mastheads | white space, scale contrast, confident type, photographic restraint |
| **Risograph / DIY** | indie gig posters, zine culture | limited spot palette, off-register, halftone, human imperfection |
| **Contemporary system** | Experimental Jetset, Pentagram, Bass-modern | concept-as-system, one idea across every touchpoint |

Use WebSearch/WebFetch to pull a *specific* lineage when the brief needs a niche (AIGA annuals, Czech New Wave, Loteria folk, etc.). The 38 `styles.js` entries are curated lineage primitives — map to the closest 1–3 as starting DNA.

---

## Art-Direction Prompt Architecture (WF-02 → WF-05)

A great prompt is a *compiled art-direction spec*, not a keyword string. Every direction carries:

1. **Concept + hidden truth** (satori) — what the image is *about*, in one sentence.
2. **Subject / scene** — the concrete depiction.
3. **Composition + leverage point** (LIFT) — what the eye hits first; the 10 m / 5 m / 1 m recognition ladder.
4. **Color tokens** — the satori 4-role palette as hex (`--palette` / brief `palette`).
5. **Type treatment** — hierarchy; ≤6 words for reliable GPT Image 2 lettering; consider the 5 typography-first presets where *lettering IS the picture*.
6. **Lighting / lens / texture** — direction, quality, grain, finish.
7. **Negative space** — the premium lever; what's deliberately empty.
8. **Memory hook** (satori GP-03) — the one thing that makes it resolve/stick.
9. **Anti-slop moves** (satori GP-11) — ≥3 human imperfections so it escapes the AI-perfect template lane.
10. **Cultural anchor** — the named reference from WF-01 (the Virgil Test demands it).

**Model-specific compilation**: Fal → `--brief` JSON or `--style` + custom prompt. Higgsfield Soul → subject + wardrobe/character + environment + lighting + lens + mood + color, character ref attached. Nano → the same, shorter. Edit → `--input` + describe-only-the-change. Video → start-frame + camera/motion.

---

## The Critique Rubric (WF-07 — the loop that makes it remarkable)

Never accept the first render. Score each output on four lenses; decide **SHIP · REFINE · REGENERATE**.

1. **The Virgil Test** (creative-director): clear POV? real tension? a *named* cultural anchor (not generically "nice")? concept in one sentence? would removing an element strengthen it? interesting *without* the logo?
2. **LIFT audit** (`/satori-lift-audit`): leverage point wins in <2s? eye journey choreographed? friction serves? transfers to thumbnail + light/dark + ≥2 formats?
3. **Type / legibility**: title ≤6 words rendered clean? hierarchy readable at 10/5/1? any garbled lettering? (GPT Image 2's known weak spot — fix via masked re-render, not a full re-roll.)
4. **Anti-slop** (`/satori-anti-ai-slop`): AI-perfect symmetry/gloss? ≥3 human-imperfection moves present? memory hook intact?

**REFINE > REGENERATE**: a targeted `--mask` edit (fix the text region, evict a weak element, adjust one zone) is cheaper and preserves what worked. Only regenerate when the concept itself failed. Loop max 2–3 passes; escalate quality (low → medium → high) only on survivors.

---

## Cost Discipline (non-negotiable — physical gate)

- **Never auto-fire paid generation.** Every paid call: `cost_gate.py check` → (needs-approval → surface to Farrice → explicit yes → `cost_gate.py approve`) → run → `cost_gate.py log`.
- Video also: `fal_budget_guard.py check --mode=<...> --duration=<N>` first.
- **seedance-1080p is HARD-BLOCKED** at the script level (~$10/call). Denied = surface + stop, do not retry. An approve token lasts ~15 min.
- **Draft cheap, promote the winner.** `--quality=low` / Nano to scout; `--variants` for cheap siblings; medium for review; high only for finals (then upscale externally — Topaz/Real-ESRGAN, not in this skill).
- The Studio pipeline PRODUCES the routed plan + ready commands; Farrice pulls the trigger.

---

## Anti-Patterns (auto-reject)

1. **Keyword-template brain** — `pickStyle` → fill blanks, no concept. Run WF-02 first. This is the diagnosed v1 failure this genius.md opens with (v2 "Studio" elevation, 2026-07-04): v1 was "a strong pair of hands... bolted to a thin brain (`pickStyle()` keyword-matches one template; `--n` nudges "shift colour accent")."
2. **Tint divergence** — "3 variations" that share one idea. Diverge on ≥2 axes (WF-03).
3. **One-model reflex** — GPT Image 2 for a job Higgsfield Soul/Nano/video would win. Check the router (WF-04).
4. **One-shot acceptance** — shipping the first render without the critique loop (WF-07).
5. **Generic-default aesthetic** — no named lineage, "modern/clean/professional." Anchor in WF-01; pass the Virgil Test.
6. **Under-used hands** — never reaching for `--mask`, `--refs`, `--rembg`, non-portrait sizes, or the video bridge when the job calls for them.
7. **Verbose ref prompts** — with `--template`/`--refs`, the shortest prompt naming only the change wins; verbose specs make the model drift. Source: SKILL.md "Trust the Reference" — "the shortest prompt that names ONLY what changes outperforms verbose specs."
8. **Auto-firing paid gen** — any generation without the cost gate + a human yes. Source: `generate.js` (2026) carries its own root-cause comment on this exact failure mode, quoted below.

> "Root cause of the 2026-05→07 fal-usage.json staleness: fal_budget_guard.py logging was AI-memory-dependent (a human/agent had to remember to run it after each call)." — `generate.js`, lines 40-41

Spend logging is now wired directly into the generator (lines 39-60) instead of relying on a human remembering the post-flight log — the same discipline this anti-pattern demands of the cost gate itself.

9. **Title > ~6 words** — GPT Image 2 garbles long lettering; shorten or render text as a masked pass. Source: `README.md`, "Settings" section.

> "GPT Image 2 is the strongest text-rendering model around — titles, billing blocks, masthead lockups all hold up. If a title runs more than ~6 words, expect typos; shorten and re-run."

10. **Skipping the satori handoff** — treating a `/satori-design-think` brief as optional. If it exists, ingest it; if not, run the concept + color inline.

---

## How Fantastic Studio Composes the Roster

- **Upstream (the brain)**: `/satori-design-think` (full production brief) · `/satori-concept` · `/satori-color` · `/satori-lift-audit` · `/satori-anti-ai-slop` · `/satori-feeling-calibrate`.
- **Peer (prompt/craft)**: `creative-direction` / creative-director agent (Virgil Test, platform prompt formulas) · `kittl-graphic-design` (type) · `jack-roberts` / `design-md` (token codification).
- **Instruments (execution)**: `generate.js` (Fal GPT Image 2) · Higgsfield MCP (Soul / Nano / Cinema / models_explore) · `fal_video_kling.py` / `fal_video_seedance.py` · `creative_router.py` (the dispatcher) · `cost_gate.py` / `fal_budget_guard.py` / `higgsfield_budget_guard.py` (the gates).

Studio is the **conductor** over that roster: it does not replace the instruments, it decides what plays, when, and judges the result.

---

**End of genius.md.** For the runnable stages, load `workflows/00-studio.md` (front door) and the eight `workflows/0N-*.md` files. For the model dispatcher, `execution/creative_router.py`. For cost, `directives/fal-usage-policy.md`.
