"""Bundle blind bar 01 for Claude Design: 21 slides (full-res PNG + 1080x1350 JPG), captions, one preview card per take."""
import pathlib, re, shutil, json
from PIL import Image
ROOT = pathlib.Path("/Users/farricecain/Google Antigravity/.claude/worktrees/scrapes-routing")
OUT = ROOT / ".tmp/design-sync/blind-bar-01"
if OUT.exists(): shutil.rmtree(OUT)
TAKES = [
    ("take-a-ag1", "Take A · AG1 teardown (named, fight picked) — Farrice's floor, 11/10", "2026-09-03-take-A-ag1-scrapes.md"),
    ("take-b-ag1", "Take B · AG1 teardown (symptom to decision) — 'I would close both'", "2026-09-03-take-B-ag1-ours.md"),
    ("take-c-greens", "Take C · the greens aisle (anonymized composite) — 9/10, client-privacy use", "2026-09-03-take-C-greens-composite.md"),
]
def caption(md):
    t = md.read_text(); c = t.split("## Caption\n\n", 1)[1].split("\n\n## ", 1)[0]
    return re.sub(r"\s*\[(VERIFIED|LIKELY|UNCONFIRMED)[^\]]*\]", "", c).strip()
index = []
for slug, title, mdname in TAKES:
    run = ROOT / f"projects/00-social-content/2026-09-03/blind-bar-01-{slug}"
    d = OUT / slug; (d / "png").mkdir(parents=True); (d / "jpg").mkdir()
    slides = sorted(run.glob("slide-0*.png"))
    for s in slides:
        shutil.copy(s, d / "png" / s.name)
        im = Image.open(s).convert("RGB"); im.thumbnail((1080, 1350)); im.save(d / "jpg" / (s.stem + ".jpg"), quality=92)
    cap = caption(ROOT / "_active/farrice-brand/content/blind-bar-01" / mdname)
    (d / "caption.md").write_text(f"# {title}\n\n{cap}\n")
    imgs = "".join(f"<img src='jpg/{s.stem}.jpg' alt='slide {i+1}'>" for i, s in enumerate(slides))
    html = f"""<!-- @dsCard group="Blind Bar 01 · LinkedIn carousels" -->
<title>{title}</title>
<style>body{{margin:0;background:#F3F3F0;color:#101010;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;padding:24px}}
h1{{font-size:22px;margin:0 0 12px}}.row{{display:flex;gap:8px;overflow-x:auto}}.row img{{height:300px;width:auto;flex:0 0 auto}}
pre{{white-space:pre-wrap;font:14px/1.5 'Helvetica Neue',Helvetica,Arial;color:#101010;max-width:720px;margin:16px 0 0}}
p.m{{color:#555553;font-size:13px;margin:8px 0 0}}</style>
<h1>{title}</h1><div class='row'>{imgs}</div>
<p class='m'>7 slides · 1080×1350 (4:5) · full-res PNG in png/, post-ready JPG in jpg/ · rendered 2026-09-03, $0</p>
<details><summary>caption</summary><pre>{cap}</pre></details>"""
    (d / "index.html").write_text(html)
    index.append({"take": slug, "title": title, "slides": len(slides), "png": f"{slug}/png/", "jpg": f"{slug}/jpg/", "caption": f"{slug}/caption.md"})
(OUT / "README.md").write_text("# Blind Bar 01 · supplement teardown carousels (2026-09-03)\n\nThree 7-slide LinkedIn carousels for Farrice Cain, editorial pool, all real evidence crops, no AI images.\n"
    "Farrice's verdict: A is the floor (11/10); B close second; C is the safe composite (9/10, client-privacy use only).\n\n" + json.dumps(index, indent=2) + "\n")
shutil.copy(ROOT / "_active/farrice-brand/content/blind-bar-01/2026-09-03-claims-ledger.md", OUT / "claims-ledger.md")
n = sum(1 for _ in OUT.rglob("*") if _.is_file()); print("bundle files:", n, "at", OUT)
