# Polymarket Arbitrage Bot — Source Code & Architecture
## Fetched: 2026-04-13
## Source: https://github.com/ImMike/polymarket-arbitrage
## Purpose: Risk management patterns, execution architecture, cross-platform arbitrage logic for MES 3.0 extraction

---

### Repository Overview

**Repository**: ImMike/polymarket-arbitrage (82 stars, 47 forks, MIT License)
**Stack**: Python 3.10+, FastAPI dashboard, async architecture
**Description**: Cross-platform arbitrage detection bot for prediction markets — monitors 10,000+ markets across Polymarket and Kalshi.

**Core Features**:
- Cross-Platform Arbitrage: Price differences between Polymarket and Kalshi
- Bundle Arbitrage: YES + NO price deviations from $1.00
- Market Making: Captures spreads through competitive bid/ask placement
- Risk Management: Position limits, loss caps, automated kill switch
- Live Dashboard: FastAPI web UI at localhost:8000
- Market Matching AI: Text similarity for cross-platform market matching

---

### Page: Project Structure

```
polymarket-arbitrage/
├── main.py
├── run_with_dashboard.py
├── config.yaml
├── requirements.txt
├── polymarket_client/          # API client
├── kalshi_client/              # Kalshi API client
├── core/
│   ├── data_feed.py            # Market data ingestion
│   ├── arb_engine.py           # Arbitrage detection
│   ├── cross_platform_arb.py   # Polymarket <-> Kalshi arb
│   ├── execution.py            # Order execution engine
│   ├── risk_manager.py         # Risk controls
│   └── portfolio.py            # Position tracking
├── dashboard/                  # FastAPI web UI
├── utils/                      # Config, logging, backtesting
├── tests/                      # Unit tests
└── logs/                       # Auto-created
```

---

### Page: config.yaml (Full Configuration)

```yaml
api:
  # Polymarket API endpoints
  polymarket_rest_url: "https://clob.polymarket.com"
  polymarket_ws_url: "wss://ws-subscriptions-clob.polymarket.com/ws/market"
  gamma_api_url: "https://gamma-api.polymarket.com"
  
  # Kalshi API endpoint (public, no auth needed for market data)
  kalshi_api_url: "https://api.elections.kalshi.com/trade-api/v2"
  
  # Authentication (replace with your credentials)
  api_key: "YOUR_API_KEY_HERE"
  api_secret: "YOUR_API_SECRET_HERE"
  passphrase: "YOUR_PASSPHRASE_HERE"
  
  # Wallet configuration
  private_key: "YOUR_PRIVATE_KEY_HERE"
  
  # Request settings
  timeout_seconds: 30
  max_retries: 3
  retry_delay_seconds: 1

trading:
  # Markets to trade (empty list = auto-discover active markets)
  markets: []
  
  # Arbitrage settings
  min_edge: 0.01           # 1% edge required for bundle arbitrage
  bundle_arb_enabled: true
  
  # Market-making settings
  min_spread: 0.05         # 5c spread to act as market maker
  tick_size: 0.01          # Minimum price increment
  mm_enabled: false        # Disabled for real data (markets too efficient)
  
  # Order sizing - SMALL for $50 budget
  default_order_size: 5    # $5 per order
  min_order_size: 2        # $2 minimum
  max_order_size: 10       # $10 max per order
  
  # Execution settings
  slippage_tolerance: 0.02  # Max allowed slippage from signal to execution
  order_timeout_seconds: 60 # Cancel unfilled orders after this time
  
  # Fees (Polymarket rates - conservative estimates)
  maker_fee_bps: 0          # 0% for maker (limit orders adding liquidity)
  taker_fee_bps: 150        # 1.5% for taker (taking liquidity)
  estimated_gas_per_order: 0.02  # ~$0.02 gas on Polygon

risk:
  # Position limits - CONSERVATIVE for $50 budget
  max_position_per_market: 15    # Max $15 per market
  max_global_exposure: 50        # Max $50 total
  
  # Loss limits - tight stops
  max_daily_loss: 10             # Stop if losing $10/day
  max_drawdown_pct: 0.15         # 15% max drawdown from peak
  
  # Market filters
  trade_only_high_volume: false
  min_24h_volume: 10000
  
  # Kill switch
  kill_switch_enabled: true
  auto_unwind_on_breach: false

mode:
  # Trading mode: "live" or "dry_run"
  trading_mode: "dry_run"
  
  # Data mode: "real" or "simulation"
  data_mode: "real"
  
  # Cross-platform arbitrage
  cross_platform_enabled: true
  kalshi_enabled: true
  min_match_similarity: 0.6       # Minimum similarity score for market matching (0-1)
  
  # Dry run settings
  dry_run_initial_balance: 10000
  simulate_fills: true
  fill_probability: 0.8

logging:
  console_level: "INFO"
  file_level: "DEBUG"
  log_dir: "logs"
  main_log_file: "bot.log"
  trades_log_file: "trades.log"
  opportunities_log_file: "opportunities.log"
  max_log_size_mb: 50
  backup_count: 5

monitoring:
  snapshot_interval: 60
  heartbeat_interval: 30
  track_latency: true
  track_fill_rates: true
```

