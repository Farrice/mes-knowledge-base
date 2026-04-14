#!/usr/bin/env python3
"""
Risk Manager CLI — View risk status, test validation, manage kill switch.

Usage:
    python execution/risk_manager.py status           # Full risk dashboard
    python execution/risk_manager.py killswitch        # Kill switch status
    python execution/risk_manager.py validate          # Validate a test order
    python execution/risk_manager.py kelly <prob> <price> [balance]  # Kelly sizing calc
"""

import argparse
import logging
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from projects.prediction_market_arb.config import load_config
from projects.prediction_market_arb.state import StateManager
from projects.prediction_market_arb.risk_manager import RiskManager
from projects.prediction_market_arb.models import OrderRequest, OrderSide


def main():
    parser = argparse.ArgumentParser(description="Risk Manager CLI")
    parser.add_argument("command", choices=["status", "killswitch", "validate", "kelly"])
    parser.add_argument("args", nargs="*", default=[])
    parser.add_argument("--config", type=str, default=None)
    args = parser.parse_args()

    logging.basicConfig(level=logging.WARNING)
    config = load_config(args.config)
    state = StateManager(config.paper.data_dir)
    risk = RiskManager(config, state)

    if args.command == "status":
        status = risk.get_status()
        print("\n  === RISK STATUS ===")
        print(f"\n  Kill Switch:  "
              f"{'🔴 TRIGGERED' if status['kill_switch']['triggered'] else '🟢 Normal'}")
        if status['kill_switch']['triggered']:
            print(f"    Level:  {status['kill_switch']['level']}")
            print(f"    Reason: {status['kill_switch']['reason']}")
            print(f"    Time:   {status['kill_switch']['time']}")

        print(f"\n  Balance:     ${status['balance']['current']:.2f} "
              f"(HWM: ${status['balance']['high_water_mark']:.2f})")
        print(f"  Return:      {status['balance']['return_pct']:+.1f}%")
        print(f"\n  Exposure:    ${status['exposure']['global']:.2f} / "
              f"${status['exposure']['max_global']:.2f}")
        print(f"  Positions:   {status['exposure']['positions']}")
        print(f"\n  Daily PnL:   ${status['daily_pnl']['amount']:.2f} "
              f"(limit: -${status['daily_pnl']['max_loss']:.2f})")
        print(f"  Drawdown:    {status['drawdown']['current']:.1%} "
              f"(limit: {status['drawdown']['max_allowed']:.1%})")
        print(f"\n  Trades:      {status['trades']['total']} "
              f"(W:{status['trades']['wins']} L:{status['trades']['losses']} "
              f"WR:{status['trades']['win_rate']:.0%})")

    elif args.command == "killswitch":
        ks = risk.get_kill_switch_status()
        if ks["triggered"]:
            print(f"\n  🔴 KILL SWITCH TRIGGERED")
            print(f"     Level:  {ks['level']}")
            print(f"     Reason: {ks['reason']}")
            print(f"     Time:   {ks['time']}")
            print(f"\n  To reset: edit .agent/polymarket-paper/state.json")
            print(f"  Set risk.kill_switch_triggered = false")
        else:
            print(f"\n  🟢 Kill switch: Normal")

    elif args.command == "kelly":
        if len(args.args) < 2:
            print("Usage: risk_manager.py kelly <probability> <price> [balance]")
            print("  Example: risk_manager.py kelly 0.75 0.15 1000")
            return
        prob = float(args.args[0])
        price = float(args.args[1])
        balance = float(args.args[2]) if len(args.args) > 2 else None
        size = risk.calc_position_size(prob, price, balance)
        b = (1.0 / price) - 1.0
        f_star = (prob * b - (1.0 - prob)) / b if b > 0 else 0
        f_adj = f_star * config.trading.kelly_fraction

        print(f"\n  Kelly Position Sizing")
        print(f"  Probability:    {prob:.1%}")
        print(f"  Market price:   ${price:.3f}")
        print(f"  Payout odds:    {b:.2f}x")
        print(f"  Raw Kelly:      {f_star:.3f}")
        print(f"  Quarter-Kelly:  {f_adj:.3f}")
        print(f"  Position size:  ${size:.2f}")
        if size > 0:
            shares = size / price
            print(f"  Shares:         {shares:.1f}")

    elif args.command == "validate":
        print("\n  Test order validation (creates a dummy order)")
        order = OrderRequest(
            market_id="test-market-id",
            token_id="test-token-id",
            side=OrderSide.BUY,
            price=0.15,
            size=100,
        )
        passed, reason = risk.check_order(order, market_volume=50000)
        if passed:
            print("  ✅ Order would pass all 8 checks")
        else:
            print(f"  ❌ Order rejected: {reason}")


if __name__ == "__main__":
    main()
