"""jen_os_page.py: regenerate The Valley OS artifact page (one-page readout of Jen's content system).

  python3 execution/jen_os_page_thumbs.py .tmp/valley-os/thumbs && python3 execution/jen_os_page.py .tmp/valley-os/thumbs .tmp/valley-os/the-valley-os.html

Then publish with the Artifact tool (url of the existing page keeps the link). Codex/Astra: the HTML file IS the
deliverable; leave its path in the DELIVER receipt and the next Claude session republishes to the same URL.

Data (IMPORT-LIST.md #1, 2026-09-09 — the run folder is the state; nothing per-week is hand-edited here):
  <week>/run.yaml          written by build_weeks.py at RENDER (posts, hooks, captions, photos, routing)
  <week>/pipeline-log.md   written by /jen at every step (the receipts shown per week, and the gate)
  06-system/VALLEY-OS-ASSETS.yaml   her assets and where each landed (living file, edited as assets arrive)
"""
import base64, datetime, html, json, pathlib, re, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import run_log  # noqa: E402

T = pathlib.Path(sys.argv[1])
LANE = pathlib.Path(__file__).resolve().parents[1]
JEN = LANE / "_active/clients/jen-listings"
WEEKS = JEN / "04-deliverables/2026-09-06-engine-v2-weeks-1-2"
ASSETS = JEN / "06-system/VALLEY-OS-ASSETS.yaml"
OUT = pathlib.Path(sys.argv[2])
TODAY = datetime.date.today().strftime("%b %-d, %Y")

MISSING = []

def img(name):
    p = T / (name + ".jpg")
    if not p.exists():
        # a render that is not on this tree (e.g. edition-01 lives in a gitignored out/); show a labeled blank, never crash
        MISSING.append(name)
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4 5"><rect width="4" height="5" fill="#C9D4E2"/><text x="2" y="2.6" font-size=".35" text-anchor="middle" fill="#1E3A5F">not rendered</text></svg>'
        return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()
    return "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode()

def esc(s): return html.escape(str(s))

def beats(pid):
    p = WEEKS / "reels" / f"{pid}.json"
    if not p.exists(): return []
    d = json.load(open(p))
    rows = []
    for b in d["beats"]:
        line = re.sub(r"<[^>]+>", " ", b["line"].replace("<br>", " / ")).replace("&#8217;", "’")
        hand = b.get("hand", "").replace("&#8594;", "→").replace("&#8217;", "’")
        rows.append((line, hand, b["secs"], b["zoom"], b["photo"]))
    return rows

# ---------- the runs (one run.yaml per week; the renderer wrote it, /jen wrote the receipts)
RUNS = []
for wdir in sorted(WEEKS.glob("week-of-*")):
    mp = wdir / "run.yaml"
    if not mp.exists():
        continue
    data = run_log.load(mp)
    ok, problems = run_log.check(wdir)
    RUNS.append({"dir": wdir, "folder": wdir.name, "data": data, "receipts": run_log.read_receipts(wdir),
                 "gate": ok, "problems": problems})
if not RUNS:
    raise SystemExit(f"no week-of-*/run.yaml under {WEEKS}; run build_weeks.py first")

SAVED = (RUNS[-1]["dir"] / "saved-replies.txt").read_text().strip()
ASSET = run_log.load(ASSETS)
N_POSTS = sum(len(r["data"].get("posts", [])) for r in RUNS)
N_HERS = sum(1 for p in ASSET["photos"] if not str(p["used"]).startswith("none"))
N_JEN_APPROVED = 0  # her thumbs-up count; flips when a run.yaml carries status: shipped

