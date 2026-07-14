# Lautspiele – CardMaker

Das aktive Projekt ist für [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker) aufgebaut. Der Spielmodus steckt im Layout; jede auswählbare CSV steht für einen kompletten Laut-/Bildsatz. Größen, Positionen, Symbolauswahl, Ausblendung und Rotation werden in den JavaScript-Feldern der [`lautspiele.cmp`](lautspiele.cmp) berechnet und nicht als lange Hilfsspalten gespeichert.

## Dateien

| Datei/Ordner | Zweck |
|---|---|
| `lautspiele.cmp` | CardMaker-Projekt mit allen Layouts |
| `lautspiele_defines.csv` | bewusst leere technische Kopfzeile für CardMaker |
| `symbols_default.csv`, `symbols_k.csv` | editierbare Master-Konfigurationen je Bildsatz |
| `<modus>_<satz>.csv` | fünf automatisch erzeugte CardMaker-Referenzen mit technischem `Count` |
| `images/symbols/default/` | neutraler Standardsatz `01.png` bis `10.png` |
| `images/symbols/k/` | aktueller K-Laut-Satz `01.png` bis `10.png` |
| `images/ui/` | Oberflächenbilder des bestehenden Designs |
| `scripts/build/build_lautspiele_files.py` | erzeugt CSVs und CMP reproduzierbar neu |
| `scripts/build/validate_lautspiele_project.py` | prüft Struktur und Kombinatorik |
| `scripts/build/build.ini` | gemeinsame Auswahl von Startsymbol und Symbolanzahl (`-1` = automatisch alle) |
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

Alle fachlich editierbaren Informationen eines Bildsatzes stehen in genau einer Master-Zeile. CardMaker benötigt seine Kartenanzahl jedoch in einer Spalte `Count`. Der Builder leitet deshalb aus jedem Master fünf technische Referenzen ab: `gruselino`, `domino`, `dobble`, `spiel` und `bingo`. Memory und Domino verwenden gemeinsam `domino_k.csv`. Jedes Layout bindet automatisch alle vorhandenen Satz-CSVs seines Modus ein; der Bildsatz kann daher direkt in CardMaker zwischen `default`, `k` und später ergänzten Sätzen gewechselt werden. Der K-Satz ist zunächst als Standard markiert. Der Layout-Standardcount bleibt wie im Original bei `1`; die tatsächliche Ausgabezahl kommt aus der gewählten Modus-CSV. Bei Memory/Domino entspricht sie automatisch der Länge von `domino_start` bis `domino_end`. Abgeleitete Dateien werden nicht von Hand gepflegt.

Das gemeinsame Symbolfenster wird in `scripts/build/build.ini` eingestellt. `start_symbol = 1` beginnt bei `01.png`; `symbol_count = -1` übernimmt automatisch alle ab dort vorhandenen Hauptsymbole. Ein positiver Count begrenzt die Auswahl. Der Builder schreibt das Fenster in alle Start-/Endfelder, während die modusspezifischen Shifts in den Master-CSVs erhalten bleiben. Mindestens acht Symbole sind für Gruselino erforderlich.

## Größenkorrektur

Neben dem Projekt liegt pro Bildsatz eine eindeutig benannte Tabelle: `symbols_default.csv` gehört zum Ordner `images/symbols/default`, `symbols_k.csv` zu `images/symbols/k`. Namen, Größenkorrekturen, Ordner und Modusbereiche stehen gemeinsam in dieser einen CSV. Die aktuellen zehn Werte stammen aus der alten Arbeitsmappe. In v1.03 ist `default` zunächst eine unabhängige Kopie des K-Satzes und darf später abweichend gepflegt werden.

CardMaker sucht automatisch nach `lautspiele_defines.csv`. Die Datei enthält absichtlich nur `define,value`: fachliche Daten stehen dort nicht mehr. Dadurch wird CardMakers fehlende-Defines-Meldung unterdrückt, ohne globale Werte oder Duplikate zu erzeugen.

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

Ohne `--set-name` wird der Dateiname der Wortliste verwendet. Bestehende Ausgaben werden nur mit `--force` ersetzt. Neu erzeugte Größenfaktoren beginnen bei `1` und können danach in `symbol_scale_map` korrigiert werden.

