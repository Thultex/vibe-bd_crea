#!/usr/bin/env python3
"""Erzeugt das minimale CardMaker-Projekt aus den WND-TSV-Listen."""

from __future__ import annotations

import argparse
import csv
import json
import os
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


CARDMAKER_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CARDMAKER_DIR.parent
CONFIG_PATH = CARDMAKER_DIR / "cardmaker.json"
PROJECT_PATH = CARDMAKER_DIR / "wanderer.cmp"
BUILD_INFO_PATH = CARDMAKER_DIR / "build-info.json"

A4_WIDTH = 2480
A4_HEIGHT = 3508
BRIDGE_WIDTH = 675
BRIDGE_HEIGHT = 1050
DPI = 300


@dataclass(frozen=True)
class ListSpec:
    key: str
    title: str
    source: Path
    plain_field: str
    font_size: int


LIST_SPECS = (
    ListSpec("ort", "Ort", PROJECT_DIR / "cards" / "ort" / "liste-ort.tsv", "phrase", 64),
    ListSpec("aufgabe", "Aufgabe", PROJECT_DIR / "cards" / "aufgabe" / "liste-aufgabe.tsv", "phrase", 68),
    ListSpec("wort", "Wort", PROJECT_DIR / "cards" / "wort" / "liste-wort.tsv", "wort", 92),
    ListSpec("figur", "Figur", PROJECT_DIR / "cards" / "figur" / "liste-figur.tsv", "name", 88),
)


def read_mode(override: str | None) -> str:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    mode = override or config.get("mode")
    if mode not in {"paper", "print"}:
        raise ValueError("cardmaker.json: 'mode' muss 'paper' oder 'print' sein.")
    return mode


def load_tsv(spec: ListSpec) -> list[dict[str, str]]:
    with spec.source.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    return [row for row in rows if (row.get("id") or "").strip()]


def image_reference(raw_value: str, source: Path) -> tuple[str, bool]:
    value = raw_value.strip()
    if not value:
        return "", False

    value_path = Path(value)
    candidates = [value_path] if value_path.is_absolute() else [source.parent / value_path, PROJECT_DIR / value_path]
    for candidate in candidates:
        if candidate.is_file():
            relative = os.path.relpath(candidate.resolve(), CARDMAKER_DIR).replace("\\", "/")
            return relative, True
    return "", False


def write_reference(spec: ListSpec, rows: list[dict[str, str]]) -> int:
    output = CARDMAKER_DIR / f"{spec.key}.csv"
    fields = ["Count", "card_id", "plain_text", "format_text", "img", "has_img", "subtyp"]
    with output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            image, has_image = image_reference(row.get("img", ""), spec.source)
            writer.writerow(
                {
                    "Count": row.get("anzahl", "1") or "1",
                    "card_id": row["id"],
                    "plain_text": row.get(spec.plain_field, ""),
                    "format_text": row.get("format_text", "") or row.get(spec.plain_field, ""),
                    "img": image,
                    "has_img": "1" if has_image else "0",
                    "subtyp": row.get("subtyp", ""),
                }
            )
    return len(rows)


def element(
    parent: ET.Element,
    *,
    name: str,
    kind: str,
    variable: str,
    x: int,
    y: int,
    width: int,
    height: int,
    font_size: int = 12,
    element_color: str = "0x000000FF",
    background_color: str = "0x00000000",
    border_color: str = "0x00000000",
    border_thickness: int = 0,
    auto_scale: bool = False,
    lock_aspect: bool = False,
) -> ET.Element:
    return ET.SubElement(
        parent,
        "Element",
        {
            "variable": variable,
            "type": kind,
            "x": str(x),
            "y": str(y),
            "width": str(width),
            "height": str(height),
            "borderthickness": str(border_thickness),
            "autoscalefont": str(auto_scale).lower(),
            "lockaspect": str(lock_aspect).lower(),
            "keeporiginalsize": "false",
            "centerimageonorigin": "false",
            "outlinethickness": "0",
            "rotation": "0",
            "horizontalalign": "1",
            "verticalalign": "1",
            "colortype": "0",
            "opacity": "255",
            "tilesize": "",
            "mirrortype": "0",
            "imagemasksurface": "false",
            "lineheight": "14",
            "wordspace": "0",
            "justifiedtext": "false",
            "name": name,
            "font": f"Arial Rounded MT Bold;{font_size};0;0;0;0",
            "elementcolor": element_color,
            "bordercolor": border_color,
            "backgroundcolor": background_color,
            "enabled": "true",
            "outlinecolor": "0x000000FF",
            "gradient": "",
            "colormatrix": "",
        },
    )


