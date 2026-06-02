#!/usr/bin/env python3
"""
Native Floor — the bedrock research engine that CANNOT break.

This is the floor every research request falls to when the paid accelerators
(Gemini Deep Research, Perplexity) are unavailable, fail, or aren't warranted.
It depends only on tools Claude always has, so it is always available at ~$0:

  • Python (deterministic, reliable):
      - Tavily search (free, 1000/mo, key already in .env) → real sourced findings
      - query decomposition (reuses deep_research_engine.decompose_query)
      - validation + provenance math + the typed ResearchResult
  • Agent-orchestrated (the depth multiplier):
      - WebSearch → WebFetch fan-out + adversarial verify, run by the workflow
        agent per the directive this module writes, then handed back via a
        native-findings.jsonl file that ingest_findings() validates.

The two halves compose but neither can fabricate. Python only emits what Tavily
actually returned; ingest drops any agent finding with no real source URL. So a
result is always honest about its depth — REAL, DEGRADED, or FAILED.

CLI:
    python3 execution/native_floor.py floor  "<query>" [--depth standard] [--slug s]
    python3 execution/native_floor.py ingest --findings path.jsonl --query "<q>" [--depth d]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "execution"))

try:
    from research_contract import (
        ResearchResult, ResearchStatus, EngineKind, Finding, Source,
        EngineAttempt, AttemptOutcome,
    )
    from deep_research_engine import decompose_query, ResearchEngine
except ImportError:  # imported as execution.native_floor
    from execution.research_contract import (
        ResearchResult, ResearchStatus, EngineKind, Finding, Source,
        EngineAttempt, AttemptOutcome,
    )
    from execution.deep_research_engine import decompose_query, ResearchEngine

import json as _json
import subprocess as _subprocess


TMP = ROOT / ".tmp" / "research"

# The native floor's source thresholds. Lighter than the paid-deep bar of 15 —
# the floor is the reliable baseline; the agent fan-out + the dispatcher's
# quality-gate pass enforce the higher bar where the depth demands it.
DEPTH_MIN_SOURCES = {"quick": 2, "standard": 3, "deep": 6, "max": 8}
DEPTH_MIN_DOMAINS = {"quick": 2, "standard": 3, "deep": 3, "max": 4}


# ---------------------------------------------------------------------------
# env
# ---------------------------------------------------------------------------

def load_env_vars() -> dict:
    env = {}
    try:
        for line in (ROOT / ".env").read_text().splitlines():
            if "=" in line and not line.strip().startswith("#"):
                k, _, v = line.partition("=")
                env[k.strip()] = v.strip().strip('"').strip("'")
    except Exception:
        pass
    return env


# ---------------------------------------------------------------------------
# Tavily — the deterministic, reliable, $0 leg
# ---------------------------------------------------------------------------

def tavily_search(query: str, max_results: int = 6,
                  env: Optional[dict] = None) -> List[Dict]:
    """Run one Tavily search. Returns raw results [{content,url,title}]. Never
    raises — on any failure returns [] so the floor degrades, never breaks."""
    env = env or load_env_vars()
    tk = env.get("TAVILY_API_KEY")
    if not tk:
        return []
    try:
        import requests
        r = requests.post(
            "https://api.tavily.com/search",
            json={"api_key": tk, "query": query, "max_results": max_results,
                  "search_depth": "advanced"},
            timeout=40,
        )
        if not r.ok:
            return []
        return r.json().get("results", []) or []
    except Exception:
        return []


def tavily_floor(query: str, search_queries: List[str], max_per: int = 6,
                 env: Optional[dict] = None) -> Tuple[List[Finding], List[Source], int]:
    """Run Tavily across the decomposed queries and build sourced findings.

    Returns (findings, sources, dropped) where `dropped` counts URL-less results
    that were rejected (never persisted as findings)."""
    env = env or load_env_vars()
    findings: List[Finding] = []
    sources: List[Source] = []
    seen_urls, seen_claims = set(), set()
    dropped = 0

    for sq in search_queries:
        for res in tavily_search(sq, max_results=max_per, env=env):
            url = (res.get("url") or "").strip()
            content = (res.get("content") or res.get("title") or "").strip().replace("\n", " ")
            title = (res.get("title") or "").strip()
            if len(content) < 40:
                continue
            if not url:
                dropped += 1
                continue
            ckey = content[:60].lower()
            if ckey in seen_claims:
                continue
            seen_claims.add(ckey)
            try:
                findings.append(Finding(
                    claim=content[:400], source_url=url, excerpt=content[:300],
                    confidence="medium", finding_type="data",
                ))
            except Exception:
                dropped += 1
                continue
            if url not in seen_urls:
                seen_urls.add(url)
                sources.append(Source(url=url, title=title))
    return findings, sources, dropped


# ---------------------------------------------------------------------------
# Tavily RESEARCH + EXTRACT — frontier-grade floor legs ($0 on the Tavily sub)
# ---------------------------------------------------------------------------

def tavily_research(query: str, model: str = "auto", timeout: int = 300) -> Dict:
    """Run Tavily's agentic deep-research endpoint via the `tvly` CLI. Returns a
    cited multi-source report: {content, sources:[{url,title}]}. Never raises —
    returns {} on any failure so the floor degrades, never breaks.

    This is the frontier-grade leg: one call yields a synthesized, ~15-20-source
    cited report (not snippets), comparable to a single Gemini/Perplexity deep call.
    """
    try:
        proc = _subprocess.run(
            ["tvly", "research", query, "--model", model, "--json", "--timeout", str(timeout)],
            capture_output=True, text=True, timeout=timeout + 30,
        )
        if proc.returncode != 0 or not proc.stdout.strip():
            return {}
        data = _json.loads(proc.stdout)
        return {"content": data.get("content", ""), "sources": data.get("sources", []) or []}
    except Exception:
        return {}


def tavily_extract(urls: List[str], query: Optional[str] = None,
                   timeout: float = 60.0) -> List[Dict]:
    """Full-page markdown extraction via `tvly extract` (up to 20 URLs/call,
    JS-rendered). Returns [{url, title, raw_content}]. Never raises."""
    if not urls:
        return []
    try:
        cmd = ["tvly", "extract", *urls[:20], "--json", "--format", "markdown",
               "--timeout", str(timeout)]
        if query:
            cmd += ["--query", query, "--chunks-per-source", "3"]
        proc = _subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 30)
        if proc.returncode != 0 or not proc.stdout.strip():
            return []
        data = _json.loads(proc.stdout)
        results = data.get("results") or (data if isinstance(data, list) else [data])
        out = []
        for r in results:
            if isinstance(r, dict) and r.get("url"):
                out.append({"url": r["url"], "title": r.get("title", ""),
                            "raw_content": r.get("raw_content") or r.get("content", "")})
        return out
    except Exception:
        return []


def research_to_findings(content: str, sources: List[Dict]) -> Tuple[List[Finding], List[Source], int]:
    """Parse a Tavily research report (content + sources) into typed Findings via
    the engine's provenance-quarantine parser (URL-less claims dropped)."""
    urls = [s.get("url", "") for s in sources if s.get("url")]
    eng = ResearchEngine()
    raw = eng._parse_perplexity_response(content, urls)
    findings: List[Finding] = []
    for f in raw:
        try:
            findings.append(Finding(claim=f.claim, source_url=f.source_url,
                                    excerpt=f.excerpt or "", confidence=f.confidence,
                                    finding_type=f.finding_type))
        except Exception:
            pass
    src_objs, seen = [], set()
    for s in sources:
        u = s.get("url", "")
        if u and u not in seen:
            seen.add(u)
            src_objs.append(Source(url=u, title=s.get("title", "")))
    return findings, src_objs, len(eng._quarantine)


