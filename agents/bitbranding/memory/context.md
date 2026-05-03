# BitBranding (Christian Pinyon) — Agent Memory

## Activation
- **First activated**: 2026-05-03
- **Source extraction**: Single BitBranding YouTube tutorial (Represent collection-page rebuild on Horizon)
- **Activation count**: 1

## Direct Deployment Context

**mybpm.store** — Farrice's EDM streetwear brand. ~30 SKUs. Currently on Shopify (theme TBD — verify Horizon vs. other before running workflows). Direct fit for all 4 workflows.

When invoked for mybpm-related work, default assumptions:
- EDM streetwear positioning (festival regulars, irreverent, community-coded)
- ~30 SKUs (variant siblings paid app NOT worth it at this scale)
- Free-tier or one-app-budget posture
- Mobile-first (festival audience checks phones, not desktops)

## Known Coverage Gaps (Honest)

This agent only knows what was in the single source video. Cannot reliably advise on:
- Product page optimization
- Cart / checkout flows
- Homepage / navigation
- Email / SMS / post-purchase
- Non-Horizon themes (Dawn, Broadcast, paid themes — generalize with caveats)
- Non-clothing categories

If a request hits one of these, flag it openly. Do not fabricate.

## Theme Lever Knowledge (As of Source — Early 2026)

Verified Horizon levers from source:
- Section: Collection page → Collection heading → Image block → Dynamic source binding
- Theme settings → Header → Collection page transparent background
- Section: Product grid → Horizontal gap (mobile + desktop)
- Theme settings → Product cards → Image aspect ratio (Portrait recommended for clothing)
- Theme settings → Product cards → Show second image on hover
- Theme settings → Product cards → Quick add (Desktop + Mobile)
- Theme settings → Product cards → Variant display (Swatches vs. Text labels)
- Section: + Add section → Rich text → Connect dynamic source → meta-field
- Section: + Add section → Collection list (carousel)
- Filters: Direction Horizontal/Vertical, padding, text labels for swatches

Sidekick AI capability map:
- ✅ Visual blocks, headlines, simple text components, layout adjustments
- ❌ Filter logic, recently-viewed sections, functional state changes
- ❌ Description truncation with read-more (failed in source video)

⚠️ Theme features may have updated since source. Verify before promising specific levers — if a setting moved, check the parent section first (hierarchical debugging).

## Stacking Activations

Track which expert pairings have been deployed:
- [ ] BitBranding × Oren (positioning → execution)
- [ ] BitBranding × Luke Iha (copy → card placement)
- [ ] BitBranding × Lara Acosta (LinkedIn → DTC traffic)
- [ ] BitBranding × fantastic-posters (hero generation → dynamic source bind)

## Performance Log Entries

(Updated automatically by `chain_runner.py finalize`)

| Date | Workflow | Brand | Quality Score | Notes |
|---|---|---|---|---|
| 2026-05-03 | extract | (extraction itself) | TBD | Initial extraction — Standard tier, 4 workflows, gate-first protocol applied |
