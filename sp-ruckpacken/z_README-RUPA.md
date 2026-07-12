# Ruckpacken

Ruckpacken ist ein semantisches Karten- und Deduktionsspiel. Der aktuelle Prototyp nutzt 73 Gegenstände in einer perfekten Dobble-Struktur mit 73 Karten und neun Symbolen je Karte.

## Dateien

- `anleitung_rupa.md`: Spielanleitung v1.00.
- `design_rupa.md`: Kartendesign und technische Grundlage.
- `files/data/ruckpacken_74.csv`: 73 Gegenstände samt Häufigkeit und Kategorien; der bestehende Dateiname bleibt aus Kompatibilitätsgründen erhalten.
- `files/data/ruckpacken_kats.csv`: Kategorien, Frequenzbewertung und Trefferzahlen im Korpus.
- `files/data/ruckpacken_arasaac_mapping.csv`: API-Kandidaten für alle 73 Gegenstände mit Farb-, Schwarz-Weiß- und Alternativlinks.
- `files/archive/ruckpacken_nanndeck.zip`: unveränderte Archivkopie des ursprünglichen nanDECK-Pakets.
- `tools/ruckpacken_arasaac_mapping_api_offiziell.py`: ARASAAC-Mapping über die offizielle API.
- `tools/nandeck/`: entpacktes, direkt nutzbares nanDECK-Werkzeug einschließlich Kartenmatrix, Vorlage, Validierung und Platzhaltersymbolen.

## ARASAAC-Mapping

```powershell
python tools/ruckpacken_arasaac_mapping_api_offiziell.py files/data/ruckpacken_74.csv files/data/ruckpacken_arasaac_mapping.csv
```

Das Skript sucht auf Deutsch und Englisch. Automatisch gewählte Kandidaten müssen wegen mehrdeutiger Begriffe anschließend visuell geprüft werden.

Der aktuelle API-Lauf fand für alle 73 Gegenstände mindestens einen Kandidaten und für 68 Gegenstände einen Alternativtreffer.

Echte ARASAAC-Bilddateien sind noch nicht vorhanden. Die PNG-Dateien unter `tools/nandeck/symbols/` sind nummerierte Platzhalter für die Kartengenerierung.
