#!/usr/bin/env python3
"""Build the Claude Design design-system bundle for Valley Native under ds/:
component previews (one HTML each, first line carries the @dsCard marker), the 21 slide templates with
images inlined, the deck, DESIGN.md, the rulebook, the photo bank, and the generator source.
Everything self-contained: base64 images, Google Fonts links only."""
import base64, pathlib, re, shutil

HERE = pathlib.Path(__file__).parent
DS = HERE / "ds"
IMG = HERE / "img"
if DS.exists():
    shutil.rmtree(DS)
(DS / "components").mkdir(parents=True)
(DS / "templates").mkdir()
(DS / "deck").mkdir()
(DS / "source").mkdir()
(DS / "photos").mkdir()

FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Overpass:wght@400;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap">'

def inline_images(html):
    def repl(m):
        p = IMG / m.group(1)
        if not p.exists():
            return m.group(0)
        return f'src="data:image/jpeg;base64,{base64.b64encode(p.read_bytes()).decode()}"'
    return re.sub(r'src="([A-Za-z0-9._-]+\.jpg)"', repl, html)

def body_of(stem):
    src = (HERE / f"{stem}.dc.html").read_text()
    return inline_images(re.search(r"</helmet>\s*(.*?)\s*</x-dc>", src, re.S).group(1))

def page(marker_group, title, inner, w=1080, h=1350, subtitle=""):
    return (f'<!-- @dsCard group="{marker_group}" name="{title}" subtitle="{subtitle}" viewport="{w}x{h}" -->\n'
            f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title>{FONTS}"
            f"<style>body{{margin:0;background:#F7F5F2;font-family:Figtree,'Avenir Next',sans-serif;}}</style></head>"
            f"<body>{inner}</body></html>")

manifest = []
def emit(path, group, title, inner, w=1080, h=1350, subtitle=""):
    (DS / path).write_text(page(group, title, inner, w, h, subtitle))
    manifest.append({"name": title, "path": path, "group": group, "viewport": {"width": w, "height": h}, "subtitle": subtitle})

# ---- templates: the 21 slides + deck ----
SETS = [("condo", "DD", "the condo has to qualify too · van nuys 91401"),
        ("rail", "DR", "the train down van nuys blvd · van nuys 91401"),
        ("insurance", "DI", "the insurance quote · sherman oaks 91403")]
for key, stem, title in SETS:
    for i in range(1, 8):
        emit(f"templates/{key}-0{i}.html", f"Templates · {key}", f"{title} · slide {i}", body_of(f"{stem}{i}"))
for i in range(1, 17):
    emit(f"deck/presentation-{i:02d}.html", "Presentation", f"presentation · board {i}", body_of(f"S{i}"))
emit("deck/saved-dm-reply.html", "Presentation", "the saved DM reply", body_of("DM"))
emit("deck/in-your-words.html", "Presentation", "in your words", body_of("P5"), h=3400)
emit("deck/rulebook.html", "Presentation", "the rulebook", body_of("P3"), h=4400)
emit("deck/photo-bank.html", "Presentation", "the photo bank", body_of("P4"), h=2600)

# ---- components: isolated previews built from the generator ----
import gen_valley as V
from gen_valley_sets import stamp as set_stamp, keyed as set_keyed, panels as set_panels, station, calendar, cone, price_tag_x, house_hill, house_flat, flame

def card(inner, w=1080, h=None, dark=False):
    bg = V.INK if dark else V.CREAM
    hh = f"height: {h}px;" if h else ""
    return f'<div style="width: {w}px; {hh} background: {bg}; padding: 60px; box-sizing: border-box;">{inner}</div>'

