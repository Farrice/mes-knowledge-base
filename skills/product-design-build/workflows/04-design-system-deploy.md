# Deploy DESIGN.md as Source of Truth in a Codebase

Wire a validated DESIGN.md into a real project so it becomes the canonical source for all visual decisions. After this workflow, future component / page work flows naturally from `skills/design-md/` → DESIGN.md edit → automatic propagation.

## When to use

- Net-new project starting with a DESIGN.md
- Existing project adopting DESIGN.md for the first time
- Migrating from inline Tailwind values / CSS-in-JS to a token system

## Inputs

- `project_root` — the codebase root
- `design_md_path` — path to validated DESIGN.md (typically already at project root)

## Prerequisites

The DESIGN.md must be lint-clean:
```bash
python3 execution/design_md_validate.py <design_md_path>
# 0 errors, ≤ 2 warnings
```

If not, route to `skills/design-md/workflows/05-validate-and-refine.md` first.

## Workflow

### Step 1 — Choose the styling target

Detect the existing setup:

```bash
cd <project_root>
test -f tailwind.config.ts && echo "Tailwind"
test -f panda.config.ts && echo "Panda CSS"
test -f stitches.config.ts && echo "Stitches"
test -f vanilla-extract.config.ts && echo "Vanilla Extract"
grep -l '@chakra-ui\|@mantine' package.json
```

If no styling system is wired yet, default to **Tailwind CSS + class-variance-authority**.

### Step 2 — Install the toolchain

```bash
# Tailwind path (recommended default)
npm install -D tailwindcss postcss autoprefixer class-variance-authority @google/design.md

# Initialize Tailwind if not present
npx tailwindcss init -p
```

### Step 3 — Generate the Tailwind theme

```bash
npx @google/design.md export --format tailwind DESIGN.md > tailwind.theme.generated.js
```

Add to `.gitignore` OR commit as generated artifact (team preference). Either way: this file is regenerated on every DESIGN.md change.

### Step 4 — Wire the theme

```typescript
// tailwind.config.ts
import type { Config } from 'tailwindcss'
import { theme } from './tailwind.theme.generated.js'

export default {
  content: [
    './src/**/*.{ts,tsx,jsx,js}',
    './app/**/*.{ts,tsx,jsx,js}',
    './pages/**/*.{ts,tsx,jsx,js}',
  ],
  theme: {
    extend: theme,
  },
} satisfies Config
```

### Step 5 — Add the lint + export scripts

```json
// package.json
{
  "scripts": {
    "design:lint": "design.md lint DESIGN.md",
    "design:export": "design.md export --format tailwind DESIGN.md > tailwind.theme.generated.js",
    "design:check": "npm run design:lint && npm run design:export"
  }
}
```

