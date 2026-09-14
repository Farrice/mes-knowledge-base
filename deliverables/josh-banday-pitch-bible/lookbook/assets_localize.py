"""Copy the L2 assets out of .tmp into lookbook/assets/ (committed) and point cast_map.json at them.

The ABC press PNG (8.8 MB) is converted to a 1400 px JPEG so the repo stays light; everything else copies as-is.
"""
import json
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
(ASSETS / "cast").mkdir(parents=True, exist_ok=True)
(ASSETS / "creator").mkdir(parents=True, exist_ok=True)
cm_path = HERE / "cast_map.json"
cm = json.loads(cm_path.read_text())


def localize(entry: dict, sub: str) -> None:
    src = Path(entry["file"])
    if not src.is_absolute():
        return  # already local
    if not src.exists():
        print("MISSING", src)
        return
    if src.suffix.lower() == ".png" and src.stat().st_size > 2_000_000:
        dst = ASSETS / sub / (src.stem + ".jpg")
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "88", "-Z", "1400",
                        str(src), "--out", str(dst)], check=True, capture_output=True)
    else:
        dst = ASSETS / sub / src.name
        shutil.copy2(src, dst)
    entry["file"] = str(dst.relative_to(HERE))
    print("->", entry["file"])


localize(cm["creator"], "creator")
for c in cm.get("lead_comps", []):
    localize(c, "cast")
for comps in cm.get("ensemble", {}).values():
    for c in comps:
        localize(c, "cast")
cm_path.write_text(json.dumps(cm, indent=2, ensure_ascii=False) + "\n")
# carry the L2 manifest (sources + licenses) alongside
src_manifest = HERE.parents[3] / ".tmp" / "inbetweener-assets" / "manifest.json"
if src_manifest.exists():
    shutil.copy2(src_manifest, ASSETS / "sources-manifest.json")
print("cast_map.json now relative; assets in", ASSETS)
