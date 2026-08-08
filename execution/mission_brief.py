#!/usr/bin/env python3
"""
mission_brief.py — one LIVING brief per ongoing thread, from the sweep bundle.

Reads .agent/sweep/latest.json (written by session_sweep.py) and renders each
promoted thread as a research brief in the Briefing Room, plus a `mission-board`
digest that indexes them all.

LIVING, NOT A RECEIPT. Every sweep re-renders the SAME slug (`mission-<thread>`),
so twelve sessions collapse into one card that gets smarter — not twelve cards
that pile up. Sessions append to the timeline; the top of the brief always states
current position. This is the LIVING-vs-RECORD standard applied to the surface
itself (directives/artifact-placement.md).

THE FACT/MEANING SPLIT IS STRUCTURAL. This module fills every number, path, date
and link from the bundle FIRST, then merges an optional synthesis file that may
only write into named prose slots (see SLOTS). The judge cannot touch a figure
because it is never handed one to edit — it is handed a slot list. That is what
makes "deterministic capture + judged synthesis" honest rather than a promise.

A CHART EARNS ITS PLACE OR IT IS NOT DRAWN. `chart_earns_place()` requires >=3
points and real variation; flat and near-empty series are dropped along with
their whole section. Farrice's constraint, mechanized: "when helpful and
meaningful, not just wastefully done."

Usage:
    python3 execution/mission_brief.py build [--slug S | --all] [--no-index] [--quiet]
    python3 execution/mission_brief.py slots [--json]     # what the judge may write
    python3 execution/mission_brief.py status

Outputs: deliverables/research-briefs/mission-<thread>/ (+ mission-board/)
"""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "execution"))

import render_brief  # noqa: E402

SWEEP_LATEST = ROOT / ".agent" / "sweep" / "latest.json"
SYNTHESIS = ROOT / ".agent" / "sweep" / "synthesis.json"
BRIEFS = ROOT / "deliverables" / "research-briefs"

CATEGORY = "mission"
BOARD_SLUG = "mission-board"

# The ONLY fields a synthesis pass may write. Anything else in the file is
# ignored — an allow-list beats a deny-list when the thing being constrained is
# a language model with an opinion about what would look better.
SLOTS = {
    "lede": "1-2 sentences: where this thread actually stands, in plain language.",
    "next_move": "One sentence: the single next action. Imperative, concrete.",
    "why": "Per decision item, keyed by item index: why it matters now.",
    "caveats": "What is unverified, stale, or at risk in this thread.",
    "operator_read": "One line an operator would tell a colleague about this thread.",
}

STAGE_LABELS = ["research", "build", "shipped", "outcome"]
STAGE_BLURB = {
    "research": "reading and deciding — nothing built yet",
    "build": "files are moving; nothing finalized",
    "shipped": "a deliverable was finalized",
    "outcome": "an outcome was recorded against it",
}


# ── helpers ─────────────────────────────────────────────────────────
def load(path, default=None):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default if default is not None else {}


def human_date(iso_s):
    d = _dt(iso_s)
    return d.strftime("%b %-d, %Y").lower() if d else ""


def _dt(iso_s):
    try:
        return datetime.fromisoformat(str(iso_s)[:19])
    except (ValueError, TypeError):
        return None


def days_since(iso_s):
    d = _dt(iso_s)
    return (datetime.now() - d).days if d else None


def title_case(slug):
    return " ".join(w for w in str(slug).replace("-", " ").split())


def chart_earns_place(values, min_points=3):
    """A chart is emitted only if it says something a sentence could not.

    Three or more points AND real variation. A flat line, a single bar, or an
    all-zero series is decoration — it costs the reader a glance and returns
    nothing. Dropping the data drops the whole section (see build_brief).
    """
    vals = [v for v in (values or []) if isinstance(v, (int, float))]
    if len(vals) < min_points:
        return False
    if max(vals) == min(vals):
        return False
    return any(v for v in vals)


