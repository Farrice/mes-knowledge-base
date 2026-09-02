#!/usr/bin/env python3
"""Copy Jen's photos from ~/Downloads into photos/jen/ with readable names, record dimensions + provenance."""
import json, pathlib, shutil, struct

SRC = pathlib.Path.home() / "Downloads"
DST = pathlib.Path(__file__).parent / "jen"
DST.mkdir(exist_ok=True)
FILES = {
    "121218098_3620139968005187_4826814210257676381_n.jpg": "jen-client-newhomeowner-kid.jpg",
    "121159323_3620139974671853_6058231677042270413_n.jpg": "jen-client-family-selfie.jpg",
    "129041531_3768674696485046_9030000756289639579_n.jpg": "jen-client-couple-dogs-selfie.jpg",
    "127211613_3751598854859297_8355297658060286938_n.jpg": "jen-client-pool-house.jpg",
    "130955729_3789601497725699_1413709692987165484_n.jpg": "jen-closing-day-selfie.jpg",
    "151465356_3969291149756732_6889135942416000295_n.jpg": "jen-client-kitchen-sold.jpg",
    "608992920_1556205542236087_2148151443032725560_n.jpg": "jen-headshot-studio.jpg",
    "725947095_1691298465393460_5210965148019033280_n.jpg": "listing-home-gym-pool.jpg",
}


def jpeg_size(p):
    with open(p, "rb") as f:
        data = f.read()
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            i += 1; continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", data[i + 5:i + 9])
            return w, h
        seg = struct.unpack(">H", data[i + 2:i + 4])[0]
        i += 2 + seg
    return None, None


rows = []
for src, dst in FILES.items():
    s = SRC / src
    if not s.exists():
        rows.append({"file": dst, "missing": True}); continue
    d = DST / dst
    shutil.copy(s, d)
    w, h = jpeg_size(d)
    rows.append({"file": dst, "w": w, "h": h, "kb": d.stat().st_size // 1024, "source": "Jen's Facebook page (Farrice, 2026-09-02)", "rights": "hers"})
    print(f"{dst:40s} {w}x{h}  {d.stat().st_size // 1024} KB")
(DST / "provenance.json").write_text(json.dumps(rows, indent=1))
