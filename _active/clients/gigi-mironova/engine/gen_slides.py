#!/usr/bin/env python3
"""Stage 6 — render Gigi's carousel specs (slides.json) into .dc.html artboards + canvas.json.

Copy lives in slides.json (written by Stage 5). This file only executes design.
Slide kinds: hook · stat · list · two · dark · quote · cta · photo-fact
Run: python3 gen_slides.py && python3 render.py && python3 review_sheet.py
"""
import html as H
import json
import pathlib
import sys

import tokens as T

HERE = pathlib.Path(__file__).parent
# Optional args: spec path, output dir (defaults: slides.json, canvas/)
SPEC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "slides.json"
OUT = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "canvas"
OUT.mkdir(parents=True, exist_ok=True)

HEAD = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="{fonts}">
  <style>{css}</style>
</helmet>
{body}
</x-dc>
</body>
</html>
"""


def esc(s):
    """Escape, then re-enable the two inline marks copy may carry: [[hl]] and [[br]]."""
    s = H.escape(str(s), quote=False)
    s = s.replace("[[br]]", "<br>")
    while "[[hl:" in s:
        a = s.index("[[hl:")
        b = s.index("]]", a)
        s = s[:a] + f'<span class="hl">{s[a+5:b]}</span>' + s[b+2:]
    return s


def rule(series, dark=False):
    c = T.D_MUTED if dark else T.MUTED
    return (f'<div class="rule"><div class="caps" style="font-size:20px">{T.NAME} · {T.DRE}</div>'
            f'<div class="caps" style="font-size:18px;color:{c}">{esc(series)}</div></div>')


def foot(n, total, dark=False, note=None):
    c = T.D_MUTED if dark else T.MUTED
    left = f'<div class="caps" style="font-size:16px;color:{c}">{T.LOCKUP}</div>'
    mid = f'<div style="font-size:14px;line-height:1.3;color:{c};letter-spacing:.03em;max-width:440px;text-align:center;padding:0 24px">{esc(note)}</div>' if note else '<div></div>'
    right = f'<div class="caps" style="font-size:18px;color:{c}">{n} / {total}</div>'
    return f'<div class="foot">{left}{mid}{right}</div>'


def photo(src, treat, pos="center", scale=1.0):
    style = f"object-position:{pos};transform:scale({scale})"
    return (f'<div class="photo {treat}"><img src="{src}" style="{style}">'
            f'<div class="tint"></div><div class="scrim"></div></div>')


def frame(inner, dark=False, ru=False, bg=None):
    cls = "frame" + (" dark" if dark else "") + (" ru" if ru else "")
    return f'<div class="{cls}">{bg or ""}<div class="pad">{inner}</div></div>'


# ---------- kinds -------------------------------------------------------------

def k_hook(s, n, total):
    """Full-bleed photo, headline low, one-line dek. STORY slide."""
    dek = f'<div style="font-size:34px;line-height:1.4;color:{T.D_MUTED};max-width:760px;margin-top:26px">{esc(s["dek"])}</div>' if s.get("dek") else ""
    inner = (rule(s["series"], True)
             + f'<div style="margin-top:auto;padding-bottom:44px"><div class="tag"><span class="dot"></span>{esc(s.get("eyebrow", "READ THIS FIRST"))}</div>'
             f'<div class="h" style="font-size:{s.get("size", 92)}px;margin-top:34px;max-width:920px">{esc(s["headline"])}</div>{dek}</div>'
             + foot(n, total, True))
    return frame(inner, dark=True, ru=s.get("ru"), bg=photo(s["img"], s.get("treat", "bleed"), s.get("pos", "center"), s.get("scale", 1.0)))


def on_photo(s, n, total, card_html):
    """Any structure slide carrying an `img`: photo held in colour, content in a white card low in the frame."""
    inner = (rule(s["series"], True)
             + f'<div style="margin-top:auto;padding-bottom:30px"><div style="padding:40px 44px;max-width:940px;background:{T.WHITE};color:{T.INK}">{card_html}</div></div>'
             + foot(n, total, True, note=s.get("source")))
    return frame(inner, dark=True, ru=s.get("ru"), bg=photo(s["img"], s.get("treat", "bleed"), s.get("pos", "center"), s.get("scale", 1.0)))


def k_stat(s, n, total):
    """White. One oversized number as the proof object; label; body. STRUCTURE."""
    if s.get("img"):
        unit = f'<span style="font-size:60px;font-weight:700;letter-spacing:-0.01em;color:{T.ACCENT};margin-left:12px">{esc(s["unit"])}</span>' if s.get("unit") else ""
        card = (f'<div class="caps" style="font-size:17px;color:{T.ACCENT}">{esc(s["eyebrow"])}</div>'
                f'<div class="num" style="font-size:{s.get("size", 190)}px;margin-top:18px;display:flex;align-items:baseline;color:{T.INK}">{esc(s["num"])}{unit}</div>'
                f'<div class="h" style="font-size:46px;margin-top:16px;max-width:860px;color:{T.INK}">{esc(s["label"])}</div>'
                + (f'<div style="font-size:28px;line-height:1.45;color:{T.MUTED};margin-top:16px;max-width:820px">{esc(s["body"])}</div>' if s.get("body") else ""))
        return on_photo(s, n, total, card)
    unit = f'<span style="font-size:88px;font-weight:700;letter-spacing:-0.01em;color:{T.ACCENT};margin-left:14px">{esc(s["unit"])}</span>' if s.get("unit") else ""
    body = f'<div style="display:flex;gap:26px;margin-top:40px"><div style="width:2px;background:{T.HAIRLINE}"></div><div style="font-size:33px;line-height:1.5;color:{T.MUTED};max-width:760px">{esc(s["body"])}</div></div>' if s.get("body") else ""
    inner = (rule(s["series"])
             + f'<div><div class="caps" style="font-size:19px;color:{T.MUTED}">{esc(s["eyebrow"])}</div>'
             f'<div class="num" style="font-size:{s.get("size", 300)}px;margin-top:30px;display:flex;align-items:baseline">{esc(s["num"])}{unit}</div>'
             f'<div class="h" style="font-size:58px;margin-top:26px;max-width:880px">{esc(s["label"])}</div>{body}</div>'
             + foot(n, total, note=s.get("source")))
    return frame(inner, ru=s.get("ru"))


def k_list(s, n, total):
    """White. Numbered evidence rows — the receipt. STRUCTURE."""
    if s.get("img"):
        rows = ""
        for i, (t, d) in enumerate(s["rows"], 1):
            rows += (f'<div style="display:flex;gap:20px;padding:16px 0;border-top:1px solid {T.HAIRLINE}">'
                     f'<div class="num" style="font-size:32px;color:{T.ACCENT};width:56px;flex:none;line-height:1.1">0{i}</div>'
                     f'<div><div style="font-size:31px;font-weight:700;letter-spacing:-.02em;line-height:1.15;color:{T.INK}">{esc(t)}</div>'
                     f'<div style="font-size:24px;line-height:1.4;color:{T.MUTED};margin-top:6px;max-width:800px">{esc(d)}</div></div></div>')
        card = (f'<div class="caps" style="font-size:17px;color:{T.ACCENT}">{esc(s["eyebrow"])}</div>'
                f'<div class="h" style="font-size:{s.get("size", 50)}px;margin:14px 0 18px;max-width:860px;color:{T.INK}">{esc(s["headline"])}</div>'
                f'<div style="border-bottom:1px solid {T.HAIRLINE}">{rows}</div>')
        return on_photo(s, n, total, card)
    rows = ""
    for i, (t, d) in enumerate(s["rows"], 1):
        rows += (f'<div style="display:flex;gap:26px;padding:26px 0;border-top:1px solid {T.HAIRLINE}">'
                 f'<div class="num" style="font-size:44px;color:{T.ACCENT};width:70px;flex:none;line-height:1">0{i}</div>'
                 f'<div><div style="font-size:40px;font-weight:700;letter-spacing:-.02em;line-height:1.15">{esc(t)}</div>'
                 f'<div style="font-size:29px;line-height:1.45;color:{T.MUTED};margin-top:10px;max-width:820px">{esc(d)}</div></div></div>')
    inner = (rule(s["series"])
             + f'<div><div class="caps" style="font-size:19px;color:{T.MUTED}">{esc(s["eyebrow"])}</div>'
             f'<div class="h" style="font-size:{s.get("size", 66)}px;margin:26px 0 34px;max-width:900px">{esc(s["headline"])}</div>'
             f'<div style="border-bottom:1px solid {T.HAIRLINE}">{rows}</div></div>'
             + foot(n, total, note=s.get("source")))
    return frame(inner, ru=s.get("ru"))


def k_two(s, n, total):
    """White. Two panels side by side — the comparison. STRUCTURE."""
    def panel(p, strong):
        bg = T.WHITE if strong else "transparent"
        border = f"1px solid {T.HAIRLINE}"
        return (f'<div style="flex:1;padding:40px 36px;background:{bg};border:{border}">'
                f'<div class="caps" style="font-size:17px;color:{T.ACCENT if strong else T.MUTED}">{esc(p["label"])}</div>'
                f'<div class="num" style="font-size:{s.get("numsize", 120)}px;margin-top:22px">{esc(p["value"])}</div>'
                f'<div style="font-size:28px;line-height:1.45;color:{T.MUTED};margin-top:22px">{esc(p["body"])}</div></div>')
    body = f'<div style="font-size:32px;line-height:1.5;color:{T.MUTED};margin-top:36px;max-width:860px">{esc(s["body"])}</div>' if s.get("body") else ""
    inner = (rule(s["series"])
             + f'<div><div class="caps" style="font-size:19px;color:{T.MUTED}">{esc(s["eyebrow"])}</div>'
             f'<div class="h" style="font-size:{s.get("size", 62)}px;margin:26px 0 36px;max-width:900px">{esc(s["headline"])}</div>'
             f'<div style="display:flex;gap:18px">{panel(s["left"], False)}{panel(s["right"], True)}</div>{body}</div>'
             + foot(n, total, note=s.get("source")))
    return frame(inner, ru=s.get("ru"))


def k_dark(s, n, total):
    """Band ground, one statement, optional body. The pause slide."""
    body = f'<div style="font-size:34px;line-height:1.5;color:{T.D_MUTED};max-width:820px;margin-top:36px">{esc(s["body"])}</div>' if s.get("body") else ""
    inner = (rule(s["series"], True)
             + f'<div><div class="caps" style="font-size:19px;color:{T.D_MUTED}">{esc(s["eyebrow"])}</div>'
             f'<div class="h" style="font-size:{s.get("size", 88)}px;margin-top:30px;max-width:920px">{esc(s["headline"])}</div>{body}</div>'
             + foot(n, total, True, note=s.get("source")))
    return frame(inner, dark=True, ru=s.get("ru"))


def k_quote(s, n, total):
    """Duotone photo carrying a single spoken line. STORY."""
    inner = (rule(s["series"], True)
             + f'<div><div class="h" style="font-size:{s.get("size", 84)}px;max-width:900px">{esc(s["headline"])}</div>'
             + (f'<div style="font-size:32px;line-height:1.5;color:{T.D_MUTED};max-width:760px;margin-top:32px">{esc(s["body"])}</div>' if s.get("body") else "")
             + '</div>' + foot(n, total, True, note=s.get("source")))
    return frame(inner, dark=True, ru=s.get("ru"), bg=photo(s["img"], s.get("treat", "duo"), s.get("pos", "center"), s.get("scale", 1.0)))


def k_photo_fact(s, n, total):
    """Listing photo held in colour, one fact card at the bottom. For the Unit 124 set."""
    card = (f'<div style="padding:38px 42px;max-width:900px;background:{T.WHITE};color:{T.INK}">'
            f'<div class="caps" style="font-size:17px;color:{T.ACCENT}">{esc(s["eyebrow"])}</div>'
            f'<div class="h" style="font-size:{s.get("size", 60)}px;color:{T.INK};margin-top:16px">{esc(s["headline"])}</div>'
            + (f'<div style="font-size:28px;line-height:1.45;color:{T.MUTED};margin-top:16px">{esc(s["body"])}</div>' if s.get("body") else "")
            + '</div>')
    inner = rule(s["series"], True) + f'<div style="margin-top:auto;padding-bottom:36px">{card}</div>' + foot(n, total, True, note=s.get("source"))
    bg = photo(s["img"], "bleed", s.get("pos", "center"), s.get("scale", 1.0))
    return frame(inner, dark=True, ru=s.get("ru"), bg=bg)


def k_cta(s, n, total):
    """Band ground, her portrait, one keyword. Every set closes here."""
    portrait = (f'<div style="width:300px;height:300px;flex:none;border:6px solid {T.WHITE};overflow:hidden">'
                f'<img src="{s.get("portrait", "../assets/brand/gigi-headshot.jpg")}" style="width:100%;height:100%;object-fit:cover;display:block"></div>')
    inner = (rule(s["series"], True)
             + f'<div style="display:flex;gap:44px;align-items:flex-start">{portrait}'
             f'<div><div class="h" style="font-size:{s.get("size", 76)}px;max-width:640px">{esc(s["headline"])}</div>'
             f'<div style="font-size:31px;line-height:1.5;color:{T.D_MUTED};max-width:620px;margin-top:26px">{esc(s["body"])}</div></div></div>'
             f'<div class="card" style="padding:40px 46px;background:{T.WHITE};border:none">'
             f'<div class="caps" style="font-size:17px;color:{T.ACCENT}">{esc(s.get("ask_label", "ONE MESSAGE GETS IT"))}</div>'
             f'<div style="display:flex;align-items:baseline;gap:20px;margin-top:14px"><span class="num" style="font-size:120px;color:{T.INK}">DM</span>'
             f'<span class="num" style="font-size:120px;color:{T.ACCENT}">&ldquo;{esc(s["keyword"])}&rdquo;</span></div>'
             f'<div style="font-size:30px;line-height:1.4;color:{T.MUTED};margin-top:12px">{esc(s["ask"])}</div>'
             f'<div class="caps" style="font-size:16px;color:{T.MUTED};margin-top:26px">{T.NAME} · {T.DRE} · 818-826-9998 · ENGLISH · РУССКИЙ</div></div>'
             + foot(n, total, True))
    bg = photo(s["img"], s.get("treat", "bleed"), s.get("pos", "center"), s.get("scale", 1.0)) if s.get("img") else None
    return frame(inner, dark=True, ru=s.get("ru"), bg=bg)


# ---------- two-zone layouts: photo zone never carries type; paper zone carries the data -------

def zone_img(s, h=None, w=None, extra=""):
    src, pos, scale = s["img"], s.get("pos", "center"), s.get("scale", 1.0)
    size = (f"height:{h}px;" if h else "height:100%;") + (f"width:{w}px;flex:none;" if w else "width:100%;")
    return (f'<div style="{size}overflow:hidden;position:relative;{extra}">'
            f'<img src="{src}" style="width:100%;height:100%;object-fit:cover;object-position:{pos};transform:scale({scale});display:block;'
            f'filter:saturate(.92) contrast(1.02)"></div>')


def stat_content(s, compact=True):
    unit = f'<span style="font-size:{56 if compact else 88}px;font-weight:700;letter-spacing:-0.01em;color:{T.ACCENT};margin-left:12px">{esc(s["unit"])}</span>' if s.get("unit") else ""
    return (f'<div class="caps" style="font-size:18px;color:{T.ACCENT}">{esc(s["eyebrow"])}</div>'
            f'<div class="num" style="font-size:{s.get("size", 200 if compact else 300)}px;margin-top:16px;display:flex;align-items:baseline">{esc(s["num"])}{unit}</div>'
            f'<div class="h" style="font-size:{46 if compact else 58}px;margin-top:14px;max-width:880px">{esc(s["label"])}</div>'
            + (f'<div style="font-size:{28 if compact else 33}px;line-height:1.45;color:{T.MUTED};margin-top:14px;max-width:820px">{esc(s["body"])}</div>' if s.get("body") else ""))


def list_content(s, compact=True):
    rows = ""
    for i, (t, d) in enumerate(s["rows"], 1):
        rows += (f'<div style="display:flex;gap:20px;padding:{14 if compact else 22}px 0;border-top:1px solid {T.HAIRLINE}">'
                 f'<div class="num" style="font-size:{32 if compact else 40}px;color:{T.ACCENT};width:56px;flex:none;line-height:1.1">0{i}</div>'
                 f'<div><div style="font-size:{31 if compact else 36}px;font-weight:700;letter-spacing:-.02em;line-height:1.15">{esc(t)}</div>'
                 f'<div style="font-size:{24 if compact else 27}px;line-height:1.4;color:{T.MUTED};margin-top:6px;max-width:820px">{esc(d)}</div></div></div>')
    return (f'<div class="caps" style="font-size:18px;color:{T.ACCENT}">{esc(s["eyebrow"])}</div>'
            f'<div class="h" style="font-size:{s.get("size", 48 if compact else 60)}px;margin:12px 0 16px;max-width:880px">{esc(s["headline"])}</div>'
            f'<div style="border-bottom:1px solid {T.HAIRLINE}">{rows}</div>')


def cta_content(s, compact=True):
    portrait = (f'<div style="width:{180 if compact else 240}px;height:{180 if compact else 240}px;flex:none;border:1px solid {T.HAIRLINE};overflow:hidden">'
                f'<img src="{s.get("portrait", "../assets/brand/gigi-headshot.jpg")}" style="width:100%;height:100%;object-fit:cover;display:block"></div>')
    return (f'<div style="display:flex;gap:32px;align-items:flex-start">{portrait}'
            f'<div><div class="h" style="font-size:{54 if compact else 70}px;max-width:640px">{esc(s["headline"])}</div>'
            f'<div style="font-size:{26 if compact else 30}px;line-height:1.45;color:{T.MUTED};max-width:620px;margin-top:14px">{esc(s["body"])}</div></div></div>'
            f'<div style="margin-top:{28 if compact else 40}px;padding:{26 if compact else 36}px 32px;background:{T.WHITE};border:1px solid {T.HAIRLINE}">'
            f'<div class="caps" style="font-size:16px;color:{T.ACCENT}">{esc(s.get("ask_label", "ONE MESSAGE GETS IT"))}</div>'
            f'<div style="display:flex;align-items:baseline;gap:16px;margin-top:8px"><span class="num" style="font-size:{88 if compact else 110}px">DM</span>'
            f'<span class="num" style="font-size:{88 if compact else 110}px;color:{T.ACCENT}">&ldquo;{esc(s["keyword"])}&rdquo;</span></div>'
            f'<div style="font-size:{26 if compact else 30}px;line-height:1.4;color:{T.MUTED};margin-top:8px">{esc(s["ask"])}</div>'
            f'<div class="caps" style="font-size:15px;color:{T.MUTED};margin-top:18px">{T.NAME} · {T.DRE} · 818-826-9998 · ENGLISH · РУССКИЙ</div></div>')


CONTENT = {"stat": stat_content, "list": list_content, "cta": cta_content}


def lay_split(s, n, total):
    """A · Split spread: photo owns the top half untouched, paper owns the bottom half with the data."""
    body = CONTENT[s["kind"]](s, compact=True)
    inner = (rule(s["series"])
             + f'<div style="display:flex;flex-direction:column;gap:0;flex:1;margin:22px -66px 0;min-height:0">'
             + zone_img(s, h=s.get("photo_h", 600))
             + f'<div style="padding:40px 66px 0;flex:1">{body}</div></div>'
             + foot(n, total, note=s.get("source")))
    return frame(inner, ru=s.get("ru"))


def lay_inset(s, n, total):
    """B · Inset column: type on the left, the photograph as a tall column on the right, edge to edge."""
    body = CONTENT[s["kind"]](s, compact=True)
    inner = (rule(s["series"])
             + f'<div style="display:flex;gap:44px;flex:1;margin:24px -66px 0 0;min-height:0;align-items:stretch">'
             f'<div style="flex:1;padding-top:26px;min-width:0">{body}</div>'
             + zone_img(s, w=s.get("photo_w", 400))
             + '</div>' + foot(n, total, note=s.get("source")))
    return frame(inner, ru=s.get("ru"))


def lay_strip(s, n, total):
    """C · Data-led: a letterboxed strip of the room across the top, the number owns the page."""
    body = CONTENT[s["kind"]](s, compact=False)
    inner = (rule(s["series"])
             + f'<div style="display:flex;flex-direction:column;flex:1;margin:22px -66px 0;min-height:0">'
             + zone_img(s, h=s.get("photo_h", 360))
             + f'<div style="padding:44px 66px 0;flex:1">{body}</div></div>'
             + foot(n, total, note=s.get("source")))
    return frame(inner, ru=s.get("ru"))


LAYOUTS = {"split": lay_split, "inset": lay_inset, "strip": lay_strip}


def dispatch(s, n, total):
    if s.get("layout") in LAYOUTS and s["kind"] in CONTENT and s.get("img"):
        return LAYOUTS[s["layout"]](s, n, total)
    return KINDS[s["kind"]](s, n, total)


KINDS = {"hook": k_hook, "stat": k_stat, "list": k_list, "two": k_two, "dark": k_dark,
         "quote": k_quote, "cta": k_cta, "photo-fact": k_photo_fact}


def main():
    spec = json.load(open(SPEC))
    artboards, count = [], 0
    for row, car in enumerate(spec["carousels"]):
        total = len(car["slides"])
        for col, s in enumerate(car["slides"], 1):
            s.setdefault("series", car["series"])
            body = dispatch(s, col, total)
            name = f'{car["slug"]}-{col:02d}'
            (OUT / f"{name}.dc.html").write_text(HEAD.format(fonts=T.FONTS, css=T.CSS, body=body))
            artboards.append({"file": f"{name}.dc.html", "title": f'{car["slug"]} · {col}/{total}',
                              "x": (col - 1) * 1180, "y": row * 1560, "w": 1080, "h": 1350})
            count += 1
    # first artboard doubles as Main for the canvas editor
    first = artboards[0]["file"]
    (OUT / "Main.dc.html").write_text((OUT / first).read_text())
    artboards[0]["file"] = "Main.dc.html"
    canvas = {"artboards": artboards, "launch": {"view": "canvas"}}
    (OUT / "canvas.json").write_text(json.dumps(canvas, indent=2))
    print(f"wrote {count} artboards + canvas.json -> {OUT}")


if __name__ == "__main__":
    main()
