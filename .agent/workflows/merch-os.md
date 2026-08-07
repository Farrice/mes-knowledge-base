---
description: "Merch OS — the Meg Heckman operating system for apparel/POD/product brands. Brand-in → launch-out: GROUND (sub-identity) → CONCEPT (sprint) → SCORE (trigger audit) → LISTING (copy + design handoff) → LAUNCH (channel plan) → DIAGNOSE (metrics instrumentation). Phase-gated, resumable, brand-agnostic (Josh, MyBPM, clients)."
tier: system
---

# /merch-os — The Buyer-Trigger Operating System for Merch

One pipeline from "I have a brand" to "I have a launch slate with listings, prompts, a channel plan, and the instruments to know why it worked." Every phase is one of Meg Heckman's four layers run in her non-negotiable order: market before design, design before volume, volume before diagnosis. **A perfect funnel cannot save a poster** — which is why the gates exist and why they fire in this order.

## Usage

```
/merch-os [brand name or _active/<project> path] [optional: niche, constraints, concept count N, channel]
/merch-os resume [run folder]               # picks up at the first incomplete phase
/merch-os [brand] from:[phase]              # force-start at a phase (prior phase outputs must exist)
```

## Pre-Flight

1. Load `skills/meg-heckman-buyer-trigger-os/genius.md` — the 4-layer system, triggers, rubric, anti-patterns. Hot-context rule applies.
2. Create or detect the run folder: `_active/<brand-slug>-merch-os-run-<n>/`. Existing phase files = resume from the first missing one.
3. Write `00-run-config.md`: brand, sources of context, N (default 12), channel (Bonfire | Shopify | drop | undecided), constraints (IP, print method, banned territory).

> **🔒 Grounding rule**: All Heckman revenue figures cited anywhere in run outputs carry UNCONFIRMED labels. Her metric thresholds are calibration defaults, not laws.

---

## Phase 0 — GROUND (Layer 1: who is the person?)

**Collect brand context, then secure the sub-identity.**

1. Pull every available brand source: project folder (`_active/`, `projects/`), per-project CLAUDE.md, memory files, prior runs. If a live store URL exists, browse it read-only (Playwright per `directives/browser-automation-safety.md`) for current product reality — names, collections, price points, copy voice.
2. **Sub-identity check**: does a behavioral-moment person already exist for this brand (prior dossier, avatar manifold, trigger pass)?
   - YES → load it; refresh only if stale or the run targets a different person.
   - NO → run `/meg-sub-identity-map` in full. This is non-optional — sprinting on a broad niche manufactures posters at volume.
3. Write `01-ground.md`: the person (behavioral moments), familiar bank, billboard statement, demand evidence (labeled), constraints inherited from brand context.

> **GATE 0**: A person you can PICTURE, written as behavioral moments — or the run stops here. "Dog mom is broad. Financially ruined by my golden retriever is very specific."

## Phase 1 — CONCEPT (Layer 2: what makes them buy?)

Run `/meg-concept-sprint` with the Phase 0 dossier: N concepts, mirror-only, all eight fields per concept (familiar/twist halves, identity statement, emotion layers, social moment, lead line, evergreen check).

Write `02-concepts.md`.

> **GATE 1**: Zero posters delivered; twist mechanisms varied; ≥N/3 self-deprecating-identity concepts. Thin sets ship strong-only with cuts named — never padded to N.

## Phase 2 — SCORE (the kill/revise/lead verdict)

Run `/meg-trigger-audit` on the full sprint: 10-criterion scorecard, weakest-trigger isolation, one revision directive per REVISE, lead lines per LEAD, portfolio read (evergreen mix, natural pairs for AOV).

Write `03-scorecard.md`.

