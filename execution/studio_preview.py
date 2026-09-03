#!/usr/bin/env python3
"""Studio Preview — our review surface for the Scrapes carousel pool and runs.

Farrice's ask (2026-09-03): "It's not even cropped right to the actual size...
doesn't show me a true preview of what it would look like on Instagram and
LinkedIn... It would be easier if a box popped up and I can type into that box
and then submit it."

So: a local page that shows every template (or every rendered slide) at its TRUE
4:5 proportion inside a LinkedIn feed card and an Instagram feed card, with a
plain comment box per item and Approve / Retire buttons.

  pool mode:  python3 execution/studio_preview.py --pool brand_context/templates/linkedin-carousel
  run  mode:  python3 execution/studio_preview.py --run projects/00-social-content/2026-09-03/blind-bar-01-take-a-ag1

Writes:
  <template>/comments.json  (pool)  or  <run>/comments.json  (run)
      — the SAME shape the vendor Studio writes (content-studio/preview_editor.py):
        {"<slide-or-template-id>": [{"id","xPct","yPct","zone","text"}, ...]}
        The vendor record carries NO timestamp key; its id suffix is base-36
        epoch-ms and that is where the displayed time comes from. We do not add
        keys the vendor never writes.
  <pool>/manifest.json      — status / approved_by / approved_on / retired_reason
  <pool>/styles.json        — a retired id is removed from every style list

stdlib only, localhost only, no network calls, $0. Never touches .claude/skills/.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import socket
import struct
import sys
import threading
import time
import webbrowser
from datetime import date, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

# Test hook: called by _atomic_write immediately BEFORE the rename, so a test can
# simulate a crash mid-write and prove the real file is still intact.
_WRITE_INTERRUPT = None


# ── file plumbing ───────────────────────────────────────────────────────
def _atomic_write(path: Path, text: str) -> None:
    """Write via temp + rename. A crash before the rename leaves the old file whole."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.parent / f".{path.name}.tmp-{os.getpid()}-{threading.get_ident()}"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    if _WRITE_INTERRUPT is not None:
        _WRITE_INTERRUPT()  # a raise here must leave `path` untouched
    os.replace(tmp, path)


