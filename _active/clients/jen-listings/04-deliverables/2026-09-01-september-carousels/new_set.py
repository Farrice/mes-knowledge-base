#!/usr/bin/env python3
"""Build a new seven-slide Valley Native carousel from a JSON spec. One command, on-system, every time.

    python3 new_set.py sets/<name>.json            # writes <STEM>1..7.dc.html next to this file
    python3 new_set.py sets/<name>.json --render   # also renders png/<key>-0n.png with headless chrome

Spec shape (see sets/example-reseda.json): stamp, stem, key, and exactly seven slides, each with a `type`:
  cover · keyed · bars · stat · dark · panels · list · italic · close
Every slide type maps to one finished component from the system, so the output can't drift off-brand.
Copy rules (plain words with punch, her close on slide 7, no warm colors) live in DESIGN.md and RULEBOOK.md;
the spec author owns the words, this file owns the design."""
import glob, json, os, pathlib, shutil, subprocess, sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import gen_valley as V                       # tokens, line art, facades, bar, marker, print_, eyebrow, body, it
from gen_valley_sets import (cover, keyed, shell, close, panels, fact,
                             station, price_tag_x, calendar, cone, house_hill, house_flat, flame)

GLYPHS = {"station": station, "price": price_tag_x, "calendar": calendar, "cone": cone,
          "hill": house_hill, "flat": house_flat, "flame": flame,
          "dingbat": lambda: V.facade("dingbat", 110, 100), "courtyard": lambda: V.facade("courtyard", 110, 100),
          "midrise": lambda: V.facade("midrise", 110, 100), "bungalow": lambda: V.facade("bungalow", 110, 100)}


def strong(txt, dark=False):
    c = V.CREAM if dark else V.INK
    return f"<span style='color: {c}; font-weight: 500;'>{txt}</span>"


def render_body(s, dark=False):
    """`body` is a string; `**...**` marks the navy-strong tail."""
    out = s
    while "**" in out:
        out = out.replace("**", f"<span style='color: {V.CREAM if dark else V.INK}; font-weight: 500;'>", 1).replace("**", "</span>", 1)
    return out


def headline_html(s, dark=False):
    """`_..._` marks the one Playfair-italic phrase; `|` is a line break."""
    parts = s.split("_")
    html = ""
    for i, part in enumerate(parts):
        html += V.it(part, dark) if i % 2 else part
    return html.replace("|", "<br>")


