# Ruckpacken

Ruckpacken ist ein semantisches Karten- und Deduktionsspiel. Der aktuelle Prototyp nutzt 73 Gegenstände in einer perfekten Dobble-Struktur mit 73 Karten und neun Symbolen je Karte.

## Dateien

- `anleitung_rupa.md`: Spielanleitung v1.00.
- `design_rupa.md`: Kartendesign und technische Grundlage.
- `files/data/ruckpacken_74.csv`: 73 Gegenstände samt Häufigkeit und Kategorien; der bestehende Dateiname bleibt aus Kompatibilitätsgründen erhalten.
- `files/data/ruckpacken_kats.csv`: Kategorien, Frequenzbewertung und Trefferzahlen im Korpus.
- `files/data/ruckpacken_arasaac_mapping.csv`: API-Kandidaten für alle 73 Gegenstände mit Farb-, Schwarz-Weiß- und Alternativlinks.
- `files/archive/ruckpacken_nanndeck.zip`: unveränderte Archivkopie des ursprünglichen nanDECK-Pakets.
- `tools/arasaac/`: API-Mapping und reproduzierbarer Download der ausgewählten ARASAAC-Piktogramme.
- `tools/cm/`: bevorzugtes Kartengenerierungswerkzeug für [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker), projektintern kurz `cm`.
- `tools/nandeck/`: Legacy-Prototyp; bleibt vorerst zur Nachvollziehbarkeit erhalten.

## ARASAAC-Mapping

```powershell
python tools/arasaac/ruckpacken_arasaac_mapping_api_offiziell.py files/data/ruckpacken_74.csv files/data/ruckpacken_arasaac_mapping.csv
```

Das Skript sucht auf Deutsch und Englisch. Automatisch gewählte Kandidaten müssen wegen mehrdeutiger Begriffe anschließend visuell geprüft werden.

Der aktuelle API-Lauf fand für alle 73 Gegenstände mindestens einen Kandidaten und für 68 Gegenstände einen Alternativtreffer. Die 73 ausgewählten farbigen Bilder liegen unter `tools/cm/assets/images/arasaac/color/`; Quellen und Prüfhilfen stehen daneben in `sources.csv`.

Der Verbandskasten wird als Arztkoffer akzeptiert. Trinkflasche, Fußballtor, Karte und Verkehrsschild wurden auf geeignete freigestellte Alternativtreffer korrigiert; Verkehrsschild verwendet ein Stoppschild.

Die Piktogramme stammen von Sergio Palao für ARASAAC/Gobierno de Aragón und stehen unter CC BY-NC-SA. Der vollständige Hinweis liegt in `tools/cm/assets/images/arasaac/ATTRIBUTION.md`.
