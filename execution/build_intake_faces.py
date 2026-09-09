#!/usr/bin/env python3
"""
build_intake_faces.py — bake the six per-artifact intake landing faces ($0, offline).

Each face is a static prospect-facing pitch page for one Growth Blueprint OS
artifact (positioning-dossier, whitespace-map, bullseye, topic-scan,
format-playbook, growth-blueprint). Reader-purity BINDING: zero operator
language, zero repo paths, zero fabricated numbers — every excerpt line is
quoted verbatim from the live farrice-parallax client exports.

Wiring comes from growth-lab/intake/faces-config.json (single source):
  form_url       Google Form viewform URL (kit: growth-lab/intake/google-form-kit.md)
  prefill_entry  the Q9 prefill parameter, e.g. "entry.123456789"
Both set   -> CTA links to the form with the face's artifact pre-selected.
Either unset -> graceful "intake opens shortly" state (no dead links, no raw tokens).

Output: growth-lab/intake/faces/face-<artifact>.html — self-contained, no JS,
no network calls, no storage. Zero {{...}} tokens may survive the bake.

Usage:
    .venv/bin/python3 execution/build_intake_faces.py            # bake all six
    .venv/bin/python3 execution/build_intake_faces.py --only bullseye
    .venv/bin/python3 execution/build_intake_faces.py --out-dir <dir> --config <json>
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TEMPLATE = ROOT / "templates" / "intake" / "face.html"
DEFAULT_CONFIG = ROOT / "growth-lab" / "intake" / "faces-config.json"
DEFAULT_OUT_DIR = ROOT / "growth-lab" / "intake" / "faces"

# Q9 choice labels — MUST match growth-lab/intake/google-form-kit.md exactly
# (they are both the routing key and the prefill value).
Q9_LABELS = {
    "positioning-dossier": "Positioning Dossier - your buyer, mapped in their own words",
    "whitespace-map": "Whitespace Map - the lanes your niche is leaving open",
    "bullseye": "Audience Bullseye - who to aim at, ring by ring",
    "topic-scan": "Topic Scan - the 50 videos your niche is voting on right now",
    "format-playbook": "Format Playbook - the shapes that carry winning ideas",
    "growth-blueprint": "Growth Blueprint - the full system in one plan",
}

# Every excerpt line below is quoted from growth-lab/farrice-parallax/exports/
# <artifact>-client.html (live engagement, 2026-08-27). Do not paraphrase.
FACES = {
    "positioning-dossier": {
        "label": "Growth report — the Positioning Dossier",
        "headline": "Your buyer, mapped in their own words.",
        "dek": ("Most positioning documents quote the founder. This one quotes the buyer — "
                "real sentences pulled from where your buyers actually talk, ranked by how often "
                "they say them, each one tied to something you sell."),
        "gets_dek": "One document. Four things most brands have never actually written down.",
        "gets": [
            ("A portrait of the one buyer worth aiming at",
             "A person, not a demographic band — what their day looks like, what they already tried, what they said right before buying."),
            ("The pain bank, in their words",
             "Real quotes from forums, reviews, and comment sections where your buyers talk when you are not in the room — each wired to an offer."),
            ("What not-buying protects",
             "The belief they hold, what saying yes would cost them socially, and why your best prospect hesitates. This is the layer generic personas never reach."),
            ("Your authority statement",
             "Three candidate shapes, pressure-tested, one recommendation."),
        ],
        "excerpt": [
            "“facebook ads work for maybe 10-14 days then performance drops off a cliff. I know it's creative fatigue, I know I need new ad concepts, but... I don't have time to endlessly scroll looking for ideas.”",
            "“Six months in looking for customers cold on Meta we've burned through about 30k and gotten only 56 orders.”",
            "Mis-diagnosis reflex: more ads, not a message decision.",
        ],
        "excerpt_source": "Quoted from a finished Positioning Dossier — 7 forum threads, a founder interview, and a 12-channel competitive scan behind it.",
        "ceiling_head": "Stop guessing what your buyer thinks.",
        "ceiling_body": ("Every flat piece of content traces back to the same root: the buyer was imagined, not listened to. "
                        "This report replaces the imagined buyer with the recorded one."),
    },
    "whitespace-map": {
        "label": "Growth report — the Whitespace Map",
        "headline": "The lanes your niche is leaving open.",
        "dek": ("Every channel in your niche is standing somewhere. This report maps where — "
                "and names the positions nobody is holding, with the evidence attached to every claim."),
        "gets_dek": "A map of the field, then the gaps in it. Every score cites the rows behind it.",
        "gets": [
            ("Who holds which position",
             "Each competing channel placed by the belief it teaches its audience — not by follower count."),
            ("The open lanes, with receipts",
             "Positions with proven demand and no owner, each backed by the specific videos and numbers that prove the gap."),
            ("Opening plays per lane",
             "For each open lane: the first piece of content that would plant a flag in it."),
        ],
        "excerpt": [
            "The supplement-specific attention leader teaches launch mechanics, never claim defensibility - and its launch-is-easy belief manufactures the sea of sameness.",
            "Supliful's top outliers: 'No Warehouse, No Problem' (20K views, 33.2x channel normal, 2025-01-24); 'Launch Your Product Line and Sell Immediately' (11K, 18.3x, 2025-01-17).",
            "Mechanism-of-the-week content is the niche's strongest current wave.",
        ],
        "excerpt_source": "Quoted from a finished Whitespace Map — competitive scan: 12 channels, 50 ranked videos, 10 transcripts.",
        "ceiling_head": "Crowded lanes cost you months.",
        "ceiling_body": ("Publishing into a lane someone already owns means paying full price for second place. "
                        "The map shows you where the field is empty before you spend a single filming day."),
    },
    "bullseye": {
        "label": "Growth report — the Audience Bullseye",
        "headline": "Who to aim at, ring by ring — with the money attached.",
        "dek": ("Reach is not one audience; it is rings of them, and each ring pays differently. "
                "This report draws yours — who converts, who feeds the inner rings, and which viral win would actually hurt you."),
        "gets_dek": "Your audience drawn as concentric rings, each with its economics stated plainly.",
        "gets": [
            ("The center ring, named",
             "The buyer segment that actually converts — sized, described, and matched to the offer it feeds."),
            ("The feeder rings",
             "Audiences that never buy directly but carry your reach — and the recognition mechanics that move them inward."),
            ("The wrong-audience warning",
             "The outer ring where a viral hit teaches the algorithm to bring you the wrong people. Marked so you never chase it by accident."),
        ],
        "excerpt": [
            "Operating category founders without a live occasion. Converts: teardown to $750 Angle Map. Competition thin: Chew On This (no breakouts), Marketing Operators (13.3K).",
            "All DTC founders with paid-acquisition pain. Reach engine only; feeds inner rings by recognition. Heavy competition: 147K-928K sub channels.",
            "Anyone into marketing/business/AI. Hormozi's 4.44M gravity. Craft-only zone; a viral hit here teaches the algorithm the wrong audience.",
        ],
        "excerpt_source": "Quoted from a finished Audience Bullseye — built on a positioning dossier, a whitespace map, and a 12-channel competitive scan.",
        "ceiling_head": "Views that never convert are not free. They are expensive.",
        "ceiling_body": ("Every video trains the algorithm on who to bring you next. The bullseye makes sure "
                        "you are training it toward buyers, not applause."),
    },
    "topic-scan": {
        "label": "Growth report — the Topic Scan",
        "headline": "The 50 videos your niche is voting on right now.",
        "dek": ("Fifty recent videos from your niche, each measured against its own channel's normal — "
                "so a small channel's breakout counts as loudly as a giant's. Then the strikes: which winners you should ignore, and why."),
        "gets_dek": "A live scoreboard of demand, with the disqualified rows shown instead of hidden.",
        "gets": [
            ("The ranked 50",
             "Every row receipted: title, views, how far past the channel's own baseline it ran, and the date."),
            ("Topic waves, named",
             "Rows clustered into the waves actually moving right now, each with the mechanism that powers it."),
            ("The strike list",
             "Winners struck with reasons — wrong audience, off-niche, or a person winning rather than a topic. The rows most reports would quietly count."),
        ],
        "excerpt": [
            "A - Mechanism Waves: median 12.0x, rising (all rows Jul-Aug 2026). Mechanism: new-tool hope.",
            "'Amazon Just Lost Control Of Shopping!' - 1.4M views, 64.2x, 2026-04-28; two of three rows are the same channel.",
            "Strikes shown, not hidden: wrong-avatar 7, off-niche 5, craft-source 5.",
        ],
        "excerpt_source": "Quoted from a finished Topic Scan — 12 channels, 50 ranked videos, two snapshots.",
        "ceiling_head": "Demand is public. Almost nobody reads it.",
        "ceiling_body": ("Your niche publishes its own scoreboard every week — which ideas pull and which die. "
                        "The scan reads it for you before you spend a filming day on a topic the market already rejected."),
    },
    "format-playbook": {
        "label": "Growth report — the Format Playbook",
        "headline": "The shapes that carry winning ideas.",
        "dek": ("Copying winners without the mechanism is cargo cult. This report names the structures "
                "behind your niche's breakouts — why each one holds attention, where it fails, and which fit you."),
        "gets_dek": "Structures and layouts with the mechanism attached — not a list of trends to imitate.",
        "gets": [
            ("The structures, verified",
             "Each one traced through real transcripts, with median performance across its rows and the psychological pull that makes it work."),
            ("The failure modes",
             "Every format has one. Named up front, so you know what breaks it before you ship in it."),
            ("Your test set",
             "The formats worth your next batch: proven bets separated from labeled experiments, never blended."),
        ],
        "excerpt": [
            "S1 The Compression Promise - promise-debt plus ranked-completion pull. 5 rows, median 10.8x.",
            "'Give Me 27 Minutes and I'll Make You Disgustingly Good at Digital Marketing' - 201K, 14.1x, 2026-07-31. Failure mode: promise bigger than payload reads as betrayal.",
            "S2 The Shift Analysis - chaos vigilance plus insider decoding. 6 rows, ceiling 64.2x (person-effect flagged).",
        ],
        "excerpt_source": "Quoted from a finished Format Playbook — 25 qualified rows, 10 transcripts behind the structures.",
        "ceiling_head": "The idea was right. The shape killed it.",
        "ceiling_body": ("Most good ideas die in the wrong container. The playbook matches your ideas to the "
                        "structures your niche has already proven it will watch."),
    },
    "growth-blueprint": {
        "label": "Growth report — the Content Growth Blueprint",
        "headline": "The full system: positioning, audience, topics, formats, money.",
        "dek": ("The flagship. Everything the single reports establish — your buyer, the open lanes, the rings, "
                "the scoreboard, the shapes — assembled into one operating plan with the bets ranked and the reasoning shown."),
        "gets_dek": "Five reports' worth of evidence, resolved into one plan you can run.",
        "gets": [
            ("The whole field, settled",
             "Buyer portrait, open lanes, audience rings, live topic scoreboard, and format structures — each built on measured data, none on vibes."),
            ("The bet register",
             "Every recommendation ranked, with what it costs, what it should return, and what would prove it wrong."),
            ("The operating plan",
             "What to publish, in which shape, aimed at which ring — sequenced so each piece feeds the next."),
        ],
        "excerpt": [
            "W1 - The Defensible Claim lane: zero of fifty ranked rows touch claims or compliance.",
            "W2 - Nobody names the operating supplement founder as their audience.",
            "Behind the plan: 5 state artifacts, 12 channels, 50 receipted rows, 12 buyer verbatims.",
        ],
        "excerpt_source": "Quoted from a finished Content Growth Blueprint — the assembled flagship, built on all five underlying reports.",
        "ceiling_head": "Strategy is deciding before you spend.",
        "ceiling_body": ("Every dollar and every filming day lands better when the message, the audience, and the "
                        "format were settled first. The Blueprint is that settlement, in writing."),
    },
}


def esc(value):
    return html.escape(str(value), quote=False) if value is not None else ""


def load_config(path):
    """Return (config_dict, note). Missing/unreadable config degrades to unset
    wiring with a loud note — the bake still ships the opening-soon state."""
    p = Path(path)
    if not p.exists():
        return {}, f"config missing: {p} — baking unwired"
    try:
        cfg = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return {}, f"config unreadable ({e.__class__.__name__}) — baking unwired"
    if not isinstance(cfg, dict):
        return {}, "config is not a JSON object — baking unwired"
    return cfg, "ok"


def cta_block(cfg, artifact):
    """(cta_html, cta_note, wired_bool). Wired only when BOTH form_url and
    prefill_entry are set and sane; anything else is the graceful soon-state."""
    form_url = (cfg.get("form_url") or "").strip()
    entry = (cfg.get("prefill_entry") or "").strip()
    wired = (form_url.startswith("https://") and re.fullmatch(r"entry\.\d+", entry) is not None)
    if wired:
        joiner = "&" if "?" in form_url else "?"
        url = f"{form_url}{joiner}usp=pp_url&{entry}={quote_plus(Q9_LABELS[artifact])}"
        cta = f'<a class="cta" href="{html.escape(url)}" rel="noopener">Start the nine questions</a>'
        note = "Opens the intake form with this report already selected. Nine questions, about seven minutes."
        return cta, note, True
    cta = '<span class="cta cta--soon">Intake opens shortly</span>'
    note = "This page is being connected to the intake form. If you were sent here directly, reply to the message that brought you and the nine questions come to you instead."
    return cta, note, False


def bake_face(template, artifact, cfg):
    face = FACES[artifact]
    gets_rows = []
    for i, (name, sub) in enumerate(face["gets"], 1):
        gets_rows.append(
            '        <li class="get-row">\n'
            f'          <span class="get-rank">{i:02d}</span>\n'
            '          <span>\n'
            f'            <span class="get-name">{esc(name)}</span>\n'
            f'            <span class="get-sub">{esc(sub)}</span>\n'
            '          </span>\n'
            '        </li>'
        )
    excerpt_rows = [f'        <p>{esc(line)}</p>' for line in face["excerpt"]]
    cta, cta_note, wired = cta_block(cfg, artifact)

    out = template
    replacements = {
        "{{FACE_TITLE}}": esc(face["label"].replace("—", "-")) + " - Farrice Cain",
        "{{FACE_LABEL}}": esc(face["label"]),
        "{{HEADLINE}}": esc(face["headline"]),
        "{{DEK}}": esc(face["dek"]),
        "{{GETS_DEK}}": esc(face["gets_dek"]),
        "{{GETS_ROWS}}": "\n".join(gets_rows),
        "{{EXCERPT_ROWS}}": "\n".join(excerpt_rows),
        "{{EXCERPT_SOURCE}}": esc(face["excerpt_source"]),
        "{{CEILING_HEAD}}": esc(face["ceiling_head"]),
        "{{CEILING_BODY}}": esc(face["ceiling_body"]),
        "{{CTA_BLOCK}}": cta,
        "{{CTA_NOTE}}": esc(cta_note),
        "{{FOOT_LINE}}": "A free mini-read of your niche within 48 hours of your answers. The full report only if you ask for it.",
    }
    for key, val in replacements.items():
        out = out.replace(key, val)

    leftover = sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", out)))
    if leftover:
        raise SystemExit(f"[build_intake_faces] FAIL — unreplaced tokens in {artifact}: {', '.join(leftover)}")
    return out, wired


def main():
    ap = argparse.ArgumentParser(description="Bake the six per-artifact intake landing faces.")
    ap.add_argument("--only", choices=sorted(FACES), help="Bake a single face")
    ap.add_argument("--config", default=str(DEFAULT_CONFIG), help="faces-config.json path")
    ap.add_argument("--template", default=str(DEFAULT_TEMPLATE), help="Template override")
    ap.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR), help="Output directory")
    args = ap.parse_args()

    tpl_path = Path(args.template)
    if not tpl_path.exists():
        raise SystemExit(f"[build_intake_faces] FAIL — template missing: {tpl_path}")
    template = tpl_path.read_text(encoding="utf-8")

    cfg, cfg_note = load_config(args.config)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    targets = [args.only] if args.only else sorted(FACES)
    wired_any = False
    for artifact in targets:
        page, wired = bake_face(template, artifact, cfg)
        dest = out_dir / f"face-{artifact}.html"
        dest.write_text(page, encoding="utf-8")
        wired_any = wired_any or wired
        print(f"[build_intake_faces] wrote {dest} — cta={'wired' if wired else 'opening-soon'}")

    state = "wired" if wired_any else "unwired (fill form_url + prefill_entry in faces-config.json, then re-bake)"
    print(f"[build_intake_faces] {len(targets)} face(s) baked — config={cfg_note} — {state} — $0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
