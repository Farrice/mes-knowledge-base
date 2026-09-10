#!/usr/bin/env python3
"""canvas_render.py — the /canvas page: an infinite whiteboard of nodes (2026-09-10).

Same pattern as brain_graph.py: one self-contained HTML string, board data
embedded, theme from board_theme.py, nav from surface_nav.py, no build step,
no framework. The page talks to pulse_serve over POST /action (canvas.*) and
polls /ping for canvas_mtime so a reply written by a detached `claude -p` run
shows up without a refresh.

    render(slug) -> html        write(slug) -> path (.agent/canvas/<slug>.html)

Interactions (vanilla SVG + foreignObject cards):
    wheel = zoom at cursor · drag empty = pan · drag card head = move
    drag from a card's right port onto another card = wire · click a wire = cut
    double-click empty = paste a URL / path / text → source node
    ⌘/ctrl+Enter in a chat box = send

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
.bar{position:fixed;top:0;left:0;right:0;height:52px;display:flex;align-items:center;gap:14px;padding:0 18px;
  background:color-mix(in srgb,var(--ground) 82%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);z-index:20}
.kicker{font-family:var(--mono);font-size:9px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted)}
.bar h1{font-size:15px;font-weight:500;margin:0;letter-spacing:-.01em}
.bar h1 em{font-style:normal;color:var(--accent)}
.bar select,.bar button{font:inherit;font-size:12px;color:var(--ink);background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:6px 10px}
.bar button{cursor:pointer}.bar button:hover{border-color:var(--accent);color:var(--accent)}
.bar .sp{flex:1}
#stage{position:absolute;inset:0;top:52px;width:100%;height:calc(100% - 52px);cursor:grab;touch-action:none}
#stage.panning{cursor:grabbing}
#stage svg{position:absolute;inset:0}
.edge{fill:none;stroke:var(--accent);stroke-width:2;opacity:.55;cursor:pointer}
.edge:hover{opacity:1;stroke-width:3}
.edge-hit{fill:none;stroke:transparent;stroke-width:14;cursor:pointer}
.rubber{fill:none;stroke:var(--accent);stroke-width:2;stroke-dasharray:6 5;pointer-events:none}
.card{width:100%;height:100%;background:var(--panel);border:1px solid var(--line);border-radius:12px;display:flex;flex-direction:column;
  overflow:visible;box-shadow:0 8px 30px rgba(0,0,0,.25);position:relative}
.card.source{border-top:3px solid var(--ok)}
.card.note{border-top:3px solid var(--warn)}
.card.chat{border-top:3px solid var(--accent)}
.card.running{box-shadow:0 0 0 2px var(--accent),0 8px 30px rgba(0,0,0,.25)}
.card.error{border-color:var(--crit)}
.card.selected{box-shadow:0 0 0 2px var(--ink),0 8px 30px rgba(0,0,0,.25)}
.head{display:flex;align-items:center;gap:8px;padding:8px 10px;cursor:move;user-select:none;border-bottom:1px solid var(--line);min-height:34px;border-radius:12px 12px 0 0}
.head .t{flex:1;font-size:12px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.head .k{font-family:var(--mono);font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.head .x{cursor:pointer;color:var(--muted);font-size:14px;line-height:1;padding:0 2px}.head .x:hover{color:var(--crit)}
.body{flex:1;overflow:auto;padding:8px 10px;font-size:12px;line-height:1.45;color:var(--soft);white-space:pre-wrap;word-break:break-word}
.body.editing{outline:1px solid var(--accent);color:var(--ink)}
.foot{font-family:var(--mono);font-size:9.5px;color:var(--muted);padding:5px 10px;border-top:1px solid var(--line);display:flex;gap:10px;align-items:center;border-radius:0 0 12px 12px}
.foot a{color:var(--accent);text-decoration:none}
.port{position:absolute;right:-9px;top:50%;width:18px;height:18px;border-radius:50%;background:var(--accent);border:2px solid var(--ground);
  cursor:crosshair;transform:translateY(-50%);z-index:3}
.port:hover{transform:translateY(-50%) scale(1.25)}
.port.in{left:-9px;right:auto;background:var(--muted);cursor:default}
.turns{flex:1;overflow:auto;padding:8px 10px;display:flex;flex-direction:column;gap:8px}
.turn{font-size:12px;line-height:1.5;white-space:pre-wrap;word-break:break-word;padding:8px 10px;border-radius:10px;max-width:100%}
.turn.user{background:color-mix(in srgb,var(--accent) 16%,transparent);align-self:flex-end;color:var(--ink)}
.turn.assistant{background:color-mix(in srgb,var(--ink) 5%,transparent);color:var(--soft)}
.turn .m{font-family:var(--mono);font-size:9px;color:var(--muted);margin-top:6px;letter-spacing:.06em}
.compose{display:flex;flex-direction:column;gap:6px;padding:8px 10px;border-top:1px solid var(--line)}
.compose textarea{width:100%;min-height:54px;resize:vertical;font:inherit;font-size:12px;color:var(--ink);background:var(--ground);
  border:1px solid var(--line);border-radius:8px;padding:7px 9px}
.compose .row{display:flex;gap:6px;align-items:center}
.compose select{font:inherit;font-size:11px;color:var(--ink);background:var(--ground);border:1px solid var(--line);border-radius:7px;padding:4px 6px}
.compose .k{font-family:var(--mono);font-size:9px;color:var(--muted);white-space:nowrap}
.compose button{margin-left:auto;font:inherit;font-size:12px;color:var(--ground);background:var(--accent);border:0;border-radius:8px;padding:6px 12px;cursor:pointer}
.compose button:disabled{opacity:.45;cursor:default}
.resize{position:absolute;right:2px;bottom:2px;width:14px;height:14px;cursor:nwse-resize;opacity:.4}
.resize:after{content:"";position:absolute;right:3px;bottom:3px;width:7px;height:7px;border-right:2px solid var(--muted);border-bottom:2px solid var(--muted)}
.err{color:var(--crit);font-size:11px;padding:6px 10px}
.hint{color:var(--muted);font-size:11px}
#modal{position:fixed;inset:0;background:rgba(0,0,0,.45);display:none;align-items:center;justify-content:center;z-index:40}
#modal.on{display:flex}
#modal .box{width:min(640px,92vw);background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px;display:flex;flex-direction:column;gap:10px}
#modal textarea{width:100%;min-height:120px;font:inherit;font-size:13px;color:var(--ink);background:var(--ground);border:1px solid var(--line);border-radius:10px;padding:10px}
#modal .row{display:flex;gap:8px;justify-content:flex-end}
#modal button{font:inherit;font-size:12px;border-radius:8px;padding:7px 14px;cursor:pointer;border:1px solid var(--line);background:var(--ground);color:var(--ink)}
#modal button.go{background:var(--accent);color:var(--ground);border-color:var(--accent)}
.foot-bar{position:fixed;left:0;right:0;bottom:0;padding:6px 18px;font-family:var(--mono);font-size:9.5px;color:var(--muted);letter-spacing:.06em;
  background:color-mix(in srgb,var(--ground) 82%,transparent);border-top:1px solid var(--line);display:flex;gap:16px;z-index:20;flex-wrap:wrap}
#toast{position:fixed;bottom:36px;left:50%;transform:translateX(-50%);background:var(--panel);border:1px solid var(--line);color:var(--ink);
  font-size:12px;padding:8px 14px;border-radius:99px;opacity:0;transition:opacity .2s;pointer-events:none;z-index:30}
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
  const view = {x: 60, y: 30, k: 1};
  try { Object.assign(view, JSON.parse(localStorage.getItem(VIEW_KEY) || '{}')); } catch (e) {}
  const drafts = {};          // chat id → unsent text
  let selected = null, dragging = null, wiring = null, panning = null, lastMtime = null;

  // Escaped-string → DOM. Every dynamic value passed here has been through esc().
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c])); }
  function setHTML(el, markup) { el.replaceChildren(document.createRange().createContextualFragment(markup)); }
  function applyView() { world.setAttribute('transform', `translate(${view.x},${view.y}) scale(${view.k})`); try { localStorage.setItem(VIEW_KEY, JSON.stringify(view)); } catch (e) {} }
  function toWorld(cx, cy) { const r = stage.getBoundingClientRect(); return {x: (cx - r.left - view.x) / view.k, y: (cy - r.top - view.y) / view.k}; }
  function node(id) { return B.nodes.find(n => n.id === id); }
  function toast(m) { const t = document.getElementById('toast'); t.textContent = m; t.classList.add('on'); clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('on'), 2200); }

  async function act(action, args) {
    if (!LIVE) { toast('open this board through the live server (127.0.0.1:8765/canvas) to edit'); return {ok: false}; }
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

  // ---------- nodes ----------
  function ctxLabel(n) {
    const parents = {}; for (const e of B.edges) (parents[e.to] = parents[e.to] || []).push(e.from);
    const seen = new Set(); const st = [...(parents[n.id] || [])];
    while (st.length) { const c = st.pop(); if (seen.has(c) || c === n.id) continue; seen.add(c); st.push(...(parents[c] || [])); }
    let tok = 0, src = 0;
    for (const id of seen) { const m = node(id); if (!m) continue; if (m.type !== 'chat') { tok += m.tokens || 0; src++; } else { for (const t of (m.turns || [])) tok += Math.ceil((t.text || '').length / 4); } }
    return `${src} src · ~${tok.toLocaleString()} tok`;
  }
  function costLabel(t) {
    const plan = t.seat === 'claude' ? 'Claude plan' : (t.seat === 'codex' ? 'ChatGPT plan' : 'metered');
    if (typeof t.cost_usd !== 'number') return plan;
    return t.seat === 'gemini' ? '$' + t.cost_usd.toFixed(4) + ' metered' : '≈$' + t.cost_usd.toFixed(3) + ' est · ' + plan;
  }
  function cardHTML(n) {
    const kind = n.type === 'source' ? (n.kind || 'source') : n.type;
    const status = n.status === 'running' ? ' running' : (n.status === 'error' ? ' error' : '');
    const sel = selected === n.id ? ' selected' : '';
    let inner = '';
    if (n.type === 'chat') {
      const opts = Object.keys(MODELS).map(m => `<option value="${esc(m)}"${m === n.model ? ' selected' : ''}>${esc(m)}</option>`).join('');
      const effs = (MODELS[n.model] ? MODELS[n.model].efforts : ['medium']).map(e => `<option value="${esc(e)}"${e === n.effort ? ' selected' : ''}>${esc(e)}</option>`).join('');
      const turns = (n.turns || []).map(t => {
        const meta = t.role === 'assistant' ? `<div class="m">${esc(t.model)}/${esc(t.effort)} · ${esc(t.seconds)}s · ${costLabel(t)} · ${Number(t.context_tokens || 0).toLocaleString()} ctx tok · ${Number(t.sources || 0)} src</div>` : '';
        return `<div class="turn ${t.role === 'user' ? 'user' : 'assistant'}">${esc(t.text)}${meta}</div>`;
      }).join('');
      const busy = n.status === 'running';
      inner = `<div class="turns" data-turns>${turns || '<div class="hint">wire sources into the left port, then ask.</div>'}</div>
        ${n.error ? `<div class="err">${esc(n.error)}</div>` : ''}
        <div class="compose">
          <textarea data-draft placeholder="${busy ? 'thinking…' : 'ask about everything upstream · ⌘⏎ to send'}"${busy ? ' disabled' : ''}>${esc(drafts[n.id] || '')}</textarea>
          <div class="row"><select data-model>${opts}</select><select data-effort>${effs}</select>
          <span class="k">${esc(ctxLabel(n))}</span>
          <button data-send${busy ? ' disabled' : ''}>${busy ? '…' : 'send'}</button></div>
        </div>`;
    } else {
      const body = n.status === 'running' ? 'fetching…' : (n.text || '');
      const isUrl = /^https?:\/\//.test(n.source || '');
      inner = `<div class="body" data-body>${esc(body.slice(0, 1200))}${body.length > 1200 ? '\n…' : ''}</div>
        ${n.error ? `<div class="err">${esc(n.error)}</div>` : ''}
        <div class="foot"><span>~${Number(n.tokens || 0).toLocaleString()} tok</span>${isUrl ? `<a href="${esc(n.source)}" target="_blank" rel="noopener">open ↗</a>` : ''}${n.type === 'note' ? '<span>dbl-click text to edit</span>' : ''}</div>`;
    }
    return `<div class="card ${esc(n.type)}${status}${sel}" data-id="${esc(n.id)}">
      <div class="head" data-head><span class="k">${esc(kind)}</span><span class="t" data-title title="${esc(n.title)}">${esc(n.title)}</span><span class="x" data-del title="delete">×</span></div>
      ${inner}
      <div class="port in" title="in"></div>
      <div class="port" data-port title="drag onto another node to wire"></div>
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
  }

  function bindCard(fo, n) {
    const card = fo.querySelector('.card');
    card.addEventListener('mousedown', () => { selected = n.id; nodesG.querySelectorAll('.card.selected').forEach(c => c.classList.remove('selected')); card.classList.add('selected'); }, true);
    fo.querySelector('[data-head]').addEventListener('mousedown', ev => {
      if (ev.target.dataset.del !== undefined) return;
      ev.stopPropagation(); const w = toWorld(ev.clientX, ev.clientY);
      dragging = {id: n.id, dx: w.x - n.x, dy: w.y - n.y, fo};
    });
    fo.querySelector('[data-del]').addEventListener('click', async ev => {
      ev.stopPropagation(); if (!confirm(`delete "${n.title}"?`)) return;
      const j = await act('canvas.delete', {id: n.id}); if (j.ok) { B.nodes = B.nodes.filter(x => x.id !== n.id); B.edges = B.edges.filter(e => e.from !== n.id && e.to !== n.id); drawNodes(); }
    });
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
    fo.querySelectorAll('.body,.turns,textarea').forEach(el => el.addEventListener('wheel', ev => { ev.stopPropagation(); }, {passive: true}));
    if (n.type === 'note') {
      const body = fo.querySelector('[data-body]');
      body.addEventListener('dblclick', ev => { ev.stopPropagation(); body.contentEditable = 'true'; body.classList.add('editing'); body.textContent = n.text || ''; body.focus(); });
      body.addEventListener('blur', async () => { if (body.contentEditable !== 'true') return; body.contentEditable = 'false'; body.classList.remove('editing'); const t = body.textContent; if (t === n.text) return; const j = await act('canvas.edit', {id: n.id, text: t}); if (j.ok) { n.text = t; n.tokens = Math.ceil(t.length / 4); drawNodes(); } });
      body.addEventListener('mousedown', ev => ev.stopPropagation());
    }
    if (n.type === 'chat') {
      const ta = fo.querySelector('[data-draft]'), send = fo.querySelector('[data-send]');
      const ms = fo.querySelector('[data-model]'), es = fo.querySelector('[data-effort]');
      ta.addEventListener('mousedown', ev => ev.stopPropagation());
      ta.addEventListener('input', () => { drafts[n.id] = ta.value; });
      ta.addEventListener('keydown', ev => { if ((ev.metaKey || ev.ctrlKey) && ev.key === 'Enter') { ev.preventDefault(); send.click(); } });
      ms.addEventListener('mousedown', ev => ev.stopPropagation()); es.addEventListener('mousedown', ev => ev.stopPropagation());
      ms.addEventListener('change', async () => { const j = await act('canvas.model', {id: n.id, model: ms.value}); if (j.ok) { n.model = j.model || ms.value; n.effort = j.effort || n.effort; drawNodes(); } });
      es.addEventListener('change', async () => { const j = await act('canvas.model', {id: n.id, effort: es.value}); if (j.ok) n.effort = es.value; });
      send.addEventListener('click', async ev => {
        ev.stopPropagation(); const text = (ta.value || '').trim(); if (!text) return;
        const j = await act('canvas.run_chat', {id: n.id, prompt: text});
        if (j.ok) { ta.value = ''; drafts[n.id] = ''; n.status = 'running'; n.error = null; (n.turns = n.turns || []).push({role: 'user', text}); drawNodes(); }
      });
      const turns = fo.querySelector('[data-turns]'); turns.scrollTop = turns.scrollHeight;
    }
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
  stage.addEventListener('wheel', ev => {
    ev.preventDefault();
    const r = stage.getBoundingClientRect(); const mx = ev.clientX - r.left, my = ev.clientY - r.top;
    const k2 = Math.min(3, Math.max(0.15, view.k * Math.exp(-ev.deltaY * 0.0012)));
    view.x = mx - (mx - view.x) * (k2 / view.k); view.y = my - (my - view.y) * (k2 / view.k); view.k = k2; applyView();
  }, {passive: false});
  stage.addEventListener('dblclick', ev => { if (ev.target !== svg && ev.target !== stage) return; const w = toWorld(ev.clientX, ev.clientY); openPaste(w.x, w.y); });

  // ---------- paste modal ----------
  const modal = document.getElementById('modal'), pasteTa = document.getElementById('paste');
  let pasteAt = {x: 40, y: 40};
  function openPaste(x, y) { pasteAt = {x, y}; pasteTa.value = ''; modal.classList.add('on'); setTimeout(() => pasteTa.focus(), 30); }
  function visibleSpot(fx, fy) { const r = stage.getBoundingClientRect(); return toWorld(r.left + r.width * fx, r.top + r.height * fy); }
  document.getElementById('addsrc').addEventListener('click', () => { const w = visibleSpot(0.12, 0.2); openPaste(w.x, w.y); });
  document.getElementById('addchat').addEventListener('click', async () => { const w = visibleSpot(0.5, 0.2); const j = await act('canvas.add_chat', {x: w.x, y: w.y}); if (j.ok && j.node) { B.nodes.push(j.node); drawNodes(); } });
  document.getElementById('addnote').addEventListener('click', async () => { const w = visibleSpot(0.12, 0.55); const j = await act('canvas.add_note', {x: w.x, y: w.y, text: 'new note — double-click to edit'}); if (j.ok && j.node) { B.nodes.push(j.node); drawNodes(); } });
  document.getElementById('pcancel').addEventListener('click', () => modal.classList.remove('on'));
  modal.addEventListener('click', ev => { if (ev.target === modal) modal.classList.remove('on'); });
  pasteTa.addEventListener('keydown', ev => { if ((ev.metaKey || ev.ctrlKey) && ev.key === 'Enter') document.getElementById('pgo').click(); if (ev.key === 'Escape') modal.classList.remove('on'); });
  document.getElementById('pgo').addEventListener('click', async () => {
    const v = pasteTa.value.trim(); if (!v) return; modal.classList.remove('on');
    const lines = v.split(/\n+/).map(s => s.trim()).filter(Boolean);
    const allUrls = lines.length > 1 && lines.every(s => /^https?:\/\//.test(s));
    const items = allUrls ? lines : [v];
    let y = pasteAt.y;
    for (const item of items) { const j = await act('canvas.add_source', {source: item, x: pasteAt.x, y}); if (j.ok && j.node) { B.nodes.push(j.node); y += 200; } }
    drawNodes(); toast(items.length > 1 ? `${items.length} sources fetching…` : 'fetching…');
  });

  // ---------- board picker ----------
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
    if ((ev.key === 'Delete' || ev.key === 'Backspace') && selected && !typing) {
      const n = node(selected); if (!n || !confirm(`delete "${n.title}"?`)) return;
      const j = await act('canvas.delete', {id: n.id}); if (j.ok) { B.nodes = B.nodes.filter(x => x.id !== n.id); B.edges = B.edges.filter(e => e.from !== n.id && e.to !== n.id); selected = null; drawNodes(); }
    }
    if (ev.key === 'Escape') modal.classList.remove('on');
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
    import html as _h
    opts = "".join(
        f'<option value="{_h.escape(b["slug"])}"{" selected" if b["slug"] == slug else ""}>'
        f'{_h.escape(str(b["title"]))} · {b["nodes"]}</option>' for b in cb.list_boards()
    ) + '<option value="__new">+ new board…</option>'
    title = _h.escape(str(board.get("title", slug)))
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
  <select id="boardpick" title="board">{opts}</select>
  <button id="addsrc" title="paste a URL, path, or text">+ source</button>
  <button id="addchat">+ chat</button>
  <button id="addnote">+ note</button>
  <span class="sp"></span>
  {nav}
</div>
<div id="stage"><div class="empty" id="empty"><b>an empty board</b>double-click anywhere · paste a YouTube link, an article, a PDF path, or raw text<br>then wire it into a chat node and ask</div></div>
<div id="modal"><div class="box">
  <div class="kicker">ADD SOURCE</div>
  <textarea id="paste" placeholder="https://www.youtube.com/watch?v=…   ·   an article URL   ·   /path/to/file.pdf   ·   or paste raw text&#10;one URL per line adds several at once"></textarea>
  <div class="row"><button id="pcancel">cancel</button><button id="pgo" class="go">add · ⌘⏎</button></div>
</div></div>
<div class="foot-bar"><span>wheel = zoom</span><span>drag empty = pan</span><span>drag head = move</span><span>drag ● onto a card = wire</span><span>click wire = cut</span><span>dbl-click empty = add</span><span>⌘⏎ = send</span></div>
<div id="toast"></div>
<script id="boarddata" type="application/json">{data}</script>
<script id="modeldata" type="application/json">{mdata}</script>
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
