# Pricing rationale

All receipts from `deliverables/research-briefs/income-master-2026-08/income-master-2026-08-brief.md` (red-team revised figures, retrieved 2026-08-22). The source brief remains pending merge from its research lane; the price bands stay `UNTESTED` until that durable path resolves in main.

## Practitioner: $49/mo

Positioned inside the brief's verified $39-59 practitioner band. The Social Broker sells a $47/mo real-estate content-pack membership with a live checkout and named testimonials; Social Realtr and My Social Boutique sit at $99/mo. **[VERIFIED]** Source: https://thesocialbroker.com/membership (primary page loaded during wargame, red-team re-verified). $49 sits $2 above the category incumbent, justified by the listing launch system no competitor pack includes, while staying under the psychological $50 line and far under the $99 tier.

## White-Label Agency: $149/mo

Positioned inside the brief's verified $100-190 agency band: SocialPilot at $100/mo, Outsourced Agency at $190/mo, with one agency deal equal to 4-5 practitioner subscriptions. **[VERIFIED]** Source: https://www.socialpilot.co/ (red-team's own verification during the attack pass). $149 is the midpoint of the band: above the volume-tool floor because it carries full white-label resale rights, below the done-for-them ceiling because delivery is templated, not custom.

## Founding Member Annual: $470/yr

Mirrors The Social Broker's $470/yr annual, the proven annual price point in this exact category. **[VERIFIED]** Source: https://thesocialbroker.com/membership. At our $49/mo base this is roughly two months free, and the brief flags founding-member annual deals as the mechanism that pulls cash forward during the ramp (first dollar ~day 45, $400/mo by day 90, red-team verified figures).

## Rails note

Own-site Stripe checkout with weekly payouts, per the brief's rail verdict: Stripe is the right rail but not zero-risk, with 2025-documented freezes and 90-180 day termination reserves; mitigations are weekly payout schedule, low refund rates, and avoiding "AI-generated" framing in product descriptors during the new-account window. **[LIKELY]** Source: https://stripe.com/legal/consumer (red-team caveat; holds trigger on dispute rates above ~0.75% and volume spikes, not low-volume digital catalogs). All three mitigations are implemented in `02-product-descriptors.md` and `03-stripe-setup-walkthrough.md`.