Sind die gewünschten ARASAAC-IDs bereits bekannt, werden sie ohne Suche zeilenweise in `scripts/generate/symbol_ids.csv` eingetragen. Der Downloader erkennt diesen Dateinamen, lädt jede ID direkt, übernimmt den ersten deutschen API-Begriff als Symbolnamen und erzeugt dieselben Bilder, Quellen- und Set-Dateien:

```powershell
python scripts/generate/symbols_download_arasaac.py scripts/generate/symbol_ids.csv --set-name mein-satz --force
```

## Vorhandenen Bildordner anbinden

Der unabhängige CSV-Generator kann auch ohne ARASAAC verwendet werden. Die erste Spalte der Namensliste enthält die Anzeigenamen; weitere Spalten werden ignoriert. Im Bildordner zählen nur lückenlos nummerierte Hauptdateien `01.png`, `02.png` usw. Dateien wie `01-d1.png` sind Alternativen und erhöhen die Symbolzahl nicht.

```powershell
python scripts/generate/symbols_generate_sets.py scripts/generate/symbol_names.csv images/symbols/k --set-name k --force
```

Der Ordnername ist ohne `--set-name` zugleich der Satzname. Vorhandene Größenkorrekturen und Shifts werden beim bewussten Neuerzeugen soweit möglich beibehalten. Danach sind Master und alle fünf technischen Modus-CSVs aktuell. Der ARASAAC-Importer benutzt intern genau dieselbe Funktion.

## Spiellogik

- **Gruselino Papier:** Vier Grundkarten zeigen dieselben acht Symbole. Acht Suchkarten zeigen diese Symbole jeweils zufällig vertauscht; auf jeder Suchkarte fehlt genau ein anderes Symbol. Die historischen Positionen bleiben erhalten, die Symbolflächen sind um 20 % verkleinert und drehen nur um ±20°. `gruselino_shift` verschiebt das aktive 8er-Fenster zyklisch.
- **Memory / Domino Papier:** Ein Modul enthält zwei klar getrennte, abgerundete 560er Kartenkästchen aus dem Original und dazwischen die ursprüngliche 22-Pixel-Schnittzone. Verbunden bilden aufeinanderfolgende Symbole den Domino-Ring. Getrennt kommt durch den geschlossenen Ring jedes Symbol zweimal vor und bildet ein Memory-Set. Es gibt keine Zufallsdrehung oder -skalierung.
- **Dobble:** Das nächstkleinere perfekte System unterhalb der 8er-Karten nutzt 31 Symbole, 31 Karten und sechs Symbole pro Karte. Jedes Kartenpaar teilt exakt ein Symbol. Bei kleineren Bildsätzen bleiben nicht vorhandene IDs leer. Die Positionen nutzen die Kartenfläche weitläufig; die Größe variiert um ±18 %.
- **Minimalspiel A4:** Ein statischer Laufweg verbindet zehn rote Symbolstationen. Größere normale Felder, zwei grüne Vorwärtssprünge von Symbolstationen (+8/+9), zwei rote Rücksprünge (-4/-6) und ein doppelt umkreistes Ziel bilden ein einfaches Leiterspiel.
- **Bingo 4x4:** Vier vollständige Karten verwenden denselben Bestand von 16 Symbolfeldern in reproduzierbar verschiedenen Anordnungen. Jede Karte ist eine halbe A4-Seite, sodass zwei Karten pro PDF-Seite stehen. Eine der vier Karten kann an den Rasterlinien als Ziehkärtchen zerschnitten werden. Bei weniger als 16 ausgewählten Symbolen wird der Bestand zyklisch aufgefüllt.

Gruselino variiert zur Laufzeit um ±5 % in der Größe und ±20° in der Drehung. Dobble variiert um ±18 % und 0–359°. Die Grundpositionen und Grundgrößen bleiben direkt im CardMaker-Editor editierbar.

Die PDF-Exportflächen übernehmen die historischen Projektwerte: `7860 × 7602` für Gruselino und Dobble sowie `2362 × 7400` für Memory/Domino. Die Breite von `2362` entspricht exakt zwei 1181 Pixel breiten Doppelmodulen nebeneinander, also vier getrennten Memory-Karten. Auch Zoom `0.6081989` und die ursprüngliche Crop-Definition des Domino-Layouts werden übernommen.

## Erzeugen und prüfen

```powershell
python scripts/build/build_lautspiele_files.py
python scripts/build/validate_lautspiele_project.py
```

CardMaker-Version des Werkzeugstands: v1.08. `symbols_generate_sets`: v1.03. `symbols_download_arasaac`: v1.02.
