#!/usr/bin/env python3
"""Erzeugt das aktive CardMaker-Projekt fuer Lautspiele.

Jeder Bildsatz besitzt eine eigene Konfigurations-CSV. Das CardMaker-Layout
bestimmt den Spielmodus; die gewaehlte Symbol-CSV liefert Bildordner, Namen,
Groessenkorrektur sowie Start, Ende und Verschiebung fuer alle Modi.
"""

from __future__ import annotations

import csv
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT / "lautspiele.cmp"
EMPTY_DEFINES = ROOT / "lautspiele_defines.csv"
SYMBOL_ROOT = ROOT / "images" / "symbols"
DEFAULT_SYMBOL_SET = "k"
GRUSELINO_SYMBOLS = 8
GRUSELINO_BASE_CARDS = 4
DOBBLE_ORDER = 5
DOBBLE_SYMBOL_COUNT = DOBBLE_ORDER * DOBBLE_ORDER + DOBBLE_ORDER + 1

GRUSELINO_CARD_POSITIONS = (
    (101, 87, 335), (409, 181, 335), (689, 226, 335), (999, 96, 335),
    (150, 439, 335), (417, 483, 335), (712, 473, 335), (965, 413, 335),
)
GRUSELINO_PAPER_BASE_POSITIONS = (
    (-18, 81, 400), (309, -17, 335), (638, -15, 335), (786, 166, 335),
    (759, 409, 335), (523, 501, 335), (279, 471, 335), (15, 386, 335),
)
GRUSELINO_PAPER_SEARCH_POSITIONS = (
    (32, 54, 400), (315, 22, 400), (471, 158, 400), (684, 31, 400),
    (51, 361, 400), (327, 434, 400), (619, 391, 400), (247, 233, 335),
)

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
        "var available=String(symbol_available_map||'').split('|');"
        "var exists=available.length?available[id-1]==='1':id<=scales.length;"
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


def _gruselino_permutation(slot: int) -> str:
    return (
        "function shuffled(slot,seed){var p=[0,1,2,3,4,5,6,7];"
        "var state=(seed*1664525+1013904223)>>>0;"
        "for(var i=7;i>0;i--){state=(state*1664525+1013904223)>>>0;"
        "var j=state%(i+1);var t=p[i];p[i]=p[j];p[j]=t;}return p[slot];}"
        f"var shuffledLogical=shuffled({slot - 1},cardIndex);"
    )


def gruselino_variable(slot: int, base: bool) -> str:
    visibility = (
        f"if(cardIndex>{GRUSELINO_BASE_CARDS}||!exists)"
        if base else
        f"var hidden=cardIndex-{GRUSELINO_BASE_CARDS + 1};"
        f"if(cardIndex<={GRUSELINO_BASE_CARDS}||shuffledLogical===hidden||!exists)"
    )
    return (
        "(function(){"
        + _gruselino_permutation(slot)
        + _selection_prelude("shuffledLogical", "gruselino")
        + visibility + "{AddOverrideField('enabled','false');return '';}"
        + "AddOverrideField('enabled','true');"
        + _transform(True, True)
        + "return symbol_folder+'/'+file+'.png';})()"
    )


def gruselino_twirl_variable(slot: int) -> str:
    return (
        "(function(){"
        + _gruselino_permutation(slot)
        + f"var hidden=cardIndex-{GRUSELINO_BASE_CARDS + 1};"
          f"if(cardIndex<={GRUSELINO_BASE_CARDS}||shuffledLogical===hidden){{"
          "AddOverrideField('enabled','false');return '';}"
          "AddOverrideField('enabled','true');"
          "AddOverrideField('rotation',Math.floor(Math.random()*360).toString());"
          "return 'images/ui/twirl.png';})()"
    )


def memory_variable() -> str:
    return (
        "(function(){"
        + _selection_prelude("Math.floor((cardIndex-1)/2)", "memory")
        + "if(!exists){AddOverrideField('enabled','false');return '';}"
          "AddOverrideField('enabled','true');"
        + _transform(False, False)
        + "return symbol_folder+'/'+file+'.png';})()"
    )


