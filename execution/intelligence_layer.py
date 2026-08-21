#!/usr/bin/env python3
"""intelligence_layer.py — the FARRICE INTELLIGENCE LAYER (2026-08-21).

Builds _active/farrice-brand/intelligence/index.html: ONE self-contained page
holding everything the system has LEARNED — the accumulated operating
intelligence, arena by arena, structured and searchable.

WHY (Kieran Flanagan's "personal intelligence layer", ported to our stores):
the learnings exist — 267 distilled rows in sovereign.db, 91 solution cards,
an operator ledger, a thought bank — and each lives behind a different reader.
Nobody (human or model) opens four readers before working. One page, one
search box, one regen command.

Doctrine (same as every Readout OS surface):
- READS existing stores, never a second collector. sovereign.db is opened
  READ-ONLY (mode=ro URI) — this generator never writes to memory.
- Every source is best-effort: a missing store renders an empty-state note,
  never a traceback. The page must build on a machine where half the stores
  have not been created yet.
- Self-contained, zero network: data embedded, CSS inline, opens over file://
  exactly like brain.html. Served at /intelligence by pulse_serve.py.
- Palette from board_theme.theme_css() — Ink + Steel Blue, one skin.

Confidentiality: this is an INTERNAL artifact. It carries Farrice's private
operating intelligence verbatim. Export/cleaning is deliberately NOT built
(deferred by Farrice's decision) — TACT LAW applies before any external share.
"""
from __future__ import annotations

import argparse
import html as _html
import json
import os
import re
import sqlite3
import sys
import time
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "execution"))

from board_theme import theme_css  # noqa: E402 — one palette for every surface

OUT_DIR = os.path.join(ROOT, "_active", "farrice-brand", "intelligence")
OUT_HTML = os.path.join(OUT_DIR, "index.html")

SOVEREIGN = os.path.join(ROOT, ".memory", "sovereign.db")
LEDGER = os.path.join(ROOT, "knowledge", "lessons", "LEDGER.jsonl")
SOLUTIONS = os.path.join(ROOT, "docs", "solutions")
THEMES = os.path.join(ROOT, "_active", "farrice-brand", "thought-bank", "themes")

# key -> (label, blurb). ORDER IS THE SIDEBAR ORDER. "home" is the cross-cutting
# front page, never a routing target for an individual item.
# KEYS ARE THE LEDGER'S KEYS (knowledge/lessons/LEDGER.jsonl `arena` field) —
# one vocabulary across both stores, so a ledger row routes with zero guessing.
ARENAS = [
    ("home", "Home", "cross-cutting — counts, newest, the rules that bind everywhere"),
    ("offer-linkedin", "Offer & LinkedIn", "positioning, pricing, pipeline, the sprint spine"),
    ("clients", "Clients", "delivery lessons from real engagements"),
    ("harness-craft", "Harness Craft", "how the machine is built, and every way it broke"),
    ("voice-brand", "Voice & Brand", "register, identity, the ban bank, what sounds like him"),
    ("content-science", "Content Science", "hooks, formats, retention, what earns attention"),
    ("health", "Health", "training, recovery, nutrition, the body as infrastructure"),
    ("markets", "Markets", "betting edges, prediction markets, position sizing"),
    ("general", "General", "everything that binds no single arena"),
]
ARENA_KEYS = [k for k, _l, _b in ARENAS]
ROUTABLE = [k for k in ARENA_KEYS if k != "home"]
# Shorthands a writer might bank instead of the canonical key. Cheap insurance:
# an unknown arena silently falling to `general` is how a taxonomy rots.
ALIASES = {"offer": "offer-linkedin", "linkedin": "offer-linkedin",
           "harness": "harness-craft", "system": "harness-craft",
           "voice": "voice-brand", "brand": "voice-brand",
           "content": "content-science", "client": "clients"}

