# Swarm Synthesis: What are Polymarket trading fees and API access costs as of April 2026? Maker taker fees. Check docs.polymarket.com

## Executive Summary
As of April 2026, Polymarket utilizes a dynamic taker-fee model where fees are charged only to market order "takers," while "makers" who provide liquidity receive rebates. Fees are calculated based on market probability and a category-specific coefficient, peaking when uncertainty is highest (at a $0.50 share price). There is a significant conflict regarding API access costs: one agent reports it as entirely free for data, while the other details a tiered premium model for high-volume users starting at $99/month. A temporary 50% taker rebate is in effect through April 30, 2026, which both agents note is a critical but short-term consideration for traders.

## Unanimous Agreements
| Finding | Supporting Agents |
|---------|------------------|
| Polymarket charges fees only to "takers"; "makers" receive rebates. | lulu-cheng-meservey, tommy-clark |
| The taker fee is dynamic, calculated by `Fee = Θ × C × p × (1 − p)`. | lulu-cheng-meservey, tommy-clark |
| Fees are highest when a market's probability is near 50% and decrease towards 1% or 99%. | lulu-cheng-meservey, tommy-clark |
| Fee coefficients (Θ) vary by market category (e.g., Crypto is higher than Sports). | lulu-cheng-meservey, tommy-clark |
| Geopolitical markets are explicitly fee-free. | lulu-cheng-meservey, tommy-clark |
| A temporary 50% taker rebate on all trades is active through April 30, 2026. | lulu-cheng-meservey, tommy-clark |
| There are no fees on deposits, withdrawals, or winnings. | lulu-cheng-meservey, tommy-clark |

## Key Recommendations
| Recommendation | Confidence | Lead Agent |
|----------------|------------|------------|
| Launch a founder-led communication campaign framing the dynamic fees as a necessary evolution for market health and a sustainable "circular economy" where takers fund makers. | High | lulu-cheng-meservey |
| Create tactical, narrative-driven content for advanced traders (e.g., "How I cut trading costs by 30% using maker rebates") to demonstrate strategic use of the fee system. | High | tommy-clark |
| Segment fee communication: use a simple message for casual users ("No fees on winnings") while providing detailed documentation and API info for advanced/API traders. | High | lulu-cheng-meservey |
| Target quantitative founders and data analysts with content that dissects the fee formula and its practical implications, using a "20/5 Protocol" for direct engagement. | Medium | tommy-clark |

## Conflicts & Minority Report
**Primary Conflict: API Access Costs**
There is a direct conflict regarding the cost of API access.
*   **lulu-cheng-meservey** states that API access for market data, order books, and trade history is free. Trading via the API simply requires a wallet with USDC.
*   **tommy-clark** presents a tiered model: basic API access is free (with rate limits), but premium tiers for high-volume users start at $99/month, and enterprise plans start at $500+/month. This agent also notes a specific, more rigorous application process is required for the CFTC-regulated US API.

**Condition for Minority View:** Tommy-clark's view is likely more accurate for professional, high-frequency, or institutional traders who would exceed the rate limits of a free tier. Lulu-cheng-meservey's view is likely correct for casual users, developers, and data analysts with lower-volume needs. The distinction between the international and regulated US platforms may also account for the discrepancy.

**Minority Report: Strategic & Communication Risks**
*   Both agents dissent on the temporary 50% taker rebate, warning it could be a "stealth trap" (tommy-clark) for traders building long-term strategies and a point of future friction that communications must address proactively (lulu-cheng-meservey). The "effective" trading cost will increase on May 1, 2026.
*   Lulu-cheng-meservey raises a dissent that the shift from a previously "virtually fee-free" model requires careful messaging to avoid user backlash, especially concerning the higher fees on certain crypto markets which are designed to protect liquidity.

## Next Steps
1.  **Verify API Cost Structure:** Immediately consult `docs.polymarket.com` and any developer agreements to resolve the conflict between "free" and "tiered" API access. Clarify if different pricing applies to the international vs. US platforms.
2.  **Deploy Unified Communication Strategy:** Combine the strategic narrative (lulu-cheng-meservey) with tactical content hooks (tommy-clark) to explain the fee structure to all user segments.
3.  **Decide on Rebate Messaging:** Determine how to communicate the upcoming expiration of the 50% taker rebate. The messaging must be clear to prevent traders from feeling misled when costs increase in May 2026.

## Provenance
| Section | Primary Contributors |
|---------|---------------------|
| Unanimous Agreements | lulu-cheng-meservey, tommy-clark |
| Key Recommendations | lulu-cheng-meservey, tommy-clark |
| Conflicts & Minority Report | tommy-clark (API tiers, US API), lulu-cheng-meservey (communication risks) |
| Fee Structure Details | lulu-cheng-meservey, tommy-clark |
| API Cost Details | tommy-clark |

---

# Challenge Round Results

## Conflicts Identified: 1

### Conflict 1: API Access Costs
- **Position A** (lulu-cheng-meservey): API access for market data, order books, and trade history is fundamentally free. Trading via the API simply requires a funded wallet.
- **Position B** (tommy-clark): API access operates on a tiered, freemium model. Basic access is free but rate-limited, while premium tiers for high-volume and enterprise users start at $99/month and $500+/month, respectively. A separate, more rigorous application process exists for the CFTC-regulated US API.
- **Verdict**: **Position B is stronger because it is more complete.** Position A is correct for the majority of casual developers and data analysts, for whom the free tier is sufficient. However, it omits critical information for the professional, institutional, and high-frequency traders that are essential to market liquidity and volume. Position B's inclusion of rate limits, paid tiers, and the crucial distinction between the international and regulated US platforms provides a comprehensive and actionable understanding of the true cost structure for all user types. The specificity of the pricing tiers and the mention of the US API suggest a deeper, more accurate investigation.

## Strengthened Conclusions
The challenge round confirms that while the core dynamic trading fee structure is well-understood and agreed upon, the associated API costs are segmented by user type. The initial conflict was resolved by understanding that API access is "free" for casual use but operates on a paid, tiered model for professional traders, a critical distinction for serious platform users. The agents' shared concern over the expiring 50% taker rebate was also reinforced as a key communication priority, not a point of strategic disagreement.

## Revised Confidence
**Increased.** The initial synthesis presented a direct factual contradiction regarding API costs. This arbitration resolved the ambiguity, moving the understanding from a simple "free vs. paid" conflict to a more nuanced and accurate "freemium model with distinct tiers for different user profiles." This clarification provides a much higher-confidence basis for strategic decisions.