def _naive_write(path: Path, text: str) -> None:
    """The sabotage twin: truncate the real file and write in place.

    Only the tests call this — it exists so the suite can prove it actually
    catches a half-written manifest rather than passing vacuously.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text[: max(1, len(text) // 2)])
        fh.flush()
        if _WRITE_INTERRUPT is not None:
            _WRITE_INTERRUPT()


def _read_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def _write_json(path: Path, data) -> None:
    _atomic_write(path, json.dumps(data, indent=2) + "\n")


def _png_size(path: Path) -> tuple[int, int] | None:
    """PNG IHDR read — no Pillow needed just to learn a width."""
    try:
        with open(path, "rb") as fh:
            head = fh.read(24)
    except OSError:
        return None
    if len(head) < 24 or head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    w, h = struct.unpack(">II", head[16:24])
    return int(w), int(h)


# ── the vendor comment shape ────────────────────────────────────────────
def _b36(n: int) -> str:
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    if n == 0:
        return "0"
    out = []
    while n:
        n, r = divmod(n, 36)
        out.append(digits[r])
    return "".join(reversed(out))


def _b36_to_int(s: str) -> int | None:
    try:
        return int(s, 36)
    except ValueError:
        return None


def _vendor_comment(text: str, seq: int) -> dict:
    """One record shaped exactly like preview_editor.py's composer writes.

    Vendor keys: id, xPct, yPct, zone, text. Nothing else. Our box is not
    pin-anchored, so the point is the frame centre and the zone is null.
    """
    return {
        "id": f"c{seq}-{_b36(int(time.time() * 1000))}",
        "xPct": 50.0,
        "yPct": 50.0,
        "zone": None,
        "text": text,
    }


def comment_time(record: dict) -> str:
    """The vendor stores no timestamp; the id suffix is base-36 epoch ms."""
    cid = str(record.get("id", ""))
    suffix = cid.rsplit("-", 1)[-1] if "-" in cid else ""
    ms = _b36_to_int(suffix)
    if ms is None or ms < 10**11 or ms > 10**14:
        return ""
    return datetime.fromtimestamp(ms / 1000).strftime("%Y-%m-%d %H:%M")


def append_comment(comments_path: Path, key: str, text: str) -> list[dict]:
    """Append one comment under `key`, preserving everything already there."""
    data = _read_json(comments_path, {})
    if not isinstance(data, dict):
        data = {}
    bucket = data.get(key)
    if not isinstance(bucket, list):
        bucket = []
    bucket.append(_vendor_comment(text, len(bucket) + 1))
    data[key] = bucket
    _write_json(comments_path, data)
    return bucket


def read_comments(comments_path: Path, key: str) -> list[dict]:
    data = _read_json(comments_path, {})
    bucket = data.get(key) if isinstance(data, dict) else None
    return bucket if isinstance(bucket, list) else []


# ── sources ─────────────────────────────────────────────────────────────
class Item:
    __slots__ = ("key", "title", "subtitle", "status", "png", "comments_path",
                 "render_cmd", "data_path")

    def __init__(self, key, title, subtitle, status, png, comments_path, render_cmd, data_path):
        self.key = key
        self.title = title
        self.subtitle = subtitle
        self.status = status
        self.png = png
        self.comments_path = comments_path
        self.render_cmd = render_cmd
        self.data_path = data_path


def _rel(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


class PoolSource:
    mode = "pool"

    def __init__(self, pool_dir: Path):
        self.dir = pool_dir.resolve()
        self.manifest_path = self.dir / "manifest.json"
        self.styles_path = self.dir / "styles.json"

    @property
    def name(self) -> str:
        m = _read_json(self.manifest_path, {})
        return str(m.get("pool") or self.dir.name)

    @property
    def brand(self) -> str | None:
        m = _read_json(self.manifest_path, {})
        b = m.get("brand")
        return str(b) if b else None

    def templates(self) -> list[dict]:
        m = _read_json(self.manifest_path, {})
        entries = m.get("templates") if isinstance(m, dict) else m
        if isinstance(entries, dict):
            entries = list(entries.values())
        return [e for e in (entries or []) if isinstance(e, dict)]

    def items(self) -> list[Item]:
        out = []
        for t in self.templates():
            tid = str(t.get("id", "")).strip()
            if not tid:
                continue
            png = self.dir / "_preview" / f"{tid}.png"
            data_file = self.dir / tid / "sample.json"
            cmd = (
                "uv run --quiet --with playwright python "
                ".claude/skills/viz-image-gen/scripts/render_template.py "
                f"--template-pool {self.name} --template-id {tid} "
                "--brand-context brand_context --use-sample-text --no-ai-bg "
                f"--data <json FILE> --output {_rel(png)}"
            )
            sub = " · ".join(x for x in [t.get("role"), t.get("style"),
                                         t.get("render_mode")] if x)
            out.append(Item(
                key=tid,
                title=tid,
                subtitle=sub,
                status=str(t.get("status", "")).lower(),
                png=png,
                comments_path=self.dir / tid / "comments.json",
                render_cmd=cmd,
                data_path=data_file if data_file.exists() else None,
            ))
        return out

    # ── status writes ──
    def set_status(self, tid: str, status: str, reason: str | None = None,
                   writer=None) -> dict:
        writer = writer or _write_json
        m = _read_json(self.manifest_path, {})
        entries = m.get("templates")
        if not isinstance(entries, list):
            raise ValueError("manifest.json has no templates[] list")
        hit = None
        for e in entries:
            if isinstance(e, dict) and str(e.get("id")) == tid:
                hit = e
                break
        if hit is None:
            raise KeyError(tid)
        hit["status"] = status
        if status == "approved":
            hit["approved_by"] = "Farrice"
            hit["approved_on"] = date.today().isoformat()
            hit.pop("retired_reason", None)
        elif status == "retired":
            hit["retired_reason"] = reason or ""
            hit.pop("approved_by", None)
            hit.pop("approved_on", None)
        m["updated"] = date.today().isoformat()
        writer(self.manifest_path, m)
        if status == "retired":
            self._drop_from_styles(tid, writer=writer)
        return hit

    def _drop_from_styles(self, tid: str, writer=None) -> None:
        writer = writer or _write_json
        if not self.styles_path.exists():
            return
        s = _read_json(self.styles_path, None)
        if not isinstance(s, dict):
            return
        changed = False
        for style in s.get("styles") or []:
            if not isinstance(style, dict):
                continue
            ids = style.get("template_ids")
            if isinstance(ids, list) and tid in ids:
                style["template_ids"] = [x for x in ids if x != tid]
                changed = True
        if changed:
            writer(self.styles_path, s)


class RunSource:
    mode = "run"

    def __init__(self, run_dir: Path):
        self.dir = run_dir.resolve()
        self.manifest_path = self.dir / "manifest.json"

    @property
    def name(self) -> str:
        return self.dir.name

    @property
    def brand(self) -> str | None:
        m = _read_json(self.manifest_path, {})
        b = m.get("brand")
        return str(b) if b else None

    def items(self) -> list[Item]:
        m = _read_json(self.manifest_path, {})
        slides = m.get("slides") if isinstance(m, dict) else None
        by_path: dict[str, dict] = {}
        if isinstance(slides, list):
            for s in slides:
                if isinstance(s, dict) and s.get("path"):
                    by_path[str(s["path"])] = s
        pngs = sorted(p for p in self.dir.glob("slide-*.png")
                      if re.fullmatch(r"slide-\d+", p.stem))
        out = []
        for png in pngs:
            sid = png.stem  # the vendor's slide_id convention: slide-01
            meta = by_path.get(png.name, {})
            tid = str(meta.get("template_id", "")) or "?"
            data_file = self.dir / f"{sid}.data.json"
            cmd = (
                "uv run --quiet --with playwright python "
                ".claude/skills/viz-image-gen/scripts/render_template.py "
                f"--template-pool linkedin-carousel --template-id {tid} "
                "--brand-context brand_context --no-ai-bg "
                f"--data {_rel(data_file)} --output {_rel(png)}"
            )
            sub = " · ".join(x for x in [tid, meta.get("render_mode"),
                                         meta.get("src")] if x)
            out.append(Item(
                key=sid,
                title=sid,
                subtitle=sub,
                status="",
                png=png,
                comments_path=self.dir / "comments.json",
                render_cmd=cmd,
                data_path=data_file if data_file.exists() else None,
            ))
        return out


# ── brand lock line ─────────────────────────────────────────────────────
def brand_lock_line(brand: str | None) -> str:
    try:
        import scrapes_brand as sb
    except Exception as exc:  # pragma: no cover - import guard
        return f"BRAND LOCK unavailable ({exc.__class__.__name__})"
    try:
        brands = sb.load_brands()
        b, status = sb.resolve(brands, brand=brand) if brand else sb.resolve(brands, cwd=str(ROOT))
        if b is None:
            return f"BRAND LOCK: {status} — no brand resolved for {brand!r}"
        return sb.lock_line(b)
    except Exception as exc:  # pragma: no cover - defensive
        return f"BRAND LOCK unavailable ({exc.__class__.__name__}: {exc})"


# ── page ────────────────────────────────────────────────────────────────
CSS = """
:root{--canvas:#F3F3F0;--ink:#101010;--graphite:#555553;--line:#D8D8D3;--paper:#FFFFFF;}
*{box-sizing:border-box}
body{margin:0;background:var(--canvas);color:var(--ink);
  font:14px/1.45 "Helvetica Neue",Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--ink)}
