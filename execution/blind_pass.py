#!/usr/bin/env python3
"""
Blind Pass — instrument the extraction blind-pass ritual (Harness Apex Wave 2b).

The blind-pass protocol (directives/embodiment-standard.md) was honor-system:
"generate outputs, place beside real pieces, judge, append an eval entry."
Result: ~32 eval_set entries for ~370 skills. This tool makes the *ritual*
unskippable and the *record* automatic. The side-by-side judgment itself stays
human/model — this tool never judges.

Commands:
    prepare --expert <slug>
        Verifies extractions/<slug>/reference-corpus/ contains ≥2 real
        published pieces (non-empty files). Prints exactly what to collect
        if missing. Exit 0 = corpus ready, 1 = not ready.

    record --expert <slug> --verdict PASS|FAIL --notes "..."
           [--generated <path>] [--reference <path>]
        Refuses if the corpus isn't ready (the ritual is unskippable).
        Appends a structured entry to
        evolution_store/ground_truth/eval_set_v1.jsonl (schema-compatible
        with existing Extraction entries) + a ledger line under
        extractions/<slug>/blind-pass-log.md. Exit 0.

    status --expert <slug>
        Shows corpus state + every recorded verdict for the slug.

chain_runner.py finalize (--type Extraction) queries recorded_verdicts()
and refuses without a verdict unless --skip-blind-pass (logged override).
Extractions stay cost-ungated per Farrice's standing decision 2026-06-09 —
this is a quality latch, not a spend gate.
"""

import argparse
import json
import re
import sys
from datetime import datetime, date
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parent.parent
EXTRACTIONS_DIR = ROOT / "extractions"
EVAL_SET = ROOT / "evolution_store" / "ground_truth" / "eval_set_v1.jsonl"

MIN_CORPUS_PIECES = 2

# Files that don't count as reference pieces.
_IGNORED_NAMES = {".DS_Store", "README.md", ".gitkeep"}


# ─────────────────────────────────────────────────────────
# Corpus inspection
# ─────────────────────────────────────────────────────────

def corpus_dir(slug: str) -> Path:
    return EXTRACTIONS_DIR / slug / "reference-corpus"


def corpus_files(slug: str) -> List[Path]:
    """Non-empty, non-hidden files under extractions/<slug>/reference-corpus/."""
    d = corpus_dir(slug)
    if not d.is_dir():
        return []
    out = []
    for p in sorted(d.rglob("*")):
        if not p.is_file():
            continue
        if p.name in _IGNORED_NAMES or p.name.startswith("."):
            continue
        try:
            if p.stat().st_size == 0:
                continue
        except OSError:
            continue
        out.append(p)
    return out


def corpus_ready(slug: str) -> bool:
    return len(corpus_files(slug)) >= MIN_CORPUS_PIECES


def _print_collect_instructions(slug: str, files: List[Path]) -> None:
    d = corpus_dir(slug)
    need = MIN_CORPUS_PIECES - len(files)
    print(f"CORPUS NOT READY — {d.relative_to(ROOT)} has {len(files)} valid piece(s); "
          f"need ≥{MIN_CORPUS_PIECES} ({need} more).")
    if files:
        for f in files:
            print(f"  present: {f.relative_to(ROOT)}")
    print("Collect exactly this:")
    print(f"  1. mkdir -p \"{d}\"")
    print(f"  2. Save {need} more VERBATIM published piece(s) by the expert into that folder")
    print("     (.md/.txt — real posts/articles/transcripts of published work, provenance line")
    print("     at the top: URL + date). Provenance-verified, NON-EMPTY files.")
    print("  3. Must NOT be pieces already quoted inside the skill files (the blind pass")
    print("     judges against unseen work — embodiment-standard.md Blind-Pass Protocol step 2).")
    print(f"  4. Re-run: python3 execution/blind_pass.py prepare --expert {slug}")


# ─────────────────────────────────────────────────────────
# Eval-set access
# ─────────────────────────────────────────────────────────

def _load_eval_entries() -> List[Dict[str, Any]]:
    if not EVAL_SET.exists():
        return []
    entries = []
    for line in EVAL_SET.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return entries


