#!/usr/bin/env python3
"""Rebuild the Emotron SVG from the checked-in OpenMoji vectors."""

from __future__ import annotations

import argparse
import copy
import math
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


SVG_NS = "http://www.w3.org/2000/svg"
NS = {"svg": SVG_NS}
ET.register_namespace("", SVG_NS)

HERE = Path(__file__).resolve()
PROJECT = HERE.parents[2]
SVG_FILE = PROJECT / "files" / "emotron.svg"
ASSET_ROOT = PROJECT / "files" / "openmoji"

CENTER_X = 357.5
CENTER_Y = 362.5
EMOJI_SIZE = 46.0
PRIMARY_RADII = (78.0, 143.0, 208.0)
COMBO_RADIUS = 280.0


@dataclass(frozen=True)
class Slot:
    asset: str
    code: str
    name: str
    angle: float
    radius: float
    kind: str

    @property
    def center(self) -> tuple[float, float]:
        radians = math.radians(self.angle)
        return (
            CENTER_X + math.cos(radians) * self.radius,
            CENTER_Y + math.sin(radians) * self.radius,
        )


BRANCHES = (
    (-135.0, (("3_freude_1_zufrieden.svg", "1F60C", "zufrieden"),
              ("3_freude_2_froehlich.svg", "1F60A", "fröhlich"),
              ("3_freude_3_begeistert.svg", "1F602", "begeistert"))),
    (-90.0, (("2_zuneigung_1_freundlich.svg", "1F609", "freundlich"),
             ("2_zuneigung_2_zugewandt.svg", "1F917", "zugewandt"),
             ("2_zuneigung_3_verbunden.svg", "1F970", "verbunden"))),
    (-45.0, (("1_neugier_1_interessiert.svg", "1F60F", "interessiert"),
             ("1_neugier_2_neugierig.svg", "1FAE2", "neugierig"),
             ("1_neugier_3_fasziniert.svg", "1F929", "fasziniert"))),
    (0.0, (("8_angst_1_besorgt.svg", "1F61F", "besorgt"),
           ("8_angst_2_aengstlich.svg", "1F628", "ängstlich"),
           ("8_angst_3_panisch.svg", "1F631", "panisch"))),
    (45.0, (("7_trauer_1_bedrueckt.svg", "1F641", "bedrückt"),
            ("7_trauer_2_traurig.svg", "1F622", "traurig"),
            ("7_trauer_3_trauernd.svg", "1F62D", "trauernd"))),
    (90.0, (("6_scham_1_verlegen.svg", "1F605", "verlegen"),
            ("6_scham_2_befangen.svg", "1F633", "befangen"),
            ("6_scham_3_beschaemt.svg", "1FAE3", "beschämt"))),
    (135.0, (("5_ekel_1_abgeneigt.svg", "1F615", "abgeneigt"),
             ("5_ekel_2_angeekelt.svg", "1F616", "angeekelt"),
             ("5_ekel_3_uebel.svg", "1F922", "übel"))),
    (180.0, (("4_wut_1_gereizt.svg", "1F612", "gereizt"),
             ("4_wut_2_veraergert.svg", "1F620", "verärgert"),
             ("4_wut_3_wuetend.svg", "1F92C", "wütend"))),
)

COMBINATIONS = (
    (-112.5, "2-3_dankbarkeit.svg", "1F979", "Dankbarkeit"),
    (-67.5, "1-2_bewunderung.svg", "1F60D", "Bewunderung"),
    (-22.5, "8-1_ueberraschung.svg", "1F632", "Überraschung"),
    (22.5, "7-8_aufgeben.svg", "1F629", "Aufgeben"),
    (67.5, "6-7_reue.svg", "1F61E", "Reue"),
    (112.5, "5-6_unbehagen.svg", "1F62C", "Unbehagen"),
    (157.5, "4-5_abwertung.svg", "1F644", "Abwertung"),
    (-157.5, "3-4_streitlust.svg", "1F608", "Streitlust"),
)

PALETTE = {
    "W": "#ef938b",
    "E": "#c2a8dc",
    "N": "#f4b56d",
    "S": "#bfe36f",
    "NW": "#f5df6f",
    "NE": "#83d4cf",
    "SE": "#6381d7",
    "SW": "#6f9f68",
}

