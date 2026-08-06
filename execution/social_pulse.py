#!/usr/bin/env python3
"""
Social Listening Pulse — Weekly recurring scans per lane.

Runs weekly per lane (staggered Mon/Tue/Wed), scrapes via Apify Scrape Creators actors,
synthesizes into listening briefs, outputs to .agent/cos/ for morning COS brief.

Budget model:
- Pulse sub-ledger: $5/mo dedicated to recurring pulse
- Per-lane allocation: configured in .agent/social-listening-lanes.json
- Graceful skip if pulse budget exhausted or global yellow/red state

Ledger: Every run logged to .agent/apify-usage.json + .agent/social-listening-runs.jsonl

Usage:
  python3 execution/social_pulse.py run-all      # Run all enabled lanes
  python3 execution/social_pulse.py run farrice-brand  # Run specific lane
  python3 execution/social_pulse.py status       # Show pulse budget status
  python3 execution/social_pulse.py config       # Show lane configuration
"""

import json
import os
import sys
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Dict, List, Any

REPO_ROOT = Path(__file__).parent.parent
LANES_CONFIG = REPO_ROOT / ".agent" / "social-listening-lanes.json"
USAGE_LEDGER = REPO_ROOT / ".agent" / "apify-usage.json"
RUN_LOG = REPO_ROOT / ".agent" / "social-listening-runs.jsonl"
COS_OUTPUT_DIR = REPO_ROOT / ".agent" / "cos"
APIFY_CLIENT = REPO_ROOT / "execution" / "apify_client.py"


def load_lanes_config() -> Dict[str, Any]:
    """Load lane configuration."""
    if not LANES_CONFIG.exists():
        print(f"ERROR: Lane config not found at {LANES_CONFIG}")
        sys.exit(1)
    with open(LANES_CONFIG) as f:
        return json.load(f)


def load_usage_ledger() -> Dict[str, Any]:
    """Load the Apify usage ledger."""
    if not USAGE_LEDGER.exists():
        return {}
    with open(USAGE_LEDGER) as f:
        return json.load(f)


def get_pulse_budget_status(config: Dict) -> Dict[str, Any]:
    """Get current pulse budget status."""
    ledger = load_usage_ledger()

    pulse_budget = config["global_settings"]["pulse_total_budget_monthly"]
    pulse_spent = ledger.get("pulse_spent_dollars", 0.0)
    pulse_remaining = pulse_budget - pulse_spent

    global_spent = ledger.get("spent_dollars", 0.0)
    global_budget = config["global_settings"]["global_budget_monthly"]
    global_remaining = global_budget - global_spent

    # Determine state
    global_pct = (global_spent / global_budget) * 100 if global_budget > 0 else 0
    soft_warn_pct = config["global_settings"]["soft_warn_pct"]
    hard_stop_pct = config["global_settings"]["hard_stop_pct"]

    if global_pct >= hard_stop_pct:
        state = "red"
    elif global_pct >= soft_warn_pct:
        state = "yellow"
    else:
        state = "green"

    return {
        "pulse_budget": pulse_budget,
        "pulse_spent": pulse_spent,
        "pulse_remaining": pulse_remaining,
        "global_budget": global_budget,
        "global_spent": global_spent,
        "global_remaining": global_remaining,
        "global_pct": round(global_pct, 1),
        "state": state,
    }


