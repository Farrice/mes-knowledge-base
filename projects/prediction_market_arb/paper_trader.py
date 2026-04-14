"""
Paper Trading Simulator — orchestrates the full trading pipeline.

This is the integration module. It connects:
  - Market discovery (Polymarket client + Gamma API)
  - Forecast pipeline (weather data from 3 sources)
  - Edge calculation (Gaussian bucket probability)
  - Risk validation (8-check chain + Kelly sizing)
  - Paper execution (simulated trades against real market data)
  - Position monitoring (dual-cadence: 10min defense, 60min offense)
  - Performance reporting (P&L, win rate, per-city breakdown)

Dual-cadence monitoring (from weatherbot extraction):
  - Defense every 10 minutes: check exits on all open positions
  - Offense every 60 minutes: scan for new market opportunities

The paper trader NEVER places real trades. It reads real market data
and simulates execution with configurable fill probability.
"""

import logging
import time
import uuid
from datetime import datetime, timezone

from projects.prediction_market_arb.config import load_config
from projects.prediction_market_arb.state import StateManager
from projects.prediction_market_arb.polymarket_client import create_client
from projects.prediction_market_arb.weather_data import WeatherPipeline
from projects.prediction_market_arb.risk_manager import RiskManager, ExitSignal
from projects.prediction_market_arb.strategy_orchestrator import StrategyOrchestrator
from projects.prediction_market_arb.models import (
    OrderRequest, OrderSide, OrderType, OrderStatus, ExitReason,
    TradeRecord, Position, Opportunity,
)

logger = logging.getLogger("polymarket.paper")


# =============================================================================
# TERMINAL COLORS
# =============================================================================

class C:
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    CYAN   = "\033[96m"
    GRAY   = "\033[90m"
    RESET  = "\033[0m"
    BOLD   = "\033[1m"


# =============================================================================
# PAPER TRADER
# =============================================================================