---

### Page: core/risk_manager.py (Complete Source)

```python
"""
Risk Manager Module
====================

Enforces position limits, loss limits, and other risk constraints.
"""

import logging
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional, Set

from polymarket_client.models import Order, OrderSide, TokenType, Trade


logger = logging.getLogger(__name__)


@dataclass
class RiskConfig:
    """Configuration for risk management."""
    # Position limits
    max_position_per_market: float = 200.0  # Max notional per market
    max_global_exposure: float = 5000.0  # Max total exposure
    
    # Loss limits
    max_daily_loss: float = 500.0
    max_drawdown_pct: float = 0.10  # 10% max drawdown from peak
    
    # Market filters
    trade_only_high_volume: bool = True
    min_24h_volume: float = 10000.0
    
    # Whitelist/blacklist
    whitelist: list[str] = field(default_factory=list)
    blacklist: list[str] = field(default_factory=list)
    
    # Kill switch
    kill_switch_enabled: bool = True
    auto_unwind_on_breach: bool = False


@dataclass
class RiskState:
    """Current risk state."""
    daily_pnl: float = 0.0
    peak_pnl: float = 0.0
    current_drawdown: float = 0.0
    global_exposure: float = 0.0
    kill_switch_triggered: bool = False
    kill_switch_reason: str = ""
    last_check: datetime = field(default_factory=datetime.utcnow)


class RiskManager:
    """
    Risk management system.
    
    Validates orders against risk limits and monitors overall exposure.
    Can trigger a kill switch to stop all trading.
    """
    
    def __init__(self, config: RiskConfig):
        self.config = config
        self.state = RiskState()
        self._market_exposure: dict[str, float] = {}
        self._market_volumes: dict[str, float] = {}
        self._session_start = datetime.utcnow()
        self._session_trades: list[Trade] = []
    
    def check_order(self, order: Order) -> bool:
        """
        Check if an order passes all risk checks.
        Returns True if allowed, False otherwise.
        
        Checks performed (in order):
        1. Kill switch status
        2. Market blacklist
        3. Whitelist (if non-empty)
        4. 24h volume minimum
        5. Per-market exposure limit
        6. Global exposure limit
        7. Daily loss limit (triggers kill switch if breached)
        8. Drawdown limit (triggers kill switch if breached)
        """
        # Kill switch check
        if self.state.kill_switch_triggered:
            return False
        
        # Market blacklist check
        if order.market_id in self.config.blacklist:
            return False
        
        # Whitelist check (if whitelist is non-empty)
        if self.config.whitelist and order.market_id not in self.config.whitelist:
            return False
        
        # Volume check
        if self.config.trade_only_high_volume:
            market_volume = self._market_volumes.get(order.market_id, 0)
            if market_volume < self.config.min_24h_volume:
                return False
        
        # Per-market exposure check
        current_market_exposure = self._market_exposure.get(order.market_id, 0)
        new_exposure = order.notional if order.side == OrderSide.BUY else -order.notional
        projected_exposure = abs(current_market_exposure + new_exposure)
        
        if projected_exposure > self.config.max_position_per_market:
            return False
        
        # Global exposure check
        projected_global = self.state.global_exposure + abs(new_exposure)
        if projected_global > self.config.max_global_exposure:
            return False
        
        # Daily loss check
        if self.state.daily_pnl < -self.config.max_daily_loss:
            if self.config.kill_switch_enabled:
                self._trigger_kill_switch("Daily loss limit exceeded")
            return False
        
        # Drawdown check
        if self.state.current_drawdown > self.config.max_drawdown_pct:
            if self.config.kill_switch_enabled:
                self._trigger_kill_switch("Drawdown limit exceeded")
            return False
        
        return True
    
    def update_position(self, market_id, token_type, size_delta, price):
        """Update position tracking after a trade."""
        notional_change = abs(size_delta * price)
        if market_id not in self._market_exposure:
            self._market_exposure[market_id] = 0.0
        if size_delta > 0:
            self._market_exposure[market_id] += notional_change
            self.state.global_exposure += notional_change
        else:
            self._market_exposure[market_id] -= notional_change
            self.state.global_exposure -= notional_change
        self._market_exposure[market_id] = max(0, self._market_exposure[market_id])
        self.state.global_exposure = max(0, self.state.global_exposure)
    
    def update_pnl(self, realized_pnl, unrealized_pnl):
        """Update PnL tracking with drawdown calculation."""
        total_pnl = realized_pnl + unrealized_pnl
        self.state.daily_pnl = total_pnl
        if total_pnl > self.state.peak_pnl:
            self.state.peak_pnl = total_pnl
        if self.state.peak_pnl > 0:
            self.state.current_drawdown = (self.state.peak_pnl - total_pnl) / self.state.peak_pnl
        else:
            self.state.current_drawdown = 0.0
        # Auto-trigger kill switch on breach
        if total_pnl < -self.config.max_daily_loss:
            if self.config.kill_switch_enabled and not self.state.kill_switch_triggered:
                self._trigger_kill_switch("Daily loss limit exceeded")
        if self.state.current_drawdown > self.config.max_drawdown_pct:
            if self.config.kill_switch_enabled and not self.state.kill_switch_triggered:
                self._trigger_kill_switch("Drawdown limit exceeded")
    
    def _trigger_kill_switch(self, reason):
        self.state.kill_switch_triggered = True
        self.state.kill_switch_reason = reason
        logger.critical(f"KILL SWITCH TRIGGERED: {reason}")
    
    def get_available_exposure(self, market_id):
        current = self._market_exposure.get(market_id, 0.0)
        return max(0, self.config.max_position_per_market - current)
    
    def get_summary(self):
        return {
            "global_exposure": self.state.global_exposure,
            "max_global_exposure": self.config.max_global_exposure,
            "utilization_pct": (self.state.global_exposure / self.config.max_global_exposure * 100
                               if self.config.max_global_exposure > 0 else 0),
            "daily_pnl": self.state.daily_pnl,
            "max_daily_loss": self.config.max_daily_loss,
            "peak_pnl": self.state.peak_pnl,
            "current_drawdown_pct": self.state.current_drawdown * 100,
            "max_drawdown_pct": self.config.max_drawdown_pct * 100,
            "kill_switch_triggered": self.state.kill_switch_triggered,
            "kill_switch_reason": self.state.kill_switch_reason,
            "markets_with_exposure": len([m for m, e in self._market_exposure.items() if e > 0]),
            "session_trade_count": len(self._session_trades),
            "within_limits": self.within_global_limits(),
        }
```