def run_actor_for_target(target: Dict, lane_name: str, config: Dict) -> Optional[Dict]:
    """
    Run a single Apify actor for a monitoring target.
    Handles both positional and named arguments per actor signature.

    Returns: result dict with status, data, cost, or None if skipped.
    """
    actor_key = target.get("actor")
    query = target.get("value")
    actor_mode = target.get("actor_mode", "auto")  # auto-detect or explicit mode

    if not actor_key or not query:
        return {"status": "skipped", "reason": "missing_config"}

    # Build the command based on actor type and signature
    cmd = [
        sys.executable,
        str(APIFY_CLIENT),
        actor_key,
    ]

    # Route to correct argument style per actor
    if actor_key == "sc-tiktok":
        # Flexible actor: supports --search, --profile, --hashtag
        if actor_mode == "profile":
            cmd.extend(["--profile", query])
        elif actor_mode == "hashtag":
            cmd.extend(["--hashtag", query])
        else:  # auto or search
            cmd.extend(["--search", query])

    elif actor_key == "sc-tiktok-profile":
        # Positional username
        cmd.append(query)

    elif actor_key == "sc-tiktok-hashtag":
        # Positional hashtag
        cmd.append(query)

    elif actor_key == "sc-tiktok-followers" or actor_key == "sc-tiktok-following":
        # Positional username
        cmd.append(query)

    elif actor_key == "instagram":
        # Positional handle
        cmd.append(query)

    elif actor_key == "reddit":
        # Optional positional query (can also use --subreddit)
        if query:
            cmd.append(query)

    elif actor_key == "youtube":
        # apidojo/youtube-scraper: positional keyword query (per_result pricing)
        cmd.append(query)

    elif actor_key == "sc-youtube-channels":
        # Positional channel handle/URL ONLY — the actor has no search mode
        # (verified 2026-07-21: input schema requires `channels` URL array).
        cmd.append(query)

    elif actor_key == "sc-youtube-transcripts":
        # Actor requires video URLs (no search/channel mode)
        cmd.extend(["--urls", query])

    else:
        # Fallback: treat as generic (might fail)
        cmd.append(query)

    # Add cost control args only for pay_per_event actors (Scrape Creators)
    pay_per_event_actors = {
        "sc-tiktok", "sc-tiktok-video", "sc-tiktok-profile", "sc-tiktok-hashtag",
        "sc-tiktok-transcripts", "sc-tiktok-followers", "sc-tiktok-following",
        "sc-youtube-transcripts", "sc-youtube-channels", "sc-youtube-comments"
    }
    if actor_key in pay_per_event_actors:
        cost_ceiling = config["lanes"].get(lane_name, {}).get("cost_ceiling", 0.25)
        cmd.extend(["--max-cost", str(cost_ceiling)])

    # Standard limits (only for non-positional actors)
    if actor_key not in {"instagram", "reddit"}:
        cmd.extend(["--limit", "20"])

    # Pulse runs spend from the $5/mo sub-ledger and skip (not fail) when tight
    cmd.append("--pulse-mode")

    # Run the actor with pulse_mode check
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            # 180s: run-sync actors can legitimately take >60s (Apify-side run
            # timeout is 90-150s; the old 60s subprocess timeout killed runs
            # that would have succeeded).
            timeout=180,
        )

        if result.returncode != 0:
            return {
                "status": "failed",
                "error": result.stderr,
                "actor": actor_key,
                "query": query,
            }

        # Parse the JSON output
        output = json.loads(result.stdout)

        # Check for fallback status (budget exhausted)
        if output.get("fallback"):
            return {
                "status": output.get("status", "fallback"),
                "actor": actor_key,
                "query": query,
                "reason": output.get("reason", "unknown"),
            }

        # Persist raw output to .tmp/social-listening/<date>-<lane>/ (fail-soft).
        # Filename = <actor-key>-<query-slug>.json so multiple targets on the
        # same actor within a lane don't clobber each other.
        raw_path = None
        try:
            date_str = datetime.now().strftime("%Y-%m-%d")
            raw_dir = REPO_ROOT / ".tmp" / "social-listening" / f"{date_str}-{lane_name}"
            raw_dir.mkdir(parents=True, exist_ok=True)
            slug = "".join(c if c.isalnum() else "-" for c in str(query)).strip("-")[:40] or "query"
            raw_file = raw_dir / f"{actor_key}-{slug}.json"
            with open(raw_file, "w") as f:
                json.dump(output, f, indent=2)
            raw_path = str(raw_file)
        except Exception:
            pass  # raw persistence must never break the run

        # Success (note: client reports cost as "cost_dollars")
        return {
            "status": "success",
            "actor": actor_key,
            "query": query,
            "items": len(output.get("items", [])),
            "cost": output.get("cost_dollars", output.get("cost", 0.0)),
            "raw_path": raw_path,
            "data": output,
        }

    except subprocess.TimeoutExpired:
        return {
            "status": "timeout",
            "actor": actor_key,
            "query": query,
        }
    except json.JSONDecodeError as e:
        return {
            "status": "parse_error",
            "error": str(e),
            "actor": actor_key,
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "actor": actor_key,
        }


