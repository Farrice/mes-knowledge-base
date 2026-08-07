"""
State persistence layer for the Prediction Market Arb Platform.

All state is stored as JSON files with atomic writes (write to temp, then rename).
This prevents corruption on crash — a critical requirement for a trading system.

State files:
  .agent/polymarket-paper/state.json        — balance, kill switch, daily PnL
  .agent/polymarket-paper/positions.json    — active positions
  .agent/polymarket-paper/trades.json       — completed trade log (append-only)
  .agent/polymarket-paper/calibration.json  — per-city per-source sigma values
  .agent/polymarket-paper/markets/          — per-market data files
"""

import json
import logging
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from projects.prediction_market_arb.models import (
    PaperBalance, Position, TradeRecord, RiskState, ForecastSnapshot,
)

logger = logging.getLogger("polymarket.state")


class StateManager:
    """JSON-based state persistence with atomic writes."""

    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        self.markets_dir = self.data_dir / "markets"
        self._ensure_dirs()

    def _ensure_dirs(self):
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.markets_dir.mkdir(parents=True, exist_ok=True)

    # -------------------------------------------------------------------------
    # Atomic write — write to temp file in same directory, then rename
    # -------------------------------------------------------------------------

    def _atomic_write(self, path: Path, data: dict):
        """Write JSON atomically: temp file → rename. Prevents corruption on crash."""
        path = Path(path)
        fd, tmp_path = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
        try:
            with os.fdopen(fd, "w") as f:
                json.dump(data, f, indent=2, default=str)
            os.replace(tmp_path, str(path))
        except Exception:
            # Clean up temp file on failure
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
            raise

    def _load_json(self, path: Path, default: any = None):
        """Load JSON file, returning default if missing or corrupt."""
        path = Path(path)
        if not path.exists():
            return default if default is not None else {}
        try:
            with open(path, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            logger.error(f"Failed to load {path}: {e}")
            return default if default is not None else {}

    # -------------------------------------------------------------------------
    # Paper Balance
    # -------------------------------------------------------------------------

    @property
    def _state_path(self) -> Path:
        return self.data_dir / "state.json"

    def load_balance(self) -> PaperBalance:
        data = self._load_json(self._state_path, {})
        balance_data = data.get("balance", {})
        if balance_data:
            return PaperBalance.from_dict(balance_data)
        return PaperBalance()

    def save_balance(self, balance: PaperBalance):
        data = self._load_json(self._state_path, {})
        data["balance"] = balance.to_dict()
        self._atomic_write(self._state_path, data)

    # -------------------------------------------------------------------------
    # Risk State
    # -------------------------------------------------------------------------

    def load_risk_state(self) -> RiskState:
        data = self._load_json(self._state_path, {})
        risk_data = data.get("risk", {})
        if risk_data:
            return RiskState.from_dict(risk_data)
        return RiskState()

    def save_risk_state(self, risk: RiskState):
        data = self._load_json(self._state_path, {})
        data["risk"] = risk.to_dict()
        self._atomic_write(self._state_path, data)

    # -------------------------------------------------------------------------
    # Positions
    # -------------------------------------------------------------------------

    @property
    def _positions_path(self) -> Path:
        return self.data_dir / "positions.json"

    def load_positions(self) -> list:
        data = self._load_json(self._positions_path, [])
        if isinstance(data, list):
            return [Position.from_dict(p) for p in data]
        return []

    def save_positions(self, positions: list):
        data = [p.to_dict() for p in positions]
        self._atomic_write(self._positions_path, data)

    def add_position(self, position: Position):
        positions = self.load_positions()
        positions.append(position)
        self.save_positions(positions)

    def remove_position(self, market_id: str) -> Optional[Position]:
        positions = self.load_positions()
        removed = None
        remaining = []
        for p in positions:
            if p.market_id == market_id and removed is None:
                removed = p
            else:
                remaining.append(p)
        self.save_positions(remaining)
        return removed

    # -------------------------------------------------------------------------
    # Trade Log (append-only)
    # -------------------------------------------------------------------------

    @property
    def _trades_path(self) -> Path:
        return self.data_dir / "trades.json"

    def load_trades(self) -> list:
        data = self._load_json(self._trades_path, [])
        if isinstance(data, list):
            return [TradeRecord.from_dict(t) for t in data]
        return []

    def append_trade(self, trade: TradeRecord):
        """Append a trade to the log. Never overwrites existing trades."""
        trades = self._load_json(self._trades_path, [])
        if not isinstance(trades, list):
            trades = []
        trades.append(trade.to_dict())
        self._atomic_write(self._trades_path, trades)
        logger.info(f"Trade logged: {trade.trade_id} | {trade.side} | PnL: ${trade.pnl:.2f}")

    # -------------------------------------------------------------------------
    # Calibration Data
    # -------------------------------------------------------------------------

    @property
    def _calibration_path(self) -> Path:
        return self.data_dir / "calibration.json"

    def load_calibration(self) -> dict:
        """Load per-city per-source calibration data.

        Format: {city: {source: {"mae": float, "count": int, "sigma": float}}}
        """
        return self._load_json(self._calibration_path, {})

    def save_calibration(self, calibration: dict):
        self._atomic_write(self._calibration_path, calibration)

    def update_calibration(self, city: str, source: str, error: float):
        """Update MAE-based calibration for a city/source pair.

        After calibration_min markets (default 30), the calibrated sigma
        replaces the default sigma for position sizing.
        """
        cal = self.load_calibration()
        if city not in cal:
            cal[city] = {}
        if source not in cal[city]:
            cal[city][source] = {"mae": 0.0, "count": 0, "sigma": None}

        entry = cal[city][source]
        entry["count"] += 1
        # Running MAE: new_mae = old_mae + (|error| - old_mae) / count
        entry["mae"] += (abs(error) - entry["mae"]) / entry["count"]
        # Sigma ≈ MAE * sqrt(π/2) for Gaussian errors
        entry["sigma"] = round(entry["mae"] * 1.2533, 2)

        self.save_calibration(cal)
        logger.info(f"Calibration updated: {city}/{source} — MAE={entry['mae']:.2f}, "
                    f"sigma={entry['sigma']:.2f}, n={entry['count']}")

    # -------------------------------------------------------------------------
    # Per-Market Data (weatherbot pattern)
    # -------------------------------------------------------------------------

    def save_market_data(self, city: str, date: str, data: dict):
        """Save per-market data (forecast snapshots, price history, etc.)."""
        filename = f"{city}_{date}.json"
        path = self.markets_dir / filename
        self._atomic_write(path, data)

    def load_market_data(self, city: str, date: str) -> dict:
        filename = f"{city}_{date}.json"
        path = self.markets_dir / filename
        return self._load_json(path, {})

    def save_forecast_snapshot(self, snapshot: ForecastSnapshot):
        """Append a forecast snapshot to the per-market data file."""
        data = self.load_market_data(snapshot.city, snapshot.date)
        if "snapshots" not in data:
            data["snapshots"] = []
        data["snapshots"].append(snapshot.to_dict())
        self.save_market_data(snapshot.city, snapshot.date, data)
