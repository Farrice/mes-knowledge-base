#!/usr/bin/env python3
"""Judging page for Farrice: the Gigi engine run on one scrollable surface.
Reads slides.json + CAROUSEL-BATCH thumbnails (.tmp/gigi-thumbs at lane root) + SEND-PACKAGE.md
+ PIPELINE-READOUT.md and writes .tmp/gigi-judging-page.html (embedded images, no external assets)."""
import base64, html, json, pathlib, re

HERE = pathlib.Path(__file__).parent
LANE = HERE.parents[3]
THUMBS = LANE / ".tmp" / "gigi-thumbs"
OUT = LANE / ".tmp" / "gigi-judging-page.html"

spec = json.load(open(HERE / "slides.json"))


def data_uri(p):
    return "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode()


def md(text):
    """Tiny markdown → HTML: headers, paragraphs, lists, blockquotes, bold, italics, hr."""
    out, para, lst, quote = [], [], None, []

    def flush():
        nonlocal para, lst, quote
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
        if lst:
            out.append(f"<{lst[0]}>" + "".join(f"<li>{inline(i)}</li>" for i in lst[1]) + f"</{lst[0]}>"); lst = None
        if quote:
            out.append("<blockquote>" + "".join(f"<p>{inline(q)}</p>" for q in quote) + "</blockquote>"); quote = []

    def inline(s):
        s = html.escape(s, quote=False)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*(?!\*)(.+?)\*", r"<em>\1</em>", s)
        s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
        return s

    for line in text.splitlines():
        if line.startswith("# "):
            flush(); out.append(f"<h2>{inline(line[2:])}</h2>")
        elif line.startswith("## "):
            flush(); out.append(f"<h3>{inline(line[3:])}</h3>")
        elif line.startswith("### "):
            flush(); out.append(f"<h4>{inline(line[4:])}</h4>")
        elif line.strip() == "---":
            flush(); out.append("<hr>")
        elif line.startswith("> "):
            if para or lst: flush()
            quote.append(line[2:])
        elif line.startswith(">"):
            quote.append("")
        elif re.match(r"^\s*[-*] ", line):
            if para or quote: flush()
            if lst is None or lst[0] != "ul": flush(); lst = ["ul", []]
            lst[1].append(re.sub(r"^\s*[-*] ", "", line))
        elif re.match(r"^\s*\d+\. ", line):
            if para or quote: flush()
            if lst is None or lst[0] != "ol": flush(); lst = ["ol", []]
            lst[1].append(re.sub(r"^\s*\d+\. ", "", line))
        elif line.startswith("|"):
            flush(); out.append(f'<div class="tbl"><code>{html.escape(line)}</code></div>')
        elif not line.strip():
            flush()
        else:
            if quote and not para: quote.append(line)
            else: para.append(line)
    flush()
    # collapse consecutive table rows into a real table
    joined = "\n".join(out)
    def to_table(m):
        rows = [r for r in re.findall(r"<code>(.*?)</code>", m.group(0))]
        rows = [html.unescape(r) for r in rows]
        cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows if not re.match(r"^\|?\s*-{2,}", r)]
        if not cells: return ""
        head = "".join(f"<th>{inline(c)}</th>" for c in cells[0])
        body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in cells[1:])
        return f'<div class="scroll"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'
    joined = re.sub(r'(?:<div class="tbl"><code>.*?</code></div>\n?)+', to_table, joined)
    return joined


send = (HERE / "SEND-PACKAGE.md").read_text()
send = send.split("\n", 1)[1]  # drop the H1; the page has its own
send = re.sub(r"^\*Forwardable.*?\*\n", "", send, flags=re.M)
readout = (HERE / "PIPELINE-READOUT.md").read_text().split("\n", 1)[1]

rows = ""
for c in spec["carousels"]:
    thumbs = ""
    for i in range(1, len(c["slides"]) + 1):
        uri = data_uri(THUMBS / f'{c["slug"]}-{i:02d}.jpg')
        thumbs += f'<button class="thumb" type="button" data-src="{uri}" aria-label="{html.escape(c["title"])} slide {i}"><img src="{uri}" alt="{html.escape(c["title"])}, slide {i}" loading="lazy"></button>'
    rows += (f'<section class="set"><div class="set-head"><div><span class="mono">{c["slug"]}</span> · pairs with video {c["video"]} · keyword <span class="mono">{c["keyword"]}</span></div>'
             f'<h3>{html.escape(c["title"])}</h3></div><div class="strip">{thumbs}</div></section>')

