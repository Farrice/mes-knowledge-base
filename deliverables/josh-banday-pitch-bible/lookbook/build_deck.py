"""Build the visual lookbook from the text deck + frames + cast map.

python3 build_deck.py --title "Recurring" [--source ../../IN-BETWEENER_pitch_deck.html]
                      [--cast-map cast_map.json] [--out RECURRING_pitch_lookbook.html]

Everything embeds as JPEG data URIs so the single HTML file travels alone.
Image conversion uses macOS `sips` (no Pillow on this box).
"""
import argparse
import base64
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FRAMES = HERE / "frames"
CACHE = HERE / ".jpg-cache"
CACHE.mkdir(exist_ok=True)


def resolve(p) -> Path:
    """cast_map paths may be absolute or relative to the lookbook folder."""
    p = Path(p)
    return p if p.is_absolute() else HERE / p


def to_jpeg(src: Path, max_px: int, quality: int = 80) -> Path:
    out = CACHE / f"{src.stem}-{max_px}.jpg"
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
        return out
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", str(quality),
                    "-Z", str(max_px), str(src), "--out", str(out)], check=True, capture_output=True)
    return out


def data_uri(src: Path, max_px: int, quality: int = 80) -> str:
    jpg = to_jpeg(src, max_px, quality)
    return "data:image/jpeg;base64," + base64.b64encode(jpg.read_bytes()).decode()


CSS = """
/* ═══ LOOKBOOK LAYER (build_deck.py) ═══ */
.hero { overflow: hidden; }
.hero-art { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center;
  opacity: 0.72; z-index: 0; filter: saturate(0.9); }
.hero::before { content: ''; position: absolute; inset: 0; z-index: 1;
  background: radial-gradient(ellipse at 50% 42%, rgba(7,7,7,0.45) 0%, rgba(7,7,7,0.55) 45%, rgba(7,7,7,0.85) 100%); }
.hero::after { z-index: 1; }
.hero > *:not(.hero-art) { position: relative; z-index: 2; }
.creator-photo { aspect-ratio: 3/4; overflow: hidden; position: relative;
  border: 1px solid rgba(201,169,110,0.2); background: var(--bg-card); }
.creator-photo img { width: 100%; height: 100%; object-fit: cover; object-position: center top;
  filter: saturate(0.85) contrast(1.05); display: block; }
.photo-credit { position: absolute; left: 0; right: 0; bottom: 0; padding: 8px 12px;
  font-family: var(--mono); font-size: 0.55rem; letter-spacing: 0.15em; text-transform: uppercase;
  color: var(--cream-dim); background: linear-gradient(to top, rgba(7,7,7,0.9), transparent); }
.lot-zone { padding-top: 0; overflow: hidden; }
.lot-zone-img { display: block; width: calc(100% + 48px); margin: 0 -24px 22px; aspect-ratio: 3/2;
  object-fit: cover; filter: saturate(0.9); border-bottom: 1px solid rgba(201,169,110,0.12); }
.lead-avatar { overflow: hidden; position: relative; }
.lead-avatar img { width: 100%; height: 100%; object-fit: cover; object-position: center top; display: block;
  filter: saturate(0.85) contrast(1.05); }
.lead-avatar-cap { position: absolute; left: 0; right: 0; bottom: 0; padding: 8px 12px;
  font-family: var(--mono); font-size: 0.55rem; letter-spacing: 0.2em; text-transform: uppercase;
  color: var(--gold); background: linear-gradient(to top, rgba(7,7,7,0.92), transparent); }
.comp-strip { display: flex; align-items: center; gap: 14px; margin-top: 18px; padding-top: 16px;
  border-top: 1px solid rgba(201,169,110,0.1); }
.comp-strip .comp { display: flex; align-items: center; gap: 10px; }
.comp-strip img { width: 54px; height: 70px; object-fit: cover; object-position: center 20%;
  border: 1px solid rgba(201,169,110,0.25); filter: saturate(0.8) contrast(1.05); display: block; }
.comp-strip .comp-name { font-family: var(--mono); font-size: 0.55rem; letter-spacing: 0.12em;
  text-transform: uppercase; color: var(--cream-dim); line-height: 1.5; }
.comp-strip .comp-label { font-family: var(--mono); font-size: 0.5rem; letter-spacing: 0.25em;
  text-transform: uppercase; color: var(--gold-dim); margin-right: 4px; white-space: nowrap; }
.credits-note { font-family: var(--mono); font-size: 0.55rem; letter-spacing: 0.08em; color: var(--cream-dim);
  opacity: 0.6; max-width: 720px; margin: 14px auto 0; line-height: 1.7; text-align: center; }
@media (max-width: 640px) { .comp-strip { flex-wrap: wrap; } .lot-zone-img { width: calc(100% + 40px); margin: 0 -20px 18px; }
  .scroll-indicator { display: none; } .hero-meta { line-height: 2; } }
"""

