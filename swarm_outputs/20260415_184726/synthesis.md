# Swarm Synthesis: What are Kalshi trading fees and API access costs as of April 2026? Per contract fee. Check kalshi.com/docs or kalshi.com/fee-schedule

## Executive Summary
As of April 2026, Kalshi does not charge a flat per-contract fee. Instead, trading fees are calculated dynamically based on the contract's price, peaking for contracts priced near 50¢ and decreasing for those at price extremes (e.g., 1¢ or 99¢). Maker orders receive a significant discount. There are no direct monetary costs for API access; however, access to higher-performance tiers is gated by achieving significant monthly exchange trading volume. Users should also be aware of a 2% processing fee on debit card transactions, which can be avoided by using ACH or wire transfers.

## Unanimous Agreements
| Finding | Supporting Agents |
|---------|------------------|
| **Variable Per-Contract Fees** | lulu-cheng-meservey, tommy-clark |
| Fees are highest for contracts priced around 50¢ and lowest for those near 1¢ or 99¢. | lulu-cheng-meservey, tommy-clark |
| **Specific Fee Formulas** | lulu-cheng-meservey, tommy-clark |
| Taker fees are `round up(0.07 * C * P * (1-P))`; Maker fees are `round up(0.0175 * C * P * (1-P))`. | lulu-cheng-meservey, tommy-clark |
| **No Direct API Access Cost** | lulu-cheng-meservey, tommy-clark |
| Access to higher API tiers (Premier/Prime) is performance-gated by monthly trading volume (3.75%/7.5%). | lulu-cheng-meservey, tommy-clark |
| **Deposit/Withdrawal Fees Exist** | lulu-cheng-meservey, tommy-clark |
| A 2% processing fee applies to debit card deposits/withdrawals; ACH and wire transfers are free. | lulu-cheng-meservey, tommy-clark |

## Key Recommendations
| Recommendation | Confidence | Lead Agent |
|----------------|------------|------------|
| **Create Narrative-Driven Content to Clarify Fee Implications** | High | tommy-clark |
| Develop founder-led content using "How I" or "Stop doing X" narratives to explain the real-world impact of the variable fee structure, especially the higher costs for "50/50" event contracts. This translates complex formulas into tactical, relatable P&L insights. |
| **Position API Tiers as a Strategic Tool, Not a Cost** | High | lulu-cheng-meservey |
| Frame the volume-gated API tiers as an exclusive benefit for serious traders. Advise new users to start with free public endpoints and optimize their strategy to "earn" higher-tier access, treating API usage as an infrastructure cost to be managed efficiently. |
| **Proactively Educate Users on Avoiding Transaction Fees** | High | tommy-clark |
| Create direct, actionable communications (e.g., "Stop losing 2% on every deposit") that guide users to fee-free ACH and wire transfer options, framing cost control as a mark of a savvy trader. |

## Conflicts & Minority Report
There are no direct factual conflicts between the agents. Both present the same fee structures and API access rules.

However, both agents submit a critical minority report on the *implications* of this structure:

*   **Complexity Can Be Perceived as Opacity:** While the fee schedule is mathematically transparent, its complexity can be a significant point of friction. For retail traders accustomed to flat fees, the `P * (1-P)` formula can feel opaque and unpredictable, potentially creating a "hidden cost" narrative if not communicated effectively.
*   **Underestimated Hedging Costs:** The fee skew means that hedging uncertain "50/50" events is more expensive than users might anticipate. This can erode small gains and significantly impact the profitability of certain strategies.
*   **API Volume as a Barrier:** The high volume thresholds for Premier/Prime API access act as a significant barrier to entry for smaller firms or individual algorithmic traders, making high-frequency capabilities effectively "expensive" despite the lack of a direct subscription fee.

## Next Steps
1.  **Develop Content:** Draft a "How I" blog post or video from a founder's perspective, modeling the true fee impact on a real-world hedging scenario involving a contract priced near 50¢.
2.  **Update Onboarding:** Add a clear, concise module to the user onboarding flow that visually compares deposit/withdrawal methods, highlighting the 2% debit card fee versus the free ACH/wire options.
3.  **Review API Documentation:** Enhance the API documentation with a "Strategy Guide" section that advises on leveraging public endpoints first and outlines a path to achieving the volume required for higher tiers.

## Provenance
| Section | Primary Contributors |
|---------|---------------------|
| **Unanimous Agreements** | lulu-cheng-meservey, tommy-clark |
| **Key Recommendations** | lulu-cheng-meservey, tommy-clark |
| **Conflicts & Minority Report** | lulu-cheng-meservey, tommy-clark |

---

# Challenge Round Results

## Conflicts Identified: 1

The initial synthesis correctly noted no direct factual conflicts. However, a meaningful strategic conflict exists in *how to communicate the platform's complex and potentially negative aspects* to users. The agents' recommendations reveal a fundamental disagreement in communication philosophy.

### Conflict 1: Optimal Communication Strategy for Complex Platform Rules
- **Position A (Tommy-Clark):** Radical Transparency and User Advocacy. This approach prioritizes building trust by directly and proactively educating users about potential cost pitfalls. Recommendations like "Stop losing 2% on every deposit" and creating content on the "real-world impact" of high fees on 50/50 contracts tackle the "opacity" concern head-on.
  - **Strongest Argument:** In finance, trust is the primary currency. By acting as a user's advocate and transparently highlighting potentially costly aspects of the platform, Kalshi can build long-term loyalty and differentiate itself from platforms that obscure their fee structures. This approach turns a potential liability into a trust-building asset.

- **Position B (Lulu-Cheng-Meservey):** Aspirational Framing and Exclusivity. This approach focuses on managing perception by framing a potential negative (volume-gated API access) as a positive. The recommendation to "Position API tiers as a strategic tool" and an "exclusive benefit" for serious traders aims to turn a barrier into a desirable status symbol, gamifying platform engagement for high-value users.
  - **Strongest Argument:** This strategy effectively targets and motivates the most sophisticated and potentially highest-volume traders. By creating an aspirational path, it encourages the exact behavior (higher trading volume) that benefits the exchange, cultivating a core user base of dedicated, high-performance participants.

- **Verdict:** **Both positions are valid but should be applied to different domains.** There is no single correct strategy; the optimal approach is a hybrid.

  1.  **Tommy-Clark's transparency-first approach is superior for universal cost elements.** Trading fees and deposit fees affect every user's bottom line. Applying radical transparency here is essential for building baseline trust and preventing users from feeling misled.
  2.  **Lulu-Cheng-Meservey's aspirational framing is superior for niche, high-end features.** The tiered API is not relevant to the average retail user. For the target audience of algorithmic traders, framing access as an "earned" competitive advantage is a powerful motivator that aligns perfectly with their goals.

  The resolution is to apply transparency to the universal and aspirational framing to the exclusive.

## Strengthened Conclusions
This challenge round confirmed that all factual findings in the initial synthesis are robust and undisputed. The primary value-add was surfacing a subtle but critical tension in communication strategy. The final, strengthened conclusion is that a one-size-fits-all communication strategy is insufficient; Kalshi must segment its approach, using radical transparency for universal cost structures and aspirational framing for advanced, performance-gated features.

## Revised Confidence
**Increased.** Confidence in the factual accuracy of the synthesis was already high and remains so. Confidence in the strategic recommendations has increased significantly because the challenge round forced a resolution between two competing communication philosophies, resulting in a more nuanced, targeted, and effective plan that addresses different user segments appropriately.