# HTML craft — Layer 3 (the HOW WELL of HTML)

> Pure knowledge, shared by scenarios A, B2, and solid. This is NOT about *when* to use HTML (that's
> identification + the isolability test) — it is about making HTML look **alive** when it IS used. Improving
> "dead" HTML touches ONLY this file.
>
> **The problem this solves:** HTML in the old builder came out "dead" — small, lifeless, dull — and text was
> positioned with absolute `%` coordinates estimated by eye from the ref, so it landed too high, too low, or
> left dead space. This file replaces guessed coordinates with **flow zones** and gives HTML real life.

---

## 0. Font-family consistency across the headline stack

**One display font family for the entire headline stack. Weight and style may vary, family never changes
mid-stack.** A headline mixes `<em>` / `<strong>` / a connector class for typographic variety (§3.6) — but
all of them resolve to the SAME display family; only weight and style differ. Switching family mid-headline
(a serif word beside a condensed-bold word in the same headline) breaks the stack's identity and reads as a
mistake. Pick one `--brand-display-*` family for the stack; vary `font-weight` / `font-style`, never
`font-family`.

---

## 1. Flow zones, not guessed absolute coordinates

The single biggest fix. Do NOT place each text line with its own `position:absolute; top:NN%`. Instead:

- Place ONE bounded **zone container** (the region text belongs in — the clean side of a Form A frame, the
  reserved band of a B2 image) and let the text **flow inside it** with flexbox + padding.
- The container is positioned to a region read from the ref (a side, a band) — a coarse, reliable placement —
  and the browser does the fine layout. No per-line coordinate guessing.

```html
<!-- Form A — text flows in the clean column beside the framed image -->
<div class="zone text-col" data-slot="HEADLINE"
     style="position:absolute; left:6%; top:8%; width:42%; height:84%;
            display:flex; flex-direction:column; justify-content:center; gap:2.5cqw;
            padding:5cqw;">
  <div class="kicker">{{KICKER}}</div>
  <div class="headline">{{{HEADLINE}}}</div>
  <div class="body">{{{BODY}}}</div>
</div>
```

`justify-content:center` (or `flex-end` / `space-between`) does what coordinate-guessing was failing at:
vertical balance. The zone owns a region; flow owns the rest.

**No absolute `top:%` per block — ONE flow column for the whole text stack (SPEC-B).** The "big-head /
starved-body / hollow-middle" failure (r04, r05, r06) is absolute `top:%` pinning + oversized `height:%`
reservations + an under-scaled body: a big headline pinned high, a small body pinned low, and a dead
~135–200px band between them. Fix: put the kicker + headline + body + CTA in a **single flow column**
spanning the content region (`display:flex; flex-direction:column`), and let `gap` + `justify-content`
distribute them — `space-between` to push chrome to the edges and fill the middle, or a tight `gap` for a
top-weighted stack. NO per-block `top:%`. The column removes the hollow middle structurally; you tune the
rhythm with `gap`, not by guessing two pinned coordinates.

