#!/usr/bin/env python3
"""Validiert das Ruckpacken-Projekt für nhmkdev/cardmaker und MPC Jumbo."""

from __future__ import annotations

import csv
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from configure_runtime_transforms import (
    CUT_HEIGHT,
    CUT_INSET,
    CUT_WIDTH,
    FULL_BLEED_HEIGHT,
    FULL_BLEED_WIDTH,
    ORIGINAL_HEIGHT,
    ORIGINAL_SPECS,
    ORIGINAL_WIDTH,
    SAFE_HEIGHT,
    SAFE_INSET,
    SAFE_WIDTH,
    runtime_variable,
)


def validate(folder: Path) -> None:
    root = ET.parse(folder / "ruckpacken.cmp").getroot()
    layout = root.find("Layout")
    if layout is None:
        raise RuntimeError("CardMaker-Layout fehlt.")
    if layout.get("width") != str(FULL_BLEED_WIDTH) or layout.get("height") != str(FULL_BLEED_HEIGHT):
        raise RuntimeError(f"Erwartetes Vollbeschnittformat: {FULL_BLEED_WIDTH} × {FULL_BLEED_HEIGHT} px.")
    if layout.get("dpi") != "300":
        raise RuntimeError("Erwartet werden 300 dpi.")

    elements = layout.findall("Element")
    graphics = [element for element in elements if element.get("type") == "Graphic"]
    if len(graphics) != 9:
        raise RuntimeError("Erwartet werden neun Graphic-Elemente.")
    by_name = {element.get("name"): element for element in graphics}

    scale_x = CUT_WIDTH / ORIGINAL_WIDTH
    scale_y = CUT_HEIGHT / ORIGINAL_HEIGHT
    symbol_scale = min(scale_x, scale_y)
    old_center_x = ORIGINAL_WIDTH / 2
    old_center_y = ORIGINAL_HEIGHT / 2
    new_center_x = FULL_BLEED_WIDTH / 2
    new_center_y = FULL_BLEED_HEIGHT / 2
    for slot in range(1, 10):
        element = by_name.get(f"Symbol {slot}")
        if element is None:
            raise RuntimeError(f"Symbol {slot} fehlt.")
        old_x, old_y, old_size = ORIGINAL_SPECS[slot]
        x = round(new_center_x + (old_x - old_center_x) * scale_x)
        y = round(new_center_y + (old_y - old_center_y) * scale_y)
        base_size = round(old_size * symbol_scale)
        expected = runtime_variable(slot, x, y, base_size)
        top_left_x = round(x - base_size / 2)
        top_left_y = round(y - base_size / 2)
        actual = (int(element.get("x", "-1")), int(element.get("y", "-1")), int(element.get("width", "-1")))
        if actual != (top_left_x, top_left_y, base_size) or element.get("height") != str(base_size):
            raise RuntimeError(f"Falsche skalierte Geometrie bei Symbol {slot}: {actual}.")
        if element.get("variable") != expected:
            raise RuntimeError(f"Falsche Laufzeittransformation bei Symbol {slot}.")
        if element.get("rotation") != "0" or element.get("centerimageonorigin") != "false":
            raise RuntimeError(f"Falscher Ursprung oder hart codierte Drehung bei Symbol {slot}.")

    translator = root.findtext("translatorName")
    if translator != "JavaScript":
        raise RuntimeError(f"Erwarteter Übersetzer: JavaScript; gefunden: {translator}.")

    helpers = {element.get("name"): element for element in elements if element.get("type") == "Text"}
    expected_helpers = {
        "White Background": (0, 0, FULL_BLEED_WIDTH, FULL_BLEED_HEIGHT),
        "Cut Area (editor only)": (CUT_INSET, CUT_INSET, CUT_WIDTH, CUT_HEIGHT),
        "Safe Area (editor only)": (SAFE_INSET, SAFE_INSET, SAFE_WIDTH, SAFE_HEIGHT),
    }
    if set(helpers) != set(expected_helpers):
        raise RuntimeError(f"Falsche Hilfselemente: {sorted(helpers)}")
    element_names = [element.get("name") for element in elements]
    if element_names[:2] != ["Safe Area (editor only)", "Cut Area (editor only)"] or element_names[-1] != "White Background":
        raise RuntimeError("Falsche Zeichenreihenfolge: Guides müssen oben und der Hintergrund unten liegen.")
    for name, geometry in expected_helpers.items():
        element = helpers[name]
        actual = tuple(int(element.get(field, "-1")) for field in ("x", "y", "width", "height"))
        if actual != geometry:
            raise RuntimeError(f"Falsche Geometrie für {name}: {actual}")
    if helpers["White Background"].get("backgroundcolor") != "0xFFFFFFFF":
        raise RuntimeError("Weißer Hintergrund fehlt.")
    for name in ("Cut Area (editor only)", "Safe Area (editor only)"):
        element = helpers[name]
        if element.get("bordercolor") != "0xFF0000FF" or element.get("backgroundcolor") != "0x00000000":
            raise RuntimeError(f"{name} ist nicht rot und ungefüllt.")
        if "AddOverrideField('enabled', 'false')" not in element.get("variable", ""):
            raise RuntimeError(f"{name} würde mit exportiert.")

    reference = layout.find("Reference")
    if reference is None or reference.get("RelativePath") != "cards.csv":
        raise RuntimeError("Reference auf cards.csv fehlt.")
    with (folder / "cards.csv").open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        expected_fields = ["Count", "card_id"] + [f"slot_{slot:02}" for slot in range(1, 10)]
        if reader.fieldnames != expected_fields:
            raise RuntimeError(f"CSV-Spalten sind nicht sauber: {reader.fieldnames}")
        cards = list(reader)
    if len(cards) != 73:
        raise RuntimeError(f"Erwartet: 73 Karten; gefunden: {len(cards)}")

    missing = []
    image_references = []
    for card in cards:
        for slot in range(1, 10):
            image = folder / card[f"slot_{slot:02}"]
            image_references.append(card[f"slot_{slot:02}"])
            if not image.is_file():
                missing.append(str(image))
    if missing:
        raise RuntimeError("Fehlende Bilder:\n" + "\n".join(missing))
    if len(set(image_references)) != 73:
        raise RuntimeError(f"Erwartet: 73 eindeutige Bildassets; gefunden: {len(set(image_references))}")
    print("CM-Projekt: MPC Jumbo 1120 × 1570 px, 300 dpi, 73 Karten, 9 zentrierte Layout-Bildplätze, 73 eindeutige Bildassets, Guides und JavaScript-Laufzeitzufall valide")


if __name__ == "__main__":
    validate(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent)
