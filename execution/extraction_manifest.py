#!/usr/bin/env python3
"""extraction_manifest.py — deterministic sizing for the /extract v3.0 adaptive pipeline.

Replaces the asserted "3-5 workflows" in extract.md and the private sizing table in
convert-extraction.md with one derived manifest. The forge (/extract-forge) remains the
explicit full-ceremony session; this helper is how plain /extract earns forge-shape
output honestly (Farrice decisions, 2026-07-23: floor >=7 prompts + multi-tier when the
corpus supports it; auto-enrich thin sources; forge-scale extensions; never pad filler).

Commands
  corpus --dir extractions/<slug>          -> corpus mass + RICH/MID/THIN verdict
  derive --patterns N --deliverables N ... -> JSON manifest (tiered workflow count,
                                              prompt floor, references, flags)
  check  --skill skills/<dir> [--manifest <json>] [--enforce]
                                           -> shipped counts vs manifest floors
                                              (observe-mode: warnings, exit 0)

Thresholds (words, post-enrichment): RICH >= 8000, MID >= 5000, THIN below.
Calibration anchors: meg-heckman 23 patterns -> 14 workflows (shipped 13),
paolo-trivellato ~17 patterns -> 10 (shipped 11).
"""

import argparse
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RICH_WORDS = 8000
MID_WORDS = 5000

# Source files that count toward corpus mass inside extractions/<slug>/
SOURCE_GLOBS = ("transcript*.txt", "transcript*.md", "source*.txt", "source*.md",
                "*-transcript.txt", "corpus/*.txt", "corpus/*.md")


def _clamp(v, lo, hi):
    return max(lo, min(hi, v))


def corpus_stats(directory: Path) -> dict:
    files, total_words = [], 0
    seen = set()
    for pattern in SOURCE_GLOBS:
        for f in sorted(directory.glob(pattern)):
            if f in seen or not f.is_file():
                continue
            seen.add(f)
            words = len(re.findall(r"\S+", f.read_text(errors="replace")))
            files.append({"file": str(f.relative_to(ROOT)) if f.is_relative_to(ROOT) else str(f),
                          "words": words})
            total_words += words
    verdict = "RICH" if total_words >= RICH_WORDS else "MID" if total_words >= MID_WORDS else "THIN"
    return {"dir": str(directory), "sources": files, "source_count": len(files),
            "total_words": total_words, "verdict": verdict,
            "thresholds": {"RICH": RICH_WORDS, "MID": MID_WORDS}}


def derive_manifest(patterns: int, hidden: int, exemplars: int, deliverables: int,
                    corpus_words: int, stacking_hits: int = 2, extension: bool = False) -> dict:
    band = "RICH" if corpus_words >= RICH_WORDS else "MID" if corpus_words >= MID_WORDS else "THIN"

    if extension:
        workflows = _clamp(round(patterns * 0.5), 2, 5)
        prompts = max(5, deliverables) if patterns >= 5 else max(2, deliverables)
        if band == "THIN" and patterns < 3:
            workflows, prompts = _clamp(patterns, 1, 2), max(1, deliverables)
        tiers = {"placement": "into existing skill's tier table (Foundation for gates/audits, "
                              "Practitioner for asset production, Stacking for cross-expert)"}
        references = ["source-quotes append (quote bank + claims-ledger entries)",
                      "provenance entries for new anti-pattern/exemplar anchors"]
        orchestrator = False
    else:
        if band == "RICH":
            workflows = _clamp(round(patterns * 0.6), 8, 15)
        elif band == "MID":
            workflows = _clamp(round(patterns * 0.6), 4, 7)
        else:
            workflows = _clamp(round(patterns * 0.5), 2, 4)
        t1 = min(4, max(3, math.ceil(workflows * 0.3))) if workflows >= 4 else workflows
        t3 = _clamp(stacking_hits, 2, 4) if workflows >= 8 else _clamp(stacking_hits, 0, 2)
        t2 = max(0, workflows - t1 - t3)
        tiers = {"tier1_foundation": t1, "tier2_practitioner": t2, "tier3_stacking": t3}
        prompts = max(7, deliverables) if band in ("RICH", "MID") else max(2, min(deliverables, patterns))
        references = ["source-quotes.md (verbatim quote bank + claims ledger)",
                      "cross-domain-patterns.md", "provenance ledger (grep-verified anchors)",
                      "genius-patterns.md", "hidden-knowledge.md"]
        orchestrator = workflows >= 8

    manifest = {
        "band": band, "corpus_words": corpus_words, "extension": extension,
        "yields": {"patterns": patterns, "hidden": hidden, "exemplars": exemplars,
                   "deliverables": deliverables, "stacking_hits": stacking_hits},
        "workflows": workflows, "tiers": tiers, "prompts_floor": prompts,
        "references": references, "orchestrator_eligible": orchestrator,
        "agent": "required (AGENT.md + memory + front door via sync_registries)",
        "fidelity": "low" if band == "THIN" else "full",
        "note": ("THIN after enrichment: ship the honest count, flag fidelity: low, never pad."
                 if band == "THIN" else
                 "Floors are minimums earned by the corpus; scale up when yields demand it."),
    }
    return manifest


