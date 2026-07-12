#!/usr/bin/env python3
"""Validiert das Ruckpacken-Projekt für nhmkdev/cardmaker."""

from __future__ import annotations

import csv
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


SIZE_RANGES = {
    151: (143, 159),
    175: (166, 184),
    211: (200, 222),
}


def validate(folder: Path) -> None:
    root = ET.parse(folder / "ruckpacken.cmp").getroot()
    layout = root.find("Layout")
    if layout is None:
        raise RuntimeError("CardMaker-Layout fehlt.")
    if layout.get("width") != "673" or layout.get("height") != "1039":
        raise RuntimeError("Erwartetes Kartenformat: 673 × 1039 px.")
    elements = layout.findall("Element")
    if len(elements) != 9 or any(e.get("type") != "Graphic" for e in elements):
        raise RuntimeError("Erwartet werden neun Graphic-Elemente.")
    reference = layout.find("Reference")
    if reference is None or reference.get("RelativePath") != "cards.csv":
        raise RuntimeError("Reference auf cards.csv fehlt.")
    for slot, element in enumerate(elements, 1):
        base_size = int(element.get("width", "0"))
        if base_size != int(element.get("height", "0")) or base_size not in SIZE_RANGES:
            raise RuntimeError(f"Unerwartete Grundgröße bei Symbol {slot}.")
        minimum, maximum = SIZE_RANGES[base_size]
        expected = (
            f"@[slot_{slot:02}]"
            "$[rotation:#random;-20;20#]"
            f"$[width:#random;{minimum};{maximum}#]"
            f"$[height:#random;{minimum};{maximum}#]"
        )
        if element.get("variable") != expected:
            raise RuntimeError(f"Falsche Laufzeittransformation bei Symbol {slot}.")
        if element.get("rotation") != "0":
            raise RuntimeError(f"Drehung bei Symbol {slot} ist noch hart codiert.")

    with (folder / "cards.csv").open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        expected_fields = ["Count", "card_id"] + [
            f"slot_{slot:02}" for slot in range(1, 10)
        ]
        if reader.fieldnames != expected_fields:
            raise RuntimeError(f"CSV-Spalten sind nicht sauber: {reader.fieldnames}")
        cards = list(reader)
    if len(cards) != 73:
        raise RuntimeError(f"Erwartet: 73 Karten; gefunden: {len(cards)}")

    missing = []
    for card in cards:
        for slot in range(1, 10):
            prefix = f"slot_{slot:02}"
            image = folder / card[prefix]
            if not image.is_file():
                missing.append(str(image))
    if missing:
        raise RuntimeError("Fehlende Bilder:\n" + "\n".join(missing))
    print("CM-Projekt: 57 × 88 mm, 73 Karten, 9 Grafiken, Laufzeitzufall, saubere CSV, 0 fehlende Bilder")


if __name__ == "__main__":
    validate(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent)
