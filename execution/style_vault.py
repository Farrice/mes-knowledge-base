#!/usr/bin/env python3
"""style_vault.py — the keyed style vault over skills/generate/styles/.

WHY THIS EXISTS
---------------
Luke Carter's anti-slop workflow (YouTube sAMArYBpDmI, 2026-08-08) locks ONE style for ONE
brand. Farrice needs many: a switchable vault keyed by brand x ICP x platform, so client work,
platform-native content and his own brand each draw the right look without retooling.

The craft is NOT here. Frame construction is nick-st-pierre; sweep/board-card discipline is
rory-flynn; "is this slop and at which layer" is grace-liu. This file is the deterministic
layer underneath: storage, keying, retrieval, and the two combinatorial operations that
replace Midjourney syntax on a no-Midjourney stack.

COMPATIBILITY CONTRACT
----------------------
execution/asset_gallery.py::load_styles() reads `<slug>/prompt.md` (para 1 = description,
rest = prompt) and ignores every other file. This module therefore writes characterization to
a SIBLING `card.md` and never touches prompt.md's shape. The assets board keeps working.

Stdlib only. Repo deps are python-dotenv + requests; this adds none.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
from datetime import date
from itertools import product

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STYLES_DIR = os.path.join(ROOT, "skills", "generate", "styles")
VAULT_INDEX = os.path.join(STYLES_DIR, "VAULT.md")

# Flynn's tiers — what job a style asset is allowed to hold.
TIERS = {
    "tight": "overrides the probe almost entirely; one exact aesthetic. Job: reproduce a look.",
    "broad": "wide range, several aesthetics coexist. Job: a house style with room.",
    "micro": "one isolated effect, barely moves subject or composition. Job: stack fuel.",
}

# Facets the vault is keyed on. Multi-valued.
LIST_FIELDS = ("brands", "icps", "platforms", "references", "tags")
# Characterization fields — Flynn's null run writes these. Missing = uncharacterized = don't ship.
CHARACTERIZATION = ("palette", "light", "texture", "subject_bias", "era", "refuses")


# ---------------------------------------------------------------- frontmatter

def _parse_scalar(raw: str):
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [p.strip().strip("'\"") for p in inner.split(",") if p.strip()]
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "'\"":
        return raw[1:-1]
    return raw


def parse_frontmatter(text: str):
    """Minimal YAML-subset reader: scalars, quoted strings, inline lists. No deps."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block, body = text[3:end], text[end + 4:]
    meta = {}
    for line in block.splitlines():
        line = line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, raw = line.partition(":")
        key = key.strip()
        if not key or line[0] in " \t":  # no nested-map support by design
            continue
        meta[key] = _parse_scalar(raw)
    for f in LIST_FIELDS:
        if f in meta and isinstance(meta[f], str):
            meta[f] = [p.strip() for p in meta[f].split(",") if p.strip()] if meta[f] else []
    return meta, body.lstrip("\n")


def dump_frontmatter(meta: dict) -> str:
    order = ["slug", "name", "status", "tier", "family", "brands", "icps", "platforms",
             "tags", "palette", "light", "texture", "subject_bias", "era", "refuses",
             "conditions", "anti_conditions", "references", "provenance", "created", "verified"]
    keys = [k for k in order if k in meta] + [k for k in meta if k not in order]
    out = ["---"]
    for k in keys:
        v = meta[k]
        if isinstance(v, list):
            out.append(f"{k}: [{', '.join(str(x) for x in v)}]")
        elif isinstance(v, str) and (":" in v or v.strip() != v or "#" in v):
            out.append(f'{k}: "{v}"')
        else:
            out.append(f"{k}: {v}")
    out.append("---")
    return "\n".join(out)


# ---------------------------------------------------------------- load

def card_path(slug: str) -> str:
    return os.path.join(STYLES_DIR, slug, "card.md")


def load_card(slug: str):
    p = card_path(slug)
    if not os.path.isfile(p):
        return None
    meta, body = parse_frontmatter(open(p, encoding="utf-8").read())
    meta.setdefault("slug", slug)
    meta["_body"] = body
    meta["_path"] = p
    return meta


