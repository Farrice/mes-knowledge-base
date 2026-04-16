# tommy-clark ✅

**Status:** success
**Model:** gemini-2.5-flash
**Tokens:** 6,643
**Cost:** $0.0032
**Duration:** 14.0s
**Thinking Tokens:** 1,201
**Grounding Queries:** 1

---

**SUMMARY**

Kalshi's trading fees are dynamic, primarily based on contract price and order type (taker vs. maker), with higher fees for contracts priced around 50 cents. While direct API access itself doesn't incur a monetary cost, advanced API tiers are performance-gated by significant monthly trading volume. Founders must strategically account for these variable fees to accurately assess profitability and hedging costs.

**KEY FINDINGS**

*   **Variable Per-Contract Trading Fees:** Kalshi employs a sliding scale for trading fees, not a flat rate. Fees are highest for contracts priced between 40¢ and 60¢, peaking at 50¢, and are lowest for contracts near 1¢ or 99¢.
*   **Taker vs. Maker Fee Structure:** General trading (taker) fees are calculated as `round up(0.07 * C * P * (1-P))`, where C is the number of contracts and P is the contract price. For maker orders (resting on the order book), the fee is `round up(0.0175 * C * P * (1-P))`. Some specific markets, such as S&P500 and Nasdaq-100, have a reduced taker fee of `round up(0.035 * C * P * (1-P))`. The maximum commission per contract is $0.02.
*   **No Direct API Access Cost, but Tiered Access:** Kalshi does not charge a direct fee for API access. However, API rate limits are tiered. Basic access is granted upon signup, Advanced requires a form, and Premier/Prime tiers are volume-gated, requiring 3.75% and 7.5% of exchange traded volume, respectively, in a given month. Public market data endpoints are accessible without API keys or authentication.
*   **Deposit/Withdrawal Fees:** Debit card deposits and withdrawals incur a 2% processing fee. ACH bank transfers and wire transfers (both deposits and withdrawals) are free from Kalshi's side. There are no settlement or membership fees.

**RECOMMENDATIONS**

1.  **"How I" De-Risked My Hedging Strategy by Understanding Kalshi's Fee Skew:** As a founder, don't just look at the headline fee. I'd model out potential hedging scenarios, especially around "50/50" events, to understand the true cost. My content would be a "How I" narrative detailing the specific event, the contract prices I considered, and the *actual* fee impact on my P&L, showing how ignoring the fee skew around 50¢ contracts is a hidden cost center. This shifts from generic "understand fees" to a tactical, lived experience.
2.  **Engineer Your API Strategy for Cost-Efficiency, Not Just Access:** For founders building algorithmic trading or sophisticated data analysis on Kalshi, the "cost" isn't a subscription fee, it's the *volume-gated API tiers*. My recommendation is to start lean, utilizing unauthenticated public endpoints for general market data before committing to the volume needed for Premier/Prime. Then, I'd build a "How I" narrative around optimizing API calls to *minimize unnecessary inference* (as one Reddit user highlighted for AI agents), treating API usage as an infrastructure cost to optimize, not a fixed expense.
3.  **Leverage Free Deposit/Withdrawal Methods; Document the Savings:** Most founders overlook the small cuts. My advice is simple: use ACH or wire transfers for all Kalshi funding and withdrawals to avoid the 2% debit card fee. My content hook here would be a "Stop doing X" post: "Stop losing 2% on every Kalshi deposit. Here's the *exact* transfer method I use to keep more capital in my trading account." This directly addresses a common, easily avoidable mistake with a clear, actionable alternative.

**CONFIDENCE**: High

**DISSENT**:
While the fee schedule is explicitly detailed on Kalshi's site, the *implication* of the variable fee structure for active traders or market makers can be easily underestimated. Casual users might not grasp how rapidly fees can accumulate on mid-priced contracts, potentially eroding small gains or increasing hedging costs more than anticipated. The "maximum commission of $0.02 per contract" also needs to be understood in the context of the variable percentage formula; it's a cap, not a flat rate, which can be misleading if not fully explained. Additionally, while no direct API *access* fees exist, the volume requirements for higher tiers are a significant barrier for smaller operations, effectively making high-frequency API trading an "expensive" endeavor if not consistently hitting volume targets.
