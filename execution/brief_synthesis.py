#!/usr/bin/env python3
"""brief_synthesis.py — the judged analyst pass over the mission sweep
(2026-08-20). Fills .agent/sweep/synthesis.json — the prose slots
mission_brief.py designed on day one and nothing ever wrote.

WHY (Farrice, verbatim): "I want these to provide me with true insight so I
can get the full read on what's going on… telling me exactly what I need to
do and what options I have. Some sections feel dry, like they're just stating
facts versus actually informing."

THE CONTRACT IS THE SAFETY. The judge writes ONLY into mission_brief.SLOTS
(lede, next_move, why, caveats, operator_read, state_read, options). Every
number, path, date and link on a brief is mechanical; judged prose may not
contain a digit, slash, URL or filename (FORBIDDEN_SYNTHESIS_VALUE) — the
canonical validator (mission_brief.py validate-synthesis) gates the write
fail-closed. A bad synthesis leaves the previous one in place.

COST: runs through `claude -p` (headless Claude Code) on the subscription —
no metered API, $0 marginal. One batched call per run.

Usage:
    python3 execution/brief_synthesis.py run [--model MODEL] [--timeout S]
    python3 execution/brief_synthesis.py status
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "execution"))

import mission_brief as mbrief  # noqa: E402 — slots, narrative mining, validator CLI
from degrade import degraded  # noqa: E402

SWEEP = ROOT / ".agent" / "sweep" / "latest.json"
SYNTHESIS = ROOT / ".agent" / "sweep" / "synthesis.json"
BOARD = "mission-board"
PY = sys.executable or "python3"


def thread_pack(slug, t):
    """The compact fact pack the analyst reads for one thread. Everything the
    deterministic layer knows, nothing it doesn't."""
    narr = mbrief.handoff_narrative(t)
    contract = mbrief.load_contract(slug)
    outcomes = [{"mission": m["title"][:120], "status": m.get("status"),
                 "outcome": m.get("outcome"), "verdict": m.get("verdict"),
                 "open": m.get("open"), "serves": m.get("serves")}
                for m in t.get("missions", []) if m.get("outcome") or m.get("open")]
    delivs = [{"date": d["date"][:10], "what": d["output"][:160],
               "notes": (d.get("notes") or "")[:160]}
              for d in t.get("deliverables", [])[:6]]
    return {
        "slug": slug,
        "title": t.get("title"),
        "status": t.get("status"), "stage": t.get("stage"),
        "pinned": bool(t.get("pin")),
        "idle_days": mbrief.days_since(t.get("last_active")),
        "resume_hint": t.get("resume_hint"), "unfinished": t.get("unfinished"),
        "counts": {"sessions": len(t.get("sessions", [])),
                   "deliverables": len(t.get("deliverables", [])),
                   "assets": len(t.get("assets", []))},
        "handoff_purpose": narr.get("purpose"),
        "handoff_state": narr.get("state"),
        "handoff_remaining": narr.get("remaining"),
        "handoff_risks": narr.get("risks"),
        "handoff_is_stub": bool(narr.get("stub")),
        "felt_standard": contract.get("felt_standard"),
        "mission_outcomes": outcomes,
        "recent_deliverables": delivs,
    }


PROMPT = """You are the senior intelligence officer who writes the operator's daily
brief for Farrice — a solo operator running an AI-orchestration studio whose active
sprint is collecting five thousand dollars a month from claim-safe content for funded
health and performance brands. You are reading the raw fact packs for every live work
thread. Your job is the layer the machine cannot do: judgment. What does each thread
MEAN, what should he do, what are his real options.

REGISTER — commander's brief, not a status report:
- Bottom line up front. Every lede answers "so what" in the first sentence.
- Assessments carry conviction ("this is stalling because…", "the leverage here is…").
  Never hedge-pad. Never restate counts the page already shows.
- next_move is ONE imperative sentence he could act on within the hour.
- options: two or three REAL choices, recommended one first, each with the tradeoff
  it carries ("costs momentum on…", "buys focus but abandons…"). Options must
  genuinely differ — resume/park/kill framings, sequencing calls, scope cuts.
- state_read: one short paragraph — momentum, risk, and how this thread relates to
  the sprint. An analyst's read, not a summary.
- caveats: what is stale, unverified, or thin in the record itself.
- operator_read: the one line you'd tell him in the hallway.
- why (optional object): only when a numbered decision item needs sharper reasoning.

HARD RULES (a validator rejects your whole output on violation):
- NO digits anywhere — write numbers as words ("twenty-one days idle").
- NO file paths, filenames, slashes, or URLs.
- Plain words. Banned: delve, leverage (as a verb), robust, seamless, comprehensive,
  landscape, "it's not X it's Y" constructions.
- If a thread's pack is thin (stub handoff, no outcomes), say so plainly in caveats
  and keep the lede modest — never invent specifics the pack doesn't contain.

OUTPUT — exactly one JSON object, no prose around it, no code fences:
- One key per thread slug (use every slug provided), plus a "mission-board" key.
- Each entry MUST have: lede, next_move, caveats, operator_read (strings).
- Each entry MAY have: state_read (string), options (list of at most three
  {"action": …, "why": …}), why (object keyed by decision-item index as a string).
- mission-board: the portfolio read — where attention is concentrated vs where the
  sprint needs it, in the same keys (options here = portfolio-level moves).

FACT PACKS:
"""