# Keyword heuristic. Distinct-hit count decides; ties break by this order.
# These are evidence of past routing, not a taxonomy — extend freely.
KEYWORDS = {
    "clients": ["andrea", "resonance", "jen santulan", "santulan", "javier",
                "carbon torch", "human values", "hvc", "listing", "realtor",
                "fthb", "client work", "client deliverable", "engagement scope"],
    "markets": ["prizepicks", "prediction market", "sportsbook", "betting",
                "parlay", "nba", "odds", "arbitrage", "kelly", "bankroll",
                "ticker", "portfolio risk"],
    "health": ["hypertrophy", "mesocycle", "workout", "training block",
               "nutrition", "protein", "sleep", "recovery", "injury",
               "rev-rate", "bowling", "calorie", "lifting"],
    "offer-linkedin": ["offer", "pricing", "price point", "sales call", "pitch",
                       "linkedin", "prospect", "lead gen", "funnel", "positioning",
                       "revenue", "sprint", "proof-to-market", "icp", "buyer",
                       "cold outreach", "close rate", "retainer", "objection"],
    "voice-brand": ["voice", "brand", "register", "tone", "identity", "avatar",
                    "persona", "ai slop", "slop ban", "banned phrase", "prose",
                    "ghostwrit", "cadence", "his own words", "sounds like"],
    "content-science": ["hook", "carousel", "post format", "thumbnail", "retention",
                        "algorithm", "engagement", "newsletter", "substack",
                        "parallax", "audience", "short-form", "content system",
                        "virality", "dwell", "scroll"],
    "harness-craft": ["hook script", "python", "execution/", "workflow", "subagent",
                      "harness", "sovereign.db", "memory", "notion", "git ", "commit",
                      "worktree", "lane", "verifier", "pipeline", "launchd",
                      "extraction", "skill", "prompt", "agent", "routing", "schema",
                      "regression", "fallback", "cli", "json", "hook fires",
                      "orchestrat", "context window", "token"],
}
# metadata.domain (sovereign) -> arena. Used only when keywords find nothing.
DOMAIN_MAP = {
    "storytelling": "voice-brand", "communications": "voice-brand",
    "writing": "voice-brand", "offer-strategy": "offer-linkedin",
    "system": "harness-craft", "family": "general",
    "projects": "general", "founder-context": "general",
}
# Categories that render most prominently. Rules first — they bind.
CATEGORY_RANK = {"rule": 0, "lesson": 1, "pattern": 2, "insight": 3,
                 "preference": 4, "template": 5, "config": 6}

PROVISIONAL_RE = re.compile(r"^\s*\[PROVISIONAL[^\]]*\]\s*", re.I)

# Canon pointers — links only. This page never copies canon content; canon is
# read at its source or it drifts (LIVING vs RECORD, 2026-08-07).
CANON = [
    ("FARRICE-MASTER-CONTEXT.md", "FARRICE-MASTER-CONTEXT.md",
     "identity canon — load before any identity / voice / offer work"),
    ("_active/linkedin/CAMPAIGN.md", "_active/linkedin/CAMPAIGN.md",
     "the live LinkedIn campaign spine"),
    ("docs/solutions/index.md", "docs/solutions/index.md",
     "every solved problem, one line each"),
]


def esc(s) -> str:
    return _html.escape(str(s if s is not None else ""))


def _norm_date(v) -> str:
    """Best-effort YYYY-MM-DD out of anything date-shaped."""
    s = str(v or "")
    m = re.search(r"(\d{4}-\d{2}-\d{2})", s)
    return m.group(1) if m else ""


def resolve_arena(declared, text: str, domain: str | None = None) -> str:
    """A declared arena wins (canonical key or known shorthand); otherwise the
    keyword heuristic runs. One entry point so both stores route identically."""
    key = str(declared or "").strip().lower()
    key = ALIASES.get(key, key)
    if key in ROUTABLE:
        return key
    return classify(text, domain)


def classify(text: str, domain: str | None = None) -> str:
    """Route one item to an arena. Distinct keyword hits win; DOMAIN_MAP is the
    fallback; general is the floor. Never raises — an unroutable item is a
    general item, not a crash."""
    low = (text or "").lower()
    best, best_n = None, 0
    for key in ("clients", "markets", "health", "offer-linkedin", "voice-brand",
                "content-science", "harness-craft"):
        n = sum(1 for kw in KEYWORDS[key] if kw in low)
        if n > best_n:
            best, best_n = key, n
    if best:
        return best
    if domain and domain in DOMAIN_MAP:
        return DOMAIN_MAP[domain]
    return "general"


