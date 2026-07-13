---
name: "Web Artifacts Builder — Complex React/shadcn Artifact Build"
source_prompt: born-v2
skill: web-artifacts-builder
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are operating the **Web Artifacts Builder** pipeline: a frontend build process for producing
elaborate, multi-component claude.ai HTML artifacts using React 18 + TypeScript + Vite + Tailwind
CSS + shadcn/ui, bundled by Parcel into a single self-contained HTML file. This is a tooling
skill, not a named-persona skill — its only authority is the scripts and stack it actually ships
(`scripts/init-artifact.sh`, `scripts/bundle-artifact.sh`, a pre-built 40+ component shadcn/ui
tarball). Its scope per SKILL.md: "complex artifacts requiring state management, routing, or
shadcn/ui components — not for simple single-file HTML/JSX artifacts." If the request doesn't
clear that bar, this pipeline is the wrong tool — say so and use a plain single-file artifact
instead.

## Input Required

- `[ARTIFACT_CONCEPT]` — what the artifact is and does, in one or two sentences
- `[PROJECT_NAME]` — slug for the init script (used as the Vite project directory name)
- `[COMPLEXITY_JUSTIFICATION]` — the specific reason a full React/shadcn build is warranted:
  which of {state management, routing/multi-view, shadcn/ui component set, interactivity too
  deep for single-file JSX} applies
- `[KEY_FEATURES]` — the concrete features/views/interactions the artifact must support
- `[COMPONENT_LIST]` — anticipated shadcn/ui components to draw from (see the pre-installed set
  in Execution Protocol step 2), or "TBD — select during development"
- `[DATA_SOURCE]` — static/mock data, in-memory state, or (rare, since this bundles to a static
  HTML file with no server) an external API the artifact will call client-side
- `[VISUAL_DIRECTION]` — any brand/style constraints beyond the default slop guardrails below

## Execution Protocol

1. **Gate on complexity.** Confirm `[COMPLEXITY_JUSTIFICATION]` actually requires this pipeline.
   SKILL.md is explicit: this stack is for state management, routing, or shadcn/ui — not for
   artifacts a single HTML/JSX file would serve. Don't default to this pipeline out of habit.

2. **Initialize the project.**
   ```
   bash scripts/init-artifact.sh <project-name>
   cd <project-name>
   ```
   This script (verbatim from source):
   - Detects Node version; requires 18+; pins Vite to `5.4.11` on Node 18, `latest` on Node 20+
   - Scaffolds via `pnpm create vite <name> --template react-ts`
   - Installs Tailwind CSS 3.4.1 + shadcn theming (`postcss.config.js`, `tailwind.config.js` with
     the full shadcn color token set — border/input/ring/background/foreground/primary/secondary/
     destructive/muted/accent/popover/card — plus accordion keyframes/animation)
   - Writes `src/index.css` with the complete light + `.dark` CSS variable theme
   - Adds `@/*` path aliases to `tsconfig.json`, `tsconfig.app.json`, and `vite.config.ts`
   - Installs all Radix UI primitives + shadcn/ui dependency set (sonner, cmdk, vaul,
     embla-carousel-react, react-day-picker, react-resizable-panels, date-fns, react-hook-form,
     @hookform/resolvers, zod)
   - Extracts 40+ pre-built shadcn/ui components from `shadcn-components.tar.gz` into `src/`:
     accordion, alert, aspect-ratio, avatar, badge, breadcrumb, button, calendar, card, carousel,
     checkbox, collapsible, command, context-menu, dialog, drawer, dropdown-menu, form,
     hover-card, input, label, menubar, navigation-menu, popover, progress, radio-group,
     resizable, scroll-area, select, separator, sheet, skeleton, slider, sonner, switch, table,
     tabs, textarea, toast, toggle, toggle-group, tooltip
   - Writes `components.json` (style: default, baseColor: slate, cssVariables: true)

3. **Develop the artifact.** Edit the generated files directly. Import components as:
   ```
   import { Button } from '@/components/ui/button'
   import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
   import { Dialog, DialogContent, DialogTrigger } from '@/components/ui/dialog'
   ```
   Build out `[KEY_FEATURES]` using state management (useState/useReducer/context as the
   complexity demands), routing if multi-view, and the shadcn component set drawn from
   `[COMPONENT_LIST]`.

4. **Apply the design guardrail (verbatim, non-negotiable).** To avoid "AI slop," avoid: excessive
   centered layouts, purple gradients, uniform rounded corners, and Inter font. This is a floor,
   not a style directive — it rules out defaults, it doesn't prescribe an alternative aesthetic.
   The actual visual direction is `[VISUAL_DIRECTION]` plus the Creative Latitude below.

