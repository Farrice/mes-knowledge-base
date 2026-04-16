"""
Kalshi API Client — Data ingestion from the second prediction market venue.

Kalshi is a CFTC-regulated centralized exchange (no blockchain).
Key differences from Polymarket:
  - Auth: RSA-PSS signed headers (not EIP-712)
  - Prices: Dollar strings ("0.6500" = 65 cents = 65%) not floats
  - Market IDs: Tickers ("FED-26MAY-T4.50") not condition IDs
  - Orders: side "yes"/"no" + action "buy"/"sell" (not token-based)
  - Fees: 0.07 * P * (1-P) per contract, max 1.75 cents. Makers 0%.
  - No market orders (simulate via limit at $0.99/$0.01)
  - Mandatory UUID4 client_order_id on every order (dedup protection)
  - Full sandbox available at demo-api.kalshi.co

Rate limits (Basic tier):
  - 20 reads/second, 10 writes/second
  - 429 responses require exponential backoff
  - BatchCancel counts each cancel as 0.2 transactions

Hardening notes (from April 2026 audit):
  - Dollar-string prices ("0.6500") replaced legacy integer cents as of March 2026
  - count_fp is a string ("10.00"), not an integer
  - Cursor-based pagination for large result sets (>200 markets)
  - 5 documented settlement disputes since 2025 — cross-platform arb must account for this

Auth requires KALSHI_API_KEY_ID and KALSHI_PRIVATE_KEY_PATH env vars.
For read-only sandbox access during paper trading, these can be demo credentials.
"""

import base64
import hashlib
import logging
import os
import random
import time
import uuid
from datetime import datetime, timezone
from typing import Optional

import requests

from projects.prediction_market_arb.constants import (
    KALSHI_API_URL, KALSHI_SANDBOX_URL, KALSHI_TAKER_FEE_RATE, KALSHI_MAX_FEE_CENTS,
)
from projects.prediction_market_arb.models import (
    KalshiMarket, OrderResult, OrderStatus, Position, OrderSide,
)
from projects.prediction_market_arb.resilience import retry_transient
from projects.prediction_market_arb.state import StateManager

logger = logging.getLogger("polymarket.kalshi")


# =============================================================================
# RSA-PSS AUTHENTICATION
# =============================================================================

def _sign_request(private_key_path: str, timestamp_ms: int,
                  method: str, path: str) -> str:
    """
    Sign a Kalshi API request using RSA-PSS.

    Signature = RSA-PSS-Sign(SHA-256, "{timestamp}{METHOD}{path}")
    Returns base64-encoded signature string.
    """
    try:
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import padding

        message = f"{timestamp_ms}{method}{path}".encode()

        with open(private_key_path, "rb") as f:
            private_key = serialization.load_pem_private_key(f.read(), password=None)

        signature = private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        return base64.b64encode(signature).decode()
    except ImportError:
        logger.error("cryptography package required for Kalshi auth: pip install cryptography")
        return ""
    except Exception as e:
        logger.error(f"Kalshi signing failed: {e}")
        return ""


def _auth_headers(api_key_id: str, private_key_path: str,
                  method: str, path: str) -> dict:
    """Build Kalshi authentication headers."""
    timestamp_ms = int(time.time() * 1000)
    signature = _sign_request(private_key_path, timestamp_ms, method, path)

    return {
        "KALSHI-ACCESS-KEY": api_key_id,
        "KALSHI-ACCESS-TIMESTAMP": str(timestamp_ms),
        "KALSHI-ACCESS-SIGNATURE": signature,
    }


# =============================================================================
# KALSHI FEE CALCULATION
# =============================================================================

def kalshi_taker_fee(price: float) -> float:
    """
    Calculate Kalshi taker fee per contract.

    Formula: min(0.07 * P * (1-P), 0.0175)
    where P is price as decimal (0-1).
    Returns fee in dollars.
    """
    if price <= 0 or price >= 1.0:
        return 0.0
    fee = KALSHI_TAKER_FEE_RATE * price * (1.0 - price)
    return min(fee, KALSHI_MAX_FEE_CENTS / 100.0)


# =============================================================================
# KALSHI CLIENT
# =============================================================================