def check_skill(skill_dir: Path, manifest: dict | None, enforce: bool) -> int:
    wf = len(list((skill_dir / "workflows").glob("*.md"))) if (skill_dir / "workflows").exists() else 0
    prompts = len(list((skill_dir / "references" / "prompts-v2").glob("*.md"))) \
        if (skill_dir / "references" / "prompts-v2").exists() else 0
    refs = [p.name for p in (skill_dir / "references").glob("*.md")] \
        if (skill_dir / "references").exists() else []

    print(f"manifest check — {skill_dir.name}")
    print(f"  shipped: workflows={wf} prompts-v2={prompts} reference-files={len(refs)}")
    failures = []
    if manifest:
        floor_wf = manifest.get("workflows", 0)
        floor_p = manifest.get("prompts_floor", 0)
        if not manifest.get("extension") and wf < floor_wf:
            failures.append(f"workflows {wf} < manifest floor {floor_wf}")
        if prompts < floor_p:
            failures.append(f"prompts-v2 {prompts} < manifest floor {floor_p}")
        if not manifest.get("extension"):
            need = {"source-quotes.md"}
            missing = need - set(refs)
            if missing:
                failures.append(f"missing mandatory references: {sorted(missing)}")
    for f in failures:
        print(f"  WARN: {f}")
    if not failures:
        print("  GATE: clear.")
    elif enforce:
        print("  GATE: FAIL (--enforce).")
        return 1
    else:
        print("  GATE: observe-mode — warnings only (pass --enforce to fail).")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("corpus", help="measure corpus mass in an extractions dir")
    c.add_argument("--dir", required=True)

    d = sub.add_parser("derive", help="derive the build manifest from extraction yields")
    d.add_argument("--patterns", type=int, required=True)
    d.add_argument("--hidden", type=int, default=0)
    d.add_argument("--exemplars", type=int, default=0)
    d.add_argument("--deliverables", type=int, required=True)
    d.add_argument("--corpus-words", type=int, required=True)
    d.add_argument("--stacking-hits", type=int, default=2)
    d.add_argument("--extension", action="store_true")
    d.add_argument("--out", help="also write the manifest JSON here")

    k = sub.add_parser("check", help="validate a shipped skill against a manifest")
    k.add_argument("--skill", required=True)
    k.add_argument("--manifest", help="manifest JSON file from derive --out")
    k.add_argument("--enforce", action="store_true")

    a = ap.parse_args()
    if a.cmd == "corpus":
        directory = Path(a.dir) if Path(a.dir).is_absolute() else ROOT / a.dir
        stats = corpus_stats(directory)
        print(json.dumps(stats, indent=2))
        return 0
    if a.cmd == "derive":
        m = derive_manifest(a.patterns, a.hidden, a.exemplars, a.deliverables,
                            a.corpus_words, a.stacking_hits, a.extension)
        out = json.dumps(m, indent=2)
        print(out)
        if a.out:
            Path(a.out).write_text(out)
        return 0
    if a.cmd == "check":
        skill_dir = Path(a.skill) if Path(a.skill).is_absolute() else ROOT / a.skill
        manifest = json.loads(Path(a.manifest).read_text()) if a.manifest else None
        return check_skill(skill_dir, manifest, a.enforce)
    return 0


if __name__ == "__main__":
    sys.exit(main())