# ── sources (all best-effort) ────────────────────────────────────────────────

def read_sovereign() -> tuple[list[dict], str | None]:
    """Distilled semantic + procedural rows. READ-ONLY — this generator is a
    reader of memory, never a writer of it."""
    if not os.path.exists(SOVEREIGN):
        return [], "sovereign.db not found at .memory/sovereign.db"
    items = []
    try:
        uri = f"file:{Path(SOVEREIGN).as_posix()}?mode=ro"
        con = sqlite3.connect(uri, uri=True, timeout=5)
        rows = con.execute(
            "SELECT id, tier, category, content, created_at, metadata, pinned "
            "FROM memories WHERE tier IN ('semantic','procedural') "
            "ORDER BY created_at DESC"
        ).fetchall()
        con.close()
    except Exception as e:  # noqa: BLE001 — a store that won't open is an empty state
        return [], f"sovereign.db unreadable ({type(e).__name__}: {e})"
    for mid, tier, cat, content, created, meta, pinned in rows:
        try:
            md = json.loads(meta or "{}")
            md = md if isinstance(md, dict) else {}
        except ValueError:
            md = {}
        body = content or ""
        provisional = bool(PROVISIONAL_RE.match(body))
        body = PROVISIONAL_RE.sub("", body).strip()
        arena = resolve_arena(
            md.get("arena"),
            f"{body} {md.get('name', '')} {md.get('expert', '')}", md.get("domain"))
        items.append({
            "arena": arena,
            "category": (cat or "insight").lower(),
            "date": _norm_date(created),
            "content": body,
            "store": f"sovereign · {tier}",
            "meta": " · ".join(
                str(md[k]) for k in ("domain", "source", "expert", "name") if md.get(k)),
            "provisional": provisional,
            "pinned": bool(pinned),
            "id": mid,
        })
    return items, None


def read_ledger() -> tuple[list[dict], str | None]:
    """knowledge/lessons/LEDGER.jsonl — the operator ledger. Its `arena` field
    routes directly when present; absent file is a normal state, not an error."""
    if not os.path.exists(LEDGER):
        return [], ("operator ledger not present yet — "
                    "knowledge/lessons/LEDGER.jsonl will appear as lessons are banked")
    items, bad = [], 0
    try:
        lines = open(LEDGER, encoding="utf-8").read().splitlines()
    except OSError as e:
        return [], f"LEDGER.jsonl unreadable ({e})"
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except ValueError:
            bad += 1
            continue
        if not isinstance(row, dict):
            bad += 1
            continue
        body = str(row.get("lesson") or row.get("content") or row.get("text")
                   or row.get("summary") or "").strip()
        title = str(row.get("title") or row.get("name") or "").strip()
        if title and title not in body:
            body = f"{title}\n{body}" if body else title
        if not body:
            continue
        arena = resolve_arena(row.get("arena"), body, row.get("domain"))
        items.append({
            "arena": arena,
            "category": str(row.get("category") or row.get("type")
                            or row.get("kind") or "lesson").lower(),
            "date": _norm_date(row.get("ts") or row.get("date")
                               or row.get("created_at") or row.get("session_date")),
            "content": body,
            "store": "operator ledger",
            "meta": " · ".join(str(row[k]) for k in ("source", "session", "project")
                               if row.get(k)),
            "provisional": False,
            "pinned": False,
            "id": str(row.get("id") or ""),
        })
    note = f"{bad} malformed ledger line(s) skipped" if bad else None
    return items, note


