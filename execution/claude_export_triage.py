#!/usr/bin/env python3
"""claude_export_triage.py — bucket every exported conversation, cheaply.

Two stages so we never pay for an LLM call on all 3,700 conversations:

  Stage A · heuristic (deterministic, $0, over ALL conversations)
      Regex/counting signals → a provisional bucket + a 0-100 score. Everything below
      threshold is finalized as its provisional bucket (usually low-signal) with no spend.

  Stage B · LLM classify (Gemini `lite`, ONLY the high-signal `needs_llm` subset)
      A compact digest (title + a couple of turns + heuristic signals — NOT the full
      transcript) → structured {bucket, confidence, extraction_value, ...}. Shardable across
      parallel agents (`--shard k --of m`) and hard-capped by a token budget.

Buckets: extraction-grade · prompt-tool-grade · knowledge-grade ·
         personal-context-grade · project-deliverable-grade · low-signal

Then `rollup` merges both stages into `triage-index.json`, and `menu` emits a ranked,
human-gated list of skill candidates (projects + rich dialogues) for /convert-prompt and
/extract-forge. The importer never builds skills automatically — Farrice picks.

Usage:
    python3 execution/claude_export_triage.py heuristic                 # Stage A, all convs
    python3 execution/claude_export_triage.py classify --dry-run-cost   # Stage B cost estimate
    python3 execution/claude_export_triage.py classify                  # Stage B (needs GEMINI_API_KEY)
    python3 execution/claude_export_triage.py classify --shard 0 --of 4 # one parallel shard
    python3 execution/claude_export_triage.py rollup                    # build triage-index.json
    python3 execution/claude_export_triage.py menu                      # ranked deployables report
    python3 execution/claude_export_triage.py stats                     # bucket distribution
"""
from __future__ import annotations

import argparse
import glob
import json
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import claude_export_state as st  # noqa: E402

BUCKETS = ["extraction-grade", "prompt-tool-grade", "knowledge-grade",
           "personal-context-grade", "project-deliverable-grade", "low-signal"]
HIGH_VALUE = {"extraction-grade", "prompt-tool-grade", "knowledge-grade"}

# ── TUNING SURFACE (edit these to reshape triage) ──────────────────────────────
# Markers are lowercased regex fragments; each group contributes to its bucket's score.
MARKERS: Dict[str, List[str]] = {
    "prompt-tool-grade": [
        r"\byou are\b", r"\byour role is\b", r"\bact as\b", r"\bsystem prompt\b",
        r"\bcustom instructions?\b", r"\bpersona\b", r"<system>", r"\bprompt template\b",
    ],
    "extraction-grade": [
        r"\bextract(ion|ed|ing)?\b", r"\bgenius pattern", r"\bmethodology\b", r"\bframework\b",
        r"\bmental model", r"\bfirst principles?\b", r"\bworkflow\b", r"\bskill\b",
        r"\bMES\b", r"\bdeconstruct", r"\bsignature move",
    ],
    "knowledge-grade": [
        r"\bresearch\b", r"\banalys[ie]s\b", r"\bdefine[ds]?\b", r"\bdefinition\b",
        r"\bstudy\b", r"\bexplain\b", r"\bstrateg(y|ic)\b", r"\bmarket\b", r"\bcompare\b",
    ],
    "personal-context-grade": [
        r"\bmy wife\b", r"\bmy son\b", r"\bmy daughter\b", r"\bmy kid\b", r"\bmy partner\b",
        r"\bi feel\b", r"\bi'm struggling\b", r"\bmy goal\b", r"\bpersonal\b", r"\bJJ\b",
        r"\bhealth\b", r"\bmy business\b", r"\bmy brand\b",
    ],
    "project-deliverable-grade": [
        r"\bwrite (me |a |an |the )", r"\bdraft\b", r"\bfinal\b", r"\bhere'?s the\b",
        r"\brevise\b", r"\brewrite\b", r"\bpolish\b", r"\bpublish\b", r"\blaunch\b",
    ],
}
# High-value expert surnames worth a routing bonus (compact, not exhaustive — the roster
# is huge; these are the ones that repeatedly matter in Farrice's world).
EXPERT_HINTS = [
    "acosta", "cole", "iha", "georgi", "gotch", "kallaway", "saraev", "hormozi",
    "brunson", "halbert", "schwartz", "ogilvy", "sutherland", "godin", "priestley",
    "hawley", "stanton", "pressfield", "connelly", "roth", "orlean", "vuong", "perell",
    "dunford", "wiebe", "fladlien", "suby", "koe", "denney", "eltakrori", "whiting",
]
WEIGHTS = {  # signal-group → contribution ceiling toward heuristic_score
    "length": 22, "markers": 40, "experts": 14, "code": 10, "attachments": 6, "turns": 8,
}
NEEDS_LLM_THRESHOLD = 42  # score at/above this (or a high-value provisional bucket) → LLM classify
SCAN_CHARS = 60_000       # cap text scanned per conversation for regexes (markers appear early)
# ───────────────────────────────────────────────────────────────────────────────

