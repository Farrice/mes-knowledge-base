"""
WebSocket Manager for Polymarket — market data + user channels.

Architecture:
  Market Channel — subscribe with asset_ids, receive book snapshots + price changes.
                   No auth required. Heartbeat loss = reconnect (recoverable).

  User Channel  — subscribe with API credentials, receive order lifecycle events
                   (MATCHED → MINED → CONFIRMED). Auth required (live mode only).
                   Heartbeat loss = ALL OPEN ORDERS CANCELLED (existential).

Heartbeat:
  - Polymarket requires heartbeat echo every 10 seconds
  - We send every 5 seconds (5-second buffer)
  - Dedicated heartbeat coroutine runs independently of message processing

Reconnection:
  - Exponential backoff: 1s, 2s, 4s, 8s (max 60s)
  - Max 5 retries before alerting

Tuesday Restart:
  - Every Tuesday 7:00 AM ET, matching engine restarts (~90s downtime)
  - Pre-cancel all orders at 6:59 AM ET
  - Probe with exponential backoff starting at 7:00 AM ET
  - Resume at 7:02 AM ET
"""

import asyncio
import json
import logging
import time
from datetime import datetime, timezone
from typing import Callable, Optional
from zoneinfo import ZoneInfo

logger = logging.getLogger("polymarket.websocket")

ET = ZoneInfo("America/New_York")


