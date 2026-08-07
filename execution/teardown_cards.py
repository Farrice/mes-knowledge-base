#!/usr/bin/env python3
"""
teardown_cards.py — render platform-ready teardown cards in the Farrice Cain
Premium Minimal design system (report dialect), HTML → PNG via headless Chrome.

Zero API cost. Tokens mirror templates/research-brief/template.html :root so the
cards read as the same system as the briefs.

Sizes shipped per teardown:
  header    1200x627   LinkedIn article header / link preview / blog hero
  square    1080x1080  LinkedIn + Instagram + X quote card
  portrait  1080x1350  LinkedIn / Instagram carousel cover

Usage:
    python3 execution/teardown_cards.py [--out DIR] [--only SLUG]
"""
import argparse
import html
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = ROOT / "_active/linkedin/03-launch/teardowns/assets"

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
]

SIZES = {"header": (1200, 627), "square": (1080, 1080), "portrait": (1080, 1350)}

# ── the cards ────────────────────────────────────────────────────────────────
# accent: wrap ONE word in *asterisks* for the italic-serif steel-blue voice.
CARDS = [
    # ── series cover ──
    dict(slug="series-cover", size="header", eyebrow="THE TEARDOWN SERIES",
         headline="Six supplement brands, read from the *outside*.",
         body="Public surface only. Every claim quoted from their own pages, "
              "sent to the brand before it went up.",
         foot_l="FARRICE CAIN", foot_r="@farricecain"),

    # ── Create Wellness ──
    dict(slug="create-header", size="header", eyebrow="TEARDOWN No. 4 · CREATE WELLNESS",
         headline="The only NSF certified creatine gummy in the world. It's in an *accordion*.",
         body="Four of six gummies failed an outside lab test. Two measured zero. "
              "Theirs came back over the label.",
         foot_l="CLAIM → PROOF → GAP", foot_r="@farricecain"),
    dict(slug="create-square", size="square", eyebrow="CREATE WELLNESS · MEASURED",
         stat="4.59g", stat_sub="against a 4.5g label",
         headline="Two competitors in the same test measured *zero*.",
         body="Creatine degrades into creatinine in water and heat. That is exactly what "
              "making a gummy involves, and it is why most of the shelf fails.",
         foot_l="TEARDOWN No. 4", foot_r="@farricecain"),
    dict(slug="create-portrait", size="portrait", eyebrow="TEARDOWN No. 4",
         headline="They hold the one receipt their category is accused of *faking*.",
         body="Batch-level NSF Certified for Sport. Impurity caps published. Product "
              "retested at eighteen months, still meeting label.\n\nThe homepage is "
              "running a summer sale.",
         foot_l="CREATE WELLNESS", foot_r="@farricecain"),

    # ── Hilma ──
    dict(slug="hilma-header", size="header", eyebrow="TEARDOWN No. 5 · HILMA",
         headline="The headline is arguing with the footnote, and the footnote is *right*.",
         body="They ran a study on the product they actually sell. Then they wrote "
              "“Clinically Proven” above their own disclosure.",
         foot_l="CLAIM → PROOF → GAP", foot_r="@farricecain"),
    dict(slug="hilma-square", size="square", eyebrow="HILMA · THEIR OWN STUDY",
         stat="94%", stat_sub="of 101 participants",
         headline="Single arm. No control group. They printed that *themselves*.",
         body="In a category where “clinically studied” usually means somebody read "
              "an abstract about an ingredient, that footnote is more honest than the "
              "entire shelf around it.",
         foot_l="TEARDOWN No. 5", foot_r="@farricecain"),
    dict(slug="hilma-portrait", size="portrait", eyebrow="TEARDOWN No. 5",
         headline="The strong version always sounds smaller than the *puffed* one.",
         body="It just happens to survive contact with a skeptic.\n\nWrite the sentence "
              "that includes your own limitation. Then read it next to your competitor's "
              "claim and notice which one you'd believe.",
         foot_l="HILMA", foot_r="@farricecain"),

    # ── BPN ──
    dict(slug="bpn-header", size="header", eyebrow="TEARDOWN No. 6 · BARE PERFORMANCE NUTRITION",
         headline="A standard nobody wrote down is a *slogan*.",
         body="NSF Certified for Sport on the whey. Creapure on the creatine. "
              "No quality page anywhere on the site.",
         foot_l="CLAIM → PROOF → GAP", foot_r="@farricecain"),
    dict(slug="bpn-square", size="square", eyebrow="BPN · THE MISSING PAGE",
         stat="404", stat_sub="/pages/quality",
         headline="The part nobody can rent is sitting in a bullet next to *gluten free*.",
         body="Belonging is rentable. Any founder with a camera and ten consistent years "
              "can build it. The certification is the one thing a competitor has to pay for.",
         foot_l="TEARDOWN No. 6", foot_r="@farricecain"),
    dict(slug="bpn-portrait", size="portrait", eyebrow="TEARDOWN No. 6",
         headline="A guy left Transparent Labs for BPN and wrote a review about *chocolate*.",
         body="Transparent Labs has one of the most honest labels in the business. It lost "
              "that customer on flavor, and the customer never mentioned a label at all.\n\n"
              "Neither brand's proof had anything to do with it.",
         foot_l="BARE PERFORMANCE NUTRITION", foot_r="@farricecain"),
]

