#!/usr/bin/env python3
"""canvas_render.py — the /canvas page, Poppy-form (2026-09-10).

Same pattern as brain_graph.py: one self-contained HTML string, board data
embedded, theme from board_theme.py, nav from surface_nav.py, no build step,
no framework. The page talks to pulse_serve over POST /action (canvas.*) and
polls /ping for canvas_mtime so a reply written by a detached `claude -p` run
shows up without a refresh.

    render(slug) -> html        write(slug) -> path (.agent/canvas/<slug>.html)

Layout (Farrice's call 2026-09-10: "make it work like Poppy, that's the muscle
memory I have"):
    left rail   = chat · video/link · profile · note · file · voice · article
    cards       = source (thumbnail + platform badge + transcript), profile
                  (handle → latest posts, each addable), note (skill/system
                  text), chat (conversation sidebar + thread + compose)
    chat panel  = model · effort · 🔎 research · wired skills as chips ·
                  fullscreen (⤢) · one thread per conversation
    right rail  = fit · + · − · light/dark
    wires       = dotted, drag ● onto a card; click a wire to cut

Safety: every string that reaches the DOM from board data (titles, ingested
text, model replies) passes through esc(); markup is assembled from those
escaped strings only and inserted through a fragment helper, never raw.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "execution"))
from board_theme import theme_css  # noqa: E402
import canvas_board as cb  # noqa: E402

OUT_DIR = ROOT / ".agent" / "canvas"

CSS = r"""
html,body{height:100%;margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);overflow:hidden}
*{box-sizing:border-box}
button{font:inherit}
.bar{position:fixed;top:0;left:0;right:0;height:52px;display:flex;align-items:center;gap:12px;padding:0 16px;
  background:color-mix(in srgb,var(--ground) 86%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);z-index:20}
.kicker{font-family:var(--mono);font-size:9px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted)}
.bar h1{font-size:15px;font-weight:500;margin:0;letter-spacing:-.01em;white-space:nowrap}
.bar h1 em{font-style:normal;color:var(--accent)}
.bar .bt{font-size:15px;font-weight:600;color:var(--ink);padding:4px 8px;border-radius:8px;cursor:text;max-width:38vw;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.bar .bt:hover{background:color-mix(in srgb,var(--ink) 6%,transparent)}
.bar select,.bar button{font-size:12px;color:var(--ink);background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:6px 10px}
.bar button{cursor:pointer}.bar button:hover{border-color:var(--accent);color:var(--accent)}
.bar .sp{flex:1}
#stage{position:absolute;inset:0;top:52px;width:100%;height:calc(100% - 52px);cursor:grab;touch-action:none;
  background-image:radial-gradient(color-mix(in srgb,var(--ink) 10%,transparent) 1px,transparent 1px);background-size:22px 22px}
#stage.panning{cursor:grabbing}
#stage svg{position:absolute;inset:0}
.rail{position:fixed;left:14px;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:4px;padding:8px 6px;
  background:var(--panel);border:1px solid var(--line);border-radius:16px;box-shadow:0 8px 30px rgba(0,0,0,.18);z-index:21}
.rail button{width:44px;height:44px;border:0;background:transparent;border-radius:12px;cursor:pointer;font-size:20px;line-height:1;color:var(--ink);position:relative}
.rail button:hover{background:color-mix(in srgb,var(--accent) 14%,transparent)}
.rail button.chat{color:var(--accent)}
.rail .sep{height:1px;background:var(--line);margin:4px 6px}
.rail button[title]:hover:after{content:attr(title);position:absolute;left:52px;top:50%;transform:translateY(-50%);white-space:nowrap;
  background:var(--ink);color:var(--ground);font-size:11px;padding:5px 9px;border-radius:7px;pointer-events:none}
.zoom{position:fixed;right:14px;bottom:36px;display:flex;flex-direction:column;gap:4px;padding:6px;background:var(--panel);border:1px solid var(--line);border-radius:14px;z-index:21}
.zoom button{width:38px;height:38px;border:0;background:transparent;border-radius:10px;cursor:pointer;font-size:16px;color:var(--ink)}
.zoom button:hover{background:color-mix(in srgb,var(--accent) 14%,transparent)}
.edge{fill:none;stroke:var(--accent);stroke-width:2;stroke-dasharray:6 6;opacity:.7;cursor:pointer}
.edge:hover{opacity:1;stroke-width:3;stroke-dasharray:none}
.edge-hit{fill:none;stroke:transparent;stroke-width:14;cursor:pointer}
.rubber{fill:none;stroke:var(--accent);stroke-width:2;stroke-dasharray:6 5;pointer-events:none}
.card{width:100%;height:100%;background:var(--panel);border:1px solid var(--line);border-radius:14px;display:flex;flex-direction:column;
  overflow:visible;box-shadow:0 8px 30px rgba(0,0,0,.18);position:relative}
