# Ruckpacken

Ruckpacken ist ein semantisches Karten- und Deduktionsspiel. Der aktuelle Prototyp nutzt 73 Gegenstände in einer perfekten Dobble-Struktur mit 73 Karten und neun Symbolen je Karte.

## Dateien

- `anleitung_ruckp.md`: Spielanleitung v1.00.
- `design_ruckp.md`: Kartendesign und technische Grundlage.
- `assets/ruckpacken_74.csv`: 73 Gegenstände samt Häufigkeit und Kategorien; der bestehende Dateiname bleibt aus Kompatibilitätsgründen erhalten.
- `assets/ruckpacken_kats.csv`: Kategorien, Frequenzbewertung und Trefferzahlen im Korpus.
- `assets/ruckpacken_nanndeck.zip`: vollständiges nanDECK-Paket.
- `tools/ruckpacken_arasaac_mapping_api_offiziell.py`: ARASAAC-Mapping über die offizielle API.

## ARASAAC-Mapping

```powershell
python tools/ruckpacken_arasaac_mapping_api_offiziell.py assets/ruckpacken_74.csv arasaac_mapping.csv
```

Das Skript sucht auf Deutsch und Englisch. Automatisch gewählte Kandidaten müssen wegen mehrdeutiger Begriffe anschließend visuell geprüft werden.