def load_all():
    cards = []
    if not os.path.isdir(STYLES_DIR):
        return cards
    for slug in sorted(os.listdir(STYLES_DIR)):
        d = os.path.join(STYLES_DIR, slug)
        if not os.path.isdir(d):
            continue
        c = load_card(slug)
        if c is None:
            # A style with prompt.md but no card.md is real but UNCHARACTERIZED.
            if os.path.isfile(os.path.join(d, "prompt.md")):
                cards.append({"slug": slug, "name": slug.replace("-", " ").title(),
                              "status": "uncharacterized", "_path": None, "_body": ""})
            continue
        cards.append(c)
    return cards


def gaps(card: dict):
    """What stops this card being production-usable. Empty list = shippable.

    `verified` is the green-from-nothing backstop. Characterization fields can be filled by
    reading a prompt string — that is inference, not evidence. A card only goes OK once
    someone has actually RUN the style and dated it. Description is not verification.
    """
    missing = []
    if card.get("status") == "uncharacterized":
        return ["no card.md — null run never recorded"]
    for f in CHARACTERIZATION:
        if not str(card.get(f, "")).strip():
            missing.append(f"missing {f}")
    if card.get("tier") not in TIERS:
        missing.append("tier not one of tight/broad/micro")
    if not card.get("brands"):
        missing.append("not keyed to any brand")
    if not str(card.get("verified", "")).strip():
        missing.append("never verified by an actual run (set `verified: YYYY-MM-DD`)")
    return missing


# ---------------------------------------------------------------- commands

def cmd_init(args):
    slug = args.slug
    d = os.path.join(STYLES_DIR, slug)
    os.makedirs(d, exist_ok=True)
    p = card_path(slug)
    if os.path.isfile(p) and not args.force:
        print(f"card exists: {p} (use --force to overwrite)")
        return 1
    today = date.today().isoformat()
    meta = {
        "slug": slug,
        "name": args.name or slug.replace("-", " ").title(),
        "status": "draft",
        "tier": args.tier or "",
        "family": args.family or "",
        "brands": args.brands or [],
        "icps": args.icps or [],
        "platforms": args.platforms or [],
        "tags": args.tags or [],
        "palette": "", "light": "", "texture": "", "subject_bias": "", "era": "", "refuses": "",
        "conditions": "", "anti_conditions": "",
        "references": [], "provenance": args.provenance or "",
        "created": today, "verified": "",
    }
    body = (
        "## Null run (what the asset does with no direction)\n\n_Record the null-run read here. "
        "Until this is written the style is a folder of vibes, not a bank entry._\n\n"
        "## Probe run (what survives contact with direction)\n\n_The delta between null and probe "
        "IS the asset's strength._\n\n"
        "## Portable string per model\n\n"
        "| Model | String / reference plan |\n|---|---|\n| nano-banana-2 | |\n| flux-2 | |\n"
        "| recraft-v3 | |\n\n"
        "## Do not use for\n\n_Anti-conditions in prose._\n"
    )
    open(p, "w", encoding="utf-8").write(dump_frontmatter(meta) + "\n\n" + body)
    print(f"created {os.path.relpath(p, ROOT)}")
    if not os.path.isfile(os.path.join(d, "prompt.md")):
        print(f"NOTE: {slug}/prompt.md not present — the assets board needs it "
              f"(para 1 = description, rest = prompt).")
    return 0


def _matches(card, args):
    def has(field, want):
        if not want:
            return True
        vals = card.get(field) or []
        if isinstance(vals, str):
            vals = [vals]
        return any(w in vals for w in want)
    if args.brand and not has("brands", [args.brand]):
        return False
    if args.icp and not has("icps", [args.icp]):
        return False
    if args.platform and not has("platforms", [args.platform]):
        return False
    if args.tier and card.get("tier") != args.tier:
        return False
    if args.status and card.get("status") != args.status:
        return False
    return True


