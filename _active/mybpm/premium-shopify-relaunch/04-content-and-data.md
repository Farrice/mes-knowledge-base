# Content and Data Contract

## Homepage sequence

1. Drop hero with one campaign image and two actions
2. Brand manifesto
3. Four-product current edit
4. Editorial story image and thesis
5. Three inspectable proof points
6. Email capture and compact navigation

## Product page sequence

1. Editorial gallery
2. Title, price, one short description, variants, and buy buttons
3. Structured garment notes: story, material, fit, care, production, shipping/returns
4. Related products labeled `COMPLETE THE EDIT`

## Product metafields

Create these fields in Shopify under **Settings → Custom data → Products**:

| Namespace and key | Type | Purpose |
|---|---|---|
| `custom.short_description` | Single-line or multi-line text | 25–45 word sales introduction |
| `custom.product_story` | Rich text | Cultural/design story without repeating specifications |
| `custom.material` | Rich text | Verified fiber, fabric weight, and construction |
| `custom.fit_note` | Rich text | Silhouette, size guidance, and model measurements |
| `custom.care` | Rich text | Supplier-confirmed care instructions |
| `custom.production_note` | Rich text | Production method and honest lead time |

Collection metafield: `custom.short_description` as multi-line text.

## Asset minimum per hero product

- 2400 px or larger long edge
- 4:5 product-card crop
- Desktop landscape campaign crop
- Mobile portrait campaign crop
- Front, back, detail, and on-body angles
- Human-written alt text that describes the image; never keyword lists

## Required policy reconciliation

Before launch, the live shipping, returns, privacy, terms, production lead time, and supplier language must agree with each other and with checkout. The theme deliberately does not invent policy promises.
