# Design Lautspiele

## Gemeinsames Datenmodell

Der Spielmodus ist durch das CardMaker-Layout festgelegt. Jeder Bildsatz besitzt eine editierbare Master-CSV mit Bildordner, Namen, Größenwertfolge, Verfügbarkeit sowie Start-, End- und Verschiebungswerten für Gruselino, Domino und Dobble. Drehung, Position, Ausblendung und Nachbarschaft werden im jeweiligen CardMaker-Feld berechnet.

Die fachliche Größenkorrektur steht in einer nach dem Bildsatz benannten Tabelle neben dem CardMaker-Projekt: `symbols_default.csv` gehört zu `images/symbols/default`, `symbols_k.csv` zu `images/symbols/k`. Weil CardMaker die Kartenanzahl nur über `Count` in der Referenz steuert, erzeugt der Builder daraus technische Modusdateien wie `gruselino_k.csv`. Diese spiegeln den Master vollständig und ergänzen nur `Count`; für Memory/Domino wird dieser Wert aus der konfigurierten Symbolspanne berechnet. Alle zum Modus gehörenden Satz-CSVs werden am Layout angeschlossen. Globale CardMaker-Defines werden dafür nicht benutzt.

`symbols_generate_sets.py` ist die gemeinsame Grenze zwischen Bildbeschaffung und Layoutdaten. Es zählt ausschließlich lückenlose Hauptdateien `01.png`, `02.png` usw., übernimmt die erste Spalte der Namensliste und aktualisiert Master plus Modusdateien. `symbols_download_arasaac.py` beschafft Bilder und Quellen und delegiert danach an diese Funktion. `generators/symbol_names.csv` dokumentiert das gemeinsame Eingabeformat.

## Gruselino

- Ein aktiver Satz umfasst acht Symbole.
- Vier Grundkarten zeigen alle acht Symbole.
- Die folgenden acht Suchkarten blenden jeweils ein anderes Symbol aus und zeigen sieben.
- Reihenfolge und Rotation werden je Karte zufällig variiert, die historischen acht Positionen bleiben fest.
- `gruselino_shift` verschiebt das aktive Achterfenster zyklisch im durch Start und Ende definierten Ring.
- Die historischen Papierpositionen bleiben erhalten, ihre Grundgrößen sind um 20 Prozent reduziert.
- Symbole variieren zusätzlich um bis zu fünf Prozent und drehen nur um ±20 Grad.

## Memory / Domino Papier

- Start und Ende bestimmen den inklusiven Symbolring.
- Jedes Modul zeigt auf zwei verbundenen 560er Karten Ringelement `n` und dessen Nachfolger.
- Das letzte Symbol wird mit dem ersten verbunden.
- Die 22 Pixel breite weiße Mitte ist die Schnittzone.
- Verbunden dienen die Module als Domino; getrennt bilden die doppelt vorkommenden Symbole das Memory.
- Die Quelldateien bleiben unverschoben und ungedreht; CardMaker korrigiert nur die individuelle Grundgröße mittig.

## Dobble

- Die kompakte Version verwendet die projektive Ebene der Ordnung 5.
- 31 Symbole bilden 31 Karten mit jeweils sechs Symbolen.
- Zwei Karten besitzen immer genau ein gemeinsames Symbol.
- Nicht vorhandene nummerierte PNGs werden über `symbol_available_map` leer gelassen.
- Die sechs Positionen sind weit über die Papierkarte verteilt; die Größe variiert um ±18 Prozent.
- Die Grundfläche entspricht ungefähr dem Gruselino-Papierlayout und kann über CardMakers PDF-Ausgabe auf A4 ausgeschossen werden.

## Dateiregeln

Aktive Generatorbilder liegen beim Tool, weil sie unmittelbar zur Ausführung gehören. Sonstige Medien gehören künftig unter `assets/`, allgemeine Dateien unter `files/` und ausführbare Hilfen unter `tools/`.