def _frontmatter(path: str) -> dict:
    """Cheap YAML-ish frontmatter reader — key: value, no deps, no eval."""
    out = {}
    try:
        text = open(path, encoding="utf-8").read()
    except OSError:
        return out
    if not text.startswith("---"):
        return out
    _, _, rest = text.partition("---")
    block, _, _ = rest.partition("\n---")
    for line in block.splitlines():
        if ":" not in line or line.strip().startswith("#"):
            continue
        k, _, v = line.partition(":")
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def read_solutions() -> tuple[list[dict], str | None]:
    """docs/solutions/*.md frontmatter — the Solved Problems list. Cards are
    the never-re-solve-it layer (Chain step 6.5)."""
    if not os.path.isdir(SOLUTIONS):
        return [], "docs/solutions/ not present"
    rows = []
    for name in sorted(os.listdir(SOLUTIONS)):
        if not name.endswith(".md") or name == "index.md":
            continue
        p = os.path.join(SOLUTIONS, name)
        fm = _frontmatter(p)
        title = fm.get("name") or name[:-3].replace("-", " ")
        rows.append({
            "title": title,
            "signature": fm.get("problem_signature", ""),
            "date": _norm_date(fm.get("date") or name),
            "domain": fm.get("domain", ""),
            "status": fm.get("status", ""),
            "path": f"docs/solutions/{name}",
        })
    rows.sort(key=lambda r: r["date"], reverse=True)
    return rows, (None if rows else "no solution cards on disk yet")


def read_themes() -> tuple[list[dict], str | None]:
    """thought-bank themes — name + first real paragraph, for the Home strip."""
    if not os.path.isdir(THEMES):
        return [], "thought-bank themes/ not present"
    out = []
    for name in sorted(os.listdir(THEMES)):
        if not name.endswith(".md"):
            continue
        try:
            lines = open(os.path.join(THEMES, name), encoding="utf-8").read().splitlines()
        except OSError:
            continue
        title, blurb = name[:-3].replace("-", " "), ""
        for line in lines:
            s = line.strip()
            if not s:
                continue
            if s.startswith("# "):
                title = s[2:].replace("Theme — ", "").strip()
                continue
            if s.startswith("#"):
                continue
            blurb = re.sub(r"[*_`>]+", "", s.lstrip("> ")).strip()
            break
        out.append({"title": title, "blurb": blurb,
                    "path": f"_active/farrice-brand/thought-bank/themes/{name}"})
    return out, (None if out else "no themes captured yet")


# ── render ───────────────────────────────────────────────────────────────────

