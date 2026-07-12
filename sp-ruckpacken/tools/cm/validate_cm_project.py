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
    if layout.get("width") != "673" or layout.get("height") != "1039":
        raise RuntimeError("Erwartetes Kartenformat: 673 × 1039 px.")
    elements = layout.findall("Element")
    if len(elements) != 9 or any(e.get("type") != "Graphic" for e in elements):
        raise RuntimeError("Erwartet werden neun Graphic-Elemente.")
    reference = layout.find("Reference")
    if reference is None or reference.get("RelativePath") != "cards.csv":
        raise RuntimeError("Reference auf cards.csv fehlt.")
    for slot, element in enumerate(elements, 1):
        if element.get("variable") != f"@[slot_{slot:02}]":
            raise RuntimeError(f"Falsche Bildvariable bei Symbol {slot}.")
        if abs(int(element.get("rotation", "0"))) > 20:
            raise RuntimeError(f"Zu starke Drehung bei Symbol {slot}.")

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
    print("CM-Projekt: 57 × 88 mm, 73 Karten, 9 Grafiken, saubere CSV, 0 fehlende Bilder")


if __name__ == "__main__":
    validate(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent)
