"""Render a data_map.json into a self-contained Pantry -> Prep -> Plate HTML.

Usage:
    python3 render_data_map.py --input data_map.json --output data_map.html

The output is a single HTML file with inline CSS and inline SVG. No external
dependencies. The operator can email the file or share it directly.

Schema: see SKILL.md Stage 6.
"""
import argparse
import html
import json
from pathlib import Path

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError:
    Environment = None
    FileSystemLoader = None
    select_autoescape = None

THIS_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = THIS_DIR / "templates"


def build_connections(data_map: dict) -> list[dict]:
    connections = []
    for prep_item in data_map.get("prep", []):
        for source_id in prep_item.get("sources", []):
            connections.append({
                "from": source_id,
                "to": prep_item["id"],
                "is_opportunity": prep_item.get("status") == "missing",
            })
    for plate_item in data_map.get("plate", []):
        for prep_id in plate_item.get("reads_from", []):
            connections.append({
                "from": prep_id,
                "to": plate_item["id"],
                "is_opportunity": plate_item.get("status") == "missing",
            })
    return connections


def group_opportunities(data_map: dict) -> dict:
    opp_by_id = {}
    for opp in data_map.get("opportunities", []):
        surface = opp.get("surface", "")
        if "/" in surface:
            _, item_id = surface.split("/", 1)
            opp_by_id.setdefault(item_id, []).append(opp)
    return opp_by_id


def esc(value) -> str:
    if value is None:
        return ""
    return html.escape(str(value), quote=True)


def join_values(values) -> str:
    if not values:
        return "None listed"
    return ", ".join(esc(value) for value in values)


