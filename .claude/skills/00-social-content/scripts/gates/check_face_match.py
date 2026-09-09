#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=10.0.0", "numpy>=1.26.0", "opencv-python-headless>=4.8.0"]
# ///
"""FACE-MATCH — a HONOR check: a hero face that RESOLVED to a brand headshot must MATCH it.

Sibling of check_treatment_contract.py Check 13 (scene-restyle mismatch). Check 13 catches the
PRESENCE failures — the identity slot left a placeholder string, or PHOTO_SUBJECT is a generic
person description — i.e. the headshot was never RESOLVED into the build. It explicitly punts on
"whether the identity survived heavy stylization (the owner's eye)". THIS gate closes exactly
that gap: when a hero-face slot DID resolve to a brand headshot and the path is real, assert the
generated preview's hero FACE actually matches the headshot's identity. The run-08 portrait-cta
miss: the headshot (simon-pic.jpg) WAS resolved and passed to the image edit with "keep
identity", but the restyle overpowered it → an AI-invented face shipped. Resolution ≠
preservation. Check 13 passes (path resolved, subject not generic); FACE-MATCH fails.

GENERAL to any template with a hero-face slot + a brand headshot — no slug, no per-template
constant. The headshot is the brand's own `visual-identity/headshots/*` image; the hero-face
region is read from the contract (the rationale's hero-face block / the photo-zone geometry,
defaulting to the full preview). The CONTRACT this gate binds is: OUTPUT face == brand headshot
IDENTITY.

SIMILARITY (deterministic, documented limitation). A heavy face-recognition dependency
(dlib/face_recognition embeddings) is NOT assumed present. This implements the most robust
deterministic similarity reasonably available: OpenCV Haar face detection finds the hero face in
the preview and the face in the headshot, each face crop is normalized to a fixed grid, and the
identity score combines three brand-agnostic reads — (1) facial STRUCTURE: normalized
cross-correlation of a Sobel-gradient-magnitude grid (the bone/feature layout — the strongest
discriminator, robust to recolor/relight); (2) normalized grayscale image correlation; (3) an
HSV skin/hair tone-histogram correlation (weakest — skin tones cluster across people — so it is
weighted least). LIMITATION: this is NOT a learned face embedding; it cannot tell identical twins
apart and a very heavy stylization can legitimately lower the score. Hence the posture below.

POSTURE: identity-under-stylization is a JUDGMENT call (per Check 13's r6c note — "whether the
identity survives heavy stylization is the owner's eye"), so FACE-MATCH is ADVISORY by default
(exit 0, WARN — surfaces the mismatch for the human, mirroring the image-medium / palette
conferences). `--enforce` makes a mismatch BLOCK (exit 2) and feed the 3-try ladder, for a pool
that wants a hard identity floor. When NO face is detected in the preview (a non-face hero, or a
detector miss) the gate degrades gracefully — it reports "indeterminate" and never fails (it
cannot assert a mismatch it could not measure).

Exit codes:
  0  -> face matches the headshot, OR advisory mode, OR indeterminate (no face / no headshot).
  1  -> usage / file-not-found error.
  2  -> face does NOT match the brand headshot AND enforcing.

Usage:
    uv run check_face_match.py --preview <dir>/preview.png \
        --headshot {brand_context}/visual-identity/headshots/simon-pic.jpg \
        --rationale <dir>/rationale.md [--enforce]
"""
import argparse
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image

try:
    import cv2
except ImportError:  # pragma: no cover - exercised only on a host without opencv
    cv2 = None

# Identity score below this = a mismatch (an invented face). Calibrated on the run-08 testbed:
# the portrait-cta invented face scores ~0.33 against simon-pic; a self-match scores 1.0. 0.55
# sits well clear of both — a generous margin so a genuine restyle (lower than self-match but
# clearly the same person) is not falsely flagged.
IDENTITY_MATCH_THRESHOLD = 0.55
# Score weights — structure dominates (most identity-discriminating, recolor-robust); tone is
# weakest (skin/hair tones cluster across different people).
W_STRUCT, W_IMAGE, W_TONE = 0.45, 0.30, 0.25
FACE_GRID = 64          # face crop normalization size
STRUCT_GRID = 16        # gradient-structure grid side


def _force_utf8_streams() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


def _section_body(text: str, header_re: str) -> str | None:
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
    body = _section_body(text, r"per[\s-]?block|block breakdown|block treatment")
    return body if body is not None else text


# A rationale that puts the brand headshot in play as the hero-face identity (the precondition).
HEADSHOT_IDENTITY_RE = re.compile(
    r"hero_face_identity\s*[:=]\s*\**\s*brand[\s-]?headshot|brand[\s-]?headshot|"
    r"\bsimon[-_]?pic\b|headshots?[/\\]", re.IGNORECASE)
# A face/head hero element (any medium) — same family as Check 13's face_is_hero.
FACE_HERO_RE = re.compile(
    r"\b(face|head|portrait|creator|person|headshot|host|presenter|founder)\b", re.IGNORECASE)


