# Impeccable Integration Setup

## Installed Surface

- Source site: https://impeccable.style/
- GitHub source: https://github.com/pbakaus/impeccable
- Upstream HEAD checked during install: `e587004ee42883dad40d14cd0f5e1b21ae1933df`
- Project skill: `.agents/skills/impeccable/`
- Global skill: `/Users/farricecain/.agents/skills/impeccable/`
- Antigravity command bridge: `/impeccable`
- CLI package: `impeccable@2.1.8`

## What It Adds

Impeccable is the frontend craft and taste layer for design work. It covers UX review, visual hierarchy, information architecture, cognitive load, accessibility, responsive behavior, typography, layout, color, motion, micro-interactions, UX copy, edge cases, and anti-pattern detection.

The system keeps it namespaced as `/impeccable ...` so the official command set does not collide with existing Antigravity commands.

## Commands

Use:

```bash
/impeccable
/impeccable critique [target]
/impeccable audit [target]
/impeccable polish [target]
/impeccable bolder [target]
/impeccable craft [feature]
/impeccable [freeform design request]
```

Official subcommands:

```text
craft, shape, teach, document, extract, critique, audit, polish,
bolder, quieter, distill, harden, onboard, animate, colorize,
typeset, layout, delight, overdrive, clarify, adapt, optimize, live
```

## Context Files

Impeccable reads `PRODUCT.md` and `DESIGN.md` before design work.

- `PRODUCT.md` defines the user, purpose, posture, tone, and anti-references.
- `DESIGN.md` defines visual direction, typography, layout, color, components, motion, and anti-slop rules.

Verify context with:

```bash
node .agents/skills/impeccable/scripts/load-context.mjs
```

## CLI Detector

Run deterministic UI anti-pattern checks with:

```bash
npm run impeccable:detect -- [file-or-directory-or-url]
```

Use detector findings as evidence, then pair them with `/design-taste-gate` or `/anti-slop-audit` for judgment and refinement directives.

## Update Process

Check skill updates:

```bash
npm run impeccable:skills:check
```

Update skill files:

```bash
npm run impeccable:skills:update
```

Update CLI version:

```bash
npm view impeccable version
npm install --save-dev impeccable@[version]
```

After updates, rerun:

```bash
node .agents/skills/impeccable/scripts/load-context.mjs
python3 execution/command_menu.py show impeccable
npm run impeccable:detect -- .tmp/impeccable-smoke/slop.html
```

## Chrome Extension

Impeccable also provides a browser extension for live design iteration. This integration documents it but does not install it silently. Install it manually from the official site when live browser selection and variant mode are needed:

https://impeccable.style/#downloads

## Operating Rule

Use Impeccable before generation when shaping or crafting UI, and after generation when auditing, polishing, hardening, or fighting generic output. The detector is useful proof, but the final verdict should still pass through human design judgment.