LOT_ORDER = ["02-stage-7", "03-craft-services", "04-trailer-village", "05-writers-room",
             "06-parking-lot", "07-production-offices"]


def pick_take(key: str, picks: dict) -> Path:
    """picks maps frame key -> take number; default take 1."""
    take = picks.get(key, 1)
    p = FRAMES / f"{key}-t{take}.png"
    if not p.exists():
        sys.exit(f"missing frame {p}")
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", default="Recurring")
    ap.add_argument("--source", default=str(HERE.parents[1] / "IN-BETWEENER_pitch_deck.html"))
    ap.add_argument("--cast-map", default=str(HERE / "cast_map.json"))
    ap.add_argument("--picks", default=str(HERE / "frames" / "picks.json"))
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    html = Path(a.source).read_text()
    cast = json.loads(Path(a.cast_map).read_text()) if Path(a.cast_map).exists() else {}
    picks = json.loads(Path(a.picks).read_text()) if Path(a.picks).exists() else {}
    slug = re.sub(r"[^A-Za-z0-9]+", "_", a.title).strip("_").upper()
    out = Path(a.out) if a.out else HERE / f"{slug}_pitch_lookbook.html"

    # 1. CSS layer
    html = html.replace("</style>", CSS + "\n</style>", 1)

    # 2. Title
    if a.title.lower() != "in-betweener":
        html = re.sub(r"<title>.*?</title>", f"<title>{a.title.upper()} — Pitch Lookbook</title>", html, count=1, flags=re.S)
        html = html.replace("<em>In-Betweener</em>", f"<em>{a.title}</em>", 1)

    # 2b. Fact fixes from the L5 pass (network attribution only; no copy rewrites)
    fixes = {
        "Slate Comps: Insecure • Hacks • Industry • Somebody Somewhere":
            "Slate Comps: Insecure • Industry • Somebody Somewhere • Hacks (Max)",
        "Slate Comps: Abbott Elementary • Ramy • Only Murders • The Bear":
            "Slate Comps: Ramy • Only Murders in the Building • PEN15 • Shrill",
    }
    for old, new in fixes.items():
        if old in html:
            html = html.replace(old, new, 1)
        else:
            print("WARN: fact-fix anchor not found:", old[:40])

    # 3. Hero key art
    hero_uri = data_uri(pick_take("01-hero-key-art", picks), 1800, 78)
    html = html.replace('<section class="hero">',
                        f'<section class="hero">\n  <img class="hero-art" src="{hero_uri}" alt="">', 1)

    # 4. Creator headshot
    creator = cast.get("creator")
    if creator and resolve(creator["file"]).exists():
        uri = data_uri(resolve(creator["file"]), 900, 82)
        credit = creator.get("credit", "")
        block = (f'<div class="creator-photo reveal reveal-delay-1"><img src="{uri}" alt="Josh Banday">'
                 f'<span class="photo-credit">{credit}</span></div>')
        html = re.sub(r'<div class="creator-photo-placeholder[^"]*">.*?</div>\s*', block + "\n", html, count=1, flags=re.S)
        # lead card avatar = Josh as Jules
        lead_uri = data_uri(resolve(creator.get("lead_file", creator["file"])), 700, 82)
        html = re.sub(r'<div class="lead-avatar">\s*<span class="lead-avatar-text">JS</span>\s*</div>',
                      f'<div class="lead-avatar"><img src="{lead_uri}" alt="Josh Banday as Jules">'
                      f'<span class="lead-avatar-cap">Josh Banday as Jules</span></div>', html, count=1, flags=re.S)

    # 5. Lot zone frames, in document order
    def lot_sub(m, _it=iter(LOT_ORDER)):
        key = next(_it)
        uri = data_uri(pick_take(key, picks), 1200, 78)
        return m.group(0) + f'\n        <img class="lot-zone-img" src="{uri}" alt="">'
    html = re.sub(r'<div class="lot-zone reveal[^"]*">', lot_sub, html, count=6)

    # 6. Cast comps per card (lead card + ensemble cards)
    def strip_for(comps, label="Casting comps"):
        items = []
        for c in comps:
            p = resolve(c["file"])
            if not p.exists():
                print("WARN: missing comp file", p)
                continue
            items.append(f'<span class="comp"><img src="{data_uri(p, 240, 80)}" alt="{c["name"]}">'
                         f'<span class="comp-name">{c["name"]}<br>{c.get("known_for", "")}</span></span>')
        return ('<div class="comp-strip"><span class="comp-label">' + label + '</span>' + "".join(items) + "</div>") if items else ""

    lead_strip = strip_for(cast.get("lead_comps", []), "If not Josh")
    if lead_strip:
        html, n = re.subn(r'(<div class="lead-quote">.*?</div>)', lambda m: m.group(1) + "\n        " + lead_strip, html, count=1, flags=re.S)
        if n == 0:
            print("WARN: no lead-quote anchor")
    for name, comps in cast.get("ensemble", {}).items():
        strip = strip_for(comps)
        if not strip:
            continue
        pat = re.compile(r'(<h4 class="char-name">' + re.escape(name) + r'</h4>.*?<div class="char-line">.*?</div>)', re.S)
        html, n = pat.subn(lambda m: m.group(1) + "\n        " + strip, html, count=1)
        if n == 0:
            print("WARN: no card for", name)

    # 6b. Companion credits file (CC BY / BY-SA attribution lives here; the deck footer points to it)
    lines = ["# Image credits — " + a.title + " pitch lookbook", "",
             "Casting comparison and location photographs are publicly available reference images used for development purposes only. They imply no attachment or offer.", "",
             "| Use | Subject | Source | License | Attribution |", "|---|---|---|---|---|"]
    if creator:
        lines.append(f"| Creator headshot (placeholder, swap for Josh's own) | Josh Banday | {creator.get('source','')} | {creator.get('license','UNCONFIRMED')} | {creator.get('attribution','')} |")
    for c in cast.get("lead_comps", []):
        lines.append(f"| Comp — Jules | {c['name']} | {c.get('source','')} | {c.get('license','')} | {c.get('attribution','')} |")
    for name, comps in cast.get("ensemble", {}).items():
        for c in comps:
            lines.append(f"| Comp — {name} | {c['name']} | {c.get('source','')} | {c.get('license','')} | {c.get('attribution','')} |")
    lines += ["", "World frames (hero and six locations) are concept renders generated for this lookbook from the shot list in SHOT-LIST.md; they depict no real person."]
    (HERE / "CREDITS.md").write_text("\n".join(lines) + "\n")

    # 7. Credits note in the footer
    note = ("Casting comparison and location photographs are publicly available reference images used for "
            "development purposes only and are not an offer of employment or a representation of attachment. "
            "World frames are concept renders. Sources listed in the companion credits file.")
    html = html.replace("<p>Confidential — For Development Purposes Only — 2026</p>",
                        f'<p>Confidential — For Development Purposes Only — 2026</p>\n    <p class="credits-note">{note}</p>', 1)

    out.write_text(html)
    n_img = html.count("<img ")
    print(f"BUILT {out} · {out.stat().st_size/1e6:.2f} MB · {n_img} images embedded · title={a.title}")

    # 8. Print variant for the PDF: reveals forced visible, backgrounds printed, no 100vh pages
    print_css = """
<style>
.reveal { opacity: 1 !important; transform: none !important; transition: none !important; }
html, body { -webkit-print-color-adjust: exact; print-color-adjust: exact; background: #070707 !important; }
@page { size: 1200px 4200px; margin: 0; }
.hero { min-height: 1400px; }
.hero::before, .hero::after, .photo-credit, .lead-avatar-cap { background: none !important; }
.hero-art { opacity: 0.5 !important; }
img { filter: none !important; }  /* CSS filters force Chrome to rasterize images into the PDF (29 MB); JPEGs pass through without them */
section, .lead-card, .char-card, .lot-zone, .network-card, .episode { break-inside: avoid; page-break-inside: avoid; }
section { padding-top: 60px !important; padding-bottom: 60px !important; }
</style>
</head>"""
    print_html = html.replace("</head>", print_css, 1)
    print_out = out.with_name(out.stem + "_print.html")
    print_out.write_text(print_html)
    print(f"PRINT VARIANT {print_out.name}")


if __name__ == "__main__":
    main()
