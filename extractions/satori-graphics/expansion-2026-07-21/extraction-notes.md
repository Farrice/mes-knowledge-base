# Satori Graphics v3 Expansion — Layout & Contrast Layer (2026-07-21)

**Source**: "3 Design Principles That Form High Level Layouts (Layout Course)" — youtube.com/watch?v=GT-K0CrrgfU, 27:46, Satori Graphics. Watched (not just transcribed): 100 scene frames + 27 transcript-cue frames read; transcript ~4,900 words (sponsor segment 9:03–11:10 excluded).
**Type**: EXPANSION of existing `skills/satori-graphics/` (v2, 20 workflows, 17 genius patterns) — never a rebuild.
**Farrice's direction** (from the forge request): integrate into Satori's workflows AND make the layer standalone-usable; target the known weak spot — *layout and composition in AI-generated design and front-end work*; output must enable "remarkable, awe-inspiring, non-generic" design.

## Vision (Phase 2 — latitude 3, autonomous per forge spec; direction honored)

**Uniqueness audit.** The roster has composition *auditing* (LIFT, flip test), grid selection, movement levels, color strategy, concept origination. What no expert in the roster had before this video:
1. A **layout spine generator** — the Three-Flow Rule gives every layout exactly three committed anchors (Hook → Secondary Detail → Finisher) *before* grid or style exist. LIFT audits hierarchy after the fact; three-flow *originates* it.
2. A **contrast system** — 9 named forms in 3 tiers. The roster used "contrast" as a one-word lever inside other frameworks; nobody could enumerate, stack, or audit it. Contrast is the single highest-leverage anti-generic mechanism for AI-produced design: AI defaults distribute emphasis evenly; deliberate contrast stacking is precisely what it fails to do.
3. **Directional hierarchy** — the gaze/light/angle toolkit that turns hierarchy into a *path of importance* (Dazed cover: hierarchy decides first fixation, direction decides the second).

**Business leverage.** Deployability × differentiation both high: every client surface Farrice ships (Jen listing frames, MyBPM posters, Parallax visuals, client landing pages, front-end builds via frontend-design/product-build) is a layout. The front-end bridge workflow is the direct answer to "AI front-end looks generic": section rhythm (temporal beats) + contrast stack + three-flow, compiled into DESIGN.md-compatible directives.

**Gap fill.** Closes the v1 caveat "visual context not captured" — this expansion is the first Satori source actually *watched*; 17 exemplar frames archived in `frames/`.

**Standalone decision.** No separate skill is created (extend-never-rebuild). Standalone use = the new slash commands work without loading the rest of the pipeline, and `/satori-frontend-flow` is the self-contained front door for UI/front-end work.

## Deep extraction (Phase 3 — MES 3.0, Deep tier)

### New genius patterns (GP-18 … GP-20; full operative text in `skills/satori-graphics/genius.md`)

- **GP-18 — Three-Flow Rule + Thumbnail Test.** One primary journey, three committed anchors: Hook (entry), Secondary Detail (middle stop), Finisher (rest — usually the essential info/CTA). Verified by literally stepping back / shrinking to thumbnail: if the path still reads calm, flow works; if the eye bounces, adjust contrast/spacing/alignment. Habit, not one-off: "this small habit will train you to see flow on every single project and not just relying on gut instinct."
- **GP-19 — Directional Hierarchy (Path of Importance).** "The goal isn't to create movement. It's actually to create a path of importance." Hierarchy decides what's seen first; direction decides where the eye goes next. Toolkit: subject gaze lines (frame text near where the face points), angled shapes funneling inward, curves/diagonals for momentum, light/shadow nudges. Dazed proof: the masthead is black-on-dark, not white — hierarchy engineering beats salience defaults.
- **GP-20 — The Contrast Stack (9 forms, 3 tiers).** Basic: color, size, typography. Intermediate: shape, style, texture. Advanced: psychology, emotion, concept. Operating rules extracted:
  1. Ship-grade designs run **3+ deliberate forms** (Nike poster: color + shape + texture).
  2. **Double-whammy**: an element contrasts its container AND its own internal content contrasts (fashion-app photo cards).
  3. Advanced tier = **subverting learned associations** — serif in an urban hip-hop narrative, a skull in uplifting playful color, humor on a deadly-serious NHS message, a lackluster 2D concept flipped to 3D-modern.
  4. **Restraint rule**: contrast of style is NOT for every design — "advanced designers know when or where not to use it."
  5. **Audience gate**: "cheap hectic slap-dash" and "minimal premium" are both valid — the brief and target audience decide, never taste alone.

