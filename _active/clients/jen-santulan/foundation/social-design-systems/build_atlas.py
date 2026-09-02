#!/usr/bin/env python3
import base64
import html
import io
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "systems.json").read_text())

ORDER = [
    "after-hours-guide",
    "sunlit-local-notes",
    "quiet-home-editorial",
    "valley-moments",
    "hidden-address-journal",
]

WHY = {
    "after-hours-guide": "Scale creates authority: one oversized editorial thought turns an ordinary place image into a point of view. Warm darkness makes unrelated locations feel like one collected issue.",
    "sunlit-local-notes": "A repeatable yellow signal and purposeful hand marks make the deck feel noticed by a person. The imperfect annotation layer creates affinity without sacrificing hierarchy.",
    "quiet-home-editorial": "It trusts one human image and one earned sentence. Quiet mastheads and negative space make Jen feel present, mature, and more credible than a conventional quote card.",
    "valley-moments": "Bold sans supplies speed; script supplies feeling. Rules and footer furniture make the deck feel contemporary and serialized while the images carry movement.",
    "hidden-address-journal": "Edition language makes the series collectible. Inset frames act as evidence, while one warm arrow or smile prevents the vintage treatment from becoming precious.",
}


def data_uri(path: Path, max_width: int = 1100, quality: int = 84) -> str:
    image = Image.open(path).convert("RGB")
    if image.width > max_width:
        height = round(image.height * max_width / image.width)
        image = image.resize((max_width, height), Image.Resampling.LANCZOS)
    payload = io.BytesIO()
    image.save(payload, "JPEG", quality=quality, optimize=True)
    return f"data:image/jpeg;base64,{base64.b64encode(payload.getvalue()).decode()}"


def proof_strip(system: str) -> str:
    images = []
    for path in sorted((ROOT / "proofs" / system).glob("slide-*.png"))[:3]:
        images.append(f'<img src="{data_uri(path, max_width=540, quality=86)}" alt="{html.escape(system)} proof slide">')
    return "".join(images)


sections = []
for number, system_id in enumerate(ORDER, start=1):
    system = DATA["systems"][system_id]
    route = next(item for item in DATA["router"] if item["system"] == system_id)
    ref = ROOT / "references" / f"{number:02d}-{system_id}-reference.jpg"
    palette = "".join(
        f'<span class="swatch" style="--c:{value}"><i></i>{html.escape(role)}<b>{value}</b></span>'
        for role, value in system["palette"].items()
    )
    jobs = "".join(f"<li>{html.escape(job)}</li>" for job in route["use_for"])
    avoid = "".join(f"<li>{html.escape(job)}</li>" for job in route["avoid_for"])
    sections.append(f'''
      <section class="system" id="{system_id}">
        <div class="system-head">
          <div><span class="num">0{number}</span><p>{html.escape(system["reference"])}</p></div>
          <h2>{html.escape(system["name"])}</h2>
          <p class="vibe">{html.escape(system["vibe"])}</p>
        </div>
        <div class="visual-grid">
          <figure><figcaption>Source grammar · supplied references</figcaption><img class="reference" src="{data_uri(ref)}" alt="Reference contact sheet"></figure>
          <figure><figcaption>Transfer proof · Jen and Valley imagery</figcaption><div class="proofs">{proof_strip(system_id)}</div></figure>
        </div>
        <div class="analysis-grid">
          <article><h3>Why it works</h3><p>{html.escape(WHY[system_id])}</p></article>
          <article><h3>Best content jobs</h3><ul>{jobs}</ul></article>
          <article><h3>Do not use for</h3><ul>{avoid}</ul></article>
        </div>
        <div class="tokens">
          <h3>Portable visual grammar</h3>
          <div class="swatches">{palette}</div>
          <dl>
            <dt>Headline</dt><dd>{html.escape(system["typography"]["headline"])}</dd>
            <dt>Composition</dt><dd>{html.escape(system["composition"])}</dd>
            <dt>Photography</dt><dd>{html.escape(system["photo_style"])}</dd>
          </dl>
        </div>
      </section>''')