---

### Page: core/cross_platform_arb.py (Complete Source)

```python
"""
Cross-Platform Arbitrage Engine
===============================

Detects arbitrage opportunities between Polymarket and Kalshi prediction markets.
"""

import asyncio
import logging
import re
from dataclasses import dataclass, field
from datetime import datetime
from difflib import SequenceMatcher
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class MarketPair:
    """A matched pair of markets on Polymarket and Kalshi."""
    polymarket_id: str
    kalshi_ticker: str
    polymarket_question: str
    kalshi_title: str
    similarity_score: float
    category: str = ""
    matched_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class CrossPlatformOpportunity:
    """Arbitrage opportunity between Polymarket and Kalshi."""
    opportunity_id: str
    market_pair: MarketPair
    buy_platform: str       # "polymarket" or "kalshi"
    sell_platform: str
    token: str              # "YES" or "NO"
    buy_price: float
    sell_price: float
    gross_edge: float       # sell_price - buy_price
    net_edge: float         # After fees
    edge_pct: float         # As percentage
    suggested_size: float = 0.0
    max_size: float = 0.0   # Limited by liquidity on both sides
    buy_liquidity: float = 0.0
    sell_liquidity: float = 0.0
    detected_at: datetime = field(default_factory=datetime.utcnow)


class MarketMatcher:
    """
    Matches similar markets between Polymarket and Kalshi.
    Uses text similarity, keyword matching, and sports-specific logic.
    
    Matching strategies (in priority order):
    1. Sports team + date matching (0.95 confidence for exact match)
    2. Person/politician matching (0.85 for same person + same prediction type)
    3. Fuzzy text similarity + entity overlap
    4. Category boosting (same sport/crypto type)
    """
    
    NOISE_WORDS = {"will", "the", "a", "an", "be", "to", "in", "on", "by", "at",
                   "what", "who", "which", "when", "is", "are", "was", "were",
                   "market", "prediction", "bet", "odds", "win", "winner"}
    
    # NFL (32 teams) and NBA (30 teams) team name mappings included
    # Full reverse lookup for team names -> canonical names
    
    def calculate_similarity(self, polymarket_question, kalshi_title) -> float:
        """Multi-strategy similarity scoring."""
        # 1. Sports team match (highest priority)
        is_sports, sports_score = self.is_sports_match(polymarket_question, kalshi_title)
        if is_sports and sports_score > 0.7:
            return sports_score
        
        # 2. Person/event match
        is_person, person_score = self.is_same_person_event(polymarket_question, kalshi_title)
        if is_person and person_score > 0.7:
            return person_score
        
        # 3. Fuzzy text + entity overlap
        norm_poly = self.normalize_text(polymarket_question)
        norm_kalshi = self.normalize_text(kalshi_title)
        text_sim = SequenceMatcher(None, norm_poly, norm_kalshi).ratio()
        
        poly_entities = self.extract_key_entities(polymarket_question)
        kalshi_entities = self.extract_key_entities(kalshi_title)
        if poly_entities and kalshi_entities:
            entity_overlap = len(poly_entities & kalshi_entities) / max(len(poly_entities), len(kalshi_entities))
            combined_sim = 0.5 * text_sim + 0.5 * entity_overlap
        else:
            combined_sim = text_sim
        
        # 4. Category boosting
        # Same sport type: +0.15
        # Same crypto coin: +0.20
        
        return combined_sim
    
    async def find_matches(self, polymarket_markets, kalshi_markets):
        """Category-based matching with progress tracking."""
        # Group by category (politics, crypto, finance, sports, entertainment, tech)
        # Match within categories only (skip 'other')
        # Yields every 500 comparisons to keep event loop responsive
        pass


class CrossPlatformArbEngine:
    """
    Detects profitable price discrepancies across platforms.
    
    Checks all 4 arbitrage directions for each matched pair:
    1. Buy YES on Polymarket, sell YES on Kalshi
    2. Buy YES on Kalshi, sell YES on Polymarket
    3. Buy NO on Polymarket, sell NO on Kalshi
    4. Buy NO on Kalshi, sell NO on Polymarket
    """
    
    def __init__(self,
                 min_edge=0.02,                # 2% minimum edge
                 polymarket_taker_fee=0.015,   # 1.5%
                 kalshi_taker_fee=0.01,        # ~1% estimate
                 gas_cost=0.02):               # Gas cost per order
        self.min_edge = min_edge
        self.polymarket_taker_fee = polymarket_taker_fee
        self.kalshi_taker_fee = kalshi_taker_fee
        self.gas_cost = gas_cost
        self.matcher = MarketMatcher()
    
    def check_arbitrage(self, market_pair, polymarket_ob, kalshi_ob):
        """
        Fee calculation per direction:
        gross = sell_price - buy_price
        fees = (buy_price * buy_platform_taker_fee + 
                sell_price * sell_platform_taker_fee + 
                gas_cost * 2)
        net = gross - fees
        
        Only signals if net >= min_edge.
        
        Size limited by min(buy_liquidity, sell_liquidity, $100 safety cap).
        """
        pass
```

