# Lautspiele

Lautspiele bündelt bildbasierte Sprachspiele, die aus einem gemeinsamen Symbolsatz erzeugt werden. Der aktuelle Werkzeugstand umfasst Gruselino, Memory, Domino und eine kompakte perfekte Dobble-Variante.

## Struktur

- `anleitung_laut.md`: kurze Spiel- und Materialübersicht.
- `design_laut.md`: technische Regeln für Symbolauswahl, Verschiebung und Layouts.
- `tools/cardmaker/`: aktives Generatorprojekt für [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker).
- `tools/cardmaker/generators/import_arasaac_symbols.py`: lädt nummerierte ARASAAC-PNGs und Quellen aus einfachen Wortlisten.
- `tools/cardmaker/generators/generate_symbol_set.py`: erzeugt dieselben CSVs ohne Netzwerk aus einer Namensliste und vorhandenen nummerierten PNGs.
- `files/archive/lautspiele-original/`: unveränderter früherer Datei- und Codebestand.
- `files/archive/Logospiele.xlsx`: unveränderte frühere Berechnungsarbeitsmappe.

Das Spielkürzel lautet `laut`. `symbols_k.csv` und `symbols_default.csv` sind die editierbaren Master. Der Builder erzeugt daraus die technischen CardMaker-Referenzen pro Modus und Bildsatz, weil CardMaker die jeweilige Kartenanzahl aus der Spalte `Count` liest.
