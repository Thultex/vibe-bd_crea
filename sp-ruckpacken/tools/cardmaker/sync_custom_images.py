#!/usr/bin/env python3
"""v1.00: Ordnet Concepts/PNG-Paare zu und aktualisiert den CardMaker-Bildsatz."""

from __future__ import annotations

import argparse
import csv
import re
import struct
from pathlib import Path

from build_cm_data import csv_bytes, render


VERSION = "1.00"
MAPPING_FIELDS = [
    "Nr", "Gegenstand", "Concepts", "PNG", "Quelle", "CardMaker_Custom", "CardMaker_Aktiv",
]


def name_key(name: str) -> str:
    name = name.casefold().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    return re.sub(r"[^a-z0-9]", "", name)


def discover_custom(folder: Path, names: dict[int, str]) -> tuple[dict, list[str]]:
    if not folder.is_dir():
        raise RuntimeError(f"Quellordner fehlt: {folder}")
    groups: dict[str, list[Path]] = {}
    for path in sorted(folder.rglob("*")):
        if path.is_file() and path.suffix.casefold() in {".png", ".concepts", ".conzepts"}:
            key = path.relative_to(folder).with_suffix("").as_posix().casefold()
            groups.setdefault(key, []).append(path)

    found = {}
    warnings = []
    for key, paths in groups.items():
        pngs = [path for path in paths if path.suffix.casefold() == ".png"]
        concepts = [path for path in paths if path.suffix.casefold() != ".png"]
        if len(pngs) > 1 or len(concepts) > 1:
            raise RuntimeError(f"Mehrdeutiges Dateipaar: {key}")
        if not pngs or not concepts or not concepts[0].stat().st_size:
            warnings.append(f"Unvollständiges Dateipaar übersprungen: {key}")
            continue

        png, concept = pngs[0], concepts[0]
        match = re.fullmatch(r"rp(\d+)_(.+)", png.stem, re.IGNORECASE)
        if match:
            number = int(match[1])
            if number not in names or name_key(match[2]) != name_key(names[number]):
                raise RuntimeError(f"Nummer und Gegenstandsname passen nicht zusammen: {png.name}")
        else:
            matches = [number for number, name in names.items() if name_key(png.stem) == name_key(name)]
            if len(matches) != 1:
                raise RuntimeError(f"Keine eindeutige Gegenstandszuordnung: {png.name}; erwartet rp<Nr>_<Name>.png")
            number = matches[0]
        if number in found:
            raise RuntimeError(f"Mehrere Bilder für {number}. {names[number]}: {found[number][0].name}, {png.name}")
        found[number] = (png, concept)
    return found, warnings


def png_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    if len(data) < 33 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise RuntimeError(f"Keine gültige PNG-Datei: {path}")
    if 0 in struct.unpack(">II", data[16:24]):
        raise RuntimeError(f"PNG ohne Bildfläche: {path}")
    return data


def plan_sync(game: Path) -> tuple[dict[Path, bytes], list[str], int]:
    cm = game / "tools/cardmaker"
    images = cm / "assets/images"
    with (game / "files/data/ruckpacken_74.csv").open(encoding="utf-8-sig", newline="") as handle:
        names = {number: row["Gegenstand"] for number, row in enumerate(csv.DictReader(handle), 1)}
    if len(names) != 73 or len(set(names.values())) != 73:
        raise RuntimeError("Erwartet: 73 eindeutige Gegenstände.")
    with (images / "arasaac/sources.csv").open(encoding="utf-8-sig", newline="") as handle:
        sources = list(csv.DictReader(handle))
    if len(sources) != 73 or {int(row["symbol_id"]): row["gegenstand"] for row in sources} != names:
        raise RuntimeError("ARASAAC-Symbolnummern stimmen nicht mit der Gegenstandsliste überein.")

    custom, warnings = discover_custom(game / "assets/img", names)
    outputs = {}
    mapping = []
    for number, name in names.items():
        active = images / f"sym_{number}.png"
        copy = images / "custom" / f"sym_{number}.png"
        pair = custom.get(number)
        source = pair[0] if pair else images / "arasaac/color" / f"sym_{number:02}.png"
        data = png_bytes(source)
        if pair:
            outputs[copy] = data
        outputs[active] = data
        mapping.append({
            "Nr": number,
            "Gegenstand": name,
            "Concepts": pair[1].relative_to(game).as_posix() if pair else "",
            "PNG": source.relative_to(game).as_posix(),
            "Quelle": "custom" if pair else "arasaac",
            "CardMaker_Custom": copy.relative_to(game).as_posix() if pair else "",
            "CardMaker_Aktiv": active.relative_to(game).as_posix(),
        })
    outputs[game / "files/data/custom-img_mapping.csv"] = csv_bytes(mapping, MAPPING_FIELDS)
    # Erst alle Quellen und Referenzen prüfen, dann Dateien aktualisieren.
    outputs[cm / "cards.csv"] = render(cm / "cards.csv")
    return outputs, warnings, len(custom)


def synchronize(game: Path, *, check: bool = False, dry_run: bool = False) -> int:
    outputs, warnings, custom_count = plan_sync(game)
    changed = [path for path, content in outputs.items() if not path.is_file() or path.read_bytes() != content]
    for warning in warnings:
        print(f"HINWEIS: {warning}")
    for path in changed:
        if not (check or dry_run):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(outputs[path])
        else:
            print(f"Ausstehend: {path.relative_to(game).as_posix()}")
    mode = "Prüfung" if check else "Vorschau" if dry_run else "Abgleich"
    print(f"{mode}: {custom_count} Custom, {73 - custom_count} ARASAAC, 73 aktive Bilder; {len(changed)} Dateien {'ausstehend' if check or dry_run else 'aktualisiert'}.")
    return 1 if check and changed else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Nur prüfen; Exitcode 1 bei ausstehenden Änderungen.")
    mode.add_argument("--dry-run", action="store_true", help="Änderungen anzeigen, ohne Dateien zu schreiben.")
    parser.add_argument("--version", action="version", version=VERSION)
    args = parser.parse_args()
    try:
        return synchronize(Path(__file__).resolve().parents[2], check=args.check, dry_run=args.dry_run)
    except (RuntimeError, OSError, ValueError, KeyError) as error:
        parser.exit(1, f"FEHLER: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