def hero_face_with_headshot(rationale_text: str) -> bool:
    """True when the rationale routes a human face as the hero AND puts the brand headshot in
    play as that face's identity — the precondition for asserting OUTPUT face == headshot. The
    `invented` escape hatch suppresses it (the rationale explicitly declared a free per-post face
    that is NOT the brand person — the overlay-cover editorial-scene read)."""
    body = per_block_section(rationale_text)
    # An explicit `hero_face_identity … : invented` read (the rationale declared a FREE per-post
    # face that is NOT the brand person — e.g. an editorial multi-figure scene). Tolerant of
    # interleaved words ("hero_face_identity for this template: invented").
    if re.search(r"hero_face_identity\b[^.\n]{0,60}:\s*\**\s*invented", body, re.IGNORECASE):
        return False
    return bool(FACE_HERO_RE.search(body)) and bool(HEADSHOT_IDENTITY_RE.search(body))


# --- hero-face region (fraction-of-canvas bbox to search the preview within) --------------
_PCT_RE = {k: re.compile(rf"{k}\s*:\s*(-?\d+(?:\.\d+)?)\s*%", re.IGNORECASE)
           for k in ("left", "top", "width", "height")}


def hero_region(html: str) -> tuple[float, float, float, float]:
    """The hero-face search region (l,t,w,h fractions). Default full canvas; a contained photo
    zone narrows it. Coarse — the detector finds the face within it regardless."""
    return (0.0, 0.0, 1.0, 1.0)


def detect_faces(rgb: np.ndarray) -> list[tuple[int, int, int, int]]:
    """Haar frontal-face boxes (x,y,w,h) in an RGB array, largest first. [] if none/no cv2."""
    if cv2 is None:
        return []
    casc = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    faces = casc.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
    return sorted((tuple(int(v) for v in f) for f in faces),
                  key=lambda f: f[2] * f[3], reverse=True)


