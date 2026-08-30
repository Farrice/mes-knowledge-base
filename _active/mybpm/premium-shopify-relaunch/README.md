# MyBPM Premium Shopify Relaunch

This package turns the current MyBPM store into a focused premium streetwear staging build: Kith-level editorial restraint, recast through MyBPM's EDM-after-dark identity.

## What is built

- A full Shopify Horizon theme source in `theme/`
- Custom MyBPM hero, manifesto, collection, product-story, proof, and product-notes sections
- A responsive visual preview in `preview/`
- A desktop design board in `preview/design-board.html`
- A portable brand-as-code contract in `DESIGN.md`
- Product and metafield implementation data in `data/`
- Live-store audit, brand direction, capsule gate, launch plan, and QA contract

## Current status

**V2 SHOPIFY STAGING BUILD — UPLOADED, NOT PUBLISHED.** The theme uses a white primary canvas, black structure, controlled acid signals, and restrained mineral texture. The exact reviewed package is installed as the unpublished Shopify theme `MyBPM v2 — White Signal Staging` (`158270324891`). It has not changed the live theme, products, navigation, policies, inventory, domains, or checkout.

The live theme remains `Updated copy of MyBPM Ira 4.3.0` (`133086773403`). Publishing requires Farrice's final approval after the unpublished theme is reviewed on desktop and mobile and the blocking checkout checks pass.

## Theme source provenance

- Upstream: Shopify's official Horizon repository
- Source URL: https://github.com/Shopify/horizon
- Pinned commit: `1c479ca2825f0a2066a935720d6512a659fa257f`
- Commit date: 2026-08-12
- Local additions are prefixed `mybpm-` where practical.

Shopify notes that Horizon's main branch can contain unreleased APIs. For that reason, this package must pass Theme Check and an unpublished-store preview before publication.

## Review order

1. Review the unpublished Shopify preview: `https://mybpm.store/?preview_theme_id=158270324891`.
2. Open `preview/index.html` for the static storefront direction.
3. Open `preview/design-board.html` for the Kith-to-MyBPM translation and page grammar.
4. Read `03-capsule-selection.md`; only the Sublevel tee presently has enough public evidence to lead.
5. Approve or replace the sample-gated hoodie, bucket hat, and Defined tee.
6. Complete `06-qa.md`; publish only after every blocking item passes.
