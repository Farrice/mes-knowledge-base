#!/usr/bin/env python3
"""
oracle_dashboard.py — Render the Oracle live dashboard (static, $0 to run).

Born 2026-08-06 (Mastery Forge, Farrice: "showing people this terminal on screen
is not how you convince people"). Same deterministic pattern as asset_gallery.py:
read the ledgers on disk, bake a self-contained HTML page, open in a browser.
No server, no API calls, no spend. Re-run to refresh.

Data sources (read-only):
  .agent/paper-trading.json        — the exam ledger (paper bets)
  .agent/bet-tracking.json         — bankroll config + real-bet ledger
  live_trader.check_gate()         — graduation criteria (prospective-only)
  .agent/event-listener-state.json — harness sensing activity
  .agent/mission-queue/            — pending/done mission counts

Output: .agent/oracle/oracle-dashboard.html
Design: Antigravity editorial tokens (templates/research-brief) + dataviz method
(stat tiles, single-hue marks, direct labels, hover layer, honest states).

Usage:
    python3 execution/oracle_dashboard.py            # render
    python3 execution/oracle_dashboard.py --open     # render + open
"""

import argparse
import html
import json
import os
import subprocess
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
OUT_DIR = os.path.join(ROOT, '.agent', 'oracle')
OUT = os.path.join(OUT_DIR, 'oracle-dashboard.html')


def load_json(rel, default=None):
    p = os.path.join(ROOT, rel)
    if os.path.exists(p):
        with open(p) as f:
            return json.load(f)
    return default if default is not None else {}


def payout(bet):
    """P/L for one settled -110-style bet using suggested stake."""
    stake = bet.get('suggested_stake') or bet.get('stake') or 0
    odds = bet.get('odds') or -110
    if bet.get('outcome') == 'win':
        return stake * (100 / abs(odds)) if odds < 0 else stake * (odds / 100)
    if bet.get('outcome') == 'loss':
        return -stake
    return 0.0


def gather():
    paper = load_json('.agent/paper-trading.json', {'bets': [], 'bankroll': {'initial': 1000, 'current': 1000}})
    bets = paper.get('bets', [])
    settled = [b for b in bets if b.get('outcome') is not None]
    prospective = [b for b in settled if not b.get('backfilled')]
    backfilled = [b for b in settled if b.get('backfilled')]

    try:
        from execution.live_trader import check_gate
        passed, gate = check_gate()
    except Exception as e:
        passed, gate = False, {'error': str(e)[:120], 'criteria': {}}

    def curve(pop):
        pts, total = [], 0.0
        for b in pop:
            total += payout(b)
            pts.append(round(total, 2))
        return pts

    conf = {}
    for lvl in (3, 4, 5):
        pop = [b for b in settled if b.get('confidence') == lvl]
        wins = sum(1 for b in pop if b['outcome'] == 'win')
        conf[lvl] = {'n': len(pop), 'hit': round(wins / len(pop) * 100, 1) if pop else None}

    clv_bets = [b for b in settled if b.get('clv') is not None]
    events = load_json('.agent/event-listener-state.json', {})
    pend_dir = os.path.join(ROOT, '.agent/mission-queue/pending')
    done_dir = os.path.join(ROOT, '.agent/mission-queue/done')
    q_pending = len([f for f in os.listdir(pend_dir) if f.endswith('.md')]) if os.path.isdir(pend_dir) else 0
    q_done = len([f for f in os.listdir(done_dir) if f.endswith('.md')]) if os.path.isdir(done_dir) else 0

    wins_p = sum(1 for b in prospective if b['outcome'] == 'win')
    wins_a = sum(1 for b in settled if b['outcome'] == 'win')
    staked = sum((b.get('suggested_stake') or 0) for b in settled) or 1
    net = sum(payout(b) for b in settled)

    return {
        'ts': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'bankroll': paper.get('bankroll', {}),
        'n_all': len(settled), 'n_prosp': len(prospective), 'n_back': len(backfilled),
        'hit_prosp': round(wins_p / len(prospective) * 100, 1) if prospective else 0,
        'hit_all': round(wins_a / len(settled) * 100, 1) if settled else 0,
        'roi': round(net / staked * 100, 1),
        'net': round(net, 2),
        'gate': gate, 'gate_go': passed,
        'curve_all': curve(settled), 'curve_prosp': curve(prospective),
        'conf': conf,
        'clv_n': len(clv_bets),
        'clv_avg': round(sum(b['clv'] for b in clv_bets) / len(clv_bets), 2) if clv_bets else None,
        'recent': settled[-10:][::-1],
        'events_runs': len(events.get('runs', [])),
        'q_pending': q_pending, 'q_done': q_done,
    }


