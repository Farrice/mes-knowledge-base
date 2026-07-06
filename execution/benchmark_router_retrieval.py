#!/usr/bin/env python3
"""benchmark_router_retrieval.py — BM25-only vs hybrid (BM25+embedding) skill router.

Compares find_skill.rank() top-1/top-3 hit rate and latency with
SKILL_ROUTER_EMBED unset (current production default: pure BM25) against
SKILL_ROUTER_EMBED=1 (hybrid: 0.6*bm25_norm + 0.4*cosine_norm, see
execution/find_skill.py rank()).

Eval set (~15 pairs):
  - 5 mined from .agent/routing-intelligence.json routing_decisions — cases
    where exactly one skill (present in the router index) was actually
    deployed for a logged request. NOTE: as of this writing the file has
    only ONE entry in feedback_log, and it's rated auto_miss, not
    auto_match — there isn't yet a validated auto_match sample to mine from.
    These 5 are "what was actually routed for this request", the closest
    real-data proxy available, not confirmed-correct ground truth.
  - 10 hand-authored paraphrase queries deliberately phrased *around* the
    target skill's literal keywords (the case hybrid retrieval exists for —
    BM25 can't see synonyms/paraphrase it has no token overlap with).

Requires .agent/skill-embeddings.json to already be built
(`python3 execution/find_skill.py --build-embeddings`) for the hybrid
condition to differ from BM25 — if the cache is empty, hybrid silently
degrades to BM25 (by design) and this script will report identical rows.

Usage:
    python3 execution/benchmark_router_retrieval.py
    python3 execution/benchmark_router_retrieval.py --top 3
"""
import argparse
import os
import statistics
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import find_skill  # noqa: E402

EVAL_SET = [
    # --- mined from real routing_decisions (see module docstring caveat) ---
    {
        "query": "Josh & Katie v2 training programs for Carbon Torch — full-body recomp and training blocks",
        "expected": "strength-conditioning-os",
    },
    {
        "query": "Chief of Staff OS daily micro briefing and weekly board system",
        "expected": "chief-of-staff-os",
    },
    {
        "query": "6853 Willis Ave weekend Instagram Reels text, email, and briefing for Jen",
        "expected": "jen-santulan-listing-content",
    },
    {
        "query": "Eightward visual brand book and lookbook preview package for Josh",
        "expected": "creative-direction",
    },
    {
        "query": "Satori Graphics design-thinking, creative-concept, and strategic-color mastery expansion",
        "expected": "satori-graphics",
    },
    # --- hand-authored paraphrases (indirect phrasing BM25 tends to miss) ---
    {
        "query": "help me pick a name for my new supplement brand without it turning into a Friday-afternoon guessing game",
        "expected": "david-placek-naming",
    },
    {
        "query": "make sure the AI stops confidently making stuff up when it doesn't actually know",
        "expected": "nate-b-jones-trust-architecture",
    },
    {
        "query": "how do I tell if my design sense is actually good or if I'm fooling myself",
        "expected": "brandon-jacoby-taste-mastery",
    },
    {
        "query": "write a direct-response promo for a financial newsletter built around one strong central idea",
        "expected": "chris-cimorelli-copywriting",
    },
    {
        "query": "structure this brand video the way a documentary director would build a character arc",
        "expected": "cinematic-documentary",
    },
    {
        "query": "I refuse to pick one niche, help me build a one-person business around everything I'm into",
        "expected": "dan-koe-multipassionate-mastery",
    },
    {
        "query": "build a punchy 30 second video ad with a mini story arc instead of a features list",
        "expected": "sarah-levinger-ad-psychology",
    },
    {
        "query": "reputation is under attack, I need a go-direct communications plan that skips the press",
        "expected": "lulu-cheng-meservey-communications",
    },
    {
        "query": "my content doesn't feel like me anymore, diagnose why it feels inauthentic",
        "expected": "tom-noske-content-creation",
    },
    {
        "query": "make this LinkedIn post land better with a sharper rehook at the very top",
        "expected": "lara-acosta-linkedin-growth",
    },
]


def _percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    s = sorted(values)
    k = (len(s) - 1) * pct
    f, c = int(k), min(int(k) + 1, len(s) - 1)
    if f == c:
        return s[f]
    return s[f] + (s[c] - s[f]) * (k - f)


def run_condition(skills: list[dict], hybrid: bool, top: int) -> dict:
    if hybrid:
        os.environ["SKILL_ROUTER_EMBED"] = "1"
    else:
        os.environ.pop("SKILL_ROUTER_EMBED", None)

    hit1 = hit3 = 0
    latencies = []
    misses = []
    for case in EVAL_SET:
        t0 = time.perf_counter()
        results = find_skill.rank(skills, case["query"], top=top)
        latencies.append(time.perf_counter() - t0)
        dirs = [s.get("directory") for s, _ in results]
        if dirs[:1] == [case["expected"]]:
            hit1 += 1
        else:
            misses.append((case["query"], case["expected"], dirs))
        if case["expected"] in dirs[:3]:
            hit3 += 1

    n = len(EVAL_SET)
    return {
        "top1_hit_rate": round(hit1 / n, 3),
        "top3_hit_rate": round(hit3 / n, 3),
        "mean_latency_ms": round(statistics.mean(latencies) * 1000, 1),
        "p95_latency_ms": round(_percentile(latencies, 0.95) * 1000, 1),
        "n": n,
        "misses": misses,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--verbose", action="store_true", help="Print per-query misses.")
    args = ap.parse_args()

    skills = find_skill.load_or_build_index()
    cache = find_skill.load_embed_cache()
    if not cache:
        print(
            "WARNING: .agent/skill-embeddings.json is empty/missing — run "
            "`python3 execution/find_skill.py --build-embeddings` first. "
            "Hybrid numbers below will be identical to BM25 (safe fallback, not a bug).\n",
            file=sys.stderr,
        )

    bm25 = run_condition(skills, hybrid=False, top=args.top)
    hybrid = run_condition(skills, hybrid=True, top=args.top)
    os.environ.pop("SKILL_ROUTER_EMBED", None)  # leave process env clean

    print(f"Eval set: {len(EVAL_SET)} query->skill pairs "
          f"(5 mined from routing-intelligence.json, 10 hand-authored paraphrases)\n")
    print(f"{'condition':10s} {'top1':>6s} {'top3':>6s} {'mean_ms':>9s} {'p95_ms':>9s}")
    for label, r in (("BM25", bm25), ("Hybrid", hybrid)):
        print(f"{label:10s} {r['top1_hit_rate']:6.2f} {r['top3_hit_rate']:6.2f} "
              f"{r['mean_latency_ms']:9.1f} {r['p95_latency_ms']:9.1f}")

    added_p95 = hybrid["p95_latency_ms"] - bm25["p95_latency_ms"]
    print(f"\nAdded p95 latency (hybrid - BM25): {added_p95:.1f} ms")

    if args.verbose:
        for label, r in (("BM25", bm25), ("Hybrid", hybrid)):
            if r["misses"]:
                print(f"\n{label} top-1 misses:")
                for q, exp, got in r["misses"]:
                    print(f"  [{exp}] {q[:70]!r} -> got {got}")

    recommend = hybrid["top3_hit_rate"] >= bm25["top3_hit_rate"] and added_p95 < 1500
    print(f"\nRecommendation: {'ENABLE (evidence supports it)' if recommend else 'KEEP DEFAULT OFF (evidence insufficient)'}")
    print("Default stays SKILL_ROUTER_EMBED unset until Farrice/report-card flips it on a week of weight data.")


if __name__ == "__main__":
    main()
