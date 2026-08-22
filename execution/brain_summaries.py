#!/usr/bin/env python3
"""brain_summaries.py — AI snapshot per second-brain node (2026-08-22).

WHY (Farrice): "when I hover over the nodes or even click on them, there's
more value in them, like a quick snapshot or a concise summary." Research
receipt (Recall's lesson): summaries must be PRECOMPUTED at build time —
generating on hover is a latency tax.

Mechanism: reads .agent/brain/brain.json nodes, excerpts each backing file
(frontmatter description / docstring / first lines), batches ~18 nodes per
`claude -p` Haiku call asking for a strict JSON map of {rel: summary}, and
caches to .agent/brain/summaries.json keyed by file mtime — only new/changed
files ever re-spend. Every run appends a receipt with MEASURED total cost
(cost-transparency binding, 2026-08-01): no estimates, sum of the CLI's own
total_cost_usd.

Summary contract: ≤160 chars, concrete, "what this is + why you'd open it".
brain_graph.py folds these into node data for the hover card.

Usage:
  python3 execution/brain_summaries.py run [--limit N] [--batch 18] [--model haiku]
  python3 execution/brain_summaries.py status
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAIN_JSON = os.path.join(ROOT, ".agent", "brain", "brain.json")
CACHE = os.path.join(ROOT, ".agent", "brain", "summaries.json")
RECEIPTS = os.path.join(ROOT, ".agent", "brain", "summary-receipts.jsonl")

EXCERPT_LINES = 26
MAX_CHARS = 200  # hard cap on stored summary


def load_cache():
    try:
        return json.load(open(CACHE, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _excerpt(path):
    """The cheapest signal-dense slice of a file: frontmatter description if
    present, else docstring/heading + first lines."""
    try:
        text = open(path, encoding="utf-8", errors="replace").read(8000)
    except OSError:
        return None
    m = re.search(r"^description:\s*['\"]?(.+?)['\"]?$", text[:2000], re.MULTILINE)
    desc = m.group(1)[:400] if m else ""
    lines = [ln for ln in text.splitlines()[:EXCERPT_LINES]]
    return (("DESC: " + desc + "\n") if desc else "") + "\n".join(lines)[:1400]


def pending(nodes, cache, limit=None):
    out = []
    for n in nodes:
        rel = n.get("rel")
        if not rel or n.get("hub"):
            continue
        path = os.path.join(ROOT, rel)
        # dir nodes point at their anchor file already (SKILL.md etc.)
        if not os.path.isfile(path):
            continue
        try:
            mt = int(os.stat(path).st_mtime)
        except OSError:
            continue
        c = cache.get(rel)
        if c and c.get("mtime") == mt and c.get("sum"):
            continue
        out.append((rel, mt, path))
        if limit and len(out) >= limit:
            break
    return out


def _call_claude(prompt, model):
    r = subprocess.run(
        ["claude", "-p", prompt, "--model", model, "--effort", "low",
         "--output-format", "json"],
        capture_output=True, text=True, timeout=600, cwd=ROOT)
    cost, text = 0.0, ""
    try:
        j = json.loads(r.stdout or "")
        cost = float(j.get("total_cost_usd") or 0)
        text = j.get("result") or ""
    except ValueError:
        text = r.stdout or ""
    return text, cost, r.returncode


def _parse_map(text):
    """The model returns a JSON object; tolerate fencing."""
    m = re.search(r"\{[\s\S]*\}", text)
    if not m:
        return {}
    try:
        d = json.loads(m.group(0))
        return {k: str(v)[:MAX_CHARS] for k, v in d.items() if isinstance(v, str)}
    except ValueError:
        return {}


PROMPT_HEAD = (
    "You write one-line snapshots for a personal knowledge-system map. "
    "For EACH file below, write ONE summary, max 150 characters: concrete, "
    "specific, 'what this is + why you'd open it'. No fluff, no 'this file', "
    "no restating the filename. Return ONLY a JSON object mapping the exact "
    "REL keys to summary strings. No other text.\n\n")


def run(limit=None, batch=18, model="haiku"):
    try:
        nodes = json.load(open(BRAIN_JSON, encoding="utf-8"))["nodes"]
    except (OSError, ValueError, KeyError) as e:
        print(f"ERROR: brain.json unreadable ({e}) — run brain_graph.py first",
              file=sys.stderr)
        return 1
    cache = load_cache()
    todo = pending(nodes, cache, limit)
    if not todo:
        print(f"summaries → fresh ({len(cache)} cached, nothing changed)")
        return 0
    print(f"summaries → {len(todo)} node(s) to write, batches of {batch}, model {model}")
    total_cost, wrote, failed = 0.0, 0, 0
    t0 = time.time()
    for i in range(0, len(todo), batch):
        chunk = todo[i:i + batch]
        parts = []
        for rel, _mt, path in chunk:
            ex = _excerpt(path) or "(empty file)"
            parts.append(f"REL: {rel}\n{ex}\n---")
        text, cost, rc = _call_claude(PROMPT_HEAD + "\n".join(parts), model)
        total_cost += cost
        got = _parse_map(text) if rc == 0 else {}
        for rel, mt, _path in chunk:
            if rel in got and got[rel].strip():
                cache[rel] = {"sum": got[rel].strip(), "mtime": mt,
                              "written": time.strftime("%Y-%m-%d")}
                wrote += 1
            else:
                failed += 1
        # persist incrementally — a crash mid-run never loses paid work
        json.dump(cache, open(CACHE, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=0)
        print(f"  batch {i // batch + 1}/{(len(todo) + batch - 1) // batch}: "
              f"+{len(got)} · running cost ${total_cost:.4f}")
    receipt = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "wrote": wrote,
               "failed": failed, "model": model,
               "total_cost_usd": round(total_cost, 4),
               "duration_s": int(time.time() - t0)}
    os.makedirs(os.path.dirname(RECEIPTS), exist_ok=True)
    open(RECEIPTS, "a", encoding="utf-8").write(json.dumps(receipt) + "\n")
    print(f"summaries → wrote {wrote}, failed {failed}, "
          f"MEASURED cost ${total_cost:.4f} ({int(time.time() - t0)}s) → {CACHE}")
    return 0


def status():
    cache = load_cache()
    costs = []
    try:
        for ln in open(RECEIPTS, encoding="utf-8"):
            costs.append(json.loads(ln).get("total_cost_usd") or 0)
    except OSError:
        pass
    print(f"{len(cache)} summaries cached · lifetime measured spend ${sum(costs):.4f} "
          f"across {len(costs)} run(s)")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Precompute AI node snapshots.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--limit", type=int, default=None)
    r.add_argument("--batch", type=int, default=18)
    r.add_argument("--model", default="haiku", choices=["haiku", "sonnet"])
    sub.add_parser("status")
    a = ap.parse_args()
    if a.cmd == "status":
        return status()
    return run(a.limit, a.batch, a.model)


if __name__ == "__main__":
    raise SystemExit(main())