CSS = """
:root{--ground:#f3f3f0;--panel:#fafaf8;--ink:#101010;--muted:#8c8c82;--soft:#555553;--line:#d8d8d3;--accent:#3d5a94;--ok:#3e7d5f;--warn:#a8853e;--crit:#a85454;
--mono:'JetBrains Mono',ui-monospace,"SF Mono",Menlo,Consolas,monospace;--sans:'Helvetica Neue','Neue Haas Grotesk Text Pro',Helvetica,Inter,system-ui,sans-serif;--serif:'Source Serif 4',Georgia,serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ground:#0e0e0d;--panel:#181817;--ink:#fafaf8;--muted:#8c8c82;--soft:#b9b9b2;--line:#2c2c2a;--accent:#7c9fd9;--ok:#6fae8c;--warn:#c9a868;--crit:#c97b73}}
:root[data-theme="dark"]{--ground:#0e0e0d;--panel:#181817;--ink:#fafaf8;--muted:#8c8c82;--soft:#b9b9b2;--line:#2c2c2a;--accent:#7c9fd9;--ok:#6fae8c;--warn:#c9a868;--crit:#c97b73}
*{box-sizing:border-box}body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:1100px;margin:0 auto;padding:48px 28px 96px}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
h1{font-family:var(--serif);font-weight:500;font-size:clamp(34px,5vw,54px);line-height:1.06;letter-spacing:-.015em;margin:14px 0 18px;text-wrap:balance;max-width:20ch}
.lede{font-family:var(--serif);font-size:21px;line-height:1.45;color:var(--soft);max-width:62ch;margin:0 0 10px}
.meta{display:flex;flex-wrap:wrap;gap:10px 22px;margin:22px 0 0;font-family:var(--mono);font-size:12.5px;color:var(--muted)}
.meta b{color:var(--ink);font-weight:500}
nav{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--ground) 88%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line);margin:34px -28px 0;padding:10px 28px;display:flex;gap:22px;flex-wrap:wrap;font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase}
nav a{color:var(--soft);text-decoration:none}nav a:hover,nav a:focus-visible{color:var(--accent);outline:none}
section.block{padding:54px 0 0;border-top:1px solid var(--line);margin-top:54px}
section.block:first-of-type{border-top:0;margin-top:0}
h2{font-family:var(--serif);font-weight:500;font-size:34px;line-height:1.15;letter-spacing:-.01em;margin:6px 0 20px;text-wrap:balance}
h3{font-family:var(--serif);font-weight:500;font-size:23px;line-height:1.25;margin:32px 0 10px;text-wrap:balance}
h4{font-family:var(--sans);font-weight:600;font-size:15px;letter-spacing:.02em;margin:26px 0 8px}
p,li{max-width:68ch}.prose p{margin:0 0 14px}.prose ul,.prose ol{padding-left:22px;margin:0 0 16px}.prose li{margin:0 0 6px}
blockquote{margin:16px 0 20px;padding:18px 22px;background:var(--panel);border-left:2px solid var(--accent);font-family:var(--serif);font-size:17.5px;line-height:1.5}
blockquote p{margin:0 0 10px;max-width:60ch}blockquote p:last-child{margin:0}
hr{border:0;border-top:1px solid var(--line);margin:34px 0}
code{font-family:var(--mono);font-size:.86em;background:var(--panel);padding:1px 5px;border:1px solid var(--line)}
.calls{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin:22px 0 0}
.call{background:var(--panel);border:1px solid var(--line);padding:20px 22px}
.call .n{font-family:var(--mono);font-size:12px;color:var(--accent);letter-spacing:.12em}
.call h4{margin:8px 0 8px;font-size:17px;font-family:var(--serif);font-weight:500}
.call p{font-size:14.5px;color:var(--soft);margin:0}
.call .rec{margin-top:12px;font-size:13.5px;color:var(--ink)}.call .rec b{color:var(--accent);font-weight:600}
.sets{display:flex;flex-direction:column;gap:38px;margin-top:8px}
.set-head{display:flex;flex-direction:column;gap:4px;margin-bottom:12px}.set-head div{font-size:13px;color:var(--muted)}.set-head h3{margin:0}
.mono{font-family:var(--mono);font-size:.92em}
.strip{display:flex;gap:10px;overflow-x:auto;padding:4px 2px 12px;scroll-snap-type:x proximity}
.thumb{flex:none;width:200px;aspect-ratio:4/5;padding:0;border:1px solid var(--line);background:var(--panel);cursor:zoom-in;scroll-snap-align:start}
.thumb img{width:100%;height:100%;display:block;object-fit:cover}
.thumb:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.scroll{overflow-x:auto;margin:14px 0 22px}table{border-collapse:collapse;width:100%;font-size:14px}th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}th{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:500}td{font-variant-numeric:tabular-nums}
.gift{background:var(--panel);border:1px solid var(--line);padding:34px 38px;max-width:820px}
.gift > hr:first-child{display:none}.gift h2{font-size:26px;margin-top:0}.gift h3{font-size:20px}.gift blockquote{background:var(--ground)}
.files{font-family:var(--mono);font-size:13px;line-height:1.7;color:var(--soft)}.files b{color:var(--ink);font-weight:500}
dialog{border:0;padding:0;background:transparent;max-width:min(92vw,720px)}dialog::backdrop{background:rgba(10,10,10,.82)}
dialog img{width:100%;display:block;border:1px solid var(--line)}dialog button{position:fixed;top:14px;right:16px;font-family:var(--mono);font-size:12px;letter-spacing:.1em;background:var(--panel);color:var(--ink);border:1px solid var(--line);padding:8px 12px;cursor:pointer}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
@media (max-width:640px){.wrap{padding:32px 18px 72px}nav{margin:26px -18px 0;padding:10px 18px}.gift{padding:24px 20px}.thumb{width:160px}}
"""