CSS = """
* { box-sizing:border-box; }
body { margin:0; background:var(--ground); color:var(--ink);
  font:15px/1.6 var(--sans); -webkit-font-smoothing:antialiased; }
a { color:var(--accent); text-decoration:none; }
a:hover { text-decoration:underline; }
.kicker, .mono { font-family:var(--mono); font-size:9px; letter-spacing:.22em;
  text-transform:uppercase; color:var(--muted); }
header { border-bottom:1px solid var(--line); padding:26px 32px 18px;
  background:var(--panel); position:sticky; top:0; z-index:20; }
header h1 { font-size:26px; font-weight:700; margin:6px 0 0; letter-spacing:-.02em; }
header h1 em { font-style:normal; color:var(--accent); }
.htop { display:flex; align-items:flex-end; justify-content:space-between;
  gap:20px; flex-wrap:wrap; }
.searchwrap { flex:1; min-width:240px; max-width:520px; }
#q { width:100%; background:var(--ground); color:var(--ink); font:13px/1.4 var(--mono);
  border:1px solid var(--line); border-radius:6px; padding:9px 12px; }
#q:focus { outline:none; border-color:var(--accent); }
.banner { margin:14px 0 0; border-left:2px solid var(--accent); padding:8px 14px;
  background:var(--ground); font-size:13px; color:var(--soft); border-radius:0 5px 5px 0; }
.banner code { font-family:var(--mono); font-size:11.5px; color:var(--ink); }
.tact { margin-top:8px; border-left-color:var(--warn); color:var(--warn);
  font-family:var(--mono); font-size:10px; letter-spacing:.14em; text-transform:uppercase; }
.layout { display:flex; align-items:flex-start; gap:0; }
nav.side { width:236px; flex:none; border-right:1px solid var(--line); padding:22px 0 60px;
  position:sticky; top:150px; align-self:flex-start; }
nav.side button { display:flex; width:100%; align-items:baseline; justify-content:space-between;
  gap:8px; background:none; border:0; border-left:2px solid transparent; cursor:pointer;
  text-align:left; padding:8px 18px; color:var(--soft); font:13px/1.35 var(--sans); }
nav.side button:hover { color:var(--ink); }
nav.side button.on { color:var(--ink); border-left-color:var(--accent); font-weight:600; }
nav.side button .c { font-family:var(--mono); font-size:9.5px; color:var(--muted); }
main { flex:1; min-width:0; padding:26px 32px 90px; }
h2.sec { font-size:19px; font-weight:700; margin:0 0 4px; letter-spacing:-.01em; }
.blurb { color:var(--muted); font-size:13px; margin:0 0 20px; }
h3 { font-family:var(--mono); font-size:9.5px; letter-spacing:.2em; text-transform:uppercase;
  color:var(--muted); margin:30px 0 12px; padding-bottom:6px; border-bottom:1px solid var(--line); }
.pane { display:none; } .pane.on { display:block; }
.item { border:1px solid var(--line); border-radius:7px; background:var(--panel);
  padding:12px 15px; margin:0 0 9px; }
.item.rule { border-left:3px solid var(--accent); }
.item.lesson { border-left:3px solid var(--ok); }
.ihead { display:flex; align-items:center; gap:8px; flex-wrap:wrap; margin-bottom:7px; }
.badge { font-family:var(--mono); font-size:8.5px; letter-spacing:.16em; text-transform:uppercase;
  border:1px solid var(--line); border-radius:99px; padding:2px 8px; color:var(--soft); }
.badge.rule { border-color:var(--accent); color:var(--accent); }
.badge.lesson { border-color:var(--ok); color:var(--ok); }
.badge.prov { border-color:var(--warn); color:var(--warn); }
.ihead .src, .ihead time { font-family:var(--mono); font-size:9px; letter-spacing:.12em;
  text-transform:uppercase; color:var(--muted); }
.ihead time { margin-left:auto; }
.ibody { white-space:pre-wrap; word-break:break-word; font-size:14px; color:var(--ink);
  max-height:12.5em; overflow:hidden; position:relative; }
.item.long .ibody:after { content:""; position:absolute; left:0; right:0; bottom:0; height:3em;
  background:linear-gradient(transparent, var(--panel)); }
.item.open .ibody { max-height:none; }
.item.open .ibody:after { display:none; }
.item.long { cursor:pointer; }
.more { font-family:var(--mono); font-size:8.5px; letter-spacing:.16em; text-transform:uppercase;
  color:var(--accent); margin-top:6px; display:none; }
.item.long .more { display:block; }
.item.open .more { color:var(--muted); }
.grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(160px,1fr)); gap:9px; }
.tile { border:1px solid var(--line); border-radius:7px; background:var(--panel); padding:13px 15px; }
.tile .n { font-family:var(--mono); font-size:24px; color:var(--accent); line-height:1; }
.tile .l { font-family:var(--mono); font-size:9px; letter-spacing:.16em; text-transform:uppercase;
  color:var(--muted); margin-top:6px; }
.solwrap { overflow-x:auto; }   /* wide table scrolls itself; the page never does */
table.sol { width:100%; min-width:560px; border-collapse:collapse; font-size:13px; }
table.sol td { border-bottom:1px solid var(--line); padding:8px 10px 8px 0; vertical-align:top; }
table.sol td.d { font-family:var(--mono); font-size:9.5px; color:var(--muted); white-space:nowrap; }
table.sol td.t { font-weight:600; width:30%; }
table.sol td.s { color:var(--soft); }
table.sol td.p { font-family:var(--mono); font-size:9.5px; color:var(--muted); white-space:nowrap; }
.themes { display:grid; grid-template-columns:repeat(auto-fill,minmax(255px,1fr)); gap:9px; }
.theme { border:1px solid var(--line); border-radius:7px; background:var(--panel); padding:12px 15px; }
.theme strong { display:block; font-size:13.5px; margin-bottom:4px; }
.theme p { margin:0; font-size:12.5px; color:var(--soft); }
.canon { border-top:1px solid var(--line); margin-top:34px; padding-top:16px; }
.canon div { margin-bottom:7px; font-size:13px; }
.canon .why { color:var(--muted); }
.empty { border:1px dashed var(--line); border-radius:7px; padding:14px 16px; color:var(--muted);
  font-size:13px; background:none; }
.hidden { display:none !important; }
footer { border-top:1px solid var(--line); padding:16px 32px; display:flex;
  justify-content:space-between; font-family:var(--mono); font-size:9px;
  letter-spacing:.18em; text-transform:uppercase; color:var(--muted); }
#count { font-family:var(--mono); font-size:9.5px; letter-spacing:.14em;
  text-transform:uppercase; color:var(--muted); margin:0 0 14px; }
@media (max-width:820px) {
  .layout { display:block; }
  nav.side { width:auto; position:static; border-right:0; border-bottom:1px solid var(--line);
    display:flex; flex-wrap:wrap; padding:10px 12px; }
  nav.side button { width:auto; border-left:0; border-bottom:2px solid transparent; padding:6px 10px; }
  nav.side button.on { border-left:0; border-bottom-color:var(--accent); }
  main, header, footer { padding-left:16px; padding-right:16px; }
}
"""

