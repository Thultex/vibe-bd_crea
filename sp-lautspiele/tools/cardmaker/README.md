# Lautspiele – CardMaker

Das aktive Projekt ist für [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker) aufgebaut. Der Spielmodus steckt im Layout; jede auswählbare CSV steht für einen kompletten Laut-/Bildsatz. Größen, Positionen, Symbolauswahl, Ausblendung und Rotation werden in den JavaScript-Feldern der [`lautspiele.cmp`](lautspiele.cmp) berechnet und nicht als lange Hilfsspalten gespeichert.

## Dateien

| Datei/Ordner | Zweck |
|---|---|
| `lautspiele.cmp` | CardMaker-Projekt mit allen Layouts |
| `lautspiele_defines.csv` | bewusst leere technische Kopfzeile für CardMaker |
| `symbols_default.csv`, `symbols_k.csv` | direkt auswählbare Bildsatz-Konfigurationen für alle Layouts |
| `images/symbols/default/` | neutraler Standardsatz `01.png` bis `10.png` |
| `images/symbols/k/` | aktueller K-Laut-Satz `01.png` bis `10.png` |
| `images/ui/` | Oberflächenbilder des bestehenden Designs |
| `build_lautspiele_project.py` | erzeugt CSVs und CMP reproduzierbar neu |
| `validate_lautspiele_project.py` | prüft Struktur und Kombinatorik |

## Konfiguration pro Bildsatz

| Spalte | Bedeutung |
|---|---|
| `symbol_set` | kurzer Name des Bildsatzes |
| `symbol_folder` | relativer Ordner des gewünschten Bildsatzes |
| `symbol_names` | Namen aller nummerierten Symbole, durch `|` getrennt |
| `symbol_scale_map` | Größenfaktoren aller nummerierten Symbole, durch `|` getrennt |
| `<modus>_start` / `<modus>_end` | inklusive Ringgrenzen für Gruselino, Domino oder Dobble |
| `<modus>_shift` | zyklischer Versatz des jeweiligen Modus |

Alle Informationen eines Bildsatzes stehen in genau einer Zeile. Standardmäßig verweisen alle vier Layouts auf `symbols_k.csv`. In CardMaker kann die Referenz eines Layouts auf `symbols_default.csv` oder eine weitere gleich aufgebaute Symbol-CSV gewechselt werden. So wechselt der Laut-/Bildsatz, ohne eine zusätzliche Modus-CSV zu benötigen. Die Kartenanzahlen 11, 10 und 7 sind Eigenschaften der Layouts.

## Größenkorrektur

Neben dem Projekt liegt pro Bildsatz eine eindeutig benannte Tabelle: `symbols_default.csv` gehört zum Ordner `images/symbols/default`, `symbols_k.csv` zu `images/symbols/k`. Namen, Größenkorrekturen, Ordner und Modusbereiche stehen gemeinsam in dieser einen CSV. Die aktuellen zehn Werte stammen aus der alten Arbeitsmappe. In v1.02 ist `default` zunächst eine unabhängige Kopie des K-Satzes und darf später abweichend gepflegt werden.

CardMaker sucht automatisch nach `lautspiele_defines.csv`. Die Datei enthält absichtlich nur `define,value`: fachliche Daten stehen dort nicht mehr. Dadurch wird CardMakers fehlende-Defines-Meldung unterdrückt, ohne globale Werte oder Duplikate zu erzeugen.

## Spiellogik

- **Gruselino:** Das Layout erzeugt eine Übersicht mit allen zehn Symbolen und zehn Spielkarten. Auf jeder Spielkarte fehlt genau eine andere Position. `gruselino_shift=1` verschiebt das 10er-Fenster um ein Symbol; bei einem Ring 1–12 werden dadurch beispielsweise 2–11 verwendet.
- **Domino:** `domino_start` und `domino_end` bestimmen den Ring. Jede Karte zeigt ein Symbol und seinen zyklischen Nachfolger; die letzte Karte führt wieder zum ersten Symbol. Die unveränderte Grafik wird mittig größenkorrigiert und anschließend als gesamtes Element zufällig gedreht.
- **Dobble:** Die kompakte Variante nutzt sieben ausgewählte Symbole, sieben Karten und drei Symbole pro Karte. Jedes Kartenpaar teilt exakt ein Symbol. Das Layout entspricht ungefähr der Gruselino-Papierkarte und lässt sich über CardMakers PDF-Ausgabe auf A4 platzieren.

Gruselino- und Dobble-Symbole variieren zur Laufzeit um ±5 % und werden um 0–359° gedreht. Die Grundpositionen und Grundgrößen bleiben direkt im CardMaker-Editor editierbar.

## Erzeugen und prüfen

```powershell
python build_lautspiele_project.py
python validate_lautspiele_project.py
```

CardMaker-Version des Werkzeugstands: v1.02.