.card.running{box-shadow:0 0 0 2px var(--accent),0 8px 30px rgba(0,0,0,.18)}
.card.error{border-color:var(--crit)}
.card.selected{box-shadow:0 0 0 2px var(--ink),0 8px 30px rgba(0,0,0,.18)}
.head{display:flex;align-items:center;gap:8px;padding:8px 10px;cursor:move;user-select:none;border-bottom:1px solid var(--line);min-height:34px;border-radius:14px 14px 0 0}
.card.chat .head{background:color-mix(in srgb,var(--accent) 12%,transparent)}
.head .t{flex:1;font-size:12px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.head .k{font-family:var(--mono);font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.head .ic{font-size:13px}
.head .x,.head .fs{cursor:pointer;color:var(--muted);font-size:14px;line-height:1;padding:0 3px}
.head .x:hover{color:var(--crit)}.head .fs:hover{color:var(--accent)}
.thumb{position:relative;height:120px;background:color-mix(in srgb,var(--ink) 8%,transparent);overflow:hidden;flex:none}
.thumb img{width:100%;height:100%;object-fit:cover;display:block}
.thumb .badge{position:absolute;left:8px;top:8px;font-family:var(--mono);font-size:9px;letter-spacing:.12em;text-transform:uppercase;
  background:rgba(0,0,0,.62);color:#fff;padding:3px 7px;border-radius:6px}
.thumb .dur{position:absolute;right:8px;bottom:8px;font-family:var(--mono);font-size:10px;background:rgba(0,0,0,.62);color:#fff;padding:2px 6px;border-radius:5px}
.thumb.fav{display:flex;align-items:center;justify-content:center;height:64px}
.thumb.fav img{width:28px;height:28px;object-fit:contain}
.body{flex:1;overflow:auto;padding:8px 10px;font-size:12px;line-height:1.45;color:var(--soft);white-space:pre-wrap;word-break:break-word}
.body.clamp{overflow:hidden;display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;flex:none;white-space:normal}
.body.editing{outline:1px solid var(--accent);color:var(--ink)}
.foot{font-family:var(--mono);font-size:9.5px;color:var(--muted);padding:5px 10px;border-top:1px solid var(--line);display:flex;gap:10px;align-items:center;border-radius:0 0 14px 14px;margin-top:auto}
.foot a,.foot .lnk{color:var(--accent);text-decoration:none;cursor:pointer}
.port{position:absolute;right:-9px;top:50%;width:18px;height:18px;border-radius:50%;background:var(--accent);border:2px solid var(--ground);
  cursor:crosshair;transform:translateY(-50%);z-index:3}
.port:hover{transform:translateY(-50%) scale(1.25)}
.port.in{left:-9px;right:auto;background:var(--muted);cursor:default}
.posts{flex:1;overflow:auto;padding:6px 8px;display:flex;flex-direction:column;gap:6px}
.post{display:flex;gap:8px;align-items:center;font-size:11px;line-height:1.3}
.post img{width:54px;height:34px;object-fit:cover;border-radius:5px;flex:none;background:color-mix(in srgb,var(--ink) 8%,transparent)}
.post .pt{flex:1;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;color:var(--ink)}
.post .pm{font-family:var(--mono);font-size:9px;color:var(--muted);white-space:nowrap}
.post button{border:1px solid var(--line);background:var(--ground);color:var(--accent);border-radius:6px;padding:2px 7px;font-size:11px;cursor:pointer;flex:none}
.post button:hover{border-color:var(--accent)}
.chatwrap{flex:1;display:flex;min-height:0}
.convos{width:132px;flex:none;border-right:1px solid var(--line);display:flex;flex-direction:column;font-size:11px}
.convos .nc{margin:8px 8px 4px;border:1px solid var(--line);background:var(--ground);color:var(--accent);border-radius:8px;padding:5px 8px;cursor:pointer;text-align:left}
.convos .nc:hover{border-color:var(--accent)}
.convos .lab{font-family:var(--mono);font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);padding:6px 10px 2px}
.convos .lst{flex:1;overflow:auto}
.convos .cv{padding:6px 10px;cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:var(--soft);display:flex;gap:4px;align-items:center}
.convos .cv:hover{background:color-mix(in srgb,var(--ink) 6%,transparent)}
.convos .cv.on{background:color-mix(in srgb,var(--accent) 16%,transparent);color:var(--ink)}
.convos .cv span{flex:1;overflow:hidden;text-overflow:ellipsis}
.convos .cv b{font-weight:400;color:var(--muted);cursor:pointer;padding:0 2px}
.convos .cv b:hover{color:var(--crit)}
.chatmain{flex:1;display:flex;flex-direction:column;min-width:0}
.turns{flex:1;overflow:auto;padding:10px 12px;display:flex;flex-direction:column;gap:10px}
.turn{font-size:12.5px;line-height:1.55;white-space:pre-wrap;word-break:break-word;padding:9px 12px;border-radius:12px;max-width:100%}
.turn.user{background:color-mix(in srgb,var(--accent) 16%,transparent);align-self:flex-end;color:var(--ink);max-width:86%}
.turn.assistant{background:color-mix(in srgb,var(--ink) 5%,transparent);color:var(--soft);white-space:normal}
.md p{margin:0 0 8px}.md p:last-child{margin-bottom:0}
.md h3,.md h4,.md h5,.md h6{margin:12px 0 6px;color:var(--ink);font-weight:600;line-height:1.3}
.md h3{font-size:15px}.md h4{font-size:13.5px}.md h5,.md h6{font-size:12.5px}
.md strong{color:var(--ink)}.md em{font-style:italic}
.md code{font-family:var(--mono);font-size:11px;background:color-mix(in srgb,var(--ink) 8%,transparent);padding:1px 5px;border-radius:4px}
.md ul,.md ol{margin:4px 0 8px;padding-left:20px}.md li{margin:2px 0}
.md hr{border:0;border-top:1px solid var(--line);margin:10px 0}
.md blockquote{margin:6px 0;padding:4px 10px;border-left:3px solid var(--accent);color:var(--soft)}
.md a{color:var(--accent)}
.md .code{position:relative;margin:8px 0;background:var(--ground);border:1px solid var(--line);border-radius:10px}
.md .code pre{margin:0;padding:10px 12px;font-family:var(--mono);font-size:11.5px;line-height:1.5;white-space:pre-wrap;word-break:break-word;color:var(--ink)}
.md .code .cb{position:absolute;right:8px;top:6px;font-family:var(--mono);font-size:10px;color:var(--muted);cursor:pointer;border:1px solid var(--line);border-radius:6px;padding:2px 7px;background:var(--panel)}
.md .code .cb:hover{color:var(--accent);border-color:var(--accent)}
.md .tbl{overflow-x:auto;margin:8px 0}
.md table{border-collapse:collapse;font-size:11.5px;min-width:60%}
.md th,.md td{border:1px solid var(--line);padding:5px 8px;text-align:left;vertical-align:top}
.md th{background:color-mix(in srgb,var(--ink) 6%,transparent);color:var(--ink);font-weight:600}
.turn .m{font-family:var(--mono);font-size:9px;color:var(--muted);margin-top:7px;letter-spacing:.06em}
.turn .cp{float:right;cursor:pointer;color:var(--muted);font-size:11px;margin-left:8px}.turn .cp:hover{color:var(--accent)}
.compose{display:flex;flex-direction:column;gap:6px;padding:8px 10px;border-top:1px solid var(--line)}
.compose textarea{width:100%;min-height:56px;resize:vertical;font:inherit;font-size:12.5px;color:var(--ink);background:var(--ground);
  border:1px solid var(--line);border-radius:10px;padding:8px 10px}
.compose .row{display:flex;gap:6px;align-items:center;flex-wrap:wrap}
.compose select{font:inherit;font-size:11px;color:var(--ink);background:var(--ground);border:1px solid var(--line);border-radius:999px;padding:4px 9px}
.compose .k{font-family:var(--mono);font-size:9px;color:var(--muted);white-space:nowrap}
.compose label.k{display:inline-flex;align-items:center;gap:4px;border:1px solid var(--line);border-radius:999px;padding:3px 8px;cursor:pointer}
.compose select.voice.on{border-color:color-mix(in srgb,var(--accent) 60%,transparent);background:color-mix(in srgb,var(--accent) 12%,transparent);color:var(--ink)}
.compose .chip b{font-weight:400;color:var(--muted);cursor:pointer;padding-left:3px}.compose .chip b:hover{color:var(--crit)}
.compose .chip{font-size:10.5px;border:1px solid color-mix(in srgb,var(--warn) 60%,transparent);color:var(--ink);background:color-mix(in srgb,var(--warn) 14%,transparent);border-radius:999px;padding:3px 9px;white-space:nowrap;max-width:160px;overflow:hidden;text-overflow:ellipsis}
.compose button{margin-left:auto;font-size:12px;color:var(--ground);background:var(--accent);border:0;border-radius:999px;padding:6px 14px;cursor:pointer}
.compose button:disabled{opacity:.45;cursor:default}
.resize{position:absolute;right:2px;bottom:2px;width:14px;height:14px;cursor:nwse-resize;opacity:.4}
.resize:after{content:"";position:absolute;right:3px;bottom:3px;width:7px;height:7px;border-right:2px solid var(--muted);border-bottom:2px solid var(--muted)}
.err{color:var(--crit);font-size:11px;padding:6px 10px}
.hint{color:var(--muted);font-size:11.5px;line-height:1.5}
#modal{position:fixed;inset:0;background:rgba(0,0,0,.45);display:none;align-items:center;justify-content:center;z-index:40}
#modal.on{display:flex}
#modal .box{width:min(640px,92vw);background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px;display:flex;flex-direction:column;gap:10px}
#modal textarea{width:100%;min-height:120px;font:inherit;font-size:13px;color:var(--ink);background:var(--ground);border:1px solid var(--line);border-radius:10px;padding:10px}
#modal .row{display:flex;gap:8px;justify-content:flex-end}
#modal button{font-size:12px;border-radius:8px;padding:7px 14px;cursor:pointer;border:1px solid var(--line);background:var(--ground);color:var(--ink)}
#modal button.go{background:var(--accent);color:var(--ground);border-color:var(--accent)}
#full{position:fixed;inset:0;background:var(--ground);display:none;flex-direction:column;z-index:35}
#full.on{display:flex}
#full .fhead{display:flex;align-items:center;gap:10px;padding:10px 16px;border-bottom:1px solid var(--line);background:color-mix(in srgb,var(--accent) 10%,transparent)}
#full .fhead .t{flex:1;font-weight:600}
#full .fhead button{font-size:12px;border:1px solid var(--line);background:var(--panel);color:var(--ink);border-radius:8px;padding:6px 12px;cursor:pointer}
#full .card{border:0;border-radius:0;box-shadow:none}
#full .convos{width:220px}
#full .turns{padding:18px 8vw}
#full .turn{font-size:14px}
#full .turn.user{max-width:70%}
#full .compose{padding:12px 8vw 18px}
.foot-bar{position:fixed;left:0;right:0;bottom:0;padding:6px 18px;font-family:var(--mono);font-size:9.5px;color:var(--muted);letter-spacing:.06em;
  background:color-mix(in srgb,var(--ground) 86%,transparent);border-top:1px solid var(--line);display:flex;gap:16px;z-index:20;flex-wrap:wrap}
#toast{position:fixed;bottom:36px;left:50%;transform:translateX(-50%);background:var(--panel);border:1px solid var(--line);color:var(--ink);
  font-size:12px;padding:8px 14px;border-radius:99px;opacity:0;transition:opacity .2s;pointer-events:none;z-index:50}
#toast.on{opacity:1}
.empty{position:absolute;left:50%;top:45%;transform:translate(-50%,-50%);text-align:center;color:var(--muted);font-size:13px;pointer-events:none;line-height:1.6}
.empty b{display:block;font-size:22px;color:var(--soft);margin-bottom:8px;font-weight:500}
"""

JS = r"""
(function () {
  'use strict';
  const LIVE = location.protocol.indexOf('http') === 0;
  let B = JSON.parse(document.getElementById('boarddata').textContent);
  const MODELS = JSON.parse(document.getElementById('modeldata').textContent);
  let VOICES = JSON.parse(document.getElementById('voicedata').textContent);
  const stage = document.getElementById('stage');
  const NS = 'http://www.w3.org/2000/svg';
  const svg = document.createElementNS(NS, 'svg');
  svg.setAttribute('width', '100%'); svg.setAttribute('height', '100%');
  stage.appendChild(svg);
  const world = document.createElementNS(NS, 'g'); svg.appendChild(world);
  const edgesG = document.createElementNS(NS, 'g'); world.appendChild(edgesG);
  const nodesG = document.createElementNS(NS, 'g'); world.appendChild(nodesG);
  const rubber = document.createElementNS(NS, 'path'); rubber.setAttribute('class', 'rubber'); world.appendChild(rubber);
  const VIEW_KEY = 'canvas_view_' + B.slug;
  const view = {x: 90, y: 30, k: 1};
  try { Object.assign(view, JSON.parse(localStorage.getItem(VIEW_KEY) || '{}')); } catch (e) {}
  const drafts = {};          // chat id → unsent text
  const expanded = {};        // source id → transcript shown in full
  let selected = null, dragging = null, wiring = null, panning = null, lastMtime = null, fullId = null;

  // Escaped-string → DOM. Every dynamic value passed here has been through esc().
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c])); }
  function setHTML(el, markup) { el.replaceChildren(document.createRange().createContextualFragment(markup)); }
  function applyView() { world.setAttribute('transform', `translate(${view.x},${view.y}) scale(${view.k})`); try { localStorage.setItem(VIEW_KEY, JSON.stringify(view)); } catch (e) {} }
  function toWorld(cx, cy) { const r = stage.getBoundingClientRect(); return {x: (cx - r.left - view.x) / view.k, y: (cy - r.top - view.y) / view.k}; }
  function node(id) { return B.nodes.find(n => n.id === id); }
  function toast(m) { const t = document.getElementById('toast'); t.textContent = m; t.classList.add('on'); clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('on'), 2400); }
  function convo(n) { const cs = n.convos || []; return cs.find(c => c.id === n.active) || cs[0] || {id: '', title: '', turns: []}; }
  function fmtN(v) { if (v == null) return ''; return v >= 1e6 ? (v / 1e6).toFixed(1) + 'M' : v >= 1e3 ? (v / 1e3).toFixed(v >= 1e4 ? 0 : 1) + 'K' : String(v); }
  function fmtDur(s) { if (!s) return ''; s = Math.round(s); return Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0'); }
  function ytId(u) { const m = String(u || '').match(/(?:v=|youtu\.be\/|shorts\/|embed\/)([A-Za-z0-9_-]{11})/); return m ? m[1] : ''; }
  function domain(u) { try { return new URL(u).hostname.replace(/^www\./, ''); } catch (e) { return ''; } }
  function platform(n) {
    const s = String(n.source || ''); const k = n.kind || '';
    if (/youtube\.com|youtu\.be/.test(s)) return 'youtube';
    if (/tiktok\.com/.test(s)) return 'tiktok';
    if (/instagram\.com/.test(s)) return 'instagram';
    if (k === 'pdf') return 'pdf'; if (k === 'local_audio') return 'voice'; if (k === 'local_video') return 'video';
    if (k === 'article' || /^https?:/.test(s)) return 'article';
    return k === 'pending' ? 'fetching' : 'text';
  }

  // ---------- markdown (what the model writes) → markup, built only from esc()'d text ----------
  function inline(s) {
    return s
      .replace(/`([^`\n]+)`/g, '<code>$1</code>')
      .replace(/\*\*([^*\n]+)\*\*/g, '<strong>$1</strong>')
      .replace(/(^|[^*\w])\*([^*\n]+)\*(?!\w)/g, '$1<em>$2</em>')
      .replace(/\[([^\]\n]+)\]\((https?:\/\/[^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  }
  function md(raw) {
    const lines = esc(raw)
      .replace(/&lt;details&gt;\s*&lt;summary&gt;([^&]*)&lt;\/summary&gt;/g, '<details><summary>$1</summary>\n')
      .replace(/&lt;\/details&gt;/g, '\n</details>')
      .split('\n'); const out = []; let i = 0;
    const isSep = l => /^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$/.test(l);
    const cells = l => l.replace(/^\s*\|/, '').replace(/\|\s*$/, '').split('|').map(c => c.trim());
    while (i < lines.length) {
      const l = lines[i];
      if (/^\s*```/.test(l)) { const buf = []; i++; while (i < lines.length && !/^\s*```/.test(lines[i])) buf.push(lines[i++]); i++;
        out.push(`<div class="code"><span class="cb" data-copyblock title="copy this block">copy</span><pre>${buf.join('\n')}</pre></div>`); continue; }
      if (l.includes('|') && i + 1 < lines.length && isSep(lines[i + 1])) {
        const head = cells(l); i += 2; const rows = [];
        while (i < lines.length && lines[i].includes('|') && lines[i].trim()) rows.push(cells(lines[i++]));
        out.push(`<div class="tbl"><table><thead><tr>${head.map(c => `<th>${inline(c)}</th>`).join('')}</tr></thead><tbody>${rows.map(r => `<tr>${r.map(c => `<td>${inline(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`); continue; }
      const h = l.match(/^\s*(#{1,4})\s+(.*)$/); if (h) { out.push(`<h${h[1].length + 2}>${inline(h[2])}</h${h[1].length + 2}>`); i++; continue; }
      if (/^\s*[-*•]\s+/.test(l)) { const items = []; while (i < lines.length && /^\s*[-*•]\s+/.test(lines[i])) items.push(lines[i++].replace(/^\s*[-*•]\s+/, '')); out.push(`<ul>${items.map(x => `<li>${inline(x)}</li>`).join('')}</ul>`); continue; }
      if (/^\s*\d+[.)]\s+/.test(l)) { const items = []; while (i < lines.length && /^\s*\d+[.)]\s+/.test(lines[i])) items.push(lines[i++].replace(/^\s*\d+[.)]\s+/, '')); out.push(`<ol>${items.map(x => `<li>${inline(x)}</li>`).join('')}</ol>`); continue; }
      if (/^\s*(---|\*\*\*|___)\s*$/.test(l)) { out.push('<hr>'); i++; continue; }
      if (/^\s*&gt;\s?/.test(l)) { const q = []; while (i < lines.length && /^\s*&gt;\s?/.test(lines[i])) q.push(lines[i++].replace(/^\s*&gt;\s?/, '')); out.push(`<blockquote>${inline(q.join('<br>'))}</blockquote>`); continue; }
      if (!l.trim()) { i++; continue; }
      const p = []; while (i < lines.length && lines[i].trim() && !/^\s*(```|#{1,4}\s|[-*•]\s|\d+[.)]\s|&gt;)/.test(lines[i]) && !(lines[i].includes('|') && i + 1 < lines.length && isSep(lines[i + 1]))) p.push(lines[i++]);
      out.push(`<p>${inline(p.join('<br>'))}</p>`);
    }
    return out.join('');
  }
  function bindCopyBlocks(root) {
    root.querySelectorAll('[data-copyblock]').forEach(el => el.addEventListener('click', ev => { ev.stopPropagation(); const pre = el.parentElement.querySelector('pre'); navigator.clipboard.writeText(pre ? pre.textContent : '').then(() => toast('copied')); }));
  }

  async function act(action, args) {
    if (!LIVE) { toast('open this board through the live server to edit'); return {ok: false}; }
    try {
      const r = await fetch('/action', {method: 'POST', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({action, args: Object.assign({slug: B.slug}, args || {})})});
      const j = await r.json();
      if (!j.ok && j.error) toast(j.error);
      return j;
    } catch (e) { toast('server unreachable'); return {ok: false}; }
  }

  // ---------- edges ----------
  function portOut(n) { return {x: n.x + n.w, y: n.y + n.h / 2}; }
  function portIn(n) { return {x: n.x, y: n.y + n.h / 2}; }
  function curve(a, b) { const dx = Math.max(40, Math.abs(b.x - a.x) * 0.5); return `M${a.x},${a.y} C${a.x + dx},${a.y} ${b.x - dx},${b.y} ${b.x},${b.y}`; }
  function drawEdges() {
    edgesG.replaceChildren();
    for (const e of B.edges) {
      const a = node(e.from), b = node(e.to); if (!a || !b) continue;
      const d = curve(portOut(a), portIn(b));
      const hit = document.createElementNS(NS, 'path'); hit.setAttribute('class', 'edge-hit'); hit.setAttribute('d', d);
      const p = document.createElementNS(NS, 'path'); p.setAttribute('class', 'edge'); p.setAttribute('d', d);
      const cut = async () => { if (!confirm('cut this wire?')) return; const j = await act('canvas.unedge', {from: e.from, to: e.to}); if (j.ok) { B.edges = B.edges.filter(x => !(x.from === e.from && x.to === e.to)); drawNodes(); } };
      hit.addEventListener('click', cut); p.addEventListener('click', cut);
      edgesG.appendChild(hit); edgesG.appendChild(p);
    }
  }

  // ---------- context helpers ----------
  function upstream(n) {
    const parents = {}; for (const e of B.edges) (parents[e.to] = parents[e.to] || []).push(e.from);
    const seen = new Set(); const st = [...(parents[n.id] || [])];
    while (st.length) { const c = st.pop(); if (seen.has(c) || c === n.id) continue; seen.add(c); st.push(...(parents[c] || [])); }
    return [...seen].map(node).filter(Boolean);
  }
  function ctxLabel(n) {
    let tok = 0, src = 0;
    for (const m of upstream(n)) { if (m.type !== 'chat') { tok += m.tokens || 0; src++; } else { for (const t of convo(m).turns) tok += Math.ceil((t.text || '').length / 4); } }
    return `${src} src · ~${tok.toLocaleString()} tok`;
  }
  function costLabel(t) {
    const plan = t.seat === 'claude' ? 'Claude plan' : (t.seat === 'codex' ? 'ChatGPT plan' : 'metered');
    if (typeof t.cost_usd !== 'number') return plan;
    return t.seat === 'gemini' ? '$' + t.cost_usd.toFixed(4) + ' metered' : '≈$' + t.cost_usd.toFixed(2) + ' est · ' + plan;
  }

  // ---------- card markup ----------
  const ICON = {youtube: '▶', tiktok: '♪', instagram: '◎', article: '🌐', pdf: '📄', voice: '🎤', video: '🎬', text: '📝', fetching: '⏳', note: '✎', chat: '💬', profile: '👤'};
  function sourceHTML(n) {
    const pf = platform(n); const id = ytId(n.source); const dom = domain(n.source);
    const meta = n.meta || {};
    let thumb = '';
    if (id) thumb = `<div class="thumb"><img src="https://i.ytimg.com/vi/${esc(id)}/hqdefault.jpg" alt=""><span class="badge">${esc(pf)}</span>${meta.duration_s ? `<span class="dur">${esc(fmtDur(meta.duration_s))}</span>` : ''}</div>`;
    else if (dom) thumb = `<div class="thumb fav"><img src="https://www.google.com/s2/favicons?domain=${esc(dom)}&sz=64" alt=""><span class="badge">${esc(pf)}</span></div>`;
    const body = n.status === 'running' ? 'fetching the transcript…' : (n.text || '');
    const open = !!expanded[n.id];
    const isUrl = /^https?:\/\//.test(n.source || '');
    return `${thumb}<div class="body${open ? '' : ' clamp'}" data-body>${esc(open ? body : body.slice(0, 600))}</div>
      ${n.error ? `<div class="err">${esc(n.error)}</div>` : ''}
      <div class="foot"><span>~${Number(n.tokens || 0).toLocaleString()} tok</span>${meta.channel ? `<span>${esc(meta.channel)}</span>` : ''}
        <span class="lnk" data-expand>${open ? 'less' : 'transcript'}</span>${isUrl ? `<a href="${esc(n.source)}" target="_blank" rel="noopener">open ↗</a>` : ''}
        ${n.type === 'note' ? '<span>dbl-click text to edit</span>' : ''}</div>`;
  }
  function profileHTML(n) {
    const posts = (n.posts || []).map((p, i) => `<div class="post"><img src="${esc(p.thumb || '')}" alt=""><div><div class="pt">${esc(p.title)}</div><div class="pm">${p.views != null ? esc(fmtN(p.views)) + ' views · ' : ''}${esc(fmtDur(p.duration_s))}</div></div><button data-addpost="${i}" title="add this post as a source card">+</button></div>`).join('');
    return `<div class="posts">${posts || '<div class="hint">no posts listed</div>'}</div>
      <div class="foot"><span>latest ${(n.posts || []).length}</span><span class="lnk" data-addall>+ add all</span><a href="${esc(n.source)}" target="_blank" rel="noopener">open ↗</a></div>`;
  }
  function chatHTML(n) {
    const c = convo(n);
    const opts = Object.keys(MODELS).map(m => `<option value="${esc(m)}"${m === n.model ? ' selected' : ''}>${esc(m)}</option>`).join('');
    const effs = (MODELS[n.model] ? MODELS[n.model].efforts : ['medium']).map(e => `<option value="${esc(e)}"${e === n.effort ? ' selected' : ''}>${esc(e)}</option>`).join('');
    const turns = (c.turns || []).map((t, i) => {
      const meta = t.role === 'assistant' ? `<div class="m">${esc(t.model)}/${esc(t.effort)}${t.research ? ' · 🔎 web' : ''}${t.voice ? ' · 🗣 ' + esc(t.voice) : ''} · ${esc(t.seconds)}s · ${costLabel(t)} · ${Number(t.context_tokens || 0).toLocaleString()} ctx tok · ${Number(t.sources || 0)} src</div>` : '';
      const body = t.role === 'user' ? esc(t.text) : `<div class="md">${md(t.text)}</div>`;
      return `<div class="turn ${t.role === 'user' ? 'user' : 'assistant'}"><span class="cp" data-copy="${i}" title="copy as text">⧉</span>${body}${meta}</div>`;
    }).join('');
    const busy = n.status === 'running';
    // Wired notes are SOURCES (they feed the model regardless of the voice menu); show them as
    // "note:" chips with an × that cuts the wire, so nothing looks locked in.
    const skills = upstream(n).filter(m => m.type === 'note').map(m => `<span class="chip note" title="wired note — its text goes in as a source on every turn; × cuts the wire">✎ note: ${esc(m.title)} <b data-unwire="${esc(m.id)}" title="cut this note's wire">×</b></span>`).join('');
    const vopts = VOICES.map(v => `<option value="${esc(v.key)}"${(n.voice || '') === v.key ? ' selected' : ''}>${esc(v.key ? '🗣 ' + v.title : v.title)}</option>`).join('') + '<option value="__add">＋ add a voice…</option>';
    const cvs = (n.convos || []).map(x => `<div class="cv${x.id === c.id ? ' on' : ''}" data-cv="${esc(x.id)}" title="${esc(x.title)}"><span>${esc(x.title)}</span>${x.id === c.id ? `<b data-cvren title="rename">✎</b><b data-cvdel title="delete">×</b>` : ''}</div>`).join('');
    return `<div class="chatwrap">
        <div class="convos"><button class="nc" data-newcv>+ new conversation</button><div class="lab">conversations</div><div class="lst">${cvs}</div></div>
        <div class="chatmain">
          <div class="turns" data-turns>${turns || '<div class="hint">wire sources (drag their ● onto this card), add a note as the skill, then ask.<br>each conversation keeps its own thread; they all read the same wired sources.</div>'}</div>
          ${n.error ? `<div class="err">${esc(n.error)}</div>` : ''}
          <div class="compose">
            <textarea data-draft placeholder="${busy ? 'thinking…' : 'ask about everything wired in · ⌘⏎ to send'}"${busy ? ' disabled' : ''}>${esc(drafts[n.id] || '')}</textarea>
            <div class="row"><select data-model title="model">${opts}</select><select data-effort title="effort">${effs}</select>
            <label class="k" title="let the Claude seat search the live web (WebSearch/WebFetch) before it answers"><input type="checkbox" data-research${n.research ? ' checked' : ''}${(MODELS[n.model] || {}).seat === 'claude' ? '' : ' disabled'}> 🔎 research</label>
            <select data-voice class="voice${n.voice ? ' on' : ''}" title="brand voice for this chat — rides in front of the sources on every turn; 'no voice' = plain model">${vopts}</select>
            ${skills}<span class="k">${esc(ctxLabel(n))}</span>
            <button data-send${busy ? ' disabled' : ''}>${busy ? '…' : 'send'}</button></div>
          </div>
        </div>
      </div>`;
  }
  function cardHTML(n) {
    const kind = n.type === 'source' ? platform(n) : n.type;
    const status = n.status === 'running' ? ' running' : (n.status === 'error' ? ' error' : '');
    const sel = selected === n.id ? ' selected' : '';
    const inner = n.type === 'chat' ? chatHTML(n) : (n.type === 'profile' ? profileHTML(n) : sourceHTML(n));
    return `<div class="card ${esc(n.type)}${status}${sel}" data-id="${esc(n.id)}">
      <div class="head" data-head><span class="ic">${ICON[kind] || '•'}</span><span class="k">${esc(kind)}</span><span class="t" data-title title="${esc(n.title)}">${esc(n.title)}</span>
        ${n.type === 'chat' ? '<span class="fs" data-full title="fullscreen">⤢</span>' : ''}<span class="x" data-del title="delete">×</span></div>
      ${inner}
      <div class="port in" title="in"></div>
      <div class="port" data-port title="drag onto another card to wire"></div>
      <div class="resize" data-resize></div>
    </div>`;
  }

  function drawNodes() {
    nodesG.querySelectorAll('[data-draft]').forEach(t => { const id = t.closest('.card').dataset.id; drafts[id] = t.value; });
    nodesG.replaceChildren();
    for (const n of B.nodes) {
      const fo = document.createElementNS(NS, 'foreignObject');
      fo.setAttribute('x', n.x); fo.setAttribute('y', n.y); fo.setAttribute('width', n.w); fo.setAttribute('height', n.h);
      fo.setAttribute('overflow', 'visible');
      fo.dataset.id = n.id;
      setHTML(fo, `<div xmlns="http://www.w3.org/1999/xhtml" style="width:100%;height:100%">${cardHTML(n)}</div>`);
      nodesG.appendChild(fo);
      bindCard(fo, n);
    }
    document.getElementById('empty').style.display = B.nodes.length ? 'none' : 'block';
    drawEdges();
    if (fullId) drawFull();
  }

  // ---------- fullscreen chat ----------
  const full = document.getElementById('full');
  function drawFull() {
    const n = node(fullId); if (!n) { closeFull(); return; }
    const ta = full.querySelector('[data-draft]'); if (ta) drafts[n.id] = ta.value;
    setHTML(full, `<div class="fhead"><span class="ic">💬</span><span class="t">${esc(n.title)}</span><span class="k">${esc(ctxLabel(n))}</span><button data-close>close · esc</button></div><div class="card chat" style="flex:1;min-height:0">${chatHTML(n)}</div>`);
    full.querySelector('[data-close]').addEventListener('click', closeFull);
    bindChat(full, n);
  }
  function openFull(id) { fullId = id; full.classList.add('on'); drawFull(); }
  function closeFull() { fullId = null; full.classList.remove('on'); full.replaceChildren(); drawNodes(); }

  function bindChat(root, n) {
    const ta = root.querySelector('[data-draft]'), send = root.querySelector('[data-send]');
    const ms = root.querySelector('[data-model]'), es = root.querySelector('[data-effort]'), rs = root.querySelector('[data-research]'), vs = root.querySelector('[data-voice]');
    const stop = ev => ev.stopPropagation();
    [ta, ms, es, rs, vs].forEach(el => el.addEventListener('mousedown', stop));
    vs.addEventListener('change', async () => {
      if (vs.value === '__add') {
        vs.value = n.voice || '';
        const title = (prompt('name this voice (e.g. "My.BPM", "Andrea — Resonance")') || '').trim(); if (!title) return;
        openPaste(0, 0, 'paste the voice / brand text here — who is speaking, how they sound, what they never say. it becomes a reusable voice for any chat.', {voice: {title, node: n}});
        return;
      }
      const j = await act('canvas.model', {id: n.id, voice: vs.value}); if (j.ok) { n.voice = j.voice || ''; drawNodes(); toast(n.voice ? 'voice: ' + n.voice : 'voice off — plain model'); }
    });
    root.querySelectorAll('.convos, .turns').forEach(el => el.addEventListener('mousedown', stop));
    ta.addEventListener('input', () => { drafts[n.id] = ta.value; });
    ta.addEventListener('keydown', ev => { if ((ev.metaKey || ev.ctrlKey) && ev.key === 'Enter') { ev.preventDefault(); send.click(); } });
    ms.addEventListener('change', async () => { const j = await act('canvas.model', {id: n.id, model: ms.value}); if (j.ok) { n.model = j.model || ms.value; n.effort = j.effort || n.effort; drawNodes(); } });
    es.addEventListener('change', async () => { const j = await act('canvas.model', {id: n.id, effort: es.value}); if (j.ok) n.effort = es.value; });
    rs.addEventListener('change', async () => { const j = await act('canvas.model', {id: n.id, research: rs.checked}); if (j.ok) { n.research = !!j.research; toast(n.research ? 'research on: Claude will search the web before answering' : 'research off'); } });
    send.addEventListener('click', async ev => {
      ev.stopPropagation(); const text = (ta.value || '').trim(); if (!text) return;
      const j = await act('canvas.run_chat', {id: n.id, prompt: text});
      if (j.ok) { ta.value = ''; drafts[n.id] = ''; n.status = 'running'; n.error = null; convo(n).turns.push({role: 'user', text}); drawNodes(); }
    });
    root.querySelectorAll('[data-copy]').forEach(el => el.addEventListener('click', ev => { ev.stopPropagation(); const t = convo(n).turns[+el.dataset.copy]; if (t) navigator.clipboard.writeText(t.text).then(() => toast('copied')); }));
    root.querySelectorAll('[data-unwire]').forEach(el => el.addEventListener('click', async ev => {
      ev.stopPropagation(); const from = el.dataset.unwire;
      const direct = B.edges.some(e => e.from === from && e.to === n.id);
      if (!direct) { toast('that note reaches this chat through another card — cut the wire on the board'); return; }
      const j = await act('canvas.unedge', {from, to: n.id}); if (j.ok) { B.edges = B.edges.filter(e => !(e.from === from && e.to === n.id)); drawNodes(); toast('note unwired'); }
    }));
    bindCopyBlocks(root);
    root.querySelector('[data-newcv]').addEventListener('click', async ev => { ev.stopPropagation(); const j = await act('canvas.convo', {id: n.id, op: 'new'}); if (j.ok && j.node) { Object.assign(n, j.node); drawNodes(); } });
    root.querySelectorAll('[data-cv]').forEach(el => el.addEventListener('click', async ev => {
      ev.stopPropagation(); const cid = el.dataset.cv;
      if (ev.target.dataset.cvren !== undefined) { const c = (n.convos || []).find(x => x.id === cid); const t = prompt('conversation name', c ? c.title : ''); if (!t) return; const j = await act('canvas.convo', {id: n.id, op: 'rename', cid, title: t}); if (j.ok && j.node) { Object.assign(n, j.node); drawNodes(); } return; }
      if (ev.target.dataset.cvdel !== undefined) { if (!confirm('delete this conversation?')) return; const j = await act('canvas.convo', {id: n.id, op: 'delete', cid}); if (j.ok && j.node) { Object.assign(n, j.node); drawNodes(); } return; }
      if (cid === n.active) return; const j = await act('canvas.convo', {id: n.id, op: 'switch', cid}); if (j.ok && j.node) { Object.assign(n, j.node); drawNodes(); }
    }));
    const turns = root.querySelector('[data-turns]'); turns.scrollTop = turns.scrollHeight;
  }

  function bindCard(fo, n) {
    const card = fo.querySelector('.card');
    card.addEventListener('mousedown', () => { selected = n.id; nodesG.querySelectorAll('.card.selected').forEach(c => c.classList.remove('selected')); card.classList.add('selected'); }, true);
    fo.querySelector('[data-head]').addEventListener('mousedown', ev => {
      if (ev.target.dataset.del !== undefined || ev.target.dataset.full !== undefined) return;
      ev.stopPropagation(); const w = toWorld(ev.clientX, ev.clientY);
      dragging = {id: n.id, dx: w.x - n.x, dy: w.y - n.y, fo};
    });
    fo.querySelector('[data-del]').addEventListener('click', async ev => {
      ev.stopPropagation(); if (!confirm(`delete "${n.title}"?`)) return;
      const j = await act('canvas.delete', {id: n.id}); if (j.ok) { B.nodes = B.nodes.filter(x => x.id !== n.id); B.edges = B.edges.filter(e => e.from !== n.id && e.to !== n.id); drawNodes(); }
    });
    const fs = fo.querySelector('[data-full]'); if (fs) fs.addEventListener('click', ev => { ev.stopPropagation(); openFull(n.id); });
    fo.querySelector('[data-port]').addEventListener('mousedown', ev => { ev.stopPropagation(); wiring = {from: n.id}; });
    fo.querySelector('[data-resize]').addEventListener('mousedown', ev => { ev.stopPropagation(); dragging = {id: n.id, resize: true, fo}; });
    card.addEventListener('mouseup', async () => {
      if (wiring && wiring.from !== n.id) {
        const from = wiring.from; wiring = null; rubber.setAttribute('d', '');
        const j = await act('canvas.edge', {from, to: n.id});
        if (j.ok) { if (!B.edges.some(e => e.from === from && e.to === n.id)) B.edges.push({from, to: n.id}); drawNodes(); }
      }
    });
    fo.querySelector('[data-title]').addEventListener('dblclick', async ev => {
      ev.stopPropagation(); const t = prompt('title', n.title); if (t == null || t === n.title) return;
      const j = await act('canvas.edit', {id: n.id, title: t}); if (j.ok) { n.title = t; drawNodes(); }
    });
    fo.querySelectorAll('.body,.turns,.posts,.convos,textarea').forEach(el => el.addEventListener('wheel', ev => { ev.stopPropagation(); }, {passive: true}));
    const ex = fo.querySelector('[data-expand]'); if (ex) ex.addEventListener('click', ev => { ev.stopPropagation(); expanded[n.id] = !expanded[n.id]; if (expanded[n.id] && n.h < 420) { n.h = 420; act('canvas.move', {id: n.id, h: n.h}); } drawNodes(); });
    if (n.type === 'note') {
      const body = fo.querySelector('[data-body]');
      body.addEventListener('dblclick', ev => { ev.stopPropagation(); body.classList.remove('clamp'); body.contentEditable = 'true'; body.classList.add('editing'); body.textContent = n.text || ''; body.focus(); });
      body.addEventListener('blur', async () => { if (body.contentEditable !== 'true') return; body.contentEditable = 'false'; body.classList.remove('editing'); const t = body.textContent; if (t === n.text) return; const j = await act('canvas.edit', {id: n.id, text: t}); if (j.ok) { n.text = t; n.tokens = Math.ceil(t.length / 4); drawNodes(); } });
      body.addEventListener('mousedown', ev => ev.stopPropagation());
    }
    if (n.type === 'profile') {
      const addPost = async (idx, dy) => { const p = (n.posts || [])[idx]; if (!p) return; const j = await act('canvas.add_source', {source: p.url, x: n.x + n.w + 60, y: n.y + dy}); if (j.ok && j.node) { B.nodes.push(j.node); B.edges.push({from: n.id, to: j.node.id}); await act('canvas.edge', {from: n.id, to: j.node.id}); } };
      fo.querySelectorAll('[data-addpost]').forEach(el => el.addEventListener('click', async ev => { ev.stopPropagation(); await addPost(+el.dataset.addpost, 0); drawNodes(); toast('fetching…'); }));
      const all = fo.querySelector('[data-addall]'); if (all) all.addEventListener('click', async ev => { ev.stopPropagation(); if (!confirm(`add all ${(n.posts || []).length} posts as source cards?`)) return; for (let i = 0; i < (n.posts || []).length; i++) await addPost(i, i * 200); drawNodes(); toast('fetching all…'); });
      fo.querySelector('.posts').addEventListener('mousedown', ev => ev.stopPropagation());
    }
    if (n.type === 'chat') bindChat(fo, n);
  }

  // ---------- stage interactions ----------
  stage.addEventListener('mousedown', ev => {
    if (ev.target !== svg && ev.target !== stage) return;
    panning = {x: ev.clientX - view.x, y: ev.clientY - view.y}; stage.classList.add('panning');
    selected = null; nodesG.querySelectorAll('.card.selected').forEach(c => c.classList.remove('selected'));
  });
  window.addEventListener('mousemove', ev => {
    if (dragging) {
      const n = node(dragging.id); if (!n) { dragging = null; return; }
      const w = toWorld(ev.clientX, ev.clientY);
      if (dragging.resize) { n.w = Math.max(220, w.x - n.x); n.h = Math.max(120, w.y - n.y); dragging.fo.setAttribute('width', n.w); dragging.fo.setAttribute('height', n.h); }
      else { n.x = w.x - dragging.dx; n.y = w.y - dragging.dy; dragging.fo.setAttribute('x', n.x); dragging.fo.setAttribute('y', n.y); }
      drawEdges(); return;
    }
    if (wiring) { const a = portOut(node(wiring.from)); const w = toWorld(ev.clientX, ev.clientY); rubber.setAttribute('d', curve(a, w)); return; }
    if (panning) { view.x = ev.clientX - panning.x; view.y = ev.clientY - panning.y; applyView(); }
  });
  window.addEventListener('mouseup', async () => {
    if (dragging) { const n = node(dragging.id); const d = dragging; dragging = null; if (n) { await act('canvas.move', {id: n.id, x: n.x, y: n.y, w: n.w, h: n.h}); if (d.resize) drawNodes(); } }
    if (wiring) { wiring = null; rubber.setAttribute('d', ''); }
    if (panning) { panning = null; stage.classList.remove('panning'); }
  });
  function zoomAt(mx, my, k2) { k2 = Math.min(3, Math.max(0.12, k2)); view.x = mx - (mx - view.x) * (k2 / view.k); view.y = my - (my - view.y) * (k2 / view.k); view.k = k2; applyView(); }
  stage.addEventListener('wheel', ev => {
    ev.preventDefault();
    const r = stage.getBoundingClientRect();
    if (ev.ctrlKey || ev.metaKey || Math.abs(ev.deltaY) > Math.abs(ev.deltaX) * 3 && !ev.shiftKey && ev.deltaMode === 0 && Number.isInteger(ev.deltaY) === false) {
      zoomAt(ev.clientX - r.left, ev.clientY - r.top, view.k * Math.exp(-ev.deltaY * 0.0012));
    } else { view.x -= ev.deltaX; view.y -= ev.deltaY; applyView(); }
  }, {passive: false});
  function fitAll() {
    if (!B.nodes.length) return; const r = stage.getBoundingClientRect();
    const x0 = Math.min(...B.nodes.map(n => n.x)), y0 = Math.min(...B.nodes.map(n => n.y));
    const x1 = Math.max(...B.nodes.map(n => n.x + n.w)), y1 = Math.max(...B.nodes.map(n => n.y + n.h));
    const k = Math.min(3, Math.max(0.12, Math.min((r.width - 160) / (x1 - x0 + 80), (r.height - 100) / (y1 - y0 + 80))));
    view.k = k; view.x = 100 + (r.width - 160 - (x1 - x0) * k) / 2 - x0 * k; view.y = 40 + (r.height - 100 - (y1 - y0) * k) / 2 - y0 * k; applyView();
  }
  document.getElementById('zfit').addEventListener('click', fitAll);
  document.getElementById('zin').addEventListener('click', () => { const r = stage.getBoundingClientRect(); zoomAt(r.width / 2, r.height / 2, view.k * 1.25); });
  document.getElementById('zout').addEventListener('click', () => { const r = stage.getBoundingClientRect(); zoomAt(r.width / 2, r.height / 2, view.k / 1.25); });
  document.getElementById('ztheme').addEventListener('click', () => { const t = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light'; document.documentElement.dataset.theme = t; try { localStorage.setItem('brain_theme', t); } catch (e) {} });
  stage.addEventListener('dblclick', ev => { if (ev.target !== svg && ev.target !== stage) return; const w = toWorld(ev.clientX, ev.clientY); openPaste(w.x, w.y); });

  // ---------- add things (rail + modal) ----------
  const modal = document.getElementById('modal'), pasteTa = document.getElementById('paste');
  let pasteAt = {x: 40, y: 40}, modalMode = null;
  function openPaste(x, y, hint, mode) { pasteAt = {x, y}; modalMode = mode || null; pasteTa.value = ''; pasteTa.placeholder = hint || pasteTa.dataset.ph; document.getElementById('mtitle').textContent = mode && mode.voice ? 'ADD VOICE · ' + mode.voice.title : 'ADD SOURCE'; modal.classList.add('on'); setTimeout(() => pasteTa.focus(), 30); }
  function visibleSpot(fx, fy) { const r = stage.getBoundingClientRect(); return toWorld(r.left + r.width * fx, r.top + r.height * fy); }
  async function addAt(action, args, fx, fy) { const w = visibleSpot(fx, fy); const j = await act(action, Object.assign({x: w.x, y: w.y}, args)); if (j.ok && j.node) { B.nodes.push(j.node); drawNodes(); } return j; }
  document.getElementById('r-chat').addEventListener('click', () => addAt('canvas.add_chat', {}, 0.5, 0.2));
  document.getElementById('r-video').addEventListener('click', () => { const w = visibleSpot(0.16, 0.2); openPaste(w.x, w.y, 'https://www.youtube.com/watch?v=…  ·  a TikTok video URL  ·  one URL per line adds several'); });
  document.getElementById('r-article').addEventListener('click', () => { const w = visibleSpot(0.16, 0.2); openPaste(w.x, w.y, 'https://… an article URL, or a PDF URL'); });
  document.getElementById('r-note').addEventListener('click', () => addAt('canvas.add_note', {text: 'new note — double-click to edit. wire it into a chat and it acts as that chat\'s skill / system prompt.'}, 0.16, 0.55));
  document.getElementById('r-profile').addEventListener('click', async () => {
    const u = (prompt('creator profile — a YouTube channel URL (…/@handle) or a TikTok profile URL (tiktok.com/@handle)') || '').trim(); if (!u) return;
    toast('listing latest posts…'); const j = await addAt('canvas.add_profile', {source: u, limit: 10}, 0.16, 0.2); if (j.ok) toast('profile added — press + on a post to pull its transcript');
  });
  document.getElementById('r-file').addEventListener('click', async () => {
    const p = (prompt('path to a file on this Mac (PDF, .md/.txt, or a video file)') || '').trim(); if (!p) return;
    const w = visibleSpot(0.16, 0.2); const j = await act('canvas.add_source', {source: p, x: w.x, y: w.y}); if (j.ok && j.node) { B.nodes.push(j.node); drawNodes(); toast('fetching…'); }
  });
  document.getElementById('r-voice').addEventListener('click', async () => {
    const p = (prompt('path to a voice note (.m4a / .mp3 / .wav) — transcribed locally with whisper') || '').trim(); if (!p) return;
    const w = visibleSpot(0.16, 0.2); const j = await act('canvas.add_source', {source: p, x: w.x, y: w.y}); if (j.ok && j.node) { B.nodes.push(j.node); drawNodes(); toast('transcribing…'); }
  });
  document.getElementById('pcancel').addEventListener('click', () => modal.classList.remove('on'));
  modal.addEventListener('click', ev => { if (ev.target === modal) modal.classList.remove('on'); });
  pasteTa.addEventListener('keydown', ev => { if ((ev.metaKey || ev.ctrlKey) && ev.key === 'Enter') document.getElementById('pgo').click(); if (ev.key === 'Escape') modal.classList.remove('on'); });
  document.getElementById('pgo').addEventListener('click', async () => {
    const v = pasteTa.value.trim(); if (!v) return; modal.classList.remove('on');
    if (modalMode && modalMode.voice) {
      const {title, node: n} = modalMode.voice; modalMode = null;
      const j = await act('canvas.add_voice', {title, key: title, text: v});
      if (j.ok) { VOICES = j.voices || VOICES; const j2 = await act('canvas.model', {id: n.id, voice: j.voice.key}); if (j2.ok) n.voice = j.voice.key; drawNodes(); toast('voice added: ' + j.voice.title); }
      return;
    }
    const lines = v.split(/\n+/).map(s => s.trim()).filter(Boolean);
    const allUrls = lines.length > 1 && lines.every(s => /^https?:\/\//.test(s));
    const items = allUrls ? lines : [v];
    let y = pasteAt.y;
    for (const item of items) { const j = await act('canvas.add_source', {source: item, x: pasteAt.x, y}); if (j.ok && j.node) { B.nodes.push(j.node); y += 240; } }
    drawNodes(); toast(items.length > 1 ? `${items.length} sources fetching…` : 'fetching…');
  });

  // ---------- board title + picker ----------
  const bt = document.getElementById('btitle');
  bt.addEventListener('click', async () => { const t = prompt('board name', B.title || B.slug); if (!t || t === B.title) return; const j = await act('canvas.board_title', {title: t}); if (j.ok) { B.title = t; bt.textContent = t; document.title = 'canvas · ' + t; } });
  const pick = document.getElementById('boardpick');
  pick.addEventListener('change', () => {
    if (pick.value === '__new') {
      const s = (prompt('new board slug (letters, digits, dashes)') || '').trim().toLowerCase();
      pick.value = B.slug;
      if (!s) return;
      if (!/^[a-z0-9][a-z0-9_-]{0,63}$/.test(s)) { toast('slug: letters, digits, dashes'); return; }
      act('canvas.new_board', {slug: s}).then(j => { if (j.ok) location.href = '/canvas/' + encodeURIComponent(s); });
    } else location.href = '/canvas/' + encodeURIComponent(pick.value);
  });

  // ---------- live refresh ----------
  async function refresh() {
    try {
      const r = await fetch('/canvas/' + encodeURIComponent(B.slug) + '.json', {cache: 'no-store'}); const nb = await r.json();
      if (dragging || wiring) return;
      B = nb; drawNodes();
    } catch (e) { /* ignore */ }
  }
  async function poll() {
    if (!LIVE) return;
    try {
      const r = await fetch('/ping', {cache: 'no-store'}); const j = await r.json();
      if (lastMtime !== null && j.canvas_mtime !== lastMtime) await refresh();
      lastMtime = j.canvas_mtime;
    } catch (e) { /* server away */ }
  }
  setInterval(poll, 1500);

  window.addEventListener('keydown', async ev => {
    const typing = document.activeElement && (document.activeElement.tagName === 'TEXTAREA' || document.activeElement.tagName === 'INPUT' || document.activeElement.tagName === 'SELECT' || document.activeElement.isContentEditable);
    if ((ev.key === 'Delete' || ev.key === 'Backspace') && selected && !typing && !fullId) {
      const n = node(selected); if (!n || !confirm(`delete "${n.title}"?`)) return;
      const j = await act('canvas.delete', {id: n.id}); if (j.ok) { B.nodes = B.nodes.filter(x => x.id !== n.id); B.edges = B.edges.filter(e => e.from !== n.id && e.to !== n.id); selected = null; drawNodes(); }
    }
    if (ev.key === 'Escape') { modal.classList.remove('on'); if (fullId) closeFull(); }
    if (ev.key === 'f' && !typing && !fullId && selected && node(selected) && node(selected).type === 'chat') openFull(selected);
  });

  applyView(); drawNodes();
})();
"""


def render(slug: str) -> str:
    board = cb.load(slug, create=True)
    try:
        import surface_nav as sn
        nav = sn.nav_html(current="canvas", style=True)
    except Exception:
        nav = ""
    data = json.dumps(board, separators=(",", ":")).replace("</", "<\\/")
    models = {k: {"seat": v[0], "default_effort": v[2], "efforts": v[3]} for k, v in cb.MODELS.items()}
    mdata = json.dumps(models, separators=(",", ":")).replace("</", "<\\/")
    vdata = json.dumps(cb.list_voices(), separators=(",", ":")).replace("</", "<\\/")
    import html as _h
    opts = "".join(
        f'<option value="{_h.escape(b["slug"])}"{" selected" if b["slug"] == slug else ""}>'
        f'{_h.escape(str(b["title"]))} · {b["nodes"]}</option>' for b in cb.list_boards()
    ) + '<option value="__new">+ new board…</option>'
    title = _h.escape(str(board.get("title", slug)))
    ph = ("https://www.youtube.com/watch?v=…   ·   an article URL   ·   /path/to/file.pdf   ·   or paste raw text"
          "&#10;one URL per line adds several at once")
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>canvas · {title}</title>
<script>document.documentElement.dataset.theme = (function () {{
  try {{ return localStorage.getItem('brain_theme') || 'dark'; }} catch (e) {{ return 'dark'; }} }})();</script>
<style>
{theme_css()}
{CSS}
</style>
<div class="bar">
  <div><span class="kicker">FARRICE CAIN · AGENTIC OS</span><h1>can<em>vas</em></h1></div>
  <span class="bt" id="btitle" title="click to rename this board">{title}</span>
  <select id="boardpick" title="switch board">{opts}</select>
  <span class="sp"></span>
  {nav}
</div>
<div class="rail">
  <button id="r-chat" class="chat" title="new chat">💬</button>
  <div class="sep"></div>
  <button id="r-video" title="YouTube / TikTok video (paste a link)">▶</button>
  <button id="r-profile" title="creator profile → latest posts">👤</button>
  <button id="r-article" title="article or PDF link">🌐</button>
  <button id="r-file" title="file on this Mac (PDF, text, video)">📄</button>
  <button id="r-voice" title="voice note (local whisper)">🎤</button>
  <div class="sep"></div>
  <button id="r-note" title="note — wire it in as a skill / system prompt">✎</button>
</div>
<div id="stage"><div class="empty" id="empty"><b>an empty board</b>double-click anywhere, or use the rail on the left · paste a YouTube link, a creator profile, an article, a PDF, or raw text<br>then wire it into a chat and ask</div></div>
<div class="zoom"><button id="zfit" title="fit all">⛶</button><button id="zin" title="zoom in">+</button><button id="zout" title="zoom out">−</button><button id="ztheme" title="light / dark">◐</button></div>
<div id="full"></div>
<div id="modal"><div class="box">
  <div class="kicker" id="mtitle">ADD SOURCE</div>
  <textarea id="paste" data-ph="{ph}" placeholder="{ph}"></textarea>
  <div class="row"><button id="pcancel">cancel</button><button id="pgo" class="go">add · ⌘⏎</button></div>
</div></div>
<div class="foot-bar"><span>scroll = pan · ⌘+scroll / pinch = zoom</span><span>drag empty = pan</span><span>drag head = move</span><span>drag ● onto a card = wire</span><span>click wire = cut</span><span>dbl-click empty = add</span><span>⌘⏎ = send</span><span>f = fullscreen chat</span></div>
<div id="toast"></div>
<script id="boarddata" type="application/json">{data}</script>
<script id="modeldata" type="application/json">{mdata}</script>
<script id="voicedata" type="application/json">{vdata}</script>
<script>
{JS}
</script>"""


def write(slug: str) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    html = render(slug)
    out = OUT_DIR / f"{slug}.html"
    out.write_text(html, encoding="utf-8")
    # canvas.html is the Homebase tile target (file:// dual mode, view-only)
    (OUT_DIR / "canvas.html").write_text(html, encoding="utf-8")
    return out


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Render a canvas board to HTML.")
    ap.add_argument("slug", nargs="?", default="demo")
    a = ap.parse_args()
    print(f"→ {write(a.slug)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