# Existing Illustrator path order, paired with sector and radial strength.
AREA_ORDER = (
    ("W", 1.0), ("E", 1.0), ("E", .68), ("E", .43), ("E", .25),
    ("W", .68), ("W", .43), ("W", .25),
    ("N", .25), ("N", .43), ("N", .68), ("N", 1.0),
    ("S", 1.0), ("S", .68), ("S", .43), ("S", .25),
    ("NW", .25), ("NW", .43), ("NW", .68),
    ("SW", 1.0), ("SW", .68), ("SW", .43), ("SW", .25),
    ("SE", 1.0), ("SE", .68), ("SE", .43), ("SE", .25),
    ("NE", 1.0), ("NE", .25), ("NE", .43), ("NE", .68),
    ("NW", 1.0),
)


def q(tag: str) -> str:
    return f"{{{SVG_NS}}}{tag}"


def slots() -> list[Slot]:
    result = [Slot("0_neutral.svg", "1F610", "ausgeglichen", 0.0, 0.0, "neutral")]
    for angle, branch in BRANCHES:
        for radius, (asset, code, name) in zip(PRIMARY_RADII, branch):
            result.append(Slot(asset, code, name, angle, radius, "base"))
    for angle, asset, code, name in COMBINATIONS:
        result.append(Slot(asset, code, name, angle, COMBO_RADIUS, "combo"))
    return result


SLOTS = slots()


def by_id(root: ET.Element, element_id: str) -> ET.Element | None:
    return root.find(f".//*[@id='{element_id}']")


def mix_white(hex_color: str, strength: float) -> str:
    channels = [int(hex_color[index:index + 2], 16) for index in (1, 3, 5)]
    mixed = [round(255 + (channel - 255) * strength) for channel in channels]
    return "#" + "".join(f"{channel:02x}" for channel in mixed)


def color_areas(areas: ET.Element, faded: bool) -> None:
    paths = areas.findall("./svg:path", NS)
    if len(paths) != len(AREA_ORDER):
        raise ValueError(f"Color hat {len(paths)} statt 32 Flächen")
    multiplier = .3 if faded else 1.0
    for path, (sector, strength) in zip(paths, AREA_ORDER):
        path.set("style", f"fill:{mix_white(PALETTE[sector], strength * multiplier)}")


def safe_id(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "_", value)


def prefix_ids(element: ET.Element, prefix: str) -> None:
    id_map: dict[str, str] = {}
    for node in element.iter():
        old_id = node.get("id")
        if old_id:
            new_id = f"{prefix}_{safe_id(old_id)}"
            id_map[old_id] = new_id
            node.set("id", new_id)
    if not id_map:
        return
    for node in element.iter():
        for key, value in list(node.attrib.items()):
            for old_id, new_id in id_map.items():
                value = value.replace(f"url(#{old_id})", f"url(#{new_id})")
                if value == f"#{old_id}":
                    value = f"#{new_id}"
            node.set(key, value)


def emoji_group(variant: str, *, faded: bool = False) -> ET.Element:
    suffix = "color_faded" if faded else variant
    data_name = "emoji_svg color faded" if faded else f"emoji_svg {variant}"
    group = ET.Element(q("g"), {
        "id": f"emoji_x5F_svg_{suffix}",
        "data-name": data_name,
    })
    if variant == "sw" or faded:
        group.set("style", "display:none")
    if faded:
        group.set("opacity", ".3")

    scale = EMOJI_SIZE / 72.0
    for index, slot in enumerate(SLOTS):
        asset_file = ASSET_ROOT / variant / slot.asset
        asset_root = ET.parse(asset_file).getroot()
        x, y = slot.center
        placed = ET.SubElement(group, q("g"), {
            "id": f"emotron_{suffix}_{index:02d}_{safe_id(slot.name.lower())}",
            "data-asset": slot.asset,
            "data-code": slot.code,
            "data-name": slot.name,
            "data-kind": slot.kind,
            "transform": f"translate({x - EMOJI_SIZE / 2:.3f} {y - EMOJI_SIZE / 2:.3f}) scale({scale:.8f})",
        })
        for child in list(asset_root):
            placed.append(copy.deepcopy(child))
        prefix_ids(placed, f"emo_{suffix}_{index:02d}")
    return group


