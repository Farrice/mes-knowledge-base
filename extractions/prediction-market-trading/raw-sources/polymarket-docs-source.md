# Polymarket Official Documentation — Raw Source Material
## Fetched: 2026-04-13
## Purpose: MES 3.0 knowledge extraction — prediction market trading infrastructure

---

### Page: https://docs.polymarket.com/ (Main Documentation Landing)

**Overview**: "Build on the world's largest prediction market. Trade, integrate, and access real-time market data with the Polymarket API."

**Developer Quickstart**: Make your first API request in minutes. Learn the basics of the Polymarket platform, fetch market data, place orders, and redeem winning positions.

**Core Documentation Cards**:
- Quickstart: Set up environment and make first API call
- Core Concepts: Understand markets, events, tokens, trading mechanics
- API Reference: Explore REST endpoints, WebSocket streams, authentication
- SDKs: Official Python, TypeScript, and Rust libraries

**Code Examples**:

TypeScript:
```typescript
import { ClobClient, Side } from "@polymarket/clob-client";
const client = new ClobClient(host, chainId, signer, creds);
const order = await client.createAndPostOrder(
  { tokenID, price: 0.50, size: 10, side: Side.BUY },
  { tickSize: "0.01", negRisk: false }
);
```

Python:
```python
from py_clob_client.client import ClobClient
from py_clob_client.order_builder.constants import BUY
client = ClobClient(host, key=key, chain_id=chain_id, creds=creds)
order = client.create_and_post_order(
    OrderArgs(token_id=token_id, price=0.50, size=10, side=BUY),
    options={"tick_size": "0.01", "neg_risk": False}
)
```

Rust:
```rust
use polymarket_client_sdk::clob::{Client, Config};
use polymarket_client_sdk::clob::types::Side;
use polymarket_client_sdk::types::dec;
let client = Client::new(host, Config::default())?.authentication_builder(&signer).authenticate().await?;
let order = client.limit_order().token_id(token_id).price(dec!(0.50)).size(dec!(10)).side(Side::Buy).build().await?;
let signed = client.sign(&signer, order).await?;
let response = client.post_order(signed).await?;
```

**Support Resources**:
- Builder Program: https://builders.polymarket.com — "Build apps on Polymarket and earn rewards for driving volume"
- Help Desk: https://help.polymarket.com
- Status: https://status.polymarket.com
- US Documentation: https://docs.polymarket.us

---

### Page: https://docs.polymarket.com/llms.txt (Full Documentation Index)

**Complete page listing with OpenAPI specs**:

**OpenAPI Specs** (machine-readable API definitions):
- bridge-openapi: https://docs.polymarket.com/api-spec/bridge-openapi.yaml
- gamma-openapi: https://docs.polymarket.com/api-spec/gamma-openapi.yaml
- clob-openapi: https://docs.polymarket.com/api-spec/clob-openapi.yaml
- data-openapi: https://docs.polymarket.com/api-spec/data-openapi.yaml
- relayer-openapi: https://docs.polymarket.com/api-spec/relayer-openapi.yaml
- data-api-openapi: https://docs.polymarket.com/api-reference/data-api-openapi.yaml
- bridge-api-openapi: https://docs.polymarket.com/api-reference/bridge-api-openapi.yaml
- openapi (full): https://docs.polymarket.com/api-reference/openapi.json

**AsyncAPI Specs** (WebSocket definitions):
- asyncapi (market): https://docs.polymarket.com/asyncapi.json
- asyncapi-user: https://docs.polymarket.com/asyncapi-user.json
- asyncapi-sports: https://docs.polymarket.com/asyncapi-sports.json

---

### Page: https://docs.polymarket.com/api-reference/introduction (API Architecture)

The platform operates **three primary APIs**:

1. **Gamma API** (`https://gamma-api.polymarket.com`)
   - Markets, events, tags, series, comments, sports, search, and public profiles
   - Main interface for discovering and browsing market information
   - No authentication required

2. **Data API** (`https://data-api.polymarket.com`)
   - User positions, trades, activity, holder data, open interest, leaderboards, and builder analytics
   - No authentication required

3. **CLOB API** (`https://clob.polymarket.com`)
   - Orderbook data, pricing, midpoints, spreads, and price history
   - Order operations and trading functions
   - Public endpoints for market data; restricted endpoints for trading require authentication

