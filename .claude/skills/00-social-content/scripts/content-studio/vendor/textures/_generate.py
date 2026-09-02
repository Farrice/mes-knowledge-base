#!/usr/bin/env python3
"""Generate the curated post-production texture set for Content Studio.

These are the texture *overlay assets* the editor and the bake share — there were
NONE in the pack before (viz-image-gen only had texture *prompt words*), so this
authors a small, light, curated set (AIOS-139 Addendum 5, confirmed with the PM).

Design:
  * 256x256 grayscale tiles, applied with ``background-repeat: repeat`` so grain stays
    crisp at the slide's native resolution and tiles seamlessly (small files, ~tens of KB).
  * Mostly-LIGHT (near-white with darker detail) so the default ``multiply`` blend reads
    as a subtle darkening texture; the user can switch blend mode + intensity per slide.
  * Deterministic (fixed seed) so re-running reproduces byte-stable assets.

Run:  python _generate.py    (writes paper.png, film-grain.png, … beside this file)
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

SIZE = 256
OUT = Path(__file__).resolve().parent
RNG = np.random.default_rng(13917)  # fixed seed → reproducible


def _save(name: str, arr: np.ndarray) -> None:
    img = Image.fromarray(np.clip(arr, 0, 255).astype("uint8"), mode="L")
    img.save(OUT / f"{name}.png", optimize=True)


def paper() -> np.ndarray:
    # soft fibrous paper: light base + low-amplitude fine + low-freq blotch
    base = np.full((SIZE, SIZE), 238.0)
    fine = RNG.normal(0, 6, (SIZE, SIZE))
    coarse = RNG.normal(0, 10, (SIZE // 8, SIZE // 8))
    coarse = np.array(Image.fromarray(coarse).resize((SIZE, SIZE), Image.BILINEAR))
    return base + fine + coarse


def film_grain() -> np.ndarray:
    # fine analog grain, light
    return np.full((SIZE, SIZE), 214.0) + RNG.normal(0, 20, (SIZE, SIZE))


def halftone() -> np.ndarray:
    # regular dot grid (period divides 256 → seamless), light bg + soft gray dots
    arr = np.full((SIZE, SIZE), 244.0)
    yy, xx = np.mgrid[0:SIZE, 0:SIZE]
    period = 8
    cx, cy = xx % period, yy % period
    d = np.hypot(cx - period / 2, cy - period / 2)
    arr[d < 2.1] = 150.0
    return arr


def grunge() -> np.ndarray:
    # sparse dark specks + a few faint scratches on white
    arr = np.full((SIZE, SIZE), 250.0)
    speck = RNG.random((SIZE, SIZE))
    arr[speck < 0.012] -= RNG.uniform(60, 150, arr[speck < 0.012].shape)
    for _ in range(6):  # faint vertical-ish scratches
        x = RNG.integers(0, SIZE)
        arr[:, x] -= 30
    return arr


def canvas() -> np.ndarray:
    # woven crosshatch (sine grid), light
    yy, xx = np.mgrid[0:SIZE, 0:SIZE]
    weave = (np.sin(xx / 256 * np.pi * 32) + np.sin(yy / 256 * np.pi * 32)) * 7
    return np.full((SIZE, SIZE), 226.0) + weave


def riso() -> np.ndarray:
    # coarse print stipple: blocky low-res noise upscaled
    small = RNG.normal(0, 26, (SIZE // 4, SIZE // 4))
    up = np.array(Image.fromarray(small).resize((SIZE, SIZE), Image.NEAREST))
    return np.full((SIZE, SIZE), 218.0) + up


def main() -> None:
    for name, fn in (
        ("paper", paper), ("film-grain", film_grain), ("halftone", halftone),
        ("grunge", grunge), ("canvas", canvas), ("riso", riso),
    ):
        _save(name, fn())
        print("wrote", name + ".png")


if __name__ == "__main__":
    main()