_CODE_FENCE = re.compile(r"```")
_WORD = re.compile(r"\w+")


def _read_text(md_path: str) -> str:
    p = ROOT / md_path
    if not p.exists():
        return ""
    return p.read_text()[:SCAN_CHARS].lower()


def score_conversation(meta: Dict[str, Any], text: str) -> Dict[str, Any]:
    """Deterministic feature vector + provisional bucket + score. No LLM."""
    signals: Dict[str, Any] = {}
    bucket_points: Dict[str, float] = {b: 0.0 for b in BUCKETS}

    # length (log-ish; median here is ~8.8k words so scale generously)
    wc = meta.get("word_count", 0)
    length_pts = min(WEIGHTS["length"], wc / 1200.0)
    signals["word_count"] = wc

    # markers per bucket
    marker_hits: Dict[str, int] = {}
    for bucket, pats in MARKERS.items():
        hits = sum(len(re.findall(p, text)) for p in pats)
        marker_hits[bucket] = hits
        bucket_points[bucket] += min(WEIGHTS["markers"], hits * 4)
    signals["marker_hits"] = marker_hits

    # expert hints (routes toward extraction)
    experts = sorted({e for e in EXPERT_HINTS if e in text})
    exp_pts = min(WEIGHTS["experts"], len(experts) * 5)
    bucket_points["extraction-grade"] += exp_pts
    signals["expert_hits"] = experts

    # code fences (prompt/deliverable)
    code = len(_CODE_FENCE.findall(text)) // 2
    code_pts = min(WEIGHTS["code"], code * 2)
    bucket_points["prompt-tool-grade"] += code_pts * 0.6
    bucket_points["project-deliverable-grade"] += code_pts * 0.4
    signals["code_blocks"] = code

    # attachments (pasted prompts → prompt/extraction)
    if meta.get("has_attachments"):
        bucket_points["prompt-tool-grade"] += WEIGHTS["attachments"] * 0.5
        bucket_points["extraction-grade"] += WEIGHTS["attachments"] * 0.5
    signals["has_attachments"] = bool(meta.get("has_attachments"))

    # conversation depth
    mc = meta.get("message_count", 0)
    turn_pts = min(WEIGHTS["turns"], mc)
    signals["message_count"] = mc

    # base score = length + depth + best marker/expert/code contribution spread
    base = length_pts + turn_pts + sum(bucket_points.values())
    heuristic_score = round(min(100.0, base), 1)

    # provisional bucket
    if wc == 0 or mc <= 1:
        provisional = "low-signal"
    elif max(bucket_points.values()) == 0:
        provisional = "low-signal" if wc < 400 else "knowledge-grade"
    else:
        provisional = max(bucket_points, key=bucket_points.get)
        if heuristic_score < 12 and wc < 400:
            provisional = "low-signal"

    needs_llm = (heuristic_score >= NEEDS_LLM_THRESHOLD) or (provisional in HIGH_VALUE and wc >= 500)
    return {
        "id": meta["id"], "heuristic_score": heuristic_score,
        "provisional_bucket": provisional, "signals": signals, "needs_llm": needs_llm,
        "md_path": meta["md_path"], "title": meta.get("title", ""),
        "word_count": wc, "message_count": mc,
    }


