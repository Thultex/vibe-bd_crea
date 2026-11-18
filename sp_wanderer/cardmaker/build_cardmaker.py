#!/usr/bin/env python3
"""Erzeugt die festen Print- und Paper-Projekte für WND aus den TSV-Listen."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


CARDMAKER_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CARDMAKER_DIR.parent
TEXT_VERSION_PATH = CARDMAKER_DIR / "text-version.json"
TEXT_VERSIONS = ("phrase", "phrase_story")
PROJECT_PATHS = {
    "print": CARDMAKER_DIR / "wanderer-print.cmp",
    "paper": CARDMAKER_DIR / "wanderer-paper.cmp",
}

BRIDGE_WIDTH = 675
BRIDGE_HEIGHT = 1050
PAPER_WIDTH = 531
PAPER_HEIGHT = 531
DPI = 300
COLOR_PATTERN = re.compile(r"^0x[0-9A-Fa-f]{6}$")
WORD_PATTERN = re.compile(r"[A-Za-zÄÖÜäöüß]+")


@dataclass(frozen=True)
class ListSpec:
    key: str
    title: str
    source: Path
    plain_field: str
    story_field: str | None
    target_fields: tuple[str, ...]
    font_size: int


LIST_SPECS = (
    ListSpec(
        "ort",
        "Ort",
        PROJECT_DIR / "cards" / "ort" / "liste-ort.tsv",
        "phrase",
        "phrase_story",
        ("wort_1", "wort_2"),
        64,
    ),
    ListSpec(
        "aufgabe",
        "Aufgabe",
        PROJECT_DIR / "cards" / "aufgabe" / "liste-aufgabe.tsv",
        "phrase",
        "phrase_story",
        ("wort_1", "wort_2"),
        68,
    ),
    ListSpec("wort", "Wort", PROJECT_DIR / "cards" / "wort" / "liste-wort.tsv", "wort", None, ("wort",), 92),
    ListSpec("figur", "Figur", PROJECT_DIR / "cards" / "figur" / "liste-figur.tsv", "name", None, ("name",), 88),
)


def load_text_version() -> str:
    with TEXT_VERSION_PATH.open(encoding="utf-8") as handle:
        value = json.load(handle).get("text_version", "")
    if value not in TEXT_VERSIONS:
        allowed = ", ".join(TEXT_VERSIONS)
        raise ValueError(f"Ungültige Textfassung {value!r} in {TEXT_VERSION_PATH}; erlaubt: {allowed}.")
    return value


def resolve_text(row: dict[str, str], spec: ListSpec, text_version: str) -> str:
    if text_version not in TEXT_VERSIONS:
        raise ValueError(f"Unbekannte Textfassung: {text_version!r}")
    if text_version == "phrase_story" and spec.story_field:
        story = (row.get(spec.story_field) or "").strip()
        if story:
            return story
    return row[spec.plain_field]


def load_tsv(spec: ListSpec) -> list[dict[str, str]]:
    with spec.source.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    return [row for row in rows if (row.get("id") or "").strip()]


def image_reference(raw_value: str, source: Path) -> str:
    value = raw_value.strip()
    if not value:
        return ""
    value_path = Path(value)
    candidates = [value_path] if value_path.is_absolute() else [source.parent / value_path, PROJECT_DIR / value_path]
    for candidate in candidates:
        if candidate.is_file():
            relative = os.path.relpath(candidate.resolve(), CARDMAKER_DIR).replace("\\", "/")
            return relative
    return ""


def darken_color(value: str, factor: float = 0.55) -> str:
    if not COLOR_PATTERN.fullmatch(value):
        raise ValueError(f"Ungültiger Farbwert: {value!r}")
    channels = [int(value[index : index + 2], 16) for index in (2, 4, 6)]
    darkened = [max(0, min(255, round(channel * factor))) for channel in channels]
    return "0x" + "".join(f"{channel:02X}" for channel in darkened)


def umlaut_variant(value: str) -> str:
    replacements = (("au", "äu"), ("a", "ä"), ("o", "ö"), ("u", "ü"))
    lowered = value.casefold()
    for old, new in replacements:
        position = lowered.rfind(old)
        if position >= 0:
            return lowered[:position] + new + lowered[position + len(old) :]
    return lowered


def token_matches(token: str, target: str) -> bool:
    token_value = token.casefold()
    target_value = target.casefold()
    if token_value == target_value:
        return True

    stems = {target_value, umlaut_variant(target_value)}
    if target_value.endswith("en") and len(target_value) > 3:
        stems.add(target_value[:-2])
    elif target_value.endswith("n") and len(target_value) > 3:
        stems.add(target_value[:-1])
    return any(len(stem) >= 3 and token_value.startswith(stem) for stem in stems)


def format_phrase(text: str, targets: list[str], colors: list[str]) -> str:
    tokens = list(WORD_PATTERN.finditer(text))
    selected: list[tuple[int, int, str]] = []
    used_tokens: set[int] = set()
    for target, color in zip(targets, colors, strict=True):
        for token_index, token in enumerate(tokens):
            if token_index not in used_tokens and token_matches(token.group(0), target):
                selected.append((token.start(), token.end(), color))
                used_tokens.add(token_index)
                break
        else:
            raise ValueError(f"Zielwort {target!r} wurde in {text!r} nicht gefunden.")

    output: list[str] = []
    cursor = 0
    for start, end, color in sorted(selected):
        output.append(text[cursor:start])
        output.append(f"<fc={color}>{text[start:end]}</fc>")
        cursor = end
    output.append(text[cursor:])
    return "".join(output)


def formatted_text(row: dict[str, str], spec: ListSpec, text_version: str, *, light_card: bool) -> str:
    text = resolve_text(row, spec, text_version)
    base_colors = [row[f"col{index}"] for index in range(1, len(spec.target_fields) + 1)]
    colors = [darken_color(color) for color in base_colors] if light_card else base_colors
    if len(spec.target_fields) == 1 and spec.target_fields[0] == spec.plain_field:
        return f"<fc={colors[0]}>{text}</fc>"
    targets = [row[field] for field in spec.target_fields]
    return format_phrase(text, targets, colors)


def display_id(value: str) -> str:
    match = re.fullmatch(r"([A-Za-z]+)0*([0-9]+)", value.strip())
    if not match:
        return value.upper()
    return f"{match.group(1).upper()}{int(match.group(2))}"


def write_reference(spec: ListSpec, rows: list[dict[str, str]], text_version: str) -> int:
    output = CARDMAKER_DIR / f"{spec.key}.csv"
    fields = [
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
    with output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            image = image_reference(row.get("img", ""), spec.source)
            writer.writerow(
                {
                    "Count": row.get("anzahl", "1") or "1",
                    "card_id": row["id"],
                    "plain_text": resolve_text(row, spec, text_version),
                    "img": image,
                    "subtyp": row.get("subtyp", ""),
                    "paper-label": f"{spec.title.upper()} · {display_id(row['id'])}",
                    "col1": row.get("col1", ""),
                    "col2": row.get("col2", ""),
                    "format-hell": formatted_text(row, spec, text_version, light_card=True),
                    "format-dunkel": formatted_text(row, spec, text_version, light_card=False),
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
    auto_scale: bool = False,
    horizontal_align: int = 1,
    vertical_align: int = 1,
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
            "borderthickness": "0",
            "autoscalefont": str(auto_scale).lower(),
            "lockaspect": "false",
            "keeporiginalsize": "false",
            "centerimageonorigin": "false",
            "outlinethickness": "0",
            "rotation": "0",
            "horizontalalign": str(horizontal_align),
            "verticalalign": str(vertical_align),
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
            "bordercolor": "0x00000000",
            "backgroundcolor": background_color,
            "enabled": "true",
            "outlinecolor": "0x000000FF",
            "gradient": "",
            "colormatrix": "",
        },
    )


def add_layout(root: ET.Element, spec: ListSpec, variant: str) -> None:
    paper = variant == "paper"
    width, height = (PAPER_WIDTH, PAPER_HEIGHT) if paper else (BRIDGE_WIDTH, BRIDGE_HEIGHT)
    layout = ET.SubElement(
        root,
        "Layout",
        {
            "combineReferences": "false",
            "width": str(width),
            "height": str(height),
            "buffer": "0",
            "Name": f"{spec.title} – {'PAPER Quadrat 45 mm' if paper else 'PRINT dunkel'}",
            "defaultCount": "1",
            "dpi": str(DPI),
            "drawBorder": str(paper).lower(),
        },
    )

    if paper:
        element(
            layout,
            name="Paper card label",
            kind="Text",
            variable="@[paper-label]",
            x=18,
            y=14,
            width=PAPER_WIDTH - 36,
            height=30,
            font_size=18,
            element_color="0x4A4A4AFF",
            horizontal_align=0,
        )
        element(
            layout,
            name="Formatted paper text",
            kind="FormattedText",
            variable="@[format-hell]",
            x=32,
            y=54,
            width=PAPER_WIDTH - 64,
            height=PAPER_HEIGHT - 86,
            font_size=round(spec.font_size * 0.70),
            element_color="0x252525FF",
            auto_scale=True,
        )
        element(
            layout,
            name="White background",
            kind="Text",
            variable="''",
            x=0,
            y=0,
            width=PAPER_WIDTH,
            height=PAPER_HEIGHT,
            background_color="0xFFFFFFFF",
        )
    else:
        element(
            layout,
            name="Formatted print fallback",
            kind="FormattedText",
            variable="#(if @[img] != #empty then #nodraw)#@[format-dunkel]",
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
            variable="#(if @[img] == #empty then #nodraw)#@[img]",
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
        ("exportNameFormat", f"wnd_{variant}_{spec.key}_#_"),
        ("exportRotation", "0"),
        ("exportTransparentBackground", "false"),
        ("exportPDFAsPageBack", "false"),
        ("exportWidth", str(width)),
        ("exportHeight", str(height)),
        ("zoom", "0.85" if paper else "0.65"),
        ("exportLayoutBorder", str(paper).lower()),
        ("exportLayoutBorderCrossSize", "0"),
    ):
        ET.SubElement(layout, tag).text = value


def write_project(variant: str) -> None:
    root = ET.Element(
        "Project",
        {
            "xmlns:xsd": "http://www.w3.org/2001/XMLSchema",
            "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        },
    )
    for spec in LIST_SPECS:
        add_layout(root, spec, variant)
    for tag, value in (
        ("translatorName", "Incept"),
        ("exportNameFormat", f"wnd_{variant}_#_"),
        ("defaultDefineReferenceType", "CSV"),
        ("overrideDefineReferenceName", ""),
        ("jsTildeMeansCode", "true"),
        ("jsKeepFunctions", "true"),
        ("jsSingleQuoteStartsCode", "true"),
        ("collapsedNodes", ""),
    ):
        ET.SubElement(root, tag).text = value
    ET.indent(root, space="  ")
    ET.ElementTree(root).write(PROJECT_PATHS[variant], encoding="utf-8", xml_declaration=True)


def build(text_version: str) -> None:
    counts: dict[str, int] = {}
    for spec in LIST_SPECS:
        counts[spec.key] = write_reference(spec, load_tsv(spec), text_version)
    write_project("print")
    write_project("paper")
    print(
        f"CardMaker-Projekte erzeugt: print + paper, vier Layouts je Projekt, "
        f"{sum(counts.values())} Karten, Textfassung {text_version}."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--text-version",
        choices=TEXT_VERSIONS,
        help="Überschreibt text-version.json für diesen Build.",
    )
    arguments = parser.parse_args()
    build(arguments.text_version or load_text_version())