def _next_eval_id(entries: List[Dict[str, Any]]) -> str:
    top = 0
    for e in entries:
        m = re.match(r"EVAL-(\d+)", str(e.get("id", "")))
        if m:
            top = max(top, int(m.group(1)))
    return f"EVAL-{top + 1:03d}"


def _slug_match(slug: str, domain: str) -> bool:
    """Exact match, or one contains the other (legacy entries used loose
    domain names, e.g. 'dara-denney-static-ads' vs skill dir
    'dara-denney-meta-ads' — those do NOT match; containment is the floor)."""
    if not slug or not domain:
        return False
    slug, domain = slug.lower(), domain.lower()
    return slug == domain or slug in domain or domain in slug


def recorded_verdicts(slug: str) -> List[Dict[str, Any]]:
    """Every Extraction eval entry that matches this slug.

    Importable API — chain_runner.py's extraction latch calls this.
    Legacy entries (pre-blind_pass.py, e.g. EVAL-032..034) count: they ARE
    recorded blind-pass verdicts, just hand-appended.
    """
    out = []
    for e in _load_eval_entries():
        if e.get("task_type") != "Extraction":
            continue
        if _slug_match(slug, str(e.get("domain", ""))):
            out.append(e)
    return out


def latest_verdict(slug: str) -> Optional[str]:
    """'PASS' | 'FAIL' | None. Legacy entries map from expected_verdict."""
    entries = recorded_verdicts(slug)
    if not entries:
        return None
    e = entries[-1]
    bp = e.get("blind_pass") or {}
    if bp.get("verdict") in ("PASS", "FAIL"):
        return bp["verdict"]
    ev = str(e.get("expected_verdict", "")).upper()
    if ev.startswith("SHIP") or "PASS" in ev:
        return "PASS"
    if "FAIL" in ev or "BLOCKED" in ev:
        return "FAIL"
    return "PASS"  # a recorded ship entry without explicit verdict = shipped


# ─────────────────────────────────────────────────────────
# Commands
# ─────────────────────────────────────────────────────────

def cmd_prepare(slug: str) -> int:
    files = corpus_files(slug)
    if len(files) >= MIN_CORPUS_PIECES:
        print(f"CORPUS READY — {len(files)} provenance piece(s) in "
              f"{corpus_dir(slug).relative_to(ROOT)}:")
        for f in files:
            print(f"  - {f.relative_to(ROOT)} ({f.stat().st_size} bytes)")
        print("Next: generate 1-2 outputs with the skill's Tier-1 workflow, judge side-by-side")
        print("per directives/embodiment-standard.md, then:")
        print(f"  python3 execution/blind_pass.py record --expert {slug} "
              "--verdict PASS|FAIL --notes \"...\"")
        return 0
    _print_collect_instructions(slug, files)
    return 1


