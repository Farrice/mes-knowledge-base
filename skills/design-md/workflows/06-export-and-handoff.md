# Export DESIGN.md and Hand Off to Agents

Convert a validated DESIGN.md into Tailwind config, DTCG tokens, or agent-injectable spec. The bridge between authoring and shipping.

## When to use

- DESIGN.md is validated; ready to wire into a real codebase
- Handing off to another team using a different stack
- Injecting brand context into a long-running coding agent session

## Inputs

- `path` — the validated DESIGN.md
- `target` — `tailwind` | `dtcg` | `spec` | `agent-prompt`

## Workflow

### Target 1: Tailwind theme

```bash
npx @google/design.md export --format tailwind <path> > tailwind.theme.generated.js
```

Output structure:
```javascript
export const theme = {
  colors: { primary: '#1A1C1E', ... },
  fontSize: { 'hero-display': ['56px', { lineHeight: '1.07', letterSpacing: '-0.02em' }], ... },
  borderRadius: { sm: '4px', md: '8px', lg: '12px', full: '9999px' },
  spacing: { xs: '4px', sm: '8px', md: '16px', lg: '32px' },
}
```

Wire into `tailwind.config.ts`:
```typescript
import { theme } from './tailwind.theme.generated.js'

export default {
  theme: { extend: theme },
  // ...
}
```

**Recommendation:** treat `tailwind.theme.generated.js` as build artifact (gitignore or commit as generated). Re-run export after every DESIGN.md change. This makes DESIGN.md the canonical source.

### Target 2: DTCG (Design Tokens Community Group format)

```bash
npx @google/design.md export --format dtcg <path> > tokens.json
```

Output is the standard `tokens.json` format readable by Figma Tokens Studio, Style Dictionary, and Token Studio plugins. Use when:
- Designers need to import tokens into Figma
- The team uses Style Dictionary for multi-platform output (web + iOS + Android)

Pipeline:
```
DESIGN.md  →  tokens.json  →  Style Dictionary  →  CSS / iOS Swift / Android XML
```

### Target 3: The spec itself (for agent education)

```bash
npx @google/design.md spec --format markdown > .design-md-spec.md
```

Use when:
- Onboarding a teammate or a fresh agent context
- Documenting why DESIGN.md is the source of truth

Add `--rules-only` to get just the lint rules — useful for embedding in CI checks or pre-commit hooks.

### Target 4: Agent prompt injection

When using DESIGN.md with Cursor / Claude Code / Copilot for an extended session:

```bash
npx @google/design.md spec --format json | jq '.fullSpec'
# (or just include the full DESIGN.md in the agent's system context)
```

**Recommended practice:** at the start of any UI session, paste the DESIGN.md content (or symlink it into the working directory) and tell the agent:
> "Use this DESIGN.md as the source of truth for all UI decisions. When generating components, reference tokens via `{colors.*}` etc. Don't invent new color values."

For Claude Code, the file at the project root is automatically discovered if named `DESIGN.md`.

For Stitch:
- Upload via [claude.ai/design](https://claude.ai/design) → "Add assets" → DESIGN.md
- Or attach in the chat with: "Create a design system from this DESIGN.md"

### Target 5: A README starter pack

For teams adopting DESIGN.md for the first time:

1. Copy the validated DESIGN.md to repo root
2. Add a short section to the project README:
```markdown
## Design System

This project uses [DESIGN.md](./DESIGN.md) as the source of truth for visual design.
- Tokens: see YAML front matter
- Rationale: see markdown body
- Validate: `npx @google/design.md lint DESIGN.md`
- Tailwind: `npx @google/design.md export --format tailwind DESIGN.md`
```

3. Add `npx @google/design.md lint DESIGN.md` to CI pre-commit checks.

## Multi-Platform Pipeline (Recommended)

For products shipping to web + mobile + design tools:

```
DESIGN.md (canonical)
    │
    ├── npx @google/design.md export --format tailwind  →  Tailwind config
    ├── npx @google/design.md export --format dtcg      →  tokens.json
    │                                                       │
    │                                                       ├── Figma Tokens Studio (designers)
    │                                                       ├── Style Dictionary → iOS .swift
    │                                                       └── Style Dictionary → Android .xml
    └── (manual) markdown body → AI agent prompt context
```

Sync direction is one-way: **DESIGN.md → everything else**. Designers edit DESIGN.md, regenerate Figma tokens. Engineers regenerate Tailwind. Single source.

## Failure modes

| Symptom | Recovery |
|---|---|
| `export` produces empty / minimal output | DESIGN.md has no YAML front matter — add tokens before exporting |
| Tailwind theme breaks existing styles | Old codebase had implicit defaults; map them to DESIGN.md tokens manually |
| Agent ignores the DESIGN.md | Re-paste at the top of the conversation; cite specific token names in prompts |
| DTCG export has unexpected structure | Spec is alpha; check the upstream repo for format updates |

## See also

- [05-validate-and-refine.md](05-validate-and-refine.md) — always validate before exporting
- [../../product-design-build/workflows/04-design-system-deploy.md](../../product-design-build/workflows/04-design-system-deploy.md) — wire DESIGN.md into a real codebase end-to-end
- Spec: https://github.com/google-labs-code/design.md
