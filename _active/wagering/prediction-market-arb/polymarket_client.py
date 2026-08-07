"""
Polymarket API Client — Paper/Live hierarchy with two-key safety gate.

Architecture:
  PaperPolymarketClient  — reads real market data from Gamma/CLOB APIs,
                           writes orders to local JSON state (no real execution)
  LivePolymarketClient   — extends Paper, overrides order methods to hit real API.
                           Requires: config mode="live" AND env POLYMARKET_LIVE_ENABLED=true
                           AND confirm_live=True on every order call.
  create_client(config)  — factory function, returns the right class.

The LLM never holds private keys or places orders directly.
This module is Layer 3 (deterministic execution).
"""

import json
import logging
import os
import time
import uuid
from datetime import datetime, timezone
from typing import Optional

import requests

from projects.prediction_market_arb.constants import (
    CLOB_URL, GAMMA_URL, DATA_URL, POLYGON_CHAIN_ID,
)
from projects.prediction_market_arb.models import (
    Market, OrderRequest, OrderResult, Position, OrderSide, OrderStatus,
)
from projects.prediction_market_arb.resilience import retry_transient
from projects.prediction_market_arb.state import StateManager

logger = logging.getLogger("polymarket.client")


# =============================================================================
# EXCEPTIONS
# =============================================================================

class LiveTradingDisabledError(Exception):
    """Raised when live trading is attempted without proper authorization."""
    pass


class LiveConfirmationRequired(Exception):
    """Raised when a live order is placed without confirm_live=True."""
    pass


# =============================================================================
# PAPER CLIENT — reads real data, writes orders to JSON
# =============================================================================

