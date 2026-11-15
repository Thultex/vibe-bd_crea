# Informationen zu Kartenlisten und Material

Diese Datei ist die zentrale Dokumentation für alle maschinenlesbaren Kartenlisten von „Wanderer und Träumende Götter“. Sie beschreibt Dateistruktur, Spaltenreihenfolge, Bewertungswerte und Bildkonventionen. Maßgeblich für die Verarbeitung bleiben die jeweiligen TSV-Dateien.

## Dateien und Kartengruppen

| Gruppe | TSV-Datei | Subtypen |
|---|---|---|
| Orte | `ort/liste-ort.tsv` | `ort` |
| Aufgaben | `aufgabe/liste-aufgabe.tsv` | `gefahr`, `sozial`, `technisch`, `hindernis` |
| Wörter | `wort/liste-wort.tsv` | `nomen`, `adjektiv` |
| Figuren | `figur/liste-figur.tsv` | `figur` |

Wortkandidaten ohne Karten-ID stehen separat in `wort/liste-wort-kandidaten.tsv` und zählen nicht zum konkretisierten Kartenbestand. Nicht konkretisierte Aufgaben werden nicht als Platzhalterzeilen geführt.

Alle Dateien sind UTF-8-kodierte TSV-Dateien mit echten Tabulatoren. Mehrere Einträge in `vorschläge-verben` sind mit Semikolon getrennt.

## Gemeinsame Produktionsstruktur

Nach `anzahl`, `id` und `punkte` folgen geschlossen die gruppenspezifischen Inhaltsfelder. Direkt dahinter stehen `col1`, `col2` usw. für die Farben der zugehörigen Zielwörter, anschließend `img` und `ai`. Eine absichtlich leere Trennspalte grenzt davon die Metadaten `subtyp`, `bildmotiv`, `frequenz`, `komplexität` und `spezifität` ab. `vorschläge-verben` ist universell die letzte Spalte.

Konkretisierte Karten haben derzeit jeweils die Stückzahl `1`. Noch nicht festgelegte Werte bleiben leer. Karten-IDs sind intern kleingeschrieben.

| Gruppe | Inhaltsfelder nach `punkte` |
|---|---|
| Ort | `ort`, `phrase`, `wort_1`, `wort_2` |
| Aufgabe | `phrase`, `wort_1`, `wort_2`, `kleinod` |
| Wort | `wort` |
| Figur | `name`, `faehigkeiten` |

Die konkreten Kopfzeilen lauten:

```text
liste-ort.tsv:
anzahl  id  punkte  ort  phrase  wort_1  wort_2  col1  col2  img  ai  [leer]  subtyp  bildmotiv  frequenz  komplexität  spezifität  vorschläge-verben

liste-aufgabe.tsv:
anzahl  id  punkte  phrase  wort_1  wort_2  kleinod  col1  col2  img  ai  [leer]  subtyp  bildmotiv  frequenz  komplexität  spezifität  vorschläge-verben

liste-wort.tsv:
anzahl  id  punkte  wort  col1  img  ai  [leer]  subtyp  bildmotiv  frequenz  komplexität  spezifität  vorschläge-verben

liste-figur.tsv:
anzahl  id  punkte  name  faehigkeiten  col1  img  ai  [leer]  subtyp  bildmotiv  frequenz  komplexität  spezifität  vorschläge-verben
```

Die Kandidatenliste ergänzt vor `vorschläge-verben` das Feld `status`.

## Bedeutung gemeinsamer Felder

- `col1`, `col2` usw.: Ausgangsfarben der zugehörigen Zielwörter als `0xRRGGBB`. Die Werte sind für dunkle Karten gewählt: `col1` gehört zu `wort_1` beziehungsweise dem Einzelwort, `col2` zu `wort_2`. Der CardMaker-Generator erzeugt für helle Karten automatisch dunklere Varianten.
- `img`: Pfad zum normalen PNG- oder JPG-Export ohne Beschnittzugabe.
- `ai`: Pfad zur editierbaren Illustrator-Originaldatei.
- leere Spalte hinter `ai`: rein visuelle Trennung zwischen Inhalts-/Produktionsdaten und den folgenden Metadaten; sie hat bewusst keinen Spaltennamen und wird nicht verarbeitet.
- `subtyp`: fachliche Untergruppe der Karte.
- `bildmotiv`: Beschreibung der geplanten visuellen Darstellung; dafür werden keine gruppenspezifischen Feldnamen verwendet.
- `vorschläge-verben`: mögliche Handlungen als Material- und Entwicklungshilfe, keine Pflichtlösung.

Bildpfade werden nur eingetragen, wenn die Datei tatsächlich vorhanden ist.

## Bewertungsskala

