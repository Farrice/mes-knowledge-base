# Extract DESIGN.md from a Live URL

Reverse-engineer a complete DESIGN.md from a public website using Playwright (browser automation) + heuristic token extraction. Output: a valid DESIGN.md that captures the visual identity of the source.

## When to use

- User says "make it look like https://stripe.com" and the brand isn't in the local library
- User wants to study a competitor's design system
- Auditing your own site to produce a canonical DESIGN.md

## Inputs

- `url` — the page to analyze (use the brand's marketing homepage, not a docs page)
- `output_path` — where to write the DESIGN.md (default: `./DESIGN.md`)

## Workflow

### Step 1 — Navigate and snapshot

Use Playwright MCP. Per `directives/browser-automation-safety.md`, navigation + screenshot are Tier 1 (auto-fire). No login, no form fills.

```
mcp__playwright__browser_navigate(url)
mcp__playwright__browser_take_screenshot(filename: ".tmp/source.png", fullPage: true)
mcp__playwright__browser_snapshot()  # accessibility tree
```

### Step 2 — Extract computed styles

Run JavaScript in the page to harvest the design tokens that actually rendered, not just the source CSS:

```javascript
// Inject via mcp__playwright__browser_evaluate
() => {
  const sample = (selector) => {
    const el = document.querySelector(selector);
    if (!el) return null;
    const cs = getComputedStyle(el);
    return {
      color: cs.color,
      backgroundColor: cs.backgroundColor,
      fontFamily: cs.fontFamily,
      fontSize: cs.fontSize,
      fontWeight: cs.fontWeight,
      lineHeight: cs.lineHeight,
      letterSpacing: cs.letterSpacing,
      borderRadius: cs.borderRadius,
      padding: cs.padding,
    };
  };
  return {
    body: sample('body'),
    h1: sample('h1'),
    h2: sample('h2'),
    h3: sample('h3'),
    p: sample('p'),
    button: sample('button, [role=button], a.btn, .button'),
    primary: sample('button[type=submit], .btn-primary, .button-primary'),
    input: sample('input[type=text], input[type=email]'),
    card: sample('.card, article, section.card'),
  };
}
```

### Step 3 — Convert RGB to hex sRGB

Computed styles return `rgb(r, g, b)` or `rgba(...)`. Convert all colors to `#RRGGBB`. Drop alpha (DESIGN.md uses opaque sRGB only). Cluster near-duplicates (within ΔE < 3) into single tokens.

### Step 4 — Identify semantic roles

From the harvested data:
- `colors.primary` = the most-used non-neutral color (typically the CTA / brand accent)
- `colors.neutral` = body background
- `colors.surface` = card / panel background (if distinct from neutral)
- `colors.ink` = body text color
- `colors.secondary` = secondary text (captions, metadata)
- Add `colors.tertiary` only if a third clearly-distinct accent is present

### Step 5 — Build typography scale

Extract h1, h2, h3, body, caption sizes. Map to canonical names:
- `hero-display` (≥ 48px) — if h1 is dramatic
- `headline-lg` / `headline-md` / `headline-sm` — h1, h2, h3
- `body-lg` / `body-md` / `body-sm` — paragraph variants
- `label-caps` — uppercase labels (look for text-transform: uppercase)

Always preserve fallback stack: `"Inter, system-ui, -apple-system, sans-serif"`.

### Step 6 — Map shapes & spacing

- `rounded.sm/md/lg` — sample `border-radius` from buttons, inputs, cards
- `spacing.sm/md/lg/xl` — sample `padding` and `gap` from major containers; quantize to 4px or 8px scale

### Step 7 — Detect elevation strategy

Inspect `box-shadow` on cards and modals. Three patterns:
- Shadows present → describe in `## Elevation & Depth` ("Subtle elevation via diffused shadows: `0 1px 3px rgba(0,0,0,0.1)`")
- No shadows, color contrast separates layers → "Flat design with tonal layering"
- Heavy shadows → "Pronounced elevation with strong drop shadows for hierarchy"

### Step 8 — Compose the DESIGN.md

Use [examples/yaml-token-format.md](../examples/yaml-token-format.md) as the structural template. Required sections in order: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts.

For the `## Overview`, write 2-3 sentences capturing the *cultural anchor* — don't say "modern, clean, professional." Look at the screenshot and name the actual aesthetic ("Editorial gallery meets fintech precision," "Brutalist tooling for developers," etc.).

### Step 9 — Validate

```bash
python3 execution/design_md_validate.py [output_path]
```

Wraps `npx @google/design.md lint`. Fix in priority order: broken-ref → contrast-ratio → other warnings. If contrast fails, re-pick a darker shade for the failing component variant.

### Step 10 — Save snapshot for future diff

Write the screenshot path and source URL into the markdown body as a comment:
```markdown
<!-- Extracted from https://stripe.com on 2026-04-27 — see .tmp/source.png -->
```

## Output

A valid DESIGN.md at `output_path` that:
- Passes `lint` with 0 errors and ≤ 2 warnings
- Has every component pair WCAG AA compliant
- Captures within 5% ΔE of the source's primary color
- Names a specific cultural anchor in the description

## Failure modes

| Symptom | Likely cause | Recovery |
|---|---|---|
| Computed styles return generic system fonts | Site uses CSS `@font-face` not yet loaded | Add `await new Promise(r => setTimeout(r, 2000))` before sampling |
| All colors come back as `rgb(0,0,0)` | Site requires JavaScript to render | Use `mcp__playwright__browser_wait_for` on a key element before sampling |
| Cards / buttons not found | Non-standard markup | Look at the screenshot; re-write selectors based on visible elements |
| Lint shows broken-ref errors | Token references typed incorrectly | Quote them properly: `"{colors.primary}"` not `{colors.primary}` |

## See also

- [02-extract-from-codebase.md](02-extract-from-codebase.md) — extract from project files instead of live site
- [05-validate-and-refine.md](05-validate-and-refine.md) — full lint+WCAG refinement loop
