# Lautspiele – CardMaker

Das aktive Projekt ist für [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker) aufgebaut. Der Spielmodus steckt im Layout; jede auswählbare CSV steht für einen kompletten Laut-/Bildsatz. Größen, Positionen, Symbolauswahl, Ausblendung und Rotation werden in den JavaScript-Feldern der [`lautspiele.cmp`](lautspiele.cmp) berechnet und nicht als lange Hilfsspalten gespeichert.

## Dateien

| Datei/Ordner | Zweck |
|---|---|
| `lautspiele.cmp` | CardMaker-Projekt mit allen Layouts |
| `lautspiele_defines.csv` | bewusst leere technische Kopfzeile für CardMaker |
| `symbols_default.csv`, `symbols_k.csv` | editierbare Master-Konfigurationen je Bildsatz |
| `<modus>_<satz>.csv` | automatisch erzeugte CardMaker-Referenzen mit technischem `Count` |
| `images/symbols/default/` | neutraler Standardsatz `01.png` bis `10.png` |
| `images/symbols/k/` | aktueller K-Laut-Satz `01.png` bis `10.png` |
| `images/ui/` | Oberflächenbilder des bestehenden Designs |
| `generators/build_lautspiele_project.py` | erzeugt CSVs und CMP reproduzierbar neu |
| `validate_lautspiele_project.py` | prüft Struktur und Kombinatorik |
| `generators/symbols_generate_sets.py` | erzeugt Master- und Modus-CSVs aus Namen und vorhandenen Bildern |
| `generators/symbols_download_arasaac.py` | lädt ARASAAC-Bilder/Quellen und ruft den Set-Generator auf |
| `generators/symbol_names.csv` | Beispiel und reproduzierbare Suchliste für einen Bildsatz |
| `generators/GENERATORS_README.md` | ausführliche Bedienung und Zusammenspiel aller Generatoren |

## Konfiguration pro Bildsatz

| Spalte | Bedeutung |
|---|---|
| `symbol_set` | kurzer Name des Bildsatzes |
| `symbol_folder` | relativer Ordner des gewünschten Bildsatzes |
| `symbol_count` | Zahl der benannten Symbole |
| `symbol_names` | Namen aller nummerierten Symbole, durch `|` getrennt |
| `symbol_scale_map` | Größenfaktoren aller nummerierten Symbole, durch `|` getrennt |
| `symbol_available_map` | `1`/`0` je ID; fehlende Bilddateien bleiben im Layout leer |
| `<modus>_start` / `<modus>_end` | inklusive Ringgrenzen für Gruselino, Memory, Domino oder Dobble |
| `<modus>_shift` | zyklischer Versatz des jeweiligen Modus |

Alle fachlich editierbaren Informationen eines Bildsatzes stehen in genau einer Master-Zeile. CardMaker benötigt seine Kartenanzahl jedoch in einer Spalte `Count`. Der Builder leitet deshalb aus jedem Master vier technische Referenzen ab, beispielsweise `gruselino_k.csv`, `memory_k.csv`, `domino_k.csv` und `dobble_k.csv`. Zum Wechseln des Bildsatzes wird am Layout die gleichnamige Modus-CSV des anderen Satzes gewählt. Abgeleitete Dateien werden nicht von Hand gepflegt.

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
python generators/symbols_download_arasaac.py generators/symbol_names.csv --set-name k --force
```

Der Satzname bestimmt automatisch:

- `images/symbols/<satz>/` für Bilder und `ATTRIBUTION.md`
- `symbols_<satz>.csv` als editierbarer Master
- vier `<modus>_<satz>.csv` als direkt auswählbare CardMaker-Referenzen
- `symbols_<satz>_sources.csv` mit ARASAAC-IDs, Suchsprache und Quelllinks

Ohne `--set-name` wird der Dateiname der Wortliste verwendet. Bestehende Ausgaben werden nur mit `--force` ersetzt. Neu erzeugte Größenfaktoren beginnen bei `1` und können danach in `symbol_scale_map` korrigiert werden.

## Vorhandenen Bildordner anbinden

Der unabhängige CSV-Generator kann auch ohne ARASAAC verwendet werden. Die erste Spalte der Namensliste enthält die Anzeigenamen; weitere Spalten werden ignoriert. Im Bildordner zählen nur lückenlos nummerierte Hauptdateien `01.png`, `02.png` usw. Dateien wie `01-d1.png` sind Alternativen und erhöhen die Symbolzahl nicht.

```powershell
python generators/symbols_generate_sets.py generators/symbol_names.csv images/symbols/k --set-name k --force
```

Der Ordnername ist ohne `--set-name` zugleich der Satzname. Vorhandene Größenkorrekturen und Shifts werden beim bewussten Neuerzeugen soweit möglich beibehalten. Danach sind Master und alle vier technischen Modus-CSVs aktuell. Der ARASAAC-Importer benutzt intern genau dieselbe Funktion.

## Spiellogik

- **Gruselino:** Vier Grundkarten zeigen dieselben acht Symbole. Acht Suchkarten zeigen diese Symbole jeweils zufällig vertauscht und gedreht; auf jeder Suchkarte fehlt genau ein anderes Symbol. Die acht historischen Positionen bleiben fest. `gruselino_shift` verschiebt das aktive 8er-Fenster zyklisch.
- **Memory:** Jedes Symbol des konfigurierten Bereichs wird genau zweimal als eigene Karte erzeugt.
- **Domino:** `domino_start` und `domino_end` bestimmen den Ring. Jede Karte zeigt ein Symbol und seinen zyklischen Nachfolger; die letzte Karte führt wieder zum ersten Symbol. Die unveränderte Grafik wird mittig größenkorrigiert und anschließend als gesamtes Element zufällig gedreht.
- **Dobble:** Das nächstkleinere perfekte System unterhalb der 8er-Karten nutzt 31 Symbole, 31 Karten und sechs Symbole pro Karte. Jedes Kartenpaar teilt exakt ein Symbol. Bei kleineren Bildsätzen bleiben nicht vorhandene IDs leer.

Gruselino- und Dobble-Symbole variieren zur Laufzeit um ±5 % und werden um 0–359° gedreht. Die Grundpositionen und Grundgrößen bleiben direkt im CardMaker-Editor editierbar.

## Erzeugen und prüfen

```powershell
python generators/build_lautspiele_project.py
python validate_lautspiele_project.py
```

CardMaker-Version des Werkzeugstands: v1.03. `symbols_generate_sets`: v1.00. `symbols_download_arasaac`: v1.00.