`frequenz`, `komplexität` und `spezifität` sind vorläufige Einschätzungen auf einer Skala von 1 bis 5. Ein niedriger Wert bedeutet häufig, einfach oder breit; ein hoher Wert bedeutet selten, komplex oder spezifisch.

| Feld | Wert 1 | Wert 3 | Wert 5 |
|---|---|---|---|
| `frequenz` | sehr häufig und früh verfügbar | mittlere Verfügbarkeit | sehr selten oder wenig verfügbar |
| `komplexität` | sehr einfach oder unterkomplex | mittlere sprachliche/inhaltliche Komplexität | sehr komplex |
| `spezifität` | sehr breit und vielseitig einsetzbar | merklich eingegrenzt | stark spezifisch und situationsgebunden |

### Ermittlungsgrundlage

- `frequenz`: Gebrauchshäufigkeit und erwartete frühe Verfügbarkeit der zentralen Wörter beziehungsweise Phrase. Als zusätzlicher Anhaltspunkt dient die Repository-Liste `sp-zeilenfuttern/tools/presets/leibnitz-100k.txt`. Sie ersetzt keine kindgerichteten oder logopädischen Normdaten.
- `komplexität`: phonologische, lexikalische und bei Phrasen auch grammatische beziehungsweise strukturelle Schwierigkeit.
- `spezifität`: Breite plausibler Bedeutungen, Handlungen und Einsatzsituationen. Wert 1 bedeutet bewusst eine große Einsatzbreite; Wert 5 eine enge, stark situationsabhängige Verwendung.

Die Werte dienen Materialauswahl, Mischung und Balance. Sie sind Arbeitshypothesen und sollen später anhand geeigneter Quellen und Spieltests geprüft werden.

## Aktuelle Bewertungen

### Orte

| ID | Inhalt | Frequenz | Komplexität | Spezifität |
|---|---|---:|---:|---:|
| `e01` | Wüste | 2 | 2 | 3 |
| `e02` | Wald | 1 | 2 | 2 |

### Aufgaben

| ID | Inhalt | Frequenz | Komplexität | Spezifität |
|---|---|---:|---:|---:|
| `ag01` | Ein Haus brennt! | 2 | 2 | 4 |
| `ag02` | Ein Dieb klaut Geld! | 3 | 2 | 4 |

### Wörter

| ID | Inhalt | Frequenz | Komplexität | Spezifität |
|---|---|---:|---:|---:|
| `wn01` | Eimer | 2 | 3 | 2 |
| `wn02` | Seil | 2 | 4 | 1 |
| `wa01` | schnell | 1 | 1 | 1 |
| `wa02` | kalt | 1 | 2 | 2 |

### Figuren

| ID | Inhalt | Frequenz | Komplexität | Spezifität |
|---|---|---:|---:|---:|
| `f01` | Jonas | 4 | 1 | 1 |
| `f02` | Mira | 4 | 1 | 1 |

### Wortkandidaten

| Inhalt | Frequenz | Komplexität | Spezifität |
|---|---:|---:|---:|
| Lupe | 2 | 1 | 4 |
| Kompass | 2 | 2 | 4 |
| Greifer | 4 | 2 | 3 |
| Maske | 2 | 2 | 3 |
| Netz | 1 | 2 | 2 |

## Bilddateien

Jede Kartengruppe hat genau einen Ordner `img/` für editierbare Illustrator-Originale und normale PNG- oder JPG-Exporte ohne Beschnittzugabe. Separate `ai/`- und `bleed/`-Ordner sind nicht vorgesehen. Druckausgaben erzeugt der CardMaker bei Bedarf aus den normalen Exporten.

Die Karten-ID wird im Dateinamen großgeschrieben. Auf einen kurzen Kartennamen folgt bei normalen Exporten die Illustrator-Zeichenflächenkennung `-01`:

```text
ort/img/E01_Wüste.ai
ort/img/E01_Wüste-01.png
aufgabe/img/AG01_Haus_brennt.ai
aufgabe/img/AG01_Haus_brennt-01.png
wort/img/WN01_Eimer.ai
wort/img/WN01_Eimer-01.png
wort/img/WA01_Schnell.ai
wort/img/WA01_Schnell-01.png
```

Bleed-Dateien wie `E01_Wüste-02.png` werden nicht versioniert. Kleine `.ai`-Quelldateien gehören ausdrücklich ins Repository. Die festen Projekte `../cardmaker/wanderer-print.cmp` und `../cardmaker/wanderer-paper.cmp` verwenden dieselben erzeugten CSV-Referenzen. Deren letzte Spalten `format-hell` und `format-dunkel` enthalten die vollständig formatierten Wörter beziehungsweise Phrasen.