def svg_line(points, svg_id, w=880, h=190, pad=34):
    """Single-series line with area fill + hover crosshair anchors. Returns (svg, js_data)."""
    if len(points) < 2:
        return '<div class="empty">Not enough settled bets to draw yet.</div>', '[]'
    lo, hi = min(points + [0]), max(points + [0])
    span = (hi - lo) or 1
    n = len(points)
    xs = [pad + i * (w - 2 * pad) / (n - 1) for i in range(n)]
    ys = [h - pad - (p - lo) * (h - 2 * pad) / span for p in points]
    path = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in zip(xs, ys))
    area = f'M{xs[0]:.1f},{h - pad} L' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in zip(xs, ys)) + f' L{xs[-1]:.1f},{h - pad} Z'
    zero_y = h - pad - (0 - lo) * (h - 2 * pad) / span
    data = json.dumps([{'x': round(x, 1), 'y': round(y, 1), 'v': p, 'i': i + 1} for i, (x, y, p) in enumerate(zip(xs, ys, points))])
    svg = f'''<svg viewBox="0 0 {w} {h}" class="chart" id="{svg_id}" role="img" aria-label="Cumulative paper profit by bet">
  <line x1="{pad}" y1="{zero_y:.1f}" x2="{w - pad}" y2="{zero_y:.1f}" stroke="var(--ag-line)" stroke-width="1"/>
  <text x="{pad}" y="{zero_y - 6:.1f}" class="axis">$0</text>
  <path d="{area}" fill="var(--ag-accent)" opacity="0.08"/>
  <path d="{path}" fill="none" stroke="var(--ag-accent)" stroke-width="2" stroke-linejoin="round"/>
  <text x="{xs[-1] - 4:.1f}" y="{ys[-1] - 10:.1f}" text-anchor="end" class="dlabel">${points[-1]:+,.0f}</text>
  <line class="crosshair" y1="{pad}" y2="{h - pad}" stroke="var(--ag-line)" stroke-width="1" style="display:none"/>
  <circle class="hoverdot" r="4" fill="var(--ag-accent)" stroke="var(--ag-surface)" stroke-width="2" style="display:none"/>
</svg>'''
    return svg, data


def svg_conf_bars(conf):
    rows = []
    y = 8
    for lvl in (3, 4, 5):
        d = conf[lvl]
        label = f'C{lvl}'
        if d['hit'] is None:
            rows.append(f'<text x="0" y="{y + 15}" class="axis">{label} — no bets</text>')
        else:
            wpx = d['hit'] / 100 * 560
            warn = lvl == 5 and conf[3]['hit'] is not None and d['hit'] < conf[3]['hit']
            fill = 'var(--ag-risk)' if warn else 'var(--ag-accent)'
            rows.append(
                f'<text x="0" y="{y + 16}" class="blabel">{label}</text>'
                f'<rect x="42" y="{y}" width="{wpx:.0f}" height="22" rx="4" fill="{fill}" class="cbar" data-tip="Confidence {lvl}: {d["hit"]}% over {d["n"]} bets"/>'
                f'<text x="{50 + wpx:.0f}" y="{y + 16}" class="dlabel">{d["hit"]}% · {d["n"]} bets</text>')
        y += 34
    gx = 42 + 0.53 * 560
    marker = (f'<line x1="{gx:.0f}" y1="0" x2="{gx:.0f}" y2="{y}" stroke="var(--ag-ink-mute)" stroke-width="1" stroke-dasharray="3,3"/>'
              f'<text x="{gx:.0f}" y="{y + 14}" class="axis" text-anchor="middle">53% gate</text>')
    return f'<svg viewBox="0 0 760 {y + 22}" class="chart" role="img" aria-label="Hit rate by confidence level">{"".join(rows)}{marker}</svg>'


