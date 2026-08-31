# Delivery Surface Verdict — Productized Content-Intelligence Reports

**Question:** Which surface wins for (i) the sellable premium report and (ii) the interactive lead magnet?
**Date:** 2026-08-27 · Sources: Adobe help docs (via search index), Mapsoft PDF Spaces analysis, multi-source pricing checks. adobe.com itself timed out from this environment; every Adobe claim below is corroborated by ≥2 independent sources.

## The make-or-break answer first

**Recipients do NOT need a subscription.** PDF Spaces has a public "Share for View" mode: anyone with the URL can open the Space, read the documents, listen to the audio overview, and chat with the AI Assistant — no Adobe account required [VERIFIED — Adobe help share-pdf-spaces page + Mapsoft]. Invited "Share for Review" collaborators need only a free Adobe ID, never a paid plan [VERIFIED]. So PDF Spaces does not die as a lead magnet on subscription grounds. It dies on a different one: **no capture.** A Space has no form, no email gate, no analytics you own, and it lives on Adobe's domain under Adobe's chrome. A lead magnet that can't capture the lead is a brochure.

## Verified facts

- **Acrobat Studio individual pricing:** $24.99/mo on the annual plan (~$300/yr), $34.99 month-to-month [VERIFIED — multiple 2026 pricing pages incl. Adobe-sourced listings]. Creating Spaces requires Studio (or the Express AI tier); Acrobat Pro/Standard alone cannot create them [VERIFIED — Mapsoft]. Studio bundles Acrobat Pro, AI Assistant, Express Premium, Adobe Stock/Fonts [VERIFIED].
- **Space limits:** 100 files per Space, 100 MB/file, 600 pages/file [VERIFIED — Mapsoft].
- **Branding:** you can apply a logo, set a color palette, edit title/summary — in both share modes [VERIFIED — Mapsoft]. Full white-label (your domain, your layout system) is not offered [LIKELY — no such option documented anywhere reviewed].
- **Selling access:** no paywall, licensing, or commerce mechanism exists for a Space; it is a sharing surface, not a product surface [LIKELY — absent from all docs reviewed].
- **Harness-native pipeline:** `execution/render_brief.py` exists and drives the Readout OS premium-brief system (Ink+Steel Blue); Adobe Express export via MCP (`export_html_to_express`) is live in this session [VERIFIED — on disk / in session]. Marginal cost $0.
- **Interactive HTML lead magnet** (static page, form + localStorage, baked per-niche) is already designed in this session's spine work [VERIFIED — session artifact]. Cost $0; hosting is a static file anywhere.

## Comparison

| Surface | Recipient experience | Cost | Brandable | Sellable | Verdict |
|---|---|---|---|---|---|
| **Acrobat Studio PDF Space** | Click link → Adobe-hosted Space; read, audio overview, AI chat; no account needed (view mode) [VERIFIED] | $24.99–34.99/mo to create [VERIFIED] | Partial: logo + palette only; Adobe chrome/domain remain [VERIFIED] | No paywall; can't gate or transact [LIKELY] | Novelty bonus layer, not a primary surface |
| **Harness HTML brief → PDF** (render_brief.py) | Opens anywhere, offline, forwardable, prints clean; zero friction | $0 [VERIFIED] | Total — your design system, pixel-level [VERIFIED] | Yes — attach to any checkout (Stripe/Gumroad/ThriveCart) | **Wins (i)** |
| **Interactive HTML lead magnet** (static, form + localStorage) | Instant in-browser, personalized per-niche, captures email on your endpoint | $0 [VERIFIED] | Total [VERIFIED] | N/A — it's the capture asset | **Wins (ii)** |

## Recommendation (i) — Sellable premium report

Ship the **harness-native premium HTML brief → PDF** (render_brief.py / Readout OS). It's $0 marginal, fully branded, and a PDF is the only format every buyer trusts, forwards, and files — which is exactly the word-of-mouth surface a $500–2,500 report needs. PDF Spaces can't be sold, can't be gated, and wraps your work in Adobe's chrome. If a client's org already lives in Acrobat, offer a PDF Space as a *delivery bonus* ("chat with your report") — $25/mo is trivial against one sale, but only buy it when a buyer asks. Don't build the product on rented ground.

## Recommendation (ii) — Interactive lead magnet

Ship the **already-designed static interactive HTML page**. It does the one thing a lead magnet exists to do — capture the email — which PDF Spaces structurally cannot (no form, no gate, Adobe's domain, Adobe's analytics silence). It's $0, per-niche bakeable, and every interaction happens on a URL you own. The AI-chat novelty of a Space is real but unmonetizable at top-of-funnel: you'd pay $300/yr to hand Adobe your traffic. Verdict: HTML magnet captures; the premium PDF converts; PDF Spaces is an optional buyer-side garnish, never the funnel.
