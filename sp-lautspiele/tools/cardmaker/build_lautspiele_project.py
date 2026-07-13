#!/usr/bin/env python3
"""Erzeugt das aktive CardMaker-Projekt fuer Lautspiele.

Jeder Bildsatz besitzt eine eigene Konfigurations-CSV. Das CardMaker-Layout
bestimmt den Spielmodus; die gewaehlte Symbol-CSV liefert Bildordner, Namen,
Groessenkorrektur sowie Start, Ende und Verschiebung fuer alle Modi.
"""

from __future__ import annotations

import csv
import math
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROJECT = ROOT / "lautspiele.cmp"
EMPTY_DEFINES = ROOT / "lautspiele_defines.csv"
SYMBOL_ROOT = ROOT / "images" / "symbols"
DEFAULT_SYMBOL_REFERENCE = "symbols_k.csv"

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


def _selection_prelude(slot_expression: str, mode: str) -> str:
    return (
        f"var start=parseInt({mode}_start,10)||1;"
        f"var end=parseInt({mode}_end,10)||start;"
        "var n=Math.max(1,end-start+1);"
        f"var shift=parseInt({mode}_shift,10)||0;"
        "function mod(v,m){return ((v%m)+m)%m;}"
        f"var logical={slot_expression};"
        "var id=start+mod(shift+logical,n);"
        "var scales=String(symbol_scale_map||'1').split('|').map(function(v){return parseFloat(v)||1;});"
        "var correction=scales[id-1]||1;"
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
        + _selection_prelude(str(slot - 1), "gruselino")
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
        + _selection_prelude(f"cardIndex-1+{offset}", "domino")
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
        + _selection_prelude(f"matrix[cardIndex-1][{slot - 1}]", "dobble")
        + _transform(True, True)
        + "return symbol_folder+'/'+file+'.png';})()"
    )


def _layout(name: str, width: int, height: int, reference: str, count: int = 1) -> ET.Element:
    layout = ET.Element("Layout", {
        "combineReferences": "false", "width": str(width), "height": str(height),
        "buffer": "0", "Name": name, "defaultCount": str(count),
        "dpi": "300", "drawBorder": "false",
    })
    ET.SubElement(layout, "Reference", {"RelativePath": reference, "Default": "true"})
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
    layout = _layout(name, width, height, DEFAULT_SYMBOL_REFERENCE, count=11)
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
    layout = _layout("Domino Papier", width, height, DEFAULT_SYMBOL_REFERENCE, count=10)
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
    layout = _layout("Dobble Papier", width, height, DEFAULT_SYMBOL_REFERENCE, count=7)
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


def _symbol_config_path(folder: Path) -> Path:
    return ROOT / f"symbols_{folder.name}.csv"


def _write_symbol_config(folder: Path) -> None:
    """Schreibt genau eine CardMaker-Datenzeile fuer einen Bildsatz."""
    path = _symbol_config_path(folder)
    fields = [
        "symbol_set", "symbol_folder", "symbol_names", "symbol_scale_map",
        "gruselino_start", "gruselino_end", "gruselino_shift",
        "domino_start", "domino_end", "domino_shift",
        "dobble_start", "dobble_end", "dobble_shift",
    ]
    row = {
        "symbol_set": folder.name,
        "symbol_folder": folder.relative_to(ROOT).as_posix(),
        "symbol_names": "|".join(SYMBOL_NAMES),
        "symbol_scale_map": "|".join(f"{scale:.4g}" for scale in SCALE_VALUES),
        "gruselino_start": "1", "gruselino_end": "10", "gruselino_shift": "0",
        "domino_start": "1", "domino_end": "10", "domino_shift": "0",
        "dobble_start": "1", "dobble_end": "10", "dobble_shift": "0",
    }
    if path.exists():
        with path.open(encoding="utf-8-sig", newline="") as handle:
            existing_rows = list(csv.DictReader(handle))
        if existing_rows and "symbol_scale_map" in existing_rows[0]:
            for field in fields:
                if existing_rows[0].get(field, "").strip():
                    row[field] = existing_rows[0][field].strip()
        elif existing_rows and "symbol_id" in existing_rows[0]:
            # Einmalige Migration der zuvor zeilenweisen Symboltabelle.
            ordered = sorted(existing_rows, key=lambda item: int(item["symbol_id"]))
            row["symbol_names"] = "|".join(item["symbol_name"] for item in ordered)
            row["symbol_scale_map"] = "|".join(
                f"{float(item['scale']):.4g}" for item in ordered
            )
    names = row["symbol_names"].split("|")
    scales = row["symbol_scale_map"].split("|")
    if names and not names[0]:
        names = names[1:]
    if len(scales) == len(names) + 1:
        scales = scales[1:]
    row["symbol_names"] = "|".join(names)
    row["symbol_scale_map"] = "|".join(scales)
    row["symbol_set"] = folder.name
    row["symbol_folder"] = folder.relative_to(ROOT).as_posix()
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerow(row)


def _ensure_symbol_sets() -> None:
    """Stellt Default und den vorhandenen K-Laut-Satz samt Manifest bereit."""
    default = SYMBOL_ROOT / "default"
    k_folder = SYMBOL_ROOT / "k"
    default.mkdir(parents=True, exist_ok=True)
    k_folder.mkdir(parents=True, exist_ok=True)
    for source in sorted(default.glob("*.png")):
        target = k_folder / source.name
        if not target.exists():
            shutil.copy2(source, target)
    _write_symbol_config(default)
    _write_symbol_config(k_folder)


def write_csv_files() -> None:
    _ensure_symbol_sets()
    # CardMaker sucht automatisch <projekt>_defines.csv. Eine reine Kopfzeile
    # verhindert die irreführende "No defines found"-Meldung, enthält aber
    # bewusst keine globalen Daten und kann daher nichts doppelt definieren.
    with EMPTY_DEFINES.open("w", encoding="utf-8", newline="") as handle:
        csv.writer(handle).writerow(["define", "value"])


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
