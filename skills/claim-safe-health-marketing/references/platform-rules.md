# Platform-Specific Compliance Rules

> Load for `/pre-launch-gate` and `/claim-safe-hooks`. FTC/FDA is the legal floor; platforms enforce a stricter, partly-automated second layer (genius.md GP-06). Passing legal review does not guarantee passing platform review — always run both passes.

## Meta (Facebook/Instagram)

Source: Meta Transparency Center, Health & Wellness ad standards (transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/).

- Ads must not claim to cure, treat, or prevent disease or serious medical conditions.
- **Disclaimer must appear in the ad copy itself** — not just the landing page. Use the full DSHEA disclaimer text (see `workflows/04-pre-launch-compliance-gate.md`).
- **Personal Attributes policy**: cannot assert or imply knowledge of a viewer's health condition. No second-person symptom framing ("Sick of your anxiety attacks?"). Applies even to fully compliant structure/function products — the violation is the implied-diagnosis framing, not the underlying claim.
- Restricted phrases trigger manual review unless supporting documentation is pre-loaded to the ad account: "guaranteed," "instant relief," "clinically proven."
- High-risk categories facing extra scrutiny: weight loss, supplements, mental health, beauty, pain relief.
- Enforcement: rejected ads, account-level restrictions, or permanent bans for repeat violations — check account health before assuming a rejection is claim-specific.

## TikTok

Source: TikTok Ads healthcare/pharmaceuticals policy + dietary supplements policy (ads.tiktok.com/help, seller-us.tiktok.com/university).

- Health-related claims are tightly restricted platform-wide: no medical, weight-management, or wellness claim is permitted unless it exactly matches an approved OTC Drug Facts "Uses" statement.
- **Weight-loss and muscle-gain positioning as the CENTRAL claim is effectively prohibited** for supplement ads — reframe to broader wellness: energy, hydration, recovery, balance, confidence.
- GLP-1/Ozempic-adjacent promotion is not allowed.
- "Clinically proven," "dermatologist tested," "scientifically formulated" all require submitted documentation at ad review — unsupported use results in rejection, not just a warning.
- US creators promoting OTC-adjacent products must enable Geo-Toggle for jurisdictional compliance.

## Amazon

Source: Amazon Seller Central dietary-supplement policy + prohibited disease-claims policy (sellercentral.amazon.com/help).

- Automated systems scan title, bullet points, description, and A+ content for disease-name tokens (cancer, diabetes, anxiety, COVID-19, herpes, HIV, lupus, Parkinson's, etc.) and treatment-verb tokens (cure, treat, treatment, heal, remedy) — **the scanner does not parse sentence-level meaning**; it flags tokens regardless of surrounding compliant context.
- Required disclaimer for any listing that could lead a customer to believe FDA reviewed the product: "This statement has not been evaluated by the FDA. This product is not intended to diagnose, treat, cure, or prevent any disease."
- **Practical rule**: write Amazon listing copy assuming a keyword scanner reads it before any human does. Avoid disease-name tokens even in negation ("not intended for people with diabetes" still trips the filter in practice).
- Listings can be suppressed even when the claim technically complies with FDA's structure/function framework — Amazon's bar is stricter and less nuanced than the FDA's.

## Cross-Platform Decision Rule

Before launch, run the claim-audit output (from `/claim-audit`) through all three platform filters independently — a claim that clears FTC/FDA/DSHEA can still fail Meta (Personal Attributes), TikTok (central-claim framing), or Amazon (keyword scanner) for reasons that have nothing to do with the underlying legal risk.
