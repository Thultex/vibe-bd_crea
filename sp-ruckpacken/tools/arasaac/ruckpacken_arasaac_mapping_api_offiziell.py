#!/usr/bin/env python3
"""
ARASAAC-Mapping über den offiziellen Suchendpunkt.

Nutzung:
    python arasaac_mapping_api_offiziell.py ruckpacken_74.csv arasaac_mapping.csv

Erwartete Eingabespalte:
    Gegenstand

Ausgabe:
    bester Treffer und optionaler Alternativtreffer,
    jeweils mit Farb-, Schwarz-Weiß- und Detailseiten-Link.
"""

from __future__ import annotations

import csv
import json
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

API_SEARCH = "https://api.arasaac.org/api/pictograms/{lang}/search/{query}"

ENGLISH_TERMS = {
    "Ball": "ball", "Besen": "broom", "Bett": "bed", "Brille": "glasses",
    "Buch": "book", "Decke": "blanket", "Gabel": "fork", "Handtuch": "towel",
    "Kissen": "pillow", "Lampe": "lamp", "Löffel": "spoon", "Messer": "knife",
    "Pfanne": "frying pan", "Regenschirm": "umbrella", "Schere": "scissors",
    "Schüssel": "bowl", "Seife": "soap", "Stift": "pen", "Tasse": "cup",
    "Teller": "plate", "Topf": "pot", "Trinkflasche": "water bottle",
    "Zahnbürste": "toothbrush", "Zeitung": "newspaper",
    "Bauklötze": "building blocks", "Computer": "computer", "Eimer": "bucket",
    "Fahrrad": "bicycle", "Föhn": "hair dryer", "Gießkanne": "watering can",
    "Hammer": "hammer", "Helm": "helmet", "Kamm": "comb", "Karte": "map",
    "Kerze": "candle", "Koffer": "suitcase", "Lineal": "ruler",
    "Maus": "computer mouse", "Mikrofon": "microphone", "Puzzle": "jigsaw puzzle",
    "Radio": "radio", "Rucksack": "backpack", "Schaufel": "shovel",
    "Schraubenzieher": "screwdriver", "Schubkarre": "wheelbarrow",
    "Spiegel": "mirror", "Tastatur": "keyboard", "Uhr": "clock",
    "Würfel": "dice", "Zange": "pliers", "Angel": "fishing rod",
    "Arztkoffer": "doctor bag", "Fernglas": "binoculars",
    "Fußballtor": "soccer goal", "Kompass": "compass", "Krücke": "crutch",
    "Lupe": "magnifying glass", "Maßband": "measuring tape",
    "Pfeife": "whistle", "Rollstuhl": "wheelchair", "Säge": "saw",
    "Schlafsack": "sleeping bag", "Schläger": "racket", "Seil": "rope",
    "Stethoskop": "stethoscope", "Taschenlampe": "flashlight",
    "Taschenmesser": "pocket knife", "Thermoskanne": "thermos flask",
    "Trommel": "drum", "Turnmatte": "gym mat",
    "Verkehrsschild": "traffic sign", "Wanderstock": "hiking stick",
    "Werkzeugkiste": "toolbox", "Zelt": "tent", "Zollstock": "folding ruler",
}

def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value.casefold())
    return "".join(c for c in value if not unicodedata.combining(c)).strip()

def fetch_json(url: str) -> Any:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 ARASAAC-Mapping/1.1",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))

def search(lang: str, query: str) -> list[dict[str, Any]]:
    url = API_SEARCH.format(lang=lang, query=urllib.parse.quote(query))
    payload = fetch_json(url)
    if not isinstance(payload, list):
        raise RuntimeError(f"Unerwartete API-Antwort für {query!r}: {type(payload).__name__}")
    return payload

def keywords(item: dict[str, Any]) -> list[str]:
    output = []
    for entry in item.get("keywords") or []:
        if isinstance(entry, dict):
            word = entry.get("keyword")
        else:
            word = str(entry)
        if word:
            output.append(str(word))
    return output

