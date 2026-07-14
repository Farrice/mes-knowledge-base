# Guide Format Contract — how every session guide is written

> The template is `docs/ROOT-CORE-OPERATOR-GUIDE.md` (the Matt Pocock merge guide — Farrice's calibrated exemplar, 2026-07-13: "a lot of depth, condensed, information density, actionable things and insights, well organized"), plus two density upgrades below. The end-session spine points here; guide writers read the exemplar + this file before writing. Never a bare change-list, never generic summary prose.

## Required structure, in order

1. **Frontmatter** — `date` / `session` / `tier: operator-guide | session-brief` / `status: enriched`.
2. **Title** — `X — What We Built [DATE] and How to Use It`, then a one-paragraph blockquote: what the session produced + companion file pointers.
3. **⚡ If you only read 10 lines** *(upgrade #1)* — the guide's densest payload as ~10 bullets: the commands, the thresholds, the one doctrine line, the first thing to run. A 30-second refresh must be possible without reading further.
4. **Command table** *(upgrade #2)* — one row per invocation surface: `command → what it produces → reach for it when`. Scannable invocations without prose.
5. **The mental model** — the 2-4 ideas that make everything else obvious. Read-once section.
6. **Per-capability sections** — for each capability shipped: **What it is** (mechanism, not marketing) / **When to reach for it** (the tell, in operator terms) / **When NOT to** (explicit, with the cheaper alternative named) / **How to invoke** (exact commands/paths, verbatim-checked against the files — never invented flags) / **Worked example** (from the live session where one exists) / **Honest edges** (what's untested, pending, or known-weak — never omitted).
7. **Composition table** (when relevant) — what this stacks with, framed as OPTIONS per no-forced-wiring, with when-it-earns-its-cost.
8. **Session-brief tier** uses items 1-3 + a snapshot (completed / decisions / where things live) — a brief is a scannable memory of the session, not a manual.

## Density rules

- Every claim actionable or load-bearing — if a sentence changes no decision and starts no action, cut it.
- Numbers and commands verbatim from the files on disk, never from memory.
- 1,200-2,000 words for operator guides; 400-800 for briefs. Tables over prose for enumerable facts.
- Pointer, don't duplicate: if a deeper guide exists (e.g. a skill's own USER-GUIDE), the session guide is the entry point that routes to it.
- No AI-slop phrasing (directives/ai-slop-ban-bank.md applies).

## Wiring (context-bloat guard — standing)

Guides are **pull-only**: no hook loads them, no router indexes them, no slash commands are generated from them. Entry is `guides/INDEX.md` (use-case table + chronology) — update it with every guide, clear the Pending line, and stamp `python3 execution/operator_guide_sync.py record`.
