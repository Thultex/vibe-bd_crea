#!/usr/bin/env python3
"""Validiert Struktur, Konfiguration und Kombinatorik des Lautspiele-Projekts."""

from __future__ import annotations

import csv
import importlib.util
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SETS = ("default", "k")
MODES = ("gruselino", "domino", "dobble")


def fail(message: str) -> None:
    raise AssertionError(message)


def load_builder():
    path = ROOT / "generators" / "build_lautspiele_project.py"
    spec = importlib.util.spec_from_file_location("lautspiele_builder", path)
    if spec is None or spec.loader is None:
        fail("Builder konnte nicht geladen werden.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_one(path: Path) -> dict[str, str]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 1:
        fail(f"{path.name} muss genau eine Datenzeile enthalten.")
    return rows[0]


def validate() -> None:
    builder = load_builder()
    project = ROOT / "lautspiele.cmp"
    empty_defines = ROOT / "lautspiele_defines.csv"
    required_fields = {
        "symbol_set", "symbol_folder", "symbol_count", "symbol_names",
        "symbol_scale_map", "symbol_available_map",
        "gruselino_start", "gruselino_end", "gruselino_shift",
        "domino_start", "domino_end", "domino_shift",
        "dobble_start", "dobble_end", "dobble_shift",
    }
    for set_name in SETS:
        master = ROOT / f"symbols_{set_name}.csv"
        if not master.is_file():
            fail(f"Master fehlt: {master.name}")
        row = read_one(master)
        if not required_fields.issubset(row):
            fail(f"{master.name} enthält nicht alle Konfigurationsfelder.")
        if row["symbol_set"] != set_name:
            fail(f"{master.name} verwendet den falschen Satznamen.")
        if row["symbol_folder"] != f"images/symbols/{set_name}":
            fail(f"{master.name} verwendet den falschen Bildordner.")
        names = row["symbol_names"].split("|")
        scales = row["symbol_scale_map"].split("|")
        available = row["symbol_available_map"].split("|")
        if int(row["symbol_count"]) != len(names) or len(names) != len(scales):
            fail(f"Namen, Anzahl und Größen in {master.name} stimmen nicht überein.")
        if len(available) < builder.DOBBLE_SYMBOL_COUNT:
            fail(f"{master.name} hat keine vollständige Verfügbarkeitskarte.")
        if any(float(value) <= 0 for value in scales):
            fail(f"{master.name} enthält eine ungültige Größenkorrektur.")
        for mode in MODES:
            start = int(row[f"{mode}_start"])
            end = int(row[f"{mode}_end"])
            int(row[f"{mode}_shift"])
            if not 1 <= start <= end:
                fail(f"Ungültige Start-/Endspanne für {mode} in {master.name}.")
        expected_counts = {
            "gruselino": 12,
            "domino": int(row["domino_end"]) - int(row["domino_start"]) + 1,
            "dobble": 31,
        }
        for mode in MODES:
            derived = ROOT / f"{mode}_{set_name}.csv"
            derived_row = read_one(derived)
            if int(derived_row.get("Count", "0")) != expected_counts[mode]:
                fail(f"{derived.name} hat einen falschen Count.")
            for field in required_fields:
                if derived_row.get(field) != row.get(field):
                    fail(f"{derived.name} weicht im Feld {field} vom Master ab.")
        if (ROOT / f"memory_{set_name}.csv").exists():
            fail(f"Veraltete separate Memory-Datei vorhanden: memory_{set_name}.csv")

    if not project.is_file() or not empty_defines.is_file():
        fail("Projekt oder technische Defines-Datei fehlt.")
    with empty_defines.open(encoding="utf-8-sig", newline="") as handle:
        if list(csv.reader(handle)) != [["define", "value"]]:
            fail("Die technische Projekt-Defines-Datei muss leer bleiben.")

    root = ET.parse(project).getroot()
    if root.findtext("translatorName") != "JavaScript":
        fail("Das Projekt muss den JavaScript-Translator verwenden.")
    layouts = {layout.get("Name"): layout for layout in root.findall("Layout")}
    expected = {
        "Gruselino Papier": ("gruselino", "7860", "7602"),
        "Memory / Domino Papier": ("domino", "2362", "7400"),
        "Dobble Papier": ("dobble", "7860", "7602"),
    }
    if set(layouts) != set(expected):
        fail("Die drei erwarteten Layouts fehlen oder wurden umbenannt.")
    for name, (mode, export_width, export_height) in expected.items():
        layout = layouts[name]
        refs = layout.findall("Reference")
        expected_refs = {f"{mode}_default.csv", f"{mode}_k.csv"}
        actual_refs = {ref.get("RelativePath") for ref in refs}
        if actual_refs != expected_refs:
            fail(f"{name} bindet nicht alle erwarteten Satz-CSVs ein.")
        defaults = [ref.get("RelativePath") for ref in refs if ref.get("Default") == "true"]
        if defaults != [f"{mode}_k.csv"]:
            fail(f"{name} muss genau den K-Satz als Standardreferenz markieren.")
        if layout.get("defaultCount") != "1":
            fail(f"{name} muss den historischen Layout-Standardcount 1 verwenden.")
        if (layout.findtext("exportWidth"), layout.findtext("exportHeight")) != (
            export_width, export_height
        ):
            fail(f"{name} verwendet nicht die erwartete PDF-Seitengröße.")

    gruselino = layouts["Gruselino Papier"].findall("Element")
    bases = [e for e in gruselino if (e.get("name") or "").startswith("Grundsymbol ")]
    searches = [e for e in gruselino if (e.get("name") or "").startswith("Suchsymbol ")]
    if len(bases) != 8 or len(searches) != 8:
        fail("Gruselino Papier braucht acht Grund- und acht Suchsymbolfelder.")
    for element in [*bases, *searches]:
        code = element.get("variable", "")
        if "shuffledLogical" not in code or "Math.random()*41" not in code:
            fail("Gruselino-Permutation oder dezente Rotation fehlt.")
    expected_sizes = sorted(
        size for _, _, size in builder._scaled_positions(
            builder.GRUSELINO_PAPER_BASE_POSITIONS, 0.8
        )
    )
    if sorted(int(e.get("width", "0")) for e in bases) != expected_sizes:
        fail("Gruselino-Papiersymbole sind nicht um 20 Prozent verkleinert.")
    if len([e for e in gruselino if (e.get("name") or "").startswith("Twirl ")]) != 8:
        fail("Gruselino Papier braucht acht Suchkarten-Effekte.")
    fronts = [e for e in gruselino if e.get("name") == "Gruselino Front"]
    if len(fronts) != 1 or "cardIndex<=4" not in fronts[0].get("variable", ""):
        fail("Gruselino Papier braucht die historische Suchkarten-Front.")

    double_layout = layouts["Memory / Domino Papier"]
    double_symbols = [
        e for e in double_layout.findall("Element")
        if (e.get("name") or "").startswith("Memory Domino Symbol")
    ]
    if len(double_symbols) != 2:
        fail("Memory/Domino benötigt zwei trennbare Symbolkarten.")
    for element in double_symbols:
        code = element.get("variable", "")
        if "AddOverrideField('rotation','0')" not in code or "Math.random" in code:
            fail("Memory/Domino darf weder drehen noch zufällig skalieren.")
    cut = [e for e in double_layout.findall("Element") if e.get("name") == "Schnittzone"]
    if len(cut) != 1 or cut[0].get("x") != "579" or cut[0].get("width") != "22":
        fail("Memory/Domino braucht die originalnahe mittige Schnittzone.")
    borders = [
        e for e in double_layout.findall("Element")
        if (e.get("name") or "").startswith("Kartenrand ")
    ]
    if len(borders) != 2 or any(
        e.get("width") != "560" or e.get("height") != "560"
        for e in borders
    ):
        fail("Memory/Domino braucht zwei identische originalnahe Kartenränder.")
    required_ui = {
        "Memory Domino Front", "Twirl links", "Twirl rechts",
        "Memory Domino Hintergrund",
    }
    actual_ui = {e.get("name") for e in double_layout.findall("Element")}
    if not required_ui.issubset(actual_ui):
        fail("Memory/Domino fehlen originale Hintergrund-, Front- oder Twirl-Ebenen.")

    dobble = [
        e for e in layouts["Dobble Papier"].findall("Element")
        if (e.get("name") or "").startswith("Dobble Symbol")
    ]
    if len(dobble) != 6:
        fail("Dobble benötigt sechs Symbolfelder.")
    if any("0.82+Math.random()*0.36" not in e.get("variable", "") for e in dobble):
        fail("Dobble braucht die Größenvarianz von plus/minus 18 Prozent.")
    centers_x = [int(e.get("x", "0")) + int(e.get("width", "0")) / 2 for e in dobble]
    centers_y = [int(e.get("y", "0")) + int(e.get("height", "0")) / 2 for e in dobble]
    if max(centers_x) - min(centers_x) < 700 or max(centers_y) - min(centers_y) < 450:
        fail("Dobble-Symbole sind nicht weit genug über die Karte verteilt.")
    cards = [set(card) for card in builder.DOBBLE]
    if len(cards) != 31 or any(len(card) != 6 for card in cards):
        fail("Dobble-Matrix hat nicht 31 Karten mit je 6 Symbolen.")
    if any(len(cards[a] & cards[b]) != 1 for a in range(31) for b in range(a + 1, 31)):
        fail("Dobble-Matrix ist nicht perfekt.")
    occurrences = {symbol: 0 for symbol in range(31)}
    for card in cards:
        for symbol in card:
            occurrences[symbol] += 1
    if set(occurrences.values()) != {6}:
        fail("Dobble-Symbole erscheinen nicht jeweils sechsmal.")

    print("OK: Lautspiele-CardMaker-Projekt ist konsistent.")
    print("Layouts: 3 | Master-CSVs: 2 | Modus-CSVs: 6")
    print("Gruselino Papier: 4 Grundkarten + 8 Suchkarten, 80 Prozent Größe")
    print("Memory/Domino: ein trennbares Doppelmodul | Dobble: 31x6, perfekt")


if __name__ == "__main__":
    validate()
