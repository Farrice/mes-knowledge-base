#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Image-medium conference — the soft sibling of Check B (r6-1-estilo, case 1).

Where Check A/B/C/D are hard GATES (exit 2 → the builder re-rolls), this is a
**conference that WARNS, never blocks** — the same posture the quality-gate's palette
check already takes (`shared/quality-gate.md`: a palette stray "warns (surfaces it for the
human); it does NOT auto-recolor"). The MEDIUM (photo / flat-illustration / watercolor /
sketch / 3d-render) is a JUDGMENT call read from each template's own ref — the marca fixes
the IDENTITY (palette / accent / grain), the STYLE (medium / lighting / treatment) is the
ref's (r6 freed lighting + treatment per-template alongside the medium; this conference covers
the medium, the lighting/treatment sibling is a logged follow-up). Per the authoring principle
(`_Desenho.md` §4: default suave → the example rules → the conference CONFIRMS, warning on
judgment and hard-failing only the non-negotiable), an inverted medium is a WARNING, not a
re-roll.

WHAT IT COMPARES (text-first, deterministic):
  - the medium the rationale §2 RECORDS for the image block (`medium: …`, read from the ref);
  - the medium the generation prompt ASKS FOR (the `[ai-image-zone]` `prompt_delta` terms in
    template.html — "flat vector illustration" / "documentary photograph" / "watercolor" / …).
  When the rationale §2 is silent on `medium`, the brand `ai-image-style.md` `default_medium`
  is used as the soft fallback (the "ambiguous ref" path) — and a `default_medium: mixed`
  brand never warns (a mixed brand legitimately ships any medium).