header.top{position:sticky;top:0;z-index:20;background:var(--canvas);
  border-bottom:1px solid var(--line);padding:18px 28px 14px}
h1{margin:0 0 6px;font-size:19px;font-weight:700;letter-spacing:-0.02em}
.lock{font-size:11px;color:var(--graphite);letter-spacing:0.02em;word-break:break-word}
.counts{margin-top:8px;font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase}
.counts span{margin-right:18px}
.zoombar{margin-top:10px;font-size:11px;letter-spacing:0.16em;text-transform:uppercase;font-weight:700}
.zoombar button{margin-right:6px}
button{font:inherit;font-size:12px;letter-spacing:0.08em;text-transform:uppercase;font-weight:700;
  background:var(--paper);color:var(--ink);border:1px solid var(--line);padding:7px 13px;cursor:pointer}
button:hover{border-color:var(--ink)}
button.primary{background:var(--ink);color:#FAFAF8;border-color:var(--ink)}
main{padding:24px 28px 80px}
section.item{border-top:1px solid var(--line);padding:26px 0 30px;display:flex;gap:28px;align-items:flex-start}
section.item:first-child{border-top:none}
.frames{display:flex;gap:24px;align-items:flex-start}
.pane{flex:1 1 auto;min-width:0}
.side{width:360px;flex:0 0 360px;position:sticky;top:150px}
.itemhead{display:flex;align-items:baseline;gap:12px;margin-bottom:14px;flex-wrap:wrap}
.itemhead h2{margin:0;font-size:16px;font-weight:700;letter-spacing:-0.01em}
.sub{font-size:11px;color:var(--graphite);letter-spacing:0.1em;text-transform:uppercase}
.badge{font-size:10px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;
  border:1px solid var(--line);padding:3px 8px}
.badge.approved{background:var(--ink);color:#FAFAF8;border-color:var(--ink)}
.badge.retired{color:var(--graphite);text-decoration:line-through}
.framelabel{font-size:10px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;
  color:var(--graphite);margin-bottom:8px}

/* LinkedIn feed card — 555px is the real desktop feed column at a 1200 viewport */
.li{width:555px;background:var(--paper);border:1px solid var(--line)}
.li .head{display:flex;gap:9px;padding:12px 16px 8px;align-items:center}
.li .name{font-size:14px;font-weight:700;line-height:1.2}
.li .meta{font-size:12px;color:var(--graphite);line-height:1.3}
.li .copy{padding:0 16px 10px;font-size:14px;color:var(--ink)}
.li .react{display:flex;gap:26px;padding:9px 16px;border-top:1px solid var(--line);
  font-size:13px;color:var(--graphite);font-weight:700}
.dot{width:48px;height:48px;border-radius:50%;background:var(--line);flex:0 0 48px}

/* Instagram feed card — 468px is the real web feed column */
.ig{width:468px;background:var(--paper);border:1px solid var(--line)}
.ig .head{display:flex;gap:10px;padding:11px 14px;align-items:center;border-bottom:1px solid var(--line)}
.ig .dot{width:32px;height:32px;flex:0 0 32px}
.ig .handle{font-size:13px;font-weight:700}
.ig .acts{display:flex;gap:14px;padding:10px 14px 4px;font-size:17px;color:var(--ink)}
.ig .pips{display:flex;gap:5px;justify-content:center;padding:8px 0 2px}
.ig .pip{width:6px;height:6px;border-radius:50%;background:var(--line)}
.ig .pip.on{background:var(--graphite)}
.ig .cap{padding:4px 14px 14px;font-size:13px;color:var(--graphite)}
.ig .cap b{color:var(--ink)}

/* the shot itself — exact 4:5, never squeezed */
.shot{width:100%;aspect-ratio:4/5;background:var(--canvas);display:block}
.shot img{width:100%;height:100%;object-fit:contain;display:block}
.missing{width:100%;aspect-ratio:4/5;display:flex;align-items:center;justify-content:center;
  background:var(--canvas);border:1px dashed var(--line);color:var(--graphite);font-size:12px;
  padding:20px;text-align:center}
.raw{display:none;margin-top:16px;max-width:100%;overflow:auto;border:1px solid var(--line);background:var(--paper)}
.raw img{display:block;max-width:none}
section.item.rawopen .raw{display:block}

label.lbl{display:block;font-size:10px;font-weight:700;letter-spacing:0.16em;
  text-transform:uppercase;color:var(--graphite);margin-bottom:6px}
textarea{width:100%;min-height:104px;padding:11px 12px;border:1px solid var(--line);
  background:var(--paper);color:var(--ink);
  font:14px/1.45 "Helvetica Neue",Helvetica,Arial,sans-serif;resize:vertical}
textarea:focus{outline:none;border-color:var(--ink)}
.btnrow{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap}
.note{font-size:11px;color:var(--graphite);margin-top:8px;min-height:14px}
ul.cmts{list-style:none;margin:16px 0 0;padding:0;border-top:1px solid var(--line)}
ul.cmts li{padding:10px 0;border-bottom:1px solid var(--line);font-size:13px;white-space:pre-wrap}
ul.cmts .when{font-size:10px;letter-spacing:0.14em;text-transform:uppercase;color:var(--graphite);
  display:block;margin-bottom:3px}
ul.cmts li.none{color:var(--graphite);font-size:12px}
footer.paths{margin-top:16px;border-top:1px solid var(--line);padding-top:10px;
  font:11px/1.6 "Helvetica Neue",Helvetica,Arial,monospace;color:var(--graphite);word-break:break-all}
"""

JS = """
function post(url, body){
  return fetch(url,{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify(body)}).then(function(r){return r.json();});
}
// Comments are rebuilt with DOM nodes and textContent only — never markup from a string.
function renderComments(key, list){
  var ul = document.getElementById('cmts-' + key);
  if(!ul) return;
  while(ul.firstChild) ul.removeChild(ul.firstChild);
  if(!list.length){
    var empty = document.createElement('li');
    empty.className = 'none';
    empty.textContent = 'No comments yet.';
    ul.appendChild(empty);
    return;
  }
  list.forEach(function(c){
    var li = document.createElement('li');
    var when = document.createElement('span');
    when.className = 'when';
    when.textContent = c.when || '';
    li.appendChild(when);
    li.appendChild(document.createTextNode(c.text || ''));
    ul.appendChild(li);
  });
}
function submitComment(key){
  var ta = document.getElementById('ta-' + key);
  var note = document.getElementById('note-' + key);
  var text = ta.value.trim();
  if(!text){ note.textContent = 'Type something in the box first.'; return; }
  note.textContent = 'Saving…';
  post('/comment', {key:key, text:text}).then(function(res){
    if(!res.ok){ note.textContent = 'Failed: ' + (res.error||'unknown'); return; }
    ta.value = '';
    renderComments(key, res.comments);
    note.textContent = 'Saved to ' + res.path;
  }).catch(function(e){ note.textContent = 'Failed: ' + e; });
}
function approve(key){
  var note = document.getElementById('note-' + key);
  note.textContent = 'Approving…';
  post('/approve', {key:key}).then(function(res){
    if(!res.ok){ note.textContent = 'Failed: ' + (res.error||'unknown'); return; }
    location.reload();
  });
}
function retire(key){
  var ta = document.getElementById('ta-' + key);
  var note = document.getElementById('note-' + key);
  var reason = ta.value.trim();
  if(!reason){ note.textContent = 'Type the retire reason in the box first, then hit Retire.'; return; }
  note.textContent = 'Retiring…';
  post('/retire', {key:key, reason:reason}).then(function(res){
    if(!res.ok){ note.textContent = 'Failed: ' + (res.error||'unknown'); return; }
    location.reload();
  });
}
function toggleRaw(key){
  document.getElementById('item-' + key).classList.toggle('rawopen');
}
function setZoom(z){
  var frames = document.querySelectorAll('.frames');
  for(var i=0;i<frames.length;i++) frames[i].style.zoom = z;
  try{ localStorage.setItem('studioPreviewZoom', z); }catch(e){}
}
(function(){
  var z = null;
  try{ z = localStorage.getItem('studioPreviewZoom'); }catch(e){}
  if(z) setZoom(z);
})();
"""


def _frame_linkedin(item: Item, src_url: str | None, n: int) -> str:
    shot = (f'<div class="shot"><img src="{src_url}" alt="{html.escape(item.title)}"></div>'
            if src_url else
            '<div class="missing">preview PNG missing — see the render command below</div>')
    return f"""<div>
  <div class="framelabel">LinkedIn · document post · 555 px feed column</div>
  <div class="li">
    <div class="head"><div class="dot"></div>
      <div><div class="name">Farrice Cain</div>
      <div class="meta">Proof-to-market for supplement &amp; performance brands · Now</div></div></div>
    <div class="copy">1/{n} — swipe →</div>
    {shot}
    <div class="react"><span>Like</span><span>Comment</span><span>Repost</span><span>Send</span></div>
  </div>
</div>"""


def _frame_instagram(item: Item, src_url: str | None, n: int) -> str:
    shot = (f'<div class="shot"><img src="{src_url}" alt="{html.escape(item.title)}"></div>'
            if src_url else '<div class="missing">preview PNG missing</div>')
    pips = "".join(f'<div class="pip{" on" if i == 0 else ""}"></div>'
                   for i in range(min(max(n, 3), 8)))
    return f"""<div>
  <div class="framelabel">Instagram · carousel · 468 px feed column</div>
  <div class="ig">
    <div class="head"><div class="dot"></div><div class="handle">farricecain</div></div>
    {shot}
    <div class="pips">{pips}</div>
    <div class="acts"><span>♡</span><span>◻</span><span>➤</span></div>
    <div class="cap"><b>farricecain</b> caption sits here — the first line is all the feed shows…</div>
  </div>
</div>"""


def render_page(src, items: list[Item], lock: str, url_for) -> str:
    counts = {"approved": 0, "ready": 0, "retired": 0, "draft": 0, "other": 0}
    for it in items:
        counts[it.status if it.status in counts else "other"] += 1
    mode_label = "Template pool" if src.mode == "pool" else "Run"
    count_html = (
        f'<span>{counts["approved"]} approved</span><span>{counts["ready"]} ready</span>'
        f'<span>{counts["retired"]} retired</span>'
        if src.mode == "pool" else f'<span>{len(items)} slides</span>'
    )

    rows = []
    for it in items:
        png_url = url_for(it) if it.png.exists() else None
        size = _png_size(it.png) if it.png.exists() else None
        raw = ""
        if png_url and size:
            raw = (f'<div class="raw"><img src="{png_url}" width="{size[0]}" height="{size[1]}"'
                   f' alt="raw {html.escape(it.title)}"></div>')
        cmts = read_comments(it.comments_path, it.key)
        if cmts:
            cl = "".join(
                f'<li><span class="when">{html.escape(comment_time(c))}</span>'
                f'{html.escape(str(c.get("text", "")))}</li>' for c in cmts)
        else:
            cl = '<li class="none">No comments yet.</li>'

        badge = (f'<span class="badge {html.escape(it.status)}">{html.escape(it.status)}</span>'
                 if it.status else "")
        actions = ""
        if src.mode == "pool":
            actions = (
                f"<button class=\"primary\" onclick=\"approve('{it.key}')\">Approve</button>"
                f"<button onclick=\"retire('{it.key}')\">Retire</button>")

        li_frame = _frame_linkedin(it, png_url, len(items))
        ig_frame = _frame_instagram(it, png_url, len(items))
        dims = f"{size[0]}×{size[1]} px" if size else "no PNG"
        data_line = (f"data   {html.escape(_rel(it.data_path))}<br>" if it.data_path else "")

        rows.append(f"""<section class="item" id="item-{it.key}">
  <div class="pane">
    <div class="itemhead"><h2>{html.escape(it.title)}</h2>
      <span class="sub">{html.escape(it.subtitle)}</span>{badge}</div>
    <div class="frames">{li_frame}{ig_frame}</div>
    <div class="btnrow"><button onclick="toggleRaw('{it.key}')">Raw PNG 100% · {dims}</button></div>
    {raw}
    <footer class="paths">
      png    {html.escape(_rel(it.png))}<br>
      {data_line}render {html.escape(it.render_cmd)}
    </footer>
  </div>
  <div class="side">
    <label class="lbl" for="ta-{it.key}">Comment</label>
    <textarea id="ta-{it.key}" placeholder="Type what you want changed…"></textarea>
    <div class="btnrow">
      <button class="primary" onclick="submitComment('{it.key}')">Submit</button>
      {actions}
    </div>
    <div class="note" id="note-{it.key}"></div>
    <ul class="cmts" id="cmts-{it.key}">{cl}</ul>
  </div>
</section>""")

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Studio Preview — {html.escape(src.name)}</title>
<style>{CSS}</style></head>
<body>
<header class="top">
  <h1>{mode_label}: {html.escape(src.name)}</h1>
  <div class="lock">{html.escape(lock)}</div>
  <div class="counts">{count_html}</div>
  <div class="zoombar">Frame scale
    <button onclick="setZoom('0.55')">55%</button>
    <button onclick="setZoom('0.75')">75%</button>
    <button onclick="setZoom('1')">100%</button>
  </div>
</header>
<main>{"".join(rows)}</main>
<script>{JS}</script>
</body></html>"""


# ── server ──────────────────────────────────────────────────────────────
def make_handler(src):
    index: dict[str, Item] = {}

    def refresh():
        index.clear()
        items = src.items()
        for it in items:
            index[it.key] = it
        return items

    class Handler(BaseHTTPRequestHandler):
        server_version = "StudioPreview/1.0"

        def log_message(self, fmt, *args):  # quiet
            pass

        # ── helpers ──
        def _send(self, code, body: bytes, ctype: str):
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _json(self, code, payload):
            self._send(code, json.dumps(payload).encode("utf-8"),
                       "application/json; charset=utf-8")

        def _body(self):
            n = int(self.headers.get("Content-Length") or 0)
            if not n:
                return {}
            try:
                return json.loads(self.rfile.read(n).decode("utf-8"))
            except (ValueError, UnicodeDecodeError):
                return {}

        # ── GET ──
        def do_GET(self):
            path = urlparse(self.path).path
            if path in ("/", "/index.html"):
                items = refresh()
                lock = brand_lock_line(src.brand)
                page = render_page(src, items, lock, lambda it: f"/png/{it.key}")
                self._send(200, page.encode("utf-8"), "text/html; charset=utf-8")
                return
            if path.startswith("/png/"):
                key = path[len("/png/"):]
                if not index:
                    refresh()
                it = index.get(key)
                if it is None or not it.png.exists():
                    self._send(404, b"not found", "text/plain; charset=utf-8")
                    return
                self._send(200, it.png.read_bytes(), "image/png")
                return
            self._send(404, b"not found", "text/plain; charset=utf-8")

        # ── POST ──
        def do_POST(self):
            path = urlparse(self.path).path
            body = self._body()
            key = str(body.get("key") or "")
            if not index:
                refresh()
            it = index.get(key)
            if it is None:
                self._json(404, {"ok": False, "error": f"unknown item {key!r}"})
                return
            try:
                if path == "/comment":
                    text = str(body.get("text") or "").strip()
                    if not text:
                        self._json(400, {"ok": False, "error": "empty comment"})
                        return
                    bucket = append_comment(it.comments_path, it.key, text)
                    self._json(200, {
                        "ok": True,
                        "path": _rel(it.comments_path),
                        "comments": [{"text": c.get("text", ""), "when": comment_time(c)}
                                     for c in bucket],
                    })
                    return
                if path == "/approve":
                    if src.mode != "pool":
                        self._json(400, {"ok": False, "error": "approve is pool mode only"})
                        return
                    src.set_status(it.key, "approved")
                    refresh()
                    self._json(200, {"ok": True, "status": "approved"})
                    return
                if path == "/retire":
                    if src.mode != "pool":
                        self._json(400, {"ok": False, "error": "retire is pool mode only"})
                        return
                    reason = str(body.get("reason") or "").strip()
                    if not reason:
                        self._json(400, {"ok": False, "error": "a retire reason is required"})
                        return
                    stamped = f"Farrice {date.today().isoformat()}: {reason}"
                    src.set_status(it.key, "retired", reason=stamped)
                    refresh()
                    self._json(200, {"ok": True, "status": "retired"})
                    return
            except Exception as exc:
                self._json(500, {"ok": False, "error": f"{exc.__class__.__name__}: {exc}"})
                return
            self._json(404, {"ok": False, "error": "no such endpoint"})

    return Handler


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


def build_server(src, port: int | None = None) -> ThreadingHTTPServer:
    return ThreadingHTTPServer(("127.0.0.1", port or free_port()), make_handler(src))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="True-size LinkedIn / Instagram review surface for the Scrapes "
                    "carousel pool and runs.")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--pool", help="template pool dir, e.g. brand_context/templates/linkedin-carousel")
    g.add_argument("--run", help="a finished run dir with slide-0N.png")
    ap.add_argument("--port", type=int, default=None, help="default: a free port")
    ap.add_argument("--no-open", action="store_true", help="print the URL, do not open a browser")
    args = ap.parse_args(argv)

    target = Path(args.pool or args.run)
    if not target.is_absolute():
        target = (Path.cwd() / target).resolve()
    if not target.is_dir():
        print(f"not a directory: {target}", file=sys.stderr)
        return 2

    src = PoolSource(target) if args.pool else RunSource(target)
    items = src.items()
    if not items:
        print(f"nothing to review in {target}", file=sys.stderr)
        return 2

    httpd = build_server(src, args.port)
    url = f"http://127.0.0.1:{httpd.server_address[1]}/"
    print(f"Studio Preview · {src.mode} · {src.name} · {len(items)} item(s)")
    print(url)
    if not args.no_open:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