class KalshiClient:
    """
    Kalshi market data client. Reads market data for cross-platform comparison.

    For paper trading phase, this is READ-ONLY — we fetch Kalshi prices
    to detect cross-platform opportunities, but simulated execution
    happens through the paper trader, not through Kalshi's order API.
    """

    def __init__(self, config):
        self.config = config
        kalshi_cfg = config.kalshi if hasattr(config, 'kalshi') else config

        use_sandbox = kalshi_cfg.use_sandbox if hasattr(kalshi_cfg, 'use_sandbox') else True
        self.api_url = (
            kalshi_cfg.sandbox_url if use_sandbox
            else kalshi_cfg.api_url
        )

        self.api_key_id = os.environ.get("KALSHI_API_KEY_ID", "")
        self.private_key_path = os.environ.get("KALSHI_PRIVATE_KEY_PATH", "")

        self._session = requests.Session()
        self._session.headers.update({
            "User-Agent": "polymarket-arb/0.2.0",
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

        self._authenticated = bool(self.api_key_id and self.private_key_path)
        if not self._authenticated:
            logger.warning("Kalshi API credentials not set — using unauthenticated mode "
                           "(will fail on Kalshi, which requires auth for all endpoints)")

        mode = "sandbox" if use_sandbox else "production"
        logger.info(f"[KALSHI] Client initialized ({mode})")

    @retry_transient()
    def _request(self, method: str, path: str, params: dict = None,
                  json_body: dict = None, max_retries: int = 3) -> Optional[dict]:
        """
        Authenticated request to Kalshi API with rate-limit backoff.

        Handles:
          - RSA-PSS authentication headers
          - 429 rate limit responses with exponential backoff
          - Connection errors with retry
          - Timeout handling
        """
        url = f"{self.api_url}{path}"

        for attempt in range(max_retries):
            headers = {}
            if self._authenticated:
                headers = _auth_headers(
                    self.api_key_id, self.private_key_path,
                    method.upper(), f"/trade-api/v2{path}",
                )

            try:
                if method.upper() == "GET":
                    resp = self._session.get(url, params=params, headers=headers, timeout=15)
                elif method.upper() == "POST":
                    resp = self._session.post(url, json=json_body, headers=headers, timeout=15)
                elif method.upper() == "DELETE":
                    resp = self._session.delete(url, params=params, headers=headers, timeout=15)
                else:
                    resp = self._session.request(method, url, params=params,
                                                  json=json_body, headers=headers, timeout=15)

                # Handle rate limiting (429)
                if resp.status_code == 429:
                    retry_after = float(resp.headers.get("Retry-After", 2 ** attempt))
                    logger.warning(f"[KALSHI] Rate limited on {path}, "
                                   f"backing off {retry_after:.1f}s (attempt {attempt + 1})")
                    time.sleep(min(retry_after, 30))  # Cap at 30s
                    continue

                resp.raise_for_status()
                return resp.json()

            except requests.ConnectionError as e:
                logger.warning(f"[KALSHI] Connection error on {path} "
                               f"(attempt {attempt + 1}/{max_retries}): {e}")
                time.sleep(2 ** attempt)
            except requests.Timeout:
                logger.warning(f"[KALSHI] Timeout on {path} "
                               f"(attempt {attempt + 1}/{max_retries})")
                time.sleep(2 ** attempt)
            except requests.HTTPError as e:
                logger.error(f"[KALSHI] HTTP error on {path}: {e}")
                return None
            except requests.RequestException as e:
                logger.error(f"[KALSHI] Request failed on {path}: {e}")
                return None

        logger.error(f"[KALSHI] All {max_retries} retries exhausted for {path}")
        return None

    def _get(self, path: str, params: dict = None) -> Optional[dict]:
        """Authenticated GET request with rate-limit backoff."""
        return self._request("GET", path, params=params)

    def _post(self, path: str, body: dict = None) -> Optional[dict]:
        """Authenticated POST request with rate-limit backoff."""
        return self._request("POST", path, json_body=body)

    # -------------------------------------------------------------------------
    # Market Data
    # -------------------------------------------------------------------------

    def get_markets(self, status: str = "open", limit: int = 200,
                    category: str = None) -> list[KalshiMarket]:
        """
        Fetch active markets from Kalshi.

        Returns list of KalshiMarket objects normalized to our format.
        Uses _parse_market for consistent parsing across all methods.
        """
        params = {"status": status, "limit": min(limit, 200)}
        if category:
            params["series_ticker"] = category

        data = self._get("/markets", params=params)
        if not data:
            return []

        markets = []
        for m in data.get("markets", []):
            km = self._parse_market(m)
            if km:
                markets.append(km)

        logger.info(f"[KALSHI] Fetched {len(markets)} markets"
                    f"{f' (category: {category})' if category else ''}")
        return markets

    def get_market(self, ticker: str) -> Optional[KalshiMarket]:
        """Fetch a single market by ticker."""
        data = self._get(f"/markets/{ticker}")
        if not data or "market" not in data:
            return None

        m = data["market"]
        return KalshiMarket(
            ticker=m.get("ticker", ""),
            title=m.get("title", ""),
            subtitle=m.get("subtitle", ""),
            category=m.get("category", ""),
            status=m.get("status", ""),
            yes_price=self._parse_price(m.get("yes_bid_dollars", "0")),
            no_price=self._parse_price(m.get("no_bid_dollars", "0")),
            yes_bid=self._parse_price(m.get("yes_bid_dollars", "0")),
            yes_ask=self._parse_price(m.get("yes_ask_dollars", "0")),
            volume=int(m.get("volume", 0) or 0),
            open_interest=int(m.get("open_interest", 0) or 0),
            end_date=m.get("expiration_time", ""),
            settlement_source=m.get("settlement_source_url", ""),
            result=m.get("result", ""),
        )

    def get_orderbook(self, ticker: str) -> dict:
        """Fetch orderbook for a Kalshi market."""
        data = self._get(f"/markets/{ticker}/orderbook")
        if not data:
            return {"yes_bids": [], "yes_asks": [], "no_bids": [], "no_asks": []}

        book = data.get("orderbook_fp", data.get("orderbook", {}))

        def parse_levels(levels):
            return [(self._parse_price(l[0]), float(l[1]))
                    for l in levels if len(l) >= 2]

        return {
            "yes_bids": parse_levels(book.get("yes", {}).get("bids", [])),
            "yes_asks": parse_levels(book.get("yes", {}).get("asks", [])),
            "no_bids": parse_levels(book.get("no", {}).get("bids", [])),
            "no_asks": parse_levels(book.get("no", {}).get("asks", [])),
        }

    def get_events(self, status: str = "open", limit: int = 100) -> list[dict]:
        """Fetch events (groups of related markets)."""
        data = self._get("/events", params={"status": status, "limit": limit})
        if not data:
            return []
        return data.get("events", [])

    def search_markets(self, query: str, status: str = "open") -> list[KalshiMarket]:
        """Search Kalshi markets by text query."""
        # Kalshi doesn't have a dedicated search endpoint — filter client-side
        all_markets = self.get_markets(status=status, limit=500)
        query_lower = query.lower()
        return [m for m in all_markets
                if query_lower in m.title.lower() or query_lower in m.subtitle.lower()]

    def get_market_price(self, ticker: str) -> Optional[dict]:
        """
        Get current prices for a Kalshi market, normalized to 0-1 for
        comparison with Polymarket.
        """
        market = self.get_market(ticker)
        if not market:
            return None
        return {
            "yes": market.yes_price_normalized,
            "no": market.no_price_normalized,
            "yes_cents": market.yes_price,
            "no_cents": market.no_price,
        }

    # -------------------------------------------------------------------------
    # Helpers
    # -------------------------------------------------------------------------

    @staticmethod
    def _parse_price(price_str) -> float:
        """
        Parse Kalshi dollar-string prices to cents.

        "0.6500" → 65.0 (cents)
        65 → 65.0 (already cents, legacy format)
        """
        if isinstance(price_str, (int, float)):
            # Legacy cent format or already numeric
            val = float(price_str)
            if val <= 1.0:
                return val * 100  # Was a decimal, convert to cents
            return val
        try:
            val = float(price_str)
            if val <= 1.0:
                return val * 100  # Dollar string → cents
            return val
        except (ValueError, TypeError):
            return 0.0

    # -------------------------------------------------------------------------
    # Paginated Market Fetch (handles >200 markets via cursor)
    # -------------------------------------------------------------------------

    def get_all_markets(self, status: str = "open",
                        max_pages: int = 5) -> list[KalshiMarket]:
        """
        Fetch ALL active markets using cursor-based pagination.

        Kalshi returns max 200 markets per request. For full scans,
        we follow the cursor until exhausted or max_pages reached.
        """
        all_markets = []
        cursor = None

        for page in range(max_pages):
            params = {"status": status, "limit": 200}
            if cursor:
                params["cursor"] = cursor

            data = self._get("/markets", params=params)
            if not data:
                break

            markets_data = data.get("markets", [])
            if not markets_data:
                break

            for m in markets_data:
                km = self._parse_market(m)
                if km:
                    all_markets.append(km)

            cursor = data.get("cursor")
            if not cursor:
                break  # No more pages

            logger.debug(f"[KALSHI] Page {page + 1}: {len(markets_data)} markets, "
                         f"total so far: {len(all_markets)}")

        logger.info(f"[KALSHI] Fetched {len(all_markets)} total markets "
                    f"across {min(page + 1, max_pages)} pages")
        return all_markets

    def _parse_market(self, m: dict) -> Optional[KalshiMarket]:
        """Parse a single market JSON object into KalshiMarket."""
        try:
            return KalshiMarket(
                ticker=m.get("ticker", ""),
                title=m.get("title", ""),
                subtitle=m.get("subtitle", ""),
                category=m.get("category", ""),
                status=m.get("status", ""),
                yes_price=self._parse_price(m.get("yes_bid_dollars", m.get("last_price", "0"))),
                no_price=self._parse_price(m.get("no_bid_dollars", "0")),
                yes_bid=self._parse_price(m.get("yes_bid_dollars", "0")),
                yes_ask=self._parse_price(m.get("yes_ask_dollars", "0")),
                volume=int(m.get("volume", 0) or 0),
                open_interest=int(m.get("open_interest", 0) or 0),
                end_date=m.get("expiration_time", ""),
                settlement_source=m.get("settlement_source_url", ""),
                result=m.get("result", ""),
            )
        except (ValueError, TypeError) as e:
            logger.warning(f"[KALSHI] Failed to parse market {m.get('ticker', '?')}: {e}")
            return None

    # -------------------------------------------------------------------------
    # Order Placement (Phase 5 — live trading only)
    # -------------------------------------------------------------------------

    def place_order(self, ticker: str, side: str, action: str,
                    count: float, price: float,
                    order_type: str = "limit") -> Optional[dict]:
        """
        Place an order on Kalshi.

        IMPORTANT:
          - Kalshi has NO market orders. For immediate fill, use limit at
            $0.99 (buy yes) or $0.01 (buy no). This simulates a market order.
          - Every order MUST have a unique client_order_id (UUID4) to prevent
            duplicate execution on retry.
          - Prices are dollar strings ("0.6500"), counts are float strings ("10.00")
          - side: "yes" or "no"
          - action: "buy" or "sell"

        Returns order response dict or None on failure.
        """
        # Generate unique client order ID for dedup
        client_order_id = str(uuid.uuid4())

        # Validate inputs
        if side not in ("yes", "no"):
            logger.error(f"[KALSHI] Invalid side: {side}. Must be 'yes' or 'no'")
            return None
        if action not in ("buy", "sell"):
            logger.error(f"[KALSHI] Invalid action: {action}. Must be 'buy' or 'sell'")
            return None

        # Convert price to dollar string format
        price_str = f"{price:.4f}" if isinstance(price, float) else str(price)
        count_str = f"{count:.2f}" if isinstance(count, float) else str(count)

        body = {
            "ticker": ticker,
            "client_order_id": client_order_id,
            "side": side,
            "action": action,
            "count_fp": count_str,
            "type": order_type,
        }

        # Kalshi limit orders require yes_price_dollars
        if order_type == "limit":
            body["yes_price_dollars"] = price_str

        logger.info(f"[KALSHI] Placing order: {action} {count_str} {side} @ ${price_str} "
                     f"on {ticker} (id: {client_order_id[:8]}...)")

        return self._post("/portfolio/orders", body=body)

    def cancel_order(self, order_id: str) -> bool:
        """Cancel a Kalshi order by order ID."""
        result = self._request("DELETE", f"/portfolio/orders/{order_id}")
        if result is not None:
            logger.info(f"[KALSHI] Order {order_id} cancelled")
            return True
        return False

    def get_positions(self) -> list[dict]:
        """Fetch current Kalshi positions."""
        data = self._get("/portfolio/positions")
        if not data:
            return []
        return data.get("market_positions", [])

    def get_balance(self) -> float:
        """Fetch current Kalshi account balance in dollars."""
        data = self._get("/portfolio/balance")
        if not data:
            return 0.0
        # Balance is in cents
        return float(data.get("balance", 0)) / 100.0

    # -------------------------------------------------------------------------
    # Helpers
    # -------------------------------------------------------------------------

    def scan_categories(self, categories: list = None) -> list[KalshiMarket]:
        """
        Scan all configured categories and return combined market list.
        Uses paginated fetch for completeness, then filters by category.
        Used by the contract matcher to find cross-platform candidates.
        """
        if categories is None:
            categories = self.config.kalshi.categories
            if isinstance(categories, str):
                categories = [categories]

        # Fetch all markets once (paginated), then filter locally
        # This is more efficient than N separate API calls per category
        all_markets = self.get_all_markets(status="open", max_pages=5)

        if not categories:
            return all_markets

        # Filter by category keywords
        cat_lower = {c.lower() for c in categories}
        filtered = []
        for m in all_markets:
            m_cat = m.category.lower() if m.category else ""
            m_title = m.title.lower() if m.title else ""
            if any(c in m_cat or c in m_title for c in cat_lower):
                filtered.append(m)

        logger.info(f"[KALSHI] Scanned {len(filtered)} markets matching categories "
                    f"{categories} (from {len(all_markets)} total)")
        return filtered


# =============================================================================
# PAPER KALSHI CLIENT — reads real data, simulates order execution
# =============================================================================

class PaperKalshiClient(KalshiClient):
    """
    Paper trading client for Kalshi. Inherits ALL market data reads from
    KalshiClient (so paper trading uses actual Kalshi prices). Order
    operations write to local JSON state instead of the real API.

    Mirrors the PaperPolymarketClient pattern:
      - Real market data reads (get_markets, get_market, get_orderbook, etc.)
      - Simulated order fills with configurable fill probability
      - State persistence via StateManager (Kalshi-namespaced positions)

    Kalshi-specific differences from Polymarket paper client:
      - Prices are in cents internally (1-99), normalized to 0-1 for position tracking
      - Orders use side ("yes"/"no") + action ("buy"/"sell"), not token IDs
      - Separate positions file (kalshi_positions.json) to avoid collision
      - Fee calculation uses Kalshi's formula: min(0.07 * P * (1-P), 0.0175)
    """

    def __init__(self, config, state_manager: StateManager):
        super().__init__(config)
        self.state = state_manager
        self._fill_probability = config.paper.get("fill_probability", 0.8)

        # Kalshi positions stored in a separate file to avoid collision
        # with Polymarket positions
        self._kalshi_positions_file = "kalshi_positions.json"

        logger.info("[KALSHI-PAPER] Paper client initialized — "
                    "orders will NOT hit the real Kalshi API")

    # -------------------------------------------------------------------------
    # Kalshi Position Persistence (separate namespace from Polymarket)
    # -------------------------------------------------------------------------

    def _load_kalshi_positions(self) -> list[Position]:
        """Load Kalshi-specific paper positions."""
        path = self.state.data_dir / self._kalshi_positions_file
        data = self.state._load_json(path, [])
        if isinstance(data, list):
            return [Position.from_dict(p) for p in data]
        return []

    def _save_kalshi_positions(self, positions: list[Position]):
        """Save Kalshi-specific paper positions."""
        data = [p.to_dict() for p in positions]
        path = self.state.data_dir / self._kalshi_positions_file
        self.state._atomic_write(path, data)

    def _add_kalshi_position(self, position: Position):
        """Add a position to the Kalshi paper positions."""
        positions = self._load_kalshi_positions()
        positions.append(position)
        self._save_kalshi_positions(positions)

    # -------------------------------------------------------------------------
    # Paper Order Execution
    # -------------------------------------------------------------------------

    def paper_place_order(self, ticker: str, side: str, action: str,
                          count: float, price_cents: float) -> OrderResult:
        """
        Simulate a Kalshi order execution for paper trading.

        Args:
            ticker: Kalshi market ticker (e.g., "FED-26MAY-T4.50")
            side: "yes" or "no"
            action: "buy" or "sell"
            count: Number of contracts
            price_cents: Price in cents (1-99)

        Returns:
            OrderResult with fill details or failure reason.

        Price handling:
            Kalshi prices are in cents (1-99). We normalize to 0-1
            for position tracking so it's compatible with the existing
            Position model and PnL calculations used by paper_trader.py.
        """
        # Validate inputs
        if side not in ("yes", "no"):
            return OrderResult(
                order_id=str(uuid.uuid4()),
                status=OrderStatus.FAILED,
                error=f"Invalid side: {side}. Must be 'yes' or 'no'",
                is_paper=True,
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
        if action not in ("buy", "sell"):
            return OrderResult(
                order_id=str(uuid.uuid4()),
                status=OrderStatus.FAILED,
                error=f"Invalid action: {action}. Must be 'buy' or 'sell'",
                is_paper=True,
                timestamp=datetime.now(timezone.utc).isoformat(),
            )

        # Normalize price to 0-1 for position tracking
        price_normalized = price_cents / 100.0

        # Calculate Kalshi taker fee
        fee_per_contract = kalshi_taker_fee(price_normalized)
        total_fee = fee_per_contract * count

        # Simulate fill
        filled = random.random() < self._fill_probability

        if not filled:
            logger.info(f"[KALSHI-PAPER] Order not filled (simulated miss) "
                        f"for {ticker}")
            return OrderResult(
                order_id=str(uuid.uuid4()),
                status=OrderStatus.CANCELLED,
                is_paper=True,
                timestamp=datetime.now(timezone.utc).isoformat(),
            )

        # Fill simulation
        order_id = str(uuid.uuid4())

        if action == "buy":
            # Cost to buy = price * count + fees
            cost = price_normalized * count + total_fee

            # Check paper balance
            balance = self.state.load_balance()
            if cost > balance.current:
                return OrderResult(
                    order_id=order_id,
                    status=OrderStatus.FAILED,
                    error=f"Insufficient balance: need ${cost:.2f}, "
                          f"have ${balance.current:.2f}",
                    is_paper=True,
                    timestamp=datetime.now(timezone.utc).isoformat(),
                )

            # Deduct cost from balance
            balance.current -= cost
            balance.total_trades += 1
            self.state.save_balance(balance)

            # Record position
            # Use ticker as market_id, side as token_id (Kalshi doesn't have token IDs)
            position = Position(
                market_id=f"kalshi:{ticker}",
                token_id=f"{side}",  # "yes" or "no"
                side=OrderSide.BUY,
                entry_price=price_normalized,
                size=count,
                current_price=price_normalized,
                entry_time=datetime.now(timezone.utc).isoformat(),
                question=f"[Kalshi] {ticker} ({side})",
            )
            self._add_kalshi_position(position)

            logger.info(f"[KALSHI-PAPER] Order filled: {action} {count:.0f} "
                        f"{side} @ {price_cents:.0f}c on {ticker} "
                        f"(cost: ${cost:.2f}, fee: ${total_fee:.4f})")

        else:  # action == "sell"
            # For sell, we receive (price * count - fees)
            proceeds = price_normalized * count - total_fee

            balance = self.state.load_balance()
            balance.current += proceeds
            balance.total_trades += 1
            self.state.save_balance(balance)

            logger.info(f"[KALSHI-PAPER] Order filled: {action} {count:.0f} "
                        f"{side} @ {price_cents:.0f}c on {ticker} "
                        f"(proceeds: ${proceeds:.2f}, fee: ${total_fee:.4f})")

        return OrderResult(
            order_id=order_id,
            status=OrderStatus.CONFIRMED,
            fill_price=price_normalized,
            fill_size=count,
            is_paper=True,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    def get_paper_positions(self) -> list[Position]:
        """Get current Kalshi paper positions."""
        return self._load_kalshi_positions()

    def get_paper_balance(self) -> float:
        """Get current paper balance (shared with Polymarket paper balance)."""
        return self.state.load_balance().current


# =============================================================================
# FACTORY
# =============================================================================

def create_kalshi_client(config, state_manager: StateManager) -> PaperKalshiClient:
    """
    Create a PaperKalshiClient for paper trading.

    Currently only supports paper mode. Live Kalshi trading will be
    added in a future phase (requires RSA-PSS auth + sandbox testing).
    """
    return PaperKalshiClient(config, state_manager)
