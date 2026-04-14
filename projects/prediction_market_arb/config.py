"""
Configuration system for the Prediction Market Arb Platform.

Loads config from JSON, merges with defaults, applies environment variable
overrides, validates, and returns a frozen Config object.

Safety architecture:
  - mode defaults to "paper" — must explicitly change
  - Live mode requires BOTH config mode="live" AND env var POLYMARKET_LIVE_ENABLED=true
  - Kelly fraction > 0.25 triggers a warning (0.25 is consensus across all sources)
"""

import json
import logging
import os
import copy
from pathlib import Path
from typing import Any

from projects.prediction_market_arb.constants import (
    CLOB_URL, GAMMA_URL, DATA_URL,
    WS_MARKET_URL, WS_USER_URL,
    POLYGON_CHAIN_ID,
)

logger = logging.getLogger("polymarket.config")


# =============================================================================
# DEFAULTS — every parameter from the Phase 0 extractions
# =============================================================================

DEFAULTS = {
    "mode": "paper",  # THE safety switch — "paper" or "live"

    "api": {
        "clob_url": CLOB_URL,
        "gamma_url": GAMMA_URL,
        "data_url": DATA_URL,
        "ws_market_url": WS_MARKET_URL,
        "ws_user_url": WS_USER_URL,
        "chain_id": POLYGON_CHAIN_ID,
    },

    "trading": {
        "kelly_fraction": 0.25,       # Quarter-Kelly — consensus across all sources
        "max_bet": 20.0,              # Hard dollar cap per trade
        "min_ev": 0.10,               # Minimum expected value to enter
        "max_price": 0.45,            # Price ceiling — avoid expensive contracts
        "max_slippage": 0.03,         # Max bid-ask spread allowed
        "min_volume": 500,            # Minimum market volume
        "min_hours_to_resolution": 2.0,
        "max_hours_to_resolution": 72.0,
        "order_timeout_seconds": 60,
    },

    "risk": {
        "max_position_per_market": 15.0,  # Max $ deployed in a single market
        "max_global_exposure": 50.0,      # Max total $ deployed across all markets
        "max_daily_loss": 10.0,           # Daily loss limit — triggers kill switch
        "max_drawdown_pct": 0.15,         # Max drawdown from peak — triggers kill switch
        "min_24h_volume": 10000,          # Minimum 24h volume for a market
        "kill_switch_enabled": True,
        "blacklist": [],                  # Market IDs to never trade
        "whitelist": [],                  # If set, only trade these market IDs
    },

    "weather": {
        "sigma_f": 2.0,               # Default forecast uncertainty (°F)
        "sigma_c": 1.2,               # Default forecast uncertainty (°C)
        "calibration_min": 30,         # Min resolved markets before calibration applies
        "forecast_sources": ["ecmwf", "hrrr", "metar"],
        "scan_interval": 3600,         # Market scan interval (seconds)
        "monitor_interval": 600,       # Position monitor interval (seconds)
    },

    "exits": {
        "stop_loss_pct": 0.20,         # Exit when price drops 20% below entry
        "trailing_stop_trigger": 0.20, # Activate trailing stop at +20%
        "take_profit_48h_plus": 0.75,  # Take profit threshold (>48h to resolution)
        "take_profit_24_48h": 0.85,    # Take profit threshold (24-48h)
        "forecast_change_buffer_f": 2.0,  # °F buffer before forecast-change exit
        "forecast_change_buffer_c": 1.0,  # °C buffer before forecast-change exit
    },

    "paper": {
        "initial_balance": 1000.0,
        "data_dir": ".agent/polymarket-paper",
        "fill_probability": 0.8,       # Simulated fill rate for paper orders
    },

    # --- Phase 2: Intelligence Layer ---

    "sports": {
        "odds_api_url": "https://api.oddspapi.io/v4",
        "preferred_bookmaker": "pinnacle",
        "min_edge_pct": 0.055,          # Minimum edge after fees (5.5% covers Polymarket fee drag)
        "vig_strip_method": "multiplicative",  # or "power" for heavy favorites
        "vig_strip_power_threshold": 300,      # Switch to Power method when line > -300
        "match_confidence_min": 0.7,           # Min fuzzy match score for event pairing
        "scan_interval": 1800,                 # Scan sportsbook odds every 30 min
        "sports": [                            # Priority order: widest gaps first
            "basketball_ncaab",
            "basketball_nba",
            "soccer_epl",
            "soccer_uefa_champs",
            "mma_mixed_martial_arts",
            "cricket_ipl",
            "americanfootball_nfl",
        ],
    },

    "ensemble": {
        "enabled": True,
        "models": {
            "analytical": {"provider": "openai", "model": "gpt-4o-mini", "weight": 0.40},
            "credibility": {"provider": "anthropic", "model": "claude-haiku-4-5-20251001", "weight": 0.35},
            "contrarian": {"provider": "google", "model": "gemini-2.5-flash", "weight": 0.25},
        },
        "market_weight": 0.30,          # 70/30 Bayesian integration (PolySwarm GP-5)
        "min_edge_pct": 0.05,           # Minimum 5% edge to trigger trade
        "max_std_dev": 0.30,            # Max cross-model disagreement (30%)
        "categories": ["politics", "economics", "ai_tech", "crypto"],
        "max_calls_per_scan": 20,       # Max markets to run ensemble on per scan
        "scan_interval": 3600,          # Scan every 60 min
    },

    "market_selection": {
        "strategy_allocation": {        # Capital allocation by strategy (conservative)
            "weather": 0.30,
            "sports_arb": 0.50,
            "ensemble": 0.20,
        },
        "mm_reserve_pct": 0.0,          # Market making reserve (0% until Phase 4)
        "min_composite_score": 0.5,     # Minimum score to enter
        "max_concurrent_positions": 10,
        "pre_filter": {
            "min_volume": 5000,
            "min_price": 0.05,
            "max_price": 0.95,
            "min_hours_to_resolution": 2.0,
            "max_hours_to_resolution": 168.0,  # 7 days max for ensemble markets
        },
    },
}


