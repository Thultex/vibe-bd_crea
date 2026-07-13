# Lautspiele – CardMaker

Das aktive Projekt ist für [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker) aufgebaut. Alle vier Layouts lesen dieselbe kleine Konfigurationsdatei [`lautspiele.csv`](lautspiele.csv). Größen, Positionen, Symbolauswahl, Ausblendung und Rotation werden in den JavaScript-Feldern der [`lautspiele.cmp`](lautspiele.cmp) berechnet und nicht als lange Hilfsspalten gespeichert.

## Dateien

| Datei/Ordner | Zweck |
|---|---|
| `lautspiele.cmp` | CardMaker-Projekt mit allen Layouts |
| `lautspiele.csv` | gemeinsame Konfiguration für Gruselino, Domino und Dobble |
| `lautspiele_defines.csv` | globale Größenkorrektur und Symbolnamen (CardMaker-Defines) |
| `images/symbols/default/` | Standard-Symbolsatz `01.png` bis `10.png` |
| `images/ui/` | Oberflächenbilder des bestehenden Designs |
| `build_lautspiele_project.py` | erzeugt CSVs und CMP reproduzierbar neu |
| `validate_lautspiele_project.py` | prüft Struktur und Kombinatorik |

## Gemeinsame Konfiguration

| Spalte | Bedeutung |
|---|---|
| `Count` | von CardMaker zu erzeugende Kartenanzahl |
| `allowed_layout` | Layout oder Layouts, für die die Zeile gilt |
| `mode` | `gruselino`, `domino` oder `dobble` |
| `symbol_folder` | relativer Ordner des gewünschten Bildsatzes |
| `symbol_start` / `symbol_end` | inklusive Ringgrenzen des verfügbaren Symbolsatzes |
| `symbol_shift` | zyklischer Versatz innerhalb dieses Rings |

Mehrere CSVs können dieselben Layouts mit anderen `symbol_folder`-Werten verwenden. Zum Wechseln wird in CardMaker die Referenzdatei ersetzt oder eine Kopie der Konfiguration unter dem erwarteten Namen verwendet.

## Größenkorrektur

`lautspiele_defines.csv` enthält 50 vorbereitete Definitionen. Die ersten zehn Werte stammen aus der alten Arbeitsmappe. Jede Zeile verbindet ID, Faktor und lesbaren Namen. Weitere Bildsätze können zusätzliche IDs verwenden, ohne die Tabellenform zu ändern.

## Spiellogik

- **Gruselino:** `Count=11` erzeugt eine Übersicht mit allen zehn Symbolen und zehn Spielkarten. Auf jeder Spielkarte fehlt genau eine andere Position. `symbol_shift=1` verschiebt das 10er-Fenster um ein Symbol; bei einem Ring 1–12 werden dadurch beispielsweise 2–11 verwendet.
- **Domino:** Start und Ende bestimmen den Ring. Jede Karte zeigt ein Symbol und seinen zyklischen Nachfolger; die letzte Karte führt wieder zum ersten Symbol. `Count` muss der Ringlänge entsprechen. Die unveränderte Grafik wird mittig größenkorrigiert und anschließend als gesamtes Element zufällig gedreht.
- **Dobble:** Die kompakte Variante nutzt sieben ausgewählte Symbole, sieben Karten und drei Symbole pro Karte. Jedes Kartenpaar teilt exakt ein Symbol. Das Layout entspricht ungefähr der Gruselino-Papierkarte und lässt sich über CardMakers PDF-Ausgabe auf A4 platzieren.

Gruselino- und Dobble-Symbole variieren zur Laufzeit um ±5 % und werden um 0–359° gedreht. Die Grundpositionen und Grundgrößen bleiben direkt im CardMaker-Editor editierbar.

## Erzeugen und prüfen

```powershell
python build_lautspiele_project.py
python validate_lautspiele_project.py
```

CardMaker-Version des Werkzeugstands: v1.00.