def cmd_list(args):
    cards = [c for c in load_all() if _matches(c, args)]
    if args.json:
        print(json.dumps([{k: v for k, v in c.items() if not k.startswith("_")}
                          for c in cards], indent=2))
        return 0
    if not cards:
        print("no styles match.")
        return 0
    print(f"{len(cards)} style(s)\n")
    for c in cards:
        g = gaps(c)
        flag = "OK " if not g else "GAP"
        brands = ",".join(c.get("brands") or []) or "-"
        plats = ",".join(c.get("platforms") or []) or "-"
        print(f"[{flag}] {c['slug']:<28} tier={c.get('tier') or '-':<6} "
              f"brands={brands:<28} platforms={plats}")
        if g and args.verbose:
            for item in g:
                print(f"        ! {item}")
    return 0


def cmd_show(args):
    c = load_card(args.slug)
    if not c:
        print(f"no card for '{args.slug}'")
        return 1
    for k, v in c.items():
        if k.startswith("_"):
            continue
        print(f"{k}: {v}")
    g = gaps(c)
    print("\nstatus: SHIPPABLE" if not g else "\ngaps:\n  " + "\n  ".join(g))
    print("\n" + c["_body"])
    return 0


def cmd_validate(args):
    cards = load_all()
    bad = [(c, gaps(c)) for c in cards if gaps(c)]
    for c, g in bad:
        print(f"{c['slug']}:")
        for item in g:
            print(f"  - {item}")
    print(f"\n{len(cards) - len(bad)}/{len(cards)} shippable.")
    return 1 if bad and args.strict else 0


def cmd_index(args):
    cards = load_all()
    lines = [
        "# Style Vault — generated index",
        "",
        "<!-- GENERATED by execution/style_vault.py index — do not hand-edit. -->",
        "",
        f"_{len(cards)} entries. Regenerate: `python3 execution/style_vault.py index`._",
        "",
        "Cards are keyed by brand x ICP x platform. `GAP` = characterization incomplete "
        "(null run not recorded, no tier, or unkeyed) — those are not production-usable yet.",
        "",
        "| Style | Tier | Family | Brands | Platforms | State |",
        "|---|---|---|---|---|---|",
    ]
    for c in cards:
        g = gaps(c)
        lines.append("| `{}` | {} | {} | {} | {} | {} |".format(
            c["slug"], c.get("tier") or "-", c.get("family") or "-",
            ", ".join(c.get("brands") or []) or "-",
            ", ".join(c.get("platforms") or []) or "-",
            "OK" if not g else f"GAP ({len(g)})"))
    lines += ["", "## Tiers", ""]
    for t, meaning in TIERS.items():
        lines.append(f"- **{t}** — {meaning}")
    lines.append("")
    os.makedirs(STYLES_DIR, exist_ok=True)
    open(VAULT_INDEX, "w", encoding="utf-8").write("\n".join(lines))
    print(f"wrote {os.path.relpath(VAULT_INDEX, ROOT)} ({len(cards)} entries)")
    return 0


# ------------------------------------------------- permute (the {a,b,c} port)

BRACE = re.compile(r"\{([^{}]*)\}")


def expand(template: str):
    """Cartesian expansion of {a, b, c} groups. Midjourney does this natively; on a
    no-Midjourney stack it is one function. Order is deterministic (left-to-right)."""
    groups = BRACE.findall(template)
    if not groups:
        return [template]
    options = [[o.strip() for o in g.split(",")] for g in groups]
    out = []
    for combo in product(*options):
        s, i = template, iter(combo)
        s = BRACE.sub(lambda _m: next(i), s)
        out.append(s)
    return out


def cmd_permute(args):
    template = args.template
    if args.file:
        template = open(args.file, encoding="utf-8").read().strip()
    prompts = expand(template)
    total = len(prompts)
    if args.sample and args.sample < total:
        random.Random(args.seed).shuffle(prompts)
        prompts = prompts[:args.sample]
    if args.limit:
        prompts = prompts[:args.limit]
    if args.json:
        print(json.dumps({"total_combinations": total, "returned": len(prompts),
                          "prompts": prompts}, indent=2))
        return 0
    print(f"# {total} combination(s); showing {len(prompts)}\n")
    for i, p in enumerate(prompts, 1):
        print(f"{i:>3}. {p}")
    return 0


# --------------------------------------------- probe (the --sref random port)

