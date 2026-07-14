# Lautspiele – CardMaker

Das aktive Projekt ist für [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker) aufgebaut. Der Spielmodus steckt im Layout; jede auswählbare CSV steht für einen kompletten Laut-/Bildsatz. Größen, Positionen, Symbolauswahl, Ausblendung und Rotation werden in den JavaScript-Feldern der [`lautspiele.cmp`](lautspiele.cmp) berechnet und nicht als lange Hilfsspalten gespeichert.

## Dateien

| Datei/Ordner | Zweck |
|---|---|
| `lautspiele.cmp` | CardMaker-Projekt mit allen Layouts |
| `symbols_default.csv`, `symbols_k.csv` | erzeugte CardMaker-Master je Bildsatz |
| `<modus>_<satz>.csv` | fünf automatisch erzeugte CardMaker-Referenzen mit technischem `Count` |
| `images/symbols/default/` | neutraler Standardsatz `01.png` bis `10.png` |
| `images/symbols/k/` | aktueller K-Laut-Satz `01.png` bis `10.png` |
| `images/symbols/<satz>/symbols.csv` | maßgebliche Namen und Größenfaktoren des Bildsatzes |
| `images/ui/` | Oberflächenbilder des bestehenden Designs |
| `scripts/build/build_lautspiele_files.py` | erzeugt CSVs und CMP reproduzierbar neu |
| `scripts/build/validate_lautspiele_project.py` | prüft Struktur und Kombinatorik |
| `images/symbols/<satz>/build.ini` | Auswahl von Startsymbol und Symbolanzahl dieses Satzes (`-1` = automatisch alle) |
| `scripts/generate/symbols_generate_sets.py` | erzeugt Master- und Modus-CSVs aus Namen und vorhandenen Bildern |
| `scripts/generate/symbols_download_arasaac.py` | lädt ARASAAC-Bilder/Quellen und ruft den Set-Generator auf |
| `scripts/generate/symbol_names.csv` | Beispiel und reproduzierbare Suchliste für einen Bildsatz |
| `scripts/generate/symbol_ids.csv` | leere Vorlage für den direkten Download bekannter ARASAAC-IDs |
| `scripts/SCRIPTS_README.md` | ausführliche Bedienung aller Build-, Prüf- und Erzeugungsskripte |

## Konfiguration pro Bildsatz

| Spalte | Bedeutung |
|---|---|
| `symbol_set` | kurzer Name des Bildsatzes |
| `symbol_folder` | relativer Ordner des gewünschten Bildsatzes |
| `symbol_count` | Zahl der benannten Symbole |
| `symbol_names` | Namen aller nummerierten Symbole, durch `|` getrennt |
| `symbol_scale_map` | Größenfaktoren aller nummerierten Symbole, durch `|` getrennt |
| `symbol_available_map` | `1`/`0` je ID; fehlende Bilddateien bleiben im Layout leer |
| `<modus>_start` / `<modus>_end` | inklusive Auswahlgrenzen für Gruselino, Domino, Dobble, Spielplan oder Bingo |
| `<modus>_shift` | zyklischer Versatz des jeweiligen Modus |

Namen und Größenkorrekturen werden direkt beim Bildsatz in `images/symbols/<satz>/symbols.csv` gepflegt. Der Builder spiegelt sie in die kompakte Master-Zeile, aus der er fünf technische CardMaker-Referenzen ableitet: `gruselino`, `domino`, `dobble`, `spiel` und `bingo`. Memory und Domino verwenden gemeinsam `domino_k.csv`. Jedes Layout bindet automatisch alle vorhandenen Satz-CSVs seines Modus ein; der Bildsatz kann daher direkt in CardMaker zwischen `default`, `k` und später ergänzten Sätzen gewechselt werden. Der K-Satz ist zunächst als Standard markiert. Der Layout-Standardcount bleibt wie im Original bei `1`; die tatsächliche Ausgabezahl kommt aus der gewählten Modus-CSV. Bei Memory/Domino entspricht sie automatisch der Länge von `domino_start` bis `domino_end`. Master- und Modusdateien werden nicht von Hand gepflegt.

