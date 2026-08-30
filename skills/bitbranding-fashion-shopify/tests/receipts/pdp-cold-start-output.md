# PDP Blueprint: Night Signal — Afterhours Tee

## Evidence Status

| Field | Value/source | Status | Build consequence |
|---|---|---|---|
| Price | $48, fixture | VERIFIED | May be used in page architecture. |
| Colors and sizes | Black/Bone; S-XL, fixture | VERIFIED | Supports swatch and size-selector requirements. |
| Care | Machine wash cold; hang dry, fixture | VERIFIED | May be used in care content. |
| Fabric composition and weight | Not supplied | MISSING | Blocks material and “heavyweight” claims. |
| Fit and garment measurements | Not supplied | MISSING | Blocks fit copy and size guidance. |
| Model data | Not supplied | MISSING | Blocks model-size caption. |
| Shipping and returns | Not supplied | MISSING | Blocks the trust row and policy FAQ. |
| Voice | No samples | MISSING | Blocks final brand-voice copy. |
| Reference PDPs | None | MISSING | Prevents a source-grounded visual-reference comparison. |

## Missing Facts

| # | Missing fact | Why it changes the page | Blocking? |
|---|---|---|---|
| 1 | Fit classification and garment measurements | Fit uncertainty and “too short” returns are the two strongest signals. | Yes |
| 2 | Fabric composition and weight | Buyers expected a heavier garment; unsupported “heavyweight” copy would increase mismatch. | Yes |
| 3 | Model height and worn size | Needed to make the on-body gallery useful. | Yes |
| 4 | Print method and tested care evidence | Needed before answering the cracking question. | Yes |
| 5 | Shipping and return policies | Needed before writing the trust row or policy FAQ. | Yes |
| 6 | Authentic voice samples | Needed before final product copy. | Yes |
| 7 | Two or three reference PDPs | Needed to distinguish desired page decisions from generic “premium” styling. | No for architecture; yes for visual direction |

## Questions

1. What are the garment's chest width and body length by size, and is the intended fit true, relaxed, boxy, or oversized?
2. What are the fabric composition and measured weight?
3. What are the model's height and worn size for each available on-body image?
4. What print method is used, and what durability evidence exists beyond the care instruction?
5. What are the exact shipping and return terms?
6. Which three authentic brand passages should govern product-page voice?
7. Which two or three PDPs contain decisions Night Signal wants to borrow—and which decisions?

## Objection Ledger

| Buyer uncertainty | Evidence/frequency | Page response | Module | Priority |
|---|---|---|---|---|
| Is it oversized or true to size? | 17 questions | Fit classification, garment measurements, model context | Size selector + fit/fabric block | 1 |
| Will it be too short? | 12 questions + 9 returns | Body length by size, silhouette media, model data | Gallery + inline size guidance | 1 |
| Is it actually heavy? | 7 returns | Composition and measured fabric weight | Value statement + fit/fabric block | 1 |
| Will the print crack? | 8 questions | Print method, tested care evidence, bounded care claim | FAQ + care block | 2 |
| Is Bone available? | 6 questions | Visual swatch state and restock behavior | Color swatches | 3 |

## Mobile-First Module Blueprint

### 1. On-body Gallery
**Job:** Establish silhouette and body length before purchase.  
**Evidence used:** Fit and length questions plus “too short” returns.  
**Copy/data/media required:** On-body front/side/back images; model height/size; garment length.  
**Acceptance check:** The first mobile image shows the garment on a body; no model claim appears until data exists.

### 2. Title, Price, and Evidence-Bound Value Statement
**Job:** Orient the buyer without an unsupported premium or heavyweight claim.  
**Evidence used:** Verified title/price only; material facts are missing.  
**Copy/data/media required:** Verified composition, weight, fit, or construction fact.  
**Acceptance check:** Value statement remains a placeholder until one differentiating fact is verified.

### 3. Color Swatches
**Job:** Make Black/Bone selection and availability visible.  
**Evidence used:** Verified colors and six restock questions.  
**Copy/data/media required:** Correct variant/media binding and restock state.  
**Acceptance check:** Swatch changes the selected variant and its media; unavailable state is truthful.

### 4. Size Selector With Inline Guidance
**Job:** Resolve the highest-frequency uncertainty before add-to-cart.  
**Evidence used:** 17 fit questions, 12 length questions, 9 length-related returns.  
**Copy/data/media required:** Fit classification and size-by-size measurements.  
**Acceptance check:** Module is blocked until measurements are supplied.

### 5. Add-to-Cart and Trust Area
**Job:** Make the action clear while exposing real policy evidence.  
**Evidence used:** Product variants are verified; policies are missing.  
**Copy/data/media required:** Stock state, shipping and return terms.  
**Acceptance check:** No fabricated shipping or return promise appears.

### 6. Fit, Fabric, Care, and Objection FAQ
**Job:** Resolve weight, fit, length, care, and print-durability questions with evidence.  
**Evidence used:** Support and return signals.  
**Copy/data/media required:** Composition, weight, measurements, print method, durability evidence.  
**Acceptance check:** FAQ answers remain blocked where evidence is absent.

## Copy Requirements

- Write the fit and material FAQ before the long description.
- Do not use “heavyweight,” “premium,” “durable,” “oversized,” or “true to size” until verified.
- Use the supplied care instruction exactly; do not infer wash durability from it.

## Media Shot List

- On-body front, side, and back views with model context.
- Close-up of fabric texture and print application.
- Measurement diagram showing body length and chest width.
- Correct Black and Bone variant media.

## Data Bindings & App Dependencies

- Variant-linked swatches and media: theme capability must be verified live.
- Size chart: editable theme section or approved app block; exact app inventory is missing.
- Reviews: no app is named; placement remains `UNCONFIRMED`.

## Claims Veto List

- Heavyweight
- Premium cotton
- Oversized or true-to-size
- Holds shape or print after a stated number of washes
- Easy returns or a shipping-speed promise
- Any model-size statement

## Blueprint Decision

`BLOCKED BY FACTS`

No Shopify mutation packet was produced. Connector state is `NO PERMISSION`. The next safe action is to answer the seven missing-fact questions.
