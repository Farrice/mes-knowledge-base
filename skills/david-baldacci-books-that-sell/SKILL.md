---
name: david-baldacci-books-that-sell
description: David Baldacci's system for writing books that actually sell — reader-control mechanics (Big Pop openings, assumption-shattering), premise-as-seed construction, character baggage architecture, Gettysburg dialogue economy, two-purpose scene audits, slow-motion peaks, one-day eyewitness research, AND the business of publishing (royalty math, partnership deals, reader-location distribution). 200M+ copies sold; former trial lawyer.
domain: Commercial fiction craft + author business economics
when_to_use: Writing fiction or narrative nonfiction that must sell, ebook/digital-product creation end-to-end, book premises and jacket/back-cover copy, character design, dialogue/scene editing passes, pacing peak moments, publishing/platform/licensing deal analysis, book launch and distribution strategy, post-release breakdowns
version: "1.0"
format: completion-engine
workflows: 13
tiers: 3
source: David Perell "How I Write" interview (yDqPHJK0E5Q, 91 min, 19,708-word transcript), extracted 2026-07-19 forge-tier
---

# David Baldacci — Books That Actually Sell

53 novels, 7 children's books, 200M+ copies, two novels a year for 16 years — and a former trial lawyer who renegotiated his contracts from 15% royalties into partnership profit-share ("no one should make more off of the book than the person who wrote it"). Baldacci is the roster's only mastery-level holder of BOTH hats: commercial storyteller and author-businessman. His craft thesis: engineer the reader's surrender — cajole them into wrong assumptions, shatter them, take control, then make every word earn its right to be there. His business thesis: writing the books is job one; understanding how the money flows is job two, and skipping it is how careers "go down the toilet."

**Load order**: `genius.md` always → workflow → references as directed. Verbatim grounding: `references/source-quotes.md`. Business spine: `references/business-of-publishing.md`. Domain transfer: `references/craft-transfer-map.md`.

## Available Workflows

Slash commands: `/baldacci-big-pop` `/baldacci-premise-seed` `/baldacci-character-baggage` `/baldacci-trenches-draft` `/baldacci-scene-audit` `/baldacci-dialogue-economy` `/baldacci-slow-the-peak` `/baldacci-eyewitness-research` `/baldacci-stakes-forge` `/baldacci-author-economics` `/baldacci-find-your-readers` `/baldacci-ebook-flywheel` `/baldacci-game-film` (wrappers in `.agent/workflows/`).

### Tier 1 — Foundation (the core methodology)

| Workflow | Command Intent | Produces |
|---|---|---|
| `workflows/big-pop.md` | Engineer an assumption-shattering opening | Finished opening (scene/lead/hook) + bet sheet of planted assumptions and their shatter points |
| `workflows/premise-seed.md` | Build a premise containing all its food + jacket copy | Premise paragraph (conflict + maximal stakes + unlikely witness), plant-food ledger, sellable jacket copy |
| `workflows/character-baggage.md` | Architect a two-layer character | Character dossier: pre-plot baggage, core-with-flexibility, value collision, motivation-magnitude ledger, reveal schedule |
| `workflows/trenches-draft.md` | Draft long-form without outline paralysis | Drafted chapters/sections (edges-inward, chapters as connected short stories), speed-signal reads, pen-ending slate when stuck |

### Tier 2 — Practitioner (edit passes & specific techniques)

| Workflow | Command Intent | Produces |
|---|---|---|
| `workflows/scene-audit.md` | Two-purpose audit of a complete draft | Scene ledger with KEEP/COMPRESS/MOVE/CUT verdicts, 99% research cut, micro-timing reorder map |
| `workflows/dialogue-economy.md` | Gettysburg compression pass | Compressed dialogue/copy (100→10), Burstyn cuts, cargo-reassignment ledger |
| `workflows/slow-the-peak.md` | Engineer the finite peak moments | Peak map + rewritten slow-motion peak passages with consequence landing |
| `workflows/eyewitness-research.md` | One-day eyewitness research pass | Day-map, primary-artifact log, 3-5 "mechanical cowboy" planted details |
| `workflows/stakes-forge.md` | Faustian stakes + zeitgeist resonance | Stakes architecture (no-clean-exit choice, consequence chain) + named current-anxiety link |

### Tier 3 — Business & Stacking (the layer other writing skills lack)