emit("components/masthead-stamp.html", "Components", "masthead + stamp", card(V.mast() + "<div style='height:40px'></div>" + card(V.mast(dark=True), w=960, dark=True)), h=520, subtitle="cream and navy variants · stamp rotates per neighborhood")
emit("components/stamp-variants.html", "Components", "stamp · neighborhoods", card(set_stamp("VAN NUYS &#183; 91401") + set_stamp("SHERMAN OAKS &#183; 91403") + set_stamp("RESEDA &#183; 91335") + set_stamp("WOODLAND HILLS &#183; 91367")), h=420, subtitle="line 1 rotates, line 2 never")
facades = "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:14px">{V.facade(k, 140, 168)}<span style="{V.SIGN} font-size:15px;letter-spacing:.2em;color:{V.INK}">{k.upper()}</span></div>' for k in ("dingbat", "courtyard", "midrise", "bungalow"))
emit("components/facades.html", "Components", "the four valley buildings", card(f'<div style="display:flex;gap:60px;align-items:flex-end">{facades}</div><div style="height:40px"></div><div style="display:flex;gap:40px">{V.facade("midrise", 100, 120, marked=True, uid="m")}{V.facade("bungalow", 100, 120, marked=True, uid="b")}</div>'), h=520, subtitle="stroke-only, 100×120 grid · hatched = marked")
glyphs = "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:12px">{g}<span style="{V.SIGN} font-size:14px;letter-spacing:.2em;color:{V.INK}">{n}</span></div>' for g, n in [(station(), "STATION"), (calendar(), "CALENDAR"), (cone(), "CONE"), (price_tag_x(), "NO PRICE PROMISE"), (house_hill(), "HILLSIDE"), (house_flat(), "VALLEY FLOOR"), (flame(), "FIRE")])
emit("components/glyphs.html", "Components", "keyed-map glyphs", card(f'<div style="display:flex;gap:40px;flex-wrap:wrap;align-items:flex-end">{glyphs}</div>'), h=420, subtitle="one weight, navy, no fills")
emit("components/line-art.html", "Components", "map · arrow · ring · pages · mark", card(f'<div style="display:flex;gap:50px;align-items:center">{V.valley_map(320,320,V.SOFT)}{V.arrow(190,86)}{V.ring(150,105)}{V.minutes_page(56,74,V.INK)}{V.stamp_mark(90)}</div>'), h=480)
emit("components/print.html", "Components", "the print", card(f'<div style="display:flex;gap:60px;align-items:flex-start">{V.print_("vannuys-blvd-2024.jpg", 300, 380, rot=-1.5, cap="VAN NUYS BLVD &#183; 91401")}{V.print_("jen-porch-vannuys.jpg", 300, 380, rot=1.5, obj_pos="50% 20%", cap="JEN &#183; VAN NUYS")}</div>').replace('src="', 'src="'), h=560, subtitle="3px navy border, 14px mat, 1.5° tilt, sign caption")
emit("components/bars-panels.html", "Components", "bars + panels", card(f'<div style="display:flex;flex-direction:column;gap:38px">{V.bar("floor today", "10%", 40)}{V.bar("from jan 4, 2027", "15%", 60, strong=True)}{set_panels("7-YEAR BUYER", "worth a second look.", "2-YEAR BUYER", "you&#8217;d be buying the construction.")}</div>'), h=620)
emit("components/markers-eyebrow-body.html", "Components", "markers · eyebrow · body", card(f'<div style="display:flex;gap:20px">{V.marker("01")}{V.marker("02")}{V.marker("03")}{V.marker("04")}</div><div style="height:30px"></div>{V.eyebrow("01 &#183; THE SAVINGS ACCOUNT")}<div style="height:20px"></div>{V.body("roofs, plumbing, balconies. thin reserves are a surprise bill waiting to happen.")}'), h=420)
emit("components/footer.html", "Components", "footer", card(V.foot("SHARE OF THE BUDGET SET ASIDE", 3) + "<div style='height:30px'></div>" + card(V.foot("READ THEM BEFORE YOU OFFER", 4, dark=True), w=960, dark=True)), h=300)

# inline images inside component previews too
for p in (DS / "components").glob("*.html"):
    p.write_text(inline_images(p.read_text()))

# ---- docs, photos, source ----
(DS / "DESIGN.md").write_text((HERE / "DESIGN.md").read_text())
(DS / "RULEBOOK.md").write_text((HERE / "VALLEY-NATIVE-RULEBOOK.md").read_text())
for p in IMG.glob("*.jpg"):
    shutil.copy(p, DS / "photos" / p.name)
shutil.copy(IMG / "provenance.json", DS / "photos" / "provenance.json")
for name in ("gen_valley.py", "gen_valley_sets.py", "gen_deck.py", "gen_present.py", "render_png.py", "canva_export.py", "new_set.py"):
    if (HERE / name).exists():
        shutil.copy(HERE / name, DS / "source" / name)
(DS / "README.md").write_text("""# Valley Native · design system bundle

Jen Santulan (@_jiing) Instagram carousel system. `DESIGN.md` is the machine-readable spec; `RULEBOOK.md` is the human one.

- `components/` isolated previews of every part (masthead + stamp, facades, glyphs, line art, print, bars, panels, markers, footer)
- `templates/` the three finished carousels, 21 slides, images inlined
- `deck/` the seven-board presentation, the saved DM reply, her words, the rulebook, the photo bank
- `photos/` the cleared photo bank with provenance
- `source/` the generators. `new_set.py` builds a new seven-slide set from a JSON spec.
""")
import json
(DS / "_ds_manifest.json").write_text(json.dumps({"assets": manifest}, indent=2))
print("bundle:", len(manifest), "cards ->", DS)
