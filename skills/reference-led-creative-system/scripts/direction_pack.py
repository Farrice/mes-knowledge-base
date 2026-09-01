#!/usr/bin/env python3
"""Capture remote/local direction previews into a verified local choice pack."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import re
import ssl
import sys
import textwrap
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "Pillow is required but unavailable. Do not install automatically; "
        "use the workspace dependency gate."
    ) from exc


MIN_WIDTH = 400
MIN_HEIGHT = 250
CONTACT_SHEET = "direction-contact-sheet.png"
RECEIPT = "receipt.json"
SYSTEM_CA_CANDIDATES = (
    Path("/etc/ssl/cert.pem"),
    Path("/private/etc/ssl/cert.pem"),
)


class PackError(RuntimeError):
    """Raised when a direction pack cannot be made visibly trustworthy."""


def _https_context() -> ssl.SSLContext:
    """Use Python's configured CA store, then macOS's system bundle if needed."""
    default_paths = ssl.get_default_verify_paths()
    configured = Path(default_paths.cafile) if default_paths.cafile else None
    if configured and configured.is_file():
        return ssl.create_default_context()
    for candidate in SYSTEM_CA_CANDIDATES:
        if candidate.is_file():
            return ssl.create_default_context(cafile=str(candidate))
    return ssl.create_default_context()


def _read_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PackError(f"Cannot read manifest {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise PackError("Manifest root must be a JSON object.")
    return payload


def _slug(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return cleaned or "direction"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
        if bold
        else "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def _directions(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    directions = manifest.get("directions")
    if not isinstance(directions, list) or len(directions) < 2:
        raise PackError("Manifest requires at least two directions.")
    seen_ids: set[str] = set()
    seen_names: set[str] = set()
    for index, direction in enumerate(directions, start=1):
        if not isinstance(direction, dict):
            raise PackError(f"Direction {index} must be an object.")
        direction_id = str(direction.get("id", "")).strip()
        name = str(direction.get("name", "")).strip()
        primary = direction.get("primary_reference")
        if not direction_id or not name:
            raise PackError(f"Direction {index} requires id and name.")
        if direction_id in seen_ids or name.lower() in seen_names:
            raise PackError(f"Duplicate direction id or name: {direction_id} / {name}")
        if not isinstance(primary, dict) or not str(primary.get("title", "")).strip():
            raise PackError(f"Direction {direction_id} requires primary_reference.title.")
        if not direction.get("preview_path") and not primary.get("preview_url"):
            raise PackError(
                f"Direction {direction_id} needs preview_path or primary_reference.preview_url."
            )
        seen_ids.add(direction_id)
        seen_names.add(name.lower())
    return directions


def _source_bytes(
    direction: dict[str, Any], manifest_dir: Path, allow_network: bool
) -> tuple[bytes, str]:
    preview_path = direction.get("preview_path")
    if preview_path:
        source = Path(str(preview_path))
        if not source.is_absolute():
            source = manifest_dir / source
        try:
            return source.read_bytes(), str(source.resolve())
        except OSError as exc:
            raise PackError(f"Cannot read local preview {source}: {exc}") from exc

    url = str(direction["primary_reference"].get("preview_url", "")).strip()
    if not allow_network:
        raise PackError(
            f"Direction {direction['id']} is remote-only and network capture is disabled."
        )
    if not url.startswith("https://"):
        raise PackError(f"Preview URL must use HTTPS: {url}")
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "ReferenceLedCreativeSystem/1.0"},
    )
    try:
        with urllib.request.urlopen(
            request, timeout=30, context=_https_context()
        ) as response:
            return response.read(), url
    except Exception as exc:  # urllib exposes several transport exceptions
        raise PackError(f"Preview capture failed for {url}: {exc}") from exc


def _normalize_image(data: bytes, destination: Path) -> tuple[int, int, str]:
    try:
        with Image.open(io.BytesIO(data)) as image:
            image.load()
            width, height = image.size
            source_format = image.format or "unknown"
            if width < MIN_WIDTH or height < MIN_HEIGHT:
                raise PackError(
                    f"Preview is too small: {width}x{height}; minimum is "
                    f"{MIN_WIDTH}x{MIN_HEIGHT}."
                )
            ImageOps.exif_transpose(image).convert("RGB").save(
                destination, format="JPEG", quality=92, optimize=True
            )
            return width, height, source_format
    except PackError:
        raise
    except Exception as exc:
        raise PackError(f"Unreadable image content: {exc}") from exc


def _contact_sheet(
    manifest: dict[str, Any], output_dir: Path, records: list[dict[str, Any]]
) -> Path:
    columns = min(3, len(records))
    rows = math.ceil(len(records) / columns)
    gap = 30
    card_width = 440
    image_height = 275
    label_height = 125
    header_height = 86
    card_height = image_height + label_height
    width = columns * card_width + (columns + 1) * gap
    height = header_height + rows * card_height + (rows + 1) * gap

    canvas = Image.new("RGB", (width, height), "#f1f1ed")
    draw = ImageDraw.Draw(canvas)
    title_font = _font(32, bold=True)
    name_font = _font(21, bold=True)
    detail_font = _font(15)
    status_font = _font(12, bold=True)

    title = str(manifest.get("title") or "Visual direction choice pack")
    draw.text((gap, 24), title, fill="#111111", font=title_font)

    for index, record in enumerate(records):
        row, column = divmod(index, columns)
        x = gap + column * (card_width + gap)
        y = header_height + gap + row * (card_height + gap)
        draw.rectangle(
            [x, y, x + card_width, y + card_height],
            fill="#ffffff",
            outline="#cfcfca",
            width=1,
        )
        with Image.open(record["local_path"]) as source:
            fitted = ImageOps.fit(
                ImageOps.exif_transpose(source).convert("RGB"),
                (card_width, image_height),
                method=Image.Resampling.LANCZOS,
            )
        canvas.paste(fitted, (x, y))
        label_y = y + image_height + 14
        draw.text(
            (x + 16, label_y),
            f"{record['id']} · {record['name']}",
            fill="#111111",
            font=name_font,
        )
        primary = f"Primary: {record['primary_title']}"
        for line_number, line in enumerate(textwrap.wrap(primary, width=48)[:2]):
            draw.text(
                (x + 16, label_y + 32 + line_number * 19),
                line,
                fill="#555555",
                font=detail_font,
            )
        draw.text(
            (x + 16, y + card_height - 26),
            "LOCAL PREVIEW · VERIFIED",
            fill="#111111",
            font=status_font,
        )

    destination = output_dir / CONTACT_SHEET
    canvas.save(destination, format="PNG", optimize=True)
    return destination


def capture(manifest_path: Path, output_dir: Path, allow_network: bool) -> dict[str, Any]:
    manifest = _read_json(manifest_path)
    directions = _directions(manifest)
    output_dir.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, Any]] = []

    for direction in directions:
        destination = output_dir / (
            f"direction-{_slug(str(direction['id']))}-{_slug(str(direction['name']))}.jpg"
        )
        data, source = _source_bytes(direction, manifest_path.parent, allow_network)
        width, height, source_format = _normalize_image(data, destination)
        primary = direction["primary_reference"]
        records.append(
            {
                "id": str(direction["id"]),
                "name": str(direction["name"]),
                "primary_title": str(primary["title"]),
                "reference_uuid": str(primary.get("uuid", "")),
                "source": source,
                "local_path": str(destination.resolve()),
                "width": width,
                "height": height,
                "source_format": source_format,
                "output_format": "JPEG",
                "bytes": destination.stat().st_size,
                "sha256": _sha256(destination),
                "status": "VISIBLE",
            }
        )

    contact_sheet = _contact_sheet(manifest, output_dir, records)
    receipt = {
        "schema_version": 1,
        "run_id": str(manifest.get("run_id") or output_dir.name),
        "title": str(manifest.get("title") or "Visual direction choice pack"),
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "manifest": str(manifest_path.resolve()),
        "status": "PASS",
        "direction_count": len(records),
        "directions": records,
        "contact_sheet": {
            "local_path": str(contact_sheet.resolve()),
            "bytes": contact_sheet.stat().st_size,
            "sha256": _sha256(contact_sheet),
        },
        "choice_gate": "VISIBLE · UNCHOSEN",
    }
    (output_dir / RECEIPT).write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return receipt


def verify(manifest_path: Path, output_dir: Path) -> dict[str, Any]:
    manifest = _read_json(manifest_path)
    expected = _directions(manifest)
    receipt_path = output_dir / RECEIPT
    receipt = _read_json(receipt_path)
    errors: list[str] = []
    records = receipt.get("directions")
    if not isinstance(records, list) or len(records) != len(expected):
        errors.append("Receipt direction count does not match the manifest.")
        records = []

    for record in records:
        path = Path(str(record.get("local_path", "")))
        if not path.is_file():
            errors.append(f"Missing local preview: {path}")
            continue
        if _sha256(path) != record.get("sha256"):
            errors.append(f"Checksum mismatch: {path}")
        try:
            with Image.open(path) as image:
                image.verify()
            with Image.open(path) as image:
                width, height = image.size
            if width < MIN_WIDTH or height < MIN_HEIGHT:
                errors.append(f"Preview below minimum dimensions: {path}")
        except Exception as exc:
            errors.append(f"Unreadable local preview {path}: {exc}")

    contact = Path(str(receipt.get("contact_sheet", {}).get("local_path", "")))
    if not contact.is_file():
        errors.append(f"Missing contact sheet: {contact}")
    else:
        try:
            with Image.open(contact) as image:
                image.verify()
        except Exception as exc:
            errors.append(f"Unreadable contact sheet {contact}: {exc}")
        if _sha256(contact) != receipt.get("contact_sheet", {}).get("sha256"):
            errors.append(f"Contact-sheet checksum mismatch: {contact}")

    if errors:
        raise PackError("Verification failed:\n- " + "\n- ".join(errors))
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build and verify locally visible visual-direction choice packs."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("capture", "verify"):
        subparser = subparsers.add_parser(command)
        subparser.add_argument("--manifest", required=True, type=Path)
        subparser.add_argument("--output-dir", required=True, type=Path)
        if command == "capture":
            subparser.add_argument(
                "--no-network",
                action="store_true",
                help="Refuse remote previews; useful for deterministic tests.",
            )

    args = parser.parse_args()
    try:
        if args.command == "capture":
            receipt = capture(args.manifest, args.output_dir, not args.no_network)
            verify(args.manifest, args.output_dir)
        else:
            receipt = verify(args.manifest, args.output_dir)
    except PackError as exc:
        print(f"FAIL — {exc}", file=sys.stderr)
        return 1

    print(
        f"PASS — {receipt['direction_count']} local previews + contact sheet verified\n"
        f"Contact sheet: {receipt['contact_sheet']['local_path']}\n"
        f"Receipt: {(args.output_dir / RECEIPT).resolve()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