> **GATE 2**: ≥3 LEAD verdicts to proceed. Fewer → execute the revision directives on the top REVISE candidates ONCE, rescore those only. Still <3 → the sub-identity is probably wrong; loop to Phase 0 with the diagnosis written down (do not brute-force concepts at a person who isn't there).

## Phase 3 — LISTING (make the leads shippable)

For each LEAD (or the test slate of 3):
1. `/meg-listing-copy` — recognition lead → identity → bridge (if twist is niche-opaque) → social moment → logic last. Channel-adapted (Bonfire page vs PDP vs drop email).
2. `/meg-design-handoff` — the trigger-grounded prompt pack ("Still Synced" anatomy: buyer scene first, one graphic system, identity micro-text, niche-specific avoid-list) + composition/typography briefs.

Write `04-listings.md` + `05-prompt-pack.md`.

> **🔒 COST GATE**: Prompt packs are the deliverable. Actual image generation (fantastic-posters / Higgsfield) is cost-gated — runs only on explicit approval, routed per `creative_router.py` pre-flight (people → Higgsfield Soul; stylized → fantastic-posters).

## Phase 4 — LAUNCH (channel plan)

Channel-specific, smallest honest test first ("Find one shirt people actually want, not build a whole brand yet" — the Josh V1 doctrine):

- **Bonfire** (no-store test): batch campaign, ~10 days, ≤3 shirts, Smart Launch off for real scarcity; founder approval gate on joke text, art, price/profit preview, page copy, IP notes, launch posts. (Template: `_active/clients/josh-swing-nerd-shirts-v1/BONFIRE_PUBLISHING_CHECKLIST.md`.)
- **Shopify** (existing store): placement via `/meg-store-stack` — which identity collection the leads join, PDP trust stack, mobile CTA check; email announce to list (the list is pre-paid traffic).
- **Drop**: capsule framing (concept family = pre-built cohesion per `/meg-aov-architect`), scarcity window, announce sequence.

Write `06-launch-plan.md` with the founder approval checklist embedded.

> **GATE 4**: The plan names its smallest honest test, its budget floor, and its 48h read protocol. No "launch everything and hope."

## Phase 5 — DIAGNOSE (Layer 4: instrument before you need it)

- Store live + ads running → `/meg-funnel-doctor` cadence: weekly 6-metric review, fault-isolation order, mockup-swap protocol pre-written.
- Pre-launch → instrumentation setup: which 6 numbers get tracked where, the thresholds (calibration defaults), who reads them weekly, and the pre-committed kill/scale rules so taste can't veto data later. "The market does not care what you love."
- Brand staying in production → `/meg-factory-loop` install: volume targets, test cadence, email rhythm, the repeat commitment.

Write `07-diagnostics.md`.

---

## Finalize (Chain Step 6 — per run)

```bash
python3 execution/chain_runner.py finalize "Merch OS run — [brand]: [n] concepts, [n] leads, listings + prompt pack + launch plan" \
    --expert meg-heckman --skill meg-heckman-buyer-trigger-os --workflow merch-os \
    --type Creative --intent [1-10] --expert-score [1-10] --adversarial [1-10] --sub-agents [measured] \
    --notes "[what worked/didn't] | Factual Grounding: [score] | Verification: [status]"
```

## Phase Map (resume points)

| Phase | File | Gate |
|---|---|---|
| 0 GROUND | 01-ground.md | Behavioral-moment person exists |
| 1 CONCEPT | 02-concepts.md | Mirror-only, varied twists |
| 2 SCORE | 03-scorecard.md | ≥3 LEADs (one revise loop max) |
| 3 LISTING | 04-listings.md, 05-prompt-pack.md | Cost gate on generation |
| 4 LAUNCH | 06-launch-plan.md | Smallest honest test named |
| 5 DIAGNOSE | 07-diagnostics.md | Pre-committed kill/scale rules |

## Anti-Patterns (OS level)

- Running CONCEPT before GROUND ("a person you can picture" is the fuel — without it the sprint is decoration manufacturing).
- Brute-forcing Gate 2 by lowering the bar instead of fixing the person.
- Generating images before scoring concepts (paying to render posters).
- Launching the full set instead of the smallest honest test.
- Skipping DIAGNOSE because the launch "feels good" — the feeling is Layer 2's job; Layer 4 runs on numbers.

## Pairs With

- `/meg-avatar-bridge` → when the brand needs full avatar depth after the run proves the person.
- `/build-bos` → when a merch test graduates into a full Brand OS.
- `/fantastic-posters` (cost-gated) → rendering the prompt pack.
- `writers-room` → refinement pass on listing copy for client-facing polish.
