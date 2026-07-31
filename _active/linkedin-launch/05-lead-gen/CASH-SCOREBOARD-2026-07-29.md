---
status: canonical
---

# Cash Scoreboard — Angle Map Validation

## Definitions

- **Sent:** a qualified, personalized message reaches a real authorized buyer or credible route to that buyer.
- **Held:** a qualified two-way sales conversation happens by message, phone, or video.
- **Sold:** the buyer explicitly accepts the scoped paid offer.
- **Collected:** cleared payment is received.
- **Price quoted:** the exact $750 price is stated to a qualified buyer.

Do not count drafts, connection requests without a message, likes, comments, profile views, compliments, free teardowns, or payment promises.

## Daily log

Day 1 begins when the first five qualified messages are sent.

| Selling day | Calendar date | New sent | Follow-ups sent | Held | Price quoted | Angle Maps sold | Sprints sold | Collected | Notes / next correction |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | — | 0 | 0 | 0 | 0 | 0 | 0 | $0 | Clock not started |
| 2 | — | 0 | 0 | 0 | 0 | 0 | 0 | $0 | |
| 3 | — | 0 | 0 | 0 | 0 | 0 | 0 | $0 | |
| 4 | — | 0 | 0 | 0 | 0 | 0 | 0 | $0 | |
| 5 | — | 0 | 0 | 0 | 0 | 0 | 0 | $0 | 50-send diagnosis applies once reached |
| 6 | — | 0 | 0 | 0 | 0 | 0 | 0 | $0 | |
| 7 | — | 0 | 0 | 0 | 0 | 0 | 0 | $0 | |
| 8 | — | 0 | 0 | 0 | 0 | 0 | 0 | $0 | |
| 9 | — | 0 | 0 | 0 | 0 | 0 | 0 | $0 | |
| 10 | — | 0 | 0 | 0 | 0 | 0 | 0 | $0 | Close deadline |
| 11 | — | 0 | 0 | 0 | 0 | 0 | 0 | $0 | Delivery/proof window |
| 12 | — | 0 | 0 | 0 | 0 | 0 | 0 | $0 | |
| 13 | — | 0 | 0 | 0 | 0 | 0 | 0 | $0 | |
| 14 | — | 0 | 0 | 0 | 0 | 0 | 0 | $0 | Final verdict |
| **Total** |  | **0** | **0** | **0** | **0** | **0** | **0** | **$0** | |

## Gate ledger

| Gate | Trigger | Current state | Decision |
|---|---|---|---|
| Opener/list gate | 50 well-targeted sends, zero replies | Not reached | No inference |
| Reach gate | Roughly 100 sends, fewer than five held | Not reached | No inference |
| Seller gate | Qualified conversations but no prices quoted | Not reached | No inference |
| Offer kill gate | 20 qualified conversations, price quoted, zero sales | Not reached | No inference |
| Initial evidence | One Angle Map sold and $750 collected | Not reached | Unconfirmed exact-offer demand |
| Repeatability | Two Angle Maps plus one Sprint conversion in 30 days | Not reached | No 90-day commitment yet |

## Payment ledger

| Buyer / brand | Offer | Amount sold | Date sold | Amount collected | Date cleared | Delivery due | Proof permission |
|---|---|---:|---|---:|---|---|---|
| — | — | $0 | — | $0 | — | — | — |

## System logging

Use the workspace revenue tracker only after cleared payment. The tracker was built for outcomes, not 150 individual outreach events, and repeated commands can create duplicate records. Keep sends, replies, held conversations, and sold-but-unpaid states in this scoreboard and `pipeline.md`.

Before logging, construct a unique identifier and verify that it is unused:

```bash
jq -e --arg id 'ANGLEMAP|YYYY-MM-DD|brand-slug|buyer-slug|collected' \
  'all(.outcomes[]; .deliverable != $id)' \
  .agent/revenue-outcomes.json
```

If that check fails, do not run the log command again. After the funds are cleared:

```bash
.venv/bin/python execution/revenue_tracker.py log \
  'ANGLEMAP|YYYY-MM-DD|brand-slug|buyer-slug|collected' \
  --revenue 750 \
  --type collected \
  --client 'Brand / Buyer' \
  --expert 'Farrice Cain' \
  --skill 'linkedin-launch/02-offer' \
  --outcome 'offer=angle-map; currency=USD; funds_cleared=yes; processor=<provider>; transaction_ref=<non-secret-reference>'
```

Until the first payment exists, the truthful cash state is **$0 collected and exact-offer demand unconfirmed**.
