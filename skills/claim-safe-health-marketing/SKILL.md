---
name: "Claim-Safe Health Marketing"
description: "The claim-substantiation gate for health, wellness, and supplement brand marketing. Classifies claims (disease vs. structure/function vs. qualified vs. puffery), maps claim strength to required evidence tier (FTC's competent-and-reliable-scientific-evidence standard), rewrites flagged copy into compliant-but-converting language, and runs the Meta/TikTok/Amazon platform-specific pass before launch. Built for Path A: claim-safe content for funded health brands."
domain: "regulatory compliance, health/supplement marketing, FTC/FDA/DSHEA claim substantiation, direct-response copywriting for health brands, platform ad policy (Meta/TikTok/Amazon)"
when_to_use: "Any health, wellness, or supplement brand asset that makes an efficacy, ingredient, or outcome claim — ads, landing pages, emails, social posts, product listings, influencer briefs. Route farrice-engine/jw-engine/copy-engine health-brand output through this gate before it ships."
version: "1.0"
format: "diagnostic-and-rewrite-engine"
workflows: 5
tier: "standard"
---

# Claim-Safe Health Marketing

> **The missing substantiation gate.** Every health-brand claim `farrice-engine`, `jw-engine`, and `copy-engine` produce is currently improvised against no expert — this skill is that expert. Built 2026-07-06 as E5 harvest-wave Target #1: grep across 338 skills / 96 agents / 16 domains returned zero hits on `complian|regulat|ftc|fda|dshea|claim-safe` before this build.

**Core Capabilities:**
- **Classify** any claim into the 5-bucket risk taxonomy (disease express / disease implied / structure-function / qualified / puffery) — the deterministic classifier at the heart of the skill
- **Map** claim strength to the FTC's evidence-tier ladder (RCT → clinical → epidemiological → in vitro/animal → anecdotal) and flag when a brand's actual evidence doesn't clear the bar the claim's strength requires
- **Rewrite** flagged copy using compliant-but-converting patterns (mechanism-over-outcome, review-language mining, social-proof-over-guarantee, realistic-expectation framing) — never hedge-and-flatten
- **Gate** any asset pre-launch with disclaimer verification + independent Meta/TikTok/Amazon platform passes (platforms enforce stricter, partly-automated rules on top of FTC/FDA baseline)
- **Generate** claim-safe hooks front-loaded from real selling points (ingredient/mechanism/experience), never from an invented outcome walked back later

**Domain**: Regulatory-compliant marketing for funded health, wellness, and supplement brands — the FTC/FDA/DSHEA/NAD/platform-policy layer that sits underneath every other health-marketing skill in the roster.

**Positioning vs. roster**: `alan-aragon-nutrition` and `andy-galpin-training-intelligence` cover coaching/science-communication for individual athletes — not advertising-compliance. `farrice-engine`/`jw-engine`/`copy-engine` write persuasive copy but carry no claim-substantiation gate. This skill is the missing layer between them: route any health-brand claim through this skill BEFORE it ships through those engines, never as a replacement for them.

---

## Available Workflows

### Tier 1 — Foundation (diagnose → fix → verify)

| # | Workflow | Produces | Use when |
|---|---------|----------|----------|
| 01 | [Claim Audit](workflows/01-claim-audit.md) | Sentence-level claim classification + net-impression + testimonial scoring | Existing copy needs a compliance pass before it ships |
| 02 | [Compliant Rewrite](workflows/02-compliant-rewrite.md) | Side-by-side original/rewrite with GP-07 move named per unit | Flagged copy needs fixing without losing persuasive power |
| 03 | [Claim Substantiation Map](workflows/03-claim-substantiation-map.md) | Claim → required evidence tier → evidence-held gap report | Verifying whether a claim's evidence actually supports its strength |
| 04 | [Pre-Launch Compliance Gate](workflows/04-pre-launch-compliance-gate.md) | Go/No-Go verdict (SHIP/HOLD/BLOCKED) across disclaimer + all platforms | Final sign-off before any asset launches |

### Tier 2 — Practitioner (generation, not just diagnosis)

| # | Workflow | Produces | Use when |
|---|---------|----------|----------|
| 05 | [Claim-Safe Hooks](workflows/05-claim-safe-hooks.md) | 10-15 hooks pre-cleared by construction, labeled with selling-point bucket + GP-07 move | Starting ideation from a blank page — compliance front-loaded, not retrofitted |

---

## Stacking Guide

| Want this | Run | Then run |
|---|---|---|
| **Full pre-launch clearance on drafted copy** | `/claim-audit` | `/compliant-rewrite` (if flagged) → `/pre-launch-compliance-gate` |
| **New health-brand hook/headline set** | `/claim-safe-hooks` | `/compliant-rewrite` if expanding to full copy, then `/pre-launch-compliance-gate` |
| **Confirming a claim is even sayable** | `/claim-substantiation-map` | `/claim-safe-hooks` or `/compliant-rewrite` using the cleared claim strength |
| **`farrice-engine`/`jw-engine`/`copy-engine` health-brand output** | Route generated copy through `/claim-audit` | `/pre-launch-compliance-gate` before publish — never skip for a health/supplement client |
| **Amazon listing specifically** | `/claim-audit` (token-scan focus) | `/pre-launch-compliance-gate` Amazon pass |
| **Influencer/UGC brief** | `/claim-safe-hooks` for the brief's hook options | `/claim-substantiation-map` to confirm creators aren't asked to exceed the brand's evidence |

