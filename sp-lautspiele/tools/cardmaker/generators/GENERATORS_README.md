# Lautspiele-Generatoren

Die Generatoren trennen Bildbeschaffung, Bildsatz-Konfiguration und CardMaker-Projektaufbau. Als Arbeitsverzeichnis wird in den Beispielen `sp-lautspiele/tools/cardmaker/` verwendet.

## Überblick

| Datei | Aufgabe |
|---|---|
| `symbols_download_arasaac.py` | Sucht Begriffe über die ARASAAC-API, lädt Hauptbilder und Alternativen und dokumentiert deren Quellen. Ruft danach automatisch `symbols_generate_sets.py` auf. |
| `symbols_generate_sets.py` | Erzeugt aus einer Namensliste und einem vorhandenen nummerierten Bildordner die Master-CSV sowie die vier CardMaker-Modus-CSVs. Benötigt kein Netzwerk. |
| `build_lautspiele_project.py` | Erzeugt `lautspiele.cmp`, aktualisiert die vorhandenen Master-CSVs und leitet alle technischen Modus-CSVs erneut ab. |
| `symbol_names.csv` | Beispiel für die gemeinsame Namens- und ARASAAC-Suchliste. |

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

## 1. ARASAAC-Bilder herunterladen

```powershell
python generators/symbols_download_arasaac.py generators/symbol_names.csv --set-name k --force
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
memory_k.csv
domino_k.csv
dobble_k.csv
```

`01.png` ist der ausgewählte Haupttreffer. `01-d1.png` und `01-e1.png` sind deutsche beziehungsweise englische Alternativen. Eine Alternative kann später durch Umbenennen zur Hauptdatei gemacht werden. Doppelte ARASAAC-IDs werden nicht zweimal gespeichert.

Ohne `--set-name` wird der Dateiname der Namensliste als Satzname verwendet. Bestehende Ausgaben werden nur mit `--force` überschrieben.

## 2. Vorhandene Bilder als Bildsatz einbinden

Sind die PNGs bereits vorhanden oder manuell ausgewählt, ist kein ARASAAC-Abruf nötig:

```powershell
python generators/symbols_generate_sets.py generators/symbol_names.csv images/symbols/k --set-name k --force
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
- `memory_<satz>.csv`,
- `domino_<satz>.csv`,
- `dobble_<satz>.csv`.

Vorhandene Größenkorrekturen und Modus-Shifts werden beim Neuerzeugen soweit möglich beibehalten. Die Modus-CSVs sind technische Ableitungen und sollten nicht von Hand bearbeitet werden.

## 3. CardMaker-Projekt neu erzeugen

```powershell
python generators/build_lautspiele_project.py
python validate_lautspiele_project.py
```

Der Builder erzeugt `lautspiele.cmp` mit diesen Layouts:

- Gruselino Karten,
- Gruselino Papier,
- Memory Papier,
- Domino Papier,
- Dobble Papier.

Er aktualisiert außerdem die Verfügbarkeitskarten anhand der tatsächlich vorhandenen nummerierten PNGs und erzeugt die Modus-CSVs erneut. Der Validator prüft anschließend Struktur, Referenzen, Counts, Gruselino-Ausblendung, Memory-Paare, Domino-Ring und die perfekte Dobble-Matrix.

## Empfohlener Ablauf

1. `symbol_names.csv` kopieren und Begriffe eintragen.
2. Bilder mit `symbols_download_arasaac.py` laden oder manuell als nummerierte PNGs bereitstellen.
3. Bei manuellen Bildern `symbols_generate_sets.py` ausführen.
4. Größenfaktoren oder Shifts bei Bedarf ausschließlich in `symbols_<satz>.csv` anpassen.
5. `build_lautspiele_project.py` ausführen.
6. `validate_lautspiele_project.py` ausführen.
7. `lautspiele.cmp` in CardMaker öffnen und für jedes Layout die passende `<modus>_<satz>.csv` wählen.

## Wichtige Regeln

- Masterdaten werden in `symbols_<satz>.csv` gepflegt.
- Modus-CSVs enthalten zusätzlich CardMakers erforderliche Spalte `Count` und werden generiert.
- Bilder liegen unter `images/symbols/<satz>/`.
- ARASAAC-Quellen und Lizenzhinweise dürfen beim Weitergeben der Bilder nicht entfernt werden.
- `--force` nur verwenden, wenn bestehende generierte Daten bewusst ersetzt werden sollen.
