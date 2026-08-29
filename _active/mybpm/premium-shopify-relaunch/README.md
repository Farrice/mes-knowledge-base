# MyBPM Premium Shopify Relaunch

This package turns the current MyBPM store into a focused premium streetwear staging build: Kith-level editorial restraint, recast through MyBPM's EDM-after-dark identity.

## What is built

- A full Shopify Horizon theme source in `theme/`
- Custom MyBPM hero, manifesto, collection, product-story, proof, and product-notes sections
- A responsive visual preview in `preview/`
- Product and metafield implementation data in `data/`
- Live-store audit, brand direction, capsule gate, launch plan, and QA contract

## Current status

**LOCAL STAGING BUILD — NOT PUBLISHED.** The theme is ready for local validation and Shopify upload. It has not changed the live store, products, navigation, policies, inventory, domains, or checkout.

Publishing requires authenticated Shopify store access and Farrice's final approval after the unpublished theme is reviewed on desktop and mobile.

## Theme source provenance

- Upstream: Shopify's official Horizon repository
- Source URL: https://github.com/Shopify/horizon
- Pinned commit: `1c479ca2825f0a2066a935720d6512a659fa257f`
- Commit date: 2026-08-12
- Local additions are prefixed `mybpm-` where practical.

Shopify notes that Horizon's main branch can contain unreleased APIs. For that reason, this package must pass Theme Check and an unpublished-store preview before publication.

## Review order

1. Open `preview/index.html` for the visual direction.
2. Read `03-capsule-selection.md`; only the Sublevel tee presently has enough public evidence to lead.
3. Approve or replace the sample-gated hoodie, bucket hat, and Defined tee.
4. Connect the Shopify store and upload `theme/` as an unpublished theme.
5. Complete `06-qa.md`; publish only after every blocking item passes.
