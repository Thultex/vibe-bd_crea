# Lautspiele-Skripte

Die Skripte trennen Bildbeschaffung und Bildsatz-Erzeugung unter `scripts/generate/` vom Projektaufbau und der Prüfung unter `scripts/build/`. Als Arbeitsverzeichnis wird in den Beispielen `sp-lautspiele/tools/cardmaker/` verwendet.

## Überblick

| Datei | Aufgabe |
|---|---|
| `generate/symbols_download_arasaac.py` | Sucht Begriffe über die ARASAAC-API, lädt Hauptbilder und Alternativen und dokumentiert deren Quellen. Ruft danach automatisch den Set-Generator auf. |
| `generate/symbols_generate_sets.py` | Erzeugt aus einer Namensliste und einem vorhandenen nummerierten Bildordner die Master-CSV sowie die fünf CardMaker-Modus-CSVs. Benötigt kein Netzwerk. |
| `generate/symbol_names.csv` | Beispiel für die gemeinsame Namens- und ARASAAC-Suchliste. |
| `generate/symbol_ids.csv` | Leere Vorlage für bekannte ARASAAC-IDs ohne Suchlauf. |
| `build/build_lautspiele_files.py` | Erzeugt `lautspiele.cmp`, aktualisiert die vorhandenen Master-CSVs und leitet alle technischen Modus-CSVs erneut ab. |
| `build/validate_lautspiele_project.py` | Prüft Struktur, Referenzen, Counts, Layoutregeln und Dobble-Kombinatorik. |
| `build/build.ini` | Legt das gemeinsame Startsymbol und die automatisch oder fest bestimmte Zahl verwendeter Symbole fest. |

## Symbolauswahl in `build.ini`

```ini
[symbols]
start_symbol = 1
symbol_count = -1
```

- `start_symbol` bezeichnet die erste nummerierte Hauptdatei; `1` entspricht `01.png`.
- `symbol_count = -1` verwendet automatisch alle ab dem Start vorhandenen Hauptsymbole.
- Ein positiver Wert begrenzt das gemeinsame inklusive Symbolfenster.
- Wegen der acht Gruselino-Positionen muss das Fenster mindestens acht Symbole enthalten.
- Dobble wiederholt bei weniger als 31 ausgewählten Symbolen keine IDs; die übrigen Punkte bleiben leer.

Der Builder übernimmt die Auswahl beim Neuerzeugen in die Start-/Endfelder aller Master- und Modus-CSVs. Modusspezifische Shifts bleiben in den jeweiligen Master-CSVs erhalten.

## Eingabeformat `symbol_names.csv`

Eine Zeile beschreibt ein Symbol:

```csv
# Deutsch,Englisch,zusaetzliche Kandidaten je Sprache
Käse,cheese,2
Keks,cookie,2
Ei,egg,2
```

- Spalte 1 ist der deutsche Symbolname und immer erforderlich.
- Spalte 2 ist ein optionaler englischer alternativer Suchbegriff.
- Spalte 3 gibt an, wie viele zusätzliche Kandidaten **je vorhandener Sprache** geladen werden.
- Leerzeilen und Zeilen, deren erste Spalte mit `#` beginnt, werden ignoriert.
- `symbols_generate_sets.py` verwendet nur die erste Spalte als Anzeigenamen.

## Eingabeformat `symbol_ids.csv`

Wenn die gewünschten ARASAAC-IDs bereits bekannt sind, werden unter der erklärenden Kopfzeile ausschließlich positive Ganzzahlen eingetragen:

```csv
arasaac_id,"Eine ARASAAC-ID pro Folgezeile eintragen; nur positive Ganzzahlen, keine Suchbegriffe."
35371
3241
```

Der Downloader erkennt `symbol_ids.csv` am Dateinamen. Er überspringt die Kopfzeile, ruft jede ID direkt über den deutschen ARASAAC-Piktogramm-Endpunkt ab, verwendet den ersten deutschen Begriff als Namen und lädt das zugehörige PNG. Doppelte oder ungültige IDs führen zu einer verständlichen Fehlermeldung.

## 1. ARASAAC-Bilder herunterladen

```powershell
python scripts/generate/symbols_download_arasaac.py scripts/generate/symbol_names.csv --set-name k --force
```

Der Befehl erzeugt:

