---
date: 2026-07-13
session: operator-guide backfill (guides fleet)
tier: operator-guide
status: enriched
---

# Dara Static Engine — What We Built and How to Use It

> On 2026-07-07 `dara-denney-meta-ads` expanded from 7 video/UGC workflows to **17** by forging Dara Denney's static-ads masterclass ("How I Make AI Static Ads", watched frame-by-frame). It is now the canonical static-ad craft engine — strategy, design, copy, AI production, and a sellable sprint — render-wired to real repo tools. Skill spine: `skills/dara-denney-meta-ads/SKILL.md` + `genius.md`; frame-grounded exemplars: `skills/dara-denney-meta-ads/references/static-ad-exemplars.md`.

## ⚡ If you only read 10 lines

- Static front door: `/dara-static-engine` — full 3-Layer build (Strategy → Design → Copy) → one production-ready static-ad spec.
- Renderer: `/dara-static-production` — locked spec → real image files in `deliverables/` + variation/QA sheet.
- Productized offer: `/dara-static-ad-sprint` — one brief → 5–10 research-grounded concepts, produced assets, QA report, delivery package.
- Gate before spend: `/dara-comprehension-audit` — the 1-second test, decisive KEEP / FIX / KILL.
- Doctrine: one ad, ONE job. Headline does the targeting; focal point sits on the messaging ~9/10 times; clarity beats creativity.
- 7 static formats, 8 copy mechanics, 3 production levels — lo-fi creator is the biggest current gap AND her needle-mover.
- **Never invent exemplars or headlines** — name every static against `references/static-ad-exemplars.md` (watched, verbatim).
- Hard Vetoes in `genius.md` are pass/fail: em dash, buried product, generalized-away specificity, competing headline/CTA, clean-vs-visceral, self-score inflation.
- Render wiring is tool-agnostic and cost-gate aware; the render step is an optional OFFER, never a forced pipeline step.
- Have a winner in one vessel? `/dara-format-swap` reuses the research into the other (static ↔ video).

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/dara-static-engine` | Full 3-Layer static spec (headline, hierarchy, copy, format, ratio, production level) | Building a static from a brand + persona — the front door |
| `/dara-static-format` | Ranked brief: 2–3 of the 7 archetypes × production level | Layer-1 strategy set; you need the vessel |
| `/dara-static-copy` | Headline + supporting-copy variants tagged by mechanic, incl. review-CSV golden-nugget mine | Strategy + design locked |
| `/dara-comprehension-audit` | KEEP / FIX / KILL verdict + exact fixes | Before any static ships or scales |
| `/dara-educational-infographic` | Infographic spec + render handoff (Sweetgreen play) | Unaware/TOF persona needs teaching |
| `/dara-transformation-static` | Before/after spec + lo-fi creator direction | Problem/solution-aware buyer who only needs proof |
| `/dara-comparison-callout` | ✓/✗ grid or benefits-callout spec | Solution-aware buyer comparing alternatives |
| `/dara-static-production` | Rendered image files + variation/QA sheet | A locked spec exists and you want pixels |
| `/dara-format-swap` | Cross-format brief, static ↔ video, one research pass | A proven winner should try the other vessel |
| `/dara-static-ad-sprint` | 5–10 concepts, locked copy + design, produced assets, testing roadmap | Someone is paying for a batch |

(Video side, 01–07, still lives here too: `/dara-format-selection`, `/dara-david-goliath`, `/dara-yapper-script`, `/dara-objection-engine`, `/dara-test-plan`, `/dara-winning-hooks`, `/dara-founder-ad`. All 17 are in the slash menu and runnable via `.agent/workflows/dara-*`.)

## The mental model

1. **Format × messaging are independent test axes.** Dara's core discipline: engineer, test, and grade each on its own. Most "our ads stopped working" diagnoses are a format-messaging mismatch, not a creative-quality problem. This is also why `/dara-format-swap` works — the message architecture (goal, persona objection, awareness level, proof mechanism) is format-agnostic; only the vessel changes.

2. **Each layer gates the next.** Layer 1 Strategy (ONE goal, a SPECIFIC persona with stage + objection, format, matched awareness level) must be buttoned up before a line of copy. Layer 2 Design is hierarchy plus the 1-second comprehension test — if a stranger can't tell what you're selling in one second, kill it. Layer 3 Copy is the most important layer: the 8 mechanics (be specific, call out the audience, lean into taboo, tap a primal desire, curiosity loop, negative marketing, borrow from customers, show the transformation).

3. **Exemplars are load-bearing.** Every one of the 7 archetypes is anchored to a watched, verbatim exemplar (Sweetgreen "The Economics of $15 Salads", GRO's ✓/✗ grid, totallee "iPhone Cases Are Weird.", the dandruff before/after…). A converting static is one you can name against these seven patterns. Inventing exemplars is the transcript-only-extraction failure all over again.

## /dara-static-engine — the front door

**What it is.** The full 3-Layer build. Loads the genius spine + exemplars, runs Strategy → Design → Copy with each layer gating the next, and outputs one production-ready spec.

**When to reach for it.** Building a static from a brand + persona; diagnosing why current statics underperform.

**When NOT to.** You already know the play → jump straight to the format builder (12/13/14). You only need the vessel ranked → `/dara-static-format` is cheaper. You need many concepts under a paid scope → `/dara-static-ad-sprint` wraps this whole system.

**Quality gate.** Every run ends with the genius.md Static rubric + the 1-second recognition test — and the Hard Vetoes block is pass/fail, inherited by all static workflows.

## /dara-static-production — the renderer

**What it is.** Takes a locked spec (from 08 / 12 / 13 / 14 / 17) and produces real files: brand-brain → research-first gap analysis → 3-variation batch → edit-to-refine loop. Dara's AI pipeline, tool-agnostic (she demoed on SuperScale — sponsor, deliberately NOT wired; method only).

**Render wiring (real repo tools — never cite one not on this list):**

```bash
python3 execution/generate_image.py "<prompt>" --aspect <1:1|4:5|9:16>   # Nano Banana 2; --edit <img.png> "<edit>" is the refine loop
python3 execution/generate_design.py --type <apparel|logo|...> --aspect <ratio> "<concept/brief>"   # art-direction → render
python3 execution/creative_router.py route --task "<task>" [--json]     # picks the service + prints the cost-gate pre-flight
```

Plus: `fantastic-posters` (Fal GPT-Image-2, **cost-gated**) for stylized/hi-fi; **Higgsfield Soul** via the router for people/faces (lo-fi creator, founder, transformation-with-a-person). The router prints the exact `cost_gate.py` pre-flight — surface it, never bypass. Per no-forced-wiring, concept workflows offer the render as an optional handoff.

## /dara-static-ad-sprint — the offer

**What it is.** The whole system as a sellable scope: 5–10 production-ready concepts with locked copy + design, produced assets, QA report, testing roadmap, delivery package.

**When to reach for it.** Someone is paying for a batch, not a single hero asset. Live deploy target: MyBPM.

**When NOT to.** One hero asset → run 08 → 11 → 15 directly; the sprint's packaging overhead isn't earned.

## Composition table

| Stacks with | What it adds | Earns its cost when |
|---|---|---|
| `/awareness-ladder` | Schwartz awareness level ↔ the 7 formats map directly | Persona's stage is fuzzy |
| `/dara-winning-hooks` | 4-layer hook anatomy for the video side of a swap | Running `/dara-format-swap` toward video |
| `/dara-test-plan` | 30-day format × messaging × persona matrix | $5K+ budget, 3+ weeks runway |
| `/hook-forge`, `/proof-stacked-ad-builder` | Hook formulas; proof stacking for D&G science beats | Video concepts need depth |
| Meg Heckman buyer-trigger OS | Trigger-level persona work upstream of Layer 1 | Cold-traffic personas built from scratch |

## Honest edges

- **Taste calibration is verbatim but narrow**: she rejects em dashes, misspellings, "too much going on", review-collage statics; she accepts visceral (Dr. Squatch "Blame your D.O., not your shirts") and advised leaning *more* visceral, not clean-and-safe. That's one expert's ledger — Farrice's felt verdict still wins.
- The blind-test MyBPM cold-TOF Headliner static scored PASS 7.5 and is **pending Farrice's A-tier judgment** (open question: does the headline need more visceral push?).
- Before/afters carry category restrictions (cosmetic/weight-loss) — claim only what the frame shows.
- Image generation can trip the cost gate mid-render; that's the system working, not a bug.
