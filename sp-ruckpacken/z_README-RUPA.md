# Ruckpacken

Ruckpacken ist ein semantisches Karten- und Deduktionsspiel. Der aktuelle Prototyp nutzt 73 Gegenstände in einer perfekten Dobble-Struktur mit 73 Karten und neun Symbolen je Karte.

## Dateien

- `anleitung_rupa.md`: Spielanleitung v1.00.
- `design_rupa.md`: Kartendesign und technische Grundlage.
- `files/ruckpacken_gegenstaende.md`: nummerierte Übersicht aller 73 Gegenstände mit Notizspalte und Kategorien; Checkliste für Gegenstandsbilder in [Issue #12](https://github.com/Thultex/vibe-bd_crea/issues/12).
- `files/ruckpacken_merkmale.md`: nummerierte Übersicht aller 85 Merkmale mit Notizspalte, Typ und zugeordneten Gegenständen; nach Handlung, Eigenschaft und Ort gruppiert, innerhalb jedes Typs nach Anzahl zugeordneter Gegenstände absteigend und dann alphabetisch nach Namen sortiert. Checkliste für Merkmalsbilder in [Issue #13](https://github.com/Thultex/vibe-bd_crea/issues/13).
- `files/data/ruckpacken_74.csv`: 73 Gegenstände samt Häufigkeit und Kategorien; der bestehende Dateiname bleibt aus Kompatibilitätsgründen erhalten.
- `files/data/ruckpacken_kats.csv`: Kategorien, Frequenzbewertung und Trefferzahlen im Korpus.
- `files/data/ruckpacken_arasaac_mapping.csv`: API-Kandidaten für alle 73 Gegenstände mit Farb-, Schwarz-Weiß- und Alternativlinks.
- `files/data/custom-img_mapping.csv`: Zuordnung aller 73 Gegenstände zu eigenen Concepts/PNG-Paaren oder ARASAAC, einschließlich der aktiven CardMaker-Bildpfade.
- `files/routine_import-img.md`: Vorgehen für spätere Bildimporte, Dateinamensregeln, Zuordnung und CardMaker-Prüfung.
- `assets/img/objects/`: eigene Concepts-Zeichnungen und gleichnamige PNG-Exporte; die leere TXT-Datei ist eine Orientierung für Größe und Linienbreite.
- `files/archive/ruckpacken_nanndeck.zip`: unveränderte Archivkopie des ursprünglichen nanDECK-Pakets.
- `tools/arasaac/`: API-Mapping und reproduzierbarer Download der ausgewählten ARASAAC-Piktogramme.
- `tools/cardmaker/`: bevorzugtes Kartengenerierungswerkzeug für [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker), projektintern kurz `cm`.
- `tools/nandeck/`: Legacy-Prototyp; bleibt vorerst zur Nachvollziehbarkeit erhalten.

## Neue Bilder übernehmen

Aus dem Repository-Root `python -B sp-ruckpacken/tools/cardmaker/sync_custom_images.py` ausführen. Das Vorgehen steht in [files/routine_import-img.md](files/routine_import-img.md). Die Routine erkennt vollständige Concepts/PNG-Paare unter `assets/img/`, aktualisiert `custom-img_mapping.csv` und kopiert eigene Bilder nach `tools/cardmaker/assets/images/custom/`.

CardMaker verlinkt über `cards.csv` direkt auf `tools/cardmaker/assets/images/sym_1.png` bis `sym_73.png`. Dort haben eigene Bilder Vorrang; fehlende Motive werden aus ARASAAC ergänzt. Aktuell sind der eigene Ball und 72 ARASAAC-Motive eingebunden.

## ARASAAC-Mapping

```powershell
python tools/arasaac/ruckpacken_arasaac_mapping_api_offiziell.py files/data/ruckpacken_74.csv files/data/ruckpacken_arasaac_mapping.csv
```

Das Skript sucht auf Deutsch und Englisch. Automatisch gewählte Kandidaten müssen wegen mehrdeutiger Begriffe anschließend visuell geprüft werden.

Der aktuelle API-Lauf fand für alle 73 Gegenstände mindestens einen Kandidaten und für 68 Gegenstände einen Alternativtreffer. Die 73 ausgewählten farbigen Bilder liegen unter `tools/cardmaker/assets/images/arasaac/color/`; Quellen und Prüfhilfen stehen daneben in `sources.csv`.

Der Verbandskasten wird als Arztkoffer akzeptiert. Trinkflasche, Fußballtor, Karte und Verkehrsschild wurden auf geeignete freigestellte Alternativtreffer korrigiert; Verkehrsschild verwendet ein Stoppschild.

Die Piktogramme stammen von Sergio Palao für ARASAAC/Gobierno de Aragón und stehen unter CC BY-NC-SA. Der vollständige Hinweis liegt in `tools/cardmaker/assets/images/arasaac/ATTRIBUTION.md`.
