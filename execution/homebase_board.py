#!/usr/bin/env python3
"""homebase_board.py — THE hub surface of the Readout OS (2026-08-20;
Agentic OS cockpit 2026-08-21).

Renders .agent/homebase/homebase.html: the one page Farrice opens to work.
Above the fold: the COCKPIT — brand header with live clock, center second-brain
portal ringed by the newest artifacts, widget columns (micro apps, focus,
needs-you, skills deck, routines, system counts) that drag-reorder and persist
locally. Below the fold: LAUNCH (resumable threads) and LIBRARY (briefs, asset
shelf, catalog) exactly as before. Served at / by pulse_serve.py; every deeper
surface is one nav hop away.

WHY (Farrice, 2026-08-20, verbatim): "a full working assets or homebase I can
rely on and can consistently work with or from so I have an actual system and
not context switching… work more fluently and easily without having to keep
switching between different tabs."
WHY 2.0 (Farrice, 2026-08-21): the ARMS-video command center "is the missing
piece — what I was trying to explain visually" — replicated here in his own
Ink + Steel Blue system, fully functional, never fancy-but-dead.

Doctrine (docs/solutions/2026-08-06-live-local-board-pattern.md):
- Reads .agent/sweep/latest.json + existing ledgers — NEVER a second collector.
- Reuses pulse_dashboard's readers/cards — one calc per fact, everywhere.
- Dual-mode JS: served → POST /action; file:// → buttons copy the honest CLI.
- Palette/typography interpolated from board_theme.theme_css() — one skin,
  client reskin = alternate token dict.
Design: Farrice Cain Premium Minimal report dialect. The asset shelf is the
one sanctioned dark interruption in the sequence.
"""
import glob
import html
import json
import math
import os
import plistlib
import sys
import time
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "execution"))

import pulse_dashboard as pd  # noqa: E402 — shared readers/cards, one source of calc
from board_theme import theme_css  # noqa: E402 — one palette for every surface
from degrade import degraded, degraded_html  # noqa: E402

OUT = os.path.join(ROOT, ".agent", "homebase", "homebase.html")
SWEEP = os.path.join(ROOT, ".agent", "sweep", "latest.json")
DECK_FILE = os.path.join(ROOT, ".agent", "homebase", "skills-deck.json")
DECK_RUNS = os.path.join(ROOT, ".agent", "homebase", "deck-runs")


def esc(s):
    return html.escape(str(s or ""))


def _rel(p):
    """Repo-relative posix path for dual-mode media/link resolution."""
    try:
        return Path(p).resolve().relative_to(Path(ROOT).resolve()).as_posix()
    except ValueError:
        return None