# A decomposable aesthetic lexicon. Every term names a MEDIUM, PROCESS, ERA, PHYSICAL LIGHT
# CONDITION, SURFACE or COMPOSITIONAL RULE — never a quality assertion ("cinematic", "8k")
# and never an artist name. Both bans are St. Pierre's, and both exist because undecomposable
# terms cannot be swept, explained, or banked.
LEXICON = {
    "process": [
        "medium-format film photograph", "35mm colour negative photograph",
        "black-and-white push-processed film photograph", "large-format view-camera photograph",
        "risograph print in two spot colours", "silkscreen print with visible registration offset",
        "letterpress impression on cotton stock", "gouache painting on textured paper",
        "watercolour wash with dry-brush edges", "ink-and-wash brush drawing",
        "cut-paper collage photographed flat", "technical pen isometric drawing",
        "airbrushed matte painting", "linocut relief print", "cyanotype contact print",
        "photogravure plate", "flat vector illustration with no gradients",
        "clay-render 3d with soft shadows", "editorial photo-illustration composite",
    ],
    "era": [
        "1930s industrial poster", "1950s modernist advertising", "1960s Swiss typographic",
        "1970s editorial magazine", "1980s technical manual", "1990s independent zine",
        "early-2000s minimal web", "contemporary gallery documentation",
    ],
    "palette_logic": [
        "two-colour duotone, one warm one cool", "single hue with a neutral ground",
        "muted earth tones with one saturated accent", "high-key pastels, no black",
        "desaturated cool palette with warm skin", "near-monochrome with a single red note",
        "complementary pair at unequal weight", "full neutral grey scale, colour only in light",
    ],
    "light": [
        "single hard source from camera left, long shadows",
        "overcast north window, soft and directionless",
        "backlit at golden hour with visible flare",
        "bare on-camera flash, stark falloff to black",
        "practical lamps only, warm pools in dark room",
        "top-down noon sun, short hard shadows",
        "bounced fill from a white surface below",
        "single source through a diffusion scrim, wraparound falloff",
    ],
    "surface": [
        "visible film grain and dust", "paper tooth and fibre", "brushed metal and glass",
        "raw concrete with formwork marks", "linen and unfinished wood",
        "matte plastic and powder-coat", "worn leather and brass", "ceramic glaze and stone",
    ],
    "composition": [
        "centred subject with generous negative space above",
        "off-centre subject, two-thirds empty ground for text",
        "tight crop, subject exceeding the frame",
        "flat-on elevation, no perspective",
        "high angle looking down, subject small in frame",
        "layered fore/mid/background with clear depth separation",
    ],
    # --- Added 2026-08-10 after Farrice's "texture looks AI-generated / looks lazy" verdict.
    # The first sweep drew style but never CAPTURE, ATMOSPHERE or IMPERFECTION — which is
    # Dave Clark's causes #5, #4 and the physics half of #7. On Midjourney these come free from
    # the model's aesthetic prior; on this stack they must be authored or every frame renders
    # digitally immaculate and therefore never photographed.
    "capture": [
        "Hasselblad 500CM, 80mm, f/8, Kodak Portra 400, tripod, mirror-up",
        "Sinar 4x5 view camera, 210mm, f/22, sheet film, front tilt for a raked focal plane",
        "Leica M6, 35mm Summicron, f/2, Tri-X pushed to 1600, handheld",
        "Pentax 67, 105mm, f/4, Ektachrome, tripod, slight camera shake at 1/15s",
        "Canon F-1, 100mm macro, f/11, Ektar 100, focus stacked across two frames",
    ],
    "atmosphere": [
        "dust motes suspended in the light beam, visible only where it rakes",
        "a faint haze of condensation in the air near the cold surface",
        "steam drifting through the mid-ground, thinning toward the top of frame",
        "airborne particulate catching the source, mid-ground only, never clean air",
    ],
    "imperfection": [
        "a partial fingerprint on the surface edge, dust settled unevenly, one element slightly out of square",
        "paper cockled and buckled where it absorbed moisture, ink feathering along the wet edge",
        "a hairline scratch across the bench, an old ring stain, a staple driven in crooked",
        "lens flare from the raking source, a single hair on the film plane, uneven vignetting",
    ],
}