def stage_a_heuristic() -> Dict[str, Any]:
    idx = json.loads(st.INDEX_PATH.read_text())
    out = {"generated_at": st._now(), "weights": WEIGHTS,
           "threshold": NEEDS_LLM_THRESHOLD, "conversations": []}
    needs = 0
    for i, c in enumerate(idx["conversations"]):
        rec = score_conversation(c, _read_text(c["md_path"]))
        out["conversations"].append(rec)
        needs += 1 if rec["needs_llm"] else 0
        if (i + 1) % 1000 == 0:
            print(f"  … {i + 1} scored")
    st.TRIAGE_DIR.mkdir(parents=True, exist_ok=True)
    (st.TRIAGE_DIR / "heuristic-scores.json").write_text(json.dumps(out, indent=2))

    prov: Dict[str, int] = {}
    for r in out["conversations"]:
        prov[r["provisional_bucket"]] = prov.get(r["provisional_bucket"], 0) + 1
    print("\n─── STAGE A · HEURISTIC ───")
    print(f"  scored: {len(out['conversations'])}  ·  needs LLM: {needs}")
    for b in BUCKETS:
        print(f"    {b:<26} {prov.get(b, 0)}")
    print(f"  next: python3 execution/claude_export_triage.py classify --dry-run-cost")
    return out


# ── Stage B · LLM classification ──

CLASSIFY_SYS = (
    "You classify one Claude.ai conversation into exactly one bucket and score its reuse value. "
    "Buckets: extraction-grade (a named expert/framework/methodology worth turning into a skill), "
    "prompt-tool-grade (a reusable system prompt / custom-instruction / tool the user built), "
    "knowledge-grade (research, analysis, insight worth keeping), "
    "personal-context-grade (identity, worldview, personal/business context about the user), "
    "project-deliverable-grade (client/creative deliverable drafting), "
    "low-signal (chatter, one-off lookup, abandoned). Output JSON only."
)
CLASSIFY_SCHEMA = {
    "type": "object",
    "properties": {
        "bucket": {"type": "string", "enum": BUCKETS},
        "confidence": {"type": "number"},
        "rationale": {"type": "string"},
        "extraction_value": {"type": "integer"},
        "expert_named": {"type": "string"},
        "reusable_asset": {"type": "boolean"},
    },
    "required": ["bucket", "confidence", "rationale", "extraction_value", "reusable_asset"],
}


def _digest(rec: Dict[str, Any]) -> str:
    """Compact, privacy-conscious digest for the classifier (not the full transcript)."""
    p = ROOT / rec["md_path"]
    body = p.read_text() if p.exists() else ""
    # first human turn + first/last assistant turn, trimmed
    turns = re.split(r"\n## ", body)
    head = "\n".join(turns[:3])[:1400]
    tail = turns[-1][:600] if len(turns) > 3 else ""
    sig = rec["signals"]
    return (
        f"TITLE: {rec['title']}\n"
        f"SIGNALS: words={sig.get('word_count')} msgs={rec['message_count']} "
        f"experts={sig.get('expert_hits')} code_blocks={sig.get('code_blocks')} "
        f"markers={sig.get('marker_hits')} provisional={rec['provisional_bucket']}\n"
        f"--- opening ---\n{head}\n--- closing ---\n{tail}"
    )


def _needs_llm_recs(shard: Optional[int], of: Optional[int]) -> List[Dict[str, Any]]:
    hs = json.loads((st.TRIAGE_DIR / "heuristic-scores.json").read_text())
    recs = [r for r in hs["conversations"] if r["needs_llm"]]
    if shard is not None and of:
        recs = [r for i, r in enumerate(recs) if i % of == shard]
    # skip ones already classified (idempotent / resumable)
    done = {p.stem.replace("triage-", "") for p in st.TRIAGE_DIR.glob("triage-*.json")
            if p.name != "triage-index.json"}
    return [r for r in recs if r["id"] not in done]


