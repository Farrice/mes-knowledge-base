#!/usr/bin/env python3
"""build_page.py: STUDY.md → a one-page readout (Readout OS look: ink + steel blue, Playfair + Jost, the table scrolls in its own box).
  python3 build_page.py            # writes ../../../../../.tmp/valley-os/ca-five-structure-study.html
Deterministic; no library. Publish with the Artifact tool.
"""
import html, pathlib, re

HERE = pathlib.Path(__file__).parent
SRC = (HERE / "STUDY.md").read_text()
OUT = pathlib.Path(__file__).resolve().parents[5] / ".tmp/valley-os/ca-five-structure-study.html"
OUT.parent.mkdir(parents=True, exist_ok=True)


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    return s


def convert(md):
    out, i, lines = [], 0, md.split("\n")
    while i < len(lines):
        l = lines[i]
        if l.startswith("# "):
            out.append(f"<h1>{inline(l[2:])}</h1>")
        elif l.startswith("## "):
            t = l[3:]
            out.append(f'<h2 id="{re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")}">{inline(t)}</h2>')
        elif l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i]); i += 1
            head = [c.strip() for c in rows[0].strip("|").split("|")]
            body = [[c.strip() for c in r.strip("|").split("|")] for r in rows[2:]]
            cls = "wide" if len(head) >= 8 else "narrow"
            t = f'<div class="tablewrap {cls}"><table><thead><tr>' + "".join(f"<th>{inline(h)}</th>" for h in head) + "</tr></thead><tbody>"
            for r in body:
                t += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
            out.append(t + "</tbody></table></div>")
            continue
        elif l.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(lines[i][2:]); i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue
        elif re.match(r"^\d+\. ", l):
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                items.append(re.sub(r"^\d+\. ", "", lines[i])); i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>")
            continue
        elif l.startswith("**Card "):
            title, _, rest = l.partition("**\n") if "**\n" in l else (l.strip("*"), "", "")
            m = re.match(r"\*\*(Card \d · [^*]+)\*\* \(([^)]+)\)", l)
            if not m:
                # section 6: a full-copy card header; the paragraphs that follow render as normal text
                out.append(f'<h3 class="copyhead">{inline(l.strip("*"))}</h3>')
                i += 1
                continue
            body = lines[i + 1] if i + 1 < len(lines) else ""
            i += 1
            parts = [p.strip() for p in re.split(r"(?<=[.\"\u201d]) (?=(?:Format|Hook formula|Beat map|CTA|Jen ICP angle):)", body)]
            pairs = []
            for p in parts:
                m2 = re.match(r"(Format|Hook formula|Beat map|CTA|Jen ICP angle):\s*(.*)", p, re.S)
                if m2:
                    pairs.append([m2.group(1), m2.group(2)])
                elif pairs:
                    pairs[-1][1] += " " + p   # never drop a sentence; glue it to the previous field
            dl = "".join(f"<div><dt>{inline(k)}</dt><dd>{inline(v)}</dd></div>" for k, v in pairs)
            out.append(f'<section class="card"><h3>{inline(m.group(1))}</h3><span class="src">{inline(m.group(2))}</span><dl>{dl}</dl></section>')
        elif l.strip():
            out.append(f"<p>{inline(l)}</p>")
        i += 1
    return "\n".join(out)