SCALE = {"header": 1.0, "square": 1.06, "portrait": 1.0}


def accent(s):
    out = html.escape(s, quote=True)
    import re
    return re.sub(r"\*([^*]+)\*", r'<em>\1</em>', out, count=1)


def page(card):
    w, h = SIZES[card["size"]]
    k = SCALE[card["size"]]
    stat_block = ""
    if card.get("stat"):
        stat_block = (
            f'<div class="stat"><span class="statnum">{html.escape(card["stat"])}</span>'
            f'<span class="statsub">{html.escape(card["stat_sub"])}</span></div>'
        )
    body = "".join(
        f"<p>{html.escape(p)}</p>" for p in card.get("body", "").split("\n\n") if p.strip()
    )
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
  :root{{
    --ag-ink:#101010; --ag-paper:#F3F3F0; --ag-line:#D8D8D3;
    --ag-accent:#3D5A94; --ag-ink-soft:#555553; --ag-ink-mute:#8C8C82;
    --sans:'Helvetica Neue',Helvetica,Inter,system-ui,Arial,sans-serif;
    --serif:'Source Serif 4',Georgia,'Times New Roman',serif;
    --mono:ui-monospace,'SF Mono',Menlo,monospace;
  }}
  *{{margin:0;padding:0;box-sizing:border-box}}
  html,body{{width:{w}px;height:{h}px}}
  body{{background:var(--ag-paper);color:var(--ag-ink);font-family:var(--sans);
    -webkit-font-smoothing:antialiased;print-color-adjust:exact}}
  .card{{width:{w}px;height:{h}px;padding:{int(64*k)}px {int(72*k)}px;
    display:flex;flex-direction:column;position:relative}}
  .eyebrow{{font-family:var(--mono);font-size:{int(12*k)}px;letter-spacing:.19em;
    text-transform:uppercase;color:var(--ag-ink-mute)}}
  .rule{{height:1px;background:var(--ag-line);margin:{int(22*k)}px 0 auto}}
  .mid{{margin:auto 0;display:flex;flex-direction:column;gap:{int(30*k)}px}}
  h1{{font-size:{int(52*k)}px;line-height:1.12;letter-spacing:-.022em;font-weight:600;
    max-width:22ch}}
  h1 em{{font-family:var(--serif);font-style:italic;font-weight:400;color:var(--ag-accent);
    letter-spacing:-.01em}}
  .body p{{font-size:{int(20*k)}px;line-height:1.5;color:var(--ag-ink-soft);max-width:46ch}}
  .body p + p{{margin-top:{int(14*k)}px}}
  .stat{{display:flex;align-items:baseline;gap:{int(18*k)}px;margin-bottom:{int(16*k)}px}}
  .statnum{{font-size:{int(148*k)}px;line-height:.86;letter-spacing:-.045em;font-weight:600}}
  .statsub{{font-family:var(--mono);font-size:{int(15*k)}px;letter-spacing:.13em;
    text-transform:uppercase;color:var(--ag-ink-mute)}}
  .foot{{margin-top:auto;padding-top:{int(22*k)}px;border-top:1px solid var(--ag-line);
    display:flex;justify-content:space-between;font-family:var(--mono);
    font-size:{int(12*k)}px;letter-spacing:.17em;text-transform:uppercase;
    color:var(--ag-ink-mute)}}
  .foot .r{{color:var(--ag-accent)}}
</style></head><body><div class="card">
  <div class="eyebrow">{html.escape(card["eyebrow"])}</div>
  <div class="rule"></div>
  <div class="mid">{stat_block}<h1>{accent(card["headline"])}</h1>
    <div class="body">{body}</div></div>
  <div class="foot"><span>{html.escape(card["foot_l"])}</span>
    <span class="r">{html.escape(card["foot_r"])}</span></div>
</div></body></html>"""


def find_chrome():
    for c in CHROME_CANDIDATES:
        if Path(c).exists():
            return c
    return shutil.which("chromium") or shutil.which("google-chrome")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--only")
    args = ap.parse_args()

    chrome = find_chrome()
    if not chrome:
        sys.exit("[teardown_cards] no Chrome/Chromium found — install one or use the MCP browser")

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    tmp = ROOT / ".tmp" / "teardown-cards"
    tmp.mkdir(parents=True, exist_ok=True)

    made = []
    for card in CARDS:
        if args.only and args.only not in card["slug"]:
            continue
        w, h = SIZES[card["size"]]
        src = tmp / f"{card['slug']}.html"
        src.write_text(page(card), encoding="utf-8")
        png = out / f"{card['slug']}-{w}x{h}.png"
        subprocess.run([
            chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=2", f"--window-size={w},{h}",
            f"--screenshot={png}", src.as_uri(),
        ], check=True, capture_output=True)
        made.append(png)
        print(f"[teardown_cards] {png.relative_to(ROOT)}  ({w}x{h} @2x)")

    print(f"[teardown_cards] {len(made)} cards → {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
