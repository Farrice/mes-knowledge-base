# Stripe setup walkthrough (about 15 minutes)

Paste-in guide for the account owner. Steps marked **[OWNER ONLY]** require the Stripe account owner's login and cannot be delegated to a teammate with limited permissions or done by anyone else on your behalf. Everything references the current Stripe Dashboard (dashboard.stripe.com).

## Part 1: Account basics (owner, ~4 min)

1. **[OWNER ONLY]** Log in at dashboard.stripe.com. If the account is brand new, complete business verification first (legal name, EIN or SSN, bank account). Payments cannot go live without it.
2. **[OWNER ONLY]** Go to **Settings → Business → Public details**. Set the public business name to **Listing Launch Studio** (or the locked brand), add the support email and the storefront URL. Mismatch between checkout brand and account details is a review flag on new accounts.
3. **[OWNER ONLY]** Still in Settings, open **Business → Bank accounts and currencies** and confirm the payout bank account is verified.
4. **[OWNER ONLY]** Go to **Settings → Payments → Statement descriptor**. Set it to `LISTINGLAUNCH`. This is freeze mitigation #3 (descriptor framing): the buyer's card statement must show the brand they bought from, and the descriptor text stays method-neutral. Use the exact wording in `02-product-descriptors.md` everywhere; never type "AI-generated" into any product name, description, or metadata field.

## Part 2: Products and prices (~5 min)

5. Go to **Product catalog → Add product**.
6. Create product 1: name **Listing Launch Studio - Practitioner Membership**. Paste the description from `02-product-descriptors.md` word for word.
7. Add its price: **Recurring**, **$49.00 USD**, billing period **Monthly**. Save product.
8. Repeat for product 2: **Listing Launch Studio - White-Label Agency License**, recurring **$149.00 USD monthly**, description pasted from the descriptor file.
9. Repeat for product 3: **Listing Launch Studio - Founding Member Annual**, recurring **$470.00 USD yearly**, description pasted from the descriptor file.
10. Double-check all three descriptions against `02-product-descriptors.md`. This is where freeze mitigation #3 lives in practice: reviewers read these fields.

## Part 3: Payment links (~3 min)

11. Go to **Payment links → New** (or the **Create payment link** button on each product page).
12. Create one link per product (three links total). For each: select the product's recurring price, turn ON **Collect customers' addresses → Billing addresses** (helps dispute defense), and leave quantity fixed at 1.
13. Under the link's **After payment** setting, choose **Redirect customers to your website** and point it at your thank-you/onboarding page so buyers land somewhere that tells them what happens next. Confused buyers file disputes; oriented buyers don't.
14. Copy the three link URLs and paste them into the three CTA buttons on the sales page (`01-sales-page.md`: Practitioner, White-Label, Founding Member).
15. Test each link in a private browser window using Stripe test mode first (**toggle Test mode**, top right), then verify once in live mode with a real card and immediately refund yourself. **[OWNER ONLY]** for the live-mode test and refund.

## Part 4: Weekly payouts (~1 min)

16. **[OWNER ONLY]** Go to **Settings → Payments → Payouts** (labeled "Payout schedule"). Set schedule to **Weekly** and pick a payout day. This is freeze mitigation #1 from the brief: a weekly schedule keeps the rolling balance small, so if the account ever gets reviewed or reserved, the amount at risk is one week's revenue, not a quarter's.

## Part 5: Refund posture and dispute hygiene (~2 min)

17. Publish the cancellation/refund policy exactly as worded on the sales page FAQ: cancel anytime in one click, delivered months are licensed on delivery and not refundable. This is freeze mitigation #2 (low refund policy wording): the policy is stated before purchase, which keeps refund requests rare and defensible, while easy cancellation keeps disputes near zero. The brief's threshold to stay far under is a ~0.75% dispute rate [LIKELY].
18. Operating rule, standing: if a buyer emails angry and asks for money back, refund them immediately anyway. A $49 refund is cheap; a dispute counts against the account forever. Refunds are issued from **Payments → (select payment) → Refund**; any teammate with refund permission can do this, it is not owner-only.
19. **[OWNER ONLY]** Go to **Settings → Team and security** and confirm two-step authentication is on for the owner login.

Done. Total: three live products, three payment links wired to the sales page, weekly payouts, and all three freeze mitigations from the brief in place (weekly payout schedule, stated low-refund policy with one-click cancel, method-neutral descriptor framing).
