#!/usr/bin/env python3
"""Lädt die ausgewählten farbigen ARASAAC-Piktogramme für nanDECK herunter."""

from __future__ import annotations

import csv
import sys
import urllib.request
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
OVERRIDE_IDS = {
    22: 38604,  # Trinkflasche statt Schnabeltasse
    53: 24161,  # Landkarte statt Kreditkarte
}
REVIEW_NOTES = {
    50: "Verbandskasten statt eindeutigem Arztkoffer; visuell prüfen.",
    52: "Fußballszene statt Fußballtor; Ersatz suchen.",
    69: "Ampel statt allgemeinem Verkehrsschild; Ersatz suchen.",
}
ATTRIBUTION = """# ARASAAC-Piktogramme

Piktogramm-Autor: Sergio Palao. Herkunft: ARASAAC (https://arasaac.org/).
Lizenz: Creative Commons BY-NC-SA. Rechteinhaber: Regierung von Aragón (Spanien).

Die Nutzung ist nur im Rahmen der ARASAAC-Nutzungsbedingungen zulässig:
https://arasaac.org/terms-of-use

Die konkreten ARASAAC-IDs und Quell-URLs stehen in
`../../../../../files/data/ruckpacken_arasaac_mapping.csv`.
"""


def download(url: str, target: Path) -> None:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Ruckpacken-ARASAAC-Downloader/1.00"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = response.read()
    if not payload.startswith(PNG_SIGNATURE):
        raise RuntimeError(f"Keine gültige PNG-Antwort für {url}")
    temporary = target.with_suffix(".tmp")
    temporary.write_bytes(payload)
    temporary.replace(target)


def update_cards(cards_path: Path) -> None:
    text = cards_path.read_text(encoding="utf-8-sig")
    text = text.replace(
        "symbols/sym_",
        "assets/images/arasaac/color/sym_",
    )
    cards_path.write_text(text, encoding="utf-8-sig", newline="")


def main(mapping_path: Path, output_dir: Path, cards_path: Path) -> None:
    with mapping_path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 73:
        raise RuntimeError(f"Erwartet: 73 Mapping-Zeilen; gefunden: {len(rows)}")

    output_dir.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    sources: list[dict[str, str | int]] = []
    for row in rows:
        symbol_id = int(row["symbol_id"])
        name = row["gegenstand"]
        arasaac_id = OVERRIDE_IDS.get(symbol_id, int(row["bester_id"]))
        url = (
            f"https://static.arasaac.org/pictograms/{arasaac_id}/"
            f"{arasaac_id}_500.png"
        )
        target = output_dir / f"sym_{symbol_id:02}.png"
        if not url:
            failures.append(f"{symbol_id:02} {name}: keine URL")
            continue
        try:
            download(url, target)
            print(f"[{symbol_id:02}/73] {name}: {target.name}")
            sources.append({
                "symbol_id": symbol_id,
                "gegenstand": name,
                "arasaac_id": arasaac_id,
                "farbig_url": url,
                "detail_url": f"https://arasaac.org/pictograms/{arasaac_id}",
                "pruefhinweis": REVIEW_NOTES.get(symbol_id, ""),
            })
        except Exception as error:
            failures.append(f"{symbol_id:02} {name}: {error}")

    (output_dir.parent / "ATTRIBUTION.md").write_text(
        ATTRIBUTION,
        encoding="utf-8",
        newline="\n",
    )
    with (output_dir.parent / "sources.csv").open(
        "w", encoding="utf-8-sig", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=sources[0].keys())
        writer.writeheader()
        writer.writerows(sources)
    if failures:
        raise RuntimeError("Downloadfehler:\n" + "\n".join(failures))
    update_cards(cards_path)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit(
            "Aufruf: python ruckpacken_download_arasaac_assets.py "
            "<mapping.csv> <ausgabeordner> <cards.csv>"
        )
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