# ---------------------------------------------------------------------------
# Decomposition (reused, flattened to plain query strings)
# ---------------------------------------------------------------------------

def decompose(query: str) -> List[str]:
    """Flatten the engine's decomposition into a deduped list of search queries."""
    queries: List[str] = []
    try:
        for sq in decompose_query(query):
            queries.extend(sq.search_queries)
    except Exception:
        queries = [query]
    # Always include the bare query; dedupe preserving order.
    queries = [query] + queries
    return list(dict.fromkeys(q for q in queries if q and q.strip()))


# ---------------------------------------------------------------------------
# The agent fan-out directive (the depth multiplier)
# ---------------------------------------------------------------------------

FINDINGS_SCHEMA = (
    '{"claim": "<one sourced claim>", "source_url": "https://...", '
    '"excerpt": "<verbatim quote/snippet>", "confidence": "high|medium|low", '
    '"finding_type": "data|quote|statistic|opinion|case_study"}'
)


def write_directive(query: str, depth: str, search_queries: List[str],
                    seed_sources: List[Source], out_dir: Path) -> Path:
    """Write the native fan-out directive the workflow agent executes to upgrade
    a Tavily-only floor result to full REAL depth."""
    out_dir.mkdir(parents=True, exist_ok=True)
    directive = out_dir / "native-directive.md"
    findings_path = out_dir / "native-findings.jsonl"
    n = len(search_queries)
    seed = "\n".join(f"  - {s.url}" for s in seed_sources[:10]) or "  (none — Tavily returned nothing; rely fully on WebSearch)"
    directive.write_text(
        f"# NATIVE RESEARCH FAN-OUT — `{query}`\n\n"
        f"Depth: **{depth}**. This is the bedrock floor's depth multiplier. Run it with\n"
        f"your own free tools (WebSearch + WebFetch). Cost: $0.\n\n"
        f"## Steps\n"
        f"1. **Fan out** WebSearch across these {n} angles (run several in parallel):\n"
        + "\n".join(f"   - {q}" for q in search_queries) + "\n\n"
        f"2. **Read** the 2-3 strongest sources per angle with WebFetch. Prefer primary\n"
        f"   sources, real user discussions (Reddit/forums), and dated reports.\n\n"
        f"3. **Adversarially verify** each non-trivial claim: would a skeptic find a\n"
        f"   contradicting source? Drop or down-rank claims you cannot stand behind.\n\n"
        f"4. **Write** one JSON object per validated finding to `{findings_path.name}`\n"
        f"   (JSONL — one per line). Schema:\n"
        f"   ```\n   {FINDINGS_SCHEMA}\n   ```\n"
        f"   **Every finding MUST carry a real `source_url`.** A claim with no URL is\n"
        f"   not a finding — omit it (it will be rejected on ingest anyway).\n\n"
        f"5. **Ingest** to produce the typed, receipt-bearing result:\n"
        f"   ```bash\n"
        f"   python3 execution/native_floor.py ingest --findings {findings_path} "
        f'--query "{query}" --depth {depth}\n'
        f"   ```\n\n"
        f"## Tavily seed sources (already pulled, $0)\n{seed}\n"
    )
    return directive


