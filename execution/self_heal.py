#!/usr/bin/env python3
"""self_heal.py — repair what a machine can prove, escalate only what needs taste.

WHY (Farrice, 2026-07-27): "What good does it do that we're logging these
things if they don't get fixed and healed and corrected? We're logging stuff,
we're tracking things, but nothing self-improving or self-healing... just
allowing me to work without having to be made aware of it — if it's not that
big of a deal that really needs my eyes or my blessings or my judgment."

He is right, and the reason everything waited on him was never his
understanding. It was a MISSING CLASSIFICATION. `verify_fleet` reports 73
verifiers as pass/fail with no notion of "who fixes this," so every failure
defaults to the human. 12 red checks looked like 12 decisions. They were 3
root causes, 2 of them purely mechanical.

Worked example — the one that sat waiting for a `--bless`:
    1 of 6,596 born-intent anchors drifted: skill:dara-denney-meta-ads.
    Baseline blessed 2026-07-24 15:51. The anchor changed in commit
    f41bd34f8 "feat(dara): creative strategy layer" on 2026-07-25.
    A named feature commit IS the deliberateness evidence the bless was
    asking a human to supply. Nothing about it needed judgment.

THE CLASSIFICATION (the whole point of this module)
    AUTO      mechanical, deterministic, reversible, and self-verifying.
              Heal it, log it, never mention it.
    EVIDENCE  a human decision is required, but the evidence for it already
              exists on disk (a git commit trail). Heal it, log it, and say
              so once in /cos.
    JUDGMENT  taste, tradeoffs, or an unexplained change. NEVER auto-healed.
              Surfaced with a diagnosis instead of a stack trace.

HARD RULES — these are what keep self-healing from becoming self-deception:
  1. Allowlist only. An unknown failure is JUDGMENT by default, never healed.
  2. NEVER heal by weakening an assertion. Loosening a threshold to turn a
     check green is laundering, which is the exact failure this whole layer
     exists to stop.
  3. Every heal RE-RUNS its check. A heal that doesn't verify green is
     reported as a failed heal, never as a success.
  4. Drift with NO commit trail is never blessed. That silence is the loss
     signal the check was built to catch.
  5. Read-only by default. Healing requires `heal`.

Usage:
    python3 execution/self_heal.py report        # classify only (read-only)
    python3 execution/self_heal.py heal          # apply AUTO + EVIDENCE fixes
    python3 execution/self_heal.py report --json
Log: .agent/health/self-heal.jsonl
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEALTH = ROOT / ".agent" / "health"
FLEET_JSON = HEALTH / "verify-fleet.json"
BASELINE = HEALTH / "born-intent-baseline.json"
HEAL_LOG = HEALTH / "self-heal.jsonl"
# Two caches, deliberately separate (D1, found 2026-07-27 during verification).
# LATEST is what cos_prep.gather_self_heal() renders. It must only ever be
# written by a `heal` run. The first version wrote it in BOTH modes, and
# verify_self_heal.py shells out to `self_heal.py report` — so every Sunday
# fleet run silently replaced the heal-mode cache with a report-mode one and
# the morning brief showed findings the healer had already repaired.
LATEST = HEALTH / "self-heal-latest.json"   # heal-mode only; read by /cos
REPORT_CACHE = HEALTH / "self-heal-report.json"   # report-mode; diagnostics only
PY = str(ROOT / ".venv" / "bin" / "python3")
if not Path(PY).exists():
    PY = sys.executable

AUTO, EVIDENCE, JUDGMENT = "AUTO", "EVIDENCE", "JUDGMENT"


def _run(args: list[str], timeout: int = 180) -> subprocess.CompletedProcess:
    return subprocess.run(args, capture_output=True, text=True,
                          timeout=timeout, cwd=str(ROOT))


def _log(entry: dict) -> None:
    try:
        HEALTH.mkdir(parents=True, exist_ok=True)
        with HEAL_LOG.open("a") as f:
            f.write(json.dumps({"ts": datetime.now().isoformat(), **entry}) + "\n")
    except OSError:
        pass


# ──────────────────────────────────────────────────────────────────
# scoped auto-commit (Farrice decision 2026-07-27)
# ──────────────────────────────────────────────────────────────────
# WHY: healers write git-TRACKED files (SKILL_INDEX.md, born-intent-baseline
# .json, SLASH_COMMANDS.md). Left uncommitted they trip divergence_alarm_hook
# .py's UNCOMMITTED alarm at every session open — the operator would greet a
# warning about repairs he never made. Committing them keeps the tree clean and
# makes every automated repair a reviewable, revertible commit (all-work-on-main,
# 2026-07-13).
#
# THE SAFETY PROPERTY: `git add <explicit paths>` ONLY. Never `git add -A`.
# end_session_closeout.py:step_commit_gate legitimately adds everything because
# a human is ending a session; a 06:45 cron job must not sweep up whatever else
# happened to be in the tree. Each healer declares exactly what it may write,
# and the staged set is verified against that declaration before committing.
#
# NOTE FOR THE OPERATOR: .git/hooks/post-commit auto-pushes every commit to
# origin in the background. A self-heal commit therefore reaches GitHub
# unattended. That is Farrice's standing policy (remote = live backup), decided
# knowingly on 2026-07-27.
HEALER_WRITES = {
    "stale_registries": ("SKILL_INDEX.md", "AGENT_INDEX.md", "SLASH_COMMANDS.md",
                         ".claude/commands/"),
    "born_intent_drift": (".agent/health/born-intent-baseline.json",),
}


def _dirty_paths() -> list[str]:
    r = _run(["git", "status", "--porcelain"], timeout=30)
    out = []
    for line in (r.stdout or "").splitlines():
        if len(line) > 3:
            out.append(line[3:].strip().strip('"'))
    return out


def _commit_healed(healer_id: str, evidence: str, no_commit: bool = False) -> str:
    """Commit ONLY the files `healer_id` is declared to write. Returns a note.

    Fail-safe and fail-closed: anything unexpected aborts the commit and leaves
    the tree exactly as it was. A failed commit is never a failed heal — the
    repair already happened and stays on disk.
    """
    if no_commit:
        return "commit skipped (--no-commit; the caller owns the commit)"
    import os
    if os.environ.get("SELF_HEAL_NO_AUTOCOMMIT") == "1":
        _log({"id": healer_id, "action": "commit_declined_env"})
        return "commit DECLINED (SELF_HEAL_NO_AUTOCOMMIT=1) — logged, not silent"
    allowed = HEALER_WRITES.get(healer_id)
    if not allowed:
        return "no declared write-set — nothing committed"
    try:
        # Refuse to touch a pre-staged index: something else is mid-commit.
        staged_before = _run(["git", "diff", "--cached", "--name-only"], timeout=30)
        if (staged_before.stdout or "").strip():
            return "index already has staged changes — commit skipped, tree untouched"

        mine = [p for p in _dirty_paths() if any(p.startswith(a) for a in allowed)]
        if not mine:
            return "nothing of this healer's to commit"

        add = _run(["git", "add", "--"] + mine, timeout=60)
        if add.returncode != 0:
            return f"git add failed: {(add.stderr or '')[:120]}"

        # Verify what actually got staged is a subset of the declaration. If the
        # add pulled in anything else, unstage and abort rather than commit it.
        staged = [p for p in (_run(["git", "diff", "--cached", "--name-only"],
                                   timeout=30).stdout or "").splitlines() if p.strip()]
        stray = [p for p in staged if not any(p.startswith(a) for a in allowed)]
        if stray:
            _run(["git", "reset", "HEAD", "--"] + staged, timeout=30)
            _log({"id": healer_id, "action": "commit_aborted_stray", "stray": stray[:5]})
            return f"ABORTED — staging pulled in undeclared paths {stray[:3]}; nothing committed"

        msg = (f"chore(self-heal): {healer_id} — {evidence[:120]}\n\n"
               f"Auto-committed by execution/self_heal.py. Scoped to this healer's\n"
               f"declared write-set; nothing else staged. Revert freely.\n\n"
               "Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>")
        c = _run(["git", "commit", "-m", msg], timeout=60)
        if c.returncode != 0:
            _run(["git", "reset", "HEAD", "--"] + staged, timeout=30)
            return f"commit failed ({(c.stderr or c.stdout or '')[:100]}) — unstaged, tree restored"
        _log({"id": healer_id, "action": "committed", "files": staged})
        return f"committed {len(staged)} file(s): {', '.join(staged[:3])}"
    except Exception as e:  # noqa: BLE001 — a commit bug must never break healing
        return f"commit skipped ({type(e).__name__})"


# ──────────────────────────────────────────────────────────────────
# healer 1 — stale registries (AUTO)
# ──────────────────────────────────────────────────────────────────
def detect_stale_registries() -> dict | None:
    r = _run([PY, str(ROOT / "execution" / "verify_system.py")], timeout=120)
    if r.returncode == 0:
        return None
    if "sync_registries" not in (r.stdout + r.stderr):
        return None  # verify_system failed for some OTHER reason -> not ours
    return {"id": "stale_registries", "cls": AUTO,
            "what": "SKILL_INDEX.md / AGENT_INDEX.md are behind the filesystem",
            "fix": "python3 execution/sync_registries.py"}


def heal_stale_registries() -> tuple[bool, str]:
    r = _run([PY, str(ROOT / "execution" / "sync_registries.py")], timeout=180)
    if r.returncode != 0:
        return False, f"sync_registries exited {r.returncode}: {(r.stderr or '')[-200:]}"
    v = _run([PY, str(ROOT / "execution" / "verify_system.py")], timeout=120)
    if v.returncode != 0 and "sync_registries" in (v.stdout + v.stderr):
        return False, "registries rebuilt but verify_system still asks for a sync"
    return True, "registries rebuilt; verify_system no longer flags them"


# ──────────────────────────────────────────────────────────────────
# healer 2 — born-intent drift (EVIDENCE)
# ──────────────────────────────────────────────────────────────────
def _anchor_path(key: str) -> Path | None:
    """Resolve an anchor key back to its file. Mirrors collect_anchors() in
    verify_born_intent_drift.py — if that mapping changes, this must too."""
    try:
        kind, rest = key.split(":", 1)
    except ValueError:
        return None
    if kind == "skill":
        return ROOT / "skills" / rest / "SKILL.md"
    if kind == "workflow":
        return ROOT / ".agent" / "workflows" / f"{rest}.md"
    if kind == "agent":
        return ROOT / "agents" / rest / "AGENT.md"
    if kind == "prompt" and "/" in rest:
        skill, stem = rest.split("/", 1)
        return ROOT / "skills" / skill / "references" / "prompts-v2" / f"{stem}.md"
    return None


def _commit_evidence(path: Path | None) -> str | None:
    """The commit that makes this anchor's current text deliberate — or None.

    BUG FOUND BY RUNNING IT (2026-07-27): this first used a time window,
    `git log --since=<baseline mtime>`. That is wrong, and it flipped a
    correct EVIDENCE verdict to JUDGMENT mid-heal. `verify_born_intent_drift`
    REWRITES the baseline on every run to adopt newborn anchors (792 of them
    here), so the baseline's mtime is "last run", never "last bless". Any
    heuristic keyed to it collapses the moment the checker runs.

    Timestamp-free test instead, which is also what the question actually
    means. An anchor's current text is deliberate when it went through a
    commit:
      untracked file            -> None (no trail at all)
      uncommitted local edit    -> None (nobody has reviewed this yet)
      clean against HEAD        -> the commit line (deliberate, reviewable)
    Whole-file cleanliness is a deliberately conservative proxy for
    description cleanliness: it can only ever escalate more, never less.
    """
    if not path or not path.exists():
        return None
    try:
        if _run(["git", "ls-files", "--error-unmatch", "--", str(path)],
                timeout=30).returncode != 0:
            return None
        if _run(["git", "diff", "HEAD", "--quiet", "--", str(path)],
                timeout=30).returncode != 0:
            return None
        r = _run(["git", "log", "-1", "--format=%h %ad %s", "--date=short",
                  "--", str(path)], timeout=30)
        return (r.stdout or "").strip() or None
    except Exception:
        return None


def classify_drift(drifted: list[str]) -> dict:
    """Decide bless-vs-escalate for a set of drifted anchor keys.

    Split out from detect() so the SAFETY PROPERTY is directly testable
    without mutating the repo: an anchor with no commit trail must classify
    JUDGMENT, always. A test that can only reach this logic through a real
    fleet run is a test that will not be written.
    """
    if not drifted:
        return {"id": "born_intent_drift", "cls": JUDGMENT,
                "what": "drift check failed without naming a drifted anchor",
                "fix": "python3 execution/verify_born_intent_drift.py"}

    explained, unexplained = [], []
    for key in drifted:
        c = _commit_evidence(_anchor_path(key))
        (explained if c else unexplained).append((key, c))

    if unexplained:
        return {"id": "born_intent_drift", "cls": JUDGMENT,
                "what": (f"{len(unexplained)} anchor(s) changed with NO commit trail "
                         f"since the last bless — that silence is the loss signal: "
                         + ", ".join(k for k, _ in unexplained[:4])),
                "fix": "review, then: python3 execution/verify_born_intent_drift.py --bless",
                "detail": {"unexplained": [k for k, _ in unexplained],
                           "explained": [k for k, _ in explained]}}
    return {"id": "born_intent_drift", "cls": EVIDENCE,
            "what": (f"{len(explained)} anchor(s) drifted, every one traceable to a "
                     f"commit since the last bless"),
            "fix": "python3 execution/verify_born_intent_drift.py --bless",
            "detail": {"explained": [f"{k} <- {c}" for k, c in explained]}}


def detect_born_intent_drift() -> dict | None:
    r = _run([PY, str(ROOT / "execution" / "verify_born_intent_drift.py")], timeout=180)
    if r.returncode == 0:
        return None
    drifted = [ln.split("DRIFT", 1)[1].split("—")[0].strip()
               for ln in (r.stdout or "").splitlines() if "DRIFT " in ln]
    return classify_drift(drifted)


def heal_born_intent_drift() -> tuple[bool, str]:
    # Re-detect immediately before acting: never bless on a stale classification.
    d = detect_born_intent_drift()
    if d is None:
        return True, "already clean"
    if d["cls"] != EVIDENCE:
        return False, "escalated — drift without a commit trail is never auto-blessed"
    r = _run([PY, str(ROOT / "execution" / "verify_born_intent_drift.py"), "--bless"],
             timeout=180)
    if r.returncode != 0:
        return False, f"--bless exited {r.returncode}"
    v = _run([PY, str(ROOT / "execution" / "verify_born_intent_drift.py")], timeout=180)
    if v.returncode != 0:
        return False, "blessed but the drift check is still red"
    return True, "; ".join(d.get("detail", {}).get("explained", []))[:300]


# ──────────────────────────────────────────────────────────────────
# healer 3 — SLASH_COMMANDS.md behind .agent/workflows/ (AUTO)
# ──────────────────────────────────────────────────────────────────
def detect_stale_slash_commands() -> dict | None:
    """SLASH_COMMANDS.md is behind .agent/workflows/.

    Written as an AUTO healer, DEMOTED to JUDGMENT the first time it ran.
    `generate_slash_commands.py --check` reports 2,398 commands to append,
    then `main()` writes a 6-line diff and exits 0 — the generator is broken,
    not the index. Retrying a known-broken fix on a daily timer is how a
    self-healer turns into noise, so it is classified honestly instead.
    Re-promote to AUTO once the generator's append region actually writes.
    """
    r = _run([PY, str(ROOT / "execution" / "verify_system.py")], timeout=120)
    if r.returncode == 0:
        return None
    n = (r.stdout + r.stderr).count("is not in SLASH_COMMANDS.md")
    if not n:
        return None
    return {"id": "stale_slash_commands", "cls": JUDGMENT,
            "what": (f"{n} workflows missing from SLASH_COMMANDS.md, and the generator "
                     f"cannot fix it: `generate_slash_commands.py --check` reports 2,398 "
                     f"to append but main() writes almost nothing — a generator bug"),
            "fix": "debug the append region in execution/generate_slash_commands.py"}


HEALERS = {
    "stale_registries": (detect_stale_registries, heal_stale_registries),
    "born_intent_drift": (detect_born_intent_drift, heal_born_intent_drift),
}

def detect_platform_drift() -> dict | None:
    """Constitution / portability drift — CLASSIFY ONLY (Farrice's call, 2026-07-27).

    evolution_orchestrator.run_daily() lines 736-802 runs platform_compiler
    `check`, `lint`, and `compile --check` — three drift checks that print a
    human-run fix command and repair nothing. It is the largest instance of the
    logging-without-healing pattern this module exists to answer.

    Deliberately NOT auto-healed. `sync` / `compile --write` rewrite the
    constitution and portability files; that earns its own pass once this healer
    has a week of proven runs behind it. Classifying it at least puts the drift
    in the morning brief instead of a daily report nobody opens.
    """
    pc = ROOT / "execution" / "platform_compiler.py"
    if not pc.exists():
        return None
    try:
        r = _run([PY, str(pc), "check", "--json"], timeout=120)
        if r.returncode == 0:
            return None
        n = ""
        try:
            d = json.loads(r.stdout or "{}")
            drifted = d.get("drifted") or d.get("mismatches") or []
            n = f"{len(drifted)} " if isinstance(drifted, list) and drifted else ""
        except ValueError:
            pass
        return {"id": "platform_drift", "cls": JUDGMENT,
                "what": (f"{n}constitution/portability drift — platform_compiler reports "
                         f"siblings out of sync; the write-mode fix is deliberately not "
                         f"automated (it rewrites constitution files)"),
                "fix": "python3 execution/platform_compiler.py sync   # review the diff first"}
    except Exception:
        return None


# Detectors that only CLASSIFY (no auto-fix exists, or the fix is known broken,
# or auto-writing would be too invasive). Kept in the scan so the finding still
# surfaces; absent from HEALERS so heal() can never dispatch to them.
CLASSIFIERS = {
    "stale_slash_commands": detect_stale_slash_commands,
    "platform_drift": detect_platform_drift,
}

# Which fleet verifier each detector speaks for. Used to decide whether a red
# verifier is already REPRESENTED in the report — never to hide it.
HEALER_OWNS = {
    "stale_registries": "verify_system.py",
    "stale_slash_commands": "verify_system.py",
    "born_intent_drift": "verify_born_intent_drift.py",
    "platform_drift": "verify_platform_portability.py",
}


# ──────────────────────────────────────────────────────────────────
# unhealable fleet failures -> JUDGMENT, with a diagnosis not a stack trace
# ──────────────────────────────────────────────────────────────────
KNOWN_JUDGMENT = {
    "verify_steering_compass.py": (
        "workflow_router no longer ranks /steering-compass top-3 — the command "
        "corpus outgrew the ranking, not a broken workflow. Fix is demoting "
        "long-tail entries (routing: long-tail), which is a taste call."),
    "verify_contextual_next_prompts.py": "same root cause as verify_steering_compass.py",
    "verify_global_steering_closeout.py": "same root cause as verify_steering_compass.py",
    "verify_system_control_plane.py": (
        "cascade — it asserts on verify_operator_core_fast_proof.py, which times out"),
}


def fleet_unhealed(found_ids: set[str]) -> list[dict]:
    """Fleet failures nothing on the allowlist covers. Grouped by root cause so
    '12 failing' reads as the 3 decisions it actually is.

    HOLE CLOSED 2026-07-27: this used to skip verify_system.py and
    verify_born_intent_drift.py unconditionally, on the assumption a healer
    owned them. When verify_system started failing for a DIFFERENT reason
    (SLASH_COMMANDS.md drift, which no healer detected yet), the failure
    vanished from the report entirely — a red check rendered invisible by the
    tool built to surface red checks. A verifier is skipped now only when a
    healer ACTUALLY produced a finding for it this scan; an owned-but-
    unrepresented failure is surfaced as an explicit blind spot.
    """
    try:
        d = json.loads(FLEET_JSON.read_text())
    except (OSError, ValueError):
        return []
    represented = {HEALER_OWNS[i] for i in found_ids if i in HEALER_OWNS}
    try:
        age_d = (datetime.now()
                 - datetime.fromtimestamp(FLEET_JSON.stat().st_mtime)).days
        fleet_age = f"{age_d}d-old" if age_d else "today's"
    except OSError:
        fleet_age = "undated"
    out, timeouts = [], []
    for r in d.get("results", []):
        st = str(r.get("status", "")).upper()
        name = str(r.get("name") or r.get("script") or "")
        if st not in ("FAIL", "TIMEOUT"):
            continue
        if name in represented:
            continue  # a healer produced a finding for it — already in the report
        if st == "TIMEOUT":
            timeouts.append(name)
            continue
        if name in HEALER_OWNS.values():
            # A detector owns this verifier but found nothing, while the fleet
            # says it is red. Three possible meanings, and conflating them is
            # how a "blind detector" alarm becomes noise: the fleet snapshot
            # predates a heal, the failure is new, or the detector is blind.
            # State the snapshot's age so the reader can tell which.
            out.append({"id": name, "cls": JUDGMENT,
                        "what": (f"{name} is red in the {fleet_age} fleet snapshot but no "
                                 f"detector found a cause now — either the snapshot "
                                 f"predates a heal, or a detector is blind"),
                        "fix": f"python3 execution/{name}   # then re-run verify_fleet.py"})
            continue
        out.append({"id": name, "cls": JUDGMENT,
                    "what": KNOWN_JUDGMENT.get(name, str(r.get("message", ""))[:150]),
                    "fix": f"python3 execution/{name}"})
    if timeouts:
        out.append({"id": "fleet_timeouts", "cls": JUDGMENT,
                    "what": (f"{len(timeouts)} verifier(s) exceed the 90s budget — a perf "
                             f"problem, not a correctness one: {', '.join(timeouts[:3])}"
                             + (f" +{len(timeouts) - 3}" if len(timeouts) > 3 else "")),
                    "fix": "profile them, or raise the per-verifier budget deliberately"})
    return out


# ──────────────────────────────────────────────────────────────────
def scan() -> list[dict]:
    found = []
    detectors = [(hid, d) for hid, (d, _) in HEALERS.items()]
    detectors += list(CLASSIFIERS.items())
    for hid, detect in detectors:
        try:
            d = detect()
        except Exception as e:  # noqa: BLE001 — a broken detector must not stop the scan
            d = {"id": hid, "cls": JUDGMENT, "what": f"detector raised {type(e).__name__}",
                 "fix": "inspect execution/self_heal.py"}
        if d:
            found.append(d)
    found.extend(fleet_unhealed({f["id"] for f in found}))
    return found


def heal(found: list[dict], no_commit: bool = False) -> list[dict]:
    results = []
    for f in found:
        if f["cls"] == JUDGMENT or f["id"] not in HEALERS:
            results.append({**f, "action": "escalated"})
            continue
        try:
            ok, note = HEALERS[f["id"]][1]()
        except Exception as e:  # noqa: BLE001
            ok, note = False, f"{type(e).__name__}: {e}"
        row = {**f, "action": "healed" if ok else "heal_failed", "note": note}
        # Commit only on success, and only this healer's declared write-set.
        # A commit failure never downgrades the heal — the repair is on disk.
        if ok:
            row["commit"] = _commit_healed(f["id"], note, no_commit=no_commit)
        results.append(row)
        _log({"id": f["id"], "cls": f["cls"],
              "action": "healed" if ok else "heal_failed", "note": note,
              **({"commit": row["commit"]} if ok else {})})
    return results


def render(rows: list[dict], healed: bool) -> str:
    if not rows:
        return "SELF-HEAL — nothing to do; every allowlisted check is green."
    L = ["SELF-HEAL — " + ("applied" if healed else "report only (read-only)")]
    auto = [r for r in rows if r["cls"] in (AUTO, EVIDENCE)]
    judg = [r for r in rows if r["cls"] == JUDGMENT]
    for r in auto:
        mark = {"healed": "FIXED", "heal_failed": "COULD NOT FIX"}.get(r.get("action"), "FIXABLE")
        L.append(f"  [{mark}] {r['id']} ({r['cls']}) — {r['what']}")
        if r.get("note"):
            L.append(f"           {r['note'][:200]}")
        if not healed:
            L.append(f"           fix: {r['fix']}")
    if judg:
        L.append(f"  {len(judg)} need your judgment (never auto-healed):")
        for r in judg:
            L.append(f"    - {r['id']}: {r['what']}")
            L.append(f"      {r['fix']}")
    return "\n".join(L)


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "report"
    if mode not in ("report", "heal"):
        print(__doc__.strip().splitlines()[-6:][0], file=sys.stderr)
        print("usage: self_heal.py [report|heal] [--json]", file=sys.stderr)
        return 2
    rows = scan()
    if mode == "heal":
        rows = heal(rows, no_commit="--no-commit" in sys.argv)
        # The anti-repeat loop (Farrice 2026-07-27): every heal outcome is fed
        # to the learner, which turns recurrence into a written prevention rule.
        # Failing to learn must never fail the heal.
        try:
            sys.path.insert(0, str(ROOT / "execution"))
            import failure_learning
            failure_learning.learn()
        except Exception:
            pass
    # Cache the result. gather_self_heal() in cos_prep.py reads LATEST, never
    # the detectors: a live scan runs verify_system.py + verify_born_intent_-
    # drift.py (6,596 anchors) and pushed the morning brief past 120s. Same
    # pattern as health_metrics.py -> .agent/health/latest.json.
    #
    # A `report` run NEVER touches LATEST — see the D1 note at the top. It is a
    # read-only diagnostic and must not overwrite the record of what was healed.
    try:
        HEALTH.mkdir(parents=True, exist_ok=True)
        (LATEST if mode == "heal" else REPORT_CACHE).write_text(json.dumps(
            {"ts": datetime.now().isoformat(), "mode": mode, "rows": rows}, indent=1))
    except OSError:
        pass
    if "--json" in sys.argv:
        print(json.dumps(rows, indent=2))
    else:
        print(render(rows, healed=(mode == "heal")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
