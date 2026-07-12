#!/usr/bin/env python3
"""Validiert das Ruckpacken-Projekt für nhmkdev/cardmaker."""

from __future__ import annotations

import csv
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def validate(folder: Path) -> None:
    root = ET.parse(folder / "ruckpacken.cmp").getroot()
    layout = root.find("Layout")
    if layout is None:
        raise RuntimeError("CardMaker-Layout fehlt.")
    elements = layout.findall("Element")
    if len(elements) != 9 or any(e.get("type") != "Graphic" for e in elements):
        raise RuntimeError("Erwartet werden neun Graphic-Elemente.")
    reference = layout.find("Reference")
    if reference is None or reference.get("RelativePath") != "cards.csv":
        raise RuntimeError("Reference auf cards.csv fehlt.")

    with (folder / "cards.csv").open(encoding="utf-8-sig", newline="") as handle:
        cards = list(csv.DictReader(handle))
    if len(cards) != 73:
        raise RuntimeError(f"Erwartet: 73 Karten; gefunden: {len(cards)}")

    missing = []
    for card in cards:
        for slot in range(1, 10):
            prefix = f"slot_{slot:02}"
            image = folder / card[f"{prefix}_file"]
            if not image.is_file():
                missing.append(str(image))
            for setting in ("rotation", "width", "height"):
                column = f"override:Symbol {slot}:{setting}"
                if not card.get(column):
                    raise RuntimeError(f"Leerer Override: {column}")
    if missing:
        raise RuntimeError("Fehlende Bilder:\n" + "\n".join(missing))
    print("CM-Projekt: 1 Layout, 73 Karten, 9 Grafiken je Karte, 0 fehlende Bilder")


if __name__ == "__main__":
    validate(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent)