def priority_for(t):
    """1 = highest. Blocked and pinned work outranks merely-active work."""
    if t.get("status") == "blocked" or t.get("pin"):
        return 1
    if any(m.get("open") for m in t.get("missions", [])):
        return 1
    if t.get("status") in ("active", "mid-build"):
        return 2
    return 3


def initiative_front_door(t):
    """The generated START-HERE.html for this thread's initiative, if one exists.

    front_door.py owns those pages; linking rather than duplicating keeps the
    one-front-door-per-initiative rule intact."""
    for art in t.get("artifacts", []):
        p = Path(art["path"])
        parts = p.parts
        if parts and parts[0] == "_active":
            for depth in (3, 2):
                if len(parts) > depth:
                    cand = ROOT.joinpath(*parts[:depth]) / "START-HERE.html"
                    if cand.exists():
                        return str(cand.relative_to(ROOT))
    return ""


# ── section builders ────────────────────────────────────────────────
def sec_summary(t, synth, window):
    sessions, arts = len(t["sessions"]), len(t["artifacts"])
    delivs, assets = len(t["deliverables"]), len(t["assets"])
    bits = []
    if sessions:
        bits.append(f"{sessions} session{'s' if sessions != 1 else ''}")
    if arts:
        bits.append(f"{arts} file{'s' if arts != 1 else ''} written")
    if delivs:
        bits.append(f"{delivs} deliverable{'s' if delivs != 1 else ''} finalized")
    if assets:
        bits.append(f"{assets} asset{'s' if assets != 1 else ''} generated")
    activity = ", ".join(bits) if bits else "no recorded activity"

    para = []
    if synth.get("lede"):
        para.append(synth["lede"])
    else:
        # Facts-only default. Reads as a status line, never as analysis it
        # hasn't earned — an unsynthesized brief must not sound synthesized.
        para.append(
            f"Stage: {t['stage']} — {STAGE_BLURB.get(t['stage'], '')}. "
            f"In the last {window['days']} days: {activity}."
        )
    idle = days_since(t.get("last_active"))
    state = f"Handoff status is **{t['status']}**." if t.get("status") else ""
    if idle is not None:
        state += f" Last activity {'today' if idle <= 0 else f'{idle}d ago'}."
    if state.strip():
        para.append(state.replace("**", ""))
    nxt = synth.get("next_move") or t.get("resume_hint")
    if nxt:
        para.append(f"Next: {nxt}")
    return {"kind": "summary", "heading": "where this *stands*",
            "kicker": "CURRENT POSITION", "body": "\n\n".join(p for p in para if p)}


def sec_stats(t, window):
    items = []

    def add(value, label, note=None, unit=None):
        if not value:
            return
        it = {"value": str(value), "label": label}
        if note:
            it["note"] = note
        if unit:
            it["unit"] = unit
        items.append(it)

    add(len(t["deliverables"]), "DELIVERABLES FINALIZED")
    add(len(t["artifacts"]), "FILES WRITTEN")
    add(len(t["assets"]), "ASSETS GENERATED")
    add(len(t["sessions"]), "SESSIONS",
        note=" · ".join(t["harnesses"]) if t["harnesses"] else None)
    spend = sum(float(a.get("cost_usd") or 0) for a in t["assets"])
    if spend:
        add(f"{spend:.2f}", "SPEND THIS WINDOW", unit="usd")
    age = days_since(t.get("first_seen"))
    if age:
        add(age, "DAYS ACTIVE", unit="d")
    if not items:
        return None
    return {"kind": "stats", "heading": "by the numbers",
            "tag": f"LAST {window['days']} DAYS", "items": items}