# =============================================================================
# CONFIG CLASS
# =============================================================================

class Config:
    """Frozen configuration object with typed property accessors."""

    def __init__(self, data: dict):
        self._data = data
        self._frozen = True

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            return super().__getattribute__(name)
        if name in self._data:
            val = self._data[name]
            if isinstance(val, dict):
                return Config(val)
            return val
        raise AttributeError(f"Config has no attribute '{name}'")

    def __setattr__(self, name: str, value: Any):
        if name.startswith("_"):
            super().__setattr__(name, value)
            return
        if hasattr(self, "_frozen") and self._frozen:
            raise AttributeError("Config is frozen — cannot modify after load")
        super().__setattr__(name, value)

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def to_dict(self) -> dict:
        return copy.deepcopy(self._data)

    @property
    def is_live(self) -> bool:
        """Check if live trading is actually enabled (two-key gate)."""
        config_says_live = self._data.get("mode") == "live"
        env_says_live = os.environ.get("POLYMARKET_LIVE_ENABLED", "").lower() == "true"
        return config_says_live and env_says_live

    @property
    def is_paper(self) -> bool:
        return not self.is_live

    @property
    def private_key(self) -> str:
        """Private key from environment variable only — never stored in config."""
        return os.environ.get("POLYMARKET_PRIVATE_KEY", "")

    @property
    def browser_wallet(self) -> str:
        """Browser wallet address from environment variable."""
        return os.environ.get("POLYMARKET_BROWSER_WALLET", "")

    @property
    def visual_crossing_key(self) -> str:
        """Visual Crossing API key from environment variable."""
        return os.environ.get("VISUAL_CROSSING_KEY", "")


# =============================================================================
# DEEP MERGE
# =============================================================================

