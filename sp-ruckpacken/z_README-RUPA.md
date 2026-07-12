# Ruckpacken

Ruckpacken ist ein semantisches Karten- und Deduktionsspiel. Der aktuelle Prototyp nutzt 73 Gegenstände in einer perfekten Dobble-Struktur mit 73 Karten und neun Symbolen je Karte.

## Dateien

- `anleitung_rupa.md`: Spielanleitung v1.00.
- `design_rupa.md`: Kartendesign und technische Grundlage.
- `files/ruckpacken_74.csv`: 73 Gegenstände samt Häufigkeit und Kategorien; der bestehende Dateiname bleibt aus Kompatibilitätsgründen erhalten.
- `files/ruckpacken_kats.csv`: Kategorien, Frequenzbewertung und Trefferzahlen im Korpus.
- `files/ruckpacken_nanndeck.zip`: vollständiges nanDECK-Paket mit nummerierten Platzhalterbildern.
- `files/ruckpacken_arasaac_mapping.csv`: API-Kandidaten für alle 73 Gegenstände mit Farb-, Schwarz-Weiß- und Alternativlinks.
- `tools/ruckpacken_arasaac_mapping_api_offiziell.py`: ARASAAC-Mapping über die offizielle API.

## ARASAAC-Mapping

```powershell
python tools/ruckpacken_arasaac_mapping_api_offiziell.py files/ruckpacken_74.csv files/ruckpacken_arasaac_mapping.csv
```

Das Skript sucht auf Deutsch und Englisch. Automatisch gewählte Kandidaten müssen wegen mehrdeutiger Begriffe anschließend visuell geprüft werden.

Der aktuelle API-Lauf fand für alle 73 Gegenstände mindestens einen Kandidaten und für 68 Gegenstände einen Alternativtreffer.

Echte ARASAAC-Bilddateien sind noch nicht unter `assets/images/` abgelegt. Die PNG-Dateien im nanDECK-Paket sind nummerierte Platzhalter.
