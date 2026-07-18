# Workflow 04: Retail Channel Pathfinder

Use this when choosing between DTC, TikTok, Amazon, direct retail, DSD, wholesale, or partner-led distribution.

## Inputs

- Product/category.
- Current demand source.
- Unit economics and margin target.
- Channel access.
- Store execution requirements.
- Buyer or partner constraints.

## Steps

1. Identify the current demand engine.
2. Map channel sequence: TikTok/influencer, DTC, Amazon, direct retail, DSD, or other.
3. Score each channel for demand creation, margin, execution incentives, lag time, and brand fit.
4. Identify buyer-request risk.
5. Define what must be true before expanding to the next channel.

## Output Schema

- Channel sequence: the ordered path (e.g., TikTok -> Amazon -> retail), not an unordered list of channels.
- Incentive map: each channel scored on demand creation, margin, execution incentives, lag time, and brand fit — five scores per channel.
- Retail lag map: for any channel with retail/wholesale exposure, what is already loaded vs. what shows up in current revenue.
- Buyer-risk notes: named per channel involving a retail buyer, or explicitly marked N/A.
- Next channel test: one falsifiable trigger that must be true before expansion.

## Quality Gate

- Does the channel sequence reflect a real demand path, not a wishlist of channels chosen by prestige or competitor mimicry?
- Is every channel scored on all five dimensions (demand creation, margin, execution incentives, lag time, brand fit) — is a channel missing a score treated as an incomplete map, not skipped silently?
- Is buyer-request risk named for every channel involving a retail buyer, or explicitly marked N/A?
- Is the "next channel test" a single falsifiable trigger, not a general growth goal like "keep scaling"?
- Does the map distinguish direct retail placement from actual store-level sell-through (shelf access is not execution)?
