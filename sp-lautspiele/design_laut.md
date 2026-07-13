# Design Lautspiele

## Gemeinsames Datenmodell

Der Spielmodus ist durch das CardMaker-Layout festgelegt. Jeder Bildsatz besitzt eine editierbare Master-CSV mit Bildordner, Namen, Größenwertfolge, Verfügbarkeit sowie Start-, End- und Verschiebungswerten für Gruselino, Memory, Domino und Dobble. Drehung, Position, Ausblendung und Nachbarschaft werden im jeweiligen CardMaker-Feld berechnet.

Die fachliche Größenkorrektur steht in einer nach dem Bildsatz benannten Tabelle neben dem CardMaker-Projekt: `symbols_default.csv` gehört zu `images/symbols/default`, `symbols_k.csv` zu `images/symbols/k`. Weil CardMaker die Kartenanzahl nur über `Count` in der Referenz steuert, erzeugt der Builder daraus technische Modusdateien wie `gruselino_k.csv`. Diese spiegeln den Master vollständig und ergänzen nur `Count`. Globale CardMaker-Defines werden dafür nicht benutzt.

`generate_symbol_set.py` ist die gemeinsame Grenze zwischen Bildbeschaffung und Layoutdaten. Es zählt ausschließlich lückenlose Hauptdateien `01.png`, `02.png` usw., übernimmt die erste Spalte der Namensliste und aktualisiert Master plus Modusdateien. `import_arasaac_symbols.py` beschafft Bilder und Quellen und delegiert danach an diese Funktion.

## Gruselino

- Ein aktiver Satz umfasst acht Symbole.
- Vier Grundkarten zeigen alle acht Symbole.
- Die folgenden acht Suchkarten blenden jeweils ein anderes Symbol aus und zeigen sieben.
- Reihenfolge und Rotation werden je Karte zufällig variiert, die historischen acht Positionen bleiben fest.
- `gruselino_shift` verschiebt das aktive Achterfenster zyklisch im durch Start und Ende definierten Ring.
- Symbole werden um bis zu fünf Prozent vergrößert oder verkleinert und vollständig zufällig gedreht.

## Memory

- Start und Ende bestimmen den inklusiven Symbolbereich.
- Jede Symbol-ID wird auf zwei aufeinanderfolgenden Karten ausgegeben.
- Memory verändert weder Größenkorrektur noch Ausrichtung zufällig.

## Domino

- Start und Ende bestimmen den inklusiven Symbolring.
- Karte `n` zeigt Ringelement `n` und dessen Nachfolger.
- Das letzte Symbol wird mit dem ersten verbunden.
- Die Quelldateien bleiben unverschoben und ungedreht; CardMaker korrigiert die Größe mittig und dreht anschließend das gesamte Graphic-Element.

## Dobble

- Die kompakte Version verwendet die projektive Ebene der Ordnung 5.
- 31 Symbole bilden 31 Karten mit jeweils sechs Symbolen.
- Zwei Karten besitzen immer genau ein gemeinsames Symbol.
- Nicht vorhandene nummerierte PNGs werden über `symbol_available_map` leer gelassen.
- Die Grundfläche entspricht ungefähr dem Gruselino-Papierlayout und kann über CardMakers PDF-Ausgabe auf A4 ausgeschossen werden.

## Dateiregeln

Aktive Generatorbilder liegen beim Tool, weil sie unmittelbar zur Ausführung gehören. Sonstige Medien gehören künftig unter `assets/`, allgemeine Dateien unter `files/` und ausführbare Hilfen unter `tools/`.