# ---------------------------------------------------------------------------
# Ingest agent findings → typed result
# ---------------------------------------------------------------------------

def _status_for(findings: List[Finding], sources: List[Source], depth: str
                ) -> Tuple[ResearchStatus, List[str]]:
    warnings: List[str] = []
    if not findings:
        return ResearchStatus.FAILED, ["no sourced findings — floor produced nothing usable"]
    urls = {f.source_url for f in findings} | {s.url for s in sources if s.url}
    domains = {Source(url=u).domain for u in urls if u}
    min_src = DEPTH_MIN_SOURCES.get(depth, 3)
    min_dom = DEPTH_MIN_DOMAINS.get(depth, 3)
    if len(urls) >= min_src and len(domains) >= min_dom:
        return ResearchStatus.REAL, warnings
    warnings.append(
        f"thin coverage for depth={depth}: {len(urls)} sources / {len(domains)} domains "
        f"(floor: {min_src} sources / {min_dom} domains) — treat as DEGRADED"
    )
    return ResearchStatus.DEGRADED, warnings


def ingest_findings(jsonl_path: Path, query: str, depth: str = "standard",
                    engine: EngineKind = EngineKind.NATIVE) -> ResearchResult:
    """Validate an agent's native-findings.jsonl into a typed ResearchResult.
    URL-less / malformed lines are dropped (counted as quarantined), never
    persisted as findings. `engine` lets the swarm label its result native_swarm."""
    findings: List[Finding] = []
    sources: List[Source] = []
    seen_urls = set()
    quarantined = 0
    warnings: List[str] = []

    raw = jsonl_path.read_text() if jsonl_path.exists() else ""
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            quarantined += 1
            continue
        url = (obj.get("source_url") or "").strip()
        claim = (obj.get("claim") or "").strip()
        if not claim or not url or not url.startswith("http"):
            quarantined += 1  # provenance integrity: no URL = not a finding
            continue
        try:
            findings.append(Finding(
                claim=claim, source_url=url,
                excerpt=(obj.get("excerpt") or "")[:400],
                confidence=obj.get("confidence", "medium"),
                finding_type=obj.get("finding_type", "data"),
            ))
        except Exception:
            quarantined += 1
            continue
        if url not in seen_urls:
            seen_urls.add(url)
            sources.append(Source(url=url, title=obj.get("title", "")))

    status, status_warnings = _status_for(findings, sources, depth)
    warnings += status_warnings
    if quarantined:
        warnings.append(f"{quarantined} agent finding(s) rejected for missing/invalid source URL")

    result = ResearchResult(
        query=query, status=status, engine_used=engine,
        findings=findings, sources=sources, depth=depth, depth_achieved=depth,
        warnings=warnings, quarantined_count=quarantined, cost_usd=0.0,
    )
    result.attempts.append(EngineAttempt(
        engine,
        AttemptOutcome.ACTIVE if status != ResearchStatus.FAILED else AttemptOutcome.FAILED,
        detail=f"{len(findings)} findings · {len(sources)} sources (agent fan-out + Tavily)",
        sources_found=len(sources),
    ))
    result.recompute_aggregates()
    return result


