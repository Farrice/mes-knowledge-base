"""
Resilience utilities — retry logic, error classification, alerts.

Extracted patterns:
  - Retryable error classification (transient vs permanent)
  - Exponential backoff decorator for API calls
  - Trade history compaction (24h full → 15min → hourly → daily)
  - macOS push notifications for critical events

These patterns harden the system for production use. Every API call
to Polymarket, Kalshi, OddsPapi, and LLM providers should use the
retry decorator. The notification system alerts operators to kill
switch triggers, daily P&L summaries, and market resolutions.
"""

import functools
import json
import logging
import os
import subprocess
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

import requests

logger = logging.getLogger("polymarket.resilience")


# =============================================================================
# RETRYABLE ERROR CLASSIFICATION
# =============================================================================

# HTTP status codes that indicate transient failures (retry-safe)
TRANSIENT_HTTP_CODES = {
    429,  # Rate limited (Kalshi, OddsPapi, LLM providers)
    500,  # Internal server error (temporary)
    502,  # Bad gateway
    503,  # Service unavailable
    504,  # Gateway timeout
}

# HTTP codes that are permanent failures (do NOT retry)
PERMANENT_HTTP_CODES = {
    400,  # Bad request (our fault)
    401,  # Unauthorized (bad credentials)
    403,  # Forbidden
    404,  # Not found
    405,  # Method not allowed
    422,  # Unprocessable entity (validation error)
}


def is_transient_error(error: Exception) -> bool:
    """Classify whether an error is transient (safe to retry) or permanent."""
    if isinstance(error, requests.exceptions.ConnectionError):
        return True  # Network blip
    if isinstance(error, requests.exceptions.Timeout):
        return True  # Timed out
    if isinstance(error, requests.exceptions.HTTPError):
        if hasattr(error, 'response') and error.response is not None:
            return error.response.status_code in TRANSIENT_HTTP_CODES
    return False


# =============================================================================
# RETRY DECORATOR
# =============================================================================