```text
images/symbols/k/
├─ 01.png
├─ 01-d1.png
├─ 01-e1.png
├─ 02.png
└─ ATTRIBUTION.md

symbols_k.csv
symbols_k_sources.csv
gruselino_k.csv
domino_k.csv
dobble_k.csv
spiel_k.csv
bingo_k.csv
```

`01.png` ist der ausgewählte Haupttreffer. `01-d1.png` und `01-e1.png` sind deutsche beziehungsweise englische Alternativen. Eine Alternative kann später durch Umbenennen zur Hauptdatei gemacht werden. Doppelte ARASAAC-IDs werden nicht zweimal gespeichert.

Ohne `--set-name` wird der Dateiname der Namensliste als Satzname verwendet. Bestehende Ausgaben werden nur mit `--force` überschrieben.

Direkter Abruf bekannter IDs:

```powershell
python scripts/generate/symbols_download_arasaac.py scripts/generate/symbol_ids.csv --set-name k --force
```

## 2. Vorhandene Bilder als Bildsatz einbinden

Sind die PNGs bereits vorhanden oder manuell ausgewählt, ist kein ARASAAC-Abruf nötig:

```powershell
python scripts/generate/symbols_generate_sets.py scripts/generate/symbol_names.csv images/symbols/k --set-name k --force
```

Gezählt werden ausschließlich lückenlos nummerierte Hauptbilder:

```text
01.png
02.png
03.png
```

Alternativen wie `01-d1.png` oder `01-e1.png` erhöhen die Symbolzahl nicht. Die Nummerierung muss bei `01.png` beginnen und darf keine Lücken enthalten. Die Namensliste muss mindestens so viele Einträge wie Hauptbilder besitzen.

Das Skript erzeugt:

- `symbols_<satz>.csv` als editierbaren Master,
- `gruselino_<satz>.csv`,
- `domino_<satz>.csv`,
- `dobble_<satz>.csv`,
- `spiel_<satz>.csv`,
- `bingo_<satz>.csv`.

Vorhandene Größenkorrekturen und Modus-Shifts werden beim Neuerzeugen soweit möglich beibehalten. Die Modus-CSVs sind technische Ableitungen und sollten nicht von Hand bearbeitet werden.

## 3. CardMaker-Projekt neu erzeugen

```powershell
python scripts/build/build_lautspiele_files.py
python scripts/build/validate_lautspiele_project.py
```

Der Builder erzeugt `lautspiele.cmp` mit diesen Layouts:

- Gruselino Papier,
- Memory / Domino Papier,
- Dobble Papier,
- Minimalspiel A4,
- Bingo 4x4.

Er aktualisiert außerdem die Verfügbarkeitskarten anhand der tatsächlich vorhandenen nummerierten PNGs, erzeugt die Modus-CSVs erneut und bindet sämtliche vorhandenen Satz-CSVs an jedes passende Layout. Der Validator prüft anschließend Struktur, vollständige Referenzauswahl, Counts, Gruselino-Ausblendung, das trennbare Memory-/Domino-Doppelmodul, die perfekte Dobble-Matrix, den statischen A4-Spielplan und vier vollständige 4x4-Bingokarten.

## Empfohlener Ablauf

1. `symbol_names.csv` für Suchbegriffe oder `symbol_ids.csv` für bekannte ARASAAC-IDs kopieren und befüllen.
2. Bilder mit `symbols_download_arasaac.py` laden oder manuell als nummerierte PNGs bereitstellen.
3. Bei manuellen Bildern `symbols_generate_sets.py` ausführen.
4. Gemeinsames Startsymbol und Anzahl bei Bedarf in `build.ini` anpassen.
5. Größenfaktoren oder Shifts bei Bedarf ausschließlich in `symbols_<satz>.csv` anpassen.
6. `build_lautspiele_files.py` ausführen.
7. `validate_lautspiele_project.py` ausführen.
8. `lautspiele.cmp` in CardMaker öffnen und für jedes Layout die passende `<modus>_<satz>.csv` wählen.

## Wichtige Regeln

- Masterdaten werden in `symbols_<satz>.csv` gepflegt.
- Modus-CSVs enthalten zusätzlich CardMakers erforderliche Spalte `Count` und werden generiert.
- Bilder liegen unter `images/symbols/<satz>/`.
- ARASAAC-Quellen und Lizenzhinweise dürfen beim Weitergeben der Bilder nicht entfernt werden.
- `--force` nur verwenden, wenn bestehende generierte Daten bewusst ersetzt werden sollen.
