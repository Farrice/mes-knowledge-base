#!/usr/bin/env python3
"""work_catalog.py — the librarian's permanent memory (2026-08-20).

WHY (Farrice, verbatim): "I need help categorizing my work… I move fast,
pursue a bunch of curiosity things, none of it's organized, none filed
properly, and when I want to resume the things that actually had merit I
lost them… a true intellectual asset and intelligence database."

The sweep is a deliberate 14-day window; anything unpromoted used to persist
as a bare slug and then vanish. This module is the memory BEYOND the window:

  .agent/catalog/catalog.jsonl — one JSON line per work key, latest-wins,
  first_seen preserved, merit sticky. Threads come from the sweep census;
  shelved artifacts (deliverables/, extractions/, knowledge/, guides/,
  docs/solutions, briefs) come from deterministic scans.

Commands:
    merge                fold current sweep census + dated sweeps + shelf scans
    add <key> [...]      file a row at birth (called by hooks + /go compile)
    find "<query>"       search the whole estate; rows + resume commands
    report               weekly shelf report → Briefing Room brief
    rows [--json]        the catalog as data (surfaces read this)
    status

Deterministic, stdlib only. Judged prose lives in triage.json (written by
brief_synthesis.py triage, validated fail-closed) — this module only reads it.
"""
import argparse
import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "execution"))
from degrade import degraded  # noqa: E402

CAT_DIR = ROOT / ".agent" / "catalog"
LEDGER = CAT_DIR / "catalog.jsonl"
TRIAGE = CAT_DIR / "triage.json"
SWEEP_DIR = ROOT / ".agent" / "sweep"
BRIEFS = ROOT / "deliverables" / "research-briefs"

DORMANT_DAYS = 14

# tag rules: (tag, regex over "arena path title serves") — deterministic.
TAG_RULES = [
    ("client", r"client|jen-|josh|andrea|javier|carbon-torch|eightward|santulan"),
    ("offer", r"offer|proof-to-market|pilot|pricing|sprint-spine|angle-map"),
    ("content", r"linkedin|post|carousel|content|newsletter|substack|thread|hook"),
    ("creative", r"trailer|video|anime|image|asset|style|poster|brand-visual|midjourney|seedance"),
    ("research", r"research|teardown|listening|zeitgeist|intel|icp|market"),
    ("harness", r"harness|hook|workflow|skill|system|catalog|homebase|pulse|readout|codex|forge"),
    ("revenue", r"revenue|cash|first-client|dm|outreach|funnel|claim-check"),
]


def now_iso():
    return datetime.now().isoformat(timespec="seconds")


def jsonl(path):
    rows = []
    try:
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    continue
    except OSError:
        pass
    return rows


def tags_for(*texts):
    hay = " ".join(str(t or "") for t in texts).lower()
    return [tag for tag, pat in TAG_RULES if re.search(pat, hay)]


def merit_for(row):
    """Deterministic merit: a good verdict, a high finalize score, or a pin.
    Sticky — once true, stays true (merit is history, not mood)."""
    why = []
    if "good" in (row.get("verdicts") or []):
        why.append("verdict good")
    if any(isinstance(s, (int, float)) and s >= 8 for s in (row.get("scores") or [])):
        why.append("finalize ≥8")
    if row.get("pin"):
        why.append("pinned")
    return (bool(why), " · ".join(why))


def load_catalog():
    latest = {}
    for r in jsonl(LEDGER):
        k = r.get("k")
        if k:
            latest[k] = r
    return latest


