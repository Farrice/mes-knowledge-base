#!/usr/bin/env python3
"""
Native Floor — the bedrock research engine that CANNOT break.

This is the floor every research request falls to when the paid accelerators
(Gemini Deep Research, Perplexity) are unavailable, fail, or aren't warranted.
It depends only on tools Claude always has, so it is always available at ~$0:

  • Python (deterministic, reliable):
      - Tavily search (API-credit metered; a free allowance may apply) → real sourced findings
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
import os as _os
import subprocess as _subprocess


TMP = ROOT / ".tmp" / "research"

# Depth floors now live in ONE place — execution/research_depth.py (the depth
# contract). The old local copies (deep=6 sources vs the protocol's 15) were how
# "deep" runs could legally be six Tavily snippets. Kept as module-level dicts
# for backward compatibility with existing importers.
try:
    from research_depth import DEPTH as _DEPTH_CONTRACT
except ImportError:
    from execution.research_depth import DEPTH as _DEPTH_CONTRACT

DEPTH_MIN_SOURCES = {d: c["sources"] for d, c in _DEPTH_CONTRACT.items()}
DEPTH_MIN_DOMAINS = {d: c["domains"] for d, c in _DEPTH_CONTRACT.items()}
DEPTH_EXTRACTS = {d: c["extracts"] for d, c in _DEPTH_CONTRACT.items()}


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
# Tavily — deterministic, reliable, and API-credit metered
# ---------------------------------------------------------------------------

def tavily_search(query: str, max_results: int = 6,
                  env: Optional[dict] = None, days: Optional[int] = None,
                  topic: Optional[str] = None,
                  search_depth: str = "advanced") -> List[Dict]:
    """Run one Tavily search. Returns raw results [{content,url,title}]. Never
    raises — on any failure returns [] so the floor degrades, never breaks.
    `days` + `topic="news"` enable Tavily's recency filter (news index only)."""
    env = env or load_env_vars()
    tk = env.get("TAVILY_API_KEY")
    if not tk:
        return []
    try:
        import requests
        depth = search_depth if search_depth in {"basic", "advanced"} else "advanced"
        payload = {"api_key": tk, "query": query, "max_results": max_results,
                   "search_depth": depth}
        if topic:
            payload["topic"] = topic
        if days:
            payload["days"] = days
        r = requests.post(
            "https://api.tavily.com/search",
            json=payload,
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
# Tavily RESEARCH + EXTRACT — credit-metered floor legs. Tavily Research is
# intentionally unavailable to Free-First Research Mission.
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
        # The tvly CLI reads TAVILY_API_KEY from the process environment, while
        # this workspace keeps it in the root .env. Search already receives the
        # parsed env explicitly; Extract used to omit this bridge and silently
        # return [] even with a valid key. Pass a child-only environment so the
        # key is neither printed nor exported globally.
        cli_env = _os.environ.copy()
        tavily_key = load_env_vars().get("TAVILY_API_KEY")
        if tavily_key and not cli_env.get("TAVILY_API_KEY"):
            cli_env["TAVILY_API_KEY"] = tavily_key
        cmd = ["tvly", "extract", *urls[:20], "--json", "--extract-depth", "basic", "--format", "markdown",
               "--timeout", str(timeout)]
        if query:
            cmd += ["--query", query, "--chunks-per-source", "3"]
        proc = _subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout + 30,
            env=cli_env,
        )
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

def _status_for(findings: List[Finding], sources: List[Source], depth: str,
                extracted_urls: Optional[set] = None
                ) -> Tuple[ResearchStatus, List[str]]:
    """Depth verdict. When `extracted_urls` is provided (the deterministic floor
    path), snippet-only sources count HALF toward the source floor — a claim
    built from a 400-char snippet is not the same evidence as a read page.
    Agent-fan-out ingest passes None (agents WebFetch full pages by contract)."""
    warnings: List[str] = []
    if not findings:
        return ResearchStatus.FAILED, ["no sourced findings — floor produced nothing usable"]
    urls = {f.source_url for f in findings} | {s.url for s in sources if s.url}
    domains = {Source(url=u).domain for u in urls if u}
    min_src = DEPTH_MIN_SOURCES.get(depth, 3)
    min_dom = DEPTH_MIN_DOMAINS.get(depth, 3)
    if extracted_urls is not None:
        full = {u for u in urls if u in extracted_urls}
        snippet_only = urls - full
        effective = len(full) + 0.5 * len(snippet_only)
        coverage_note = (f"{len(full)} full-page + {len(snippet_only)} snippet-only "
                         f"= {effective:.1f} effective sources")
    else:
        effective = float(len(urls))
        coverage_note = f"{len(urls)} sources"
    if effective >= min_src and len(domains) >= min_dom:
        return ResearchStatus.REAL, warnings
    warnings.append(
        f"thin coverage for depth={depth}: {coverage_note} / {len(domains)} domains "
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

    # FULL-PAGE EXTRACTION — the anti-snippet leg (2026-07-26 shallow-research
    # fix). tavily_extract sat here as dead code with zero callers while every
    # claim shipped as a 400-char snippet. Now the floor reads real pages: top
    # URLs (spread across domains, capped at tvly's 20/call) get extracted, and
    # each extracted page upgrades its finding's claim/excerpt to page content.
    extracted_urls: set = set()
    n_extract = DEPTH_EXTRACTS.get(depth, 0)
    if n_extract and sources:
        by_domain: Dict[str, List[str]] = {}
        for s in sources:
            if s.url:
                by_domain.setdefault(s.domain, []).append(s.url)
        picks: List[str] = []
        # round-robin across domains so extraction depth also buys domain spread
        while len(picks) < min(20, n_extract * max(3, len(by_domain))) and any(by_domain.values()):
            for dom in list(by_domain):
                if by_domain[dom]:
                    picks.append(by_domain[dom].pop(0))
                if len(picks) >= 20:
                    break
        pages = tavily_extract(picks, query=query)
        by_url = {f.source_url: f for f in findings}
        for pg in pages:
            content = (pg.get("raw_content") or "").strip().replace("\n", " ")
            if len(content) < 80:
                continue
            extracted_urls.add(pg["url"])
            try:
                upgraded = Finding(
                    claim=content[:400], source_url=pg["url"], excerpt=content[:300],
                    confidence="high", finding_type="data",
                )
            except Exception:
                continue
            if pg["url"] in by_url:
                findings[findings.index(by_url[pg["url"]])] = upgraded
            else:
                findings.append(upgraded)
                if pg["url"] not in {s.url for s in sources}:
                    sources.append(Source(url=pg["url"], title=pg.get("title", "")))

    directive = write_directive(query, depth, queries, sources, out_dir)

    warnings: List[str] = []
    if findings:
        status, status_warnings = _status_for(findings, sources, depth,
                                              extracted_urls=extracted_urls)
        warnings += status_warnings
        leg = "research+search" if used_research else "search"
        extract_note = (f", {len(extracted_urls)} full-page extract(s)"
                        if extracted_urls else ", 0 full-page extracts")
        if status == ResearchStatus.REAL:
            warnings.append(
                f"Tavily {leg} floor met the {depth} depth contract "
                f"({len(sources)} sources{extract_note})."
            )
        else:
            warnings.append(
                f"Tavily {leg} floor ({len(sources)} sources{extract_note}). Run the "
                f"agent fan-out in {directive.name} → ingest to reach REAL depth."
            )
        outcome = AttemptOutcome.ACTIVE
        detail = (f"Tavily {len(sources)} sources{extract_note}"
                  + (" + cited report" if used_research else ""))
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