JS = r"""
const q = document.getElementById('q');
const panes = Array.from(document.querySelectorAll('.pane'));
const tabs = Array.from(document.querySelectorAll('nav.side button'));
const countEl = document.getElementById('count');
let current = 'home';

function show(key) {
  current = key;
  panes.forEach(p => p.classList.toggle('on', p.dataset.arena === key));
  tabs.forEach(t => t.classList.toggle('on', t.dataset.arena === key));
  if (!q.value.trim()) countEl.textContent = '';
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
tabs.forEach(t => t.addEventListener('click', () => { q.value = ''; filter(); show(t.dataset.arena); }));

// Search index: built ONCE from rendered text, so the page never ships a second
// lowercase copy of every learning (file size doctrine — see item_html).
const HITS = Array.from(document.querySelectorAll('[data-hit]'));
const IDX = HITS.map(el => el.textContent.toLowerCase());

function filter() {
  const term = q.value.trim().toLowerCase();
  if (!term) {
    HITS.forEach(r => r.classList.remove('hidden'));
    panes.forEach(p => p.classList.toggle('on', p.dataset.arena === current));
    countEl.textContent = '';
    return;
  }
  let hits = 0;
  for (let i = 0; i < HITS.length; i++) {
    const ok = IDX[i].indexOf(term) !== -1;
    HITS[i].classList.toggle('hidden', !ok);
    if (ok) hits++;
  }
  panes.forEach(p => p.classList.add('on'));   // search spans every arena
  countEl.textContent = hits + ' match' + (hits === 1 ? '' : 'es') + ' across all arenas — clear the box to browse';
}
q.addEventListener('input', filter);
q.addEventListener('keydown', e => { if (e.key === 'Escape') { q.value = ''; filter(); show(current); } });

document.addEventListener('click', e => {
  const it = e.target.closest('.item.long');
  if (it) it.classList.toggle('open');
});

// nav live rewrite (same pattern as every board)
if (location.protocol.startsWith('http'))
  document.querySelectorAll('a[data-route]').forEach(a => { a.href = a.dataset.route; });
"""