page = f"""<title>Gigi Engine Run</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,500&family=JetBrains+Mono:wght@400;500&display=swap">
<style>{CSS}</style>
<div class="wrap">
<div class="eyebrow">Jen-engine · dry run · Gigi Mironova · 2026-09-01</div>
<h1>The Jen pipeline, pointed at a teammate with three sentences of voice on record.</h1>
<p class="lede">Seven stages ran end to end. What thin context cost was voice confidence, not output. Everything after Stage 1 stands on research and documents, so it is as strong as Jen's would be. Stage 1 is the only stage that needs her, and the pipeline made that visible instead of papering over it.</p>
<div class="meta"><span><b>20</b> videos scripted</span><span><b>10</b> carousels · <b>61</b> slides rendered</span><span><b>$0</b> paid API</span><span><b>3</b> dispatches</span><span>fair-housing lint <b>PASS</b> on every artifact</span><span>Unit 124 live: <b>$299,999 · $620/mo dues</b></span></div>
<nav><a href="#calls">Your three calls</a><a href="#gift">The gift, as Gigi reads it</a><a href="#sets">The ten carousels</a><a href="#readout">Stage readout</a><a href="#files">Files</a></nav>

<section class="block" id="calls">
<div class="eyebrow">Only three things this run could not decide</div>
<h2>Your calls</h2>
<div class="calls">
<div class="call"><div class="n">01 · REGISTER</div><h4>Does "plain-spoken paperwork" read as her?</h4><p>Built from her personal post, her brokerage bio, and two reviews. Calm, exact, no exclamation marks. Her own post has more edge than the deck keeps.</p><div class="rec"><b>Lean:</b> ship as is; edge lives in the dark "pause" slides if she wants more.</div></div>
<div class="call"><div class="n">02 · SEND ORDER</div><h4>Gift first, offer later?</h4><p>The send package carries no ask beyond a screenshot and one sentence. The founding rate is named only after she has posted a few pieces.</p><div class="rec"><b>Lean:</b> yes. Confirm with Jen that showing team work to a teammate is fine before it goes.</div></div>
<div class="call"><div class="n">03 · OPENER</div><h4>Same door, or the five pages?</h4><p>Same door is the strongest hook and only she can post it. Five pages carries no numbers, so it survives a price change.</p><div class="rec"><b>Lean:</b> Same door, once she confirms $299,999 and $620 still hold.</div></div>
</div>
</section>

<section class="block" id="gift">
<div class="eyebrow">Stage 7 · reader-only · zero operator language</div>
<h2>The gift, as Gigi reads it</h2>
<div class="gift prose">{md(send)}</div>
</section>

<section class="block" id="sets">
<div class="eyebrow">Stages 5 and 6 · tap any slide to enlarge</div>
<h2>The ten carousels</h2>
<p>One visual system, keyed to her: warm paper, band navy, one clay mark per slide, her name in the masthead and the brokerage in the footer. Same grammar as the First Home Valley floor; different agent, unmistakably.</p>
<div class="sets">{rows}</div>
</section>

<section class="block" id="readout">
<div class="eyebrow">Operator readout · what the pipeline did and where thin context showed</div>
<h2>Stage readout</h2>
<div class="prose">{md(readout)}</div>
</section>

<section class="block" id="files">
<div class="eyebrow">On disk · lane worktree-gigi-engine-run</div>
<h2>Files</h2>
<div class="files">
<b>_active/clients/gigi-mironova/</b><br>
VOICE.md · BRAIN.md — Stage 1, dry-run lock, confidence labeled<br>
<b>engine/</b><br>
DEMAND-REPORT.md — Stage 2 · PRODUCTION-CALENDAR.md — Stage 3 · SCRIPT-PACK.md — Stage 4 (20 videos + run sheet)<br>
CAROUSEL-SPECS.md + slides.json — Stage 5 · CAROUSEL-BATCH/&lt;slug&gt;/NN.png + review/sheet.png — Stage 6<br>
SEND-PACKAGE.md — Stage 7 · PIPELINE-READOUT.md — this readout<br>
gen_slides.py → render.py → review_sheet.py — regenerate; share_page.py — this page
</div>
</section>
</div>
<dialog id="lb"><button type="button" id="lbx">CLOSE · ESC</button><img id="lbi" alt=""></dialog>
<script>
(function(){{var d=document.getElementById('lb'),im=document.getElementById('lbi');
document.querySelectorAll('.thumb').forEach(function(b){{b.addEventListener('click',function(){{im.src=b.dataset.src;im.alt=b.getAttribute('aria-label');d.showModal();}});}});
document.getElementById('lbx').addEventListener('click',function(){{d.close();}});
d.addEventListener('click',function(e){{if(e.target===d)d.close();}});}})();
</script>
"""
OUT.write_text(page)
print(OUT, OUT.stat().st_size // 1024, "KB")