def _age_words(iso):
    try:
        t = time.mktime(time.strptime(iso[:19], "%Y-%m-%dT%H:%M:%S"))
        h = max(0, int((time.time() - t) // 3600))
        return f"{h}h ago" if h < 48 else f"{h // 24}d ago"
    except Exception:
        return "age unknown"


def load_sweep():
    try:
        return json.load(open(SWEEP, encoding="utf-8"))
    except (OSError, ValueError) as e:
        return degraded(None, "sweep bundle unreadable — launch zone degrades", e)


def launch_cards(sweep):
    """THE thread card (2026-08-20 collapse): the one merged shape that
    replaced Pulse's thread_cards and Mission Control's card. Shows the
    why-needs-you fact, stage, idle recency; acts with resume / brief /
    context / done / park / kill. Pinned first, then needs-you rank, then
    idle; parked sinks."""
    if not sweep:
        return degraded_html(
            "launch zone unavailable — .agent/sweep/latest.json unreadable; "
            "run python3 execution/session_sweep.py run", None)
    import mission_board as mb
    try:
        synth_all = json.load(open(os.path.join(ROOT, ".agent", "sweep", "synthesis.json"),
                                   encoding="utf-8"))
    except (OSError, ValueError):
        synth_all = {}
    wdays = (sweep.get("window") or {}).get("days", 14)
    rank = {"blocked": 0, "mid-build": 1, "active": 2, "ready": 3, "parked": 9}
    threads = list((sweep.get("threads") or {}).items())
    threads.sort(key=lambda kv: (0 if kv[1].get("pin") else 1,
                                 rank.get(kv[1].get("status"), 2),
                                 -mb.idle_days(kv[1], wdays)))
    cards = []
    for slug, t in threads[:12]:
        pin = " 📌" if t.get("pin") else ""
        scls = {"blocked": "crit", "mid-build": "warn", "ready": "ok",
                "active": "ok", "parked": "muted"}.get(t.get("status"), "muted")
        stage = (f'<span class="pill muted">{esc(t.get("stage"))}</span>'
                 if t.get("stage") else "")
        _, why = mb.why_needs_you(t, wdays)
        why_html = f'<p class="last">⚑ {esc(why)}</p>' if why else ""
        synth = synth_all.get(slug) or {}
        read_html = ""
        if synth.get("operator_read") or synth.get("next_move"):
            read = synth.get("operator_read") or ""
            move = synth.get("next_move") or ""
            read_html = (f'<p class="read">{esc(read)}'
                         + (f' <b>➤ {esc(move)}</b>' if move else "") + '</p>')
        hint = t.get("resume_hint") or ""
        hint_html = (f'<p class="last">↪ {esc(hint[:150])}</p>'
                     if hint and hint != t.get("title") else "")
        unf = (f'<p class="last">⧗ {esc(str(t.get("unfinished"))[:150])}</p>'
               if t.get("unfinished") else "")
        made = []
        if t.get("deliverables"):
            made.append(f'{len(t["deliverables"])} deliverable(s)')
        if t.get("assets"):
            made.append(f'{len(t["assets"])} asset(s)')
        if t.get("sessions"):
            made.append(f'{len(t["sessions"])} session(s)')
        idle = mb.days_since(t.get("last_active"))
        when = ("today" if (idle is not None and idle <= 0)
                else (f"last {idle}d ago" if idle is not None else "no activity in window"))
        brief_rel = f"deliverables/research-briefs/mission-{slug}/mission-{slug}-brief.html"
        brief_btn = ""
        if os.path.isfile(os.path.join(ROOT, brief_rel)):
            brief_btn = (f'<a class="actbtn alink" href="{esc((Path(ROOT) / brief_rel).as_uri())}"'
                         f' data-repo="/repo/{esc(brief_rel)}">open brief ↗</a>')
        open_mission = next((m for m in t.get("missions", []) if m.get("open")), None)
        mission_btns = ""
        if open_mission:
            mslug = esc(open_mission.get("slug") or slug)
            mission_btns = (
                f'<button class="actbtn ok" type="button" data-action="done" data-slug="{mslug}">✓ done</button>'
                f'<button class="actbtn" type="button" data-action="park" data-slug="{mslug}">park</button>')
        kill_btn = (f'<button class="actbtn kill" type="button" data-action="kill" '
                    f'data-slug="{esc(slug)}">kill</button>')
        ctx_btn = (f'<button class="copybtn" type="button" '
                   f'data-copy="{esc(mb.context_pack(slug, t))}">copy context</button>')
        cards.append(
            f'<div class="mcard">'
            f'<div class="row1"><h3>{esc(str(t.get("title") or slug)[:120])}{pin}</h3>'
            f'<span class="pill {scls}">{esc(t.get("status"))}</span>{stage}</div>'
            f'{why_html}{read_html}{hint_html}{unf}'
            f'<div class="meta"><span class="m">{esc(" · ".join(made) or "quiet")}</span>'
            f'<span class="m">{esc(when)}</span>'
            f'<span class="acts">'
            f'<button class="copybtn" type="button" data-copy="/resume {esc(slug)}">copy /resume</button>'
            f'{ctx_btn}{brief_btn}{mission_btns}{kill_btn}</span></div></div>')
    return "".join(cards) or '<div class="empty">no promoted threads in the sweep window</div>'


def asset_shelf():
    """The dark interruption: newest visual assets straight off the manifest.
    Thumbs resolve dual-mode via data-rel (live → /repo/, file:// → absolute)."""
    try:
        from asset_index import reduced_manifest
        from asset_gallery import thumb_name
        rows = [r for r in reduced_manifest().values()
                if r.get("status", "active") == "active"
                and r.get("type") in ("image", "video") and r.get("keep") is not False]
    except Exception as e:
        return degraded_html("asset shelf unavailable — asset_index failed; "
                             "run python3 execution/asset_index.py", e), 0
    total = len(rows)
    rows.sort(key=lambda r: r.get("ts") or "", reverse=True)
    tiles = []
    for r in rows[:8]:
        rel = str(r.get("path") or "")
        thumb_rel = f".agent/assets/thumbs/{thumb_name(rel)}"
        if not os.path.isfile(os.path.join(ROOT, thumb_rel)):
            continue
        label = (r.get("project") or r.get("zone") or "").replace("-", " ")[:24]
        kind = "▶" if r.get("type") == "video" else ""
        tiles.append(
            f'<a class="shelf-tile" href="{esc((Path(ROOT) / rel).as_uri())}" title="{esc(rel)}">'
            f'<img data-rel="{esc(thumb_rel)}" alt="{esc(label)}" loading="lazy">'
            f'<span class="shelf-cap">{kind} {esc(label)}</span></a>')
        if len(tiles) == 8:
            break
    if not tiles:
        return '<div class="empty">no thumbed assets yet — run python3 execution/asset_gallery.py</div>', total
    return "".join(tiles), total


def brief_rows():
    try:
        import brief_library as bl
        entries = [e for e in bl.collect() if e.get("status") != "archived"][:5]
    except Exception as e:
        return degraded_html("briefing room index unavailable — "
                             "run python3 execution/brief_library.py audit", e), 0, 0
    try:
        all_count = len(bl.collect())
    except Exception:
        all_count = len(entries)
    rows = []
    for e in entries:
        pri = f'<span class="pill warn">P{e["priority"]}</span>' if e.get("priority") else ""
        rows.append(
            f'<a class="intel" href="{esc(Path(e["html"]).as_uri())}">'
            f'<span class="ik">📋 {esc(e["category"])}</span>'
            f'<span class="it">{esc(str(e["title"]).replace("*", ""))}</span>'
            f'{pri}<span class="m">{esc(e["compiled"])}</span></a>')
    return "".join(rows) or '<div class="empty">no briefs yet</div>', all_count, len(entries)


def resume_strip():
    """Top merit-dormant items from the permanent catalog — the lost-merit fix
    on the front page (Farrice, 2026-08-20)."""
    try:
        import work_catalog as wc
        rows = wc.shelves()["resume"][:3]
    except Exception as e:
        return degraded_html("worth-resuming strip unavailable — run "
                             "python3 execution/work_catalog.py merge", e)
    if not rows:
        return '<div class="empty">nothing dormant with merit — clean</div>'
    cards = []
    for r in rows:
        tri = (r.get("triage") or {})
        why = tri.get("why") or (r.get("merit_why") or "")
        acts = []
        if r.get("resume"):
            acts.append(f'<button class="copybtn" type="button" data-copy="{esc(r["resume"])}">copy /resume</button>')
        if r.get("brief"):
            acts.append(f'<a class="actbtn alink" href="{esc((Path(ROOT) / r["brief"]).as_uri())}"'
                        f' data-repo="/repo/{esc(r["brief"])}">open brief ↗</a>')
        cards.append(
            f'<div class="mcard"><div class="row1"><h3>★ {esc(str(r.get("title"))[:100])}</h3>'
            f'<span class="pill ok">{esc(r.get("merit_why") or "merit")}</span></div>'
            + (f'<p class="last">{esc(why)}</p>' if why else "")
            + f'<div class="meta"><span class="m">last {esc((r.get("last_active") or "—")[:10])}</span>'
            f'<span class="acts">{"".join(acts)}</span></div></div>')
    return "".join(cards)


def system_counts():
    try:
        h = json.load(open(os.path.join(ROOT, ".agent", "health", "latest.json"),
                           encoding="utf-8"))
        a = h.get("assets") or {}
        return {"skills": a.get("skills"), "workflows": a.get("workflows"),
                "scripts": a.get("execution_scripts"), "solutions": a.get("solution_cards")}
    except (OSError, ValueError) as e:
        return degraded({}, "health receipt unreadable — system counts unknown", e)


# ── Agentic OS cockpit widgets (2026-08-21) ─────────────────────────────────

def _next_fire(cal):
    """Next epoch for one launchd StartCalendarInterval dict. launchd Weekday:
    0/7 = Sunday; python weekday(): Mon=0 → launchd = (py+1) % 7."""
    import datetime as dt
    now = dt.datetime.now()
    hours = [cal["Hour"]] if "Hour" in cal else list(range(24))
    minute = cal.get("Minute", 0)
    for d in range(0, 42):
        day = (now + dt.timedelta(days=d)).date()
        if "Day" in cal and day.day != cal["Day"]:
            continue
        if "Weekday" in cal and (day.weekday() + 1) % 7 != cal["Weekday"] % 7:
            continue
        for h in hours:
            cand = dt.datetime.combine(day, dt.time(hour=h, minute=minute))
            if cand > now:
                return cand.timestamp()
    return None


def _sched_words(d):
    """(schedule text, next-fire epoch|None, always_on) for one plist dict."""
    cal = d.get("StartCalendarInterval")
    if cal:
        cals = cal if isinstance(cal, list) else [cal]
        nxt = min((n for n in (_next_fire(c) for c in cals) if n), default=None)
        c0 = cals[0]
        wd = {0: "Sun", 1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 7: "Sun"}
        parts = []
        if "Weekday" in c0:
            parts.append(wd.get(c0["Weekday"], "?"))
        if "Day" in c0:
            parts.append(f"day {c0['Day']}")
        parts.append(f"{c0.get('Hour', 0):02d}:{c0.get('Minute', 0):02d}"
                     if "Hour" in c0 else f":{c0.get('Minute', 0):02d} hourly")
        if len(cals) > 1:
            parts.append(f"×{len(cals)}")
        return " ".join(parts), nxt, False
    si = d.get("StartInterval")
    if si:
        return (f"every {si // 3600}h" if si >= 3600 else f"every {si // 60}m"), time.time() + si, False
    if d.get("KeepAlive"):
        return "always-on", None, True
    return "on load", None, False


def _in_words(epoch):
    if epoch is None:
        return ""
    s = int(epoch - time.time())
    if s < 0:
        return "now"
    if s < 3600:
        return f"in {s // 60}m"
    if s < 86400:
        return f"in {s // 3600}h {(s % 3600) // 60:02d}m"
    return f"in {s // 86400}d"


def routines_board(limit=12):
    """The routines firing board: every com.antigravity.* launchd job, next
    fire first, health-joined from the daily audit receipt. Read-only —
    launchd stays the scheduler, this is the window onto it."""
    try:
        recs = (json.load(open(os.path.join(ROOT, ".agent", "health", "latest.json"),
                               encoding="utf-8")).get("launchd") or {})
    except (OSError, ValueError):
        recs = {}
    rows = []
    for p in sorted(glob.glob(os.path.expanduser(
            "~/Library/LaunchAgents/com.antigravity.*.plist"))):
        try:
            d = plistlib.load(open(p, "rb"))
        except Exception:
            continue
        label = d.get("Label") or os.path.basename(p)[:-6]
        name = label.replace("com.antigravity.", "")
        sched, nxt, always = _sched_words(d)
        rec = recs.get(label) or {}
        exit_code = rec.get("last_exit")
        chip = ("ok" if exit_code == 0 else "crit" if isinstance(exit_code, int) and exit_code != 0
                else "muted")
        log = str(rec.get("log_path") or "")
        rows.append((nxt if nxt is not None else float("inf"), name, sched, always, chip, log))
    if not rows:
        return degraded_html("no routines found — ~/Library/LaunchAgents empty "
                             "or unreadable", None), 0

    def _row(name, sched, when, chip, log):
        log_attr = f' data-log="{esc(log)}" role="button" tabindex="0"' if log else ""
        cls = "routine haslog" if log else "routine"
        hint = ' title="click — open the last run log"' if log else ""
        return (f'<div class="{cls}"{log_attr}{hint}><span class="dot {chip}"></span>'
                f'<span class="rn">{esc(name)}</span>'
                f'<span class="rs">{esc(sched)}</span>'
                f'<span class="rt">{esc(when)}</span></div>')
    total = len(rows)
    fires = sorted([r for r in rows if not r[3]], key=lambda r: r[0])[:limit]
    always = [r for r in rows if r[3]]
    out = [_row(name, sched, _in_words(nxt), chip, log)
           for nxt, name, sched, _a, chip, log in fires]
    out += [_row(name, sched, "∞", chip, log)
            for _n, name, sched, _a, chip, log in always]
    return "".join(out), total


def artifact_ring(limit=24):
    """The ring around the portal: newest artifacts the system produced —
    briefs, assets, merit catalog entries, deck-run reports. All from existing
    indexes; never a second collector. Every node opens a popover with real
    actions (open / copy path) — a click never dead-ends on a raw file."""
    items = []
    try:
        import brief_library as bl
        for e in bl.collect()[:10]:
            if e.get("status") == "archived":
                continue
            rel = _rel(e["html"])
            if rel:
                items.append({"icon": "📋", "kind": "brief",
                              "title": str(e["title"]).replace("*", ""),
                              "date": str(e.get("compiled") or ""), "rel": rel})
    except Exception:
        pass
    try:
        from asset_index import reduced_manifest
        from asset_gallery import thumb_name
        rows = [r for r in reduced_manifest().values()
                if r.get("status", "active") == "active"
                and r.get("type") in ("image", "video") and r.get("keep") is not False]
        rows.sort(key=lambda r: r.get("ts") or "", reverse=True)
        for r in rows[:8]:
            rel = str(r.get("path") or "")
            if rel and os.path.isfile(os.path.join(ROOT, rel)):
                thumb_rel = f".agent/assets/thumbs/{thumb_name(rel)}"
                items.append({"icon": "▶" if r.get("type") == "video" else "🎨",
                              "kind": "asset",
                              "title": (r.get("project") or r.get("zone") or "asset").replace("-", " "),
                              "date": str(r.get("ts") or "")[:10], "rel": rel,
                              "thumb": (thumb_rel if os.path.isfile(
                                  os.path.join(ROOT, thumb_rel)) else None)})
    except Exception:
        pass
    try:
        import work_catalog as wc
        for r in wc.shelves()["resume"][:6]:
            brel = str(r.get("brief") or "")
            if brel and os.path.isfile(os.path.join(ROOT, brel)):
                items.append({"icon": "★", "kind": "work",
                              "title": str(r.get("title") or "catalog entry"),
                              "date": str(r.get("last_active") or "")[:10],
                              "rel": brel, "resume": r.get("resume")})
    except Exception:
        pass
    try:
        for p in sorted(glob.glob(os.path.join(DECK_RUNS, "*.json")), reverse=True)[:6]:
            d = json.load(open(p, encoding="utf-8"))
            rel = d.get("report_rel")
            if rel and os.path.isfile(os.path.join(ROOT, rel)):
                items.append({"icon": "⚙", "kind": "run",
                              "title": f"deck · {d.get('card_id', 'run')}",
                              "date": str(d.get("ended") or d.get("started") or "")[:16],
                              "rel": rel})
    except Exception:
        pass
    # dedupe by target (a brief can arrive via briefs AND the catalog)
    seen, deduped = set(), []
    for it in items:
        if it["rel"] in seen:
            continue
        seen.add(it["rel"])
        deduped.append(it)
    deduped.sort(key=lambda i: i.get("date") or "", reverse=True)
    items = deduped[:limit]
    n = max(len(items), 1)
    nodes = []
    for i, it in enumerate(items):
        ang = 2 * math.pi * i / n - math.pi / 2
        x = 50 + 46.5 * math.cos(ang)
        y = 50 + 46.5 * math.sin(ang)
        uri = (Path(ROOT) / it["rel"]).as_uri()
        face = (f'<img data-rel="{esc(it["thumb"])}" alt="">' if it.get("thumb")
                else f'<span class="ri">{it["icon"]}</span>')
        resume_attr = f' data-resume="{esc(it["resume"])}"' if it.get("resume") else ""
        nodes.append(
            f'<a class="ringnode" style="left:{x:.2f}%;top:{y:.2f}%;animation-delay:{i * 35}ms"'
            f' href="{esc(uri)}" data-repo="/repo/{esc(it["rel"])}"'
            f' data-search="{esc(it["title"].lower())}" data-kind="{esc(it["kind"])}"'
            f' data-title="{esc(it["title"])}" data-date="{esc(it["date"])}"'
            f' data-relpath="{esc(it["rel"])}"{resume_attr}>'
            f'{face}</a>')
    return "".join(nodes), len(items)


def _deck_receipts():
    out = []
    for p in sorted(glob.glob(os.path.join(DECK_RUNS, "*.json")), reverse=True):
        try:
            out.append(json.load(open(p, encoding="utf-8")))
        except (OSError, ValueError):
            continue
    return out


def _receipt_age_min(d):
    try:
        t = time.mktime(time.strptime(str(d.get("started"))[:19], "%Y-%m-%dT%H:%M:%S"))
        return (time.time() - t) / 60
    except Exception:
        return 9999


def skills_deck():
    """Deck cards from the curated skills-deck.json — model + effort pickers,
    Run fires POST /action run_skill (guarded server-side by
    skill_deck_runner.py). A fresh in-flight run disables the deck (session
    lock is global — the UI says so instead of letting a click bounce).
    Receipts from deck-runs/ listed below the cards; a 'running' receipt older
    than 35 min renders as stalled, never as forever-running."""
    try:
        deck = json.load(open(DECK_FILE, encoding="utf-8"))
        cards_def = deck.get("cards") or []
    except (OSError, ValueError):
        return ('<div class="empty">deck not configured — create '
                '.agent/homebase/skills-deck.json</div>')
    receipts = _deck_receipts()
    live = next((d for d in receipts
                 if d.get("state") == "running" and _receipt_age_min(d) < 35), None)
    cards = []
    for c in cards_def:
        cid = esc(c.get("id"))
        models = c.get("models") or ["sonnet"]
        efforts = c.get("efforts") or ["medium"]
        mo = "".join(f'<option{" selected" if m == c.get("default_model") else ""}>{esc(m)}</option>'
                     for m in models)
        eo = "".join(f'<option{" selected" if e == c.get("default_effort") else ""}>{esc(e)}</option>'
                     for e in efforts)
        if live and live.get("card_id") == c.get("id"):
            btn = '<button class="actbtn warn dk-live" type="button" disabled>● running…</button>'
        elif live:
            btn = ('<button class="actbtn dk-run" type="button" disabled '
                   'title="one run at a time — the session lock is global">▸ run</button>')
        else:
            btn = '<button class="actbtn ok dk-run" type="button">▸ run</button>'
        last = next((d for d in receipts if d.get("card_id") == c.get("id")
                     and d.get("state") != "running"), None)
        last_line = ""
        if last:
            cost = last.get("total_cost_usd")
            cost_s = f"${cost:.2f}" if isinstance(cost, (int, float)) else "n/a"
            ok = "✓" if last.get("state") == "done" else "✕"
            last_line = (f'<span class="m">last {ok} '
                         f'{esc(str(last.get("ended") or "")[5:16])} · {esc(cost_s)}</span>')
        cards.append(
            f'<div class="deckcard" data-card="{cid}">'
            f'<div class="row1"><h3>{esc(c.get("command"))}</h3>{last_line}</div>'
            f'<p class="last">{esc(c.get("blurb"))}</p>'
            f'<div class="meta"><select class="dk-model">{mo}</select>'
            f'<select class="dk-effort">{eo}</select>'
            f'<span class="acts">{btn}</span>'
            f'</div></div>')
    runs = []
    for d in receipts[:3]:
        cost = d.get("total_cost_usd")
        cost_s = f"${cost:.2f}" if isinstance(cost, (int, float)) else "cost n/a"
        state = d.get("state", "done")
        stalled = state == "running" and _receipt_age_min(d) >= 35
        chip = ("muted" if stalled
                else {"done": "ok", "running": "warn", "failed": "crit"}.get(state, "muted"))
        label = "stalled" if stalled else state
        rep = d.get("report_rel")
        link = (f' <a class="actbtn alink" href="{esc((Path(ROOT) / rep).as_uri())}"'
                f' data-repo="/repo/{esc(rep)}">report ↗</a>') if rep else ""
        runs.append(f'<div class="routine"><span class="dot {chip}" title="{esc(label)}"></span>'
                    f'<span class="rn">{esc(d.get("card_id"))}</span>'
                    f'<span class="rs">{esc(d.get("model", ""))} · {esc(d.get("effort", ""))}'
                    f' · {esc(cost_s)}</span>'
                    f'<span class="rt">{esc(str(d.get("ended") or d.get("started") or "")[5:16])}</span>{link}</div>')
    runs_html = (f'<div class="deckruns"><span class="m">last runs · measured cost</span>'
                 f'{"".join(runs)}</div>') if runs else ""
    return "".join(cards) + runs_html


def micro_apps():
    """The micro-apps rail: every surface of the OS, one hop away. Same
    dual-mode pattern as everywhere else (file:// href + data-route)."""
    apps = [
        ("🧠", "second brain", ".agent/brain/brain.html", "/brain", "workspace graph"),
        ("🎛", "intelligence", "_active/farrice-brand/intelligence/index.html",
         "/intelligence", "farrice intel layer"),
        ("🏛", "library", ".agent/catalog/library.html", "/library", "permanent catalog"),
        ("📋", "briefing room", "deliverables/research-briefs/index.html", "/room", "all briefs"),
        ("🎨", "asset board", ".agent/assets/assets-board.html", "/assets", "generations"),
        ("🔮", "oracle", ".agent/oracle/oracle-dashboard.html", "/oracle", "mastery forge"),
        ("🗺", "mission board",
         "deliverables/research-briefs/mission-board/mission-board-brief.html",
         "/repo/deliverables/research-briefs/mission-board/mission-board-brief.html",
         "mission map"),
        ("📄", "docs", ".agent/mdview/index.html", "/repo/.agent/mdview/index.html", "md mirrors"),
    ]
    rows = []
    for icon, label, rel, route, blurb in apps:
        if not os.path.isfile(os.path.join(ROOT, rel)):
            continue
        uri = (Path(ROOT) / rel).as_uri()
        rows.append(f'<a class="app" href="{esc(uri)}" data-route="{esc(route)}">'
                    f'<span class="ai">{icon}</span><span class="al">{esc(label)}</span>'
                    f'<span class="ab">{esc(blurb)}</span></a>')
    return "".join(rows) or '<div class="empty">no surfaces generated yet</div>'


# ── page assembly ────────────────────────────────────────────────────────────

CSS = """
* { box-sizing:border-box; }
body { background:var(--ground); color:var(--ink); font:14px/1.5 var(--sans); margin:0; padding:32px 24px 80px; }
.wrap { max-width:1400px; margin:0 auto; display:flex; flex-direction:column; gap:18px; }
header { display:flex; align-items:baseline; gap:14px; flex-wrap:wrap; }
.kicker { font-family:var(--mono); font-size:9px; letter-spacing:.22em; text-transform:uppercase; color:var(--muted); display:block; margin-bottom:8px; }
h1 { font-size:38px; font-weight:700; letter-spacing:-.022em; margin:0; line-height:1.05; }
h1 em { font-family:var(--serif); font-style:italic; font-weight:400; color:var(--accent); }
.homenav { margin-left:auto; display:flex; gap:6px; align-items:center; flex-wrap:wrap; }
.homenav a, .homenav .here { font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; text-decoration:none;
  color:var(--soft); border:1px solid var(--line); border-radius:99px; padding:4px 11px; }
.homenav a:hover { border-color:var(--accent); color:var(--accent); }
.homenav .here { opacity:.45; border-style:dashed; }
.stamp { color:var(--muted); font-family:var(--mono); font-size:10px; letter-spacing:.1em; text-transform:uppercase;
  display:flex; gap:10px; align-items:center; flex-wrap:wrap; border-top:1px solid var(--ink); padding-top:10px; }
.zone { font-family:var(--mono); font-size:9px; letter-spacing:.26em; text-transform:uppercase; color:var(--accent);
  margin:8px 0 -8px; }
.sprint { background:var(--panel); border:1px solid var(--accent); border-radius:8px; padding:12px 16px;
  display:flex; gap:12px; align-items:baseline; flex-wrap:wrap; }
.sprint-tag { font-family:var(--mono); font-size:9px; letter-spacing:.18em; color:var(--accent); text-transform:uppercase; }
/* ── cockpit grid ── */
.cockpit { display:grid; grid-template-columns:minmax(250px,300px) 1fr minmax(300px,340px); gap:16px; align-items:start; }
.col { display:flex; flex-direction:column; gap:16px; min-width:0; }
@media (max-width:1100px) { .cockpit { grid-template-columns:1fr; } .stagewrap { order:-1; } }
.widget { position:relative; }
.widget .grip { position:absolute; top:14px; right:14px; cursor:grab; color:var(--muted); font-size:11px;
  user-select:none; letter-spacing:2px; opacity:0; transition:opacity .15s; }
.widget:hover .grip { opacity:.7; }
.widget .grip:hover { color:var(--accent); opacity:1; }
.widget.dragging { opacity:.4; }
.widget .wbody { max-height:420px; overflow:auto; resize:vertical; }
/* stage — the second-brain portal + artifacts ring */
.stagewrap { display:flex; flex-direction:column; gap:10px; align-items:center; }
.stage { position:relative; width:100%; max-width:640px; aspect-ratio:1/1; margin:0 auto; }
.portal { position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); width:56%; aspect-ratio:1/1;
  border-radius:50%; border:1px solid var(--line); display:block; cursor:pointer; background:var(--panel); }
.portal:hover { border-color:var(--accent); }
.portal canvas { width:100%; height:100%; display:block; border-radius:50%; }
.portal .pcap { position:absolute; left:50%; bottom:12%; transform:translateX(-50%); font-family:var(--mono);
  font-size:8.5px; letter-spacing:.22em; text-transform:uppercase; color:var(--muted); white-space:nowrap; }
.portal:hover .pcap { color:var(--accent); }
.ringnode { position:absolute; transform:translate(-50%,-50%); width:36px; height:36px; border-radius:50%;
  border:1px solid var(--line); background:var(--panel); display:flex; align-items:center; justify-content:center;
  text-decoration:none; font-size:13px; overflow:hidden; cursor:pointer;
  transition:transform .12s ease, border-color .12s ease, opacity .2s;
  animation:ringin .4s ease both; }
@keyframes ringin { from { opacity:0; transform:translate(-50%,-50%) scale(.4); }
  to { opacity:1; transform:translate(-50%,-50%) scale(1); } }
@media (prefers-reduced-motion: reduce) { .ringnode { animation:none; } }
.ringnode img { width:100%; height:100%; object-fit:cover; display:block; }
.ringnode:hover { transform:translate(-50%,-50%) scale(1.35); border-color:var(--accent); z-index:5; }
.ringnode.dim { opacity:.18; }
.ringnode.hit { border-color:var(--accent); box-shadow:0 0 0 2px var(--panel), 0 0 0 3px var(--accent); }
/* ring popover — the click target every node deserves */
#ringpop { position:absolute; z-index:20; width:250px; background:var(--panel); border:1px solid var(--accent);
  border-radius:8px; padding:12px 14px; display:none; }
#ringpop.show { display:block; }
#ringpop h4 { font-size:12.5px; font-weight:700; margin:0 0 2px; line-height:1.35; }
#ringpop .pk { font-family:var(--mono); font-size:8px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted);
  display:block; margin-bottom:8px; }
#ringpop .pa { display:flex; gap:6px; flex-wrap:wrap; }
.ringbar { display:flex; gap:10px; align-items:center; width:100%; max-width:520px; }
.ringbar input { flex:1; font-family:var(--mono); font-size:11px; letter-spacing:.06em; background:var(--panel);
  color:var(--ink); border:1px solid var(--line); border-radius:99px; padding:8px 16px; outline:none; }
.ringbar input:focus { border-color:var(--accent); }
#ringcap { font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted);
  min-height:14px; text-align:center; }
/* clock */
.clock { font-variant-numeric:tabular-nums; }
.clock .ct { font-size:40px; font-weight:700; letter-spacing:-.02em; line-height:1; }
.clock .ct .ap { font-family:var(--serif); font-style:italic; font-weight:400; color:var(--accent); font-size:20px; }
.clock .cd { font-family:var(--mono); font-size:9px; letter-spacing:.18em; text-transform:uppercase; color:var(--muted); margin-top:6px; }
/* micro apps */
.app { display:flex; gap:10px; align-items:baseline; text-decoration:none; color:var(--ink);
  border-bottom:1px solid var(--line); padding:8px 2px; }
.app:last-child { border-bottom:none; }
.app:hover .al { color:var(--accent); }
.app .ai { width:18px; text-align:center; }
.app .al { font-size:12.5px; font-weight:600; flex:0 0 auto; }
.app .ab { font-family:var(--mono); font-size:8px; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); margin-left:auto; }
/* routines */
.routine { display:flex; gap:8px; align-items:baseline; border-bottom:1px solid var(--line); padding:6px 2px; }
.routine.haslog { cursor:pointer; }
.routine.haslog:hover .rn { color:var(--accent); }
.routine.haslog:hover::after { content:"log ↗"; font-family:var(--mono); font-size:8px; letter-spacing:.1em;
  text-transform:uppercase; color:var(--accent); margin-left:2px; }
.routine:last-child { border-bottom:none; }
.routine .dot { width:6px; height:6px; border-radius:50%; background:var(--line); flex:0 0 auto; align-self:center; }
.routine .dot.ok { background:var(--ok); } .routine .dot.crit { background:var(--crit); } .routine .dot.muted { background:var(--line); }
.routine .rn { font-size:11.5px; font-weight:600; flex:1; min-width:0; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
.routine .rs { font-family:var(--mono); font-size:8px; letter-spacing:.1em; text-transform:uppercase; color:var(--muted); }
.routine .rt { font-family:var(--mono); font-size:8.5px; letter-spacing:.1em; color:var(--accent); white-space:nowrap; }
/* skills deck */
.deckcard { border:1px solid var(--line); border-radius:6px; background:var(--ground); padding:10px 12px; margin-bottom:8px; }
.deckcard h3 { font-family:var(--mono); font-size:11.5px; letter-spacing:.04em; margin:0; }
.deckcard select { font-family:var(--mono); font-size:9px; letter-spacing:.08em; text-transform:uppercase;
  background:var(--panel); color:var(--soft); border:1px solid var(--line); border-radius:4px; padding:2px 5px; }
.deckruns { margin-top:10px; border-top:1px solid var(--line); padding-top:8px; display:flex; flex-direction:column; gap:2px; }
/* tiles */
.tiles { display:grid; grid-template-columns:repeat(auto-fit,minmax(120px,1fr)); gap:12px; }
.cockpit .tiles { grid-template-columns:repeat(2,1fr); }
.tile { border-top:2px solid var(--ink); padding-top:10px; }
.tile a { color:inherit; text-decoration:none; }
.tile .n { font-size:28px; font-weight:700; letter-spacing:-.02em; font-variant-numeric:tabular-nums; }
.tile .l { color:var(--muted); font-family:var(--mono); font-size:8.5px; letter-spacing:.16em; text-transform:uppercase; margin-top:4px; }
section { background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:16px 18px; }
h2 { font-family:var(--mono); font-size:9px; letter-spacing:.2em; text-transform:uppercase;
  color:var(--muted); margin:0 0 12px; border-bottom:1px solid var(--line); padding-bottom:8px; }
.mcard { border:1px solid var(--line); border-radius:6px; background:var(--ground); padding:12px 14px; margin-bottom:10px; }
.mcard:last-child { margin-bottom:0; }
.mcard .row1 { display:flex; gap:10px; align-items:baseline; flex-wrap:wrap; }
.mcard h3 { font-size:13.5px; font-weight:600; margin:0; line-height:1.35; flex:1; min-width:200px; }
.mcard .gline { font-size:11.5px; color:var(--soft); margin-top:5px; }
.mcard .gline::before { content:"goal · "; font-family:var(--mono); font-size:8.5px; letter-spacing:.14em;
  text-transform:uppercase; color:var(--muted); }
.mcard .last { font-size:11.5px; color:var(--muted); margin:5px 0 0; line-height:1.45; }
.mcard .read { font-size:12px; color:var(--ink); margin:6px 0 0; line-height:1.5;
  border-left:2px solid var(--accent); padding-left:10px; }
.mcard .read b { color:var(--accent); font-weight:600; }
.mcard .meta { display:flex; gap:12px; align-items:center; margin-top:8px; flex-wrap:wrap; }
.m { font-family:var(--mono); font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }
.pill { font-family:var(--mono); font-size:8px; letter-spacing:.12em; text-transform:uppercase; padding:2px 8px;
  border-radius:3px; white-space:nowrap; font-weight:700; }
.pill.ok { color:var(--ok); border:1px solid var(--ok); }
.pill.warn { color:var(--warn); border:1px solid var(--warn); }
.pill.crit { color:var(--crit); border:1px solid var(--crit); }
.pill.muted { color:var(--muted); border:1px solid var(--line); }
.acts { margin-left:auto; display:flex; gap:6px; align-items:center; flex-wrap:wrap; }
.copybtn, .actbtn { font-family:var(--mono); font-size:8.5px; letter-spacing:.12em; text-transform:uppercase;
  cursor:pointer; background:none; border:1px solid var(--line); border-radius:4px; padding:3px 9px; color:var(--soft);
  text-decoration:none; display:inline-block; }
.copybtn:hover, .actbtn:hover { border-color:var(--accent); color:var(--accent); }
.actbtn.ok { color:var(--ok); border-color:var(--ok); }
.actbtn.ok:hover { background:var(--ok); color:var(--panel); }
.actbtn.kill { color:var(--crit); border-color:var(--crit); }
.actbtn.kill:hover { background:var(--crit); color:var(--panel); }
.actbtn.warn { color:var(--warn); border-color:var(--warn); }
.actbtn:disabled { opacity:.55; cursor:not-allowed; }
.actbtn.dk-live { animation:pulse 1.6s ease-in-out infinite; }
@keyframes pulse { 0%,100% { opacity:.55; } 50% { opacity:1; } }
.tile a[data-scrollto] { cursor:pointer; }
.tile a[data-scrollto]:hover .n { color:var(--accent); }
.tog { cursor:pointer; user-select:none; }
.tog::before { content:"▾ "; color:var(--accent); }
section.closed .tog { margin-bottom:0; border-bottom:none; padding-bottom:0; }
section.closed .tog::before { content:"▸ "; }
section.closed .body { display:none; }
.oform { display:none; gap:8px; margin-top:10px; flex-wrap:wrap; }
.oform.show { display:flex; }
.oform input { font-family:var(--mono); font-size:11px; background:var(--panel); color:var(--ink);
  border:1px solid var(--line); border-radius:4px; padding:6px 9px; }
.oform .o-rev { width:120px; }
.oform .o-out { flex:1; min-width:200px; }
.livechip { font-family:var(--mono); font-size:8px; letter-spacing:.14em; text-transform:uppercase; padding:2px 8px;
  border-radius:3px; font-weight:700; }
.intelgrid { display:flex; flex-direction:column; gap:8px; }
.intel { display:flex; gap:12px; align-items:baseline; text-decoration:none; color:var(--ink);
  border:1px solid var(--line); border-radius:6px; background:var(--ground); padding:10px 14px; flex-wrap:wrap; }
.intel:hover { border-color:var(--accent); }
.intel .ik { font-family:var(--mono); font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--accent); }
.intel .it { font-size:13px; font-weight:600; flex:1; min-width:200px; }
.roomlink { display:inline-block; margin-top:10px; margin-right:16px; font-family:var(--mono); font-size:9px; letter-spacing:.14em;
  text-transform:uppercase; color:var(--accent); text-decoration:none; }
.roomlink:hover { text-decoration:underline; }
.empty { color:var(--muted); font-style:italic; font-size:12.5px; }
/* the ONE dark interruption — asset shelf */
section.shelf { background:#101010; border-color:#101010; }
section.shelf h2 { color:#8c8c82; border-color:#2c2c2a; }
.shelfgrid { display:grid; grid-template-columns:repeat(auto-fill,minmax(150px,1fr)); gap:10px; }
.shelf-tile { display:block; text-decoration:none; border-radius:6px; overflow:hidden; background:#181817;
  border:1px solid #2c2c2a; transition:transform .15s ease; }
.shelf-tile:hover { transform:scale(1.03); border-color:#7c9fd9; }
.shelf-tile img { width:100%; aspect-ratio:4/3; object-fit:cover; display:block; }
.shelf-cap { display:block; padding:6px 9px; font-family:var(--mono); font-size:8px; letter-spacing:.12em;
  text-transform:uppercase; color:#8c8c82; }
section.shelf .roomlink { color:#7c9fd9; }
section.shelf .empty { color:#8c8c82; }
.sysline { font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }
#toast { position:fixed; bottom:24px; left:50%; transform:translateX(-50%); background:var(--ink); color:var(--panel);
  font-family:var(--mono); font-size:10px; letter-spacing:.14em; text-transform:uppercase; padding:9px 20px;
  border-radius:99px; opacity:0; transition:opacity .2s; pointer-events:none; z-index:99; }
#toast.show { opacity:1; }
footer { border-top:1px solid var(--ink); padding-top:12px; display:flex; justify-content:space-between;
  font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }
"""

SCRIPT = r"""
const PULSE_LIVE = location.protocol.startsWith('http');
const REPO_ROOT_URI = __REPO_ROOT_URI__;
if (PULSE_LIVE) {
  const lc = document.getElementById('livechip');
  lc.textContent = 'live — actions write instantly';
  lc.classList.remove('muted'); lc.classList.add('ok');
}
if (PULSE_LIVE) document.querySelectorAll('a[data-route]').forEach(a => { a.href = a.dataset.route; });
if (PULSE_LIVE) document.querySelectorAll('a[data-repo]').forEach(a => { a.href = a.dataset.repo; });
// dual-mode media: live pages load thumbs over /repo/, file:// pages from disk
document.querySelectorAll('img[data-rel]').forEach(img => {
  img.src = PULSE_LIVE ? '/repo/' + img.dataset.rel : REPO_ROOT_URI + '/' + img.dataset.rel;
});
function _toast(msg) {
  const t = document.getElementById('toast'); t.textContent = msg; t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 1600);
}
function _copy(txt, msg) {
  function done() { _toast(msg || 'copied'); }
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(txt).then(done, () => {
      const ta = document.createElement('textarea'); ta.value = txt; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); } catch (e) {}
      document.body.removeChild(ta); done();
    });
  }
}
function _sq(s) { return "'" + String(s).replace(/'/g, `'\\''`) + "'"; }
function _cli(action, args) {
  const base = 'python3 execution/pulse_actions.py ';
  if (action === 'done') return base + 'done ' + _sq(args.slug) + ' --outcome ' + _sq(args.outcome || '');
  if (action === 'park') return base + 'park ' + _sq(args.slug) + ' --reason ' + _sq(args.reason || '');
  if (action === 'refresh') return base + 'refresh';
  if (action === 'kill') return base + 'kill ' + _sq(args.slug) + ' --reason ' + _sq(args.reason || '');
  if (action === 'reopen') return base + 'reopen ' + _sq(args.slug);
  if (action === 'outcome') return base + 'outcome ' + _sq(args.deliverable) + ' --revenue ' + (args.revenue || 0) + ' --outcome ' + _sq(args.outcome || '');
  if (action === 'outcome-snooze') return base + 'outcome-snooze ' + _sq(args.deliverable);
  if (action === 'outcome-dismiss') return base + 'outcome-dismiss ' + _sq(args.deliverable);
  if (action === 'run_skill') return 'python3 execution/skill_deck_runner.py run ' + _sq(args.card_id) + ' --model ' + _sq(args.model) + ' --effort ' + _sq(args.effort);
  return base;
}
function doAction(action, args) {
  if (!PULSE_LIVE) { _copy(_cli(action, args), 'server offline — command copied'); return; }
  fetch('/action', { method: 'POST', headers: { 'Content-Type': 'application/json' },
                     body: JSON.stringify({ action, args }) })
    .then(r => r.json())
    .then(j => {
      if (j.ok) {
        if (action === 'run_skill') { _toast('deck run started — receipt lands when it finishes'); return; }
        _toast(action === 'refresh' ? 'refreshing data — page reloads when ready' : 'done — refreshing');
        if (action !== 'refresh') setTimeout(() => location.reload(), 700);
      }
      else { _toast(j.error ? ('failed — ' + j.error) : 'action failed — see server log'); }
    })
    .catch(() => { _copy(_cli(action, args), 'server unreachable — command copied'); });
}
document.querySelectorAll('.actbtn[data-action]').forEach(b => b.addEventListener('click', () => {
  const act = b.dataset.action;
  if (act === 'done') {
    const outcome = prompt('One-line outcome for the log:', 'closed from homebase');
    if (outcome === null) return;
    doAction('done', { slug: b.dataset.slug, outcome });
  } else if (act === 'park') {
    const reason = prompt('Park reason (one line):');
    if (reason === null) return;
    doAction('park', { slug: b.dataset.slug, reason });
  } else if (act === 'kill') {
    if (!confirm('Kill this thread? It disappears from every board (ledger-recoverable).')) return;
    const reason = prompt('Kill reason (required):');
    if (!reason) return;
    doAction('kill', { slug: b.dataset.slug, reason });
  } else if (act === 'reopen') {
    doAction('reopen', { slug: b.dataset.slug });
  } else if (act === 'outcome') {
    b.closest('.mcard').querySelector('.oform').classList.toggle('show');
  } else if (act === 'outcome-snooze') {
    doAction('outcome-snooze', { deliverable: b.closest('.mcard').dataset.deliverable });
  } else if (act === 'outcome-dismiss') {
    if (confirm('Mark as no-outcome-expected? (writes archived-no-data)'))
      doAction('outcome-dismiss', { deliverable: b.closest('.mcard').dataset.deliverable });
  } else if (act === 'refresh') {
    doAction('refresh', {});
  }
}));
document.querySelectorAll('.o-save').forEach(b => b.addEventListener('click', () => {
  const card = b.closest('.mcard');
  doAction('outcome', { deliverable: card.dataset.deliverable,
                        revenue: parseFloat(card.querySelector('.o-rev').value) || 0,
                        outcome: card.querySelector('.o-out').value || '' });
}));
document.querySelectorAll('.tog').forEach(h => h.addEventListener('click', () =>
  h.closest('section').classList.toggle('closed')));
document.querySelectorAll('.copybtn').forEach(b => b.addEventListener('click', () => {
  if (b.dataset.copy !== undefined) _copy(b.dataset.copy);
}));
// ── skills deck: run headlessly through the guarded server verb ──
document.querySelectorAll('.dk-run').forEach(b => b.addEventListener('click', () => {
  const card = b.closest('.deckcard');
  doAction('run_skill', { card_id: card.dataset.card,
                          model: card.querySelector('.dk-model').value,
                          effort: card.querySelector('.dk-effort').value });
}));
// ── live clock (textContent only — no markup injection) ──
function _tick() {
  const d = new Date();
  const hh = String(d.getHours() % 12 || 12).padStart(2, '0');
  const mm = String(d.getMinutes()).padStart(2, '0');
  const ss = String(d.getSeconds()).padStart(2, '0');
  const hmEl = document.getElementById('clockhm');
  if (hmEl) hmEl.textContent = hh + ':' + mm + ':' + ss;
  const apEl = document.getElementById('clockap');
  if (apEl) apEl.textContent = d.getHours() < 12 ? 'am' : 'pm';
  const dt = document.getElementById('clockdate');
  if (dt) dt.textContent = d.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' });
}
_tick(); setInterval(_tick, 1000);
// ── portal: dot-field sphere, brand accent, reduced-motion aware ──
(function () {
  const cv = document.getElementById('portalcv');
  if (!cv) return;
  const ctx = cv.getContext('2d');
  const N = 650, pts = [];
  for (let i = 0; i < N; i++) {
    const u = Math.random() * 2 - 1, th = Math.random() * Math.PI * 2;
    const r = Math.sqrt(1 - u * u);
    pts.push([r * Math.cos(th), u, r * Math.sin(th)]);
  }
  let ang = 0;
  const still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function frame() {
    const s = cv.clientWidth || 300;
    if (cv.width !== s * 2) { cv.width = s * 2; cv.height = s * 2; }
    const accent = getComputedStyle(document.documentElement).getPropertyValue('--accent').trim() || '#3d5a94';
    ctx.clearRect(0, 0, cv.width, cv.height);
    const c = cv.width / 2, R = cv.width * 0.36;
    for (const p of pts) {
      const x = p[0] * Math.cos(ang) + p[2] * Math.sin(ang);
      const z = -p[0] * Math.sin(ang) + p[2] * Math.cos(ang);
      const px = c + x * R, py = c + p[1] * R;
      const a = 0.12 + 0.5 * (z + 1) / 2;
      ctx.globalAlpha = a;
      ctx.fillStyle = accent;
      ctx.beginPath();
      ctx.arc(px, py, 1.1 + 1.3 * (z + 1) / 2, 0, 7);
      ctx.fill();
    }
    ctx.globalAlpha = 1;
    ang += 0.0028;
    if (!still) requestAnimationFrame(frame);
  }
  frame();
})();
// ── artifacts ring: hover caption, click popover, search filters ──
(function () {
  const inp = document.getElementById('ringsearch');
  if (!inp) return;
  const nodes = Array.from(document.querySelectorAll('.ringnode'));
  const cap = document.getElementById('ringcap');
  const stage = document.querySelector('.stage');
  const pop = document.getElementById('ringpop');
  function closePop() { pop.classList.remove('show'); }
  function openPop(n) {
    while (pop.firstChild) pop.removeChild(pop.firstChild);
    const h4 = document.createElement('h4'); h4.textContent = n.dataset.title; pop.appendChild(h4);
    const pk = document.createElement('span'); pk.className = 'pk';
    pk.textContent = (n.dataset.kind || '') + (n.dataset.date ? ' · ' + n.dataset.date : '');
    pop.appendChild(pk);
    const pa = document.createElement('div'); pa.className = 'pa';
    const open = document.createElement('a'); open.className = 'actbtn ok';
    open.textContent = 'open ↗'; open.href = n.href;
    if (n.dataset.kind === 'asset' || n.href.startsWith('file:')) {
      // http pages cannot hop to file:// — reuse the OS-opener route
      open.addEventListener('click', ev => {
        if (!PULSE_LIVE || !open.href.startsWith('file:')) return;
        ev.preventDefault();
        fetch('/action', { method: 'POST', headers: { 'Content-Type': 'application/json' },
                           body: JSON.stringify({ action: 'open-path', args: { uri: open.getAttribute('data-file') || open.href } }) })
          .then(r => r.json()).then(j => _toast(j.ok ? 'opened' : 'open failed'));
      });
    }
    pa.appendChild(open);
    const cp = document.createElement('button'); cp.className = 'actbtn'; cp.textContent = 'copy path';
    cp.addEventListener('click', () => _copy(n.dataset.relpath, 'path copied'));
    pa.appendChild(cp);
    if (n.dataset.resume) {
      const rs = document.createElement('button'); rs.className = 'actbtn'; rs.textContent = 'copy /resume';
      rs.addEventListener('click', () => _copy(n.dataset.resume));
      pa.appendChild(rs);
    }
    pop.appendChild(pa);
    const sr = stage.getBoundingClientRect();
    const nr = n.getBoundingClientRect();
    const cx = nr.left - sr.left + nr.width / 2;
    const cy = nr.top - sr.top + nr.height / 2;
    pop.classList.add('show');
    const w = pop.offsetWidth, h = pop.offsetHeight;
    let x = cx + (cx < sr.width / 2 ? 24 : -24 - w);
    let y = Math.min(Math.max(cy - h / 2, 4), sr.height - h - 4);
    pop.style.left = Math.min(Math.max(x, 4), sr.width - w - 4) + 'px';
    pop.style.top = y + 'px';
  }
  nodes.forEach(n => {
    n.addEventListener('mouseenter', () => { if (cap) cap.textContent = (n.dataset.title || '') + ' · ' + (n.dataset.date || ''); });
    n.addEventListener('mouseleave', () => { if (cap) cap.textContent = ''; });
    n.addEventListener('click', ev => { ev.preventDefault(); openPop(n); });
  });
  document.addEventListener('click', ev => {
    if (!pop.contains(ev.target) && !ev.target.closest('.ringnode')) closePop();
  });
  addEventListener('keydown', e => { if (e.key === 'Escape') closePop(); });
  inp.addEventListener('input', () => {
    const q = inp.value.trim().toLowerCase();
    let first = null;
    nodes.forEach(n => {
      const hit = !q || (n.dataset.search || '').includes(q);
      n.classList.toggle('dim', !!q && !hit);
      n.classList.toggle('hit', !!q && hit);
      if (hit && q && !first) first = n;
    });
    if (cap) cap.textContent = first ? (first.dataset.title + ' — Enter opens') : (q ? 'no artifact matches' : '');
  });
  inp.addEventListener('keydown', e => {
    if (e.key !== 'Enter') return;
    const hit = nodes.find(n => n.classList.contains('hit')) || null;
    if (hit) openPop(hit);
  });
})();
// ── routines: a row with a log opens it (live) or copies the path (static) ──
document.querySelectorAll('.routine[data-log]').forEach(r => r.addEventListener('click', () => {
  const p = r.dataset.log;
  if (PULSE_LIVE) {
    fetch('/action', { method: 'POST', headers: { 'Content-Type': 'application/json' },
                       body: JSON.stringify({ action: 'open-path', args: { uri: 'file://' + p } }) })
      .then(x => x.json()).then(j => _toast(j.ok ? 'log opened' : 'open failed'))
      .catch(() => _copy(p, 'server unreachable — path copied'));
  } else { _copy(p, 'log path copied'); }
}));
// ── focus tiles that point somewhere on this page scroll there ──
document.querySelectorAll('[data-scrollto]').forEach(a => a.addEventListener('click', ev => {
  ev.preventDefault();
  const t = document.getElementById(a.dataset.scrollto);
  if (!t) return;
  t.classList.remove('closed');
  t.scrollIntoView({ behavior: 'smooth', block: 'center' });
}));
// ── widget layout: drag to reorder within a column; order persists locally ──
(function () {
  const KEY = 'hb_layout_v2';
  const cols = ['col-left', 'col-right'].map(id => document.getElementById(id)).filter(Boolean);
  let saved = {};
  try { saved = JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) {}
  cols.forEach(col => {
    const order = saved[col.id];
    if (Array.isArray(order)) {
      order.forEach(wid => {
        const w = col.querySelector('.widget[data-wid="' + wid + '"]');
        if (w) col.appendChild(w);
      });
    }
  });
  function persist() {
    const out = {};
    cols.forEach(col => {
      out[col.id] = Array.from(col.querySelectorAll('.widget')).map(w => w.dataset.wid);
    });
    try { localStorage.setItem(KEY, JSON.stringify(out)); } catch (e) {}
  }
  let dragged = null;
  document.querySelectorAll('.widget').forEach(w => {
    const grip = w.querySelector('.grip');
    if (!grip) return;
    grip.addEventListener('mousedown', () => { w.setAttribute('draggable', 'true'); });
    w.addEventListener('dragstart', e => { dragged = w; w.classList.add('dragging'); e.dataTransfer.effectAllowed = 'move'; });
    w.addEventListener('dragend', () => {
      if (dragged) dragged.classList.remove('dragging');
      dragged = null; w.removeAttribute('draggable');
      persist();
    });
  });
  cols.forEach(col => {
    col.addEventListener('dragover', e => {
      if (!dragged) return;
      e.preventDefault();
      const after = Array.from(col.querySelectorAll('.widget:not(.dragging)'))
        .find(w => e.clientY < w.getBoundingClientRect().top + w.offsetHeight / 2);
      if (after) col.insertBefore(dragged, after); else col.appendChild(dragged);
    });
  });
})();
if (PULSE_LIVE) {
  // http pages cannot navigate to file:// — route those clicks through the server's OS opener.
  document.querySelectorAll('a[href^="file:"]:not([data-route]):not([data-repo])').forEach(a => a.addEventListener('click', ev => {
    ev.preventDefault();
    fetch('/action', { method: 'POST', headers: { 'Content-Type': 'application/json' },
                       body: JSON.stringify({ action: 'open-path', args: { uri: a.href } }) })
      .then(r => r.json()).then(j => _toast(j.ok ? 'opened' : 'open failed'))
      .catch(() => _toast('open failed'));
  }));
  // side-window live reload — refresh when the board regenerates underneath us
  let baseline = null;
  setInterval(() => {
    fetch('/ping').then(r => r.json()).then(j => {
      if (baseline === null) { baseline = j.homebase_mtime; return; }
      if (j.homebase_mtime && j.homebase_mtime !== baseline) location.reload();
    }).catch(() => {});
  }, 5000);
}
"""


def main():
    now = time.strftime("%Y-%m-%d %H:%M")
    sweep = load_sweep()
    sweep_age = _age_words(sweep.get("generated", "")) if sweep else "unknown"
    counts = (sweep or {}).get("counts") or {}

    # --- FOCUS: reuse the Pulse's own calcs — one source per fact ---
    missions = pd.jsonl(os.path.join(ROOT, ".agent", "missions.jsonl"))
    latest = {}
    for m in missions:
        latest[pd.mission_key(m)] = m
    active = [m for m in latest.values() if m.get("status") in ("compiled", "running")]
    active.sort(key=lambda m: -(pd.mission_age_days(m) or 0))
    goals, names = pd.load_goals()
    sprint = next((g for g in goals if "SPRINT" in (g.get("why") or "")), None)
    sprint_id = (sprint or {}).get("id")

    def _t23(m):
        return str(m.get("tier") or "").upper().startswith(("T2", "T3"))
    waiting = [m for m in latest.values() if _t23(m) and m.get("status") == "compiled"]
    stale = [m for m in active if (pd.mission_age_days(m) or 0) >= 7 and m not in waiting]
    flagged = waiting + stale
    flagged.sort(key=lambda m: (0 if (sprint_id and m.get("serves") == sprint_id) else 1,
                                0 if _t23(m) else 1,
                                -(pd.mission_age_days(m) or 0)))
    needs_you = flagged[:3]
    needs_html = ("".join(pd.mission_card(m, names, show_actions=True) for m in needs_you)
                  or '<div class="empty">nothing flagged — clean</div>')

    outcomes_html, due_count = pd.outcomes_due_cards()
    recent_done = [m for m in latest.values() if m.get("status") == "done"][-6:][::-1]
    closed_html = ("".join(pd.mission_card(m, names, show_verdict=True, show_reopen=True)
                   for m in recent_done) or '<div class="empty">none yet</div>')

    sprint_html = ""
    if sprint:
        import re as _re
        mm = _re.search(r"~(\d{2})-(\d{2})", sprint.get("why", ""))
        cd = ""
        if mm and 1 <= int(mm.group(1)) <= 12:
            deadline = time.mktime(time.strptime(
                f"{time.strftime('%Y')}-{mm.group(1)}-{mm.group(2)}", "%Y-%m-%d"))
            days = int((deadline - time.time()) // 86400)
            if 0 <= days <= 366:
                cd = f'<span class="pill warn">{days} days left</span>'
        sprint_html = (f'<div class="sprint"><span class="sprint-tag">ACTIVE SPRINT</span>'
                       f'<strong>{esc(sprint.get("target"))}</strong>{cd}'
                       f'{pd.money_line()}</div>')

    # --- LIBRARY ---
    briefs_html, brief_total, _shown = brief_rows()
    shelf_html, asset_total = asset_shelf()
    sc = system_counts()
    sys_line = " · ".join(f"{v:,} {k}" for k, v in sc.items() if v) if sc else ""

    resume_html = resume_strip()
    library_uri = Path(ROOT, ".agent", "catalog", "library.html").as_uri()
    intel_uri = Path(ROOT, "_active", "farrice-brand", "intelligence", "index.html").as_uri()

    # --- LAUNCH ---
    launch_html = launch_cards(sweep)
    threads_promoted = counts.get("threads_promoted", "?")

    room_uri = Path(ROOT, "deliverables", "research-briefs", "index.html").as_uri()
    board_uri = Path(ROOT, ".agent", "assets", "assets-board.html").as_uri()
    board_brief = "deliverables/research-briefs/mission-board/mission-board-brief.html"
    missions_uri = Path(ROOT, board_brief).as_uri()

    # --- COCKPIT widgets ---
    ring_html, ring_n = artifact_ring()
    routines_html, routines_total = routines_board()
    deck_html = skills_deck()
    apps_html = micro_apps()
    brain_rel = ".agent/brain/brain.html"
    brain_uri = (Path(ROOT) / brain_rel).as_uri()

    tiles_html = f"""<div class="tiles">
  <div class="tile"><a href="{esc(missions_uri)}" data-repo="/repo/{esc(board_brief)}"><div class="n">{len(active)}</div><div class="l">missions live</div></a></div>
  <div class="tile"><a data-scrollto="w-needs" title="jump to the flagged missions"><div class="n">{len(needs_you)}</div><div class="l">need you now</div></a></div>
  <div class="tile"><a data-scrollto="outcomes-sec" title="open the outcomes-due list"><div class="n">{due_count}</div><div class="l">outcomes due</div></a></div>
  <div class="tile"><a href="{esc(room_uri)}" data-route="/room"><div class="n">{brief_total}</div><div class="l">briefs in the room</div></a></div>
  <div class="tile"><a href="{esc(board_uri)}" data-route="/assets"><div class="n">{asset_total}</div><div class="l">assets on the board</div></a></div>
  <div class="tile"><div class="n">{esc(threads_promoted)}</div><div class="l">threads promoted</div></div>
</div>"""

    script = SCRIPT.replace("__REPO_ROOT_URI__", json.dumps(Path(ROOT).as_uri()))

    body = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>homebase · Agentic OS</title>
<style>
{theme_css()}
{CSS}
</style>
<div class="wrap">
<header>
  <div><span class="kicker">FARRICE CAIN · AGENTIC OS</span><h1>home<em>base</em></h1></div>
  {pd._shared_nav("homebase")}
</header>
<div class="stamp"><span>{now}</span>
  <span class="livechip pill muted" id="livechip">static — actions copy commands</span>
  <span class="m">sweep {esc(sweep_age)}</span>
  <button class="actbtn" type="button" data-action="refresh">↻ refresh data</button></div>

{sprint_html}

<div class="cockpit">
  <div class="col" id="col-left">
    <section class="widget" data-wid="clock"><span class="grip" title="drag to reorder">⠿</span>
      <h2>Now</h2><div class="clock"><div class="ct"><span id="clockhm">--:--:--</span> <span class="ap" id="clockap"></span></div>
      <div class="cd" id="clockdate"></div></div></section>
    <section class="widget" data-wid="apps"><span class="grip" title="drag to reorder">⠿</span>
      <h2>Micro apps</h2><div class="wbody">{apps_html}</div></section>
    <section class="widget" data-wid="focus"><span class="grip" title="drag to reorder">⠿</span>
      <h2>Focus</h2><div class="wbody">{tiles_html}</div></section>
  </div>
  <div class="stagewrap">
    <div class="stage">
      {ring_html}
      <a class="portal" href="{esc(brain_uri)}" data-route="/brain" title="open the second brain">
        <canvas id="portalcv"></canvas>
        <span class="pcap">open the second brain</span>
      </a>
      <div id="ringpop"></div>
    </div>
    <div class="ringbar"><input id="ringsearch" type="search"
      placeholder="search {ring_n} artifacts on the ring…" autocomplete="off"></div>
    <div id="ringcap"></div>
  </div>
  <div class="col" id="col-right">
    <section class="widget" data-wid="needs" id="w-needs"><span class="grip" title="drag to reorder">⠿</span>
      <h2>⚑ Needs you — top {len(needs_you)} of {len(flagged)} flagged</h2>
      <div class="wbody">{needs_html}</div></section>
    <section class="widget" data-wid="deck"><span class="grip" title="drag to reorder">⠿</span>
      <h2>Skills deck</h2><div class="wbody">{deck_html}</div></section>
    <section class="widget" data-wid="routines"><span class="grip" title="drag to reorder">⠿</span>
      <h2>Routines — {routines_total} scheduled</h2><div class="wbody">{routines_html}</div></section>
    <section class="widget" data-wid="sys"><span class="grip" title="drag to reorder">⠿</span>
      <h2>What the system holds</h2><span class="sysline">{esc(sys_line) or "health receipt unavailable"}</span>
      <a class="roomlink" href="{esc(library_uri)}" data-route="/library">browse the library ↗</a></section>
  </div>
</div>

<div class="zone">Launch — pick up where work left off</div>
<section><h2>Resumable threads (sweep, {esc(sweep_age)})</h2>{launch_html}</section>

<div class="zone">Library</div>
<section><h2>★ Worth resuming — merit, gone quiet</h2>{resume_html}
  <a class="roomlink" href="{esc(library_uri)}" data-route="/library">open the full library ↗</a></section>
<section><h2>Fresh intel — newest briefs</h2><div class="intelgrid">{briefs_html}</div>
  <a class="roomlink" href="{esc(room_uri)}" data-route="/room">open the briefing room ↗</a>
  <a class="roomlink" href="{esc(missions_uri)}" data-repo="/repo/{esc(board_brief)}">mission board ↗</a></section>
<section><h2>Intelligence Layer — your accumulated operating intelligence</h2>
  <div class="empty">Every learning the system has banked — sovereign memory, the operator
  ledger, solved problems — one searchable page, arena by arena.</div>
  <a class="roomlink" href="{esc(intel_uri)}" data-route="/intelligence">open the intelligence layer ↗</a></section>
<section class="shelf"><h2>Asset shelf — newest generations</h2>
  <div class="shelfgrid">{shelf_html}</div>
  <a class="roomlink" href="{esc(board_uri)}" data-route="/assets">open the asset board ↗</a></section>

<section class="closed" id="outcomes-sec"><h2 class="tog">Outcomes due ({due_count})</h2><div class="body">{outcomes_html}</div></section>
<section class="closed"><h2 class="tog">Recently closed</h2><div class="body">{closed_html}</div></section>

<footer><span>FARRICE CAIN · AGENTIC OS · HOMEBASE</span><span>@farricecain</span></footer>
</div>
<div id="toast">copied</div>
<script>
{script}
</script>"""

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(body)
    print(f"homebase → {OUT}")


if __name__ == "__main__":
    main()
