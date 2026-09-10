#!/usr/bin/env python3
"""
Unified Research Engine — the single entry point every consumer calls.

Current policy:
  • AUTO / CODEX-NATIVE is the default. It compiles a Free-First mission for
    the host Codex web tools and never silently invokes a provider API.
  • GEMINI is an explicit provider mode behind the Research OS parity budget
    ledger, shared cost gate, and a machine-verified provider hard ceiling.
  • BENCHMARK-IMPORT normalizes subscription reports without API spend.
  • LEGACY-ACCELERATORS preserves the older Gemini → Perplexity → native-floor
    dispatcher only as an explicit compatibility route.
  • HONEST RECEIPT on every completed result records what fired, what failed,
    achieved depth, and provider exposure.

The engine never fabricates to fill a gap, never logs cost for a call that
didn't return validated content, and never persists an unsourced finding. It can
degrade — it cannot lie.

This is a thin façade: it orchestrates the (now bug-fixed) clients and the floor
behind one typed contract. Existing consumers migrate to it one at a time; the
old client CLIs keep working.

CLI:
    python3 execution/research.py "<query>" [--depth standard|quick|deep|max] [--json]
    python3 execution/research.py run --mission <mission.json> --mode auto|codex-native|gemini|benchmark-import|ensemble
    python3 execution/research.py bakeoff --mission <mission.json> --candidates-dir <dir> --out-dir <dir>
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
    if remaining < 3.00:
        return None, EngineAttempt(GE.GEMINI_DEEP, AO.SKIPPED, detail=f"budget ${remaining:.2f} < $3 conservative reservation")
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
                                   detail=f"{type(e).__name__}: {str(e)[:110]}",
                                   duration_seconds=round(time.monotonic() - t0, 1))
    dur = round(time.monotonic() - t0, 1)
    ok, reason = validate_engine_text(dr.text, dr.citations)
    if getattr(dr, "status", "") == "failed" or not ok:
        return None, EngineAttempt(GE.GEMINI_DEEP, AO.FAILED,
                                   detail=f"{reason} (report invalid; provider exposure still recorded)",
                                   cost_logged=float(getattr(dr, "estimated_cost", 0.0) or 0.0),
                                   duration_seconds=dur)
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

def _legacy_research(query: str, depth: str = "standard",
                     task_context: str = "legacy-accelerators") -> ResearchResult:
    """Explicit compatibility route: Gemini → Perplexity → native floor.

    This is intentionally not the generic default. Provider billing is separate
    from consumer subscriptions and must be approved by the owning workflow.
    """
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


def research(query: str, depth: str = "standard",
             task_context: str = "unified-research", mode: str = "codex-native") -> ResearchResult:
    """Programmatic research boundary with no silent paid-provider activation.

    Host-native web execution needs the active Codex thread, so callers should
    use the CLI mission compiler for ``auto``/``codex-native``.  The returned
    FAILED contract makes that limitation explicit instead of firing Gemini.
    """
    if mode == "legacy-accelerators":
        return ResearchResult(
            query=query,
            status=RS.FAILED,
            engine_used=GE.NATIVE,
            depth=depth,
            warnings=[
                "legacy accelerator fan-out is parked at the public research boundary; "
                "use Codex-native or the explicit mission-ledger Gemini route"
            ],
            attempts=[EngineAttempt(GE.NATIVE, AO.NOT_ATTEMPTED, detail="legacy paid fan-out disabled")],
        )
    if mode == "gemini":
        return ResearchResult(
            query=query,
            status=RS.FAILED,
            engine_used=GE.GEMINI_DEEP,
            depth=depth,
            warnings=[
                "programmatic Gemini mode cannot bypass the mission spend ledger; "
                "use `research.py run --mode gemini --mission ...`"
            ],
            attempts=[EngineAttempt(GE.GEMINI_DEEP, AO.NOT_ATTEMPTED, detail="mission spend reservation required")],
        )
    if mode not in {"auto", "codex-native"}:
        return ResearchResult(
            query=query, status=RS.FAILED, engine_used=GE.NATIVE, depth=depth,
            warnings=[f"unsupported programmatic research mode: {mode}"],
        )
    return ResearchResult(
        query=query,
        status=RS.FAILED,
        engine_used=GE.NATIVE,
        depth=depth,
        synthesis="Compile and execute a Free-First Research Mission in the active Codex thread.",
        warnings=[
            "codex-native research requires host web tools; use `research.py run --mode codex-native` "
            "to compile the mission instead of silently invoking a provider"
        ],
        attempts=[EngineAttempt(GE.NATIVE, AO.NOT_ATTEMPTED, detail="host-native mission not yet executed")],
    )


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
# CLI
# ---------------------------------------------------------------------------

def _cli() -> int:
    import argparse
    argv = sys.argv[1:]
    sub = argv[0] if argv else ""

    if sub == "bakeoff":
        p = argparse.ArgumentParser(prog="research.py bakeoff")
        p.add_argument("--mission", required=True)
        p.add_argument("--candidates", default="codex-native,gemini-native,chatgpt-native")
        p.add_argument("--candidates-dir", required=True)
        p.add_argument("--out-dir", required=True)
        p.add_argument("--blind", action="store_true")
        p.add_argument("--max-total-provider-spend", type=float, default=10.0)
        a = p.parse_args(argv[1:])
        if a.max_total_provider_spend > 10.0:
            print(json.dumps({"ok": False, "status": "BLOCKED", "reason": "$10 absolute cap cannot be raised"}, indent=2))
            return 2
        try:
            from research_bakeoff import build_bakeoff
        except ImportError:
            from execution.research_bakeoff import build_bakeoff
        try:
            payload = build_bakeoff(Path(a.mission), Path(a.candidates_dir), Path(a.out_dir))
        except Exception as e:
            print(json.dumps({"ok": False, "status": "INVALID", "reason": str(e)}, indent=2))
            return 2
        print(json.dumps({
            "ok": True,
            "verdict": payload["verdict"],
            "candidate_count": payload["candidate_count"],
            "results": str((Path(a.out_dir) / "bakeoff-results.json").resolve()),
        }, indent=2))
        return 0

    if sub == "run":
        p = argparse.ArgumentParser(prog="research.py run")
        p.add_argument("query", nargs="?", default="")
        p.add_argument("--mission", default="")
        p.add_argument("--mode", default="auto",
                       choices=["auto", "codex-native", "gemini", "benchmark-import", "ensemble", "legacy-accelerators"])
        p.add_argument("--depth", default="standard", choices=["quick", "standard", "deep", "max"])
        p.add_argument("--task-context", default="unified-research")
        p.add_argument("--max-total-provider-spend", type=float, default=10.0)
        p.add_argument("--out-dir", default="")
        p.add_argument("--report", default="")
        p.add_argument("--receipt", default="")
        p.add_argument("--audit", default="")
        p.add_argument("--provider-spend-approved", action="store_true")
        p.add_argument("--json", action="store_true")
        a = p.parse_args(argv[1:])
        if a.max_total_provider_spend > 10.0:
            print(json.dumps({"ok": False, "status": "BLOCKED", "reason": "$10 absolute cap cannot be raised"}, indent=2))
            return 2

        if a.mode in {"auto", "codex-native"}:
            if a.mission:
                try:
                    from research_bakeoff import ResearchMission, SpendLedger
                except ImportError:
                    from execution.research_bakeoff import ResearchMission, SpendLedger
                try:
                    mission = ResearchMission.from_path(Path(a.mission))
                    out_dir = Path(a.out_dir) if a.out_dir else Path(a.mission).resolve().parent
                    out_dir.mkdir(parents=True, exist_ok=True)
                    prompt_path = out_dir / "frozen-research-prompt.md"
                    prompt_path.write_text(mission.frozen_prompt(), encoding="utf-8")
                    SpendLedger(out_dir / "spend-ledger.json", mission)
                    print(json.dumps({
                        "ok": True,
                        "status": "PLANNED",
                        "mode": "codex-native",
                        "incremental_api_cost_usd": 0.0,
                        "mission_id": mission.mission_id,
                        "prompt": str(prompt_path.resolve()),
                        "next_action": "execute the frozen prompt with Codex native web tools, then import the sealed report",
                    }, indent=2))
                    return 0
                except Exception as e:
                    print(json.dumps({"ok": False, "status": "INVALID", "reason": str(e)}, indent=2))
                    return 2
            if not a.query:
                p.error("auto/codex-native mode requires query or --mission")
            cmd = [
                sys.executable, str(EXEC / "free_first_research.py"), "plan",
                "--objective", a.query,
                "--decision", "Produce decision-grade current research without provider API spend",
                "--downstream", "Deep Research OS",
                "--artifact", "Codex-native research brief and evidence receipt",
                "--depth", a.depth,
            ]
            proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT))
            print(proc.stdout or proc.stderr)
            return proc.returncode

        if a.mode == "benchmark-import":
            if not (a.mission and a.report and a.out_dir):
                p.error("benchmark-import requires --mission, --report, and --out-dir")
            try:
                from research_bakeoff import ResearchMission, load_audit, read_json, score_candidate, validate_import_report, write_json
                mission = ResearchMission.from_path(Path(a.mission))
                import_validation = validate_import_report(mission, Path(a.report))
                if not import_validation["passed"]:
                    raise ValueError("import validation failed: " + "; ".join(import_validation["errors"]))
                receipt = read_json(Path(a.receipt)) if a.receipt else {
                    "provider": "chatgpt-native", "engine": "chatgpt-deep-research-subscription",
                    "run_id": "subscription-import", "elapsed_seconds": 0.0,
                    "estimated_cost_usd": 0.0,
                    "billing_verification": "subscription_import_no_incremental_api_cost",
                    "stop_reason": "completed",
                }
                audit = load_audit(Path(a.audit) if a.audit else None)
                candidate = score_candidate(mission, "chatgpt-native", Path(a.report), receipt, audit)
                candidate["import_validation"] = import_validation
                out_path = Path(a.out_dir) / "chatgpt-native.candidate.json"
                write_json(out_path, candidate)
                print(json.dumps({"ok": True, "candidate": str(out_path.resolve()),
                                  "grade_status": candidate["grade_status"]}, indent=2))
                return 0
            except Exception as e:
                print(json.dumps({"ok": False, "status": "INVALID", "reason": str(e)}, indent=2))
                return 2

        if a.mode == "ensemble":
            if not (a.mission and a.out_dir):
                p.error("ensemble requires --mission and --out-dir; use `research.py bakeoff` for sealed grading")
            print(json.dumps({
                "ok": True, "status": "STAGED", "mode": "ensemble",
                "reason": "ensemble never auto-fires providers; import sealed candidates then run research.py bakeoff",
            }, indent=2))
            return 0

        if a.mode == "gemini":
            if not (a.mission and a.out_dir):
                p.error("gemini mode requires --mission and --out-dir")
            try:
                from research_bakeoff import ResearchMission, SpendLedger, SpendBlocked, unique_domains, write_json
                mission = ResearchMission.from_path(Path(a.mission))
                out_dir = Path(a.out_dir)
                out_dir.mkdir(parents=True, exist_ok=True)
                ledger = SpendLedger(out_dir / "spend-ledger.json", mission)
                reservation = ledger.reserve_gemini_standard(
                    mission.spending_policy.get("gemini_billing_verification", {})
                )
            except Exception as e:
                print(json.dumps({"ok": False, "status": "BLOCKED", "reason": str(e)}, indent=2))
                return 2

            gate = subprocess.run(
                [sys.executable, str(EXEC / "cost_gate.py"), "check",
                 "--service", "gemini-deep-research", "--request", mission.mission_id],
                capture_output=True, text=True, cwd=str(ROOT),
            )
            if gate.returncode == 1 or (gate.returncode == 2 and not a.provider_spend_approved):
                ledger.release(reservation, "shared cost gate denied or lacked explicit approval", interaction_started=False)
                print(json.dumps({"ok": False, "status": "BLOCKED", "reason": gate.stdout or gate.stderr}, indent=2))
                return 2

            DRC, BEE = _load_gemini()
            if DRC is None:
                ledger.release(reservation, "Gemini client unavailable", interaction_started=False)
                print(json.dumps({"ok": False, "status": "BLOCKED", "reason": "Gemini client unavailable"}, indent=2))
                return 2
            started_at = time.monotonic()
            try:
                result = DRC().research(
                    mission.frozen_prompt(), mode="standard",
                    spend_authorization={
                        "ledger_path": str(ledger.path.resolve()),
                        "reservation_id": reservation,
                        "mission_id": mission.mission_id,
                    },
                    task_context=mission.mission_id,
                    query_type="research-parity-bakeoff",
                )
                elapsed = round(time.monotonic() - started_at, 2)
                if result.status != "completed" or not result.text:
                    ledger.release(reservation, "provider returned no validated report", interaction_started=True)
                    print(json.dumps({"ok": False, "status": "FAILED", "reason": "Gemini report invalid; paid retry forbidden"}, indent=2))
                    return 2
                ledger.complete(reservation, result.interaction_id, result.estimated_cost or 3.0)
                report_path = out_dir / "gemini-native-report.md"
                report_path.write_text(result.text, encoding="utf-8")
                urls = list(dict.fromkeys(result.citations or []))
                receipt = {
                    "provider": "gemini-native",
                    "engine": result.agent,
                    "run_id": result.interaction_id,
                    "elapsed_seconds": elapsed,
                    "source_count": len(urls),
                    "domain_count": len(unique_domains(urls)),
                    "resolved_citations": len(urls),
                    "estimated_cost_usd": result.estimated_cost or 3.0,
                    "actual_cost_usd": None,
                    "billing_verification": "machine_verified_hard_ceiling",
                    "stop_reason": "completed",
                    "warnings": ["actual provider invoice unavailable at run time; estimated exposure recorded"],
                }
                write_json(out_dir / "gemini-native-receipt.json", receipt)
                print(json.dumps({"ok": True, "status": "COMPLETED", "report": str(report_path.resolve()),
                                  "receipt": str((out_dir / "gemini-native-receipt.json").resolve())}, indent=2))
                return 0
            except Exception as e:
                ledger.release(reservation, str(e), interaction_started=True)
                print(json.dumps({"ok": False, "status": "FAILED", "reason": str(e),
                                  "retry_allowed": False}, indent=2))
                return 2

        print(json.dumps({
            "ok": False,
            "status": "BLOCKED",
            "reason": "legacy-accelerators can fan into multiple paid providers and is disabled from the unified CLI; use explicit capped Gemini mode or Codex-native",
        }, indent=2))
        return 2

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
        print(json.dumps({
            "ok": False,
            "status": "BLOCKED",
            "reason": "uncapped background Gemini starts are retired; use `research.py run --mode gemini --mission ...`",
        }, indent=2))
        return 2

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
                              "citations": cites, "cost_usd": r.estimated_cost or 0.0}))
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
        # Bare query retains compatibility but defaults to Codex-native. It
        # returns an explicit host-tool handoff rather than firing a provider.
        p = argparse.ArgumentParser(prog="research.py")
        p.add_argument("query")
        p.add_argument("--depth", default="standard", choices=["quick", "standard", "deep", "max"])
        p.add_argument("--task-context", default="unified-research")
        p.add_argument("--mode", default="codex-native",
                       choices=["auto", "codex-native", "gemini", "legacy-accelerators"])
        p.add_argument("--json", action="store_true")
        a = p.parse_args(argv)
        if a.mode in {"auto", "codex-native"}:
            proc = subprocess.run(
                [
                    sys.executable, str(EXEC / "free_first_research.py"), "plan",
                    "--objective", a.query,
                    "--decision", "Produce decision-grade current research without provider API spend",
                    "--downstream", "Deep Research OS",
                    "--artifact", "Codex-native research brief and evidence receipt",
                    "--depth", a.depth,
                ],
                capture_output=True, text=True, cwd=str(ROOT),
            )
            print(proc.stdout or proc.stderr)
            return proc.returncode
        res = research(a.query, depth=a.depth, task_context=a.task_context, mode=a.mode)

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
    if getattr(a, "json", False):
        try:
            payload = json.loads(res.to_json())
        except Exception:
            payload = {"raw": res.to_json()}
        payload["acceptable"] = bool(res.is_usable and not strict_fail)
        print(json.dumps(payload, indent=2))
    else:
        print(res.render_receipt())
        if strict_fail:
            print(f"\n⛔ DEPTH CONTRACT UNMET — depth={req_depth} result is DEGRADED. "
                  f"This output is RECON-GRADE, not decision-grade. Exit 2.")
    return 0 if (res.is_usable and not strict_fail) else 2


if __name__ == "__main__":
    raise SystemExit(_cli())
