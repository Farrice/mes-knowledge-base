#!/usr/bin/env python3
"""
build_lead_magnet.py — bake the interactive lead-magnet mini-report ($0, offline).

The step-down of the premium Content Growth Blueprint: reads a signal-pack JSON
(the outlier_radar.py contract, spec: .scratch/kallaway-sandcastles-forge/spec-outlier-radar.md),
prunes it to a mini payload (top-5 ranked videos with receipts, top-5 topic
leaderboard, ONE derived whitespace insight, coverage honesty line), renders the
data blocks plus a 5-beat teaching panel, and injects everything into
templates/lead-magnet/mini-report.html placeholders. Output is a single
self-contained HTML file — zero network calls, works from file://.

Graceful degradation: a missing, unreadable, contract-invalid, degraded, or
empty pack bakes the interview-only variant (inputs + teaching panel + CTA,
no fabricated numbers, an honest "data refresh pending" line). Never raises
on bad pack data; the receipt line says which mode shipped and why.

Enrichment taste: when the pack carries an `enrichment` block (pack_enrich.py),
the full bake adds AT MOST 2 sourced nuggets — one rising-topic demand note +
one market-pulse line — as a taste of the full report's enrichment layer
(extension, not duplication). No enrichment -> byte-identical to the plain bake.

Plain-language floor (cold-read fix, 2026-08-28): no raw taxonomy token
(hook_format keys, desire_template names, topic trigrams) ever reaches prose.
A mapping layer translates known keys to founder language; unknown keys fall
back to plain phrasing, never the token. The old topic re-list section is
replaced by a one-line why-it-broke-pattern read per top video; topic rows
render only for themes with >= 2 videos.

Usage:
    .venv/bin/python3 execution/build_lead_magnet.py \
        --pack .agent/outlier-radar/packs/<niche>/latest.json \
        --niche-label "Fitness coaches on YouTube" \
        --cta-url "https://example.com/blueprint" \
        --exclude vidid1,vidid2 \
        --out deliverables/lead-magnets/<niche>/mini-report.html

--exclude skips those video ids (off-avatar receipts, per the niche's top-50
strike list); next-ranked pack rows backfill the top-5 automatically.
"""
import argparse
import html
import json
import re
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, urlencode

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TEMPLATE = ROOT / "templates" / "lead-magnet" / "mini-report.html"

MAX_VIDEOS = 5
MAX_TOPICS = 5

# Fields a pack must carry to be trusted for the full bake (subset of the contract).
REQUIRED_PACK_KEYS = ("pack_version", "niche_slug", "generated_at", "status", "ranked_videos")


def esc(value):
    """HTML-escape any pack-derived string; None becomes empty string."""
    return html.escape(str(value)) if value is not None else ""


def safe_url(url):
    """Only pass through http(s) URLs; anything else becomes a dead anchor."""
    if isinstance(url, str) and url.startswith(("http://", "https://")):
        return url
    return "#"


def fmt_views(n):
    if not isinstance(n, (int, float)) or n < 0:
        return None
    n = float(n)
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M views"
    if n >= 1_000:
        return f"{n / 1_000:.0f}K views"
    return f"{int(n):,} views"


def fmt_mult(m):
    if not isinstance(m, (int, float)) or m <= 0:
        return "—"
    return f"{m:.1f}×"


# ------------------------------------------------- plain-language mapping layer
# Internal taxonomy keys never reach prose. Known keys map to founder language;
# unknown keys get the plain fallback — never the raw token.

PLAIN_HOOK_FORMAT = {
    "concrete-declarative": "videos that open by stating one concrete claim as fact",
    "specific-number": "videos that open on one specific, checkable number",
    "condition-free": "videos that promise the result with the usual requirement removed",
    "tutorial-system": "videos that walk one complete system start to finish",
    "question": "videos that open on a question the viewer is already asking",
}
PLAIN_HOOK_FALLBACK = "a hook style this niche has barely touched"

PLAIN_DESIRE = {
    "unfair-advantage filter": "an edge the viewer's competitors can't easily copy",
    "condition-free method": "the result without the usual requirement attached",
    "relatable character": "a person the viewer recognizes as themselves",
    "specificity-first declarative": "one precise claim the viewer could go check",
    "dream outcome": "the end state the viewer actually wants",
}
PLAIN_DESIRE_FALLBACK = "something the rest of the field isn't selling"

