#!/usr/bin/env python3
"""Prüft TSV-Farben, CSV-Formate und beide WND-CardMaker-Projekte."""

from __future__ import annotations

import argparse
import csv
import re
import xml.etree.ElementTree as ET

from build_cardmaker import (
    BRIDGE_HEIGHT,
    BRIDGE_WIDTH,
    CARDMAKER_DIR,
    COLOR_PATTERN,
    ListSpec,
    LIST_SPECS,
    PAPER_HEIGHT,
    PAPER_WIDTH,
    PROJECT_PATHS,
    TEXT_VERSIONS,
    formatted_text,
    load_tsv,
    load_text_version,
    resolve_text,
)


COLOR_TAG = re.compile(r"<fc=(0x[0-9A-Fa-f]{6})>.+?</fc>")
TAG = re.compile(r"</?fc(?:=0x[0-9A-Fa-f]{6})?>")


def channel_sum(color: str) -> int:
    return sum(int(color[index : index + 2], 16) for index in (2, 4, 6))


def validate_tsv() -> None:
    specs = list(LIST_SPECS)
    idea_source = CARDMAKER_DIR.parent / "cards" / "liste-wortideen.tsv"
    for source, color_count in [(spec.source, len(spec.target_fields)) for spec in specs] + [(idea_source, 1)]:
        with source.open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.reader(handle, delimiter="\t"))
        header = rows[0]
        if len({len(row) for row in rows}) != 1:
            raise RuntimeError(f"Uneinheitliche Spaltenzahl: {source}")
        if "format_text" in header:
            raise RuntimeError(f"format_text gehört nicht mehr in die TSV-Datei: {source}")
        if source.name in {"liste-ort.tsv", "liste-aufgabe.tsv"}:
            words_and_phrases = ["wort_1", "wort_2", "phrase", "phrase_story"]
            if [field for field in header if field in words_and_phrases] != words_and_phrases:
                raise RuntimeError(f"Zielwörter, phrase und phrase_story stehen in falscher Reihenfolge: {source}")
        expected_colors = [f"col{index}" for index in range(1, color_count + 1)]
        if header[header.index("img") - color_count : header.index("img")] != expected_colors:
            raise RuntimeError(f"Farbspalten müssen direkt vor img stehen: {source}")
        if header[header.index("ai") + 1] != "":
            raise RuntimeError(f"Leere Trennspalte hinter ai fehlt: {source}")
        indexes = [header.index(color) for color in expected_colors]
        for line_number, row in enumerate(rows[1:], start=2):
            for index in indexes:
                if not COLOR_PATTERN.fullmatch(row[index]):
                    raise RuntimeError(f"Ungültiger Farbwert: {source}:{line_number}")

    with idea_source.open(encoding="utf-8-sig", newline="") as handle:
        ideas = list(csv.DictReader(handle, delimiter="\t"))
    words = [(row.get("wort") or "").strip().casefold() for row in ideas]
    if len(words) != len(set(words)):
        raise RuntimeError(f"Doppelte Wörter in {idea_source}")
    for line_number, row in enumerate(ideas, start=2):
        if row.get("anzahl") or row.get("id"):
            raise RuntimeError(f"Wortidee ist bereits konkretisiert: {idea_source}:{line_number}")
        if not row.get("wort") or row.get("subtyp") not in {"nomen", "adjektiv"} or not row.get("status"):
            raise RuntimeError(f"Unvollständige Wortidee: {idea_source}:{line_number}")
        for field in ("frequenz", "komplexität", "spezifität"):
            if row.get(field) not in {"1", "2", "3", "4", "5"}:
                raise RuntimeError(f"Ungültige Bewertung in {field}: {idea_source}:{line_number}")


def validate_text_selection() -> None:
    for spec in LIST_SPECS:
        if not spec.story_field:
            continue
        source_row = load_tsv(spec)[0]
        if resolve_text(source_row, spec, "phrase_story") != source_row[spec.plain_field]:
            raise RuntimeError(f"Leeres phrase_story fällt bei {spec.key} nicht auf phrase zurück.")
        story_row = source_row.copy()
        story_row[spec.story_field] = f"{source_row[spec.plain_field]} Danach geht die Geschichte weiter."
        if resolve_text(story_row, spec, "phrase_story") != story_row[spec.story_field]:
            raise RuntimeError(f"phrase_story wird bei {spec.key} nicht ausgewählt.")
        for light_card in (True, False):
            formatted = formatted_text(story_row, spec, "phrase_story", light_card=light_card)
            if TAG.sub("", formatted) != story_row[spec.story_field]:
                raise RuntimeError(f"Storyformatierung verändert den Text bei {spec.key}.")