def cmd_record(slug: str, verdict: str, notes: str,
               generated: str = "", reference: str = "") -> int:
    files = corpus_files(slug)
    if len(files) < MIN_CORPUS_PIECES:
        print("RECORD REFUSED — the blind pass requires a real reference corpus first.")
        _print_collect_instructions(slug, files)
        return 1

    entries = _load_eval_entries()
    eval_id = _next_eval_id(entries)
    now = datetime.now().isoformat(timespec="seconds")

    entry = {
        "id": eval_id,
        "source": f"blind-pass-{slug}-{date.today().isoformat()}",
        "task_type": "Extraction",
        "domain": slug,
        "user_request": f"blind-pass verdict for extraction '{slug}' (instrumented ritual)",
        "produced_by": "blind_pass.py record — side-by-side judgment stays human/model; this tool records it",
        "expected_verdict": ("SHIP" if verdict == "PASS"
                             else "FAIL — fix weakest checklist item, retry once, else ship B-tier with the gap named"),
        "blind_detection": {"identified_real": None, "preferred": None},
        "self_assessment": notes,
        "blind_pass": {
            "verdict": verdict,
            "generated": generated,
            "reference": reference,
            "corpus_files": [str(f.relative_to(ROOT)) for f in files],
            "recorded_at": now,
        },
        "calibrated_by_human": False,
    }
    EVAL_SET.parent.mkdir(parents=True, exist_ok=True)
    with open(EVAL_SET, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    # Ledger line under the extraction dir
    log_path = EXTRACTIONS_DIR / slug / "blind-pass-log.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        log_path.write_text(
            f"# Blind-Pass Log — {slug}\n\n"
            "Recorded by `execution/blind_pass.py` per "
            "`directives/embodiment-standard.md` Blind-Pass Protocol.\n\n",
            encoding="utf-8",
        )
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(
            f"- {now} — **{verdict}** — eval: {eval_id}"
            + (f" — generated: `{generated}`" if generated else "")
            + (f" — reference: `{reference}`" if reference else "")
            + f" — corpus: {len(files)} piece(s) — {notes}\n"
        )

    print(f"RECORDED — {verdict} for '{slug}'")
    print(f"  eval entry:  {eval_id} → {EVAL_SET.relative_to(ROOT)}")
    print(f"  ledger line: {log_path.relative_to(ROOT)}")
    if verdict == "FAIL":
        print("  FAIL path (embodiment-standard.md): fix the weakest checklist item, retry once,")
        print("  else ship B-tier with the gap named in the finalize notes.")
    return 0


def cmd_status(slug: str) -> int:
    files = corpus_files(slug)
    ready = len(files) >= MIN_CORPUS_PIECES
    print(f"Blind-pass status — {slug}")
    print(f"  corpus: {'READY' if ready else 'NOT READY'} "
          f"({len(files)}/{MIN_CORPUS_PIECES} piece(s) in {corpus_dir(slug).relative_to(ROOT)})")
    for f in files:
        print(f"    - {f.relative_to(ROOT)}")
    verdicts = recorded_verdicts(slug)
    if not verdicts:
        print("  verdicts: NONE recorded — finalize --type Extraction will refuse without one")
        print(f"    run: python3 execution/blind_pass.py prepare --expert {slug}")
        return 0
    print(f"  verdicts: {len(verdicts)} recorded (latest = {latest_verdict(slug)})")
    for e in verdicts:
        bp = e.get("blind_pass") or {}
        v = bp.get("verdict") or e.get("expected_verdict", "?")
        when = bp.get("recorded_at", e.get("source", "?"))
        print(f"    - {e.get('id', '?')} · {v} · {when}")
    log_path = EXTRACTIONS_DIR / slug / "blind-pass-log.md"
    print(f"  ledger: {log_path.relative_to(ROOT)} "
          f"({'exists' if log_path.exists() else 'missing'})")
    return 0


# ─────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Blind Pass — instrumented extraction blind-pass ritual (record is automatic, judgment stays human/model)")
    sub = parser.add_subparsers(dest="command")

    prep = sub.add_parser("prepare", help="Verify reference corpus (≥2 real published pieces); exit 1 + collect list if missing")
    prep.add_argument("--expert", required=True, help="Extraction slug == skill dir name (extractions/<slug>/reference-corpus/)")

    rec = sub.add_parser("record", help="Record a side-by-side PASS/FAIL verdict → eval_set entry + ledger line")
    rec.add_argument("--expert", required=True)
    rec.add_argument("--verdict", required=True, choices=["PASS", "FAIL"])
    rec.add_argument("--notes", required=True, help="What the judgment saw (which real pieces, what gave it away / what held)")
    rec.add_argument("--generated", default="", help="Path to the skill-generated output judged")
    rec.add_argument("--reference", default="", help="Path to the real published piece(s) judged against")

    st = sub.add_parser("status", help="Corpus state + recorded verdicts for a slug")
    st.add_argument("--expert", required=True)

    args = parser.parse_args()
    if args.command == "prepare":
        return cmd_prepare(args.expert)
    if args.command == "record":
        return cmd_record(args.expert, args.verdict, args.notes, args.generated, args.reference)
    if args.command == "status":
        return cmd_status(args.expert)
    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
