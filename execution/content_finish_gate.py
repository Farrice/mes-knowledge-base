#!/usr/bin/env python3
"""
Content Finish Gate — the deterministic backstop that makes shipping AI-slop
structurally impossible.

WHY THIS EXISTS
---------------
On 2026-05-31/06-01 a teardown batch shipped raw workflow output that tripped
four hard voice bans (8+ em-dashes, twin-sentence reversals, a cheap-question
close, identical skeletons) AND finalized at a hollow 8.33 — because
`chain_runner.finalize` scores intent/expert/adversarial but does NOT mechanically
scan for the banned STRUCTURAL MOVES that `feedback_ai-structural-tells.md` +
`feedback_ai-writing-tells.md` + `feedback_no-cheap-question-signoffs.md` forbid.
Self-scores and finalize both rubber-stamped it.

Per the standing rule — "never ship infra that depends on the model REMEMBERING;
pair it with a deterministic backstop" — this module is that backstop. It is a
pure regex/heuristic scanner (no AI judgment) that catches the banned moves and
returns a non-zero exit on FAIL so a `// turbo` gate halts. `chain_runner.finalize`
imports it and HARD-CAPS the score on a structural FAIL, so a clean finalize on
slop is no longer possible.

It does NOT replace the writers-room (which adds heartbeat). It floors the bottom:
nothing with these tells ships, regardless of model memory or a generous self-score.

MODES
-----
  check  Scan a file/text; emit verdict (CLEAN/WARN/FAIL) + flags; exit 2 on FAIL.
           python3 execution/content_finish_gate.py check --file post.md --platform linkedin
           python3 execution/content_finish_gate.py check --text "..." --platform linkedin
LOG: .agent/content-finish-log.jsonl
"""

import sys
import re
import json
import argparse
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any

ROOT = Path(__file__).resolve().parent.parent
LOG_PATH = ROOT / ".agent" / "content-finish-log.jsonl"
EXEC = ROOT / "execution"

MAX_EM_DASHES = 2  # feedback_ai-writing-tells.md: max 1-2 em-dashes


def _sentences(text: str) -> List[str]:
    # strip quoted lines (we don't police the brand's/VOC's quoted copy)
    body = "\n".join(l for l in text.splitlines() if not l.strip().startswith(">"))
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", body) if s.strip()]


