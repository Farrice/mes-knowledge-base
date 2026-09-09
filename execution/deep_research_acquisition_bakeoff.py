#!/usr/bin/env python3
"""Zero-dollar acquisition bakeoff for the existing Deep Research OS.

This is an evaluation harness, not a research command or scraper product. It
compares two public, no-account acquisition paths over a fixed URL fixture:

1. direct HTTP using Python's standard library;
2. Jina Reader's public URL-prefix endpoint.

It stores only acquisition metadata, hashes, short excerpts, and quality
signals. Raw page bodies are intentionally not persisted.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import ipaddress
import json
import re
import socket
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FIXTURE = (
    ROOT
    / "execution"
    / "fixtures"
    / "research-acquisition-bakeoff"
    / "health-performance-30.json"
)
USER_AGENT = "Mozilla/5.0 (compatible; AntigravityResearchBakeoff/1.0; public research)"
BLOCK_MARKERS = (
    "access denied",
    "target url returned error",
    "blocked by network security",
    "verify you are human",
    "temporarily blocked",
    "request unsuccessful",
    "enable javascript and cookies",
    "security check",
)
STATUS_ORDER = {"PASS": 0, "PARTIAL": 1, "BLOCKED": 2, "FAIL": 3}


class VisibleTextParser(HTMLParser):
    """Small stdlib HTML-to-text extractor for benchmark scoring only."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._hidden = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in {"script", "style", "noscript", "svg", "template"}:
            self._hidden += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"script", "style", "noscript", "svg", "template"}:
            self._hidden = max(0, self._hidden - 1)

    def handle_data(self, data: str) -> None:
        if not self._hidden:
            cleaned = " ".join(data.split())
            if cleaned:
                self.parts.append(cleaned)

    def text(self) -> str:
        return " ".join(self.parts)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def is_public_http_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        return False
    host = parsed.hostname.lower()
    if host in {"localhost", "localhost.localdomain"} or host.endswith(".local"):
        return False
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        return True
    return not (
        address.is_private
        or address.is_loopback
        or address.is_link_local
        or address.is_reserved
        or address.is_multicast
    )


