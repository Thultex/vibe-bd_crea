#!/usr/bin/env python3
"""Prüft WND-TSV-Schemata, erzeugte CSVs und das CardMaker-Projekt."""

from __future__ import annotations

import csv
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from build_cardmaker import (
    A4_HEIGHT,
    A4_WIDTH,
    BRIDGE_HEIGHT,
    BRIDGE_WIDTH,
    BUILD_INFO_PATH,
    CARDMAKER_DIR,
    LIST_SPECS,
    PROJECT_PATH,
    load_tsv,
)


COLOR_TAG = re.compile(r"<fc=0x[0-9A-Fa-f]{6}>.+?</fc>")


def validate_tsv() -> None:
    all_sources = [spec.source for spec in LIST_SPECS]
    all_sources.append(CARDMAKER_DIR.parent / "cards" / "wort" / "liste-wort-kandidaten.tsv")
    for source in all_sources:
        with source.open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.reader(handle, delimiter="\t"))
        header = rows[0]
        if len({len(row) for row in rows}) != 1:
            raise RuntimeError(f"Uneinheitliche Spaltenzahl: {source}")
        if "format_text" not in header or header.index("format_text") != header.index("img") - 1:
            raise RuntimeError(f"format_text muss direkt vor img stehen: {source}")
        if header[header.index("ai") + 1] != "":
            raise RuntimeError(f"Leere Trennspalte hinter ai fehlt: {source}")
        fmt_index = header.index("format_text")
        for line_number, row in enumerate(rows[1:], start=2):
            if not row[fmt_index] or not COLOR_TAG.search(row[fmt_index]):
                raise RuntimeError(f"Farbiger format_text fehlt: {source}:{line_number}")


def validate_csv(spec_key: str, expected_count: int) -> None:
    path = CARDMAKER_DIR / f"{spec_key}.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["Count", "card_id", "plain_text", "format_text", "img", "has_img", "subtyp"]:
            raise RuntimeError(f"Falsches CSV-Schema: {path}")
        rows = list(reader)
    if len(rows) != expected_count:
        raise RuntimeError(f"Falsche Kartenanzahl in {path}: {len(rows)} statt {expected_count}")
    for row in rows:
        if row["has_img"] == "1" and not (CARDMAKER_DIR / row["img"]).is_file():
            raise RuntimeError(f"Fehlendes Bild für {row['card_id']}: {row['img']}")


def validate_project() -> None:
    info = json.loads(BUILD_INFO_PATH.read_text(encoding="utf-8"))
    mode = info["mode"]
    expected_size = (A4_WIDTH, A4_HEIGHT) if mode == "paper" else (BRIDGE_WIDTH, BRIDGE_HEIGHT)
    root = ET.parse(PROJECT_PATH).getroot()
    if root.findtext("translatorName") != "JavaScript":
        raise RuntimeError("CardMaker-Projekt muss den JavaScript-Übersetzer verwenden.")
    layouts = root.findall("Layout")
    if len(layouts) != len(LIST_SPECS):
        raise RuntimeError("Erwartet werden genau vier typbezogene Layouts.")

    for layout, spec in zip(layouts, LIST_SPECS, strict=True):
        actual_size = (int(layout.get("width", "0")), int(layout.get("height", "0")))
        if actual_size != expected_size or layout.get("dpi") != "300":
            raise RuntimeError(f"Falsches Format für {spec.key}: {actual_size}")
        reference = layout.find("Reference")
        if reference is None or reference.get("RelativePath") != f"{spec.key}.csv":
            raise RuntimeError(f"Falsche Referenz für {spec.key}.")
        elements = {item.get("name"): item for item in layout.findall("Element")}
        if mode == "paper":
            crops = [name for name in elements if name and name.startswith("Crop ")]
            if len(crops) != 8 or elements["White A4 background"].get("backgroundcolor") != "0xFFFFFFFF":
                raise RuntimeError(f"A4-Hintergrund oder Schnittmarken fehlen bei {spec.key}.")
            if elements["Formatted content"].get("verticalalign") != "1":
                raise RuntimeError(f"Text ist bei {spec.key} nicht vertikal zentriert.")
        else:
            if elements["Black background"].get("backgroundcolor") != "0x000000FF":
                raise RuntimeError(f"Schwarzer Print-Hintergrund fehlt bei {spec.key}.")
            if "has_img" not in elements["Card image"].get("variable", ""):
                raise RuntimeError(f"Bildumschaltung fehlt bei {spec.key}.")
            if elements["Formatted fallback"].get("verticalalign") != "1":
                raise RuntimeError(f"Fallbacktext ist bei {spec.key} nicht vertikal zentriert.")


def main() -> None:
    validate_tsv()
    counts = {spec.key: len(load_tsv(spec)) for spec in LIST_SPECS}
    for key, count in counts.items():
        validate_csv(key, count)
    validate_project()
    print(
        "WND CardMaker valide: "
        f"{sum(counts.values())} Karten, vier Layouts, Modus {json.loads(BUILD_INFO_PATH.read_text(encoding='utf-8'))['mode']}."
    )


if __name__ == "__main__":
    main()