def post_card(p):
    pid, district = p["id"], p["district"]
    photos = p.get("photos") or []
    hers = bool(photos) and all("(hers" in x for x in photos)
    b = beats(pid)
    slides = int(p.get("slides") or 0)
    if slides:
        gallery = '<div class="slides">' + "".join(f'<img src="{img(pid + "-" + str(i))}" alt="{esc(pid)} slide {i}">' for i in range(1, slides + 1)) + "</div>"
    else:
        gallery = f'<div class="slides"><img class="reelframe" src="{img(p.get("thumb") or pid)}" alt="{esc(pid)} first frame"><div class="reelnote">reel, beat 1 as a still · the mp4 lives in the Drive folder</div></div>'
    beat_html = ""
    if b:
        beat_html = '<h4>the reel, beat by beat</h4><table class="beats"><thead><tr><th>on screen</th><th>hand line</th><th>secs</th><th>move</th></tr></thead><tbody>' + \
            "".join(f"<tr><td>{esc(l)}</td><td>{esc(h)}</td><td class=num>{s}</td><td>{z}</td></tr>" for l, h, s, z, _ in b) + "</tbody></table>"
    ph = "".join(f'<span class="ph">{esc(x)}</span>' for x in dict.fromkeys(photos))
    extras = "".join(f"<p class=\"routing\"><b>{esc(k.replace('_', ' '))}:</b> {esc(p[k])}</p>" for k in ("story", "collab", "first_comment") if p.get(k))
    return f'''
<article class="post" id="{pid}">
  <div class="post-head">
    <span class="chip {esc(district)}">{esc(district)}</span>
    <span class="mono">{esc(p.get("day", ""))}</span>
    <span class="mono dim">{esc(p.get("format_note", p.get("format", "")))}</span>
    <span class="badge {'hers' if hers else 'placeholder'}">{'her photos' if hers else 'placeholder photos'}</span>
  </div>
  <h3 class="hook">{esc(p.get("hook", ""))}</h3>
  {gallery}
  <details>
    <summary>caption, script, routing</summary>
    <h4>caption, as it posts</h4>
    <pre class="caption">{esc(p.get("caption", ""))}</pre>
    {beat_html}
    <h4>when someone writes back</h4>
    <p class="routing">{esc(p.get("reply", ""))}</p>
    {extras}
    <h4>photos on these frames</h4>
    <p class="phlist">{ph}</p>
  </details>
</article>'''

def receipts_html(run):
    rec = run["receipts"]
    if not rec:
        return '<p class="receipts none">no pipeline-log.md yet: this week has not been run through /jen since the run folder became the state (2026-09-09)</p>'
    rows = "".join(
        f'<li class="{"skip" if r["skipped"] else ""}"><b>{esc(r["step"])}</b> {esc(r["text"])}'
        + (f'<span class="why">{esc(r["reason"])}</span>' if r.get("reason") else "") + "</li>" for r in rec)
    gate = '<span class="state used">gate pass</span>' if run["gate"] else \
        f'<span class="state none">gate fail</span> <span class="dim">{esc("; ".join(run["problems"]))}</span>'
    return f'<ol class="receipts">{rows}</ol><p class="gateline">{gate} <span class="mono dim">run.yaml · pipeline-log.md · {esc(run["data"].get("updated", ""))}</span></p>'

weeks_html = ""
for run in RUNS:
    d = run["data"]
    status = d.get("status", "draft")
    weeks_html += f'''
<section class="week">
  <div class="week-head"><h3>{esc(d.get("label", run["folder"]))}</h3><span class="mono dim">{esc(run["folder"])}</span><span class="state {'used' if status in ('shipped','delivered') else 'banked'}">{esc(status)}</span></div>
  <blockquote class="msg"><span class="lbl">the text she gets</span>{esc(d.get("message", ""))}</blockquote>
  <div class="posts">{"".join(post_card(p) for p in d.get("posts", []))}</div>
  <h4>the receipts, this week</h4>
  {receipts_html(run)}
</section>'''

# ---------- her assets (living file)
hers_html = "".join(f'<figure><img src="{img("hers-"+p["file"])}" alt="{esc(p["what"])}"><figcaption><b>{esc(p["what"])}</b><span class="{ "ok" if not str(p["used"]).startswith("none") else "no"}">{esc(p["used"])}</span></figcaption></figure>' for p in ASSET["photos"])
pool_html = "".join(f'<figure><img src="{img("pool-"+p["file"])}" alt="{esc(p["file"])}"><figcaption><b>{esc(p["file"])}</b><span class="{ "ok" if not str(p["used"]).startswith("none") else "no"}">{esc(p["used"])}</span></figcaption></figure>' for p in ASSET["pool"])
memo_rows = "".join(f"<tr><td>{esc(m['memo'])}</td><td>{esc(m['lines'])}</td><td>{esc(m['where'])}</td><td><span class='state'>{esc(m['state'])}</span></td></tr>" for m in ASSET["memos"])
other_rows = "".join(f"<tr><td>{esc(o['asset'])}</td><td><span class='state {str(o['state']).split(',')[0].replace(' ','-')}'>{esc(o['state'])}</span></td><td>{esc(o['note'])}</td></tr>" for o in ASSET["other"])

