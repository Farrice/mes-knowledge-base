#!/usr/bin/env python3
"""Three two-zone directions for the Unit 124 set, each a full 7-slide set. Writes slides-directions.json."""
import copy, json, pathlib

CAL = pathlib.Path(__file__).parent
spec = json.load(open(CAL / "slides-cal.json"))
c01 = next(c for c in spec["carousels"] if c["slug"] == "c01-read-before-you-tour")

DIRS = [
    ("A", "split", "Split spread · photo owns the top half untouched, paper owns the data"),
    ("B", "inset", "Inset column · type left, the room as a tall column right"),
    ("C", "strip", "Data-led · a strip of the room on top, the number owns the page"),
]
out = {"carousels": []}
for letter, layout, title in DIRS:
    c = copy.deepcopy(c01)
    c["slug"] = f"dir-{letter.lower()}-unit-124"
    c["title"] = f"Direction {letter} · {title}"
    for i, s in enumerate(c["slides"], 1):
        if i in (2, 3, 7):
            s["layout"] = layout
        if i == 2 and layout == "strip":
            s["size"] = 280
    out["carousels"].append(c)
(CAL / "slides-directions.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
print("wrote slides-directions.json:", [c["slug"] for c in out["carousels"]])