def render(d):
    gate = d['gate']
    crit = gate.get('criteria', {})

    def badge(status):
        cls = {'PASS': 'ok', 'FAIL': 'bad', 'PENDING': 'wait', 'GO': 'ok'}.get(status, 'wait')
        return f'<span class="badge {cls}">{status}</span>'

    labels = {'bet_count': 'Prospective bets', 'hit_rate': 'Hit rate', 'clv': 'Closing Line Value', 'calibration': 'Confidence calibration'}
    cal_rates = (crit.get('calibration', {}) or {}).get('rates') or {}
    details = {
        'bet_count': f"{crit.get('bet_count', {}).get('value', '—')} / 200",
        'hit_rate': f"{crit.get('hit_rate', {}).get('value', '—')}% (need &gt;53%)",
        'clv': f"{crit.get('clv', {}).get('data_points', 0)} data points — capture began 2026-08-06",
        'calibration': ', '.join(f"C{k}={v:.0f}%" for k, v in cal_rates.items() if v) or '—',
    }
    gate_rows = ''
    for key, lab in labels.items():
        st = crit.get(key, {}).get('status', 'PENDING')
        gate_rows += f'<div class="grow"><span class="gk">{lab}</span><span class="gv">{details[key]}</span>{badge(st)}</div>'

    curve_svg, curve_data = svg_line(d['curve_all'], 'svgAll')
    curve_p_svg, curve_p_data = svg_line(d['curve_prosp'], 'svgProsp')
    bars = svg_conf_bars(d['conf'])
    verdict = 'GO — LIVE MODE UNLOCKED' if d['gate_go'] else 'NO-GO — PAPER EXAM IN PROGRESS'
    verdict_cls = 'ok' if d['gate_go'] else 'wait'
    pct = min(100, round(d['n_prosp'] / 200 * 100))

    recent_rows = ''
    for b in d['recent']:
        out = b.get('outcome', '')
        recent_rows += (f"<tr><td>{html.escape(str(b.get('date', '')))[:12]}</td><td>{html.escape(str(b.get('player', '')))}</td>"
                        f"<td>{html.escape(str(b.get('prop', '')))} {html.escape(str(b.get('direction', '')))} {b.get('line', '')}</td>"
                        f"<td class=\"{'win' if out == 'win' else 'loss'}\">{out.upper()}</td>"
                        f"<td>{'backfill' if b.get('backfilled') else 'prospective'}</td></tr>")

    clv_val = f"{d['clv_avg']:+.2f} pts over {d['clv_n']} bets" if d['clv_avg'] is not None else "Capture live as of 2026-08-06 — accrues from the next slate"

    page = f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>THE ORACLE — Mastery Forge Instance #1</title>