doc = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Jen Social Design Library</title>
<style>
  :root{{--ink:#151511;--paper:#f2eee6;--sun:#f2d65c;--muted:#6f6b62;--line:#cfc8bb}}
  *{{box-sizing:border-box}} body{{margin:0;background:var(--paper);color:var(--ink);font-family:Inter,"Avenir Next",Arial,sans-serif}}
  .hero{{min-height:92vh;padding:7vw;display:grid;grid-template-columns:1.2fr .8fr;gap:6vw;align-items:end;background:#10110e;color:#f8f4ea}}
  .eyebrow,.status,.num,figcaption,h3,dt{{font-size:12px;line-height:1.2;letter-spacing:.16em;text-transform:uppercase}}
  .hero h1{{font-family:"Bodoni 72",Didot,serif;font-size:clamp(72px,11vw,180px);font-weight:400;line-height:.78;letter-spacing:-.055em;margin:22px 0}}
  .hero h1 em{{color:var(--sun);font-weight:400}} .hero .lead{{font-family:"Bodoni 72",Didot,serif;font-size:28px;line-height:1.35;max-width:620px}}
  .status{{border-top:1px solid #55564d;padding-top:22px;color:#d4d0c7}} .status b{{display:block;color:var(--sun);font-size:24px;letter-spacing:0;text-transform:none;margin:8px 0 28px}}
  .summary{{padding:80px 7vw;display:grid;grid-template-columns:.8fr 1.2fr;gap:8vw;border-bottom:1px solid var(--line)}}
  .summary h2,.system h2{{font-family:"Bodoni 72",Didot,serif;font-weight:400;letter-spacing:-.04em}}
  .summary h2{{font-size:54px;margin:0}} .summary p{{font-size:20px;line-height:1.6;margin:0}}
  .system{{padding:100px 7vw;border-bottom:1px solid var(--line)}} .system-head{{display:grid;grid-template-columns:.5fr 1fr 1.2fr;gap:4vw;align-items:start}}
  .num{{font-size:15px;color:var(--muted)}} .system-head>div p{{font-size:12px;line-height:1.5;color:var(--muted);max-width:240px}}
  .system h2{{font-size:72px;line-height:.95;margin:0}} .vibe{{font-family:"Bodoni 72",Didot,serif;font-size:25px;line-height:1.4;margin:0}}
  .visual-grid{{margin-top:60px;display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start}} figure{{margin:0}} figcaption{{margin-bottom:12px;color:var(--muted)}}
  .reference{{display:block;width:100%;max-height:650px;object-fit:contain;object-position:top;background:#ddd8cf}}
  .proofs{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;background:#111;padding:8px}} .proofs img{{display:block;width:100%;height:auto}}
  .analysis-grid{{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:22px;margin-top:28px}} article,.tokens{{border-top:1px solid var(--ink);padding-top:14px}}
  article p,article li,dd{{font-size:15px;line-height:1.55}} article ul{{padding-left:18px;margin:0}} h3{{margin:0 0 12px}}
  .tokens{{margin-top:36px}} .swatches{{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 28px}} .swatch{{display:grid;grid-template-columns:28px 1fr;gap:3px 8px;align-items:center;font-size:12px;min-width:150px}}
  .swatch i{{grid-row:1/3;width:28px;height:40px;background:var(--c);border:1px solid #aaa}} .swatch b{{font-weight:400;color:var(--muted)}} dl{{display:grid;grid-template-columns:150px 1fr;gap:12px 20px;margin:0}} dt{{padding-top:4px}} dd{{margin:0}}
  .close{{padding:90px 7vw;background:#10110e;color:#f8f4ea;display:grid;grid-template-columns:1fr 1fr;gap:8vw}} .close h2{{font-family:"Bodoni 72",Didot,serif;font-size:58px;font-weight:400;margin:0}} .close p{{font-size:18px;line-height:1.6;margin:0}}
  @media(max-width:900px){{.hero,.summary,.system-head,.visual-grid,.analysis-grid,.close{{grid-template-columns:1fr}}.hero{{min-height:auto;padding:70px 25px}}.system,.summary{{padding:70px 25px}}.system h2{{font-size:52px}}.proofs{{overflow:auto}}dl{{grid-template-columns:1fr}}}}
</style></head><body>
<header class="hero"><div><span class="eyebrow">Jen Santulan · Social Design Library</span><h1>Five styles.<br><em>Five systems.</em></h1><p class="lead">A repeatable visual library harvested from 27 supplied reference slides—built so the vibe survives when the subject becomes Jen, the Valley, a listing, or a real buyer question.</p></div><div class="status">Direction proof<b>5 systems · 15 transfer slides</b>Source visuals verified<br>Typography analogues labeled<br>No publishing authorized</div></header>
<section class="summary"><h2>Separate engines.<br>One Jen layer.</h2><p>Each reference keeps its own palette, type behavior, photography, motifs, and slide rhythm. Only identity, voice, accessibility, sourcing, fair-housing safety, and human approval are shared. That preserves the range Farrice liked while preventing the account from feeling like five unrelated template packs.</p></section>
{''.join(sections)}
<footer class="close"><h2>Hand over content.<br>Select an engine.<br>Render, inspect, approve.</h2><p>The durable asset is the written and machine-readable grammar. When a visual drifts, repair the system specification—not the individual slide. Current state: production-capable direction proof; Jen taste review and full-deck validation remain open.</p></footer>
</body></html>'''
(ROOT / "SYSTEM-ATLAS.html").write_text(doc)
print(f"SYSTEM-ATLAS.html: {len(doc) / 1024 / 1024:.1f} MB self-contained")
