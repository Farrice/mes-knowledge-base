---
description: Spy on Amazon Best Sellers to find underserved niches (KDP/Products).
---

1. Ask the user for the **Category** or **Type** they want to investigate (e.g., "Non-fiction books", "Pet Supplies").

2. Perform a "Market Infiltration" search using `search_web`:
   - Target Domain: `amazon.com`
   - Query: `site:amazon.com "Best Sellers" [Category]`

3. specific look for **"Profit Anomalies"**:
   - **High Rank, Low Quality**: Products with high sales rank (#1-#5000) but:
     - Ugly/Unprofessional Covers/Images.
     - Low Review Counts (< 50 reviews).
     - Bad Descriptions.
   - **Keyword Stuffing**: Titles that are clearly keyword-stuffed (indicates high demand, low brand loyalty).

4. Return a **"Profit Alert"** table:
   - **Sub-Niche**: (e.g., "Mushroom Foraging Logs")
   - **Observation**: "Top seller has 3 stars and a blurry cover."
   - **Opportunity**: "Create a premium, well-designed version to capture this demand."