def build(spec):
    Z = spec["stamp"]
    stem = spec["stem"]
    out = {}
    for n, sl in enumerate(spec["slides"], 1):
        t = sl["type"]
        dark = sl.get("dark", False)
        if t == "cover":
            html = cover(Z, sl["photo"], sl["caption"], headline_html(sl["headline"]), sl["dek"], obj_pos=sl.get("focus", "50% 30%"))
        elif t == "keyed":
            stops = [(GLYPHS[g](), lab) for g, lab in sl["stops"]]
            html = keyed(Z, sl["eyebrow"], sl["italic"], sl["sans"], render_body(sl["body"]), stops, sl["footer"])
        elif t == "bars":
            bars = "".join(V.bar(l, v, w, strong=bool(s)) for l, v, w, s in sl["bars"])
            inner = f'''{V.eyebrow(sl["eyebrow"])}
    <div style="font-size: 60px; font-weight: 600; line-height: 1.16; color: {V.INK}; letter-spacing: -0.01em;">{headline_html(sl["headline"])}</div>
{V.body(render_body(sl["body"]), width=760, size=31)}
    <div style="display: flex; flex-direction: column; gap: 38px; padding-top: 6px;">{bars}</div>'''
            html = shell(Z, inner, sl["footer"], n)
        elif t == "stat":
            unit = f'<span style="{V.SERIF} font-style: italic; font-size: 90px; color: {V.STEEL};">{sl["unit"]}</span>' if sl.get("unit") else ""
            inner = f'''{V.eyebrow(sl["eyebrow"])}
    <div style="display: flex; align-items: baseline; gap: 6px;"><span style="{V.SERIF} font-size: 170px; font-weight: 500; line-height: 0.95; color: {V.INK}; letter-spacing: -0.03em;">{sl["numeral"]}</span>{unit}</div>
    <div style="font-size: 48px; font-weight: 600; line-height: 1.22; color: {V.INK}; letter-spacing: -0.01em; max-width: 860px;">{headline_html(sl["headline"])}</div>
{V.body(render_body(sl["body"]), width=760, size=31)}'''
            html = shell(Z, inner, sl["footer"], n)
        elif t == "dark":
            pr = V.print_(sl["photo"], 300, 230, rot=1.5, dark=True, obj_pos=sl.get("focus", "50% 50%"), cap=sl["caption"]) if sl.get("photo") else ""
            inner = f'''{V.eyebrow(sl["eyebrow"], dark=True)}
    <div style="display: flex; gap: 46px; align-items: flex-start;">
      <div style="flex: 1; display: flex; flex-direction: column; gap: 36px;">
        <div style="font-size: 76px; font-weight: 600; line-height: 1.14; color: {V.CREAM}; letter-spacing: -0.01em;">{headline_html(sl["headline"], dark=True)}</div>
{V.body(render_body(sl["body"], dark=True), dark=True, width=460, size=32)}
      </div>
      <div style="flex: none; padding-top: 8px;">{pr}</div>
    </div>'''
            html = shell(Z, inner, sl["footer"], n, dark=True)
        elif t == "panels":
            l, r = sl["left"], sl["right"]
            inner = f'''{V.eyebrow(sl["eyebrow"], dark=dark)}
    <div style="font-size: 62px; font-weight: 600; line-height: 1.16; color: {V.CREAM if dark else V.INK}; letter-spacing: -0.01em;">{headline_html(sl["headline"], dark)}</div>
{panels(l[0], l[1], r[0], r[1], dark=dark)}
{V.body(render_body(sl["body"], dark), dark=dark, width=780, size=31) if sl.get("body") else ""}'''
            html = shell(Z, inner, sl["footer"], n, dark=dark)
        elif t == "list":
            rows = "".join(f'''      <div style="display: flex; align-items: center; gap: 26px; height: 58px;">
        <div style="position: relative; width: 20px; height: 20px; border: 2px solid {V.INK}; background: {V.INK if i in (0, len(sl["rows"]) - 1) else V.CREAM}; box-sizing: border-box; flex: none;"></div>
        <span style="{V.SERIF} font-size: 38px; font-weight: 500; color: {V.INK}; white-space: nowrap;">{name}</span>
        <span style="{V.SIGN} font-size: 15px; font-weight: 600; letter-spacing: 0.18em; color: {V.GREY}; padding-left: 6px;">{tag}</span>
      </div>''' for i, (name, tag) in enumerate(sl["rows"]))
            inner = f'''{V.eyebrow(sl["eyebrow"])}
    <div style="font-size: 52px; font-weight: 600; line-height: 1.18; color: {V.INK}; letter-spacing: -0.01em;">{headline_html(sl["headline"])}</div>
    <div style="position: relative; display: flex; flex-direction: column; padding: 4px 0;">
      <div style="position: absolute; left: 9px; top: 29px; bottom: 29px; width: 2px; background: {V.INK};"></div>
{rows}
    </div>'''
            html = shell(Z, inner, sl["footer"], n)
        elif t == "italic":
            inner = f'''{V.eyebrow(sl["eyebrow"])}
    <div style="{V.SERIF} font-style: italic; font-size: 140px; font-weight: 400; line-height: 1.0; color: {V.INK};">{sl["italic"]}</div>
{V.body(render_body(sl["body"]), width=780, size=32)}'''
            html = shell(Z, inner, sl["footer"], n)
        elif t == "close":
            html = close(Z, sl["photo"], sl["caption"], headline_html(sl["headline"], dark=True), sl["body"], sl["source"],
                         obj_pos=sl.get("focus", "50% 14%"), img_h=sl.get("img_h"))
        else:
            raise SystemExit(f"unknown slide type: {t}")
        out[f"{stem}{n}"] = html
    return out


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    spec = json.loads(pathlib.Path(sys.argv[1]).read_text())
    assert len(spec["slides"]) == 7, "a set is exactly seven slides"
    slides = build(spec)
    for name, html in slides.items():
        (HERE / f"{name}.dc.html").write_text(V.HEAD.format(body=html))
    print("wrote", ", ".join(slides))
    if "--render" in sys.argv:
        chrome = sorted(glob.glob(os.path.expanduser("~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]
        tmp = HERE / ".render_tmp"; tmp.mkdir(exist_ok=True)
        for img in (HERE / "img").glob("*.jpg"):
            shutil.copy(img, tmp / img.name)
        (HERE / "png").mkdir(exist_ok=True)
        for i, (name, html) in enumerate(slides.items(), 1):
            shim = tmp / f"{name}.html"
            shim.write_text(V.HEAD.format(body=html).replace('<script src="./support.js"></script>', "").replace("<x-dc>", "").replace("</x-dc>", "").replace("<helmet>", "").replace("</helmet>", ""))
            png = HERE / "png" / f'{spec["key"]}-0{i}.png'
            subprocess.run([chrome, "--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1080,1350", "--virtual-time-budget=4000", f"--screenshot={png}", f"file://{shim}"], check=True, capture_output=True)
            print("  ", png.name)
        shutil.rmtree(tmp)


if __name__ == "__main__":
    main()
