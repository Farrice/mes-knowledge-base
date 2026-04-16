# lulu-cheng-meservey ✅

**Status:** success
**Model:** gemini-2.5-flash
**Tokens:** 8,907
**Cost:** $0.0037
**Duration:** 26.7s
**Thinking Tokens:** 3,311
**Grounding Queries:** 1

---

**SUMMARY**

As of April 2026, Polymarket has transitioned to a dynamic taker-fee model for most markets, calculated by a formula that scales with price uncertainty, while implementing maker rebates and maintaining zero fees on deposits, withdrawals, and winnings. API access for market data remains free, with trading capabilities requiring a wallet and USDC.

**KEY FINDINGS**

*   **Dynamic Trading Fees:** Polymarket has moved from a largely fee-free model to a dynamic taker-fee structure, effective March 30, 2026, across various market categories. Fees are calculated using the formula `Fee = Θ × C × p × (1 − p)`, where `Θ` (theta) is a market-specific coefficient, `C` is the number of contracts, and `p` is the trade price.
*   **Price-Sensitive Taker Fees:** Fees are highest when market probabilities are near 50% ($0.50 per share) and decrease towards the price extremes (near $0.01 or $0.99), designed to protect liquidity providers in high-risk scenarios.
    *   Specific `Θ` values vary: Crypto markets have the highest rate (up to 1.80% or 3.15% peak), while Finance, Politics, and Tech markets are around 1.00%, and Sports markets are lower. Geopolitical and global events markets remain notably fee-free.
*   **Maker Rebate Program:** Polymarket operates a "circular economy" where taker fees fund rebates for market makers, incentivizing liquidity provision. The Maker Rebate Coefficient (`Θ`) is 0.0125 (25% of taker fees, applied at the point of trade), with some Finance markets offering up to 50% rebate. A temporary 50% taker rebate for all markets is also in effect through April 30th.
*   **Zero Ancillary Fees:** Polymarket charges no fees for deposits, withdrawals, or winnings. Standard blockchain network (gas) fees may still apply for cryptocurrency transactions.
*   **Free API Data Access:** Polymarket provides API access to events, markets, order books, and trade history for free. Trading via API requires a wallet and USDC. The international exchange is the primary venue for serious API traders, offering robust features.

**RECOMMENDATIONS**

*   **Proactive Founder-Led Narrative on Fee Evolution (p01, p08):** The founder, or a key leader, must issue a direct, first-person communication (e.g., a blog post, video, or detailed thread) explaining the transition from a virtually fee-free environment to the current dynamic model. This narrative should frame the change not as a revenue grab, but as a necessary evolution for a mature, sustainable, and efficient prediction market, emphasizing enhanced liquidity and a healthier ecosystem. Use "Conviction Copy Transmutation" to transform the dry fee details into a compelling story of market improvement and longevity.
*   **Champion "Market Health" and "Circular Economy" as Core Differentiators (p02, p06):** Actively promote the maker rebate program and the concept that taker fees directly fund liquidity providers as a core philosophical advantage. Position Polymarket as the "smart-fee" platform that prioritizes market vitality, drawing a "line in the sand" against traditional, extractive models. This appeals to sophisticated traders and DeFi enthusiasts who value ecosystem sustainability and fair market mechanics.
*   **Segmented and Transparent Fee Communication (p04):**
    *   **For Casual Users:** Simplify the message: "No deposit/withdrawal fees, no fees on winnings, and dynamically low trading fees designed for market health." Highlight the fee-free geopolitical markets prominently.
    *   **For Advanced Traders/Makers & API Users:** Provide direct, easily accessible links to the detailed fee schedules and API documentation (`docs.polymarket.com`). Clearly articulate the benefits of the maker rebate program and the dynamic fee structure for optimizing their strategies and building applications. Emphasize the "free for data" API access as a significant advantage for builders.
*   **Amplify "No Fees on Winnings" as a Brand Pillar (p04):** This is a powerful, user-centric differentiator against traditional betting platforms. Integrate this message prominently into all marketing, user acquisition funnels, and product messaging. It directly addresses a key "cultural erogenous zone" of user fairness and value retention, fostering trust and converting attention into tangible sign-ups and trading activity.

**CONFIDENCE**: High

**DISSENT**:
*   The communication strategy must carefully manage the perception of the fee increase. While the dynamic model is sophisticated and aims for market health, the shift from "virtually fee-free" can still be a point of friction for some users, particularly those who haven't fully grasped the nuances of prediction market mechanics. The messaging needs to proactively address the "why now?" question and clearly articulate the long-term benefits to the user base.
*   The temporary nature of the "Taker Rebate = 50% of taker fees through April 30th" is a critical detail. While beneficial in April 2026, future communications beyond this date will need to adjust, and the founder's narrative should acknowledge this as a promotional period rather than a permanent feature.
*   The varying fee rates across different market categories, especially the higher rates for 15-minute crypto markets, could be confusing or off-putting if not explained within the context of combating latency arbitrage and protecting liquidity. The messaging should preemptively address these higher rates by emphasizing their purpose in maintaining market integrity, rather than letting users discover them in isolation.
