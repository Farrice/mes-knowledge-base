"""
Data models for the Prediction Market Arb Platform.

All shared dataclasses and enums used across the system.
Designed for JSON serialization (state persistence) and type safety.
"""

from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
from typing import Optional


# =============================================================================
# ENUMS
# =============================================================================

class TradingMode(str, Enum):
    PAPER = "paper"
    LIVE = "live"


class OrderSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(str, Enum):
    GTC = "GTC"   # Good til cancelled
    GTD = "GTD"   # Good til date
    FOK = "FOK"   # Fill or kill
    FAK = "FAK"   # Fill and kill (partial fill ok, cancel remainder)


class ExitReason(str, Enum):
    STOP_LOSS = "stop_loss"
    TRAILING_STOP = "trailing_stop"
    TAKE_PROFIT = "take_profit"
    FORECAST_CHANGE = "forecast_change"
    RESOLUTION = "resolution"
    MANUAL = "manual"
    KILL_SWITCH = "kill_switch"


class OrderStatus(str, Enum):
    PENDING = "PENDING"
    MATCHED = "MATCHED"
    MINED = "MINED"
    CONFIRMED = "CONFIRMED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class KillSwitchLevel(int, Enum):
    NORMAL = 0      # All systems operational
    CAUTION = 1     # New positions blocked, exits allowed
    HALT = 2        # All orders cancelled, no new activity
    EMERGENCY = 3   # Full unwind, manual review required


class StrategyType(str, Enum):
    """Which strategy pipeline generated this opportunity."""
    WEATHER = "weather"         # Weather forecast arbitrage (ECMWF/HRRR/METAR)
    SPORTS_ARB = "sports_arb"   # Sportsbook reference price arbitrage (Vegas Anchor)
    ENSEMBLE = "ensemble"       # Multi-model LLM ensemble (politics/econ/tech)
    MARKET_MAKING = "market_making"  # Reward-optimized liquidity provision


class MarketCategory(str, Enum):
    """Polymarket market category — determines strategy routing."""
    WEATHER = "weather"
    SPORTS = "sports"
    POLITICS = "politics"
    CRYPTO = "crypto"
    ECONOMICS = "economics"
    AI_TECH = "ai_tech"
    ENTERTAINMENT = "entertainment"
    OTHER = "other"


class EdgeType(str, Enum):
    """Classification of WHY an edge exists (from AI Event Analysis SM-5)."""
    INFORMATION_ASYMMETRY = "information_asymmetry"  # EXECUTE — core edge
    NARRATIVE_MISPRICING = "narrative_mispricing"      # EXECUTE — secondary edge
    LOW_LIQUIDITY = "low_liquidity"                    # EXECUTE CAREFULLY
    DATA_ERROR = "data_error"                          # DO NOT EXECUTE
    STRUCTURAL_DIFFERENCE = "structural_difference"    # DO NOT EXECUTE
    UNKNOWN = "unknown"                                # DO NOT EXECUTE


# =============================================================================
# MARKET DATA
# =============================================================================

@dataclass
class Market:
    """A Polymarket prediction market."""
    id: str                          # Market/condition ID
    question: str                    # Market question text
    slug: str = ""                   # URL slug (for weather market matching)
    outcomes: list = field(default_factory=lambda: ["Yes", "No"])
    end_date: str = ""               # ISO format
    volume: float = 0.0              # 24h volume
    active: bool = True
    condition_id: str = ""           # On-chain condition ID
    tokens: list = field(default_factory=list)   # Token IDs for each outcome
    neg_risk: bool = False           # Whether this is a neg-risk market
    category: str = ""               # Market category (weather, sports, etc.)

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Market":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


# =============================================================================
# ORDERS
# =============================================================================

@dataclass
class OrderRequest:
    """An order to be placed (validated by risk manager before execution)."""
    market_id: str
    token_id: str
    side: OrderSide
    price: float
    size: float
    order_type: OrderType = OrderType.GTC
    expiration: Optional[str] = None   # ISO format, for GTD orders
    neg_risk: bool = False

    def to_dict(self) -> dict:
        d = asdict(self)
        d["side"] = self.side.value
        d["order_type"] = self.order_type.value
        return d


@dataclass
class OrderResult:
    """Result of an order placement attempt."""
    order_id: str
    status: OrderStatus
    fill_price: float = 0.0
    fill_size: float = 0.0
    timestamp: str = ""
    error: str = ""
    is_paper: bool = True

    def to_dict(self) -> dict:
        d = asdict(self)
        d["status"] = self.status.value
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "OrderResult":
        d = dict(d)
        if isinstance(d.get("status"), str):
            d["status"] = OrderStatus(d["status"])
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


