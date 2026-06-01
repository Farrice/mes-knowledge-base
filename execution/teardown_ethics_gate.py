#!/usr/bin/env python3
"""
Teardown Ethics Gate — deterministic constructive/legal floor for the
Teardown Engine (.agent/workflows/teardown.md).

WHY THIS EXISTS
---------------
Publicly tearing down a named brand's copy ("brand-jack / authority-jack") is a
powerful lead engine — and a reputational/legal liability if it slips into a
hit piece (defamation), reproduces the target's copyrighted copy wholesale, or
asserts unverified factual claims about them. Per the banned-pattern rule
("AI-Memory-Dependent Observability is BANNED: never ship infra requiring Claude
manual invocation; always pair with a deterministic backstop"), the persona's
"be constructive" judgment MUST be floored by a deterministic mechanism.

This module is that backstop, modeled on execution/context_ethics_gate.py. It
does NOT replace persona judgment — it floors three structural risks:
  1. CONTEMPT framing (hit-piece shape) → not constructive.
  2. COPYRIGHT: verbatim reproduction of the target's copy beyond fair-use-ish
     excerpting (transform, don't republish).
  3. UNGROUNDED factual claims ABOUT the brand → defer to verify_proof_ledger.

The ethic, made deterministic: tear down the COPY, never the PEOPLE; excerpt +
transform, never reproduce; assert nothing about the brand you can't source.

MODES
-----
  intake  Catch a hit-piece framing in the REQUEST before any spend.
            python3 execution/teardown_ethics_gate.py intake --brand "Acme" \
                --angle their-own-customer --request "..."
  check   Load-bearing pass on the teardown artifact (constructive + copyright
          + factual). Pass --recon to enable the copyright guard.
            python3 execution/teardown_ethics_gate.py check \
                --file .tmp/teardown/<slug>/teardown.md \
                --recon .tmp/teardown/<slug>/recon.md
  public  Strictest pass on the FINAL post text before it ships.
            python3 execution/teardown_ethics_gate.py public --file post.md --recon recon.md
  report  Summarize recent verdicts.
            python3 execution/teardown_ethics_gate.py report --days 7

Exit: 2 on BLOCK (so a `// turbo` line halts), 0 otherwise. LOG:
.agent/teardown-ethics-log.jsonl
"""

import sys
import re
import json
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional

ROOT = Path(__file__).resolve().parent.parent
LOG_PATH = ROOT / ".agent" / "teardown-ethics-log.jsonl"

TEARDOWN_WORKFLOWS = {"teardown", "brand-teardown", "jackpost"}

# Copyright guard thresholds.
MAX_VERBATIM_WORDS = 40        # contiguous run of the target's copy reproduced
MAX_ASSET_REPRO_FRACTION = 0.25  # share of a captured asset reproduced verbatim

# ── CONTEMPT (hit-piece) markers — tear down COPY, never PEOPLE ──────────────
_CONTEMPT = [
    r"\bexpos(e|ing|é)\b", r"\bdestroy(ing|ed)?\b", r"\broast(ing|ed)?\b",
    r"\bincompeten(t|ce)\b", r"\bclueless\b", r"\bidiots?\b", r"\bmorons?\b",
    r"\bdumb(ass)?\b", r"\bstupid\b", r"\bpathetic\b", r"\bgarbage\b",
    r"\btrash\b", r"\bawful\b", r"\bterrible\b", r"\bworst\b", r"\bhate\b",
    r"\bscam(mers?|ming)?\b", r"\bfrauds?\b", r"\bripoffs?\b", r"\blazy\b",
    r"\bembarrass(ing|ment)\b", r"\bhumiliat(e|ing)\b", r"\bcan'?t write\b",
    r"\bdon'?t (know|understand) (their|the) (customer|audience|market)\b",
]

# ── CONSTRUCTIVE markers — at least one must be present (check/public) ───────
_CONSTRUCTIVE = [
    r"\bwhat (they|.{0,15}) (got|did) right\b", r"\bto their credit\b",
    r"\bwhat (they|.{0,15}) did well\b", r"\bsmart (move|play|choice)\b",
    r"\bwhat i'?d (improve|change|test|try)\b", r"\bthe opportunity\b",
    r"\bcould be (stronger|sharper|tighter)\b", r"\bhere'?s the (fix|upgrade)\b",
    r"\bwhat'?s (left on the table|missing)\b", r"\bnot a knock\b",
    r"\bthey'?re not wrong\b", r"\bgreat (brand|product|company)\b",
    r"\bsolid (foundation|positioning|copy)\b", r"\bwith respect\b",
    # Credit-giving phrasings (broadened 2026-06-01 — posts that genuinely
    # lead with credit were false-REVIEWing on too-narrow a marker list).
    r"\bcredit where it'?s due\b", r"\bto be (fair|clear)\b",
    r"\bthe craft is real\b", r"\bnails? (the )?surface\b",
    r"\bone of the cleanest\b", r"\b(is|are) (genuinely )?sharp\b",
    r"\bhonest,? (and )?clear\b", r"\bmost of .{0,25} (copy|site) is\b",
    r"\bexactly right\b", r"\bclean(est)? (line|copy|promise)\b",
    r"\band it converts\b", r"\bnobody (finishes|watches) .{0,30}(lied to|feeling)\b",
]

