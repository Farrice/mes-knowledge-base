# Extract DESIGN.md from an Existing Codebase

Reverse-engineer a DESIGN.md from project source files (Tailwind config, theme constants, CSS variables). Faster and more accurate than URL extraction when you have repo access.

## When to use

- The user has an existing app and wants to formalize its design system
- Migrating from CSS-in-JS / Tailwind to a portable spec
- Auditing a codebase before a refresh

## Inputs

- `project_root` — path to the repo
- `output_path` — where to write DESIGN.md (default: `<project_root>/DESIGN.md`)

## Workflow

### Step 1 — Detect the styling system

Look for these files in priority order:

| File | System | What to read |
|---|---|---|
| `tailwind.config.{js,ts,mjs}` | Tailwind | `theme.extend` for colors, fontSize, fontFamily, borderRadius, spacing |
| `theme.{ts,js}` / `tokens.{ts,js}` | Custom theme module | exported objects |
| `styles/globals.css` / `app.css` | CSS variables | `:root { --color-*, --font-*, --space-* }` |
| `styled-system.config.{ts,js}` | Panda CSS | `theme.tokens` |
| `unocss.config.{ts,js}` | UnoCSS | similar to Tailwind |
| `package.json` deps | Detection | `tailwindcss`, `@chakra-ui`, `@mantine`, `panda-css` |

If multiple are present, prefer the most authoritative (the one that actually renders in production — usually the build config, not abandoned CSS files).

### Step 2 — Parse colors

#### Tailwind config
```javascript
// Read tailwind.config.ts
theme.extend.colors = {
  primary: {
    50: "#EFF6FF",
    500: "#3B82F6",
    900: "#1E3A8A",
  },
  // ...
}
```

Map directly to atomic tokens: `colors.primary-50`, `colors.primary-500`. Identify semantic anchors by usage frequency in components (grep for `bg-primary-500` etc.).

#### CSS variables
```css
:root {
  --color-primary: #3b82f6;
  --color-bg: #fafafa;
}
```

Map prefixes: `--color-*` → `colors.*`, `--space-*` → `spacing.*`, `--radius-*` → `rounded.*`.

### Step 3 — Parse typography

For each font size + weight + family combo defined in config, create a typography level. Common patterns:

```javascript
// Tailwind extended fontSize
fontSize: {
  'display': ['56px', { lineHeight: '1.07', letterSpacing: '-0.02em', fontWeight: 600 }],
  'body': ['16px', { lineHeight: '1.6' }],
}
```

Map directly to `typography.{name}`. Always include the fallback stack.

### Step 4 — Parse shapes & spacing

```javascript
borderRadius: { sm: '4px', md: '8px', lg: '12px', full: '9999px' }
// → rounded: {sm: 4px, md: 8px, lg: 12px, full: 9999px}

spacing: { 1: '4px', 2: '8px', 4: '16px', 8: '32px' }
// → spacing: {xs: 4px, sm: 8px, md: 16px, lg: 32px}
```

If the codebase uses numeric Tailwind scale (1, 2, 4, 8), rename to canonical (`xs`, `sm`, `md`, `lg`). Document the mapping in `## Layout` so the team knows what changed.

### Step 5 — Sample components

Find the most-used components. For React:
```bash
# Find Button component
find . -name "Button*.tsx" -not -path "*/node_modules/*" | head -3
```

Read the variants. Each variant becomes a component token block:
```yaml
components:
  button-primary:
    backgroundColor: "{colors.primary-500}"
    textColor: "#FFFFFF"
    rounded: "{rounded.md}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.primary-700}"
```

### Step 6 — Detect elevation

Search for `box-shadow` / `shadow-*` Tailwind utilities. The most common pattern in the codebase becomes the elevation strategy described in `## Elevation & Depth`.

### Step 7 — Compose the DESIGN.md

Use [examples/yaml-token-format.md](../examples/yaml-token-format.md) as the structural template.

For `## Overview`, look at the README, marketing site, or recent commits to infer the brand's *intent*. If unclear, ask the user one question: "How would you describe the visual identity in one sentence?"

### Step 8 — Validate

```bash
python3 execution/design_md_validate.py [output_path]
```

Common findings when extracting from real codebases:
- `orphaned-tokens` — Tailwind defines colors that no component uses → cut them
- `missing-primary` — codebase has `blue-500` but no semantic `primary` → add a semantic alias
- `contrast-ratio` — `gray-400` text on `gray-200` background → mark as "for placeholder only" in components

### Step 9 — Generate Tailwind compatibility shim (optional)

If the user wants to keep the existing codebase compiling while adopting DESIGN.md:

```bash
npx @google/design.md export --format tailwind DESIGN.md > tailwind.theme.generated.js
```

Then in `tailwind.config.ts`:
```javascript
import { generated } from './tailwind.theme.generated.js'
export default { theme: { extend: generated } }
```

This way, DESIGN.md becomes the source of truth and Tailwind auto-syncs.

## Output

A valid DESIGN.md at `output_path` that:
- Reflects the codebase's actual rendered styling (not its aspirational README)
- Has 0 lint errors
- Identifies orphaned tokens for cleanup

## See also

- [01-extract-from-url.md](01-extract-from-url.md) — when no codebase access
- [06-export-and-handoff.md](06-export-and-handoff.md) — emit Tailwind/DTCG from DESIGN.md
- [04-design-system-deploy.md](../../product-design-build/workflows/04-design-system-deploy.md) — wire DESIGN.md back into the codebase as source of truth
