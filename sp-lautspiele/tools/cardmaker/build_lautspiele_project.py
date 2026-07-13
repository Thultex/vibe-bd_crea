#!/usr/bin/env python3
"""Erzeugt das aktive CardMaker-Projekt fuer Lautspiele.

Alle Karten benutzen dieselbe kleine Konfigurations-CSV. Symbolauswahl,
Groessenkorrektur, Ausblendung, Rotation und Positionierung werden zur Laufzeit
in den CardMaker-Elementen berechnet.
"""

from __future__ import annotations

import csv
import math
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROJECT = ROOT / "lautspiele.cmp"
CONFIG = ROOT / "lautspiele.csv"
DEFINES = ROOT / "lautspiele_defines.csv"

SCALE_VALUES = [
    0.91, 0.88, 0.91, 0.91, 0.94,
    0.90, 1.03, 0.97, 0.97, 0.97,
]
SYMBOL_NAMES = [
    "Käse", "Bankkarte", "Stecker", "Katze", "Keks",
    "Ei", "Kuh", "Mädchen", "Mädchen (Duplikat 1)",
    "Mädchen (Duplikat 2)",
]


def _element(name: str, kind: str, x: int, y: int, width: int, height: int,
             variable: str, **overrides: str) -> ET.Element:
    attrs = {
        "variable": variable,
        "type": kind,
        "x": str(x),
        "y": str(y),
        "width": str(width),
        "height": str(height),
        "borderthickness": "0",
        "autoscalefont": "false",
        "lockaspect": "true" if kind == "Graphic" else "false",
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
        "font": "Arial;12;0;0;0;0",
        "elementcolor": "0x000000FF",
        "bordercolor": "0x00000000",
        "backgroundcolor": "0x00000000",
        "enabled": "true",
        "outlinecolor": "0x000000FF",
        "gradient": "",
        "colormatrix": "",
    }
    attrs.update(overrides)
    return ET.Element("Element", attrs)


def _scale_array() -> str:
    values = ["1"]
    values.extend(f"parseFloat(symbol_{idx:02}__scale)||1" for idx in range(1, 51))
    return "[" + ",".join(values) + "]"


def _selection_prelude(slot_expression: str) -> str:
    return (
        "var start=parseInt(symbol_start,10)||1;"
        "var end=parseInt(symbol_end,10)||start;"
        "var n=Math.max(1,end-start+1);"
        "var shift=parseInt(symbol_shift,10)||0;"
        "function mod(v,m){return ((v%m)+m)%m;}"
        f"var logical={slot_expression};"
        "var id=start+mod(shift+logical,n);"
        f"var scales={_scale_array()};"
        "var correction=scales[id]||1;"
        "var file=id.toString().padStart(2,'0');"
    )


def _transform(random_size: bool, random_rotation: bool) -> str:
    size_random = "*(0.95+Math.random()*0.10)" if random_size else ""
    rotation = (
        "AddOverrideField('rotation',Math.floor(Math.random()*360).toString());"
        if random_rotation else "AddOverrideField('rotation','0');"
    )
    return (
        f"var factor=correction{size_random};"
        "var w=Math.round(Element.width*factor);"
        "var h=Math.round(Element.height*factor);"
        "AddOverrideField('x',Math.round(Element.x+(Element.width-w)/2).toString());"
        "AddOverrideField('y',Math.round(Element.y+(Element.height-h)/2).toString());"
        "AddOverrideField('width',w.toString());"
        "AddOverrideField('height',h.toString());"
        + rotation
    )


def gruselino_variable(slot: int) -> str:
    return (
        "(function(){"
        + _selection_prelude(str(slot - 1))
        + f"var hidden=cardIndex-1;if(cardIndex>1&&hidden==={slot}){{"
          "AddOverrideField('enabled','false');return ''; }"
          "AddOverrideField('enabled','true');"
        + _transform(True, True)
        + "return symbol_folder+'/'+file+'.png';})()"
    )


def domino_variable(offset: int) -> str:
    # Die Bilddatei wird unveraendert geladen. Erst danach dreht CardMaker das
    # gesamte, mittig groessenkorrigierte Graphic-Element.
    return (
        "(function(){"
        + _selection_prelude(f"cardIndex-1+{offset}")
        + _transform(False, True)
        + "return symbol_folder+'/'+file+'.png';})()"
    )


DOBBLE = (
    (0, 1, 2), (0, 3, 4), (0, 5, 6),
    (1, 3, 5), (1, 4, 6), (2, 3, 6), (2, 4, 5),
)


def dobble_variable(slot: int) -> str:
    encoded = "[" + ",".join("[" + ",".join(map(str, row)) + "]" for row in DOBBLE) + "]"
    return (
        "(function(){"
        f"var matrix={encoded};"
        + _selection_prelude(f"matrix[cardIndex-1][{slot - 1}]")
        + _transform(True, True)
        + "return symbol_folder+'/'+file+'.png';})()"
    )


def _layout(name: str, width: int, height: int, count: int = 1) -> ET.Element:
    layout = ET.Element("Layout", {
        "combineReferences": "false", "width": str(width), "height": str(height),
        "buffer": "0", "Name": name, "defaultCount": str(count),
        "dpi": "300", "drawBorder": "false",
    })
    ET.SubElement(layout, "Reference", {"RelativePath": "lautspiele.csv", "Default": "true"})
    for tag, value in (
        ("exportNameFormat", ""), ("exportRotation", "0"),
        ("exportTransparentBackground", "false"), ("exportPDFAsPageBack", "false"),
        ("exportWidth", "0"), ("exportHeight", "0"), ("zoom", "0.65"),
        ("exportLayoutBorder", "false"), ("exportLayoutBorderCrossSize", "0"),
    ):
        ET.SubElement(layout, tag).text = value
    return layout


