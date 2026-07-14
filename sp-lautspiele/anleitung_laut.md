# Anleitung Lautspiele v1.00

Lautspiele verwendet nummerierte Bildsymbole für mehrere bekannte Such- und Zuordnungsspiele.

## Gruselino

Vier Grundkarten zeigen dieselben acht Symbole. Auf jeder der acht Suchkarten fehlt genau eines davon; Position, Reihenfolge und Drehung variieren. Die Spielenden vergleichen die Karten und nennen oder markieren das fehlende Symbol.

## Memory / Domino Papier

Jedes Druckmodul enthält zwei verbundene Karten mit aufeinanderfolgenden Symbolen. Verbunden werden die Module als Domino aneinandergelegt; die Folge schließt sich vom letzten Symbol wieder zum ersten. Werden alle Module an der weißen Mitte getrennt, kommt durch diesen geschlossenen Ring jedes Symbol genau zweimal vor und die Einzelkarten können als Memory gespielt werden.

## Dobble

Zwei beliebige Karten besitzen genau ein gemeinsames Symbol. Wer es zuerst entdeckt und benennt, gewinnt die Karte oder einen Punkt. Die konkrete Rundenwertung kann an Alter und Sprachziel angepasst werden.

## Minimalspiel A4

Die Spielfigur folgt dem Weg vom gelben Start zum doppelt umkreisten Ziel. Rote Symbolstationen können für Benenn-, Laut- oder Satzaufgaben verwendet werden. Grüne Pfeile führen ausschließlich von einer Symbolstation acht oder neun Felder vorwärts; rote Pfeile setzen vier oder sechs Felder zurück.

## Bingo 4x4

Vier Bingokarten zeigen denselben Symbolbestand in unterschiedlicher Anordnung. Zwei Karten passen auf eine A4-Seite. Eine der vollständigen Karten kann entlang des 4x4-Rasters zerschnitten und als Ziehsatz verwendet werden. Gewonnen hat, wer zuerst eine vereinbarte Reihe, Spalte, Diagonale oder die ganze Karte markiert hat.

## Material erzeugen

Das CardMaker-Projekt liegt unter `tools/cardmaker/`. Die editierbaren Master heißen `symbols_k.csv` und `symbols_default.csv`. Der Builder erzeugt daraus die CardMaker-Referenzen für Gruselino, Memory/Domino, Dobble, Minimalspiel und Bingo mit der jeweils nötigen Kartenanzahl. In jedem Layout sind alle vorhandenen Bildsätze als Referenzen angeschlossen und können direkt in CardMaker gewechselt werden; `k` ist der Standard. Danach wird das gewünschte Layout als Bilder oder PDF exportiert.

Neue Laut-/Bildsätze können dort mit `scripts/generate/symbols_download_arasaac.py` aus einer Wortliste geladen werden. Eine Zeile `Katze,cat,2` lädt neben dem deutschen Hauptbild zusätzliche deutsche und englische Kandidaten, die vor dem Druck durch Umbenennen ausgewählt werden können. Bekannte ARASAAC-IDs können stattdessen direkt in `scripts/generate/symbol_ids.csv` eingetragen werden. Für bereits vorhandene, als `01.png`, `02.png` usw. nummerierte Bilder erzeugt `scripts/generate/symbols_generate_sets.py` dieselben CSVs ohne Netzwerkabruf. Vorlagen liegen als `scripts/generate/symbol_names.csv` und `scripts/generate/symbol_ids.csv` bei.
