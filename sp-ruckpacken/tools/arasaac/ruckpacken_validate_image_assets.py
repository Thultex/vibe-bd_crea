#!/usr/bin/env python3
"""Prüft Ruckpacken-PNGs auf vollflächige quadratische Hintergründe."""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image


def is_square_filling(path: Path) -> tuple[bool, str]:
    with Image.open(path) as image:
        rgba = image.convert("RGBA")
        width, height = rgba.size
        alpha = rgba.getchannel("A")
        corners = [
            alpha.getpixel((0, 0)),
            alpha.getpixel((width - 1, 0)),
            alpha.getpixel((0, height - 1)),
            alpha.getpixel((width - 1, height - 1)),
        ]
        bbox = alpha.getbbox()
        opaque_corners = sum(value > 8 for value in corners)
        fills_canvas = bbox == (0, 0, width, height)
        visible_pixels = sum(value > 8 for value in alpha.get_flattened_data())
        coverage = visible_pixels / (width * height)
        flagged = (opaque_corners >= 3 and fills_canvas) or coverage >= 0.82
        return flagged, (
            f"coverage={coverage:.3f}, corners={corners}, "
            f"alpha_bbox={bbox}, size={width}x{height}"
        )


def main(folder: Path) -> None:
    paths = sorted(folder.glob("sym_*.png"))
    flagged = []
    undersized = []
    for path in paths:
        bad, details = is_square_filling(path)
        if bad:
            flagged.append((path.name, details))
        with Image.open(path) as image:
            if image.width < 500 or image.height < 500:
                undersized.append((path.name, image.size))
    print(
        f"images={len(paths)} square_filling={len(flagged)} "
        f"undersized={len(undersized)}"
    )
    for name, details in flagged:
        print(f"FLAG {name}: {details}")
    for name, size in undersized:
        print(f"SMALL {name}: {size[0]}x{size[1]}")
    if len(paths) != 73:
        raise SystemExit("Erwartet werden 73 PNG-Dateien.")
    if flagged or undersized:
        raise SystemExit("Bildsatz verletzt Freistellungs- oder Größenregel.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Aufruf: python ruckpacken_validate_image_assets.py <bildordner>")
    main(Path(sys.argv[1]))
