#!/usr/bin/env python3
"""
Creative model router for the Antigravity Supercomputer.

Given a creative task description, returns:
  - which service to call (fal-poster, higgsfield-soul, veo-3, etc.)
  - estimated cost
  - reason for the route
  - the cost_gate.py command to run as pre-flight

Goal: replace Higgsfield Supercomputer's opaque "Orchestrator picks the right model"
with a transparent, editable routing table that Farrice owns.

Routing is signal-based: we look for keywords/patterns in the task description
and route to the cheapest-good-enough model that handles that signal. If multiple
signals match, prefer the more specific one.

Usage:
  python3 creative_router.py route --task "photoreal hero shot for resistance band product page"
  python3 creative_router.py route --task "15-second cinematic ad for streetwear brand" --budget 3.00
  python3 creative_router.py route --task "stylized vintage poster for indie game" --json
  python3 creative_router.py rules         # show all routing rules
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# ───────────────────────────────────────────────────────────────────
# ROUTING RULES — TASTE-CALL ZONE (Farrice)
#
# These are first-pass heuristics. Tune them after running 5-10 real
# Supercomputer missions. Order matters: first match wins, so put the
# most specific patterns FIRST and the generic fallbacks LAST.
#
# Each rule:
#   - patterns: regex patterns that signal this task type
#   - service:  cost_gate.py --service value
#   - reason:   why this route (shown in route output)
#   - notes:    optional Farrice-only notes
# ───────────────────────────────────────────────────────────────────
RULES = [
    # ─── Logos / transparent assets ───
    {
        "patterns": [r"\blogo\b", r"\btransparent\b", r"\bremove\s+background\b",
                     r"\brembg\b", r"\bcutout\b"],
        "service": "fal-rembg",
        "reason": "Logo / transparent asset → Fal rembg (cheapest transparency)",
        "notes": "Chain after a poster generation if logo is brand new",
    },

    # ─── Stylized posters / brand visuals (Fal GPT-Image-2 is best at this) ───
    {
        "patterns": [r"\bposter\b", r"\bstylized\b", r"\bvintage\b", r"\bSwiss\b",
                     r"\bUkiyo[- ]?e\b", r"\bbrutalism\b", r"\bneon[- ]?noir\b",
                     r"\beditorial\b", r"\bstreet\s*wear\b", r"\bchalkboard\b",
                     r"\bmenu\b", r"\bpackaging\b", r"\bUI\s*mockup\b"],
        "service": "fal-poster",
        "reason": "Stylized visual → Fal GPT-Image-2 via fantastic-posters (38 styles)",
        "notes": "For concept-first, non-redundant work run /fantastic-studio (art-direct → divergence → route → critique) instead of a bare prompt. --quality=medium first pass; high only for finals.",
    },

    # ─── Photoreal product / lifestyle / hero shots + PEOPLE (Higgsfield Soul wins) ───
    {
        "patterns": [r"\bphotoreal\b", r"\bphoto[- ]?realistic\b", r"\bproduct\s+(hero|shot|photo)\b",
                     r"\blifestyle\s+shot\b", r"\bproduct\s+page\b",
                     r"\bamazon\s+listing\b", r"\be-?commerce\b",
                     # People / character consistency — Soul is the roster's face model
                     r"\bportrait\b", r"\b(a\s+)?person\b", r"\bpeople\b", r"\bmodel\s+(wearing|shot|photo)\b",
                     r"\bcharacter\s+(consistency|reference)?\b", r"\bheadshot\b", r"\bface\b",
                     r"\bon[- ]?body\b", r"\bugc\s+(photo|still)\b", r"\btalent\b"],
        "service": "higgsfield-soul",
        "reason": "Photoreal / people / character → Higgsfield Soul 2.0 (best photoreal + face consistency)",
        "notes": "One-off people shots and product heroes route here, not fal-poster. Attach a character ref for consistency. Character BUILDS (face lock, outfit base, character sheet, persistent characters) → load skills/banana-pro-director/SKILL.md: Banana Pro (Nano Banana) is the build default, Higgsfield GPT-2 the fidelity escalation (≠ OpenAI GPT Image 2 / gpt-image-2-director), Soul the two-step iteration path.",
    },

    # ─── Quick concept images / cheap iteration (Nano Banana Pro) ───
    {
        "patterns": [r"\bquick\b", r"\bdraft\b", r"\bconcept\s+image\b", r"\biterate\b",
                     r"\bsketch\b", r"\bvariation\b"],
        "service": "higgsfield-nano",
        "reason": "Quick iteration → Higgsfield Nano Banana Pro (fastest, cheapest)",
    },

    # ─── Editing an existing image ───
    {
        "patterns": [r"\bedit\s+this\s+(image|photo|poster)\b", r"\bswap\b",
                     r"\bchange\s+the\b", r"\breplace\b", r"\binpaint\b", r"\boutpaint\b"],
        "service": "fal-edit",
        "reason": "Image edit → Fal GPT-Image-2 image-to-image (mask-aware)",
        "notes": "Requires --input + optional --mask; see directives/fal-edit-mode-guide.md",
    },

    # ─── Multi-shot video / longer UGC ad (Kling v3 — multi-shot is its strength) ───
    {
        "patterns": [r"\bmulti[- ]?shot\b", r"\bsequence\b", r"\bnarrative\s+video\b",
                     r"\b(\d{2,}|\d+)\s*(?:-|\s)?second\s+(ad|video)\b",
                     r"\bUGC\s+ad\b", r"\bad\s+with\s+cuts\b"],
        "service": "fal-kling",
        "reason": "Multi-shot video → Kling v3 Pro (handles cuts/sequences better than Seedance)",
        "notes": "Default duration 10s; pass --duration=15 for longer",
    },

    # ─── Cinematic single-shot video (Higgsfield Cinema Studio) ───
    {
        "patterns": [r"\bcinematic\b", r"\bfilm\s+look\b", r"\bmoody\b",
                     r"\bcinema\s+studio\b", r"\bdolly\b", r"\bcrane\s+shot\b"],
        "service": "higgsfield-cinema",
        "reason": "Cinematic single-shot → Higgsfield Cinema Studio 3.5",
        "notes": "5-10s clips. For longer/multi-shot, prefer Kling. Cinematic prompt construction → skills/cinema-worldbuilder-pro/SKILL.md (block grammar, FOV degrees, Capture Realism).",
    },

    # ─── Premium cinema-grade (Veo 3.1 — uses Google Ultra quota) ───
    {
        "patterns": [r"\bveo\b", r"\bgoogle\s+flow\b", r"\bpremium\s+cinema\b",
                     r"\bfinal\s+spot\b", r"\bbroadcast[- ]?quality\b"],
        "service": "veo-3",
        "reason": "Premium cinema → Veo 3.1 via Google Flow (Ultra quota, $0 marginal)",
        "notes": "Use sparingly — quota is limited per day. Prefer for hero spots only.",
    },

    # ─── Short cinematic clip — Seedance 720p as the cheap cinematic default ───
    {
        "patterns": [r"\b(short|\d?\s*sec(ond)?s?)\s+(video|clip|ad)\b",
                     r"\b5[- ]?second\b", r"\b8[- ]?second\b"],
        "service": "fal-seedance-720p",
        "reason": "Short cinematic clip → Seedance 720p (cheaper than Cinema Studio for single shots)",
        "notes": "Audio NOT consistent across multi-clip stitches — use single-take only. Seedance prompt construction → skills/cinema-worldbuilder-pro/SKILL.md (Fal surface = no @tags, use prose descriptors).",
    },

    # ─── Virality check ───
    {
        "patterns": [r"\bvirality\b", r"\bpredict\s+engagement\b", r"\bhook\s+strength\b",
                     r"\battention\s+score\b"],
        "service": "higgsfield-virality",
        "reason": "Virality prediction → Higgsfield virality predictor",
    },

    # ─── Voiceover / TTS (wrapper-less recipe via generate_media.py) ───
    {
        "patterns": [r"\bvoice[- ]?over\b", r"\btts\b", r"\btext[- ]to[- ]speech\b",
                     r"\bnarrat(e|ion|or)\b", r"\bread\s+(this|it)\s+aloud\b"],
        "service": "fal-generic",
        "reason": "Voiceover/TTS → Fal-hosted speech recipe via generate_media.py (see skills/generate/models/)",
        "notes": "python3 execution/generate_media.py run --model minimax-speech --prompt \"<text>\" — quote first.",
    },

    # ─── Music / jingle (wrapper-less recipe via generate_media.py) ───
    {
        "patterns": [r"\bmusic\b", r"\bjingle\b", r"\bsoundtrack\b", r"\btheme\s+song\b",
                     r"\bbackground\s+audio\b"],
        "service": "fal-generic",
        "reason": "Music generation → Fal-hosted music recipe via generate_media.py (see skills/generate/models/)",
        "notes": "Quote first; per-generation pricing in the recipe file.",
    },

    # ─── Text-only generation (always free under Gemini Ultra) ───
    {
        "patterns": [r"\bcopy\b", r"\bheadline\b", r"\bcaption\b", r"\bscript\b",
                     r"\bemail\b", r"\bpost\b", r"\bnewsletter\b", r"\bdescription\b",
                     r"\bbrief\b"],
        "service": "gemini-text",
        "reason": "Text generation → Gemini text (Ultra quota, effectively free)",
        "notes": "Routes to ghostwrite/parallax/writers-room/copy skills downstream",
    },

    # ─── FALLBACK: generic image request ───
    {
        "patterns": [r"\bimage\b", r"\bvisual\b", r"\bgraphic\b", r"\bpicture\b"],
        "service": "fal-poster",
        "reason": "Generic image request → default to Fal GPT-Image-2 (highest quality general-purpose)",
        "notes": "If this matches when you expected Higgsfield Soul, add more specific signal words",
    },

    # ─── FALLBACK: generic video request ───
    {
        "patterns": [r"\bvideo\b", r"\bmotion\b", r"\banimat(e|ion)\b"],
        "service": "fal-seedance-720p",
        "reason": "Generic video request → default to Seedance 720p (best cost/quality for single shots)",
    },
]


def find_route(task: str, budget_usd: float | None = None) -> dict:
    """Walk RULES in order, return first match."""
    task_lower = task.lower()
    for rule in RULES:
        for pattern in rule["patterns"]:
            if re.search(pattern, task_lower):
                route = {
                    "service": rule["service"],
                    "reason": rule["reason"],
                    "matched_pattern": pattern,
                    "task": task,
                    "notes": rule.get("notes", ""),
                }
                route["cost_gate_cmd"] = (
                    f'python3 execution/cost_gate.py check '
                    f'--service {rule["service"]} --request "{task}"'
                )
                return route
    return {
        "service": None,
        "reason": "No matching rule. Add a rule to creative_router.RULES or pass an explicit --service.",
        "task": task,
        "cost_gate_cmd": None,
    }


# ───────────────────────────────────────────────────────────────────
# CLI
# ───────────────────────────────────────────────────────────────────
def cmd_route(args) -> int:
    route = find_route(args.task, budget_usd=args.budget)
    if args.json:
        print(json.dumps(route, indent=2))
        return 0 if route.get("service") else 1

    if not route.get("service"):
        print(f"❌ No route found for: {args.task}")
        print(f"   {route['reason']}")
        return 1

    print("=" * 60)
    print(f"CREATIVE ROUTER")
    print("=" * 60)
    print(f"Task:    {route['task']}")
    print(f"Service: {route['service']}")
    print(f"Why:     {route['reason']}")
    print(f"Matched: /{route['matched_pattern']}/")
    if route.get("notes"):
        print(f"Notes:   {route['notes']}")
    print()
    print(f"Pre-flight:")
    print(f"  {route['cost_gate_cmd']}")
    return 0


def cmd_rules(_args) -> int:
    print(f"Creative Router — {len(RULES)} rules (first match wins)\n")
    for i, rule in enumerate(RULES, 1):
        print(f"{i:>2}. {rule['service']:<24s} {rule['reason']}")
        for p in rule["patterns"]:
            print(f"      /{p}/")
        if rule.get("notes"):
            print(f"      └ {rule['notes']}")
        print()
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Creative model router")
    sub = p.add_subparsers(dest="cmd", required=True)

    pr = sub.add_parser("route", help="Route a creative task to the right service")
    pr.add_argument("--task", required=True, help="Free-text task description")
    pr.add_argument("--budget", type=float, help="(Optional) max USD for this call")
    pr.add_argument("--json", action="store_true", help="Emit JSON instead of human-readable")

    sub.add_parser("rules", help="Show all routing rules")

    args = p.parse_args()
    return {
        "route": cmd_route,
        "rules": cmd_rules,
    }[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
