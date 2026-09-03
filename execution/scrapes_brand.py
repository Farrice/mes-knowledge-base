#!/usr/bin/env python3
"""scrapes_brand.py — BRAND LOCK for the Scrapes Skill Systems pipelines.

WHY (Farrice, 2026-09-02): "I do a lot of client-facing work … nothing just
auto-routes or orchestrates poorly to the wrong place, working on the wrong
client and the wrong thing, pulling from the wrong context."

The vendored Scrapes skills assume ONE brand at `<project_root>/brand_context/`.
This repo serves Farrice plus a growing roster of clients (Jen, Andrea, Gigi…).
Every brand declares itself once in `<brand-root>/brand_context/BRAND.yaml`;
every front-door workflow (/social-carousel, /social-post, …) resolves the
brand through this script BEFORE touching a pipeline and echoes the returned
`BRAND LOCK` line into the run's pipeline-log.

Resolution is explicit or it stops:
  1. `--brand <name|alias>`            → that brand.
  2. `--from-prompt "<text>"`          → exactly ONE brand's alias appears → that
                                         brand. Zero or two+ → AMBIGUOUS (exit 3).
  3. `--cwd <path>` (fallback only when the prompt names nobody) → the brand
     whose `client_root` contains the path.
  Never defaults to the owner brand when a client alias is present anywhere.

Commands:
  list                                  every registered brand, one line each
  resolve (--brand B | --from-prompt T) [--cwd P] [--json]
  check <brand> [--pool linkedin-carousel] [--json]
                                        readiness for a Scrapes run: brand_context,
                                        voice-profile.md, tokens.json, template
                                        pool with ≥1 `status: ready`, and the
                                        CROSS-BRAND check (every path resolves
                                        under this brand's roots, none under
                                        another brand's). Exit 2 when not ready.
Exit codes: 0 ok · 1 error · 2 not ready · 3 ambiguous brand.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("Need PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
BRAND_FILE = "BRAND.yaml"
SEARCH_ROOTS = (ROOT / "_active",)
MAX_DEPTH = 4


# ── registry ────────────────────────────────────────────────────────────
def _find_brand_files() -> list[Path]:
    found = []
    for base in SEARCH_ROOTS:
        if not base.is_dir():
            continue
        for depth in range(1, MAX_DEPTH + 1):
            pattern = "/".join(["*"] * depth) + f"/brand_context/{BRAND_FILE}"
            found.extend(base.glob(pattern))
    return sorted(set(found))


def load_brands() -> dict[str, dict]:
    brands: dict[str, dict] = {}
    for f in _find_brand_files():
        try:
            data = yaml.safe_load(f.read_text()) or {}
        except yaml.YAMLError as e:
            print(f"WARN: {f}: {e}", file=sys.stderr)
            continue
        name = str(data.get("brand") or "").strip().lower()
        if not name:
            continue
        data["_file"] = str(f.relative_to(ROOT))
        data.setdefault("brand_root", str(f.parent.parent.relative_to(ROOT)))
        data.setdefault("brand_context", str(f.parent.relative_to(ROOT)))
        data.setdefault("aliases", [])
        data["aliases"] = [str(a).lower() for a in ([name] + list(data["aliases"]))]
        brands[name] = data
    return brands


def _resolve_rel(rel: str) -> Path:
    p = Path(rel)
    return (p if p.is_absolute() else ROOT / p).resolve(strict=False)


# ── resolution ──────────────────────────────────────────────────────────
def _alias_hits(text: str, brands: dict[str, dict]) -> dict[str, str]:
    low = text.lower()
    hits: dict[str, str] = {}
    for name, b in brands.items():
        for alias in sorted(b["aliases"], key=len, reverse=True):
            if re.search(rf"(?<![a-z0-9]){re.escape(alias)}(?![a-z0-9])", low):
                hits[name] = alias
                break
    return hits


def resolve(brands: dict[str, dict], brand: str | None = None, prompt: str | None = None,
            cwd: str | None = None) -> tuple[dict | None, str]:
    """Returns (brand dict, status) — status ∈ {ok, ambiguous, unknown}."""
    if brand:
        key = brand.strip().lower()
        for name, b in brands.items():
            if key == name or key in b["aliases"]:
                return b, "ok"
        return None, "unknown"
    hits = _alias_hits(prompt or "", brands)
    if len(hits) == 1:
        return brands[next(iter(hits))], "ok"
    if len(hits) > 1:
        return None, "ambiguous"
    if cwd:
        here = Path(cwd).resolve(strict=False)
        for name, b in brands.items():
            root = _resolve_rel(b["brand_root"])
            client_root = _resolve_rel(b["client_root"]) if b.get("client_root") else root
            for r in {root, client_root}:
                try:
                    here.relative_to(r)
                    return b, "ok"
                except ValueError:
                    pass
    return None, "ambiguous"


def lock_line(b: dict) -> str:
    return (f"BRAND LOCK: {b['brand']} ({b.get('display', b['brand'])}, {b.get('kind', '?')}) — "
            f"brand_context={b['brand_context']} output_base={b.get('output_base', '?')} "
            f"pens={b.get('pens', {}).get('hook', '?')}+{b.get('pens', {}).get('integrator', '?')} "
            f"veto={b.get('pens', {}).get('veto', '?')} voice_dial={b.get('voice', {}).get('dial', 'OFF')}")


# ── readiness ───────────────────────────────────────────────────────────
def _pool_ready_count(pool_dir: Path) -> tuple[int, int]:
    manifest = pool_dir / "manifest.json"
    if not manifest.exists():
        return 0, 0
    try:
        data = json.loads(manifest.read_text())
    except json.JSONDecodeError:
        return 0, 0
    entries = data.get("templates") if isinstance(data, dict) else data
    if isinstance(entries, dict):
        entries = list(entries.values())
    entries = entries or []
    # Their pipeline walks both states: `ready` (builder's gate passed) and
    # `approved` (Farrice clicked Approve in the Template Studio, or said so).
    ready = sum(1 for e in entries if isinstance(e, dict)
                and str(e.get("status", "")).lower() in ("ready", "approved"))
    return ready, len(entries)


def check(brands: dict[str, dict], b: dict, pool: str | None) -> dict:
    bc = _resolve_rel(b["brand_context"])
    report = {"brand": b["brand"], "lock": lock_line(b), "checks": [], "ready": True}

    def add(name, ok, detail, hard=True):
        report["checks"].append({"check": name, "ok": bool(ok), "detail": detail})
        if hard and not ok:
            report["ready"] = False

    add("brand_context dir", bc.is_dir(), str(bc.relative_to(ROOT)) if bc.is_relative_to(ROOT) else str(bc))
    add("voice-profile.md", (bc / "voice-profile.md").exists(), "voice canon for tool-humanizer deep / caption seam")
    tokens = bc / "visual-identity" / "tokens.json"
    add("tokens.json", tokens.exists(), "Phase 1 hard gate of 00-social-content (mkt-visual-identity Import)")
    pools = b.get("template_pools") or {}
    if pool:
        pool_dir = _resolve_rel(pools.get(pool) or str(Path(b["brand_context"]) / "templates" / pool))
        ready, total = _pool_ready_count(pool_dir)
        fallback = b.get("renderer_fallback")
        add(f"template pool {pool}", ready >= 1 or bool(fallback),
            f"{ready}/{total} ready at {pool_dir.relative_to(ROOT) if pool_dir.is_relative_to(ROOT) else pool_dir}"
            + (f" — fallback renderer: {fallback}" if ready < 1 and fallback else
               ("" if ready >= 1 else " — no pool and no fallback: Phase 1 would fail loudly")))
        report["render_path"] = "scrapes-template-pool" if ready >= 1 else ("brand-renderer" if fallback else "blocked")
    # CROSS-BRAND: every declared path must sit under this brand's roots and under no other brand's
    my_roots = {_resolve_rel(b["brand_root"]), bc}
    if b.get("client_root"):
        my_roots.add(_resolve_rel(b["client_root"]))
    others = {n: _resolve_rel(o["brand_root"]) for n, o in brands.items() if n != b["brand"]}
    others.update({f"{n}:brand_context": _resolve_rel(o["brand_context"]) for n, o in brands.items() if n != b["brand"]})
    leaks = []
    declared = {"brand_context": b["brand_context"], "output_base": b.get("output_base"),
                "research_cache": b.get("research_cache"), **{f"pool:{k}": v for k, v in pools.items()}}
    for label, rel in declared.items():
        if not rel:
            continue
        p = _resolve_rel(str(rel))
        for oname, oroot in others.items():
            try:
                p.relative_to(oroot)
                if not any(p == r or p.is_relative_to(r) for r in my_roots):
                    leaks.append(f"{label} → {rel} lies under {oname}")
            except ValueError:
                pass
    add("cross-brand isolation", not leaks, "; ".join(leaks) or "no declared path resolves under another brand")
    return report


# ── CLI ─────────────────────────────────────────────────────────────────
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    r = sub.add_parser("resolve")
    r.add_argument("--brand")
    r.add_argument("--from-prompt", dest="prompt")
    r.add_argument("--cwd")
    r.add_argument("--json", action="store_true")
    c = sub.add_parser("check")
    c.add_argument("brand")
    c.add_argument("--pool", default=None)
    c.add_argument("--json", action="store_true")
    args = ap.parse_args()

    brands = load_brands()
    if args.cmd == "list":
        if not brands:
            print("no BRAND.yaml found under _active/**/brand_context/")
            return 1
        for name, b in brands.items():
            print(f"{name:10s} {b.get('kind', '?'):7s} {b['brand_context']:55s} aliases={', '.join(b['aliases'][1:6])}")
        return 0

    if args.cmd == "resolve":
        if not args.brand and not args.prompt:
            print("resolve needs --brand or --from-prompt", file=sys.stderr)
            return 1
        b, status = resolve(brands, args.brand, args.prompt, args.cwd)
        if status != "ok":
            names = ", ".join(sorted(brands))
            hits = _alias_hits(args.prompt or "", brands) if args.prompt else {}
            msg = (f"BRAND AMBIGUOUS — {len(hits)} brand(s) named ({', '.join(hits) or 'none'}). "
                   f"Name the brand: {names}. The door refuses to guess."
                   if status == "ambiguous" else f"BRAND UNKNOWN: {args.brand!r}. Known: {names}")
            if args.json:
                print(json.dumps({"status": status, "hits": hits, "known": sorted(brands)}))
            else:
                print(msg)
            return 3
        if args.json:
            out = {k: v for k, v in b.items() if not k.startswith("_")}
            out["lock"] = lock_line(b)
            print(json.dumps(out, indent=2))
        else:
            print(lock_line(b))
        return 0

    if args.cmd == "check":
        b, status = resolve(brands, args.brand)
        if status != "ok":
            print(f"BRAND UNKNOWN: {args.brand!r}. Known: {', '.join(sorted(brands))}", file=sys.stderr)
            return 1
        rep = check(brands, b, args.pool)
        if args.json:
            print(json.dumps(rep, indent=2))
        else:
            print(rep["lock"])
            for ch in rep["checks"]:
                print(f"  {'✓' if ch['ok'] else '✗'} {ch['check']}: {ch['detail']}")
            if rep.get("render_path"):
                print(f"  render path: {rep['render_path']}")
            print("READY" if rep["ready"] else "NOT READY")
        return 0 if rep["ready"] else 2
    return 1


if __name__ == "__main__":
    sys.exit(main())
