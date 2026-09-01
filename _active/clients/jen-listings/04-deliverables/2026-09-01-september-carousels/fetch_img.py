#!/usr/bin/env python3
"""Pull real, cleared photography for the September carousel directions and shrink it under ~70 KB.
Sources: Wikimedia Commons (licence noted per file) + Jen's CC0 pool from the First Home Valley build."""
import json, os, pathlib, shutil, subprocess, urllib.parse, urllib.request

HERE = pathlib.Path(__file__).parent
IMG = HERE / "img"
IMG.mkdir(exist_ok=True)
H = {"User-Agent": "JenCarouselResearch/1.0 (farrice.cain@gmail.com)"}

COMMONS = {
    # file, url, licence
    "vannuys-valerio-2024.jpg": ("https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Van_Nuys_Boulevard_from_Valerio_Street_%28Los_Angeles%29%2C_October_2024.JPG/1024px-Van_Nuys_Boulevard_from_Valerio_Street_%28Los_Angeles%29%2C_October_2024.JPG", "CC0"),
    "vannuys-blvd-2024.jpg": ("https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Van_Nuys_Boulevard_in_Van_Nuys%2C_Los_Angeles%2C_Oct._2024.jpg/1024px-Van_Nuys_Boulevard_in_Van_Nuys%2C_Los_Angeles%2C_Oct._2024.jpg", "CC0"),
    "vannuys-street-scene.jpg": ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Van_Nuys_Boulevard_Street_Scene.JPG/1280px-Van_Nuys_Boulevard_Street_Scene.JPG", "Public domain"),
    "sfv-aerial-nara.jpg": ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/California_-_San_Fernando_Valley_-_NARA_-_23935171.jpg/1280px-California_-_San_Fernando_Valley_-_NARA_-_23935171.jpg", "Public domain (NARA)"),
}
POOL_SRC = pathlib.Path("/Users/farricecain/Google Antigravity/.claude/worktrees/jen-carousel-reel-concepts/_active/clients/jen-santulan/production/first-home-valley/imagery/prepared")
POOL = ["apartment-building-dusk-03.jpg", "palm-tree-sunset-city-02.jpg", "california-bungalow-00.jpg",
        "suburban-neighborhood-aerial-02.jpg", "valley-street-01.jpg", "front-door-house-00.jpg",
        "house-key-lock-00.jpg", "sunlight-through-window-floor-00.jpg"]

prov = []
for name, (url, lic) in COMMONS.items():
    try:
        data = urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=40).read()
        (IMG / name).write_bytes(data)
        prov.append({"file": name, "source": "Wikimedia Commons", "url": url, "licence": lic})
        print("ok", name, len(data) // 1024, "KB")
    except Exception as e:
        print("FAIL", name, e)
for f in POOL:
    shutil.copy(POOL_SRC / f, IMG / f)
    prov.append({"file": f, "source": "First Home Valley CC0 pool (Openverse)", "licence": "CC0 / PDM"})

# one more search: hillside views, for the insurance set
u = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
    "action": "query", "generator": "search", "gsrsearch": "Mulholland Drive view San Fernando Valley hillside houses",
    "gsrnamespace": 6, "gsrlimit": 8, "prop": "imageinfo", "iiprop": "url|extmetadata|size", "iiurlwidth": 1000, "format": "json"})
d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=25))
for p in d.get("query", {}).get("pages", {}).values():
    ii = p["imageinfo"][0]; m = ii.get("extmetadata", {})
    print("-", p["title"][:60], "|", m.get("LicenseShortName", {}).get("value", "?"), "|", ii.get("width"), "x", ii.get("height"), "|", ii.get("thumburl", "")[:150])

for f in sorted(IMG.glob("*.jpg")):
    for px, q in ((1000, 52), (900, 45), (800, 40), (720, 36)):
        subprocess.run(["sips", "-Z", str(px), "-s", "format", "jpeg", "-s", "formatOptions", str(q), str(f), "--out", str(f)], check=True, capture_output=True)
        if f.stat().st_size <= 70 * 1024:
            break
    print(f"{f.name}: {f.stat().st_size // 1024} KB")
(IMG / "provenance.json").write_text(json.dumps(prov, indent=2))