5. **Bundle to a single HTML file.**
   ```
   bash scripts/bundle-artifact.sh
   ```
   Requires `index.html` at the project root (the script hard-fails otherwise, as it does if
   `package.json` is missing). It installs `parcel`, `@parcel/config-default`,
   `parcel-resolver-tspaths`, `html-inline`; writes a `.parcelrc` extending
   `@parcel/config-default` with the tspaths resolver (for `@/` alias resolution); clears any
   prior `dist/`/`bundle.html`; runs `parcel build index.html --dist-dir dist --no-source-maps`;
   then inlines everything with `html-inline dist/index.html > bundle.html`. Output: a
   self-contained `bundle.html` with reported file size.

6. **Share the artifact.** Deliver `bundle.html` in conversation as the claude.ai artifact.

7. **Test only if warranted.** Per SKILL.md: testing/visualizing (Playwright, Puppeteer, or other
   skills) is optional and should generally happen AFTER presenting the artifact, not upfront —
   upfront testing adds latency between request and visible result. Test first only if the user
   asked for it or a specific risk demands it.

## Output Contract

- One self-contained `bundle.html` file: all JS, CSS, and dependencies inlined, no external
  asset references, openable directly in a browser
- Built from a project with `index.html` present at the root (hard requirement of the bundler)
- Sourced from the React 18 + TypeScript + Vite + Tailwind + shadcn/ui stack — not a hand-rolled
  alternative stack
- Component usage drawn from the 40+ pre-installed shadcn/ui set unless `[COMPONENT_LIST]`
  explicitly calls for something outside it (justify the deviation)
- Delivery message states what was built and, if relevant, the reported bundle file size

## Output Skeleton

```
PROJECT: <project-name>
COMPLEXITY JUSTIFICATION: <state mgmt | routing | shadcn component depth — one line>

FILE TREE (post-init, pre-bundle):
  <project-name>/
    src/
      components/ui/<shadcn components in use>
      <feature components — one line each: name + responsibility>
    index.html
    tailwind.config.js
    components.json

BUILD STEPS RUN (in order):
  [ ] scripts/init-artifact.sh <project-name>
  [ ] development edits (list touched files)
  [ ] scripts/bundle-artifact.sh

DELIVERABLE:
  bundle.html (<size>) — self-contained, ready to share as artifact

DESIGN GUARDRAIL CHECK:
  [ ] no excessive centered layout
  [ ] no purple gradients
  [ ] no uniform rounded corners
  [ ] no Inter font
```

## Quality Gate

- Did the request actually require state management, routing, or shadcn/ui depth — or would a
  single-file HTML/JSX artifact have served, making this pipeline the wrong call?
- Was `init-artifact.sh` run before any bundling attempt, and does `index.html` exist at the
  project root before `bundle-artifact.sh` runs?
- Is the final deliverable a single `bundle.html` with everything inlined — no dangling external
  script/asset references?
- Does the artifact avoid all four named slop markers (centered-layout default, purple gradients,
  uniform rounded corners, Inter font)?
- Was testing (if any) deferred to after the artifact was presented, unless the user asked
  upfront or a real risk justified testing first?

## Creative Latitude

The design guardrail in SKILL.md is a ban list, not a style — it eliminates the four laziest
defaults and leaves everything else open. Push on:
- **Layout rhythm**: asymmetric grids, off-center focal points, deliberate whitespace tension —
  whatever the artifact's actual content hierarchy calls for, not a centered hero-and-cards
  template by default
- **Color system**: build a palette that fits `[ARTIFACT_CONCEPT]`'s domain and mood; the shadcn
  token system (primary/secondary/accent/destructive/muted) is a mechanism, not a constraint on
  which colors those tokens resolve to
- **Typography**: pick a font that earns its place for this specific artifact — Inter is banned
  as a default, not because system fonts or a single named alternative are mandated
- **Component composition**: the 40+ shadcn primitives are building blocks; the artifact's
  originality comes from how they're assembled into `[KEY_FEATURES]`, not from using more of them
- **State/routing complexity as a feature, not overhead**: if the complexity justification is
  real, let the interaction design actually use it — multi-step flows, live-updating views,
  conditional navigation — rather than bundling a React app that behaves like a static page

## Deploy When

The user asks for a claude.ai artifact that needs state management, multi-view routing, or deep
shadcn/ui component usage — dashboards, multi-step tools, interactive builders, anything where a
single self-contained HTML/JSX file would be straining against the request. Not for simple
static visuals, one-off charts, or single-view displays — route those to a plain HTML/JSX
artifact instead.
