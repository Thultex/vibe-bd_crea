# Anleitung Lautspiele v1.00

Lautspiele verwendet nummerierte Bildsymbole für mehrere bekannte Such- und Zuordnungsspiele.

## Gruselino

Vier Grundkarten zeigen dieselben acht Symbole. Auf jeder der acht Suchkarten fehlt genau eines davon; Position, Reihenfolge und Drehung variieren. Die Spielenden vergleichen die Karten und nennen oder markieren das fehlende Symbol.

## Memory

Jedes ausgewählte Symbol kommt auf genau zwei Karten vor. Die Karten werden verdeckt ausgelegt und paarweise aufgedeckt.

## Domino

Jede Karte verbindet zwei aufeinanderfolgende Symbole. Die Karten werden so aneinandergelegt, dass gleiche Symbole zusammentreffen; die Folge schließt sich vom letzten Symbol wieder zum ersten.

## Dobble

Zwei beliebige Karten besitzen genau ein gemeinsames Symbol. Wer es zuerst entdeckt und benennt, gewinnt die Karte oder einen Punkt. Die konkrete Rundenwertung kann an Alter und Sprachziel angepasst werden.

## Material erzeugen

Das CardMaker-Projekt liegt unter `tools/cardmaker/`. Die editierbaren Master heißen `symbols_k.csv` und `symbols_default.csv`. Der Builder erzeugt daraus die CardMaker-Referenzen `gruselino_k.csv`, `memory_k.csv`, `domino_k.csv` und `dobble_k.csv` mit der jeweils nötigen Kartenanzahl. Danach wird das gewünschte Layout als Bilder oder PDF exportiert.

Neue Laut-/Bildsätze können dort mit `import_arasaac_symbols.py` aus einer Wortliste geladen werden. Eine Zeile `Katze,cat,2` lädt neben dem deutschen Hauptbild zusätzliche deutsche und englische Kandidaten, die vor dem Druck durch Umbenennen ausgewählt werden können. Für bereits vorhandene, als `01.png`, `02.png` usw. nummerierte Bilder erzeugt `generate_symbol_set.py` dieselben CSVs ohne Netzwerkabruf.
