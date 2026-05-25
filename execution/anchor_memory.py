#!/usr/bin/env python3
"""
Project-scoped anchor memory for the Antigravity Supercomputer.

The killer mechanic from Higgsfield Supercomputer ported into our stack:
early-step outputs (brand brief, product sheet, hero visual) become
PERSISTENT CONTEXT ANCHORS that every later step force-references.

State lives at projects/<slug>/state.yaml. Every supercomputer phase:
  1. Calls `load <slug>` to inject current anchors as context
  2. Produces output
  3. Calls `anchor <slug> --type X --path Y` to register output
  4. (Optionally) `decide <slug> --key K --value V` to lock decisions

Schema (projects/<slug>/state.yaml):
  slug: kebab-case-project-id
  created_at: ISO8601
  updated_at: ISO8601
  brand:
    name: "Higgs"
    tagline: "..."
    voice: "..."
    audience: "..."
    palette: ["#hex", ...]
  decisions:
    positioning: "premium"
    primary_platform: "amazon"
    ...
  anchors:
    - id: anchor-001
      type: product_sheet          # product_sheet|brand_brief|hero_visual|copy|video|...
      path: projects/<slug>/deliverables/product-sheet.md
      created_at: ISO8601
      description: "Foldable resistance band rack — final product sheet"
      ref_for: ["listing_visuals", "ad_concepts"]  # what later phases must reference
  history:
    - ts: ISO8601
      phase: "Phase 2: brand foundation"
      action: "skill:build-bos invoked"
      output_ref: anchor-002

Usage:
  python3 anchor_memory.py init <slug> [--brand-name "..."] [--audience "..."]
  python3 anchor_memory.py load <slug>           # prints formatted context block
  python3 anchor_memory.py anchor <slug> --type product_sheet --path <file> --desc "..."
  python3 anchor_memory.py decide <slug> --key positioning --value "premium"
  python3 anchor_memory.py log <slug> --phase "Phase 3" --action "skill:ghostwrite invoked"
  python3 anchor_memory.py list                  # all projects with state
  python3 anchor_memory.py describe <slug>       # full pretty-print
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
PROJECTS = ROOT / "projects"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def project_dir(slug: str) -> Path:
    return PROJECTS / slug


def state_path(slug: str) -> Path:
    return project_dir(slug) / "state.yaml"


def load_state(slug: str) -> dict:
    p = state_path(slug)
    if not p.exists():
        sys.exit(f"ERROR: no state.yaml for project '{slug}'. Run `init {slug}` first.")
    with p.open() as f:
        return yaml.safe_load(f) or {}


def save_state(slug: str, state: dict) -> None:
    state["updated_at"] = now_iso()
    p = state_path(slug)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w") as f:
        yaml.safe_dump(state, f, sort_keys=False, default_flow_style=False)


def next_anchor_id(state: dict) -> str:
    existing = [a.get("id", "") for a in state.get("anchors", [])]
    n = len(existing) + 1
    return f"anchor-{n:03d}"


# ───────────────────────────────────────────────────────────────────
# Vendored helpers (avoid sibling-module coupling)
# Mirrors execution/knowledge_compiler.DOMAIN_MAP and
# execution/orchestration_ledger._verdict_marker shape.
# ───────────────────────────────────────────────────────────────────
_DOMAIN_HINTS = {
    "brand": "brand", "voice": "brand", "naming": "brand", "storybrand": "brand",
    "copy": "copy", "vsl": "copy", "email": "copy", "headline": "copy",
    "content": "content", "post": "content", "social": "content", "carousel": "content",
    "research": "research", "icp": "research", "audience": "research",
    "product": "product", "hero": "product", "listing": "product", "sku": "product",
    "video": "video", "ad": "video", "ugc": "video", "clip": "video",
    "design": "design", "ui": "design", "layout": "design", "wireframe": "design",
    "strategy": "strategy", "positioning": "strategy", "audit": "strategy",
    "deliberation": "decision",
}

_DOMAIN_ICONS = {
    "brand": "🎨", "copy": "✍️", "content": "📝", "research": "🔍",
    "product": "📦", "video": "🎬", "design": "🖼️", "strategy": "📊",
    "decision": "⚖️", "general": "◆",
}


def _classify_anchor_domain(anchor: dict) -> str:
    """Infer domain from anchor type + description. Used by `board`."""
    haystack = (anchor.get("type", "") + " " + anchor.get("description", "")).lower()
    for hint, domain in _DOMAIN_HINTS.items():
        if hint in haystack:
            return domain
    return "general"


def _anchor_health(anchor: dict) -> str:
    """Return health marker for an anchor based on ref_for coverage."""
    refs = anchor.get("ref_for") or []
    n = len([r for r in refs if r])  # ignore empty strings
    if n >= 3:
        return "🟢"  # high reuse — green
    if n >= 1:
        return "🟡"  # moderate reuse — yellow
    return "🔴"      # unused — red


# ───────────────────────────────────────────────────────────────────
# COMMANDS
# ───────────────────────────────────────────────────────────────────
def cmd_init(args) -> int:
    slug = args.slug
    if state_path(slug).exists():
        print(f"State already exists for '{slug}'. Use `load {slug}` to view.")
        return 1
    state = {
        "slug": slug,
        "created_at": now_iso(),
        "updated_at": now_iso(),
        "brand": {
            "name": args.brand_name or "",
            "tagline": "",
            "voice": "",
            "audience": args.audience or "",
            "palette": [],
        },
        "decisions": {},
        "anchors": [],
        "history": [
            {
                "ts": now_iso(),
                "phase": "init",
                "action": "project initialized",
                "output_ref": "",
            }
        ],
    }
    save_state(slug, state)
    # Ensure conventional subdirs exist
    (project_dir(slug) / "deliverables").mkdir(parents=True, exist_ok=True)
    (project_dir(slug) / "research").mkdir(parents=True, exist_ok=True)
    print(f"✅ Initialized project '{slug}' at {state_path(slug)}")
    return 0


def _walk_parent_chain(slug: str, visited: set, depth: int = 0, max_depth: int = 5) -> list:
    """Walk meta_parent chain upward; return list of (parent_slug, parent_state)
    tuples, root-to-immediate-parent order. Detects cycles and depth overflow.
    Raises ValueError on cycle; truncates silently at max_depth."""
    if depth >= max_depth:
        return []
    state = load_state(slug)
    parent = state.get("meta_parent")
    if not parent:
        return []
    if parent in visited:
        raise ValueError(f"meta_parent cycle detected: {' → '.join(visited)} → {parent}")
    visited.add(parent)
    parent_state = load_state(parent)
    chain = _walk_parent_chain(parent, visited, depth + 1, max_depth)
    chain.append((parent, parent_state))
    return chain


def cmd_load(args) -> int:
    """Print the context block that goes into the next supercomputer phase prompt.

    If state.yaml declares `meta_parent: <slug>`, walks the chain up to 5 levels
    and prepends inherited anchors (only those with non-empty ref_for) under an
    "Inherited from <parent>" header. Lineage flows root → immediate parent →
    current project.
    """
    state = load_state(args.slug)
    brand = state.get("brand", {})
    decisions = state.get("decisions", {})
    anchors = state.get("anchors", [])

    print(f"# Project Context: {state.get('slug')}")
    print(f"_Loaded from anchor memory at {now_iso()}_\n")

    # ─── Meta-parent inheritance (root-to-immediate-parent order) ───
    try:
        chain = _walk_parent_chain(args.slug, visited={args.slug})
    except ValueError as e:
        print(f"⚠️  {e}", file=sys.stderr)
        chain = []

    for parent_slug, parent_state in chain:
        propagating = [
            a for a in parent_state.get("anchors", [])
            if a.get("ref_for") and any(r for r in a["ref_for"])
        ]
        if not propagating:
            continue
        print(f"## Inherited from `{parent_slug}` (cross-project context)\n")
        for a in propagating:
            print(f"- `{parent_slug}::{a['id']}` ({a['type']}): {a.get('description', '')}")
            print(f"  Path: `{a['path']}`")
            if a.get("ref_for"):
                print(f"  Was required reference for: {', '.join(a['ref_for'])}")
        print()

    print("## Brand")
    if brand.get("name"): print(f"- **Name:** {brand['name']}")
    if brand.get("tagline"): print(f"- **Tagline:** {brand['tagline']}")
    if brand.get("voice"): print(f"- **Voice:** {brand['voice']}")
    if brand.get("audience"): print(f"- **Audience:** {brand['audience']}")
    if brand.get("palette"): print(f"- **Palette:** {', '.join(brand['palette'])}")
    if not any(brand.values()): print("_(brand fields empty — fill in via `decide` calls)_")
    print()

    if decisions:
        print("## Locked Decisions")
        for k, v in decisions.items():
            print(f"- **{k}:** {v}")
        print()

    if anchors:
        print("## Anchors (must be referenced in subsequent generation)")
        for a in anchors:
            print(f"- `{a['id']}` ({a['type']}): {a.get('description', '')}")
            print(f"  Path: `{a['path']}`")
            if a.get("ref_for"):
                print(f"  Required reference for: {', '.join(a['ref_for'])}")
        print()
    else:
        print("## Anchors\n_(none yet — first generation will become the first anchor)_\n")

    return 0


def cmd_anchor(args) -> int:
    state = load_state(args.slug)
    aid = next_anchor_id(state)
    anchor = {
        "id": aid,
        "type": args.type,
        "path": args.path,
        "created_at": now_iso(),
        "description": args.desc or "",
        "ref_for": args.ref_for.split(",") if args.ref_for else [],
    }
    state.setdefault("anchors", []).append(anchor)
    state.setdefault("history", []).append({
        "ts": now_iso(),
        "phase": args.phase or "",
        "action": f"anchor added: {args.type}",
        "output_ref": aid,
    })
    save_state(args.slug, state)
    print(f"✅ Anchor {aid} added: {args.type} → {args.path}")
    if anchor["ref_for"]:
        print(f"   Required reference for: {', '.join(anchor['ref_for'])}")
    return 0


def cmd_decide(args) -> int:
    state = load_state(args.slug)
    state.setdefault("decisions", {})[args.key] = args.value
    state.setdefault("history", []).append({
        "ts": now_iso(),
        "phase": args.phase or "",
        "action": f"decision: {args.key} = {args.value}",
        "output_ref": "",
    })
    save_state(args.slug, state)
    print(f"✅ Decision locked: {args.key} = {args.value}")
    return 0


def cmd_brand(args) -> int:
    """Update brand fields (name/tagline/voice/audience/palette)."""
    state = load_state(args.slug)
    brand = state.setdefault("brand", {})
    if args.name is not None: brand["name"] = args.name
    if args.tagline is not None: brand["tagline"] = args.tagline
    if args.voice is not None: brand["voice"] = args.voice
    if args.audience is not None: brand["audience"] = args.audience
    if args.palette is not None: brand["palette"] = [c.strip() for c in args.palette.split(",")]
    state.setdefault("history", []).append({
        "ts": now_iso(),
        "phase": args.phase or "",
        "action": "brand fields updated",
        "output_ref": "",
    })
    save_state(args.slug, state)
    print(f"✅ Brand updated for '{args.slug}'")
    return 0


def cmd_log(args) -> int:
    state = load_state(args.slug)
    state.setdefault("history", []).append({
        "ts": now_iso(),
        "phase": args.phase,
        "action": args.action,
        "output_ref": args.output_ref or "",
    })
    save_state(args.slug, state)
    print(f"Logged: {args.phase} → {args.action}")
    return 0


def cmd_list(_args) -> int:
    if not PROJECTS.exists():
        print("No projects directory.")
        return 0
    found = []
    for p in sorted(PROJECTS.iterdir()):
        if p.is_dir() and (p / "state.yaml").exists():
            try:
                with (p / "state.yaml").open() as f:
                    s = yaml.safe_load(f) or {}
                found.append((p.name, s))
            except Exception:
                continue
    if not found:
        print("No projects with anchor-memory state.")
        return 0
    print(f"Found {len(found)} project(s) with state:\n")
    for slug, s in found:
        anchor_n = len(s.get("anchors", []))
        decisions_n = len(s.get("decisions", {}))
        brand_name = s.get("brand", {}).get("name", "(unnamed)")
        print(f"  {slug:<32s} {brand_name:<24s} {anchor_n} anchors, {decisions_n} decisions")
    return 0


def cmd_describe(args) -> int:
    state = load_state(args.slug)
    print(yaml.safe_dump(state, sort_keys=False, default_flow_style=False))
    return 0


def cmd_clone(args) -> int:
    """Clone an existing project's state as a template for a new project.

    Brand-level fields (voice, audience, palette) PRESERVED.
    Per-project fields (anchors, history) CLEARED.
    Decisions PRESERVED by default; pass --no-decisions to drop them.
    --vary "key=value,key=value" overrides specific brand fields.
    meta_parent automatically set to source slug (lineage recorded).
    """
    source = load_state(args.source)
    target_path = state_path(args.to)
    if target_path.exists():
        print(f"❌ Target '{args.to}' already exists. Refusing to overwrite.", file=sys.stderr)
        return 1

    # Parse --vary k=v,k=v overrides
    vary_map = {}
    if args.vary:
        for pair in args.vary.split(","):
            if "=" not in pair:
                continue
            k, v = pair.split("=", 1)
            vary_map[k.strip()] = v.strip()

    new_state = {
        "slug": args.to,
        "created_at": now_iso(),
        "updated_at": now_iso(),
        "meta_parent": args.source,   # lineage
        "brand": {
            "name": vary_map.get("name", source.get("brand", {}).get("name", "")),
            "tagline": vary_map.get("tagline", source.get("brand", {}).get("tagline", "")),
            "voice": vary_map.get("voice", source.get("brand", {}).get("voice", "")),
            "audience": vary_map.get("audience", source.get("brand", {}).get("audience", "")),
            "palette": (
                [c.strip() for c in vary_map["palette"].split(";")]
                if "palette" in vary_map else source.get("brand", {}).get("palette", [])
            ),
        },
        "decisions": ({} if args.no_decisions else dict(source.get("decisions", {}))),
        "anchors": [],   # per-project, cleared
        "history": [
            {
                "ts": now_iso(),
                "phase": "init",
                "action": f"cloned from {args.source}"
                          + (f" with vary: {args.vary}" if args.vary else ""),
                "output_ref": "",
            }
        ],
    }
    save_state(args.to, new_state)
    (project_dir(args.to) / "deliverables").mkdir(parents=True, exist_ok=True)
    (project_dir(args.to) / "research").mkdir(parents=True, exist_ok=True)
    print(f"✅ Cloned '{args.source}' → '{args.to}'")
    print(f"   meta_parent: {args.source}  (load will inherit propagating anchors)")
    if vary_map:
        print(f"   vary applied: {', '.join(f'{k}={v}' for k, v in vary_map.items())}")
    if not args.no_decisions and source.get("decisions"):
        print(f"   {len(source['decisions'])} decision(s) preserved")
    return 0


def _render_board_ascii(state: dict) -> str:
    """Render state as a readable ASCII timeline. Returns full string."""
    lines = []
    slug = state.get("slug", "(unnamed)")
    brand_name = state.get("brand", {}).get("name", "(unnamed)")
    created = state.get("created_at", "?")
    meta_parent = state.get("meta_parent")

    lines.append("=" * 72)
    lines.append(f"PROJECT: {slug}  |  Brand: {brand_name}  |  Created: {created}")
    if meta_parent:
        lines.append(f"   ↑ inherits from: {meta_parent}")
    lines.append("=" * 72)
    lines.append("")

    # Decisions
    decisions = state.get("decisions") or {}
    if decisions:
        lines.append("DECISIONS LOCKED")
        for k, v in decisions.items():
            lines.append(f"  ◆ {k}: {v}")
        lines.append("")

    # Anchors with health markers + domain icons
    anchors = state.get("anchors") or []
    lines.append(f"ANCHORS ({len(anchors)})")
    if not anchors:
        lines.append("  _(none yet)_")
    else:
        for a in anchors:
            health = _anchor_health(a)
            domain = _classify_anchor_domain(a)
            icon = _DOMAIN_ICONS.get(domain, "◆")
            desc = (a.get("description") or "")[:60]
            lines.append(f"  {health} {a['id']:<14s} {icon} {a['type']:<18s} {desc}")
            refs = [r for r in (a.get("ref_for") or []) if r]
            if refs:
                lines.append(f"      └─ ref_for: {', '.join(refs)}  ({len(refs)} phase{'s' if len(refs) != 1 else ''})")
            else:
                lines.append(f"      └─ ref_for: (none — unused anchor)")
    lines.append("")

    # Timeline
    history = state.get("history") or []
    lines.append("TIMELINE")
    if not history:
        lines.append("  _(no events logged)_")
    else:
        for entry in history:
            ts = (entry.get("ts") or "")[:19].replace("T", " ")
            phase = (entry.get("phase") or "")[:14]
            action = (entry.get("action") or "")[:80]
            output_ref = entry.get("output_ref") or ""
            suffix = f" → {output_ref}" if output_ref else ""
            lines.append(f"  {ts}  {phase:<14s} {action}{suffix}")
    lines.append("")
    lines.append("=" * 72)
    return "\n".join(lines)


def _render_board_mermaid(state: dict) -> str:
    """Render state as Mermaid timeline syntax (paste into Notion/GitHub)."""
    lines = ["```mermaid", "timeline", f"    title {state.get('slug', '(unnamed)')} — anchor timeline"]
    history = state.get("history") or []
    for entry in history:
        ts = (entry.get("ts") or "")[:10]   # YYYY-MM-DD
        action = (entry.get("action") or "").replace(":", "—")[:80]
        phase = entry.get("phase") or "step"
        lines.append(f"    {ts} : {phase} : {action}")
    lines.append("```")
    return "\n".join(lines)


def cmd_board(args) -> int:
    """Render state.yaml as a readable timeline (ASCII default; --format mermaid)."""
    state = load_state(args.slug)
    if args.format == "mermaid":
        print(_render_board_mermaid(state))
    else:
        print(_render_board_ascii(state))
    return 0


# ───────────────────────────────────────────────────────────────────
# CLI
# ───────────────────────────────────────────────────────────────────
def main() -> int:
    p = argparse.ArgumentParser(description="Anchor memory for Antigravity Supercomputer")
    sub = p.add_subparsers(dest="cmd", required=True)

    pi = sub.add_parser("init", help="Initialize a new project's anchor memory")
    pi.add_argument("slug")
    pi.add_argument("--brand-name", default="")
    pi.add_argument("--audience", default="")

    pl = sub.add_parser("load", help="Print formatted context block for prompt injection")
    pl.add_argument("slug")

    pa = sub.add_parser("anchor", help="Register a deliverable as a context anchor")
    pa.add_argument("slug")
    pa.add_argument("--type", required=True,
                    help="Anchor type (product_sheet|brand_brief|hero_visual|copy|video|...)")
    pa.add_argument("--path", required=True, help="Relative path to the deliverable")
    pa.add_argument("--desc", default="")
    pa.add_argument("--ref-for", default="",
                    help="Comma-separated list of later phase names that must reference this")
    pa.add_argument("--phase", default="")

    pd = sub.add_parser("decide", help="Lock a project decision")
    pd.add_argument("slug")
    pd.add_argument("--key", required=True)
    pd.add_argument("--value", required=True)
    pd.add_argument("--phase", default="")

    pb = sub.add_parser("brand", help="Update brand fields")
    pb.add_argument("slug")
    pb.add_argument("--name")
    pb.add_argument("--tagline")
    pb.add_argument("--voice")
    pb.add_argument("--audience")
    pb.add_argument("--palette", help="Comma-separated hex codes")
    pb.add_argument("--phase", default="")

    plog = sub.add_parser("log", help="Append a history entry")
    plog.add_argument("slug")
    plog.add_argument("--phase", required=True)
    plog.add_argument("--action", required=True)
    plog.add_argument("--output-ref", default="")

    sub.add_parser("list", help="List all projects with anchor-memory state")

    pdesc = sub.add_parser("describe", help="Pretty-print full state YAML")
    pdesc.add_argument("slug")

    pc = sub.add_parser(
        "clone",
        help="Clone an existing project's state as a template (mission templates)",
    )
    pc.add_argument("source", help="Source project slug")
    pc.add_argument("--to", required=True, help="Target slug for the cloned project")
    pc.add_argument(
        "--vary",
        default="",
        help="Comma-separated brand-field overrides (e.g., 'name=NewBrand,audience=new-segment'). "
             "Use ';' to separate palette colors when overriding palette.",
    )
    pc.add_argument(
        "--no-decisions",
        action="store_true",
        help="Drop source decisions instead of preserving them",
    )

    pboard = sub.add_parser(
        "board",
        help="Render state.yaml as a readable timeline (ASCII or Mermaid)",
    )
    pboard.add_argument("slug")
    pboard.add_argument(
        "--format",
        choices=["ascii", "mermaid"],
        default="ascii",
        help="Output format. Default: ascii.",
    )

    args = p.parse_args()
    return {
        "init": cmd_init,
        "load": cmd_load,
        "anchor": cmd_anchor,
        "decide": cmd_decide,
        "brand": cmd_brand,
        "log": cmd_log,
        "list": cmd_list,
        "describe": cmd_describe,
        "clone": cmd_clone,
        "board": cmd_board,
    }[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
