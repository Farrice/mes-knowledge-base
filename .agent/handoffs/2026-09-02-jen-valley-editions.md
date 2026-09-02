---
thread: jen-valley-editions
status: active
resume_hint: DIVISION OF LABOR CHANGED (Farrice, 2026-09-02): Claude Design does the visual from the kit in `valley-editions/claude-design-kit/`; this repo supplies the design system, copy, references, photos and prompts. Take 2 of the code render is on the canvas (https://claude.ai/code/artifact/b76c3b1c-c8ba-409f-a14f-8e9ab1680cf4). Next is his verdict, then plates A–E behind the cost gate, then Jen's Bothwell confirmation. Extend editions.py; never a second generator.
branch: worktree-jen-engine-v2-weeks
pin: true
---

## The one sentence
Build Jen (@_jiing) her own Coffee & Contracts: a place-magazine carousel system ("The Valley · <neighborhood> · Edition NN") in the six Canva template grammars Farrice picked, in her palette, filled with researched, sourced Tarzana content and her real photos, delivered as a Claude Design canvas he can drag, retype and export, and show her.

## What Farrice approved (his brief, 2026-09-02 evening; "what good looks like")
1. Every frame is one of the six template grammars, geometry exact (numbers in `06-system/valley-editions/CANVA-GRAMMAR.md`), palette hers: navy #1E3A5F, steel #4C7CA8, cream #F7F5F2, white; type-and-accent only, no yellow, no orange, no navy color blocks.
2. Every claim on a frame is in a facts ledger with a VERIFIED / LIKELY / UNCONFIRMED label. No invented lines ("the coffee line on ventura at 7am" was invented; that class of line is banned until sourced).
3. No stock photo. Her photos, her listing, or a labeled AI Valley plate (style vault, realism lint, cost gate first, ~$1–3).
4. Type never sits on a face. Subject small, negative space where the type goes. His verdict on the first canvas cover: pill on her hand and headline over her body = sloppy.
5. Every frame teaches one thing and asks one thing, in her words. Ethos: a DM from someone willing to be educated, qualified in the reply layer. "Buying or selling" in the ask; never "your first home".
6. Sequence that must hold: content pack → photo plan → layout → canvas. Designing before researching is how the last three attempts failed.
7. Deliverable shape: Edition 01 full (5 frames) on the Local Gem grammar (his pick, "take A"), plus one cover per other grammar as the system sheet. ~11 artboards, one canvas.

## What exists (extend, never rebuild)
- `_active/clients/jen-listings/06-system/valley-editions/`
  - `DESIGN.md` — the system spec (tokens, type, wash, seven archetypes, edition shape, photo rules).
  - `CANVA-GRAMMAR.md` — every element of the five Canva designs with exact px/%, fonts by fontRef, wash recipes. A sixth design ("Brown and Beige Local Cafe City Guide", zip in ~/Downloads, also in his Canva) is NOT yet extracted.
  - `editions.py` — HTML→PNG generator: cover_gem, cover_stack, statement, moment, spot, grid, close, plus `cover_exact()` = Local Gem cover with nothing moved; `fit()` stops line wraps. Renders with chrome-headless-shell. Outputs in `out/`.
  - `photos/jen/` — 12 photos + provenance.json: her studio headshot (2048), closing-day selfie (2048×1536), kitchen family with SOLD sign (2048×1536), four 414px client photos (inset use only), the four listing photos (exterior, living, pool, kitchen; VERIFIED 5421 Bothwell, $5,695,000, Active, matched against the listing gallery 9/2), plus one older listing gym/pool shot. Facebook album pull was abandoned (Comet browser, not Chrome; downloads never landed).
  - `canva/` — the Canva-native route: `README.md` recipe (copy-design → upload-asset-from-url → read-design open_transaction → edit-design per page → commit → export), `edition-01/` five exported PNGs of design `DAHUEKxS7Ig` (a copy of Local Gem `DAHUD1-FGgs`, filled, committed, editable at https://www.canva.com/d/iTM4E22rg0sc9gG). Farrice's verdict: composition not right, stock placeholders, not what he wants; keep as reference only.
  - `edition-01/RESEARCH-PACK.md` — DONE, 61 lines, six sections, every fact sourced and labeled (Tarzana places with sources, market this month, $869K comps refresh, recent sales, FAIR Plan Oct 15 confirmation, Bothwell status + whether the four photos are that house). If it is missing or thin, rerun the brief in this session's transcript.
- `_active/clients/jen-listings/04-deliverables/2026-09-06-engine-v2-weeks-1-2/` — FACTS.md (comps verified 9/2: 6324 Tampa $869K etc.), weeks 1–2 captions, saved replies, `build_weeks.py`. Copy engine + reply layer, reuse.
- `_active/clients/jen-listings/06-system/ENGINE-V2.md` — identity, the deal, realism gate, districts, what beats Coffee & Contracts (§11), research findings (§12).
- Voice: `skills/jen-santulan-listing-content/references/jen-real-voice-profile.md` + `jen-calibration-log.md` + `06-system/jen-voice-answers/transcripts.md` (her verbatim close and lines).
- Canvas mechanics: the `design` skill (Claude Design canvas in an Artifact; `.dc.html` artboards + `canvas.json`, seeded with its helper, images as bare base64 under ~70 KB each, publish with contract 0.1.31). Load it fresh; the September folder's `.dc.html` slides are the prior art for the format.

## Shipped 2026-09-02 (this thread, second session)
- `edition-01/CONTENT-PACK.md` (five frames + one post caption + the five other-grammar covers; every number labeled; fair-housing lint PASS; classifier CLEAN 1.5/10 on the copy).
- `edition-01/PHOTO-PLAN.md` (cover = headshot backdrop-extended, Jen small bottom-right; F3 = Bothwell exterior + living/pool panels; F5 = pool sky; F2 and F4 = labeled plate slots A–E).
- `editions.py` extended: `spot_exact`, `close_exact` (D1 pages 2–5, unmoved), `plate_bg/plate_inset`, `fact_panel`, `headline_size`, the five other covers (`cover_moment_exact`, `cover_stack_exact`, `cover_guide_exact`, `cover_urban_exact`, `cover_initial_exact`), `frames()` feeding both `edition01`/`sheet` renders and `canvas` (seeds + checks the Claude Design page).
- `CANVA-GRAMMAR.md` now has Design 6 (`DAHUEETAQQs`, the big-initial move). `DESIGN.md` §3/§6/§10/§11 updated.
- Renders: `out/edition-01/01..05.png` + `S2..S6`. Canvas: `out/edition-01/canvas/tarzana-edition-01.html` → artifact b76c3b1c (contract 0.1.31, save + export on).

## Take 2 (same day, after his verdict "pretty bad")
What was wrong with take 1, in his words and mine: didn't look like the templates he handed over. Diagnosis against the actual Canva exports (`~/Downloads/Yellow Vintage…/1.png`): the template's identity is ONE tall condensed serif in every role (masthead, headline, pill, body), a light wash that lets a warm photo carry the frame, thick hand-drawn doodles, and a photo in every slot. Take 1 had Playfair fitted small, a murky full-page wash, thin doodles, two dead dark "slot" panels, and Jen tiny in a corner.
Fixed: Instrument Serif everywhere on D1 pages (Playfair retired); headline gradient pale steel → white in the yellow's slot; accent #C9D4E2 on doodles/pill; wash lightened; pill = hand-drawn ellipse; arrow with the template's long tail; every slot photographed (her interiors as demo placeholders, CC0 pool where honest); cover = Jen large, lower right, on an extended flat wall (`placed()`), type never on her face. Canvas republished to the same artifact.
Still true: placeholders are named in PHOTO-PLAN and never ship to her grid; plates A–E wait on the cost gate.

## The Claude Design kit (Farrice's call, 2026-09-02 evening)
His read: "I should just be using you to get the design system, or just the actual prompts... go into Claude Design and give it the reference material, and then you give me all the content." So: `claude-design-kit/` = DESIGN.md (Google Labs spec, Instrument Serif + #C9D4E2 accent, D1 geometry in px), COPY-DECK.md (final copy, all five frames + caption + system sheet), GRAMMAR.md (= CANVA-GRAMMAR.md), HANDOFF.md, PROMPTS.md (0 ground → 1 five frames → 2 cover placements → 3 five grammars → 4 panels → 5 export), photos/ (her 12, 1600px), reference/ (template pages = TARGET; canva-native attempt; our take 2 = floor to beat). Zip: `jen-valley-editions-claude-design-kit.zip` (34 MB, gitignored; rebuild by re-running the assembly in this session's transcript or `zip -r` the folder).
When he brings PNGs back from Claude Design: encode what changed into `editions.py` so future editions inherit it; the generator stays the system of record for geometry and copy, Claude Design is the visual explorer.

## Next session, in order (updated)
1. His verdict on the canvas and the ten PNGs (Feedback Triad). Two rejected takes on one frame = back to the input, not a third take.
2. Plates A–E (Laidrey storefront, espresso bar, cup on table, Tarzana street, porch step): cost gate first (~$1–3), style vault key for Jen, realism lint, craft master loaded per `skills/generate/references/craft-map.md`. Drop into `photos/plates/`, point `frames()` at them, re-render, `python3 editions.py canvas`, republish to the same artifact. Her own photo of Laidrey beats a plate.
3. Jen confirms 5421 Bothwell price/status from her MLS before post day; re-check 6324 Tampa still active (FACTS.md re-check column).
4. Edition 02 = a new neighborhood: research pack → content pack → photo plan → render → canvas. Same files, same order.

## Prior plan (kept for the record)
1. Read RESEARCH-PACK.md; write `edition-01/CONTENT-PACK.md`: five frames (cover · place · her listing · what $869K buys · close), each with headline, subline/body, the fact it carries + label, the ask, and the caption; Jen-as-herself seat over every line; fair-housing lint + prose classifier on the file.
2. Write `edition-01/PHOTO-PLAN.md`: frame → photo (from photos/jen/ or a plate to generate), crop and subject placement per the template geometry, so type never lands on a face.
3. Render the five frames with `editions.py` on the exact Local Gem geometry, view every PNG, fix, then the five other-grammar covers.
4. Seed the Claude Design canvas from those artboards (design skill), publish, send him the link + PNGs.
5. Only then: the AI Valley plates for the place frames (cost gate), and the Bothwell confirmation from Jen.

## Do-NOT-Rebuild
Weeks 1–2 builder. Valley Editions generator + DESIGN.md. CANVA-GRAMMAR.md. The Canva-native edition (reference). Never a second generator, never a mission-card ceremony on this thread, never a photo-motion reel (he called them cheesy), never a talking reel, never a recurring ask on Jen.
