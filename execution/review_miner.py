#!/usr/bin/env python3
"""review_miner.py — deterministic pre-pass for Dara Denney's customer review mining.

$0, stdlib-only, no API. Ingests a review CSV (any schema — columns auto-detected),
ranks products by review count x rating, surfaces golden-nugget CANDIDATES via
emotion/specificity heuristics, and emits an analysis-ready markdown pack.

The machine compiles; the human/model judges. Final golden-nugget selection stays
a judgment call (Dara's explicit automation boundary).

Usage:
    python3 execution/review_miner.py <reviews.csv> [--out DIR] [--top N] [--min-rating R]

Output (in --out, default .tmp/review-mine/):
    product-ranking.md      products by count x avg rating
    nugget-candidates.md    ranked candidate quotes with heuristic scores + why
    corpus-stats.md         corpus shape, rating distribution, length stats
    analysis-pack.md        all of the above concatenated as one LLM context doc
"""

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

PRODUCT_COLS = ["product", "product_name", "product title", "product_title", "item", "sku", "title"]
RATING_COLS = ["rating", "stars", "score", "review_rating", "rating_value"]
TEXT_COLS = ["text", "review", "body", "content", "review_text", "comment", "review body", "review_content"]

EMOTION_WORDS = {
    "love", "hate", "obsessed", "amazing", "incredible", "life", "changed", "changing",
    "finally", "never", "always", "best", "worst", "cried", "shocked", "skeptical",
    "scam", "honestly", "literally", "actually", "cannot", "can't", "won't", "wow",
    "perfect", "terrible", "disappointed", "surprised", "hooked", "addicted", "swear",
    "converted", "believer", "doubted", "hesitant", "worth", "waste", "regret",
}
SELF_STORY_MARKERS = [
    "i was", "i had", "i've been", "i have been", "my husband", "my wife", "my kids",
    "my doctor", "as a", "i work", "i tried", "i used to", "before this", "after ",
    "years of", "months of", "i'm a ", "i am a ",
]
TRIGGER_EVENT_MARKERS = [
    "the moment", "the day", "one night", "that night", "that morning",
    "when i", "when my", "after i", "after my", "until i", "until my",
    "woke up", "at 2", "at 3", "couldn't", "could not", "wouldn't",
    "would not", "finally", "enough was enough", "realized", "noticed",
    "stopped", "started", "refused", "starving", "bleeding", "crying",
]
SPECIFICITY_RE = re.compile(r"\b\d+[\d,.]*\s*(?:lbs?|pounds?|kg|days?|weeks?|months?|years?|minutes?|hours?|%|x|times?|inches?|sizes?)\b", re.I)
NUMBER_RE = re.compile(r"\b\d+\b")


def detect_col(header, candidates):
    lower = {h.lower().strip(): h for h in header}
    for c in candidates:
        if c in lower:
            return lower[c]
    for h in header:  # fuzzy: substring match
        hl = h.lower()
        if any(c in hl for c in candidates):
            return h
    return None


def score_nugget(text):
    """Heuristic 0-100: how likely this quote could carry an ad. Returns (score, reasons)."""
    t = text.lower()
    words = re.findall(r"[a-z']+", t)
    if not words:
        return 0, []
    reasons, score = [], 0
    emo = sum(1 for w in words if w in EMOTION_WORDS)
    if emo:
        pts = min(30, emo * 8)
        score += pts
        reasons.append(f"emotional language x{emo}")
    if SPECIFICITY_RE.search(text):
        score += 25
        reasons.append("specific number w/ unit (time/qty/result)")
    elif NUMBER_RE.search(text):
        score += 10
        reasons.append("contains a number")
    story = sum(1 for m in SELF_STORY_MARKERS if m in t)
    if story:
        score += min(20, story * 7)
        reasons.append("first-person story marker")
    if "!" in text:
        score += min(10, text.count("!") * 4)
        reasons.append("exclamation")
    if any(k in t for k in ("skeptical", "doubted", "scam", "hesitant", "didn't believe", "didnt believe", "too good to be true")):
        score += 15
        reasons.append("skepticism-flip (objection language)")
    n = len(words)
    if 12 <= n <= 80:
        score += 10
        reasons.append("quotable length")
    elif n < 6:
        score -= 20
    return max(0, min(100, score)), reasons


