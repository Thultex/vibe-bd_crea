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
    config = ROOT / "lautspiele.csv"
    defines = ROOT / "lautspiele_defines.csv"
    for path in (project, config, defines):
        if not path.is_file():
            fail(f"Datei fehlt: {path.name}")

    with config.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 3:
        fail("Die gemeinsame Konfiguration muss genau drei Moduszeilen enthalten.")
    expected = {"gruselino": 11, "domino": 10, "dobble": 7}
    for row in rows:
        mode = row["mode"]
        if mode not in expected or int(row["Count"]) != expected[mode]:
            fail(f"Unerwartete Kartenanzahl fuer {mode}.")
        if not row["symbol_folder"]:
            fail(f"Symbolordner fehlt fuer {mode}.")
        if mode == "domino":
            ring = int(row["symbol_end"]) - int(row["symbol_start"]) + 1
            if int(row["Count"]) != ring:
                fail("Domino Count muss der inklusiven Start-/Endspanne entsprechen.")

    with defines.open(encoding="utf-8-sig", newline="") as handle:
        define_rows = list(csv.DictReader(handle))
    if len(define_rows) != 50:
        fail("Es werden 50 erweiterbare Symboldefinitionen erwartet.")
    for index, row in enumerate(define_rows, start=1):
        if row["define"] != f"symbol_{index:02}" or not row["name"]:
            fail(f"Ungueltige Symboldefinition in Zeile {index}.")
        if float(row["scale"]) <= 0:
            fail(f"Ungueltige Groessenkorrektur fuer Symbol {index}.")

    root = ET.parse(project).getroot()
    if root.findtext("translatorName") != "JavaScript":
        fail("Das Projekt muss den JavaScript-Translator verwenden.")
    layouts = {layout.get("Name"): layout for layout in root.findall("Layout")}
    expected_layouts = {"Gruselino Karten", "Gruselino Papier", "Domino Papier", "Dobble Papier"}
    if set(layouts) != expected_layouts:
        fail("Die vier erwarteten Layouts fehlen oder wurden umbenannt.")
    for name, layout in layouts.items():
        refs = layout.findall("Reference")
        if len(refs) != 1 or refs[0].get("RelativePath") != "lautspiele.csv":
            fail(f"{name} verwendet nicht die gemeinsame CSV.")

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

    default_symbols = ROOT / "images" / "symbols" / "default"
    for index in range(1, 11):
        if not (default_symbols / f"{index:02}.png").is_file():
            fail(f"Standardbild {index:02}.png fehlt.")

    print("OK: Lautspiele-CardMaker-Projekt ist konsistent.")
    print("Layouts: 4 | Konfigurationszeilen: 3 | Definitionen: 50")
    print("Gruselino: 11 Karten je Layout | Domino: 10 | Dobble: 7 perfekt")


if __name__ == "__main__":
    validate()