# =============================================================================
# POSITIONS
# =============================================================================

@dataclass
class Position:
    """An active position (paper or live)."""
    market_id: str
    token_id: str
    side: OrderSide
    entry_price: float
    size: float
    current_price: float = 0.0
    unrealized_pnl: float = 0.0
    entry_time: str = ""
    question: str = ""
    city: str = ""                    # For weather positions
    forecast_temp: Optional[float] = None
    # Exit management
    trailing_stop_level: Optional[float] = None
    trailing_stop_active: bool = False
    stop_loss_price: Optional[float] = None

    @property
    def cost(self) -> float:
        return self.entry_price * self.size

    @property
    def market_value(self) -> float:
        return self.current_price * self.size

    def update_pnl(self, current_price: float):
        self.current_price = current_price
        self.unrealized_pnl = (current_price - self.entry_price) * self.size

    def to_dict(self) -> dict:
        d = asdict(self)
        d["side"] = self.side.value
        d["cost"] = self.cost
        d["market_value"] = self.market_value
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "Position":
        d = dict(d)
        if isinstance(d.get("side"), str):
            d["side"] = OrderSide(d["side"])
        # Remove computed properties that aren't constructor args
        d.pop("cost", None)
        d.pop("market_value", None)
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


# =============================================================================
# WEATHER
# =============================================================================

@dataclass
class ForecastSnapshot:
    """A weather forecast snapshot from multiple sources."""
    city: str
    timestamp: str                    # ISO format
    date: str                         # Target date YYYY-MM-DD
    ecmwf_temp: Optional[float] = None
    hrrr_temp: Optional[float] = None
    metar_temp: Optional[float] = None
    best_temp: Optional[float] = None
    best_source: str = ""
    sigma: float = 2.0                # Current calibrated uncertainty (°F default)
    unit: str = "F"                   # F or C

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "ForecastSnapshot":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


# =============================================================================
# RISK STATE
# =============================================================================

@dataclass
class RiskState:
    """Global risk state — persisted across restarts."""
    daily_pnl: float = 0.0
    daily_pnl_date: str = ""          # Resets when date changes
    peak_balance: float = 0.0
    current_drawdown: float = 0.0     # As fraction of peak
    global_exposure: float = 0.0      # Total capital deployed
    kill_switch_triggered: bool = False
    kill_switch_level: int = 0        # KillSwitchLevel value
    kill_switch_reason: str = ""
    kill_switch_time: str = ""
    blacklist: list = field(default_factory=list)
    whitelist: list = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "RiskState":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


# =============================================================================
# TRADE RECORDS
# =============================================================================

@dataclass
class TradeRecord:
    """A completed trade (entry + exit paired)."""
    trade_id: str
    market_id: str
    question: str = ""
    side: str = ""                    # BUY/SELL
    entry_price: float = 0.0
    exit_price: float = 0.0
    size: float = 0.0
    pnl: float = 0.0
    entry_time: str = ""
    exit_time: str = ""
    exit_reason: str = ""             # ExitReason value
    city: str = ""
    is_paper: bool = True

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "TradeRecord":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


# =============================================================================
# PAPER BALANCE
# =============================================================================

# =============================================================================
# STRATEGY OPPORTUNITIES (Phase 2 — Intelligence Layer)
# =============================================================================

@dataclass
class Opportunity:
    """
    A scored trading opportunity from any strategy pipeline.
    This is the universal format that the market selector ranks across strategies.
    """
    strategy: str                     # StrategyType value
    market_id: str
    token_id: str
    question: str = ""
    category: str = ""                # MarketCategory value
    # Probability estimates
    our_probability: float = 0.0      # Our estimate (from weather/sportsbook/ensemble)
    market_price: float = 0.0         # Current Polymarket price
    # Edge calculation
    edge: float = 0.0                 # our_probability - market_price (raw gap)
    edge_after_fees: float = 0.0      # Edge minus fee drag
    ev: float = 0.0                   # Expected value per dollar
    kelly_f: float = 0.0              # Raw Kelly fraction
    edge_type: str = ""               # EdgeType value — WHY the edge exists
    # Source details
    reference_source: str = ""        # "pinnacle", "ecmwf", "ensemble", etc.
    confidence: float = 0.0           # 0-1 confidence in edge estimate
    # Market metadata
    volume: float = 0.0               # 24h volume
    hours_left: float = 0.0           # Hours to resolution
    neg_risk: bool = False
    # Strategy-specific context (JSON-serializable dict)
    context: dict = field(default_factory=dict)
    # Scoring
    composite_score: float = 0.0      # Market selector's cross-strategy ranking score
    timestamp: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Opportunity":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


