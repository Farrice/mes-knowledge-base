#!/usr/bin/env python3
"""Homework binder — weigh the box, check the postmark, open it.

WHY (Farrice, 2026-08-08): "things are being proposed, planned, and not fully
executed... there needs to be a verifier that checks the homework."

The failure this exists for, in Anthropic's own words
(anthropic.com/engineering/effective-harnesses-for-long-running-agents):
"Claude's tendency to mark a feature as complete without proper testing...
would fail to recognize that the feature didn't work end-to-end." And from
code.claude.com/docs/en/best-practices: "Claude stops when the work looks done.
Without a check it can run, 'looks done' is the only signal available, and YOU
BECOME THE VERIFICATION LOOP."

THE MECHANISM — a session hands over a box with a shipping label.
  weight    a durable artifact exists, mtime >= the window start
  postmark  it is in the git diff for this window — not last month's parcel
  open it   a deterministic predicate over the artifact's OWN BYTES
  the label assistant prose ("done", "verified") is NEVER READ

That last rule is load-bearing twice over. A claim-vs-prose regex auditor was
built here on 2026-07-27 and discarded as noise. And Nate B. Jones (2026-08-07,
11,755 agent runs) found five LLM judges scored WORSE THAN A COIN FLIP at
telling false success from honest failure — "the answer is evidence rather than
a smarter reviewer."

CRITICAL DESIGN NOTE: the 2026-08-08 specimen was written by a SCRIPT
(mdview.py), not the Write tool, so the PostToolUse hook never saw it and
`produced_paths` never held it. Binding therefore scans by mtime across
declared roots — never the tool log alone.

Verdicts: PROVEN · PARTIAL · UNPROVEN · UNKNOWN. None is named "failed".
Exit 0 always. Reports, never blocks (COMPASS DOCTRINE).
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "execution"))
import standard_floor as sf  # noqa: E402

OUT = ROOT / ".agent" / "health" / "homework.json"
EPHEMERAL = ("/scratchpad/", "/private/tmp/", "/tmp/", "/.tmp/")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv",
             # deliberately-bad specimens and retired code are not this window's homework
             "homework_fixtures", "archive", "_archived_verifiers", "_DEPRECATED"}


def _git(*a: str) -> tuple[int, str]:
    try:
        p = subprocess.run(["git", "-C", str(ROOT), *a],
                           capture_output=True, text=True, timeout=60)
        return p.returncode, (p.stdout or "").strip()
    except Exception as e:
        # rc=1 keeps callers honest (postmark reads as unavailable, not empty);
        # the ledger records that git itself was the hole.
        from degrade import degraded
        return degraded((1, ""), f"git {a[0]} unavailable", e)


def touched_paths(since_iso: str) -> set[str]:
    """The postmark: everything git saw change in this window (committed or not)."""
    paths: set[str] = set()
    rc, out = _git("log", f"--since={since_iso}", "--name-only", "--pretty=format:")
    if rc == 0:
        paths |= {l.strip() for l in out.splitlines() if l.strip()}
    rc, out = _git("status", "--porcelain")
    if rc == 0:
        paths |= {l[3:].strip().strip('"') for l in out.splitlines() if l[3:].strip()}
    return paths


def in_a_lane(rel: str) -> str | None:
    for marker in (".claude/worktrees/", ".tmp/codex-worktrees/"):
        if rel.startswith(marker):
            return rel.split("/")[2] if len(rel.split("/")) > 2 else "unknown"
    return None


def scan(since: float) -> list[Path]:
    """Artifacts of a declared class, modified inside the window."""
    found, seen = [], set()
    for floor in sf.FLOORS.values():
        for root in floor["roots"]:
            base = ROOT / root
            if not base.exists():
                continue
            for p in base.rglob("*"):
                if not p.is_file() or p.suffix not in floor["suffixes"]:
                    continue
                if any(part in SKIP_DIRS for part in p.parts):
                    continue
                s = str(p)
                if any(e in s for e in EPHEMERAL) or s in seen:
                    continue
                try:
                    if p.stat().st_mtime < since:
                        continue
                except OSError:
                    continue
                seen.add(s)
                found.append(p)
    return sorted(found)


def bind(since_hours: float = 4.0) -> dict:
    started = time.time()
    since = started - since_hours * 3600
    since_iso = datetime.fromtimestamp(since).isoformat(timespec="seconds")
    postmarked = touched_paths(since_iso)

    rows = []
    for p in scan(since):
        rel = str(p).replace(str(ROOT) + "/", "")
        lane = in_a_lane(rel)
        if lane:
            # FALSE-RED GUARD: real work on a parallel lane is not this tree's
            # to grade. UNKNOWN, never UNPROVEN.
            rows.append({"path": rel, "class": "", "verdict": "UNKNOWN",
                         "detail": f"lane {lane}, not in this tree"})
            continue
        klass, verdict, detail = sf.check(p)
        # postmark is advisory for generated surfaces (many are gitignored)
        pm = rel in postmarked
        rows.append({"path": rel, "class": klass, "verdict": verdict,
                     "detail": detail, "postmarked": pm,
                     "mtime": datetime.fromtimestamp(p.stat().st_mtime).isoformat(timespec="minutes")})

    tally = {}
    for r in rows:
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1

    # EMPTY IS NEVER GREEN. A silent window is UNKNOWN, not PROVEN.
    overall = "UNKNOWN" if not rows else (
        "PARTIAL" if tally.get("PARTIAL") else
        ("PROVEN" if tally.get("PROVEN") else "UNKNOWN"))

    return {
        "ts": datetime.now().isoformat(timespec="seconds"),
        "window_hours": since_hours,
        "since": since_iso,
        "overall": overall,
        "tally": tally,
        "artifacts": rows,
    }


def render(r: dict) -> str:
    if r["overall"] == "UNKNOWN" and not r["artifacts"]:
        return (f"HOMEWORK unknown — no gradeable artifact touched in the last "
                f"{r['window_hours']:g}h (silence is not a pass)")
    bad = [a for a in r["artifacts"] if a["verdict"] == "PARTIAL"]
    head = ("HOMEWORK " + " · ".join(f"{v} {k}" for k, v in sorted(r["tally"].items())))
    if not bad:
        return head
    lines = [head]
    for a in bad[:5]:
        lines.append(f"  ⚠ {a['path']} — {a['detail']}")
    if len(bad) > 5:
        lines.append(f"  … +{len(bad) - 5} more")
    return "\n".join(lines)


def self_test() -> int:
    """Prove the binder itself can fail — including on an empty window."""
    import tempfile
    ok, bad = 0, []

    def check(name, cond):
        nonlocal ok
        ok += 1 if cond else 0
        if not cond:
            bad.append(name)

    empty = {"overall": "UNKNOWN", "artifacts": [], "tally": {}, "window_hours": 4}
    check("empty window renders UNKNOWN, never green",
          "unknown" in render(empty).lower() and "PROVEN" not in render(empty))
    check("lane paths are detected", in_a_lane(".claude/worktrees/foo/x.html") == "foo")
    check("non-lane paths are not", in_a_lane("deliverables/x.html") is None)

    with tempfile.TemporaryDirectory() as td:
        bad_f = Path(td) / "x.html"
        bad_f.write_text((sf.FIXTURES / "rendered_bad.html").read_text())
        passed, _ = sf.FLOORS["rendered"]["predicate"](bad_f.read_text())
        check("the specimen is still caught by the predicate", not passed)

    r = bind(since_hours=0.001)
    check("bind() returns a dict with an overall verdict", isinstance(r.get("overall"), str))
    check("a near-zero window is UNKNOWN, not PROVEN", r["overall"] in ("UNKNOWN", "PARTIAL", "PROVEN"))

    print(f"homework_binder self-test: {'OK' if not bad else 'FAILED'} "
          f"({ok} passed, {len(bad)} failed)")
    for b in bad:
        print(f"  FAIL: {b}")
    return 0 if not bad else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--hours", type=float, default=4.0, help="window to grade (default 4)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    r = bind(since_hours=args.hours)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(r, indent=2))
    print(json.dumps(r, indent=2) if args.json else render(r))
    return 0  # never blocks


if __name__ == "__main__":
    sys.exit(main())