def sec_spark(t, window):
    """Momentum. Only series that clear the bar are drawn; if none clear it, the
    whole section is dropped rather than shipping an empty chart frame."""
    series = []
    for key, label, unit in (("sessions", "sessions", "total"),
                             ("artifacts", "files written", "files"),
                             ("assets", "assets", "made")):
        vals = t["daily"].get(key) or []
        if chart_earns_place(vals):
            series.append({"label": label, "values": vals,
                           "value": str(sum(vals)), "unit": unit, "note": "per day"})
    if not series:
        return None
    return {"kind": "spark", "heading": "momentum",
            "caption": f"daily, last {window['days']} days — each series scaled to itself",
            "series": series}


def sec_progress(t):
    idx = t.get("stage_index", 0)
    blocked = t.get("status") == "blocked"
    stages = []
    for i, name in enumerate(STAGE_LABELS):
        if i < idx:
            state = "done"
        elif i == idx:
            state = "blocked" if blocked else "current"
        else:
            state = "todo"
        st = {"label": name, "state": state}
        if i == idx:
            st["note"] = STAGE_BLURB.get(name, "")
        stages.append(st)
    return {"kind": "progress", "heading": "lifecycle", "stages": stages,
            "note": "stage is inferred from records only — a deliverable, an asset, a logged outcome"}


def sec_decision(t, synth):
    items = []
    whys = synth.get("why") or {}

    def add(action, why):
        items.append({"action": action, "why": why})

    if t.get("status") == "blocked":
        add("Unblock this thread", t.get("unfinished") or "Handoff is marked blocked.")
    if t.get("unfinished") and t.get("status") != "blocked":
        add("Finish what's open", t["unfinished"])
    for m in t.get("missions", []):
        if m.get("open"):
            add(f"Close or park: {m['title'][:80]}",
                f"Open mission ({m['status']}), serves {m['serves'] or 'no stated goal'}.")
    idle = days_since(t.get("last_active"))
    if idle is not None and idle >= 7 and not items:
        add("Decide: resume or park",
            f"No recorded activity in {idle} days while the handoff is still {t.get('status') or 'open'}.")
    if not items:
        return None
    for i, it in enumerate(items):
        if str(i) in whys:
            it["why"] = whys[str(i)]
    return {"kind": "decision", "heading": "what needs *you*", "kicker": "OPEN",
            "dek": "Everything here is derived from an open record — a blocked handoff, an unfinished line, an open mission.",
            "items": items}


def sec_assets(t):
    """Artifacts + generated assets, newest first. Paths feed the context pack,
    so this section is also what makes the brief hand-off-able to an agent."""
    items = []
    for a in sorted(t["assets"], key=lambda x: x.get("ts") or "", reverse=True)[:12]:
        it = {"title": Path(a["path"]).name, "role": (a.get("type") or "asset").upper(),
              "path": a["path"]}
        if a.get("type") == "image":
            it["thumb"] = a["path"]
        note = " · ".join(x for x in [a.get("model"), human_date(a.get("ts"))] if x)
        if note:
            it["note"] = note
        items.append(it)
    for art in sorted(t["artifacts"], key=lambda x: x.get("ts") or "", reverse=True)[:14]:
        items.append({"title": Path(art["path"]).name, "role": "FILE",
                      "path": art["path"], "note": human_date(art.get("ts"))})
    for g in t.get("guides", [])[:3]:
        items.append({"title": g["name"], "role": "GUIDE", "path": g["path"]})
    for s in t.get("solutions", [])[:3]:
        items.append({"title": s["name"], "role": "SOLUTION", "path": s["path"]})
    if not items:
        return None
    return {"kind": "assets", "heading": "what this thread *made*",
            "tag": "COPY THE PATH", "items": items[:28]}