4. **Bridge API** (`https://bridge.polymarket.com`)
   - Financial transactions — proxy for fun.xyz
   - Not directly operated by Polymarket

---

### Page: https://docs.polymarket.com/trading/overview (Trading System Architecture)

**Hybrid-Decentralized Trading System**: Combines "offchain order matching with onchain settlement via the Exchange contract." The system is non-custodial, with orders represented as EIP-712 signed messages that settle atomically on Polygon. "The operator cannot set prices or execute unauthorized trades — users can always cancel orders onchain independently."

**SDK Clients**:
- TypeScript: `npm install @polymarket/clob-client`
- Python: `pip install py-clob-client`
- Rust: `cargo add polymarket-client-sdk`

Direct REST API usage is possible but requires manual implementation of EIP-712 order signing and HMAC authentication headers.

**Two-Level Authentication Framework**:

| Level | Method | Purpose |
|-------|--------|---------|
| L1 | EIP-712 signature (private key) | Create/derive API credentials |
| L2 | HMAC-SHA256 (API credentials) | Place orders, cancel, query trades |

Users derive L2 credentials (API key, secret, passphrase) once using their private key, then use these for all subsequent trading requests.

**Signature Types & Wallet Configuration**:

| Type | ID | Use Case | Funder |
|------|----|----|--------|
| EOA | 0 | Standalone wallets | Your EOA address |
| POLY_PROXY | 1 | Magic Link accounts | Your proxy wallet |
| GNOSIS_SAFE | 2 | Browser/embedded wallets | Your proxy wallet |

**REST API Headers Required**:

L1 Headers (credential derivation): `POLY_ADDRESS`, `POLY_SIGNATURE`, `POLY_TIMESTAMP`, `POLY_NONCE`

L2 Headers (trading operations): `POLY_ADDRESS`, `POLY_SIGNATURE`, `POLY_TIMESTAMP`, `POLY_API_KEY`, `POLY_PASSPHRASE`

Note: "Even with L2 authentication, methods that create orders still require the user's private key for EIP-712 order payload signing."

---

### Page: https://docs.polymarket.com/api-reference/authentication (Authentication Details)

**Two-Tier Authentication**:

1. **L1 (Private Key)**: Uses wallet's private key to sign EIP-712 messages. Proves ownership while keeping the private key under user control. Used for creating API credentials and signing orders locally.

2. **L2 (API Key)**: Uses credentials generated from L1 authentication (apiKey, secret, passphrase). Employs HMAC-SHA256 signing for API requests to cancel orders, check balances, and post signed orders.

**Public vs. Protected Endpoints**: The Gamma API, Data API, and CLOB read endpoints (orderbook, prices, spreads) require no authentication. Protected endpoints handle trading operations and require all five POLY_* L2 HTTP headers.

**Obtaining API Credentials** via SDK:
```typescript
const credentials = await client.createOrDeriveApiKey();
// Returns: { apiKey, secret, passphrase }
```

REST API endpoints:
- `POST https://clob.polymarket.com/auth/api-key` (create)
- `GET https://clob.polymarket.com/auth/derive-api-key` (derive)

Both require L1 headers: `POLY_ADDRESS`, `POLY_SIGNATURE`, `POLY_TIMESTAMP`, `POLY_NONCE`

**L2 Authentication Headers** (all trading requests):
- `POLY_ADDRESS` (signer address)
- `POLY_SIGNATURE` (HMAC-SHA256)
- `POLY_TIMESTAMP` (UNIX timestamp)
- `POLY_API_KEY`
- `POLY_PASSPHRASE`

**Signature Types**:
- EOA (0): Standard Ethereum wallets requiring POL for gas
- POLY_PROXY (1): Custom proxy for Magic Link users
- GNOSIS_SAFE (2): Multisig proxy wallets (most common)

---

### Page: https://docs.polymarket.com/trading/fees (Fee Structure)

**Core Fee Formula**: `fee = C * feeRate * p * (1 - p)`

Where:
- C = shares traded
- p = share price
- feeRate = market-specific fee rate

**Key Characteristics**:
- "Makers are never charged fees. Only takers pay fees."
- Fees vary by market category:
  - Sports: 0.03
  - Crypto: 0.072
  - Geopolitical and world events: completely exempt (0)
