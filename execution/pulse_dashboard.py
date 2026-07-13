#!/usr/bin/env python3
"""Pulse board generator — the operator console (Maestro layer, 2026-07-13).

Reads live system state and renders .agent/pulse/pulse-board.html for
publication as an artifact via /pulse-board. Deterministic; no LLM.

Sources: .agent/missions.jsonl · .agent/cos/goals.json · .agent/jam/taste-ledger.jsonl
         .agent/handoffs (via handoff_store) · .agent/session.lock
"""
import html
import json
import os
import subprocess
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, ".agent", "pulse", "pulse-board.html")


def jsonl(path):
    rows = []
    try:
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    pass
    except OSError:
        pass
    return rows


def esc(s):
    return html.escape(str(s or ""))


def pill(status):
    cls = {"running": "warn", "compiled": "warn", "waiting": "warn",
           "done": "ok", "stopped": "crit", "blocked": "crit"}.get(status, "muted")
    return f'<span class="pill {cls}">{esc(status)}</span>'


def main():
    now = time.strftime("%Y-%m-%d %H:%M")
    missions = jsonl(os.path.join(ROOT, ".agent", "missions.jsonl"))
    # latest state per mission
    latest = {}
    for m in missions:
        latest[m.get("mission", "?")] = m
    active = [m for m in latest.values() if m.get("status") in ("compiled", "running")]
    recent_done = [m for m in latest.values() if m.get("status") == "done"][-6:]

    goals = json.load(open(os.path.join(ROOT, ".agent", "cos", "goals.json"))).get("goals", [])
    sprint = next((g for g in goals if "SPRINT" in (g.get("why") or "")), None)

    taste = jsonl(os.path.join(ROOT, ".agent", "jam", "taste-ledger.jsonl"))

    try:
        due_raw = subprocess.run(["python3", os.path.join(ROOT, "execution", "revenue_tracker.py"), "due"],
                                 capture_output=True, text=True, timeout=20).stdout
        due_count = sum(1 for l in due_raw.splitlines() if l.strip().startswith(("-", "•")))
    except Exception:
        due_raw, due_count = "", 0

    try:
        threads_raw = subprocess.run(["python3", os.path.join(ROOT, "execution", "handoff_store.py"), "list"],
                                     capture_output=True, text=True, timeout=15).stdout
        threads = [l for l in threads_raw.splitlines() if l.strip()][:12]
    except Exception:
        threads = []

    lock = None
    try:
        lock = json.load(open(os.path.join(ROOT, ".agent", "session.lock")))
    except (OSError, ValueError):
        pass

    waiting = [m for m in latest.values() if m.get("tier") in ("T2", "T3") and m.get("status") == "compiled"]

    def mission_rows(ms):
        if not ms:
            return '<tr><td colspan="4" class="empty">none</td></tr>'
        return "\n".join(
            f"<tr><td>{esc(m.get('mission'))}</td><td class='mono'>{esc(m.get('serves'))}</td>"
            f"<td>{esc(m.get('pattern'))}</td><td>{pill(m.get('status'))}</td></tr>"
            for m in ms)

    sprint_html = ""
    if sprint:
        sprint_html = (f'<div class="sprint"><span class="sprint-tag">ACTIVE SPRINT</span>'
                       f'<strong>{esc(sprint.get("target"))}</strong>'
                       f'<span class="muted">goal: {esc(sprint.get("id"))}</span></div>')

    lock_html = (f'<span class="pill warn">lock: {esc(lock["mission"])}</span>' if lock
                 else '<span class="pill ok">tree: single driver</span>')

    body = f"""<title>Antigravity Pulse</title>
<style>
:root {{
  --ground:#f7f7f9; --panel:#ffffff; --ink:#1c1e28; --muted:#6a6d80; --line:#e3e4ec;
  --accent:#5b6ee1; --ok:#3fa96c; --warn:#d99a2b; --crit:#c4554d;
  --mono:"SF Mono",Menlo,Consolas,monospace;
  --display:"Avenir Next",Seravek,"Segoe UI",sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root {{
  --ground:#12141d; --panel:#191c28; --ink:#e8e9f0; --muted:#8b8fa8; --line:#272b3b;
  --accent:#7c8cf0; --ok:#4dbd7f; --warn:#e3ad45; --crit:#d96a61;
}} }}
:root[data-theme="dark"] {{
  --ground:#12141d; --panel:#191c28; --ink:#e8e9f0; --muted:#8b8fa8; --line:#272b3b;
  --accent:#7c8cf0; --ok:#4dbd7f; --warn:#e3ad45; --crit:#d96a61;
}}
:root[data-theme="light"] {{
  --ground:#f7f7f9; --panel:#ffffff; --ink:#1c1e28; --muted:#6a6d80; --line:#e3e4ec;
  --accent:#5b6ee1; --ok:#3fa96c; --warn:#d99a2b; --crit:#c4554d;
}}
body {{ background:var(--ground); color:var(--ink); font:15px/1.5 -apple-system,"Segoe UI",sans-serif;
  margin:0; padding:32px 24px; }}
.wrap {{ max-width:960px; margin:0 auto; display:flex; flex-direction:column; gap:20px; }}
header {{ display:flex; justify-content:space-between; align-items:baseline; gap:12px; flex-wrap:wrap; }}
h1 {{ font-family:var(--display); font-size:22px; font-weight:600; margin:0; letter-spacing:-.01em; }}
h1 b {{ color:var(--accent); font-weight:600; }}
.stamp {{ color:var(--muted); font-family:var(--mono); font-size:12px; }}
.sprint {{ background:var(--panel); border:1px solid var(--accent); border-radius:8px; padding:12px 16px;
  display:flex; gap:12px; align-items:baseline; flex-wrap:wrap; }}
.sprint-tag {{ font-family:var(--mono); font-size:11px; letter-spacing:.08em; color:var(--accent); }}
.tiles {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:12px; }}
.tile {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:14px 16px; }}
.tile .n {{ font-family:var(--mono); font-size:26px; font-variant-numeric:tabular-nums; }}
.tile .l {{ color:var(--muted); font-size:12px; letter-spacing:.04em; text-transform:uppercase; }}
section {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:16px 18px; }}
h2 {{ font-family:var(--display); font-size:13px; letter-spacing:.06em; text-transform:uppercase;
  color:var(--muted); margin:0 0 10px; }}
table {{ width:100%; border-collapse:collapse; font-size:14px; }}
td, th {{ text-align:left; padding:7px 10px 7px 0; border-top:1px solid var(--line); vertical-align:top; }}
tr:first-child td {{ border-top:none; }}
.mono {{ font-family:var(--mono); font-size:12.5px; color:var(--muted); }}
.pill {{ font-family:var(--mono); font-size:11px; padding:2px 8px; border-radius:999px; white-space:nowrap; }}
.pill.ok {{ background:color-mix(in srgb,var(--ok) 15%,transparent); color:var(--ok); }}
.pill.warn {{ background:color-mix(in srgb,var(--warn) 18%,transparent); color:var(--warn); }}
.pill.crit {{ background:color-mix(in srgb,var(--crit) 16%,transparent); color:var(--crit); }}
.pill.muted {{ background:color-mix(in srgb,var(--muted) 14%,transparent); color:var(--muted); }}
.empty {{ color:var(--muted); font-style:italic; }}
pre {{ overflow-x:auto; font-family:var(--mono); font-size:12px; color:var(--muted); margin:0; }}
</style>
<div class="wrap">
<header><h1><b>Antigravity</b> Pulse</h1><div class="stamp">{now} · {lock_html}</div></header>
{sprint_html}
<div class="tiles">
  <div class="tile"><div class="n">{len(active)}</div><div class="l">missions live</div></div>
  <div class="tile"><div class="n">{len(waiting)}</div><div class="l">waiting on Farrice</div></div>
  <div class="tile"><div class="n">{due_count}</div><div class="l">outcomes due</div></div>
  <div class="tile"><div class="n">{len(taste)}</div><div class="l">taste verdicts banked</div></div>
</div>
<section><h2>⚑ Waiting on you</h2><table>{mission_rows(waiting)}</table></section>
<section><h2>Missions — live</h2><table>{mission_rows(active)}</table></section>
<section><h2>Recently closed</h2><table>{mission_rows(recent_done)}</table></section>
<section><h2>Threads (handoff store)</h2><pre>{esc(chr(10).join(threads)) or "none"}</pre></section>
</div>"""

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(body)
    print(f"pulse board → {OUT}")


if __name__ == "__main__":
    main()
