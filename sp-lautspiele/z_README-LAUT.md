# Lautspiele

Lautspiele bündelt bildbasierte Sprachspiele, die aus einem gemeinsamen Symbolsatz erzeugt werden. Der aktuelle Werkzeugstand umfasst Gruselino Papier, ein doppelt nutzbares Memory-/Domino-Papiermodul und eine kompakte perfekte Dobble-Variante.

## Struktur

- `anleitung_laut.md`: kurze Spiel- und Materialübersicht.
- `design_laut.md`: technische Regeln für Symbolauswahl, Verschiebung und Layouts.
- `tools/cardmaker/`: aktives Generatorprojekt für [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker).
- `tools/cardmaker/generators/symbols_download_arasaac.py`: lädt nummerierte ARASAAC-PNGs und Quellen aus einfachen Wortlisten.
- `tools/cardmaker/generators/symbols_generate_sets.py`: erzeugt dieselben CSVs ohne Netzwerk aus einer Namensliste und vorhandenen nummerierten PNGs.
- `tools/cardmaker/generators/symbol_names.csv`: Beispiel für das gemeinsame Eingabeformat.
- `tools/cardmaker/generators/symbol_ids.csv`: leere Vorlage für den direkten Abruf bekannter ARASAAC-IDs.
- `tools/cardmaker/generators/GENERATORS_README.md`: ausführliche Anleitung für Download, lokale Set-Erzeugung und CardMaker-Build.
- `files/archive/lautspiele-original/`: unveränderter früherer Datei- und Codebestand.
- `files/archive/Logospiele.xlsx`: unveränderte frühere Berechnungsarbeitsmappe.

Das Spielkürzel lautet `laut`. `symbols_k.csv` und `symbols_default.csv` sind die editierbaren Master. Der Builder erzeugt daraus die technischen CardMaker-Referenzen pro Modus und Bildsatz, weil CardMaker die jeweilige Kartenanzahl aus der Spalte `Count` liest.
