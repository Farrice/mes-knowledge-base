# Validate and Refine a DESIGN.md

Run the official linter, fix every finding in priority order, ensure WCAG AA compliance, and tighten the markdown rationale.

## When to use

- After any DESIGN.md is created (extract / synthesize / import)
- Before shipping to a client
- When inheriting a DESIGN.md from another team

## Inputs

- `path` — the DESIGN.md to validate

## Workflow

### Step 1 — Run lint

```bash
python3 execution/design_md_validate.py <path>
```

Or directly:
```bash
npx @google/design.md lint <path>
```

The Python wrapper produces a richer report with auto-fix suggestions. Output is JSON-structured for parsing.

### Step 2 — Fix in priority order

Per `genius.md` Section 4, address findings in this order:

1. **`broken-ref` (errors)** — fix first; the file is structurally invalid until errors are 0
2. **`contrast-ratio` (warnings)** — fix second; agents will follow the file even when contrast fails, producing inaccessible UI
3. **`section-order` (warnings)** — easy fix; reorder canonical
4. **`missing-primary` (warnings)** — promote a color to semantic `primary`
5. **`orphaned-tokens` (warnings)** — delete or document
6. **`missing-sections` (info)** — generate stubs from YAML
7. **`token-summary` (info)** — read for bloat detection

Re-lint after each fix. Don't batch — each fix can introduce new findings.

### Step 3 — Manual contrast audit

The linter checks defined component pairs. **It cannot check pairs you haven't declared.** For each color in `colors`, mentally test:
- against `colors.neutral` (canvas) — is it readable as text?
- against `colors.surface` (cards) — is it readable as text?
- against `colors.primary` (CTAs) — is it usable as text on the primary?

For any pair that fails AA, either:
- Adjust the shade to clear AA
- Document the exclusion in `## Do's and Don'ts` ("Don't use `colors.warning` for body copy — its contrast is for icon-only contexts")

### Step 4 — Markdown rationale audit

Read each markdown section:
- **`## Overview`**: Does it name a specific cultural anchor? Does it identify a tension? If it could describe a competitor, it's too generic.
- **`## Colors`**: Is each color named with a descriptive identity (e.g., "Boston Clay," "warm limestone")? Or just "primary" / "secondary"? The descriptive names help agents make qualitative decisions.
- **`## Typography`**: Does the prose explain the *role* of each font, not just the visual? ("Public Sans for narrative; Space Grotesk for technical metadata")
- **`## Layout`**: Is the grid model named? (Fixed Max Width, Fluid Grid, Margins-Only)
- **`## Components`**: Are hover/active variants defined for interactives?
- **`## Do's and Don'ts`**: Are at least 4 specific guardrails present?

### Step 5 — Token-to-prose alignment

Every YAML token should appear in the markdown rationale. Conversely, if the markdown describes a feature ("we use a tertiary accent for warnings"), there should be a `colors.tertiary` token. Mismatch = lint warning eventually.

Quick check:
```bash
# All YAML colors mentioned in markdown?
grep -oP '"[a-z\-]+":' DESIGN.md | head -20
```

### Step 6 — The Virgil Test pass

(From `genius.md` Section 7)

1. Does it have a clear point of view?
2. Is there a specific cultural anchor?
3. One-sentence concept test — can you describe the brand visual essence in one sentence?
4. Would removing any token make it stronger?
5. Would this still be interesting without the logo?

Fail any → revise. Pass all → ship.

### Step 7 — Final lint

```bash
npx @google/design.md lint <path>
```

Acceptance criteria:
- 0 errors
- ≤ 2 warnings (with documented justification for each)
- All component pairs WCAG AA compliant

## Common Refinements

| Symptom | Refinement |
|---|---|
| Description reads "modern, clean, professional" | Add cultural anchor + tension; aim for 2-3 specific sentences |
| 18+ colors defined | Cluster atomic shades; expose only 6-10 semantic tokens |
| 20+ typography levels | Cut to 9-12; merge `body-md` / `body-default` if duplicated |
| `## Do's and Don'ts` is generic | Replace with 4-8 brand-specific guardrails about CTAs, color hierarchy, weight rules |
| No `## Elevation & Depth` section | Add at minimum: "Flat by default; tonal layering via `colors.surface`" |
| Components reference literal hex values | Refactor to use `{colors.*}` references for cascade safety |

## See also

- [genius.md Section 4](../genius.md) — Lint rules with auto-fix patterns
- [genius.md Section 7](../genius.md) — The Virgil Test
- [06-export-and-handoff.md](06-export-and-handoff.md) — once validated, export to Tailwind/DTCG and inject into agents