class PaperPolymarketClient:
    """
    Paper trading client. All market data reads hit the REAL Polymarket APIs
    (so paper trading uses actual prices). Order operations write to local
    JSON state instead of the API.
    """

    def __init__(self, config, state_manager: StateManager):
        self.config = config
        self.state = state_manager
        self.gamma_url = config.api.gamma_url
        self.clob_url = config.api.clob_url
        self.data_url = config.api.data_url
        self._session = requests.Session()
        self._session.headers.update({
            "User-Agent": "polymarket-arb/0.1.0",
            "Accept": "application/json",
        })
        logger.info("[PAPER] Client initialized — orders will NOT hit the real API")

    # -------------------------------------------------------------------------
    # Market Data (reads from REAL APIs — same in paper and live mode)
    # -------------------------------------------------------------------------

    @retry_transient()
    def get_markets(self, active: bool = True, limit: int = 100,
                    category: str = None) -> list:
        """Fetch markets from Gamma API."""
        params = {"active": str(active).lower(), "limit": limit, "closed": "false"}
        if category:
            params["tag"] = category
        try:
            resp = self._session.get(
                f"{self.gamma_url}/markets", params=params, timeout=15
            )
            resp.raise_for_status()
            markets = []
            for m in resp.json():
                markets.append(Market(
                    id=m.get("id", ""),
                    question=m.get("question", ""),
                    slug=m.get("slug", ""),
                    end_date=m.get("endDate", "") or m.get("end_date_iso", ""),
                    volume=float(m.get("volume", 0) or 0),
                    active=m.get("active", True),
                    condition_id=m.get("conditionId", "") or m.get("condition_id", ""),
                    tokens=[t.get("token_id", "") for t in m.get("tokens", [])],
                    neg_risk=m.get("neg_risk", False) or m.get("negRisk", False),
                    category=m.get("groupItemTitle", ""),
                ))
            return markets
        except requests.RequestException as e:
            logger.error(f"Failed to fetch markets: {e}")
            return []

    @retry_transient()
    def get_market(self, condition_id: str) -> Optional[Market]:
        """Fetch a single market by condition ID."""
        try:
            resp = self._session.get(
                f"{self.gamma_url}/markets/{condition_id}", timeout=15
            )
            resp.raise_for_status()
            m = resp.json()
            return Market(
                id=m.get("id", ""),
                question=m.get("question", ""),
                slug=m.get("slug", ""),
                end_date=m.get("endDate", "") or m.get("end_date_iso", ""),
                volume=float(m.get("volume", 0) or 0),
                active=m.get("active", True),
                condition_id=m.get("conditionId", "") or m.get("condition_id", ""),
                tokens=[t.get("token_id", "") for t in m.get("tokens", [])],
                neg_risk=m.get("neg_risk", False) or m.get("negRisk", False),
            )
        except requests.RequestException as e:
            logger.error(f"Failed to fetch market {condition_id}: {e}")
            return None

    @retry_transient()
    def get_event(self, slug: str) -> Optional[dict]:
        """Fetch event by slug (used for weather market discovery)."""
        try:
            resp = self._session.get(
                f"{self.gamma_url}/events", params={"slug": slug}, timeout=15
            )
            resp.raise_for_status()
            data = resp.json()
            if data and isinstance(data, list) and len(data) > 0:
                return data[0]
            return None
        except requests.RequestException as e:
            logger.error(f"Failed to fetch event {slug}: {e}")
            return None

    @retry_transient()
    def get_orderbook(self, token_id: str) -> dict:
        """Fetch orderbook for a token from CLOB API."""
        try:
            resp = self._session.get(
                f"{self.clob_url}/book",
                params={"token_id": token_id},
                timeout=15,
            )
            resp.raise_for_status()
            book = resp.json()
            return {
                "bids": [(float(b["price"]), float(b["size"])) for b in book.get("bids", [])],
                "asks": [(float(a["price"]), float(a["size"])) for a in book.get("asks", [])],
            }
        except requests.RequestException as e:
            logger.error(f"Failed to fetch orderbook for {token_id}: {e}")
            return {"bids": [], "asks": []}

    def get_best_price(self, token_id: str) -> tuple:
        """Get best bid and ask for a token. Returns (best_bid, best_ask)."""
        book = self.get_orderbook(token_id)
        best_bid = max((p for p, _ in book["bids"]), default=0.0) if book["bids"] else 0.0
        best_ask = min((p for p, _ in book["asks"]), default=1.0) if book["asks"] else 1.0
        return (best_bid, best_ask)

    @retry_transient()
    def get_market_price(self, market_id: str) -> Optional[dict]:
        """Get current prices for a market from Gamma API."""
        try:
            resp = self._session.get(
                f"{self.gamma_url}/markets/{market_id}", timeout=15
            )
            resp.raise_for_status()
            m = resp.json()
            prices_str = m.get("outcomePrices", "[0.5,0.5]")
            prices = json.loads(prices_str) if isinstance(prices_str, str) else prices_str
            return {
                "yes": float(prices[0]) if len(prices) > 0 else 0.5,
                "no": float(prices[1]) if len(prices) > 1 else 0.5,
            }
        except (requests.RequestException, json.JSONDecodeError, IndexError) as e:
            logger.error(f"Failed to get price for {market_id}: {e}")
            return None

    @retry_transient()
    def search_events(self, query: str) -> list:
        """Search events by text query."""
        try:
            resp = self._session.get(
                f"{self.gamma_url}/events",
                params={"title": query, "limit": 50},
                timeout=15,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            logger.error(f"Event search failed for '{query}': {e}")
            return []

    # -------------------------------------------------------------------------
    # Order Operations (PAPER — writes to state, does NOT hit API)
    # -------------------------------------------------------------------------

    def place_order(self, order: OrderRequest, confirm_live: bool = False) -> OrderResult:
        """Place a paper order. Simulates execution against real market data."""
        # Get current market price for fill simulation
        best_bid, best_ask = self.get_best_price(order.token_id)
        spread = best_ask - best_bid

        # Simulate fill based on configurable probability
        import random
        fill_prob = self.config.paper.get("fill_probability", 0.8)
        filled = random.random() < fill_prob

        # Check slippage
        if spread > self.config.trading.max_slippage:
            logger.info(f"[PAPER] Order rejected — spread ${spread:.3f} > "
                        f"max ${self.config.trading.max_slippage:.3f}")
            return OrderResult(
                order_id=str(uuid.uuid4()),
                status=OrderStatus.FAILED,
                error=f"Spread too wide: {spread:.3f}",
                is_paper=True,
                timestamp=datetime.now(timezone.utc).isoformat(),
            )

        if filled:
            # Simulate fill at the order price (paper mode simplification)
            fill_price = order.price
            result = OrderResult(
                order_id=str(uuid.uuid4()),
                status=OrderStatus.CONFIRMED,
                fill_price=fill_price,
                fill_size=order.size,
                is_paper=True,
                timestamp=datetime.now(timezone.utc).isoformat(),
            )

            # Update paper state
            if order.side == OrderSide.BUY:
                balance = self.state.load_balance()
                cost = fill_price * order.size
                if cost > balance.current:
                    return OrderResult(
                        order_id=str(uuid.uuid4()),
                        status=OrderStatus.FAILED,
                        error=f"Insufficient balance: need ${cost:.2f}, have ${balance.current:.2f}",
                        is_paper=True,
                        timestamp=datetime.now(timezone.utc).isoformat(),
                    )
                balance.current -= cost
                balance.total_trades += 1
                self.state.save_balance(balance)

                position = Position(
                    market_id=order.market_id,
                    token_id=order.token_id,
                    side=order.side,
                    entry_price=fill_price,
                    size=order.size,
                    current_price=fill_price,
                    entry_time=datetime.now(timezone.utc).isoformat(),
                )
                self.state.add_position(position)

            logger.info(f"[PAPER] Order filled: {order.side.value} {order.size:.2f} "
                        f"@ ${fill_price:.3f} (market {order.market_id[:8]}...)")
            return result
        else:
            logger.info(f"[PAPER] Order not filled (simulated miss)")
            return OrderResult(
                order_id=str(uuid.uuid4()),
                status=OrderStatus.CANCELLED,
                is_paper=True,
                timestamp=datetime.now(timezone.utc).isoformat(),
            )

    def cancel_order(self, order_id: str) -> bool:
        """Cancel a paper order (no-op since paper orders are instant)."""
        logger.info(f"[PAPER] Order {order_id} cancelled")
        return True

    def cancel_all(self, market_id: str = None) -> int:
        """Cancel all paper orders (no-op since paper orders are instant)."""
        logger.info(f"[PAPER] All orders cancelled" +
                    (f" for market {market_id}" if market_id else ""))
        return 0

    # -------------------------------------------------------------------------
    # Position & Balance (paper reads from state)
    # -------------------------------------------------------------------------

    def get_positions(self) -> list:
        """Get current positions from state."""
        return self.state.load_positions()

    def get_balance(self) -> float:
        """Get current paper balance."""
        return self.state.load_balance().current


# =============================================================================
# LIVE CLIENT — extends Paper, overrides order methods for real API
# =============================================================================

class LivePolymarketClient(PaperPolymarketClient):
    """
    Live trading client. Extends PaperPolymarketClient and overrides order
    methods to call the real Polymarket CLOB API.

    TWO-KEY SAFETY GATE:
      1. Config mode must be "live"
      2. Environment variable POLYMARKET_LIVE_ENABLED must be "true"
      3. Every order call requires confirm_live=True

    The py-clob-client SDK handles EIP-712 signing and HMAC-SHA256 auth.
    """

    def __init__(self, config, state_manager: StateManager):
        # Check two-key gate BEFORE any initialization
        if config.is_paper:
            raise LiveTradingDisabledError(
                "Live trading requires BOTH config mode='live' AND "
                "POLYMARKET_LIVE_ENABLED=true environment variable"
            )

        if not config.private_key:
            raise LiveTradingDisabledError(
                "Live trading requires POLYMARKET_PRIVATE_KEY environment variable"
            )

        if not config.browser_wallet:
            raise LiveTradingDisabledError(
                "Live trading requires POLYMARKET_BROWSER_WALLET environment variable"
            )

        # Initialize parent (for market data reads)
        super().__init__(config, state_manager)

        # Initialize py-clob-client SDK
        try:
            from py_clob_client.client import ClobClient
            from py_clob_client.constants import POLYGON

            self._clob = ClobClient(
                host=config.api.clob_url,
                key=config.private_key,
                chain_id=POLYGON,
                funder=config.browser_wallet,
                signature_type=2,  # GNOSIS_SAFE
            )
            self._creds = self._clob.create_or_derive_api_creds()
            self._clob.set_api_creds(self._creds)
            logger.warning("[LIVE] Client initialized — orders WILL execute on Polymarket")
        except ImportError:
            raise LiveTradingDisabledError(
                "py-clob-client not installed. Install with: pip install py-clob-client==0.28.0"
            )
        except Exception as e:
            raise LiveTradingDisabledError(f"Failed to initialize CLOB client: {e}")

    @property
    def api_credentials(self) -> dict:
        """API credentials for WebSocket auth. Only available on live client."""
        return {
            "apiKey": self._creds.api_key,
            "secret": self._creds.api_secret,
            "passphrase": self._creds.api_passphrase,
        }

    def place_order(self, order: OrderRequest, confirm_live: bool = False) -> OrderResult:
        """
        Place a REAL order on Polymarket.

        SAFETY: Requires confirm_live=True. Without it, raises LiveConfirmationRequired.
        This prevents accidentally-compatible code from paper mode executing real trades.
        """
        if not confirm_live:
            raise LiveConfirmationRequired(
                "Live order requires confirm_live=True. "
                "This is a safety mechanism — real money is at stake."
            )

        try:
            from py_clob_client.clob_types import OrderArgs, PartialCreateOrderOptions

            order_args = OrderArgs(
                token_id=str(order.token_id),
                price=order.price,
                size=order.size,
                side=order.side.value,
            )

            options = None
            if order.neg_risk:
                options = PartialCreateOrderOptions(neg_risk=True)

            signed_order = self._clob.create_order(order_args, options=options)
            resp = self._clob.post_order(signed_order)

            result = OrderResult(
                order_id=resp.get("orderID", resp.get("id", str(uuid.uuid4()))),
                status=OrderStatus.MATCHED,
                fill_price=order.price,
                fill_size=order.size,
                is_paper=False,
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
            logger.warning(f"[LIVE] Order placed: {order.side.value} {order.size:.2f} "
                           f"@ ${order.price:.3f} (market {order.market_id[:8]}...)")
            return result

        except Exception as e:
            logger.error(f"[LIVE] Order failed: {e}")
            return OrderResult(
                order_id=str(uuid.uuid4()),
                status=OrderStatus.FAILED,
                error=str(e),
                is_paper=False,
                timestamp=datetime.now(timezone.utc).isoformat(),
            )

    def cancel_order(self, order_id: str) -> bool:
        """Cancel a live order."""
        try:
            self._clob.cancel(order_id)
            logger.warning(f"[LIVE] Order {order_id} cancelled")
            return True
        except Exception as e:
            logger.error(f"[LIVE] Cancel failed for {order_id}: {e}")
            return False

    def cancel_all(self, market_id: str = None) -> int:
        """Cancel all live orders, optionally for a specific market."""
        try:
            if market_id:
                self._clob.cancel_market_orders(market=market_id)
            else:
                self._clob.cancel_all()
            logger.warning(f"[LIVE] All orders cancelled" +
                           (f" for market {market_id}" if market_id else ""))
            return 1  # CLOB doesn't return count
        except Exception as e:
            logger.error(f"[LIVE] Cancel all failed: {e}")
            return 0

    @retry_transient()
    def get_positions(self) -> list:
        """Get positions from the real Data API."""
        try:
            resp = self._session.get(
                f"{self.data_url}/positions",
                params={"user": self.config.browser_wallet},
                timeout=15,
            )
            resp.raise_for_status()
            positions = []
            for p in resp.json():
                positions.append(Position(
                    market_id=p.get("market", ""),
                    token_id=str(p.get("asset", "")),
                    side=OrderSide.BUY,
                    entry_price=float(p.get("avgPrice", 0)),
                    size=float(p.get("size", 0)),
                    current_price=float(p.get("curPrice", p.get("avgPrice", 0))),
                    entry_time=p.get("createdAt", ""),
                ))
            return positions
        except requests.RequestException as e:
            logger.error(f"[LIVE] Failed to fetch positions: {e}")
            return []

    def get_balance(self) -> float:
        """Get real USDC.e balance from on-chain."""
        try:
            from web3 import Web3
            from web3.middleware import ExtraDataToPOAMiddleware

            w3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))
            w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

            # Minimal ERC20 ABI for balanceOf
            abi = [{"constant": True, "inputs": [{"name": "_owner", "type": "address"}],
                    "name": "balanceOf", "outputs": [{"name": "balance", "type": "uint256"}],
                    "type": "function"}]
            usdc = w3.eth.contract(
                address="0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174", abi=abi
            )
            raw = usdc.functions.balanceOf(
                Web3.to_checksum_address(self.config.browser_wallet)
            ).call()
            return raw / 10**6  # USDC has 6 decimals
        except Exception as e:
            logger.error(f"[LIVE] Failed to get balance: {e}")
            return 0.0


# =============================================================================
# FACTORY
# =============================================================================

def create_client(config, state_manager: StateManager):
    """
    Create the appropriate client based on config mode.
    Returns PaperPolymarketClient by default (safe).
    """
    if config.is_live:
        return LivePolymarketClient(config, state_manager)
    return PaperPolymarketClient(config, state_manager)
