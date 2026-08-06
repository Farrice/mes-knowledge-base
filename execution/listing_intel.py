#!/usr/bin/env python3
"""listing_intel.py — client-agnostic real-estate listing intake for the
automated content pipeline.

WHY THIS EXISTS
---------------
Listing content gets spoken ON CAMERA. A hallucinated spa, a phantom finished
basement, or a bed count that doesn't survive arithmetic is a credibility kill
for the agent whose face is on the video (factual veto territory). MLS
structured fields and the free-text description are written by different hands
and routinely disagree — so intake must be deterministic (regex + arithmetic,
zero LLM judgment) and every fact must carry a provenance label before a
script ever quotes it. Same law as content_finish_gate.py: never ship infra
that depends on a model remembering to check.

Stdlib only (no network, no env) — this is pure local parsing.

Subcommands:
    parse <dump_path> --slug S [--out-dir D] [--paste <txt>]
                    Ingest a saved page dump (HTML with JSON-LD, a
                    hand-assembled listing .json, or --paste plain text) into
                    <out-dir>/<slug>/listing.json. Every field nullable;
                    unknown = null, NEVER a guess.
    diff --slug S   Compare structured facts vs the free-text description;
                    emit contradictions/risks/confirm items to
                    <slug>/claims-diff.json + a human table.
    ledger --slug S Build <slug>/claims-ledger.json — every on-camera claim
                    with source + VERIFIED/LIKELY/UNCONFIRMED confidence,
                    merged with diff findings.
    selftest        Run parse+diff+ledger against the bundled fixture in a
                    temp dir; exit 0 all pass / 1 any fail.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import sys
import tempfile
from datetime import datetime
from html import unescape
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT_DIR = REPO_ROOT / "_active" / "jen-listings"
FIXTURE = Path(__file__).resolve().parent / "tests" / "fixtures" / "5200-armida.json"

# ---------------------------------------------------------------- schema ----

ADU_KEYS = ["present", "beds", "baths", "sqft", "has_kitchen"]
FEATURE_KEYS = ["pool", "spa", "basement", "fireplace", "garage_spaces",
                "central_air", "single_story", "outdoor_kitchen", "furnished"]
SCALAR_KEYS = ["slug", "address", "city", "zip", "price", "beds", "baths",
               "baths_full", "baths_half", "beds_main", "baths_main", "sqft",
               "lot_acres", "lot_sqft", "year_built", "stories",
               "property_type", "mls", "brokerage", "description",
               "zestimate", "rent_zestimate", "walk_score",
               "parsed_at", "source"]
LIST_KEYS = ["agents", "open_houses", "photos", "price_history", "schools"]


def empty_listing(slug: str) -> Dict[str, Any]:
    d: Dict[str, Any] = {k: None for k in SCALAR_KEYS}
    d.update({k: [] for k in LIST_KEYS})
    d["adu"] = {k: None for k in ADU_KEYS}
    d["features"] = {k: None for k in FEATURE_KEYS}
    d["tax"] = {"assessed": None, "annual": None}
    d["slug"] = slug
    return d


def _num(s: Any) -> Optional[float]:
    """'4,200' / '4.5' -> number; None on anything that doesn't cleanly parse."""
    if s is None:
        return None
    if isinstance(s, (int, float)):
        return s
    try:
        v = float(str(s).replace(",", "").replace("$", "").strip())
        return int(v) if v == int(v) else v
    except ValueError:
        return None


def _int(s: Any) -> Optional[int]:
    v = _num(s)
    return int(v) if v is not None else None


def _money(v: float) -> str:
    return f"${int(v):,}"

# ----------------------------------------------------------- parse: HTML ----

JSONLD_RE = re.compile(
    r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.S | re.I)
PROPERTY_TYPES = {"RealEstateListing", "Product", "SingleFamilyResidence",
                  "House", "Residence", "Apartment"}