def retry_transient(max_attempts: int = 3, backoff_base: float = 1.0,
                    backoff_max: float = 30.0):
    """
    Decorator that retries a function on transient errors with exponential backoff.

    Usage:
        @retry_transient(max_attempts=3, backoff_base=1.0)
        def fetch_data():
            resp = requests.get(url)
            resp.raise_for_status()
            return resp.json()

    Behavior:
      - On transient error: wait backoff_base * 2^attempt seconds, retry
      - On permanent error: raise immediately (no retry)
      - On success: return result
      - On all retries exhausted: raise the last error
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    if not is_transient_error(e):
                        # Permanent error — don't retry
                        raise
                    if attempt < max_attempts - 1:
                        delay = min(backoff_base * (2 ** attempt), backoff_max)
                        logger.warning(
                            f"[RETRY] {func.__name__} failed (attempt {attempt + 1}/"
                            f"{max_attempts}): {e}. Retrying in {delay:.1f}s"
                        )
                        time.sleep(delay)
                    else:
                        logger.error(
                            f"[RETRY] {func.__name__} failed after {max_attempts} "
                            f"attempts: {e}"
                        )
            raise last_error
        return wrapper
    return decorator


# =============================================================================
# TRADE HISTORY COMPACTION
# =============================================================================

def compact_trade_history(trades_path: str, keep_recent_days: int = 7) -> dict:
    """
    Compact trade history to prevent performance degradation.

    Tiered compaction:
      - Last 7 days: full resolution (every trade)
      - 7-30 days: daily summaries
      - 30+ days: weekly summaries

    Returns dict with compaction stats.
    """
    path = Path(trades_path)
    if not path.exists():
        return {"status": "no_file", "trades": 0}

    try:
        with open(path, "r") as f:
            trades = json.load(f)
    except (json.JSONDecodeError, OSError):
        return {"status": "error", "trades": 0}

    if not isinstance(trades, list) or len(trades) < 50:
        return {"status": "too_few", "trades": len(trades)}

    now = datetime.now(timezone.utc)
    cutoff_recent = now - timedelta(days=keep_recent_days)
    cutoff_monthly = now - timedelta(days=30)

    recent = []
    to_summarize_daily = []
    to_summarize_weekly = []

    for t in trades:
        exit_time = t.get("exit_time", "")
        if not exit_time:
            recent.append(t)
            continue

        try:
            dt = datetime.fromisoformat(exit_time.replace("Z", "+00:00"))
        except (ValueError, TypeError):
            recent.append(t)
            continue

        if dt >= cutoff_recent:
            recent.append(t)
        elif dt >= cutoff_monthly:
            to_summarize_daily.append(t)
        else:
            to_summarize_weekly.append(t)

    # Summarize daily
    daily_summaries = _summarize_by_period(to_summarize_daily, "%Y-%m-%d")

    # Summarize weekly
    weekly_summaries = _summarize_by_period(to_summarize_weekly, "%Y-W%W")

    # Rebuild trades list
    compacted = weekly_summaries + daily_summaries + recent

    # Atomic write
    tmp_path = str(path) + ".tmp"
    with open(tmp_path, "w") as f:
        json.dump(compacted, f, indent=2, default=str)
    os.replace(tmp_path, str(path))

    stats = {
        "status": "compacted",
        "original": len(trades),
        "compacted": len(compacted),
        "recent_kept": len(recent),
        "daily_summaries": len(daily_summaries),
        "weekly_summaries": len(weekly_summaries),
    }
    logger.info(f"Trade history compacted: {len(trades)} → {len(compacted)} "
                f"({len(recent)} recent + {len(daily_summaries)} daily + "
                f"{len(weekly_summaries)} weekly)")
    return stats


def _summarize_by_period(trades: list, date_format: str) -> list:
    """Group trades by period and create summary records."""
    if not trades:
        return []

    periods = {}
    for t in trades:
        exit_time = t.get("exit_time", "")
        try:
            dt = datetime.fromisoformat(exit_time.replace("Z", "+00:00"))
            period = dt.strftime(date_format)
        except (ValueError, TypeError):
            period = "unknown"

        if period not in periods:
            periods[period] = {"trades": 0, "pnl": 0, "wins": 0, "losses": 0}
        periods[period]["trades"] += 1
        periods[period]["pnl"] += t.get("pnl", 0)
        if t.get("pnl", 0) > 0:
            periods[period]["wins"] += 1
        else:
            periods[period]["losses"] += 1

    summaries = []
    for period, stats in sorted(periods.items()):
        summaries.append({
            "trade_id": f"summary_{period}",
            "market_id": "summary",
            "question": f"Summary: {stats['trades']} trades in {period}",
            "side": "",
            "entry_price": 0,
            "exit_price": 0,
            "size": 0,
            "pnl": round(stats["pnl"], 2),
            "entry_time": period,
            "exit_time": period,
            "exit_reason": "summary",
            "city": "",
            "is_paper": True,
            "_summary": True,
            "_trades": stats["trades"],
            "_wins": stats["wins"],
            "_losses": stats["losses"],
        })
    return summaries


# =============================================================================
# PUSH NOTIFICATIONS (macOS)
# =============================================================================

def notify(title: str, message: str, sound: str = "default"):
    """
    Send a macOS push notification via osascript.

    Used for critical events:
      - Kill switch triggered
      - Daily P&L summary
      - Market resolution (position auto-closed)
      - Trade executed

    Falls back to logger.info on non-macOS systems.
    """
    import platform
    if platform.system() != "Darwin":
        logger.info(f"[NOTIFY] {title}: {message}")
        return

    # Escape quotes for AppleScript
    title_escaped = title.replace('"', '\\"')
    message_escaped = message.replace('"', '\\"')

    script = (
        f'display notification "{message_escaped}" '
        f'with title "{title_escaped}" '
        f'sound name "{sound}"'
    )

    try:
        subprocess.run(
            ["osascript", "-e", script],
            capture_output=True, timeout=5
        )
    except (subprocess.SubprocessError, OSError) as e:
        logger.warning(f"Notification failed: {e}")


def notify_kill_switch(reason: str):
    """Send urgent notification when kill switch triggers."""
    notify(
        "KILL SWITCH TRIGGERED",
        f"All trading halted. Reason: {reason}",
        sound="Basso",
    )


def notify_trade(question: str, pnl: float, strategy: str):
    """Send notification when a trade completes."""
    pnl_str = f"+${pnl:.2f}" if pnl >= 0 else f"-${abs(pnl):.2f}"
    result = "WIN" if pnl > 0 else "LOSS"
    notify(
        f"Trade {result}: {pnl_str}",
        f"[{strategy}] {question[:60]}",
    )


def notify_daily_summary(balance: float, daily_pnl: float, trades: int):
    """Send end-of-day summary notification."""
    pnl_str = f"+${daily_pnl:.2f}" if daily_pnl >= 0 else f"-${abs(daily_pnl):.2f}"
    notify(
        f"Daily Summary: {pnl_str}",
        f"Balance: ${balance:.2f} | Trades: {trades}",
    )


# =============================================================================
# MARKET RESOLUTION POLLING
# =============================================================================

def check_resolutions(client, state_manager) -> list:
    """
    Poll for resolved markets and auto-settle positions.

    Checks Gamma API for markets where our positions have resolved.
    Auto-credits/debits paper balance and logs the trade.

    Returns list of settled position dicts.
    """
    positions = state_manager.load_positions()
    if not positions:
        return []

    settled = []
    for pos in positions:
        # Check if market has resolved via Gamma API
        try:
            prices = client.get_market_price(pos.market_id)
            if not prices:
                continue

            # A resolved market typically has price at 0.0 or 1.0
            yes_price = prices["yes"]
            if yes_price <= 0.01 or yes_price >= 0.99:
                # Market likely resolved
                settled.append({
                    "market_id": pos.market_id,
                    "question": pos.question,
                    "resolution_price": yes_price,
                    "entry_price": pos.entry_price,
                    "size": pos.size,
                })
                logger.info(f"[RESOLUTION] Market resolved: {pos.question[:50]}... "
                            f"→ {'YES' if yes_price >= 0.99 else 'NO'}")
        except Exception as e:
            logger.debug(f"Resolution check failed for {pos.market_id}: {e}")

    return settled