(Use `npx` if `@google/design.md` isn't a direct dep; or use `design.md` if installed locally and on the PATH.)

### Step 6 — Add CI / pre-commit guards

#### Pre-commit (Husky)
```bash
npm install -D husky lint-staged
npx husky init

# .husky/pre-commit
npm run design:check
```

#### CI (GitHub Actions)
```yaml
# .github/workflows/design-check.yml
name: Design Check
on: [pull_request]
jobs:
  design:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '22' }
      - run: npm ci
      - run: npm run design:check
```

Fails the PR if DESIGN.md has lint errors or if the Tailwind theme is out of sync.

### Step 7 — Token migration sweep

For existing codebases with literal hex values / inline styles:

```bash
# Find all hex literals in source
grep -rE '#[0-9a-fA-F]{6}\b' src/ --include="*.tsx" --include="*.ts" | grep -v generated > /tmp/hex-literals.txt
wc -l /tmp/hex-literals.txt
```

For each hit, decide:
- Replace with Tailwind class referencing DESIGN.md token (`bg-primary` etc.)
- Or, if it's a one-off accent, add to DESIGN.md as a new semantic token

Run the sweep iteratively: prioritize most-used components first, knock out 5-10 per session.

### Step 8 — Document for the team

Add to project README:

```markdown
## Design System

This project uses [DESIGN.md](./DESIGN.md) as the source of truth for visual design.

- **YAML front matter** = machine-readable design tokens (colors, typography, spacing, etc.)
- **Markdown body** = human-readable rationale and usage rules

### Working with the design system

- View the spec: open `DESIGN.md`
- Validate: `npm run design:lint`
- Regenerate Tailwind theme: `npm run design:export`
- Run both: `npm run design:check` (also runs in CI)

### Adding a new color / typography level / component

1. Edit `DESIGN.md` — add the YAML token + rationale
2. Run `npm run design:check`
3. Use the new token in components: `bg-<token-name>`, `text-<level>`, etc.

### Adding a new component

Build it in `src/components/primitives/<Name>.tsx` using `class-variance-authority`. Reference DESIGN.md tokens via Tailwind classes. Never use literal hex values.
```

### Step 9 — Onboard agents

For Cursor / Claude Code / Copilot:

```bash
# Symlink DESIGN.md into agent-readable locations
ln -s ../DESIGN.md .cursorrules.design-md      # Cursor (will reference)
# Claude Code automatically picks up DESIGN.md at project root
```

Add to `CLAUDE.md` (or equivalent agent context file):
```markdown
## Design System

When generating UI code, reference [DESIGN.md](./DESIGN.md) for all visual decisions.
- Use Tailwind classes that map to DESIGN.md tokens (`bg-primary`, `text-headline-lg`)
- Never use literal hex values or px sizes — use tokens
- Validate changes with `npm run design:check`
```

### Step 10 — First validation run

```bash
npm run design:check
npm run typecheck
npm run dev
# Open http://localhost:3000 (or your dev URL)
# Visually verify: colors, typography, spacing all match DESIGN.md
```

Then run a smoke component build per [01-component-build.md](01-component-build.md) to confirm the toolchain works end-to-end.

## Multi-platform extension (optional)

For projects shipping web + iOS:

```bash
# Add Style Dictionary
npm install -D style-dictionary

# Generate iOS / Android tokens
npx @google/design.md export --format dtcg DESIGN.md > tokens.json

# tokens.config.json (Style Dictionary)
{
  "source": ["tokens.json"],
  "platforms": {
    "ios":     { "transformGroup": "ios-swift",   "buildPath": "ios/Tokens/",  "files": [{ "destination": "DesignTokens.swift", "format": "ios-swift/class.swift" }] },
    "android": { "transformGroup": "android",     "buildPath": "android/res/", "files": [{ "destination": "values/colors.xml", "format": "android/colors" }] }
  }
}

# Build all
npx style-dictionary build
```

Now DESIGN.md drives Tailwind (web), Swift constants (iOS), and Android XML (Android) — single source.

## Failure modes

| Symptom | Recovery |
|---|---|
| `tailwind.theme.generated.js` is empty | DESIGN.md has no YAML front matter; add tokens |
| Existing styles break after migration | Old defaults clashed with new tokens; map old vars to DESIGN.md tokens |
| Pre-commit hook fails on every commit | Run `npm run design:export` and commit the regenerated theme file |
| Agent ignores DESIGN.md and uses literal hex | Cite specific token names in prompts; add explicit instruction to CLAUDE.md / .cursorrules |

## Output Schema

A deployed codebase where:
- `tailwind.config.ts` imports `tailwind.theme.generated.js` and extends `theme` with it (Step 4)
- `package.json` carries `design:lint` / `design:export` / `design:check` scripts (Step 5)
- A pre-commit hook and a `.github/workflows/design-check.yml` CI job both run `design:check` (Step 6)
- The token-migration sweep (Step 7) has been run at least once, with a logged remaining-hex-literal count (`wc -l /tmp/hex-literals.txt`)
- The project README documents the Design System workflow (Step 8) and `CLAUDE.md`/`.cursorrules` is onboarded (Step 9)
- A smoke component build (Step 10, via `01-component-build.md`) confirms the toolchain end-to-end

## Quality Gate

- `npm run design:check` (Step 5) exits 0 — DESIGN.md lints clean and the Tailwind theme regenerates without error.
- Both the pre-commit hook and the CI workflow (Step 6) actually invoke `design:check` — not just documented as a plan.
- The hex-literal sweep (Step 7) was run and its output count is reported, even if the count is nonzero with a stated remediation plan — silently skipping the sweep fails this gate.
- The end-to-end smoke test (Step 10 → `01-component-build.md`) produced a component that compiles, renders, and traces every value to a token — deployment isn't "done" on config alone.
- If `tailwind.theme.generated.js` came out empty or agents keep reaching for literal hex post-deploy, the specific Failure Mode row above was consulted and its Recovery applied, not reinvented.

## See also

- [01-component-build.md](01-component-build.md) — first component after deploy
- [02-page-build.md](02-page-build.md) — first page after deploy
- [`skills/design-md/workflows/06-export-and-handoff.md`](../../design-md/workflows/06-export-and-handoff.md) — broader handoff strategies

**Execution prompts**: before producing the deliverable, check `skills/design-md/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