def domino_variable(offset: int) -> str:
    # Die Bilddatei wird unveraendert geladen. Erst danach dreht CardMaker das
    # gesamte, mittig groessenkorrigierte Graphic-Element.
    return (
        "(function(){"
        + _selection_prelude(f"cardIndex-1+{offset}", "domino")
        + "if(!exists){AddOverrideField('enabled','false');return '';}"
          "AddOverrideField('enabled','true');"
        + _transform(False, True)
        + "return symbol_folder+'/'+file+'.png';})()"
    )


def _projective_plane(order: int) -> tuple[tuple[int, ...], ...]:
    cards: list[tuple[int, ...]] = []
    for slope in range(order):
        for intercept in range(order):
            points = tuple(
                x * order + ((slope * x + intercept) % order)
                for x in range(order)
            )
            cards.append((*points, order * order + slope))
    for x in range(order):
        points = tuple(x * order + y for y in range(order))
        cards.append((*points, order * order + order))
    cards.append(tuple(range(order * order, order * order + order + 1)))
    return tuple(cards)


# Das naechstkleinere perfekte System unterhalb der 8er-Karten ist die
# projektive Ebene der Ordnung 5: 31 Karten, 31 Symbole, 6 je Karte.
DOBBLE = _projective_plane(DOBBLE_ORDER)