def synthesize_listening_brief(lane_name: str, results: List[Dict]) -> str:
    """
    Synthesize raw Apify results into a listening brief.
    """
    timestamp = datetime.now(timezone.utc).isoformat()

    # Extract successful data
    successful_results = [r for r in results if r.get("status") == "success"]
    skipped_results = [r for r in results if r.get("status") in ("pulse_skipped", "fallback")]
    failed_results = [r for r in results if r.get("status") in ("failed", "timeout", "error")]

    # Build receipts table
    receipts = []
    total_items = 0
    total_cost = 0.0

    for result in results:
        if result.get("status") == "success":
            receipts.append([
                result.get("actor", "—"),
                result.get("query", "—"),
                str(result.get("items", 0)),
                f"${result.get('cost', 0.0):.2f}",
                "✓",
            ])
            total_items += result.get("items", 0)
            total_cost += result.get("cost", 0.0)
        elif result.get("status") == "pulse_skipped":
            receipts.append([
                result.get("actor", "—"),
                result.get("query", "—"),
                "—",
                "—",
                f"⊘ pulse budget",
            ])
        elif result.get("status") == "fallback":
            receipts.append([
                result.get("actor", "—"),
                result.get("query", "—"),
                "—",
                "—",
                f"⊘ {result.get('reason', 'budget')}",
            ])
        else:
            receipts.append([
                result.get("actor", "—"),
                "—",
                "—",
                "—",
                f"✗ {result.get('status', 'error')}",
            ])

    # Format receipts table as markdown
    receipts_md = "| Actor | Query | Items | Cost | Status |\n"
    receipts_md += "|-------|-------|-------|------|--------|\n"
    for row in receipts:
        receipts_md += f"| {' | '.join(row)} |\n"

    # Build brief markdown
    brief = f"""# Social Listening Pulse: {lane_name}

**Generated**: {timestamp}
**Status**: {'✓ Complete' if not skipped_results and not failed_results else '⚠ Partial' if skipped_results else '✗ Failed'}

---

## Data Collection

{receipts_md}

**Summary**: {total_items} items collected | ${total_cost:.2f} spent

"""

    # Add skip/failure notes if applicable
    if skipped_results:
        brief += f"\n⚠ **Note**: {len(skipped_results)} actor(s) skipped due to pulse budget constraints or global budget state.\n"

    if failed_results:
        brief += f"\n✗ **Errors**: {len(failed_results)} actor(s) failed. Check logs for details.\n"

    # Add recommendations
    brief += """
---

## Recommendations

- Check for emerging trends in the data above
- Review actual actor outputs in `.tmp/social-listening/` for full detail
- Schedule follow-up deep dives via `/social-listen` if strategic themes emerge
"""

    return brief


def log_pulse_run(lane_name: str, results: List[Dict], config: Dict):
    """
    Log the pulse run to .agent/social-listening-runs.jsonl (JSONL format for streaming).
    """
    COS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Prepare log entry
    successful = [r for r in results if r.get("status") == "success"]
    total_cost = sum(r.get("cost", 0.0) for r in successful)

    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "lane": lane_name,
        "actors_run": len(results),
        "actors_success": len(successful),
        "total_cost": round(total_cost, 4),
        "status": "partial" if any(r.get("status") in ("failed", "fallback") for r in results) else "success",
        "results_summary": {
            "successful": len(successful),
            "skipped": len([r for r in results if r.get("status") == "pulse_skipped"]),
            "failed": len([r for r in results if r.get("status") in ("failed", "timeout", "error")]),
        },
    }

    # Append to JSONL log
    RUN_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(RUN_LOG, "a") as f:
        f.write(json.dumps(log_entry) + "\n")


