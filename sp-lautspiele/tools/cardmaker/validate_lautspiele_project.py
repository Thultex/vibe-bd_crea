#!/usr/bin/env python3
"""Validiert Struktur, Konfiguration und Kombinatorik des Lautspiele-Projekts."""

from __future__ import annotations

import csv
import importlib.util
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SETS = ("default", "k")
MODES = ("gruselino", "memory", "domino", "dobble")


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
        "memory_start", "memory_end", "memory_shift",
        "domino_start", "domino_end", "domino_shift",
        "dobble_start", "dobble_end", "dobble_shift",
    }
    expected_mode_counts: dict[tuple[str, str], int] = {}
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
        expected_mode_counts.update({
            ("gruselino", set_name): 12,
            ("memory", set_name): 2 * (
                int(row["memory_end"]) - int(row["memory_start"]) + 1
            ),
            ("domino", set_name): (
                int(row["domino_end"]) - int(row["domino_start"]) + 1
            ),
            ("dobble", set_name): 31,
        })
        for mode in MODES:
            derived = ROOT / f"{mode}_{set_name}.csv"
            derived_row = read_one(derived)
            if int(derived_row.get("Count", "0")) != expected_mode_counts[(mode, set_name)]:
                fail(f"{derived.name} hat einen falschen Count.")
            for field in required_fields:
                if derived_row.get(field) != row.get(field):
                    fail(f"{derived.name} weicht im Feld {field} vom Master ab.")

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
        "Gruselino Karten": ("gruselino_k.csv", "12"),
        "Gruselino Papier": ("gruselino_k.csv", "12"),
        "Memory Papier": ("memory_k.csv", "20"),
        "Domino Papier": ("domino_k.csv", "10"),
        "Dobble Papier": ("dobble_k.csv", "31"),
    }
    if set(layouts) != set(expected):
        fail("Die fünf erwarteten Layouts fehlen oder wurden umbenannt.")
    for name, (reference, default_count) in expected.items():
        layout = layouts[name]
        refs = layout.findall("Reference")
        if len(refs) != 1 or refs[0].get("RelativePath") != reference:
            fail(f"{name} verwendet nicht die erwartete Modus-CSV.")
        if layout.get("defaultCount") != default_count:
            fail(f"{name} hat eine unerwartete Standard-Kartenanzahl.")

    for name in ("Gruselino Karten", "Gruselino Papier"):
        elements = layouts[name].findall("Element")
        bases = [e for e in elements if (e.get("name") or "").startswith("Grundsymbol ")]
        searches = [e for e in elements if (e.get("name") or "").startswith("Suchsymbol ")]
        if len(bases) != 8 or len(searches) != 8:
            fail(f"{name} braucht acht Grund- und acht Suchsymbolfelder.")
        for element in [*bases, *searches]:
            code = element.get("variable", "")
            if "shuffledLogical" not in code or "Math.random()*360" not in code:
                fail(f"Permutation oder Rotation fehlt in {name}.")
        if name == "Gruselino Papier":
            twirls = [e for e in elements if (e.get("name") or "").startswith("Twirl ")]
            if len(twirls) != 8:
                fail("Gruselino Papier braucht acht Suchkarten-Effekte.")
            fronts = [e for e in elements if e.get("name") == "Gruselino Front"]
            if len(fronts) != 1 or "cardIndex<=4" not in fronts[0].get("variable", ""):
                fail("Gruselino Papier braucht die historische Suchkarten-Front.")

    memory = [e for e in layouts["Memory Papier"].findall("Element")
              if e.get("name") == "Memory Symbol"]
    if len(memory) != 1 or "Math.floor((cardIndex-1)/2)" not in memory[0].get("variable", ""):
        fail("Memory muss jedes Symbol genau als Paar erzeugen.")

    domino = [e for e in layouts["Domino Papier"].findall("Element")
              if (e.get("name") or "").startswith("Domino Symbol")]
    if len(domino) != 2:
        fail("Domino benötigt zwei Symbolfelder.")
    for element in domino:
        code = element.get("variable", "")
        if "Math.random()*360" not in code or "0.95+Math.random" in code:
            fail("Domino darf drehen, aber nicht zufällig skalieren.")

    dobble = [e for e in layouts["Dobble Papier"].findall("Element")
              if (e.get("name") or "").startswith("Dobble Symbol")]
    if len(dobble) != 6:
        fail("Dobble benötigt sechs Symbolfelder.")
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
    print("Layouts: 5 | Master-CSVs: 2 | Modus-CSVs: 8")
    print("Gruselino: 4 Grundkarten + 8 Suchkarten | Memory: Symbolpaare")
    print("Domino: Bereichs-Count | Dobble: 31 Karten, 6 Symbole, perfekt")


if __name__ == "__main__":
    validate()
