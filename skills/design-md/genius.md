# DESIGN.md — Deep Reference (Tier 2)

This is the deep reference for `skills/design-md/SKILL.md`. Load it when:
- Producing tokens for a high-stakes brand (client work, launch product)
- Diagnosing a tricky lint failure or contrast collision
- Designing a multi-mode (light + dark + high-contrast) system
- Bridging DESIGN.md tokens into Higgsfield/Kittl/Midjourney prompts so video and image work inherits the brand
- Calibrating taste before drafting (route to oren-taste / nate-b-jones first)

---

## 1. Token Theory

A design token is the smallest indivisible unit of design intent. The DESIGN.md spec defines four token types:

### Color
- **Format:** `"#" + 6-hex sRGB` only. No `rgb()`, no HSL, no `oklch()`, no named colors.
- **Why hex/sRGB:** maximum agent compatibility — Tailwind, CSS variables, Figma all consume hex without translation.
- **Limitation:** sRGB clips wide-gamut displays. Don't fight it; the spec is alpha and will likely add color-space metadata later.

### Dimension
- **Format:** number + unit (`px`, `em`, `rem`).
- **Use `rem` for type scale** (respects user font size preferences → accessibility win).
- **Use `px` for borders, single-pixel hairlines, fine geometric details** where rendering predictability matters more than scaling.
- **Use `em` for spacing inside typographic units** (e.g., letter-spacing: `-0.02em`).
- **Negative values are valid:** `letterSpacing: -0.02em` (tightening display headlines).

### Typography
A composite object (not a primitive). Required: `fontFamily`, `fontSize`. Optional but recommended: `fontWeight`, `lineHeight`, `letterSpacing`, `fontFeature`, `fontVariation`.

```yaml
hero-display:
  fontFamily: "SF Pro Display, system-ui, -apple-system, sans-serif"  # always include fallback stack
  fontSize: 56px
  fontWeight: 600
  lineHeight: 1.07     # unitless = multiplier of fontSize (CSS best practice)
  letterSpacing: -0.28px  # negative for large display, 0 for body, positive for caps/labels
```

**Line height heuristic:** display ≤ 1.1 / headline 1.1–1.2 / body 1.5–1.7 / caption 1.4–1.5. Tight line height for short large text; loose line height for long body copy.

**Weight rule:** never define more than 4 weights in a single system unless the brand specifically demands it. 400 / 500 / 600 / 700 is the standard quartet.

### Token Reference
- **Syntax:** `"{path.to.token}"` — must be quoted in YAML to avoid being parsed as flow syntax
- **Inside top-level token groups (colors, typography, rounded, spacing):** must point to a primitive, never a group
  - ✓ `"{colors.primary}"` (primitive)
  - ✗ `"{colors}"` (group — invalid)
- **Inside `components`:** composite references allowed
  - ✓ `typography: "{typography.body-md}"` (composite — fine inside components)

---

## 2. Atomic vs Semantic Token Architecture

Two-layer model produces the most maintainable systems:

### Layer 1 — Atomic (raw values)
Numbered shades. Don't carry meaning, just position in a scale.
```yaml
colors:
  blue-50: "#EBF4FF"
  blue-500: "#3B82F6"
  blue-900: "#1E3A8A"
  gray-50: "#F9FAFB"
  gray-900: "#111827"
```

### Layer 2 — Semantic (intent)
Named by role. Reference atoms via `{path}`. This is what components consume.
```yaml
colors:
  primary: "{colors.blue-500}"
  ink: "{colors.gray-900}"
  surface: "{colors.gray-50}"
  on-primary: "#FFFFFF"  # literal is fine when the value is system-fixed
```

**The win:** when the brand evolves from blue to teal, you change one atom and every semantic token + component cascades. Components never reference atoms — they reference semantics.

**When to skip atomic layer:** brands with ≤ 6 colors total. The indirection costs more than it saves.

---

## 3. WCAG Contrast Math

The lint rule `contrast-ratio` checks every component pair (`backgroundColor` vs `textColor`) against WCAG AA thresholds:

| Text size | AA ratio | AAA ratio |
|---|---|---|
| Normal (< 18pt regular, < 14pt bold) | 4.5:1 | 7:1 |
| Large (≥ 18pt regular, ≥ 14pt bold) | 3:1 | 4.5:1 |