def run_pulse_lane(lane_name: str, config: Dict) -> Dict:
    """
    Run a complete pulse cycle for a single lane.

    Returns: status dict with results, cost, etc.
    """
    lane = config["lanes"].get(lane_name)
    if not lane:
        return {"status": "error", "reason": f"lane {lane_name} not found"}

    if not lane.get("enabled"):
        return {"status": "disabled", "reason": f"lane {lane_name} is disabled"}

    # Check budget before proceeding
    budget_status = get_pulse_budget_status(config)
    if budget_status["state"] == "red":
        return {
            "status": "pulse_skipped",
            "reason": "global_budget_red",
            "budget_status": budget_status,
        }

    # Run each monitoring target
    results = []
    for target in lane.get("monitoring_targets", []):
        result = run_actor_for_target(target, lane_name, config)
        if result:
            results.append(result)

    # Synthesize brief
    brief_md = synthesize_listening_brief(lane_name, results)

    # Save to .agent/cos/
    COS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    brief_path = COS_OUTPUT_DIR / f"{date_str}-{lane_name}-pulse.md"
    with open(brief_path, "w") as f:
        f.write(brief_md)

    # Log the run
    log_pulse_run(lane_name, results, config)

    # Honest lane status: any actor error OR zero items collected across all
    # targets means the lane produced no usable signal → "degraded", never
    # "success". (Previously this always said success even when every actor
    # failed — the routine-health channel couldn't see empty runs.)
    successful = [r for r in results if r.get("status") == "success"]
    total_items = sum(r.get("items", 0) for r in successful)
    failed = [r for r in results if r.get("status") in ("failed", "timeout", "error", "parse_error")]
    lane_status = "degraded" if (failed or total_items == 0) else "success"

    return {
        "status": lane_status,
        "lane": lane_name,
        "results_count": len(results),
        "total_items": total_items,
        "failed_actors": len(failed),
        "brief_saved_to": str(brief_path),
    }


def cmd_run_all(config: Dict):
    """Run all enabled lanes. Exit 2 if any lane is degraded."""
    print("🎧 Social Listening Pulse — Running all lanes...\n")

    any_degraded = False
    for lane_name, lane in config["lanes"].items():
        if lane.get("enabled"):
            print(f"  Running {lane_name}...")
            result = run_pulse_lane(lane_name, config)
            if result.get("status") == "success":
                print(f"    ✓ {result.get('results_count')} actors completed, {result.get('total_items')} items")
            elif result.get("status") == "degraded":
                any_degraded = True
                print(f"    ✗ degraded: {result.get('total_items', 0)} items, "
                      f"{result.get('failed_actors', 0)} failed actor(s)")
            else:
                print(f"    ⚠ {result.get('status')}: {result.get('reason', '')}")

    if any_degraded:
        sys.exit(2)


def cmd_run_lane(lane_name: str, config: Dict):
    """Run a specific lane. Exit codes: 0 success, 2 degraded (errors or zero items), 1 crash."""
    print(f"🎧 Social Listening Pulse — {lane_name}\n")
    result = run_pulse_lane(lane_name, config)
    # Don't dump full raw data into stdout — raw JSON lives in .tmp/social-listening/
    printable = {k: v for k, v in result.items() if k != "data"}
    print(json.dumps(printable, indent=2))
    if result.get("status") == "degraded":
        sys.exit(2)
    if result.get("status") == "error":
        sys.exit(1)


def cmd_status(config: Dict):
    """Show budget status."""
    status = get_pulse_budget_status(config)
    print("📊 Social Listening Pulse Budget Status\n")
    print(f"Global Budget: ${status['global_spent']:.2f} / ${status['global_budget']:.2f} ({status['global_pct']:.1f}%) [{status['state'].upper()}]")
    print(f"Pulse Budget:  ${status['pulse_spent']:.2f} / ${status['pulse_budget']:.2f} ({(status['pulse_spent']/status['pulse_budget']*100):.1f}%)\n")
    print(f"Remaining: Global ${status['global_remaining']:.2f} | Pulse ${status['pulse_remaining']:.2f}")


def cmd_config(config: Dict):
    """Show lane configuration."""
    print("📋 Social Listening Lane Configuration\n")
    for lane_name, lane in config["lanes"].items():
        status = "🟢" if lane.get("enabled") else "⚫"
        print(f"{status} {lane_name}")
        print(f"   Schedule: {lane.get('schedule', {}).get('day_of_week', 'N/A')} @ {lane.get('schedule', {}).get('time', 'N/A')}")
        print(f"   Budget allocation: ${lane.get('pulse_budget_allocation', 0.0)}/mo")
        print(f"   Targets: {len(lane.get('monitoring_targets', []))} items\n")


def main():
    config = load_lanes_config()

    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "run-all":
        cmd_run_all(config)
    elif cmd == "run" and len(sys.argv) > 2:
        cmd_run_lane(sys.argv[2], config)
    elif cmd == "status":
        cmd_status(config)
    elif cmd == "config":
        cmd_config(config)
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
