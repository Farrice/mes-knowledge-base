#!/usr/bin/env python3
"""Two resolved artifacts: system comparison and definitive listing hero."""
import base64
import json
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
SAFE = ROOT / "same-door"
STUDY = ROOT / "codex-editorial-study"

PAPER = "#F4F0E8"
INK = "#173A54"
NAVY = "#244C68"
CLAY = "#BD765E"
MUTED = "#657783"
LINE = "#CBD6DB"


def encoded(path):
    mime = "image/png" if path.suffix == ".png" else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


FONTS = """@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&display=swap');"""


def comparison():
    safe = encoded(SAFE / "png" / "01-c1-same-door.png")
    editorial = encoded(STUDY / "png" / "01-cover.png")
    css = f"""{FONTS}*{{box-sizing:border-box}}body{{margin:0}}.b{{width:1800px;height:1100px;background:{PAPER};color:{INK};padding:72px 84px;font-family:Manrope,Arial,sans-serif}}.serif{{font-family:Newsreader,Georgia,serif;letter-spacing:-.035em}}.caps{{font-size:15px;font-weight:700;letter-spacing:.18em;text-transform:uppercase}}.muted{{color:{MUTED}}}"""
    return f"""<!doctype html><meta charset=utf-8><style>{css}</style><div class=b>
      <header style="display:flex;justify-content:space-between;align-items:flex-end;border-bottom:1px solid {INK};padding-bottom:28px">
        <div><div class=caps style="color:{CLAY};margin-bottom:12px">Identity decision</div><div class=serif style="font-size:62px;line-height:.95">one identity. two modes.</div></div>
        <div class=muted style="font-size:18px;text-align:right;line-height:1.5">Gigi Mironova<br>Codex art-direction review</div>
      </header>
      <main style="display:grid;grid-template-columns:1fr 1fr;gap:74px;margin-top:50px">
        <section style="display:grid;grid-template-columns:240px 1fr;gap:34px">
          <img src="{safe}" style="width:240px;height:300px;object-fit:cover;border:1px solid {LINE}">
          <div><div class=caps>01 · Calm Closer</div><div class=serif style="font-size:42px;line-height:1;margin:18px 0">the recurring identity</div><p class=muted style="font-size:19px;line-height:1.55;margin:0">Clear, trustworthy and repeatable. It makes Gigi's document intelligence recognizable even when no listing is being promoted.</p></div>
          <div style="grid-column:1/-1;border-top:1px solid {LINE};padding-top:24px;display:grid;grid-template-columns:repeat(4,1fr);gap:18px">
            <div><div class=caps>Different</div><div style="font-size:28px;margin-top:9px">8/10</div></div><div><div class=caps>Readable</div><div style="font-size:28px;margin-top:9px">9/10</div></div><div><div class=caps>Repeatable</div><div style="font-size:28px;margin-top:9px">9/10</div></div><div><div class=caps>Premium</div><div style="font-size:28px;margin-top:9px">8/10</div></div>
          </div>
          <div style="grid-column:1/-1;background:{NAVY};color:{PAPER};padding:24px 28px"><div class=caps style="color:#D4DFE4">Use for</div><div style="font-size:21px;margin-top:10px">Education · market intelligence · document authority · recurring content</div></div>
        </section>
        <section style="display:grid;grid-template-columns:240px 1fr;gap:34px">
          <img src="{editorial}" style="width:240px;height:300px;object-fit:cover;border:1px solid {LINE}">
          <div><div class=caps>02 · Property Dossier</div><div class=serif style="font-size:42px;line-height:1;margin:18px 0">the listing campaign mode</div><p class=muted style="font-size:19px;line-height:1.55;margin:0">The property becomes the visual draw. Stronger desire and premium perception—but too specialized and photograph-dependent to carry every post.</p></div>
          <div style="grid-column:1/-1;border-top:1px solid {LINE};padding-top:24px;display:grid;grid-template-columns:repeat(4,1fr);gap:18px">
            <div><div class=caps>Different</div><div style="font-size:28px;margin-top:9px">9/10</div></div><div><div class=caps>Readable</div><div style="font-size:28px;margin-top:9px">7/10</div></div><div><div class=caps>Repeatable</div><div style="font-size:28px;margin-top:9px">6/10</div></div><div><div class=caps>Premium</div><div style="font-size:28px;margin-top:9px">9/10</div></div>
          </div>
          <div style="grid-column:1/-1;border:2px solid {NAVY};padding:22px 26px"><div class=caps>Use for</div><div style="font-size:21px;margin-top:10px">New listings · property reveals · open houses · seller presentation moments</div></div>
        </section>
      </main>
      <footer style="margin-top:50px;border-top:5px solid {CLAY};padding-top:25px;display:flex;justify-content:space-between;align-items:baseline">
        <div class=serif style="font-size:42px">Verdict: Calm Closer leads. Property Dossier launches.</div><div class=caps>One brand · two jobs</div>
      </footer>
    </div>"""


def hero():
    photo = encoded(SAFE / "canvas-assets" / "unit-124-open-plan.jpg")
    css = f"""{FONTS}*{{box-sizing:border-box}}body{{margin:0}}.b{{width:1080px;height:1350px;background:{PAPER};color:{INK};font-family:Manrope,Arial,sans-serif;overflow:hidden}}.serif{{font-family:Newsreader,Georgia,serif;letter-spacing:-.042em}}.caps{{font-size:16px;font-weight:700;letter-spacing:.18em;text-transform:uppercase}}"""
    return f"""<!doctype html><meta charset=utf-8><style>{css}</style><div class=b>
      <div style="height:785px;position:relative;overflow:hidden">
        <img src="{photo}" style="width:100%;height:100%;object-fit:cover;object-position:50% 50%;filter:saturate(.82) contrast(1.02)">
        <div style="position:absolute;left:48px;right:48px;top:42px;display:flex;justify-content:space-between;color:white;text-shadow:0 1px 12px rgba(10,30,43,.45)" class=caps><span>Gigi Mironova</span><span>Unit 124 · Reseda</span></div>
      </div>
      <div style="height:565px;padding:48px 58px 46px;display:flex;flex-direction:column">
        <div class=caps style="color:{CLAY}">The first-month ledger</div>
        <div class=serif style="font-size:84px;line-height:.96;margin-top:20px">$158 more leaves.<br><span style="color:{CLAY}">$224</span> remains yours.</div>
        <div style="height:1px;background:{INK};opacity:.26;margin:30px 0 22px"></div>
        <div style="display:grid;grid-template-columns:1.22fr .78fr;gap:56px;font-size:21px;line-height:1.5;color:{MUTED}">
          <div>Same apartment. The ownership payment is higher—but part of it becomes principal instead of disappearing as rent.</div>
          <div>Estimate, not a quote.<br>Full breakdown available.</div>
        </div>
        <div style="margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end"><div class=caps>DRE 02025393 · Equity Union</div><div class=serif style="font-size:45px">DM <span style="color:{CLAY}">“124”</span></div></div>
      </div>
    </div>"""


def main():
    assets = {"comparison": (1800,1100,comparison()), "hero": (1080,1350,hero())}
    manifest = {"concept":"One identity, two modes","assets":{}}
    for name,(w,h,html) in assets.items():
        (HERE/f"{name}.html").write_text(html)
        manifest["assets"][name] = {"width":w,"height":h}
    (HERE/"manifest.json").write_text(json.dumps(manifest,indent=2))
    print("comparison + hero built")


if __name__ == "__main__": main()