def classify(shard: Optional[int], of: Optional[int], dry_cost: bool,
             max_items: Optional[int], top: Optional[int], rpm: int) -> Dict[str, Any]:
    """Paced, resumable, free-tier-aware classification.

    The default GEMINI_API_KEY is free-tier (≈15 requests/min), so this runs a paced
    SEQUENTIAL loop (not 8-way parallel, which just triggers 429s) and writes each triage
    record as it goes — kill/resume anytime, already-done items are skipped. Focus spend
    on the densest conversations with `--top N` (they're the deployable candidates); the
    heuristic already buckets the long tail. With a paid key, raise --rpm and/or shard.
    """
    recs = _needs_llm_recs(shard, of)
    # densest first — these are the extraction/prompt candidates the menu ranks
    recs.sort(key=lambda r: r["heuristic_score"], reverse=True)
    if top:
        recs = recs[:top]
    if max_items:
        recs = recs[:max_items]

    from gemini_client import GeminiClient, load_env, estimate_cost, MODEL_TIERS
    load_env()
    model_name = MODEL_TIERS["lite"]

    digests = [_digest(r) for r in recs]
    in_tokens = sum(len(CLASSIFY_SYS) + len(d) for d in digests) // 4
    out_tokens = len(recs) * 160
    est = estimate_cost(model_name, in_tokens, out_tokens)
    eta_min = round(len(recs) / max(1, rpm), 1)
    print(f"─── STAGE B · CLASSIFY ({len(recs)} conversations{f', shard {shard}/{of}' if of else ''}) ───")
    print(f"  model: {model_name}  ·  est input ~{in_tokens:,} tok, output ~{out_tokens:,} tok")
    print(f"  estimated cost: ${est:.3f}  ·  paced at {rpm} rpm → ETA ~{eta_min} min")
    if dry_cost:
        print("  (dry-run-cost — no API calls made)")
        return {"to_classify": len(recs), "estimated_cost_usd": round(est, 4), "dry": True}
    if not recs:
        print("  nothing to classify (all done).")
        return {"to_classify": 0, "written": 0}

    client = GeminiClient()
    interval = 60.0 / max(1, rpm)  # seconds between requests to respect the RPM cap
    st.TRIAGE_DIR.mkdir(parents=True, exist_ok=True)
    written = 0
    failed = 0
    for i, (rec, digest) in enumerate(zip(recs, digests)):
        t0 = time.monotonic()
        parsed = None
        try:
            text, _meta = client.generate_sync(
                digest, system_instruction=CLASSIFY_SYS, model="lite",
                response_mime_type="application/json", response_schema=CLASSIFY_SCHEMA,
                temperature=0.1, max_output_tokens=400)
            parsed = json.loads(text) if text else None
        except (json.JSONDecodeError, Exception):  # noqa: B014 — any failure → skip, retry on re-run
            parsed = None
        if not parsed:
            failed += 1
        else:
            route = _route_for(parsed["bucket"], parsed.get("extraction_value", 0),
                               parsed.get("reusable_asset", False))
            record = {
                "conversation_id": rec["id"], "classified_at": st._now(), "classified_by": "llm",
                "bucket": parsed["bucket"], "confidence": parsed.get("confidence", 0.3),
                "heuristic_score": rec["heuristic_score"], "signals": rec["signals"],
                "rationale": parsed.get("rationale", ""),
                "extraction_value": parsed.get("extraction_value", 0),
                "expert_named": parsed.get("expert_named", ""),
                "reusable_asset": parsed.get("reusable_asset", False),
                "title": rec["title"], "md_path": rec["md_path"], "recommended_route": route,
            }
            (st.TRIAGE_DIR / f"triage-{rec['id']}.json").write_text(json.dumps(record, indent=2))
            written += 1
        if (i + 1) % 25 == 0:
            print(f"  … {i + 1}/{len(recs)} processed ({written} ok, {failed} skipped)")
        # pace: sleep the remainder of the interval
        elapsed = time.monotonic() - t0
        if elapsed < interval and i < len(recs) - 1:
            time.sleep(interval - elapsed)

    print(f"\n  classified: {written}  ·  skipped (retry on re-run): {failed}")
    print("  next: python3 execution/claude_export_triage.py rollup")
    return {"to_classify": len(recs), "written": written, "failed": failed}