# ── Factual-claim-ABOUT-the-brand patterns (must be sourced) ────────────────
_BRAND_FACTUAL = [
    r"\bthey (spend|spent|make|made|earn|raised|lost)\s+\$?\d", r"\b\d+%\s+(of\s+)?their\b",
    r"\btheir (revenue|conversion|churn|cac|ltv|valuation|arr|mrr)\s+(is|was|=)\s*\$?\d",
    r"\b(they have|they'?ve got)\s+\d[\d,]*\s+(customers|users|employees|subscribers)\b",
    r"\b(founded|launched|raised|acquired)\s+in\s+\d{4}\b",
]
_SOURCE_NEARBY = re.compile(r"https?://|\[(VERIFIED|LIKELY|UNCONFIRMED)\]|\(source", re.I)


def _hits(patterns: List[str], text: str) -> List[str]:
    out = []
    for p in patterns:
        m = re.search(p, text, re.I)
        if m:
            out.append(m.group(0).strip())
    return out


# Negators that flip a contempt word into a constructive refusal ("NOT lazy",
# "the opposite of clueless", "never incompetent"). A contempt match preceded by
# one of these within a short window is the copy *refusing* the slur, not slinging it.
_NEGATORS = re.compile(
    r"(not|n'?t|never|opposite of|far from|hardly|isn'?t|aren'?t|wasn'?t|"
    r"weren'?t|anything but|no longer|nobody'?s)\W+(\w+\W+){0,3}$", re.I)


def _contempt_hits(text: str) -> List[str]:
    """Contempt words that are NOT negated (negation = the copy refusing the slur)."""
    out = []
    for p in _CONTEMPT:
        for m in re.finditer(p, text, re.I):
            preceding = text[max(0, m.start() - 40): m.start()]
            if _NEGATORS.search(preceding):
                continue  # "not lazy" / "the opposite of clueless" → constructive
            out.append(m.group(0).strip())
            break
    return out


def _normalize_words(text: str) -> List[str]:
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", text.lower())).split()


def _copyright_flags(artifact: str, recon: str) -> List[str]:
    """Flag verbatim reproduction of the target's captured copy in the artifact."""
    if not recon.strip():
        return []
    flags: List[str] = []
    art_words = _normalize_words(artifact)
    recon_words = _normalize_words(recon)
    if len(recon_words) < MAX_VERBATIM_WORDS or len(art_words) < MAX_VERBATIM_WORDS:
        return []
    art_join = " " + " ".join(art_words) + " "
    # Slide an N-word window over the recon copy; if that exact run appears in
    # the artifact, it's a verbatim reproduction beyond excerpt-and-transform.
    n = MAX_VERBATIM_WORDS
    seen = set()
    for i in range(0, len(recon_words) - n + 1):
        window = " ".join(recon_words[i:i + n])
        if window in seen:
            continue
        seen.add(window)
        if (" " + window + " ") in art_join:
            flags.append(f"verbatim ≥{n}-word run of target copy reproduced: \"{window[:60]}…\"")
            if len(flags) >= 3:
                break
    return flags


