#!/usr/bin/env python3
"""Validiert Struktur, Konfiguration und Kombinatorik des Lautspiele-Projekts."""

from __future__ import annotations

import csv
import importlib.util
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def fail(message: str) -> None:
    raise AssertionError(message)


def load_builder():
    path = ROOT / "build_lautspiele_project.py"
    spec = importlib.util.spec_from_file_location("lautspiele_builder", path)
    if spec is None or spec.loader is None:
        fail("Builder konnte nicht geladen werden.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate() -> None:
    project = ROOT / "lautspiele.cmp"
    config_paths = {
        "default": ROOT / "symbols_default.csv",
        "k": ROOT / "symbols_k.csv",
    }
    empty_defines = ROOT / "lautspiele_defines.csv"
    for path in (project, empty_defines, *config_paths.values()):
        if not path.is_file():
            fail(f"Datei fehlt: {path.name}")

    required_fields = {
        "symbol_set", "symbol_folder", "symbol_names", "symbol_scale_map",
        "gruselino_start", "gruselino_end", "gruselino_shift",
        "domino_start", "domino_end", "domino_shift",
        "dobble_start", "dobble_end", "dobble_shift",
    }
    for set_name, config in config_paths.items():
        with config.open(encoding="utf-8-sig", newline="") as handle:
            config_rows = list(csv.DictReader(handle))
        if len(config_rows) != 1:
            fail(f"{config.name} muss genau eine CardMaker-Datenzeile enthalten.")
        row = config_rows[0]
        if not required_fields.issubset(row):
            fail(f"{config.name} enthält nicht alle Konfigurationsfelder.")
        expected_folder = f"images/symbols/{set_name}"
        if row["symbol_set"] != set_name or row["symbol_folder"] != expected_folder:
            fail(f"{config.name} ist nicht dem Bildsatz {set_name} zugeordnet.")
        names = row["symbol_names"].split("|")
        scales = row["symbol_scale_map"].split("|")
        if len(names) != len(scales) or len(scales) < 1:
            fail(f"Namen und Skalierungen sind in {config.name} nicht deckungsgleich.")
        if any(float(value) <= 0 for value in scales):
            fail(f"{config.name} enthält eine ungültige Größenkorrektur.")
        for mode in ("gruselino", "domino", "dobble"):
            start = int(row[f"{mode}_start"])
            end = int(row[f"{mode}_end"])
            int(row[f"{mode}_shift"])
            if not 1 <= start <= end <= len(scales):
                fail(f"Ungültige Start-/Endspanne für {mode} in {config.name}.")

    with empty_defines.open(encoding="utf-8-sig", newline="") as handle:
        define_lines = list(csv.reader(handle))
    if define_lines != [["define", "value"]]:
        fail("Die technische Projekt-Defines-Datei muss leer bleiben.")

    root = ET.parse(project).getroot()
    if root.findtext("translatorName") != "JavaScript":
        fail("Das Projekt muss den JavaScript-Translator verwenden.")
    layouts = {layout.get("Name"): layout for layout in root.findall("Layout")}
    expected_layouts = {"Gruselino Karten", "Gruselino Papier", "Domino Papier", "Dobble Papier"}
    if set(layouts) != expected_layouts:
        fail("Die vier erwarteten Layouts fehlen oder wurden umbenannt.")
    expected_refs = {
        "Gruselino Karten": "symbols_k.csv",
        "Gruselino Papier": "symbols_k.csv",
        "Domino Papier": "symbols_k.csv",
        "Dobble Papier": "symbols_k.csv",
    }
    expected_counts = {
        "Gruselino Karten": "11", "Gruselino Papier": "11",
        "Domino Papier": "10", "Dobble Papier": "7",
    }
    for name, layout in layouts.items():
        refs = layout.findall("Reference")
        if len(refs) != 1 or refs[0].get("RelativePath") != expected_refs[name]:
            fail(f"{name} verwendet nicht die erwartete Symbol-CSV.")
        if layout.get("defaultCount") != expected_counts[name]:
            fail(f"{name} hat eine unerwartete Kartenanzahl.")
        for element in layout.findall("Element"):
            code = element.get("variable", "")
            if "symbol_01__scale" in code or "symbol_scale_map" not in code and element.get("type") == "Graphic" and "Symbol" in (element.get("name") or ""):
                fail(f"{name} enthält alte globale Größen-Defines.")

    for name in ("Gruselino Karten", "Gruselino Papier"):
        symbols = [e for e in layouts[name].findall("Element") if (e.get("name") or "").startswith("Symbol ")]
        if len(symbols) != 10:
            fail(f"{name} muss zehn Symbolpositionen besitzen.")
        for element in symbols:
            code = element.get("variable", "")
            if "cardIndex>1" not in code or "Math.random()*360" not in code:
                fail(f"Ausblendung/Rotation fehlt in {name}.")

    domino = [e for e in layouts["Domino Papier"].findall("Element") if (e.get("name") or "").startswith("Domino Symbol")]
    if len(domino) != 2:
        fail("Domino benoetigt zwei Symbolfelder.")
    for element in domino:
        code = element.get("variable", "")
        if "Math.random()*360" not in code or "0.95+Math.random" in code:
            fail("Domino muss das ganze Element drehen, aber nicht zufaellig skalieren.")

    dobble = [e for e in layouts["Dobble Papier"].findall("Element") if (e.get("name") or "").startswith("Dobble Symbol")]
    if len(dobble) != 3:
        fail("Dobble benoetigt drei Symbolfelder.")

    builder = load_builder()
    cards = [set(card) for card in builder.DOBBLE]
    if len(cards) != 7 or any(len(card) != 3 for card in cards):
        fail("Dobble-Matrix hat nicht 7 Karten mit je 3 Symbolen.")
    if any(len(cards[a] & cards[b]) != 1 for a in range(7) for b in range(a + 1, 7)):
        fail("Dobble-Matrix ist nicht perfekt.")

    for set_name in ("default", "k"):
        symbol_folder = ROOT / "images" / "symbols" / set_name
        symbol_config = ROOT / f"symbols_{set_name}.csv"
        if not symbol_config.is_file():
            fail(f"Symboltabelle fuer {set_name} fehlt.")
        for index in range(1, 11):
            if not (symbol_folder / f"{index:02}.png").is_file():
                fail(f"Bild {set_name}/{index:02}.png fehlt.")

    print("OK: Lautspiele-CardMaker-Projekt ist konsistent.")
    print("Layouts: 4 | Symbol-CSVs: 2 | globale Definitionen: 0")
    print("Symbolordner: default, k | CSV-Auswahl wechselt den Bildsatz")
    print("Gruselino: 11 Karten je Layout | Domino: 10 | Dobble: 7 perfekt")


if __name__ == "__main__":
    validate()