- Peak fees occur at 50% probability and decrease symmetrically toward both extremes
- Example: 100-share Crypto trade at $0.50 = $1.80 fee

**SDK Integration**: "Official CLOB clients automatically handle fees for you — they fetch the fee rate and include it in the signed order payload."

**REST API**: Must manually fetch fees via `/fee-rate` endpoint and include `feeRateBps` field before signing orders.

**Rebate Program**: Collected fees "fund the Maker Rebates Program, which redistributes fees daily to market makers to incentivize deeper liquidity and tighter spreads."

---

### Page: https://docs.polymarket.com/api-reference/rate-limits (Rate Limits)

**Rate Limiting**: Cloudflare's throttling system — requests are queued rather than rejected when exceeded.

**General Endpoints**: 15,000 requests per 10 seconds

**Gamma API** (`https://gamma-api.polymarket.com`):
- General: 4,000 req/10s
- `/events`: 500 req/10s
- `/markets`: 300 req/10s
- `/markets` + `/events` listing: 900 req/10s
- `/comments`: 200 req/10s
- `/tags`: 200 req/10s
- `/public-search`: 350 req/10s

**Data API** (`https://data-api.polymarket.com`):
- General: 1,000 req/10s
- `/trades`: 200 req/10s
- `/positions`: 150 req/10s
- `/closed-positions`: 150 req/10s

**CLOB API** (`https://clob.polymarket.com`):

General:
- General: 9,000 req/10s
- GET balance allowance: 200 req/10s
- UPDATE balance allowance: 50 req/10s

Market Data:
- `/book`, `/price`, `/midpoint`: 1,500 req/10s each
- `/books`, `/prices`, `/midpoints`: 500 req/10s each
- `/prices-history`: 1,000 req/10s
- Market tick size: 200 req/10s

Ledger:
- `/trades`, `/orders`, `/notifications`, `/order`: 900 req/10s
- `/data/orders` and `/data/trades`: 500 req/10s each
- `/notifications`: 125 req/10s

Authentication:
- API key endpoints: 100 req/10s

Trading (Burst/Sustained):
- `POST /order`: 3,500/10s | 36,000/10min
- `DELETE /order`: 3,000/10s | 30,000/10min
- `POST /orders`: 1,000/10s | 15,000/10min
- `DELETE /orders`: 1,000/10s | 15,000/10min
- `DELETE /cancel-all`: 250/10s | 6,000/10min
- `DELETE /cancel-market-orders`: 1,000/10s | 1,500/10min

Other:
- Relayer `/submit`: 25 req/1 min
- User PNL API: 200 req/10s

---

### Page: https://docs.polymarket.com/concepts/order-lifecycle (Order Lifecycle)

**Core Concept**: Orders follow a hybrid model: "offchain creation and matching with onchain settlement through smart contracts."

**All orders are limit orders.** "Market orders" are limit orders with a price set to execute immediately.

**Order Types**:

| Type | Definition |
|------|-----------|
| GTC | Good Till Cancelled — rests on book until filled or cancelled |
| GTD | Good Till Date — auto-expires at specified time |
| FOK | Fill Or Kill — fill entirely or cancel immediately |
| FAK | Fill And Kill — fill what's available, cancel the rest |

**Post-Only Orders**: "Will only rest on the book. If a post-only order would match immediately (cross the spread), it's rejected."

**Five-Step Order Lifecycle**:

1. **Create & Sign**: Order object contains token ID, side, price, size, expiration, and nonce. Signed with private key via EIP712.
2. **Submit to CLOB**: Operator validates signature, balance, allowances, and tick size requirements.
3. **Match or Rest**: Marketable orders (buy price >= lowest ask OR sell price <= highest bid) match immediately. Non-marketable orders rest until matched, cancelled, or expired.
4. **Settlement**: "Exchange contract verifies both signatures, transfers tokens from seller to buyer, transfers USDC.e from buyer to seller" with atomic execution.
5. **Confirmation**: Trade achieves finality on Polygon and appears in history.

**Order Statuses**: `live` (resting), `matched` (filled immediately), `delayed` (marketable order with 1-second sports market delay), `unmatched` (marketable but failed to match)

**Trade Statuses (Post-Matching)**:

| Status | Terminal | Description |
|--------|----------|-------------|
| MATCHED | No | Trade matched, sent to executor for onchain submission |
| MINED | No | Transaction mined into the blockchain |
| CONFIRMED | Yes | Trade achieved finality, successful |
| RETRYING | No | Transaction failed, being retried |
| FAILED | Yes | Trade failed permanently |

**Maker vs. Taker**: Maker adds liquidity (order rests). Taker removes liquidity (matches immediately). "Price improvement always benefits the taker" with execution at the better resting price.

**Size Formula**: `maxOrderSize = balance - sum(openOrderSize - filledAmount)`

---

### Page: https://docs.polymarket.com/concepts/prices-orderbook (Prices & Orderbook)

**Price Range**: "Every share on Polymarket is priced between $0.00 and $1.00." Cost directly correlates to market sentiment on outcome likelihood.

**Display Price**: "The displayed price is the midpoint of the bid-ask spread. If the spread is wider than $0.10, the last traded price is shown instead."

**Order Book Structure**:
- Bids: "Buy orders — the highest prices traders are willing to pay"
- Asks: "Sell orders — the lowest prices traders are willing to accept"
- Spread: gap between highest bid and lowest ask; narrower = more liquid

**Order Types**:
- Market Orders: Execute immediately at available pricing
- Limit Orders: "Execute only at your specified price or better. Use when you want price control and are willing to wait."
- "All orders on Polymarket are technically limit orders. A 'market order' is simply a limit order priced to execute immediately."

**Price Discovery**: Initial market prices emerge when complementary limit orders match — e.g., $0.60 for Yes and $0.40 for No, totaling $1.00.

**Trading Constraints**: "Polymarket's orderbook has no trading size limits" though substantial orders may significantly impact pricing.

---

### Page: https://docs.polymarket.com/trading/orders/create (Order Creation)

**Order Types**:
- GTC (Good-Til-Cancelled): Rests on book until filled or cancelled (default)
- GTD (Good-Til-Date): Active until specified expiration time
- FOK (Fill-Or-Kill): Must fill immediately and entirely, or cancel
- FAK (Fill-And-Kill): Fills what's available immediately, cancels the rest

**Creating Limit Orders**: SDK provides single-step (`createAndPostOrder()`) and two-step (`createOrder()` + `postOrder()`) approaches.

**Market Order Mechanics**: Amount parameter changes meaning by side:
- BUY: represents dollar amount to spend
- SELL: represents number of shares to sell
- `price` field functions as "a worst-price limit (slippage protection), not a target execution price."

**GTD Order Requirements**: "A security threshold of one minute on GTD expiration." To achieve N-second effective lifetime: `expiration = now + 60 + N`

**Post-Only Orders**: "Guarantee you're always the maker" by rejecting orders that would cross the spread. Work exclusively with GTC/GTD types.

**Batch Operations**: Up to 15 orders in a single request via `postOrders()`.

**Market-Specific Options**:
- tickSize: Market's precision level (0.1, 0.01, 0.001, or 0.0001)
- negRisk: Boolean flag for multi-outcome conditional token markets

**Prerequisites & Validation**:
- USDC.e allowance >= spending amount (buy orders)
- Conditional token allowance >= selling amount (sell orders)
- Price conforms to market tick size
- Sufficient balance accounting for reserved amounts from open orders

**Session Management**: "If a valid heartbeat is not received within 10 seconds (with a 5-second buffer), all open orders are cancelled." Send heartbeats every 5 seconds using the most recent heartbeat_id.

**Response Statuses**: `live` (resting), `matched` (filled immediately), `delayed` (marketable order subject to matching delay), `unmatched` (marketable but failed to match)

---

### Page: https://docs.polymarket.com/trading/orderbook (Orderbook)

**Core Endpoints**: Public orderbook access via SDKs and REST API at `https://clob.polymarket.com`. No authentication required.

**Key Data Retrieval Methods**:
- Orderbook Snapshot: Complete bid/ask levels with tick size and minimum order size
- `getPrice()`: Best bid/ask
- `getMidpoint()`: Average (displayed as implied probability)
- `getSpread()`: Bid-ask width
- Historical Data: Intervals 1h, 6h, 1d, 1w, 1m, max; or custom timestamp ranges

