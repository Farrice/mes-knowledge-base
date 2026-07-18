# Kittl Graphic Design — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## How to Use This Skill (Model Calibration)

These are intuition primitives, not a checklist. Absorb the mood-first logic, the contrast pairing, the optical-over-mathematical instinct — then execute; don't narrate. If a deliverable stamps "Pattern 1, Pattern 3, Pattern 8 applied" onto the page, it has failed the test. The real question: would a working Kittl designer recognize this as theirs — someone who felt the mood before touching the font panel — or as someone reciting typography vocabulary? If it reads as the second, rebuild it.

Specifically:
- Do NOT label sections "here's the mood-first selection" or "here's the optical centering pass." Execute the move; never announce it.
- The craft is invisible machinery — a good pairing just *looks* inevitable. Naming "Pattern 4: Letter Spacing as Mood Amplifier" inside a client-facing deliverable breaks the spell the same way a magician narrating the trick does.
- The texture is a working designer's shorthand ("this needs more '90s serif energy," "pull the tracking," "does this LOOK centered") — not academic type theory. Numbers are real settings someone would actually type in (tracking -20 to -60, leading -20 or tighter), not decoration.
- Polish-is-the-tell: an AI prompt with every technical term stacked ("35mm lens, Rembrandt lighting, shallow DOF, hyper-detailed, 8K, trending on artstation") reads as trying too hard. The Big Six answered plainly, in the order asked, beats a keyword salad — match "Technical-First Prompt Structure" (Pattern 15), not a thesaurus pass over it.

## Recognition Test

A Kittl power-user opening this skill's output would recognize this as theirs on the first pass: mood words typed straight into the font-search panel before any manual browsing (Pattern 6), height-width contrast named as the actual pairing logic instead of "these look nice together" (Pattern 3), tracking pushed to specific values instead of left at zero (Pattern 4), and AI prompts structured Big-Six-first with camera language for photorealism (Pattern 14, Tacit 7). It would NOT recognize generic "clean, modern, professional" font language, default letter spacing, or bare negative-only prompts ("no clutter," full stop) as belonging to this method — those are the tells of someone who never internalized the platform's own reframe of moodboard-to-typography as a repeatable pattern, and it would distinguish this output from that generic default immediately.

## Anti-Patterns

Failure modes documented directly in the source material — not generic mistakes, but the specific ways this platform's own guidance says not to work it.

- **Skipping the negatives building block.** Kittl's official prompt guide treats "Don't" instructions as one of its 4 core building blocks, not an optional extra — exclusions are "Powerful for complex scenes" and "Saves time on re-prompts" (extractions/creative-direction/kittl_notes.md, added 2026-04-14). Writing only positive description and hoping the model infers what to leave out wastes generations.
- **Letting the written prompt fight the style preset.** The same guide warns to "Match preset style with written prompt (don't conflict)" (extractions/creative-direction/kittl_notes.md, 2026-04-14) — picking the "Anime" preset and then prompting "photorealistic" produces muddy, unusable output.
- **Over-prompting an image edit.** "Image editing AI needs minimal, surgical prompts. Over-prompting causes unwanted changes" (Tacit 8, above) — stacking five instructions onto a single edit call regenerates the whole image instead of touching one element.
- **Stacking multiple actions into one video prompt.** Kittl's video-prompting guide states to "Focus on one main action (multiple actions break consistency)" (extractions/creative-direction/kittl_video_nodes.md, documenting the Feb 3, 2026 Kittl Video launch) — asking for a product to spin AND the background to shift AND text to fade in produces incoherent motion.
- **Over-directing motion instead of trusting the model.** The same guide's fifth best practice is to "Avoid over-directing (fewer, clearer instructions = smoother motion)" (extractions/creative-direction/kittl_video_nodes.md, 2026-04-14) — over-specifying every camera micro-movement fights the model's own interpolation.
- **Negative-only instruction framing.** Pattern 17's anti-exemplar below shows the failure mode directly: a prompt built from "no people looking bored" produced a "bland, uninspired stock photo" rather than a directed one — negatives need reframing positive ("minimal, clean composition"), never shipped as bare exclusions.
- **Mathematical centering treated as finished.** The same anti-exemplar's banner is described as having "No intentional adjustments to tracking or leading" and, on alignment, "Relies on numerical centering" — shipping the moment the tool reports 0,0 instead of running the optical check in Pattern 8.

## Genius Patterns

## Pattern 1: Mood-First Font Selection
**Execute**: Look at any image for 5 seconds. Write 3 mood words. Type those exact words into font search. Select from results.