def sec_playbook(t):
    plays = []
    if t.get("resume_hint"):
        touches = [t["handoff"]] if t.get("handoff") else []
        plays.append({"title": "Resume here", "intent": t["resume_hint"],
                      "command": f"python3 execution/handoff_store.py resume {t['slug']}",
                      "touches": touches,
                      "receipt": "The stored handoff prints with drift since it was written."})
    if t.get("missions"):
        plays.append({"title": "Close the mission", "intent": "Mark it done or park it with a reason.",
                      "command": f"python3 execution/pulse_actions.py done {t['slug']} --outcome \"<one line>\"",
                      "receipt": "It leaves the open set on the next pulse regen."})
    if not plays:
        return None
    return {"kind": "playbook", "heading": "pick it back *up*", "tag": "RUN THIS", "plays": plays}


def sec_timeline(t):
    items = []
    for d in t["deliverables"]:
        items.append({"date": d["date"], "title": f"Finalized · {d['workflow'] or d['skill'] or 'deliverable'}",
                      "body": d["output"][:220], "done": True})
    for s in sorted(t["sessions"], key=lambda x: x.get("ts") or "", reverse=True)[:10]:
        items.append({"date": (s.get("ts") or "")[:10],
                      "title": f"{s['harness']} session" + (f" · {s['messages']} msgs" if s.get("messages") else ""),
                      "body": (s.get("title") or "")[:180], "done": True})
    for c in t.get("commits", [])[:6]:
        items.append({"date": (c.get("ts") or "")[:10], "title": f"commit {c['sha']}",
                      "body": c["subject"][:180], "done": True})
    if not items:
        return None
    items.sort(key=lambda x: x.get("date") or "", reverse=True)
    return {"kind": "timeline", "heading": "how it got *here*",
            "tag": "HISTORY, NOT TRUTH", "items": items[:16]}


def sec_related(t, bundle):
    links = []
    if t.get("handoff"):
        links.append({"k": "HANDOFF", "title": "Stored handoff (source of resume)", "path": t["handoff"]})
    fd = initiative_front_door(t)
    if fd:
        links.append({"k": "FRONT DOOR", "title": f"START HERE · {title_case(t['slug'])}", "path": fd})
    links.append({"k": "BOARD", "title": "Mission board — every live thread",
                  "path": f"deliverables/research-briefs/{BOARD_SLUG}/{BOARD_SLUG}-brief.html"})
    siblings = [(k, v) for k, v in bundle["threads"].items()
                if k != t["slug"] and v.get("arena") and v["arena"] == t.get("arena")]
    for k, v in siblings[:4]:
        links.append({"k": "THREAD", "title": title_case(k),
                      "path": f"deliverables/research-briefs/mission-{k}/mission-{k}-brief.html"})
    return {"kind": "related", "heading": "swings to", "tag": "CONNECTED", "links": links}


def sec_caveats(t, bundle, synth):
    lines = []
    if synth.get("caveats"):
        lines.append(synth["caveats"])
    else:
        lines.append("No synthesis pass has run against this thread yet — everything above is "
                     "mechanically collected, and nothing here is interpretation.")
    lines.append("Session ledgers keep only the last 10 files per session and are pruned at 7 days, "
                 "so file counts are a floor, not a census. Sweeps persist their own record, so "
                 "anything already swept is kept.")
    if bundle.get("degraded"):
        lines.append("Sources unavailable on this sweep: " + "; ".join(bundle["degraded"]))
    return {"kind": "caveats", "heading": "what this *isn't*", "kicker": "READ THE EDGES",
            "body": "\n\n".join(lines)}


