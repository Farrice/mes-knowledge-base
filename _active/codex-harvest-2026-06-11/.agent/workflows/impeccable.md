---
description: Namespaced Impeccable bridge for taste-aware frontend design, critique, polish, and anti-slop QA
---

# /impeccable - Impeccable Design Bridge

Use the installed Impeccable skill as the taste, judgment, and frontend craft layer for Codex Antigravity.

This bridge keeps Impeccable namespaced so its 23 official commands do not collide with existing Antigravity commands.

## Usage

```bash
/impeccable
/impeccable critique [target]
/impeccable audit [target]
/impeccable polish [target]
/impeccable bolder [target]
/impeccable craft [feature]
/impeccable [freeform design request]
```

## Pre-Flight

Read, in order:

1. `.agents/skills/impeccable/SKILL.md`
2. `PRODUCT.md`
3. `DESIGN.md` if present
4. The matching command reference under `.agents/skills/impeccable/reference/` when the first argument is an Impeccable command

Run the context loader before any design action:

```bash
node .agents/skills/impeccable/scripts/load-context.mjs
```

If PRODUCT.md is missing, empty, or placeholder-like, stop and run `/impeccable teach` before continuing. If DESIGN.md is missing, nudge once and continue unless the task depends on a design system.

State this before any implementation file edits:

```text
IMPECCABLE_PREFLIGHT: context=pass product=pass command_reference=pass shape=pass|not_required image_gate=pass|skipped:<reason> mutation=open
```

## Command Routing

Valid official subcommands:

| Command | Purpose |
|---|---|
| `craft` | Shape, confirm, then build a feature end to end |
| `shape` | Plan UX/UI before implementation |
| `teach` | Establish PRODUCT.md and DESIGN.md context |
| `document` | Generate DESIGN.md from existing project code |
| `extract` | Pull reusable design tokens and components into the system |
| `critique` | UX and visual design review |
| `audit` | Technical quality checks, accessibility, performance, responsive behavior |
| `polish` | Final quality pass before shipping |
| `bolder` | Make bland work more distinctive |
| `quieter` | Reduce overstimulation while preserving quality |
| `distill` | Strip complexity to the essential design |
| `harden` | Add production edge cases, overflow, i18n, and errors |
| `onboard` | First-run, empty-state, and activation design |
| `animate` | Purposeful motion and micro-interactions |
| `colorize` | Strategic color pass |
| `typeset` | Typography, hierarchy, and readability |
| `layout` | Spacing, rhythm, alignment, and composition |
| `delight` | Memorable touches and personality |
| `overdrive` | Ambitious visual effects and advanced craft |
| `clarify` | UX writing, labels, and error messages |
| `adapt` | Responsive and cross-device adaptation |
| `optimize` | UI performance diagnosis and fixes |
| `live` | Browser-based variant exploration |

Routing rules:

1. No argument: show the grouped official command menu and suggest the most likely starting command.
2. First word matches a command: load `.agents/skills/impeccable/reference/[command].md` and follow it.
3. First word does not match: treat the full argument as a general design task and apply the Impeccable setup, register, and shared design laws.
4. Do not create standalone shortcut commands in v1. Use `node .agents/skills/impeccable/scripts/pin.mjs pin <command>` only if the user explicitly asks.

## Antigravity Integration

Use Impeccable as a support gate with these workflows:

- `/creative-design-agent`: use for frontend craft, visual judgment, design shaping, and anti-generic refinement.
- `/design-taste-gate`: use `critique`, `polish`, `typeset`, `layout`, or `bolder` when a finished design needs sharper directives.
- `/anti-slop-audit`: run `impeccable detect` when an HTML/file/URL target is available, then combine deterministic findings with the human 15-point scorecard.
- `/design-md-synthesize`: make sure the resulting DESIGN.md includes anti-references and specific visual laws that Impeccable can use.

## Detector

When a file, directory, or URL is available, run:

```bash
npm run impeccable:detect -- [target]
```

Use the detector as evidence, not as the whole verdict. Pair it with human taste judgment and the relevant Antigravity creative gate.

## Output

Return:

- Intent and target interpreted
- Impeccable command/reference used
- Context loader status
- Findings, build plan, or revised artifact
- Detector result if available
- Next useful command only when it moves the work forward