FOUNDER_MAKE = {
    "concrete-declarative": ("open your next video with the one thing you know is true about your corner "
                             "of the market, stated flat with no hedge, then spend the video proving it"),
    "specific-number": ("lead with the most specific number your operation can defend; "
                        "a real figure from your own books beats a round one"),
    "condition-free": ("name the requirement your buyers assume is mandatory, then show the route that skips it"),
    "tutorial-system": ("film the system you already run, start to finish, exactly the way you run it"),
    "question": ("open on the question your buyers actually type into search, and answer it inside the first minute"),
}
FOUNDER_MAKE_FALLBACK = "make the version only your operation could make; the shape is open, and the proof is yours"


def _norm_key(key):
    return str(key or "").strip().lower()


def plain_hook(key):
    return PLAIN_HOOK_FORMAT.get(_norm_key(key), PLAIN_HOOK_FALLBACK)


def plain_desire(key):
    return PLAIN_DESIRE.get(_norm_key(key), PLAIN_DESIRE_FALLBACK)


def founder_make(key):
    return FOUNDER_MAKE.get(_norm_key(key), FOUNDER_MAKE_FALLBACK)


# --------------------------------------------------- why-it-broke-pattern reads

NEWS_RE = re.compile(r"\b(just|officially|quietly|last week|this week|announced|banned"
                     r"|is killing|lost control|changed)\b", re.I)
FIRSTHAND_RE = re.compile(r"\b(we use|i use|i built|i sold|i spent|i tried|i went|i tracked"
                          r"|i ate|my own|our own|you exited|exited for)\b", re.I)
MONEY_RE = re.compile(r"\$|\b(billion|million|figure)\b", re.I)
NUM_RE = re.compile(r"\$\s?\d[\d,.]*\s*(?:billion|million|k)?"
                    r"|\b\d[\d,.]*\s?%"
                    r"|\b\d[\d,.]*\s+(?:billion|million|sellers|platforms|minutes|hours|days"
                    r"|weeks|years|steps|clients|videos|products)\b"
                    r"|\b\d{2,}[\d,]*\b", re.I)


def derive_why(v):
    """One plain-language line on WHY a video broke pattern, from format_hint +
    hook_text/title. Deterministic, mechanically derived, no taxonomy tokens."""
    hint = _norm_key(v.get("format_hint"))
    hook = " ".join(str(v.get("hook_text") or "").split())
    title = str(v.get("title") or "")
    text = f"{title} {hook}".strip()
    if not text:
        return None
    news = bool(NEWS_RE.search(text))
    firsthand = bool(FIRSTHAND_RE.search(text))
    m = NUM_RE.search(text)
    num = m.group(0).strip() if m else None

    if hint == "specific-number":
        if num and news:
            return (f"Opens on a hard number ({num}) inside a piece of market news that just broke. "
                    "Specific and urgent at once, and the viewer is the one affected.")
        if num:
            return (f"Opens on a hard number ({num}) and lets that one figure carry the promise. "
                    "A claim specific enough to check reads as true.")
        return "Stakes one specific, checkable outcome up front and lets the specificity do the convincing."
    if hint == "concrete-declarative":
        if news:
            return ("States a flat claim about something that just changed in the market. No hedge, "
                    "no question, so the stakes feel current and the viewer stays to see it proven.")
        if firsthand and MONEY_RE.search(text):
            return ("Opens inside a founder's own story with the outcome in dollars on the table. "
                    "Proof first, mechanics second.")
        if firsthand:
            return ("States its claim from inside the operation, with the author's own working material "
                    "on screen. That is the one kind of proof an operator audience can't argue with.")
        return ("States one concrete claim as settled fact in the first line, "
                "then makes the viewer stay to watch it get proven.")
    if hint == "condition-free":
        return ("Promises the result with the usual requirement stripped out, "
                "so the viewer's biggest objection is answered before it forms.")
    if hint == "tutorial-system":
        return "Walks one complete, repeatable system start to finish instead of teasing it. Completeness is the hook."
    if hint == "question":
        return "Opens on a question the viewer is already arguing about, and holds the answer just long enough."
    # Unknown or missing format hint — read the hook itself; never surface the raw key.
    if news:
        return "Rides a fresh piece of market news and lands it on what the viewer should do about it."
    if firsthand:
        return "Tells it firsthand, with the author's own numbers on the table, and lets the receipts do the persuading."
    if num:
        return f"Leads with a hard number ({num}) and lets specificity stand in for hype."
    return "Beat its channel's normal on subject pull alone. No hook trick; the topic itself did the work."


def _videos_by_id(pack):
    out = {}
    for v in pack.get("ranked_videos") or []:
        if isinstance(v, dict) and v.get("video_id"):
            out[v["video_id"]] = v
    return out