# ── brief assembly ──────────────────────────────────────────────────
def build_brief(slug, t, bundle, synth):
    window = bundle["window"]
    sections = [sec_summary(t, synth, window)]
    for maybe in (sec_stats(t, window), sec_spark(t, window), sec_progress(t),
                  sec_decision(t, synth), sec_assets(t), sec_playbook(t), sec_timeline(t)):
        if maybe:
            sections.append(maybe)
    sections.append(sec_related(t, bundle))
    sections.append(sec_caveats(t, bundle, synth))

    arena = (t.get("arena") or "thread").upper().replace("-", " ")
    title = t.get("title") or title_case(slug)
    # One accent word for the italic-serif voice; the last word reads best.
    words = title.split()
    accent_title = " ".join(words[:-1] + [f"*{words[-1]}*"]) if len(words) > 1 else f"*{title}*"

    dek = synth.get("operator_read") or (
        f"Everything this thread has produced, where it stands, and the next move — "
        f"assembled from {len(t['sessions'])} session(s), the handoff store, the finalize "
        f"ledger and the asset manifest.")

    return {
        "slug": f"mission-{slug}",
        "chip": f"MISSION · {arena}",
        "title": accent_title[:160],
        "dek": dek,
        "window": f"last {window['days']} days",
        "lens": " · ".join(t["harnesses"]) or "claude",
        "sources": f"{len(t['sessions'])} sessions · {len(t['artifacts'])} files · {len(t['assets'])} assets",
        "compiled": human_date(bundle["generated"]),
        "footer_left": "ANTIGRAVITY · MISSION SWEEP",
        "footer_right": "@farricecain",
        "category": CATEGORY,
        "priority": priority_for(t),
        "status": "active",  # Preserved by write_brief() when re-rendering; auto-archives per AUTO_ARCHIVE_DAYS
        "sections": sections,
    }


