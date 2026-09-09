#!/usr/bin/env python3
"""Print the visible copy of artboards, for narration checks. Usage: python3 slide_text.py DD2 DD3 ..."""
import html, pathlib, re, sys

HERE = pathlib.Path(__file__).parent
for stem in sys.argv[1:]:
    raw = (HERE / f"{stem}.dc.html").read_text()
    raw = re.sub(r"<style.*?</style>", " ", raw, flags=re.S)
    raw = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    txt = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    txt = re.sub(r"\s+", " ", txt).strip()
    print(f"== {stem}\n{txt[:900]}\n")