<style>
:root{{--ag-ink:oklch(18% 0 0);--ag-paper:oklch(96% 0.003 107);--ag-surface:oklch(98% 0.002 107);
--ag-line:oklch(88% 0.005 107);--ag-accent:oklch(46% 0.084 262);--ag-proof:oklch(48% 0.07 165);
--ag-risk:oklch(52% 0.10 25);--ag-ink-soft:oklch(44% 0.003 110);--ag-ink-mute:oklch(62% 0.012 110);
--sans:'Helvetica Neue',Helvetica,Inter,system-ui,Arial,sans-serif;
--serif:'Source Serif 4',Georgia,serif;--mono:'JetBrains Mono',ui-monospace,'SF Mono',Menlo,monospace}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--ag-paper);color:var(--ag-ink);font-family:var(--sans);padding:38px 20px 80px}}
.wrap{{max-width:960px;margin:0 auto}}
.kicker{{font-family:var(--mono);font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:var(--ag-ink-mute)}}
h1{{font-size:42px;letter-spacing:-.01em;margin:6px 0 2px}} h1 em{{font-family:var(--serif);font-style:italic;font-weight:400;color:var(--ag-accent)}}
.sub{{color:var(--ag-ink-soft);font-size:14px;margin-bottom:8px}}
.chips{{margin:14px 0 26px}} .chip{{display:inline-block;font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;border:1px solid var(--ag-line);border-radius:999px;padding:5px 12px;margin:0 8px 8px 0;color:var(--ag-ink-soft);background:var(--ag-surface)}}
.chip.dark{{opacity:.55}}
.tiles{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin-bottom:26px}}
.tile{{background:var(--ag-surface);border:1px solid var(--ag-line);border-radius:10px;padding:16px 18px}}
.tile .k{{font-family:var(--mono);font-size:8.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--ag-ink-mute);display:block;margin-bottom:7px}}
.tile .v{{font-size:26px;font-weight:700;letter-spacing:-.01em}}
.tile .d{{font-size:11.5px;color:var(--ag-ink-mute);margin-top:4px}}
.panel{{background:var(--ag-surface);border:1px solid var(--ag-line);border-radius:12px;padding:22px 24px;margin-bottom:18px}}
.panel h2{{font-size:17px;margin-bottom:4px}} .panel h2 em{{font-family:var(--serif);font-style:italic;font-weight:400;color:var(--ag-accent)}}
.panel .note{{font-size:12.5px;color:var(--ag-ink-mute);margin-bottom:14px}}
.badge{{font-family:var(--mono);font-size:8px;letter-spacing:.14em;border-radius:3px;padding:3px 8px;font-weight:700}}
.badge.ok{{background:color-mix(in oklab,var(--ag-proof) 14%,white);color:var(--ag-proof)}}
.badge.bad{{background:color-mix(in oklab,var(--ag-risk) 12%,white);color:var(--ag-risk)}}
.badge.wait{{background:var(--ag-paper);color:var(--ag-ink-mute);border:1px solid var(--ag-line)}}
.verdict{{display:flex;align-items:center;gap:12px;margin-bottom:6px}}
.pbar{{height:8px;background:var(--ag-paper);border:1px solid var(--ag-line);border-radius:999px;overflow:hidden;margin:10px 0 16px}}
.pbar i{{display:block;height:100%;width:{pct}%;background:var(--ag-accent);border-radius:999px}}
.grow{{display:flex;align-items:center;gap:12px;padding:9px 0;border-bottom:1px solid var(--ag-line)}}
.grow:last-child{{border-bottom:0}}
.gk{{font-size:13.5px;flex:0 0 210px;font-weight:600}} .gv{{font-size:12.5px;color:var(--ag-ink-soft);flex:1;font-family:var(--mono)}}
.chart{{width:100%;height:auto;display:block}}
.axis{{font:9.5px var(--mono);fill:var(--ag-ink-mute)}}
.dlabel{{font:700 11px var(--mono);fill:var(--ag-ink-soft)}}
.blabel{{font:700 12px var(--sans);fill:var(--ag-ink)}}
.cbar:hover{{opacity:.85;cursor:default}}
.filters{{margin-bottom:10px}}
.fbtn{{font-family:var(--mono);font-size:9.5px;letter-spacing:.12em;text-transform:uppercase;border:1px solid var(--ag-line);background:var(--ag-paper);border-radius:999px;padding:5px 12px;cursor:pointer;color:var(--ag-ink-soft);margin-right:6px}}
.fbtn.on{{background:var(--ag-accent);color:white;border-color:var(--ag-accent)}}
table{{width:100%;border-collapse:collapse;font-size:12.5px}}
th{{font-family:var(--mono);font-size:8.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--ag-ink-mute);text-align:left;padding:6px 8px;border-bottom:1px solid var(--ag-line)}}
td{{padding:7px 8px;border-bottom:1px solid var(--ag-line);color:var(--ag-ink-soft)}}
td.win{{color:var(--ag-proof);font-weight:700}} td.loss{{color:var(--ag-risk);font-weight:700}}
.integrity{{border-left:3px solid var(--ag-accent);padding:12px 16px;background:var(--ag-surface);border-radius:0 10px 10px 0;font-size:13px;color:var(--ag-ink-soft);margin-bottom:18px}}
.empty{{font-size:13px;color:var(--ag-ink-mute);padding:20px 0}}
#tip{{position:fixed;pointer-events:none;background:var(--ag-ink);color:white;font:11px var(--mono);padding:6px 10px;border-radius:6px;display:none;z-index:9}}
footer{{font-family:var(--mono);font-size:10px;letter-spacing:.08em;color:var(--ag-ink-mute);margin-top:28px}}
</style></head><body><div class="wrap">
<div class="kicker">MASTERY FORGE · INSTANCE #1 · RENDERED {d['ts']}</div>
<h1>THE <em>ORACLE</em></h1>
<div class="sub">A forged betting master under a falsifiable graduation exam. It decides; a human executes. Real money stays locked until the gate says GO.</div>
<div class="chips"><span class="chip">MODE: PAPER EXAM</span><span class="chip dark">NBA · DARK UNTIL LATE OCT</span><span class="chip">WNBA · PORT QUEUED</span><span class="chip">KALSHI · LANE QUEUED</span><span class="chip">SENSING: {d['events_runs']} LISTENER RUNS · {d['q_pending']} MISSIONS QUEUED · {d['q_done']} DONE</span></div>

<div class="tiles">
<div class="tile"><span class="k">Paper bankroll</span><span class="v">${d['bankroll'].get('current', 0):,.0f}</span><div class="d">started ${d['bankroll'].get('initial', 0):,.0f}</div></div>
<div class="tile"><span class="k">Net P/L (paper)</span><span class="v">${d['net']:+,.0f}</span><div class="d">ROI {d['roi']:+.1f}% on staked</div></div>
<div class="tile"><span class="k">Hit rate · prospective</span><span class="v">{d['hit_prosp']}%</span><div class="d">{d['n_prosp']} forward-logged bets</div></div>
<div class="tile"><span class="k">Gate progress</span><span class="v">{d['n_prosp']}/200</span><div class="d">{pct}% of the exam sat</div></div>
</div>