**Success Metric**: Font selection time drops from 15+ minutes to under 90 seconds.

---

## Pattern 2: Serif/Sans-Serif Mood Mapping
**Execute**: 
- Ethereal/Elegant/Nostalgic/Romantic/Gothic = SERIF first
- Techy/Futuristic/Sporty/Brutalist/Modern = SANS-SERIF first
- Western/Vintage = DISPLAY/DECORATIVE first

**Success Metric**: Correct font category on first attempt 90%+ of time.

---

## Pattern 3: Height-Width Contrast Pairing
**Execute**: Identify headline font's dominant characteristic (tall/condensed OR wide/extended). Select subtitle font with opposite characteristic.

**Success Metric**: Visual tension and hierarchy immediately apparent. The Everbloom Botanicals exemplar below runs this exact move — condensed serif headline against a wider sans-serif tagline, tracking loosened +40 so the contrast registers instantly.

---

## Pattern 4: Letter Spacing as Mood Amplifier
**Execute**:
- Modern/Tech/Editorial = Tighten tracking (-20 to -60)
- Luxurious/Airy/Minimal = Loosen tracking (+100 to +600)

**Success Metric**: Single tracking adjustment transforms "close" into "perfect."

---

## Pattern 5: Line Spacing Compression
**Execute**: For headline/display typography, reduce line spacing to -20 or tighter until lines nearly touch but remain legible.

**Success Metric**: Text block feels intentional and designed.

---

## Pattern 6: The Keyword Font Search
**Execute**: Type mood/style keywords directly into font panel → Browse filtered results only.

**Success Metric**: Relevant fonts appear without endless scrolling — this is the mechanism that gets Pattern 1's font-selection window under 90 seconds.

---

## Pattern 7: Pinterest-to-Execution Training Loop
**Execute**: Daily practice—select 1 reference design, recreate it completely, note what made it work.

**Success Metric**: After 30 days, can execute any typography style within 10 minutes.

---

## Pattern 8: Optical vs. Mathematical Centering
**Execute**: After mathematical centering, ask "Does this LOOK centered?" Adjust by 5-10% if script tails or visual weight create imbalance.

**Success Metric**: Compositions feel balanced without measuring.

---

## Pattern 9: Same-Font-Family Pairing Shortcut
**Execute**: When pairing is difficult, check if headline font has alternate weights, widths, or companion fonts. Pair within family first.

**Success Metric**: Guaranteed visual harmony with minimal risk. This is Tacit 2 in practice — "always check the family pack before looking elsewhere for pairs."

---

## Pattern 10: The Text Shading Technique
**Execute**: For thin fonts: add same-color stroke (offset 0, width 1-2). For dimension: add contrasting shadow (offset 3-5).

**Success Metric**: Fonts gain presence and dimension. This is the same tool Kittl's own hack list names "Knock-out text effects (Text Shading → Block Shadow)" (Design Hack #7, extractions/creative-direction/kittl_flows_advanced.md).

---

## Pattern 11: Gray Text for Visual Hierarchy
**Execute**: Primary text = full color. Secondary text = 40-60% opacity or gray value.

**Success Metric**: Eye naturally flows to important information first.

---

## Pattern 12: Border-as-Cutout Technique
**Execute**: Shape needs to "cut" into another? Add thick border matching background color instead of complex masking.

**Success Metric**: Complex visual effects in seconds — this is Kittl's own "Punch Through / Subtract" shape-builder cutout tool (Design Hack #10, extractions/creative-direction/kittl_flows_advanced.md) applied to typography.

---

## Pattern 13: AI Model-to-Task Matching
**Execute**:
- Graphic design with text = Ideogram 2/3
- Photorealistic images = Google Image Gen 4
- Artistic/stylized = Seedream 3/4
- Fast concepting = Flux/Flash
- Image editing = Nana Banana

**Success Metric**: First-generation accuracy increases 60%+.

---

## Pattern 14: The "Big Six" Prompt Architecture
**Execute**: Before prompting, answer: What is it? Where is it? How does it feel? How is it lit? What style? What angle?

**Success Metric**: Prompts produce intended results on first/second generation. Kittl's own guide runs the same completeness check under the "4 Building Blocks of a Good Prompt" heading, opening with the "5 Ws" — WHO, WHAT, WHERE, WHEN, WHY (extractions/creative-direction/kittl_notes.md).

---

## Pattern 15: Technical-First Prompt Structure
**Execute**: Structure as: [Shot type] + [Lighting] + [Subject] + [Setting] + [Style] + [Mood]

