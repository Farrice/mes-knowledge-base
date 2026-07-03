#!/usr/bin/env python3
"""Create reusable AI carousel packages from articles, ideas, or transcripts."""

from __future__ import annotations

import argparse
import json
import re
import textwrap
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
OUT_ROOT = ROOT / "deliverables" / "ai-carousel-engine"


DEFAULT_STYLE = {
    "name": "Premium operator carousel",
    "platform": "Instagram and LinkedIn",
    "aspect_ratio": "4:5 portrait",
    "visual_style": "clean editorial social carousel, premium consulting brand, high contrast typography, generous whitespace, structured visual hierarchy, subtle abstract illustrations, no clutter",
    "palette": ["#101827", "#F8FAFC", "#7C3AED", "#22C55E", "#E5E7EB"],
    "typography": "bold geometric sans headlines, readable modern sans body, small uppercase labels",
    "composition": "one core idea per slide, large headline, one visual anchor, short supporting copy, consistent slide number",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="AI Carousel Content Engine")
    parser.add_argument("--mode", choices=["copy", "prompt", "pack"], default="pack")
    parser.add_argument("--source", help="Path to article/idea markdown or text file.")
    parser.add_argument("--text", help="Raw idea or source text.")
    parser.add_argument("--title", help="Carousel title/topic override.")
    parser.add_argument("--audience", default="consultants, founders, creators, and service businesses")
    parser.add_argument("--mission", choices=["attract", "position", "convert"], default="position")
    parser.add_argument("--out-dir", help="Output directory. Defaults to deliverables/ai-carousel-engine/<slug>.")
    parser.add_argument("--style", help="Optional style brief or reference description.")
    parser.add_argument("--slides", type=int, default=10, help="Target slide count, 7-10 recommended.")
    args = parser.parse_args()

    source_text = load_source(args.source, args.text)
    if not source_text.strip():
        parser.error("Provide --source or --text")

    title = args.title or infer_title(source_text)
    slug = slugify(title)
    out_dir = Path(args.out_dir) if args.out_dir else OUT_ROOT / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    slides = build_slides(source_text, title, args.audience, args.mission, args.slides)
    style = build_style(args.style)
    prompt = build_gpt_image_prompt(title, args.audience, slides, style)

    if args.mode in {"copy", "pack"}:
        write_source(out_dir, source_text, title, args.audience, args.mission)
        write_carousel_script(out_dir, title, slides)
        write_json(out_dir / "slide-brief.json", {"title": title, "audience": args.audience, "mission": args.mission, "slides": slides})

    if args.mode in {"prompt", "pack"}:
        write_json(out_dir / "gpt-image-2-prompt.json", prompt)
        write_style_board(out_dir, style, args.style)

    if args.mode == "pack":
        write_review_checklist(out_dir)
        write_publish_pack(out_dir, title, args.audience, slides)

    print(f"AI carousel package written to: {out_dir}")
    print(f"Slides: {len(slides)}")
    print(f"Mode: {args.mode}")
    return 0


def load_source(source_path: str | None, raw_text: str | None) -> str:
    if source_path:
        return Path(source_path).read_text(encoding="utf-8", errors="ignore")
    return raw_text or ""


def infer_title(text: str) -> str:
    for line in text.splitlines():
        clean = line.strip().strip("#").strip()
        if clean and len(clean) < 90:
            return clean
    words = re.findall(r"[A-Za-z0-9]+", text)
    return " ".join(words[:8]) or "ai-carousel"


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:80] or f"carousel-{int(time.time())}"


def build_slides(source_text: str, title: str, audience: str, mission: str, slide_count: int) -> list[dict[str, Any]]:
    slide_count = max(7, min(10, slide_count))
    insights = extract_insights(source_text)
    core_slots = slide_count - 5
    while len(insights) < core_slots:
        insights.append("Turn the source idea into one clear, reusable action the audience can apply.")

    promise = build_promise(title, audience, mission)
    slides: list[dict[str, Any]] = []
    slides.append(
        slide(
            1,
            "Cover",
            hook_title(title, mission),
            promise,
            "Bold cover with a sharp headline, high contrast type, and one symbolic visual showing transformation.",
        )
    )
    slides.append(
        slide(
            2,
            "Retention Bridge",
            "Most people stop at the content.",
            "The advantage is turning the idea into a repeatable asset system.",
            "Split-screen: raw notes on one side, polished carousel system on the other.",
        )
    )

    for idx in range(core_slots):
        insight = insights[idx]
        slides.append(
            slide(
                len(slides) + 1,
                f"Step {idx + 1}",
                short_headline(insight),
                compress_body(insight),
                visual_for(insight),
            )
        )

    slides.append(
        slide(
            len(slides) + 1,
            "Transformation",
            "Before vs. After",
            "Before: one idea trapped in a long article. After: a swipeable asset that teaches, positions, and routes attention back to your owned platform.",
            "Before/after layout with messy article document transforming into a clean 10-slide carousel grid.",
        )
    )
    slides.append(
        slide(
            len(slides) + 1,
            "Human Review",
            "Do not fully automate taste.",
            "Let the system draft and design fast. Then choose the strongest hook, tighten the copy, and regenerate only the slides that miss.",
            "Human hand selecting one polished slide from three generated options.",
        )
    )
    slides.append(
        slide(
            len(slides) + 1,
            "CTA",
            "Save this workflow.",
            "Use it the next time one article, thought, or client insight deserves to become a visual asset.",
            "Clean final slide with checklist and subtle arrow toward save/share action.",
        )
    )
    return slides[:slide_count]


