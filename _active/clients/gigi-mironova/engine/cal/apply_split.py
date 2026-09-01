#!/usr/bin/env python3
"""Lock Direction A (split spread) into the Unit 124 set; archive the direction sketches."""
import json, pathlib
CAL = pathlib.Path(__file__).parent
p = CAL / "slides-cal.json"
spec = json.load(open(p))
c01 = next(c for c in spec["carousels"] if c["slug"] == "c01-read-before-you-tour")
for i, s in enumerate(c01["slides"], 1):
    if i in (2, 3, 7):
        s["layout"] = "split"
json.dump(spec, open(p, "w"), indent=2, ensure_ascii=False)
d = CAL / "slides-directions.json"
if d.exists():
    d.rename(CAL / "directions-archive-2026-09-01.json")
print("split locked on slides 2, 3, 7; directions archived")
