# lulu-cheng-meservey ✅

**Status:** success
**Model:** gemini-2.5-flash
**Tokens:** 6,224
**Cost:** $0.0029
**Duration:** 13.3s
**Thinking Tokens:** 1,128
**Grounding Queries:** 1

---

**SUMMARY**

As of April 2026, Kalshi's trading fees are variable per contract, primarily based on the contract's price, with higher fees for contracts nearing 50¢ and lower fees for contracts at the extreme ends of the price spectrum (1¢ or 99¢). API access itself does not incur direct monetary fees but is tiered, with higher access requiring significant trading volume thresholds.

**KEY FINDINGS**

*   **Variable Per-Contract Trading Fees:** Kalshi employs a dynamic fee structure where the cost per contract is not fixed but varies with the contract's price. Contracts priced around 40¢-60¢ (representing market uncertainty) incur the highest fees, while those at 1¢-5¢ or 95¢-99¢ have the lowest fees.
*   **Formulaic Fee Calculation:** General trading fees are calculated using the formula `fees = round up(0.07 x C x P x (1-P))`, where C is the number of contracts and P is the contract price in dollars. Maker fees for resting orders are lower, at `fees = round up(0.0175 x C x P x (1-P))`. Specific markets like S&P500 and Nasdaq-100 have a different formula: `fees = round up(0.035 x C x P x (1-P))`.
*   **No Direct API Access Costs, Tiered Access:** There are no explicit direct monetary costs for API access. However, API access is tiered (Basic, Advanced, Premier, Prime), with higher tiers requiring significant monthly exchange traded volume (e.g., Premier at 3.75% and Prime at 7.5%). Public market data endpoints are freely accessible without authentication.
*   **Deposit/Withdrawal Fee Considerations:** While not per-contract trading fees, users should be aware of a 2% processing fee for debit card deposits and withdrawals. ACH, wire transfers, PayPal, and Venmo deposits do not incur Kalshi's processing fees.

**RECOMMENDATIONS**

*   **Simplify Fee Communication for Broad Appeal (p01, p04):** While the detailed fee schedule is transparent, the variable nature can be a point of friction for new users. Develop founder-led content (e.g., a short video from the founder) that uses real-world examples to illustrate the fee impact across different contract prices, perhaps using a "what you see is what you get" narrative. Focus on the *value* derived despite the fee, converting attention to understanding and adoption.
*   **Highlight API Tier Benefits as a Value Proposition (p06, p07):** Position the API access tiers not as a cost, but as a commitment to serious traders and institutional partners. The volume-based qualification for Premier/Prime access can be framed as an exclusive benefit, attracting high-value users by creating a reality where Kalshi is the platform for sophisticated market participants. Emphasize the "no direct cost" for API usage as a competitive advantage.
*   **Address Debit Card Fees with a "Control Your Costs" Narrative (p01, p02):** Proactively address the 2% debit card fee in communications, framing it as a choice users can make to control their costs by opting for fee-free ACH or wire transfers. This taps into the cultural erogenous zone of financial autonomy and smart decision-making, rather than letting the fee be a surprise or a perceived penalty.

**CONFIDENCE**: High

**DISSENT**:
While the fee structure is mathematically clear on the Kalshi fee schedule, the complexity of a variable fee based on `P x (1-P)` (especially for those unfamiliar with probability distributions) could be perceived as opaque by a significant portion of the retail user base. This complexity, even if fair, might inadvertently deter casual traders who prefer simpler, flat-rate pricing models, potentially creating a "hidden cost" narrative if not effectively communicated. The current communication leans towards transparency for those who *seek* the detail, but it could be more proactive in simplifying the *implication* of the fees for the average user.
