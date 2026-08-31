# Video Context Ledger

Source: [I Rebuilt a Shopify Product Page Without a Developer or Page Builder](https://www.youtube.com/watch?v=fwv1l_kdW18), BitBranding, uploaded 2026-08-27.

The machine-readable ledger contains 1,100 caption-backed spoken rows. The rows below are the reviewed decision anchors that changed the extraction.

| Time | Evidence type | Observation | Confidence |
|---|---|---|---|
| 00:00-03:50 | observed_spoken | The product page is framed as the conversion bottleneck after traffic acquisition; the under-1% conversion figure is a demo claim, not audited store evidence. | high for speech; unverified outcome |
| 03:50-07:10 | observed_spoken + observed_visual | Eleven apparel PDP modules are arranged around buyer objections, from media and value statement through fit, reviews, FAQ, and cross-sell. | high |
| 07:10-10:30 | observed_spoken | Five copy rules: customer evidence before product prose, spec-tied claims, FAQ before description, authentic voice samples, and fit as a conversion feature. | high |
| 10:30-16:40 | observed_spoken + observed_visual | A brand dossier gathers customer, product, fit, support, return, voice, constraint, and reference-page evidence into one paste-ready context block. | high |
| 16:40-22:55 | observed_spoken + observed_visual | The build prompt explicitly asks the model to ask questions first; the model then produces a blueprint and flags missing facts before theme mutation. | high |
| 23:00-26:20 | observed_spoken + observed_visual | The demonstrated deployment uses a Shopify connector and a uniquely named duplicated draft theme. | high for demo; current connector availability unverified |
| 26:20-31:40 | observed_spoken + observed_visual | The first mutation is incomplete. A numbered repair prompt corrects media, swatches, CTA hierarchy, accelerated checkout, quantity, copy density, reviews, and size-chart behavior. | high |
| 31:40-36:25 | observed_spoken + observed_visual | Some app blocks require manual Shopify editor work; the size chart is inspected as an editable table, not accepted from summary text alone. | high |
| 36:25-40:27 | observed_spoken | Known limits include checkout constraints, cart risk, hallucinated theme references, performance weight, and the inability to infer conversion without an experiment. | high |

## Evidence boundary

- `observed_spoken`: native YouTube captions, cleaned and retained with timestamped segments.
- `observed_visual`: ten manually reviewed screen-share frames retained in `frames/`.
- No OCR engine was used; visible UI text was read manually from the retained frames.
- No store analytics, A/B-test results, or post-launch revenue receipts were supplied.