def validate_csv(spec: ListSpec, source_rows: list[dict[str, str]], text_version: str) -> None:
    path = CARDMAKER_DIR / f"{spec.key}.csv"
    expected_fields = [
        "Count",
        "card_id",
        "plain_text",
        "img",
        "subtyp",
        "paper-label",
        "col1",
        "col2",
        "format-hell",
        "format-dunkel",
    ]
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_fields:
            raise RuntimeError(f"Falsches CSV-Schema: {path}")
        rows = list(reader)
    if len(rows) != len(source_rows):
        raise RuntimeError(f"Falsche Kartenanzahl in {path}: {len(rows)} statt {len(source_rows)}")
    for row, source_row in zip(rows, source_rows, strict=True):
        expected_text = resolve_text(source_row, spec, text_version)
        if row["plain_text"] != expected_text:
            raise RuntimeError(f"Falsche Textfassung bei {row['card_id']}: erwartet {text_version}.")
        if not re.fullmatch(r"[A-ZÄÖÜ]+ · [A-Z]+[1-9][0-9]*", row["paper-label"]):
            raise RuntimeError(f"Ungültige Paper-Kennung bei {row['card_id']}: {row['paper-label']}")
        if TAG.sub("", row["format-hell"]) != row["plain_text"]:
            raise RuntimeError(f"format-hell verändert den Text von {row['card_id']}.")
        if TAG.sub("", row["format-dunkel"]) != row["plain_text"]:
            raise RuntimeError(f"format-dunkel verändert den Text von {row['card_id']}.")
        light_colors = COLOR_TAG.findall(row["format-hell"])
        dark_colors = COLOR_TAG.findall(row["format-dunkel"])
        if not light_colors or len(light_colors) != len(dark_colors) or light_colors == dark_colors:
            raise RuntimeError(f"Helle/dunkle Farbvarianten fehlen bei {row['card_id']}.")
        expected_dark = [color for color in (row["col1"], row["col2"]) if color]
        if sorted(dark_colors) != sorted(expected_dark):
            raise RuntimeError(f"format-dunkel übernimmt die TSV-Farben bei {row['card_id']} nicht unverändert.")
        if any(channel_sum(light) >= channel_sum(dark) for light, dark in zip(light_colors, dark_colors, strict=True)):
            raise RuntimeError(f"format-hell ist bei {row['card_id']} nicht dunkler als format-dunkel.")
        if row["img"] and not (CARDMAKER_DIR / row["img"]).is_file():
            raise RuntimeError(f"Fehlendes Bild für {row['card_id']}: {row['img']}")


def validate_project(variant: str) -> None:
    root = ET.parse(PROJECT_PATHS[variant]).getroot()
    if root.findtext("translatorName") != "Incept":
        raise RuntimeError(f"{variant}: Incept-Übersetzer fehlt.")
    layouts = root.findall("Layout")
    if len(layouts) != len(LIST_SPECS):
        raise RuntimeError(f"{variant}: Erwartet werden vier typbezogene Layouts.")

    for layout, spec in zip(layouts, LIST_SPECS, strict=True):
        size = (int(layout.get("width", "0")), int(layout.get("height", "0")))
        expected_size = (PAPER_WIDTH, PAPER_HEIGHT) if variant == "paper" else (BRIDGE_WIDTH, BRIDGE_HEIGHT)
        if size != expected_size or layout.get("dpi") != "300":
            raise RuntimeError(f"{variant}/{spec.key}: Falsches Kartenformat {size}.")
        if layout.findtext("exportWidth") != str(expected_size[0]) or layout.findtext("exportHeight") != str(expected_size[1]):
            raise RuntimeError(f"{variant}/{spec.key}: Exportmaß fehlt.")
        if layout.findtext("exportLayoutBorderCrossSize") != "0":
            raise RuntimeError(f"{variant}/{spec.key}: Crop-Zeichen sind aktiviert.")
        elements = {element.get("name"): element for element in layout.findall("Element")}
        if any(name and name.startswith("Crop ") for name in elements):
            raise RuntimeError(f"{variant}/{spec.key}: Eingezeichnete Crop-Zeichen gefunden.")
        reference = layout.find("Reference")
        if reference is None or reference.get("RelativePath") != f"{spec.key}.csv":
            raise RuntimeError(f"{variant}/{spec.key}: CSV-Referenz fehlt.")

        if variant == "paper":
            if elements["White background"].get("backgroundcolor") != "0xFFFFFFFF":
                raise RuntimeError(f"paper/{spec.key}: Weißer Hintergrund fehlt.")
            if elements["Formatted paper text"].get("variable") != "@[format-hell]":
                raise RuntimeError(f"paper/{spec.key}: format-hell wird nicht verwendet.")
            label = elements.get("Paper card label")
            if label is None or label.get("variable") != "@[paper-label]" or label.get("horizontalalign") != "0":
                raise RuntimeError(f"paper/{spec.key}: Kennzeichnung links oben fehlt.")
            if any(element.get("type") == "Graphic" for element in elements.values()):
                raise RuntimeError(f"paper/{spec.key}: Paper soll keine Bilder enthalten.")
            if layout.findtext("exportLayoutBorder") != "true":
                raise RuntimeError(f"paper/{spec.key}: Export-Kartenrand fehlt.")
        else:
            if elements["Black background"].get("backgroundcolor") != "0x000000FF":
                raise RuntimeError(f"print/{spec.key}: Schwarzer Hintergrund fehlt.")
            if "@[format-dunkel]" not in elements["Formatted print fallback"].get("variable", ""):
                raise RuntimeError(f"print/{spec.key}: format-dunkel wird nicht verwendet.")
            fallback_variable = elements["Formatted print fallback"].get("variable", "")
            image_variable = elements["Card image"].get("variable", "")
            if "@[img]" not in fallback_variable or "#empty" not in fallback_variable:
                raise RuntimeError(f"print/{spec.key}: Textumschaltung prüft img nicht direkt.")
            if "@[img]" not in image_variable or "#empty" not in image_variable:
                raise RuntimeError(f"print/{spec.key}: Bildumschaltung prüft img nicht direkt.")

def main(text_version: str) -> None:
    validate_tsv()
    validate_text_selection()
    source_rows = {spec.key: load_tsv(spec) for spec in LIST_SPECS}
    for spec in LIST_SPECS:
        validate_csv(spec, source_rows[spec.key], text_version)
    validate_project("print")
    validate_project("paper")
    count = sum(len(rows) for rows in source_rows.values())
    print(
        f"WND CardMaker valide: {count} Karten, vier Print- und vier quadratische Paper-Layouts, "
        f"Textfassung {text_version}."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--text-version",
        choices=TEXT_VERSIONS,
        help="Prüft einen Build mit abweichender Textfassung.",
    )
    arguments = parser.parse_args()
    main(arguments.text_version or load_text_version())
