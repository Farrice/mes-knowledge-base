# tommy-clark ✅

**Status:** success
**Model:** gemini-2.5-flash
**Tokens:** 6,991
**Cost:** $0.0029
**Duration:** 16.1s
**Thinking Tokens:** 1,628
**Grounding Queries:** 1

---

**SUMMARY**

Polymarket employs a dynamic taker-fee model that varies by market category and probability, with makers receiving rebates. API access ranges from free for basic use to premium tiers starting at $99/month for high-volume and enterprise needs. Understanding these nuances is critical for optimizing trading strategies and data utilization.

**KEY FINDINGS**

*   **Dynamic Taker-Only Fees**: Polymarket charges fees exclusively to "takers" (market orders), while "makers" (limit orders) receive rebates. The fee amount is dynamic, peaking when the event probability is 50% ($0.50 per share) and decreasing towards the extremes of $0.01 or $0.99.
*   **Category-Specific Fee Coefficients**: The "taker fee coefficient" (Θ) varies significantly by market category. For instance, crypto markets have the highest peak fee at 1.80% (Θ = 0.072) for a $0.50 trade, while geopolitics markets are entirely fee-free. Other categories like sports (0.75%), finance/politics/tech (1.00%), and economics/general (1.25%) fall in between.
*   **Maker Rebates & Temporary Taker Rebate**: Makers receive rebates ranging from 20% of taker fees in crypto to 50% in finance markets, incentivizing liquidity provision. Additionally, a temporary 50% taker rebate is applied to all trades across all markets through April 30th, distributed weekly.
*   **Tiered API Access**: Basic API access is free, offering core market and price data with rate limits of up to 1,000 calls/hour for non-trading queries. Premium tiers for high-volume users start at $99/month, providing WebSocket feeds and deeper historical data, with enterprise plans beginning at $500+/month for dedicated nodes and institutional support.
*   **Regulatory Compliance for US API**: For Polymarket US, a CFTC-regulated entity, API access requires an application process and integration testing to ensure compliance and security, indicating a higher barrier to entry for institutional use.

**RECOMMENDATIONS**

*   **For Founders Building Trading Strategies ("How I" Narrative Pivot):** Instead of generic advice on "how to trade," share "How I cut my Polymarket trading costs by 30% by strategically placing limit orders and leveraging maker rebates, especially in Finance markets where rebates hit 50%." Detail a specific scenario where understanding the fee curve at $0.50 vs. $0.90 made a tangible difference in profit.
*   **For Content on API Integration (Stealth Hook Engineering):** To capture attention, use a stealth hook like: "The 'free' Polymarket API isn't just for hobbyists. Here's how my team extracted high-intent market sentiment for our SaaS product, bypassing the $99/month tier and what we learned about its hidden capabilities." This targets founders looking for cost-effective data solutions.
*   **For Audience Design & Engagement (20/5 Protocol):** To attract quantitative founders and crypto data analysts, create content that dissects the fee formula (`Fee = Θ × C × p × (1 - p)`) with real-world examples across different market categories. Engage with 20 relevant ICPs daily (e.g., founders of crypto analytics platforms, algo trading firms) and comment on 5 Hub accounts (e.g., DeFi research groups, prominent crypto economists) discussing prediction market mechanics or API data use.

**CONFIDENCE**: High

**DISSENT**: While Polymarket's documentation is specific about fees, the temporary 50% taker rebate expiring on April 30th means that any long-term content or strategy built around this specific rebate will quickly become outdated. Founders need to be aware that the "effective" cost of trading will increase after this date, and strategies should account for the permanent fee structure rather than temporary promotions. This could be a "stealth trap" for those who don't read the fine print.
