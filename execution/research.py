#!/usr/bin/env python3
"""
Unified Research Engine — the single entry point every consumer calls.

Implements the locked design:
  • GEMINI-FIRST for depth (standard/deep/max) — the accelerator, free under Ultra.
  • PERPLEXITY second (deep/max only) — paid fallback accelerator.
  • CLAUDE BEDROCK FLOOR catches every failure — WebSearch+WebFetch+Tavily+Recall,
    $0, cannot break (execution/native_floor.py).
  • HONEST RECEIPT on every result — what fired, what failed, what depth was
    achieved, what it cost. So you can build on grounded truth and KNOW it.

The engine never fabricates to fill a gap, never logs cost for a call that
didn't return validated content, and never persists an unsourced finding. It can
degrade — it cannot lie.

This is a thin façade: it orchestrates the (now bug-fixed) clients and the floor
behind one typed contract. Existing consumers migrate to it one at a time; the
old client CLIs keep working.

CLI:
    python3 execution/research.py "<query>" [--depth standard|quick|deep|max] [--json]
    python3 execution/research.py run "<query>" [--depth ...] [--json]
    python3 execution/research.py ground --slug <s> --market "<m>" [--tier deep] [--refresh]
    python3 execution/research.py ingest --findings <jsonl> --query "<q>" [--depth ...]
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
EXEC = ROOT / "execution"
sys.path.insert(0, str(EXEC))

try:
    from research_contract import (
        ResearchResult, ResearchStatus, EngineKind, Finding, Source,
        EngineAttempt, AttemptOutcome, validate_engine_text,
    )
    from native_floor import run_floor, ingest_findings, DEPTH_MIN_SOURCES, DEPTH_MIN_DOMAINS
    from deep_research_engine import ResearchEngine
except ImportError:  # imported as execution.research
    from execution.research_contract import (
        ResearchResult, ResearchStatus, EngineKind, Finding, Source,
        EngineAttempt, AttemptOutcome, validate_engine_text,
    )
    from execution.native_floor import run_floor, ingest_findings, DEPTH_MIN_SOURCES, DEPTH_MIN_DOMAINS
    from execution.deep_research_engine import ResearchEngine

GROUND_TMP = ROOT / ".tmp" / "copy-engine"
# Every research body is written here by the CLI before anything is printed.
# 2026-09-02: a paid Gemini run printed only the receipt; the report was lost
# until re-fetched by id. The receipt is the summary - the body is the product.
REPORT_DIR = ROOT / ".tmp" / "research"
GE = EngineKind  # shorthand
AO = AttemptOutcome
RS = ResearchStatus


# ---------------------------------------------------------------------------
# Lazy client loaders (safe if keys/clients are absent)
# ---------------------------------------------------------------------------

def _load_gemini():
    try:
        from deep_research_client import DeepResearchClient, BudgetExhaustedError, load_env
        load_env()
        return DeepResearchClient, BudgetExhaustedError
    except Exception:
        return None, None


def _load_perplexity():
    try:
        from perplexity_client import PerplexityClient, BudgetExhaustedError, load_env
        load_env()
        return PerplexityClient, BudgetExhaustedError
    except Exception:
        return None, None


# ---------------------------------------------------------------------------
# Map raw client output → typed contract (reuses engine's provenance quarantine)
# ---------------------------------------------------------------------------

def _findings_from_text(text: str, citations: List[str], perplexity: bool) -> Tuple[List[Finding], int]:
    """Parse synthesized report text into sourced Findings using the engine's
    provenance-quarantine parser (URL-less claims are dropped, never persisted)."""
    eng = ResearchEngine()
    raw = (eng._parse_perplexity_response(text, citations or [])
           if perplexity else eng._parse_deep_research_response(text, citations or []))
    findings: List[Finding] = []
    for f in raw:
        try:
            findings.append(Finding(
                claim=f.claim, source_url=f.source_url, excerpt=f.excerpt or "",
                confidence=f.confidence, finding_type=f.finding_type,
            ))
        except Exception:
            pass  # contract invariant backstop — engine already drops URL-less
    return findings, len(eng._quarantine)


def _map_engine_result(text: str, citations: List[str], cost: float, query: str,
                       depth: str, engine: EngineKind) -> ResearchResult:
    findings, quarantined = _findings_from_text(text, citations, perplexity=(engine == GE.PERPLEXITY))
    sources, seen = [], set()
    for c in (citations or []):
        if c and c not in seen:
            seen.add(c)
            sources.append(Source(url=c))
    res = ResearchResult(
        query=query, status=RS.REAL, engine_used=engine,
        findings=findings, sources=sources, synthesis=text,
        cost_usd=cost or 0.0, depth=depth, depth_achieved=depth,
        quarantined_count=quarantined,
    )
    res.recompute_aggregates()
    return res


# ---------------------------------------------------------------------------
# Accelerator attempts (each catches ALL exceptions → honest receipt row)
# ---------------------------------------------------------------------------

def _try_gemini(query: str, depth: str, task_context: str
                ) -> Tuple[Optional[ResearchResult], EngineAttempt]:
    DRC, BEE = _load_gemini()
    if DRC is None:
        return None, EngineAttempt(GE.GEMINI_DEEP, AO.SKIPPED, detail="client unavailable (no GOOGLE_AI_STUDIO_KEY)")
    try:
        client = DRC()
        remaining = client.budget_remaining()
    except Exception as e:
        return None, EngineAttempt(GE.GEMINI_DEEP, AO.SKIPPED, detail=f"init failed ({type(e).__name__})")
    if remaining < 0.50:
        return None, EngineAttempt(GE.GEMINI_DEEP, AO.SKIPPED, detail=f"budget ${remaining:.2f} < $0.50 → fallback")
    mode = "max" if depth == "max" else "standard"
    t0 = time.monotonic()
    try:
        dr = client.research(query, mode=mode, task_context=task_context)
    except BEE as e:  # type: ignore
        return None, EngineAttempt(GE.GEMINI_DEEP, AO.SKIPPED, detail=f"budget: {str(e)[:60]}")
    except Exception as e:
        # Keep the real reason in the receipt — an opaque "RuntimeError" hid a
        # depleted-prepay-credits 429 for days (found 2026-07-13).
        return None, EngineAttempt(GE.GEMINI_DEEP, AO.FAILED,
                                   detail=f"{type(e).__name__}: {str(e)[:320]}",
                                   duration_seconds=round(time.monotonic() - t0, 1))
    dur = round(time.monotonic() - t0, 1)
    ok, reason = validate_engine_text(dr.text, dr.citations)
    if getattr(dr, "status", "") == "failed" or not ok:
        return None, EngineAttempt(GE.GEMINI_DEEP, AO.FAILED,
                                   detail=f"{reason} (empty body, $0 — NOT charged)",
                                   cost_logged=0.0, duration_seconds=dur)
    res = _map_engine_result(dr.text, dr.citations, dr.estimated_cost or 0.0, query, depth, GE.GEMINI_DEEP)
    return res, EngineAttempt(GE.GEMINI_DEEP, AO.SUCCESS, detail=f"{res.source_count} sources",
                              cost_logged=res.cost_usd, sources_found=res.source_count, duration_seconds=dur)


def _try_perplexity(query: str, depth: str, task_context: str
                    ) -> Tuple[Optional[ResearchResult], EngineAttempt]:
    PC, BEE = _load_perplexity()
    if PC is None:
        return None, EngineAttempt(GE.PERPLEXITY, AO.SKIPPED, detail="client unavailable (no PERPLEXITY_API_KEY)")
    try:
        client = PC()
        remaining = client.budget_remaining()
    except Exception as e:
        return None, EngineAttempt(GE.PERPLEXITY, AO.SKIPPED, detail=f"init failed ({type(e).__name__})")
    if remaining < 0.50:
        return None, EngineAttempt(GE.PERPLEXITY, AO.SKIPPED, detail=f"budget ${remaining:.2f} < $0.50 → floor")
    model = "sonar-deep-research" if depth in ("deep", "max") else "sonar-pro"
    t0 = time.monotonic()
    try:
        sr = client.search(query, model=model, task_context=task_context, query_type="research")
    except BEE as e:  # type: ignore
        return None, EngineAttempt(GE.PERPLEXITY, AO.SKIPPED, detail=f"budget: {str(e)[:60]}")
    except Exception as e:
        return None, EngineAttempt(GE.PERPLEXITY, AO.FAILED,
                                   detail=f"{type(e).__name__}", duration_seconds=round(time.monotonic() - t0, 1))
    dur = round(time.monotonic() - t0, 1)
    ok, reason = validate_engine_text(sr.text, sr.citations)
    if getattr(sr, "status", "") == "failed" or not ok:
        return None, EngineAttempt(GE.PERPLEXITY, AO.FAILED,
                                   detail=f"{reason} (empty body, $0 — NOT charged)",
                                   cost_logged=0.0, duration_seconds=dur)
    res = _map_engine_result(sr.text, sr.citations, sr.estimated_cost or 0.0, query, depth, GE.PERPLEXITY)
    return res, EngineAttempt(GE.PERPLEXITY, AO.SUCCESS, detail=f"{res.source_count} sources",
                              cost_logged=res.cost_usd, sources_found=res.source_count, duration_seconds=dur)


# ---------------------------------------------------------------------------
# Quality gate pass (REAL vs DEGRADED) + best-effort session cost log
# ---------------------------------------------------------------------------

def _apply_gate(result: ResearchResult, depth: str) -> ResearchResult:
    if result.status == RS.FAILED:
        return result
    min_src = DEPTH_MIN_SOURCES.get(depth, 3)
    min_dom = DEPTH_MIN_DOMAINS.get(depth, 3)
    if (result.source_count < min_src or result.unique_domains < min_dom) and result.status == RS.REAL:
        result.status = RS.DEGRADED
        result.warnings.append(
            f"below floor for depth={depth}: {result.source_count} sources / "
            f"{result.unique_domains} domains (need {min_src}/{min_dom})"
        )
    return result


def _cost_gate_log(engine: EngineKind, cost: float) -> None:
    service = {GE.GEMINI_DEEP: "gemini-deep-research", GE.PERPLEXITY: "perplexity-research"}.get(engine)
    if not service:
        return
    try:
        subprocess.run(
            [sys.executable, str(EXEC / "cost_gate.py"), "log", "--service", service,
             "--status", "success", "--actual-cost", str(round(cost, 4))],
            capture_output=True, text=True, timeout=20,
        )
    except Exception:
        pass  # session-cost visibility is best-effort; client usage files are authoritative


# ---------------------------------------------------------------------------
# THE DISPATCHER
# ---------------------------------------------------------------------------

def research(query: str, depth: str = "standard",
             task_context: str = "unified-research") -> ResearchResult:
    """Run unified research. Gemini-first → Perplexity → bedrock floor. Always
    returns a typed result with an honest receipt; never raises for engine failure."""
    attempts: List[EngineAttempt] = []
    result: Optional[ResearchResult] = None

    # 1. GEMINI-FIRST accelerator (skip for quick — Deep Research is slow + overkill)
    if depth in ("standard", "deep", "max"):
        result, attempt = _try_gemini(query, depth, task_context)
        attempts.append(attempt)

    # 2. PERPLEXITY second accelerator (deep/max only; standard goes straight to floor)
    if result is None and depth in ("deep", "max"):
        result, attempt = _try_perplexity(query, depth, task_context)
        attempts.append(attempt)
    elif result is None and depth == "standard":
        attempts.append(EngineAttempt(GE.PERPLEXITY, AO.NOT_ATTEMPTED, detail="reserved for deep/max"))

    # 3. CLAUDE BEDROCK FLOOR — catches failure AND below-floor "successes".
    #    2026-07-08: gemini_deep returned SUCCESS with 0 sources (132 claims
    #    quarantined) and the healthy floor was never attempted — $0.50 for
    #    unusable output. An accelerator only "delivers" if it clears the
    #    depth floor; otherwise the floor runs and the better result wins.
    min_src = DEPTH_MIN_SOURCES.get(depth, 3)
    min_dom = DEPTH_MIN_DOMAINS.get(depth, 3)
    accel_below_floor = (result is not None and result.status != RS.FAILED
                         and (result.source_count < min_src or result.unique_domains < min_dom))
    if result is None or result.status == RS.FAILED:
        floor = run_floor(query, depth=depth)
        floor.attempts = attempts + floor.attempts  # prepend the accelerator receipt rows
        result = floor
    elif accel_below_floor:
        floor = run_floor(query, depth=depth)
        if floor.source_count > result.source_count:
            # Accelerator spend was real even though the floor result wins —
            # log it here since step 5 will only see the floor's $0.
            if result.cost_usd and result.cost_usd > 0:
                _cost_gate_log(result.engine_used, result.cost_usd)
            floor.warnings.append(
                f"accelerator {result.engine_used} below floor "
                f"({result.source_count} sources / {result.unique_domains} domains) — "
                f"native floor result used instead")
            floor.attempts = attempts + floor.attempts
            result = floor
        else:
            result.warnings.append(
                "native floor attempted (accelerator below floor) but did not improve source count")
            result.attempts = attempts + floor.attempts + result.attempts
    else:
        attempts.append(EngineAttempt(GE.NATIVE, AO.NOT_ATTEMPTED, detail="accelerator delivered"))
        result.attempts = attempts + result.attempts

    # 4. Quality gate: set REAL vs DEGRADED honestly
    result = _apply_gate(result, depth)

    # 5. Cost: only validated spend; best-effort unified session log
    if result.cost_usd and result.cost_usd > 0:
        _cost_gate_log(result.engine_used, result.cost_usd)

    return result


# ---------------------------------------------------------------------------
# GROUND delegation — market grounding via avatar_manifold_runner (unchanged).
# The dispatcher only SHELLS OUT and reads status; it never re-implements the
# 30-day WARM-cache reuse gate (that stays the runner's single source of truth).
# ---------------------------------------------------------------------------

def ground(slug: str, market: str = "", product: str = "", tier: str = "deep",
           mode: str = "standard", refresh: bool = False, no_ground: bool = False,
           voc_file: str = "") -> ResearchResult:
    runner = EXEC / "avatar_manifold_runner.py"
    cmd = [sys.executable, str(runner), "ground", "--slug", slug, "--tier", tier, "--mode", mode]
    if market:
        cmd += ["--market", market]
    if product:
        cmd += ["--product", product]
    if refresh:
        cmd += ["--refresh"]
    if no_ground:
        cmd += ["--no-ground"]
    if voc_file:
        cmd += ["--voc-file", voc_file]

    t0 = time.monotonic()
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=1200)
        stdout = proc.stdout or ""
    except Exception as e:
        res = ResearchResult(query=f"ground:{slug}", status=RS.FAILED, engine_used=GE.NATIVE,
                             depth=tier, warnings=[f"runner error: {type(e).__name__}"])
        res.attempts.append(EngineAttempt(GE.NATIVE, AO.FAILED, detail=str(e)[:80]))
        return res
    dur = round(time.monotonic() - t0, 1)

    warm = ("WARM: reusing" in stdout) or ("REUSING anyway" in stdout)
    status_json = GROUND_TMP / "ground-status.json"
    dossier = GROUND_TMP / slug / "ground-dossier.md"
    st = {}
    try:
        st = json.loads(status_json.read_text()) if status_json.exists() else {}
    except Exception:
        st = {}
    # status.json is shared (last ground wins); only trust it if it's THIS slug.
    if st.get("slug") != slug:
        st = {}

    voc_urls = int(st.get("voc_source_urls", 0))
    has_modeled = bool(st.get("has_modeled", False))
    rqg = bool(st.get("rqg_strict_pass", False))
    gstatus = st.get("status", "")
    est_cost = 0.0 if warm else float(st.get("est_cost_usd", 0.0))

    engine = GE.CACHE_WARM if warm else (GE.GEMINI_DEEP if tier == "deep" else GE.NATIVE)
    warnings: List[str] = []
    if warm:
        status = RS.REAL if dossier.exists() else RS.FAILED
        warnings.append("WARM cache reuse — $0, no research re-fired")
    elif rqg and not has_modeled and gstatus in ("PASS",):
        status = RS.REAL
    elif gstatus in ("DEGRADED", "BYPASSED") or (has_modeled and voc_urls == 0):
        status = RS.DEGRADED
        warnings.append("grounding degraded — built on [MODELED] language; replace before shipping")
    elif gstatus or dossier.exists():
        status = RS.DEGRADED
        warnings.append(f"grounding partial (status={gstatus or 'unknown'}, voc_urls={voc_urls}, modeled={has_modeled})")
    else:
        status = RS.FAILED
        warnings.append("no grounding dossier produced")

    res = ResearchResult(
        query=f"ground:{slug} ({market or product or slug})",
        status=status, engine_used=engine, depth=tier, depth_achieved=tier,
        synthesis=(f"Grounding dossier: {dossier}" if dossier.exists() else "No dossier produced"),
        source_count=voc_urls, cost_usd=est_cost, warnings=warnings,
        quarantined_count=int(st.get("modeled_flag_count", 0)),
    )
    res.unique_domains = voc_urls  # voc urls are the source proxy for grounding
    res.provenance_pct = 100.0 if (voc_urls and not has_modeled) else (0.0 if not voc_urls else 50.0)
    res.attempts.append(EngineAttempt(
        engine, AO.ACTIVE if status != RS.FAILED else AO.FAILED,
        detail=f"{gstatus or 'warm'} · voc_urls={voc_urls} · modeled={has_modeled}",
        cost_logged=est_cost, sources_found=voc_urls, duration_seconds=dur))
    return res


# ---------------------------------------------------------------------------
# Report persistence - the body is never stdout-only
# ---------------------------------------------------------------------------

def persist_report(res: ResearchResult, label: str = "") -> Optional[Path]:
    """Write synthesis + sources + receipt to .tmp/research/<ts>-<slug>.md and
    return the path. Fires for every engine (Gemini, Perplexity, floor). Never
    raises - persistence must not be the thing that breaks a paid run."""
    try:
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        slug = re.sub(r"[^a-z0-9]+", "-", (label or res.query).lower()).strip("-")[:60] or "research"
        ts = time.strftime("%Y%m%d-%H%M%S")
        path = REPORT_DIR / f"{ts}-{slug}.md"
        srcs = "\n".join(f"{i}. {s.url}" for i, s in enumerate(res.sources, 1))
        body = (res.synthesis or "").strip() or "_(no synthesis body - see findings)_"
        findings = "\n".join(f"- {f.claim} [{f.source_url}]" for f in res.findings[:200])
        path.write_text(
            f"# Research report\n\n- query: {res.query}\n- depth: {res.depth} "
            f"(achieved {res.depth_achieved})\n- status: {res.status.value}\n"
            f"- engine: {res.engine_used.value}\n- cost_usd: {res.cost_usd:.2f}\n"
            f"- saved: {res.timestamp}\n\n---\n\n{body}\n\n"
            f"## Findings ({len(res.findings)})\n\n{findings}\n\n"
            f"## Sources ({len(res.sources)})\n\n{srcs}\n\n---\n\n```\n{res.render_receipt()}\n```\n")
        return path
    except Exception:
        return None


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cli() -> int:
    import argparse
    argv = sys.argv[1:]
    sub = argv[0] if argv else ""

    if sub == "plan":
        # Emit the expert-swarm plan (decompose → cast personas → per-agent briefs).
        # The deep-research-swarm workflow consumes this to fan out.
        p = argparse.ArgumentParser(prog="research.py plan")
        p.add_argument("--query", required=True)
        p.add_argument("--depth", default="deep", choices=["quick", "standard", "deep", "max"])
        a = p.parse_args(argv[1:])
        try:
            from research_personas import build_swarm_plan
        except ImportError:
            from execution.research_personas import build_swarm_plan
        print(json.dumps(build_swarm_plan(a.query, a.depth), indent=2))
        return 0

    if sub == "gemini-start":
        # Fire Gemini Deep Research in the background; return the interaction id
        # immediately so the swarm can run in parallel and merge later. $0 to start.
        p = argparse.ArgumentParser(prog="research.py gemini-start")
        p.add_argument("--query", required=True)
        p.add_argument("--mode", default="standard", choices=["standard", "max"])
        a = p.parse_args(argv[1:])
        DRC, BEE = _load_gemini()
        if DRC is None:
            print(json.dumps({"ok": False, "reason": "gemini client unavailable"}))
            return 0
        try:
            iid = DRC().start_async(a.query, mode=a.mode)
            print(json.dumps({"ok": True, "interaction_id": iid, "mode": a.mode}))
        except Exception as e:
            print(json.dumps({"ok": False, "reason": f"{type(e).__name__}: {str(e)[:120]}"}))
        return 0

    if sub == "gemini-collect":
        p = argparse.ArgumentParser(prog="research.py gemini-collect")
        p.add_argument("--id", required=True)
        p.add_argument("--query", default="")
        p.add_argument("--mode", default="standard", choices=["standard", "max"])
        a = p.parse_args(argv[1:])
        DRC, BEE = _load_gemini()
        if DRC is None:
            print(json.dumps({"status": "unavailable"}))
            return 0
        try:
            r = DRC().collect(a.id, query=a.query, mode=a.mode)
            text = r.text or ""
            cites = r.citations or []
            # Resolve Gemini's [cite: N] / [cite: N, M] markers into real URLs so the
            # downstream synthesis cites resolvable sources, never bare placeholders.
            if cites and text:
                def _resolve(m):
                    nums = [int(x) for x in re.findall(r"\d+", m.group(0))]
                    urls = [cites[n - 1] for n in nums if 1 <= n <= len(cites)]
                    return "[" + ", ".join(urls) + "]" if urls else m.group(0)
                text = re.sub(r"\[cite:\s*[\d,\s]+\]", _resolve, text)
            print(json.dumps({"status": r.status, "text": text,
                              "citations": cites, "cost_usd": r.estimated_cost or 0.0,
                              "report_path": getattr(r, "report_path", None)}))
        except Exception as e:
            print(json.dumps({"status": "error", "reason": f"{type(e).__name__}"}))
        return 0

    if sub == "ground":
        p = argparse.ArgumentParser(prog="research.py ground")
        p.add_argument("--slug", required=True)
        p.add_argument("--market", default="")
        p.add_argument("--product", default="")
        p.add_argument("--tier", default="deep", choices=["free", "lean", "deep"])
        p.add_argument("--mode", default="standard", choices=["standard", "max"])
        p.add_argument("--refresh", action="store_true")
        p.add_argument("--no-ground", action="store_true")
        p.add_argument("--voc-file", default="")
        p.add_argument("--json", action="store_true")
        a = p.parse_args(argv[1:])
        res = ground(a.slug, a.market, a.product, a.tier, a.mode, a.refresh, a.no_ground, a.voc_file)

    elif sub == "ingest":
        p = argparse.ArgumentParser(prog="research.py ingest")
        p.add_argument("--findings", required=True)
        p.add_argument("--query", required=True)
        p.add_argument("--depth", default="standard", choices=["quick", "standard", "deep", "max"])
        p.add_argument("--swarm", action="store_true", help="label result as native_swarm (multi-agent fan-out)")
        p.add_argument("--json", action="store_true")
        a = p.parse_args(argv[1:])
        engine = EngineKind.NATIVE_SWARM if a.swarm else EngineKind.NATIVE
        res = ingest_findings(Path(a.findings), a.query, depth=a.depth, engine=engine)

    else:
        # default: run. Accept either `run "<q>"` or a bare "<q>".
        if sub == "run":
            argv = argv[1:]
        p = argparse.ArgumentParser(prog="research.py")
        p.add_argument("query")
        p.add_argument("--depth", default="standard", choices=["quick", "standard", "deep", "max"])
        p.add_argument("--task-context", default="unified-research")
        p.add_argument("--json", action="store_true")
        a = p.parse_args(argv)
        res = research(a.query, depth=a.depth, task_context=a.task_context)

    # DEPTH CONTRACT ENFORCEMENT (2026-07-26 shallow-research fix): at deep/max,
    # DEGRADED is a FAILURE, not a pass. A "deep" result below its floor used to
    # return quietly and get treated as trusted insight downstream. Now it exits
    # non-zero, carries acceptable:false, and names the unmet floor.
    req_depth = getattr(a, "depth", "standard")
    strict_fail = (res.status == RS.DEGRADED and req_depth in ("deep", "max"))
    if strict_fail:
        res.warnings.append(
            f"DEPTH CONTRACT UNMET (depth={req_depth}): DEGRADED is a hard fail at this "
            f"tier — run the agent fan-out + `research.py ingest` before using this result."
        )
    report_path = persist_report(res, label=getattr(a, "task_context", "") or "")
    if getattr(a, "json", False):
        try:
            payload = json.loads(res.to_json())
        except Exception:
            payload = {"raw": res.to_json()}
        payload["acceptable"] = bool(res.is_usable and not strict_fail)
        payload["report_path"] = str(report_path) if report_path else None
        print(json.dumps(payload, indent=2))
    else:
        print(res.render_receipt())
        if report_path:
            print(f"Report body:   {report_path}")
        else:
            print("Report body:   NOT SAVED (persist_report failed) - use --json to capture synthesis")
        if strict_fail:
            print(f"\n⛔ DEPTH CONTRACT UNMET — depth={req_depth} result is DEGRADED. "
                  f"This output is RECON-GRADE, not decision-grade. Exit 2.")
    return 0 if (res.is_usable and not strict_fail) else 2


if __name__ == "__main__":
    raise SystemExit(_cli())