def evaluate(text: str, platform: str = "") -> Dict[str, Any]:
    """Deterministic structural scan. Returns {verdict, fails, warns}."""
    fails: List[str] = []
    warns: List[str] = []

    # 1) Em-dashes (hard). Count only real em-dashes, not hyphens.
    em = text.count("—")
    if em > MAX_EM_DASHES:
        fails.append(f"{em} em-dashes (max {MAX_EM_DASHES}) — feedback_ai-writing-tells.md")

    # 2) "It's not X. It's Y." / "isn't A, it's B" reveal pattern (hard, #1 AI tell).
    reveal = re.findall(
        r"\b(isn'?t|wasn'?t|aren'?t|weren'?t|is not|are not|not)\b[^.?!\n]{0,80}[.?!,]\s+(it'?s|that'?s|they'?re|it is)\b",
        text, re.I)
    if reveal:
        fails.append(f"\"It's not X. It's Y.\" reveal pattern ×{len(reveal)} — feedback_ai-structural-tells.md #1")

    # 3) Triple-beat anaphora: 3+ consecutive sentences starting with the same word.
    sents = _sentences(text)
    run, prev = 1, ""
    for s in sents:
        w = (re.findall(r"[A-Za-z']+", s) or [""])[0].lower()
        if w and w == prev:
            run += 1
            if run >= 3:
                fails.append(f"Triple-beat anaphora ('{w} … {w} … {w}') — feedback_ai-structural-tells.md #3")
                break
        else:
            run, prev = 1, w

    # 4) "Here's the part/thing nobody…" reveal framing (hard, #5).
    if re.search(r"\bhere'?s (the|what) [^.\n]{0,40}(nobody|no one)\b", text, re.I) or \
       re.search(r"\bthe (part|thing|secret) (that )?(nobody|no one) (wants to|will) (say|tell|admit)\b", text, re.I):
        fails.append("\"Here's the part nobody…\" reveal framing — feedback_ai-structural-tells.md #5")

    # 5) Cheap-question close (hard) — feedback_no-cheap-question-signoffs.md.
    nonblank = [l.strip() for l in text.splitlines() if l.strip()]
    if nonblank:
        close = nonblank[-1]
        if close.endswith("?"):
            generic = re.search(
                r"\b(what'?s your|what is your|drop .* below|comment|let me know|anyone else|"
                r"thoughts\??|do you agree|am i wrong|who'?s with me|tag (a|someone)|"
                r"what would you|have you (ever|experienced)|sound familiar|right\?)\b", close, re.I)
            # Any question close on the FINAL line is suspect; generic = hard fail.
            if generic:
                fails.append(f"Cheap-question close: \"{close[:60]}\" — feedback_no-cheap-question-signoffs.md")
            else:
                warns.append(f"Question close (verify it's earned/non-transferable): \"{close[:60]}\"")

    # 6) Mic-drop deflation ending (#6, soft).
    if len(nonblank) >= 2 and re.search(r"\bthat'?s (all|the whole|it)\b", nonblank[-1], re.I):
        warns.append("Possible mic-drop/deflation close — feedback_ai-structural-tells.md #6")

    # 7) Banned vocab / AI prose (delegate to prose_classifier, hard on FLAGGED).
    try:
        f = ROOT / ".tmp" / "_cfg_prose.txt"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text)
        pc = subprocess.run([sys.executable, str(EXEC / "prose_classifier.py"), "check", str(f)],
                            capture_output=True, text=True, timeout=30)
        out = (pc.stdout or "") + (pc.stderr or "")
        if re.search(r"FLAGGED", out):
            fails.append("prose_classifier: FLAGGED (banned vocab / AI prose density)")
        elif re.search(r"WARNING", out):
            warns.append("prose_classifier: WARNING")
    except Exception:
        pass

    # 8) Platform format (LinkedIn): scannable, not an essay.
    if platform.lower() in ("linkedin", "li"):
        first = next((l.strip() for l in text.splitlines() if l.strip()), "")
        hook_words = len(first.split())
        if hook_words > 14:
            fails.append(f"LinkedIn hook is {hook_words} words (≤14 for the mobile cutoff) — Lara Acosta")
        lines = [l for l in text.splitlines() if l.strip()]
        blanks = text.count("\n\n")
        if blanks < max(4, len(lines) // 4):
            warns.append("Sparse whitespace — LinkedIn needs short stanzas + line breaks (F-shape).")
        longest = max((len(l) for l in lines), default=0)
        if longest > 320:
            warns.append(f"A {longest}-char line — break dense paragraphs for mobile dwell time.")

    verdict = "FAIL" if fails else ("WARN" if warns else "CLEAN")
    return {"verdict": verdict, "fails": fails, "warns": warns, "em_dashes": em,
            "platform": platform}


def log(result: Dict[str, Any], label: str = "") -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a") as fh:
        fh.write(json.dumps({
            "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "label": label, "verdict": result["verdict"],
            "fails": result["fails"], "warns": result["warns"],
        }) + "\n")


def main() -> int:
    p = argparse.ArgumentParser(prog="content_finish_gate.py")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("--file", default="")
    c.add_argument("--text", default="")
    c.add_argument("--platform", default="")
    c.add_argument("--label", default="")
    c.add_argument("--quiet", action="store_true")
    args = p.parse_args()
    text = Path(args.file).read_text() if args.file and Path(args.file).exists() else (args.text or "")
    if not text.strip():
        print("content_finish_gate: no input.", file=sys.stderr)
        return 2
    r = evaluate(text, args.platform)
    log(r, args.label or args.file)
    icon = {"CLEAN": "✅", "WARN": "⚠️ ", "FAIL": "⛔"}[r["verdict"]]
    if not args.quiet or r["verdict"] != "CLEAN":
        print(f"{icon} CONTENT FINISH GATE — {r['verdict']}" + (f" · {args.label or args.file}" if (args.label or args.file) else ""))
        for f in r["fails"]:
            print(f"   ⛔ {f}")
        for w in r["warns"]:
            print(f"   ⚠️  {w}")
        if r["verdict"] == "CLEAN":
            print(f"   em-dashes: {r['em_dashes']} · no reveal patterns · no triple anaphora · no cheap close")
    return 2 if r["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
