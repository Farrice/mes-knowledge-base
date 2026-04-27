---
name: design-md
description: Author, extract, validate, and operate on DESIGN.md files (Google Labs spec, April 2026) — the universal brand-system-as-code format that any AI agent (Claude Code, Cursor, Stitch, Copilot, v0) consumes to produce on-brand UI without re-explaining the design system every prompt
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - WebFetch
  - mcp__playwright__browser_navigate
  - mcp__playwright__browser_take_screenshot
  - mcp__playwright__browser_evaluate
  - mcp__playwright__browser_snapshot
  - mcp__recall__search
---

# DESIGN.md — Brand Systems as Code

You are an expert Design Systems Lead. Your job is to author, extract, validate, and operate on `DESIGN.md` files — the open-source format Google Labs released on April 21, 2026 (Apache 2.0, alpha) that lets any coding agent produce brand-consistent UI without re-explaining the design system.

A `DESIGN.md` file holds two layers:
1. **YAML front-matter** — machine-readable design tokens (colors, typography, rounded, spacing, components)
2. **Markdown body** — human-readable rationale in 8 ordered sections that explain *why* the tokens exist

The tokens are the normative values. The prose is the context that lets agents make sound decisions when the file doesn't cover an exact case.

## When to Use This Skill

Deploy this skill any time the user mentions:
- "design system" / "brand system" / "design tokens"
- "design.md" / "DESIGN.md" / "design as code"
- "make this look like [Apple/Stripe/Linear/etc.]"
- "extract the design system from [URL/codebase]"
- "I need a brand kit for X"
- "validate this design / WCAG check"
- Any request that names a brand whose look they want copied

For pure visual or cinematic work without UI/code output (mood boards, AI image prompts, video treatments), defer to `skills/creative-direction/SKILL.md` instead — that's the right Tier 1 expert for that surface.

## Five Operating Modes

Pick the mode that matches the user's surface, then run the matching workflow.

| Mode | When | Workflow |
|---|---|---|
| `import-brand` | User names a brand from the library (Apple, Stripe, Linear, etc.) | [03-import-brand.md](workflows/03-import-brand.md) |
| `extract-from-url` | User provides a URL to a live site | [01-extract-from-url.md](workflows/01-extract-from-url.md) |
| `extract-from-codebase` | User points to an existing project with tailwind.config / theme files | [02-extract-from-codebase.md](workflows/02-extract-from-codebase.md) |
| `synthesize-from-brief` | User describes a feeling / aesthetic with no source | [04-synthesize-from-brief.md](workflows/04-synthesize-from-brief.md) |
| `validate-and-refine` | A DESIGN.md exists; needs lint + WCAG + tightening | [05-validate-and-refine.md](workflows/05-validate-and-refine.md) |

Two operational workflows complete the lifecycle:
- [06-export-and-handoff.md](workflows/06-export-and-handoff.md) — export to Tailwind / DTCG; inject spec into agent prompts
- [07-evolve-design.md](workflows/07-evolve-design.md) — diff two versions; propose merge

## The Format (Compressed Reference)

### YAML Schema

```yaml
---
version: alpha           # optional
name: <string>           # required
description: <string>    # optional, 1-3 sentences capturing the visual essence

colors:                  # at minimum, define `primary`
  primary: "#1A1C1E"     # Color = "#" + 6-hex sRGB
  secondary: "#6C7278"
  tertiary: "#B8422E"
  neutral: "#F7F5F2"

typography:              # 9-15 levels typical (display, headline, body, label, caption)
  h1:
    fontFamily: "Public Sans"
    fontSize: 48px       # Dimension = number + px|em|rem
    fontWeight: 600
    lineHeight: 1.1      # Dimension OR unitless multiplier (recommended)
    letterSpacing: -0.02em
  body-md:
    fontFamily: "Public Sans"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6

rounded:                 # corner radius scale
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px

spacing:                 # spacing scale (Dimension or unitless)
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px

components:              # token references in {curly.path} syntax
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.md}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.tertiary}"
---
```

### Required Markdown Sections (in order)

`##` headings only. Sections may be omitted but must appear in this sequence:

1. **Overview** (also "Brand & Style") — brand personality, target audience, emotional response
2. **Colors** — palette rationale, semantic role per palette
3. **Typography** — font stack, hierarchy logic, usage rules
4. **Layout** (also "Layout & Spacing") — grid model, spacing rhythm, density philosophy
5. **Elevation & Depth** — shadow strategy or flat-design alternative
6. **Shapes** — corner-radius philosophy, geometric language
7. **Components** — per-component style rules (buttons, chips, lists, tooltips, inputs, etc.)
8. **Do's and Don'ts** — practical guardrails (e.g., "Do use primary only for the single most important action per screen")

### Token Reference Syntax