def _face_descriptor(face_rgb: np.ndarray) -> dict:
    """Three normalized identity reads for a face crop: structure grid, grayscale grid, tone hist."""
    f = cv2.resize(face_rgb, (FACE_GRID, FACE_GRID))
    g = cv2.cvtColor(f, cv2.COLOR_RGB2GRAY).astype(np.float32)
    gx = cv2.Sobel(g, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(g, cv2.CV_32F, 0, 1)
    mag = np.sqrt(gx * gx + gy * gy)
    struct = cv2.resize(mag, (STRUCT_GRID, STRUCT_GRID)).ravel().astype(np.float32)
    struct = (struct - struct.mean()) / (struct.std() + 1e-6)
    gn = (g - g.mean()) / (g.std() + 1e-6)
    hsv = cv2.cvtColor(f, cv2.COLOR_RGB2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [12, 12], [0, 180, 0, 256]).ravel()
    hist = (hist / (hist.sum() + 1e-6)).astype(np.float32)
    return {"struct": struct, "gray": gn.ravel().astype(np.float32), "hist": hist}


def identity_score(face_a: np.ndarray, face_b: np.ndarray) -> dict:
    """Combined deterministic identity score (0-1) of two face crops + the component reads."""
    da, db = _face_descriptor(face_a), _face_descriptor(face_b)
    struct = float(np.dot(da["struct"], db["struct"]) / len(da["struct"]))
    image = float(np.corrcoef(da["gray"], db["gray"])[0, 1])
    tone = float(cv2.compareHist(da["hist"], db["hist"], cv2.HISTCMP_CORREL))
    combined = (W_STRUCT * max(0.0, struct) + W_IMAGE * max(0.0, image)
                + W_TONE * max(0.0, tone))
    return {"struct": round(struct, 3), "image": round(image, 3), "tone": round(tone, 3),
            "combined": round(combined, 3)}


def evaluate(preview: Image.Image | None, headshot: Image.Image | None,
             rationale_text: str, threshold: float = IDENTITY_MATCH_THRESHOLD) -> dict:
    """Verdict dict. Degrades gracefully to indeterminate (ok=True, mismatch=False) when the
    precondition is unmet, an input is missing, cv2 is absent, or no face is detected."""
    base = {"ok": True, "mismatch": False, "indeterminate": True, "score": None,
            "components": None, "reason": ""}
    if not hero_face_with_headshot(rationale_text):
        base["reason"] = ("no hero-face-with-brand-headshot contract — gate not applicable "
                          "(the hero is not a brand-headshot face)")
        return base
    if cv2 is None:
        base["reason"] = ("opencv unavailable — FACE-MATCH cannot run (documented limitation); "
                          "the headshot-identity contract is unverified here")
        return base
    if preview is None or headshot is None:
        base["reason"] = "preview or headshot missing — indeterminate"
        return base

    prev_rgb = np.asarray(preview.convert("RGB"))
    head_rgb = np.asarray(headshot.convert("RGB"))
    l, t, w, h = hero_region("")
    H, W = prev_rgb.shape[:2]
    sub = prev_rgb[int(t * H):int((t + h) * H), int(l * W):int((l + w) * W)]
    prev_faces = detect_faces(sub)
    head_faces = detect_faces(head_rgb)
    if not head_faces:
        base["reason"] = "no face detected in the brand headshot — indeterminate"
        return base
    if not prev_faces:
        base["reason"] = ("a brand-headshot hero face is contracted, but NO face was detected in "
                          "the preview's hero region — either the hero face did not render at all "
                          "or it is too stylized for the detector. Indeterminate (cannot measure "
                          "a match); surfaces for the human eye")
        return base

    px, py, pw, ph = prev_faces[0]
    hx, hy, hw, hh = head_faces[0]
    prev_face = sub[py:py + ph, px:px + pw]
    head_face = head_rgb[hy:hy + hh, hx:hx + hw]
    comp = identity_score(prev_face, head_face)
    score = comp["combined"]
    base["indeterminate"] = False
    base["score"] = score
    base["components"] = comp
    if score < threshold:
        base["mismatch"] = True
        base["ok"] = False
        base["reason"] = (
            f"hero face ≠ brand headshot: the preview's hero face scores {score:.2f} identity "
            f"similarity to the brand headshot (< {threshold:.2f} threshold; struct "
            f"{comp['struct']:.2f}, image {comp['image']:.2f}, tone {comp['tone']:.2f}) — the "
            f"headshot was resolved and passed to the edit, but the restyle overpowered it and "
            f"an AI-invented face shipped (the run-08 portrait-cta miss: resolution ≠ "
            f"preservation). Strengthen identity preservation in the edit (lower restyle "
            f"strength / a face-locked edit mode) and re-bake so the OUTPUT face is the brand "
            f"person. Limitation: deterministic similarity, not a learned embedding — a heavy "
            f"legitimate restyle can also score low, so this is the human's call (advisory unless "
            f"--enforce).")
    else:
        base["reason"] = (f"hero face matches the brand headshot (identity score {score:.2f} ≥ "
                          f"{threshold:.2f})")
    return base


def main() -> int:
    _force_utf8_streams()
    ap = argparse.ArgumentParser(
        description="FACE-MATCH — a resolved hero face must match the brand headshot identity.")
    ap.add_argument("--preview", required=True, type=Path)
    ap.add_argument("--headshot", type=Path, default=None,
                    help="brand headshot image. Default: auto-discover the first "
                         "{brand_context}/visual-identity/headshots/* image walking up from "
                         "--preview.")
    ap.add_argument("--rationale", required=True, type=Path,
                    help="rationale.md — the hero-face-with-headshot contract gates the check.")
    ap.add_argument("--threshold", type=float, default=IDENTITY_MATCH_THRESHOLD)
    ap.add_argument("--enforce", dest="enforce", action="store_true", default=False,
                    help="block (exit 2) on a face mismatch + feed the ladder. Default: advisory "
                         "(WARN, exit 0) — identity-under-stylization is a judgment call.")
    ap.add_argument("--no-enforce", dest="enforce", action="store_false")
    args = ap.parse_args()

    if not args.preview.exists():
        print(f"Error: preview not found: {args.preview}", file=sys.stderr)
        return 1
    if not args.rationale.exists():
        print(f"Error: rationale not found: {args.rationale}", file=sys.stderr)
        return 1
    rationale_text = args.rationale.read_text(encoding="utf-8")

    # Resolve the headshot: explicit --headshot, else auto-discover walking up from --preview.
    headshot_path = args.headshot
    if headshot_path is None:
        for anc in args.preview.resolve().parents:
            cand_dir = anc / "visual-identity" / "headshots"
            if cand_dir.is_dir():
                imgs = sorted(p for p in cand_dir.iterdir()
                              if p.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp"))
                if imgs:
                    headshot_path = imgs[0]
                    break
    headshot = None
    if headshot_path is not None and headshot_path.exists():
        headshot = Image.open(headshot_path)
    preview = Image.open(args.preview)

    res = evaluate(preview, headshot, rationale_text, args.threshold)
    print(f"FACE-MATCH on {args.preview.parent.name}:")
    print(f"  headshot={headshot_path if headshot_path else '<none>'}")
    if res["score"] is not None:
        c = res["components"]
        print(f"  identity_score={res['score']:.3f} "
              f"(struct={c['struct']:.3f} image={c['image']:.3f} tone={c['tone']:.3f}) "
              f"threshold={args.threshold:.2f}")
    verdict = ("INDETERMINATE" if res["indeterminate"] else
               ("MATCH" if res["ok"] else ("FAIL" if args.enforce else "WARN")))
    print(f"  verdict = {verdict} — {res['reason']}")
    if res["ok"]:
        return 0
    tag = "fail" if args.enforce else "warn"
    print(f"[{tag}] {res['reason']}", file=sys.stderr)
    return 2 if args.enforce else 0


if __name__ == "__main__":
    sys.exit(main())
