---
name: bitbranding-fashion-shopify
description: Christian Pinyon (BitBranding) — Fashion DTC Shopify execution. Audit/rebuild clothing-brand collection pages, product cards, and evidence-led product-detail pages on Horizon. Draft-theme-safe, free-tier-fluent, gap-honest, mobile-first.
version: "3.0"
format: completion-engine
workflows: 7
---

# BitBranding — Fashion Shopify Execution

**Expert**: Christian Pinyon, co-founder of BitBranding (Shopify agency for clothing brands, Allen TX)
**Domain**: Fashion e-commerce / Shopify theme execution / DTC clothing-brand conversion
**Roster slot**: First Shopify/fashion-DTC expert in the system. Direct fit for mybpm.store and any future apparel brand work.

---

## Core Thesis

> "Almost everything premium streetwear brands are doing can be rebuilt on a standard Shopify theme for free. No custom code, no expensive apps."

Christian doesn't sell custom dev. He sells **taste + tooling literacy** — the ability to close 80% of the visual gap between a $0 store and a $5K/mo Shopify Plus build by knowing exactly which theme levers to pull. The remaining 20% he names honestly and routes to merchandising alternatives instead of faking capability.

---

## Workflow Table

| # | Workflow | Slash command | Produces | Trigger |
|---|---|---|---|---|
| 01 | Premium-Reference Collection Audit | `/bb-audit` | 3-strategy breakdown (layout / product card / content) of any clothing brand's collection page vs. a premium reference. Free-tier triage. | "Audit my collection page against Represent" |
| 02 | Free-Stack Horizon Rebuild Plan | `/bb-rebuild` | Lever-by-lever execution plan for free Horizon. Every theme setting named. Honest gaps with paid alternatives + free fallbacks. | "Rebuild my store like Represent on free Horizon" |
| 03 | Fashion Product Card Optimizer | `/bb-product-card` | Configured optimized product card using the 5-component system. One-fix focus, not blanket optimization. | "Optimize my product cards for conversion" |
| 04 | Collection Content & SEO Stack | `/bb-collection-content` | Hero direction + truncated top description + rich-text bottom description with interlinking + below-grid merchandising. | "Build the SEO + storytelling layer for my collection page" |
| 05 | Fashion PDP Evidence Blueprint | `/bb-pdp-blueprint` | Truth-labeled dossier, missing-facts questions, objection ledger, and mobile-first PDP architecture. No store mutation. | "Blueprint this apparel product page from customer evidence" |
| 06 | Draft-Theme PDP Build Loop | `/bb-pdp-build-loop` | Connector-ready or explicitly authorized draft-theme delta, rendered inspection, defect ledger, state-aware repair, QA, and rollback. | "Turn the approved PDP blueprint into a safe Shopify draft" |
| 07 | Fashion PDP Rebuild System | `/bb-pdp-rebuild` | Conducted blueprint → approval → draft build → review → experiment handoff with all permission boundaries intact. | "Rebuild this Shopify fashion PDP with AI" |

---

## Quick Reference

### When to deploy this skill
- Brand on Shopify (especially Horizon free theme)
- Clothing / apparel / accessories DTC
- Wants premium aesthetic without paid theme/apps budget
- Wants a source-grounded PDP blueprint or an AI-assisted draft-theme rebuild
- Specifically: mybpm.store work

### When NOT to deploy
- Non-Shopify platforms (Webflow, Magento, Woo) — lever paths don't transfer
- Non-clothing categories (food, electronics, services) — Christian's lane is fashion
- Already on Shopify Plus with custom theme — under-leverages his free-tier specialty
- Wants brand strategy or positioning — route to **Oren** instead, then return for execution

### Stacking Guide

