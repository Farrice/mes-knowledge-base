#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent

systems = json.loads((ROOT / "systems.json").read_text())
schema = json.loads((ROOT / "input.schema.json").read_text())
proof = json.loads((ROOT / "examples" / "proof-content.json").read_text())
manifest = json.loads((ROOT / "reference-manifest.json").read_text())

assert len(systems["systems"]) == 5
assert len(systems["router"]) == 5
assert set(systems["systems"]) == set(proof["proofs"])
assert manifest["source_count"] == 27
assert len(manifest["sources"]) == 27
assert schema["properties"]["system"]["enum"] == list(systems["systems"])

for source in manifest["sources"]:
    path = Path(source["source_path"])
    assert path.exists(), path
    assert hashlib.sha256(path.read_bytes()).hexdigest() == source["sha256"], path

reference_sheets = sorted((ROOT / "references").glob("*-reference.jpg"))
assert len(reference_sheets) == 5
for path in reference_sheets:
    with Image.open(path) as image:
        assert image.width >= 1000 and image.height >= 1000, path

proof_paths = []
for system, packet in proof["proofs"].items():
    assert len(packet["slides"]) == 3
    for index, slide in enumerate(packet["slides"], start=1):
        assert (ROOT / slide["image"]).exists(), slide["image"]
        for inset in slide.get("insets", []):
            assert (ROOT / inset).exists(), inset
        path = ROOT / "proofs" / system / f"slide-{index:02d}.png"
        proof_paths.append(path)
        with Image.open(path) as image:
            assert image.size == (1080, 1350), path

assert len(proof_paths) == 15
assert (ROOT / "proofs" / "jen-five-system-proof-sheet.jpg").exists()
assert (ROOT / "SYSTEM-ATLAS.html").stat().st_size > 1_000_000
assert len(list((ROOT / "systems").glob("*.md"))) == 5

print("PASS: 5 systems | 27 source slides | 15 transfer proofs | 1080x1350 | manifest hashes current")