def _jsonld_blocks(html: str) -> List[dict]:
    """All JSON-LD objects in the page, @graph/list flattened. Bad JSON is
    skipped silently — a broken block must never invent a fact."""
    out: List[dict] = []
    for raw in JSONLD_RE.findall(html):
        try:
            data = json.loads(raw.strip())
        except json.JSONDecodeError:
            continue
        stack = data if isinstance(data, list) else [data]
        for node in stack:
            if not isinstance(node, dict):
                continue
            out.append(node)
            graph = node.get("@graph")
            if isinstance(graph, list):
                out.extend(n for n in graph if isinstance(n, dict))
    return out


def _visible_text(html: str) -> str:
    body = re.sub(r"<(script|style)\b.*?</\1>", " ", html, flags=re.S | re.I)
    return unescape(re.sub(r"<[^>]+>", " ", body))


def _apply_jsonld(listing: Dict[str, Any], blocks: List[dict]) -> None:
    for node in blocks:
        t = node.get("@type", "")
        types = set(t) if isinstance(t, list) else {t}
        if types & PROPERTY_TYPES:
            addr = node.get("address") or {}
            if isinstance(addr, dict):
                listing["address"] = listing["address"] or addr.get("streetAddress")
                listing["city"] = listing["city"] or addr.get("addressLocality")
                listing["zip"] = listing["zip"] or addr.get("postalCode")
            offers = node.get("offers") or {}
            if isinstance(offers, dict):
                listing["price"] = listing["price"] or _int(offers.get("price"))
            listing["beds"] = listing["beds"] or _num(node.get("numberOfBedrooms"))
            listing["baths"] = listing["baths"] or _num(node.get("numberOfBathroomsTotal"))
            listing["year_built"] = listing["year_built"] or _int(node.get("yearBuilt"))
            fs = node.get("floorSize") or {}
            if isinstance(fs, dict):
                listing["sqft"] = listing["sqft"] or _int(fs.get("value"))
            if node.get("description") and not listing["description"]:
                listing["description"] = str(node["description"]).strip()
            imgs = node.get("image")
            if isinstance(imgs, list) and not listing["photos"]:
                listing["photos"] = [str(i) for i in imgs]
        if "Event" in types:  # Zillow open-house Events
            start, end = str(node.get("startDate", "")), str(node.get("endDate", ""))
            if len(start) >= 16:
                listing["open_houses"].append({
                    "date": start[:10], "start": start[11:16],
                    "end": end[11:16] if len(end) >= 16 else None})


# Facts Zillow renders as visible "Label: value" text. Conservative: each
# regex is anchored to its label — no label, no value, no guess.
def _apply_text_facts(listing: Dict[str, Any], text: str) -> None:
    def grab(pattern: str, flags=re.I) -> Optional[str]:
        m = re.search(pattern, text, flags)
        return m.group(1).strip() if m else None

    listing["year_built"] = listing["year_built"] or _int(grab(r"Year built:\s*(\d{4})"))
    listing["baths_full"] = listing["baths_full"] or _int(grab(r"Full bathrooms:\s*(\d+)"))
    listing["baths_half"] = listing["baths_half"] or _int(grab(r"1/2 bathrooms:\s*(\d+)"))
    if listing["baths"] is None and listing["baths_full"] is not None:
        listing["baths"] = _num(listing["baths_full"] + 0.5 * (listing["baths_half"] or 0))

    # Single-token capture only: tag-stripped text runs labels together
    # ("Spa features: None Basement: Finished ..."), and a greedy class here
    # swallowed the next label — turning "None" truthy. First token decides.
    spa = grab(r"Spa features:\s*([A-Za-z][A-Za-z/-]*)")
    if spa is not None and listing["features"]["spa"] is None:
        listing["features"]["spa"] = spa.strip().lower() not in ("none", "no")
    basement = grab(r"Basement:\s*([A-Za-z][A-Za-z/-]*)")
    if basement is not None and listing["features"]["basement"] is None:
        listing["features"]["basement"] = None if basement.lower() in ("none", "no") else basement
    garage = grab(r"Garage spaces:\s*(\d+)")
    if garage is not None and listing["features"]["garage_spaces"] is None:
        listing["features"]["garage_spaces"] = _int(garage)
    levels = grab(r"Levels?:\s*(One|Two|Three|\d+)")
    if levels is not None and listing["stories"] is None:
        listing["stories"] = {"one": 1, "two": 2, "three": 3}.get(levels.lower()) or _int(levels)
        listing["features"]["single_story"] = listing["stories"] == 1

    listing["walk_score"] = listing["walk_score"] or _int(grab(r"Walk Score(?:®)?\D{0,10}(\d{1,3})"))
    listing["rent_zestimate"] = listing["rent_zestimate"] or _int(
        grab(r"Rent Zestimate(?:®)?\D{0,20}\$([\d,]+)"))
    listing["zestimate"] = listing["zestimate"] or _int(
        grab(r"(?<!Rent )Zestimate(?:®)?\D{0,20}\$([\d,]+)"))
    listing["mls"] = listing["mls"] or grab(r"MLS\s*#?\s*:?\s*([A-Z]{1,3}\d{6,10})", 0)
    # Bare-number fallbacks — only fire when nothing structured already won.
    _apply_paste_facts(listing, text)