ED = [("ed01-01-cover","cover"),("ed01-02-laidrey","Laidrey, 7am"),("ed01-03-bothwell","Three Buildings. One Lot."),("ed01-04-what-869k-buys","What $869K Buys Here."),("ed01-05-close","Send Me the Street.")]
EDS = [("ed01-S2-moment-cover","moment"),("ed01-S3-stack-cover","stack"),("ed01-S4-guide-cover","guide"),("ed01-S5-urban-cover","urban"),("ed01-S6-initial-cover","big initial")]
ed_html = "".join(f'<figure><img src="{img(f)}" alt="{esc(c)}"><figcaption>{esc(c)}</figcaption></figure>' for f, c in ED)
eds_html = "".join(f'<figure><img src="{img(f)}" alt="{esc(c)}"><figcaption>{esc(c)}</figcaption></figure>' for f, c in EDS)

STAGES = [
 ("0 · Load", "Eight files, in order, before a word is written: the operating doc, the mix, the vault, her voice profile, the calibration log, the client card, the last pulse, the winners sheet.", "/jen step 0 · LOAD: 8/8", "us"),
 ("1 · Read", "What the account moved on last month decides this week's three slots. Shares come from the extractions, never from taste.", "CONTENT-MIX.md · pulse · outlier audit", "us"),
 ("2 · Research", "Redfin comps and market pages, Freddie Mac rates, CA Dept of Insurance. Read the day of the build, dated, labeled. The realism gate on every topic.", "FACTS.md · RESEARCH-PACK.md", "us"),
 ("3 · Write", "One pen, her seat first. Every hook opens on her or the reader; the number or the house is beat 2. Her verbatim lines are a bank drawn once a week, never a stamp.", "build_weeks.py WEEKS · COPY.md", "us"),
 ("4 · Amplify", "One pen sharpens (Alyssa placement, Luke Iha grip), then the Jen-as-herself check reverts any line she would not say. Plain words with punch.", "AMPLIFY.md in the week folder", "us"),
 ("5 · Check", "Fair-housing lint (hard). Prose classifier (nudge). Stamp-lint: a sentence in two posts of one week fails the week (hard).", "fair_housing_lint.py · prose_classifier.py · jen_stamp_lint.py", "script"),
 ("6 · Render", "Cards, reel stills and the week's run.yaml from one generator family. Photos are placeholders until hers arrive.", "week-of-YYYY-MM-DD/ · run.yaml · PHOTO-SWAP.md", "script"),
 ("7 · Deliver", "This page, read from every week's run.yaml and receipts; then the Sunday folder: files, one text to her, captions, the day plan, the saved replies.", "Drive · Jen · Content Drop / 04", "us"),
 ("Her two moves", "A thumbs-up on the preview (30 seconds). Same-evening replies from the saved replies. Nothing else.", "iMessage · Instagram", "Jen"),
 ("8 · Learn", "Monday pulse of public numbers. First of the month: outlier audit, her four numbers into the funnel, vault rows, one line back to her.", "jen_pulse.py · jen-outlier-audit.md · FUNNEL-MATH.md", "us"),
]
stages_html = "".join(f'''<li><span class="who {w.replace(" ","-")}">{esc(w)}</span><h4>{esc(n)}</h4><p>{esc(d)}</p><code>{esc(f)}</code></li>''' for n, d, f, w in STAGES)

