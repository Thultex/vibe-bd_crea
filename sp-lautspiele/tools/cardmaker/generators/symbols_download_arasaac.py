#!/usr/bin/env python3
"""Erzeugt einen Lautspiele-Bildsatz aus ARASAAC-Suchergebnissen.

Eingabe je Zeile: Deutsch[,Englisch][,zusätzliche Kandidaten je Sprache]
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
API_SEARCH = "https://api.arasaac.org/api/pictograms/{language}/search/{query}"
STATIC_IMAGE = "https://static.arasaac.org/pictograms/{id}/{id}_500.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
GENERATED_IMAGE = re.compile(r"^\d{2,}(?:-[de]\d+)?\.png$")
SOURCE_FIELDS = [
    "symbol_id", "name_de", "language", "query", "candidate_index",
    "filename", "arasaac_id", "keywords", "image_url", "detail_url",
    "selected_primary",
]


@dataclass(frozen=True)
class WordEntry:
    german: str
    english: str
    additional: int


def parse_word_file(path: Path) -> list[WordEntry]:
    entries: list[WordEntry] = []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for line_number, row in enumerate(csv.reader(handle), start=1):
            if not row or not any(cell.strip() for cell in row):
                continue
            if row[0].lstrip().startswith("#"):
                continue
            if len(row) > 3:
                raise ValueError(f"Zeile {line_number}: höchstens drei Felder erlaubt.")
            values = [cell.strip() for cell in row]
            german = values[0]
            english = values[1] if len(values) >= 2 else ""
            count_text = values[2] if len(values) == 3 else "0"
            if len(values) == 2 and english.isdecimal():
                count_text, english = english, ""
            if not german:
                raise ValueError(f"Zeile {line_number}: deutsches Wort fehlt.")
            try:
                additional = int(count_text or "0")
            except ValueError as error:
                raise ValueError(
                    f"Zeile {line_number}: Anzahl muss eine ganze Zahl sein."
                ) from error
            if not 0 <= additional <= 20:
                raise ValueError(f"Zeile {line_number}: Anzahl muss zwischen 0 und 20 liegen.")
            entries.append(WordEntry(german, english, additional))
    if not entries:
        raise ValueError("Die Wortliste enthält keine Einträge.")
    return entries


def fetch_json(url: str) -> Any:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Lautspiele-ARASAAC-Importer/1.00",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def search(language: str, query: str) -> list[dict[str, Any]]:
    url = API_SEARCH.format(
        language=language,
        query=urllib.parse.quote(query, safe=""),
    )
    payload = fetch_json(url)
    if not isinstance(payload, list):
        raise RuntimeError(
            f"Unerwartete ARASAAC-Antwort für {language}:{query!r}."
        )
    return [item for item in payload if isinstance(item.get("_id"), int)]


def keywords(item: dict[str, Any]) -> str:
    values: list[str] = []
    for entry in item.get("keywords") or []:
        value = entry.get("keyword") if isinstance(entry, dict) else str(entry)
        if value:
            values.append(str(value))
    return " | ".join(values)


def download_png(arasaac_id: int, target: Path) -> str:
    url = STATIC_IMAGE.format(id=arasaac_id)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Lautspiele-ARASAAC-Importer/1.00"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = response.read()
    if not payload.startswith(PNG_SIGNATURE):
        raise RuntimeError(f"ARASAAC lieferte keine PNG-Datei: {url}")
    target.write_bytes(payload)
    return url


def distinct_candidates(
    candidates: list[dict[str, Any]], used: set[int], amount: int
) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    for candidate in candidates:
        candidate_id = int(candidate["_id"])
        if candidate_id in used:
            continue
        used.add(candidate_id)
        selected.append(candidate)
        if len(selected) == amount:
            break
    return selected


def source_row(
    symbol_id: int,
    entry: WordEntry,
    language: str,
    query: str,
    candidate_index: int,
    filename: str,
    candidate: dict[str, Any],
    image_url: str,
    primary: bool,
) -> dict[str, str | int]:
    arasaac_id = int(candidate["_id"])
    return {
        "symbol_id": symbol_id,
        "name_de": entry.german,
        "language": language,
        "query": query,
        "candidate_index": candidate_index,
        "filename": filename,
        "arasaac_id": arasaac_id,
        "keywords": keywords(candidate),
        "image_url": image_url,
        "detail_url": f"https://arasaac.org/pictograms/{arasaac_id}",
        "selected_primary": "ja" if primary else "nein",
    }


def clean_generated_images(folder: Path) -> None:
    for path in folder.iterdir():
        if path.is_file() and GENERATED_IMAGE.fullmatch(path.name):
            path.unlink()


def write_sources(path: Path, rows: list[dict[str, str | int]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=SOURCE_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def write_attribution(folder: Path, sources_name: str) -> None:
    text = (
        "# ARASAAC-Piktogramme\n\n"
        "Piktogramm-Autor: Sergio Palao. Herkunft: ARASAAC "
        "(https://arasaac.org/).\n"
        "Lizenz: Creative Commons BY-NC-SA. Rechteinhaber: Regierung von "
        "Aragón (Spanien).\n\n"
        "Nutzungsbedingungen: https://arasaac.org/terms-of-use\n\n"
        f"Konkrete IDs und URLs: `../../../{sources_name}`.\n"
    )
    (folder / "ATTRIBUTION.md").write_text(text, encoding="utf-8", newline="\n")


def normalized_set_name(value: str) -> str:
    result = value.strip().lower().replace(" ", "-")
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", result):
        raise ValueError(
            "Der Satzname darf nur a-z, 0-9, Bindestrich und Unterstrich enthalten."
        )
    return result


def import_symbols(input_path: Path, set_name: str, force: bool) -> None:
    entries = parse_word_file(input_path)
    output_folder = ROOT / "images" / "symbols" / set_name
    config_path = ROOT / f"symbols_{set_name}.csv"
    sources_path = ROOT / f"symbols_{set_name}_sources.csv"
    output_folder.mkdir(parents=True, exist_ok=True)
    existing_images = any(
        path.is_file() and GENERATED_IMAGE.fullmatch(path.name)
        for path in output_folder.iterdir()
    )
    if (config_path.exists() or sources_path.exists() or existing_images) and not force:
        raise FileExistsError(
            "Ausgabe existiert bereits. Mit --force bewusst neu erzeugen."
        )
    if force:
        clean_generated_images(output_folder)

    source_rows: list[dict[str, str | int]] = []
    for symbol_id, entry in enumerate(entries, start=1):
        label = f"[{symbol_id:02}/{len(entries):02}] {entry.german}"
        print(label, file=sys.stderr)
        german_results = search("de", entry.german)
        time.sleep(0.12)
        english_results = search("en", entry.english) if entry.english else []
        if entry.english:
            time.sleep(0.12)
        used: set[int] = set()
        primary_pool = german_results or english_results
        if not primary_pool:
            raise RuntimeError(f"Kein ARASAAC-Treffer für {entry.german!r}.")
        primary = distinct_candidates(primary_pool, used, 1)[0]
        primary_language = "de" if german_results else "en"
        primary_query = entry.german if german_results else entry.english
        primary_name = f"{symbol_id:02}.png"
        primary_url = download_png(int(primary["_id"]), output_folder / primary_name)
        source_rows.append(source_row(
            symbol_id, entry, primary_language, primary_query, 0,
            primary_name, primary, primary_url, True,
        ))

        german_alternatives = distinct_candidates(
            german_results, used, entry.additional
        )
        if len(german_alternatives) < entry.additional:
            print(
                f"  Hinweis: nur {len(german_alternatives)} von "
                f"{entry.additional} deutschen Alternativen gefunden.",
                file=sys.stderr,
            )
        for index, candidate in enumerate(german_alternatives, start=1):
            filename = f"{symbol_id:02}-d{index}.png"
            url = download_png(int(candidate["_id"]), output_folder / filename)
            source_rows.append(source_row(
                symbol_id, entry, "de", entry.german, index,
                filename, candidate, url, False,
            ))

        english_alternatives = distinct_candidates(
            english_results, used, entry.additional
        )
        if entry.english and len(english_alternatives) < entry.additional:
            print(
                f"  Hinweis: nur {len(english_alternatives)} von "
                f"{entry.additional} englischen Alternativen gefunden.",
                file=sys.stderr,
            )
        for index, candidate in enumerate(english_alternatives, start=1):
            filename = f"{symbol_id:02}-e{index}.png"
            url = download_png(int(candidate["_id"]), output_folder / filename)
            source_rows.append(source_row(
                symbol_id, entry, "en", entry.english, index,
                filename, candidate, url, False,
            ))

    from symbols_generate_sets import create_symbol_set_config
    create_symbol_set_config(
        [entry.german for entry in entries], output_folder, set_name, force=True,
    )
    write_sources(sources_path, source_rows)
    write_attribution(output_folder, sources_path.name)
    print(f"Erstellt: {config_path}", file=sys.stderr)
    print(f"Bilder: {output_folder}", file=sys.stderr)
    print(f"Quellen: {sources_path}", file=sys.stderr)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="ARASAAC-Bilder und Lautspiele-Symbol-CSV erzeugen."
    )
    parser.add_argument("wortliste", type=Path, help="UTF-8-Textdatei/CSV ohne Kopfzeile")
    parser.add_argument(
        "--set-name",
        help="Bildsatzname; standardmäßig der Dateiname der Wortliste",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Vorhandene generierte PNGs und CSVs bewusst ersetzen",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    set_name = normalized_set_name(args.set_name or args.wortliste.stem)
    import_symbols(args.wortliste.resolve(), set_name, args.force)


if __name__ == "__main__":
    main()