### Hidden knowledge (new)

- **HK-13 — Contrast is choice architecture.** CTA color contrast is "how social media UI creates an addictive response"; between two options "the larger option will most likely be clicked simply because of contrast"; premium-vs-basic price perception (dog food) is a contrast effect. Contrast isn't decoration — it's behavioral steering.
- **HK-14 — Temporal flow is the 99% edge.** "Something like 99% of designers don't consider this temporal flow" — punch/linger/release beats (A$AP Rocky spread, Apple product page) are the cheapest differentiation available because almost nobody engineers them.
- Grayscale + one color = engineered sadness/atmosphere lever (mood via desaturation contrast).
- Contrast of size deliberately pushed to surreal scale = intrigue/captivation play.

### Hall of Fame exemplars (new; frames archived)

| Exemplar | Teaches | Frame |
|---|---|---|
| Buck Design "Universe '24" | Three-flow journey: 3D graphics (hook) → white heading (secondary) → logo bottom-left (finisher) | buck-universe24-flow.jpg |
| Dazed cover | Directional hierarchy: amber-lit face wins first fixation, gaze delivers the eye to a deliberately BLACK masthead | dazed-directional-hierarchy.jpg |
| Yakult / ATTISM pair | 3-Key Levels incl. the exception: product-hero vs. typography-hook with date/location as finisher | yakult-attism-hook-finisher.jpg |
| Art-SYNc 2025 build | The movement ladder built live on one poster (L2→L5) — canonical visual for GP-04 | artsync-*.jpg |
| Nike "MOVE DIFFERENT" | The count-the-contrasts audit: color + shape + texture on one simple poster | nike-triple-contrast.jpg |
| Teal skull "Yes" | Contrast of psychology: death symbol × playful uplifting palette | skull-psychology-contrast.jpg |
| Apple iMac page | Temporal beats in *front-end*: hero punch → detail-block linger → white-space release | apple-imac-temporal-beats.jpg |
| Fashion-app UI | Double-whammy contrast + UI contrasting the phone chrome itself | (transcript + blurred frames) |

### Signature moves (new)

16. **Count-the-Contrasts** — read any design and name every form present; <3 nameable = flat, generic-risk.
17. **Draw-the-Flow-Line** — physically trace the eye path over a comp; three anchors or it's chaos.
18. **The Expectation Flip** — pick one learned association the audience holds and deliberately invert it (type-psychology, symbol-emotion, or genre-concept).

### Quality rubric additions (layout work)

13. **Three-anchor flow**: Hook/Secondary/Finisher each nameable, and the path reads at thumbnail size.
14. **Contrast stack depth**: ≥3 deliberate contrast forms nameable; any advanced-tier form is intentional (or its absence is a stated audience-gate decision).

### Overlap honestly logged (no double-extraction)

4:48–15:24 re-teaches the 6-level movement ladder already extracted as GP-04 / `references/movement-flow-ladder.md`. Treatment: no new pattern; the reference gains the Art-SYNc visual exemplar walk and the A$AP/Apple temporal-beat examples. The three-flow segment's "hook/secondary/finisher" is adjacent to but distinct from movement L2 (visual weight): L2 explains *why* the eye moves; GP-18 commits *which three anchors* carry the journey.

## Architecture (Phase 4)

Six new workflows (21–26), one new reference pair, five born-v2 prompts. Numbering and register continue the house pattern. See `skills/satori-graphics/SKILL.md` v3 table. Stacking: 21+22 are the new Tier-1 layout front line; 26 is the front-end bridge (frontend-design / DESIGN.md / product-build); 25 stacks with memory-encoding and novelty workflows.

**Attribution caveat** (rubric honesty, mirrors the LIFT caveat): contrast-of-color/size/typography are canonical design-school material; Satori's contribution is the 9-form enumeration, the 3-tier escalation, the count-the-contrasts audit, the double-whammy observation, and the psychology/emotion/concept advanced tier. The Three-Flow Rule and 3-Key Levels are Satori's names for focal-hierarchy sequencing (Hook/Secondary/Finisher). Workflows attribute accordingly.