**Success Metric**: Consistent visual style across generations. Kittl's video-prompting guide mirrors this with its own modular "CAMERA, ACTION, AUDIO, TEXT blocks" structure (extractions/creative-direction/kittl_video_nodes.md).

---

## Pattern 16: Line Break Prompt Separation
**Execute**: After each major element, hit Shift+Enter to create logical separation.

**Success Metric**: AI respects distinct elements rather than blending them — the same claim Tacit 4 makes directly: "AI models parse line breaks as semantic separators."

---

## Pattern 17: Positive Instruction Framing
**Execute**: Reframe every negative as positive. "No clutter" becomes "minimal, clean composition."

**Success Metric**: Fewer unwanted elements; clearer AI interpretation.

---

## Pattern 18: The Emotional Design Vocabulary
**Execute**: Build personal mood vocabulary. When a design "feels right," name that feeling.

**Success Metric**: Can articulate "why" a design works in reproducible terms.

## Hidden Knowledge

## Tacit 1: The 90s Serif Secret
Fonts like Instrument Serif and Shaharazad carry inherent "90s elegance" that triggers nostalgia without appearing dated. This era maps to sophisticated but approachable emotional territory.

**Deploy**: When brief calls for "timeless but not stuffy," reach for 90s-era serif revivals.

---

## Tacit 2: Western Fonts Self-Pair
Western/adventure font families are designed to work together. The designers already solved the harmony problem.

**Deploy**: When using western fonts, always check the family pack before looking elsewhere for pairs — this is why the Apex Ascent exemplar below pulls its companion font from the same Western pack rather than hunting for a match, paired against the -30 line-spacing compression from Pattern 5.

---

## Tacit 3: Condensed = Sporty/Urgent
Any time a design needs energy, athleticism, or urgency, condensed fonts create inherent tension and movement.

**Deploy**: For sports, fitness, news, or action contexts, condensed is your first reach. The Apex Ascent exemplar below is the demonstration: condensed sans-serif headline, line spacing compressed to -30, built for exactly this athletic urgency.

---

## Tacit 4: Line Breaks Are Prompting Syntax
AI models parse line breaks as semantic separators. Using them strategically is as important as the words.

**Deploy**: Structure complex prompts with line breaks between major elements — Kittl's video-prompt guide operationalizes exactly this as "CAMERA, ACTION, AUDIO, TEXT blocks" (extractions/creative-direction/kittl_video_nodes.md), each break a semantic separator.

---

## Tacit 5: Texture Blending Modes Transform Mood
The "exclusion" blending mode on textures creates color combinations you'd never manually choose—often better than planned palettes.

**Deploy**: When stuck on colors, add texture layer in exclusion mode and sample results.

---

## Tacit 6: The Pinterest Training Ground
Every professional typographer maintains active, daily Pinterest practice—not for inspiration but for skill acquisition through recreation.

**Deploy**: Daily recreate 1 reference design. This is practice, not production — the daily engine behind Pattern 7's 30-day ramp to executing any typography style within 10 minutes.

---

## Tacit 7: Photorealism Requires Camera Language
AI photorealism responds dramatically to real photography terminology—lens types, aperture settings, lighting names.

**Deploy**: Learn 10 photography terms (35mm, shallow DOF, Rembrandt lighting) and use them in prompts.

---

## Tacit 8: Edit Prompts ≠ Generation Prompts
Image editing AI needs minimal, surgical prompts. Over-prompting causes unwanted changes.

**Deploy**: For edits: "[specific change], keep everything else the same." No more.

---

## Hall of Fame Exemplars

**1. "Everbloom Botanicals" Brand Identity**
*Description*: A sophisticated organic skincare brand logo and packaging. The primary wordmark "Everbloom" is set in a slightly condensed, elegant serif font (e.g., Instrument Serif, Tacit 1) with tracking loosened by +40 (Pattern 4) for an airy, luxurious feel. The tagline "Purely from Nature" is in a delicate, wider sans-serif, chosen for height-width contrast (Pattern 3). Packaging uses subtle gray text (Pattern 11) for ingredient lists, ensuring the brand name remains the focal point. The entire composition is subtly nudged for optical centering (Pattern 8), giving it an intuitive balance.
*What makes this excellent*:
    *   **Mood-First Font Selection (Pattern 1) & 90s Serif Secret (Tacit 1)**: The serif instantly evokes timeless elegance and natural grace, perfectly aligning with an organic brand.
    *   **Height-Width Contrast Pairing (Pattern 3)**: The contrasting sans-serif for the tagline provides visual interest and hierarchy without competing.
    *   **Letter Spacing as Mood Amplifier (Pattern 4)**: Loosened tracking elevates the perceived luxury and spaciousness.
    *   **Gray Text for Visual Hierarchy (Pattern 11)**: Guides the eye to the most important information (brand name) while keeping secondary text legible.
    *   **Optical vs. Mathematical Centering (Pattern 8)**: The final composition *feels* balanced and premium, rather than rigidly mathematical.

