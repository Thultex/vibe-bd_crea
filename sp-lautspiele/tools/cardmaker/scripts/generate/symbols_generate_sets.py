#!/usr/bin/env python3
"""Erzeugt Lautspiele-Sets aus Namensliste und nummeriertem Bildordner."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BUILD_SCRIPTS = Path(__file__).resolve().parents[1] / "build"
if str(BUILD_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(BUILD_SCRIPTS))
PRIMARY_IMAGE = re.compile(r"^(\d{2,})\.png$")
CONFIG_FIELDS = [
    "symbol_set", "symbol_folder", "symbol_count", "symbol_names",
    "symbol_scale_map", "symbol_available_map",
    "gruselino_start", "gruselino_end", "gruselino_shift",
    "domino_start", "domino_end", "domino_shift",
    "dobble_start", "dobble_end", "dobble_shift",
    "spiel_start", "spiel_end", "spiel_shift",
    "bingo_start", "bingo_end", "bingo_shift",
]
MANIFEST_FIELDS = ["symbol_id", "name", "scale"]


def normalized_set_name(value: str) -> str:
    result = value.strip().lower().replace(" ", "-")
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", result):
        raise ValueError(
            "Der Satzname darf nur a-z, 0-9, Bindestrich und Unterstrich enthalten."
        )
    return result


def input_set_name(path: Path) -> str | None:
    """Liest optional `name,<satz>` aus der ersten Tabellenzeile nach dem Kopf."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        next(reader, [])
        name_row = next(reader, [])
    if not name_row or name_row[0].strip().lower() != "name":
        return None
    if len(name_row) < 2 or not name_row[1].strip():
        raise ValueError(
            "Die erste Tabellenzeile nach dem Kopf muss `name,<satzname>` enthalten."
        )
    return normalized_set_name(name_row[1])


def read_names(path: Path) -> list[str]:
    names: list[str] = []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for line_number, row in enumerate(csv.reader(handle), start=1):
            if not row or not row[0].strip() or row[0].lstrip().startswith("#"):
                continue
            first_value = row[0].strip().lower()
            if line_number == 1 and first_value in {"deutsch", "name_de"}:
                continue
            if line_number == 2 and first_value == "name":
                continue
            names.append(row[0].strip())
    if not names:
        raise ValueError("Die Namensliste enthält keine Einträge.")
    return names


def primary_image_ids(folder: Path) -> list[int]:
    ids = sorted(
        int(match.group(1))
        for path in folder.iterdir()
        if path.is_file() and (match := PRIMARY_IMAGE.fullmatch(path.name))
    )
    if not ids:
        raise ValueError(f"Keine Hauptbilder wie 01.png in {folder} gefunden.")
    expected = list(range(1, ids[-1] + 1))
    if ids != expected:
        raise ValueError(
            "Hauptbilder müssen ohne Lücke ab 01.png nummeriert sein: "
            f"gefunden {ids}."
        )
    return ids