def build_board(bundle, synth):
    threads = bundle["threads"]
    live = sorted(threads.items(), key=lambda kv: kv[1].get("last_active") or "", reverse=True)
    window = bundle["window"]
    c = bundle["counts"]

    sections = []
    lede = synth.get("lede") or (
        f"{len(live)} threads are live. "
        f"{c['deliverables']} deliverables were finalized and {c['assets']} assets generated "
        f"in the last {window['days']} days, across {c['sessions']} sessions on both harnesses.")
    needs = [k for k, v in live if v.get("status") == "blocked" or any(m.get("open") for m in v["missions"])]
    body = [lede]
    if needs:
        body.append("Needs a decision: " + ", ".join(title_case(k) for k in needs[:6]) + ".")
    body.append("Each thread below has its own brief. Open the one you're resuming — it carries "
                "the resume line, what it made, and what's still open.")
    sections.append({"kind": "summary", "heading": "the state of *play*",
                     "kicker": "ALL LIVE THREADS", "body": "\n\n".join(body)})

    sections.append({"kind": "stats", "heading": "across every thread",
                     "tag": f"LAST {window['days']} DAYS", "items": [
                         {"value": str(len(live)), "label": "LIVE THREADS"},
                         {"value": str(c["deliverables"]), "label": "DELIVERABLES FINALIZED"},
                         {"value": str(c["artifacts"]), "label": "FILES WRITTEN"},
                         {"value": str(c["assets"]), "label": "ASSETS GENERATED"},
                         {"value": str(c["sessions"]), "label": "SESSIONS SWEPT"},
                     ]})

    # Cross-thread momentum: sum the per-thread daily series.
    days = window["days"]
    totals = {k: [0] * days for k in ("sessions", "artifacts", "assets")}
    for _, v in live:
        for k in totals:
            for i, n in enumerate(v["daily"].get(k) or []):
                if i < days:
                    totals[k][i] += n
    series = [{"label": lab, "values": totals[k], "value": str(sum(totals[k])), "note": "per day"}
              for k, lab in (("sessions", "sessions"), ("artifacts", "files written"), ("assets", "assets"))
              if chart_earns_place(totals[k])]
    if series:
        sections.append({"kind": "spark", "heading": "momentum", "series": series,
                         "caption": f"every live thread combined, last {days} days"})

    # Comparison bars: single value per series puts render_bars in shared-scale
    # horizontal mode, which is the honest way to compare threads.
    weights = [(title_case(k), len(v["deliverables"]) * 3 + len(v["artifacts"]) + len(v["assets"]))
               for k, v in live]
    weights = [w for w in weights if w[1] > 0][:10]
    if len(weights) >= 3 and len({w[1] for w in weights}) > 1:
        sections.append({"kind": "bars", "heading": "where the work *went*",
                         "caption": "weighted: deliverables ×3 + files + assets",
                         "series": [{"label": n, "values": [v]} for n, v in weights]})

    links = []
    for k, v in live:
        stat = v.get("status") or v.get("stage")
        links.append({"k": (stat or "THREAD").upper()[:9], "title": title_case(k),
                      "path": f"deliverables/research-briefs/mission-{k}/mission-{k}-brief.html"})
    sections.append({"kind": "related", "heading": "every live *thread*",
                     "tag": "OPEN ONE", "links": links})

    shipped = bundle.get("also_shipped") or []
    if shipped:
        sections.append({"kind": "timeline", "heading": "also shipped",
                         "tag": "NO LIVE THREAD",
                         "items": [{"date": s["date"], "title": s["workflow"] or s["type"] or "deliverable",
                                    "body": s["output"], "done": True} for s in shipped[:12]]})

    caveats = [synth.get("caveats") or
               "This board is assembled mechanically from the handoff store, the finalize ledger, "
               "the session ledgers and the asset manifest. Nothing here is interpretation."]
    over = bundle.get("overflow") or []
    if over:
        caveats.append(f"{len(over)} more threads cleared the bar but sit below the "
                       f"{len(live)}-card ceiling and were not carded: "
                       + ", ".join(title_case(k) for k in over[:12]) + ".")
    if bundle.get("filtered_out"):
        caveats.append(f"{len(bundle['filtered_out'])} keys were seen but never declared a thread "
                       "(no live handoff, no open mission, no finalized deliverable) — activity "
                       "alone does not mint a mission.")
    if bundle.get("degraded"):
        caveats.append("Sources unavailable on this sweep: " + "; ".join(bundle["degraded"]))
    sections.append({"kind": "caveats", "heading": "what this board *isn't*",
                     "kicker": "READ THE EDGES", "body": "\n\n".join(caveats)})

    return {
        "slug": BOARD_SLUG,
        "chip": "MISSION BOARD · ALL THREADS",
        "title": "the *board*",
        "dek": "Every live thread in one place, newest first. Open the one you're resuming.",
        "window": f"last {window['days']} days",
        "lens": "claude · codex",
        "sources": f"{c['sessions']} sessions swept",
        "compiled": human_date(bundle["generated"]),
        "footer_left": "ANTIGRAVITY · MISSION SWEEP",
        "footer_right": "@farricecain",
        "category": CATEGORY,
        "priority": 1,
        "status": "active",  # Mission-board is always active (never archived)
        "sections": sections,
    }


# ── commands ────────────────────────────────────────────────────────
def _save_brief(brief):
    """Write one mission brief through the SHARED brief writer.

    This used to inline its own html+json writes, which quietly dropped two
    files every other brief in the Room has: the `.md` agent-paste mirror and
    the `-context.json` pack. Those are not decoration — the md is what gets
    pasted into a chat, and the context pack is what makes a brief hand-off-able
    to an agent. One writer, one layout: render_brief.write_brief().

    `share=True` is deliberate here: a mission brief is the thing most likely to
    be forwarded, and the share variant is the only form safe to send outward
    (internal file paths stripped).
    """
    return render_brief.write_brief(brief, share=True)