**2. "Apex Ascent" Adventure Gear Ad**
*Description*: A dynamic social media ad for an outdoor gear company. The headline "APEX ASCENT" is set in a bold, extremely condensed sans-serif font, with line spacing compressed to -30 (Pattern 5) to create a powerful, urgent block of text (Tacit 3). A secondary, wider display font (from the same Western family, Tacit 2) is used for "Conquer the Peak" to provide visual relief and reinforce the adventure theme. A gritty texture layer is applied with an "exclusion" blending mode (Tacit 5) over a stock photo of a mountain climber, generating an unexpected, vibrant, high-contrast color palette that screams energy.
*What makes this excellent*:
    *   **Condensed = Sporty/Urgent (Tacit 3)**: The condensed font immediately conveys energy, athleticism, and the challenge of climbing.
    *   **Line Spacing Compression (Pattern 5)**: The tight leading transforms the headline into an impactful, intentional visual element.
    *   **Western Fonts Self-Pair (Tacit 2) & Height-Width Contrast (Pattern 3)**: Using a companion font from the same family ensures harmony while the width contrast maintains visual tension.
    *   **Texture Blending Modes Transform Mood (Tacit 5)**: The "exclusion" blend creates a unique, high-energy color scheme that enhances the adventurous and rugged feel, impossible to achieve with standard color picking.

**3. "Cosmic Bloom" AI Art Generation**
*Description*: A visually stunning image of a bioluminescent alien garden at night, generated with meticulous prompt engineering. The prompt was structured as: "Shot type: Extreme close-up. Lighting: Soft, glowing bioluminescence, subtle starlight. Subject: Alien flora with intricate, glowing patterns, dew drops reflecting light. Setting: Lush, overgrown alien garden at dusk. Style: Hyper-detailed, ethereal fantasy art. Mood: Mystical, serene. Camera: Macro lens, ultra shallow depth of field, bokeh."
*What makes this excellent*:
    *   **AI Model-to-Task Matching (Pattern 13)**: Likely used Seedream 3/4 or Google Image Gen 4 for artistic photorealism.
    *   **The "Big Six" Prompt Architecture (Pattern 14) & Technical-First Structure (Pattern 15)**: Ensures all critical visual elements are explicitly defined and ordered for maximum AI comprehension.
    *   **Line Break Prompt Separation (Pattern 16)**: Prevents elements from blending unintentionally, allowing the AI to render each distinct concept.
    *   **Positive Instruction Framing (Pattern 17)**: Focuses on what *should* be present, avoiding negatives that AI can misinterpret.
    *   **Photorealism Requires Camera Language (Tacit 7)**: Incorporating "Macro lens, ultra shallow depth of field, bokeh" elevates the artistic quality and realism to a professional photography standard.

**Anti-Exemplar: "Tech Solutions Inc." Website Banner**
*Description*: A website banner for a tech company featuring a generic stock photo of people looking at laptops. The headline is in a default system sans-serif font, and the subheading is a slightly smaller version of the same font. Both are mathematically centered. No intentional adjustments to tracking or leading. The image prompt used was "modern office, tech workers, no people looking bored."
*What makes this mediocre*:
    *   **Lack of Mood-First Font Selection (Pattern 1)**: The generic font conveys no specific tech mood (e.g., innovative, secure, fast).
    *   **No Height-Width Contrast (Pattern 3) or Same-Font-Family Pairing (Pattern 9)**: The default font pairing creates visual monotony and fails to establish clear hierarchy.
    *   **Default Spacing (Patterns 4, 5)**: Ignoring letter and line spacing makes the text feel unrefined and un-designed, lacking impact.
    *   **Mathematical vs. Optical Centering (Pattern 8)**: Relies on numerical centering, likely resulting in a banner that doesn't *feel* balanced.
    *   **Ineffective AI Prompting (Anti-Pattern: Generic Output)**: "No people looking bored" is a negative instruction (Pattern 17 anti-pattern); the lack of technical detail (Tacit 7) or specific style (Pattern 15) results in a bland, uninspired stock photo rather than a unique, branded image.

## Signature Moves