def previous_values(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return rows[0] if len(rows) == 1 else {}


def read_manifest_scales(path: Path) -> dict[int, str]:
    """Bewahrt manuell korrigierte Groessen eines vorhandenen Bildsatzes."""
    if not path.is_file():
        return {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    result: dict[int, str] = {}
    for row in rows:
        symbol_id = int(row["symbol_id"])
        scale = float(row["scale"])
        if symbol_id < 1 or scale <= 0:
            raise ValueError(f"Ungültiger Eintrag in {path}.")
        result[symbol_id] = f"{scale:.2f}"
    return result


def write_symbol_manifest(
    image_folder: Path, names: list[str], preserve_existing: bool = True,
) -> list[str]:
    """Schreibt Namen/Groessen direkt in den Ordner des Bildsatzes."""
    path = image_folder / "symbols.csv"
    previous_scales = read_manifest_scales(path) if preserve_existing else {}
    scales = [previous_scales.get(index, "1.00") for index in range(1, len(names) + 1)]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS)
        writer.writeheader()
        for index, (name, scale) in enumerate(zip(names, scales), start=1):
            writer.writerow({"symbol_id": index, "name": name, "scale": scale})
    return scales


def ensure_build_config(image_folder: Path) -> Path:
    """Erzeugt die satzlokale Auswahlkonfiguration mit Standardwerten."""
    path = image_folder / "build.ini"
    if not path.is_file():
        path.write_text(
            "[symbols]\n"
            "# Erstes Symbol: Erste verwendete Hauptdatei; 1 entspricht 01.png.\n"
            "start_symbol = 1\n"
            "# Anzahl verwendeter Symbole: -1 verwendet automatisch alle ab start_symbol vorhandenen Symbole.\n"
            "symbol_count = -1\n",
            encoding="utf-8",
        )
    return path


def create_symbol_set_config(
    names: list[str], image_folder: Path, set_name: str | None = None,
    force: bool = False,
) -> Path:
    image_folder = image_folder.resolve()
    try:
        relative_folder = image_folder.relative_to(ROOT.resolve()).as_posix()
    except ValueError as error:
        raise ValueError("Der Bildordner muss unterhalb des CardMaker-Ordners liegen.") from error
    ids = primary_image_ids(image_folder)
    amount = len(ids)
    if len(names) < amount:
        raise ValueError(
            f"{amount} Hauptbilder, aber nur {len(names)} Namen vorhanden."
        )
    selected_names = names[:amount]
    set_name = normalized_set_name(set_name or image_folder.name)
    config_path = ROOT / f"symbols_{set_name}.csv"
    previous = previous_values(config_path)
    if config_path.exists() and not force:
        raise FileExistsError("Master-CSV existiert bereits; mit --force neu erzeugen.")

    scales = write_symbol_manifest(image_folder, selected_names)
    build_config = ensure_build_config(image_folder)
    availability_length = max(31, amount)
    from build_lautspiele_files import selection_range
    selection_start, selection_end = selection_range(amount, build_config)
    row = {
        "symbol_set": set_name,
        "symbol_folder": relative_folder,
        "symbol_count": str(amount),
        "symbol_names": "|".join(selected_names),
        "symbol_scale_map": "|".join(scales),
        "symbol_available_map": "|".join(
            "1" if index in ids else "0"
            for index in range(1, availability_length + 1)
        ),
        "gruselino_start": str(selection_start),
        "gruselino_end": str(selection_end),
        "gruselino_shift": previous.get("gruselino_shift", "0") or "0",
        "domino_start": str(selection_start),
        "domino_end": str(selection_end),
        "domino_shift": previous.get("domino_shift", "0") or "0",
        "dobble_start": str(selection_start),
        "dobble_end": str(selection_end),
        "dobble_shift": previous.get("dobble_shift", "0") or "0",
        "spiel_start": str(selection_start),
        "spiel_end": str(selection_end),
        "spiel_shift": previous.get("spiel_shift", "0") or "0",
        "bingo_start": str(selection_start),
        "bingo_end": str(selection_end),
        "bingo_shift": previous.get("bingo_shift", "0") or "0",
    }
    with config_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CONFIG_FIELDS)
        writer.writeheader()
        writer.writerow(row)

    from build_lautspiele_files import write_mode_reference_files
    write_mode_reference_files()
    return config_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Master- und Modus-CSVs aus Namensliste und Bildordner erzeugen."
    )
    parser.add_argument("namensliste", type=Path)
    parser.add_argument("bildordner", type=Path)
    parser.add_argument("--set-name", help="Standardmäßig der Name des Bildordners")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = args.namensliste.resolve()
    names = read_names(input_path)
    set_name = args.set_name or input_set_name(input_path)
    path = create_symbol_set_config(
        names, args.bildordner, set_name, args.force,
    )
    print(f"Erstellt: {path}")


if __name__ == "__main__":
    main()
