#!/usr/bin/env python3
"""
Avatar Manifold Runner — the deterministic GROUND backstop for
skills/luke-iha-avatar-machine.

WHY THIS EXISTS
---------------
The Avatar Machine workflows must cold-start (zero pre-provided material) and
ground every plot in REAL market data, never contextual guessing. The standing
rule (feedback_ai-memory-dependent-observability.md): never ship infra that
depends on the model *remembering* to run research — pair it with a
deterministic backstop. This runner IS that backstop. It mechanically assembles
the research dossier the reasoning workflows consume, at fixed canonical paths,
BEFORE the model reasons. If the dossier is missing, the model has nothing to
plot from — so the research must have run.

THE SPLIT (heartbeat preservation)
----------------------------------
Python owns the MECHANICAL work only: firing Gemini Deep Research + Apify VOC,
source-URL tagging, anchor-memory plumbing, the GROUND quality gate. It writes
INPUTS, never INTERPRETATIONS. ALL avatar thinking (Pain Matrix scoring, Core
Wound refraction, Anti-Hero prose, Epiphany calibration) stays with the
reasoning model + loaded frameworks. The runner produces a dossier; it never
writes the Manifold.

Canonical outputs (match the wired workflows + research-spine.md):
  .tmp/copy-engine/deep-research.md          # Gemini foundation (market landscape)
  .tmp/copy-engine/voc-pack.md               # raw, source-tagged VOC soundbites
  .tmp/copy-engine/<slug>/ground-dossier.md  # concat + GROUND STATUS (orchestrated runs)
  .tmp/copy-engine/ground-status.json        # {status, sources, modeled_flags}

MCP tools (Playwright FB Ad Library, Recall) are model-side — the runner cannot
call MCP. It does the Python-callable research (Gemini + Apify + Perplexity) and
notes the MCP enrichment the model should add in Phase 0.

Usage:
  python3 execution/avatar_manifold_runner.py ground \
      --market "coaches drowning in consumed-but-undeployed content" \
      --product "AI Brain Build" --slug course-graveyard-coach --mode max
  python3 execution/avatar_manifold_runner.py ground --slug invisible-expert \
      --voc-file _active/.../deep-icp-profile-invisible-expert.md --no-ground
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXEC = ROOT / "execution"
TMP = ROOT / ".tmp" / "copy-engine"
DEEP_RESEARCH = TMP / "deep-research.md"
VOC_PACK = TMP / "voc-pack.md"
STATUS_JSON = TMP / "ground-status.json"

MIN_VOC_URLS = 15  # mirrors research-spine.md floor-check + research_quality_gate --strict
DEFAULT_MAX_AGE_DAYS = 30  # grounding freshness window before a --refresh is suggested

# Cost transparency (USD). The clients self-gate; these are for the up-front estimate
# the user asked for ("let me know how much it costs"). Tiers let the user trade
# cost for depth — and reuse means iterations cost $0.
COST_EST = {
    "free": {"gemini": 0.0, "apify": 0.0, "label": "FREE (model-side: Recall + WebFetch + search_web + Playwright — real live social listening, $0)"},
    "lean": {"gemini": 0.0, "apify": 0.11, "label": "LEAN (Apify VOC: reddit ~$0.05 + amazon ~$0.045 + youtube ~$0.05 — real verbatim VOC, no paid synthesis)"},
    "deep": {"gemini": 1.50, "apify": 0.11, "label": "DEEP (Gemini Deep Research max ~$1.50 + Apify VOC ~$0.11 — full synthesized foundation)"},
}


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def est_cost(tier: str, mode: str) -> float:
    c = COST_EST.get(tier, COST_EST["deep"])
    g = c["gemini"]
    if tier == "deep" and mode == "standard":
        g = 0.50
    return round(g + c["apify"], 2)


def dossier_age_days(slug: str):
    """Returns age in days of an existing GROUND dossier, or None if absent."""
    import datetime as _dt
    f = TMP / slug / "ground-dossier.md"
    if not f.exists():
        return None
    try:
        st = json.loads(STATUS_JSON.read_text())
        if st.get("slug") == slug and st.get("ts"):
            then = _dt.datetime.strptime(st["ts"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=_dt.timezone.utc)
            return (_dt.datetime.now(_dt.timezone.utc) - then).total_seconds() / 86400.0
    except Exception:
        pass
    # fall back to file mtime
    return (datetime.now(timezone.utc).timestamp() - f.stat().st_mtime) / 86400.0


def log(msg: str) -> None:
    print(f"  {msg}", flush=True)


# ─────────────────────────────────────────────────────────────────────────
# Gemini foundation (PRIMARY) → Perplexity (fallback) → degrade
# ─────────────────────────────────────────────────────────────────────────

def gemini_foundation(market: str, product: str, slug: str, mode: str) -> tuple[str, str]:
    """Returns (markdown, status) where status ∈ PASS|FALLBACK|DEGRADED."""
    query = (
        f"Comprehensive market intelligence for: {market}"
        + (f" (product context: {product})" if product else "")
        + ". Cover: demographics; the core problem and how it shows up (symptoms); "
        "the specific solutions buyers have already tried and why they failed; their "
        "biggest objections; what they believe about the problem and about the ideal "
        "solution; pricing and competitor angles; and the current zeitgeist of this "
        "market. Cite sources with URLs."
    )
    sys.path.insert(0, str(EXEC))
    # Resolve BudgetExhaustedError up front so the except clause can distinguish a
    # budget stop (→ DEGRADE to $0, never escalate pools) from a transient error.
    try:
        from deep_research_client import BudgetExhaustedError
    except Exception:
        class BudgetExhaustedError(Exception):  # sentinel if import path is unavailable
            pass
    # ---- Gemini (primary) ----
    try:
        from deep_research_client import DeepResearchClient, load_env
        load_env()
        client = DeepResearchClient()
        log(f"Gemini Deep Research ({mode}) firing…")
        res = client.research(query, mode=mode, task_context=f"avatar-{slug}")
        if not (res.text or "").strip():
            # Completed but empty = NOT a real success. Never report a false PASS.
            raise RuntimeError("Gemini Deep Research returned empty text (no usable report)")
        cites = "\n".join(f"- {c}" for c in (res.citations or [])) or "- (none returned)"
        md = (
            f"# Market Landscape — {market}\n"
            f"_Source: Gemini Deep Research ({mode}) · {now()} · {len(res.text)} chars_\n\n"
            f"{res.text}\n\n## Citations\n{cites}\n"
        )
        return md, "PASS"
    except BudgetExhaustedError as e:
        # Cheap pool exhausted → fail-CLOSED to $0 (recall-only). Do NOT auto-escalate
        # to the more expensive Perplexity deep-research pool — that would spend MORE
        # when the budget is already tight (the cost-leak the user explicitly fears).
        log(f"Gemini budget exhausted ({e}) → DEGRADE to recall-only ($0); NOT escalating to paid Perplexity.")
        md = (
            f"# Market Landscape — {market}\n"
            f"_GROUND STATUS: DEGRADED — Gemini budget exhausted; Perplexity NOT auto-fired "
            f"(fail-closed on budget). Model: fire `mcp__recall__search` (focused) + free "
            f"WebFetch/search_web, proceed with `[MODELED]` flags where unfilled._\n"
        )
        return md, "DEGRADED"
    except Exception as e:  # transient/network/API — a different-pool fallback is reasonable
        log(f"Gemini unavailable ({type(e).__name__}: {e}) → Perplexity fallback")
    # ---- Perplexity (fallback) ----
    try:
        from perplexity_client import PerplexityClient, load_env as pload
        pload()
        pclient = PerplexityClient()
        res = pclient.search(query, model="sonar-deep-research")
        cites = "\n".join(f"- {c}" for c in (getattr(res, "citations", None) or [])) or "- (none)"
        md = (
            f"# Market Landscape — {market}\n"
            f"_Source: Perplexity sonar-deep-research (Gemini fallback) · {now()}_\n\n"
            f"{res.text}\n\n## Citations\n{cites}\n"
        )
        return md, "FALLBACK"
    except Exception as e:
        log(f"Perplexity also unavailable ({type(e).__name__}) → DEGRADED (recall-only, model-side)")
    md = (
        f"# Market Landscape — {market}\n"
        f"_GROUND STATUS: DEGRADED — Gemini + Perplexity unavailable. "
        f"Model: fire `mcp__recall__search` (focused) and proceed with `[MODELED]` flags._\n"
    )
    return md, "DEGRADED"


# ─────────────────────────────────────────────────────────────────────────
# Apify VOC (raw voices) — subprocess the budget-gated client
# ─────────────────────────────────────────────────────────────────────────

_TEXT_KEYS = ("text", "body", "comment", "reviewText", "content", "title", "description", "snippet")
_URL_KEYS = ("url", "link", "permalink", "postUrl", "commentUrl", "reviewUrl")


def _harvest(obj, out: list, url_hint: str = "") -> None:
    """Recursively pull (text, url) pairs from arbitrary Apify item JSON."""
    if isinstance(obj, dict):
        url = ""
        for k in _URL_KEYS:
            if isinstance(obj.get(k), str) and obj[k].startswith("http"):
                url = obj[k]
                break
        url = url or url_hint
        for k in _TEXT_KEYS:
            v = obj.get(k)
            if isinstance(v, str) and len(v.strip()) >= 25:
                out.append((v.strip().replace("\n", " "), url))
        for v in obj.values():
            if isinstance(v, (dict, list)):
                _harvest(v, out, url)
    elif isinstance(obj, list):
        for v in obj:
            _harvest(v, out, url_hint)


def apify_pull(actor: str, query: str, limit: int, comments: bool = False,
               transcript: bool = False) -> tuple[list, bool]:
    """Returns (soundbites[(text,url)], degraded?)."""
    cmd = [sys.executable, str(EXEC / "apify_client.py"), actor, query, "--limit", str(limit)]
    if comments:
        cmd.append("--comments")
    if transcript:
        cmd.append("--transcript")
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        data = json.loads(proc.stdout or "{}")
    except Exception as e:
        log(f"Apify {actor} error ({type(e).__name__}) → degraded")
        return [], True
    if data.get("fallback"):
        log(f"Apify {actor}: budget/fallback → reroute to Perplexity verbatim-quote (model-side)")
        return [], True
    items = data.get("items", []) or []
    out: list = []
    _harvest(items, out)
    # de-dup, keep longest variants
    seen = set()
    uniq = []
    for text, url in out:
        key = text[:80].lower()
        if key in seen:
            continue
        seen.add(key)
        uniq.append((text, url))
    log(f"Apify {actor}: {len(uniq)} soundbites from {len(items)} items")
    return uniq[:limit], False


def free_reddit_voc(query: str, limit: int = 40) -> list:
    """FREE real VOC via Reddit's public .json search — no Apify, $0.

    Reddit actively blocks scraper actors, but its public JSON endpoints work
    with a normal User-Agent. This is genuine verbatim social listening at zero
    cost — the user's 'free tools that actually do the research' intent.
    Returns [(text, permalink_url)].
    """
    out: list = []
    # Use requests (bundles certifi → no macOS SSL cert-store failures that
    # urllib hits). A browser UA avoids reddit's bot 403s.
    try:
        import requests
        resp = requests.get(
            "https://www.reddit.com/search.json",
            params={"q": query, "limit": limit, "sort": "relevance", "t": "year"},
            headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        log(f"free reddit VOC error ({type(e).__name__}) → model-side WebFetch fallback")
        return out
    for child in data.get("data", {}).get("children", []):
        d = child.get("data", {})
        perma = "https://www.reddit.com" + d.get("permalink", "")
        for field in ("title", "selftext"):
            v = (d.get(field) or "").strip().replace("\n", " ")
            if len(v) >= 30:
                out.append((v[:400], perma))
    log(f"free reddit VOC: {len(out)} soundbites from r/ search ($0)")
    return out


def free_hn_voc(query: str, limit: int = 30) -> list:
    """FREE real VOC via the Hacker News (Algolia) public API — $0, unblocked.

    Reddit 403s server-side; HN's API is open and rich for professional/AI/
    founder/consultant audiences (exactly the Avatar Machine's markets).
    Returns [(comment_text, item_url)].
    """
    out: list = []
    try:
        import requests
        import html, re as _re
        resp = requests.get(
            "https://hn.algolia.com/api/v1/search",
            params={"query": query, "tags": "comment", "hitsPerPage": limit},
            timeout=30,
        )
        resp.raise_for_status()
        for h in resp.json().get("hits", []):
            raw = h.get("comment_text") or ""
            txt = html.unescape(_re.sub(r"<[^>]+>", " ", raw)).strip().replace("\n", " ")
            if len(txt) >= 40:
                url = f"https://news.ycombinator.com/item?id={h.get('objectID')}"
                out.append((txt[:400], url))
    except Exception as e:
        log(f"free HN VOC error ({type(e).__name__})")
    if out:
        log(f"free HN VOC: {len(out)} soundbites ($0)")
    return out


def build_voc_pack(market: str, depth: str, tier: str = "deep") -> tuple[str, int, bool]:
    """Returns (markdown, url_count, any_degraded).

    Primary VOC = FREE Reddit public-JSON pull ($0, reliable). Apify is an
    optional accelerator for amazon/youtube on heavy depth (and only if its
    cheap actors return data). Free-first honors the cost-conscious intent.
    """
    rows: list = []
    degraded = False

    # --- FREE primary VOC: unblocked public APIs ($0, all tiers) ---
    # HN Algolia (reliable, rich for professional/AI/founder/consultant markets)
    # + best-effort Reddit JSON (works where not 403-blocked).
    short_q = " ".join(market.split()[:6])  # keep the query tight for relevance
    free_sb = []
    for q in (short_q, short_q + " advice"):
        free_sb += free_hn_voc(q, 25)
    for q in (short_q + " frustrated", short_q + " problem"):
        free_sb += free_reddit_voc(q, 25)  # best-effort; harmless if blocked
    seen = set()
    for text, url in free_sb:
        k = text[:60].lower()
        if k in seen:
            continue
        seen.add(k)
        rows.append(f'| "{text[:280]}" | {url} | [VOC] | _(classify)_ |')

    # --- Optional Apify accelerator (heavy depth, paid tiers only) ---
    plan = []
    if depth == "heavy" and tier in ("lean", "deep"):
        plan = [("amazon", short_q + " book course", 20, False, False),
                ("youtube", short_q, 8, False, True)]
    for actor, q, lim, com, tr in plan:
        sb, deg = apify_pull(actor, q, lim, comments=com, transcript=tr)
        degraded = degraded or deg
        for text, url in sb:
            tag = "[VOC]" if url else "[MODELED — replace with VOC]"
            src = url or "(no source — MODELED)"
            rows.append(f'| "{text[:280]}" | {src} | {tag} | _(classify: emotion/objection/failed-solution/desired-outcome/belief)_ |')
    url_count = sum(1 for r in rows if "http" in r)
    body = "\n".join(rows) if rows else "| _(no VOC pulled — all sources degraded; mine via /buyer-sourcer)_ | — | [MODELED] | |"
    md = (
        f"# VOC Soundbite Bank — {market}\n"
        f"_Raw, source-tagged. The MODEL classifies by emotion/objection/etc. during "
        f"Build-a-Buyer + Specific-Language. {url_count} source-linked soundbites._\n\n"
        f"> MCP enrichment to add model-side: Playwright FB Ad Library (live hooks), "
        f"`mcp__recall__search` (expert grounding), WebFetch raw review/forum pages.\n\n"
        f"| Verbatim soundbite | Source | Tag | Classify |\n|---|---|---|---|\n{body}\n"
    )
    return md, url_count, degraded


# ─────────────────────────────────────────────────────────────────────────
# anchor memory + quality gate plumbing
# ─────────────────────────────────────────────────────────────────────────

def anchor_cmd(*args) -> None:
    try:
        subprocess.run([sys.executable, str(EXEC / "anchor_memory.py"), *args],
                       capture_output=True, text=True, timeout=30)
    except Exception as e:
        log(f"anchor_memory {args[0]} skipped ({type(e).__name__})")


def quality_gate(path: Path) -> bool:
    try:
        proc = subprocess.run(
            [sys.executable, str(EXEC / "research_quality_gate.py"), "validate", str(path), "--strict"],
            capture_output=True, text=True, timeout=60)
        return proc.returncode == 0
    except Exception:
        return False


# ─────────────────────────────────────────────────────────────────────────
# GROUND command
# ─────────────────────────────────────────────────────────────────────────

def cmd_ground(args) -> int:
    TMP.mkdir(parents=True, exist_ok=True)
    slug_dir = TMP / args.slug
    slug_dir.mkdir(parents=True, exist_ok=True)

    tier = getattr(args, "tier", "deep")
    estimate = est_cost(tier, args.mode)

    # ── REUSE GATE (the budget-saver): iterations cost $0 ──
    # If a GROUND dossier already exists and is fresh, REUSE it — do not re-fire
    # research. Refinement passes / variants / writers-room all land here at $0.
    # Re-fire only on --refresh or when stale (> --max-age-days).
    age = dossier_age_days(args.slug)
    if age is not None and not getattr(args, "refresh", False) and not args.no_ground:
        if age <= args.max_age_days:
            log(f"♻️  WARM: reusing cached GROUND for '{args.slug}' ({age:.1f}d old < {args.max_age_days}d) — $0, no research fired.")
            log(f"   Iterations / refinement / writers-room reuse the dossier. Re-fire with --refresh if the market changed.")
            log(f"   Dossier: {slug_dir / 'ground-dossier.md'}")
            return 0
        # STALE: nudge, do NOT auto-spend. The user runs many passes — budget safety
        # beats freshness automation. Re-grounding is always an explicit --refresh choice.
        log(f"⏳ STALE: cached GROUND for '{args.slug}' is {age:.1f}d old (> {args.max_age_days}d). REUSING anyway ($0).")
        log(f"   Markets drift — re-ground with `--refresh` (est ${estimate:.2f}) ONLY if it actually moved. Not auto-spending.")
        log(f"   Dossier: {slug_dir / 'ground-dossier.md'}")
        return 0

    # ── COST TRANSPARENCY ──
    log(f"Tier: {COST_EST[tier]['label']}")
    log(f"Estimated cost: ${estimate:.2f}  (reuse on subsequent iterations = $0)")
    if getattr(args, "dry_run", False):
        log("--dry-run: estimate only, no research fired.")
        return 0
    try:
        subprocess.run([sys.executable, str(EXEC / "cost_gate.py"), "status"],
                       capture_output=True, text=True, timeout=15)
    except Exception:
        pass

    anchor_cmd("init", args.slug, "--audience", (args.market or args.product or args.slug)[:200])

    # ---- BYPASS path (--no-ground): user supplies VOC, or pure-stub ----
    if args.no_ground:
        if args.voc_file and Path(args.voc_file).exists():
            user_voc = Path(args.voc_file).read_text()
            VOC_PACK.write_text(
                f"# VOC — {args.market or args.slug} (VERIFIED-FROM-USER)\n"
                f"_Imported from {args.voc_file} · treat as real VOC ('import, don't regenerate'). "
                f"Run ONE Gemini gap-fill query model-side for the missing dimensional layers._\n\n"
                + user_voc
            )
            # one gap-fill foundation query so dimensional layers aren't modeled
            md, gstatus = gemini_foundation(args.market or args.slug, args.product, args.slug, "standard")
            DEEP_RESEARCH.write_text(md)
            status = "BYPASSED-IMPORT"
        else:
            DEEP_RESEARCH.write_text(
                f"# Market Landscape — {args.market or args.slug}\n"
                f"_GROUND STATUS: BYPASSED (--no-ground, no --voc-file). "
                f"All downstream specific-language is [MODELED] until VOC is supplied._\n")
            VOC_PACK.write_text("# VOC — BYPASSED\n_All soundbites [MODELED]. Supply --voc-file or run /buyer-sourcer._\n")
            status = "BYPASSED"
        _write_status(status, 0, args.slug, tier=tier, cost=estimate)
        log(f"GROUND {status} for '{args.slug}'. Dossier: {VOC_PACK}")
        return 0

    # ---- COLD-START path (tier-gated) ----
    log(f"Cold-start GROUND for '{args.slug}' (market: {args.market})")

    # FREE tier — runner fires no paid API; the dossier is a directive the model
    # executes with free live tools (Recall + WebFetch + search_web + Playwright).
    if tier == "free":
        DEEP_RESEARCH.write_text(
            f"# Market Landscape — {args.market}\n"
            f"_FREE-TIER GROUND ($0). Runner fired no paid API. The MODEL executes live, "
            f"free social listening now:_\n\n"
            f"1. `mcp__recall__search` (focused, 2 queries) — expert/precedent grounding.\n"
            f"2. `search_web` + `WebFetch` — read real Reddit threads, review pages, forum posts, "
            f"articles for **<{args.market}>**; pull verbatim soundbites with their URLs.\n"
            f"3. `mcp__playwright__browser_navigate` → `facebook.com/ads/library` → `browser_snapshot` — "
            f"live winning ad angles/hooks (Tier-1 read-only, free).\n"
            f"4. Append every verbatim soundbite to `voc-pack.md` with its source URL. "
            f"No URL ⇒ tag `[MODELED]`.\n")
        VOC_PACK.write_text(
            f"# VOC Soundbite Bank — {args.market} (FREE-TIER — model fills via WebFetch/Playwright/Recall)\n"
            f"_$0. The model must populate ≥15 source-linked verbatim soundbites here using free live tools._\n\n"
            f"| Verbatim soundbite | Source | Tag |\n|---|---|---|\n"
            f"| _(model: fill from WebFetch/Playwright/Recall — real URLs required)_ | — | [MODELED] |\n")
        gstatus, url_count, voc_degraded = "FREE", 0, False
        log("FREE tier: wrote model-side social-listening directive ($0). Model executes the free pulls.")
    else:
        # DEEP fires Gemini synthesis; LEAN skips it (Apify-only, cheap real VOC).
        if tier == "deep":
            deep_md, gstatus = gemini_foundation(args.market, args.product, args.slug, args.mode)
        else:  # lean
            deep_md, gstatus = (
                f"# Market Landscape — {args.market}\n"
                f"_LEAN tier ($0 synthesis): no Gemini Deep Research. Foundation = Apify VOC below "
                f"+ model-side Recall/WebFetch. Upgrade to --tier deep for synthesized landscape._\n", "LEAN")
            log("LEAN tier: skipping Gemini Deep Research (saves ~$0.50–1.50). Apify VOC only.")
        DEEP_RESEARCH.write_text(deep_md)
        log(f"Wrote {DEEP_RESEARCH} ({gstatus})")

        voc_md, url_count, voc_degraded = build_voc_pack(args.market, args.depth, tier)
        VOC_PACK.write_text(voc_md)
        log(f"Wrote {VOC_PACK} ({url_count} source-linked soundbites)")

    # concat dossier for orchestrated runs (read from files — works for all tiers)
    dossier = slug_dir / "ground-dossier.md"
    dossier.write_text(
        f"# AVATAR RESEARCH DOSSIER — {args.market}\n_Assembled {now()} · runner GROUND (tier={tier})_\n\n"
        + DEEP_RESEARCH.read_text() + "\n\n---\n\n" + VOC_PACK.read_text()
    )

    # status
    if tier == "free":
        status = "FREE-DIRECTIVE"  # model fills via free live tools; not yet graded
    elif gstatus == "DEGRADED" and voc_degraded:
        status = "DEGRADED"
    elif gstatus in ("FALLBACK", "DEGRADED", "LEAN") or voc_degraded or url_count < MIN_VOC_URLS:
        status = "PARTIAL"
    else:
        status = "PASS"
    rqg = quality_gate(dossier)
    _write_status(status, url_count, args.slug, rqg=rqg, tier=tier, cost=estimate)
    # append status to dossier header
    dossier.write_text(f"<!-- GROUND STATUS: {status} | voc_urls={url_count} | rqg_strict={'pass' if rqg else 'fail'} -->\n"
                       + dossier.read_text())

    anchor_cmd("anchor", args.slug, "--type", "ground_dossier", "--path",
               str(dossier.relative_to(ROOT)), "--desc", f"GROUND dossier ({status})",
               "--ref-for", "build-a-buyer,specific-language,pain-matrix,core-wound")
    anchor_cmd("log", args.slug, "--phase", "Phase 0: GROUND",
               "--action", f"runner cold-start research ({status})")

    log(f"GROUND {status}. Dossier: {dossier}")
    if status == "DEGRADED":
        log("⚠️  All research degraded — manifold will build on [MODELED] language. Flag before shipping.")
    return 0  # never hard-fail the pipeline; status carries the signal


def _write_status(status: str, urls: int, slug: str, rqg: bool = False,
                  tier: str = "deep", cost: float = 0.0) -> None:
    STATUS_JSON.write_text(json.dumps({
        "slug": slug, "status": status, "voc_source_urls": urls,
        "rqg_strict_pass": rqg, "ts": now(), "tier": tier,
        "est_cost_usd": cost, "min_voc_urls": MIN_VOC_URLS,
    }, indent=2))


def cmd_estimate(args) -> int:
    print("Avatar Machine — GROUND research cost (per cold start; iterations reuse = $0):")
    for t in ("free", "lean", "deep"):
        print(f"  --tier {t:<4} ${est_cost(t, args.mode):.2f}   {COST_EST[t]['label']}")
    print("\nReuse: a fresh dossier (< --max-age-days, default 30) is reused at $0. "
          "Re-fire only with --refresh. Copy iterations / writers-room / variants never re-fire.")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(prog="avatar_manifold_runner.py")
    sub = p.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("ground", help="Cold-start GROUND research dossier (reused on iterations)")
    g.add_argument("--market", default="")
    g.add_argument("--product", default="")
    g.add_argument("--slug", required=True)
    g.add_argument("--tier", default="deep", choices=["free", "lean", "deep"],
                   help="free=$0 (model-side live tools) · lean=~$0.10 (Apify VOC) · deep=~$1.10-1.60 (Gemini+Apify)")
    g.add_argument("--mode", default="standard", choices=["standard", "max"])
    g.add_argument("--voc-file", default="", dest="voc_file")
    g.add_argument("--no-ground", action="store_true", dest="no_ground")
    g.add_argument("--refresh", action="store_true", help="Force re-fire even if a fresh dossier exists")
    g.add_argument("--dry-run", action="store_true", dest="dry_run", help="Show cost estimate, fire nothing")
    g.add_argument("--max-age-days", type=int, default=DEFAULT_MAX_AGE_DAYS, dest="max_age_days")
    g.add_argument("--depth", default="heavy", choices=["heavy", "light"])
    e = sub.add_parser("estimate", help="Print per-tier cost estimate")
    e.add_argument("--mode", default="standard", choices=["standard", "max"])
    args = p.parse_args()
    if args.cmd == "ground":
        if not args.no_ground and not args.market:
            print("ERROR: --market required for cold-start (or pass --no-ground).", file=sys.stderr)
            return 2
        return cmd_ground(args)
    if args.cmd == "estimate":
        return cmd_estimate(args)
    return 2


if __name__ == "__main__":
    sys.exit(main())