> **Scope — this is about not GUESSING per-line coordinates by eye, NOT about ignoring measured bboxes.** The
> flow column applies to a text stack that belongs together in ONE content region (a cover's kicker + headline
> + body). It does NOT override `_measurements.yaml`: when the ref places blocks at *distinct measured
> positions spread across the canvas* (masthead 2%, line1 10%, line2 32%, body 60%, wordmark 97%), those are
> SEPARATE zones, each positioned `absolute` to its measured bbox (`shared/template-conventions.md` "When
> `_measurements.yaml` exists, it is the position contract"). Collapsing such spread-out measured blocks into
> one top-anchored `justify-content:flex-start` column is the kraft miss. Flow distributes content *within* a
> zone; the measured bbox fixes *where the zone is*.

**Give the flow-zone container an explicit `font-size`.** Children inherit it; OMIT it and the text falls
back to the UA default (~16px) and renders tiny on a 1080-wide canvas. Set it on the container (in `cqw`, so
it scales with the canvas) — its children then inherit a sane base and only the hero/kicker override up or
down. One line, but it cost two re-renders on ref-06 when it was missing:

```html
<div class="zone text-col" data-slot="HEADLINE"
     style="position:absolute; left:6%; top:8%; width:42%; height:84%;
            display:flex; flex-direction:column; justify-content:center; gap:2.5cqw;
            padding:5cqw; font-size:3.2cqw;">   <!-- explicit base; children inherit it -->
  ...
</div>
```

**The gap between headline and body is not a coordinate — it is the result of both blocks being at target
size.** If the gap looks too large, the type is too small. Do not author the gap to fill space; scale the
headline and body to their targets (§3) and the gap resolves itself.

---

## 2. Breathing room (the gate enforces this)

- **30–50px margin at the canvas edges by default.** Without it, text glues to the margin and reads cheap.
  On a 1080×1350 canvas that is roughly `padding: 3cqw 4cqw;` on the outer zone.
- **Proportion:** text must not sit crammed at the top leaving half the canvas empty below. The gate fails a
  layout where the text zone occupies **< 25% of canvas height AND the largest empty contiguous region
  > 55%** (see `shared/quality-gate.md`). Fix by growing the zone, centering the flow, or scaling type up.
- **Platform safe zones (RULE, not a gate — keep critical type clear of the dead bands):**
  - **Instagram:** the bottom **200px** is dead (caption / action bar) and the top **120px** is dead (handle / overflow) — keep headline + footer clear of both.
  - **LinkedIn:** the bottom **160px** is dead — keep the footer / CTA above it.

---

## 3. Live type hierarchy and scale

Dead HTML is usually under-scaled and flat. For a post (not a document):

- **Make the hero type big.** A headline carries the slide — display weight, generous `font-size` in `cqw`
  units (container-relative, so it scales with canvas). A timid 4cqw headline reads dead; 8–12cqw reads like
  a post.
- **Type-craft TARGETS and floors (SPEC-B — shared defaults live in `_shared/styles.css`; aim for the target, the floor is the hard minimum):**
  - **Display: target 11–16cqw** (a cover hero), **floor 9cqw.** Below ~8cqw a "display" headline reads as body. The floor is where it stops being display, not where you aim.
  - **Body: target 4–5cqw**, **floor 3.2cqw.** An under-scaled ~2.8cqw body under a big headline is the "starved body" half of
    the hollow-middle failure — bump it.
  - **Display:body ratio: target ~3:1, never exceed 4:1.** Past 4:1 the body strands as a footnote.
  - **Display line-height ~0.95, letter-spacing −0.02…−0.035em** (poster-tight). Body line-height ~1.35.
  - **NEVER bump display font-WEIGHT to "fix" limp type.** Limpness was the fallback-sans bug (fixed in
    SPEC-C); the brand display is already a black poster face. Tighten line-height/tracking and grow size —
    never reach for heavier weight.
- **Real hierarchy:** kicker (small, uppercase, tracked) → headline (display, heavy) → body (readable) →
  caption. Contrast the sizes; don't let everything sit at one weight.
- **Accent once, and let the SHARED `mark` rule drive its color.** Use the brand accent on at most one element
  per slide — typically an `<mark>` word on the meaning word (weight 700). **Do NOT locally override
  `mark { color }`** in a template (e.g. `.headline-display mark { color: var(--brand-primary) }`) — that
  discards the shared surface-aware coral and the deck ships with ZERO accent (the r06 miss). The shared rule
  already flips coral↔on-dark by `data-surface`; leave it alone.
- All sizes/colors/fonts via `var(--brand-*)` — never hardcode hex or font names.

---

## 3.5. Text fit — the box must hold the text (a hard contract)

§3 pushes type UP (big, alive). This is the guard that stops it from going wrong in the OTHER
direction: **a fixed font-size in a fixed-dimension box has no idea what text will land in it**, because the
text is a per-post slot the author can't see when writing the template. A short word fits; a long word, or two
words, **overflow the box** — the glyphs spill past the edges or clip the canvas. The fit is a property of the
*value*, not the template, so it cannot be hand-tuned per template.

> **The rule (per-BOX, template-agnostic):** every text box of **fixed dimension** declares HOW the text fits.
> Two legitimate forms — never neither:
>
> - **(a) auto-shrink** — the authored `font-size` is the **ceiling**, and a mechanism reduces it until the
>   text fits **both** width AND height, down to a declared legibility floor; `overflow:hidden` is the
>   backstop. The size you pick is the *maximum*, not a guess that happens to fit your example value.
> - **(b) box-grows** — the box has **no fixed height**; it grows with the content (`height:auto`,
>   flow + padding), so longer text makes a taller box instead of spilling.
>
> ❌ **Anti-pattern:** a fixed `font-size` in a box with fixed `height`/`width` and **no fit mechanism**, with
> `overflow` left default-visible. A per-post value that is one glyph too wide spills the frame. This is the
> `highlight-headline-render` miss — three highlight boxes with `font-size:NNcqw` in `height:13.5%` boxes; the
> short example word ("Workflow") fit by luck, a longer one ("Internationalization") burst the outlined box on
> every side. The box held the *example*, not the *slot*.

**This is a floor the bake also enforces.** `render_template.py` runs a deterministic autosize net on every
fixed-dimension text box right before the screenshot — it measures against the box and shrinks the font-size to
fit, so a template that forgets this contract still cannot ship overflow. But **do not lean on the net as the
plan**: author the contract here so the type is *designed* to fit (the net is the safety floor, not the layout
engine). When even the floor cannot hold a value, the net clamps + clips and flags it (the value is too long
for that slot — a content decision, not a render bug).

The choice is per-BOX, not per-template: a tight headline box wants (a) auto-shrink (keep the poster scale, let
long words step down); a body/quote block usually wants (b) box-grows (let length drive height). Pick per box;
the highlight box above is an EXAMPLE of where (a) applies, not the definition of the rule.

---

## 3.6. The headline COMPOSITION contract — declare its zone, anchor it, keep type variety

§3 sets the type *scale*; §3.5 makes a fixed box *hold* its text. This is the third leg: **where the headline
zone sits and how it is anchored**, so the headline reads centered-and-composed like the gabarito instead of
crammed at the top with half the canvas empty (the about-callout miss: the headline+pills were baked into the
AI and burst the frame; once in HTML, the zone needs a declared composition or it floats wrong).

**Declare the headline's target zone — do not let it float.** A display headline that carries the slide
occupies a real share of the canvas; an under-declared zone reads as a caption lost in white space.

- **bbox target ≈ 58–65% of canvas height** for a headline-led slide — the headline stack (kicker + headline +
  any connector) should fill roughly the central three-fifths, not a thin top strip. State it on the zone
  (`top` + `height` in %), measured, NOT "AI-integrated, not measured".
- **Side margins ≥ 8%** (`left:8%; width:84%` or tighter) — the headline never glues to the canvas edge.
- **Reserve the top for the kicker and the BOTTOM for the footer.** The zone's `top` leaves room for a kicker
  band; the zone's bottom stops ABOVE the footer (see next point). The headline is *framed* by chrome top and
  bottom — that framing is what compresses it to the center in the gabarito.

**Reinstate the footer pill as the bottom anchor — it is NOT a SKIP.** When the ref shows a footer pill / CTA
strip at the bottom edge, author it (a real bottom-anchored zone, e.g. `bottom:6%`), do not drop it. The footer
is the lower bookend that pushes the headline up off the bottom and centers the composition; skipping it lets
the headline sag and leaves the bottom dead. (Author it only when the ref shows one — same ref-read discipline
as every element; the point is *don't skip a footer the ref has*, not *invent one*.)

**Keep typographic VARIETY — do not collapse the headline to one heavy face.** The gabarito headline mixes
weights and styles: sentence-case base + italic / heavy **emphases** on the meaning words + a `medium`-weight
**connector** ("and", "to", "for") that steps down between the punches. Author that variety with `<em>` /
`<strong>` / a connector class — NOT every word in one flat "Anton heavy" slab. Flattening the headline to a
single weight kills the rhythm the ref has (and the `mark` accent still rides ONE word, per §3, on its own).

**The FIT mechanic is §3.5 — this section does not restate it.** Declaring the zone (above) does not by itself
stop a long per-post headline from overflowing; the box must still hold the text. A headline box with a fixed
height applies §3.5 **(a) auto-shrink** (the declared `font-size` is the ceiling; it steps down to a floor to
fit), and a box that should grow with length uses §3.5 **(b)**. The overflow *detection* is the gate's job
(r6g Check-B), not authored here. Net split: **this §3.6 declares the bbox / margins / footer / type variety;
§3.5 (r6h) owns the fit mechanic; the r6g gate owns overflow detection.**

---

## 3.7. Type-craft floors that "fit but look bad" — the craft-LINT rules (RC-B)

§3 pushes type up, §3.5 makes a box hold its text, §3.6 places the headline zone. This section
closes the gap none of them catch: HTML that **fits the canvas but still reads bad** — small body,
airy spacing, crammed condensed glyphs, a stack that runs into the image. The overflow gate only
sees text spilling the CANVAS; the autosize net only shrinks text that overflows its OWN box. Every
defect below is *ugly-but-fits* or *cross-zone collision* — neither is a pixel-overflow event, so a
deterministic **craft-LINT** (`00-social-content/scripts/gates/check_craft_lint.py`, advisory) measures
these from the authored CSS. Author to the rules; the lint is the floor that surfaces the miss.

1. **FLOW, don't PIN — keep blocks' relationship; whitespace scales with content.** This is §1
   restated as a craft *invariant*, because the regressions kept reappearing: stop authoring each
   block as an independent `position:absolute; top:NN%`. A hardcoded `top:11%` headline + a
   `top:52%` body leaves a dead 40%-of-canvas gap the moment the body is short — the whitespace is
   *frozen* instead of scaling. Group related type into ONE flow container (`display:flex;
   flex-direction:column`) with proportional `gap`/`margin`, so the blocks keep their relationship
   and the whitespace breathes with the content, not with a guessed coordinate.

2. **ONE coordinate system for text + image.** When the AI image reserves a zone, the HTML text
   zones are defined **against that same reservation** — never a parallel set of `top:%` guesses.
   Two un-reconciled coordinate systems (an HTML zone pinned at `top:72%` over AI-baked content that
   already fills that band) collide. The reserved zone is the single shared contract: text sits in
   the clean band the image left, never in the band the image fills.

3. **CAP the display-block height to the reserved clean zone.** A display stack with no
   `max-height` / line budget runs a tall headline down into the image subject below it (the
   cross-zone collision). Give the display zone a `max-height` (or `-webkit-line-clamp`) bounded by
   the clean zone, so a 4-line headline can't invade the image — it steps down to fit (§3.5 (a))
   instead of overflowing the *layout* (which the box-overflow gate never sees, because the glyphs
   never leave their own box — they leave the clean ZONE).

4. **NO negative tracking on multi-line condensed display; condensed line-height ≥ 1.0.** A
   condensed display face (Anton, Oswald, Bebas, …) with `letter-spacing` negative AND
   `line-height < 1.0` over **multiple lines** crams the glyphs until they touch. Single-line
   poster-tight tracking is fine (§3); the collision is a multi-line condensed property. Don't let
   the autosizer trade tracking for fit on a condensed face — keep `line-height ≥ 1.0` and drop the
   negative tracking the moment the headline wraps.

5. **SCALE discipline — body ≥ ~4–4.5cqw, display:body ratio ≤ ~4:1; tighten line-height.** A body
   at 3.2cqw under a 19cqw display is a 6:1 ratio — the body is stranded as a footnote even though
   it fits. Floor the body at **~4–4.5cqw** and keep the **display:body ratio ≤ ~4:1** so the
   hierarchy is strong AND the body stays legible. And apply Gustavo's rule — **"diminuir entrelinha,
   aumentar fonte"**: prefer a bigger font with a *tighter* line-height over small text with airy
   spacing. Concrete defaults: **display `line-height` ~0.95–1.05** (condensed ≥ 1.0), **body
   `line-height` ~1.25–1.4**. Above ~1.5 on body reads airy/dead; that's the "espaçamentos muito
   altos" miss. **If the layout looks empty, the type is too small — scale up, never adjust the gap.**

6. **The scale/rhythm relationship (agnostic, NOT a canvas-fill target).** State the hierarchy as
   relationships, never as "fill N% of the canvas": **display DOMINATES** (the unmistakable largest element);
   **body is CONFIDENT, not a footnote** (a moderate ratio below the display — a small multiple, never an order
   of magnitude); **tight leading INSIDE the cluster + breathing room OUTSIDE it** (§3.8); **annotations are
   ANCHORED** (a pill / label / caption touches the word, line, or object it refers to — distance kills it); and
   **ONE accent** (a single coral element — never spread across many). Liveness reads as: dominant display ·
   confident body · tight clusters with space outside · text anchored to an element · single accent.

> These are GENERAL craft, not a patch for any one template (rules 1–5 are lint-checkable; rule 6 is the
> relationship the others serve). The lint keys on the CSS values
> (cqw font-sizes, line-heights, letter-spacing, line count, height cap), never on a slug — so it
> catches the *class* (footnote body, glyph collision, cross-zone run-in, airy spacing) wherever it
> recurs. It is **advisory** (warns, surfaces for the human — the project's "gate WARNS on judgment"
> posture); `--enforce` makes it block and feed the 3-try ladder.

---

## 3.8. White space lives OUTSIDE the cluster, never inside it (anchor, don't float)

The "text floating in dead-center" failure: a block parked in the vertical middle with a large empty band
above AND below it, reporting to nothing. The rule, agnostic:

- **Every block anchors to a scene element OR to its sibling block** — a number badge, the subject, a surface
  edge, the frame edge, or the block directly above/below it in the same cluster. A block is never placed in
  free negative space on its own.
- **Group related blocks into ONE cluster** (kicker → headline → body → CTA) with **tight internal rhythm**
  (small `gap`, tight leading), then place the *cluster* against its anchor.
- **Distribute breathing room to the EDGES / OUTSIDE the cluster** — margins, the gap between the cluster and
  the footer — **never as a vertical gap INSIDE the cluster.** A block separated from its anchor or sibling by
  more than roughly its own height reads as "far" and must be pulled back. (This is §1's flow column stated as
  the spacing invariant: white space outside, never a hollow middle.)

## 3.9. Don't extract-flat + overlay when the appeal is text INTEGRATED into a textured/relief surface

When the reference's appeal comes from text being **printed / embossed / relief / integrated into a textured
surface** — ink debossed into paper grain, type carrying the surface's material — **bake it.** Stripping the
surface to a flat extracted texture and overlaying HTML type throws away the integration (the ink-on-paper, the
debossed feel, the grain interacting with the letters), and the words read pasted-on, flat, and lifeless.
HTML overlay is correct ONLY when the landing zone is genuinely flat/empty and the type owes nothing to the
surface's material. If you catch yourself extracting a surface only to re-paste type flat onto it — or stacking
HTML over a baked object with no depth/occlusion relationship, so the overlay collides with the object — the
integration that made the ref good is gone: route that text to AI-baked (or hybrid, where the baked surface
carries the integrated type) instead. This is the same routing question as §3.8's anchor rule and the
identification tree's decisive question — relief/integrated text is object-bound.

## 3.10. Woven elements — a pill rides BETWEEN lines, never on top of them

A pill / chip woven into a text stack belongs to the rhythm of the lines around it, not over them:

- **A pill must never overlap the text on its own line — only adjacent lines above or below.** A pill on a line covers the words it shares that line with; it must sit on its own baseline (its own flow row) or be anchored to the gap above/below an adjacent line. Overlap on the same line is the collision; adjacency is the woven look.

## 4. The html-overlay (pill) — a first-class pattern

A semi-opaque or solid container placed over an image with text inside it. It gives a **guaranteed breathing
zone independent of the photo behind it** — the text never fights the image's detail. This recurs across
real refs (Nomba notifications, the Hermes "← Swipe" pill, the Visual Brain body) — document and use it as
its own deliberate move, NOT an ad-hoc div.

```html
<div class="zone pill" data-slot="BODY"
     style="position:absolute; left:8%; bottom:8%; width:84%;
            background: var(--brand-surface); border-radius: 4cqw;
            padding: 4cqw 5cqw; display:flex; flex-direction:column; gap:1.5cqw;">
  <div class="body">{{{BODY}}}</div>
</div>
```

When to reach for it: an isolable text block (`isolable: true`) that must sit over a busy image. The pill is
the breathing zone the photo can't guarantee. (For a reserved *clean* band the AI deliberately generated,
text can sit directly on it without a pill — see reserved-zone prompting in `ai-prompt-craft.md`.)

**A full-width scrim / band is NOT a default — it copies the ref's legibility method.** A `.bottom-scrim` /
solid full-width strip is authored ONLY when the ref shows an intentional band (`legibility-method: ref-band` in
`rationale.md` §2). When the ref resolves legibility by **natural composition** (the scene is dark/calm where the
text sits, no band), `legibility-method: natural-composition` → the dark zone is GENERATED in the scene by the bg
`prompt_delta` (reserved-zone / composition prompting), and **no scrim div is authored**. Stamping a band the ref
lacks is the run-02 INVENTA miss — see the scrim anti-pattern in `agents/ssc-template-builder.md` and
"Legibility method copies the ref" in `ai-prompt-craft.md`. (A pill differs from a scrim: the pill is a small
breathing zone for ONE isolable block; the scrim is a full-width band — both are authored only when the ref's
treatment calls for them.) Check B's scrim-vs-ref assertion flags a full-width opaque band authored against a
`natural-composition` rationale.

**Full-bleed caption strip:** an HTML caption strip over a photographic lower edge reproduces the REF's strip
treatment — qa ref-01's bottom caption sits on a solid white bar, so the authored strip carries that bar — and
is authored ONLY when the ref shows the strip.

**Do NOT add a pill / card behind text that sits inside an in-scene surface (B1).** There the surface
(frame/screen/wall) ALREADY exists in the AI scene — an HTML card duplicates it and reads as "pasted on".
The B1 text element must be `background: transparent; box-shadow: none; border-radius: 0;`.

### Isolability vocabulary — `text-on-scene-no-box` vs `chip-with-fill` (default = NO box)

A text block over an image is one of two things — name which, because the wrong one invents a box the ref
never had:

- **`text-on-scene-no-box`** *(the DEFAULT)* — the text sits directly on the scene/surface; legibility comes
  from the zone behind it being calm, or from text weight/colour. **No background, no border, no chip.**
  `background: transparent; border:0; box-shadow:none;`.
- **`chip-with-fill`** — the text sits in a real filled container (a pill / card) **that the ref shows as a
  material object**. Authored ONLY on a **material-edge proof**: would the container's edge survive if you
  *erased the text*? A real chip has its own border / fill / shadow independent of the words. If erasing the
  text would erase the "box", there is no box — it is `text-on-scene-no-box`.

**"Callout" / "highlight" / "emphasis" is a property of the TEXT, not a new object.** Making a line a callout
means heavier weight or the accent colour on it — NOT wrapping it in a coral rectangle the ref doesn't show.
A conceptual role ("this is the callout line") reified into a white/coral box is the numbered-photo "phantom
white rectangle" miss (a `fill:white` read off the *water behind the text*, not off a real border).

**Do NOT fuse a paragraph STACK into one block and then "compensate" by promoting the last line to a pill.**
When the ref shows N left-aligned paragraphs, author N stacked text zones — preserve the pile. Collapsing them
into one merged block and dressing the final line as a chip to "balance" it destroys the ref's stacked rhythm
(the about-callout class of reification). The pile is the composition; keep each paragraph its own zone.

---

## 5. Font fidelity — get the path EXACTLY right

`_shared/styles.css` lives at `brand_context/templates/<pool>/_shared/`; the fonts live at
`brand_context/visual-identity/fonts/`. From `_shared/` that is **three** levels up:

```css
@font-face {
  font-family: 'BrandDisplay';
  src: url('../../../visual-identity/fonts/<file>.woff2') format('woff2');
}
```

A 2-level `../../` path lands in `templates/` and the fonts **silently** fall back to a system font — killing
brand-font fidelity in both the bake and the editor. Create `_shared/styles.css` from
`shared/shared-styles-template.css` on the first template in the pool, then prepend the brand `@font-face`
blocks.

The shared stylesheet carries a **surface-aware** `mark` rule so an accent `<mark>` word inside a triple-brace
slot stays legible on every surface: brand accent on a light/paper slide, inverting to the on-dark/paper color
on an accent or dark slide (accent-on-accent would be invisible — e.g. a `<mark>` verb on a solid-terracotta
CTA). It is pool-shared — every template inherits it once `_shared/styles.css` exists. The flip is driven by
`data-surface` on the slide root (`light`|`dark`|`accent`) — see section 6 and `shared/template-conventions.md`.

---

## 6. Renderer contracts — `data-slot` + triple-brace (never break these)

- **`data-slot`** on every editable zone, set to the exact Mustache key with trailing `_PATH`/`_HTML`/`_SRC`
  stripped (`{{{HERO}}}` → `data-slot="HERO"`; `<img src="{{PHOTO_MAIN_PATH}}">` → `data-slot="PHOTO_MAIN"`).
  This is the handle `render_template.py --tweaks` and the Content Studio editor key overrides by. Chrome
  zones get one too, so global toggles can target them.
- **Triple-brace `{{{SLOT}}}` for HTML-bearing slots** (headline / title / subhead / body / CTA — anything
  that can carry `<mark>`, `<br>`, `<em>`, `<strong>`). Double-brace `{{SLOT}}` HTML-escapes the value, so
  `<mark>word</mark>` renders as literal characters. Plain-text-only slots (numerals, dates, handles, page
  indicators) stay double-brace. (`render_template.py` resolves triple-brace first, then double.)
- **Image slots MUST end in `_PATH`** — that suffix is what makes the renderer inline the image as a
  data-URI. A slot like `BRAND_LOGO` (no `_PATH`) renders broken.
- **`data-surface` on the slide root** (`light` | `dark` | `accent`) declares the bg family so the shared
  surface-aware `mark` rule can stay legible (accent on light; on-dark/paper on accent+dark). CSS can't read
  an inline `background:` — this attribute is the only hook. Match it to whatever `background` resolves to.

See `shared/template-conventions.md` for the full slot schema, the `[ai-image-zone]` block, and the
`brand-badge` per-post logo slot.

---

## 7. A hero FACE carries the brand identity — never a baked AI stranger (SPEC-B, generalized r07)

**Trigger: a human face / head is a HERO element of the composition** — in ANY medium or style (editorial
photo, 3D render, illustration, line-art, even surreal: a giant head sculpted in stone). The trigger is **the
face being hero**, NOT the template being labelled a "creator / portrait cover". When the brand has a
**headshot**, the hero face carries the **brand person** (e.g. Simon), restyled for the ref's medium — never a
stranger the AI invented. (The full generation mechanic is the `scene-restyle-with-real-face` ROTA in
`craft/ai-prompt-craft.md`; this section is the HTML/slot side.)

- Author a `PHOTO_*_PATH` image slot for the person, **`user_editable: true`**, and declare
  **`brand-headshot`** in the template's `bg_substitution_methods` (manifest entry). That is the hook the
  `ssc-designer` **tier-1-headshot** rule looks for — it then fills the slot from the brand headshot
  (`brand_context/visual-identity/headshots/*.jpg`), as-is (`HYBRID_REAL`) or fed to AI as `--input-image`
  for a stylized-but-same-person treatment (`HYBRID_FROM_REAL`).
- **The headshot RESOLVES IN THE BUILD when it exists** — the build passes the real `headshots/*.jpg` path as
  the identity `--input-image` and generates with the brand person. It does **NOT** leave the identity slot as
  a literal string like `"(filled from brand-headshot: …simon-pic.jpg)"` (the `creator-cover-cta` defect — the
  slot never resolved). The *text marker* (`[fill with the brand headshot when one exists]`) is for the case
  where **no headshot exists yet** — a text placeholder documenting intent, not a deferral when one is present.
- Do NOT bake the person via a generic `PHOTO_SUBJECT` text prompt (e.g. *"a male creator, dark hair, arms
  crossed"*) — that invents a random face and ignores the real headshot (the r07 miss: the generator consumed
  the generic description, not the headshot). **A generic `PHOTO_SUBJECT` is forbidden when a headshot exists.**
  An AI-invented person is the fallback ONLY when no headshot exists (the soft default — it does not block).
- **A real-photo slot gives the template NO control over the fill's luminance** — `legibility-method:
  natural-composition` is invalid over it. The ref's legibility scene becomes a contract: hybrid regeneration
  around the real face, or a fixed gradient + declared slot framing/palette requirements, with reserved-zone
  contrast measured against the ACTUAL preview fill (see `scenarios/b2-filled-bg.md` "Real-photo slot
  legibility contract" — the run-06 coral-on-coral miss).

---

## Anti-patterns (HTML)

- ❌ Per-line `position:absolute; top:NN%` guessed from the ref → ONE flow column for the text stack (kills
  the big-head/starved-body/hollow-middle bands).
- ❌ Timid under-scaled type → display ≥ 9cqw, body ≥ 3.2cqw; tighten line-height/tracking, never bump weight.
- ❌ A body stranded as a FOOTNOTE under a giant display (display:body ratio > ~4:1, body < ~4cqw) → floor
  the body at ~4–4.5cqw and keep the ratio ≤ ~4:1 (§3.7 rule 5; craft-LINT). It FITS, so the overflow gate
  never sees it — the lint does.
- ❌ Airy spacing — body `line-height` > ~1.5 or display > ~1.1 ("espaçamentos muito altos") → "diminuir
  entrelinha, aumentar fonte": display ~0.95–1.05, body ~1.25–1.4 (§3.7 rule 5).
- ❌ Negative `letter-spacing` + `line-height < 1.0` on a MULTI-LINE condensed display (Anton/Oswald/…) → the
  glyphs collide; drop the negative tracking and keep `line-height ≥ 1.0` once it wraps (§3.7 rule 4).
- ❌ A display stack with no `max-height` / line budget → a tall headline runs into the reserved image zone
  below it (a cross-ZONE collision the box-overflow gate can't see). Cap the display block to its clean zone
  (§3.7 rule 3).
- ❌ Pinning an HTML text block with `top:NN%` over a band the AI image already fills (two un-reconciled
  coordinate systems) → define text zones against the SAME reservation the image left; text sits in the clean
  band, never the filled one (§3.7 rule 2).
- ❌ Fixed `font-size` in a fixed-dimension box with no fit mechanism (`overflow` default-visible) → a per-post
  value spills/clips the frame. Declare the per-box fit contract (§3.5): auto-shrink with a floor (the authored
  size is the ceiling) OR a box that grows with content. The size you author is the MAXIMUM, not a lucky guess.
- ❌ Locally overriding `mark { color }` → let the shared surface-aware rule drive the coral accent.
- ❌ A baked AI **stranger** where a hero face carries the brand → a real-photo `PHOTO_*_PATH` slot
  (`brand-headshot`) that **resolves to the real headshot in the build** when one exists; a generic
  `PHOTO_SUBJECT` person description is forbidden when a headshot exists (§7 + the `scene-restyle-with-real-face`
  ROTA). Applies to ANY hero face/head, any medium — not only "creator covers".
- ❌ `filter: invert(...)` / `brightness(0)` / `grayscale(...)` on a COLOURED brand logo → it destroys the
  brand colour (the one-page `filter: brightness(0) invert(1)` turned the coral Claude glyph white). Render a
  provided logo **as-is**; if it must read on a dark surface, put it on its own light card — never filter it
  (`shared/icons.md` "Brand seal composition").
- ❌ Reifying a conceptual "callout / highlight" role into a coral/white **box** the ref doesn't show, or
  wrapping `text-on-scene-no-box` text in a chip with no material edge → a callout is text WEIGHT/COLOUR, not a
  new object; a chip needs a real edge that survives erasing the text (§4 "Isolability vocabulary"). Merging a
  paragraph STACK into one block + promoting the last line to a pill to "balance" it is the same miss — keep
  each paragraph its own stacked zone.
- ❌ Text glued to the canvas edge → 30–50px breathing margin.
- ❌ Rebuilding an AI scene (subject + cards + arrows) as HTML/SVG/CSS → one scene is ONE image zone.
- ❌ A pill/card behind text that sits inside an in-scene surface (B1) → the scene surface IS the container.
- ❌ Double-brace on an HTML-bearing slot; a 2-level font path; an image slot without `_PATH`.
- ❌ Adding a callout-pill when the canonical ref does not show one — the pill is a deliberate brand move
  (coral rounded rectangle) that must come from the ref, not be added by default. If the ref shows no pill,
  no pill goes in the template. Adding one pollutes the layout with an element the designer never chose.
- ❌ Using `%` units for badge circle dimensions — `%` is relative to the containing block and resolves
  differently in width vs height when the block is not square, producing an ellipse. Use equal `cqw` units for
  both width and height of a circle badge (e.g. `width:9cqw; height:9cqw;`) — `cqw` is always relative to
  canvas width on both axes, guaranteeing a true circle.
- ❌ Badge circle on a dark surface with `background: var(--brand-primary)` — brand-primary is near-black
  (#1f1816) and is invisible on a dark bg. Use a surface-adaptive rule:
  `[data-surface="dark"] .badge-circle { background: var(--brand-text-on-dark); color: var(--brand-primary); }`
  in the template's `<style>` block so the badge stays legible on any surface.
