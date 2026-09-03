#!/usr/bin/env python3
"""Reduziert eine 73-Karten-Matrix auf die schlanke CardMaker-CSV."""

from __future__ import annotations

import csv
import io
import re
import sys
from pathlib import Path


def active_image_path(value: str) -> str:
    filename = value.replace("\\", "/").rsplit("/", 1)[-1]
    match = re.fullmatch(r"sym_(\d+)\.png", filename, re.IGNORECASE)
    if not match or not 1 <= int(match[1]) <= 73:
        raise RuntimeError(f"Unbekannte Symbolreferenz: {value}")
    return f"assets/images/sym_{int(match[1])}.png"


def csv_bytes(rows: list[dict], fields: list[str]) -> bytes:
    handle = io.StringIO(newline="")
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
    return handle.getvalue().encode("utf-8-sig")


def render(source: Path) -> bytes:
    with source.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 73:
        raise RuntimeError(f"Erwartet: 73 Karten; gefunden: {len(rows)}")

    output = []
    for row in rows:
        converted = {"Count": row.get("Count") or 1, "card_id": row["card_id"]}
        for slot in range(1, 10):
            prefix = f"slot_{slot:02}"
            source_value = row.get(f"{prefix}_file") or row.get(prefix)
            if not source_value:
                raise RuntimeError(f"Fehlende Bildspalte: {prefix}")
            converted[prefix] = active_image_path(source_value)
        output.append(converted)

    return csv_bytes(output, list(output[0]))


def build(source: Path, target: Path) -> None:
    content = render(source)
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.is_file() or target.read_bytes() != content:
        target.write_bytes(content)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Aufruf: python build_cm_data.py <quelle.csv> <cards.csv>")
    build(Path(sys.argv[1]), Path(sys.argv[2]))
