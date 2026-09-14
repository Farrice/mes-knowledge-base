"""Make 640px JPEG thumbs of every frame PNG, plus one contact-sheet HTML for eyeballing takes."""
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
T = HERE / "thumbs"
T.mkdir(exist_ok=True)
rows = []
for png in sorted(HERE.glob("*.png")):
    out = T / (png.stem + ".jpg")
    if not out.exists():
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "70", "-Z", "640",
                        str(png), "--out", str(out)], check=True, capture_output=True)
    rows.append(f'<figure><img src="thumbs/{out.name}"><figcaption>{png.stem}</figcaption></figure>')
(HERE / "contact-sheet.html").write_text(
    "<style>body{background:#070707;color:#C9A96E;font:12px monospace;margin:0;padding:12px}"
    ".g{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}figure{margin:0}img{width:100%;display:block}"
    "figcaption{padding:4px 0 8px}</style><div class='g'>" + "".join(rows) + "</div>")
print(len(rows), "thumbs")