# ---------- gates, from the receipts (never typed here)
gate_rows = []
for run in RUNS:
    wk = run["folder"].replace("week-of-", "week of ")
    if not run["receipts"]:
        gate_rows.append((f"{wk}: run through /jen", "none", "no pipeline-log.md yet; the week was built before the run folder became the state"))
        continue
    for r in run["receipts"]:
        if r["step"] in ("RESEARCH", "AMPLIFY", "CHECK"):
            gate_rows.append((f"{wk}: {r['step'].lower()}", "banked" if r["skipped"] else "used", r["text"]))
    gate_rows.append((f"{wk}: run gate (nine receipts in order + run.yaml)", "used" if run["gate"] else "none",
                      "pass" if run["gate"] else "; ".join(run["problems"])))
facts = WEEKS / "FACTS.md"
if facts.exists():
    n = sum(1 for ln in facts.read_text().split("\n") if ln.startswith("| ") and not ln.startswith("| used in") and not ln.startswith("|---"))
    gate_rows.append(("Facts ledger", "used", f"{n} rows; every number read from Redfin, Freddie Mac, or CDI on the build day, with a re-check date"))
pulse = JEN / "06-system/pulse/latest.md"
if pulse.exists():
    first = pulse.read_text().split("\n")[0].replace("# pulse · ", "")
    gate_rows.append((f"Public pulse ({first.split(' · ')[-1]})", "used", pulse.read_text().split("\n")[2] if len(pulse.read_text().split("\n")) > 2 else ""))
gates_html = "".join(f"<tr><td>{esc(a)}</td><td><span class='state {b}'>{esc({'used': 'pass', 'none': 'not run', 'banked': 'skipped'}[b])}</span></td><td>{esc(c)}</td></tr>" for a, b, c in gate_rows)

