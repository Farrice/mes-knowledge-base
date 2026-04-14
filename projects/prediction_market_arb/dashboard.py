"""
Production Dashboard Generator — Reads live system state and renders HTML.

Unlike the static demo dashboard, this reads actual data from:
  - .agent/polymarket-paper/state.json (balance, risk state)
  - .agent/polymarket-paper/positions.json (open positions)
  - .agent/polymarket-paper/trades.json (trade history)
  - .agent/polymarket-paper/calibration.json (per-city sigma)

Generates a self-contained HTML file that can be opened in any browser
or served via a simple HTTP server for remote monitoring.

Usage:
  python execution/strategy_orchestrator.py dashboard     # Generate + open
  python -c "from projects.prediction_market_arb.dashboard import generate; generate()"
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

from projects.prediction_market_arb.config import load_config
from projects.prediction_market_arb.state import StateManager
from projects.prediction_market_arb.risk_manager import RiskManager


def generate(output_path: str = None, open_browser: bool = False) -> str:
    """
    Generate a production dashboard HTML from live system state.

    Returns the path to the generated HTML file.
    """
    config = load_config()
    state = StateManager(config.paper.data_dir)
    risk = RiskManager(config, state)

    # Load all state
    balance = state.load_balance()
    positions = state.load_positions()
    trades = state.load_trades()
    risk_status = risk.get_status()
    calibration = state.load_calibration()

    # Compute stats
    total_pnl = sum(t.pnl for t in trades) if trades else 0
    wins = sum(1 for t in trades if t.pnl > 0)
    losses = sum(1 for t in trades if t.pnl <= 0) if trades else 0
    win_rate = wins / len(trades) * 100 if trades else 0
    avg_win = sum(t.pnl for t in trades if t.pnl > 0) / max(1, wins) if trades else 0
    avg_loss = sum(t.pnl for t in trades if t.pnl <= 0) / max(1, losses) if trades else 0
    profit_factor = abs(avg_win * wins / (avg_loss * losses)) if avg_loss != 0 and losses > 0 else 0

    # Per-city stats
    city_stats = {}
    for t in trades:
        city = t.city or "unknown"
        if city not in city_stats:
            city_stats[city] = {"trades": 0, "pnl": 0, "wins": 0}
        city_stats[city]["trades"] += 1
        city_stats[city]["pnl"] += t.pnl
        if t.pnl > 0:
            city_stats[city]["wins"] += 1

    # Strategy detection
    has_sports_key = bool(os.environ.get("ODDSPAPI_KEY"))
    has_ensemble_keys = any([
        os.environ.get("OPENAI_API_KEY"),
        os.environ.get("ANTHROPIC_API_KEY"),
        os.environ.get("GOOGLE_API_KEY"),
    ])
    has_kalshi = bool(os.environ.get("KALSHI_API_KEY_ID"))

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Build positions HTML
    positions_html = ""
    if positions:
        for p in positions:
            pnl = p.unrealized_pnl
            pnl_class = "positive" if pnl >= 0 else "negative"
            pnl_sign = "+" if pnl >= 0 else ""
            positions_html += f"""
            <tr>
              <td>{p.question[:60] if p.question else p.market_id[:16]}...</td>
              <td>{p.city or 'N/A'}</td>
              <td class="mono">${p.entry_price:.3f}</td>
              <td class="mono">${p.current_price:.3f}</td>
              <td class="mono">{p.size:.1f}</td>
              <td class="mono ${pnl_class}">{pnl_sign}${pnl:.2f}</td>
              <td>{p.entry_time[:10] if p.entry_time else 'N/A'}</td>
            </tr>"""
    else:
        positions_html = '<tr><td colspan="7" class="empty">No open positions</td></tr>'

    # Build trades HTML
    trades_html = ""
    for t in reversed(trades[-20:]):  # Last 20 trades
        pnl_class = "positive" if t.pnl >= 0 else "negative"
        pnl_sign = "+" if t.pnl >= 0 else ""
        result = "WIN" if t.pnl > 0 else "LOSS"
        result_class = "win" if t.pnl > 0 else "loss"
        trades_html += f"""
            <tr>
              <td>{t.exit_time[:10] if t.exit_time else 'N/A'}</td>
              <td>{t.question[:50] if t.question else t.market_id[:16]}...</td>
              <td>{t.city or 'N/A'}</td>
              <td class="mono">${t.entry_price:.3f}</td>
              <td class="mono">${t.exit_price:.3f}</td>
              <td class="mono {pnl_class}">{pnl_sign}${t.pnl:.2f}</td>
              <td><span class="result-badge {result_class}">{result}</span></td>
              <td>{t.exit_reason or 'N/A'}</td>
            </tr>"""
    if not trades:
        trades_html = '<tr><td colspan="8" class="empty">No completed trades yet</td></tr>'

    # Build city stats HTML
    city_html = ""
    for city, stats in sorted(city_stats.items(), key=lambda x: x[1]["pnl"], reverse=True):
        wr = stats["wins"] / stats["trades"] * 100 if stats["trades"] > 0 else 0
        pnl_class = "positive" if stats["pnl"] >= 0 else "negative"
        pnl_sign = "+" if stats["pnl"] >= 0 else ""
        city_html += f"""
            <tr>
              <td>{city}</td>
              <td class="mono">{stats['trades']}</td>
              <td class="mono">{wr:.0f}%</td>
              <td class="mono {pnl_class}">{pnl_sign}${stats['pnl']:.2f}</td>
            </tr>"""

    # Calibration HTML
    cal_html = ""
    for city, sources in sorted(calibration.items()):
        for source, data in sources.items():
            count = data.get("count", 0)
            sigma = data.get("sigma", "N/A")
            mae = data.get("mae", 0)
            cal_html += f"""
            <tr>
              <td>{city}</td>
              <td>{source}</td>
              <td class="mono">{count}</td>
              <td class="mono">{mae:.2f}</td>
              <td class="mono">{sigma if isinstance(sigma, str) else f'{sigma:.2f}'}</td>
            </tr>"""
    if not cal_html:
        cal_html = '<tr><td colspan="5" class="empty">No calibration data yet (needs 30+ resolved markets)</td></tr>'

    # Pipeline statuses
    def pipeline_dot(active):
        return "dot-green" if active else "dot-yellow"

    # Kill switch
    ks = risk_status["kill_switch"]
    ks_class = "ks-triggered" if ks["triggered"] else "ks-normal"
    ks_text = f"TRIGGERED: {ks['reason']}" if ks["triggered"] else "NORMAL"

    # Drawdown bar
    dd = risk_status["drawdown"]
    dd_pct = min(100, dd["current"] / dd["max_allowed"] * 100) if dd["max_allowed"] > 0 else 0

    # Daily PnL bar
    dp = risk_status["daily_pnl"]
    dp_pct = min(100, abs(dp["amount"]) / dp["max_loss"] * 100) if dp["max_loss"] > 0 else 0

    # Exposure bar
    ex = risk_status["exposure"]
    ex_pct = min(100, ex["global"] / ex["max_global"] * 100) if ex["max_global"] > 0 else 0

    ret_class = "positive" if balance.total_return_pct >= 0 else "negative"
    ret_sign = "+" if balance.total_return_pct >= 0 else ""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Prediction Market AI Trading System — Live Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  :root {{
    --bg: #0a0e1a; --bg2: #111827; --card: #151c2e; --border: #1e293b;
    --text: #e2e8f0; --text2: #94a3b8; --muted: #64748b;
    --green: #22c55e; --red: #ef4444; --yellow: #eab308; --blue: #3b82f6;
    --purple: #a855f7; --cyan: #06b6d4;
  }}
  body {{ font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); padding: 20px; }}
  .mono {{ font-family: 'JetBrains Mono', monospace; }}
  .positive {{ color: var(--green); }} .negative {{ color: var(--red); }}

  /* Header */
  .header {{ display: flex; justify-content: space-between; align-items: center; padding: 16px 24px; background: linear-gradient(135deg, #111827, #1a1f35); border: 1px solid var(--border); border-radius: 12px; margin-bottom: 20px; }}
  .header h1 {{ font-size: 20px; font-weight: 600; }}
  .header .badges {{ display: flex; gap: 8px; align-items: center; }}
  .badge {{ padding: 4px 12px; border-radius: 6px; font-size: 12px; font-weight: 600; }}
  .badge-paper {{ background: rgba(234,179,8,0.15); color: var(--yellow); border: 1px solid rgba(234,179,8,0.3); }}
  .badge-live {{ background: rgba(239,68,68,0.15); color: var(--red); border: 1px solid rgba(239,68,68,0.3); }}
  .timestamp {{ color: var(--muted); font-size: 13px; }}

  /* Cards */
  .cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 20px; }}
  .card {{ background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 20px; }}
  .card-label {{ font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; }}
  .card-value {{ font-size: 28px; font-weight: 700; font-family: 'JetBrains Mono', monospace; }}
  .card-sub {{ font-size: 12px; color: var(--text2); margin-top: 4px; }}

  /* Pipelines */
  .pipelines {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 20px; }}
  .pipe {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 14px; display: flex; align-items: center; gap: 10px; }}
  .dot {{ width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }}
  .dot-green {{ background: var(--green); box-shadow: 0 0 8px rgba(34,197,94,0.4); }}
  .dot-yellow {{ background: var(--yellow); box-shadow: 0 0 8px rgba(234,179,8,0.4); }}
  .dot-gray {{ background: var(--muted); }}
  .pipe h4 {{ font-size: 13px; font-weight: 600; }} .pipe p {{ font-size: 11px; color: var(--muted); }}

  /* Tables */
  .section {{ background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 20px; margin-bottom: 20px; }}
  .section h2 {{ font-size: 16px; font-weight: 600; margin-bottom: 14px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  th {{ text-align: left; padding: 8px 12px; color: var(--muted); font-weight: 500; border-bottom: 1px solid var(--border); font-size: 11px; text-transform: uppercase; }}
  td {{ padding: 8px 12px; border-bottom: 1px solid rgba(30,41,59,0.5); }}
  tr:nth-child(even) {{ background: rgba(10,14,26,0.4); }}
  .empty {{ color: var(--muted); text-align: center; padding: 20px; }}
  .result-badge {{ padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; }}
  .win {{ background: rgba(34,197,94,0.15); color: var(--green); }}
  .loss {{ background: rgba(239,68,68,0.15); color: var(--red); }}

  /* Risk */
  .risk-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; }}
  .risk-item {{ display: flex; flex-direction: column; gap: 6px; }}
  .risk-label {{ font-size: 12px; color: var(--muted); }}
  .risk-bar {{ height: 8px; background: rgba(30,41,59,0.8); border-radius: 4px; overflow: hidden; }}
  .risk-fill {{ height: 100%; border-radius: 4px; transition: width 0.5s; }}
  .risk-fill-green {{ background: var(--green); }} .risk-fill-yellow {{ background: var(--yellow); }} .risk-fill-red {{ background: var(--red); }}
  .risk-text {{ font-size: 12px; font-family: 'JetBrains Mono', monospace; }}
  .ks-normal {{ color: var(--green); }} .ks-triggered {{ color: var(--red); font-weight: 700; }}

  /* Footer */
  .footer {{ text-align: center; padding: 20px; color: var(--muted); font-size: 12px; }}

  /* Two-column layout for bottom sections */
  .two-col {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
  @media (max-width: 900px) {{ .two-col {{ grid-template-columns: 1fr; }} }}
</style>
</head>
<body>

<!-- Header -->
<div class="header">
  <div>
    <h1>Prediction Market AI Trading System</h1>
    <div class="timestamp">Generated: {now}</div>
  </div>
  <div class="badges">
    <span class="badge {'badge-live' if config.is_live else 'badge-paper'}">{'LIVE MODE' if config.is_live else 'PAPER MODE'}</span>
    <span class="badge" style="background:rgba(59,130,246,0.15);color:var(--blue);border:1px solid rgba(59,130,246,0.3);">v0.2.5</span>
  </div>
</div>

<!-- Portfolio Summary -->
<div class="cards">
  <div class="card">
    <div class="card-label">Balance</div>
    <div class="card-value">${balance.current:.2f}</div>
    <div class="card-sub">Started ${balance.initial:.2f}</div>
  </div>
  <div class="card">
    <div class="card-label">Return</div>
    <div class="card-value {ret_class}">{ret_sign}{balance.total_return_pct:.1f}%</div>
    <div class="card-sub">High water: ${balance.high_water_mark:.2f}</div>
  </div>
  <div class="card">
    <div class="card-label">Win Rate</div>
    <div class="card-value">{win_rate:.0f}%</div>
    <div class="card-sub">{wins}W / {losses}L ({len(trades)} total)</div>
  </div>
  <div class="card">
    <div class="card-label">Profit Factor</div>
    <div class="card-value">{profit_factor:.2f}</div>
    <div class="card-sub">Avg win ${avg_win:.2f} / Avg loss ${avg_loss:.2f}</div>
  </div>
  <div class="card">
    <div class="card-label">Open Positions</div>
    <div class="card-value">{len(positions)}</div>
    <div class="card-sub">${sum(p.cost for p in positions):.2f} deployed</div>
  </div>
</div>

<!-- Strategy Pipelines -->
<div class="pipelines">
  <div class="pipe"><div class="dot dot-green"></div><div><h4>Weather</h4><p>Active &mdash; 20 cities, 3 sources</p></div></div>
  <div class="pipe"><div class="dot {'dot-green' if has_sports_key else 'dot-yellow'}"></div><div><h4>Sports Arb</h4><p>{'Active' if has_sports_key else 'Ready &mdash; needs API key'}</p></div></div>
  <div class="pipe"><div class="dot {'dot-green' if has_ensemble_keys else 'dot-yellow'}"></div><div><h4>AI Ensemble</h4><p>{'Active' if has_ensemble_keys else 'Ready &mdash; needs API keys'}</p></div></div>
  <div class="pipe"><div class="dot {'dot-green' if has_kalshi else 'dot-yellow'}"></div><div><h4>Cross-Platform</h4><p>{'Active' if has_kalshi else 'Ready &mdash; Poly &harr; Kalshi'}</p></div></div>
  <div class="pipe"><div class="dot dot-gray"></div><div><h4>Market Making</h4><p>Phase 4 &mdash; deferred</p></div></div>
</div>

<!-- Risk Dashboard -->
<div class="section">
  <h2>Risk Dashboard</h2>
  <div class="risk-grid">
    <div class="risk-item">
      <div class="risk-label">Kill Switch</div>
      <div class="risk-text {ks_class}">{ks_text}</div>
    </div>
    <div class="risk-item">
      <div class="risk-label">Daily P&L (limit: -${dp['max_loss']:.2f})</div>
      <div class="risk-bar"><div class="risk-fill {'risk-fill-red' if dp_pct > 80 else 'risk-fill-yellow' if dp_pct > 50 else 'risk-fill-green'}" style="width:{dp_pct:.0f}%"></div></div>
      <div class="risk-text">${dp['amount']:.2f} ({dp_pct:.0f}% of limit)</div>
    </div>
    <div class="risk-item">
      <div class="risk-label">Drawdown (limit: {dd['max_allowed']:.0%})</div>
      <div class="risk-bar"><div class="risk-fill {'risk-fill-red' if dd_pct > 80 else 'risk-fill-yellow' if dd_pct > 50 else 'risk-fill-green'}" style="width:{dd_pct:.0f}%"></div></div>
      <div class="risk-text">{dd['current']:.1%} ({dd_pct:.0f}% of limit)</div>
    </div>
    <div class="risk-item">
      <div class="risk-label">Global Exposure (limit: ${ex['max_global']:.2f})</div>
      <div class="risk-bar"><div class="risk-fill {'risk-fill-red' if ex_pct > 80 else 'risk-fill-yellow' if ex_pct > 50 else 'risk-fill-green'}" style="width:{ex_pct:.0f}%"></div></div>
      <div class="risk-text">${ex['global']:.2f} ({ex_pct:.0f}% of limit)</div>
    </div>
  </div>
</div>

<!-- Open Positions -->
<div class="section">
  <h2>Open Positions ({len(positions)})</h2>
  <table>
    <thead><tr><th>Market</th><th>City</th><th>Entry</th><th>Current</th><th>Shares</th><th>P&L</th><th>Opened</th></tr></thead>
    <tbody>{positions_html}</tbody>
  </table>
</div>

<!-- Trade History -->
<div class="section">
  <h2>Trade History ({len(trades)} total)</h2>
  <table>
    <thead><tr><th>Date</th><th>Market</th><th>City</th><th>Entry</th><th>Exit</th><th>P&L</th><th>Result</th><th>Reason</th></tr></thead>
    <tbody>{trades_html}</tbody>
  </table>
</div>

<!-- Bottom: Per-City + Calibration -->
<div class="two-col">
  <div class="section">
    <h2>Performance by City</h2>
    <table>
      <thead><tr><th>City</th><th>Trades</th><th>Win Rate</th><th>P&L</th></tr></thead>
      <tbody>{city_html if city_html else '<tr><td colspan="4" class="empty">No city data yet</td></tr>'}</tbody>
    </table>
  </div>
  <div class="section">
    <h2>Forecast Calibration</h2>
    <table>
      <thead><tr><th>City</th><th>Source</th><th>Samples</th><th>MAE</th><th>Sigma</th></tr></thead>
      <tbody>{cal_html}</tbody>
    </table>
  </div>
</div>

<div class="footer">
  <div>System v0.2.5 &mdash; 15 modules &middot; 2 platforms &middot; 5 strategies &middot; 8-check risk validation</div>
  <div style="margin-top:4px;">Dashboard generated from live system state at {now}</div>
</div>

</body>
</html>"""

    # Write output
    if output_path is None:
        output_path = str(Path(config.paper.data_dir) / "dashboard.html")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(html)

    if open_browser:
        import webbrowser
        webbrowser.open(f"file://{os.path.abspath(output_path)}")

    return output_path