# ---------------------------------------------------------------------------
# run_floor — the deterministic standalone floor (Tavily-only, writes directive)
# ---------------------------------------------------------------------------

def run_floor(query: str, depth: str = "standard", slug: Optional[str] = None,
              out_dir: Optional[Path] = None, env: Optional[dict] = None
              ) -> ResearchResult:
    """The deterministic floor: Tavily search → typed result, and write the
    agent fan-out directive so the result can be upgraded to full depth.

    Returns DEGRADED when Tavily produced sources (real, but un-fanned-out),
    FAILED only when nothing sourced could be found at all."""
    env = env or load_env_vars()
    slug = slug or "".join(c if c.isalnum() else "-" for c in query.lower())[:50].strip("-")
    out_dir = out_dir or (TMP / slug)
    out_dir.mkdir(parents=True, exist_ok=True)

    queries = decompose(query)
    findings, sources, dropped = tavily_floor(query, queries, env=env)

    # For standard+ depth, add Tavily's agentic cited REPORT — turns the floor
    # from snippets into a synthesized, ~15-20-source frontier-grade result.
    synthesis = ""
    used_research = False
    if depth in ("standard", "deep", "max"):
        model = "mini" if depth == "standard" else "auto"
        rr = tavily_research(query, model=model)
        if rr.get("content"):
            used_research = True
            synthesis = rr["content"]
            rf, rs, rq = research_to_findings(rr["content"], rr.get("sources", []))
            dropped += rq
            seen = {s.url for s in sources}
            for s in rs:
                if s.url not in seen:
                    seen.add(s.url); sources.append(s)
            fseen = {f.source_url for f in findings}
            for f in rf:
                if f.source_url not in fseen:
                    fseen.add(f.source_url); findings.append(f)

    directive = write_directive(query, depth, queries, sources, out_dir)

    warnings: List[str] = []
    if findings:
        status = ResearchStatus.DEGRADED
        if used_research:
            warnings.append(
                f"Tavily research+search floor ({len(sources)} sources, cited report). "
                f"Run the agent fan-out in {directive.name} → ingest for full swarm depth."
            )
        else:
            warnings.append(
                f"Tavily-only floor ({len(sources)} sources). Run the agent fan-out in "
                f"{directive.name} → ingest to reach REAL depth."
            )
        outcome = AttemptOutcome.ACTIVE
        detail = f"Tavily {len(sources)} sources" + (" + cited report" if used_research else " (fan-out pending)")
    else:
        status = ResearchStatus.FAILED
        warnings.append(
            "Tavily returned nothing (no key, rate-limit, or no hits). Run the agent "
            f"fan-out in {directive.name} → ingest to produce a result."
        )
        outcome = AttemptOutcome.FAILED
        detail = "Tavily empty — agent fan-out required"
    if dropped:
        warnings.append(f"{dropped} URL-less Tavily result(s) rejected")

    result = ResearchResult(
        query=query, status=status, engine_used=EngineKind.NATIVE,
        findings=findings, sources=sources, synthesis=synthesis, depth=depth,
        depth_achieved=depth, warnings=warnings, quarantined_count=dropped, cost_usd=0.0,
    )
    result.attempts.append(EngineAttempt(
        EngineKind.NATIVE, outcome, detail=detail, sources_found=len(sources)))
    result.recompute_aggregates()
    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cli() -> int:
    import argparse
    p = argparse.ArgumentParser(prog="native_floor.py")
    sub = p.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("floor", help="Run the deterministic Tavily floor + write the fan-out directive")
    f.add_argument("query")
    f.add_argument("--depth", default="standard", choices=["quick", "standard", "deep", "max"])
    f.add_argument("--slug", default=None)
    f.add_argument("--json", action="store_true")

    g = sub.add_parser("ingest", help="Ingest agent native-findings.jsonl → typed result")
    g.add_argument("--findings", required=True)
    g.add_argument("--query", required=True)
    g.add_argument("--depth", default="standard", choices=["quick", "standard", "deep", "max"])
    g.add_argument("--json", action="store_true")

    args = p.parse_args()
    if args.cmd == "floor":
        res = run_floor(args.query, depth=args.depth, slug=args.slug)
    else:
        res = ingest_findings(Path(args.findings), args.query, depth=args.depth)

    print(res.to_json() if args.json else res.render_receipt())
    return 0 if res.is_usable else 2


if __name__ == "__main__":
    raise SystemExit(_cli())