def _topic_example_title(pack, topic_row, exclude=frozenset()):
    """Plain display name for a topic cluster: the title of one of its videos
    (preferring non-excluded ids). Never the raw topic key."""
    by_id = _videos_by_id(pack)
    ids = [i for i in (topic_row.get("example_video_ids") or []) if isinstance(i, str)]
    for vid in [i for i in ids if i not in exclude] + ids:
        v = by_id.get(vid)
        if v and v.get("title"):
            return str(v["title"])
    return None


def _leaderboard_topic_title(pack, topic_key):
    """Resolve a leaderboard topic key to a real video title from that cluster."""
    for t in ((pack.get("leaderboard") or {}).get("topics")) or []:
        if isinstance(t, dict) and t.get("topic") == topic_key:
            return _topic_example_title(pack, t)
    return None


# ---------------------------------------------------------------- pack loading

def load_pack(path):
    """Return (pack_dict, reason). pack_dict is None when the interview-only
    variant must ship; reason is a short receipt-friendly string."""
    if not path:
        return None, "no pack path given"
    p = Path(path)
    if not p.exists():
        return None, f"pack missing: {p}"
    try:
        pack = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return None, f"pack unreadable: {e.__class__.__name__}"
    if not isinstance(pack, dict):
        return None, "pack is not a JSON object"
    missing = [k for k in REQUIRED_PACK_KEYS if k not in pack]
    if missing:
        return None, f"pack missing contract fields: {', '.join(missing)}"
    if pack.get("status") != "ok":
        return None, f"pack status={pack.get('status')!r} — numbers not trusted"
    videos = pack.get("ranked_videos")
    if not isinstance(videos, list) or not videos:
        return None, "pack has no ranked_videos"
    return pack, "ok"


def prune_pack(pack, niche_label, exclude=frozenset()):
    """Reduce a full signal pack to the mini payload the page embeds.

    `exclude` skips those video ids (off-avatar receipts); next-ranked rows
    backfill. Topic rows keep only clusters (>= 2 videos) — a 1-video row is a
    title, not a topic — and each carries a plain example_title for display."""
    videos = []
    ranked = sorted(
        [v for v in pack.get("ranked_videos", []) if isinstance(v, dict)
         and v.get("video_id") not in exclude],
        key=lambda v: (v.get("outlier_score") or v.get("outlier_multiplier") or 0),
        reverse=True,
    )
    for v in ranked[:MAX_VIDEOS]:
        videos.append({
            "video_id": v.get("video_id"),
            "title": v.get("title") or "(untitled)",
            "url": safe_url(v.get("url")),
            "channel": v.get("channel_title") or v.get("channel_handle") or "(unknown channel)",
            "outlier_multiplier": v.get("outlier_multiplier"),
            "views": v.get("views"),
            "views_per_day": v.get("views_per_day"),
            "topic": v.get("topic"),
            "published_at": v.get("published_at"),
            "why": derive_why(v),
        })

    topics = []
    raw_topics = ((pack.get("leaderboard") or {}).get("topics")) or []
    raw_topics = [t for t in raw_topics if isinstance(t, dict) and t.get("topic")
                  and isinstance(t.get("video_count"), int) and t["video_count"] >= 2]
    raw_topics.sort(key=lambda t: t.get("score_sum") or 0, reverse=True)
    for t in raw_topics[:MAX_TOPICS]:
        topics.append({
            "topic": t.get("topic"),
            "score_sum": t.get("score_sum"),
            "video_count": t.get("video_count"),
            "example_title": _topic_example_title(pack, t, exclude),
        })

    channels = pack.get("channels") or []
    mini = {
        "mode": "full",
        "pack_version": pack.get("pack_version"),
        "niche_slug": pack.get("niche_slug"),
        "niche_label": niche_label,
        "generated_at": pack.get("generated_at"),
        "status": pack.get("status"),
        "coverage": pack.get("coverage") or {},
        "channel_count": len(channels) if isinstance(channels, list) else None,
        "videos": videos,
        "topics": topics,
        "whitespace": derive_whitespace(pack),
    }
    applied = sorted(set(exclude) & set(_videos_by_id(pack)))
    if applied:  # key only present when an exclusion actually bit — plain bakes byte-identical
        mini["excluded_ids"] = applied
    nuggets = extract_enrichment_nuggets(pack)
    if nuggets:  # key only present when the pack carries usable enrichment — plain bakes byte-identical
        mini["enrichment_nuggets"] = nuggets
    return mini


# ---------------------------------------------------------- whitespace insight