PAGE = f'''<title>The Valley OS</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Jost:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{{--ink:#1E3A5F;--steel:#4C7CA8;--cream:#F7F5F2;--paper:#FFFFFF;--rule:#C9D4E2;--slate:#5B6472;--text:#1B2431;--good:#2F7D5B;--warn:#9A6B1F;--bad:#9B3F3F;--chip-attract:#DCE7F2;--chip-position:#E7EEF5;--chip-convert:#EAE5DA;--chip-connect:#E4EFE8;--shadow:0 1px 0 rgba(30,58,95,.06)}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--ink:#DCE6F2;--steel:#8FB3D6;--cream:#141B26;--paper:#1C2532;--rule:#2B3746;--slate:#9AA7B8;--text:#E9EEF4;--good:#6FBF95;--warn:#D8A54A;--bad:#E07A7A;--chip-attract:#243A52;--chip-position:#22313F;--chip-convert:#3A3427;--chip-connect:#22392E;--shadow:none}}}}
:root[data-theme="dark"]{{--ink:#DCE6F2;--steel:#8FB3D6;--cream:#141B26;--paper:#1C2532;--rule:#2B3746;--slate:#9AA7B8;--text:#E9EEF4;--good:#6FBF95;--warn:#D8A54A;--bad:#E07A7A;--chip-attract:#243A52;--chip-position:#22313F;--chip-convert:#3A3427;--chip-connect:#22392E;--shadow:none}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--cream);color:var(--text);font-family:Jost,system-ui,sans-serif;font-weight:400;line-height:1.5;font-size:16px}}
a{{color:var(--steel)}}
.mono{{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:.82rem;color:var(--ink)}}
.dim{{color:var(--slate)}}
h1,h2,h3{{font-family:"Playfair Display",Georgia,serif;font-weight:400;color:var(--ink);text-wrap:balance;margin:0}}
h1{{font-size:clamp(2.2rem,4.5vw,3.4rem);line-height:1.05}}
h2{{font-size:1.9rem;line-height:1.15}}
h3{{font-size:1.25rem}}
h4{{font-family:Jost,sans-serif;font-weight:600;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--slate);margin:1.4rem 0 .5rem}}
nav{{position:sticky;top:0;z-index:5;background:var(--cream);border-bottom:1px solid var(--rule);display:flex;gap:1.4rem;padding:.8rem 1.4rem;overflow-x:auto;font-size:.85rem;font-weight:500;letter-spacing:.04em}}
nav a{{color:var(--ink);text-decoration:none;white-space:nowrap}} nav a:hover,nav a:focus-visible{{color:var(--steel);outline:none;text-decoration:underline}}
main{{max-width:1120px;margin:0 auto;padding:2.5rem 1.4rem 5rem}}
header.hero{{display:grid;grid-template-columns:1.2fr .8fr;gap:2.5rem;align-items:end;padding:1rem 0 2.5rem;border-bottom:1px solid var(--rule)}}
.hero p{{max-width:62ch;font-size:1.05rem;color:var(--slate)}}
.hero .stat{{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}}
.stat div{{background:var(--paper);border:1px solid var(--rule);padding:.9rem 1rem;box-shadow:var(--shadow)}}
.stat b{{display:block;font-family:"Playfair Display",serif;font-weight:400;font-size:1.7rem;color:var(--ink);font-variant-numeric:tabular-nums}}
.stat span{{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--slate)}}
section.block{{padding:3rem 0;border-bottom:1px solid var(--rule)}}
.lede{{max-width:66ch;color:var(--slate);margin:.6rem 0 1.6rem}}
ol.read{{margin:0;padding:0;list-style:none;display:grid;gap:1rem;max-width:78ch}}
ol.read li{{background:var(--paper);border-left:3px solid var(--steel);padding:1rem 1.2rem;box-shadow:var(--shadow)}}
ol.read b{{color:var(--ink)}}
ul.stages{{list-style:none;margin:0;padding:.5rem 0 1rem;display:grid;grid-auto-flow:column;grid-auto-columns:minmax(230px,1fr);gap:.9rem;overflow-x:auto}}
ul.stages li{{background:var(--paper);border:1px solid var(--rule);padding:1rem 1rem 1.1rem;position:relative;box-shadow:var(--shadow)}}
ul.stages li::after{{content:"→";position:absolute;right:-.85rem;top:1rem;color:var(--steel);font-size:1.1rem}}
ul.stages li:last-child::after{{content:"↺";right:.8rem;top:.6rem}}
ul.stages h4{{margin:.4rem 0 .3rem;color:var(--ink);letter-spacing:0;text-transform:none;font-family:"Playfair Display",serif;font-weight:400;font-size:1.15rem}}
ul.stages p{{font-size:.9rem;margin:0 0 .6rem;color:var(--text)}}
ul.stages code{{font-family:"IBM Plex Mono",monospace;font-size:.72rem;color:var(--slate);display:block}}
.who{{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;padding:.15rem .45rem;border:1px solid var(--rule);color:var(--slate)}}
.who.Jen{{border-color:var(--steel);color:var(--steel)}}
.week{{margin-top:2.2rem}}
.week-head{{display:flex;align-items:baseline;gap:1rem;flex-wrap:wrap;margin-bottom:.6rem}}
.msg{{margin:0 0 1.2rem;background:var(--paper);border:1px solid var(--rule);padding:.9rem 1.1rem;font-size:.95rem;max-width:70ch;position:relative;white-space:pre-wrap}}
.msg .lbl{{display:block;font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;color:var(--slate);margin-bottom:.3rem}}
.posts{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.2rem}}
.post{{background:var(--paper);border:1px solid var(--rule);padding:1rem 1rem 1.1rem;box-shadow:var(--shadow);display:flex;flex-direction:column;gap:.6rem}}
.post-head{{display:flex;flex-wrap:wrap;gap:.5rem .8rem;align-items:center}}
.chip{{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;padding:.2rem .55rem;color:var(--ink);font-weight:600}}
.chip.attract{{background:var(--chip-attract)}} .chip.position{{background:var(--chip-position)}} .chip.convert{{background:var(--chip-convert)}} .chip.connect{{background:var(--chip-connect)}}
.badge{{font-size:.68rem;letter-spacing:.06em;padding:.15rem .45rem;border:1px dashed var(--warn);color:var(--warn);margin-left:auto}}
.badge.hers{{border-style:solid;border-color:var(--good);color:var(--good)}}
.hook{{font-size:1.15rem;line-height:1.3}}
.slides{{display:grid;grid-template-columns:repeat(3,1fr);gap:.4rem}}
.slides img{{width:100%;aspect-ratio:4/5;object-fit:cover;display:block;border:1px solid var(--rule)}}
.slides .reelframe{{grid-column:1/2;aspect-ratio:9/16}}
.reelnote{{grid-column:2/4;font-size:.8rem;color:var(--slate);align-self:end}}
details{{border-top:1px solid var(--rule);padding-top:.5rem}}
summary{{cursor:pointer;font-weight:500;color:var(--steel);font-size:.9rem;list-style:none}} summary::-webkit-details-marker{{display:none}} summary::before{{content:"+ ";}} details[open] summary::before{{content:"– ";}}
summary:focus-visible{{outline:2px solid var(--steel);outline-offset:2px}}
pre.caption{{white-space:pre-wrap;font-family:Jost,sans-serif;font-size:.92rem;line-height:1.5;margin:0;background:var(--cream);padding:.9rem 1rem;border:1px solid var(--rule);max-width:64ch}}
table{{border-collapse:collapse;width:100%;font-size:.88rem}}
th{{text-align:left;font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--slate);font-weight:600;padding:.4rem .5rem;border-bottom:1px solid var(--rule)}}
td{{padding:.5rem .5rem;border-bottom:1px solid var(--rule);vertical-align:top}}
td.num{{font-variant-numeric:tabular-nums;font-family:"IBM Plex Mono",monospace;font-size:.8rem}}
.routing{{margin:0;font-size:.9rem}}
.ph{{font-family:"IBM Plex Mono",monospace;font-size:.72rem;background:var(--cream);border:1px solid var(--rule);padding:.1rem .4rem;margin:0 .3rem .3rem 0;display:inline-block}}
ol.receipts{{margin:0;padding:0;list-style:none;display:grid;gap:.25rem;max-width:90ch;font-size:.85rem}}
ol.receipts li{{background:var(--paper);border:1px solid var(--rule);padding:.45rem .7rem;font-family:"IBM Plex Mono",monospace;font-size:.76rem;line-height:1.45;color:var(--text)}}
ol.receipts li b{{color:var(--ink);font-weight:500;margin-right:.5rem}}
ol.receipts li.skip{{color:var(--slate);border-style:dashed}}
ol.receipts .why{{display:block;color:var(--slate);font-family:Jost,sans-serif;font-size:.8rem}}
.receipts.none{{color:var(--bad);font-size:.9rem}}
.gateline{{margin:.5rem 0 0;font-size:.85rem;display:flex;gap:.7rem;align-items:center;flex-wrap:wrap}}
.tablewrap{{overflow-x:auto}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:.8rem;margin-top:.8rem}}
figure{{margin:0}} figure img{{width:100%;aspect-ratio:1;object-fit:cover;display:block;border:1px solid var(--rule)}}
.ed figure img{{aspect-ratio:4/5}}
figcaption{{font-size:.76rem;line-height:1.35;margin-top:.35rem;color:var(--slate)}} figcaption b{{display:block;color:var(--text);font-weight:500}}
figcaption .ok{{color:var(--good)}} figcaption .no{{color:var(--bad)}}
.state{{font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;padding:.15rem .45rem;border:1px solid var(--rule);white-space:nowrap}}
.state.used{{color:var(--good);border-color:var(--good)}} .state.none,.state.not-done{{color:var(--bad);border-color:var(--bad)}} .state.banked,.state.built{{color:var(--warn);border-color:var(--warn)}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:2rem}}
.filemap{{font-family:"IBM Plex Mono",monospace;font-size:.78rem;line-height:1.7;color:var(--slate);background:var(--paper);border:1px solid var(--rule);padding:1rem 1.2rem;overflow-x:auto}}
.filemap b{{color:var(--ink);font-weight:500}}
@media (max-width:820px){{header.hero,.two{{grid-template-columns:1fr}} .slides{{grid-template-columns:repeat(3,1fr)}}}}
@media (prefers-reduced-motion:no-preference){{summary{{transition:color .15s}}}}
</style>

<nav>
  <a href="#read">The honest read</a><a href="#machine">The machine</a><a href="#month">The month</a><a href="#edition">Edition 01</a><a href="#assets">Her assets</a><a href="#gates">Gates</a><a href="#gaps">Against Coffee &amp; Contracts</a><a href="#files">Files</a>
</nav>
<main>
<header class="hero">
  <div>
    <h1>The Valley OS</h1>
    <p>Jen's content system as of {esc(TODAY)}: how it runs, the posts it has produced, which of her own assets it uses, and the places it is not working yet. Every week below is read from its own run folder (run.yaml + the receipts /jen wrote), never typed into this page.</p>
  </div>
  <div class="stat">
    <div><b>{N_POSTS}</b><span>posts built, {len(RUNS)} weeks</span></div>
    <div><b>{N_JEN_APPROVED}</b><span>posted or approved by Jen</span></div>
    <div><b>{N_HERS} / {len(ASSET["photos"])}</b><span>of her photos in use</span></div>
  </div>
</header>

<section class="block" id="read">
  <h2>The honest read</h2>
  <p class="lede">Written Sept 2, kept as the record of why it did not feel like a system that works. The receipts under each week below are the live part.</p>
  <ol class="read">
    <li><b>We ship the system, not the posts.</b> Coffee &amp; Contracts shows a post, then a calendar, then a price. The first build produced funnel math, amendments, a vault, and a contract before anything you could flick through. This page is the correction: posts first.</li>
    <li><b>The cards cannot look like her yet.</b> Every weekly frame runs on a CC0 pool photo or a 360-pixel image of Jen from her old grid. Her twelve real photos are only in Edition 01 and week 1. Drive folder 01 is still empty. The generator is not the problem; the inputs are.</li>
    <li><b>Two generators, two looks.</b> The weekly cards (centered serif over a full-bleed photo) and the editions (six Canva grammars) are not one wardrobe. Whichever you prefer should become the only one.</li>
    <li><b>Her close was in nine of nine captions.</b> “i'm here for you. that's my job.” is her best line, and it had become a template. Fixed for week 1 on Sept 2 and for week 2 on Sept 9 (the stamp-lint receipt under each week is the proof); week 3 still carries it three times until its re-run.</li>
    <li><b>Every re-run hook opens on her or on you, not on the house.</b> Her account's own numbers: life-first hooks beat property-first two to one; every bottom-quartile post led with the property.</li>
    <li><b>Three of five voice memos are unused on the grid.</b> Lipstick remodel, the $80M beach house, the skyline: written, not built.</li>
    <li><b>No Jen since “hated it.”</b> Rebuilds, zero thumbs-up. The system is optimized for operator legibility, not for the two humans who decide: your verdict and her yes.</li>
    <li><b>Zero stories, zero bio change, zero pinned post, zero Insights.</b> Those are the parts of Coffee &amp; Contracts that make the feed feel alive and measurable.</li>
  </ol>
</section>

<section class="block" id="machine">
  <h2>The machine</h2>
  <p class="lede">One front door, <code>/jen</code>, nine steps in a fixed order with a receipt after each, written into the week folder as it runs. Jen appears in exactly one of them.</p>
  <ul class="stages">{stages_html}</ul>
</section>

<section class="block" id="month">
  <h2>The month, as she would see it</h2>
  <p class="lede">Open any card for the caption as it posts, the reel beat by beat, and what happens when someone writes back. The dashed badge means the photos are placeholders from the cleared pool. Under each week: the receipts that week's run left behind, and whether the run gate passes.</p>
  {weeks_html}
  <h4>the saved replies she pastes</h4>
  <pre class="caption">{esc(SAVED)}</pre>
</section>

<section class="block" id="edition">
  <h2>Edition 01, the other lane's surface</h2>
  <p class="lede">The Valley · Tarzana · Edition 01 on the Local Gem grammar, plus one cover per other grammar. Her headshot and her Bothwell photos, researched Tarzana facts, awaiting your verdict.</p>
  <div class="grid ed">{ed_html}</div>
  <h4>the other five grammars</h4>
  <div class="grid ed">{eds_html}</div>
</section>

<section class="block" id="assets">
  <h2>Her assets: used, unused</h2>
  <p class="lede">What we have of hers, and where each piece actually landed. Source: <code>06-system/VALLEY-OS-ASSETS.yaml</code>, edited as assets arrive.</p>
  <h4>her five voice memos (2026-09-01)</h4>
  <div class="tablewrap"><table><thead><tr><th>memo</th><th>her lines</th><th>where it went</th><th>state</th></tr></thead><tbody>{memo_rows}</tbody></table></div>
  <h4>her twelve photos</h4>
  <div class="grid">{hers_html}</div>
  <h4>the placeholder pool the weekly cards actually run on</h4>
  <div class="grid">{pool_html}</div>
  <h4>everything else of hers</h4>
  <div class="tablewrap"><table><thead><tr><th>asset</th><th>state</th><th>note</th></tr></thead><tbody>{other_rows}</tbody></table></div>
</section>

<section class="block" id="gates">
  <h2>Gates and receipts</h2>
  <p class="lede">Every row here comes from a week's pipeline-log.md or from a file on disk. Nothing is typed into this page.</p>
  <div class="tablewrap"><table><thead><tr><th>check</th><th>result</th><th>what it means</th></tr></thead><tbody>{gates_html}</tbody></table></div>
</section>

<section class="block" id="gaps">
  <h2>Against Coffee &amp; Contracts</h2>
  <div class="two">
    <div><h4>they have, we match or beat</h4>
      <div class="tablewrap"><table><tbody>
      <tr><td>Weekly template drop</td><td>Sunday folder, finished posts, her streets, dated facts</td></tr>
      <tr><td>Captions with local nouns</td><td>captions with verified local numbers and her words</td></tr>
      <tr><td>Reel scripts</td><td>photo-motion reels, beats written, rendered</td></tr>
      <tr><td>“5 minutes to post”</td><td>thumbs-up + reply DMs; we post for her once we have access</td></tr>
      <tr><td>Analytics dashboard</td><td>Monday pulse, monthly outlier audit</td></tr>
      </tbody></table></div>
    </div>
    <div><h4>they have, we have not built</h4>
      <div class="tablewrap"><table><tbody>
      <tr><td>Stories, daily</td><td><span class="state none">none</span></td></tr>
      <tr><td>Lead magnet / the valley file</td><td><span class="state none">not rendered</span></td></tr>
      <tr><td>Bio and link-in-bio</td><td><span class="state none">untouched</span></td></tr>
      <tr><td>Two style options shown to her</td><td><span class="state none">not yet</span></td></tr>
      <tr><td>Insights-based numbers</td><td><span class="state none">no access</span></td></tr>
      <tr><td>Trending audio at post time</td><td><span class="state banked">optional</span></td></tr>
      </tbody></table></div>
    </div>
  </div>
</section>

<section class="block" id="files">
  <h2>Where everything lives</h2>
  <div class="filemap">
<b>_active/clients/jen-listings/</b><br>
&nbsp;&nbsp;06-system/ENGINE-V2.md &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the operating doc (four districts, rhythm, scoreboard)<br>
&nbsp;&nbsp;06-system/VAULT.md &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;every asset by district, with status<br>
&nbsp;&nbsp;06-system/VALLEY-OS-ASSETS.yaml &nbsp;her assets, used / unused (this page reads it)<br>
&nbsp;&nbsp;06-system/FUNNEL-MATH.md &nbsp;&nbsp;&nbsp;&nbsp;operator only; placeholders until her four numbers<br>
&nbsp;&nbsp;06-system/pulse/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weekly public numbers (jen_pulse.py)<br>
&nbsp;&nbsp;06-system/valley-editions/ &nbsp;&nbsp;DESIGN.md · CANVA-GRAMMAR.md · editions.py · photos/jen/<br>
&nbsp;&nbsp;04-deliverables/2026-09-06-engine-v2-weeks-1-2/ &nbsp;build_weeks.py · FACTS.md · PHOTO-SWAP.md · week-of-*/ (run.yaml · pipeline-log.md · COPY.md · captions.txt · day-plan.txt)<br>
&nbsp;&nbsp;04-deliverables/connect-posts-01/COPY.md &nbsp;four Connect posts, three still unbuilt<br>
&nbsp;&nbsp;04-deliverables/jen-outlier-audit.md<br>
<b>execution/run_log.py</b> &nbsp;receipt · manifest · check (the run folder is the state; same commands on Claude and Codex)<br>
<b>execution/jen_pulse.py</b>
  </div>
</section>
</main>'''

OUT.write_text(PAGE)
print(len(PAGE) // 1024, "KB ·", len(RUNS), "weeks ·", N_POSTS, "posts ·", "missing thumbs:", ", ".join(MISSING) or "none")