<div class="panel"><h2>Graduation <em>gate</em></h2>
<div class="note">Four criteria, all falsifiable. The Oracle earns real-money mode only by passing all four — no override, no vibes.</div>
<div class="verdict"><span class="badge {verdict_cls}">{verdict}</span></div>
<div class="pbar"><i></i></div>
{gate_rows}</div>

<div class="integrity">⚖ <b>Integrity rule:</b> {d['n_back']} of {d['n_all']} historical bets were retroactive backfills. This dashboard and the gate count <b>prospective bets only</b> — a system that grades its own homework with hindsight is lying to you. That refusal is the product.</div>

<div class="panel"><h2>Cumulative paper <em>profit</em></h2>
<div class="note">Ledger order, suggested stakes, -110 style payouts. Hover the line for per-bet values.</div>
<div class="filters"><button class="fbtn on" data-set="all">All settled ({d['n_all']})</button><button class="fbtn" data-set="prosp">Prospective only ({d['n_prosp']})</button></div>
<div id="curveAll">{curve_svg}</div><div id="curveProsp" style="display:none">{curve_p_svg}</div></div>

<div class="panel"><h2>Hit rate by <em>confidence</em></h2>
<div class="note">All settled bets. The exam's honest finding: highest-confidence picks (C5) underperform mid-confidence — flagged red until the calibration layer (Platt scaling) ships and proves itself. The gate's calibration row uses prospective bets only.</div>
{bars}</div>

<div class="panel"><h2>Closing Line <em>Value</em></h2>
<div class="note">The #1 edge indicator: did we beat the number the market closed at?</div>
<div class="grow"><span class="gk">Average CLV</span><span class="gv">{clv_val}</span>{badge(crit.get('clv', {}).get('status', 'PENDING'))}</div></div>

<div class="panel"><h2>Recent <em>bets</em></h2>
<table><tr><th>Date</th><th>Player</th><th>Bet</th><th>Result</th><th>Class</th></tr>{recent_rows}</table></div>

<footer>REFRESH: python3 execution/oracle_dashboard.py --open · $0 TO RUN — READS LOCAL LEDGERS ONLY · ANTIGRAVITY / MASTERY FORGE</footer>
</div><div id="tip"></div>
<script>
const D_ALL={curve_data},D_PROSP={curve_p_data};
const tip=document.getElementById('tip');
function wireCurve(svgId,data){{const box=document.getElementById(svgId);if(!box||!data.length)return;
const dot=box.querySelector('.hoverdot');const ch=box.querySelector('.crosshair');
box.addEventListener('mousemove',e=>{{const r=box.getBoundingClientRect();const sx=(e.clientX-r.left)*(box.viewBox.baseVal.width/r.width);
let best=data[0];for(const p of data){{if(Math.abs(p.x-sx)<Math.abs(best.x-sx))best=p}}
dot.style.display='block';dot.setAttribute('cx',best.x);dot.setAttribute('cy',best.y);
ch.style.display='block';ch.setAttribute('x1',best.x);ch.setAttribute('x2',best.x);
tip.style.display='block';tip.style.left=(e.clientX+14)+'px';tip.style.top=(e.clientY-10)+'px';
tip.textContent='bet #'+best.i+' · cumulative $'+best.v.toLocaleString();}});
box.addEventListener('mouseleave',()=>{{dot.style.display='none';ch.style.display='none';tip.style.display='none'}});}}
wireCurve('svgAll',D_ALL);wireCurve('svgProsp',D_PROSP);
document.querySelectorAll('.fbtn').forEach(b=>b.addEventListener('click',()=>{{
document.querySelectorAll('.fbtn').forEach(x=>x.classList.remove('on'));b.classList.add('on');
const s=b.dataset.set;document.getElementById('curveAll').style.display=s==='all'?'':'none';
document.getElementById('curveProsp').style.display=s==='prosp'?'':'none';}}));
document.querySelectorAll('.cbar').forEach(r=>{{r.addEventListener('mousemove',e=>{{tip.style.display='block';tip.style.left=(e.clientX+14)+'px';tip.style.top=(e.clientY-10)+'px';tip.textContent=r.dataset.tip}});r.addEventListener('mouseleave',()=>tip.style.display='none')}});
</script></body></html>'''
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, 'w') as f:
        f.write(page)
    return OUT


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--open', action='store_true')
    args = p.parse_args()
    d = gather()
    path = render(d)
    print(f"oracle dashboard: {d['n_all']} settled bets ({d['n_prosp']} prospective) → {os.path.relpath(path, ROOT)}")
    if args.open:
        subprocess.run(['open', path], check=False)


if __name__ == '__main__':
    main()