def _deep_merge(base: dict, override: dict) -> dict:
    """Deep merge override into base. Override values win."""
    result = copy.deepcopy(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result


# =============================================================================
# VALIDATION
# =============================================================================

def validate_config(data: dict) -> list:
    """Validate configuration values. Returns list of error strings (empty = valid)."""
    errors = []

    # Mode
    mode = data.get("mode", "paper")
    if mode not in ("paper", "live"):
        errors.append(f"mode must be 'paper' or 'live', got '{mode}'")

    # Live mode prerequisites
    if mode == "live":
        if not os.environ.get("POLYMARKET_PRIVATE_KEY"):
            errors.append("Live mode requires POLYMARKET_PRIVATE_KEY environment variable")
        if not os.environ.get("POLYMARKET_BROWSER_WALLET"):
            errors.append("Live mode requires POLYMARKET_BROWSER_WALLET environment variable")
        if os.environ.get("POLYMARKET_LIVE_ENABLED", "").lower() != "true":
            errors.append("Live mode requires POLYMARKET_LIVE_ENABLED=true environment variable")

    # Trading parameters
    trading = data.get("trading", {})
    kelly = trading.get("kelly_fraction", 0.25)
    if not 0 < kelly <= 1.0:
        errors.append(f"kelly_fraction must be in (0, 1.0], got {kelly}")
    if kelly > 0.25:
        logger.warning(
            f"kelly_fraction={kelly} exceeds consensus 0.25. "
            "Quarter-Kelly is the maximum safe value across all studied implementations."
        )

    max_bet = trading.get("max_bet", 20.0)
    if max_bet <= 0:
        errors.append(f"max_bet must be positive, got {max_bet}")

    max_price = trading.get("max_price", 0.45)
    if not 0 < max_price < 1.0:
        errors.append(f"max_price must be in (0, 1.0), got {max_price}")

    min_ev = trading.get("min_ev", 0.10)
    if min_ev < 0:
        errors.append(f"min_ev must be non-negative, got {min_ev}")

    # Risk parameters
    risk = data.get("risk", {})
    max_drawdown = risk.get("max_drawdown_pct", 0.15)
    if not 0 < max_drawdown < 1.0:
        errors.append(f"max_drawdown_pct must be in (0, 1.0), got {max_drawdown}")

    max_daily_loss = risk.get("max_daily_loss", 10.0)
    if max_daily_loss <= 0:
        errors.append(f"max_daily_loss must be positive, got {max_daily_loss}")

    return errors


# =============================================================================
# LOADER
# =============================================================================

def load_config(path: str = None) -> Config:
    """
    Load configuration with the following precedence:
      1. DEFAULTS (built-in)
      2. JSON file (if exists)
      3. Environment variable overrides (secrets only)

    Returns a frozen Config object.
    """
    data = copy.deepcopy(DEFAULTS)

    # Load JSON config if provided or if default exists
    if path is None:
        # Look for config.json in the package directory
        pkg_dir = Path(__file__).parent
        default_path = pkg_dir / "config.json"
        if default_path.exists():
            path = str(default_path)

    if path and os.path.exists(path):
        with open(path, "r") as f:
            file_config = json.load(f)
        data = _deep_merge(data, file_config)
        logger.info(f"Loaded config from {path}")

    # Environment variable overrides for mode
    env_mode = os.environ.get("POLYMARKET_MODE")
    if env_mode:
        data["mode"] = env_mode

    # Validate
    errors = validate_config(data)
    if errors:
        for err in errors:
            logger.error(f"Config validation error: {err}")
        # In paper mode, warnings are non-fatal. In live mode, they're fatal.
        if data.get("mode") == "live":
            raise ValueError(f"Config validation failed for live mode: {'; '.join(errors)}")

    config = Config(data)

    # Log mode
    if config.is_live:
        logger.warning("=== LIVE TRADING MODE ENABLED ===")
    else:
        logger.info("=== PAPER TRADING MODE ===")

    return config
