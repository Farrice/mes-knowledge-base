#!/usr/bin/env python3
"""verify_swarm_meter.py — exercises execution/swarm_meter.py end to end.

Covers every subcommand in both directions (pass path + each documented STOP
reason), the round cap, `reconcile` against the committed fixtures under
execution/fixtures/swarm_meter/ (both harnesses), `close`'s required keys and
est/actual basis switch, and shells out to swarm_meter_hook.py --self-test.

Runs entirely inside a temp SWARM_METER_HOME (never the real .agent/). Prints
ok/FAIL per check and a final "N pass / M fail" line; exits 1 on any fail.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
METER = REPO_ROOT / "execution" / "swarm_meter.py"
HOOK = REPO_ROOT / "execution" / "hooks" / "swarm_meter_hook.py"
FIXTURES = REPO_ROOT / "execution" / "fixtures" / "swarm_meter"

RESULTS = []


def check(name, cond, detail=""):
    ok = bool(cond)
    RESULTS.append((name, ok))
    tag = "ok  " if ok else "FAIL"
    suffix = f" — {detail}" if (detail and not ok) else ""
    print(f"{tag} {name}{suffix}")


def run_cli(args, env):
    proc = subprocess.run([sys.executable, str(METER)] + args, env=env,
                           capture_output=True, text=True, cwd=str(REPO_ROOT))
    return proc.returncode, proc.stdout, proc.stderr


def run_json(env, kind, run_id):
    p = Path(env["SWARM_METER_HOME"]) / kind / f"{run_id}.json"
    return json.loads(p.read_text())


def main():
    tmp = tempfile.mkdtemp(prefix="swarm-meter-verify-")
    env = dict(os.environ)
    env["SWARM_METER_HOME"] = tmp
    try:
        _run(env)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    passed = sum(1 for _, ok in RESULTS if ok)
    failed = len(RESULTS) - passed
    print(f"\n{passed} pass / {failed} fail")
    sys.exit(1 if failed else 0)


def _run(env):
    home = Path(env["SWARM_METER_HOME"])

    # --- open ---------------------------------------------------------
    rc, out, err = run_cli(["open", "--budget", "10.0", "--run", "verify-run", "--harness", "claude"], env)
    check("open: exits 0", rc == 0, err)
    run_path = home / "swarm-runs" / "verify-run.json"
    check("open: writes run file", run_path.exists())
    run = json.loads(run_path.read_text())
    required_keys = ["run_id", "harness", "budget_usd", "warn_usd", "spent_est_usd", "spent_actual_usd",
                      "seats", "rounds", "max_seats", "max_rounds", "max_brief_bytes", "opened_ts",
                      "closed_ts", "status"]
    check("open: run has all required keys", all(k in run for k in required_keys),
          [k for k in required_keys if k not in run])
    check("open: warn_usd = 0.7 * budget", abs(run["warn_usd"] - 7.0) < 1e-6, run["warn_usd"])
    check("open: status OPEN", run["status"] == "OPEN", run["status"])
    usage_path = home / "swarm-usage.json"
    check("open: creates swarm-usage.json", usage_path.exists())
    usage = json.loads(usage_path.read_text())
    check("open: usage schema tag present", usage.get("_schema") == "swarm-usage-v1", usage.get("_schema"))
    check("open: sets state.active_run", usage["state"]["active_run"] == "verify-run", usage["state"])

    # --- price: pass path ----------------------------------------------
    rc, out, err = run_cli(
        ["price", "--seat", "sonnet", "--brief-bytes", "1000", "--label", "critic-1", "--run", "verify-run"], env)
    check("price: pass exits 0", rc == 0, err or out)
    check("price: prints PRICE receipt", out.startswith("PRICE"), out)
    check("price: reserves seat on run", len(run_json(env, "swarm-runs", "verify-run")["seats"]) == 1)

    # --- price: BRIEF_TOO_BIG -------------------------------------------
    rc, out, err = run_cli(
        ["price", "--seat", "sonnet", "--brief-bytes", "7000", "--run", "verify-run"], env)
    check("price: BRIEF_TOO_BIG exits 1", rc == 1, out)
    check("price: BRIEF_TOO_BIG reason in output", "BRIEF_TOO_BIG" in out, out)
    check("price: BRIEF_TOO_BIG did not reserve a seat",
          len(run_json(env, "swarm-runs", "verify-run")["seats"]) == 1)

    # --- price: SEAT_CAP (fill to max_seats=4, then overflow) ----------
    for i in range(3):
        rc, out, err = run_cli(
            ["price", "--seat", "haiku", "--brief-bytes", "100", "--label", f"seat-{i}", "--run", "verify-run"],
            env)
        check(f"price: fills seat {i + 2}/4 exits 0", rc == 0, out)
    rc, out, err = run_cli(
        ["price", "--seat", "haiku", "--brief-bytes", "100", "--label", "overflow", "--run", "verify-run"], env)
    check("price: SEAT_CAP exits 1", rc == 1, out)
    check("price: SEAT_CAP reason in output", "SEAT_CAP" in out, out)

    # --- price: OVER_BUDGET ---------------------------------------------
    run_cli(["open", "--budget", "0.001", "--run", "verify-over", "--harness", "claude"], env)
    rc, out, err = run_cli(["price", "--seat", "opus", "--brief-bytes", "1000", "--run", "verify-over"], env)
    check("price: OVER_BUDGET exits 1", rc == 1, out)
    check("price: OVER_BUDGET reason in output", "OVER_BUDGET" in out, out)

    # --- price: WARN (passes, but crosses the 0.7x warn line) ----------
    run_cli(["open", "--budget", "0.01", "--run", "verify-warn", "--harness", "claude"], env)
    rc, out, err = run_cli(
        ["price", "--seat", "haiku", "--brief-bytes", "0", "--out-tokens", "1200", "--run", "verify-warn"], env)
    check("price: WARN case still exits 0", rc == 0, out)
    check("price: WARN line printed", "WARN" in out, out)

    # --- charge: pass path + LABEL_NOT_FOUND ----------------------------
    run_cli(["open", "--budget", "50.0", "--run", "verify-charge", "--harness", "claude"], env)
    run_cli(["price", "--seat", "sonnet", "--brief-bytes", "1000", "--label", "critic-x", "--run", "verify-charge"],
            env)
    rc, out, err = run_cli(["charge", "--run", "verify-charge", "--label", "critic-x", "--in", "1000", "--out", "300"],
                            env)
    check("charge: pass exits 0", rc == 0, err or out)
    check("charge: prints CHARGE receipt", out.startswith("CHARGE"), out)
    seat = run_json(env, "swarm-runs", "verify-charge")["seats"][0]
    check("charge: seat actual_usd set", seat["actual_usd"] is not None, seat)
    rc, out, err = run_cli(["charge", "--run", "verify-charge", "--label", "nope", "--in", "1", "--out", "1"], env)
    check("charge: LABEL_NOT_FOUND exits 1", rc == 1, out)
    check("charge: LABEL_NOT_FOUND reason in output", "LABEL_NOT_FOUND" in out, out)

    # --- round: pass path + ROUND_CAP -----------------------------------
    run_cli(["open", "--budget", "10.0", "--run", "verify-round", "--harness", "claude"], env)
    for i in range(3):
        rc, out, err = run_cli(["round", "--run", "verify-round"], env)
        check(f"round: round {i + 1}/3 exits 0", rc == 0, out)
    rc, out, err = run_cli(["round", "--run", "verify-round"], env)
    check("round: ROUND_CAP exits 1", rc == 1, out)
    check("round: ROUND_CAP reason in output", "ROUND_CAP" in out, out)
    check("round: rounds did not exceed max_rounds",
          run_json(env, "swarm-runs", "verify-round")["rounds"] == 3)

    # --- status ----------------------------------------------------------
    rc, out, err = run_cli(["status", "--run", "verify-round"], env)
    check("status: exits 0", rc == 0, err)
    check("status: prints run JSON", out.strip().startswith("{") and '"run_id"' in out, out[:80])

    # --- reconcile: RUN_NOT_FOUND (bad-input direction) -------------------
    rc, out, err = run_cli(["reconcile", "--run", "does-not-exist", "--harness", "claude"], env)
    check("reconcile: RUN_NOT_FOUND exits 1", rc == 1, out)
    check("reconcile: RUN_NOT_FOUND reason in output", "RUN_NOT_FOUND" in out, out)

    # --- reconcile: claude fixture ----------------------------------------
    run_cli(["open", "--budget", "10.0", "--run", "test-run", "--harness", "claude"], env)
    run_cli(["price", "--seat", "sonnet", "--brief-bytes", "500", "--label", "bar-gap critic", "--run", "test-run"],
            env)
    subagents_dir = str(FIXTURES / "claude" / "subagents")
    rc, out, err = run_cli(
        ["reconcile", "--run", "test-run", "--harness", "claude", "--subagents-dir", subagents_dir], env)
    check("reconcile(claude): exits 0", rc == 0, err or out)
    check("reconcile(claude): prints an actual= line", "actual=" in out, out)
    seat = run_json(env, "swarm-runs", "test-run")["seats"][0]
    check("reconcile(claude): charges the seat", seat["actual_usd"] is not None, seat)
    p_in, p_out = 3, 15  # sonnet
    expected = (3 * 1200 * p_in + 3 * 2000 * p_in * 0.10 + 3 * 300 * p_in * 1.25) / 1e6 + 3 * 400 * p_out / 1e6
    check("reconcile(claude): actual matches cache-weighted formula",
          abs(seat["actual_usd"] - round(expected, 4)) < 1e-3, (seat["actual_usd"], expected))

    # --- reconcile: never prints UNMEASURED for a matched seat, does for a
    #     genuinely unmatched one -----------------------------------------
    run_cli(["open", "--budget", "10.0", "--run", "unmeasured-run", "--harness", "claude"], env)
    run_cli(["price", "--seat", "sonnet", "--brief-bytes", "100", "--label", "ghost-seat", "--run", "unmeasured-run"],
            env)
    rc, out, err = run_cli(
        ["reconcile", "--run", "unmeasured-run", "--harness", "claude", "--subagents-dir", subagents_dir], env)
    check("reconcile: prints UNMEASURED for a seat with no matching transcript", "UNMEASURED" in out, out)
    rc, out, err = run_cli(
        ["reconcile", "--run", "test-run", "--harness", "claude", "--subagents-dir", subagents_dir], env)
    check("reconcile: never prints UNMEASURED once a transcript matched", "UNMEASURED" not in out, out)

    # --- reconcile: codex fixture ------------------------------------------
    run_cli(["open", "--budget", "10.0", "--run", "codex-run", "--harness", "codex"], env)
    run_cli(["price", "--seat", "sonnet", "--brief-bytes", "500", "--label", "codex-seat", "--run", "codex-run"], env)
    sessions_dir = str(FIXTURES / "codex")
    rc, out, err = run_cli(
        ["reconcile", "--run", "codex-run", "--harness", "codex", "--sessions-dir", sessions_dir,
         "--parent", "parent-1"], env)
    check("reconcile(codex): exits 0", rc == 0, err or out)
    check("reconcile(codex): prints an actual= line", "actual=" in out, out)
    seat2 = run_json(env, "swarm-runs", "codex-run")["seats"][0]
    check("reconcile(codex): charges the seat", seat2["actual_usd"] is not None, seat2)
    expected2 = (5000 * p_in + 3000 * p_in * 0.10) / 1e6 + 900 * p_out / 1e6
    check("reconcile(codex): actual matches cached-token formula",
          abs(seat2["actual_usd"] - round(expected2, 4)) < 1e-3, (seat2["actual_usd"], expected2))

    # --- reconcile: codex missing --parent -----------------------------
    run_cli(["open", "--budget", "10.0", "--run", "codex-noparent", "--harness", "codex"], env)
    rc, out, err = run_cli(["reconcile", "--run", "codex-noparent", "--harness", "codex",
                             "--sessions-dir", sessions_dir], env)
    check("reconcile(codex): MISSING_PARENT exits 1", rc == 1, out)
    check("reconcile(codex): MISSING_PARENT reason in output", "MISSING_PARENT" in out, out)

    # --- close: required keys, receipt shape, log entry ------------------
    rc, out, err = run_cli(["close", "--run", "verify-charge", "--dissent", "1"], env)
    check("close: exits 0", rc == 0, err or out)
    check("close: prints Swarm: receipt", out.startswith("Swarm:"), out)
    check("close: receipt reports dissent", "dissent=1" in out, out)
    closed_run = run_json(env, "swarm-runs", "verify-charge")
    check("close: status CLOSED when all seats charged", closed_run["status"] == "CLOSED", closed_run["status"])
    check("close: sets closed_ts", closed_run["closed_ts"] is not None)
    usage_after = json.loads(usage_path.read_text())
    check("close: clears active_run when it matches the closed run",
          usage_after["state"]["active_run"] != "verify-charge", usage_after["state"])
    check("close: appends a log entry",
          any(entry["run_id"] == "verify-charge" for entry in usage_after["log"]), usage_after["log"])
    check("close: log entry basis is 'actual' (seat was charged)",
          next(e for e in usage_after["log"] if e["run_id"] == "verify-charge")["basis"] == "actual")

    # --- close: --partial with an unmeasured seat -> PARTIAL ------------
    run_cli(["open", "--budget", "10.0", "--run", "verify-partial", "--harness", "claude"], env)
    run_cli(["price", "--seat", "sonnet", "--brief-bytes", "100", "--label", "unc", "--run", "verify-partial"], env)
    rc, out, err = run_cli(["close", "--run", "verify-partial", "--partial"], env)
    check("close --partial: exits 0", rc == 0, err or out)
    partial_run = run_json(env, "swarm-runs", "verify-partial")
    check("close --partial: status PARTIAL when a seat is unmeasured",
          partial_run["status"] == "PARTIAL", partial_run["status"])

    # --- close: without --partial stays CLOSED even with unmeasured seats -
    run_cli(["open", "--budget", "10.0", "--run", "verify-closed-anyway", "--harness", "claude"], env)
    run_cli(["price", "--seat", "sonnet", "--brief-bytes", "100", "--label", "unc2", "--run", "verify-closed-anyway"],
            env)
    rc, out, err = run_cli(["close", "--run", "verify-closed-anyway"], env)
    check("close (no --partial): exits 0", rc == 0, err or out)
    default_close_run = run_json(env, "swarm-runs", "verify-closed-anyway")
    check("close (no --partial): status stays CLOSED", default_close_run["status"] == "CLOSED",
          default_close_run["status"])

    # --- close: RUN_NOT_FOUND -------------------------------------------
    rc, out, err = run_cli(["close", "--run", "does-not-exist"], env)
    check("close: RUN_NOT_FOUND exits 1", rc == 1, out)
    check("close: RUN_NOT_FOUND reason in output", "RUN_NOT_FOUND" in out, out)

    # --- hook self-test ----------------------------------------------------
    proc = subprocess.run([sys.executable, str(HOOK), "--self-test"], env=env,
                           capture_output=True, text=True, cwd=str(REPO_ROOT))
    check("swarm_meter_hook.py --self-test passes", proc.returncode == 0, proc.stdout + proc.stderr)


if __name__ == "__main__":
    main()