def _is_long(text: str) -> bool:
    """Does this body overflow the 12.5em clamp? Decided HERE, in Python, not
    by measuring in JS: eight of nine panes are display:none at load, where
    every element measures 0x0 — a JS measurement silently marks only the Home
    pane expandable and every other arena's long items look truncated with no
    affordance (caught in browser check, 2026-08-21)."""
    lines = sum(max(1, -(-len(ln) // 95)) for ln in (text or "").split("\n"))
    return lines > 12


def item_html(it: dict) -> str:
    cat = it["category"]
    cls = "item" + (f" {cat}" if cat in ("rule", "lesson") else "")
    if _is_long(it["content"]):
        cls += " long"
    badges = f'<span class="badge {esc(cat)}">{esc(cat)}</span>'
    if it.get("provisional"):
        badges += '<span class="badge prov">provisional</span>'
    if it.get("pinned"):
        badges += '<span class="badge">pinned</span>'
    meta = f'<span class="src">{esc(it["store"])}'
    if it.get("meta"):
        meta += f' · {esc(it["meta"])}'
    meta += "</span>"
    date = f'<time>{esc(it["date"])}</time>' if it.get("date") else ""
    # No data-text mirror of the body: at ~1,600 items a duplicated lowercase
    # copy nearly doubles the file. The search index is built once from
    # textContent at load (see JS) — same behaviour, half the bytes.
    return (f'<article class="{cls}" data-hit>'
            f'<div class="ihead">{badges}{meta}{date}</div>'
            f'<div class="ibody">{esc(it["content"])}</div>'
            f'<div class="more">click to expand ↕</div></article>')


def items_html(items: list[dict], empty: str) -> str:
    if not items:
        return f'<div class="empty">{esc(empty)}</div>'
    return "".join(item_html(i) for i in items)


def sort_items(items: list[dict]) -> list[dict]:
    """Rules first (they bind), newest first inside each band. Two passes
    because the directions differ — date descending, rank ascending — and
    Python's sort is stable, so the second pass preserves the first."""
    out = sorted(items, key=lambda i: i.get("date", ""), reverse=True)
    out.sort(key=lambda i: CATEGORY_RANK.get(i["category"], 9))
    return out


def solutions_html(rows: list[dict], note: str | None) -> str:
    if not rows:
        return f'<div class="empty">{esc(note or "no solution cards yet")}</div>'
    body = []
    for r in rows:
        body.append(
            f'<tr data-hit><td class="d">{esc(r["date"])}</td>'
            f'<td class="t">{esc(r["title"])}</td>'
            f'<td class="s">{esc(r["signature"])}</td>'
            f'<td class="p">{esc(r["path"])}</td></tr>')
    return f'<div class="solwrap"><table class="sol"><tbody>{"".join(body)}</tbody></table></div>'


def build() -> dict:
    sov, sov_note = read_sovereign()
    led, led_note = read_ledger()
    sols, sol_note = read_solutions()
    themes, theme_note = read_themes()

    items = sov + led
    by_arena = {k: [] for k in ROUTABLE}
    for it in items:
        by_arena.setdefault(it["arena"], []).append(it)
    for k in by_arena:
        by_arena[k] = sort_items(by_arena[k])

    newest = sorted(items, key=lambda i: i.get("date", ""), reverse=True)[:10]
    cross = [i for i in items if i["arena"] == "general" and i["category"] == "rule"]
    cross += [i for i in items if i["arena"] != "general" and i["category"] == "rule"][:8]
    cross = cross[:14]

    now = time.strftime("%Y-%m-%d %H:%M")
    try:
        import surface_nav as sn
        nav = sn.nav_html(current="intelligence", style=False)
    except Exception:  # noqa: BLE001 — nav is a nicety, never a build blocker
        nav = ""

    # sidebar
    tabs = []
    for key, label, _b in ARENAS:
        n = len(by_arena.get(key, [])) if key != "home" else len(items)
        on = ' class="on"' if key == "home" else ""
        tabs.append(f'<button data-arena="{key}"{on}>'
                    f'<span>{esc(label)}</span><span class="c">{n}</span></button>')

    # home pane
    tiles = "".join(
        f'<div class="tile"><div class="n">{len(by_arena.get(k, []))}</div>'
        f'<div class="l">{esc(lbl)}</div></div>'
        for k, lbl, _b in ARENAS if k != "home")
    tiles = (f'<div class="grid"><div class="tile"><div class="n">{len(items)}</div>'
             f'<div class="l">learnings held</div></div>'
             f'<div class="tile"><div class="n">{len(sols)}</div>'
             f'<div class="l">solved problems</div></div>{tiles}</div>')

    themes_html = "".join(
        f'<div class="theme" data-hit>'
        f'<strong>{esc(t["title"])}</strong><p>{esc(t["blurb"])}</p></div>'
        for t in themes) or f'<div class="empty">{esc(theme_note or "")}</div>'

    canon = "".join(
        f'<div><a href="{esc(rel)}" data-route="/repo/{esc(rel)}">{esc(label)}</a> '
        f'<span class="why">— {esc(why)}</span></div>'
        for label, rel, why in CANON)

    notes = [n for n in (sov_note, led_note) if n]
    notes_html = ("".join(f'<div class="empty">{esc(n)}</div>' for n in notes)
                  if notes else "")

    home = f"""<section class="pane on" data-arena="home">
  <h2 class="sec">Home</h2>
  <p class="blurb">{esc(dict((k, b) for k, _l, b in ARENAS)["home"])}</p>
  {tiles}
  {notes_html}
  <h3>Cross-cutting rules — these bind everywhere</h3>
  {items_html(cross, "no rules distilled yet — they arrive as sessions bank lessons")}
  <h3>Newest {len(newest)} learnings across every arena</h3>
  {items_html(newest, "nothing banked yet")}
  <h3>Themes — the thought bank</h3>
  <div class="themes">{themes_html}</div>
  <div class="canon"><h3>Canon — read at the source, never copied here</h3>{canon}</div>
</section>"""

    panes = [home]
    for key, label, blurb in ARENAS:
        if key == "home":
            continue
        extra = ""
        if key == "harness-craft":
            extra = (f'<h3>Solved problems — {len(sols)} cards, never re-solve one</h3>'
                     f'{solutions_html(sols, sol_note)}')
        panes.append(
            f'<section class="pane" data-arena="{key}">'
            f'<h2 class="sec">{esc(label)}</h2><p class="blurb">{esc(blurb)}</p>'
            f'{items_html(by_arena.get(key, []), "nothing banked in this arena yet — it fills as sessions land")}'
            f'{extra}</section>')

    html_doc = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Farrice Intelligence Layer</title>
<style>
{theme_css()}
{CSS}
</style>
<header>
  <div class="htop">
    <div><span class="kicker">FARRICE CAIN · AGENTIC OS</span>
      <h1>Farrice <em>Intelligence Layer</em></h1></div>
    <div class="searchwrap"><input id="q" type="search"
      placeholder="search {len(items)} learnings + {len(sols)} solved problems…" autocomplete="off"></div>
    {nav}
  </div>
  <div class="banner"><strong>Living document.</strong> Regenerated by
    <code>python3 execution/intelligence_layer.py regen</code> from
    <code>.memory/sovereign.db</code>, the operator ledger
    (<code>knowledge/lessons/LEDGER.jsonl</code>) and the solution cards in
    <code>docs/solutions/</code> — any AI assistant reading this page should treat it as
    Farrice's accumulated operating intelligence: what he has already learned, decided,
    and paid for. Build on it; do not re-derive it.</div>
  <div class="banner tact">Internal artifact — TACT LAW applies before any external share</div>
</header>
<div class="layout">
  <nav class="side">{"".join(tabs)}</nav>
  <main><div id="count"></div>{"".join(panes)}</main>
</div>
<footer><span>FARRICE CAIN · AGENTIC OS · INTELLIGENCE LAYER</span>
  <span>regenerated {esc(now)}</span></footer>
<script>
{JS}
</script>"""

    os.makedirs(OUT_DIR, exist_ok=True)
    open(OUT_HTML, "w", encoding="utf-8").write(html_doc)
    return {"items": len(items), "sovereign": len(sov), "ledger": len(led),
            "solutions": len(sols), "themes": len(themes),
            "by_arena": {k: len(v) for k, v in by_arena.items()},
            "notes": notes, "bytes": len(html_doc.encode("utf-8"))}


def main() -> int:
    ap = argparse.ArgumentParser(description="Build the Farrice Intelligence Layer.")
    ap.add_argument("cmd", nargs="?", default="regen", choices=["regen"],
                    help="regen (default) — rebuild index.html from every store")
    ap.parse_args()
    t0 = time.time()
    r = build()
    print(f"intelligence → {OUT_HTML}  ({r['items']} learnings "
          f"[{r['sovereign']} sovereign + {r['ledger']} ledger], "
          f"{r['solutions']} solution cards, {r['themes']} themes, "
          f"{r['bytes'] / 1024:.0f} KB, {time.time() - t0:.2f}s)")
    print("  arenas: " + " · ".join(f"{k} {v}" for k, v in r["by_arena"].items()))
    for n in r["notes"]:
        print(f"  note: {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