def candidate_score(item: dict[str, Any], query: str, lang: str, rank: int) -> int:
    q = normalize(query)
    kws = [normalize(k) for k in keywords(item)]
    score = 0
    if q in kws:
        score += 100
    if any(k.startswith(q) or q.startswith(k) for k in kws):
        score += 35
    if any(q in k or k in q for k in kws):
        score += 20
    if lang == "de":
        score += 5
    score -= rank
    return score

def collect_candidates(term_de: str, term_en: str) -> list[dict[str, Any]]:
    collected = []
    seen = set()
    for lang, query in [("de", term_de), ("en", term_en)]:
        try:
            results = search(lang, query)
        except Exception as exc:
            print(f"WARNUNG {term_de}/{lang}: {exc}", file=sys.stderr)
            continue
        for rank, item in enumerate(results):
            pid = item.get("_id")
            if not isinstance(pid, int) or pid in seen:
                continue
            seen.add(pid)
            enriched = dict(item)
            enriched["_lang"] = lang
            enriched["_query"] = query
            enriched["_score"] = candidate_score(item, query, lang, rank)
            collected.append(enriched)
        time.sleep(0.12)
    return sorted(collected, key=lambda x: x["_score"], reverse=True)

def image_url(pid: int, color: bool, size: int = 500) -> str:
    suffix = "" if color else "_nocolor"
    return f"https://static.arasaac.org/pictograms/{pid}/{pid}{suffix}_{size}.png"

def detail_url(pid: int) -> str:
    return f"https://arasaac.org/pictograms/{pid}"

def candidate_name(item: dict[str, Any]) -> str:
    kws = keywords(item)
    return kws[0] if kws else str(item.get("_id", ""))

def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit(
            "Nutzung: python arasaac_mapping_api_offiziell.py "
            "ruckpacken_74.csv arasaac_mapping.csv"
        )

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    with input_path.open(encoding="utf-8-sig", newline="") as handle:
        source_rows = list(csv.DictReader(handle))

    fields = [
        "symbol_id", "gegenstand", "suchbegriff_de", "suchbegriff_en", "status",
        "bester_id", "bester_name", "bester_keywords",
        "bester_farbig_link", "bester_sw_link", "bester_arasaac_link",
        "alternative_id", "alternative_name", "alternative_keywords",
        "alternative_farbig_link", "alternative_sw_link", "alternative_arasaac_link",
        "api_suche_de", "api_suche_en", "notiz",
    ]

    output_rows = []

    for symbol_id, source in enumerate(source_rows, start=1):
        term_de = source["Gegenstand"].strip()
        term_en = ENGLISH_TERMS.get(term_de, term_de)
        print(f"[{symbol_id:02d}/{len(source_rows)}] {term_de}", file=sys.stderr)

        candidates = collect_candidates(term_de, term_en)
        best = candidates[0] if candidates else None
        alt = candidates[1] if len(candidates) > 1 else None

        row = {
            "symbol_id": symbol_id,
            "gegenstand": term_de,
            "suchbegriff_de": term_de,
            "suchbegriff_en": term_en,
            "status": "API-Kandidat – visuell prüfen" if best else "kein Treffer",
            "api_suche_de": API_SEARCH.format(
                lang="de", query=urllib.parse.quote(term_de)
            ),
            "api_suche_en": API_SEARCH.format(
                lang="en", query=urllib.parse.quote(term_en)
            ),
            "notiz": "",
        }

        if best:
            pid = best["_id"]
            row.update({
                "bester_id": pid,
                "bester_name": candidate_name(best),
                "bester_keywords": " | ".join(keywords(best)),
                "bester_farbig_link": image_url(pid, True),
                "bester_sw_link": image_url(pid, False),
                "bester_arasaac_link": detail_url(pid),
            })

        if alt:
            pid = alt["_id"]
            row.update({
                "alternative_id": pid,
                "alternative_name": candidate_name(alt),
                "alternative_keywords": " | ".join(keywords(alt)),
                "alternative_farbig_link": image_url(pid, True),
                "alternative_sw_link": image_url(pid, False),
                "alternative_arasaac_link": detail_url(pid),
            })

        output_rows.append(row)

    with output_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Erstellt: {output_path}", file=sys.stderr)

if __name__ == "__main__":
    main()
