"""
Kalshi API Client — Data ingestion from the second prediction market venue.

Kalshi is a CFTC-regulated centralized exchange (no blockchain).
Key differences from Polymarket:
  - Auth: RSA-PSS signed headers (not EIP-712)
  - Prices: Dollar strings ("0.6500" = 65 cents = 65%) not floats
  - Market IDs: Tickers ("FED-26MAY-T4.50") not condition IDs
  - Orders: side "yes"/"no" + action "buy"/"sell" (not token-based)
  - Fees: 0.07 * P * (1-P) per contract, max 1.75 cents. Makers 0%.
  - Full sandbox available at demo-api.kalshi.co

This module provides:
  1. Market data reads (list markets, get prices, get orderbook)
  2. Market search and filtering by category
  3. Normalization to our common Market/KalshiMarket format

Order placement is deferred — for Phase 3 paper trading, we only need
to READ Kalshi prices to detect cross-platform opportunities.
The paper trader simulates execution on both sides.

Auth requires KALSHI_API_KEY_ID and KALSHI_PRIVATE_KEY_PATH env vars.
For read-only sandbox access during paper trading, these can be demo credentials.
"""

import base64
import hashlib
import logging
import os
import time
from datetime import datetime, timezone
from typing import Optional

import requests

from projects.prediction_market_arb.constants import (
    KALSHI_API_URL, KALSHI_SANDBOX_URL, KALSHI_TAKER_FEE_RATE, KALSHI_MAX_FEE_CENTS,
)
from projects.prediction_market_arb.models import KalshiMarket

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

    def _get(self, path: str, params: dict = None) -> Optional[dict]:
        """Authenticated GET request to Kalshi API."""
        url = f"{self.api_url}{path}"

        headers = {}
        if self._authenticated:
            headers = _auth_headers(
                self.api_key_id, self.private_key_path,
                "GET", f"/trade-api/v2{path}",
            )

        try:
            resp = self._session.get(url, params=params, headers=headers, timeout=15)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            logger.error(f"Kalshi GET {path} failed: {e}")
            return None

    # -------------------------------------------------------------------------
    # Market Data
    # -------------------------------------------------------------------------

    def get_markets(self, status: str = "open", limit: int = 200,
                    category: str = None) -> list[KalshiMarket]:
        """
        Fetch active markets from Kalshi.

        Returns list of KalshiMarket objects normalized to our format.
        """
        params = {"status": status, "limit": limit}
        if category:
            params["series_ticker"] = category

        data = self._get("/markets", params=params)
        if not data:
            return []

        markets = []
        for m in data.get("markets", []):
            km = KalshiMarket(
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

    def scan_categories(self, categories: list = None) -> list[KalshiMarket]:
        """
        Scan all configured categories and return combined market list.
        Used by the contract matcher to find cross-platform candidates.
        """
        if categories is None:
            categories = self.config.kalshi.categories
            if isinstance(categories, str):
                categories = [categories]

        all_markets = []
        seen_tickers = set()

        for cat in categories:
            markets = self.get_markets(status="open", limit=200)
            for m in markets:
                if m.ticker not in seen_tickers:
                    # Filter by category if the market has category info
                    if not cat or cat.lower() in m.category.lower() or cat.lower() in m.title.lower():
                        all_markets.append(m)
                        seen_tickers.add(m.ticker)

        logger.info(f"[KALSHI] Scanned {len(all_markets)} unique markets "
                    f"across {len(categories)} categories")
        return all_markets
