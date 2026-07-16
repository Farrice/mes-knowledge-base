# Oren John Arsenal Map — Pre-Build Check for Identity Brand OS

Purpose: confirm what already exists before building a new "Identity Brand OS" extraction, so it EXTENDS the arsenal instead of rebuilding it.

## 1. Oren Asset Inventory

7 skill directories, 1 agent, ~39 wired `/oren-*` slash commands (plus additional workflow files nested in skill folders without top-level wrappers). No `routing: long-tail` or `status: archived` flags on any of the 7 SKILL.md files — all are live/default-routed.

| Asset | Covers | Status |
|---|---|---|
| `skills/oren-brand-archetypes` (v2.0, 15 wf) | FRONT DOOR. Resource-reality audit → 5 archetypes (Oracle/Performer/World Builder/Catalyst/Helper) → content roadmap → revenue bridge → pitch deck | Live, default-routed |
| `skills/oren-content-team-architecture` (v1.1, 15 wf) | Pods, hiring specs, operating cadence, signature series, creator networks, founder content identity, brand-as-media-company transformation, paid/organic bridge, scaling | Live |
| `skills/oren-luxury-psychology` (v2.0, 3 wf) | Insider codes, connoisseurship ladders, premium positioning vs. luxury incumbents, aesthetic world-building | Live |
| `skills/oren-one-person-ai-marketer` (v1.0, 12 wf, tier: system) | ACTIVATION layer. Weekly time-block OS, brand-voice Project builder, anti-slop classifier, MESSAGES cycle, INFO-RELEASE/AEO, referral engine, virality audit, influencer ops, performance block, "Claude-Operator Legend" positioning | Live |
| `skills/oren-operational-systems` (v2.0, 3 wf) | Reference-repo architecture, ideas→calendar pipeline, capture-organize-deploy loop, weekly stakeholder updates, team trackers, process docs | Live |
| `skills/oren-repositioning` (v2.0, 3 wf) | Category/aesthetic-code audit, personality repositioning, vision extension into "worlds," cultural-authenticity scaling | Live |
| `skills/oren-taste-development` (v2.0, 5 wf, 2 backup variant files) | CEV (Composition/Effectivity/Vibes) critique framework, curriculum design, taste-as-competitive-advantage | Live |
| `agents/oren-taste-development/AGENT.md` | Single agent persona spanning taste + luxury + repositioning + ops + AI-marketing (NOT brand-archetypes or content-team-architecture explicitly) | Live |

Workflow counts by SKILL.md frontmatter total 56 declared; 39 have top-level `/oren-*` command wrappers in `.agent/workflows/`. The rest resolve through skill-internal workflow paths (e.g., `oren-brand-archetypes` workflows are invoked via the front-door diagnostic, not individually wrapped).

## 2. Memory / Recall Findings

**Memory facade** (`memory_facade.py "Oren John identity marketing brand OS extraction" --top 10`): sources queried were sovereign(10)/automem(10)/wiki(10)/agents(1)/episodic(10)/solutions(3)/prompts(10) — no skipped stores reported. Results were weak signal for this specific query: top hits were generic craft cards (Orlean/Connelly "telling detail," economy-not-minimalism) and unrelated session notes (COS brief verdict, 30-day money sprint, family context). **No existing Oren-specific solution card or prior "Identity Brand OS" planning artifact surfaced** — this appears to be a genuinely new build, not a re-solve.

**Recall search** (3 queries, 19+30 cards) surfaced real, not-yet-extracted Oren John source material:
- **AI Clone Architecture Builder** — "Oren John Crown Jewel Prompt 3 of 7 | MES 3.0 Practitioner Architecture" (card `71602c2a`, captured 2025-12-27). Builds AI clones (identity core, expertise map, reasoning framework, voice calibration) from content archives so outputs are "eerily accurate" to the source person — a full system-prompt clone, deeper than the existing `brand-voice-machine-builder` workflow (which produces a lighter "Project instructions" config). Only prompt 3 of 7 is in Recall; the other 6 Crown Jewels for this specific set were not found — **partial source, not a complete prior extraction**.
- **"Content TAM"** concept (Justin Welsh interview, card `8b97a8a7`) — Oren's platform-agnostic content distribution logic (one idea → cross-platform TAM capture). Adjacent to `oren-paid-organic-bridge` and `oren-scale-media-machine` but not named/extracted as its own pattern.
- **Product-vs-Brand signature series** and **"Hyper" newsletter co-brand** concept (card `e14d017a`, `1ddbd1c3`) — already substantially covered by `oren-signature-series` and `oren-content-flywheel`.
- **Identity vs. expression sequencing** ("do identity work before expression work" — general branding-podcast source, not confirmed Oren) and **"people buy identity/identification"** (Myron/Oren podcast, card `8252722a`) — directly relevant to the proposed OS's core thesis; not yet systematized anywhere in the Oren stack.

No pre-existing "Identity Brand OS" planning doc, brief, or card was found in sovereign memory, episodic history, or Recall.

## 3. Prior Oren Sources Already Extracted