def score_trigger_event(text):
    """Heuristic pre-pass for an exact moment when a problem became intolerable.

    This deliberately returns candidates, not truth. A human/model must verify
    that the quote contains a concrete problem transition before using it.
    """
    t = text.lower()
    nugget_score, nugget_reasons = score_nugget(text)
    score = 0
    reasons = []
    markers = [marker for marker in TRIGGER_EVENT_MARKERS if marker in t]
    if markers:
        score += min(35, 12 + len(markers) * 7)
        reasons.append("moment/inflection marker: " + ", ".join(markers[:3]))
    if any(marker in t for marker in SELF_STORY_MARKERS):
        score += 20
        reasons.append("first-person situation")
    if SPECIFICITY_RE.search(text) or re.search(r"\b\d{1,2}:\d{2}\b", text):
        score += 20
        reasons.append("specific time/quantity")
    if any(word in t for word in ("pain", "itch", "chew", "sleep", "eat", "work", "walk", "doctor", "vet", "embarrass", "scared", "worried")):
        score += 15
        reasons.append("problem consequence")
    if nugget_score >= 50:
        score += 10
        reasons.append("emotion/specificity support")
    return max(0, min(100, score)), reasons or nugget_reasons[:1]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("csv_path")
    ap.add_argument("--out", default=".tmp/review-mine")
    ap.add_argument("--top", type=int, default=60, help="max nugget candidates (default 60)")
    ap.add_argument("--min-rating", type=float, default=0, help="only consider reviews >= this rating for nuggets (0 = all; low-star reviews are objection gold, so default keeps them)")
    args = ap.parse_args()

    path = Path(args.csv_path)
    if not path.exists():
        sys.exit(f"ERROR: {path} not found")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    with open(path, newline="", encoding="utf-8-sig", errors="replace") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames or []
        rows = list(reader)
    if not rows:
        sys.exit("ERROR: empty CSV")

    pcol = detect_col(header, PRODUCT_COLS)
    rcol = detect_col(header, RATING_COLS)
    tcol = detect_col(header, TEXT_COLS)
    if not tcol:
        sys.exit(f"ERROR: no review-text column found in {header} — expected one of {TEXT_COLS}")

    # Product ranking
    stats = defaultdict(lambda: {"n": 0, "sum": 0.0, "rated": 0})
    for r in rows:
        prod = (r.get(pcol) or "ALL").strip() if pcol else "ALL"
        s = stats[prod]
        s["n"] += 1
        if rcol:
            try:
                s["sum"] += float(str(r.get(rcol, "")).strip() or 0)
                s["rated"] += 1
            except ValueError:
                pass

    ranking = sorted(stats.items(), key=lambda kv: (-kv[1]["n"], kv[0]))
    rank_md = ["# Product Ranking (count x rating)\n", "| Product | # Reviews | Avg Rating |", "|---|---|---|"]
    for prod, s in ranking:
        avg = f"{s['sum']/s['rated']:.2f}" if s["rated"] else "—"
        rank_md.append(f"| {prod} | {s['n']} | {avg} |")
    (out / "product-ranking.md").write_text("\n".join(rank_md) + "\n")

    # Nugget candidates
    cands = []
    trigger_cands = []
    for row_number, r in enumerate(rows, start=2):
        text = (r.get(tcol) or "").strip()
        if not text:
            continue
        if rcol and args.min_rating:
            try:
                if float(str(r.get(rcol, "0")).strip() or 0) < args.min_rating:
                    continue
            except ValueError:
                pass
        sc, reasons = score_nugget(text)
        if sc >= 30:
            prod = (r.get(pcol) or "").strip() if pcol else ""
            rating = (str(r.get(rcol, "")).strip() if rcol else "")
            cands.append((sc, text, reasons, prod, rating))
        trigger_score, trigger_reasons = score_trigger_event(text)
        if trigger_score >= 45:
            prod = (r.get(pcol) or "").strip() if pcol else ""
            rating = (str(r.get(rcol, "")).strip() if rcol else "")
            trigger_cands.append((trigger_score, text, trigger_reasons, prod, rating, row_number))
    cands.sort(key=lambda x: -x[0])
    cands = cands[: args.top]

    nug_md = [
        "# Golden Nugget CANDIDATES (heuristic pre-pass — human/model judgment decides)\n",
        f"Corpus: {len(rows)} reviews · candidates >= score 30 · top {args.top} shown\n",
    ]
    for sc, text, reasons, prod, rating in cands:
        one = " ".join(text.split())
        if len(one) > 400:
            one = one[:397] + "..."
        meta = " · ".join(x for x in (prod, f"{rating}★" if rating else "") if x)
        nug_md.append(f"- **[{sc}]** \"{one}\"" + (f"  \n  _{meta}_" if meta else "") + f"  \n  _why: {', '.join(reasons)}_")
    (out / "nugget-candidates.md").write_text("\n".join(nug_md) + "\n")

    trigger_cands.sort(key=lambda x: -x[0])
    trigger_cands = trigger_cands[: args.top]
    trigger_md = [
        "# Trigger-Event CANDIDATES (heuristic pre-pass — verification required)\n",
        "A trigger event is a concrete moment when the problem became intolerable. "
        "These rows are candidates, not invented stories or approved ad claims.\n",
    ]
    for sc, text, reasons, prod, rating, row_number in trigger_cands:
        one = " ".join(text.split())
        if len(one) > 500:
            one = one[:497] + "..."
        meta = " · ".join(x for x in (prod, f"{rating}★" if rating else "", f"CSV row {row_number}") if x)
        trigger_md.append(
            f"- **[{sc}]** \"{one}\"  \n"
            f"  _{meta}_  \n"
            f"  _why surfaced: {', '.join(reasons)}_"
        )
    (out / "trigger-event-candidates.md").write_text("\n".join(trigger_md) + "\n")

    # Corpus stats
    lens = [len((r.get(tcol) or "").split()) for r in rows]
    dist = defaultdict(int)
    if rcol:
        for r in rows:
            try:
                dist[int(float(str(r.get(rcol, "")).strip() or 0))] += 1
            except ValueError:
                dist["?"] += 1
    stats_md = [
        "# Corpus Stats\n",
        f"- Reviews: {len(rows)} · Products: {len(stats)} · Text col: `{tcol}`"
        + (f" · Rating col: `{rcol}`" if rcol else " · Rating col: none")
        + (f" · Product col: `{pcol}`" if pcol else " · Product col: none"),
        f"- Review length (words): min {min(lens)} / median {sorted(lens)[len(lens)//2]} / max {max(lens)}",
    ]
    if dist:
        stats_md.append("- Rating distribution: " + " · ".join(f"{k}★: {v}" for k, v in sorted(dist.items(), key=lambda kv: str(kv[0]))))
    stats_md.append("\nLow-star reviews are objection gold — mine them for friction language, not just praise.")
    (out / "corpus-stats.md").write_text("\n".join(stats_md) + "\n")

    pack = "\n\n---\n\n".join(
        (out / n).read_text()
        for n in ("corpus-stats.md", "product-ranking.md", "nugget-candidates.md", "trigger-event-candidates.md")
    )
    (out / "analysis-pack.md").write_text(
        "# Review Mining Pre-Pass (deterministic)\n\n"
        "> Machine compiled; judgment pending. Next: golden-nugget selection + Dara's 4 AI-analysis questions "
        "(see skills/dara-denney-meta-ads/workflows/20-review-mining.md).\n\n" + pack
    )

    print(
        f"review_miner: {len(rows)} reviews -> {out}/ "
        f"(product-ranking, nugget-candidates x{len(cands)}, "
        f"trigger-event-candidates x{len(trigger_cands)}, corpus-stats, analysis-pack)"
    )


if __name__ == "__main__":
    main()
