# Design Lautspiele

## Gemeinsames Datenmodell

Der Spielmodus ist durch das CardMaker-Layout festgelegt. Jedes Layout liest eine frei auswählbare Bildsatz-CSV. Diese enthält Bildordner, Namen, Größenwertfolge sowie getrennte Start-, End- und Verschiebungswerte für Gruselino, Domino und Dobble. Drehung, Position, Ausblendung und Nachbarschaft werden im jeweiligen CardMaker-Feld berechnet.

Die fachliche Größenkorrektur steht in einer nach dem Bildsatz benannten Tabelle neben dem CardMaker-Projekt: `symbols_default.csv` gehört zu `images/symbols/default`, `symbols_k.csv` zu `images/symbols/k`. Die Tabelle ist zugleich die CardMaker-Referenz und verbindet den gesamten Bildsatz mit Namen, Faktoren und Moduseinstellungen. Dadurch können Layouts unterschiedliche, gleich nummerierte Bildsätze nutzen, ohne zusätzliche Modusdateien. Globale CardMaker-Defines werden dafür nicht benutzt.

## Gruselino

- Ein aktiver Satz umfasst zehn Symbole.
- Karte 1 ist die Übersicht und zeigt alle zehn.
- Die folgenden zehn Karten blenden jeweils ein anderes Symbol aus und zeigen neun.
- `gruselino_shift` verschiebt das aktive Zehnerfenster zyklisch im durch Start und Ende definierten Ring.
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