- `extractions/oren/` — 3 reports: `extraction-report.md` (Psychology of Luxury Branding, ~25min/4,674 words → became `oren-luxury-psychology`), `extraction-report-repositioning.md` (Repositioning & Creative Direction, ~18min/3,809 words → became `oren-repositioning`), `oren-systems-extraction-report.md` (11 Ways to Get Your Life Together, ~25min → became `oren-operational-systems`), plus `transcript.txt`.
- `extractions/oren-1person-ai-marketing/` — `mastery-extraction.md` (How to Be a 1-Person Marketing Machine, ~25min/6,051 words, 28 REAL patterns → became `oren-one-person-ai-marketer`), plus `transcript.txt`.
- `extractions/oren-john-identity-marketing/` — **empty, target directory for this build**, confirmed created but contains no prior work.
- Not yet traced to a source-extraction folder: `oren-brand-archetypes` and `oren-content-team-architecture` (likely extracted directly to skill form, or under a differently-named extraction folder not matched by an `oren*` glob — worth a follow-up `grep -r "archetype" extractions/` pass if precise provenance is needed later, not done here to stay in scope).

## 4. Adjacent-Asset Compose List (identity-marketing landscape)

| Skill | Covers |
|---|---|
| `skills/michael-bernoff-identity-engineering` | Identity engineering + communication mastery for transforming a PROSPECT's self-concept mid-conversation (sales/persuasion frame, not brand-building) |
| `skills/jeremy-miner-identity-persuasion` | Identity-based persuasion, frame engineering, NPQ conversation design — sales-psychology frame, 28 patterns |
| `skills/benjamin-hardy-identity` | Future-self psychology, 10x-vs-2x goal architecture — personal transformation, not brand/market-facing |
| `.agent/workflows/avatar-machine.md` (Luke Iha stack) | Cold-start → converting copy via grounded Avatar Manifold — ICP research, not brand identity |
| `.agent/workflows/brand-in-a-box.md` (Jack Roberts design mastery) | Productized DESIGN.md + website + presentation + social templates in 48 hrs — visual system packaging |
| `.agent/workflows/zero-to-brand.md` (Caleb Ralston personal-brand) | Zero-to-first-30-days personal brand launch pipeline |
| `.agent/workflows/build-bos.md` | Universal 6-layer Brand Operating System builder (43 docs) — foundation/visual/briefs/marketing/AI-handoff/ops layers |
| `.agent/workflows/meg-sub-identity-map.md` (Meg Heckman buyer-trigger-os) | Finds the ignored sub-identity inside a saturated niche — positioning wedge, not full identity system |
| `.agent/workflows/lynch-identity-campaign.md` + `lynch-identity-posture.md` | Campaign-level identity-transformation creative (name the identity in one word) validated against Dai Media consumer-posture psychology |

None of these own "identity brand marketing from zero → cult following → 1,000 true fans → scale" as a single through-line. They each own one slice (persuasion-frame identity, personal-brand launch, visual-system packaging, campaign-level identity naming).

## 5. Gap Analysis

What "identity brand marketing from zero → cult following → 1,000 true fans → scale any creator/founder" needs, mapped against what's owned:

**Already owned — extend, don't rebuild:**
- Archetype selection + content roadmap → `oren-brand-archetypes` (front door)
- Team/pod scaling once traction exists → `oren-content-team-architecture`
- Premium positioning once identity has value → `oren-luxury-psychology`
- Solo-operator execution engine (the "how" once strategy is set) → `oren-one-person-ai-marketer`
- Personality/brand repositioning from generic to differentiated → `oren-repositioning`
- Judgment/quality-control layer → `oren-taste-development`
- Ops infrastructure once producing → `oren-operational-systems`
- Sales-conversation identity shifting → `michael-bernoff-identity-engineering`, `jeremy-miner-identity-persuasion`
- Full 6-layer brand doc system once identity is set → `build-bos`
- Niche-wedge finding inside saturation → `meg-sub-identity-map`
- Campaign-level identity-word naming → `lynch-identity-campaign`

**Net-new — no existing asset covers these:**
1. **Zero-to-first-audience identity formation mechanics** — none of the 7 Oren skills, nor `zero-to-brand`, actually answers "who am I as a public identity, before any archetype/content decision." `oren-brand-archetypes` presupposes the archetype choice is the starting line; `zero-to-brand` (Caleb Ralston) is closer but is a different expert's voice/frame, not Oren's. This is the true zero-point gap.
2. **Cult-following / true-fans mechanics as a named system** — no Oren asset systematizes 1,000-true-fans density (depth over reach, parasocial intensity, tribal-belonging engineering) as its own workflow. `oren-repositioning`'s "vision extension into worlds" and the Recall-sourced "identity = what people buy" thread are adjacent but not assembled into a fandom-density protocol.
3. **AI-clone / identity-capture depth layer** — the Recall-sourced Crown Jewel #3 (AI Clone Architecture Builder) is deeper than the existing `brand-voice-machine-builder` (Pattern 13) and was never fully extracted (only 1 of 7 prompts in Recall). Building the new OS should either (a) source-hunt the missing 6 Crown Jewels before building this piece, or (b) explicitly scope identity-capture at the existing lighter tier and flag the deeper version as a future extraction, not silently reinvent it.
4. **Cross-domain "scale any creator/founder" generalization layer** — every existing Oren asset is calibrated to Oren's own case (creative director/brand consultant, product-vs-brand series, Kajabi ecosystem). A generalized intake/diagnostic that maps ANY founder's raw material (not just creative-director-shaped ones) to the archetype/content/team stack doesn't exist yet — closest analog is the resource-reality audit inside `oren-brand-archetypes`, which is brand-level, not identity-level.

**Recommendation**: the new Identity Brand OS should be a thin orchestration + the zero-point/cult-following/generalization gaps above, routing everything else (archetype selection, team scaling, positioning, ops, taste QC, solo execution) to the existing 7 skills rather than re-authoring them.
