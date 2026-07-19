# /lynch-price-architecture — Price-Increment Psychology (Ron Lynch)

> Lynch's pricing method for products and offers: people think in $20 bills (the ATM increment), then $100 bills — price to the increment ceiling, test UP before down, and never focus-group what you can market-test. Verbatim, on hearing $29.95: *"We got to test that at 39 cuz you just left 10 bucks on the table."* Distinct from `/lynch-deal-structure` (how the STRATEGIST gets paid) — this is how the PRODUCT gets priced.

Source anchor: `extractions/ron-lynch/transcript-2-dOM.txt`; ledger in `references/source-ledger.md`.

## When to Use
- Setting or revising a price for a product, offer, tier, or bundle
- "Should this be $29 or $39?" questions — the increment logic decides
- Designing price tests (how many versions, what ladder)
- Multi-audience offers where targeting allows different prices per segment
- Client pricing conversations (supplement offers, digital products, services)

## When NOT to Use
- The strategist's own fees (→ `/lynch-deal-structure`)
- Offer-tier DESIGN across audiences (→ `/lynch-umbrella-map` Step 4 — stack after)

## Inputs Required
1. The offer and its cost structure (COGS/delivery cost, even rough)
2. Current or proposed price
3. Channel (DR/online lets you test; retail anchors differently)
4. Audience segments if targeting allows per-segment offers

## Execution Steps

### Step 1: Find the Increment Ceiling
Map the proposed price to the mental increment ladder: $19.95 / $39.95 / $59.95 / $99.95 (then $100-bill steps: $199, $299...). A price mid-increment ($29.95) pays for the increment above it in perception while collecting the one below — move to the ceiling of its increment band and test there first. Flag multiples that silently sum to the next bill in the buyer's head (Lynch: 3 × $29 reads as $100).

### Step 2: Anchor High for Margin
Verbatim: *"I very much like to anchor at the highest possible retail price I can find so that I have margin because... the audience is actually paying for the marketing."* And the retail foresight: win DR and *"it ends up in Walmart and I just lost 50% of the retail price."* Set the anchor so wholesale at 50% still works. Margin is what funds contests, giveaways, media, and royalties — a thin-margin price kills every downstream Lynch mechanism.

### Step 3: Design the Test Ladder
Market-test, never focus-group (*"No, it's actually online testing"* — up to 14 versions per show in his practice). Minimum viable ladder: current price, increment ceiling, one step UP. Payments variant where the channel supports it (N × increment), checked against Step 1's summing trap.

### Step 4: Per-Segment Offers (if targeting allows)
Same product, different offer per audience — his CTV example: the teen sees $14.95 acne framing; the mother sees the $59 version. Map segments → offer framings → price points. Guardrail: segment pricing must never be discoverable cross-segment in a way that violates trust (HK-14: never violate trust without them knowing).

### Step 5: Decide and Instrument
Pick the launch price and the test plan. Name the metric that settles it (efficiency per order, not just conversion). In DR/royalty contexts, the price decision is also the attribution economics — note the impact on any royalty math.

## Output Format
```
## PRICE ARCHITECTURE — [Offer]

### Increment analysis
Current/proposed: [$X] → band: [$__ bill] → ceiling: [$X]
Summing trap check: [any multiples that read as the next bill]

### Anchor + margin
Anchor price: [$X] · COGS: [$X] · Margin at anchor: [%] · Survives 50% wholesale: [Y/N]

### Test ladder
| Version | Price | Hypothesis |
|---|---|---|

### Per-segment offers (if applicable)
| Segment | Framing | Price |
|---|---|---|

### Decision
Launch at [$X]; settle by [metric] after [test window]
```
Execution prompt: `references/prompts-v2/lynch-price-architecture.md`

## Quality Gate
- Price sits at an increment ceiling, not mid-band, unless a test says otherwise
- Test ladder includes at least one step UP from the proposed price
- Margin survives the 50% wholesale future at the chosen anchor
- No focus-group logic anywhere — every open question resolves by market test
- Per-segment pricing passes the trust guardrail
