# Preview and Iterate via Playwright

Render generated UI in a real browser, screenshot, critique against the DESIGN.md, and refine. The mandatory feedback loop for any non-trivial component or page.

## When to use

- After [01-component-build.md](01-component-build.md) or [02-page-build.md](02-page-build.md)
- When visual fidelity matters (always, except quick prototypes)
- Before declaring any UI work complete

## Inputs

- `target` — component or page to render
- `design_md_path` — DESIGN.md to compare against
- `breakpoints` (optional) — `[375, 768, 1280]` default

## Prerequisites

A working dev server. If none, scaffold:

```bash
# In project root, if not already initialized
npm create vite@latest .preview -- --template react-ts
cd .preview && npm install
cp ../DESIGN.md . && npx @google/design.md export --format tailwind DESIGN.md > tailwind.theme.generated.js
# Wire tailwind.config.ts to use the generated theme
npm install -D tailwindcss postcss autoprefixer class-variance-authority
```

Per `directives/browser-automation-safety.md`, Playwright navigation + screenshots are Tier 1 (auto-fire). No login or form submission.

## Workflow

### Step 1 — Start the dev server (background)

```bash
cd .preview && npm run dev
```

Use `run_in_background: true` so the loop can continue.

Wait for "Local: http://localhost:5173" in the log:
```bash
sleep 3 && curl -s http://localhost:5173 | head -5
```

### Step 2 — Navigate

```
mcp__playwright__browser_navigate("http://localhost:5173/<route>")
```

For component-only previews, build a temp route (`/preview/Button`) that renders all variants:

```tsx
// .preview/src/routes/preview/Button.tsx
export default function ButtonPreview() {
  return (
    <div className="p-lg space-y-md bg-neutral min-h-screen">
      <section>
        <h2 className="text-label-caps text-secondary mb-sm">Intent</h2>
        <div className="flex gap-sm">
          <Button intent="primary">Primary</Button>
          <Button intent="secondary">Secondary</Button>
          <Button intent="ghost">Ghost</Button>
        </div>
      </section>
      <section>
        <h2 className="text-label-caps text-secondary mb-sm">Size</h2>
        <div className="flex gap-sm items-center">
          <Button size="sm">Small</Button>
          <Button size="md">Medium</Button>
          <Button size="lg">Large</Button>
        </div>
      </section>
      <section>
        <h2 className="text-label-caps text-secondary mb-sm">State</h2>
        <div className="flex gap-sm">
          <Button>Default</Button>
          <Button disabled>Disabled</Button>
          <Button loading>Loading</Button>
        </div>
      </section>
    </div>
  )
}
```

### Step 3 — Multi-breakpoint screenshots

```
# Desktop
mcp__playwright__browser_resize(width: 1280, height: 800)
mcp__playwright__browser_take_screenshot(filename: ".tmp/preview-desktop.png", fullPage: true)

# Tablet
mcp__playwright__browser_resize(width: 768, height: 1024)
mcp__playwright__browser_take_screenshot(filename: ".tmp/preview-tablet.png", fullPage: true)

# Mobile
mcp__playwright__browser_resize(width: 375, height: 812)
mcp__playwright__browser_take_screenshot(filename: ".tmp/preview-mobile.png", fullPage: true)
```

### Step 4 — Critique against DESIGN.md

For each screenshot, ask:

| Aspect | What to check |
|---|---|
| **Color** | Primary background matches `colors.primary` hex? CTAs use `colors.primary` not a literal? |
| **Typography** | Headings match `headline-lg` size + weight + letter-spacing? Body uses `body-md`? |
| **Geometry** | Buttons have `rounded.md` corners (8px in Heritage example)? Cards use `rounded.lg`? |
| **Spacing** | Padding inside buttons matches DESIGN.md's `padding: 12px`? Section gaps match `spacing.lg`? |
| **States** | Hover state visually distinct? Focus ring visible? Disabled has reduced opacity? |
| **Hierarchy** | Most important action is most prominent? Eye flows top-to-bottom, primary-then-secondary? |

Read each screenshot literally — don't assume. If you can't tell from the screenshot whether a hover state works, hover programmatically:

```
mcp__playwright__browser_hover(selector: "button")
mcp__playwright__browser_take_screenshot(filename: ".tmp/preview-hover.png")
```

### Step 5 — Console + accessibility check

```
mcp__playwright__browser_console_messages()
```

Any errors / warnings = fix before iterating on visuals. React errors often hide visual issues.

For accessibility, install axe-core in the preview project and add a test route or programmatic check:

```bash
cd .preview && npm install -D @axe-core/react axe-core
```

Then in a dev-only entry:
```tsx
// .preview/src/main.tsx (dev branch only)
if (import.meta.env.DEV) {
  import('@axe-core/react').then(({ default: axe }) => {
    axe(React, ReactDOM, 1000)
  })
}
```

Violations log to the browser console. Capture them with:
```
mcp__playwright__browser_console_messages()
```

Fix critical / serious violations before proceeding.

### Step 6 — Edit

Based on critique, edit the component / page source. Vite hot-reloads automatically — no manual rebuild needed.

### Step 7 — Re-screenshot

Repeat steps 3-5. Compare iter-1 vs iter-2 by reading both screenshots:
- Did the change land?
- Did anything regress unintentionally?

### Step 8 — Convergence rule

**Maximum 3 iterations.** If you can't reach visual fidelity after 3 cycles:
- The DESIGN.md is under-specified → return to `skills/design-md/workflows/05-validate-and-refine.md`
- Or the design itself is fighting itself (contradictions in tokens) → `skills/design-md/workflows/07-evolve-design.md`

Don't keep guessing. The token system is the source of truth; if it's not specifying enough, fix the token system, not the code.

### Step 9 — Final acceptance screenshots

Once converged, save the final screenshots as visual regression baselines:

```bash
cp .tmp/preview-desktop.png tests/visual/<component>-desktop.png
cp .tmp/preview-tablet.png tests/visual/<component>-tablet.png
cp .tmp/preview-mobile.png tests/visual/<component>-mobile.png
```

Future runs can pixel-diff against these baselines to catch regressions.

### Step 10 — Stop the server

```
KillShell <shell_id>
```

(Or leave running if more iteration is expected.)

## Anti-patterns

- **Skipping screenshots and trusting the code** — code reading is unreliable for visual work; always render
- **Making 5+ small edits between screenshots** — too much change to attribute; iterate one focused change at a time
- **Ignoring console errors** — they hide visual bugs
- **Approving ugly hover states** — hover is half the interaction; if it looks bad, the system has a gap

## See also

- [01-component-build.md](01-component-build.md) / [02-page-build.md](02-page-build.md) — what produces the code being previewed
- [genius.md Section 4](../genius.md) — Playwright loop in technical detail
- `directives/browser-automation-safety.md` — what's allowed without confirmation