def _route_for(bucket: str, extraction_value: int, reusable: bool) -> str:
    if bucket == "extraction-grade" and extraction_value >= 6:
        return "extract-forge"
    if bucket == "prompt-tool-grade" or (reusable and bucket in HIGH_VALUE):
        return "convert-prompt"
    if bucket in ("knowledge-grade", "personal-context-grade"):
        return "ingest-only"
    if bucket == "project-deliverable-grade":
        return "ingest-only"
    return "skip"


# ── Rollup + menu + stats ──

def rollup() -> Dict[str, Any]:
    hs = json.loads((st.TRIAGE_DIR / "heuristic-scores.json").read_text())
    llm = {}
    for p in st.TRIAGE_DIR.glob("triage-*.json"):
        if p.name == "triage-index.json":  # our own rollup output; not a per-conv record
            continue
        r = json.loads(p.read_text())
        llm[r["conversation_id"]] = r

    buckets: Dict[str, List[Dict[str, Any]]] = {b: [] for b in BUCKETS}
    for rec in hs["conversations"]:
        cid = rec["id"]
        if cid in llm:
            r = llm[cid]
            entry = {"id": cid, "title": r["title"], "bucket": r["bucket"],
                     "extraction_value": r.get("extraction_value", 0),
                     "reusable_asset": r.get("reusable_asset", False),
                     "expert_named": r.get("expert_named", ""),
                     "recommended_route": r["recommended_route"], "classified_by": r["classified_by"]}
        else:
            entry = {"id": cid, "title": rec["title"], "bucket": rec["provisional_bucket"],
                     "extraction_value": 0, "reusable_asset": False, "expert_named": "",
                     "recommended_route": _route_for(rec["provisional_bucket"], 0, False),
                     "classified_by": "heuristic"}
        buckets[entry["bucket"]].append(entry)

    out = {"generated_at": st._now(),
           "counts": {b: len(v) for b, v in buckets.items()}, "buckets": buckets}
    (st.TRIAGE_DIR / "triage-index.json").write_text(json.dumps(out, indent=2))

    # mark triaged in state
    state = st.load_state()
    for b, items in buckets.items():
        for it in items:
            st.mark(state, "triaged", it["id"], {"bucket": b})
    st.save_state(state)

    print("─── ROLLUP · triage-index.json ───")
    for b in BUCKETS:
        print(f"    {b:<26} {out['counts'][b]}")
    print("  next: python3 execution/claude_export_triage.py menu")
    return out


def _menu_rank(entry: Dict[str, Any], wc_pct: float) -> float:
    ev = max(0, min(10, entry.get("extraction_value", 0)))  # clamp — LLM sometimes returns out-of-range
    return (0.35 * (ev / 10.0)
            + 0.20 * wc_pct
            + 0.20 * (1.0 if entry.get("expert_named") else 0.0)
            + 0.15 * (1.0 if entry.get("reusable_asset") else 0.0)
            + 0.10 * min(1.0, ev / 8.0))


