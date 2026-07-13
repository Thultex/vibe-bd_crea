# Design Lautspiele

## Gemeinsames Datenmodell

Alle Layouts lesen dieselbe Konfigurations-CSV. Sie enthält ausschließlich Kartenanzahl, Layoutfilter, Modus, Symbolordner, Start, Ende und Verschiebung. Drehung, Größenkorrektur, Position, Ausblendung und Nachbarschaft werden im jeweiligen CardMaker-Feld berechnet.

Die Größenkorrektur steht separat in `tools/cardmaker/lautspiele_defines.csv`. Sie verbindet jede Symbol-ID mit einem Namen und einem Faktor. Dadurch können mehrere Konfigurations-CSVs auf unterschiedliche, gleich nummerierte Ordner verweisen und trotzdem dieselben Layouts verwenden.

## Gruselino

- Ein aktiver Satz umfasst zehn Symbole.
- Karte 1 ist die Übersicht und zeigt alle zehn.
- Die folgenden zehn Karten blenden jeweils ein anderes Symbol aus und zeigen neun.
- `symbol_shift` verschiebt das aktive Zehnerfenster zyklisch im durch Start und Ende definierten Ring.
- Symbole werden um bis zu fünf Prozent vergrößert oder verkleinert und vollständig zufällig gedreht.

## Domino

- Start und Ende bestimmen den inklusiven Symbolring.
- Karte `n` zeigt Ringelement `n` und dessen Nachfolger.
- Das letzte Symbol wird mit dem ersten verbunden.
- Die Quelldateien bleiben unverschoben und ungedreht; CardMaker korrigiert die Größe mittig und dreht anschließend das gesamte Graphic-Element.

## Dobble

- Die erste Version verwendet die projektive Ebene der Ordnung 2.
- Sieben Symbole bilden sieben Karten mit jeweils drei Symbolen.
- Zwei Karten besitzen immer genau ein gemeinsames Symbol.
- Die Grundfläche entspricht ungefähr dem Gruselino-Papierlayout und kann über CardMakers PDF-Ausgabe auf A4 ausgeschossen werden.

## Dateiregeln

Aktive Generatorbilder liegen beim Tool, weil sie unmittelbar zur Ausführung gehören. Sonstige Medien gehören künftig unter `assets/`, allgemeine Dateien unter `files/` und ausführbare Hilfen unter `tools/`.