def _insert_elements(layout: ET.Element, elements: list[ET.Element]) -> None:
    reference = layout.find("Reference")
    assert reference is not None
    index = list(layout).index(reference)
    for element in elements:
        layout.insert(index, element)
        index += 1


def _background(width: int, height: int, name: str = "White Background") -> ET.Element:
    return _element(name, "Text", 0, 0, width, height, "''",
                    lockaspect="false", backgroundcolor="0xFFFFFFFF")


def _gruselino_layout(name: str, width: int, height: int) -> ET.Element:
    layout = _layout(name, width, height)
    cx, cy = width / 2, height / 2
    radius_x, radius_y = width * 0.39, height * 0.34
    size = round(min(width, height) * 0.25)
    graphics: list[ET.Element] = []
    for slot in range(1, 11):
        angle = math.radians(-108 + (slot - 1) * 36)
        center_x = cx + math.cos(angle) * radius_x
        center_y = cy + math.sin(angle) * radius_y
        graphics.append(_element(
            f"Symbol {slot}", "Graphic", round(center_x - size / 2),
            round(center_y - size / 2), size, size, gruselino_variable(slot),
        ))
    bg_path = "cardIndex===1?'images/ui/gruselino-bg2.png':'images/ui/gruselino-bg1.png'"
    bg = _element("Gruselino Background", "Graphic", 0, 0, width, height, bg_path,
                  lockaspect="false")
    _insert_elements(layout, [*graphics, bg, _background(width, height)])
    return layout


def _domino_layout() -> ET.Element:
    width, height = 1181, 590
    layout = _layout("Domino Papier", width, height)
    size = 420
    graphics = [
        _element("Domino Symbol links", "Graphic", 88, 85, size, size, domino_variable(0)),
        _element("Domino Symbol rechts", "Graphic", 673, 85, size, size, domino_variable(1)),
    ]
    divider = _element("Domino Trennlinie", "Text", 586, 45, 9, 500, "''",
                       lockaspect="false", backgroundcolor="0x333333FF")
    frame = _element("Domino Rahmen", "Text", 20, 12, 1141, 566, "''",
                     lockaspect="false", borderthickness="5",
                     bordercolor="0x333333FF", backgroundcolor="0xF7FBFFFF")
    _insert_elements(layout, [*graphics, divider, frame, _background(width, height)])
    return layout


def _dobble_layout() -> ET.Element:
    width, height = 1122, 826
    layout = _layout("Dobble Papier", width, height)
    specs = ((561, 205, 260), (325, 555, 285), (797, 555, 285))
    graphics = [
        _element(f"Dobble Symbol {slot}", "Graphic", round(x - size / 2),
                 round(y - size / 2), size, size, dobble_variable(slot))
        for slot, (x, y, size) in enumerate(specs, start=1)
    ]
    card = _element("Dobble Kartenflaeche", "Text", 20, 12, 1082, 802, "''",
                    lockaspect="false", borderthickness="5",
                    bordercolor="0x5A7D8AFF", backgroundcolor="0xF7FBFFFF")
    _insert_elements(layout, [*graphics, card, _background(width, height)])
    return layout


def write_csv_files() -> None:
    with CONFIG.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Count", "allowed_layout", "mode", "symbol_folder",
                         "symbol_start", "symbol_end", "symbol_shift"])
        writer.writerow([11, "Gruselino Karten;Gruselino Papier", "gruselino",
                         "images/symbols/default", 1, 10, 0])
        writer.writerow([10, "Domino Papier", "domino",
                         "images/symbols/default", 1, 10, 0])
        writer.writerow([7, "Dobble Papier", "dobble",
                         "images/symbols/default", 1, 10, 0])

    with DEFINES.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["define", "scale", "name"])
        for symbol_id in range(1, 51):
            scale = SCALE_VALUES[symbol_id - 1] if symbol_id <= len(SCALE_VALUES) else 1.0
            name = SYMBOL_NAMES[symbol_id - 1] if symbol_id <= len(SYMBOL_NAMES) else f"Symbol {symbol_id:02}"
            writer.writerow([f"symbol_{symbol_id:02}", f"{scale:.2f}", name])


def build() -> None:
    write_csv_files()
    root = ET.Element("Project", {
        "xmlns:xsd": "http://www.w3.org/2001/XMLSchema",
        "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    })
    root.extend([
        _gruselino_layout("Gruselino Karten", 1488, 897),
        _gruselino_layout("Gruselino Papier", 1122, 826),
        _domino_layout(),
        _dobble_layout(),
    ])
    for tag, value in (
        ("translatorName", "JavaScript"), ("exportNameFormat", "##_#L"),
        ("defaultDefineReferenceType", "CSV"), ("overrideDefineReferenceName", ""),
        ("jsTildeMeansCode", "true"), ("jsKeepFunctions", "true"),
        ("jsSingleQuoteStartsCode", "true"), ("collapsedNodes", ""),
    ):
        ET.SubElement(root, tag).text = value
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(PROJECT, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    build()