**The contrast formula** (relative luminance):
```
L = 0.2126 R + 0.7152 G + 0.0722 B   (with sRGB → linear conversion per channel)
ratio = (L_lighter + 0.05) / (L_darker + 0.05)
```

You don't need to compute by hand — `npx @google/design.md lint` reports the exact ratio per pair. But know the heuristics:
- **Pure black on pure white = 21:1** (max possible)
- **#1A1C1E on #F7F5F2 ≈ 15.4:1** (Heritage example — well over AA)
- **#6C7278 on #F7F5F2 ≈ 4.7:1** (just clears AA for normal text)
- **#B8422E on #F7F5F2 ≈ 4.4:1** (FAILS AA for normal text — only safe for large/bold)

**Auto-fix pattern when contrast fails:**
1. If `textColor` is too light, darken it 10–20% (drop the L value in HSL space mentally).
2. If `backgroundColor` is too light, deepen the `textColor` until ratio clears.
3. Never sacrifice the brand color — instead, declare the offending pair "large-only" via component variant naming.

---

## 4. The 7 Lint Rules — Fix Patterns

### `broken-ref` (error)
A `{path.to.token}` doesn't resolve.

**Cause:** typo, deleted token, or wrong scope (referencing component property as if it were top-level).

**Fix:**
- If the target exists at a different path, update the reference.
- If the target was renamed, search-and-replace.
- If unrecoverable, replace with the literal value and document in markdown why.

### `missing-primary` (warning)
No `colors.primary` defined.

**Fix:** identify the most-used or most-emotionally-loaded color in the system; promote to `primary`. Every system needs a primary anchor — the lint exists because agents reach for `primary` first when generating new components.

### `contrast-ratio` (warning)
A component's text/background pair fails AA.

**Fix sequence:**
1. Adjust the lighter color to be lighter, or the darker to be darker.
2. If brand-locked, restrict the variant to large-text-only and rename: `button-primary-large` instead of `button-primary`.
3. As last resort, document the WCAG exception in `## Do's and Don'ts` (e.g., "Don't use the warning chip for body copy — its color pairing is for icon-only contexts").

### `orphaned-tokens` (warning)
A token is defined in YAML but never referenced anywhere (not in components, not in markdown).

**Fix:** delete it. Or, if it's intentional (e.g., reserved for future variants), reference it in `## Do's and Don'ts` ("Reserved: `colors.tertiary-90` for future seasonal accent campaigns").

### `token-summary` (info)
Statistical summary — count of colors, type levels, components. Use it to detect bloat: > 12 color tokens or > 18 type levels usually means the system isn't disciplined.

### `missing-sections` (info)
A canonical section is absent from markdown.

**Fix:** generate a stub from the YAML tokens. Even one sentence is better than absence — agents use the prose to make judgment calls when YAML is silent.

### `section-order` (warning)
Sections present but in wrong order.

**Fix:** reorder to: Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts. Order matters because consumers (agents) scan top-down.

---

## 5. Brand Library Decision Tree

Located at `knowledge/design-libraries/brands/` — 59 brands.

```
User says "make it look like X"
│
├── Is X in the local library?
│   │
│   ├── YES → import-brand mode (workflow 03)
│   │         └── Customize 1-3 tokens to differentiate
│   │
│   └── NO → check getdesign.md upstream
│             │
│             ├── Found upstream → fetch with `npx getdesign@latest add X`,
│             │                    save to library, then import-brand
│             │
│             └── Not found → extract-from-url mode (workflow 01)
│                              └── If site has clear design system: extract
│                              └── If chaotic / no clear system: synthesize-from-brief instead
```

**Customization rule:** never ship an unmodified brand-library file as the user's project DESIGN.md. The library is reference, not output. At minimum, change the `name`, `description`, and one signature element (often the tertiary/accent color or a typography weight pairing) to make it the user's own.

---

## 6. Cross-Domain Bridge — Tokens → AI Image / Video Prompts

When the user is building marketing assets that must match the UI brand, inject DESIGN.md tokens into prompts for Higgsfield/Kittl/Midjourney/Flux:

### Pattern: hex codes in prompt
```
Higgsfield prompt:
"...lit by warm tungsten at 3200K, primary highlight color #1A1C1E (deep ink),
accent backlight #B8422E (warm earthy red), shot on Cooke S7 anamorphic,
shallow DOF, color graded toward #F7F5F2 limestone neutrals..."
```

