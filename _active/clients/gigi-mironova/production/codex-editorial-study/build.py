#!/usr/bin/env python3
"""The Property Dossier — three-board Codex-only editorial study."""
import base64
import json
from pathlib import Path

HERE = Path(__file__).parent
SOURCE = HERE.parent / "same-door" / "canvas-assets"

PAPER = "#F3EFE7"
INK = "#173A54"
NAVY = "#244C68"
CLAY = "#BD765E"
MUTED = "#657683"


def data(name):
    raw = (SOURCE / name).read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(raw).decode()


BASE = f"""
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&display=swap');
*{{box-sizing:border-box}}html,body{{margin:0;background:{PAPER}}}
.board{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{PAPER};color:{INK};font-family:'Manrope',Arial,sans-serif}}
.serif{{font-family:'Newsreader',Georgia,serif;font-weight:500;letter-spacing:-.045em}}
.caps{{font-size:16px;font-weight:700;letter-spacing:.19em;text-transform:uppercase}}
.folio{{position:absolute;left:54px;top:54px;bottom:54px;width:32px;display:flex;align-items:flex-end;border-right:1px solid {INK}}}
.folio span{{writing-mode:vertical-rl;transform:rotate(180deg);padding-right:12px;color:{MUTED}}}
.rule{{height:1px;background:{INK};opacity:.28}}
.clay{{color:{CLAY}}}
"""


def page(inner, extra=""):
    return f"""<!doctype html><meta charset=utf-8><style>{BASE}{extra}</style><div class=board>{inner}</div>"""


def board_one():
    return page(f"""
    <div class=folio><span class=caps>Property dossier · 001</span></div>
    <div style="position:absolute;left:118px;right:56px;top:54px;display:flex;justify-content:space-between" class=caps>
      <span>Gigi Mironova</span><span>Reseda · Unit 124</span>
    </div>
    <div style="position:absolute;left:118px;right:0;top:112px;height:685px;overflow:hidden">
      <img src="{data('unit-124-open-plan.jpg')}" style="width:100%;height:100%;object-fit:cover;object-position:48% 50%;filter:saturate(.78) contrast(1.02)">
    </div>
    <div style="position:absolute;left:118px;right:60px;top:848px">
      <div class=caps style="color:{CLAY};margin-bottom:24px">The ownership issue</div>
      <div class=serif style="font-size:91px;line-height:.94;max-width:890px">the apartment that<br>changes the <span class=clay>math.</span></div>
      <div class=rule style="margin:34px 0 24px"></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:48px;color:{MUTED};font-size:23px;line-height:1.45">
        <div>$2,500 to rent.<br>$2,658 estimated to own.</div>
        <div>Same door. Same rooms.<br>A different kind of payment.</div>
      </div>
    </div>
    """)


def board_two():
    return page(f"""
    <div class=folio><span class=caps>Property dossier · evidence</span></div>
    <div style="position:absolute;left:118px;right:58px;top:54px;display:flex;justify-content:space-between" class=caps>
      <span>The first-month ledger</span><span>01 / 03</span>
    </div>
    <div style="position:absolute;left:118px;right:58px;top:132px" class=rule></div>
    <div style="position:absolute;left:118px;top:192px;width:558px">
      <div class=serif style="font-size:190px;line-height:.82">$158</div>
      <div class=caps style="margin-top:26px;color:{CLAY}">more cash leaving</div>
      <div style="font-size:26px;line-height:1.5;color:{MUTED};margin-top:28px;max-width:455px">The monthly payment is higher. That is true—and incomplete.</div>
    </div>
    <div style="position:absolute;right:58px;top:188px;width:292px;height:402px;overflow:hidden">
      <img src="{data('unit-124-door.jpg')}" style="width:100%;height:100%;object-fit:cover;object-position:52% 50%;filter:grayscale(1) contrast(1.06)">
      <div style="position:absolute;inset:0;border:12px solid {PAPER}"></div>
    </div>
    <div style="position:absolute;left:118px;right:58px;top:650px" class=rule></div>
    <div style="position:absolute;left:118px;right:58px;top:714px;display:grid;grid-template-columns:360px 1fr;gap:80px">
      <div>
        <div class=serif style="font-size:152px;line-height:.82">$224</div>
        <div class=caps style="margin-top:24px;color:{CLAY}">stays as principal</div>
      </div>
      <div style="padding-top:10px">
        <div class=serif style="font-size:58px;line-height:1.03">cash flow is not the same thing as <span class=clay>cost.</span></div>
        <div style="font-size:23px;line-height:1.52;color:{MUTED};margin-top:34px">Estimated first-month housing cost: $2,434—about $66 below rent, before maintenance, transaction costs or appreciation.</div>
      </div>
    </div>
    <div style="position:absolute;left:118px;right:58px;bottom:56px;display:flex;justify-content:space-between" class=caps>
      <span>Estimate, not a quote</span><span>DRE 02025393</span>
    </div>
    """)


def board_three():
    return page(f"""
    <div style="position:absolute;inset:0 46% 0 0;background:{NAVY}"></div>
    <div style="position:absolute;left:58px;top:58px;width:468px;height:626px;overflow:hidden">
      <img src="{data('unit-124-living.jpg')}" style="width:100%;height:100%;object-fit:cover;object-position:51% 50%;filter:grayscale(1) contrast(1.07)">
      <div style="position:absolute;inset:0;background:{NAVY};mix-blend-mode:multiply;opacity:.42"></div>
    </div>
    <div style="position:absolute;left:58px;bottom:62px;width:450px;color:{PAPER}">
      <div class=caps style="color:#D6DEE3">Gigi Mironova · Realtor®</div>
      <div class=serif style="font-size:67px;line-height:1.02;margin-top:28px">I read the pages most people <span style="color:#F0C7B8">skip.</span></div>
      <div style="font-size:22px;line-height:1.55;color:#D6DEE3;margin-top:34px">Sixteen years in litigation support before real estate. HOA documents, disclosures and offers—in plain English or по-русски.</div>
    </div>
    <div style="position:absolute;left:604px;right:56px;top:58px" class=caps>Private briefing · Unit 124</div>
    <div style="position:absolute;left:604px;right:56px;top:166px" class=rule></div>
    <div style="position:absolute;left:604px;right:58px;top:236px">
      <div class=serif style="font-size:84px;line-height:.98">before you sign,<br>read what the<br>building is <span class=clay>saying.</span></div>
      <div style="margin-top:72px;border-top:4px solid {INK};padding-top:28px">
        <div class=caps>Request the dossier</div>
        <div style="font-size:29px;line-height:1.5;color:{MUTED};margin-top:22px">The payment breakdown.<br>The three HOA documents.<br>The questions worth asking.</div>
      </div>
    </div>
    <div style="position:absolute;left:604px;right:58px;bottom:58px">
      <div class=serif style="font-size:61px">DM <span class=clay>“124”</span></div>
      <div class=rule style="margin:25px 0 18px"></div>
      <div class=caps style="display:flex;justify-content:space-between"><span>Equity Union</span><span>818.826.9998</span></div>
    </div>
    """)


def main():
    boards = [("01-cover", board_one()), ("02-ledger", board_two()), ("03-briefing", board_three())]
    for name, html in boards:
        (HERE / f"{name}.html").write_text(html)
    (HERE / "manifest.json").write_text(json.dumps({"concept":"The Property Dossier","boards":[n for n,_ in boards]}, indent=2))
    print("3 editorial boards built")


if __name__ == "__main__":
    main()