---

### Page: core/arb_engine.py (Architecture Summary)

**ArbConfig** operational parameters:
- Bundle arbitrage thresholds: 1% minimum edge
- Market-making spreads: 5 cents minimum
- Order sizing: 5-200 unit range
- Fee structures: 1.5% taker, ~$0.02 gas per order

**ArbEngine** detection strategies:

1. **Bundle Arbitrage**: Identifies YES/NO token mispricing
   - Long: `ask_yes + ask_no < $1.00` (buy both, guaranteed $1 payout)
   - Short: `bid_yes + bid_no > $1.00` (sell both, lock premium)
   - Net edge = gross edge - (taker fees + gas costs)

2. **Market Making**: Detects spreads wide enough (>= 5c) to place inside
   - Bid slightly above best bid, ask slightly below best ask

**Features**:
- Opportunity lifespan tracking (duration buckets: <100ms, 500ms, 1s, etc.)
- Cooldown mechanism prevents duplicate signals
- Generates specific order pairs per strategy

---

### Page: core/execution.py (Architecture Summary)

**ExecutionConfig**: 2% slippage tolerance, 60-second order timeouts

**ExecutionStats**: Tracks orders_placed, orders_filled, slippage_rejections

**ExecutionEngine**:
- Consumes signals from arb engine via async queue
- Places/cancels orders through PolymarketClient API
- Enforces risk limits via RiskManager integration
- Retry logic with configurable attempts and delays
- Slippage validation: compares intended price vs market snapshot at signal time
- Order tracking: `_open_orders`, `_orders_by_market`, `_orders_by_strategy`
- `_monitor_order_timeouts()`: checks every 10 seconds for expired orders
- Fill handling: updates order state, portfolio, and risk manager
- Supports dry-run mode