def load_fixture(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    urls = data.get("urls")
    if not isinstance(urls, list):
        raise ValueError("fixture must contain a urls list")
    if len(urls) != 30:
        raise ValueError(f"fixture must contain exactly 30 URLs; found {len(urls)}")
    ids = [row.get("id") for row in urls]
    values = [row.get("url") for row in urls]
    if len(set(ids)) != len(ids):
        raise ValueError("fixture contains duplicate ids")
    if len(set(values)) != len(values):
        raise ValueError("fixture contains duplicate URLs")
    for row in urls:
        if not is_public_http_url(str(row.get("url", ""))):
            raise ValueError(f"fixture contains non-public URL: {row.get('url')}")
        if not row.get("class") or not isinstance(row.get("expected_tokens"), list):
            raise ValueError(f"fixture row missing class or expected_tokens: {row.get('id')}")
    return data


def reader_url(url: str) -> str:
    return f"https://r.jina.ai/{url}"


def normalize_text(body: bytes, content_type: str) -> tuple[str, bool]:
    is_pdf = body.startswith(b"%PDF") or "application/pdf" in content_type.lower()
    if is_pdf:
        return "", True
    charset = "utf-8"
    match = re.search(r"charset=([^;\s]+)", content_type, re.I)
    if match:
        charset = match.group(1).strip('"\'')
    text = body.decode(charset, errors="replace")
    if "html" in content_type.lower() or "<html" in text[:1000].lower():
        parser = VisibleTextParser()
        try:
            parser.feed(text)
            text = parser.text()
        except Exception:
            text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return " ".join(text.split()), False


def method_content(text: str, method: str) -> str:
    """Remove transport metadata before measuring recovered source content."""
    if method == "jina_reader" and "Markdown Content:" in text:
        return text.split("Markdown Content:", 1)[1].strip()
    return text


def classify(
    *,
    http_status: int | None,
    text: str,
    body: bytes,
    is_pdf: bool,
    expected_tokens: list[str],
    error: str,
) -> tuple[str, list[str], str]:
    lowered = text.lower()
    marker = next((item for item in BLOCK_MARKERS if item in lowered[:12000]), "")
    hits = [token for token in expected_tokens if token.lower() in lowered]
    if http_status in {401, 403, 407, 429} or marker:
        return "BLOCKED", hits, marker or f"http_{http_status}"
    if error or http_status is None or http_status >= 400:
        return "FAIL", hits, ""
    if is_pdf:
        return ("PASS" if len(body) >= 10_000 else "PARTIAL"), hits, ""
    if len(text) < 100:
        return "FAIL", hits, ""
    if len(text) < 500:
        return "PARTIAL", hits, ""
    if expected_tokens and not hits:
        return "PARTIAL", hits, ""
    return "PASS", hits, ""


def fetch_once(
    row: dict[str, Any],
    method: str,
    timeout: float,
    max_bytes: int,
) -> dict[str, Any]:
    source_url = row["url"]
    target_url = source_url if method == "direct_http" else reader_url(source_url)
    headers = {"User-Agent": USER_AGENT, "Accept": "text/markdown,text/html,application/pdf,*/*"}
    started = time.monotonic()
    http_status: int | None = None
    final_url = ""
    content_type = ""
    body = b""
    error = ""
    truncated = False
    try:
        request = Request(target_url, headers=headers)
        with urlopen(request, timeout=timeout) as response:
            http_status = int(response.status)
            final_url = response.geturl()
            content_type = response.headers.get("Content-Type", "")
            body = response.read(max_bytes + 1)
            if len(body) > max_bytes:
                body = body[:max_bytes]
                truncated = True
    except HTTPError as exc:
        http_status = int(exc.code)
        final_url = exc.geturl()
        content_type = exc.headers.get("Content-Type", "") if exc.headers else ""
        try:
            body = exc.read(min(max_bytes, 128_000))
        except Exception:
            body = b""
        error = f"HTTPError: {exc.code}"
    except (URLError, TimeoutError, socket.timeout, OSError) as exc:
        error = f"{type(exc).__name__}: {str(exc)[:180]}"
    except Exception as exc:  # defensive receipt; never fabricate a successful fetch
        error = f"{type(exc).__name__}: {str(exc)[:180]}"

    text, is_pdf = normalize_text(body, content_type)
    text = method_content(text, method)
    status, hits, blocked_marker = classify(
        http_status=http_status,
        text=text,
        body=body,
        is_pdf=is_pdf,
        expected_tokens=row["expected_tokens"],
        error=error,
    )
    elapsed_ms = int((time.monotonic() - started) * 1000)
    return {
        "id": row["id"],
        "class": row["class"],
        "source_url": source_url,
        "method": method,
        "status": status,
        "http_status": http_status,
        "final_url": final_url,
        "content_type": content_type,
        "bytes": len(body),
        "text_chars": len(text),
        "word_count": len(text.split()),
        "expected_tokens": row["expected_tokens"],
        "expected_hits": hits,
        "expected_hit_ratio": round(len(hits) / max(1, len(row["expected_tokens"])), 2),
        "blocked_marker": blocked_marker,
        "truncated": truncated,
        "elapsed_ms": elapsed_ms,
        "sha256": hashlib.sha256(body).hexdigest() if body else "",
        "excerpt": text[:300],
        "error": error,
        "cost_usd": 0.0,
        "retrieved_at": utc_now(),
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_method: dict[str, Counter[str]] = defaultdict(Counter)
    by_class_method: dict[str, dict[str, Counter[str]]] = defaultdict(
        lambda: defaultdict(Counter)
    )
    latency: dict[str, list[int]] = defaultdict(list)
    for row in rows:
        by_method[row["method"]][row["status"]] += 1
        by_class_method[row["class"]][row["method"]][row["status"]] += 1
        latency[row["method"]].append(row["elapsed_ms"])
    return {
        "methods": {
            method: {
                "counts": dict(counts),
                "usable": counts["PASS"] + counts["PARTIAL"],
                "pass_rate": round(counts["PASS"] / max(1, sum(counts.values())), 3),
                "usable_rate": round(
                    (counts["PASS"] + counts["PARTIAL"]) / max(1, sum(counts.values())), 3
                ),
                "median_latency_ms": sorted(latency[method])[len(latency[method]) // 2],
                "cost_usd": 0.0,
            }
            for method, counts in by_method.items()
        },
        "classes": {
            source_class: {
                method: dict(counts) for method, counts in methods.items()
            }
            for source_class, methods in by_class_method.items()
        },
    }


def status_cell(row: dict[str, Any]) -> str:
    detail = str(row.get("http_status") or row.get("blocked_marker") or "-")
    return f"{row['status']} ({detail})"


def render_markdown(
    fixture: dict[str, Any],
    rows: list[dict[str, Any]],
    summary: dict[str, Any],
) -> str:
    grouped: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    for row in rows:
        grouped[row["id"]][row["method"]] = row

    lines = [
        "# Free-First Research Acquisition Bakeoff",
        "",
        f"- Fixture: `{fixture['name']}`",
        f"- URLs: {len(fixture['urls'])}",
        "- Paid calls: 0",
        "- Accounts created: 0",
        "- Methods: direct public HTTP; Jina Reader public no-key endpoint",
        "- Raw page bodies persisted: no",
        "- Tavily: NOT RUN — account overage boundary not independently verified",
        "",
        "## Method Summary",
        "",
        "| Method | PASS | PARTIAL | BLOCKED | FAIL | Usable rate | Median latency | Cost |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for method, stats in summary["methods"].items():
        counts = stats["counts"]
        lines.append(
            f"| {method} | {counts.get('PASS', 0)} | {counts.get('PARTIAL', 0)} | "
            f"{counts.get('BLOCKED', 0)} | {counts.get('FAIL', 0)} | "
            f"{stats['usable_rate']:.0%} | {stats['median_latency_ms']} ms | $0.00 |"
        )

    lines.extend(
        [
            "",
            "## Evidence Matrix",
            "",
            "PASS means usable content and at least one expected signal (or a valid PDF payload). "
            "PARTIAL means content arrived but was thin or missed the expected signal. BLOCKED and "
            "FAIL remain failures; the harness performs no CAPTCHA or authentication escalation.",
            "",
            "| ID | Class | Domain | Direct HTTP | Jina Reader | Better zero-dollar path |",
            "|---|---|---|---|---|---|",
        ]
    )
    for fixture_row in fixture["urls"]:
        direct = grouped[fixture_row["id"]]["direct_http"]
        jina = grouped[fixture_row["id"]]["jina_reader"]
        direct_rank = STATUS_ORDER[direct["status"]]
        jina_rank = STATUS_ORDER[jina["status"]]
        if direct["status"] not in {"PASS", "PARTIAL"} and jina["status"] not in {
            "PASS",
            "PARTIAL",
        }:
            better = "none - use native web or mark gap"
        elif direct_rank < jina_rank:
            better = "direct_http"
        elif jina_rank < direct_rank:
            better = "jina_reader"
        elif direct["text_chars"] >= jina["text_chars"]:
            better = "direct_http (tie)"
        else:
            better = "jina_reader (tie)"
        domain = urlparse(fixture_row["url"]).netloc
        lines.append(
            f"| {fixture_row['id']} | {fixture_row['class']} | {domain} | "
            f"{status_cell(direct)} | {status_cell(jina)} | {better} |"
        )

    lines.extend(["", "## Class Breakdown", ""])
    for source_class, methods in sorted(summary["classes"].items()):
        lines.append(f"### {source_class}")
        lines.append("")
        for method, counts in sorted(methods.items()):
            rendered = ", ".join(
                f"{label}={counts.get(label, 0)}" for label in ("PASS", "PARTIAL", "BLOCKED", "FAIL")
            )
            lines.append(f"- `{method}`: {rendered}")
        lines.append("")

    lines.extend(
        [
            "## Boundary Receipt",
            "",
            "- Public URLs only.",
            "- No login, cookies, private data, contact enrichment, CAPTCHA solving, or proxy rotation.",
            "- No paid provider, new dependency, API key, account, scheduler, or background worker.",
            "- This matrix measures acquisition, not truth. Evidence promotion still requires source and claim review.",
        ]
    )
    return "\n".join(lines) + "\n"


def self_test(fixture: dict[str, Any]) -> None:
    assert len(fixture["urls"]) == 30
    html_sample = b"<html><body><h1>Health Products Compliance Guidance</h1><script>x</script></body></html>"
    text, is_pdf = normalize_text(html_sample, "text/html; charset=utf-8")
    assert not is_pdf and "Health Products" in text and "x" not in text
    status, hits, marker = classify(
        http_status=200,
        text=text * 20,
        body=html_sample,
        is_pdf=False,
        expected_tokens=["Health Products"],
        error="",
    )
    assert status == "PASS" and hits == ["Health Products"] and not marker
    blocked, _, marker = classify(
        http_status=403,
        text="verify you are human",
        body=b"blocked",
        is_pdf=False,
        expected_tokens=[],
        error="HTTPError: 403",
    )
    assert blocked == "BLOCKED" and marker
    jina_error = method_content(
        "URL Source: https://reddit.com/r/test/creatine "
        "Warning: Target URL returned error 403: Forbidden Markdown Content: "
        "Blocked by network security.",
        "jina_reader",
    )
    blocked, hits, marker = classify(
        http_status=200,
        text=jina_error,
        body=jina_error.encode(),
        is_pdf=False,
        expected_tokens=["creatine"],
        error="",
    )
    assert blocked == "BLOCKED" and not hits and marker

    failed_direct = {"status": "FAIL", "text_chars": 30}
    blocked_jina = {"status": "BLOCKED", "text_chars": 300}
    assert failed_direct["status"] not in {"PASS", "PARTIAL"}
    assert blocked_jina["status"] not in {"PASS", "PARTIAL"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--timeout", type=float, default=25.0)
    parser.add_argument("--max-bytes", type=int, default=5_000_000)
    parser.add_argument("--delay-ms", type=int, default=200)
    parser.add_argument("--self-test-only", action="store_true")
    args = parser.parse_args()

    fixture = load_fixture(args.fixture)
    self_test(fixture)
    if args.self_test_only:
        print("PASS: fixture and zero-dollar acquisition classifiers")
        return 0

    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    for fixture_row in fixture["urls"]:
        for method in ("direct_http", "jina_reader"):
            result = fetch_once(fixture_row, method, args.timeout, args.max_bytes)
            rows.append(result)
            print(
                f"{result['id']} {method} {result['status']} "
                f"http={result['http_status']} chars={result['text_chars']}"
            )
            time.sleep(max(0, args.delay_ms) / 1000)

    summary = summarize(rows)
    payload = {
        "schema_version": "deep-research-acquisition-bakeoff/v1",
        "generated_at": utc_now(),
        "fixture": fixture,
        "summary": summary,
        "rows": rows,
        "boundary": {
            "paid_calls": 0,
            "accounts_created": 0,
            "new_dependencies": 0,
            "authenticated_scraping": False,
            "raw_bodies_persisted": False,
        },
    }
    json_path = output_dir / "evidence-matrix.json"
    md_path = output_dir / "evidence-matrix.md"
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(fixture, rows, summary), encoding="utf-8")
    print(json.dumps({"json": str(json_path), "markdown": str(md_path), "summary": summary}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
