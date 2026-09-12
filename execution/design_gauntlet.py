#!/usr/bin/env python3
"""design_gauntlet.py — the design gauntlet as a state machine on disk (2026-09-11, agent-loops-real L5).

Scar: `/design-gauntlet` existed as a workflow (canon: skills/jack-roberts-design-mastery/workflows/
design-gauntlet.md) with one ad hoc receipt in six weeks and no runner — screenshots, verdicts,
repairs and "surviving risks" were chat output, so Farrice could not tell whether a gauntlet ever
ran on his design work. This runner performs every transition and writes the receipt; the model
still does the looking (critic) and the editing (repair). Rule it obeys: a loop exists only when
a script performs the transition and writes a receipt file.

State lives beside the artifact: <artifact dir>/gauntlet/<slug>/ (or --out):
  fingerprint.json          Phase 1 context fingerprint (artifact, mode, bar, preserve, never)
  round-N/{desktop,tablet,mobile}.png   Phase 3 screenshots (captured by whatever renderer exists,
                            or attached by the model from the Playwright MCP / Browser pane)
  round-N/verdict.json      Phase 4 blind-bar verdict (A|B|TIE|INCOMPARABLE, gap, evidence)
  round-N/repair.json       Phase 5 bounded repair (what changed, checks re-run)
  GAUNTLET-RECEIPT.md       the receipt: rounds, verdicts, repairs (cap 2), surviving risks,
                            VISUAL VERIFIED vs VISUAL UNVERIFIED per round
Global log: .agent/design-gauntlet-log.jsonl (one line per open/close) — the evidence it ran.

Usage:
  python3 execution/design_gauntlet.py open <slug> --artifact <path|url> --bar <path|url> --mode "Precision Polish|Theme-Respect Elevate|Creative Unleash" [--preserve ...] [--never ...] [--out DIR]
  python3 execution/design_gauntlet.py shoot <slug> [--round N]           # tries a headless renderer; else prints the MCP capture plan
  python3 execution/design_gauntlet.py attach <slug> --round N --desktop p.png --tablet p.png --mobile p.png
  python3 execution/design_gauntlet.py verdict <slug> --round N --verdict A|B|TIE|INCOMPARABLE --gap "…" --evidence "…" [--preserve "…"]
  python3 execution/design_gauntlet.py repair <slug> --round N --did "…" [--checks "…"]   # cap 2 (blind-bar default); a third nudges
  python3 execution/design_gauntlet.py close <slug> --risks "…" [--verdict PASS|FAIL]
  python3 execution/design_gauntlet.py status <slug>
Exit 0 on success; 1 on a refused transition (e.g. verdict before a baseline shoot).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / ".agent" / "design-gauntlet-log.jsonl"
VIEWPORTS = {"desktop": (1440, 900), "tablet": (768, 1024), "mobile": (375, 667)}
REPAIR_CAP = 2
MODES = ("Precision Polish", "Theme-Respect Elevate", "Creative Unleash")


def now() -> str:
    return _dt.datetime.now().astimezone().isoformat(timespec="seconds")


def gdir(slug: str, out: str | None = None, artifact: str | None = None) -> Path:
    if out:
        return Path(out).resolve()
    env = os.environ.get("DESIGN_GAUNTLET_ROOT")
    if env:
        return Path(env).resolve() / slug
    if artifact and not artifact.startswith("http"):
        return Path(artifact).resolve().parent / "gauntlet" / slug
    return ROOT / ".tmp" / "gauntlet" / slug


def find_dir(slug: str) -> Path | None:
    env = os.environ.get("DESIGN_GAUNTLET_ROOT")
    cands = [Path(env) / slug] if env else []
    cands += [ROOT / ".tmp" / "gauntlet" / slug]
    idx = ROOT / ".agent" / "design-gauntlet-index.json"
    if idx.exists():
        try:
            p = json.loads(idx.read_text()).get(slug)
            if p:
                cands.insert(0, Path(p))
        except Exception:
            pass
    for c in cands:
        if (c / "fingerprint.json").exists():
            return c
    return None


def index_put(slug: str, d: Path) -> None:
    idx = ROOT / ".agent" / "design-gauntlet-index.json"
    try:
        data = json.loads(idx.read_text()) if idx.exists() else {}
    except Exception:
        data = {}
    data[slug] = str(d)
    idx.parent.mkdir(parents=True, exist_ok=True)
    idx.write_text(json.dumps(data, indent=2))


def log(rec: dict) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec) + "\n")


def load_fp(d: Path) -> dict:
    return json.loads((d / "fingerprint.json").read_text(encoding="utf-8"))


def rounds(d: Path) -> list[int]:
    return sorted(int(p.name.split("-")[1]) for p in d.glob("round-*") if p.is_dir())


def shots_of(d: Path, n: int) -> dict:
    return {v: (d / f"round-{n}" / f"{v}.png") for v in VIEWPORTS}


def visual_state(d: Path, n: int) -> str:
    return "VISUAL VERIFIED" if all(p.exists() and p.stat().st_size > 0 for p in shots_of(d, n).values()) else "VISUAL UNVERIFIED"


def write_receipt(d: Path, closing: dict | None = None) -> Path:
    fp = load_fp(d)
    lines = [f"# GAUNTLET RECEIPT — {fp['slug']}", "",
             f"- artifact: {fp['artifact']}", f"- mode: {fp['mode']}", f"- bar: {fp['bar']}",
             f"- preserve: {fp.get('preserve') or '—'}", f"- never: {fp.get('never') or '—'}",
             f"- opened: {fp['opened']}", ""]
    reps = 0
    for n in rounds(d):
        rd = d / f"round-{n}"
        lines.append(f"## Round {n} — {visual_state(d, n)}")
        for v, p in shots_of(d, n).items():
            lines.append(f"- {v}: {p if p.exists() else 'NOT CAPTURED'}")
        vj = rd / "verdict.json"
        if vj.exists():
            v = json.loads(vj.read_text())
            lines += [f"- verdict: {v['verdict']} · gap: {v['gap']}", f"- evidence: {v['evidence']}"]
            if v.get("preserve"):
                lines.append(f"- preserve: {v['preserve']}")
        else:
            lines.append("- verdict: none recorded")
        rj = rd / "repair.json"
        if rj.exists():
            reps += 1
            r = json.loads(rj.read_text())
            lines.append(f"- repair {reps}/{REPAIR_CAP}: {r['did']}" + (f" · checks re-run: {r['checks']}" if r.get("checks") else ""))
        lines.append("")
    if closing:
        lines += ["## Close", f"- verdict: {closing['verdict']}", f"- surviving risks: {closing['risks']}",
                  f"- repairs used: {reps}/{REPAIR_CAP}", f"- closed: {closing['closed']}", ""]
    else:
        lines += ["## Close", "- open", ""]
    rp = d / "GAUNTLET-RECEIPT.md"
    rp.write_text("\n".join(lines), encoding="utf-8")
    return rp


def try_render(artifact: str, rd: Path) -> tuple[bool, str]:
    """Headless capture if a renderer exists (python playwright); else False + reason."""
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except Exception:
        return False, "python playwright not installed"
    url = artifact if artifact.startswith("http") else Path(artifact).resolve().as_uri()
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            for v, (w, h) in VIEWPORTS.items():
                pg = b.new_page(viewport={"width": w, "height": h})
                pg.goto(url, wait_until="networkidle")
                pg.screenshot(path=str(rd / f"{v}.png"), full_page=True)
                pg.close()
            b.close()
        return True, "playwright"
    except Exception as e:  # noqa: BLE001
        return False, f"playwright failed: {e}"


def cmd_open(a):
    if a.mode not in MODES:
        print(f"mode must be one of {MODES}")
        return 1
    d = gdir(a.slug, a.out, a.artifact)
    d.mkdir(parents=True, exist_ok=True)
    fp = {"slug": a.slug, "artifact": a.artifact, "bar": a.bar, "mode": a.mode, "preserve": a.preserve or "",
          "never": a.never or "", "opened": now(), "dir": str(d)}
    (d / "fingerprint.json").write_text(json.dumps(fp, indent=2), encoding="utf-8")
    index_put(a.slug, d)
    log({"ts": now(), "event": "open", "slug": a.slug, "artifact": a.artifact, "mode": a.mode, "dir": str(d)})
    rp = write_receipt(d)
    print(f"GAUNTLET OPEN — {a.slug} · mode {a.mode} · dir {d}\n  receipt: {rp}\n  next: python3 execution/design_gauntlet.py shoot {a.slug}   (baseline before any taste call)")
    return 0


def cmd_shoot(a):
    d = find_dir(a.slug)
    if not d:
        print(f"no gauntlet '{a.slug}' — open it first")
        return 1
    fp = load_fp(d)
    n = a.round or (max(rounds(d)) + 1 if rounds(d) else 1)
    rd = d / f"round-{n}"
    rd.mkdir(parents=True, exist_ok=True)
    ok, how = try_render(fp["artifact"], rd)
    if ok:
        log({"ts": now(), "event": "shoot", "slug": a.slug, "round": n, "renderer": how})
        write_receipt(d)
        print(f"SHOT — {a.slug} round {n} · {how} · {rd}")
        return 0
    (rd / "CAPTURE-PLAN.md").write_text(
        f"# Capture plan — {a.slug} round {n}\n\nNo headless renderer on this machine ({how}). Capture with the Playwright MCP "
        f"or the Browser pane and save EXACTLY here, then attach:\n\n"
        + "\n".join(f"- {v} {w}x{h}: {rd / (v + '.png')}" for v, (w, h) in VIEWPORTS.items())
        + f"\n\nArtifact: {fp['artifact']}\nThen: python3 execution/design_gauntlet.py attach {a.slug} --round {n} "
        f"--desktop {rd / 'desktop.png'} --tablet {rd / 'tablet.png'} --mobile {rd / 'mobile.png'}\n"
        f"Until attached this round is VISUAL UNVERIFIED and a verdict on it is refused.\n", encoding="utf-8")
    log({"ts": now(), "event": "shoot-unverified", "slug": a.slug, "round": n, "reason": how})
    write_receipt(d)
    print(f"NO RENDERER — {a.slug} round {n}: {how}. Capture plan: {rd / 'CAPTURE-PLAN.md'}")
    print("  " + " · ".join(f"{v} {w}x{h} → {rd / (v + '.png')}" for v, (w, h) in VIEWPORTS.items()))
    return 0


def cmd_attach(a):
    d = find_dir(a.slug)
    if not d:
        print(f"no gauntlet '{a.slug}'")
        return 1
    rd = d / f"round-{a.round}"
    rd.mkdir(parents=True, exist_ok=True)
    missing = []
    for v in VIEWPORTS:
        src = getattr(a, v)
        if not src:
            continue
        sp = Path(src)
        if not sp.exists() or sp.stat().st_size == 0:
            missing.append(f"{v}: {src} not found or empty")
            continue
        dst = rd / f"{v}.png"
        if sp.resolve() != dst.resolve():
            shutil.copy(sp, dst)
    if missing:
        print("  nudge: " + "; ".join(missing))
    state = visual_state(d, a.round)
    log({"ts": now(), "event": "attach", "slug": a.slug, "round": a.round, "state": state})
    write_receipt(d)
    print(f"ATTACHED — {a.slug} round {a.round}: {state}")
    return 0 if state == "VISUAL VERIFIED" else 1


def cmd_verdict(a):
    d = find_dir(a.slug)
    if not d:
        print(f"no gauntlet '{a.slug}'")
        return 1
    if a.round not in rounds(d):
        print(f"REFUSED — round {a.round} has no baseline: python3 execution/design_gauntlet.py shoot {a.slug} --round {a.round}")
        return 1
    state = visual_state(d, a.round)
    if state != "VISUAL VERIFIED" and not a.allow_unverified:
        print(f"REFUSED — round {a.round} is VISUAL UNVERIFIED (screenshots missing). Attach them, or pass --allow-unverified "
              f"to record a source-only verdict that the receipt will label as such.")
        return 1
    v = {"verdict": a.verdict, "gap": a.gap, "evidence": a.evidence, "preserve": a.preserve or "", "visual": state, "ts": now()}
    (d / f"round-{a.round}" / "verdict.json").write_text(json.dumps(v, indent=2), encoding="utf-8")
    log({"ts": now(), "event": "verdict", "slug": a.slug, "round": a.round, "verdict": a.verdict, "visual": state})
    write_receipt(d)
    print(f"VERDICT — {a.slug} round {a.round}: {a.verdict} · gap: {a.gap} · {state}")
    return 0


def cmd_repair(a):
    d = find_dir(a.slug)
    if not d:
        print(f"no gauntlet '{a.slug}'")
        return 1
    if not (d / f"round-{a.round}" / "verdict.json").exists():
        print(f"REFUSED — repair before a verdict on round {a.round} (the biggest visible gap must be named first)")
        return 1
    used = sum(1 for n in rounds(d) if (d / f"round-{n}" / "repair.json").exists())
    r = {"did": a.did, "checks": a.checks or "", "ts": now()}
    (d / f"round-{a.round}" / "repair.json").write_text(json.dumps(r, indent=2), encoding="utf-8")
    used += 1
    log({"ts": now(), "event": "repair", "slug": a.slug, "round": a.round, "n": used})
    write_receipt(d)
    print(f"REPAIR {used}/{REPAIR_CAP} — {a.slug} round {a.round}: {a.did}")
    if used > REPAIR_CAP:
        print(f"  nudge: over the blind-bar cap ({REPAIR_CAP}) — the brief is the problem, not the pixels; close with the surviving risk")
    print(f"  next: python3 execution/design_gauntlet.py shoot {a.slug}   (re-render the same viewports before judging the delta)")
    return 0


def cmd_close(a):
    d = find_dir(a.slug)
    if not d:
        print(f"no gauntlet '{a.slug}'")
        return 1
    rs = rounds(d)
    if not rs:
        print("REFUSED — nothing to close: no round was shot")
        return 1
    unverified = [n for n in rs if visual_state(d, n) != "VISUAL VERIFIED"]
    verdict = a.verdict or ("FAIL" if unverified else "PASS")
    if unverified and verdict == "PASS" and not a.allow_unverified:
        print(f"REFUSED — rounds {unverified} are VISUAL UNVERIFIED; a PASS needs captured screenshots (--allow-unverified labels it)")
        return 1
    closing = {"verdict": verdict, "risks": a.risks, "closed": now()}
    rp = write_receipt(d, closing)
    log({"ts": now(), "event": "close", "slug": a.slug, "verdict": verdict, "rounds": len(rs),
         "repairs": sum(1 for n in rs if (d / f"round-{n}" / "repair.json").exists()), "receipt": str(rp)})
    print(f"GAUNTLET CLOSED — {a.slug}: {verdict} · {len(rs)} round(s) · surviving risks: {a.risks}\n  receipt: {rp}")
    return 0


def cmd_status(a):
    d = find_dir(a.slug)
    if not d:
        print(f"no gauntlet '{a.slug}'")
        return 1
    print((d / "GAUNTLET-RECEIPT.md").read_text(encoding="utf-8") if (d / "GAUNTLET-RECEIPT.md").exists() else write_receipt(d).read_text())
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="design_gauntlet.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("open"); s.add_argument("slug"); s.add_argument("--artifact", required=True); s.add_argument("--bar", required=True)
    s.add_argument("--mode", required=True); s.add_argument("--preserve"); s.add_argument("--never"); s.add_argument("--out"); s.set_defaults(fn=cmd_open)
    s = sub.add_parser("shoot"); s.add_argument("slug"); s.add_argument("--round", type=int); s.set_defaults(fn=cmd_shoot)
    s = sub.add_parser("attach"); s.add_argument("slug"); s.add_argument("--round", type=int, required=True)
    for v in VIEWPORTS:
        s.add_argument(f"--{v}")
    s.set_defaults(fn=cmd_attach)
    s = sub.add_parser("verdict"); s.add_argument("slug"); s.add_argument("--round", type=int, required=True)
    s.add_argument("--verdict", required=True, choices=["A", "B", "TIE", "INCOMPARABLE"]); s.add_argument("--gap", required=True)
    s.add_argument("--evidence", required=True); s.add_argument("--preserve"); s.add_argument("--allow-unverified", dest="allow_unverified", action="store_true")
    s.set_defaults(fn=cmd_verdict)
    s = sub.add_parser("repair"); s.add_argument("slug"); s.add_argument("--round", type=int, required=True); s.add_argument("--did", required=True)
    s.add_argument("--checks"); s.set_defaults(fn=cmd_repair)
    s = sub.add_parser("close"); s.add_argument("slug"); s.add_argument("--risks", required=True); s.add_argument("--verdict", choices=["PASS", "FAIL"])
    s.add_argument("--allow-unverified", dest="allow_unverified", action="store_true"); s.set_defaults(fn=cmd_close)
    s = sub.add_parser("status"); s.add_argument("slug"); s.set_defaults(fn=cmd_status)
    a = p.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
