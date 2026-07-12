#!/usr/bin/env python3
"""Konfiguriert CardMaker-Zufallstransformationen direkt im CMP-Projekt."""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path


SIZE_RANGES = {
    151: (143, 159),
    175: (166, 184),
    211: (200, 222),
}


def configure(project: Path) -> None:
    tree = ET.parse(project)
    root = tree.getroot()
    root.set("xmlns:xsd", "http://www.w3.org/2001/XMLSchema")
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    layout = root.find("Layout")
    if layout is None:
        raise RuntimeError("CardMaker-Layout fehlt.")

    elements = layout.findall("Element")
    if len(elements) != 9:
        raise RuntimeError(f"Erwartet: 9 Elemente; gefunden: {len(elements)}")

    for slot, element in enumerate(elements, 1):
        base_size = int(element.get("width", "0"))
        if base_size != int(element.get("height", "0")) or base_size not in SIZE_RANGES:
            raise RuntimeError(f"Unerwartete Grundgröße bei Symbol {slot}: {base_size}")
        minimum, maximum = SIZE_RANGES[base_size]
        image = f"@[slot_{slot:02}]"
        element.set(
            "variable",
            image
            + "$[rotation:#random;-20;20#]"
            + f"$[width:#random;{minimum};{maximum}#]"
            + f"$[height:#random;{minimum};{maximum}#]",
        )
        element.set("rotation", "0")

    ET.indent(tree, space="  ")
    tree.write(project, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    configure(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("ruckpacken.cmp"))