The agent reading the DESIGN.md picks up the brand's emotional center (Heritage = ink + clay + limestone) and renders video that *belongs* in the same world as the UI. Without the tokens, the video drifts toward whatever the model's prior is — usually a muddied teal-orange.

### Pattern: typography → motion graphics
Title cards in video / motion ads inherit type tokens directly:
- `hero-display` → 4–6 second establishing card
- `body-md` → captions, lower-thirds
- `label-caps` → timestamps, technical metadata overlays

### Coupling point
The Creative Director agent at `agents/creative-director/AGENT.md` is the orchestrator. When it deploys both `design-md` (UI) and `creative-direction` (cinematic) skills together, both must read the same DESIGN.md.

---

## 7. The Virgil Test — Applied to DESIGN.md

(From the Creative Director agent's quality bar.)

Before shipping any DESIGN.md, ask:

1. **Does it have a clear point of view?** Read the `description` and `## Overview`. If you could swap the brand name and it would describe a competitor, the POV is too weak.
2. **Is there a specific cultural anchor?** "Modern, clean, professional" is dead. "Bauhaus precision meets neon-noir," "Scandinavian editorial gallery," "1970s NASA telemetry" — these are anchors.
3. **One-sentence concept test.** Can you describe the brand's visual essence in one sentence? Apple's: *"A photography-first interface where chrome recedes so the product can speak."*
4. **Would removing any element make it stronger?** 12 colors with similar roles → cut to 4. 18 type levels for a marketing site → cut to 9. Less, but more disciplined.
5. **Would this still be interesting without the logo?** If the answer is no, the system is decoration, not identity.

---

## 8. Common Pitfalls

| Pitfall | Symptom | Fix |
|---|---|---|
| Color sprawl | 20+ unique hex values | Cluster into atomic shades; reference via semantics |
| Typography sprawl | 18+ type levels | Define 9–12 levels max; reuse via component composition |
| Vague description | "A modern, clean design system" | Name two cultural anchors and one tension between them |
| Decorative tokens | `colors.purple-fun: "#8B5CF6"` | Names should describe role, not vibe — `colors.accent-secondary` |
| Pure-black text | `#000000` on light backgrounds | Use `#1A1C1E` or `#111827` — softer, more readable, signals craft |
| 9999px corner radius everywhere | Pill obsession | Use `rounded.full` only for chips/avatars; use `rounded.md` for buttons |
| No `## Do's and Don'ts` | Agents make wrong calls in edge cases | Add 4–8 specific guardrails, especially around CTAs and color hierarchy |
| Components without variants | Buttons that don't define `:hover`, `:active` | Define at least `-hover` for interactive components |

---

## 9. Cross-Skill Routing — When to Defer

| Need | Skill |
|---|---|
| Generate UI components from this DESIGN.md | `skills/product-design-build/` |
| Cinematic video / AI image prompts inheriting brand | `skills/creative-direction/` |
| Premium website implementation | `skills/andy-lo-premium-websites/` |
| Frontend code architecture | `skills/frontend-design/` |
| Deep design philosophy / first-principles work | `skills/jack-roberts-design-mastery/workflows/design-philosophy-architect.md` |
| Taste calibration before token decisions | `skills/oren-taste-development/` + `skills/nate-b-jones-ai-taste-mastery/` |
| Brand strategy / identity layer above visuals | `skills/greg-hoffman-brand-mastery/` |
| Storytelling / narrative for the brand | `skills/donald-miller-storybrand/` |

Every DESIGN.md production-grade enough to ship benefits from a 2–3 minute taste calibration pass before drafting tokens. Don't skip it.

---

## 10. Why This Format Won

DESIGN.md works where prior attempts (Figma exports, brand PDFs, design-system websites) failed because:

1. **It puts token, rule, and rationale in the same file.** Figma tells you *what*; brand PDFs talk to humans; DESIGN.md is specific enough for an agent's next decision *and* carries the *why* so it stays on-system in cases the file never covered.
2. **It's plain text.** Markdown is the format LLMs read best. No special tooling required.
3. **It's machine-readable AND human-readable.** Front-matter is YAML; body is markdown. Both layers serve.
4. **It's portable across agents.** Same file feeds Claude Design, Stitch, Cursor, Copilot, v0, Claude Code. No vendor lock.
5. **It versions cleanly.** Git diff shows token changes line-by-line; `npx @google/design.md diff` adds semantic awareness on top.

The format is alpha; the value is already proven.