CSS = """
:root{--ink:#1E2430;--paper:#F5F6F8;--steel:#1E3A5F;--steel-2:#3D6B9E;--mist:#C9D4E2;--muted:#6B7684;--line:#DDE3EA;--card:#FFFFFF}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--ink:#E8ECF1;--paper:#141920;--steel:#C9D4E2;--steel-2:#7FA6D1;--mist:#2A3543;--muted:#9AA6B5;--line:#2A3340;--card:#1B222C}}
:root[data-theme="dark"]{--ink:#E8ECF1;--paper:#141920;--steel:#C9D4E2;--steel-2:#7FA6D1;--mist:#2A3543;--muted:#9AA6B5;--line:#2A3340;--card:#1B222C}
body{background:var(--paper);color:var(--ink);font-family:Jost,system-ui,sans-serif;font-size:15px;line-height:1.55;margin:0}
main{max-width:1080px;margin:0 auto;padding:2.5rem 1.5rem 5rem}
h1{font-family:'Playfair Display',Georgia,serif;font-weight:400;font-size:2.4rem;line-height:1.1;letter-spacing:-.01em;margin:0 0 .4rem;text-wrap:balance}
h2{font-family:'Playfair Display',Georgia,serif;font-weight:400;font-size:1.5rem;margin:2.6rem 0 .8rem;color:var(--steel);text-wrap:balance}
h3{font-family:'Playfair Display',Georgia,serif;font-weight:400;font-size:1.2rem;margin:0}
p{max-width:68ch;margin:.6rem 0}
ul,ol{max-width:72ch;padding-left:1.3rem;margin:.6rem 0}
li{margin:.35rem 0}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.86em;background:var(--mist);color:var(--ink);padding:.05em .35em;border-radius:3px}
b{font-weight:500;color:var(--steel)}
.tablewrap{overflow-x:auto;border:1px solid var(--line);background:var(--card);margin:1rem 0}
table{border-collapse:collapse;font-size:13.5px;min-width:100%}
.wide table{min-width:1700px}
th{font-family:Jost,sans-serif;font-weight:500;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);text-align:left;padding:.7rem .7rem;border-bottom:1px solid var(--line);background:var(--card);position:sticky;top:0}
td{vertical-align:top;padding:.7rem .7rem;border-bottom:1px solid var(--line);line-height:1.45;font-variant-numeric:tabular-nums}
.wide td:first-child{font-weight:500;min-width:190px}
.wide td:nth-child(9){text-align:center;font-size:1.05rem;color:var(--steel)}
.card{background:var(--card);border-left:3px solid var(--steel-2);padding:1rem 1.2rem;margin:1rem 0;max-width:80ch}
.card .src{display:block;font-size:12px;color:var(--muted);letter-spacing:.04em;margin:.2rem 0 .7rem}
.card dl{margin:0;display:grid;gap:.45rem}
.card dl div{display:grid;grid-template-columns:120px 1fr;gap:.8rem}
.card dt{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding-top:.15em}
.card dd{margin:0}
nav{display:flex;flex-wrap:wrap;gap:.3rem 1.1rem;font-size:13px;margin:1.2rem 0 2rem;padding-bottom:1rem;border-bottom:1px solid var(--line)}
nav a{color:var(--steel-2);text-decoration:none}
nav a:hover,nav a:focus-visible{text-decoration:underline;outline:none}
.copyhead{margin:2rem 0 .5rem;color:var(--steel);border-top:1px solid var(--line);padding-top:1.2rem}
.lede{color:var(--muted);max-width:70ch;margin:0 0 .5rem}
@media (max-width:640px){.card dl div{grid-template-columns:1fr}}
"""

NAV = '<nav><a href="#the-table">The table</a><a href="#1-top-5-hook-formulas-ranked-by-how-often-they-appear-across-the-48-reels-on-the-four-live-reels-tabs">Hook formulas</a><a href="#2-top-3-cta-patterns">CTA patterns</a><a href="#3-the-proof-post-pattern-closings-and-process-without-bragging">Proof pattern</a><a href="#4-what-not-to-copy-for-a-warm-valley-brand">What not to copy</a><a href="#5-five-structure-cards">Structure cards</a><a href="#what-this-says-about-post-11">Post 11</a><a href="#credits-and-gaps">Credits and gaps</a></nav>'

body = convert(SRC)
body = body.replace("</h1>", "</h1>" + NAV, 1)
page = f'''<title>CA Five Structure Study</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500&family=Playfair+Display:ital,wght@0,400;1,400&display=swap">
<style>{CSS}</style>
<main>{body}</main>'''
OUT.write_text(page)
print(OUT, len(page) // 1024, "KB")
