#!/usr/bin/env python3
"""Erzeugt Lautspiele-CSVs aus Namensliste und nummeriertem Bildordner."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PRIMARY_IMAGE = re.compile(r"^(\d{2,})\.png$")
CONFIG_FIELDS = [
    "symbol_set", "symbol_folder", "symbol_count", "symbol_names",
    "symbol_scale_map", "symbol_available_map",
    "gruselino_start", "gruselino_end", "gruselino_shift",
    "memory_start", "memory_end", "memory_shift",
    "domino_start", "domino_end", "domino_shift",
    "dobble_start", "dobble_end", "dobble_shift",
]


def normalized_set_name(value: str) -> str:
    result = value.strip().lower().replace(" ", "-")
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", result):
        raise ValueError(
            "Der Satzname darf nur a-z, 0-9, Bindestrich und Unterstrich enthalten."
        )
    return result


def read_names(path: Path) -> list[str]:
    names: list[str] = []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.reader(handle):
            if not row or not row[0].strip() or row[0].lstrip().startswith("#"):
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

    old_scales = previous.get("symbol_scale_map", "").split("|")
    scales = [
        old_scales[index] if index < len(old_scales) and old_scales[index] else "1"
        for index in range(amount)
    ]
    availability_length = max(31, amount)
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
        "gruselino_start": "1", "gruselino_end": str(amount),
        "gruselino_shift": previous.get("gruselino_shift", "0") or "0",
        "memory_start": "1", "memory_end": str(amount),
        "memory_shift": previous.get("memory_shift", "0") or "0",
        "domino_start": "1", "domino_end": str(amount),
        "domino_shift": previous.get("domino_shift", "0") or "0",
        "dobble_start": "1", "dobble_end": "31",
        "dobble_shift": previous.get("dobble_shift", "0") or "0",
    }
    with config_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CONFIG_FIELDS)
        writer.writeheader()
        writer.writerow(row)

    from build_lautspiele_project import write_mode_reference_files
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
    names = read_names(args.namensliste.resolve())
    path = create_symbol_set_config(
        names, args.bildordner, args.set_name, args.force,
    )
    print(f"Erstellt: {path}")


if __name__ == "__main__":
    main()