| Workflow | Command Intent | Produces |
|---|---|---|
| `workflows/author-economics.md` | Analyze any creator-distributor deal | Money-flow map, mantra verdict, leverage-stage assessment, raise script or leverage plan, accountability questions |
| `workflows/find-your-readers.md` | Distribution & format strategy | Reader-location map, format derivatives, release-window decision, channel accountability loop |
| `workflows/ebook-flywheel.md` | Zero-to-sellable ebook sprint (STACKING) | Scheduled sprint chaining premise→draft→edit→price→launch over Dollwet/Cole machinery |
| `workflows/game-film.md` | Post-release breakdown | Intent-vs-received table, sourced reception evidence, banked corrections, raised standard |

## Stacking Guide

| Pair with | For |
|---|---|
| `sean-dollwet-kdp-publishing` | KDP mechanics under `/baldacci-ebook-flywheel`; Baldacci raises the craft ceiling and adds the economics literacy |
| `nicolas-cole-digital-products` / `nicolas-cole-nonfiction-value-architecture` | Digital packaging of the premise-seed output; nonfiction chapter architecture |
| `michael-connelly-vivid-writing` | Connelly writes the vivid scene; Baldacci controls the reader and audits the scene's right to exist |
| `how-i-write-os` | Registers Baldacci as the commercial-fiction + author-business lane of the writing arsenal |
| `luke-iha-*` / `copy-engine` | Big Pop as hook layer, motivation-magnitude as proof-to-claim law on DR copy |
| `meg-heckman-buyer-trigger-os` | Jacket copy × buyer triggers for listing/back-cover conversion |
| `kallaway-*` / `novelty-*` | Knowledge pots + unanswered questions as premise-grade seeds for the novelty engine |
| `writers-room` | Baldacci as a seat for commercial-viability and reader-control dissent on drafts |

## Quick Reference

- **The Pop**: plant 2+ assumptions, shatter via the least likely plausible path, early.
- **The premise test**: conflict + maximal stakes + unlikely witness; the plant comes with all its food; jacket copy before the book.
- **The plausibility law**: motivation magnitude must match act magnitude — the only binding constraint.
- **The Gettysburg standard**: 277 words beat two hours; 100→10; one line does the work of ten (if the character is built).
- **Two-purpose rule**: every scene advances plot / fleshes character / arms the reader — pick ≥2 or cut.
- **The 99% cut**: research everything, print the mechanical cowboy, delete the rest.
- **Slow the peak**: finite setups; anticipation over bang; decelerate at the payoff.
- **The mantra**: no one makes more off the book than the person who wrote it. Build fan base → raise the deal.
- **Distribution**: a good story sells if you find the readers where they are; marketing changes, writing doesn't.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

13 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **David Baldacci — Author Deal Brief** — `skills/david-baldacci-books-that-sell/references/prompts-v2/author-deal-brief.md`
- **David Baldacci — Big Pop Opening** — `skills/david-baldacci-books-that-sell/references/prompts-v2/big-pop-opening.md`
- **David Baldacci — Character Baggage Dossier** — `skills/david-baldacci-books-that-sell/references/prompts-v2/character-baggage-dossier.md`
- **David Baldacci — Dialogue Compression Pass** — `skills/david-baldacci-books-that-sell/references/prompts-v2/dialogue-compression-pass.md`
- **David Baldacci — Ebook Flywheel Launch Sprint** — `skills/david-baldacci-books-that-sell/references/prompts-v2/ebook-flywheel-launch.md`
- **David Baldacci — Eyewitness Research Day** — `skills/david-baldacci-books-that-sell/references/prompts-v2/eyewitness-research-day.md`
- **David Baldacci — Game-Film Breakdown** — `skills/david-baldacci-books-that-sell/references/prompts-v2/game-film-breakdown.md`
- **David Baldacci — Premise & Jacket Copy** — `skills/david-baldacci-books-that-sell/references/prompts-v2/premise-and-jacket-copy.md`
- **David Baldacci — Reader Acquisition Plan** — `skills/david-baldacci-books-that-sell/references/prompts-v2/reader-acquisition-plan.md`
- **David Baldacci — Scene Audit Report** — `skills/david-baldacci-books-that-sell/references/prompts-v2/scene-audit-report.md`
- **David Baldacci — Slow-Motion Peak Scene** — `skills/david-baldacci-books-that-sell/references/prompts-v2/slow-motion-peak-scene.md`
- **David Baldacci — Stakes Architecture** — `skills/david-baldacci-books-that-sell/references/prompts-v2/stakes-architecture.md`
- **David Baldacci — Trenches Drafting Run** — `skills/david-baldacci-books-that-sell/references/prompts-v2/trenches-drafting-run.md`

<!-- END:execution-prompts -->