Das Symbolfenster wird je Bildsatz in `images/symbols/<satz>/build.ini` eingestellt. `start_symbol = 1` beginnt bei `01.png`; `symbol_count = -1` übernimmt automatisch alle ab dort vorhandenen Hauptsymbole. Ein positiver Count begrenzt die Auswahl. Generator und Builder legen die Datei bei Bedarf mit diesen Standardwerten an. Der Builder schreibt das Fenster in alle Start-/Endfelder, während die modusspezifischen Shifts in den erzeugten Master-CSVs erhalten bleiben. Mindestens acht Symbole sind für Gruselino erforderlich.

## Größenkorrektur

Jeder Bildordner enthält eine einfache Tabelle `symbols.csv` mit `symbol_id,name,scale`. Sie ist die Quelle für Symbolname und Größenkorrektur; `scale = 1.00` bedeutet unverändert. Die aktuellen zehn Korrekturen wurden aus der alten Arbeitsmappe übernommen. Neue Bildsätze erhalten für alle Hauptbilder zunächst `1.00`. Nach einer manuellen Korrektur dieser ordnerlokalen Datei wird der Builder erneut ausgeführt. `symbols_default.csv` und `symbols_k.csv` spiegeln diese Werte lediglich für CardMaker und enthalten zusätzlich Ordner, Verfügbarkeit und Modusbereiche.

## ARASAAC-Bildsatz erzeugen

Die Wortliste ist eine UTF-8-Textdatei ohne Kopfzeile. Pro Zeile sind folgende Formen erlaubt:

```text
Käse
Stecker,electrical plug
Katze,cat,2
Keks,,2
```

Das dritte Feld gibt die Zahl zusätzlicher Kandidaten **je vorhandener Sprache** an. Der beste deutsche Treffer wird als `01.png` verwendet. Weitere deutsche Treffer heißen `01-d1.png`, `01-d2.png` usw.; englische Alternativen heißen `01-e1.png`, `01-e2.png` usw. Doppelte ARASAAC-IDs werden übersprungen. Dadurch kann später eine Alternative durch einfaches Umbenennen zur Hauptdatei gemacht werden.

```powershell
python scripts/generate/symbols_download_arasaac.py scripts/generate/symbol_names.csv --set-name k --force
```

Der Satzname bestimmt automatisch:

- `images/symbols/<satz>/` für Bilder und `ATTRIBUTION.md`
- `symbols_<satz>.csv` als editierbarer Master
- fünf `<modus>_<satz>.csv` als direkt auswählbare CardMaker-Referenzen
- `symbols_<satz>_sources.csv` mit ARASAAC-IDs, Suchsprache und Quelllinks

Ohne `--set-name` wird der Dateiname der Wortliste verwendet. Bestehende Ausgaben werden nur mit `--force` ersetzt. Neu erzeugte Größenfaktoren beginnen in `images/symbols/<satz>/symbols.csv` bei `1.00`; vorhandene manuelle Korrekturen bleiben bei einem erneuten Lauf erhalten.

Sind die gewünschten ARASAAC-IDs bereits bekannt, werden sie ohne Suche zeilenweise in `scripts/generate/symbol_ids.csv` eingetragen. Der Downloader erkennt diesen Dateinamen, lädt jede ID direkt, übernimmt den ersten deutschen API-Begriff als Symbolnamen und erzeugt dieselben Bilder, Quellen- und Set-Dateien:

```powershell
python scripts/generate/symbols_download_arasaac.py scripts/generate/symbol_ids.csv --set-name mein-satz --force
```

## Vorhandenen Bildordner anbinden

Der unabhängige CSV-Generator kann auch ohne ARASAAC verwendet werden. Die erste Spalte der Namensliste enthält die Anzeigenamen; weitere Spalten werden ignoriert. Im Bildordner zählen nur lückenlos nummerierte Hauptdateien `01.png`, `02.png` usw. Dateien wie `01-d1.png` sind Alternativen und erhöhen die Symbolzahl nicht.

```powershell
python scripts/generate/symbols_generate_sets.py scripts/generate/symbol_names.csv images/symbols/k --set-name k --force
```

Der Ordnername ist ohne `--set-name` zugleich der Satzname. Namen werden aus der Namensliste übernommen; vorhandene Größenkorrekturen aus der ordnerlokalen `symbols.csv` und Modus-Shifts bleiben beim bewussten Neuerzeugen erhalten. Danach sind Manifest, Master und alle fünf technischen Modus-CSVs aktuell. Der ARASAAC-Importer benutzt intern genau dieselbe Funktion.

