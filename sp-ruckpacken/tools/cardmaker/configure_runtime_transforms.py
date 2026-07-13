#!/usr/bin/env python3
"""Konfiguriert das MPC-Jumbo-Layout und CardMaker-Laufzeittransformationen."""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ORIGINAL_WIDTH = 673
ORIGINAL_HEIGHT = 1039
FULL_BLEED_WIDTH = 1120
FULL_BLEED_HEIGHT = 1570
CUT_WIDTH = 1050
CUT_HEIGHT = 1500
CUT_INSET = 35
SAFE_INSET = 72
SAFE_WIDTH = 975
SAFE_HEIGHT = 1425

# Mittelpunktkoordinaten und Grundgrößen des abgestimmten 57-x-88-mm-Layouts.
ORIGINAL_SPECS = {
    1: (337, 100, 135),
    2: (170, 241, 157),
    3: (504, 241, 157),
    4: (100, 500, 135),
    5: (337, 500, 189),
    6: (574, 500, 135),
    7: (170, 760, 157),
    8: (504, 760, 157),
    9: (337, 940, 135),
}


def _helper_element(name: str, x: int, y: int, width: int, height: int, *,
                    border: int, border_color: str, background_color: str,
                    editor_only: bool = False) -> ET.Element:
    variable = "#(if ![exporting] == 1 then $[enabled:false])#" if editor_only else ""
    return ET.Element(
        "Element",
        {
            "variable": variable,
            "type": "Text",
            "x": str(x),
            "y": str(y),
            "width": str(width),
            "height": str(height),
            "borderthickness": str(border),
            "autoscalefont": "false",
            "lockaspect": "false",
            "keeporiginalsize": "false",
            "centerimageonorigin": "false",
            "outlinethickness": "0",
            "rotation": "0",
            "horizontalalign": "0",
            "verticalalign": "0",
            "colortype": "0",
            "opacity": "255",
            "tilesize": "",
            "mirrortype": "0",
            "imagemasksurface": "false",
            "lineheight": "14",
            "wordspace": "0",
            "justifiedtext": "false",
            "name": name,
            "font": "Arial;12;0;0;0;0",
            "elementcolor": "0x000000FF",
            "bordercolor": border_color,
            "backgroundcolor": background_color,
            "enabled": "true",
            "outlinecolor": "0x000000FF",
            "gradient": "",
            "colormatrix": "",
        },
    )


def configure(project: Path) -> None:
    tree = ET.parse(project)
    root = tree.getroot()
    root.set("xmlns:xsd", "http://www.w3.org/2001/XMLSchema")
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    layout = root.find("Layout")
    if layout is None:
        raise RuntimeError("CardMaker-Layout fehlt.")

    graphics = [element for element in layout.findall("Element") if element.get("type") == "Graphic"]
    by_name = {element.get("name"): element for element in graphics}
    if set(by_name) != {f"Symbol {slot}" for slot in range(1, 10)}:
        raise RuntimeError("Erwartet werden die Graphic-Elemente Symbol 1 bis Symbol 9.")

    scale_x = CUT_WIDTH / ORIGINAL_WIDTH
    scale_y = CUT_HEIGHT / ORIGINAL_HEIGHT
    symbol_scale = min(scale_x, scale_y)
    old_center_x = ORIGINAL_WIDTH / 2
    old_center_y = ORIGINAL_HEIGHT / 2
    new_center_x = FULL_BLEED_WIDTH / 2
    new_center_y = FULL_BLEED_HEIGHT / 2

    ordered_graphics = []
    for slot in range(1, 10):
        element = by_name[f"Symbol {slot}"]
        old_x, old_y, old_size = ORIGINAL_SPECS[slot]
        x = round(new_center_x + (old_x - old_center_x) * scale_x)
        y = round(new_center_y + (old_y - old_center_y) * scale_y)
        base_size = round(old_size * symbol_scale)
        minimum = round(base_size * 0.95)
        maximum = round(base_size * 1.05)
        element.set("x", str(x))
        element.set("y", str(y))
        element.set("width", str(base_size))
        element.set("height", str(base_size))
        element.set("centerimageonorigin", "true")
        element.set(
            "variable",
            f"@[slot_{slot:02}]"
            "$[rotation:#random;0;359#]"
            f"$[width:#random;{minimum};{maximum}#]"
            f"$[height:#random;{minimum};{maximum}#]",
        )
        element.set("rotation", "0")
        ordered_graphics.append(element)

    layout.set("width", str(FULL_BLEED_WIDTH))
    layout.set("height", str(FULL_BLEED_HEIGHT))
    layout.set("Name", "Ruckpacken MPC Jumbo 3.5x5")
    layout.set("dpi", "300")

    safe_guide = _helper_element(
        "Safe Area (editor only)", SAFE_INSET, SAFE_INSET, SAFE_WIDTH, SAFE_HEIGHT,
        border=3, border_color="0xFF0000FF", background_color="0x00000000", editor_only=True,
    )
    cut_guide = _helper_element(
        "Cut Area (editor only)", CUT_INSET, CUT_INSET, CUT_WIDTH, CUT_HEIGHT,
        border=3, border_color="0xFF0000FF", background_color="0x00000000", editor_only=True,
    )
    background = _helper_element(
        "White Background", 0, 0, FULL_BLEED_WIDTH, FULL_BLEED_HEIGHT,
        border=0, border_color="0x00000000", background_color="0xFFFFFFFF",
    )

    for element in layout.findall("Element"):
        layout.remove(element)
    # CardMaker zeichnet Elemente in umgekehrter XML-Reihenfolge.
    # Guides liegen oben, der weiße Hintergrund ganz unten.
    for index, element in enumerate([safe_guide, cut_guide, *ordered_graphics, background]):
        layout.insert(index, element)

    ET.indent(tree, space="  ")
    tree.write(project, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    configure(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("ruckpacken.cmp"))