def _append(rows):
    CAT_DIR.mkdir(parents=True, exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def _upsert(cat, key, kind, **fields):
    """Merge into the in-memory catalog. first_seen min-wins; merit sticky."""
    prev = cat.get(key, {})
    row = {"k": key, "kind": kind, "updated": now_iso()}
    row.update({p: prev.get(p) for p in
                ("title", "arena", "tags", "status", "stage", "pin", "promoted",
                 "killed", "merit", "merit_why", "first_seen", "last_active",
                 "evidence", "path", "brief", "handoff", "resume") if prev.get(p) is not None})
    for k2, v in fields.items():
        if v not in (None, "", [], {}):
            row[k2] = v
        elif k2 in ("promoted", "killed", "pin") and v is not None:
            row[k2] = v
    if prev.get("first_seen") and row.get("first_seen"):
        row["first_seen"] = min(prev["first_seen"], row["first_seen"])
    m, mw = merit_for(row)
    if prev.get("merit"):
        row["merit"], row["merit_why"] = True, prev.get("merit_why") or mw
    elif m:
        row["merit"], row["merit_why"] = True, mw
    cat[key] = row
    return row


def _thread_row(cat, c):
    brief_rel = f"deliverables/research-briefs/mission-{c['key']}/mission-{c['key']}-brief.html"
    _upsert(cat, c["key"], "thread",
            title=c.get("title"), arena=c.get("arena"), status=c.get("status"),
            stage=c.get("stage"), pin=c.get("pin"), promoted=c.get("promoted"),
            killed=c.get("killed"), handoff=c.get("handoff"),
            first_seen=c.get("first_seen"), last_active=c.get("last_active"),
            evidence=c.get("evidence"), verdicts=c.get("verdicts"),
            scores=c.get("scores"),
            brief=brief_rel if (ROOT / brief_rel).exists() else None,
            resume=f"/resume {c['key']}",
            tags=tags_for(c.get("arena"), c.get("title"), c.get("key")))


def _scan_shelves(cat):
    """Deterministic scans of the unindexed masses. Title = first heading or
    prettified name; evidence = item count; cheap on purpose."""
    def first_heading(p):
        try:
            for line in open(p, encoding="utf-8", errors="ignore"):
                line = line.strip()
                if line.startswith("#"):
                    return line.lstrip("# ").strip()[:160]
                if line and len(line) > 12 and not line.startswith("---"):
                    return line[:160]
        except OSError:
            pass
        return ""

    def stamp(p):
        try:
            return datetime.fromtimestamp(p.stat().st_mtime).isoformat(timespec="seconds")
        except OSError:
            return ""

    def scan_dir(base, kind, depth_title=True):
        if not base.exists():
            return
        for p in sorted(base.iterdir()):
            if p.name.startswith(".") or p.name == "research-briefs":
                continue
            key = f"{kind}:{p.stem}"[:120]
            title = ""
            items = 1
            if p.is_dir():
                inner = [f for f in p.rglob("*") if f.is_file()][:400]
                items = len(inner)
                for cand in ("README.md", "START-HERE.md", "INDEX.md"):
                    if (p / cand).exists():
                        title = first_heading(p / cand)
                        break
                if not title and depth_title:
                    mds = sorted(p.glob("*.md"))
                    if mds:
                        title = first_heading(mds[0])
            elif p.suffix.lower() in (".md", ".html", ".txt"):
                title = first_heading(p)
            title = title or p.stem.replace("-", " ").replace("_", " ")
            _upsert(cat, key, kind, title=title[:200],
                    path=str(p.relative_to(ROOT)), last_active=stamp(p),
                    first_seen=stamp(p), evidence={"items": items},
                    tags=tags_for(p.name, title, kind))

    scan_dir(ROOT / "deliverables", "deliverable")
    scan_dir(ROOT / "extractions", "extraction")
    scan_dir(ROOT / "knowledge", "knowledge")
    scan_dir(ROOT / "guides", "guide")
    scan_dir(ROOT / "docs" / "solutions", "solution")

    # briefs ride in with their own metadata
    try:
        import brief_library as bl
        for e in bl.collect():
            key = f"brief:{e['slug']}"
            _upsert(cat, key, "brief", title=str(e["title"]).replace("*", "")[:200],
                    status=e.get("status"),
                    path=str(Path(e["html"]).relative_to(ROOT)),
                    last_active=datetime.fromtimestamp(float(e["mtime"])).isoformat(timespec="seconds"),
                    evidence={"category": e.get("category")},
                    tags=tags_for(e.get("category"), e.get("title")))
    except Exception as e:
        degraded(None, "brief library scan skipped in catalog merge", e)


def cmd_merge(args):
    cat = load_catalog()
    before = len(cat)
    sweeps = sorted(SWEEP_DIR.glob("sweep-*.json")) + [SWEEP_DIR / "latest.json"]
    seen_census = 0
    for sp in sweeps:
        try:
            b = json.loads(sp.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for c in b.get("census") or []:
            _thread_row(cat, c)
            seen_census += 1
        # older sweeps have no census — mine their promoted threads at least
        if not b.get("census"):
            for k, t in (b.get("threads") or {}).items():
                _thread_row(cat, {"key": k, "title": t.get("title"), "arena": t.get("arena"),
                                  "status": t.get("status"), "stage": t.get("stage"),
                                  "pin": t.get("pin"), "promoted": True,
                                  "killed": t.get("killed"), "handoff": t.get("handoff"),
                                  "first_seen": t.get("first_seen"),
                                  "last_active": t.get("last_active"),
                                  "evidence": {"sessions": len(t.get("sessions", [])),
                                               "deliverables": len(t.get("deliverables", [])),
                                               "assets": len(t.get("assets", []))},
                                  "verdicts": [m.get("verdict") for m in t.get("missions", []) if m.get("verdict")],
                                  "scores": []})
    _scan_shelves(cat)
    # rewrite compacted (latest-wins materialized) — the jsonl stays readable
    CAT_DIR.mkdir(parents=True, exist_ok=True)
    tmp = LEDGER.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        for r in sorted(cat.values(), key=lambda x: x.get("last_active") or "", reverse=True):
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    tmp.replace(LEDGER)
    print(f"[work_catalog] {len(cat)} rows ({len(cat) - before:+d}) · census rows folded: {seen_census} → {LEDGER.relative_to(ROOT)}")
    return 0


def cmd_add(args):
    cat = load_catalog()
    row = _upsert(cat, args.key, args.kind, title=args.title or args.key.replace("-", " "),
                  arena=args.arena, status="active",
                  first_seen=now_iso(), last_active=now_iso(),
                  resume=f"/resume {args.key}",
                  tags=tags_for(args.arena, args.title, args.key, args.serves))
    _append([row])
    print(f"[work_catalog] filed at birth: {args.key} ({row.get('tags')})")
    return 0


def _dormant(row):
    la = row.get("last_active") or row.get("updated") or ""
    try:
        return (datetime.now() - datetime.fromisoformat(la[:19])) > timedelta(days=DORMANT_DAYS)
    except ValueError:
        return True


def shelves():
    """The catalog, shelved — the one calc every surface shares."""
    cat = load_catalog()
    triage = {}
    try:
        triage = json.loads(TRIAGE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        pass
    for k, r in cat.items():
        r["triage"] = triage.get(k) or {}
        r["dormant"] = _dormant(r)
    rows = list(cat.values())
    dead = [r for r in rows if r.get("killed") or r.get("status") == "archived"]
    live = [r for r in rows if r.get("promoted") and r not in dead]
    resume = [r for r in rows if r.get("merit") and r.get("dormant") and r not in dead
              and (r.get("triage") or {}).get("call") != "kill"]
    resume.sort(key=lambda r: ((r.get("triage") or {}).get("call") != "resume",
                               -(len(r.get("merit_why") or "")),
                               r.get("last_active") or ""))
    stacks = [r for r in rows if r not in dead]
    stacks.sort(key=lambda r: r.get("last_active") or "", reverse=True)
    return {"resume": resume, "live": live, "stacks": stacks, "dead": dead}


def cmd_rows(args):
    s = shelves()
    if args.json:
        print(json.dumps({k: v for k, v in s.items()}, ensure_ascii=False, default=str)[:200000])
    else:
        for name in ("resume", "live", "stacks", "dead"):
            print(f"\n== {name} ({len(s[name])}) ==")
            for r in s[name][:8 if name != "stacks" else 15]:
                t = (r.get("triage") or {}).get("call", "")
                print(f"  [{r['kind']:11s}] {str(r.get('title'))[:70]:70s} {r.get('last_active','')[:10]} "
                      f"{'★' if r.get('merit') else ' '} {t}")
    return 0


def cmd_find(args):
    """Search the estate by half-remembered phrase. Token-overlap ranking over
    title+tags+key+arena; honest empty result beats fuzzy hallucination."""
    q = [w for w in re.split(r"\W+", args.query.lower()) if len(w) > 2]
    if not q:
        print("[work_catalog] query too thin")
        return 1
    scored = []
    for r in load_catalog().values():
        hay = " ".join([str(r.get("title") or ""), r.get("k", ""),
                        " ".join(r.get("tags") or []), r.get("arena") or "",
                        r.get("resume") or ""]).lower()
        hits = sum(1 for w in q if w in hay)
        if hits:
            scored.append((hits, r.get("last_active") or "", r))
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    if not scored:
        print(f"NO MATCH in the catalog for: {args.query!r} — it may predate the catalog; try episodic memory.")
        return 0
    for hits, _, r in scored[:args.top]:
        open_cmd = (f"open '{ROOT / r['brief']}'" if r.get("brief")
                    else f"open '{ROOT / r['path']}'" if r.get("path") else "")
        resume = r.get("resume") or ""
        print(f"[{r['kind']}] {str(r.get('title'))[:90]}")
        print(f"    last {r.get('last_active','?')[:10]} · {'★ ' + (r.get('merit_why') or '') if r.get('merit') else 'no merit signal'}"
              f" · tags {','.join(r.get('tags') or []) or '—'}")
        if resume:
            print(f"    resume: {resume}")
        if open_cmd:
            print(f"    {open_cmd}")
    return 0


def cmd_report(args):
    """Weekly shelf report → a Briefing Room brief through the standard writer."""
    import render_brief
    s = shelves()
    week_ago = (datetime.now() - timedelta(days=7)).isoformat()
    entered = [r for r in s["stacks"] if (r.get("first_seen") or "") >= week_ago]
    moved = [r for r in s["stacks"] if (r.get("last_active") or "") >= week_ago]
    decaying = [r for r in s["resume"][:6]]
    kill_list = [r for r in s["stacks"] if (r.get("triage") or {}).get("call") == "kill"]
    triage_board = {}
    try:
        triage_board = (json.loads(TRIAGE.read_text(encoding="utf-8")) or {}).get("_report", {})
    except (OSError, ValueError):
        pass

    def rel_rows(rows, cap=8):
        out = []
        for r in rows[:cap]:
            p = r.get("brief") or r.get("path")
            link = {"k": r["kind"].upper()[:9], "title": str(r.get("title"))[:90]}
            if p:
                link["path"] = p
            out.append(link)
        return out

    sections = [
        {"kind": "summary", "heading": "the state of the *estate*", "kicker": "SHELF REPORT",
         "body": triage_board.get("lede") or
                 (f"{len(entered)} new items entered the catalog this week, {len(moved)} moved, "
                  f"{len(s['resume'])} merit items sit dormant, and {len(kill_list)} await a kill decision. "
                  "The shelves below are the week in one read.")},
        {"kind": "stats", "heading": "the estate", "tag": "CATALOG", "items": [
            {"value": str(len(s["stacks"])), "label": "ITEMS CATALOGED"},
            {"value": str(len(entered)), "label": "NEW THIS WEEK"},
            {"value": str(len(s["resume"])), "label": "WORTH RESUMING"},
            {"value": str(len(kill_list)), "label": "KILL DECISIONS WAITING"}]},
        {"kind": "related", "heading": "worth *resuming*", "tag": "MERIT, DORMANT",
         "links": rel_rows(decaying)},
        {"kind": "related", "heading": "entered this week", "tag": "NEW",
         "links": rel_rows(entered)},
    ]
    if kill_list:
        sections.append({"kind": "related", "heading": "the librarian recommends killing",
                         "tag": "YOUR WORD", "links": rel_rows(kill_list)})
    sections.append({"kind": "caveats", "heading": "what this *isn't*", "kicker": "EDGES",
                     "body": triage_board.get("caveats") or
                     "Assembled mechanically from the catalog ledger; judged calls come from the "
                     "validated triage pass and are recommendations, never actions."})
    brief = {
        "slug": "library-shelf-report",
        "chip": "LIBRARY · WEEKLY",
        "title": "the shelf *report*",
        "dek": triage_board.get("operator_read") or
               "What entered, what moved, what is decaying, and what awaits your word.",
        "window": "last 7 days", "lens": "librarian",
        "sources": f"{len(s['stacks'])} catalog rows",
        "compiled": datetime.now().strftime("%b %-d, %Y").lower(),
        "footer_left": "ANTIGRAVITY · LIBRARIAN", "footer_right": "@farricecain",
        "category": "library", "priority": 2, "sections": sections,
    }
    render_brief.write_brief(brief, share=False)
    print("[work_catalog] shelf report → deliverables/research-briefs/library-shelf-report/")
    return 0


def cmd_nudge(args):
    """One digest line for session start (house style: silent when nothing)."""
    s = shelves()
    kill_n = sum(1 for r in s["stacks"] if (r.get("triage") or {}).get("call") == "kill")
    bits = []
    if s["resume"]:
        top = s["resume"][0]
        bits.append(f"{len(s['resume'])} item(s) worth resuming (top: {str(top.get('title'))[:48]})")
    if kill_n:
        bits.append(f"{kill_n} kill decision(s) waiting")
    if bits:
        print("LIBRARY: " + " · ".join(bits) + " — http://127.0.0.1:8765/library")
    return 0


def cmd_status(args):
    s = shelves()
    print(json.dumps({"rows": len(s["stacks"]) + len(s["dead"]),
                      "worth_resuming": len(s["resume"]), "live": len(s["live"]),
                      "dead": len(s["dead"]),
                      "triage_present": TRIAGE.exists()}, indent=2))
    return 0


def main():
    ap = argparse.ArgumentParser(description="The librarian's permanent catalog.")
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("merge")
    a = sub.add_parser("add")
    a.add_argument("key"); a.add_argument("--kind", default="thread")
    a.add_argument("--title", default=""); a.add_argument("--arena", default="")
    a.add_argument("--serves", default="")
    f = sub.add_parser("find"); f.add_argument("query"); f.add_argument("--top", type=int, default=6)
    r = sub.add_parser("rows"); r.add_argument("--json", action="store_true")
    sub.add_parser("report")
    sub.add_parser("nudge")
    sub.add_parser("status")
    args = ap.parse_args()
    return {"merge": cmd_merge, "add": cmd_add, "find": cmd_find,
            "rows": cmd_rows, "report": cmd_report, "nudge": cmd_nudge,
            "status": cmd_status}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