---

## When NOT to Use This Skill

| Need | Route to |
|---|---|
| Coaching business / individual athlete programming | `alan-aragon-nutrition`, `andy-galpin-training-intelligence`, `strength-conditioning` |
| Generic DR persuasion with no health/efficacy claim | `jw-engine`, `copy-engine` (no gate needed if there's no claim to substantiate) |
| Non-U.S. regulatory regimes (EU health claims reg, Health Canada NHP) | Out of scope — flag explicitly, do not apply U.S. rules cross-jurisdiction |
| Brand strategy / positioning for a funded health brand (not claim-level) | Nearest is `ross-mckay-premium-at-scale` (generic CPG) — this is a capability gap the E5 roadmap flags separately (Target #2, not this skill) |
| Turning a scientific study into accurate content (evidence translation, not claim compliance) | Gap flagged separately as E5 Target #3 — not yet built; until it exists, this skill's substantiation-ladder logic (GP-02) is the interim reference |

---

## The 9 Genius Patterns

See [genius.md](genius.md) for full context, sources, and the complete anti-pattern list. Quick reference:

| # | Pattern | Operating test |
|---|---|---|
| GP-01 | Claim-Risk Taxonomy | Every claim sorts into 1 of 5 buckets; Bucket 1/2 = hard stop |
| GP-02 | Substantiation Ladder | Claim strength must not exceed evidence tier actually held; ingredient evidence ≠ product evidence (NAD rule) |
| GP-03 | Net Impression | Whole-page skim-read test, not sentence-by-sentence |
| GP-04 | Qualified-Claims Escape Hatch | Only FDA's pre-authorized list + FDA's own disclaimer language — never self-authored |
| GP-05 | Testimonials Reflect Typical Results | "Results not typical" micro-print no longer cures a deceptive testimonial (2023 rule) |
| GP-06 | Platform Rules Are a Second, Stricter Layer | Meta/TikTok/Amazon each add rules beyond FTC/FDA baseline |
| GP-07 | Compliant-But-Converting Rewrite Patterns | Mechanism-over-outcome, review-mining, social-proof-over-guarantee, realistic-expectation framing |
| GP-08 | Two-Experts Test | Would a regulatory attorney AND a DR copywriter both sign off unchanged? |
| GP-09 | FTC Gut Check | 7 weight-loss claim patterns are auto-fail regardless of substantiation attempt |

---

## Quality Rubric (8 criteria, veto on 2)

A claim-safe asset earns ≥8/10 on each of 8 criteria (see [genius.md](genius.md#quality-rubric-8-criteria-810-ship-grade-composite-80) for full anchors). **Veto rule**: criterion 1 (claim classification) or 5 (disclaimer present/placed) below 8 caps the whole audit at FAIL regardless of composite — these are the two dimensions actual FTC/FDA/platform enforcement gates on.

---

## Reference Files

| File | Purpose |
|---|---|
| [genius.md](genius.md) | Unified genius context — all 9 patterns, anti-patterns, exemplars, rubric, source caveats |
| [references/source-ledger.md](references/source-ledger.md) | Timestamp→signal→translation for every regulatory/practitioner source, plus what was searched and yielded nothing |
| [references/red-flag-word-bank.md](references/red-flag-word-bank.md) | Full banned-term → compliant-swap tables, organized by risk category |
| [references/platform-rules.md](references/platform-rules.md) | Meta / TikTok / Amazon specific rules beyond the FTC/FDA baseline |

---

## Quick Reference

- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Start an audit here**: `/claim-audit` (existing copy) or `/claim-safe-hooks` (blank page)
- **Final gate before anything ships**: `/pre-launch-compliance-gate` — non-negotiable for Path A client work
- **Recognition test**: would a supplement regulatory attorney AND a direct-response copywriter both sign off on this unchanged? (genius.md GP-08)

---

## Source Caveats

This is a regulatory-knowledge extraction, not a person-voice extraction — there is no single expert whose cadence is being captured, so the embodiment-standard blind-pass is adapted: Tier-1 outputs are compared against real compliant ad-copy patterns (Ballard/Dougherty published examples) and real FTC/NAD enforcement language, not against one expert's published prose. Full caveats, confidence labels (VERIFIED/LIKELY/UNCONFIRMED), and what was searched-but-yielded-nothing are in [genius.md](genius.md#source-caveats) and [references/source-ledger.md](references/source-ledger.md). This skill covers U.S. FTC/FDA/DSHEA + Meta/TikTok/Amazon platform rules only — international regimes are explicitly out of scope.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

5 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Claim Audit — [asset name]** — `skills/claim-safe-health-marketing/references/prompts-v2/claim-audit.md`
- **Claim-Safe Hooks — [brand/product/category]** — `skills/claim-safe-health-marketing/references/prompts-v2/claim-safe-hooks.md`
- **Substantiation Map — [asset/brand/claim set]** — `skills/claim-safe-health-marketing/references/prompts-v2/claim-substantiation-map.md`
- **Compliant Rewrite — [asset name]** — `skills/claim-safe-health-marketing/references/prompts-v2/compliant-rewrite.md`
- **Pre-Launch Compliance Gate — [asset name] — [target platform(s)]** — `skills/claim-safe-health-marketing/references/prompts-v2/pre-launch-compliance-gate.md`

<!-- END:execution-prompts -->
