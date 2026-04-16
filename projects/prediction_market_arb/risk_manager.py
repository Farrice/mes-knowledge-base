"""
Risk Manager — 8-check validation chain, Kelly position sizing, kill switch.

8-Check Sequential Validation Chain (cheapest first, most severe first):
  1. Kill switch status      — O(1), rejects ALL orders if triggered
  2. Market blacklist        — O(1), check against banned market IDs
  3. Whitelist (if set)      — O(1), only allow pre-approved markets
  4. 24h volume minimum      — O(1), reject illiquid markets
  5. Per-market exposure     — O(n), check total exposure in this market
  6. Global exposure ceiling — O(n), check total exposure across all markets
  7. Daily loss limit        — O(1), triggers kill switch if breached
  8. Drawdown from peak      — O(1), triggers kill switch if breached

Kill Switch:
  One-way state machine — once triggered, NO automatic recovery.
  All subsequent orders rejected at check 1.
  Recovery requires manual JSON edit (deliberate friction).

Position Sizing:
  Quarter-Kelly (0.25 fraction) — consensus across every profitable
  implementation studied. Hard dollar cap on top. Price ceiling filter.

Exit Monitoring:
  Five exit mechanisms (from weatherbot extraction):
  1. Stop-loss: 20% below entry
  2. Trailing stop: activates at +20%, floor at breakeven
  3. Take-profit: time-horizon scaled (0.75/0.85/hold)
  4. Forecast-change: 2°F buffer outside bucket
  5. Resolution: market resolves
"""

import logging
import math
import time
from datetime import datetime, timezone
from typing import Optional

from projects.prediction_market_arb.models import (
    OrderRequest, Position, RiskState, KillSwitchLevel, ExitReason,
    OrderSide, PaperBalance,
)
from projects.prediction_market_arb.state import StateManager

logger = logging.getLogger("polymarket.risk")


# =============================================================================
# EXIT SIGNAL
# =============================================================================

class ExitSignal:
    """Signal to close a position, with reason and recommended price."""
    def __init__(self, market_id: str, reason: ExitReason, price: float = 0.0,
                 message: str = ""):
        self.market_id = market_id
        self.reason = reason
        self.price = price
        self.message = message

    def __repr__(self):
        return f"ExitSignal({self.market_id[:8]}..., {self.reason.value}, ${self.price:.3f})"


# =============================================================================
# RISK MANAGER
# =============================================================================

class TokenCircuitBreaker:
    """
    Per-token circuit breaker — isolates misbehaving tokens without halting all trading.

    Extracted from braedonsaunders/homerun. Trips on:
      - 2+ large trades (size > threshold) within 30 seconds on the same token
      - 5 consecutive API errors per token

    Auto-expires after 120 seconds. Sits between kill switch (nuclear) and
    normal validation (per-trade). A flash crash on one weather market
    shouldn't freeze the sports arb pipeline.
    """

    def __init__(self, trip_window_s: float = 30.0, expire_s: float = 120.0,
                 max_rapid_trades: int = 2, max_errors: int = 5):
        self._trips = {}       # {token_id: trip_timestamp}
        self._trade_times = {} # {token_id: [timestamps]}
        self._error_counts = {} # {token_id: count}
        self.trip_window = trip_window_s
        self.expire_s = expire_s
        self.max_rapid = max_rapid_trades
        self.max_errors = max_errors

    def is_tripped(self, token_id: str) -> bool:
        """Check if a token's circuit breaker is currently tripped."""
        if token_id not in self._trips:
            return False
        elapsed = time.time() - self._trips[token_id]
        if elapsed > self.expire_s:
            # Auto-expire
            del self._trips[token_id]
            self._error_counts.pop(token_id, None)
            self._trade_times.pop(token_id, None)
            logger.info(f"Circuit breaker expired for token {token_id[:8]}...")
            return False
        return True

    def record_trade(self, token_id: str):
        """Record a trade for rapid-trade detection."""
        now = time.time()
        if token_id not in self._trade_times:
            self._trade_times[token_id] = []
        self._trade_times[token_id].append(now)
        # Clean old timestamps
        self._trade_times[token_id] = [
            t for t in self._trade_times[token_id]
            if now - t < self.trip_window
        ]
        # Check for rapid trading
        if len(self._trade_times[token_id]) >= self.max_rapid:
            self._trip(token_id, "rapid trades detected")

    def record_error(self, token_id: str):
        """Record an API error for error-count detection."""
        self._error_counts[token_id] = self._error_counts.get(token_id, 0) + 1
        if self._error_counts[token_id] >= self.max_errors:
            self._trip(token_id, f"{self.max_errors} consecutive errors")

    def clear_errors(self, token_id: str):
        """Clear error count on successful operation."""
        self._error_counts.pop(token_id, None)

    def _trip(self, token_id: str, reason: str):
        """Trip the circuit breaker for a specific token."""
        self._trips[token_id] = time.time()
        logger.warning(f"Circuit breaker TRIPPED for {token_id[:8]}...: {reason} "
                       f"(expires in {self.expire_s}s)")

    def get_status(self) -> dict:
        """Get current circuit breaker state."""
        now = time.time()
        active = {
            tid: round(self.expire_s - (now - ts), 1)
            for tid, ts in self._trips.items()
            if now - ts < self.expire_s
        }
        return {"active_trips": len(active), "tokens": active}