def text_group(element_id: str, data_name: str, mode: str) -> ET.Element:
    group = ET.Element(q("g"), {"id": element_id, "data-name": data_name})
    if mode == "names":
        group.set("style", "display:none")

    for index, slot in enumerate(SLOTS):
        x, y = slot.center
        if mode != "names":
            y += 30.0 if slot.kind != "combo" else 28.0
        style = "font-family:Tahoma,sans-serif;font-size:11px;text-anchor:middle;fill:#1d1d1b"
        if mode == "back":
            style += ";stroke:#fff;stroke-width:3px;stroke-linejoin:round;paint-order:stroke"
        text = ET.SubElement(group, q("text"), {
            "id": f"{element_id}_{index:02d}",
            "x": f"{x:.3f}",
            "y": f"{y:.3f}",
            "style": style,
            "data-code": slot.code,
        })
        text.text = slot.name
    return group


def rebuild() -> None:
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    tree = ET.parse(SVG_FILE, parser=parser)
    root = tree.getroot()
    axes = by_id(root, "achsen")
    areas = by_id(root, "areas_x5F_colors")
    if axes is None or areas is None:
        raise ValueError("achsen oder areas_x5F_colors fehlt")

    color_areas(areas, faded=False)
    areas.set("data-name", "Color")

    faded_areas = copy.deepcopy(areas)
    faded_areas.set("id", "areas_x5F_colors_faded")
    faded_areas.set("data-name", "Color faded")
    faded_areas.set("style", "display:none")
    color_areas(faded_areas, faded=True)

    preserved = []
    replaced_ids = {
        "areas_x5F_colors", "areas_x5F_colors_faded",
        "emoji_x5F_svg_sw", "emoji_x5F_svg_color", "emoji_x5F_svg_color_faded",
        "names", "names_for_emoji", "names_for_emoji_-_front",
    }
    for child in list(axes):
        if child.get("id") not in replaced_ids:
            if child.get("id") == "orientierung":
                child.set("style", "display:none")
            preserved.append(child)

    axes[:] = [
        areas,
        faded_areas,
        emoji_group("sw"),
        emoji_group("color", faded=True),
        emoji_group("color"),
        text_group("names", "names", "names"),
        text_group("names_for_emoji", "names for emoji", "back"),
        text_group("names_for_emoji_-_front", "names for emoji - front", "front"),
        *preserved,
    ]

    ET.indent(tree, space="  ")
    tree.write(SVG_FILE, encoding="utf-8", xml_declaration=True)


def validate() -> None:
    root = ET.parse(SVG_FILE).getroot()
    expected_names = [slot.name for slot in SLOTS]
    expected_codes = [slot.code for slot in SLOTS]

    if len(SLOTS) != 33 or len(set(expected_names)) != 33 or len(set(expected_codes)) != 33:
        raise ValueError("Mapping enthält doppelte Namen oder OpenMoji-Codes")
    if root.findall(".//svg:image", NS):
        raise ValueError("SVG enthält noch ein Bild oder eine externe Bildverknüpfung")

    for group_id in ("emoji_x5F_svg_color", "emoji_x5F_svg_sw", "emoji_x5F_svg_color_faded"):
        group = by_id(root, group_id)
        if group is None:
            raise ValueError(f"Gruppe fehlt: {group_id}")
        children = [child for child in list(group) if child.get("data-code")]
        codes = [child.get("data-code") for child in children]
        if codes != expected_codes:
            raise ValueError(f"Falsche OpenMoji-Reihenfolge in {group_id}")

    for group_id in ("names", "names_for_emoji", "names_for_emoji_-_front"):
        group = by_id(root, group_id)
        if group is None:
            raise ValueError(f"Gruppe fehlt: {group_id}")
        names = [node.text for node in group.findall("./svg:text", NS)]
        if names != expected_names:
            raise ValueError(f"Falsche Namen in {group_id}")

    for group_id in ("areas_x5F_colors", "areas_x5F_colors_faded"):
        group = by_id(root, group_id)
        if group is None or len(group.findall("./svg:path", NS)) != 32:
            raise ValueError(f"Farbflächen fehlen in {group_id}")

    ids = [node.get("id") for node in root.iter() if node.get("id")]
    duplicates = sorted({element_id for element_id in ids if ids.count(element_id) > 1})
    if duplicates:
        raise ValueError("Doppelte SVG-IDs: " + ", ".join(duplicates[:8]))

    print("OK: 33 OpenMoji je Variante, 33 eindeutige Namen, 32 Farbflächen je Ebene, keine Bildverknüpfung")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Nur die fertige SVG prüfen")
    args = parser.parse_args()
    if not args.check:
        rebuild()
    validate()


if __name__ == "__main__":
    main()