# --------------------------------------------------------- parse: paste -----

def _apply_paste_facts(listing: Dict[str, Any], text: str) -> None:
    """Regex-only extraction for unstructured text. Anything a pattern can't
    pin down with confidence stays null."""
    def grab(pattern: str) -> Optional[str]:
        m = re.search(pattern, text, re.I)
        return m.group(1) if m else None

    listing["price"] = listing["price"] or _int(grab(r"\$(\d{1,3}(?:,\d{3}){1,3})(?!\d)"))
    listing["beds"] = listing["beds"] or _num(grab(r"(\d+)\s*(?:bd|beds?)\b"))
    listing["baths"] = listing["baths"] or _num(grab(r"(\d+(?:\.\d+)?)\s*(?:ba|baths?)\b"))
    listing["sqft"] = listing["sqft"] or _int(grab(r"([\d,]{3,})\s*(?:sq\s*\.?\s*ft|sqft)\b(?!\s*lot)"))
    listing["lot_acres"] = listing["lot_acres"] or _num(grab(r"([\d.]+)\s*acres?\b"))
    listing["lot_sqft"] = listing["lot_sqft"] or _int(grab(r"([\d,]{4,})\s*(?:sq\s*\.?\s*ft|sqft)\s*lot\b"))
    listing["year_built"] = listing["year_built"] or _int(grab(r"(?:year\s*built|built\s*in)\D{0,5}((?:19|20)\d{2})"))
    listing["mls"] = listing["mls"] or grab(r"MLS\s*#?\s*:?\s*([A-Z]{0,3}\d{6,10})")


# ----------------------------------------------------------- parse: json ----

def _merge_json(listing: Dict[str, Any], data: Dict[str, Any]) -> List[str]:
    """Pass-through with validation: known keys deep-merged, unknown top-level
    keys reported (kept out of the artifact — schema is the contract)."""
    unknown: List[str] = []
    for k, v in data.items():
        if k == "adu" and isinstance(v, dict):
            listing["adu"].update({kk: vv for kk, vv in v.items()})
        elif k == "features" and isinstance(v, dict):
            listing["features"].update(v)  # features is open-ended by design
        elif k == "tax" and isinstance(v, dict):
            listing["tax"].update(v)
        elif k in SCALAR_KEYS or k in LIST_KEYS:
            listing[k] = v
        else:
            unknown.append(k)
    return unknown


