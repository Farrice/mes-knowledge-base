#!/usr/bin/env python3
"""
Buyer Trigger Research - source-backed research layer for /buyer-trigger-os.

Default behavior is public/free research through the native floor. Apify is
supported only as a guarded optional lane: preview by default, execute only when
explicitly requested and still capped by the existing Apify budget guard.

The script is deliberately conservative. It produces evidence, source ledgers,
and research-informed trigger hypotheses; it never fabricates current trends,
buyer language, or social-listening quotes when sources are missing.
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import parse_qs, quote_plus, unquote, urlencode, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
EXEC = ROOT / "execution"
sys.path.insert(0, str(EXEC))

try:
    from research_contract import (
        AttemptOutcome,
        EngineAttempt,
        EngineKind,
        Finding,
        ResearchResult,
        ResearchStatus,
        Source,
    )
    from native_floor import run_floor
except ImportError:  # pragma: no cover - package import fallback
    from execution.research_contract import (
        AttemptOutcome,
        EngineAttempt,
        EngineKind,
        Finding,
        ResearchResult,
        ResearchStatus,
        Source,
    )
    from execution.native_floor import run_floor


OUTPUT_ROOT = ROOT / "research_outputs" / "buyer-trigger-os"
TRIGGERS = [
    "identity_signal",
    "recognition_speed",
    "specificity",
    "social_currency",
    "familiar_twist",
    "emotion_first",
]
APIFY_DEFAULT_LANES = ["reddit"]
APIFY_DEFAULT_LIMIT = 20
APIFY_DEFAULT_RUN_CAP = 0.25
HARD_STOP_PCT = 0.90
RELEVANCE_STOPWORDS = {
    "about", "after", "apparel", "best", "brands", "bought", "buyer", "buyers",
    "comments", "community", "competitors", "current", "discussion", "frustrations",
    "language", "market", "marketplace", "people", "positioning", "product",
    "public", "reviews", "shirts", "slogans", "trends", "wear", "wish",
}


@dataclass
class EvidenceItem:
    id: str
    claim: str
    source_url: str
    source_title: str
    source_domain: str
    source_type: str
    evidence_status: str
    confidence: str
    excerpt: str
    recency: str
    mapped_trigger: str
    query_lane: str


@dataclass
class ApifyPlan:
    mode: str
    lanes: list[str]
    limit: int
    estimated_cost: float
    monthly_state: str
    spent_dollars: float
    remaining_dollars: float
    projected_spent: float
    per_run_cap: float
    executed: bool
    fallback: bool
    message: str
    result_count: int = 0


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def slugify(text: str, max_len: int = 72) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return (slug[:max_len].strip("-") or "buyer-trigger-research")


def clean_text(text: str, max_len: int = 420) -> str:
    text = re.sub(r"\s+", " ", (text or "")).strip()
    return text[:max_len].rstrip()


def domain_for(url: str) -> str:
    return urlparse(url).netloc.lower()


def source_type_for(url: str, lane: str = "") -> str:
    d = domain_for(url)
    lane = lane.lower()
    if "reddit" in d or "reddit" in lane:
        return "social_listening"
    if any(x in d for x in ["forum", "quora", "stackexchange", "discord"]):
        return "social_listening"
    if any(x in d for x in ["amazon", "etsy", "redbubble", "teepublic", "bonfire", "shopify"]):
        return "marketplace_or_review"
    if any(x in d for x in ["trends.google", "explodingtopics", "pinterest", "tiktok"]):
        return "trend_signal"
    if "competitor" in lane or "marketplace" in lane:
        return "competitor_or_marketplace"
    return "public_web"


def relevance_tokens(query: str) -> list[str]:
    return [
        token for token in re.findall(r"[a-z0-9]+", query.lower())
        if len(token) > 3 and token not in RELEVANCE_STOPWORDS
    ]


def is_relevant_result(query: str, row: dict[str, str]) -> bool:
    haystack = " ".join([row.get("title", ""), row.get("snippet", ""), row.get("url", "")]).lower()
    q = query.lower()
    if "swing dance" in q:
        return any(term in haystack for term in ["swing dance", "lindy", "balboa", "west coast swing", "dancer"])
    if "edm" in q or "rave" in q or " dj" in q or "djs" in q:
        return any(term in haystack for term in ["edm", "dj", "rave", "festival", "techno", "house music", "electronic dance"])
    tokens = relevance_tokens(query)
    if not tokens:
        return True
    matched = sum(1 for token in set(tokens) if token in haystack)
    return matched >= min(2, len(set(tokens)))


def map_trigger(claim: str, source_type: str, lane: str = "") -> str:
    text = f"{claim} {source_type} {lane}".lower()
    if source_type == "social_listening":
        if any(w in text for w in ["comment", "share", "reaction", "wear", "gift", "post"]):
            return "social_currency"
        return "identity_signal"
    if any(w in text for w in ["identity", "community", "culture", "belong", "fan", "people like"]):
        return "identity_signal"
    if any(w in text for w in ["quick", "recogn", "scroll", "thumbnail", "instant"]):
        return "recognition_speed"
    if any(w in text for w in ["specific", "niche", "scene", "subculture", "use case"]):
        return "specificity"
    if any(w in text for w in ["trend", "twist", "meme", "remix", "new take", "familiar"]):
        return "familiar_twist"
    if any(w in text for w in ["emotion", "feel", "love", "frustrat", "wish", "fear"]):
        return "emotion_first"
    return "specificity"


def build_query_plan(topic: str, mode: str) -> list[dict[str, str]]:
    topic = topic.strip()
    base = topic
    lower = topic.lower()
    if "swing dance" in lower:
        base = f"{topic} lindy hop balboa west coast swing dancers t-shirt apparel"
    elif "edm" in lower or "dj" in lower or "rave" in lower:
        base = f"{topic} DJs rave festival techno house streetwear apparel"
    plan = [
        {
            "lane": "market_context",
            "query": f"{base} current buyer trends public discussion reviews",
            "purpose": "Find current public evidence and category context.",
        },
        {
            "lane": "social_listening",
            "query": f"site:reddit.com {base} comments frustrations wish bought wear community",
            "purpose": "Find public community language and buyer scenes.",
        },
        {
            "lane": "marketplace_or_review",
            "query": f"{base} best sellers reviews Etsy Amazon apparel product",
            "purpose": "Find marketplace/review signals and product language.",
        },
        {
            "lane": "competitor_or_alternative",
            "query": f"{base} brands competitors product pages positioning",
            "purpose": "Find competitor and alternative positioning signals.",
        },
    ]
    if mode in {"generate", "score"}:
        plan.append({
            "lane": "concept_language",
            "query": f"{base} slogans inside jokes community language apparel",
            "purpose": "Find language that can become source-backed concept direction.",
        })
    if mode in {"transfer", "audit"}:
        plan.append({
            "lane": "purchase_intent",
            "query": f"{base} buyer objections purchase intent why people buy",
            "purpose": "Find purchase intent and resistance evidence.",
        })
    return plan


def unwrap_duckduckgo_url(href: str) -> str:
    href = html.unescape(href or "").strip()
    if not href:
        return ""
    parsed = urlparse(href)
    if "duckduckgo.com" in parsed.netloc and parsed.path.startswith("/l/"):
        target = parse_qs(parsed.query).get("uddg", [""])[0]
        return unquote(target)
    if href.startswith("//duckduckgo.com/l/"):
        parsed = urlparse("https:" + href)
        target = parse_qs(parsed.query).get("uddg", [""])[0]
        return unquote(target)
    return href


def unwrap_bing_url(href: str) -> str:
    href = html.unescape(href or "").strip()
    parsed = urlparse(href)
    if "bing.com" not in parsed.netloc:
        return href
    encoded = parse_qs(parsed.query).get("u", [""])[0]
    if not encoded:
        return href
    if encoded.startswith("a1"):
        encoded = encoded[2:]
    try:
        padded = encoded + "=" * (-len(encoded) % 4)
        return base64.urlsafe_b64decode(padded.encode()).decode("utf-8", errors="ignore")
    except Exception:
        return href


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    return clean_text(html.unescape(value), 500)


def public_html_search(query: str, max_results: int = 8) -> list[dict[str, str]]:
    """Free public web fallback using DuckDuckGo HTML results.

    This is not a deep research provider. It gives URL-backed snippets so the
    OS can avoid fabricating when Tavily is unavailable or quota-limited.
    """
    url = "https://duckduckgo.com/html/?" + urlencode({"q": query})
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        body = urlopen(req, timeout=30).read().decode("utf-8", errors="ignore")
    except Exception:
        return []

    matches = list(re.finditer(r'<a[^>]+class="result__a"[^>]+href="([^"]+)"[^>]*>(.*?)</a>', body, re.S))
    results: list[dict[str, str]] = []
    for i, match in enumerate(matches[:max_results * 2]):
        href = unwrap_duckduckgo_url(match.group(1))
        title = strip_tags(match.group(2))
        if not href or "duckduckgo.com" in domain_for(href) or not title:
            continue
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else min(len(body), start + 2200)
        segment = body[start:end]
        snippet_match = re.search(r'<a[^>]+class="result__snippet"[^>]*>(.*?)</a>|<div[^>]+class="result__snippet"[^>]*>(.*?)</div>', segment, re.S)
        snippet = strip_tags((snippet_match.group(1) or snippet_match.group(2)) if snippet_match else title)
        results.append({"url": href, "title": title, "snippet": snippet})
        if len(results) >= max_results:
            break
    return results


def jina_bing_search(query: str, max_results: int = 8) -> list[dict[str, str]]:
    url = "https://r.jina.ai/http://www.bing.com/search?q=" + quote_plus(query)
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        body = urlopen(req, timeout=45).read().decode("utf-8", errors="ignore")
    except Exception:
        return []
    if "Too Many Requests" in body and "About " not in body:
        return []
    pattern = re.compile(
        r"\n\d+\.\s+##\s+\[(.*?)\]\((https?://[^\)]+)\)\n\n(.*?)(?=\n\d+\.\s+##|\Z)",
        re.S,
    )
    results: list[dict[str, str]] = []
    for title_md, href, snippet_md in pattern.findall(body):
        href = unwrap_bing_url(href)
        if not href or "bing.com" in domain_for(href):
            continue
        title = clean_text(re.sub(r"[*_`\\[\\]]", "", title_md), 180)
        snippet = clean_text(re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", snippet_md), 420)
        snippet = clean_text(re.sub(r"[*_`#>-]+", " ", snippet), 420)
        if not title:
            continue
        results.append({"url": href, "title": title, "snippet": snippet or title})
        if len(results) >= max_results:
            break
    return results


def public_search_result(query: str, depth: str, lane: str, prior_warning: str = "") -> ResearchResult:
    findings: list[Finding] = []
    sources: list[Source] = []
    rows = public_html_search(query, max_results=8)
    fallback_label = "DuckDuckGo HTML"
    if not rows:
        rows = jina_bing_search(query, max_results=8)
        fallback_label = "Jina/Bing public search"

    for row in rows:
        if not is_relevant_result(query, row):
            continue
        claim = clean_text(f"{row['title']}. {row['snippet']}", 420)
        url = row["url"]
        try:
            findings.append(Finding(
                claim=claim,
                source_url=url,
                excerpt=clean_text(row["snippet"], 300),
                confidence="medium",
                finding_type="data",
            ))
            sources.append(Source(url=url, title=row["title"]))
        except Exception:
            continue

    status = ResearchStatus.REAL if findings else ResearchStatus.FAILED
    warnings = [f"native floor returned no sources; used {fallback_label} fallback"]
    if prior_warning:
        warnings.append(prior_warning)
    if not findings:
        warnings.append("public HTML fallback returned no source-backed results")
    res = ResearchResult(
        query=query,
        status=status,
        engine_used=EngineKind.NATIVE,
        findings=findings,
        sources=sources,
        synthesis=f"Public HTML fallback for buyer-trigger lane: {lane}",
        depth=depth,
        depth_achieved=depth,
        warnings=warnings,
    )
    res.recompute_aggregates()
    res.attempts.append(EngineAttempt(
        EngineKind.NATIVE,
        AttemptOutcome.SUCCESS if findings else AttemptOutcome.FAILED,
        detail=f"public HTML fallback {len(findings)} findings",
        sources_found=len(sources),
    ))
    return res


def reader_url_for(url: str) -> str:
    cleaned = re.sub(r"^https?://", "", url.strip())
    return "https://r.jina.ai/http://" + cleaned


def fetch_seed_url(url: str) -> dict[str, str]:
    try:
        body = urlopen(Request(reader_url_for(url), headers={"User-Agent": "Mozilla/5.0"}), timeout=45).read().decode("utf-8", errors="ignore")
    except Exception:
        return {}
    title_match = re.search(r"^Title:\s*(.+)$", body, re.M)
    content = body.split("Markdown Content:", 1)[-1] if "Markdown Content:" in body else body
    content = clean_text(re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", content), 700)
    block_signals = [
        "you've been blocked by network security",
        "verifying you're not a bot",
        "too many requests",
        "captcha",
        "confirm you're not a robot",
        "please log in",
    ]
    if any(signal in content.lower() for signal in block_signals):
        return {}
    return {
        "url": url,
        "title": clean_text(title_match.group(1), 180) if title_match else domain_for(url),
        "snippet": content,
    }


def seed_urls_to_evidence(urls: list[str], start_index: int) -> list[EvidenceItem]:
    evidence: list[EvidenceItem] = []
    for url in urls:
        row = fetch_seed_url(url)
        if not row or not row.get("snippet"):
            continue
        source_type = source_type_for(url, "seed_source")
        claim = clean_text(f"{row['title']}. {row['snippet']}", 420)
        evidence.append(EvidenceItem(
            id=f"E{start_index + len(evidence)}",
            claim=claim,
            source_url=url,
            source_title=row["title"],
            source_domain=domain_for(url),
            source_type=source_type,
            evidence_status="verified",
            confidence="medium",
            excerpt=clean_text(row["snippet"], 320),
            recency="unknown",
            mapped_trigger=map_trigger(claim, source_type, "seed_source"),
            query_lane="seed_source",
        ))
    return evidence


def seed_findings_to_evidence(values: list[str], start_index: int) -> list[EvidenceItem]:
    evidence: list[EvidenceItem] = []
    for raw in values:
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            continue
        url = str(obj.get("url") or "").strip()
        claim = clean_text(str(obj.get("claim") or obj.get("snippet") or ""), 420)
        if not url or not claim:
            continue
        source_type = str(obj.get("source_type") or source_type_for(url, "seed_finding"))
        title = clean_text(str(obj.get("title") or domain_for(url)), 180)
        evidence.append(EvidenceItem(
            id=f"E{start_index + len(evidence)}",
            claim=claim,
            source_url=url,
            source_title=title,
            source_domain=domain_for(url),
            source_type=source_type,
            evidence_status=str(obj.get("evidence_status") or "verified"),
            confidence=str(obj.get("confidence") or "medium"),
            excerpt=clean_text(str(obj.get("excerpt") or claim), 320),
            recency=str(obj.get("recency") or "search_snippet"),
            mapped_trigger=str(obj.get("mapped_trigger") or map_trigger(claim, source_type, "seed_finding")),
            query_lane="seed_finding",
        ))
    return evidence


def research_lane(query: str, depth: str, lane: str) -> ResearchResult:
    result = run_floor(query, depth=depth, slug=f"buyer-trigger-{slugify(lane + '-' + query, 50)}")
    if result.findings:
        return result
    prior_warning = "; ".join(result.warnings[:2])
    return public_search_result(query, depth, lane, prior_warning=prior_warning)


def evidence_from_result(
    result: ResearchResult,
    lane: str,
    start_index: int,
    max_items: int,
) -> list[EvidenceItem]:
    items: list[EvidenceItem] = []
    seen: set[str] = set()
    for finding in result.findings:
        url = (finding.source_url or "").strip()
        claim = clean_text(finding.claim)
        if not url or not claim:
            continue
        key = f"{url}|{claim[:90]}"
        if key in seen:
            continue
        seen.add(key)
        source_type = source_type_for(url, lane)
        items.append(EvidenceItem(
            id=f"E{start_index + len(items)}",
            claim=claim,
            source_url=url,
            source_title="",
            source_domain=domain_for(url),
            source_type=source_type,
            evidence_status="verified" if url else "unverified",
            confidence=getattr(finding, "confidence", "medium") or "medium",
            excerpt=clean_text(getattr(finding, "excerpt", "") or claim, 320),
            recency="unknown",
            mapped_trigger=map_trigger(claim, source_type, lane),
            query_lane=lane,
        ))
        if len(items) >= max_items:
            break
    return items


def merge_source_titles(items: list[EvidenceItem], sources: Iterable[Source]) -> None:
    titles = {s.url: s.title for s in sources if s.url and s.title}
    for item in items:
        item.source_title = titles.get(item.source_url, item.source_title)


def load_apify_client() -> Any:
    import apify_client  # type: ignore
    return apify_client


def apify_budget_snapshot(apify: Any) -> dict[str, Any]:
    apify.load_env()
    usage = apify.load_usage()
    state = apify.budget_state(usage)
    return {
        "usage": usage,
        "state": state,
        "spent": float(usage.get("spent_dollars", 0.0)),
        "plan": float(usage.get("plan_dollars", 0.0)),
        "remaining": round(float(usage.get("plan_dollars", 0.0)) - float(usage.get("spent_dollars", 0.0)), 4),
    }


def estimate_apify_cost(apify: Any, lanes: list[str], limit: int) -> float:
    total = 0.0
    for lane in lanes:
        actor = apify.ACTORS.get(lane)
        if actor:
            total += float(actor.get("cost_per_result", 0.0)) * limit
    return round(total, 4)


def apify_payload(lane: str, topic: str, limit: int) -> dict[str, Any]:
    if lane == "reddit":
        from urllib.parse import quote_plus
        return {
            "startUrls": [{"url": f"https://www.reddit.com/search/?q={quote_plus(topic)}&type=link&sort=relevance"}],
            "maxItems": limit,
            "scrollTimeout": 40,
            "skipComments": False,
            "skipUserPosts": False,
            "skipCommunity": False,
        }
    if lane == "youtube":
        return {"keywords": [topic], "maxItems": limit, "downloadSubtitles": False}
    if lane == "tiktok":
        return {"hashtags": [re.sub(r'[^A-Za-z0-9_]', '', topic)[:80] or "streetwear"], "resultsPerPage": limit}
    if lane == "instagram":
        return {"directUrls": [topic], "resultsType": "posts", "resultsLimit": limit, "onlyPostsNewerThan": "365 days"}
    if lane == "amazon":
        return {"categoryOrProductUrls": [{"url": f"https://www.amazon.com/s?k={topic.replace(' ', '+')}"}], "maxItemsPerStartUrl": limit}
    return {"query": topic, "maxResults": limit}


def apify_items_to_evidence(raw_items: list[dict[str, Any]], lane: str, start_index: int) -> list[EvidenceItem]:
    out: list[EvidenceItem] = []
    for obj in raw_items:
        url = str(obj.get("url") or obj.get("postUrl") or obj.get("link") or obj.get("pageUrl") or "").strip()
        title = clean_text(str(obj.get("title") or obj.get("caption") or obj.get("text") or obj.get("name") or ""), 180)
        body = clean_text(str(obj.get("body") or obj.get("text") or obj.get("description") or obj.get("caption") or title), 420)
        if not url or not body:
            continue
        source_type = source_type_for(url, lane)
        out.append(EvidenceItem(
            id=f"E{start_index + len(out)}",
            claim=body,
            source_url=url,
            source_title=title,
            source_domain=domain_for(url),
            source_type=source_type,
            evidence_status="verified",
            confidence="medium",
            excerpt=body,
            recency=str(obj.get("date") or obj.get("createdAt") or obj.get("timestamp") or "unknown"),
            mapped_trigger=map_trigger(body, source_type, lane),
            query_lane=f"apify_{lane}",
        ))
    return out


def maybe_run_apify(
    topic: str,
    mode: str,
    lanes: list[str],
    limit: int,
    per_run_cap: float,
    start_index: int,
) -> tuple[ApifyPlan, list[EvidenceItem]]:
    try:
        apify = load_apify_client()
        snap = apify_budget_snapshot(apify)
        estimate = estimate_apify_cost(apify, lanes, limit)
    except Exception as exc:
        return ApifyPlan(
            mode=mode, lanes=lanes, limit=limit, estimated_cost=0.0,
            monthly_state="unavailable", spent_dollars=0.0, remaining_dollars=0.0,
            projected_spent=0.0, per_run_cap=per_run_cap, executed=False,
            fallback=True, message=f"Apify unavailable: {type(exc).__name__}",
        ), []

    projected = round(snap["spent"] + estimate, 4)
    plan = ApifyPlan(
        mode=mode,
        lanes=lanes,
        limit=limit,
        estimated_cost=estimate,
        monthly_state=snap["state"],
        spent_dollars=round(snap["spent"], 4),
        remaining_dollars=round(snap["remaining"], 4),
        projected_spent=projected,
        per_run_cap=per_run_cap,
        executed=False,
        fallback=False,
        message="preview only; no Apify actor executed",
    )

    if mode != "execute":
        return plan, []
    if snap["state"] == "red":
        plan.fallback = True
        plan.message = "Apify skipped because monthly budget state is red."
        return plan, []
    if estimate > per_run_cap:
        plan.fallback = True
        plan.message = f"Apify skipped because estimated run cost ${estimate:.4f} exceeds per-run cap ${per_run_cap:.4f}."
        return plan, []
    if snap["plan"] and (projected / snap["plan"]) >= HARD_STOP_PCT:
        plan.fallback = True
        plan.message = "Apify skipped because projected monthly usage would cross the hard-stop threshold."
        return plan, []

    evidence: list[EvidenceItem] = []
    for lane in lanes:
        result = apify.run_actor(lane, apify_payload(lane, topic, limit), limit)
        if result.get("fallback"):
            plan.fallback = True
            plan.message = result.get("message", "Apify returned fallback.")
            continue
        lane_items = apify_items_to_evidence(result.get("items") or [], lane, start_index + len(evidence))
        evidence.extend(lane_items)
    plan.executed = True
    plan.result_count = len(evidence)
    if evidence:
        plan.message = f"Apify executed with {len(evidence)} source-backed item(s)."
    return plan, evidence


def fixture_result(kind: str, topic: str) -> tuple[list[EvidenceItem], list[dict[str, str]], str]:
    if kind == "empty":
        return [], [], "FAILED"
    if kind == "thin":
        return [
            EvidenceItem(
                id="E1",
                claim=f"A single source mentions {topic}, but coverage is too thin to support a buyer-trigger recommendation.",
                source_url="https://example.com/thin-buyer-signal",
                source_title="Thin buyer signal fixture",
                source_domain="example.com",
                source_type="public_web",
                evidence_status="directional",
                confidence="low",
                excerpt="One thin fixture source only.",
                recency="fixture",
                mapped_trigger="specificity",
                query_lane="fixture",
            )
        ], [{"lane": "fixture", "query": topic, "purpose": "Validation fixture."}], "DEGRADED"
    return [
        EvidenceItem(
            id="E1",
            claim=f"Public discussion around {topic} contains identity language that can be mapped to a buyer self-statement.",
            source_url="https://www.reddit.com/r/example/comments/source_backed_identity",
            source_title="Source-backed identity fixture",
            source_domain="www.reddit.com",
            source_type="social_listening",
            evidence_status="verified",
            confidence="medium",
            excerpt="Fixture social listening excerpt with source URL.",
            recency="fixture",
            mapped_trigger="identity_signal",
            query_lane="fixture_social",
        ),
        EvidenceItem(
            id="E2",
            claim=f"Marketplace language around {topic} suggests the concept needs specific scenes, not broad demographic labels.",
            source_url="https://www.etsy.com/listing/source-backed-marketplace",
            source_title="Source-backed marketplace fixture",
            source_domain="www.etsy.com",
            source_type="marketplace_or_review",
            evidence_status="verified",
            confidence="medium",
            excerpt="Fixture marketplace excerpt with source URL.",
            recency="fixture",
            mapped_trigger="specificity",
            query_lane="fixture_marketplace",
        ),
        EvidenceItem(
            id="E3",
            claim=f"Trend evidence around {topic} should be used only as directional input until validated against actual buyers.",
            source_url="https://trends.google.com/trends/explore?q=source-backed-trend",
            source_title="Source-backed trend fixture",
            source_domain="trends.google.com",
            source_type="trend_signal",
            evidence_status="verified",
            confidence="medium",
            excerpt="Fixture trend excerpt with source URL.",
            recency="fixture",
            mapped_trigger="familiar_twist",
            query_lane="fixture_trend",
        ),
        EvidenceItem(
            id="E4",
            claim=f"Competitor positioning around {topic} should be treated as source-backed category context, not proof of demand.",
            source_url="https://example.com/source-backed-competitor",
            source_title="Source-backed competitor fixture",
            source_domain="example.com",
            source_type="competitor_or_marketplace",
            evidence_status="verified",
            confidence="medium",
            excerpt="Fixture competitor excerpt with source URL.",
            recency="fixture",
            mapped_trigger="recognition_speed",
            query_lane="fixture_competitor",
        ),
        EvidenceItem(
            id="E5",
            claim=f"Review language around {topic} can reveal emotion-first reasons, but the quote context must stay attached.",
            source_url="https://example.org/source-backed-review",
            source_title="Source-backed review fixture",
            source_domain="example.org",
            source_type="marketplace_or_review",
            evidence_status="verified",
            confidence="medium",
            excerpt="Fixture review excerpt with source URL.",
            recency="fixture",
            mapped_trigger="emotion_first",
            query_lane="fixture_review",
        ),
    ], [{"lane": "fixture", "query": topic, "purpose": "Validation fixture."}], "REAL"


def run_research(args: argparse.Namespace) -> tuple[list[EvidenceItem], list[dict[str, str]], list[str], str, str]:
    if args.fixture:
        evidence, plan, status = fixture_result(args.fixture, args.topic)
        return evidence, plan, [], status, "fixture"

    query_plan = build_query_plan(args.topic, args.mode)
    evidence: list[EvidenceItem] = []
    receipts: list[str] = []
    result_statuses: list[str] = []

    if args.source_only:
        return [], query_plan, ["Source-only mode: live public research intentionally skipped."], "SOURCE_ONLY", "source_only"

    for entry in query_plan:
        result = research_lane(entry["query"], args.depth, entry["lane"])
        result_statuses.append(result.status.value if isinstance(result.status, ResearchStatus) else str(result.status))
        receipts.append(result.render_receipt())
        lane_items = evidence_from_result(result, entry["lane"], len(evidence) + 1, args.max_items_per_lane)
        merge_source_titles(lane_items, result.sources)
        evidence.extend(lane_items)

    if args.seed_url:
        query_plan.append({
            "lane": "seed_source",
            "query": ", ".join(args.seed_url),
            "purpose": "Codex web-search or user-provided source URLs ingested into the same evidence ledger.",
        })
        seed_evidence = seed_urls_to_evidence(args.seed_url, len(evidence) + 1)
        evidence.extend(seed_evidence)
        receipts.append(json.dumps({
            "seed_sources": {
                "requested": len(args.seed_url),
                "ingested": len(seed_evidence),
                "urls": args.seed_url,
            }
        }, indent=2))

    if args.seed_finding_json:
        query_plan.append({
            "lane": "seed_finding",
            "query": f"{len(args.seed_finding_json)} structured finding(s)",
            "purpose": "Codex web-search snippets or user-provided findings ingested with source URLs.",
        })
        seeded_findings = seed_findings_to_evidence(args.seed_finding_json, len(evidence) + 1)
        evidence.extend(seeded_findings)
        receipts.append(json.dumps({
            "seed_findings": {
                "requested": len(args.seed_finding_json),
                "ingested": len(seeded_findings),
            }
        }, indent=2))

    apify_plan, apify_evidence = maybe_run_apify(
        args.topic,
        args.apify,
        args.apify_lane or APIFY_DEFAULT_LANES,
        args.apify_limit,
        args.apify_run_cap,
        len(evidence) + 1,
    )
    evidence.extend(apify_evidence)
    receipts.append(json.dumps({"apify_plan": asdict(apify_plan)}, indent=2))

    unique_urls = {e.source_url for e in evidence if e.source_url}
    unique_domains = {e.source_domain for e in evidence if e.source_domain}
    social_count = sum(1 for e in evidence if e.source_type == "social_listening")
    enough_evidence = (
        len(unique_urls) >= args.min_sources
        and len(unique_domains) >= args.min_domains
        and social_count >= args.min_social_sources
    )
    seeded_evidence_present = bool(args.seed_url or args.seed_finding_json)
    if not evidence:
        status = "FAILED"
    elif not enough_evidence:
        status = "DEGRADED"
    elif "FAILED" in result_statuses and not seeded_evidence_present and len(unique_urls) < args.min_sources + 2:
        status = "DEGRADED"
    else:
        status = "REAL"
    return evidence, query_plan, receipts, status, "native_floor"


def source_rows(evidence: list[EvidenceItem]) -> list[EvidenceItem]:
    seen: set[str] = set()
    rows: list[EvidenceItem] = []
    for item in evidence:
        if item.source_url in seen:
            continue
        seen.add(item.source_url)
        rows.append(item)
    return rows


def trigger_counts(evidence: list[EvidenceItem]) -> dict[str, int]:
    counts = {trigger: 0 for trigger in TRIGGERS}
    for item in evidence:
        counts[item.mapped_trigger] = counts.get(item.mapped_trigger, 0) + 1
    return counts


def concept_rows(topic: str, mode: str, evidence: list[EvidenceItem]) -> list[dict[str, str]]:
    rows = []
    for item in evidence[:6]:
        buyer = f"Buyer researching or participating in {topic}"
        if item.source_type == "social_listening":
            buyer = f"Public community participant around {topic}"
        elif item.source_type == "marketplace_or_review":
            buyer = f"Marketplace buyer comparing {topic}"
        candidate = f"Research-backed {mode} direction from {item.id}"
        rows.append({
            "candidate": candidate,
            "target_buyer": buyer,
            "identity_signal": f"Use {item.id} to name the self-statement instead of a generic demographic.",
            "recognition_speed": "Needs a short, visible hook tied to the sourced language.",
            "specificity": f"Anchor to {item.query_lane}; avoid broad category wording.",
            "social_currency": "Use only if the sourced scene implies a reaction, share, gift, comment, or status moment.",
            "familiar_twist": "Pair the familiar category with the sourced unexpected buyer scene.",
            "emotion_first": "Lead with recognition, relief, pride, irritation, or belonging before rationale.",
            "risk": f"Research-informed hypothesis only; validate with buyers. Source: {item.id}",
            "revision": "Turn this into final creative only after preserving the source-backed buyer language.",
        })
    return rows


def write_source_ledger(out_dir: Path, evidence: list[EvidenceItem]) -> Path:
    lines = [
        "# Buyer Trigger Source Ledger",
        "",
        "| ID | Status | Type | Domain | URL | Trigger | Notes |",
        "|---|---|---|---|---|---|---|",
    ]
    if not evidence:
        lines.append("| S0 | unverified | none | none | none | none | No sources captured. |")
    for idx, item in enumerate(source_rows(evidence), 1):
        lines.append(
            f"| S{idx} | {item.evidence_status} | {item.source_type} | {item.source_domain} | "
            f"{item.source_url} | {item.mapped_trigger} | Evidence item {item.id}. |"
        )
    path = out_dir / "source_ledger.md"
    path.write_text("\n".join(lines) + "\n")
    return path


def write_insight_ledger(out_dir: Path, evidence: list[EvidenceItem]) -> Path:
    lines = [
        "# Buyer Trigger Insight Ledger",
        "",
        "| Evidence | Claim | Source Type | Status | Confidence | Trigger | Source |",
        "|---|---|---|---|---|---|---|",
    ]
    if not evidence:
        lines.append("| none | No source-backed insight captured. | none | unverified | low | none | none |")
    for item in evidence:
        claim = item.claim.replace("|", "\\|")
        lines.append(
            f"| {item.id} | {claim} | {item.source_type} | {item.evidence_status} | "
            f"{item.confidence} | {item.mapped_trigger} | {item.source_url} |"
        )
    path = out_dir / "insight_ledger.md"
    path.write_text("\n".join(lines) + "\n")
    return path


def render_report(
    topic: str,
    mode: str,
    depth: str,
    evidence: list[EvidenceItem],
    query_plan: list[dict[str, str]],
    receipts: list[str],
    status: str,
    engine: str,
    source_ledger: Path,
    insight_ledger: Path,
    source_only: bool,
) -> str:
    counts = trigger_counts(evidence)
    social_count = sum(1 for e in evidence if e.source_type == "social_listening")
    source_count = len({e.source_url for e in evidence if e.source_url})
    domain_count = len({e.source_domain for e in evidence if e.source_domain})
    rows = concept_rows(topic, mode, evidence)

    def safe_receipt(receipt: str) -> str:
        cleaned: list[str] = []
        for line in receipt.splitlines():
            if line.strip().startswith("Provenance:"):
                cleaned.append("Source ledger: see Source Ledger and Insight Ledger for URL-backed evidence.")
            elif line.strip().startswith("Cost this run:"):
                cleaned.append("Cost this run: see execution receipt; no paid buyer-trigger provider was used by default.")
            else:
                cleaned.append(line)
        return "\n".join(cleaned)

    lines = [
        f"# Research-Backed Buyer Trigger OS: {topic}",
        "",
        "## Trigger Research Trace",
        f"- Topic: {topic}",
        f"- Mode: {mode}",
        f"- Depth: {depth}",
        f"- Status: {status}",
        f"- Engine lane: {engine}",
        f"- Source-only mode: {str(source_only).lower()}",
        f"- Source count: {source_count}",
        f"- Domain count: {domain_count}",
        f"- Social-listening source count: {social_count}",
        f"- Source Ledger: {source_ledger}",
        f"- Insight Ledger: {insight_ledger}",
        "",
        "## Research Receipt",
        "",
    ]
    if receipts:
        for i, receipt in enumerate(receipts, 1):
            lines.extend([f"### Receipt {i}", "", "```", safe_receipt(receipt).strip(), "```", ""])
    else:
        lines.append("- No live research receipt because source-only mode was selected.")
        lines.append("")

    lines.extend([
        "## Query Plan",
        "",
        "| Lane | Query | Purpose |",
        "|---|---|---|",
    ])
    for entry in query_plan:
        lines.append(f"| {entry['lane']} | {entry['query']} | {entry['purpose']} |")

    lines.extend([
        "",
        "## Insight Ledger",
        "",
        "| Evidence | Claim | Type | Status | Confidence | Trigger | Source |",
        "|---|---|---|---|---|---|---|",
    ])
    if evidence:
        for item in evidence:
            claim_cell = item.claim.replace('|', '\\|')
            lines.append(
                f"| {item.id} | {claim_cell} | {item.source_type} | "
                f"{item.evidence_status} | {item.confidence} | {item.mapped_trigger} | {item.source_url} |"
            )
    else:
        lines.append("| none | No source-backed insight captured. | none | unverified | low | none | none |")

    lines.extend([
        "",
        "## Meg Mechanics Used",
        "",
        "- Identity Signal: use evidence to name what the buyer says about themselves.",
        "- Recognition Speed: turn sourced buyer language into fast visual or headline recognition.",
        "- Specificity: replace broad market labels with sourced scenes, complaints, use cases, or self-statements.",
        "- Social Currency: use public/community evidence only when it shows a share, comment, gift, status, or reaction moment.",
        "- Familiar/Twist: pair the known category with a sourced non-obvious angle.",
        "- Emotion First: lead with the feeling suggested by evidence, then justify.",
        "",
        "## Live Evidence Used",
        "",
    ])
    if evidence:
        for item in evidence[:12]:
            lines.append(f"- {item.id}: {item.source_type} -> {item.mapped_trigger} -> {item.source_url}")
    else:
        lines.append("- None. Output must remain source-only or hypothesis-labeled.")

    lines.extend([
        "",
        "## Domain Extrapolation",
        "",
    ])
    if evidence:
        lines.append("- The table below is research-informed, not buyer-validated. Use it to create or revise concepts, then test with real buyers.")
    else:
        lines.append("- No live market extrapolation is allowed because no source-backed evidence was captured.")

    lines.extend([
        "",
        "## Trigger Fit Table",
        "",
        "| Candidate | Target Buyer | Identity Signal | Recognition Speed | Specificity | Social Currency Moment | Familiar/Twist Pair | Emotion-First Reason | Risk | Revision |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ])
    if rows:
        for row in rows:
            lines.append(
                f"| {row['candidate']} | {row['target_buyer']} | {row['identity_signal']} | "
                f"{row['recognition_speed']} | {row['specificity']} | {row['social_currency']} | "
                f"{row['familiar_twist']} | {row['emotion_first']} | {row['risk']} | {row['revision']} |"
            )
    else:
        lines.append("| No candidate | No source-backed buyer | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | Research failed or source-only. | Run public research or provide buyer evidence. |")

    weakest = min(counts, key=lambda k: counts.get(k, 0)) if evidence else "all_triggers"
    lines.extend([
        "",
        "## Evidence Gaps / Risks",
        f"- Weakest evidence trigger: {weakest}",
        f"- Status handling: {status}. Treat DEGRADED as useful but not final. Treat FAILED as no live-research output.",
        "- Current trend, buyer-language, competitor, pricing, and social-listening claims must remain URL-backed.",
        "- Direct quotes should not be used unless the source URL and quote context are preserved next to the quote.",
        "",
    ])
    return "\n".join(lines)


def write_outputs(args: argparse.Namespace, evidence: list[EvidenceItem], query_plan: list[dict[str, str]], receipts: list[str], status: str, engine: str) -> Path:
    date = datetime.now().strftime("%Y-%m-%d")
    out_dir = Path(args.output_root) / f"{date}-{slugify(args.topic)}-{args.mode}"
    out_dir.mkdir(parents=True, exist_ok=True)

    source_ledger = write_source_ledger(out_dir, evidence)
    insight_ledger = write_insight_ledger(out_dir, evidence)
    report = render_report(
        args.topic,
        args.mode,
        args.depth,
        evidence,
        query_plan,
        receipts,
        status,
        engine,
        source_ledger,
        insight_ledger,
        args.source_only,
    )
    report_path = out_dir / "buyer_trigger_research_report.md"
    report_path.write_text(report + "\n")
    metadata = {
        "schema": "buyer-trigger-research/v1",
        "topic": args.topic,
        "mode": args.mode,
        "depth": args.depth,
        "status": status,
        "engine": engine,
        "source_count": len({e.source_url for e in evidence if e.source_url}),
        "domain_count": len({e.source_domain for e in evidence if e.source_domain}),
        "social_listening_count": sum(1 for e in evidence if e.source_type == "social_listening"),
        "created_at": now_iso(),
        "userFacingSurface": "rendered-conversation-document",
        "sourceRole": "persistence-copy",
        "externalExportRequested": False,
        "files": {
            "report": str(report_path),
            "source_ledger": str(source_ledger),
            "insight_ledger": str(insight_ledger),
        },
    }
    (out_dir / "buyer_trigger_research_report.metadata.json").write_text(json.dumps(metadata, indent=2))
    (out_dir / "evidence.json").write_text(json.dumps([asdict(e) for e in evidence], indent=2))
    (out_dir / "query_plan.json").write_text(json.dumps(query_plan, indent=2))
    return report_path


def run_guards(report_path: Path, source_ledger: Path) -> dict[str, Any]:
    results: dict[str, Any] = {}
    qg = [
        sys.executable,
        str(EXEC / "research_quality_gate.py"),
        "validate",
        str(report_path),
        "--source-ledger",
        str(source_ledger),
    ]
    gg = [
        sys.executable,
        str(EXEC / "grounding_guard.py"),
        str(report_path),
        "--task-type",
        "Research",
    ]
    for label, cmd in [("research_quality_gate", qg), ("grounding_guard", gg)]:
        proc = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, timeout=120)
        results[label] = {
            "returncode": proc.returncode,
            "stdout": proc.stdout[-4000:],
            "stderr": proc.stderr[-1000:],
        }
    return results


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run source-backed buyer-trigger research.")
    p.add_argument("topic")
    p.add_argument("--mode", choices=["research", "audit", "generate", "score", "transfer"], default="research")
    p.add_argument("--depth", choices=["quick", "standard", "deep", "max"], default="standard")
    p.add_argument("--source-only", action="store_true", help="Skip live research; preserve Meg/source-only mode.")
    p.add_argument("--apify", choices=["off", "preview", "execute"], default="preview")
    p.add_argument("--apify-lane", action="append", choices=["reddit", "youtube", "tiktok", "instagram", "amazon", "web"], default=[])
    p.add_argument("--apify-limit", type=int, default=APIFY_DEFAULT_LIMIT)
    p.add_argument("--apify-run-cap", type=float, default=APIFY_DEFAULT_RUN_CAP)
    p.add_argument("--max-items-per-lane", type=int, default=5)
    p.add_argument("--min-sources", type=int, default=5)
    p.add_argument("--min-domains", type=int, default=3)
    p.add_argument("--min-social-sources", type=int, default=1)
    p.add_argument("--output-root", default=str(OUTPUT_ROOT))
    p.add_argument("--seed-url", action="append", default=[], help="Source URL found by Codex web search or provided by the user; fetched through the public reader and added to the evidence ledger.")
    p.add_argument("--seed-finding-json", action="append", default=[], help="JSON object with url, claim/snippet, optional title/source_type/confidence. Used for Codex web-search snippets when the source page blocks readers.")
    p.add_argument("--fixture", choices=["ok", "thin", "empty"], default="", help="Validation fixture; does not run live research.")
    p.add_argument("--run-guards", action="store_true")
    p.add_argument("--json", action="store_true")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    evidence, query_plan, receipts, status, engine = run_research(args)
    report_path = write_outputs(args, evidence, query_plan, receipts, status, engine)
    source_ledger = report_path.parent / "source_ledger.md"
    guard_results = run_guards(report_path, source_ledger) if args.run_guards else {}
    payload = {
        "status": status,
        "report": str(report_path),
        "source_ledger": str(source_ledger),
        "insight_ledger": str(report_path.parent / "insight_ledger.md"),
        "source_count": len({e.source_url for e in evidence if e.source_url}),
        "domain_count": len({e.source_domain for e in evidence if e.source_domain}),
        "social_listening_count": sum(1 for e in evidence if e.source_type == "social_listening"),
        "guard_results": guard_results,
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"Buyer trigger research report: {report_path}")
        print(f"Status: {status}")
        print(f"Sources: {payload['source_count']} | Domains: {payload['domain_count']} | Social: {payload['social_listening_count']}")
    return 0 if status in {"REAL", "DEGRADED", "SOURCE_ONLY"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
