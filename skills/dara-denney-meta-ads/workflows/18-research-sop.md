---
description: "Front door — Dara Denney's complete Elite Creative Strategy build in one sitting: reputation analysis → review mining → persona & desire segmentation → gap audit → mission doc → creative roadmap. Produces the full client-grade research + strategy package"
---

# `/dara-research-sop` — Elite Creative Strategy in One Sitting (Front Door)

The orchestrator for the whole Creative Strategy OS layer. Runs her agency's research SOP end-to-end and lands the complete package: 4 research context documents + the persona research deck + the three-gap audit + the mission doc + the creative roadmap. "The worst creative strategy is copying your competitors; the only thing slightly better is trying to get as many formats as you can. The best creative strategists can actually do strategy."

Every output doubles as an LLM context document — the package is simultaneously a client deliverable AND an AI context engine for all future creative work on the brand.

## Genius Context (Load First)

Read `genius.md` — Creative Strategy OS layer (Patterns 11-22) + `references/creative-strategy-research-sop.md` (the frame-grounded SOP source of truth).

## Input Required

- **Brand + focus product** · **Mode** (client / spec-work / own brand) · **Category posture** (direct problem-solution vs vibes-with-performance)
- **Available evidence**: review export? account access? surveys? (Missing evidence narrows steps, never skips the chain)
- **Depth**: One-Sitting (2-4h, spec/pitch grade) or Engagement (full, client grade)

## Execution (the pipeline — each step is its own workflow; run in order)

1. **`/dara-reputation-analysis`** (19) — the 7-station customer-journey doc; names THE friction point.
2. **`/dara-review-mining`** (20) — corpus + top-20 ad comments + golden nuggets + AI analysis. Deterministic pre-pass: `python3 execution/review_miner.py <reviews.csv>`.
3. **`/dara-persona-intel`** (21) — evidence-ranked personas + desire segments → research deck. **The moat deliverable.**
4. **`/dara-gap-analysis`** (22) — persona / awareness / diversity gaps vs the live account (public Ad Library version for spec mode).
5. **`/dara-mission-doc`** (23) — the strategy synthesis.
6. **`/dara-creative-roadmap`** (24) — quarterly plan + monthly roadmap + testing sheet.
7. **Handoff to production** — roadmap rows execute through workflows 01-17 (formats, hooks, statics, test plans).

One-Sitting mode: timebox steps 1-2 (prioritize Reddit + YouTube comments + Ad Library), full-strength steps 3-5, sheet-only step 6. That's her Grüns/Oats/Rhode demonstration shape.

## Output Schema — The Package

```
deliverables/<brand>-creative-strategy/   (or the client folder)
├── 01-reputation-analysis.md
├── 02-review-mining-and-analysis.md
├── 03-persona-research-deck.md          ← the moat
├── 04-gap-analysis.md
├── 05-mission-doc.md
├── 06-creative-roadmap.md               (+ testing sheet)
└── README.md                            (package map + "attach these docs when prompting" note)
```

Notion mirror: the package deploys into the **Creative Strategy OS** Notion template (see SKILL.md → Notion Template) for client-facing delivery.

## Context Adaptations

| Context | Adaptation |
|---|---|
| Brand client | Full engagement depth; package = the paid deliverable |
| Spec work / pitch | One-Sitting depth; package (or its persona brief alone) IS the pitch weapon — pair with `/dara-spec-work-engine` |
| Personal brand / creators | Same chain with audience-evidence substitutions (per-workflow adaptation tables) |

## Quality Gate

- All six artifacts present (or narrowed with reasons stated).
- The package passes each workflow's own gate — this front door adds the COHERENCE check: personas in the deck = personas in the mission doc = personas on the roadmap; every roadmap row traces to a gap; THE friction point named in step 1 is addressed somewhere in the roadmap.
- Chain Step 5.5 verification fires before client delivery (claims about real brands/people → isolated verify pass).

## When to Return

- Every new brand/client (always the entry point) · quarterly refresh of the whole package · before any high-stakes pitch.