def do_parse(dump_path: Optional[Path], slug: str, out_dir: Path,
             paste_path: Optional[Path] = None) -> Dict[str, Any]:
    listing = empty_listing(slug)
    if paste_path is not None:
        text = paste_path.read_text()
        _apply_paste_facts(listing, text)
        listing["description"] = text.strip()
        listing["source"] = "paste"
    elif dump_path is not None and dump_path.suffix.lower() == ".json":
        data = json.loads(dump_path.read_text())
        if not isinstance(data, dict):
            raise ValueError(f"{dump_path}: expected a JSON object")
        unknown = _merge_json(listing, data)
        if unknown:
            print(f"  note: unknown keys ignored: {', '.join(unknown)}")
        listing["slug"] = slug
        listing["source"] = "json"
    elif dump_path is not None:
        html = dump_path.read_text(errors="replace")
        _apply_jsonld(listing, _jsonld_blocks(html))
        _apply_text_facts(listing, _visible_text(html))
        listing["source"] = "html_dump"
    else:
        raise ValueError("parse needs a dump path or --paste")

    listing["parsed_at"] = datetime.now().isoformat(timespec="seconds")
    dest = out_dir / slug
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "listing.json").write_text(json.dumps(listing, indent=2) + "\n")
    return listing

# ------------------------------------------------------------------ diff ----
# The core mechanic: structured MLS facts vs free-text description. A
# contradiction here is exactly the thing that gets an agent called out in
# the comments — catch it before the script is written, not after.

SPA_RE = re.compile(r"\b(spa|hot\s*tub|jacuzzi)\b", re.I)
BRAND_RE = re.compile(r"\b(Thermador|Sub-?Zero|Wolf|Viking|Miele)\b")
MATERIAL_RE = re.compile(r"\b(porcelain|quartz|granite)\b", re.I)
BED_COUNT_RE = re.compile(r"(\d+(?:\.\d+)?)[\s-]*bed(?:room)?s?\b", re.I)
BATH_COUNT_RE = re.compile(r"(\d+(?:\.\d+)?)[\s-]*bath(?:room)?s?\b", re.I)


def _feature_false(v: Any) -> bool:
    return v is False or (isinstance(v, str) and v.strip().lower() in ("none", "no", "false"))


def _feature_true(v: Any) -> bool:
    if isinstance(v, str):
        return v.strip().lower() not in ("none", "no", "false", "")
    return v is True