def derive_whitespace(pack):
    """ONE honest whitespace insight from the leaderboard, or None.

    Priority 1 — underused format: appears rarely but scores at/above the pack's
    median average score (the lane works; nobody is crowding it).
    Priority 2 — concentrated topic: outsized score from few videos
    (demand is proven, supply is thin).
    """
    lb = pack.get("leaderboard") or {}

    formats = [f for f in (lb.get("formats") or [])
               if isinstance(f, dict) and f.get("hook_format")
               and isinstance(f.get("avg_score"), (int, float))
               and isinstance(f.get("count"), int) and f.get("count") >= 1]
    if len(formats) >= 3:
        med_count = statistics.median(f["count"] for f in formats)
        med_score = statistics.median(f["avg_score"] for f in formats)
        cands = [f for f in formats if f["count"] < med_count and f["avg_score"] >= med_score]
        if cands:
            best = max(cands, key=lambda f: f["avg_score"])
            lane = plain_hook(best["hook_format"])
            if best.get("desire_template"):
                lane += f", where the payoff on the table is {plain_desire(best['desire_template'])}"
            times = "exactly once" if best["count"] == 1 else f"only {best['count']} times"
            ratio_bit = ""
            if med_score and best["avg_score"] / med_score >= 1.15:
                ratio_bit = (f", and it scored about {best['avg_score'] / med_score:.1f}× "
                             "the field's median when it ran")
            return {
                "kind": "format",
                "headline": "One lane is sitting open",
                "body": (f"The open lane: {lane}. That exact combination shows up {times} "
                         f"in this sample{ratio_bit}. It works, and nobody is crowding it yet. "
                         f"A founder's move here: {founder_make(best['hook_format'])}."),
                "receipt": f"count {best['count']} vs sample median {med_count:.0f} · avg score {best['avg_score']:.1f} vs median {med_score:.1f}",
            }

    topics = [t for t in (lb.get("topics") or [])
              if isinstance(t, dict) and t.get("topic")
              and isinstance(t.get("score_sum"), (int, float))
              and isinstance(t.get("video_count"), int) and t.get("video_count") >= 1]
    if len(topics) >= 2:
        max_count = max(t["video_count"] for t in topics)
        cands = [t for t in topics if t["video_count"] <= max(1, max_count // 2)]
        if cands:
            best = max(cands, key=lambda t: t["score_sum"] / t["video_count"])
            title = _topic_example_title(pack, best)
            subject = (f"the subject behind “{title}”" if title
                       else "one narrow subject in this sample")
            vids = "a single video" if best["video_count"] == 1 else f"just {best['video_count']} videos"
            return {
                "kind": "topic",
                "headline": "Concentrated demand, thin supply",
                "body": (f"One theme is pulling far more than its share: {subject} sits near the top "
                         f"of this board on {vids}, while the busiest theme here has {max_count} videos "
                         "chasing it. The demand is proven and the shelf is close to empty. "
                         "A founder's move here: the same subject answered from your own "
                         "operation, numbers on screen, as the second voice in a lane that barely has a first."),
                "receipt": f"score {best['score_sum']:.1f} across {best['video_count']} video(s) · busiest topic: {max_count} videos",
            }
    return None


# -------------------------------------------------------- enrichment nuggets

def extract_enrichment_nuggets(pack):
    """AT MOST 2 nuggets from an optional pack `enrichment` block (pack_enrich.py):
    one rising-topic demand note + one market-pulse line, each with a source URL.
    A taste of the full report's enrichment layer — extension, not duplication.
    Missing/malformed enrichment -> [] (silent degrade to pre-enrichment behavior)."""
    enr = pack.get("enrichment")
    if not isinstance(enr, dict):
        return []
    nuggets = []

    topics = [t for t in (enr.get("topics") or [])
              if isinstance(t, dict) and t.get("topic") and t.get("demand_note")
              and isinstance(t.get("sources"), list)
              and any(isinstance(s, dict) and isinstance(s.get("url"), str)
                      and s["url"].startswith(("http://", "https://")) for s in t["sources"])
              and t.get("label")]
    rising = [t for t in topics if t.get("trend_direction") == "rising"]
    pick = (rising or topics)[:1]
    for t in pick:
        src = next(s for s in t["sources"]
                   if isinstance(s, dict) and isinstance(s.get("url"), str)
                   and s["url"].startswith(("http://", "https://")))
        nuggets.append({
            "kind": "topic_demand",
            "topic": t["topic"],
            "topic_title": _leaderboard_topic_title(pack, t["topic"]),
            "text": t["demand_note"],
            "trend_direction": t.get("trend_direction") or "unknown",
            "url": src["url"],
            "source_title": src.get("title") or "",
            "label": str(t["label"]),
        })

    pulses = [m for m in (enr.get("market_pulse") or [])
              if isinstance(m, dict) and m.get("note") and m.get("label")
              and isinstance(m.get("url"), str) and m["url"].startswith(("http://", "https://"))]
    for m in pulses[:1]:
        nuggets.append({
            "kind": "market_pulse",
            "text": m["note"],
            "url": m["url"],
            "source_title": "",
            "label": str(m["label"]),
        })
    return nuggets


def render_enrichment_nuggets(nuggets):
    parts = []
    for n in nuggets:
        if n["kind"] == "topic_demand":
            # Plain reference only — the internal topic key never reaches prose.
            subject = (f"the subject behind &ldquo;{esc(_shorten(n['topic_title']))}&rdquo;"
                       if n.get("topic_title") else "this board&rsquo;s top subject")
            head = f"Demand is moving on {subject}"
            if n.get("trend_direction") == "rising":
                head = f"Rising demand: {subject}"
        else:
            head = "What changed in this niche recently"
        parts.append(
            '        <div class="ws-insight">\n'
            f'          <p class="ws-headline">{head}</p>\n'
            f'          <p>{esc(n["text"])}</p>\n'
            f'          <p class="ws-receipt">{esc(n["label"])} &middot; '
            f'<a href="{esc(safe_url(n["url"]))}" rel="noopener">{esc(n.get("source_title") or "source")}</a></p>\n'
            '        </div>'
        )
    return "\n".join(parts)


# ------------------------------------------------------------------ rendering

def render_video_rows(videos):
    rows = []
    for i, v in enumerate(videos, 1):
        meta_bits = [esc(v["channel"])]
        views = fmt_views(v.get("views"))
        if views:
            meta_bits.append(esc(views))
        if v.get("published_at"):
            meta_bits.append(esc(str(v["published_at"])[:10]))
        rows.append(
            '        <li class="video-row">\n'
            f'          <span class="vr-rank">{i:02d}</span>\n'
            '          <span class="vr-main">\n'
            f'            <a class="vr-title" href="{esc(v["url"])}" rel="noopener">{esc(v["title"])}</a>\n'
            f'            <span class="vr-meta">{" &middot; ".join(meta_bits)}</span>\n'
            '          </span>\n'
            '          <span class="vr-mult">\n'
            f'            <span class="vr-mult-n">{esc(fmt_mult(v.get("outlier_multiplier")))}</span>\n'
            '            <span class="vr-mult-label">channel normal</span>\n'
            '          </span>\n'
            '        </li>'
        )
    return "\n".join(rows)


def _shorten(text, limit=56):
    text = str(text or "").strip()
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0].rstrip(" ,;:—-")
    return cut + "…"


def render_topic_rows(topics):
    """Cluster rows only (video_count >= 2). Display name is a real video title
    from the cluster — never the internal topic key."""
    scores = [t.get("score_sum") or 0 for t in topics]
    top = max(scores) if scores else 0
    rows = []
    for i, t in enumerate(topics, 1):
        score = t.get("score_sum") or 0
        width = int(round((score / top) * 100)) if top else 0
        count = t.get("video_count")
        name = (f"The theme behind &ldquo;{esc(_shorten(t['example_title']))}&rdquo;"
                if t.get("example_title") else "A theme this sample repeats")
        meta = (f"{count} videos on it &middot; score {score:.1f}"
                if isinstance(count, int) else f"score {score:.1f}")
        rows.append(
            '        <li class="topic-row">\n'
            f'          <span class="tr-rank">{i:02d}</span>\n'
            f'          <span class="tr-name">{name}</span>\n'
            f'          <span class="tr-bar"><span style="width:{width}%"></span></span>\n'
            f'          <span class="tr-meta">{meta}</span>\n'
            '        </li>'
        )
    return "\n".join(rows)


def render_why_rows(videos):
    """One line per top video on WHY it broke pattern — the mechanism, plainly."""
    rows = []
    for i, v in enumerate(videos, 1):
        if not v.get("why"):
            continue
        rows.append(
            '        <li class="why-row">\n'
            f'          <span class="wr-rank">{i:02d}</span>\n'
            '          <span class="wr-main">\n'
            f'            <span class="wr-title">{esc(_shorten(v["title"]))}</span>\n'
            f'            <span class="wr-why">{esc(v["why"])}</span>\n'
            '          </span>\n'
            '        </li>'
        )
    return "\n".join(rows)


def render_whitespace(ws):
    if ws is None:
        return (
            '        <div class="ws-insight">\n'
            '          <p class="ws-headline">No lane cleared the evidence bar</p>\n'
            '          <p>Nothing in this sample is both working and uncrowded enough to call an open lane. '
            'That is a finding, not a gap &mdash; a comforting whitespace map that hides a crowded field would cost you months.</p>\n'
            '        </div>'
        )
    return (
        '        <div class="ws-insight">\n'
        f'          <p class="ws-headline">{esc(ws["headline"])}</p>\n'
        f'          <p>{esc(ws["body"])}</p>\n'
        f'          <p class="ws-receipt">Receipt: {esc(ws["receipt"])}</p>\n'
        '        </div>'
    )


def _variant_paragraphs():
    """Goal- and size-personalized closers for beat 05. All variants baked in;
    the page's JS reveals the pair matching the visitor's answers."""
    goal = {
        "reach": "Your pick: weight the topic leaderboard. Demand the niche has already proven pulls hardest for discovery.",
        "trust": "Your pick: teach the mechanism behind one outlier instead of chasing five. Depth converts attention into belief.",
        "conversion": "Your pick: the open lane. Reach numbers are proxies for you &mdash; less crowd means more buyer attention per view.",
    }
    size = {
        "s0": "Under 1K, your own channel median is still noise. Read these outliers as the niche&rsquo;s scoreboard, not yours &mdash; copy the packaging move, never the topic verbatim.",
        "s1": "At 1K&ndash;10K you have enough signal to test against your own median. One leaderboard topic against one open-lane bet per batch.",
        "s2": "At 10K&ndash;100K your own outliers outrank the niche&rsquo;s. Use this page to check whether your winners sit where the pull actually is.",
        "s3": "Past 100K you set part of this scoreboard. The open lane is your cheapest expansion &mdash; nobody expects you there yet.",
    }
    lines = []
    for k, v in goal.items():
        lines.append(f'              <p class="variant" data-goal="{k}" hidden>{v}</p>')
    for k, v in size.items():
        lines.append(f'              <p class="variant" data-size="{k}" hidden>{v}</p>')
    return "\n".join(lines)


def render_teaching_panel(mini, mode):
    """The 5-beat teaching panel (what it is → total menu → scoreboard →
    white space → what it means for you). Full mode cites real numbers;
    interview mode teaches the frame with none."""
    if mode == "full":
        top_video = mini["videos"][0] if mini["videos"] else None
        mult_line = ""
        if top_video and isinstance(top_video.get("outlier_multiplier"), (int, float)):
            mult_line = (f" The top outlier in this report runs at {fmt_mult(top_video['outlier_multiplier'])} "
                         "&mdash; the channel&rsquo;s own audience voting “more of this.”")
        beat1 = ("An outlier is a video that beat its own channel&rsquo;s normal &mdash; views per day "
                 "divided by that channel&rsquo;s typical views per day. A 6× outlier did six times "
                 "the channel&rsquo;s usual daily pull." + mult_line)

        ch = mini.get("channel_count")
        menu_src = (f"{ch} channels" if isinstance(ch, int) and ch > 0 else "the sampled channels")
        beat2 = (f"The five outlier rows in this report are the winners, not the field. They surfaced from {menu_src} "
                 "and every recent video each one published &mdash; the full menu of what this niche is currently trying.")

        if mini["topics"]:
            t0 = mini["topics"][0]
            ref = (f" &mdash; the one behind &ldquo;{esc(_shorten(t0['example_title']))}&rdquo; &mdash;"
                   if t0.get("example_title") else "")
            count_bit = (f"{t0['video_count']} separate videos"
                         if isinstance(t0.get("video_count"), int) else "several videos")
            beat3 = (f"Pull concentrates. One theme{ref} put {count_bit} on this board. "
                     "A subject that repeats among outliers is demand talking &mdash; before you spend a single filming day.")
        else:
            beat3 = ("Pull usually concentrates &mdash; a few subjects hold most of the outlier energy in a niche. "
                     "In this sample it hasn&rsquo;t clustered yet: each winner above broke pattern on its own subject, "
                     "which is why the one-line read on each hook matters more than any topic list.")

        if mini.get("whitespace"):
            beat4 = ("White space means demand without supply: a lane that scores when tried but almost "
                     "nobody is trying. The open-lane note on this page is exactly one of those, with its receipt attached.")
        else:
            beat4 = ("White space means demand without supply: a lane that scores when tried but almost nobody is trying. "
                     "This sample surfaced none that cleared the evidence bar &mdash; also worth knowing.")
    else:
        beat1 = ("An outlier is a video that beat its own channel&rsquo;s normal &mdash; views per day divided "
                 "by that channel&rsquo;s typical views per day. A 6× outlier did six times the channel&rsquo;s usual daily pull.")
        beat2 = ("A real read starts from the full menu: every recent video across a set of niche channels, "
                 "not a highlight reel. That menu is what the refreshed edition of this page will carry.")
        beat3 = ("Pull concentrates. A few topics usually hold most of the outlier energy in any niche &mdash; "
                 "a scoreboard like that is demand talking before you spend a filming day.")
        beat4 = ("White space means demand without supply: a lane that scores when tried but almost nobody is trying. "
                 "Finding one honestly requires the measured data this edition is still waiting on.")

    beat5_base = ("Outliers are the niche handing you its receipts. What to do with them depends on who you are "
                  "and where you stand &mdash; which is why this page asked.")

    beats = [
        ("What an outlier is", f"<p>{beat1}</p>"),
        ("The total menu", f"<p>{beat2}</p>"),
        ("The scoreboard", f"<p>{beat3}</p>"),
        ("The open lane", f"<p>{beat4}</p>"),
        ("What it means for you", f"<p>{beat5_base}</p>\n{_variant_paragraphs()}"),
    ]
    rows = []
    for i, (title, body) in enumerate(beats, 1):
        rows.append(
            '        <li class="beat">\n'
            f'          <span class="beat-n">{i:02d}</span>\n'
            '          <span>\n'
            f'            <p class="beat-title">{title}</p>\n'
            f'            <span class="beat-body">{body}</span>\n'
            '          </span>\n'
            '        </li>'
        )
    return "\n".join(rows)


def _block(name, index, title, dek, inner):
    return (
        f'      <section class="block" data-block="{name}">\n'
        '        <div class="block-head">\n'
        f'          <span class="label note-index">NOTE / {index:02d}</span>\n'
        '        </div>\n'
        f'        <h2>{title}</h2>\n'
        f'        <p class="block-dek">{dek}</p>\n'
        '        <p class="lead-why"></p>\n'
        f'{inner}\n'
        '      </section>'
    )


def compose_blocks(mini, mode):
    blocks = []
    idx = 1
    if mode == "full":
        blocks.append(_block(
            "outliers", idx, "The five that broke pattern",
            "Ranked by how far each video ran past its own channel&rsquo;s normal. Every row links to its receipt.",
            '        <ol class="video-list">\n' + render_video_rows(mini["videos"]) + "\n        </ol>",
        ))
        idx += 1
        why_rows = render_why_rows(mini["videos"])
        if why_rows:
            blocks.append(_block(
                "pattern", idx, "Why each one broke pattern",
                "One line each on the hook mechanics &mdash; the part you can copy. The numbers stay in the list above.",
                '        <ol class="why-list">\n' + why_rows + "\n        </ol>",
            ))
            idx += 1
        if mini["topics"]:
            blocks.append(_block(
                "topics", idx, "Where the pull concentrates",
                "Only themes that repeat make this list &mdash; a subject that breaks pattern more than once is demand talking.",
                '        <ol class="topic-list">\n' + render_topic_rows(mini["topics"]) + "\n        </ol>",
            ))
            idx += 1
        blocks.append(_block(
            "whitespace", idx, "One open lane",
            "The single clearest gap this sample supports &mdash; stated with its evidence, or honestly absent.",
            render_whitespace(mini.get("whitespace")),
        ))
        idx += 1
        if mini.get("enrichment_nuggets"):
            n_sig = len(mini["enrichment_nuggets"])
            blocks.append(_block(
                "market-signal", idx,
                "Two live market signals" if n_sig == 2 else "One live market signal",
                "A taste of the live-market layer behind the full Content Growth Blueprint &mdash; "
                "each line carries its source.",
                render_enrichment_nuggets(mini["enrichment_nuggets"]),
            ))
            idx += 1
    blocks.append(_block(
        "teach", idx, "How to read an outlier",
        "Five beats. After these, the numbers above read themselves.",
        '        <ol class="beats">\n' + render_teaching_panel(mini, mode) + "\n        </ol>",
    ))
    return "\n\n".join(blocks)


# ----------------------------------------------------------------- honesty UI

def coverage_line(mini, mode):
    if mode != "full":
        return "No measured window behind this edition yet. Nothing on this page pretends otherwise."
    cov = mini.get("coverage") or {}
    names = {"youtube": "YouTube", "tiktok": "TikTok", "instagram": "Instagram"}
    label = lambda k: names.get(str(k).lower(), str(k).capitalize())
    measured = [label(k) for k, v in cov.items() if v == "measured"]
    partial = [label(k) for k, v in cov.items() if v == "partial"]
    absent = [label(k) for k, v in cov.items() if v == "none"]
    bits = []
    if measured:
        bits.append("Measured: " + ", ".join(measured))
    if partial:
        bits.append("Partial: " + ", ".join(partial))
    if absent:
        bits.append("Not yet measured: " + ", ".join(absent))
    gen = str(mini.get("generated_at") or "")[:10]
    if gen:
        bits.append(f"Data window closed {gen}")
    return ". ".join(bits) + "." if bits else ""


def status_note(mode):
    if mode == "full":
        return ""
    return ('<p class="status-note">Live niche data refresh pending &mdash; this edition ships the reading '
            'frame now; the measured numbers land in the next bake. No number on this page is invented.</p>')


def generated_line(mini, mode, niche_label):
    if mode == "full":
        gen = str(mini.get("generated_at") or "")[:10]
        return f"Outlier mini-report &middot; {esc(niche_label)} &middot; data window closed {esc(gen)}"
    return f"Outlier mini-report &middot; {esc(niche_label)} &middot; interview edition (data refresh pending)"


def with_utm(cta_url, niche_slug):
    """The one permitted analytics surface: UTM params on the outbound CTA."""
    if "utm_" in cta_url:
        return cta_url
    params = urlencode({
        "utm_source": "outlier-mini-report",
        "utm_medium": "lead_magnet",
        "utm_campaign": niche_slug or "mini-report",
    })
    joiner = "&" if "?" in cta_url else "?"
    return cta_url + joiner + params


# ----------------------------------------------------------------------- bake

def bake(template_path, pack_path, niche_label, cta_url, out_path, exclude=frozenset()):
    template = Path(template_path).read_text(encoding="utf-8")

    pack, reason = load_pack(pack_path)
    if pack is not None:
        mode = "full"
        mini = prune_pack(pack, niche_label, exclude=exclude)
        niche_slug = pack.get("niche_slug")
    else:
        mode = "interview"
        mini = {"mode": "interview", "niche_label": niche_label, "videos": [], "topics": [],
                "whitespace": None, "coverage": {}, "generated_at": None}
        niche_slug = None

    final_cta = with_utm(cta_url, niche_slug)
    data_json = json.dumps(mini, ensure_ascii=False).replace("</", "<\\/")

    out = template
    replacements = {
        "{{NICHE_LABEL}}": esc(niche_label),
        "{{REPORT_BLOCKS}}": compose_blocks(mini, mode),
        "{{COVERAGE_LINE}}": coverage_line(mini, mode),
        "{{STATUS_NOTE}}": status_note(mode),
        "{{GENERATED_LINE}}": generated_line(mini, mode, niche_label),
        "{{CTA_URL}}": esc(final_cta),
        "{{DATA_JSON}}": data_json,
    }
    for key, val in replacements.items():
        out = out.replace(key, val)

    leftover = sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", out)))
    if leftover:
        raise SystemExit(f"[build_lead_magnet] FAIL — unreplaced placeholders: {', '.join(leftover)}")

    dest = Path(out_path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out, encoding="utf-8")
    return mode, reason, mini, dest


def main():
    ap = argparse.ArgumentParser(description="Bake the interactive lead-magnet mini-report from a signal pack.")
    ap.add_argument("--pack", required=True, help="Path to a signal-pack JSON (outlier_radar contract)")
    ap.add_argument("--niche-label", required=True, help="Human niche label shown on the page")
    ap.add_argument("--cta-url", required=True, help="Outbound offer/ESP URL for the CTA (UTM appended)")
    ap.add_argument("--out", required=True, help="Output HTML path")
    ap.add_argument("--exclude", default="",
                    help="Comma-separated video ids to skip (off-avatar receipts); next-ranked rows backfill")
    ap.add_argument("--template", default=str(DEFAULT_TEMPLATE), help="Template override (default: templates/lead-magnet/mini-report.html)")
    args = ap.parse_args()

    if not Path(args.template).exists():
        raise SystemExit(f"[build_lead_magnet] FAIL — template missing: {args.template}")

    exclude = frozenset(x.strip() for x in args.exclude.split(",") if x.strip())
    mode, reason, mini, dest = bake(args.template, args.pack, args.niche_label,
                                    args.cta_url, args.out, exclude=exclude)

    cta_host = urlparse(args.cta_url).netloc or "?"
    enrich_bit = (f"enrichment_nuggets={len(mini['enrichment_nuggets'])} "
                  if mini.get("enrichment_nuggets") else "")
    excl_bit = (f"excluded={len(mini['excluded_ids'])}/{len(exclude)} " if mini.get("excluded_ids")
                else (f"excluded=0/{len(exclude)} " if exclude else ""))
    print(f"[build_lead_magnet] wrote {dest} — mode={mode} videos={len(mini.get('videos', []))} "
          f"topics={len(mini.get('topics', []))} whitespace={'yes' if mini.get('whitespace') else 'no'} "
          f"{enrich_bit}{excl_bit}pack_reason=\"{reason}\" cta_host={cta_host} $0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
