# Marketing Studio Director — Genius Context

> Load this before routing any Higgsfield Marketing Studio prompt. This is a TOOL/SYSTEM skill — the "expert" is the documented product behavior of Higgsfield Marketing Studio itself, not a person. Every pattern below is grounded in the skill's own primary sources: `skills/marketing-studio-director/SKILL.md` (20,405 bytes), `references/genius-patterns.md` (1,808 bytes), `references/hidden-knowledge.md` (546 bytes), and the 9 structure-pure v2 workflow files in `references/prompts-v2/` (~13,000 bytes each, `refactored: 2026-07-13`). No `extractions/` folder exists for Higgsfield or Marketing Studio (checked: `ls extractions/ | grep -i higgsfield` and `grep -i "marketing.studio"` both return nothing) — this skill is built from the tool's own documented interface, not a watched/transcribed source, so every claim below anchors to an in-repo file, never to an invented interview or transcript.

---

## How to Use This Skill (Model Calibration)

These are intuition primitives for routing and writing Marketing Studio prompts, not a checklist to recite. Absorb the preset grammar, then write the prompt — never announce the machinery.

Specifically:
- Do NOT enumerate which of the 9 presets, which Engine Rule, or which Hard Constraint you applied. Execute the routing silently; only the final prompt paragraph and the `Generate:` link are ever shown to the user.
- Do NOT label parts of your output "Camera:", "Style & Mood:", "Product Placement:" — SKILL.md is explicit that section labels are a broken-output condition, not a style choice.
- The tool's entire fidelity model depends on invisible restraint: when a product or avatar image is attached, the highest-skill move is describing it with zero embellishment — same packaging, same face, same wardrobe — not "elevating" it. Polish that adds unrequested claims or restyled products is the tell-class failure this skill exists to prevent.
- Register discipline over vocabulary: UGC and TV Spot can describe the same product, but a TV Spot prompt that reads like a UGC prompt (or vice versa) has failed the preset router even if every individual sentence is well-written. The 9-preset table and the ≤15-second hard duration cap are the two non-negotiable structural facts to check before writing a word.

---

## Genius Patterns

Five governing patterns (source: `skills/marketing-studio-director/references/genius-patterns.md`, 1,808 bytes, migrated verbatim below with entities restored from SKILL.md for grounding).

### 1. Preset Is the Grammar
**Execute**: Identify or honor the Marketing Studio preset before writing. Let the preset decide camera behavior, pacing, environment, and register.
**Deploy When**: Every one of the 9 Higgsfield Marketing Studio prompts (UGC, Tutorial, Unboxing, Hyper Motion, Product Review, TV Spot, Wild Card, UGC Virtual Try On, Pro Virtual Try On — SKILL.md preset router table, lines 50-60).
**Success Metric**: UGC feels phone-native, TV Spot feels composed, Hyper Motion is kinetic — the same product image produces 9 visibly distinct registers, never one register with swapped nouns.

### 2. Fidelity Before Flourish
**Execute**: When product or avatar images are attached, preserve exact product packaging, color, logo placement, proportions, avatar face/build, and user-specified wardrobe.
**Deploy When**: Any prompt with product or avatar references — SKILL.md names this "non-negotiable" twice in the same paragraph ("Product fidelity is non-negotiable" / "Avatar fidelity is non-negotiable").
**Success Metric**: Zero restyled reference assets, zero invented brand claims (e.g. never "clinically proven" or "10x faster" — the two example fabrications SKILL.md explicitly bans).