class PolymarketWebSocket:
    """
    Manages WebSocket connections to Polymarket for real-time data.

    Usage:
        ws = PolymarketWebSocket(config, client)
        ws.on_book_update = my_callback      # book snapshot handler
        ws.on_price_change = my_callback     # price change handler
        ws.on_trade_event = my_callback      # trade lifecycle handler
        await ws.start(token_ids=["abc123", "def456"])
    """

    def __init__(self, config, client=None):
        self.config = config
        self.client = client  # For API credentials (user channel auth)
        self._running = False
        self._market_ws = None
        self._user_ws = None
        self._reconnect_attempts = {"market": 0, "user": 0}
        self._max_reconnect_attempts = 5
        self._last_heartbeat = {"market": 0, "user": 0}

        # Callbacks
        self.on_book_update: Optional[Callable] = None
        self.on_price_change: Optional[Callable] = None
        self.on_trade_event: Optional[Callable] = None
        self.on_order_event: Optional[Callable] = None
        self.on_heartbeat: Optional[Callable] = None

    # -------------------------------------------------------------------------
    # Market Channel
    # -------------------------------------------------------------------------

    async def connect_market(self, token_ids: list):
        """Connect to market WebSocket and subscribe to token price updates."""
        try:
            import websockets
        except ImportError:
            logger.error("websockets package not installed: pip install websockets")
            return

        uri = self.config.api.ws_market_url
        while self._running:
            try:
                async with websockets.connect(
                    uri, ping_interval=5, ping_timeout=None
                ) as ws:
                    self._market_ws = ws
                    self._reconnect_attempts["market"] = 0

                    # Subscribe in chunks of 100 (WebSocket subscription limit)
                    for i in range(0, len(token_ids), 100):
                        chunk = token_ids[i:i+100]
                        await ws.send(json.dumps({"assets_ids": chunk}))
                        logger.info(f"Market WS: subscribed to {len(chunk)} tokens "
                                    f"(batch {i//100 + 1})")

                    # Process messages
                    async for message in ws:
                        self._last_heartbeat["market"] = time.time()
                        try:
                            data = json.loads(message)
                            await self._process_market_message(data)
                        except json.JSONDecodeError:
                            logger.warning(f"Market WS: invalid JSON: {message[:100]}")

            except Exception as e:
                self._reconnect_attempts["market"] += 1
                if self._reconnect_attempts["market"] > self._max_reconnect_attempts:
                    logger.error(f"Market WS: max reconnect attempts exceeded")
                    break

                backoff = min(60, 2 ** self._reconnect_attempts["market"])
                logger.warning(f"Market WS disconnected: {e}. "
                               f"Reconnecting in {backoff}s "
                               f"(attempt {self._reconnect_attempts['market']})")
                await asyncio.sleep(backoff)

    async def _process_market_message(self, data):
        """Process a market WebSocket message."""
        if isinstance(data, list):
            for item in data:
                await self._process_market_message(item)
            return

        event_type = data.get("event_type", "")

        if event_type == "book":
            # Full book snapshot
            if self.on_book_update:
                self.on_book_update(data)

        elif event_type == "price_change":
            # Incremental price update
            if self.on_price_change:
                for change in data.get("price_changes", []):
                    self.on_price_change({
                        "market": data.get("market", ""),
                        "side": change.get("side", ""),
                        "price": float(change.get("price", 0)),
                        "size": float(change.get("size", 0)),
                        "asset_id": change.get("asset_id", ""),
                    })

    # -------------------------------------------------------------------------
    # User Channel (live mode only)
    # -------------------------------------------------------------------------

    async def connect_user(self):
        """
        Connect to user WebSocket for order lifecycle events.
        Requires live client with API credentials.

        EXISTENTIAL: Missing heartbeat cancels ALL open orders.
        """
        if not self.client or not hasattr(self.client, 'api_credentials'):
            logger.info("User WS: skipped (no API credentials — paper mode)")
            return

        try:
            import websockets
        except ImportError:
            logger.error("websockets package not installed")
            return

        uri = self.config.api.ws_user_url
        while self._running:
            try:
                async with websockets.connect(
                    uri, ping_interval=5, ping_timeout=None
                ) as ws:
                    self._user_ws = ws
                    self._reconnect_attempts["user"] = 0

                    # Authenticate
                    auth_msg = {
                        "type": "user",
                        "auth": self.client.api_credentials,
                    }
                    await ws.send(json.dumps(auth_msg))
                    logger.info("User WS: authenticated")

                    # Start heartbeat coroutine
                    heartbeat_task = asyncio.create_task(
                        self._user_heartbeat_loop(ws)
                    )

                    try:
                        async for message in ws:
                            self._last_heartbeat["user"] = time.time()
                            try:
                                data = json.loads(message)
                                await self._process_user_message(data)
                            except json.JSONDecodeError:
                                logger.warning(f"User WS: invalid JSON")
                    finally:
                        heartbeat_task.cancel()
                        try:
                            await heartbeat_task
                        except asyncio.CancelledError:
                            pass

            except Exception as e:
                self._reconnect_attempts["user"] += 1
                if self._reconnect_attempts["user"] > self._max_reconnect_attempts:
                    logger.error("User WS: max reconnect attempts exceeded — "
                                 "ALL OPEN ORDERS MAY BE CANCELLED")
                    break

                backoff = min(60, 2 ** self._reconnect_attempts["user"])
                logger.warning(f"User WS disconnected: {e}. "
                               f"Reconnecting in {backoff}s "
                               f"(attempt {self._reconnect_attempts['user']})")
                await asyncio.sleep(backoff)

    async def _user_heartbeat_loop(self, ws):
        """
        Send heartbeat every 5 seconds (10-second timeout window).
        This is existential — missing heartbeat cancels ALL open orders.
        Runs as a dedicated coroutine independent of message processing.
        """
        while self._running:
            try:
                await ws.ping()
                self._last_heartbeat["user"] = time.time()
                if self.on_heartbeat:
                    self.on_heartbeat("user")
            except Exception as e:
                logger.error(f"User heartbeat failed: {e}")
                break
            await asyncio.sleep(5)

    async def _process_user_message(self, data):
        """Process user WebSocket messages (trade lifecycle, order events)."""
        if isinstance(data, list):
            for item in data:
                await self._process_user_message(item)
            return

        event_type = data.get("event_type", "")

        if event_type == "trade":
            # Trade lifecycle: MATCHED → MINED → CONFIRMED / FAILED
            status = data.get("status", "")
            logger.info(f"User WS trade: {data.get('market', '')[:8]}... "
                        f"status={status} side={data.get('side', '')}")
            if self.on_trade_event:
                self.on_trade_event(data)

        elif event_type == "order":
            # Order status change
            logger.info(f"User WS order: {data.get('market', '')[:8]}... "
                        f"status={data.get('status', '')} type={data.get('type', '')}")
            if self.on_order_event:
                self.on_order_event(data)

    # -------------------------------------------------------------------------
    # Tuesday Restart Handling
    # -------------------------------------------------------------------------

    def is_tuesday_restart_window(self) -> bool:
        """Check if we're in the Tuesday matching engine restart window."""
        now = datetime.now(ET)
        if now.weekday() != 1:  # Tuesday = 1
            return False
        # Window: 6:59 AM to 7:02 AM ET
        hour_min = now.hour * 60 + now.minute
        return 419 <= hour_min <= 422  # 6:59 to 7:02

    async def handle_tuesday_restart(self):
        """
        Handle the Tuesday 7:00 AM ET matching engine restart.
        Pre-cancel at 6:59 AM, probe with backoff, resume at 7:02 AM.
        """
        if not self.is_tuesday_restart_window():
            return

        logger.warning("Tuesday restart window detected — pre-cancelling all orders")
        if self.client:
            self.client.cancel_all()

        # Wait for restart to complete (probe with exponential backoff)
        backoff = 1
        while backoff <= 16:
            await asyncio.sleep(backoff)
            now = datetime.now(ET)
            if now.hour * 60 + now.minute >= 422:  # Past 7:02 AM
                logger.info("Tuesday restart complete — resuming")
                return
            backoff *= 2

        logger.info("Tuesday restart probe complete — resuming")

    # -------------------------------------------------------------------------
    # Lifecycle
    # -------------------------------------------------------------------------

    async def start(self, token_ids: list = None):
        """Start WebSocket connections. Market channel + user channel (if live)."""
        self._running = True
        token_ids = token_ids or []

        tasks = []
        if token_ids:
            tasks.append(self.connect_market(token_ids))
        tasks.append(self.connect_user())

        logger.info(f"WebSocket manager starting — "
                    f"{len(token_ids)} tokens, "
                    f"user channel={'enabled' if self.client else 'disabled'}")

        await asyncio.gather(*tasks, return_exceptions=True)

    async def stop(self):
        """Gracefully stop all WebSocket connections."""
        self._running = False
        if self._market_ws:
            await self._market_ws.close()
        if self._user_ws:
            await self._user_ws.close()
        logger.info("WebSocket manager stopped")

    @property
    def is_connected(self) -> dict:
        """Connection status for both channels."""
        now = time.time()
        return {
            "market": now - self._last_heartbeat["market"] < 30,
            "user": now - self._last_heartbeat["user"] < 30,
        }