| Pair | Compound output | Sequence |
|---|---|---|
| BitBranding × **Oren** | Brand positioning → page execution | Oren first (positioning), BitBranding second (execution) |
| BitBranding × **Luke Iha** | Product copy → card placement | Luke first (copy), BitBranding second (placement in 5-component system) |
| BitBranding × **Lara Acosta** | LinkedIn brand intro → DTC traffic landing | Lara drives traffic, BitBranding converts it |
| BitBranding × **fantastic-posters** | Premium hero/lookbook generation → collection hero | Posters generates, BitBranding directs + binds via dynamic source |
| BitBranding × **Nick Saraev** | Theme automation / inventory sync agents | Nick builds the automation, BitBranding informs Shopify-specific lever knowledge |

### mybpm.store Deployment Sequence

For Farrice's direct mybpm.store work, recommended order:
1. `/bb-audit` against a chosen premium reference (Represent, Aimé Leon Dore, etc.) — produces gap list
2. `/bb-rebuild` based on audit — produces execution plan
3. `/bb-product-card` for the highest-leverage card fix
4. `/bb-collection-content` per active collection (Spring 26, Hoodies, etc.)
5. `/bb-pdp-blueprint` for the priority product using real questions, returns, fit data, and voice evidence
6. Approve the blueprint, then `/bb-pdp-build-loop` for a duplicated draft theme only
7. **Stack only where evidence is missing**: `/posters` for an approved media shot list; Oren for unresolved positioning; Luke for bounded copy support

Total time: ~3-4 hours across all 4 workflows for a single store.

---

## Genius Source

Two source-grounded BitBranding tutorial extractions: the original Represent collection-page rebuild on Horizon and a 2026-08-27 screen-share of an evidence-led apparel PDP rebuild with Claude and a duplicated Shopify draft theme. The expansion adds 15 PDP patterns, ten reviewed visual frames, three born-v2 workflows, and a permission-aware build loop.

**Source limitation**: Two tutorials cover collection-page and product-page execution. Christian's full methodology likely spans more sources. Cart/checkout, homepage, navigation, and post-purchase remain separate gaps.

**Honest scope**: The PDP workflow can prepare a connector-ready packet or operate on an explicitly authorized duplicated draft theme. It does not authorize live-theme changes or publication, and it does not claim conversion uplift without an experiment.

---

## File Map

```
skills/bitbranding-fashion-shopify/
├── SKILL.md                                              (this file)
├── genius.md                                             (full genius context)
└── workflows/
    ├── 01-premium-reference-collection-audit.md
    ├── 02-free-stack-horizon-rebuild-plan.md
    ├── 03-fashion-product-card-optimizer.md
    ├── 04-collection-content-seo-stack.md
    ├── 05-fashion-pdp-blueprint.md
    ├── 06-claude-pdp-build-loop.md
    └── 07-fashion-pdp-rebuild-system.md
```

```
agents/bitbranding/
├── AGENT.md
└── memory/
    └── context.md
```

```
.agent/workflows/
├── bb-audit.md
├── bb-rebuild.md
├── bb-product-card.md
├── bb-collection-content.md
├── bb-pdp-blueprint.md
├── bb-pdp-build-loop.md
└── bb-pdp-rebuild.md
```

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

7 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Draft-Theme PDP Build: [Product]** — `skills/bitbranding-fashion-shopify/references/prompts-v2/claude-pdp-build-loop.md`
- **Collection Content Stack: [Collection name]** — `skills/bitbranding-fashion-shopify/references/prompts-v2/collection-content-seo-stack.md`
- **[Brand] Collection Page Audit** — `skills/bitbranding-fashion-shopify/references/prompts-v2/collection-page-audit.md`
- **PDP Blueprint: [Product]** — `skills/bitbranding-fashion-shopify/references/prompts-v2/fashion-pdp-blueprint.md`
- **Fashion PDP Rebuild Run: [Product]** — `skills/bitbranding-fashion-shopify/references/prompts-v2/fashion-pdp-rebuild-system.md`
- **Free-Stack Rebuild Plan: [Brand]** — `skills/bitbranding-fashion-shopify/references/prompts-v2/horizon-rebuild-plan.md`
- **Product Card Optimization: [Brand]** — `skills/bitbranding-fashion-shopify/references/prompts-v2/product-card-optimizer.md`

<!-- END:execution-prompts -->