### 3. Visible Action Only
**Execute**: Describe what can be seen or heard. Use outcome-based action instead of biomechanics, and show state changes on camera.
**Deploy When**: Product demos, tutorials, unboxings, reviews, try-ons — any preset where a hand touches a product.
**Success Metric**: Every action reads like "twists the cap off, sets the bottle down" — never "right hand rotates cap counterclockwise while left stabilizes base" (the skill's own correct/wrong pair).

### 4. Single-Paragraph Production Prose
**Execute**: Return one flowing paragraph with camera, action, environment, product placement, mood, and audio woven together, followed by the generation link.
**Deploy When**: Every Marketing Studio final output — this is what SKILL.md calls "the defining difference from a Seedance prompt."
**Success Metric**: Zero labels, shot headers, markdown, JSON, or commentary leak into the final response; response ends in exactly one blank line then the `Generate:` link.

### 5. Age-Blind Avatar Description
**Execute**: Describe avatars by appearance, wardrobe, and delivery style, never by age category.
**Deploy When**: Any prompt involving a presenter, creator, model, or wearer.
**Success Metric**: The prompt contains none of the six banned trigger words — "boy, girl, child, kid, young, teen, little" — and still gives enough visual direction to generate a distinct-looking avatar.

---

## Hidden Knowledge

Source: `skills/marketing-studio-director/references/hidden-knowledge.md` (546 bytes — small file, fully read, not truncated).

- **Platform bias**: Marketing Studio works best when one location, one product focus, and one preset grammar are clear per generation. Product placement needs to be stated in-frame, not implied — this is why the "Product placement in frame must be explicit" hard constraint exists as its own bullet in SKILL.md rather than folded into fidelity.
- **Failure mode**: reference drift. If a product or avatar image is provided, fidelity beats style upgrades, extra claims, and aesthetic embellishment — every single time, with no preset-level exception (all 9 presets inherit the same Engine Rules block).
- **Operating rule**: write for what the model can see or hear. Off-screen state changes are treated as nonexistent by the renderer — "Exit-frame = implicit cut" and "Off-screen = nonexistent" are two separate hard constraints in SKILL.md's Engine Rules, not one restated twice.

---

## Known Anti-Patterns (Sourced)

Each item below is source-attributed to the exact in-repo file it is drawn from — no invented provenance. Where the skill's own text is quoted verbatim, the quote is reproduced exactly as written in the cited file.

- **Never restyle or "improve" a fidelity-locked product.** Verbatim source: `skills/marketing-studio-director/SKILL.md`, Engine Rules — "Never restyle or 'improve' the product." A prompt that upgrades packaging color or logo placement on an attached product image is a broken generation, not a creative choice.
- **Never describe an avatar with an age marker.** Verbatim source: `skills/marketing-studio-director/SKILL.md` — "Trigger words to avoid: boy, girl, child, kid, young, teen, little." This is listed as a Safety-tier Hard Constraint, not a style preference, and repeats identically across all 9 workflow files in `references/prompts-v2/` (dated `refactored: 2026-07-13` in each file's frontmatter).
- **Never write biomechanical action description.** Verbatim source: `skills/marketing-studio-director/SKILL.md` — the banned example reads "right hand rotates cap counterclockwise while left stabilizes base," contrasted against the approved "twists the cap off, sets the bottle down."
- **Never invent an invisible sensory claim.** Verbatim source: `skills/marketing-studio-director/SKILL.md` — banned example: "The product smells fresh." Only what is visible or audible in frame is permitted (the approved pairing is condensation beading on a bottle, label glistening).
- **Never leak a section label into final output.** Verbatim source: `skills/marketing-studio-director/SKILL.md`, Output Rules — "No section labels (no 'Style & Mood:', 'Dynamic Description:', etc.)." This is the single most-repeated constraint in the file, appearing in both the Output Format section and the Hard Constraints section.
- **Never use a banned Antislop word.** Verbatim source: `skills/marketing-studio-director/SKILL.md`, Antislop list — 40+ banned terms including "breathtaking," "cinematic masterpiece," and "game-changer." This list is reproduced identically in every one of the 9 `references/prompts-v2/*.md` workflow files (each carrying `standard: structure-pure-v2` in frontmatter), confirming it is a hard floor, not a per-preset suggestion.
- **Never shoot a reflection unless the preset explicitly calls for a mirror.** Verbatim source: `skills/marketing-studio-director/SKILL.md`, Engine Rules — "Avoid reflection shots (in screens, mirrors, glass, puddles) — reflections break geometry," with the single named exception being UGC Virtual Try On's mirror-framing device.

---

## Corpus Exemplars (Verbatim)

Three worked examples quoted directly from `skills/marketing-studio-director/SKILL.md` (Output Format section) to calibrate register — not to be copied, only studied for density of sensory/physical beats.

> A phone-native selfie handheld take in a sunlit kitchen — warm morning light through a window behind her, soft highlights on the countertop. The creator sits at the counter in a cream knit sweater, hair loose, holding a chilled matcha energy can at chest height, label angled toward camera.

Source: SKILL.md Example 1 (UGC), quoted from the 20,405-byte file's Output Format section.

> Cinematic wide establishing shot of a marble-topped dresser in a dimly lit penthouse at dusk, city lights glowing through a floor-to-ceiling window behind it. The camera pushes slowly forward on a motorized dolly, passing a folded silk pocket square and a crystal tumbler, settling on the watch resting on a dark leather tray.

Source: SKILL.md Example 2 (TV Spot), user input line specifies "12 seconds" — the only example with an explicit duration constraint.

> A saturated gradient void — deep magenta bleeding into electric blue — as the energy gel sachet rockets into frame from below on a tight orbit, the camera whipping around it at 180 degrees per second.

Source: SKILL.md Example 3 (Hyper Motion) — the 180-degrees-per-second orbit speed is the only quantified camera-motion figure anywhere in the skill's three worked examples.

---

## Recognition Test

The test for any generated Marketing Studio prompt: would a Higgsfield Marketing Studio operator — someone who has run all 9 presets and knows the platform's actual rendering failure mode, named in `hidden-knowledge.md` as "reference drift" — recognize this as theirs, or would they recognize this as a generic AI-video prompt wearing Marketing Studio vocabulary? If the second, rebuild it against the preset's camera signature and register (SKILL.md's Appendix B quick-reference table, 9 rows, one per preset) before shipping.

A prompt passes the recognition test only if a person who has actually used the 9-preset system could identify which preset it targets without being told — UGC's phone-native single take, Hyper Motion's beat-driven multi-cut, and TV Spot's structured arc must each be legible from the prose alone, with zero section labels to give it away.

---

## Source Ledger (Pointer)

Full claim-by-claim VERIFIED/LIKELY/UNCONFIRMED table lives at `skills/marketing-studio-director/references/source-ledger.md` (12 sources catalogued: SKILL.md, genius-patterns.md, hidden-knowledge.md, and the 9 `prompts-v2/*.md` workflow files). No claim in this document is sourced from anywhere outside that ledger.
