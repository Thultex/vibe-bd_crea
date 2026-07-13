# Lautspiele

Lautspiele bündelt bildbasierte Sprachspiele, die aus einem gemeinsamen Symbolsatz erzeugt werden. Der aktuelle Werkzeugstand umfasst Gruselino, Domino und eine kompakte Dobble-Variante.

## Struktur

- `anleitung_laut.md`: kurze Spiel- und Materialübersicht.
- `design_laut.md`: technische Regeln für Symbolauswahl, Verschiebung und Layouts.
- `tools/cardmaker/`: aktives Generatorprojekt für [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker).
- `files/archive/lautspiele-original/`: unveränderter früherer Datei- und Codebestand.
- `files/archive/Logospiele.xlsx`: unveränderte frühere Berechnungsarbeitsmappe.

Das Spielkürzel lautet `laut`. Die aktiven Layouts verwenden gemeinsam `tools/cardmaker/lautspiele.csv`; ein Symbolsatz wird dort über seinen Ordner ausgewählt.
