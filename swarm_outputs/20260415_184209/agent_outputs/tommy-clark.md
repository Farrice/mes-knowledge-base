# tommy-clark ✅

**Status:** success
**Model:** gemini-2.5-flash
**Tokens:** 6,779
**Cost:** $0.0023
**Duration:** 13.7s
**Thinking Tokens:** 1,715
**Grounding Queries:** 1

---

**SUMMARY**
The Odds API currently offers five distinct pricing tiers, ranging from a free Starter plan to a high-volume 15M plan, with monthly costs up to $249. The pricing model is credit-based, but a crucial nuance is that "credits" do not directly equate to API requests; consumption varies significantly based on the number of markets and regions queried per call.

**KEY FINDINGS**
*   The Odds API provides five main subscription tiers: Starter (Free), 20K, 100K, 5M, and 15M.
*   Monthly prices for paid plans are $30 for 20K credits, $59 for 100K credits, $119 for 5M credits, and $249 for 15M credits. The free Starter plan includes 500 credits per month.
*   A critical detail for users is that one API call can consume varying amounts of credits (from 1 to dozens) depending on the number of markets and regions requested, and historical data queries incur a 10x credit cost.

**RECOMMENDATIONS**
*   **Decouple "Credits" from "Requests" in Your Evaluation**: As a founder, you *must* go beyond the headline credit numbers. Don't just see "20,000 credits" and assume 20,000 calls. Model your projected usage based on *actual market and region combinations* you intend to query, and factor in the 10x multiplier for historical data. This is the messy reality of API consumption; don't get caught by vanity metrics.
*   **Pilot with the Free Tier to Establish "Gravedigger Details"**: Before committing to a paid plan, leverage the "Starter" (Free) tier. Use this period to rigorously test your anticipated query patterns and precisely calculate your true credit burn rate. This "How I" experience will give you the specific, lived data points to understand the real cost, rather than relying on general estimates.
*   **Consider the "Build vs. Buy" Narrative with Competitors**: The existence of alternative APIs (like OddsPapi or ParlayAPI) with different credit/request models presents an opportunity. As a founder building a product relying on this data, you should internally construct a "How I evaluated API providers and chose X due to Y specific cost-efficiency for *our* use case" narrative. This deep dive into the credit system (e.g., OddsPapi's flat per-request pricing vs. The Odds API's variable credit cost) is crucial for justifying your tech stack and can even become a powerful internal or external content piece.

**CONFIDENCE**: High

**DISSENT**:
While the pricing tiers are clearly stated, the "credit" system introduces a significant layer of complexity that can lead to unexpected costs if not thoroughly understood. The direct comparison of "credits" across different APIs is misleading, as one API's credit might represent a vastly different amount of data or number of calls than another's. Founders need to be acutely aware of this nuance.