def menu() -> int:
    tix_path = st.TRIAGE_DIR / "triage-index.json"
    if not tix_path.exists():
        print("Run `rollup` first."); return 1
    tix = json.loads(tix_path.read_text())
    idx = json.loads(st.INDEX_PATH.read_text())
    wc = {c["id"]: c["word_count"] for c in idx["conversations"]}
    mdmap = {c["id"]: c["md_path"] for c in idx["conversations"]}
    wc_sorted = sorted(wc.values()) or [0]

    def pct(v):
        import bisect
        return bisect.bisect_left(wc_sorted, v) / max(1, len(wc_sorted))

    forge = []  # extract-forge candidates (rich dialogues)
    convert = []  # convert-prompt candidates (prompts)
    for b in ("extraction-grade", "prompt-tool-grade", "knowledge-grade"):
        for e in tix["buckets"].get(b, []):
            e = dict(e, rank=round(_menu_rank(e, pct(wc.get(e["id"], 0))), 3),
                     md_path=mdmap.get(e["id"], ""))
            if e["recommended_route"] == "extract-forge":
                forge.append(e)
            elif e["recommended_route"] == "convert-prompt":
                convert.append(e)
    forge.sort(key=lambda e: e["rank"], reverse=True)
    convert.sort(key=lambda e: e["rank"], reverse=True)

    # projects are first-class /convert-prompt candidates
    projects = sorted(
        [p for p in idx["projects"] if p["has_instructions"]],
        key=lambda p: p["instruction_chars"], reverse=True)

    lines = ["# Claude Export — Extraction Candidates (ranked)", "",
             f"_generated {tix['generated_at']}_", "",
             "Human-gated: pick rows, then run the noted workflow on the `md_path`.", "",
             "## → /convert-prompt · Project custom instructions (112 total)", "",
             "| # | Project | chars | md_path |", "|---|---------|-------|---------|"]
    for i, p in enumerate(projects[:40], 1):
        lines.append(f"| {i} | {p['name'][:60]} | {p['instruction_chars']} | `{p['md_path']}` |")
    lines += ["", "## → /convert-prompt · Prompts & tools found in conversations", "",
              "| # | Title | expert | rank | md_path |", "|---|-------|--------|------|---------|"]
    for i, e in enumerate(convert[:40], 1):
        lines.append(f"| {i} | {e['title'][:55]} | {e.get('expert_named', '')} | {e['rank']} | `{e['md_path']}` |")
    lines += ["", "## → /extract-forge · Rich expert dialogues", "",
              "| # | Title | expert | value | rank | md_path |",
              "|---|-------|--------|-------|------|---------|"]
    for i, e in enumerate(forge[:40], 1):
        lines.append(f"| {i} | {e['title'][:50]} | {e.get('expert_named', '')} | "
                     f"{e.get('extraction_value', 0)} | {e['rank']} | `{e['md_path']}` |")

    st.REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out = st.REPORTS_DIR / "extraction-menu.md"
    out.write_text("\n".join(lines) + "\n")
    print(f"─── MENU · {out.relative_to(ROOT)} ───")
    print(f"  projects (convert-prompt): {len(projects)}")
    print(f"  conversation prompts (convert-prompt): {len(convert)}")
    print(f"  expert dialogues (extract-forge): {len(forge)}")
    return 0


def stats() -> int:
    tix_path = st.TRIAGE_DIR / "triage-index.json"
    if not tix_path.exists():
        print("Run `heuristic` → `rollup` first."); return 1
    tix = json.loads(tix_path.read_text())
    print("─── TRIAGE · BUCKET DISTRIBUTION ───")
    total = sum(tix["counts"].values())
    for b in BUCKETS:
        n = tix["counts"][b]
        print(f"    {b:<26} {n:>5}  ({100*n/max(1,total):.0f}%)")
    print(f"    {'TOTAL':<26} {total:>5}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Triage claude.ai export conversations")
    ap.add_argument("command", choices=["heuristic", "classify", "rollup", "menu", "stats"])
    ap.add_argument("--shard", type=int, help="this shard index (0-based)")
    ap.add_argument("--of", type=int, help="total shard count")
    ap.add_argument("--dry-run-cost", action="store_true", help="estimate LLM cost, no calls")
    ap.add_argument("--max", type=int, help="cap items classified (smoke test)")
    ap.add_argument("--top", type=int, help="classify only the top-N densest candidates "
                    "(heuristic buckets the rest); focuses free-tier spend")
    ap.add_argument("--rpm", type=int, default=14, help="requests/min pacing (default 14 for "
                    "the free tier's 15-rpm cap; raise with a paid key)")
    args = ap.parse_args()

    if args.command == "heuristic":
        stage_a_heuristic()
    elif args.command == "classify":
        classify(shard=args.shard, of=args.of, dry_cost=args.dry_run_cost,
                 max_items=args.max, top=args.top, rpm=args.rpm)
    elif args.command == "rollup":
        rollup()
    elif args.command == "menu":
        return menu()
    elif args.command == "stats":
        return stats()
    return 0


if __name__ == "__main__":
    sys.exit(main())