def diff_listing(listing: Dict[str, Any]) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    desc = listing.get("description") or ""
    feats = listing.get("features") or {}
    adu = listing.get("adu") or {}

    def add(check: str, severity: str, detail: str,
            dont_say: Optional[str] = None, fallback: Optional[str] = None) -> None:
        item: Dict[str, Any] = {"check": check, "severity": severity, "detail": detail}
        if dont_say:
            item["dont_say"] = dont_say
        if fallback:
            item["fallback_line"] = fallback
        items.append(item)

    # 1) Spa: description says spa/hot tub, structured says no (or unknown).
    spa_hit = SPA_RE.search(desc)
    if spa_hit:
        if _feature_false(feats.get("spa")):
            add("spa_claim", "contradiction",
                f"Description mentions '{spa_hit.group(1)}' but MLS spa features say none",
                dont_say="spa / hot tub",
                fallback="The listing copy mentions a spa but MLS features say none — verify on the walkthrough before it goes on camera.")
        elif feats.get("spa") is None:
            add("spa_claim", "confirm",
                f"'{spa_hit.group(1)}' appears only in the description — no structured backing",
                fallback="Confirm the spa exists on the walkthrough before naming it on camera.")

    # 2) Basement phantom: structured claims one, description never says the word.
    if _feature_true(feats.get("basement")) and not re.search(r"\bbasement\b", desc, re.I):
        add("basement_phantom", "risk",
            f"MLS lists basement '{feats['basement']}' but the description never mentions a basement",
            fallback="MLS shows a finished basement the listing copy never mentions — verify it exists and is usable before featuring it.")

    # 3) Bed/bath arithmetic: main + ADU must equal totals; description-stated
    #    counts must match SOME structured count (total, main, or ADU).
    if adu.get("present"):
        for unit, main_k, total_k in (("beds", "beds_main", "beds"), ("baths", "baths_main", "baths")):
            m, a, t = listing.get(main_k), adu.get(unit), listing.get(total_k)
            if None not in (m, a, t) and abs((m + a) - t) > 1e-9:
                add("bedbath_arithmetic", "contradiction",
                    f"{unit}: main {m} + ADU {a} = {m + a}, but total says {t}",
                    fallback=f"Recount the {unit} split before quoting any number on camera.")
    if desc:
        for label, rx, keys in (("bed", BED_COUNT_RE, ("beds", "beds_main")),
                                ("bath", BATH_COUNT_RE, ("baths", "baths_main"))):
            allowed = {float(listing[k]) for k in keys if listing.get(k) is not None}
            if adu.get(label + "s") is not None:
                allowed.add(float(adu[label + "s"]))
            if not allowed:
                continue  # nothing structured to check against — not a diff
            for m in rx.finditer(desc):
                if float(m.group(1)) not in allowed:
                    add("desc_count_mismatch", "contradiction",
                        f"Description says '{m.group(0)}' — matches no structured {label} count {sorted(allowed)}",
                        fallback=f"Description {label} count disagrees with MLS — recount before quoting on camera.")

    # 4) Remodel-gap ambush: big jump over last sale, or list far above Zestimate.
    price = listing.get("price")
    solds = [h for h in (listing.get("price_history") or [])
             if "sold" in str(h.get("event", "")).lower() and h.get("price")]
    last = max(solds, key=lambda h: str(h.get("date", ""))) if solds else None
    zest = listing.get("zestimate")
    if price:
        parts = []
        if last:
            pct = round((price - last["price"]) / last["price"] * 100, 1)
            if pct > 50:
                parts.append(f"list {_money(price)} is {pct:+}% over last sale "
                             f"{_money(last['price'])} ({last.get('date')})")
        if zest and price >= zest * 1.5:
            parts.append(f"list is {round(price / zest, 1)}x the Zestimate ({_money(zest)})")
        if parts:
            add("price_jump_ambush", "risk",
                "Remodel-gap ambush: " + "; ".join(parts),
                fallback="Frame the price around the full reimagining, never appreciation — buyers WILL pull the sale history.")

    # 5) Luxury-brand/material claims: description-only until walked through.
    seen = set()
    for rx in (BRAND_RE, MATERIAL_RE):
        for m in rx.finditer(desc):
            term = m.group(1)
            if term.lower() in seen:
                continue
            seen.add(term.lower())
            add("luxury_claim", "confirm",
                f"Description claims '{term}' with no structured backing",
                fallback=f"Confirm {term} on the walkthrough before naming it on camera.")
    return items


def print_diff_table(items: List[Dict[str, Any]]) -> None:
    if not items:
        print("CLEAN — no contradictions, risks, or confirm items.")
        return
    w_check = max(len(i["check"]) for i in items)
    for i in items:
        print(f"  {i['severity']:<13} {i['check']:<{w_check}}  {i['detail']}")
        if i.get("dont_say"):
            print(f"  {'':<13} {'':<{w_check}}  DON'T SAY: {i['dont_say']}")
        if i.get("fallback_line"):
            print(f"  {'':<13} {'':<{w_check}}  -> {i['fallback_line']}")


# ---------------------------------------------------------------- ledger ----
# Provenance rule (factual-grounding standard): structured MLS field =
# VERIFIED; description-only = LIKELY; derived arithmetic on verified inputs
# = VERIFIED(derived); anything needing outside data = UNCONFIRMED(external)
# placeholder for the research-receipt step to fill.

