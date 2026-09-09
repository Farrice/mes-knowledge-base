# Build and Launch Runbook

## 1. Prepare the merchandise

- Approve the four-product edit or replace any sample-gated item.
- Order and inspect samples.
- Record measurements and supplier-confirmed material/care data.
- Complete the editorial shoot and final crops.

## 2. Upload as an unpublished theme

From this package directory, authenticate to the correct store and push the theme without publishing:

```sh
shopify auth login --store mybpm.store
shopify theme push --store mybpm.store --unpublished --theme "MyBPM v2 — White Signal Staging" --path theme
```

Record the returned theme ID and preview URL. Do not use `--publish` during staging. Verify that `Updated copy of MyBPM Ira 4.3.0` remains the `MAIN` theme after upload.

## 3. Configure the store in Shopify Admin

- Create collection `DROP 001 / SUBLEVEL` and add only approved products.
- Point the homepage product list and primary hero CTA to that collection.
- Create or verify the `our-story` page.
- Simplify the main menu to New Drop / Shop / Editorial / About.
- Create the metafields in `04-content-and-data.md` and populate every launch product.
- Replace social links only with real MyBPM profiles.
- Reconcile policies, fulfillment app, analytics, consent, and email capture.
- Remove or disable the broken `thisnew` and `popcustoms` storefront scripts if they are no longer operationally required.

## 4. Preview and QA

Use the unpublished Shopify preview—not the static direction preview—as the launch truth. Test every item in `06-qa.md` on current iPhone, Android-sized, tablet, and desktop viewports.

## 5. Publish boundary

Publishing is an external write with real revenue impact. It requires Farrice's explicit final approval after:

- Sample/capsule approval
- Mobile and desktop visual approval
- Checkout and policy PASS
- Broken-link/app console PASS
- Analytics purchase-event PASS
- A rollback copy of the current live theme is identified

Then publish the exact reviewed theme ID in Shopify Admin or with `shopify theme publish --theme <id>`.

## Rollback

Keep the current live theme unpublished and named with its former publish date. If a launch blocker appears, republish that known theme while the staging build is repaired.