THE ONE WARNING: the prompt's medium INVERTS the ref's — the run-07 `services-billboard`
miss, where ref-04 is a flat cartoon but the prompt opened "documentary photograph …" (the
brand grade crava'd one medium brand-wide). That is a WARN the human sees, never a block.

NOT here (logged follow-ups):
  - a VISUAL cartoon-vs-photo classifier on the rendered preview (read the pixels, not the
    text). This conference is text-first — it reads the declared medium vs the prompted medium.
    The pixel classifier is the deeper, costlier read; deliberately deferred, like Check B's
    full per-block pixel comparator.
  - a parallel LIGHTING / SUBJECT_TREATMENT conference. The r6 image-style redesign freed those
    two fields per-template alongside the medium (read into rationale §2 `lighting:` /
    `subject_treatment:`, written to the block's `image_style`). A deterministic TEXT read for
    them is fuzzier than for the medium (lighting/treatment vocab overlaps prose far more than
    "photograph" vs "illustration"), so a substring conference would over-warn and risk becoming
    a new pedra (`_Desenho.md` §4). Kept medium-only here and deferred — the design sanctions
    "leave medium-only + note as follow-up". The builder/craft docs carry the same note.

Exit codes (this gate NEVER blocks — it is advisory):
  0  -> always when it ran (clean OR a medium-mismatch WARNING). A warning prints to stderr;
        exit stays 0 so the build is not re-rolled on a judgment call.
  1  -> usage / file-not-found error only.

Usage:
    uv run check_image_medium.py --rationale <dir>/rationale.md \
        --template-html <dir>/template.html [--ai-image-style <brand>/ai-image-style.md]
"""
import argparse
import re
import sys
from pathlib import Path


def _force_utf8_streams() -> None:
    """UTF-8 stdout/stderr so medium glyphs never crash a cp1252 Windows console."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


# ---------------------------------------------------------------------------------------
# Medium vocabulary — each canonical medium + the surface terms that name it in a ref read
# or a prompt opener. Coarse + deterministic (substring match on lowercased text), the same
# altitude as Check B's hint tables. `mixed` is a brand-level value, not a per-image medium.
# ---------------------------------------------------------------------------------------
PHOTO = "photo"
ILLUSTRATION = "illustration"
WATERCOLOR = "watercolor"
SKETCH = "sketch"
RENDER_3D = "3d-render"
MIXED = "mixed"

# Ordered longest/most-specific first so "flat illustration" wins over a bare "flat", and
# "3d render" / "photorealistic 3d" classify as RENDER_3D before the generic PHOTO terms.
MEDIUM_TERMS: list[tuple[str, tuple[str, ...]]] = [
    (RENDER_3D, ("3d-render", "3d render", "3d-rendered", "3d rendered", "photorealistic 3d",
                 "rendered 3d", "cgi render", "octane render", "blender render")),
    (WATERCOLOR, ("watercolor", "watercolour", "gouache", "ink-wash", "ink wash")),
    (SKETCH, ("pencil sketch", "hand-drawn sketch", "hand drawn sketch", "line drawing",
              "line-art sketch", "charcoal sketch", "doodle")),
    (ILLUSTRATION, ("flat vector illustration", "vector illustration", "flat illustration",
                    "flat-illustration", "flat vector", "cartoon", "illustration",
                    "illustrated", "vector art", "comic", "anime", "drawn illustration")),
    (PHOTO, ("documentary photograph", "documentary photo", "photorealistic",
             "photo-realistic", "photograph", "photographic", "dslr", "candid photo",
             "studio photo", "real photo", "lifelike photo", "photo")),
]

# A medium-negative in a prompt ("no illustration", "no photographs") that CONTRADICTS the
# ref's medium is itself an inversion signal — the run-07 grade carried "no illustration" over
# a cartoon brand. Map the canonical medium → the negative phrasings that forbid it.
MEDIUM_NEGATIVES: dict[str, tuple[str, ...]] = {
    ILLUSTRATION: ("no illustration", "no illustrations", "not an illustration", "no cartoon",
                   "no cartoons", "no vector art", "not illustrated"),
    PHOTO: ("no photograph", "no photographs", "no photo", "not a photograph",
            "no photorealism", "not photographic"),
    WATERCOLOR: ("no watercolor", "no watercolour", "no painting"),
    SKETCH: ("no sketch", "no doodle", "no line drawing"),
    RENDER_3D: ("no 3d", "no 3d render", "no cgi"),
}


def canonical_medium(value: str) -> str | None:
    """Map a free-text medium string (a §2 `medium:` value or a `default_medium:` value) to a
    canonical token, or None if it names no known medium. `mixed` maps to MIXED."""
    if value is None:
        return None
    v = value.strip().lower()
    if not v:
        return None
    if "mixed" in v:
        return MIXED
    for canon, terms in MEDIUM_TERMS:
        if any(t in v for t in terms):
            return canon
    return None


def mediums_in_text(text: str) -> list[str]:
    """Every canonical medium whose surface terms appear in a blob of prompt text, most-specific
    first, de-duplicated. Used to read what the `prompt_delta` ASKS for."""
    if not text:
        return []
    low = text.lower()
    found: list[str] = []
    for canon, terms in MEDIUM_TERMS:
        if canon in found:
            continue
        if any(t in low for t in terms):
            found.append(canon)
    return found


def negated_mediums_in_text(text: str) -> list[str]:
    """Every canonical medium a prompt's NEGATIVES forbid (e.g. 'no illustration' → ILLUSTRATION)."""
    if not text:
        return []
    low = text.lower()
    out: list[str] = []
    for canon, negs in MEDIUM_NEGATIVES.items():
        if any(n in low for n in negs):
            out.append(canon)
    return out


# ---------------------------------------------------------------------------------------
# Rationale §2 parsing — the ref's recorded medium. Self-contained (no numpy/Pillow import):
# scope to the per-block section, then read the image-block `medium:` line.
# ---------------------------------------------------------------------------------------

def _section_body(text: str, header_re: str) -> str | None:
    """Body of the first markdown section whose header matches header_re (header → next header)."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        m = re.match(r"^\s{0,3}#{1,6}\s+(.*\S)\s*$", line)
        if m and re.search(header_re, m.group(1), re.IGNORECASE):
            start = i + 1
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start, len(lines)):
        if re.match(r"^\s{0,3}#{1,6}\s+\S", lines[j]):
            end = j
            break
    return "\n".join(lines[start:end])


def per_block_section(text: str) -> str:
    """The §2 per-block body (where the image block's `medium:` read lives); whole text if absent."""
    body = _section_body(text, r"per[\s-]?block|block breakdown|block treatment")
    return body if body is not None else text


# `medium: flat-illustration` / `medium = photo` / `**medium:** flat vector illustration — why`.
# Capture up to an em/en-dash (the "why" that follows on the line) or end of line.
_MEDIUM_LINE_RE = re.compile(
    r"medium\s*[:=]\s*\**\s*([^\n—–]+)", re.IGNORECASE)


def rationale_medium(text: str) -> str | None:
    """The canonical medium the rationale §2 records for the image block, or None when it records
    none. Reads the FIRST `medium:` line in §2 (the image-block line)."""
    body = per_block_section(text)
    m = _MEDIUM_LINE_RE.search(body)
    if not m:
        return None
    return canonical_medium(m.group(1))


# ---------------------------------------------------------------------------------------
# template.html — the prompt_delta the model actually receives (mirrors check_treatment_contract).
# ---------------------------------------------------------------------------------------

def parse_prompt_delta(html: str) -> str:
    """Concatenate every [ai-image-zone] block's `prompt_delta:` text from template.html — the
    prompt the model receives. Same extraction as Check B's parse_prompt_delta."""
    out: list[str] = []
    blocks = re.findall(r"\[ai-image-zone.*?\[/ai-image-zone\]", html, re.IGNORECASE | re.DOTALL)
    targets = blocks or ([html] if "prompt_delta" in html.lower() else [])
    for block in targets:
        m = re.search(
            r"prompt_delta\s*:\s*\|?\s*(.*?)"
            r"(?=^\s*(?:variables|output_aspect|ref_input|brand_style_source|slot_path|"
            r"generation_route|output|generated)\s*:|\[/ai-image-zone\]|\Z)",
            block, re.IGNORECASE | re.DOTALL | re.MULTILINE)
        if m:
            out.append(m.group(1).strip())
    return "\n".join(out)


def has_ai_image_zone(html: str) -> bool:
    """True when template.html declares an [ai-image-zone…] block (AI generation happens)."""
    return bool(re.search(r"\[ai-image-zone", html, re.IGNORECASE))


# ---------------------------------------------------------------------------------------
# ai-image-style.md — the soft brand default_medium (fallback when the ref is ambiguous).
# ---------------------------------------------------------------------------------------

_DEFAULT_MEDIUM_RE = re.compile(r"default_medium\s*[:=]\s*([^\n#]+)", re.IGNORECASE)
_LEGACY_MEDIUM_RE = re.compile(r"^\s*medium\s*[:=]\s*([^\n#]+)", re.IGNORECASE | re.MULTILINE)


def brand_default_medium(style_text: str) -> str | None:
    """The brand's canonical `default_medium` from ai-image-style.md (the soft fallback). Falls
    back to a legacy `medium:` key if a pre-r6 brand file still carries one. None if neither."""
    if not style_text:
        return None
    m = _DEFAULT_MEDIUM_RE.search(style_text)
    if m:
        return canonical_medium(m.group(1))
    m = _LEGACY_MEDIUM_RE.search(style_text)
    if m:
        return canonical_medium(m.group(1))
    return None


# ---------------------------------------------------------------------------------------
# The verdict (pure — unit-tested).
# ---------------------------------------------------------------------------------------

def evaluate(rationale_text: str, html: str, style_text: str | None = None) -> dict:
    """Compare the ref's recorded medium against the prompt's medium. Returns a verdict dict.

    `ref_medium` resolves from rationale §2 `medium:`; when §2 is silent it falls back to the
    brand `default_medium` (the ambiguous-ref path). A `mixed` ref-medium (brand default mixed,
    §2 silent) never warns — a mixed brand may ship any medium. The single warning fires when
    the prompt asks for a DIFFERENT concrete medium than the ref records (or a prompt negative
    forbids the ref's medium). Advisory: the verdict carries `warn`, never a block.
    """
    ai_zone = has_ai_image_zone(html)
    prompt_delta = parse_prompt_delta(html)

    declared = rationale_medium(rationale_text)
    default = brand_default_medium(style_text) if style_text else None
    # The ref's effective medium: what §2 records, else the soft brand default (ambiguous ref).
    ref_medium = declared if declared is not None else default
    ref_source = ("rationale §2" if declared is not None
                  else ("ai-image-style default_medium" if default is not None else None))

    prompt_mediums = mediums_in_text(prompt_delta)
    prompt_negated = negated_mediums_in_text(prompt_delta)

    warn: str | None = None

    # Only a conference when there is an AI image zone with a prompt to read AND a ref medium to
    # compare it to. No zone / no prompt / no recorded medium → nothing to confer on (clean).
    if ai_zone and prompt_delta and ref_medium is not None and ref_medium != MIXED:
        # (a) the prompt asks for a concrete medium that is NOT the ref's, and does NOT also ask
        #     for the ref's medium (a prompt naming BOTH is a mixed/explicit case — don't warn).
        divergent = [m for m in prompt_mediums if m != ref_medium]
        if divergent and ref_medium not in prompt_mediums:
            warn = (
                f"the ref's medium is '{ref_medium}' ({ref_source}) but the prompt_delta asks "
                f"for '{divergent[0]}' — the prompt inverts the example's medium (the run-07 "
                f"services-billboard miss: a cartoon ref prompted as a documentary photograph). "
                f"The marca fixes the IDENTITY (palette/accent/grain); the MEDIUM is read from "
                f"THIS ref. Open the prompt in '{ref_medium}' (or, if this ref is genuinely that "
                f"other medium, fix the §2 `medium:` read). Medium is judgment — this WARNS, it "
                f"does not block.")
        # (b) the prompt forbids the ref's own medium via a negative (the grade's "no illustration"
        #     over a cartoon brand) — same inversion, surfaced even if no positive medium term hit.
        elif ref_medium in prompt_negated:
            warn = (
                f"the ref's medium is '{ref_medium}' ({ref_source}) but the prompt_delta carries "
                f"a medium-negative that forbids it (e.g. 'no {ref_medium}') — the brand grade's "
                f"blanket negative kills this ref's own medium (the run-07 miss). Drop the "
                f"medium-negative; the medium is the ref's call. WARNS, does not block.")

    return {
        "ai_zone": ai_zone,
        "ref_medium": ref_medium,
        "ref_source": ref_source,
        "declared_medium": declared,
        "default_medium": default,
        "prompt_mediums": prompt_mediums,
        "prompt_negated": prompt_negated,
        "warn": warn,
        "ok": warn is None,  # ok == "no warning"; either way the gate exits 0 (advisory).
    }


def main() -> int:
    _force_utf8_streams()
    ap = argparse.ArgumentParser(
        description="Image-medium conference — WARNS (never blocks) when the prompt's medium "
                    "inverts the ref's recorded medium.")
    ap.add_argument("--rationale", required=True, type=Path)
    ap.add_argument("--template-html", required=True, type=Path)
    ap.add_argument("--ai-image-style", type=Path, default=None,
                    help="brand ai-image-style.md for the default_medium fallback (used only "
                         "when rationale §2 records no `medium:`). Default: auto-discovered at "
                         "brand_context/visual-identity/ai-image-style.md walking up from "
                         "--template-html/--rationale.")
    args = ap.parse_args()

    if not args.rationale.exists():
        print(f"Error: rationale not found: {args.rationale}", file=sys.stderr)
        return 1
    if not args.template_html.exists():
        print(f"Error: template.html not found: {args.template_html}", file=sys.stderr)
        return 1

    rationale_text = args.rationale.read_text(encoding="utf-8")
    html = args.template_html.read_text(encoding="utf-8")

    # Resolve ai-image-style.md (explicit, else auto-discover up from the template/rationale path).
    style_path = args.ai_image_style or _discover_ai_image_style(args.template_html, args.rationale)
    style_text = None
    if style_path is not None and style_path.exists():
        style_text = style_path.read_text(encoding="utf-8")

    res = evaluate(rationale_text, html, style_text)

    print(f"Image-medium conference on {args.rationale.name}:")
    print(f"  ai_zone={res['ai_zone']}  ref_medium={res['ref_medium'] or '?'} "
          f"({res['ref_source'] or 'none'})  prompt_mediums={res['prompt_mediums'] or '[]'}")
    if res["warn"] is None:
        print("  verdict = OK (medium consistent / nothing to confer)")
    else:
        print("  verdict = WARN (advisory — does NOT block the build)")
        print(f"[warn] {res['warn']}", file=sys.stderr)
    return 0  # advisory: NEVER a non-zero block on a judgment call.


def _discover_ai_image_style(*anchors: Path) -> Path | None:
    """Walk up from each anchor to a brand_context/visual-identity/ai-image-style.md."""
    for anchor in anchors:
        if anchor is None:
            continue
        for anc in anchor.resolve().parents:
            candidates = [anc / "brand_context" / "visual-identity" / "ai-image-style.md"]
            if anc.name == "brand_context":
                candidates.insert(0, anc / "visual-identity" / "ai-image-style.md")
            for cand in candidates:
                if cand.is_file():
                    return cand
    return None


if __name__ == "__main__":
    sys.exit(main())