def dobble_variable(slot: int) -> str:
    encoded = "[" + ",".join("[" + ",".join(map(str, row)) + "]" for row in DOBBLE) + "]"
    return (
        "(function(){"
        f"var matrix={encoded};"
        + _selection_prelude(f"matrix[cardIndex-1][{slot - 1}]", "dobble")
        + "if(!exists){AddOverrideField('enabled','false');return '';}"
          "AddOverrideField('enabled','true');"
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


def _reference(mode: str, set_name: str = DEFAULT_SYMBOL_SET) -> str:
    return f"{mode}_{set_name}.csv"


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
    layout = _layout(name, width, height, _reference("gruselino"), count=12)
    if name == "Gruselino Karten":
        base_positions = search_positions = GRUSELINO_CARD_POSITIONS
        base_bg, search_bg = "gruselino-bg1.png", "gruselino-bg2.png"
        ui_x, ui_y, ui_width, ui_height = 46, 41, 1395, 816
    else:
        base_positions = GRUSELINO_PAPER_BASE_POSITIONS
        search_positions = GRUSELINO_PAPER_SEARCH_POSITIONS
        base_bg, search_bg = "gruselino-bg2.png", "gruselino-bg1.png"
        ui_x, ui_y, ui_width, ui_height = 7, 6, 1104, 816
    base_graphics = [
        _element(f"Grundsymbol {slot}", "Graphic", x, y, size, size,
                 gruselino_variable(slot, True))
        for slot, (x, y, size) in enumerate(base_positions, start=1)
    ]
    search_graphics = [
        _element(f"Suchsymbol {slot}", "Graphic", x, y, size, size,
                 gruselino_variable(slot, False))
        for slot, (x, y, size) in enumerate(search_positions, start=1)
    ]
    twirls: list[ET.Element] = []
    if name == "Gruselino Papier":
        twirls = [
            _element(f"Twirl {slot}", "Graphic", x, y, size, size,
                     gruselino_twirl_variable(slot), opacity="105")
            for slot, (x, y, size) in enumerate(search_positions, start=1)
        ]
    bg_path = (
        f"cardIndex<={GRUSELINO_BASE_CARDS}?"
        f"'images/ui/{base_bg}':'images/ui/{search_bg}'"
    )
    bg = _element("Gruselino Background", "Graphic", ui_x, ui_y,
                  ui_width, ui_height, bg_path,
                  lockaspect="false")
    front: list[ET.Element] = []
    if name == "Gruselino Papier":
        front_path = (
            f"cardIndex<={GRUSELINO_BASE_CARDS}?"
            "'':'images/ui/gruselino_front.png'"
        )
        front = [_element("Gruselino Front", "Graphic", ui_x, ui_y,
                          ui_width, ui_height, front_path,
                          lockaspect="false", opacity="150")]
    _insert_elements(layout, [*front, *search_graphics, *base_graphics,
                              *twirls, bg, _background(width, height)])
    return layout


def _memory_layout() -> ET.Element:
    width, height = 590, 590
    layout = _layout("Memory Papier", width, height, _reference("memory"), count=20)
    symbol = _element("Memory Symbol", "Graphic", 85, 85, 420, 420,
                      memory_variable())
    frame = _element("Memory Rahmen", "Text", 12, 12, 566, 566, "''",
                     lockaspect="false", borderthickness="5",
                     bordercolor="0x5A7D8AFF", backgroundcolor="0xF7FBFFFF")
    _insert_elements(layout, [symbol, frame, _background(width, height)])
    return layout


def _domino_layout() -> ET.Element:
    width, height = 1181, 590
    layout = _layout("Domino Papier", width, height, _reference("domino"), count=10)
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
    layout = _layout("Dobble Papier", width, height, _reference("dobble"), count=31)
    specs = (
        (561, 145, 235), (285, 300, 230), (837, 300, 230),
        (285, 610, 230), (837, 610, 230), (561, 485, 270),
    )
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
        "symbol_set", "symbol_folder", "symbol_count", "symbol_names",
        "symbol_scale_map", "symbol_available_map",
        "gruselino_start", "gruselino_end", "gruselino_shift",
        "memory_start", "memory_end", "memory_shift",
        "domino_start", "domino_end", "domino_shift",
        "dobble_start", "dobble_end", "dobble_shift",
    ]
    row = {
        "symbol_set": folder.name,
        "symbol_folder": folder.relative_to(ROOT).as_posix(),
        "symbol_count": str(len(SYMBOL_NAMES)),
        "symbol_names": "|".join(SYMBOL_NAMES),
        "symbol_scale_map": "|".join(f"{scale:.4g}" for scale in SCALE_VALUES),
        "symbol_available_map": "",
        "gruselino_start": "1", "gruselino_end": "10", "gruselino_shift": "0",
        "memory_start": "1", "memory_end": "10", "memory_shift": "0",
        "domino_start": "1", "domino_end": "10", "domino_shift": "0",
        "dobble_start": "1", "dobble_end": str(DOBBLE_SYMBOL_COUNT), "dobble_shift": "0",
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
    row["symbol_count"] = str(len(names))
    availability_length = max(DOBBLE_SYMBOL_COUNT, len(names))
    row["symbol_available_map"] = "|".join(
        "1" if (folder / f"{index:02}.png").is_file() else "0"
        for index in range(1, availability_length + 1)
    )
    row["dobble_end"] = str(max(
        DOBBLE_SYMBOL_COUNT,
        int(row.get("dobble_end", str(DOBBLE_SYMBOL_COUNT)) or str(DOBBLE_SYMBOL_COUNT)),
    ))
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


def write_mode_reference_files() -> None:
    """Leitet CardMaker-Referenzen mit technischem Count aus den Mastern ab."""
    for master in sorted(ROOT.glob("symbols_*.csv")):
        if master.name.endswith("_sources.csv"):
            continue
        with master.open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if len(rows) != 1 or not rows[0].get("symbol_set"):
            continue
        row = rows[0]
        set_name = row["symbol_set"]
        counts = {
            "gruselino": 12,
            "memory": 2 * (int(row["memory_end"]) - int(row["memory_start"]) + 1),
            "domino": int(row["domino_end"]) - int(row["domino_start"]) + 1,
            "dobble": len(DOBBLE),
        }
        for mode, count in counts.items():
            target = ROOT / f"{mode}_{set_name}.csv"
            fields = ["Count", *row.keys()]
            with target.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow({"Count": count, **row})


def write_csv_files() -> None:
    _ensure_symbol_sets()
    write_mode_reference_files()
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
        _memory_layout(),
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