@dataclass
class SportsOdds:
    """
    Sportsbook odds for a single event, with vig stripped.
    The reference price for sports arbitrage (GP-1: The Vegas Anchor).
    """
    event_id: str                     # Sportsbook event identifier
    sport: str = ""                   # e.g., "basketball_ncaab", "soccer_epl"
    home_team: str = ""
    away_team: str = ""
    commence_time: str = ""           # ISO format
    # Raw odds (American format from Pinnacle)
    pinnacle_home: float = 0.0        # e.g., -150
    pinnacle_away: float = 0.0        # e.g., +130
    pinnacle_draw: Optional[float] = None  # For 3-way markets (soccer)
    # Vig-stripped true probabilities
    true_prob_home: float = 0.0       # After vig removal
    true_prob_away: float = 0.0
    true_prob_draw: Optional[float] = None
    vig_pct: float = 0.0              # Total overround (e.g., 0.035 for 3.5%)
    # Metadata
    bookmaker: str = "pinnacle"
    last_update: str = ""
    # Polymarket matching
    polymarket_market_id: str = ""    # Matched Polymarket market
    polymarket_question: str = ""
    match_confidence: float = 0.0     # 0-1 fuzzy match quality

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "SportsOdds":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


@dataclass
class EnsembleEstimate:
    """
    Multi-model probability estimate for a single market.
    Implements PolySwarm's 70/30 Bayesian integration (GP-5).
    """
    market_id: str
    question: str = ""
    # Individual model estimates (independent — GP-2)
    model_1_prob: float = 0.0         # GPT-4o-mini (analytical, 40% weight)
    model_1_confidence: float = 0.0
    model_1_reasoning: str = ""
    model_2_prob: float = 0.0         # Haiku 4.5 (credibility, 35% weight)
    model_2_confidence: float = 0.0
    model_2_reasoning: str = ""
    model_3_prob: float = 0.0         # Gemini Flash (contrarian, 25% weight)
    model_3_confidence: float = 0.0
    model_3_reasoning: str = ""
    # Aggregated estimates
    ensemble_prob: float = 0.0        # Weighted average of models
    std_dev: float = 0.0              # Cross-model disagreement
    # Bayesian integration with market
    market_price: float = 0.0
    final_prob: float = 0.0           # 0.70 * ensemble + 0.30 * market
    # Trade signal
    edge: float = 0.0                 # final_prob - market_price
    trade_signal: bool = False        # edge > 5% AND std_dev < 30%
    timestamp: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "EnsembleEstimate":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


@dataclass
class RewardEstimate:
    """
    Estimated market making reward for a market.
    Used for market selection, not execution (quoting engine deferred to Phase 4).
    """
    market_id: str
    question: str = ""
    sport: str = ""
    # Reward pool
    reward_pool_daily: float = 0.0    # Estimated daily reward pool for this market
    # Scoring inputs
    spread_cents: float = 0.0         # Our projected spread in cents
    max_spread_cents: float = 10.0    # v parameter in scoring function
    two_sided: bool = True            # Whether we'd quote both sides
    # Calculated Q score: S(v,s) = ((v-s)/v)^2 * b * (3.0 if two_sided else 1.0)
    q_score: float = 0.0
    # Estimated share of rewards (assumes N competitors)
    estimated_competitors: int = 10
    estimated_daily_reward: float = 0.0
    timestamp: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "RewardEstimate":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


# =============================================================================
# PAPER BALANCE
# =============================================================================

@dataclass
class PaperBalance:
    """Paper trading balance state."""
    initial: float = 1000.0
    current: float = 1000.0
    high_water_mark: float = 1000.0
    total_trades: int = 0
    wins: int = 0
    losses: int = 0

    @property
    def win_rate(self) -> float:
        if self.total_trades == 0:
            return 0.0
        return self.wins / self.total_trades

    @property
    def total_return_pct(self) -> float:
        if self.initial == 0:
            return 0.0
        return (self.current - self.initial) / self.initial * 100

    def to_dict(self) -> dict:
        d = asdict(self)
        d["win_rate"] = self.win_rate
        d["total_return_pct"] = self.total_return_pct
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "PaperBalance":
        d = dict(d)
        d.pop("win_rate", None)
        d.pop("total_return_pct", None)
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})