def cmd_probe(args):
    """Replaces Midjourney's `--sref random`. MJ rolls a private latent index; here we roll a
    DECOMPOSABLE descriptor, which is strictly better for banking: when one wins you can read
    off exactly which decisions produced it and write them onto a card."""
    rng = random.Random(args.seed)
    n = args.n
    keys = list(LEXICON)
    draws = []
    seen = set()
    attempts = 0
    while len(draws) < n and attempts < n * 50:
        attempts += 1
        pick = {k: rng.choice(LEXICON[k]) for k in keys}
        sig = tuple(pick.values())
        if sig in seen:
            continue
        seen.add(sig)
        draws.append(pick)
    subject = args.subject or "a single person at work"
    if args.json:
        print(json.dumps({"seed": args.seed, "subject": subject, "draws": draws}, indent=2))
        return 0
    print(f"# Style probe sweep — {len(draws)} candidates (seed {args.seed})\n")
    print(f"Fixed probe subject (do NOT change mid-sweep): **{subject}**\n")
    print("Run every candidate against this one subject. Judge the SET, not keepers. "
          "Winners get a card; everything else is deleted.\n")
    print("RULE: generate at least 4 per candidate and SELECT. Dave Clark's cause #1 of flat "
          "is 'one generation deep' — a selection problem, not a prompting one. One image per "
          "concept is not a sweep, it is a first take.\n")
    for i, d in enumerate(draws, 1):
        line = (f"{d['process']}, {d['era']} register. {subject}. "
                f"{d['composition'].capitalize()}. Light: {d['light']}. "
                f"Palette: {d['palette_logic']}. Surfaces: {d['surface']}. "
                f"Shot on {d['capture']}. Air: {d['atmosphere']}. "
                f"Wear: {d['imperfection']}.")
        print(f"## Candidate {i:02d}\n{line}\n")
    return 0


# ------------------------------------------------------- lint (the realism floor)

# Farrice's 8/10 verdict on the COA plate (2026-08-10) set the floor. This linter exists so the
# floor is MECHANICAL, not a document someone has to remember — the house rule is that
# AI-memory-dependent observability is banned and must be paired with a deterministic backstop.
#
# Each layer is a physical CAUSE the frame needs. Missing layers are what the model fills with
# its own averaged defaults, and averaged defaults are what "AI slop" means.
FLOOR = [
    ("capture", "camera, lens, aperture, stock/format — the physical cause of the texture",
     r"\b(hasselblad|leica|sinar|pentax|canon|nikon|mamiya|contax|rollei|view camera|"
     r"\d{2,3}\s*mm|f/\d|portra|ektar|ektachrome|tri-?x|provia|velvia|neopan|cinestill|"
     r"large format|medium format|4x5|8x10|sheet film|tripod|handheld)\b"),
    ("light", "one nameable source with a direction",
     r"\b(source from|light from|raking|backlit|side ?light|top ?light|window light|"
     r"key light|scrim|diffus|bounce|flash|overhead|camera (left|right))\b"),
    ("black_point", "shadows landing on real black — not lifted mid-grey",
     r"\b(black point|falls? to (true )?black|true black|deep black|clips? at|"
     r"whites? .{0,20}white and blacks?)\b"),
    ("atmosphere", "something physically in the mid-ground — never clean air",
     r"\b(dust|haze|mist|fog|steam|smoke|particulate|condensation|vapou?r|motes)\b"),
    # NB: no trailing \b on stem-based groups — it would prevent "cockl" matching "cockled".
    ("imperfection", "marks of the object's own history",
     r"\b(fingerprint|scratch|scuff|stain|ring mark|worn|crooked|uneven|chipped|dented|"
     r"frayed|creas|dog-?eared|patina|tarnish|smudge|vignett)"),
    ("provenance", "the object is a specific thing with a history, not a described abstraction",
     r"\b(lot (no|number)|batch|serial|date stamp|signature|signed|letterhead|staple|"
     r"fold(ed| lines?)|stamped|handwritten|receipt|certificate|invoice|label)\b"),
    ("material_response", "materials behaving the way that material behaves (physics)",
     r"\b(cockl|buckl|warp|feather|bloom|soak|wick|pool|sag|drape|slump|melt|"
     r"collaps|absorb|bleed|curl)"),
    ("micro_surface", "micro-contrast: the high-frequency detail models average away",
     r"\b(pore|fibre|fiber|tooth|grain|weave|brushed|micro-?contrast|subsurface|"
     r"specular|catchlight|translucen|sheen)"),
]

