# Domain Docs

> Wired by `/setup-matt-pocock-skills` on 2026-06-15. Layout = single-context. `CONTEXT.md` and `docs/adr/` are created lazily by `/grill-with-docs` when terms/decisions actually get resolved — nothing is scaffolded upfront.

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

- **`CONTEXT.md`** at the repo root (ubiquitous-language glossary), and
- **`docs/adr/`** — read ADRs that touch the area you're about to work in.

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. The producer skill (`/grill-with-docs`) creates them lazily when terms or decisions actually get resolved.

## File structure (single-context)

```
/
├── CONTEXT.md            ← created lazily by /grill-with-docs
├── docs/adr/             ← created lazily; 0001-*.md, 0002-*.md, …
└── …
```

## Use the glossary's vocabulary

When your output names a domain concept (issue title, refactor proposal, hypothesis, test name), use the term as defined in `CONTEXT.md`. Don't drift to synonyms the glossary explicitly avoids. If a concept isn't in the glossary yet, that's a signal — either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/grill-with-docs`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0007 — but worth reopening because…_

## Antigravity note

This repo's PRIMARY domain knowledge lives in `CLAUDE.md`, `directives/`, and `knowledge/` — not in `CONTEXT.md`. The `CONTEXT.md`/`docs/adr/` convention here is scoped to the Matt Pocock engineering-skill workflow (software-dev tasks), kept deliberately separate from the content/orchestration system's own knowledge layer.