class RiskManager:
    """
    Capital protection layer. Sits between every strategy and the execution layer.
    No order reaches the API without passing all 8 checks + circuit breaker.
    """

    def __init__(self, config, state_manager: StateManager):
        self.config = config
        self.state = state_manager
        self.circuit_breaker = TokenCircuitBreaker()

    # -------------------------------------------------------------------------
    # 8-CHECK VALIDATION CHAIN
    # -------------------------------------------------------------------------

    def check_order(self, order: OrderRequest, market_volume: float = 0.0) -> tuple:
        """
        Run the 8-check sequential validation chain.

        Returns (passed: bool, reason: str).
        If passed=True, reason is empty.
        If passed=False, reason describes which check failed and why.

        Checks are ordered cheapest-first. If check N fails,
        checks N+1 through 8 never run.
        """
        risk = self.state.load_risk_state()
        positions = self.state.load_positions()
        balance = self.state.load_balance()

        # --- CHECK 1: Kill switch (nuclear — halts ALL trading) ---
        if risk.kill_switch_triggered:
            return (False, f"Kill switch triggered: {risk.kill_switch_reason}")

        # --- CHECK 1.5: Token circuit breaker (per-token isolation) ---
        if order.token_id and self.circuit_breaker.is_tripped(order.token_id):
            return (False, f"Circuit breaker tripped for token {order.token_id[:8]}...")

        # --- CHECK 2: Market blacklist ---
        if order.market_id in risk.blacklist:
            return (False, f"Market {order.market_id[:8]}... is blacklisted")

        # --- CHECK 3: Whitelist (if set) ---
        if risk.whitelist and order.market_id not in risk.whitelist:
            return (False, f"Market {order.market_id[:8]}... not in whitelist")

        # --- CHECK 4: 24h volume ---
        min_volume = self.config.risk.min_24h_volume
        if market_volume < min_volume:
            return (False, f"Market volume ${market_volume:.0f} < "
                           f"minimum ${min_volume:.0f}")

        # --- CHECK 5: Per-market exposure ---
        market_exposure = sum(
            p.cost for p in positions if p.market_id == order.market_id
        )
        order_cost = order.price * order.size
        projected = market_exposure + order_cost
        max_per_market = self.config.risk.max_position_per_market
        if projected > max_per_market:
            return (False, f"Per-market exposure ${projected:.2f} would exceed "
                           f"limit ${max_per_market:.2f}")

        # --- CHECK 6: Global exposure ---
        global_exposure = sum(p.cost for p in positions) + order_cost
        max_global = self.config.risk.max_global_exposure
        if global_exposure > max_global:
            return (False, f"Global exposure ${global_exposure:.2f} would exceed "
                           f"ceiling ${max_global:.2f}")

        # --- CHECK 7: Daily loss limit ---
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        if risk.daily_pnl_date != today:
            # Reset daily PnL on new day
            risk.daily_pnl = 0.0
            risk.daily_pnl_date = today
            self.state.save_risk_state(risk)

        max_daily_loss = self.config.risk.max_daily_loss
        if risk.daily_pnl < -max_daily_loss:
            self._trigger_kill_switch(
                risk, KillSwitchLevel.HALT,
                f"Daily loss ${abs(risk.daily_pnl):.2f} exceeds limit ${max_daily_loss:.2f}"
            )
            return (False, f"Daily loss limit breached — kill switch triggered")

        # --- CHECK 8: Drawdown from peak ---
        if balance.high_water_mark > 0:
            drawdown = (balance.high_water_mark - balance.current) / balance.high_water_mark
            max_drawdown = self.config.risk.max_drawdown_pct
            if drawdown > max_drawdown:
                self._trigger_kill_switch(
                    risk, KillSwitchLevel.HALT,
                    f"Drawdown {drawdown:.1%} exceeds limit {max_drawdown:.1%}"
                )
                return (False, f"Drawdown limit breached — kill switch triggered")

        return (True, "")

    # -------------------------------------------------------------------------
    # KILL SWITCH (one-way state machine)
    # -------------------------------------------------------------------------

    def _trigger_kill_switch(self, risk: RiskState, level: KillSwitchLevel,
                             reason: str):
        """
        Trigger the kill switch. ONE-WAY — no programmatic reset.
        Recovery requires manual edit of state.json.
        """
        risk.kill_switch_triggered = True
        risk.kill_switch_level = level.value
        risk.kill_switch_reason = reason
        risk.kill_switch_time = datetime.now(timezone.utc).isoformat()
        self.state.save_risk_state(risk)

        logger.critical(f"KILL SWITCH TRIGGERED (level {level.value}): {reason}")
        logger.critical("All trading halted. Manual review required.")
        logger.critical("To reset: edit .agent/polymarket-paper/state.json → "
                        "set risk.kill_switch_triggered = false")

    def get_kill_switch_status(self) -> dict:
        """Get current kill switch state."""
        risk = self.state.load_risk_state()
        return {
            "triggered": risk.kill_switch_triggered,
            "level": risk.kill_switch_level,
            "reason": risk.kill_switch_reason,
            "time": risk.kill_switch_time,
        }

    # -------------------------------------------------------------------------
    # KELLY POSITION SIZING
    # -------------------------------------------------------------------------

    def calc_position_size(self, probability: float, price: float,
                           balance: float = None) -> float:
        """
        Calculate position size using fractional Kelly criterion.

        Kelly formula: f* = (p*b - (1-p)) / b
        where p = probability, b = payout odds = (1/price) - 1

        Then: f_adj = f* × kelly_fraction (default 0.25)
        Then: capped at max_bet

        Returns dollar amount to wager (0 if no edge).
        """
        if balance is None:
            balance = self.state.load_balance().current

        if probability <= 0 or probability >= 1.0:
            return 0.0
        if price <= 0 or price >= 1.0:
            return 0.0

        b = (1.0 / price) - 1.0
        if b <= 0:
            return 0.0

        # Raw Kelly fraction
        f_star = (probability * b - (1.0 - probability)) / b
        if f_star <= 0:
            return 0.0

        # Apply fractional Kelly
        kelly_fraction = self.config.trading.kelly_fraction
        f_adj = f_star * kelly_fraction

        # Dollar amount
        raw = f_adj * balance

        # Hard dollar cap
        max_bet = self.config.trading.max_bet
        capped = min(raw, max_bet)

        # Noise filter — don't place tiny bets
        if capped < 0.50:
            return 0.0

        return round(capped, 2)

    # -------------------------------------------------------------------------
    # EXIT MONITORING
    # -------------------------------------------------------------------------

    def check_exits(self, positions: list, forecasts: dict = None) -> list:
        """
        Check all positions for exit conditions.

        Five exit mechanisms:
          1. Stop-loss: price drops > stop_loss_pct below entry
          2. Trailing stop: activates at +trailing_stop_trigger, floor at breakeven
          3. Take-profit: time-horizon scaled thresholds
          4. Forecast-change: forecast moved outside bucket by > buffer
          5. Resolution: market resolved (checked separately)

        Returns list of ExitSignal objects.
        """
        signals = []
        forecasts = forecasts or {}

        for pos in positions:
            if pos.current_price <= 0:
                continue

            # 1. Stop-loss
            stop_pct = self.config.exits.stop_loss_pct
            stop_price = pos.entry_price * (1.0 - stop_pct)
            if pos.current_price < stop_price:
                signals.append(ExitSignal(
                    market_id=pos.market_id,
                    reason=ExitReason.STOP_LOSS,
                    price=pos.current_price,
                    message=f"Price ${pos.current_price:.3f} below stop "
                            f"${stop_price:.3f} ({stop_pct:.0%} loss)",
                ))
                continue

            # 2. Trailing stop
            pnl_pct = (pos.current_price - pos.entry_price) / pos.entry_price
            trigger_pct = self.config.exits.trailing_stop_trigger

            if pnl_pct >= trigger_pct:
                # Activate trailing stop — floor at breakeven
                pos.trailing_stop_active = True
                # Update trailing stop level (only moves up, never down)
                new_level = max(
                    pos.trailing_stop_level or pos.entry_price,
                    pos.entry_price,  # Floor at breakeven
                )
                pos.trailing_stop_level = new_level

            if pos.trailing_stop_active and pos.trailing_stop_level:
                if pos.current_price < pos.trailing_stop_level:
                    signals.append(ExitSignal(
                        market_id=pos.market_id,
                        reason=ExitReason.TRAILING_STOP,
                        price=pos.current_price,
                        message=f"Price ${pos.current_price:.3f} below trailing "
                                f"stop ${pos.trailing_stop_level:.3f}",
                    ))
                    continue

            # 3. Take-profit (time-horizon scaled)
            hours_left = self._hours_to_resolution(pos)
            if hours_left > 48:
                tp_threshold = self.config.exits.take_profit_48h_plus
            elif hours_left > 24:
                tp_threshold = self.config.exits.take_profit_24_48h
            else:
                tp_threshold = None  # Hold to resolution within 24h

            if tp_threshold and pos.current_price >= tp_threshold:
                signals.append(ExitSignal(
                    market_id=pos.market_id,
                    reason=ExitReason.TAKE_PROFIT,
                    price=pos.current_price,
                    message=f"Price ${pos.current_price:.3f} >= take-profit "
                            f"${tp_threshold:.3f} ({hours_left:.0f}h left)",
                ))
                continue

            # 4. Forecast-change exit
            if pos.city and pos.city in forecasts:
                forecast = forecasts[pos.city]
                if forecast and forecast.best_temp is not None and pos.forecast_temp is not None:
                    buffer = (self.config.exits.forecast_change_buffer_f
                              if forecast.unit == "F"
                              else self.config.exits.forecast_change_buffer_c)
                    temp_diff = abs(forecast.best_temp - pos.forecast_temp)
                    if temp_diff > buffer:
                        signals.append(ExitSignal(
                            market_id=pos.market_id,
                            reason=ExitReason.FORECAST_CHANGE,
                            price=pos.current_price,
                            message=f"Forecast changed {temp_diff:.1f}° "
                                    f"(entry={pos.forecast_temp}°, "
                                    f"now={forecast.best_temp}°, "
                                    f"buffer={buffer}°)",
                        ))
                        continue

        return signals

    def _hours_to_resolution(self, position: Position) -> float:
        """Estimate hours until a position's market resolves."""
        import re
        from projects.prediction_market_arb.constants import MONTHS

        if position.question:
            for i, month in enumerate(MONTHS):
                pattern = rf'{month}\s+(\d+),?\s+(\d{{4}})'
                m = re.search(pattern, position.question, re.IGNORECASE)
                if m:
                    day = int(m.group(1))
                    year = int(m.group(2))
                    # Assume resolution at end of day UTC
                    resolution_dt = datetime(year, i + 1, day, 23, 59, 59,
                                             tzinfo=timezone.utc)
                    now = datetime.now(timezone.utc)
                    hours = (resolution_dt - now).total_seconds() / 3600.0
                    return max(hours, 0.0)

        # Fallback: assume 48 hours
        return 48.0

    # -------------------------------------------------------------------------
    # PNL TRACKING
    # -------------------------------------------------------------------------

    def record_trade_pnl(self, pnl: float):
        """Record a realized P&L and update risk state."""
        risk = self.state.load_risk_state()
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        # Reset daily PnL on new day
        if risk.daily_pnl_date != today:
            risk.daily_pnl = 0.0
            risk.daily_pnl_date = today

        risk.daily_pnl += pnl

        # Update balance high water mark
        balance = self.state.load_balance()
        if balance.current > balance.high_water_mark:
            balance.high_water_mark = balance.current
            self.state.save_balance(balance)

        # Update drawdown
        if balance.high_water_mark > 0:
            risk.current_drawdown = (
                (balance.high_water_mark - balance.current) / balance.high_water_mark
            )

        # Update global exposure
        positions = self.state.load_positions()
        risk.global_exposure = sum(p.cost for p in positions)

        self.state.save_risk_state(risk)

        # Check if daily loss or drawdown limits are now breached
        if risk.daily_pnl < -self.config.risk.max_daily_loss:
            self._trigger_kill_switch(
                risk, KillSwitchLevel.HALT,
                f"Daily loss ${abs(risk.daily_pnl):.2f} exceeds "
                f"limit ${self.config.risk.max_daily_loss:.2f}"
            )

        if risk.current_drawdown > self.config.risk.max_drawdown_pct:
            self._trigger_kill_switch(
                risk, KillSwitchLevel.HALT,
                f"Drawdown {risk.current_drawdown:.1%} exceeds "
                f"limit {self.config.risk.max_drawdown_pct:.1%}"
            )

    # -------------------------------------------------------------------------
    # STATUS
    # -------------------------------------------------------------------------

    def get_status(self) -> dict:
        """Get comprehensive risk status."""
        risk = self.state.load_risk_state()
        balance = self.state.load_balance()
        positions = self.state.load_positions()

        return {
            "kill_switch": {
                "triggered": risk.kill_switch_triggered,
                "level": risk.kill_switch_level,
                "reason": risk.kill_switch_reason,
                "time": risk.kill_switch_time,
            },
            "balance": {
                "current": balance.current,
                "initial": balance.initial,
                "high_water_mark": balance.high_water_mark,
                "return_pct": balance.total_return_pct,
            },
            "exposure": {
                "global": sum(p.cost for p in positions),
                "max_global": self.config.risk.max_global_exposure,
                "positions": len(positions),
            },
            "daily_pnl": {
                "amount": risk.daily_pnl,
                "date": risk.daily_pnl_date,
                "max_loss": self.config.risk.max_daily_loss,
            },
            "drawdown": {
                "current": risk.current_drawdown,
                "max_allowed": self.config.risk.max_drawdown_pct,
            },
            "trades": {
                "total": balance.total_trades,
                "wins": balance.wins,
                "losses": balance.losses,
                "win_rate": balance.win_rate,
            },
        }
