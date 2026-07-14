# Lautspiele

Lautspiele bündelt bildbasierte Sprachspiele, die aus einem gemeinsamen Symbolsatz erzeugt werden. Der aktuelle Werkzeugstand umfasst Gruselino, ein doppelt nutzbares Memory- und Domino-Modul, eine kompakte perfekte Dobble-Variante, einen A4-Spielplan und 4x4-Bingo.

## Struktur

- `anleitung_laut.md`: kurze Spiel- und Materialübersicht.
- `design_laut.md`: technische Regeln für Symbolauswahl, Verschiebung und Layouts.
- `tools/cardmaker/`: aktives Generatorprojekt für [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker).
- `tools/cardmaker/scripts/generate/symbols_download_arasaac.py`: lädt nummerierte ARASAAC-PNGs und Quellen aus einfachen Wortlisten.
- `tools/cardmaker/scripts/generate/symbols_generate_sets.py`: erzeugt dieselben CSVs ohne Netzwerk aus einer Namensliste und vorhandenen nummerierten PNGs.
- `tools/cardmaker/scripts/generate/symbol_names.csv`: Beispiel für das gemeinsame Eingabeformat.
- `tools/cardmaker/scripts/generate/symbol_ids.csv`: leere Vorlage für den direkten Abruf bekannter ARASAAC-IDs.
- `tools/cardmaker/scripts/build/`: Builder und Validator; die jeweilige `build.ini` liegt beim Bildsatz.
- `tools/cardmaker/scripts/SCRIPTS_README.md`: ausführliche Anleitung für Download, lokale Set-Erzeugung, Build und Prüfung.
- `files/archive/lautspiele-original/`: unveränderter früherer Datei- und Codebestand.
- `files/archive/Logospiele.xlsx`: unveränderte frühere Berechnungsarbeitsmappe.

Das Spielkürzel lautet `laut`. Namen, Größen und Auswahl stehen in `images/symbols/<satz>/symbols.csv` und `build.ini`. Der Builder erzeugt daraus Master und technische CardMaker-Referenzen pro Modus und Bildsatz, weil CardMaker die jeweilige Kartenanzahl aus der Spalte `Count` liest.
