#!/usr/bin/env python3
"""Konvertiert die bestehende 73-Karten-Matrix in eine CardMaker-CSV."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

PX_PER_CM = 750 / 6.3


def build(source: Path, target: Path) -> None:
    with source.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 73:
        raise RuntimeError(f"Erwartet: 73 Karten; gefunden: {len(rows)}")

    output = []
    for row in rows:
        converted = {"Count": 1, "card_id": row["card_id"]}
        for slot in range(1, 10):
            prefix = f"slot_{slot:02}"
            element = f"Symbol {slot}"
            filename = Path(row[f"{prefix}_file"]).name
            size_px = round(float(row[f"{prefix}_size"]) * PX_PER_CM)
            converted[f"{prefix}_id"] = row[f"{prefix}_id"]
            converted[f"{prefix}_name"] = row[f"{prefix}_name"]
            converted[f"{prefix}_file"] = (
                f"assets/images/arasaac/color/{filename}"
            )
            converted[f"override:{element}:rotation"] = row[f"{prefix}_rot"]
            converted[f"override:{element}:width"] = size_px
            converted[f"override:{element}:height"] = size_px
        output.append(converted)

    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=output[0].keys())
        writer.writeheader()
        writer.writerows(output)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Aufruf: python build_cm_data.py <quelle.csv> <cards.csv>")
    build(Path(sys.argv[1]), Path(sys.argv[2]))