def cmd_build(args):
    bundle = load(SWEEP_LATEST)
    if not bundle.get("threads"):
        print("[mission_brief] no sweep bundle — run: python3 execution/session_sweep.py run")
        return 0
    synth_all = load(SYNTHESIS, {})
    targets = bundle["threads"]
    if args.slug:
        key = args.slug.replace("mission-", "")
        if key not in targets:
            print(f"[mission_brief] '{key}' is not a promoted thread. "
                  f"Live: {', '.join(sorted(targets))}")
            return 0
        targets = {key: targets[key]}

    written = []
    for slug, t in targets.items():
        brief = build_brief(slug, t, bundle, synth_all.get(slug, {}))
        try:
            _save_brief(brief)
            written.append(brief["slug"])
        except Exception as e:  # noqa: BLE001 — one bad thread must not stop the rest
            print(f"[mission_brief] FAIL {slug}: {type(e).__name__}: {e}", file=sys.stderr)

    if not args.slug:
        board = build_board(bundle, synth_all.get(BOARD_SLUG, {}))
        try:
            _save_brief(board)
            written.append(BOARD_SLUG)
        except Exception as e:  # noqa: BLE001
            print(f"[mission_brief] FAIL board: {type(e).__name__}: {e}", file=sys.stderr)

    # Reawaken: a thread that came back gets un-archived so it returns to the
    # front tab instead of staying shelved by the 14-day currency policy.
    revived = []
    for slug in targets:
        j = BRIEFS / f"mission-{slug}" / f"mission-{slug}-brief.json"
        try:
            meta = json.loads(j.read_text(encoding="utf-8"))
            if meta.get("status") == "archived":
                meta["status"] = "active"
                j.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
                revived.append(slug)
        except (OSError, ValueError):
            continue

    if not args.quiet:
        print(f"[mission_brief] {len(written)} brief(s) written: {', '.join(written[:6])}"
              + (" …" if len(written) > 6 else ""))
        if revived:
            print(f"[mission_brief] reawakened from the shelf: {', '.join(revived)}")

    if not args.no_index:
        try:
            import brief_library
            brief_library.generate(open_after=False)
        except Exception as e:  # noqa: BLE001
            print(f"[mission_brief] index refresh skipped: {type(e).__name__}: {e}")
    return 0


def cmd_slots(args):
    bundle = load(SWEEP_LATEST)
    payload = {
        "contract": ("Write ONLY these keys, per thread slug. Every number, path, date and "
                     "link in the brief is already filled from the sweep bundle and must not "
                     "be restated or amended here."),
        "file": str(SYNTHESIS.relative_to(ROOT)),
        "slots": SLOTS,
        "threads": sorted(bundle.get("threads", {})) + [BOARD_SLUG],
    }
    print(json.dumps(payload, indent=2))
    return 0


def cmd_status(args):
    bundle = load(SWEEP_LATEST)
    live = sorted(bundle.get("threads", {}))
    built = sorted(p.name.replace("mission-", "") for p in BRIEFS.glob("mission-*")) if BRIEFS.exists() else []
    print(json.dumps({
        "sweep_generated": bundle.get("generated"),
        "live_threads": live,
        "briefs_on_disk": built,
        "missing": [s for s in live if s not in built],
        "synthesis_present": SYNTHESIS.exists(),
    }, indent=2))
    return 0


def main():
    ap = argparse.ArgumentParser(description="Render one living brief per ongoing thread.")
    sub = ap.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build", help="Render mission briefs from the latest sweep.")
    b.add_argument("--slug", default="", help="One thread only (default: all + the board).")
    b.add_argument("--all", action="store_true", help="Explicit all — the default.")
    b.add_argument("--no-index", action="store_true", help="Skip the Briefing Room index refresh.")
    b.add_argument("--quiet", action="store_true")
    s = sub.add_parser("slots", help="Print the synthesis contract (what a judge may write).")
    s.add_argument("--json", action="store_true")
    sub.add_parser("status", help="What's live vs what's on disk.")
    args = ap.parse_args()
    try:
        return {"build": cmd_build, "slots": cmd_slots, "status": cmd_status}[args.command](args)
    except Exception as e:  # noqa: BLE001
        print(f"[mission_brief] FAILED (non-blocking): {type(e).__name__}: {e}", file=sys.stderr)
        return 0


if __name__ == "__main__":
    sys.exit(main())
