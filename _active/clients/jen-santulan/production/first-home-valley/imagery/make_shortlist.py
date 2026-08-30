#!/usr/bin/env python3
"""Copy the visually-curated keepers into shortlist/ by filename stem prefix."""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
RAW = HERE / "raw"
SHORT = HERE / "shortlist"

KEEP = [
    "apartment-building-dusk-01", "apartment-building-dusk-02", "apartment-building-dusk-03",
    "balcony-plants-apartment-02", "california-bungalow-00",
    "front-door-house-00", "front-door-house-02", "front-porch-chairs-00",
    "house-key-lock-00",
    "los-angeles-street-00", "los-angeles-street-01",
    "palm-tree-sunset-city-00", "palm-tree-sunset-city-01", "palm-tree-sunset-city-02",
    "stucco-house-00",
    "suburban-neighborhood-aerial-00", "suburban-neighborhood-aerial-01",
    "suburban-neighborhood-aerial-02", "suburban-neighborhood-aerial-03",
    "sunlight-through-window-floor-00", "sunlight-through-window-floor-03",
    "vintage-suburban-street-01", "vintage-suburban-street-02",
    "contract-signing-pen-01", "contract-signing-pen-02",
    "person-writing-notebook-01", "morning-light-interior-02",
    "valley-street-00", "valley-street-01", "table-math-01", "paper-sheet-01",
]

def main():
    SHORT.mkdir(exist_ok=True)
    index = {}
    for p in RAW.rglob("*"):
        if p.is_file() and p.suffix.lower() in (".jpg", ".png"):
            index.setdefault(p.stem.rsplit("-", 1)[0], []).append(p)
    hit = miss = 0
    for k in KEEP:
        matches = index.get(k)
        if not matches:
            print("  MISSING %s" % k, file=sys.stderr)
            miss += 1
            continue
        src = matches[0]
        shutil.copy2(src, SHORT / src.name)
        hit += 1
    print("%d copied, %d missing -> %s" % (hit, miss, SHORT))

if __name__ == "__main__":
    main()
