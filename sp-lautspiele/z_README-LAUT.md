# Lautspiele

Lautspiele bündelt bildbasierte Sprachspiele, die aus einem gemeinsamen Symbolsatz erzeugt werden. Der aktuelle Werkzeugstand umfasst Gruselino, Domino und eine kompakte Dobble-Variante.

## Struktur

- `anleitung_laut.md`: kurze Spiel- und Materialübersicht.
- `design_laut.md`: technische Regeln für Symbolauswahl, Verschiebung und Layouts.
- `tools/cardmaker/`: aktives Generatorprojekt für [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker).
- `files/archive/lautspiele-original/`: unveränderter früherer Datei- und Codebestand.
- `files/archive/Logospiele.xlsx`: unveränderte frühere Berechnungsarbeitsmappe.

Das Spielkürzel lautet `laut`. Gruselino, Domino und Dobble sind eigene Layouts, benötigen aber keine eigenen Modus-CSVs. Stattdessen wählt jedes Layout eine vollständige Symbol-CSV wie `symbols_k.csv`; sie enthält Bildordner, Namen, Größenkorrekturen und die modusspezifischen Bereiche.