def _extract_json(text):
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```\w*\n|\n```$", "", text.strip("`").strip())
    start = text.find("{")
    if start < 0:
        return None
    depth = 0
    for i, ch in enumerate(text[start:], start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(text[start:i + 1])
                except ValueError:
                    return None
    return None


def _validate():
    r = subprocess.run([PY, str(ROOT / "execution" / "mission_brief.py"),
                        "validate-synthesis"], capture_output=True, text=True, timeout=60)
    try:
        return json.loads(r.stdout)
    except ValueError:
        return {"valid": False, "errors": [f"validator crashed: {(r.stderr or '')[:200]}"]}


def _prune(synth, errors):
    """Drop only the offending entries so one bad slug never sinks the pass.
    A broken mission-board entry sinks everything (it is required)."""
    bad_slugs = set()
    for e in errors:
        if "mission-board is required" in e:
            return None
        m = (re.match(r"unknown thread slug: ([\w-]+)", e)
             or re.match(r"([\w-]+)[.:]", e))
        if m:
            bad_slugs.add(m.group(1))
    if BOARD in bad_slugs:
        return None
    for s in bad_slugs:
        synth.pop(s, None)
    return synth if synth.get(BOARD) else None


def cmd_run(args):
    bundle = mbrief.load(SWEEP)
    threads = bundle.get("threads") or {}
    if not threads:
        print("[brief_synthesis] no sweep bundle — run session_sweep first")
        return 0
    packs = [thread_pack(slug, t) for slug, t in threads.items()]
    prompt = PROMPT + json.dumps(packs, indent=1, ensure_ascii=False)

    try:
        r = subprocess.run(["claude", "-p", "--model", args.model, prompt],
                           capture_output=True, text=True, timeout=args.timeout)
        out = r.stdout
    except FileNotFoundError:
        print("[brief_synthesis] claude CLI not found — briefs stay facts-only (honest, not broken)")
        return 0
    except subprocess.TimeoutExpired:
        print(f"[brief_synthesis] analyst pass timed out at {args.timeout}s — previous synthesis kept")
        return 0

    synth = _extract_json(out or "")
    if not synth:
        degraded(None, "analyst pass returned no parseable JSON — previous synthesis kept", None)
        print("[brief_synthesis] FAILED: no parseable JSON in model output")
        return 1

    prev = SYNTHESIS.read_text(encoding="utf-8") if SYNTHESIS.exists() else None
    for attempt in range(2):
        SYNTHESIS.write_text(json.dumps(synth, indent=1, ensure_ascii=False) + "\n",
                             encoding="utf-8")
        v = _validate()
        if v.get("valid"):
            stamp = {"generated": datetime.now().isoformat(timespec="seconds"),
                     "entries": len(synth), "model": args.model}
            (SYNTHESIS.parent / "synthesis-receipt.json").write_text(
                json.dumps(stamp, indent=1) + "\n", encoding="utf-8")
            print(f"[brief_synthesis] OK — {len(synth)} entries validated → {SYNTHESIS.relative_to(ROOT)}")
            return 0
        synth = _prune(synth, v.get("errors", []))
        if synth is None:
            break
        print(f"[brief_synthesis] pruning invalid entries, revalidating "
              f"({len(v.get('errors', []))} error(s))")

    # Fail closed: restore what was there before.
    if prev is not None:
        SYNTHESIS.write_text(prev, encoding="utf-8")
    else:
        SYNTHESIS.unlink(missing_ok=True)
    print("[brief_synthesis] FAILED validation — previous synthesis kept. Errors:")
    for e in (v.get("errors") or [])[:8]:
        print(f"  - {e}")
    return 1


TRIAGE = ROOT / ".agent" / "catalog" / "triage.json"
TRIAGE_CALLS = {"resume", "shelve", "kill"}

TRIAGE_PROMPT = """You are the librarian of Farrice's work estate. Below are catalog rows for
dormant or uncarded work items. For each, judge its fate:
- "resume" — real merit, worth picking back up (say what the merit is)
- "shelve" — keep, but it can sleep (say why it keeps value)
- "kill" — recommend killing/archiving (say why it is dead weight)
The active sprint: collecting five thousand dollars a month from claim-safe content
for funded health and performance brands. Judge against THAT, plus evident craft value.

HARD RULES: no digits (numbers as words), no file paths, no slashes, no URLs.
One short sentence per why. Output exactly one JSON object, no fences:
{"<key>": {"call": "resume|shelve|kill", "why": "..."}, ...,
 "_report": {"lede": "...", "caveats": "...", "operator_read": "..."}}
The _report entry is the estate-level read for the weekly shelf report.

ROWS:
"""


def _validate_triage(t):
    errs = []
    if not isinstance(t, dict):
        return ["triage must be an object"]
    for k, v in t.items():
        if k == "_report":
            for rk in ("lede", "caveats", "operator_read"):
                val = (v or {}).get(rk)
                if not isinstance(val, str) or not val:
                    errs.append(f"_report.{rk} missing")
                elif FORB.search(val):
                    errs.append(f"_report.{rk} forbidden metadata")
            continue
        if not isinstance(v, dict) or v.get("call") not in TRIAGE_CALLS:
            errs.append(f"{k}: call must be resume|shelve|kill")
            continue
        why = v.get("why")
        if not isinstance(why, str) or not why:
            errs.append(f"{k}: why required")
        elif FORB.search(why):
            errs.append(f"{k}: why contains forbidden metadata")
    return errs


FORB = mbrief.FORBIDDEN_SYNTHESIS_VALUE


def cmd_triage(args):
    import work_catalog as wc
    s = wc.shelves()
    cands = {}
    for r in s["resume"] + [r for r in s["stacks"] if r.get("dormant") and r.get("kind") == "thread"]:
        if len(cands) >= 40:
            break
        cands[r["k"]] = {"title": r.get("title"), "kind": r.get("kind"),
                         "merit_why": r.get("merit_why"), "last_active": (r.get("last_active") or "")[:10],
                         "status": r.get("status"), "evidence": r.get("evidence"),
                         "tags": r.get("tags")}
    if not cands:
        print("[brief_synthesis] nothing to triage")
        return 0
    prompt = TRIAGE_PROMPT + json.dumps(cands, indent=1, ensure_ascii=False)
    try:
        r = subprocess.run(["claude", "-p", "--model", args.model, prompt],
                           capture_output=True, text=True, timeout=args.timeout)
        out = r.stdout
    except FileNotFoundError:
        print("[brief_synthesis] claude CLI not found — triage skipped (honest, not broken)")
        return 0
    except subprocess.TimeoutExpired:
        print("[brief_synthesis] triage timed out — previous kept")
        return 0
    t = _extract_json(out or "")
    if not t:
        print("[brief_synthesis] triage FAILED: no parseable JSON")
        return 1
    errs = _validate_triage(t)
    if errs:
        # prune bad entries; _report failure sinks the pass
        if any(e.startswith("_report") for e in errs):
            print("[brief_synthesis] triage FAILED validation (_report) — previous kept")
            return 1
        for e in errs:
            t.pop(e.split(":")[0], None)
    TRIAGE.parent.mkdir(parents=True, exist_ok=True)
    TRIAGE.write_text(json.dumps(t, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"[brief_synthesis] triage OK — {len(t) - 1} calls → {TRIAGE.relative_to(ROOT)}")
    return 0


def cmd_status(args):
    receipt = mbrief.load(SYNTHESIS.parent / "synthesis-receipt.json", {})
    synth = mbrief.load(SYNTHESIS, {})
    bundle = mbrief.load(SWEEP, {})
    live = set(bundle.get("threads") or {})
    covered = set(synth) & live
    print(json.dumps({
        "present": SYNTHESIS.exists(),
        "generated": receipt.get("generated"),
        "model": receipt.get("model"),
        "entries": len(synth),
        "live_threads": len(live),
        "covered": len(covered),
        "uncovered": sorted(live - covered)[:10],
    }, indent=2))
    return 0


def main():
    ap = argparse.ArgumentParser(description="Judged analyst pass over the mission sweep.")
    sub = ap.add_subparsers(dest="command", required=True)
    r = sub.add_parser("run", help="Generate + validate synthesis.json (fail-closed).")
    r.add_argument("--model", default="opus", help="claude -p model (default opus — judged prose seat)")
    r.add_argument("--timeout", type=int, default=600)
    t = sub.add_parser("triage", help="Judge dormant catalog rows: resume | shelve | kill (fail-closed).")
    t.add_argument("--model", default="opus")
    t.add_argument("--timeout", type=int, default=600)
    sub.add_parser("status")
    args = ap.parse_args()
    return {"run": cmd_run, "triage": cmd_triage, "status": cmd_status}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
