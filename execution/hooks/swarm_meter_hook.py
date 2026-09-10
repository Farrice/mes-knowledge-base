#!/usr/bin/env python3
"""swarm_meter_hook.py — Claude Code PreToolUse hook for matcher `Agent|Task`.

WHY: swarm_meter.py's `price` reservation is only real spend control if it
fires on every subagent dispatch, not just when a session remembers to call
it. This hook makes the meter physical, the same way cost_gate_hook.py makes
the money gate physical for paid Bash calls (read that file first — this one
mirrors its payload shape and its asymmetric fail-safe).

Behavior:
    - No active run (`state.active_run` in swarm-usage.json) -> exit 0,
      silently. Ordinary Agent/Task use outside a metered swarm is never
      gated — this hook only activates once `swarm_meter.py open` has run.
    - Active run -> price the dispatch in-process (seat = tool_input.model,
      brief bytes = len(tool_input.prompt), label = description or name).
      Success reserves the seat and allows the call (exit 0, PRICE/WARN
      lines on stderr). A STOP from swarm_meter (OVER_BUDGET, SEAT_CAP,
      BRIEF_TOO_BIG, ...) blocks the call (exit 2).

Fail-safe is ASYMMETRIC, same shape as cost_gate_hook.py:
    - exception BEFORE an active run is confirmed -> exit 0 (never break
      ordinary Agent/Task use because the meter itself hiccuped)
    - exception AFTER an active run is confirmed  -> exit 2 (a broken meter
      must not silently let an unpriced seat through a live swarm budget)

Wire via .claude/settings.json -> hooks.PreToolUse (matcher: "Agent|Task").
Run `python3 execution/hooks/swarm_meter_hook.py --self-test` after any edit.
"""

import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "execution"))


def resolve_seat(model) -> str:
    """seat = tool_input.model; default 'sonnet'; map claude-* ids to seat
    names by substring (e.g. 'claude-opus-4-1' -> 'opus')."""
    if not model:
        return "sonnet"
    m = str(model).strip().lower()
    import swarm_meter
    if m in swarm_meter.PRICING:
        return m
    for name in ("opus", "sonnet", "haiku"):
        if name in m:
            return name
    return "sonnet"


def run_hook(payload: dict):
    """Core logic, no sys.exit — returns (exit_code, stderr_message)."""
    tool_name = payload.get("tool_name")
    if tool_name not in ("Agent", "Task"):
        return 0, ""

    try:
        import swarm_meter
        usage = swarm_meter.load_usage()
        active_run = (usage.get("state") or {}).get("active_run")
    except Exception:
        return 0, ""  # fail-open: no active run confirmed yet

    if not active_run:
        return 0, ""

    # Active run confirmed — fail CLOSED from here.
    try:
        tool_input = payload.get("tool_input") or {}
        seat = resolve_seat(tool_input.get("model"))
        prompt = tool_input.get("prompt") or ""
        brief_bytes = len(prompt)
        label = tool_input.get("description") or tool_input.get("name") or "unlabeled"
        result = swarm_meter.do_price(active_run, seat, brief_bytes, label=label)
        note = " [UNCONFIRMED PRICING]" if result["unconfirmed"] else ""
        lines = [f"PRICE {result['seat']} {result['label']} est=${result['est_usd']:.2f} "
                 f"run_total=${result['projected']:.2f}/${result['budget']:.2f}{note}"]
        if result["warn"]:
            lines.append(f"WARN projected ${result['projected']:.2f} exceeds warn threshold "
                          f"${result['warn_usd']:.2f}")
        return 0, "\n".join(lines)
    except swarm_meter.SwarmMeterError as e:
        return 2, f"STOP {e.reason}: {e.message}"
    except Exception as e:
        return 2, (f"SWARM METER — unexpected {type(e).__name__} after active run '{active_run}' "
                    f"was found. Failing CLOSED: a broken meter must not let an unpriced seat "
                    f"through a live swarm budget. ({e})")


def main():
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
    except Exception:
        sys.exit(0)  # unparseable stdin before any active-run check -> fail open
    code, msg = run_hook(payload)
    if msg:
        print(msg, file=sys.stderr)
    sys.exit(code)


def self_test() -> int:
    """Golden corpus, run in a temp SWARM_METER_HOME so it never touches the
    real .agent/. Cases:
        (a) no run                                  -> 0
        (b) run budget=10, sonnet 6000-byte prompt   -> 0
        (c) budget=0.01                              -> 2, "OVER_BUDGET"
        (d) 5th seat                                 -> 2, "SEAT_CAP"
        (e) 7000-byte prompt                         -> 2, "BRIEF_TOO_BIG"
    """
    import shutil
    import tempfile

    tmp = tempfile.mkdtemp(prefix="swarm-meter-hook-selftest-")
    old_home = os.environ.get("SWARM_METER_HOME")
    os.environ["SWARM_METER_HOME"] = tmp
    results = []
    try:
        import swarm_meter

        def agent_payload(prompt_len, model="sonnet", desc="case"):
            return {"tool_name": "Agent",
                    "tool_input": {"model": model, "prompt": "x" * prompt_len, "description": desc}}

        # (a) no run at all
        code, msg = run_hook(agent_payload(100))
        results.append(("a_no_run_exit_0", code == 0, f"code={code} msg={msg!r}"))

        # (b) run budget 10, sonnet, 6000-byte prompt -> allowed
        swarm_meter.do_open("run-b", "claude", 10.0)
        code, msg = run_hook(agent_payload(6000, desc="seat-b"))
        results.append(("b_within_budget_exit_0", code == 0, f"code={code} msg={msg!r}"))

        # (c) budget 0.01 -> OVER_BUDGET
        swarm_meter.do_open("run-c", "claude", 0.01)
        code, msg = run_hook(agent_payload(100, desc="seat-c"))
        results.append(("c_over_budget_exit_2",
                         code == 2 and "OVER_BUDGET" in msg, f"code={code} msg={msg!r}"))

        # (d) 5th seat -> SEAT_CAP
        swarm_meter.do_open("run-d", "claude", 1000.0)
        for i in range(4):
            swarm_meter.do_price("run-d", "sonnet", 100, label=f"prefill-{i}")
        code, msg = run_hook(agent_payload(100, desc="seat-d-overflow"))
        results.append(("d_seat_cap_exit_2",
                         code == 2 and "SEAT_CAP" in msg, f"code={code} msg={msg!r}"))

        # (e) 7000-byte prompt -> BRIEF_TOO_BIG
        swarm_meter.do_open("run-e", "claude", 1000.0)
        code, msg = run_hook(agent_payload(7000, desc="seat-e"))
        results.append(("e_brief_too_big_exit_2",
                         code == 2 and "BRIEF_TOO_BIG" in msg, f"code={code} msg={msg!r}"))
    finally:
        if old_home is None:
            os.environ.pop("SWARM_METER_HOME", None)
        else:
            os.environ["SWARM_METER_HOME"] = old_home
        shutil.rmtree(tmp, ignore_errors=True)

    ok = True
    for name, passed, detail in results:
        print(f"{'PASS' if passed else 'FAIL'} {name} — {detail}")
        if not passed:
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    main()