# Undecomposable quality assertions. You cannot sweep them, explain them, or bank them —
# St. Pierre's ban, and every one of them is a wish rather than a direction.
BANNED = re.compile(
    r"\b(8k|4k ultra|hdr|vray|octane|unreal engine|masterpiece|award-?winning|"
    r"hyper-?realistic|photo-?realistic|ultra-?detailed|highly detailed|stunning|"
    r"beautiful|gorgeous|breathtaking|epic|cinematic)\b", re.I)


def cmd_lint(args):
    text = args.prompt
    if args.file:
        text = open(args.file, encoding="utf-8").read()
    if not text.strip():
        print("nothing to lint.")
        return 1
    missing, present = [], []
    for name, why, pattern in FLOOR:
        (present if re.search(pattern, text, re.I) else missing).append((name, why))
    banned = sorted(set(m.group(0).lower() for m in BANNED.finditer(text)))

    for name, _ in present:
        print(f"  ok      {name}")
    for name, why in missing:
        print(f"  MISSING {name:<18} — {why}")
    if banned:
        print(f"\n  BANNED terms present: {', '.join(banned)}")
        print("  Replace each with the physical cause underneath it.")

    score = len(present)
    print(f"\n{score}/{len(FLOOR)} floor layers present.")
    if missing:
        print("Every missing layer is one the model will fill with its own averaged default.")
    if args.json:
        print(json.dumps({"present": [n for n, _ in present],
                          "missing": [n for n, _ in missing],
                          "banned": banned, "score": score, "of": len(FLOOR)}))
    return 1 if (missing or banned) and args.strict else 0


# ---------------------------------------------------------------- cli

def main():
    ap = argparse.ArgumentParser(
        prog="style_vault.py",
        description="Keyed style vault over skills/generate/styles/ (brand x ICP x platform).")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="scaffold a card.md for a style")
    p.add_argument("slug")
    p.add_argument("--name")
    p.add_argument("--tier", choices=sorted(TIERS))
    p.add_argument("--family")
    p.add_argument("--brands", nargs="*")
    p.add_argument("--icps", nargs="*")
    p.add_argument("--platforms", nargs="*")
    p.add_argument("--tags", nargs="*")
    p.add_argument("--provenance")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("list", help="list/filter the vault")
    for f in ("brand", "icp", "platform", "tier", "status"):
        p.add_argument(f"--{f}")
    p.add_argument("--json", action="store_true")
    p.add_argument("-v", "--verbose", action="store_true")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("show", help="print one card in full")
    p.add_argument("slug")
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("validate", help="report uncharacterized / unkeyed cards")
    p.add_argument("--strict", action="store_true", help="exit 1 if any card has gaps")
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("index", help="regenerate skills/generate/styles/VAULT.md")
    p.set_defaults(func=cmd_index)

    p = sub.add_parser("permute", help="expand {a, b, c} groups into every combination")
    p.add_argument("template", nargs="?", default="")
    p.add_argument("--file", help="read the template from a file instead")
    p.add_argument("--sample", type=int, help="randomly sample N of the combinations")
    p.add_argument("--limit", type=int, help="cap output after expansion")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_permute)

    p = sub.add_parser("lint", help="check a prompt against the realism floor before generating")
    p.add_argument("prompt", nargs="?", default="")
    p.add_argument("--file", help="read the prompt from a file instead")
    p.add_argument("--strict", action="store_true", help="exit 1 on any missing layer or banned term")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_lint)

    p = sub.add_parser("probe", help="generate a decomposable style-probe sweep")
    p.add_argument("--n", type=int, default=8)
    p.add_argument("--subject", help="the fixed probe subject (never change mid-sweep)")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_probe)

    args = ap.parse_args()
    if args.cmd == "permute" and not args.template and not args.file:
        ap.error("permute needs a template string or --file")
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