def render_fallback(data_map: dict) -> str:
    business = data_map.get("business", {})
    connections = build_connections(data_map)
    opp_by_id = group_opportunities(data_map)

    def card(item: dict, kind: str) -> str:
        title = item.get("tool") or item.get("name") or item.get("title") or item.get("id")
        details = []
        for key in ("format", "cadence", "volume", "domain", "schedule", "agent", "approval_gate", "status"):
            if item.get(key):
                details.append(f"<li><strong>{esc(key.replace('_', ' ').title())}:</strong> {esc(item[key])}</li>")
        if item.get("feeds"):
            details.append(f"<li><strong>Feeds:</strong> {join_values(item.get('feeds'))}</li>")
        if item.get("sources"):
            details.append(f"<li><strong>Sources:</strong> {join_values(item.get('sources'))}</li>")
        if item.get("reads_from"):
            details.append(f"<li><strong>Reads From:</strong> {join_values(item.get('reads_from'))}</li>")
        if item.get("sample_content"):
            details.append(f"<li><strong>Sample:</strong> {esc(item.get('sample_content'))}</li>")
        if item.get("sample_output"):
            details.append(f"<li><strong>Sample:</strong> {esc(item.get('sample_output'))}</li>")

        badges = "".join(
            f"<span class=\"badge\">{esc(op.get('title'))}</span>"
            for op in opp_by_id.get(item.get("id"), [])
        )
        return (
            f"<article class=\"card {esc(kind)}\">"
            f"<p class=\"eyebrow\">{esc(kind)}</p>"
            f"<h3>{esc(title)}</h3>"
            f"<ul>{''.join(details)}</ul>"
            f"<p>{esc(item.get('explanation'))}</p>"
            f"<div class=\"badges\">{badges}</div>"
            "</article>"
        )

    def section(title: str, kind: str, rows: list[dict]) -> str:
        return (
            f"<section><h2>{esc(title)}</h2>"
            f"<div class=\"grid\">{''.join(card(row, kind) for row in rows)}</div>"
            "</section>"
        )

    opportunities = "".join(
        "<tr>"
        f"<td>{esc(op.get('surface'))}</td>"
        f"<td>{esc(op.get('type'))}</td>"
        f"<td>{esc(op.get('title'))}</td>"
        f"<td>{esc(op.get('impact') or op.get('explanation'))}</td>"
        "</tr>"
        for op in data_map.get("opportunities", [])
    )
    setup = "".join(
        "<li>"
        f"<strong>{esc(step.get('title_friendly') or step.get('title'))}</strong>"
        f"<span>{esc(step.get('what_to_do'))}</span>"
        f"<em>{esc(step.get('working_when'))}</em>"
        "</li>"
        for step in data_map.get("setup_priority", [])
    )
    recipe_rows = "".join(
        "<tr>"
        f"<td>{esc(recipe.get('headline'))}</td>"
        f"<td>{esc(recipe.get('goal'))}</td>"
        f"<td>{join_values(recipe.get('stack'))}</td>"
        f"<td>{esc(recipe.get('after'))}</td>"
        "</tr>"
        for recipe in data_map.get("recipes", [])
    )
    connection_rows = "".join(
        "<tr>"
        f"<td>{esc(connection.get('from'))}</td>"
        f"<td>{esc(connection.get('to'))}</td>"
        f"<td>{'Opportunity' if connection.get('is_opportunity') else 'Mapped'}</td>"
        "</tr>"
        for connection in connections
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Silver Platter Data Map, {esc(business.get("name") or "Your Business")}</title>
<style>
:root {{ --bg:#faf9f7; --ink:#1d1b18; --muted:#67615a; --card:#fff; --line:#d8d2c8; --accent:#d96f3d; --soft:#f7eadf; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--ink); font:14px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
header {{ padding:40px 44px 28px; background:var(--card); border-bottom:1px solid var(--line); }}
h1 {{ margin:0 0 10px; font-size:30px; line-height:1.2; }}
h2 {{ margin:34px 0 14px; font-size:19px; }}
h3 {{ margin:4px 0 10px; font-size:16px; }}
.lead {{ max-width:780px; color:var(--muted); font-size:15px; }}
main {{ padding:0 44px 48px; }}
.stats {{ display:flex; gap:22px; flex-wrap:wrap; margin-top:18px; }}
.stat {{ padding:10px 14px; border:1px solid var(--line); background:var(--bg); border-radius:6px; }}
.stat strong {{ display:block; font-size:22px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:14px; }}
.card {{ background:var(--card); border:1px solid var(--line); border-radius:6px; padding:15px; box-shadow:0 1px 2px rgba(0,0,0,.04); }}
.eyebrow {{ color:var(--accent); text-transform:uppercase; font-size:11px; font-weight:700; margin:0; }}
ul {{ padding-left:18px; margin:8px 0; }}
.badges {{ display:flex; gap:6px; flex-wrap:wrap; margin-top:10px; }}
.badge {{ background:var(--soft); color:var(--accent); border:1px solid #edc6ad; border-radius:999px; padding:2px 8px; font-size:12px; }}
table {{ width:100%; border-collapse:collapse; background:var(--card); border:1px solid var(--line); }}
th,td {{ text-align:left; vertical-align:top; border-bottom:1px solid var(--line); padding:9px 10px; }}
th {{ background:#f3efe8; }}
.priority li {{ margin-bottom:10px; }}
.priority span,.priority em {{ display:block; color:var(--muted); }}
</style>
</head>
<body>
<header>
<p class="eyebrow">Silver Platter Data Map</p>
<h1>{esc(business.get("name") or "Your Business")}</h1>
<p class="lead">{esc(business.get("stack_summary") or business.get("one_liner") or "Pantry -> Prep -> Plate operating map.")}</p>
<div class="stats">
<div class="stat"><strong>{len(data_map.get("pantry", []))}</strong>Pantry sources</div>
<div class="stat"><strong>{len(data_map.get("prep", []))}</strong>Prep tables</div>
<div class="stat"><strong>{len(data_map.get("plate", []))}</strong>Plate outputs</div>
<div class="stat"><strong>{len(data_map.get("opportunities", []))}</strong>Opportunities</div>
</div>
</header>
<main>
{section("Pantry, Raw Sources", "pantry", data_map.get("pantry", []))}
{section("Prep, Silver Platters", "prep", data_map.get("prep", []))}
{section("Plate, Human Outputs", "plate", data_map.get("plate", []))}
<section><h2>Connections</h2><table><thead><tr><th>From</th><th>To</th><th>Status</th></tr></thead><tbody>{connection_rows}</tbody></table></section>
<section><h2>Opportunities</h2><table><thead><tr><th>Surface</th><th>Type</th><th>Title</th><th>Impact</th></tr></thead><tbody>{opportunities}</tbody></table></section>
<section><h2>Setup Priority</h2><ol class="priority">{setup}</ol></section>
<section><h2>Recipes</h2><table><thead><tr><th>Recipe</th><th>Goal</th><th>Stack</th><th>After</th></tr></thead><tbody>{recipe_rows}</tbody></table></section>
</main>
</body>
</html>
"""


def render(data_map: dict, template_dir: Path = TEMPLATE_DIR) -> str:
    if Environment is None:
        return render_fallback(data_map)

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    tpl = env.get_template("data_map.html.j2")

    return tpl.render(
        business=data_map.get("business", {}),
        pantry=data_map.get("pantry", []),
        prep=data_map.get("prep", []),
        plate=data_map.get("plate", []),
        connections=build_connections(data_map),
        opportunities=data_map.get("opportunities", []),
        opp_by_id=group_opportunities(data_map),
        recipes=data_map.get("recipes", []),
        setup_priority=data_map.get("setup_priority", []),
        setup_total_time=data_map.get("setup_total_time"),
        interaction_layer=data_map.get("interaction_layer", []),
    )


def main():
    parser = argparse.ArgumentParser(description="Render a silver-platter data map to HTML")
    parser.add_argument("--input", "-i", required=True, help="Path to data_map.json")
    parser.add_argument("--output", "-o", required=True, help="Path for output data_map.html")
    parser.add_argument("--template-dir", default=str(TEMPLATE_DIR), help="Override template directory")
    args = parser.parse_args()

    data_map = json.loads(Path(args.input).read_text(encoding="utf-8"))
    html = render(data_map, template_dir=Path(args.template_dir))
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    print(f"[ok] wrote {out_path} ({out_path.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
