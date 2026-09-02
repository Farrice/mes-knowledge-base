#!/usr/bin/env python3
"""Render Jen's five reference-derived social systems from one JSON content packet.

The renderer proves the visual contracts; it does not approve copy, claims, imagery,
or publication. Output is always 1080x1350 PNG.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent
W, H = 1080, 1350
INTER = Path("/Users/farricecain/Library/Fonts/Inter-V.otf")
BODONI = Path("/System/Library/Fonts/Supplemental/Bodoni 72 OS.ttc")
BODONI_STD = Path("/System/Library/Fonts/Supplemental/Bodoni 72.ttc")
SIGNPAINTER = Path("/System/Library/Fonts/Supplemental/SignPainter.ttc")


def font(path: Path, size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    fallback = "/System/Library/Fonts/Helvetica.ttc"
    return ImageFont.truetype(str(path if path.exists() else fallback), size=size, index=index)


def resolve_asset(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def cover_image(path: Path, darken: float = 0.0, warmth: tuple[int, int, int, int] | None = None) -> Image.Image:
    image = Image.open(path).convert("RGB")
    image = ImageOps.fit(image, (W, H), method=Image.Resampling.LANCZOS)
    image = ImageEnhance.Contrast(image).enhance(1.08)
    image = ImageEnhance.Color(image).enhance(0.86)
    if warmth:
        veil = Image.new("RGBA", (W, H), warmth)
        image = Image.alpha_composite(image.convert("RGBA"), veil).convert("RGB")
    if darken:
        veil = Image.new("RGBA", (W, H), (0, 0, 0, round(255 * darken)))
        image = Image.alpha_composite(image.convert("RGBA"), veil).convert("RGB")
    return image


def gradient(image: Image.Image, top_alpha: int = 10, bottom_alpha: int = 180) -> Image.Image:
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pixels = overlay.load()
    for y in range(H):
        t = y / (H - 1)
        alpha = int(top_alpha + (bottom_alpha - top_alpha) * (t ** 1.6))
        for x in range(W):
            pixels[x, y] = (0, 0, 0, alpha)
    return Image.alpha_composite(image.convert("RGBA"), overlay).convert("RGB")


def width(draw: ImageDraw.ImageDraw, text: str, face: ImageFont.FreeTypeFont) -> int:
    box = draw.textbbox((0, 0), text, font=face)
    return box[2] - box[0]


def wrap(draw: ImageDraw.ImageDraw, text: str, face: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        candidate = " ".join(current + [word])
        if current and width(draw, candidate, face) > max_width:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return lines or [""]


def fit_lines(
    draw: ImageDraw.ImageDraw,
    text: str,
    path: Path,
    start_size: int,
    max_width: int,
    max_lines: int,
    min_size: int = 44,
    index: int = 0,
) -> tuple[ImageFont.FreeTypeFont, list[str]]:
    for size in range(start_size, min_size - 1, -2):
        face = font(path, size, index=index)
        lines = wrap(draw, text, face, max_width)
        if len(lines) <= max_lines:
            return face, lines
    face = font(path, min_size, index=index)
    return face, wrap(draw, text, face, max_width)[:max_lines]


def text_block(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    lines: Iterable[str],
    face: ImageFont.FreeTypeFont,
    fill: str,
    leading: float = 0.95,
    anchor: str = "la",
    align: str = "left",
    stroke_width: int = 0,
    stroke_fill: str | None = None,
) -> int:
    x, y = xy
    step = int(face.size * leading)
    for line in lines:
        draw.text((x, y), line, font=face, fill=fill, anchor=anchor, align=align,
                  stroke_width=stroke_width, stroke_fill=stroke_fill)
        y += step
    return y


def small_caps(draw: ImageDraw.ImageDraw, text: str, xy: tuple[int, int], color: str, size: int = 22) -> None:
    draw.text(xy, text.upper(), font=font(INTER, size), fill=color, spacing=4)


def footer(draw: ImageDraw.ImageDraw, handle: str, index: int, total: int, color: str, rule: str | None = None) -> None:
    if rule:
        draw.line((65, 1272, 1015, 1272), fill=rule, width=2)
    small_caps(draw, handle, (68, 1290), color, 20)
    label = f"SLIDE {index:02d} / {total:02d}"
    face = font(INTER, 19)
    draw.text((1012, 1290), label, font=face, fill=color, anchor="ra")


def spark(draw: ImageDraw.ImageDraw, x: int, y: int, r: int, color: str, width_px: int = 3) -> None:
    draw.line((x - r, y, x + r, y), fill=color, width=width_px)
    draw.line((x, y - r, x, y + r), fill=color, width=width_px)
    draw.line((x - r // 2, y - r // 2, x + r // 2, y + r // 2), fill=color, width=width_px)
    draw.line((x - r // 2, y + r // 2, x + r // 2, y - r // 2), fill=color, width=width_px)


def loose_circle(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], color: str, width_px: int = 3) -> None:
    x1, y1, x2, y2 = box
    pts = []
    for i in range(42):
        theta = 2 * math.pi * i / 41
        wobble = 1 + 0.035 * math.sin(i * 2.7)
        x = (x1 + x2) / 2 + (x2 - x1) / 2 * math.cos(theta) * wobble
        y = (y1 + y2) / 2 + (y2 - y1) / 2 * math.sin(theta) * wobble
        pts.append((x, y))
    draw.line(pts, fill=color, width=width_px, joint="curve")


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str, width_px: int = 5) -> None:
    draw.line((*start, *end), fill=color, width=width_px)
    ex, ey = end
    sx, sy = start
    angle = math.atan2(ey - sy, ex - sx)
    for delta in (2.55, -2.55):
        draw.line((ex, ey, ex + 28 * math.cos(angle + delta), ey + 28 * math.sin(angle + delta)), fill=color, width=width_px)


def render_after_hours(slide: dict, meta: dict, index: int, total: int) -> Image.Image:
    image = gradient(cover_image(resolve_asset(slide["image"]), 0.18, (79, 43, 20, 34)), 18, 168)
    draw = ImageDraw.Draw(image)
    small_caps(draw, slide.get("eyebrow", meta["series"]), (72, 78), "#F1ECE4", 22)
    small_caps(draw, meta.get("location", "THE VALLEY"), (1005, 78), "#F1ECE4", 20)
    headline = slide["headline"]
    face, lines = fit_lines(draw, headline, BODONI, 132 if slide["type"] == "cover" else 112, 900, 5, 66)
    y = 250 if slide["type"] == "cover" else 610
    text_block(draw, (72, y), lines, face, "#FFFFFF", 0.86, stroke_width=1, stroke_fill="#17110D")
    copy = slide.get("body") or slide.get("cta")
    if copy:
        body_face = font(BODONI_STD, 30)
        body_lines = wrap(draw, copy, body_face, 760)
        text_block(draw, (76, 1115), body_lines[:4], body_face, "#F1ECE4", 1.12)
    footer(draw, meta["handle"], index, total, "#F1ECE4")
    return image


def render_sunlit(slide: dict, meta: dict, index: int, total: int) -> Image.Image:
    image = gradient(cover_image(resolve_asset(slide["image"]), 0.17, (25, 43, 26, 45)), 24, 120)
    draw = ImageDraw.Draw(image)
    small_caps(draw, slide.get("eyebrow", meta["series"]), (70, 72), "#F0DB6D", 21)
    headline = slide["headline"]
    face, lines = fit_lines(draw, headline, BODONI_STD, 128 if slide["type"] == "cover" else 108, 820, 5, 62)
    y = 210 if slide["type"] == "cover" else 540
    text_block(draw, (70, y), lines, face, "#F0DB6D", 0.9, stroke_width=1, stroke_fill="#172018")
    if slide.get("body"):
        body_face = font(INTER, 30)
        body_lines = wrap(draw, slide["body"], body_face, 720)
        text_block(draw, (74, 1010), body_lines[:5], body_face, "#FBF8F1", 1.12, stroke_width=1, stroke_fill="#172018")
    if slide.get("cta"):
        note_face = font(SIGNPAINTER, 42)
        draw.text((72, 1110), slide["cta"], font=note_face, fill="#F0DB6D")
    loose_circle(draw, (770, 760, 1010, 1040), "#FBF8F1", 4)
    arrow(draw, (728, 1180), (950, 1170), "#FBF8F1", 4)
    footer(draw, meta["handle"], index, total, "#F0DB6D")
    return image


def render_quiet(slide: dict, meta: dict, index: int, total: int) -> Image.Image:
    image = gradient(cover_image(resolve_asset(slide["image"]), 0.08, (42, 48, 35, 26)), 12, 196)
    draw = ImageDraw.Draw(image)
    small_caps(draw, meta["series"], (72, 70), "#F8F7F2", 18)
    small_caps(draw, slide.get("eyebrow", "A NOTE"), (1005, 70), "#F8F7F2", 18)
    face, lines = fit_lines(draw, slide["headline"], BODONI_STD, 122 if slide["type"] == "cover" else 104, 850, 5, 58)
    y = 190 if slide["type"] == "cover" else 650
    text_block(draw, (72, y), lines, face, "#F8F7F2", 0.92, stroke_width=1, stroke_fill="#171713")
    copy = slide.get("body") or slide.get("cta")
    if copy:
        body_face = font(BODONI_STD, 29)
        body_lines = wrap(draw, copy, body_face, 650)
        text_block(draw, (76, 1060), body_lines[:5], body_face, "#F8F7F2", 1.12)
    footer(draw, meta["handle"], index, total, "#F8F7F2")
    return image


def render_valley_moments(slide: dict, meta: dict, index: int, total: int) -> Image.Image:
    image = gradient(cover_image(resolve_asset(slide["image"]), 0.2, (83, 48, 22, 22)), 20, 170)
    draw = ImageDraw.Draw(image)
    draw.line((55, 64, 1025, 64), fill="#CFC7B8", width=2)
    small_caps(draw, meta["series"], (65, 82), "#FFF8EA", 19)
    small_caps(draw, "•••", (1008, 78), "#FFF8EA", 20)
    face, lines = fit_lines(draw, slide["headline"], INTER, 112, 860, 5, 58)
    y = 235 if slide["type"] == "cover" else 315
    y2 = text_block(draw, (65, y), lines, face, "#F7E174", 0.87, stroke_width=1, stroke_fill="#0B0B0A")
    if slide.get("accent"):
        script = font(SIGNPAINTER, 90)
        draw.text((470, y2 - 20), slide["accent"], font=script, fill="#F7E174", anchor="la", stroke_width=1, stroke_fill="#0B0B0A")
        spark(draw, 945, y2 + 25, 20, "#FFF8EA", 3)
    if slide.get("body"):
        body_face = font(INTER, 31)
        body_lines = wrap(draw, slide["body"], body_face, 610)
        text_block(draw, (68, 1015), body_lines[:5], body_face, "#FFF8EA", 1.05, stroke_width=1, stroke_fill="#0B0B0A")
    if slide.get("cta"):
        body_face = font(INTER, 30)
        body_lines = wrap(draw, slide["cta"], body_face, 650)
        text_block(draw, (68, 1055), body_lines[:4], body_face, "#FFF8EA", 1.08, stroke_width=1, stroke_fill="#0B0B0A")
    footer(draw, meta["handle"], index, total, "#FFF8EA", "#CFC7B8")
    return image


def render_hidden_address(slide: dict, meta: dict, index: int, total: int) -> Image.Image:
    image = gradient(cover_image(resolve_asset(slide["image"]), 0.27, (33, 31, 23, 34)), 20, 176)
    draw = ImageDraw.Draw(image)
    mast = slide.get("eyebrow", meta["series"])
    small_caps(draw, mast, (540, 66), "#F8F4E8", 18)
    face, lines = fit_lines(draw, slide["headline"], BODONI, 122 if slide["type"] == "cover" else 104, 900, 5, 58)
    y = 205 if slide["type"] == "cover" else 170
    text_block(draw, (58, y), lines, face, "#F3DE73", 0.84, stroke_width=1, stroke_fill="#0D0D0B")
    insets = [resolve_asset(value) for value in slide.get("insets", [])]
    if insets:
        sizes = [(410, 290), (410, 290)] if len(insets) == 2 else [(280, 250)] * len(insets)
        start_x = 95 if len(insets) == 2 else 70
        for pos, (path, size) in enumerate(zip(insets, sizes)):
            inset = ImageOps.fit(Image.open(path).convert("RGB"), size, method=Image.Resampling.LANCZOS)
            x = start_x + pos * (size[0] + 30)
            y_inset = 790
            image.paste(inset, (x, y_inset))
            draw.rectangle((x - 4, y_inset - 4, x + size[0] + 4, y_inset + size[1] + 4), outline="#F8F4E8", width=3)
        arrow(draw, (455, 1130), (710, 1030), "#F3DE73", 6)
    copy = slide.get("body") or slide.get("cta")
    if copy:
        body_face = font(BODONI_STD, 29)
        body_lines = wrap(draw, copy, body_face, 780)
        copy_y = 650 if insets else 1040
        text_block(draw, (540, copy_y), body_lines[:5], body_face, "#F8F4E8", 1.1, anchor="ma", align="center")
    if slide["type"] == "close":
        draw.arc((460, 1080, 620, 1190), 15, 165, fill="#F3DE73", width=7)
        draw.ellipse((485, 1100, 495, 1110), fill="#F3DE73")
        draw.ellipse((585, 1100, 595, 1110), fill="#F3DE73")
    footer(draw, meta["handle"], index, total, "#F8F4E8")
    return image


RENDERERS = {
    "after-hours-guide": render_after_hours,
    "sunlit-local-notes": render_sunlit,
    "quiet-home-editorial": render_quiet,
    "valley-moments": render_valley_moments,
    "hidden-address-journal": render_hidden_address,
}


def render_packet(system: str, packet: dict, output_root: Path) -> list[Path]:
    renderer = RENDERERS[system]
    slides = packet["slides"]
    output = output_root / system
    output.mkdir(parents=True, exist_ok=True)
    paths = []
    for index, slide in enumerate(slides, start=1):
        image = renderer(slide, packet, index, len(slides))
        path = output / f"slide-{index:02d}.png"
        image.save(path, "PNG", optimize=True)
        paths.append(path)
    return paths


def contact_sheet(outputs: dict[str, list[Path]], target: Path) -> None:
    thumb_w, thumb_h = 324, 405
    gap, label_h = 22, 62
    sheet_w = gap + 3 * (thumb_w + gap)
    sheet_h = gap + len(outputs) * (label_h + thumb_h + gap)
    sheet = Image.new("RGB", (sheet_w, sheet_h), "#F2EFE9")
    draw = ImageDraw.Draw(sheet)
    y = gap
    names = json.loads((ROOT / "systems.json").read_text())["systems"]
    for system, paths in outputs.items():
        draw.text((gap, y), names[system]["name"], font=font(INTER, 28), fill="#171713")
        y += label_h
        for index, path in enumerate(paths[:3]):
            thumb = Image.open(path).convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            sheet.paste(thumb, (gap + index * (thumb_w + gap), y))
        y += thumb_h + gap
    target.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(target, "JPEG", quality=92, optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="examples/proof-content.json")
    parser.add_argument("--style", choices=sorted(RENDERERS))
    parser.add_argument("--output", default="proofs")
    args = parser.parse_args()

    source = resolve_asset(args.input)
    data = json.loads(source.read_text())
    output_root = resolve_asset(args.output)
    outputs: dict[str, list[Path]] = {}

    if "proofs" in data:
        systems = [args.style] if args.style else list(RENDERERS)
        for system in systems:
            packet = {k: v for k, v in data.items() if k != "proofs"}
            packet.update(data["proofs"][system])
            packet["system"] = system
            outputs[system] = render_packet(system, packet, output_root)
    else:
        system = args.style or data["system"]
        outputs[system] = render_packet(system, data, output_root)

    contact_sheet(outputs, output_root / "jen-five-system-proof-sheet.jpg")
    for system, paths in outputs.items():
        print(f"{system}: {len(paths)} slides")
    print(output_root / "jen-five-system-proof-sheet.jpg")


if __name__ == "__main__":
    main()