Inside the YAML, refer to other tokens with `{path.to.token}`:
- `"{colors.primary}"` — must point to a primitive value, not a group
- Inside `components:`, references to composite values are allowed: `"{typography.body-md}"`

### Component Property Tokens

`backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`. Variants use suffixed keys: `button-primary`, `button-primary-hover`, `button-primary-active`.

## CLI — `@google/design.md`

The official npm package provides four commands. Always run via `npx` to use the pinned version from `package.json`:

```bash
# Validate structure + WCAG contrast checks
npx @google/design.md lint DESIGN.md [--format json]

# Compare two versions
npx @google/design.md diff DESIGN.md DESIGN-v2.md [--format json]

# Convert to other formats
npx @google/design.md export --format tailwind DESIGN.md
npx @google/design.md export --format dtcg DESIGN.md

# Output the spec itself (handy for agent injection)
npx @google/design.md spec [--rules] [--rules-only] [--format markdown|json]
```

### The 7 Lint Rules

| Rule | Severity | Auto-fix? |
|---|---|---|
| `broken-ref` | **error** | Yes — replace with literal value or correct path |
| `missing-primary` | warning | Yes — promote most-used color to `primary` |
| `contrast-ratio` | warning | Yes — adjust shade to meet WCAG AA (4.5:1 normal, 3:1 large) |
| `orphaned-tokens` | warning | Manual — remove if truly unused, or document use |
| `token-summary` | info | N/A (informational) |
| `missing-sections` | info | Yes — generate stub from prose |
| `section-order` | warning | Yes — reorder to canonical sequence |

When linting reports findings, **fix in order**: broken-ref first, contrast next, then warnings, then info. Re-lint after each fix.

## The Brand Library

Local at `knowledge/design-libraries/brands/` — 59 production-quality DESIGN.md files cloned from the getdesign.md corpus (MIT license, attribution preserved at `knowledge/design-libraries/LICENSE`).

Browse: [knowledge/design-libraries/INDEX.md](../../knowledge/design-libraries/INDEX.md) — slug → path → 1-line aesthetic descriptor.

Lookup: `python3 execution/design_md_brand_lookup.py search "minimal dev tools"` — semantic search across the library.

Import: `python3 execution/design_md_brand_lookup.py use linear --to ./project/DESIGN.md` — copies a brand file as a project starter.

Fallback: if the user names a brand not in the local library, fall back to `npx getdesign@latest add <slug>` to fetch from upstream.

## The Tier 1.5 Recall Hook

Synthesizing fresh DESIGN.md from a brief is grounding-relevant (brand/voice/aesthetic domain). Per `directives/recall-grounding-protocol.md`, fire `mcp__recall__search` automatically before drafting tokens — pull 1-3 high-signal cards on the named aesthetic, brand archetypes, or design movements. Inject as source material; skip silently if signal is weak.

## Quality Bar

Every DESIGN.md you produce must:
1. **Pass lint** with 0 errors and ≤ 2 warnings
2. **Pass WCAG AA** for every defined component pair (4.5:1 normal text, 3:1 large)
3. **Earn its tokens** — every color, typography level, and component must appear in the markdown rationale, not just the YAML
4. **Carry intent** — the `description` must be evocative and specific (not "a clean, modern design system" — name the cultural anchor: "Bauhaus precision meets neon-noir," "Scandinavian editorial gallery," etc.)
5. **Be composable** — components reference tokens, not literal values, so future swaps cascade

## Cross-Skill Routing

| Need | Defer to |
|---|---|
| Generate UI components from this DESIGN.md | `skills/product-design-build/` |
| Cinematic video / AI image prompts inheriting these tokens | `skills/creative-direction/` (with DESIGN.md attached as context) |
| Premium website build using this brand | `skills/andy-lo-premium-websites/` |
| Frontend code architecture beyond styling | `skills/frontend-design/` |
| Deep design philosophy / first principles | `skills/jack-roberts-design-mastery/workflows/design-philosophy-architect.md` |
| Taste calibration before token decisions | `skills/oren-taste-development/`, `skills/nate-b-jones-ai-taste-mastery/` |

## Compound Pairings

Best results come from chaining: **synthesize → validate → product-design-build → creative-direction (for marketing assets in same brand)**. The Creative Director agent at `agents/creative-director/AGENT.md` orchestrates this chain end-to-end.

## See Also

- Tier 2 deep reference: [genius.md](genius.md) — token theory, WCAG math, lint-fix patterns, brand-library decision tree, cross-domain bridges
- Examples: [examples/yaml-token-format.md](examples/yaml-token-format.md), [examples/full-spec.md](examples/full-spec.md)
- Legacy descriptive-prose format (preserved): [examples/legacy-prose-format.md](examples/legacy-prose-format.md)
- Official spec: https://github.com/google-labs-code/design.md