def build_ledger(listing: Dict[str, Any], diff_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    claims: List[Dict[str, Any]] = []
    feats = listing.get("features") or {}
    adu = listing.get("adu") or {}

    def fb(check: str) -> Optional[str]:
        for i in diff_items:
            if i["check"] == check:
                return i.get("fallback_line")
        return None

    def contra(check: str) -> bool:
        return any(i["check"] == check and i["severity"] == "contradiction" for i in diff_items)

    def add(claim: str, source: str, confidence: str,
            contradiction: bool = False, fallback: Optional[str] = None) -> None:
        claims.append({"claim": claim, "source": source, "confidence": confidence,
                       "contradiction": contradiction, "fallback_line": fallback})

    # --- VERIFIED: straight off structured fields (only when present) ---
    if listing.get("price"):
        add(f"Listed at {_money(listing['price'])}", "mls_field", "VERIFIED")
    if listing.get("beds") is not None and listing.get("baths") is not None:
        add(f"{listing['beds']} bed / {listing['baths']} bath total", "mls_field", "VERIFIED",
            contradiction=contra("bedbath_arithmetic") or contra("desc_count_mismatch"),
            fallback=fb("bedbath_arithmetic") or fb("desc_count_mismatch"))
    if adu.get("present"):
        kitchen = {True: "with kitchen", False: "no kitchen", None: "kitchen unconfirmed"}[adu.get("has_kitchen")]
        add(f"ADU: {adu.get('beds')} bd / {adu.get('baths')} ba, ~{adu.get('sqft')} sqft, {kitchen}",
            "mls_field", "VERIFIED")
        if listing.get("beds_main") is not None:
            add(f"Main house: {listing['beds_main']} bd / {listing['baths_main']} ba",
                "mls_field", "VERIFIED")
    simple = [("sqft", "{} sqft"), ("lot_acres", "{} acre lot"), ("year_built", "Built {}"),
              ("stories", "{} story"), ("property_type", "{}"), ("walk_score", "Walk Score {}"),
              ("mls", "MLS #{}")]
    for key, tpl in simple:
        if listing.get(key) is not None:
            add(tpl.format(listing[key]), "mls_field", "VERIFIED")
    feat_claims = [("pool", "Pool"), ("fireplace", "Fireplace"), ("central_air", "Central air"),
                   ("outdoor_kitchen", "Outdoor kitchen")]
    for key, label in feat_claims:
        if _feature_true(feats.get(key)):
            add(label, "mls_field", "VERIFIED")
    if _feature_false(feats.get("spa")):
        add("No spa (MLS: spa features none)", "mls_field", "VERIFIED",
            contradiction=contra("spa_claim"), fallback=fb("spa_claim"))
    if _feature_true(feats.get("basement")):
        add(f"Basement: {feats['basement']}", "mls_field", "VERIFIED",
            fallback=fb("basement_phantom"))
    if feats.get("garage_spaces"):
        add(f"{feats['garage_spaces']}-car garage", "mls_field", "VERIFIED")
    if feats.get("furnished") and str(feats["furnished"]).lower() not in ("no", "none"):
        add(f"Furnished: {feats['furnished']}", "mls_field", "VERIFIED")
    if listing.get("zestimate"):
        add(f"Zestimate {_money(listing['zestimate'])}", "mls_field", "VERIFIED")
    if (listing.get("tax") or {}).get("annual"):
        add(f"Annual tax {_money(listing['tax']['annual'])}", "mls_field", "VERIFIED")
    for s in listing.get("schools") or []:
        add(f"{s.get('name')} ({s.get('grades')}, rated {s.get('rating')}/10, {s.get('distance_mi')} mi)",
            "mls_field", "VERIFIED")
    for h in listing.get("price_history") or []:
        add(f"{h.get('event')} {h.get('date')} at {_money(h['price'])}" if h.get("price")
            else f"{h.get('event')} {h.get('date')}", "mls_field", "VERIFIED")
    for oh in listing.get("open_houses") or []:
        add(f"Open house {oh.get('date')} {oh.get('start')}-{oh.get('end')}", "mls_field", "VERIFIED")

    # --- LIKELY: lives only in the description (walkthrough confirms) ---
    desc = listing.get("description") or ""
    lux = {i["detail"].split("'")[1] for i in diff_items if i["check"] == "luxury_claim"}
    for term in sorted(lux):
        add(f"{term} (description claim)", "description", "LIKELY", fallback=fb("luxury_claim"))
    if re.search(r"\boutdoor kitchen\b", desc, re.I) and feats.get("outdoor_kitchen") is None:
        add("Outdoor kitchen (description claim)", "description", "LIKELY",
            fallback="Confirm the outdoor kitchen on the walkthrough.")
    if SPA_RE.search(desc) and not _feature_true(feats.get("spa")):
        add("Spa/hot tub (description claim)", "description", "LIKELY",
            contradiction=contra("spa_claim"), fallback=fb("spa_claim"))

    # --- derived arithmetic (verified inputs => verified output) ---
    if listing.get("price") and listing.get("sqft"):
        add(f"{_money(round(listing['price'] / listing['sqft']))}/sqft", "derived", "VERIFIED")
    if fb("price_jump_ambush"):
        detail = next(i["detail"] for i in diff_items if i["check"] == "price_jump_ambush")
        add(detail, "derived", "VERIFIED", fallback=fb("price_jump_ambush"))

    # --- external placeholders: the workflow fills these from receipts ---
    add("Price vs area median (needs market receipts)", "external", "UNCONFIRMED",
        fallback="Fill from research receipts before speaking to market position.")
    return claims

# ------------------------------------------------------------------- CLI ----


def _load_listing(slug: str, out_dir: Path) -> Optional[Dict[str, Any]]:
    path = out_dir / slug / "listing.json"
    if not path.exists():
        print(f"listing_intel: no listing at {path} — run parse first.", file=sys.stderr)
        return None
    return json.loads(path.read_text())


def cmd_parse(args) -> int:
    out_dir = Path(args.out_dir)
    paste = Path(args.paste) if args.paste else None
    dump = Path(args.dump_path) if args.dump_path else None
    src = paste or dump
    if src is None or not src.exists():
        print(f"listing_intel: input not found: {src}", file=sys.stderr)
        return 1
    listing = do_parse(dump, args.slug, out_dir, paste)
    filled = sum(1 for k in SCALAR_KEYS if listing.get(k) is not None)
    print(f"Parsed [{listing['source']}] -> {out_dir / args.slug / 'listing.json'}")
    print(f"  {filled}/{len(SCALAR_KEYS)} scalar fields resolved (unknown stays null, never guessed)")
    return 0


def cmd_diff(args) -> int:
    listing = _load_listing(args.slug, Path(args.out_dir))
    if listing is None:
        return 1
    items = diff_listing(listing)
    dest = Path(args.out_dir) / args.slug / "claims-diff.json"
    dest.write_text(json.dumps(items, indent=2) + "\n")
    n_c = sum(1 for i in items if i["severity"] == "contradiction")
    print(f"CLAIMS DIFF — {args.slug}: {n_c} contradiction(s), "
          f"{sum(1 for i in items if i['severity'] == 'risk')} risk(s), "
          f"{sum(1 for i in items if i['severity'] == 'confirm')} confirm item(s)")
    print_diff_table(items)
    print(f"-> {dest}")
    return 0


def cmd_ledger(args) -> int:
    listing = _load_listing(args.slug, Path(args.out_dir))
    if listing is None:
        return 1
    diff_path = Path(args.out_dir) / args.slug / "claims-diff.json"
    diff_items = json.loads(diff_path.read_text()) if diff_path.exists() else diff_listing(listing)
    claims = build_ledger(listing, diff_items)
    dest = Path(args.out_dir) / args.slug / "claims-ledger.json"
    dest.write_text(json.dumps(claims, indent=2) + "\n")
    by_conf: Dict[str, int] = {}
    for c in claims:
        by_conf[c["confidence"]] = by_conf.get(c["confidence"], 0) + 1
    print(f"CLAIMS LEDGER — {args.slug}: {len(claims)} claims "
          f"({', '.join(f'{v} {k}' for k, v in sorted(by_conf.items()))}), "
          f"{sum(1 for c in claims if c['contradiction'])} carrying contradictions")
    print(f"-> {dest}")
    return 0

# -------------------------------------------------------------- selftest ----


def cmd_selftest(_args) -> int:
    """End-to-end against the 5200-armida fixture (VERIFIED Zillow/CRMLS data
    pulled 2026-08-05). Exercises the exact failure modes this tool exists to
    catch — including one in-memory mutation to prove the spa check FIRES when
    it should, not just stays quiet when it shouldn't."""
    results: List[bool] = []

    def t(name: str, ok: bool) -> None:
        results.append(ok)
        print(f"{'PASS' if ok else 'FAIL'}  {name}")

    tmp = Path(tempfile.mkdtemp(prefix="listing_intel_selftest_"))
    listing = do_parse(FIXTURE, "5200-armida", tmp)
    items = diff_listing(listing)
    (tmp / "5200-armida" / "claims-diff.json").write_text(json.dumps(items, indent=2))
    ledger = build_ledger(listing, items)
    (tmp / "5200-armida" / "claims-ledger.json").write_text(json.dumps(ledger, indent=2))

    # 1) Basement phantom: structured "Finished", description silent.
    t("diff catches basement phantom (risk)",
      any(i["check"] == "basement_phantom" and i["severity"] == "risk" for i in items))

    # 2) Spa: fixture is CONSISTENT (spa false + description silent) — must not
    #    flag. Then mutate the description in memory and prove it WOULD flag.
    t("diff does NOT flag spa on the consistent fixture",
      not any(i["check"] == "spa_claim" for i in items))
    mutated = copy.deepcopy(listing)
    mutated["description"] += " Relax in the sparkling pool and spa."
    t("mutated description ('pool and spa') DOES trip spa contradiction",
      any(i["check"] == "spa_claim" and i["severity"] == "contradiction"
          for i in diff_listing(mutated)))

    # 3) Bed/bath arithmetic: 4+1=5 beds, 4.5+1=5.5 baths, desc counts all match.
    t("bed/bath arithmetic + description counts pass clean",
      not any(i["check"] in ("bedbath_arithmetic", "desc_count_mismatch") for i in items))

    # 4) Remodel-gap ambush: +132.7% over the 2024 sale AND 2.2x Zestimate.
    jump = [i for i in items if i["check"] == "price_jump_ambush"]
    t("price-jump ambush fires (+132.7% and Zestimate gap)",
      bool(jump) and "+132.7%" in jump[0]["detail"] and "Zestimate" in jump[0]["detail"])

    # 5) Luxury claims -> confirm-on-walkthrough items.
    lux = [i["detail"].lower() for i in items if i["check"] == "luxury_claim"]
    t("Thermador + porcelain produce confirm items",
      any("thermador" in d for d in lux) and any("porcelain" in d for d in lux))

    # 6) Ledger provenance: description-only claims land as LIKELY.
    t("ledger marks description-only claims LIKELY",
      any(c["source"] == "description" and c["confidence"] == "LIKELY" for c in ledger))

    n_fail = results.count(False)
    print(f"\nselftest: {results.count(True)}/{len(results)} passed"
          + (f" — {n_fail} FAILED" if n_fail else "") + f"  (artifacts: {tmp})")
    return 1 if n_fail else 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Listing intake parser + claims contradiction scanner (stdlib only)")
    sub = parser.add_subparsers(dest="command", required=True)

    pp = sub.add_parser("parse", help="Ingest a page dump / listing JSON / pasted text")
    pp.add_argument("dump_path", nargs="?", help="Saved HTML dump or hand-assembled listing .json")
    pp.add_argument("--slug", required=True, help="Listing slug (output folder name)")
    pp.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    pp.add_argument("--paste", default="", help="Plain-text listing description (regex-only extraction)")
    pp.set_defaults(func=cmd_parse)

    pd = sub.add_parser("diff", help="Structured facts vs description — contradictions/risks")
    pd.add_argument("--slug", required=True)
    pd.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    pd.set_defaults(func=cmd_diff)

    pl = sub.add_parser("ledger", help="Every on-camera claim with provenance + confidence")
    pl.add_argument("--slug", required=True)
    pl.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    pl.set_defaults(func=cmd_ledger)

    pt = sub.add_parser("selftest", help="Run parse+diff+ledger against the bundled fixture")
    pt.set_defaults(func=cmd_selftest)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