## Spiellogik

- **Gruselino:** Vier Grundkarten zeigen dieselben acht Symbole. 28 Suchkarten zeigen diese Symbole jeweils vertauscht; auf jeder Suchkarte fehlt zyklisch genau eines. Die insgesamt 32 Karten entsprechen dem belegten Count aus `Logospiele.xlsx`. Die historischen Positionen bleiben erhalten, die Symbolflächen sind um 20 % verkleinert und drehen nur um ±20°. `gruselino_shift` verschiebt das aktive 8er-Fenster zyklisch.
- **Memory + Domino:** Ein Modul enthält zwei klar getrennte, abgerundete 560er Kartenkästchen aus dem Original und dazwischen die ursprüngliche 22-Pixel-Schnittzone. Verbunden bilden aufeinanderfolgende Symbole den Domino-Ring. Getrennt kommt durch den geschlossenen Ring jedes Symbol zweimal vor und bildet ein Memory-Set. Es gibt keine Zufallsdrehung oder -skalierung.
- **Dobble:** Das nächstkleinere perfekte System unterhalb der 8er-Karten nutzt 31 Symbole, 31 Karten und sechs Symbole pro Karte. Jedes Kartenpaar teilt exakt ein Symbol. Bei kleineren Bildsätzen bleiben nicht vorhandene IDs leer. Größere Symbolflächen stehen etwas kompakter, bleiben selbst bei der Größenvarianz von ±18 % aber ohne starke Überdeckung. Die Karte besitzt abgerundete Ecken.
- **Minimalspiel A4:** Ein statischer Laufweg verbindet zehn rote, weiß hinterlegte Symbolstationen. Sehr hellgraue normale Felder liegen vor den Sprungpfeilen; die zwei klar hellrot markierten Ausgangsfelder kennzeichnen Rücksprünge. Kleine Felder halten Abstand zu den Symbolstationen, das Ziel steht frei. Zwei grüne Vorwärtssprünge von Symbolstationen (+8/+9), zwei rote Rücksprünge auf normale Felder (-4/-6) und ein doppelt umkreistes Ziel bilden ein einfaches Leiterspiel. Das Layout ist proportional auf CardMakers A4-Nutzfläche `2250 × 3150 px` skaliert.
- **Bingo 4x4:** Vier vollständige Karten verwenden denselben Bestand von 16 Symbolfeldern in reproduzierbar verschiedenen Anordnungen. Mindestens acht Bilder sind erforderlich. Bei 8–15 Bildern wird der Bestand zyklisch aufgefüllt; auf den ersten beiden Karten teilen gleiche Bilder keine horizontale, vertikale oder diagonale Gewinnlinie. Jede Karte ist eine halbe A4-Seite, sodass zwei Karten pro PDF-Seite stehen. Eine der vier Karten kann an den Rasterlinien als Ziehkärtchen zerschnitten werden.

Gruselino variiert zur Laufzeit um ±5 % in der Größe und ±20° in der Drehung. Dobble variiert um ±18 % und 0–359°. Die Grundpositionen und Grundgrößen bleiben direkt im CardMaker-Editor editierbar.

Die PDF-Exportflächen übernehmen die historischen Werte: `7860 × 7602` für Gruselino und Dobble sowie `2362 × 7400` für Memory+Domino. Das Doppelmodul bleibt originalgetreu `1181 × 590 px` groß; daraus zeigt CardMakers Layout-Export wie im Original `2` Stitched Columns und `12` Stitched Rows. Diese Stitched-Werte steuern jedoch nicht den direkten PDF-Seitenumbruch. Damit dort zwei Module beziehungsweise vier getrennte Memory-Karten nebeneinander passen, werden in CardMakers globalen PDF-Einstellungen A4 (`210 × 297 mm`) und horizontale wie vertikale Ränder von `5 mm` verwendet. Bei `0,5″` Standardrand steht mit `540 pt` zu wenig Breite für die benötigten rund `566,9 pt` zur Verfügung. Zoom `0.6081989` und die ursprüngliche Crop-Definition bleiben erhalten.

## Erzeugen und prüfen

```powershell
python scripts/build/build_lautspiele_files.py
python scripts/build/validate_lautspiele_project.py
```

CardMaker-Version des Werkzeugstands: v1.09. `symbols_generate_sets`: v1.04. `symbols_download_arasaac`: v1.02.