**Market Order Estimation**: `calculateMarketPrice()` walks the orderbook to estimate slippage for a given order size.

**Batch Capabilities**: All single-token queries support batch variants handling up to 500 tokens simultaneously via POST requests.

**Real-Time Updates**: WebSocket at `wss://ws-subscriptions-clob.polymarket.com/ws/market` with live orderbook snapshots, price changes, trade executions, and market lifecycle events.

---

### Page: https://docs.polymarket.com/trading/matching-engine (Matching Engine)

**Schedule**: Weekly restarts on Tuesdays at 7:00 AM ET, ~90 seconds downtime.

**During Restart**: Order matching pauses, API returns HTTP 425 status codes.

**Announcement Channels**: Telegram (Polymarket Trading APIs) and Discord (#trading-apis).

**Handling HTTP 425**:
1. Detect 425 response — signals temporary restart, not permanent failure
2. Implement exponential backoff — 1-2 second delays, doubling each retry
3. Resume operations when successful responses return

---

### Page: https://docs.polymarket.com/market-data/websocket/overview (WebSocket Overview)

**All WebSocket Endpoints**:

| Channel | Endpoint | Authentication |
|---------|----------|----------------|
| Market | `wss://ws-subscriptions-clob.polymarket.com/ws/market` | Not required |
| User | `wss://ws-subscriptions-clob.polymarket.com/ws/user` | Required |
| Sports | `wss://sports-api.polymarket.com/ws` | Not required |
| RTDS | `wss://ws-live-data.polymarket.com` | Optional |

**Message Types by Channel**:

Market Channel: `book` (orderbook snapshot), `price_change` (level updates), `tick_size_change`, `last_trade_price` (executions), `best_bid_ask` (requires custom_feature_enabled), `new_market` (custom), `market_resolved` (custom)

User Channel: `trade` (lifecycle updates from MATCHED to CONFIRMED), `order` (placements, updates, cancellations)

Sports Channel: `sport_result` (game scores, periods, status)

**Subscription Messages**:
- Market: assets_ids as string array, type identifier, optional custom_feature_enabled boolean
- User: API credentials object (apiKey, secret, passphrase) plus condition IDs (not asset IDs — each market has one condition ID but two asset IDs for Yes and No tokens)
- Sports: no subscription message required

**Heartbeat Protocol**:
- Market/User: Send `PING` every 10 seconds; server responds with `PONG`
- Sports: Server sends `ping` every 5 seconds; respond with `pong` within 10 seconds or connection closes

**Dynamic Operations**: Subscribe/unsubscribe with `"operation": "subscribe"` / `"operation": "unsubscribe"`

---

### Page: https://docs.polymarket.com/market-data/websocket/market-channel (Market Channel Detail)

**WebSocket URL**: `wss://ws-subscriptions-clob.polymarket.com/ws/market`

**Subscription Format**:
```json
{
  "assets_ids": ["<token_id_1>", "<token_id_2>"],
  "type": "market",
  "custom_feature_enabled": true
}
```

**Event Types**:
- `book`: Initial snapshot and post-trade updates with bid/ask levels
- `price_change`: Triggered by order placement/cancellation; includes side (BUY/SELL), best bid/ask
- `tick_size_change`: When minimum tick adjusts due to price extremes (>0.96 or <0.04)
- `last_trade_price`: Execution data when maker/taker match, including fee rates and trade size
- `best_bid_ask`: Best bid/ask price changes with spread (custom feature only)
- `new_market`: New market creation with metadata (custom feature only)
- `market_resolved`: Resolution notification with winning asset ID (custom feature only)

---

### Page: https://docs.polymarket.com/trading/ctf/overview (Conditional Token Framework)

**Overview**: Open standard by Gnosis creating ERC1155 tokens representing outcomes of prediction markets.

**Token Structure** (binary markets):
- Yes token: Redeems for $1.00 USDC.e when event occurs
- No token: Redeems for $1.00 USDC.e when event doesn't occur
- "Always fully collateralized — every Yes/No pair is backed by exactly $1.00 USDC.e locked in the CTF contract."

**Three Core Operations**:
- Split: Convert USDC.e into Yes + No token pairs
- Merge: Convert Yes + No pairs back to USDC.e
- Redeem: Exchange winning tokens for USDC.e after resolution

**Token Identification Process**:
1. Condition ID: oracle address (UMA CTF Adapter) + questionId (UMA ancillary data hash) + outcomeSlotCount (always 2 for binary)
2. Collection IDs: parentCollectionId (always zero) + conditionId + indexSet (1 for first outcome, 2 for second)
3. Position IDs: collateralToken (USDC.e on Polygon) + collectionId

**Market Types**:
- Standard Markets: CTF Exchange, independent markets
- Neg Risk Markets: Neg Risk CTF Exchange, linked conversion operations

---

### Page: https://docs.polymarket.com/advanced/neg-risk (Negative Risk Markets)

**Core Mechanism**: Capital-efficient trading in multi-outcome events where only one outcome can win. "A No share in any market can be converted into 1 Yes share in every other market" through the Neg Risk Adapter contract.

**API Implementation**: Gamma API flags with `negRisk` boolean. Orders must explicitly set `negRisk: true`.

**Augmented Negative Risk**: Accommodates emerging outcomes post-launch through placeholder outcomes. Standard: `negRisk: true`. Augmented: `enableNegRisk: true` AND `negRiskAugmented: true`.

---

### Page: https://docs.polymarket.com/concepts/resolution (Market Resolution)

**UMA Optimistic Oracle**: Polymarket's resolution mechanism.

**Resolution Rules**: Each market has predefined rules specifying resolution source, end date, and edge cases. "The market title describes the question, but the rules define how it resolves."

**Three-Step Flow**:
1. **Proposal**: Anyone proposes outcome, posts $750 USDC.e bond
2. **Challenge Period**: 2-hour window for disputes via counter-bonds
   - No dispute: resolves in ~2 hours
   - One dispute: second proposal accepted
   - Two disputes: escalates to UMA token holder vote
3. **UMA Token Holder Voting** (~48 hours): Proposer victory, disputer victory, "Too Early", or "Unknown/50-50" ($0.50 per token)

**Timelines**: Undisputed ~2 hours; Disputed 4-6 days total.

**Post-Resolution**: Trading ceases immediately. Winning tokens redeemable via `redeemPositions` on CTF contract at 1:1.

---

### Page: https://docs.polymarket.com/resources/contract-addresses (Smart Contracts — Polygon Mainnet, Chain ID 137)

**Core Trading Contracts**:
- CTF Exchange: `0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E` — Standard market order matching and settlement
- Neg Risk CTF Exchange: `0xC5d563A36AE78145C45a50134d48A1215220f80a` — Order matching for neg risk markets
- Neg Risk Adapter: `0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296` — Converts No tokens between outcomes
- Conditional Tokens (CTF): `0x4D97DCd97eC945f40cF65F87097ACe5EA0476045` — ERC1155 token storage (split, merge, redeem)

**Token Contracts**:
- USDC.e (Bridged USDC): `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174` — Collateral token (6 decimals)

**Wallet Factory Contracts**:
- Gnosis Safe Factory: `0xaacfeea03eb1561c4e67d661e40682bd20e3541b`
- Polymarket Proxy Factory: `0xaB45c5A4B0c941a2F231C04C3f49182e1A254052`

**Resolution Contracts**:
- UMA Adapter: `0x6A9D222616C90FcA5754cd1333cFD9b7fb6a4F74` — Adapter to UMA Optimistic Oracle
- UMA Optimistic Oracle: `0xCB1822859cEF82Cd2Eb4E6276C7916e692995130` — Resolution proposals and disputes

**Liquidity**:
- Uniswap v3 USDC.e/USDC Pool: `0xd36ec33c8bed5a9f7b6630855f1533455b98a418`

---

### Page: https://docs.polymarket.com/resources/error-codes (Complete Error Reference)

**Global Errors (All Authenticated Endpoints)**:
- 401: Invalid API Key — missing, expired, or invalid auth headers
- 401: Invalid L1 Request Headers — HMAC signature malformed or mismatched
- 503: Trading Disabled — exchange temporarily paused
- 503: Cancel-Only Mode — new orders not accepted, cancels allowed
- 429: Too Many Requests — rate limit exceeded, exponential backoff required

**Order Placement (POST /order)**:
- "Invalid order payload" — malformed, missing fields, or invalid values
- "the order owner has to be the owner of the API KEY" — maker address mismatch
- "the order signer address has to be the address of the API KEY"
- "'{address}' address banned"
- "'{address}' address in closed only mode"

**Order Processing**:
- "invalid post-only order: order crosses book"
- "order {id} is invalid. Price ({price}) breaks minimum tick size rule: {tick}"
- "order {id} is invalid. Size ({size}) lower than the minimum: {min}"
- "order {id} is invalid. Duplicated."
- "order {id} crosses the book"
- "not enough balance / allowance"
- "invalid nonce"
- "invalid expiration"
- "order canceled in the CTF exchange contract"
- "order match delayed due to market conditions"
- "order couldn't be fully filled. FOK orders are fully filled or killed."
- "no orders found to match with FAK order."
- "the market is not yet ready to process new orders"

**Matching Engine**: 425 Too Early — matching engine restarting, retry with exponential backoff

**HTTP Status Code Reference**:

| Code | Meaning |
|------|---------|
| 400 | Bad Request — invalid parameters, malformed payload, business logic violation |
| 401 | Unauthorized — missing/invalid API key, bad HMAC signature |
| 404 | Not Found — market/order/token doesn't exist |
| 425 | Too Early — matching engine restarting |
| 429 | Too Many Requests — rate limit exceeded |
| 500 | Internal Server Error — unexpected, retry with backoff |
| 503 | Service Unavailable — exchange paused or cancel-only mode |

---

### Page: https://docs.polymarket.com/quickstart (Developer Quickstart)

**Step 1 — Fetch Market Data**: "All data endpoints are public — no API key or authentication needed." Query markets endpoint via cURL/TypeScript/Python/Rust.

**Step 2 — SDK Installation**: `@polymarket/clob-client` (TS), `py-clob-client` (Python), `polymarket-client-sdk` (Rust)

**Step 3 — Client Configuration**: Derive API credentials through L1-to-L2 authentication using private key and signer. "Your funder address needs USDC.e (for buying outcome tokens) and POL (for gas, if using EOA type 0)."

**Step 4 — Place Orders**: Submit limit orders with token ID, price, size, side.

---

### Page: https://docs.polymarket.com/market-makers/overview (Market Making)

**Definition**: Market Maker "continuously posts bid and ask orders" to provide liquidity, earning spread as compensation.

**Essential Functions**: Provide liquidity, tighten spreads, enable price discovery, absorb trading flow.

**Setup**: Deploy wallets + fund USDC.e -> Connect WebSocket for orderbook -> Submit orders via CLOB REST API.

**Critical Warning**: "If your bid price is higher than your ask price (a 'negative spread' or 'crossed market'), you will lose money on every fill."

---

### Page: https://docs.polymarket.com/market-makers/liquidity-rewards (Liquidity Rewards Program)

**Overview**: Automatic compensation for posting resting limit orders. "Rewards distributed directly to maker addresses daily at midnight UTC." $5M+ allocated for April 2026 across sports and esports.

**Order Scoring Function**: `S(v,s) = ((v-s)/v)^2 * b`
Where: v = maximum spread from midpoint (cents), s = spread from size-cutoff-adjusted midpoint, b = in-game multiplier

**Score Calculation Chain**:
1. Q_one: Aggregates scoring across bid positions on primary + ask on complementary
2. Q_two: Mirrors Q_one with reversed bid/ask
3. Q_min (midpoints 0.10-0.90): `max(min(Q_one, Q_two), max(Q_one/c, Q_two/c))` where c=3.0
4. Q_min (extreme midpoints <0.10 or >0.90): `min(Q_one, Q_two)`
5. Q_normal: Individual Q_min / sum of all MMs' Q_min
6. Q_epoch: Sum of Q_normal across 10,080 samples (one week)
7. Q_final: Q_epoch / total * market rewards

**Parameters**:
- Minimum payout: $1
- Sampling: 1-minute intervals
- Epoch: 10,080 samples (one week)
- Inspired by dYdX liquidity provider rewards

**April 2026 Reward Highlights** (per game):
- NBA: $7,700/game
- English Premier League: $10,000/game
- Champions League QFs: $24,000/game
- MLB: $1,650/game
- NHL: $1,500/game
- UFC Main Card: $4,250/game
- CS2 A-Tier: $5,500/game
- IPL Cricket: $4,500/game
