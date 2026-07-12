#!/usr/bin/env python3
"""Reduziert eine 73-Karten-Matrix auf die schlanke CardMaker-CSV."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

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
            source_value = row.get(f"{prefix}_file") or row.get(prefix)
            if not source_value:
                raise RuntimeError(f"Fehlende Bildspalte: {prefix}")
            filename = Path(source_value).name
            converted[prefix] = f"assets/images/arasaac/color/{filename}"
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