def add_crop_marks(layout: ET.Element) -> None:
    card_x = round((A4_WIDTH - BRIDGE_WIDTH) / 2)
    card_y = round((A4_HEIGHT - BRIDGE_HEIGHT) / 2)
    mark_length = 48
    gap = 14
    thickness = 3
    right = card_x + BRIDGE_WIDTH
    bottom = card_y + BRIDGE_HEIGHT
    marks = (
        ("Crop top left horizontal", card_x - gap - mark_length, card_y, mark_length, thickness),
        ("Crop top left vertical", card_x, card_y - gap - mark_length, thickness, mark_length),
        ("Crop top right horizontal", right + gap, card_y, mark_length, thickness),
        ("Crop top right vertical", right - thickness, card_y - gap - mark_length, thickness, mark_length),
        ("Crop bottom left horizontal", card_x - gap - mark_length, bottom - thickness, mark_length, thickness),
        ("Crop bottom left vertical", card_x, bottom + gap, thickness, mark_length),
        ("Crop bottom right horizontal", right + gap, bottom - thickness, mark_length, thickness),
        ("Crop bottom right vertical", right - thickness, bottom + gap, thickness, mark_length),
    )
    for name, x, y, width, height in marks:
        element(
            layout,
            name=name,
            kind="Text",
            variable="''",
            x=x,
            y=y,
            width=width,
            height=height,
            background_color="0x111111FF",
        )


def add_layout(root: ET.Element, spec: ListSpec, mode: str) -> None:
    paper = mode == "paper"
    width, height = (A4_WIDTH, A4_HEIGHT) if paper else (BRIDGE_WIDTH, BRIDGE_HEIGHT)
    layout = ET.SubElement(
        root,
        "Layout",
        {
            "combineReferences": "false",
            "width": str(width),
            "height": str(height),
            "buffer": "0",
            "Name": f"{spec.title} – {'PAPER A4' if paper else 'PRINT Bridge'}",
            "defaultCount": "1",
            "dpi": str(DPI),
            "drawBorder": "false",
        },
    )

    if paper:
        card_x = round((A4_WIDTH - BRIDGE_WIDTH) / 2)
        card_y = round((A4_HEIGHT - BRIDGE_HEIGHT) / 2)
        element(
            layout,
            name="Formatted content",
            kind="FormattedText",
            variable="format_text",
            x=card_x + 48,
            y=card_y + 48,
            width=BRIDGE_WIDTH - 96,
            height=BRIDGE_HEIGHT - 96,
            font_size=spec.font_size,
            element_color="0x252525FF",
            auto_scale=True,
        )
        add_crop_marks(layout)
        element(
            layout,
            name="White A4 background",
            kind="Text",
            variable="''",
            x=0,
            y=0,
            width=A4_WIDTH,
            height=A4_HEIGHT,
            background_color="0xFFFFFFFF",
        )
    else:
        element(
            layout,
            name="Formatted fallback",
            kind="FormattedText",
            variable="if (has_img === '1') { AddOverrideField('enabled', 'false'); } format_text",
            x=48,
            y=48,
            width=BRIDGE_WIDTH - 96,
            height=BRIDGE_HEIGHT - 96,
            font_size=spec.font_size,
            element_color="0xF7F4EFFF",
            auto_scale=True,
        )
        element(
            layout,
            name="Card image",
            kind="Graphic",
            variable="if (has_img !== '1') { AddOverrideField('enabled', 'false'); } img",
            x=0,
            y=0,
            width=BRIDGE_WIDTH,
            height=BRIDGE_HEIGHT,
        )
        element(
            layout,
            name="Black background",
            kind="Text",
            variable="''",
            x=0,
            y=0,
            width=BRIDGE_WIDTH,
            height=BRIDGE_HEIGHT,
            background_color="0x000000FF",
        )

    ET.SubElement(layout, "Reference", {"RelativePath": f"{spec.key}.csv", "Default": "true"})
    for tag, value in (
        ("exportNameFormat", f"wnd_{spec.key}_#_"),
        ("exportRotation", "0"),
        ("exportTransparentBackground", "false"),
        ("exportPDFAsPageBack", "false"),
        ("exportWidth", str(width)),
        ("exportHeight", str(height)),
        ("zoom", "0.24" if paper else "0.65"),
        ("exportLayoutBorder", "false"),
        ("exportLayoutBorderCrossSize", "0"),
    ):
        ET.SubElement(layout, tag).text = value


def write_project(mode: str) -> None:
    root = ET.Element(
        "Project",
        {
            "xmlns:xsd": "http://www.w3.org/2001/XMLSchema",
            "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        },
    )
    for spec in LIST_SPECS:
        add_layout(root, spec, mode)
    for tag, value in (
        ("translatorName", "JavaScript"),
        ("exportNameFormat", "wnd_#_"),
        ("defaultDefineReferenceType", "CSV"),
        ("overrideDefineReferenceName", ""),
        ("jsTildeMeansCode", "true"),
        ("jsKeepFunctions", "true"),
        ("jsSingleQuoteStartsCode", "true"),
        ("collapsedNodes", ""),
    ):
        ET.SubElement(root, tag).text = value
    ET.indent(root, space="  ")
    ET.ElementTree(root).write(PROJECT_PATH, encoding="utf-8", xml_declaration=True)


def build(mode_override: str | None = None) -> None:
    mode = read_mode(mode_override)
    counts: dict[str, int] = {}
    for spec in LIST_SPECS:
        counts[spec.key] = write_reference(spec, load_tsv(spec))
    write_project(mode)
    BUILD_INFO_PATH.write_text(
        json.dumps({"mode": mode, "dpi": DPI, "cards": counts}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    total = sum(counts.values())
    print(f"CardMaker-Projekt erzeugt: {mode}, {len(LIST_SPECS)} Layouts, {total} Karten.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("paper", "print"), help="Überschreibt den Modus aus cardmaker.json.")
    args = parser.parse_args()
    build(args.mode)


if __name__ == "__main__":
    main()