def evaluate(mode: str, text: str, recon: str = "") -> Dict[str, Any]:
    """Deterministic structural checks. Returns verdict (PASS/REVIEW/BLOCK) + flags."""
    contempt = _contempt_hits(text)
    constructive = _hits(_CONSTRUCTIVE, text)
    flags: List[str] = []
    verdict = "PASS"

    # 1) Contempt framing — present in any mode = a hit-piece shape.
    if contempt:
        flags.append(f"CONTEMPT framing (tear down the copy, not the people): {contempt[:4]}")
        verdict = "BLOCK"

    # 2) Constructive requirement (check/public only — intake is request-only).
    if mode in ("check", "public") and not constructive:
        flags.append("NO constructive marker found — add 'what they got right' / "
                     "'what I'd improve' (the jackpost constructive triad).")
        verdict = "BLOCK" if verdict == "BLOCK" else "REVIEW"

    # 3) Copyright / verbatim reproduction (check/public, needs --recon).
    if mode in ("check", "public") and recon:
        cflags = _copyright_flags(text, recon)
        if cflags:
            flags.extend(cflags)
            flags.append("→ excerpt + transform; do not republish their copy at length.")
            verdict = "BLOCK" if verdict == "BLOCK" else "REVIEW"

    # 4) Ungrounded factual claims ABOUT the brand → defer to verify_proof_ledger.
    if mode in ("check", "public"):
        for p in _BRAND_FACTUAL:
            for m in re.finditer(p, text, re.I):
                seg = text[max(0, m.start() - 80): m.end() + 80]
                if not _SOURCE_NEARBY.search(seg):
                    flags.append(f"UNSOURCED brand claim — label via verify_proof_ledger or cut: \"{m.group(0)}\"")
                    verdict = "BLOCK" if verdict == "BLOCK" else "REVIEW"
                    break

    if verdict == "PASS":
        flags.append("Constructive frame present; no verbatim reproduction; "
                     "brand claims sourced or absent.")
    return {"mode": mode, "verdict": verdict, "flags": flags,
            "contempt": contempt, "constructive": bool(constructive)}


def log_verdict(verdict: str, mode: str, brand: str = "", workflow: str = "teardown",
                flags: Optional[List[str]] = None, note: str = "") -> Dict[str, Any]:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "verdict": (verdict or "UNKNOWN").upper(), "mode": mode,
        "brand": brand, "workflow": workflow, "flags": flags or [], "note": note,
    }
    with LOG_PATH.open("a") as f:
        f.write(json.dumps(entry) + "\n")
    return entry


def _print(result: Dict[str, Any], brand: str) -> None:
    icon = {"PASS": "✅", "REVIEW": "⚠️ ", "BLOCK": "⛔"}.get(result["verdict"], "?")
    print(f"{icon} TEARDOWN ETHICS [{result['mode']}] — {result['verdict']}"
          + (f" · {brand}" if brand else ""))
    for fl in result["flags"]:
        print(f"   - {fl}")


def cmd_intake(args) -> int:
    text = args.request or f"teardown of {args.brand} angle {args.angle}"
    result = evaluate("intake", text)
    _print(result, args.brand)
    log_verdict(result["verdict"], "intake", args.brand, args.workflow, result["flags"])
    return 2 if result["verdict"] == "BLOCK" else 0


def cmd_check(args, mode: str) -> int:
    text = Path(args.file).read_text() if args.file and Path(args.file).exists() else (args.text or "")
    recon = Path(args.recon).read_text() if args.recon and Path(args.recon).exists() else ""
    result = evaluate(mode, text, recon)
    _print(result, args.brand)
    log_verdict(result["verdict"], mode, args.brand, args.workflow, result["flags"])
    return 2 if result["verdict"] == "BLOCK" else 0


def cmd_report(args) -> int:
    if not LOG_PATH.exists():
        print("No teardown-ethics verdicts logged yet.")
        return 0
    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    entries = []
    for line in LOG_PATH.read_text().splitlines():
        try:
            e = json.loads(line)
            if datetime.strptime(e["ts"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc) >= cutoff:
                entries.append(e)
        except Exception:
            continue
    counts: Dict[str, int] = {}
    for e in entries:
        counts[e.get("verdict", "?")] = counts.get(e.get("verdict", "?"), 0) + 1
    print(f"Teardown ethics — last {args.days}d: {len(entries)} verdicts {counts}")
    for e in [x for x in entries if x.get("verdict") in ("BLOCK", "REVIEW")]:
        print(f"  {e['ts']} [{e['mode']}] {e['verdict']} · {e.get('brand','')}: {(e.get('flags') or [''])[0][:80]}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(prog="teardown_ethics_gate.py")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("intake", "check", "public"):
        s = sub.add_parser(name)
        s.add_argument("--brand", default="")
        s.add_argument("--angle", default="")
        s.add_argument("--request", default="")
        s.add_argument("--file", default="")
        s.add_argument("--text", default="")
        s.add_argument("--recon", default="")
        s.add_argument("--workflow", default="teardown")
    r = sub.add_parser("report")
    r.add_argument("--days", type=int, default=7)
    args = p.parse_args()
    if args.cmd == "intake":
        return cmd_intake(args)
    if args.cmd in ("check", "public"):
        return cmd_check(args, args.cmd)
    if args.cmd == "report":
        return cmd_report(args)
    return 2


if __name__ == "__main__":
    sys.exit(main())
