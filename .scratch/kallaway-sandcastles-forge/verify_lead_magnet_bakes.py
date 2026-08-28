#!/usr/bin/env python3
"""Fixture tests for execution/build_lead_magnet.py — plain, degraded, enriched,
and excluded bakes. $0, offline, deterministic. Run from repo root:

    .venv/bin/python3 .scratch/kallaway-sandcastles-forge/verify_lead_magnet_bakes.py

Contracts under test (post cold-read fix, 2026-08-28):
- Plain-language floor: no raw taxonomy token (hook_format keys, desire_template
  names, topic trigrams) in the visible page — the mapping layer translates known
  keys and falls back to plain phrasing for unknown ones (the fixture pack uses
  deliberately unknown keys to exercise the fallback).
- Pattern block: one plainly-worded WHY-it-broke-pattern line per top video,
  derived from hook_text/format_hint.
- Topic rows render only for clusters (video_count >= 2), displayed via a real
  video title (example_title), never the topic key. 1-video rows never render.
- --exclude skips ids and backfills from next-ranked rows; excluded_ids lands in
  DATA_JSON and the receipt. No exclude -> no key (byte-identical behavior).
- Enrichment: at most 2 sourced nuggets ONLY when the pack carries enrichment.
- Degraded pack -> interview-only variant, no fabricated numbers.
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIX = ROOT / ".scratch" / "kallaway-sandcastles-forge"
PY = str(ROOT / ".venv" / "bin" / "python3")

# The fixture pack's internal taxonomy vocabulary — none of it may reach the
# visible page (DATA_JSON island excluded; it is data, not prose).
FIXTURE_TAXONOMY_TOKENS = [
    "receipt-confession", "replacement-claim", "contrarian-take",
    "template-giveaway", "self-experiment", "meta-test",
    "insider proof", "less effort, same result", "permission to simplify",
    "steal my exact asset", "vicarious proof",
]

RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    print(f"  {'PASS' if ok else 'FAIL'} — {name}" + (f" ({detail})" if detail and not ok else ""))


def bake(pack, out, extra=()):
    proc = subprocess.run(
        [PY, str(ROOT / "execution" / "build_lead_magnet.py"),
         "--pack", str(pack), "--niche-label", "FIXTURE — Fitness coaches on YouTube",
         "--cta-url", "https://example.com/blueprint", "--out", str(out), *extra],
        capture_output=True, text=True, cwd=str(ROOT))
    return proc, Path(out).read_text(encoding="utf-8") if Path(out).exists() else ""


def data_json(html):
    m = re.search(r'<script id="mini-data" type="application/json">(.*?)</script>', html, re.S)
    return json.loads(m.group(1)) if m else {}


def visible(html):
    """Page minus the DATA_JSON island — what a reader can actually see."""
    return re.sub(r'<script id="mini-data" type="application/json">.*?</script>', "", html, flags=re.S)


def main():
    tmp = Path(tempfile.mkdtemp(prefix="lm-bakes-"))

    print("[plain bake — fixture-pack.json]")
    proc, html = bake(FIX / "fixture-pack.json", tmp / "plain.html")
    mini = data_json(html)
    vis = visible(html)
    check("plain: exit 0", proc.returncode == 0, proc.stderr[-200:])
    check("plain: mode=full receipt", "mode=full" in proc.stdout)
    check("plain: 5 videos", len(mini.get("videos", [])) == 5)
    check("plain: every video carries a why line",
          all(isinstance(v.get("why"), str) and v["why"] for v in mini.get("videos", [])))
    check("plain: pattern block rendered once with 5 why rows",
          html.count('data-block="pattern"') == 1 and html.count('class="why-row"') == 5)
    check("plain: topics are clusters only (>=2 videos), with example titles",
          len(mini.get("topics", [])) == 2
          and all(t.get("video_count", 0) >= 2 and t.get("example_title") for t in mini.get("topics", [])))
    check("plain: topic rows display real titles, never 1-video rows",
          html.count('class="topic-row"') == 2 and "1 video" not in vis
          and "The theme behind" in vis)
    check("plain: whitespace present", bool(mini.get("whitespace")))
    check("plain: whitespace speaks founder language",
          "A founder&#x27;s move here" in vis or "A founder's move here" in vis)
    check("plain: no taxonomy token reaches the visible page",
          not [t for t in FIXTURE_TAXONOMY_TOKENS if t in vis],
          str([t for t in FIXTURE_TAXONOMY_TOKENS if t in vis]))
    check("plain: topic keys stay out of the visible page",
          not [t["topic"] for t in mini.get("topics", []) if t["topic"] in vis])
    check("plain: NO market-signal block", 'data-block="market-signal"' not in html)
    check("plain: NO enrichment_nuggets key", "enrichment_nuggets" not in mini)
    check("plain: NO excluded_ids key without --exclude", "excluded_ids" not in mini)
    check("plain: NO enrichment bit in receipt", "enrichment_nuggets=" not in proc.stdout)
    check("plain: no unreplaced placeholders", not re.findall(r"\{\{[A-Z_]+\}\}", html))
    check("plain: template orders the pattern block", '"pattern"' in html)

    print("[excluded bake — fixture-pack.json --exclude fixA00001]")
    proc, html = bake(FIX / "fixture-pack.json", tmp / "excl.html", extra=("--exclude", "fixA00001"))
    mini = data_json(html)
    ids = [v.get("video_id") for v in mini.get("videos", [])]
    check("exclude: exit 0", proc.returncode == 0, proc.stderr[-200:])
    check("exclude: excluded id skipped", "fixA00001" not in ids)
    check("exclude: still 5 videos, next-ranked backfilled",
          len(ids) == 5 and "fixC00006" in ids)
    check("exclude: excluded_ids recorded in DATA_JSON", mini.get("excluded_ids") == ["fixA00001"])
    check("exclude: receipt says excluded=1/1", "excluded=1/1" in proc.stdout)
    check("exclude: cluster example title prefers a non-excluded video",
          any("retention email" in (t.get("example_title") or "") for t in mini.get("topics", [])))
    proc, html = bake(FIX / "fixture-pack.json", tmp / "excl-miss.html", extra=("--exclude", "nosuchid"))
    mini = data_json(html)
    check("exclude: unknown id is a no-op (excluded=0/1, no key, 5 videos)",
          proc.returncode == 0 and "excluded=0/1" in proc.stdout
          and "excluded_ids" not in mini and len(mini.get("videos", [])) == 5)

    print("[degraded bake — fixture-pack-degraded.json]")
    proc, html = bake(FIX / "fixture-pack-degraded.json", tmp / "degraded.html")
    mini = data_json(html)
    check("degraded: exit 0", proc.returncode == 0, proc.stderr[-200:])
    check("degraded: interview mode", "mode=interview" in proc.stdout)
    check("degraded: honest reason in receipt", "numbers not trusted" in proc.stdout)
    check("degraded: no videos/topics/nuggets", not mini.get("videos") and not mini.get("topics")
          and "enrichment_nuggets" not in mini)
    check("degraded: NO market-signal block", 'data-block="market-signal"' not in html)
    check("degraded: NO pattern block", 'data-block="pattern"' not in html)

    print("[enriched bake — fixture-pack-enriched.json]")
    proc, html = bake(FIX / "fixture-pack-enriched.json", tmp / "enriched.html")
    mini = data_json(html)
    nuggets = mini.get("enrichment_nuggets", [])
    check("enriched: exit 0", proc.returncode == 0, proc.stderr[-200:])
    check("enriched: receipt says enrichment_nuggets=2", "enrichment_nuggets=2" in proc.stdout)
    check("enriched: exactly 2 nuggets in DATA_JSON", len(nuggets) == 2, f"got {len(nuggets)}")
    check("enriched: nugget 1 is rising topic demand", nuggets and nuggets[0]["kind"] == "topic_demand"
          and nuggets[0]["trend_direction"] == "rising")
    check("enriched: nugget 2 is market pulse", len(nuggets) == 2 and nuggets[1]["kind"] == "market_pulse")
    check("enriched: market-signal block rendered once", html.count('data-block="market-signal"') == 1)
    check("enriched: block titled for two signals", "Two live market signals" in html)
    check("enriched: both source links present", "https://example.com/fixture-retention-trend" in html
          and "https://example.com/fixture-pulse" in html)
    check("enriched: labels rendered", html.count("LIKELY &middot;") == 2)
    check("enriched: every nugget carries url+label", all(
        n.get("url", "").startswith("https://") and n.get("label") for n in nuggets))
    check("enriched: taste framing (extension not duplication)", "taste of the live-market layer" in html)
    check("enriched: nugget headline uses a real title, never the topic key",
          "the subject behind" in visible(html)
          and "client retention psychology" not in visible(html))
    check("enriched: no unreplaced placeholders", not re.findall(r"\{\{[A-Z_]+\}\}", html))

    passed = sum(1 for _, ok, _ in RESULTS if ok)
    total = len(RESULTS)
    print(f"\n{passed}/{total} checks passed")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