class PaperTrader:
    """
    Paper trading simulator. Uses real market data, simulates execution.
    Validates every trade through the 8-check risk manager.
    """

    def __init__(self, config=None, config_path=None):
        self.config = config or load_config(config_path)
        self.state = StateManager(self.config.paper.data_dir)
        self.client = create_client(self.config, self.state)
        self.weather = WeatherPipeline(self.config, self.state)
        self.risk = RiskManager(self.config, self.state)
        # Phase 2: Multi-strategy orchestrator
        self.orchestrator = StrategyOrchestrator(self.config)

    # -------------------------------------------------------------------------
    # SCAN & TRADE (offense — every 60 minutes)
    # -------------------------------------------------------------------------

    def scan_and_trade(self) -> dict:
        """
        Full scan loop:
          1. Discover weather markets on Polymarket
          2. Fetch forecasts from multiple sources
          3. Calculate edge for each opportunity
          4. Validate through 8-check risk manager
          5. Size position via Kelly criterion
          6. Execute paper trade

        Returns summary dict with scan results.
        """
        print(f"\n{C.BOLD}{C.CYAN}=== PAPER TRADING SCAN ==={C.RESET}")
        print(f"  Mode: {C.YELLOW}PAPER{C.RESET}")
        print(f"  Time: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")

        balance = self.state.load_balance()
        print(f"  Balance: {C.BOLD}${balance.current:.2f}{C.RESET} "
              f"(started ${balance.initial:.2f}, "
              f"{'+' if balance.total_return_pct >= 0 else ''}"
              f"{balance.total_return_pct:.1f}%)")

        # Check kill switch
        ks = self.risk.get_kill_switch_status()
        if ks["triggered"]:
            print(f"\n  {C.RED}KILL SWITCH TRIGGERED: {ks['reason']}{C.RESET}")
            print(f"  {C.RED}All trading halted. Manual reset required.{C.RESET}")
            return {"status": "killed", "reason": ks["reason"]}

        # Scan weather markets
        print(f"\n{C.BOLD}Scanning weather markets...{C.RESET}")
        opportunities = self.weather.scan_weather_markets(self.client)

        if not opportunities:
            print(f"  {C.GRAY}No opportunities found{C.RESET}")
            return {"status": "no_opportunities", "scanned": 0, "traded": 0}

        print(f"  Found {len(opportunities)} opportunities")

        # Process each opportunity
        trades_placed = 0
        trades_rejected = 0

        for opp in opportunities:
            # Risk check
            order = OrderRequest(
                market_id=opp["market_id"],
                token_id=opp["token_id"],
                side=OrderSide.BUY,
                price=opp["market_price"],
                size=0,  # Will be set by Kelly
                neg_risk=opp.get("neg_risk", False),
            )

            passed, reason = self.risk.check_order(
                order, market_volume=opp.get("volume", 0)
            )

            if not passed:
                print(f"  {C.GRAY}SKIP {opp['city_name']} {opp['date']}: "
                      f"{reason}{C.RESET}")
                trades_rejected += 1
                continue

            # Kelly position sizing
            size_dollars = self.risk.calc_position_size(
                probability=opp["probability"],
                price=opp["market_price"],
                balance=balance.current,
            )

            if size_dollars <= 0:
                print(f"  {C.GRAY}SKIP {opp['city_name']} {opp['date']}: "
                      f"Kelly says no edge{C.RESET}")
                trades_rejected += 1
                continue

            # Calculate shares
            shares = size_dollars / opp["market_price"]

            # Check if already in this market
            positions = self.state.load_positions()
            already_in = any(p.market_id == opp["market_id"] for p in positions)
            if already_in:
                print(f"  {C.GRAY}SKIP {opp['city_name']} {opp['date']}: "
                      f"already have position{C.RESET}")
                continue

            # Place paper order
            order.size = shares
            result = self.client.place_order(order)

            if result.status == OrderStatus.CONFIRMED:
                trades_placed += 1
                print(f"\n  {C.GREEN}TRADE {opp['city_name']} {opp['date']}{C.RESET}")
                print(f"    Question: {opp['question'][:60]}...")
                print(f"    Forecast: {opp['forecast_temp']}°{opp['unit']} "
                      f"({opp['forecast_source']})")
                print(f"    Probability: {opp['probability']:.1%} vs "
                      f"market ${opp['market_price']:.3f}")
                print(f"    Edge: {opp['edge']:.1%} | EV: {opp['ev']:.3f}")
                print(f"    Size: ${size_dollars:.2f} "
                      f"({shares:.1f} shares @ ${opp['market_price']:.3f})")

                # Update position with weather context
                positions = self.state.load_positions()
                for p in positions:
                    if p.market_id == opp["market_id"]:
                        p.question = opp["question"]
                        p.city = opp["city"]
                        p.forecast_temp = opp["forecast_temp"]
                self.state.save_positions(positions)

                # Reload balance
                balance = self.state.load_balance()
            else:
                print(f"  {C.YELLOW}MISS {opp['city_name']} {opp['date']}: "
                      f"{result.error or 'order not filled'}{C.RESET}")

        # Summary
        print(f"\n{'=' * 50}")
        print(f"{C.BOLD}Scan Summary:{C.RESET}")
        print(f"  Opportunities: {len(opportunities)}")
        print(f"  Trades placed: {C.GREEN}{trades_placed}{C.RESET}")
        print(f"  Rejected: {trades_rejected}")
        print(f"  Balance: ${balance.current:.2f}")

        return {
            "status": "ok",
            "scanned": len(opportunities),
            "traded": trades_placed,
            "rejected": trades_rejected,
            "balance": balance.current,
        }

    # -------------------------------------------------------------------------
    # MULTI-STRATEGY SCAN & TRADE (Phase 2 — offense, every 60 minutes)
    # -------------------------------------------------------------------------

    def scan_and_trade_multi(self) -> dict:
        """
        Full multi-strategy scan loop (Phase 2):
          1. Run strategy orchestrator (weather + sports + ensemble)
          2. Get ranked opportunities across all strategies
          3. Validate each through 8-check risk manager
          4. Size position via Kelly criterion
          5. Execute paper trade

        Returns summary dict with results by strategy.
        """
        print(f"\n{C.BOLD}{C.CYAN}=== MULTI-STRATEGY PAPER TRADING ==={C.RESET}")
        print(f"  Mode: {C.YELLOW}PAPER{C.RESET}")
        print(f"  Time: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")

        balance = self.state.load_balance()
        print(f"  Balance: {C.BOLD}${balance.current:.2f}{C.RESET} "
              f"(started ${balance.initial:.2f}, "
              f"{'+' if balance.total_return_pct >= 0 else ''}"
              f"{balance.total_return_pct:.1f}%)")

        # Check kill switch
        ks = self.risk.get_kill_switch_status()
        if ks["triggered"]:
            print(f"\n  {C.RED}KILL SWITCH TRIGGERED: {ks['reason']}{C.RESET}")
            return {"status": "killed", "reason": ks["reason"]}

        # Run multi-strategy scan
        opportunities = self.orchestrator.scan_all()

        if not opportunities:
            print(f"\n  {C.GRAY}No opportunities across any strategy{C.RESET}")
            return {"status": "no_opportunities", "scanned": 0, "traded": 0}

        # Process each opportunity
        trades_placed = 0
        trades_rejected = 0
        results_by_strategy = {}

        for opp in opportunities:
            strategy = opp.strategy
            if strategy not in results_by_strategy:
                results_by_strategy[strategy] = {"scanned": 0, "traded": 0, "rejected": 0}
            results_by_strategy[strategy]["scanned"] += 1

            # Risk check
            order = OrderRequest(
                market_id=opp.market_id,
                token_id=opp.token_id,
                side=OrderSide.BUY,
                price=opp.market_price,
                size=0,  # Will be set by Kelly
                neg_risk=opp.neg_risk,
            )

            passed, reason = self.risk.check_order(
                order, market_volume=opp.volume
            )

            if not passed:
                print(f"  {C.GRAY}SKIP [{opp.strategy}] {opp.question[:40]}...: "
                      f"{reason}{C.RESET}")
                trades_rejected += 1
                results_by_strategy[strategy]["rejected"] += 1
                continue

            # Kelly position sizing
            size_dollars = self.risk.calc_position_size(
                probability=opp.our_probability,
                price=opp.market_price,
                balance=balance.current,
            )

            if size_dollars <= 0:
                trades_rejected += 1
                results_by_strategy[strategy]["rejected"] += 1
                continue

            shares = size_dollars / opp.market_price

            # Check if already in this market
            positions = self.state.load_positions()
            already_in = any(p.market_id == opp.market_id for p in positions)
            if already_in:
                continue

            # Place paper order
            order.size = shares
            result = self.client.place_order(order)

            if result.status == OrderStatus.CONFIRMED:
                trades_placed += 1
                results_by_strategy[strategy]["traded"] += 1

                # Color by strategy
                colors = {
                    "weather": C.CYAN, "sports_arb": C.GREEN,
                    "ensemble": "\033[95m", "market_making": C.YELLOW,
                }
                sc = colors.get(strategy, C.RESET)

                print(f"\n  {sc}TRADE [{strategy}]{C.RESET} {opp.question[:55]}...")
                print(f"    Our prob: {opp.our_probability:.1%} vs "
                      f"market ${opp.market_price:.3f}")
                print(f"    Edge: {opp.edge_after_fees:+.1%} | "
                      f"Score: {opp.composite_score:.3f} | "
                      f"Ref: {opp.reference_source}")
                print(f"    Size: ${size_dollars:.2f} "
                      f"({shares:.1f} shares @ ${opp.market_price:.3f})")

                # Update position with strategy context
                positions = self.state.load_positions()
                for p in positions:
                    if p.market_id == opp.market_id:
                        p.question = opp.question
                        if opp.context.get("city"):
                            p.city = opp.context["city"]
                            p.forecast_temp = opp.context.get("forecast_temp")
                self.state.save_positions(positions)

                balance = self.state.load_balance()

        # Summary
        print(f"\n{'=' * 60}")
        print(f"{C.BOLD}Multi-Strategy Summary:{C.RESET}")
        for strategy, stats in results_by_strategy.items():
            color = {
                "weather": C.CYAN, "sports_arb": C.GREEN,
                "ensemble": "\033[95m",
            }.get(strategy, C.RESET)
            print(f"  {color}{strategy:15s}{C.RESET}: "
                  f"{stats['scanned']} found, "
                  f"{C.GREEN}{stats['traded']} traded{C.RESET}, "
                  f"{stats['rejected']} rejected")
        print(f"  Total trades: {C.GREEN}{trades_placed}{C.RESET}")
        print(f"  Balance: ${balance.current:.2f}")

        return {
            "status": "ok",
            "scanned": len(opportunities),
            "traded": trades_placed,
            "rejected": trades_rejected,
            "by_strategy": results_by_strategy,
            "balance": balance.current,
        }

    # -------------------------------------------------------------------------
    # MONITOR POSITIONS (defense — every 10 minutes)
    # -------------------------------------------------------------------------

    def monitor_positions(self) -> list:
        """
        Check all open positions for exit conditions.
        Defense runs at HIGHER FREQUENCY than offense (10min vs 60min).

        Returns list of exit actions taken.
        """
        positions = self.state.load_positions()
        if not positions:
            return []

        print(f"\n{C.BOLD}Monitoring {len(positions)} positions...{C.RESET}")

        # Update current prices
        for pos in positions:
            prices = self.client.get_market_price(pos.market_id)
            if prices:
                pos.update_pnl(prices["yes"])

        # Fetch fresh forecasts for weather positions
        forecasts = {}
        for pos in positions:
            if pos.city and pos.city not in forecasts:
                # Get the date from the position's market
                date = self._extract_date_from_position(pos)
                if date:
                    forecast = self.weather.fetch_forecast(pos.city, date)
                    if forecast:
                        forecasts[pos.city] = forecast

        # Check exits
        exit_signals = self.risk.check_exits(positions, forecasts)
        actions = []

        for signal in exit_signals:
            pos = next((p for p in positions if p.market_id == signal.market_id), None)
            if not pos:
                continue

            # Execute exit
            pnl = (signal.price - pos.entry_price) * pos.size
            balance = self.state.load_balance()
            balance.current += pos.cost + pnl
            if pnl > 0:
                balance.wins += 1
            else:
                balance.losses += 1
            self.state.save_balance(balance)

            # Record trade
            trade = TradeRecord(
                trade_id=str(uuid.uuid4()),
                market_id=pos.market_id,
                question=pos.question,
                side=pos.side.value,
                entry_price=pos.entry_price,
                exit_price=signal.price,
                size=pos.size,
                pnl=round(pnl, 2),
                entry_time=pos.entry_time,
                exit_time=datetime.now(timezone.utc).isoformat(),
                exit_reason=signal.reason.value,
                city=pos.city,
                is_paper=True,
            )
            self.state.append_trade(trade)

            # Remove position
            self.state.remove_position(pos.market_id)

            # Update risk state
            self.risk.record_trade_pnl(pnl)

            pnl_str = (f"{C.GREEN}+${pnl:.2f}{C.RESET}" if pnl >= 0
                       else f"{C.RED}-${abs(pnl):.2f}{C.RESET}")
            print(f"  {C.YELLOW}EXIT{C.RESET} {pos.question[:50]}...")
            print(f"    Reason: {signal.reason.value} | {signal.message}")
            print(f"    Entry: ${pos.entry_price:.3f} → Exit: ${signal.price:.3f} | "
                  f"PnL: {pnl_str}")

            actions.append({
                "market_id": pos.market_id,
                "reason": signal.reason.value,
                "pnl": pnl,
            })

        # Save updated positions (with new current prices)
        remaining = [p for p in positions
                     if p.market_id not in [s.market_id for s in exit_signals]]
        self.state.save_positions(remaining)

        return actions

    def _extract_date_from_position(self, pos: Position) -> str:
        """Extract the target date from a weather position's question."""
        import re
        from projects.prediction_market_arb.constants import MONTHS

        if not pos.question:
            return ""
        for i, month in enumerate(MONTHS):
            pattern = rf'{month}\s+(\d+),?\s+(\d{{4}})'
            m = re.search(pattern, pos.question, re.IGNORECASE)
            if m:
                day = int(m.group(1))
                year = int(m.group(2))
                return f"{year}-{i+1:02d}-{day:02d}"
        return ""

    # -------------------------------------------------------------------------
    # CONTINUOUS LOOP (dual-cadence)
    # -------------------------------------------------------------------------

    def run(self, multi_strategy: bool = True):
        """
        Main trading loop with dual cadence:
          - Defense every 10 minutes (position monitoring)
          - Offense every 60 minutes (market scanning)

        Args:
          multi_strategy: If True, uses scan_and_trade_multi() (all strategies).
                         If False, uses scan_and_trade() (weather only, Phase 1).

        Ctrl+C to stop.
        """
        mode_label = "MULTI-STRATEGY" if multi_strategy else "WEATHER ONLY"
        print(f"\n{C.BOLD}{C.CYAN}{'=' * 60}{C.RESET}")
        print(f"{C.BOLD}{C.CYAN}  POLYMARKET PAPER TRADER — {mode_label}{C.RESET}")
        print(f"{C.BOLD}{C.CYAN}{'=' * 60}{C.RESET}")
        print(f"  Defense interval: 10 minutes")
        print(f"  Offense interval: 60 minutes")
        if multi_strategy:
            print(f"  Strategies: Weather + Sports Arb + AI Ensemble")
        print(f"  Press Ctrl+C to stop\n")

        last_scan = 0
        last_monitor = 0
        scan_interval = self.config.weather.scan_interval    # 3600
        monitor_interval = self.config.weather.monitor_interval  # 600

        try:
            while True:
                now = time.time()

                # Defense — higher frequency
                if now - last_monitor >= monitor_interval:
                    self.monitor_positions()
                    last_monitor = now

                # Offense — lower frequency
                if now - last_scan >= scan_interval:
                    if multi_strategy:
                        self.scan_and_trade_multi()
                    else:
                        self.scan_and_trade()
                    last_scan = now

                time.sleep(30)  # Check every 30 seconds

        except KeyboardInterrupt:
            print(f"\n{C.YELLOW}Stopping paper trader...{C.RESET}")

    # -------------------------------------------------------------------------
    # STATUS & REPORTING
    # -------------------------------------------------------------------------

    def status(self):
        """Print current paper trading status."""
        balance = self.state.load_balance()
        positions = self.state.load_positions()
        risk_status = self.risk.get_status()

        print(f"\n{C.BOLD}{'=' * 50}{C.RESET}")
        print(f"{C.BOLD}  POLYMARKET PAPER TRADER — STATUS{C.RESET}")
        print(f"{'=' * 50}")

        # Balance
        ret_color = C.GREEN if balance.total_return_pct >= 0 else C.RED
        print(f"\n  Balance:     {C.BOLD}${balance.current:.2f}{C.RESET}")
        print(f"  Started:     ${balance.initial:.2f}")
        print(f"  High water:  ${balance.high_water_mark:.2f}")
        print(f"  Return:      {ret_color}{'+' if balance.total_return_pct >= 0 else ''}"
              f"{balance.total_return_pct:.1f}%{C.RESET}")

        # Trades
        print(f"\n  Total trades: {balance.total_trades}")
        print(f"  Wins/Losses:  {balance.wins}/{balance.losses}")
        if balance.total_trades > 0:
            wr_color = C.GREEN if balance.win_rate >= 0.5 else C.RED
            print(f"  Win rate:     {wr_color}{balance.win_rate:.1%}{C.RESET}")

        # Risk
        print(f"\n  Kill switch:  "
              f"{'🔴 TRIGGERED' if risk_status['kill_switch']['triggered'] else '🟢 Normal'}")
        print(f"  Daily PnL:    ${risk_status['daily_pnl']['amount']:.2f} "
              f"(limit: -${risk_status['daily_pnl']['max_loss']:.2f})")
        print(f"  Drawdown:     {risk_status['drawdown']['current']:.1%} "
              f"(limit: {risk_status['drawdown']['max_allowed']:.1%})")
        print(f"  Exposure:     ${risk_status['exposure']['global']:.2f} / "
              f"${risk_status['exposure']['max_global']:.2f}")

        # Positions
        if positions:
            print(f"\n{C.BOLD}  Open Positions ({len(positions)}):{C.RESET}")
            total_pnl = 0
            for pos in positions:
                prices = self.client.get_market_price(pos.market_id)
                if prices:
                    pos.update_pnl(prices["yes"])
                pnl = pos.unrealized_pnl
                total_pnl += pnl
                pnl_str = (f"{C.GREEN}+${pnl:.2f}{C.RESET}" if pnl >= 0
                           else f"{C.RED}-${abs(pnl):.2f}{C.RESET}")
                print(f"\n    {pos.question[:60]}...")
                print(f"      Entry: ${pos.entry_price:.3f} | "
                      f"Now: ${pos.current_price:.3f} | "
                      f"PnL: {pnl_str}")
        else:
            print(f"\n  {C.GRAY}No open positions{C.RESET}")

    def report(self):
        """Print full performance report."""
        trades = self.state.load_trades()
        balance = self.state.load_balance()

        print(f"\n{C.BOLD}{'=' * 50}{C.RESET}")
        print(f"{C.BOLD}  PERFORMANCE REPORT{C.RESET}")
        print(f"{'=' * 50}")

        if not trades:
            print(f"\n  {C.GRAY}No completed trades yet{C.RESET}")
            return

        # Overall stats
        total_pnl = sum(t.pnl for t in trades)
        wins = sum(1 for t in trades if t.pnl > 0)
        losses = sum(1 for t in trades if t.pnl <= 0)
        avg_win = sum(t.pnl for t in trades if t.pnl > 0) / max(1, wins)
        avg_loss = sum(t.pnl for t in trades if t.pnl <= 0) / max(1, losses)

        print(f"\n  Total trades:   {len(trades)}")
        print(f"  Win rate:       {wins}/{len(trades)} "
              f"({wins/len(trades):.1%})")
        pnl_color = C.GREEN if total_pnl >= 0 else C.RED
        print(f"  Total PnL:      {pnl_color}${total_pnl:+.2f}{C.RESET}")
        print(f"  Avg win:        ${avg_win:+.2f}")
        print(f"  Avg loss:       ${avg_loss:+.2f}")
        if avg_loss != 0:
            print(f"  Profit factor:  {abs(avg_win * wins / (avg_loss * losses)):.2f}")

        # Per-city breakdown
        cities = {}
        for t in trades:
            city = t.city or "unknown"
            if city not in cities:
                cities[city] = {"trades": 0, "pnl": 0, "wins": 0}
            cities[city]["trades"] += 1
            cities[city]["pnl"] += t.pnl
            if t.pnl > 0:
                cities[city]["wins"] += 1

        if cities:
            print(f"\n  {C.BOLD}Per-City Breakdown:{C.RESET}")
            for city, stats in sorted(cities.items(), key=lambda x: x[1]["pnl"],
                                       reverse=True):
                wr = stats["wins"] / stats["trades"] if stats["trades"] > 0 else 0
                pnl_c = C.GREEN if stats["pnl"] >= 0 else C.RED
                print(f"    {city:15s} | {stats['trades']:3d} trades | "
                      f"WR {wr:.0%} | "
                      f"{pnl_c}${stats['pnl']:+.2f}{C.RESET}")

        # Exit reason breakdown
        reasons = {}
        for t in trades:
            r = t.exit_reason or "unknown"
            if r not in reasons:
                reasons[r] = 0
            reasons[r] += 1

        if reasons:
            print(f"\n  {C.BOLD}Exit Reasons:{C.RESET}")
            for reason, count in sorted(reasons.items(), key=lambda x: x[1],
                                         reverse=True):
                print(f"    {reason:20s} | {count}")

        # Recent trades
        recent = trades[-10:]
        if recent:
            print(f"\n  {C.BOLD}Recent Trades:{C.RESET}")
            for t in reversed(recent):
                pnl_c = C.GREEN if t.pnl >= 0 else C.RED
                print(f"    {t.exit_time[:10]} | {t.question[:40]}... | "
                      f"{pnl_c}${t.pnl:+.2f}{C.RESET} | {t.exit_reason}")
