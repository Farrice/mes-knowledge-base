---
description: Spy on Amazon Best Sellers to find underserved
---

1. Ask the user for the **Category** or **Type** they want to investigate (e.g., "Non-fiction books", "Pet Supplies").

2. **Pull structured Amazon data via Apify** (PRIMARY — replaces fragile SERP scraping):

   ```bash
   python execution/apify_client.py amazon "[Category]" --limit 50
   ```

   This returns full structured product data: title, price, rating, review count, image URL, sales rank, description. Far richer than parsing `site:amazon.com` SERP results.

   **Fallback Contract**: If response contains `{"fallback": true}`, Apify cap is hit. Reroute to:
   - `search_web` with query: `site:amazon.com "Best Sellers" [Category]`
   - OR `perplexity_ask`: "List the top 20 Amazon Best Sellers in [Category] with their ratings, review counts, and any quality issues."

3. Specifically look for **"Profit Anomalies"** in the structured data:
   - **High Rank, Low Quality**: Products with high sales rank (#1-#5000) but:
     - Ugly/Unprofessional cover images (visible in `image_url` field)
     - Low review counts (`review_count < 50`)
     - Bad descriptions (short, keyword-stuffed)
     - Mediocre ratings (`rating < 4.0` despite high rank)
   - **Keyword Stuffing**: Titles that are clearly keyword-stuffed (indicates high demand, low brand loyalty).

4. Return a **"Profit Alert"** table:
   - **Sub-Niche**: (e.g., "Mushroom Foraging Logs")
   - **Observation**: "Top seller has 3 stars and a blurry cover. 47 reviews, ranked #2,300."
   - **Opportunity**: "Create a premium, well-designed version to capture this demand."
   - **Source URL**: Direct Amazon link from the scrape.