---

### Page: core/portfolio.py (Architecture Summary)

**PortfolioPosition**: Tracks per-position:
- Market/token ID, size, entry price, cost basis
- Trade history (total bought/sold, trade count)
- PnL calculations (unrealized, realized, total)

**Portfolio**: Manages:
- Cash balance and positions across markets/tokens
- Trade processing with buy/sell logic (add to long, cover short, full cover + go long)
- Price updates for unrealized PnL recalculation
- Exposure by market and overall
- `reset()` restores initial state

---

### Trading Strategies (from README)

**Cross-Platform Arbitrage**:
Buy underpriced asset on one platform, sell overpriced on another.
Example: Trump YES at $0.52 on Polymarket, $0.58 on Kalshi = 6% edge opportunity.

**Bundle Arbitrage**:
- Buy both YES+NO when `ask_yes + ask_no < $1.00` (guarantees $1 payout)
- Sell both when `bid_yes + bid_no > $1.00` (locks premium)

**Market Making**:
Place orders inside wide spreads (>= 5c) with bids slightly above best bid and asks slightly below best ask.

---

### Platform Notes

**Polymarket**:
- Hybrid model: centralized matching, on-chain settlement
- No gas fees (Polymarket covers)
- USDC holdings on Polygon
- API keys required for trading

**Kalshi**:
- CFTC-regulated US exchange
- Prices in cents (55c for YES)
- Public data requires no authentication
- US-based trading requires KYC
- API: docs.kalshi.com

---

### Key Warnings

- "Real prediction markets are highly efficient. Arbitrage opportunities are rare and fleeting."
- Always start in dry-run mode before live trading
- Begin with minimal capital ($50-100)
- Monitor actively; don't leave unattended
- Trading carries risk of loss
- Experimental software - use at own risk

---

### Environment Variables

```bash
export POLYMARKET_API_KEY="your_api_key"
export POLYMARKET_PRIVATE_KEY="your_private_key"
```