def extract_insights(text: str) -> list[str]:
    cleaned = re.sub(r"\[[0-9:.]+\]", " ", text)
    cleaned = re.sub(r"(?m)^#{1,6}\s+", "", cleaned)
    candidates = re.split(r"(?<=[.!?])\s+|\n+-\s+|\n+\d+[.)]\s+", cleaned)
    scored: list[tuple[int, str]] = []
    keywords = ["should", "must", "because", "workflow", "system", "prompt", "design", "content", "strategy", "brand", "carousel", "article", "audience", "offer", "client"]
    for candidate in candidates:
        c = re.sub(r"\s+", " ", candidate).strip()
        if len(c) < 45 or len(c) > 340:
            continue
        score = sum(1 for keyword in keywords if keyword in c.lower()) + min(len(c) // 80, 3)
        scored.append((score, c))
    scored.sort(key=lambda item: (-item[0], len(item[1])))
    unique: list[str] = []
    seen = set()
    for _, candidate in scored:
        key = candidate[:80].lower()
        if key not in seen:
            seen.add(key)
            unique.append(candidate)
        if len(unique) >= 8:
            break
    return unique


def build_promise(title: str, audience: str, mission: str) -> str:
    if mission == "convert":
        return f"A practical carousel that shows {audience} why this matters now and what to do next."
    if mission == "attract":
        return f"A swipeable breakdown that makes {audience} stop, understand the idea, and save it."
    return f"A visual authority asset that turns '{title}' into a repeatable, on-brand carousel."


def hook_title(title: str, mission: str) -> str:
    if mission == "convert":
        return f"Stop explaining {title}. Show the system."
    if mission == "attract":
        return f"The {title} playbook people will save."
    return f"Turn {title} into a visual asset."


def short_headline(text: str) -> str:
    text = re.sub(r"^[A-Z][a-z]+:\s*", "", text).strip()
    text = text.lstrip("#").strip()
    words = text.split()
    if len(words) <= 9:
        return text.rstrip(".")
    headline_words = words[:9]
    while headline_words and headline_words[-1].lower().rstrip(".,:;") in {"and", "or", "but", "to", "of", "the", "a", "an"}:
        headline_words.pop()
    return " ".join(headline_words).rstrip(".,:;") + "."


def compress_body(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= 220:
        return text
    return text[:217].rsplit(" ", 1)[0] + "..."


def visual_for(text: str) -> str:
    lower = text.lower()
    if "article" in lower or "blog" in lower:
        return "A long article page breaking into clean carousel cards."
    if "prompt" in lower or "gpt" in lower or "image" in lower:
        return "A structured prompt panel connected to a grid of designed carousel slides."
    if "brand" in lower or "style" in lower:
        return "A brand style board with colors, typography, and reference cards feeding a slide layout."
    if "strategy" in lower or "audience" in lower:
        return "A target audience map connected to a content strategy pathway."
    return "Simple symbolic illustration that makes the slide idea instantly visible."


def slide(number: int, label: str, title: str, body: str, visual: str) -> dict[str, Any]:
    return {
        "number": number,
        "label": label,
        "title": title,
        "body": body,
        "visual": visual,
        "transition": "Swipe for the next step." if number < 10 else "Save and reuse.",
    }


def build_style(style_brief: str | None) -> dict[str, Any]:
    style = dict(DEFAULT_STYLE)
    if style_brief:
        style["name"] = "Custom style from user/reference"
        style["visual_style"] = style_brief
        style["composition"] += " Match the provided reference direction while preserving legibility."
    return style


def build_gpt_image_prompt(title: str, audience: str, slides: list[dict[str, Any]], style: dict[str, Any]) -> dict[str, Any]:
    return {
        "type": "10-slide social media carousel design system",
        "output": {
            "format": "single image containing all carousel slides as separate panels",
            "platform": style["platform"],
            "aspect_ratio": style["aspect_ratio"],
            "slide_count": len(slides),
        },
        "style": style["visual_style"],
        "brand_system": {
            "palette": style["palette"],
            "typography": style["typography"],
            "composition": style["composition"],
        },
        "audience": audience,
        "topic": title,
        "layout_rules": [
            "Create one clearly separated portrait slide panel per carousel slide.",
            "Keep all text exactly as supplied in the slide list.",
            "Every slide gets one hero line only; supporting text must be smaller and readable.",
            "Use consistent margins, slide numbers, and visual motif across all slides.",
            "Where illustrations or photos appear, create new visuals that fit the slide copy and match the same visual style.",
            "Do not overcrowd slides. If copy is long, prioritize hierarchy and line breaks.",
        ],
        "slides": [
            {
                "slide": s["number"],
                "label": s["label"],
                "headline": s["title"],
                "body": s["body"],
                "visual_direction": s["visual"],
            }
            for s in slides
        ],
        "human_review_note": "After generation, review for text accuracy, visual cohesion, brand fit, and whether each slide earns the next swipe.",
    }


def write_source(out_dir: Path, source_text: str, title: str, audience: str, mission: str) -> None:
    content = f"# Source\n\n- Title: {title}\n- Audience: {audience}\n- Mission: {mission}\n\n## Raw Source\n\n{source_text.strip()}\n"
    (out_dir / "source.md").write_text(content, encoding="utf-8")


def write_carousel_script(out_dir: Path, title: str, slides: list[dict[str, Any]]) -> None:
    lines = [f"# Carousel Script: {title}", ""]
    for s in slides:
        lines.extend(
            [
                f"## Slide {s['number']}: {s['label']}",
                f"**Title:** {s['title']}",
                "",
                f"**Body:** {s['body']}",
                "",
                f"**Visual:** {s['visual']}",
                "",
                f"**Transition:** {s['transition']}",
                "",
            ]
        )
    (out_dir / "carousel-script.md").write_text("\n".join(lines), encoding="utf-8")


def write_style_board(out_dir: Path, style: dict[str, Any], custom: str | None) -> None:
    lines = [
        "# Style Board",
        "",
        f"## Name\n{style['name']}",
        "",
        f"## Visual Style\n{style['visual_style']}",
        "",
        "## Palette",
    ]
    lines.extend(f"- `{color}`" for color in style["palette"])
    lines.extend(
        [
            "",
            f"## Typography\n{style['typography']}",
            "",
            f"## Composition\n{style['composition']}",
        ]
    )
    if custom:
        lines.extend(["", "## Custom Reference Direction", custom])
    (out_dir / "style-board.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_review_checklist(out_dir: Path) -> None:
    checklist = """# Carousel Review Checklist

## Copy
- [ ] Slide 1 creates a clear swipe reason.
- [ ] Slide 2 locks the reader into the sequence.
- [ ] Each core slide has one idea only.
- [ ] The final slide asks for the right action.

## Design
- [ ] Text is readable on every slide.
- [ ] Style is consistent across the full set.
- [ ] Visuals support the copy instead of decorating it.
- [ ] The strongest line is visually dominant.

## Evidence And Strategy
- [ ] Claims from source material are not distorted.
- [ ] The carousel routes attention to the owned asset, offer, or next step.
- [ ] Human review happened before publishing.
"""
    (out_dir / "review-checklist.md").write_text(checklist, encoding="utf-8")


def write_publish_pack(out_dir: Path, title: str, audience: str, slides: list[dict[str, Any]]) -> None:
    caption = textwrap.dedent(
        f"""
        # Publish Pack

        ## Caption Draft
        {slides[0]['title']}

        Most people leave good ideas trapped in long-form content.
        This carousel turns one source into a visual asset people can save, share, and use.

        Save this if you want a faster way to turn insight into distribution.

        ## Platform Notes
        - Instagram: use stronger visual contrast and shorter caption.
        - LinkedIn: use the caption to add behind-the-scenes context and a soft CTA.
        - Client delivery: include `carousel-script.md`, `gpt-image-2-prompt.json`, and `review-checklist.md`.

        ## CTA Options
        - Save this for your next content sprint.
        - Comment `CAROUSEL` if you want the workflow.
        - Read the full article on the owned site.

        ## Audience
        {audience}
        """
    ).strip()
    (out_dir / "publish-pack.md").write_text(caption + "\n", encoding="utf-8")


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