1.  **Mood-First Font Dive**: Immediately identifies the core emotion or desired feeling of the design, translates it into 2-3 precise keywords, and uses those as the primary filter for font selection (Pattern 1, Pattern 6). → **Deploy when**: Starting any new design project involving text or branding.
2.  **Optical Balance Override**: After any element is numerically centered or aligned, it performs a critical visual scan, often zooming out, and nudges elements by 5-10% to achieve perceived balance and natural flow, prioritizing visual harmony over mathematical precision (Pattern 8). → **Deploy when**: Finalizing layout, aligning complex shapes, or placing text blocks.
3.  **The Daily Re-Creation Gauntlet**: Dedicates a specific block of time daily to meticulously recreate a chosen reference design (often from Pinterest, Tacit 6), breaking it down into its constituent elements to understand the underlying principles of typography, layout, and composition. → **Deploy when**: Seeking to internalize new styles, refine existing skills, or overcome creative blocks.
4.  **Structured Prompt Blueprint**: Before typing a single word into an AI image generator, mentally (or physically) outlines the "Big Six" (What, Where, How it feels, Lighting, Style, Angle) and applies a technical-first structure with explicit line breaks, considering model-to-task matching (Pattern 13, 14, 15, 16). → **Deploy when**: Initiating any AI image generation task, especially for complex or specific visuals.
5.  **Texture Blend Experimentation**: When a design feels flat, lacks depth, or needs a unique color palette, it introduces a subtle texture layer and cycles through blending modes (especially "Exclusion," Tacit 5) to discover unexpected, harmonious color and depth combinations that would be difficult to manually conceive. → **Deploy when**: A design needs added visual interest, unique color exploration, or feels visually stagnant.

## Expert-Specific Quality Rubric

| Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Savant) |
|---|---|---|---|
| **Typographic Harmony & Impact** | Font selections are legible but lack distinct personality or intentional pairing. Spacing is default. | Fonts generally match the mood; pairings show basic contrast. Some manual spacing adjustments are present. | Fonts perfectly embody the desired mood (Pattern 1, Tacit 1, 3); pairings leverage height/width contrast (Pattern 3) or same-family shortcuts (Pattern 9) for maximum tension/harmony. Tracking (Pattern 4) and line spacing (Pattern 5) are meticulously adjusted for optimal effect. |
| **Visual Hierarchy & Flow** | Information is present but requires effort to discern primary from secondary. Centering is mathematical. | Clear primary and secondary text (Pattern 11) is evident. Elements are visually grouped. | Eye-path is effortlessly guided. Primary information jumps out, secondary supports. Hierarchy is reinforced by color/opacity (Pattern 11) and deliberate sizing/placement. Compositions are optically balanced (Pattern 8). |
| **AI Prompt Precision & Control** | Prompts are descriptive but often generic, leading to inconsistent or unexpected results. Many rerolls needed. | Prompts show some structure (Pattern 14) and positive framing (Pattern 17), yielding generally good results after a few attempts. | Prompts are surgically precise, employing technical-first structure (Pattern 15), line breaks (Pattern 16), and camera language (Tacit 7) to achieve intended visuals on 1st/2nd generation, utilizing optimal model-to-task matching (Pattern 13). |
| **Emotional Resonance & Mood Delivery** | Design conveys general appropriateness but doesn't evoke a specific, intended feeling. | Design aligns with the stated mood, but the emotional impact could be stronger or more nuanced. | Design powerfully and intentionally triggers the desired emotional response (Pattern 18). Font choices, color palettes (Tacit 5), and composition work in concert to create a palpable and specific mood (Tacit 1, 3). |
| **Efficiency & Cleverness of Execution** | Relies on trial-and-error for many design decisions; common problems take significant time to solve. | Utilizes some shortcuts (e.g., keyword font search, Pattern 6) but still spends time on basic elements. | Achieves complex visual effects rapidly through specific techniques (e.g., Border-as-Cutout, Pattern 12), leverages font families (Pattern 9), and applies learned patterns (Tacit 6) for near-instant, high-quality solutions. |
| **Subtlety of Centering & Alignment** | Elements are mathematically centered, leading to noticeable visual imbalance in some cases. | Most elements are mathematically centered, with some minor visual adjustments. | All elements, especially text blocks, logos, and complex shapes, are optically centered (Pattern 8) and aligned, creating a composition that *feels* perfectly balanced and professional to the eye, not just numerically. |
| **Stylistic Authenticity** | Design attempts a style but feels forced or generic, lacking depth. | Design adopts a style with reasonable fidelity, but lacks unique character or "soul." | Design authentically embodies a chosen style (e.g., 90s elegance, Western, modern tech), leveraging hidden knowledge (Tacit 1, 2, 3) to give it true character and make it feel like an original, not a copy. |
