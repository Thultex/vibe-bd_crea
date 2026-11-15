# Kartendaten

Die Unterordner enthalten die Kartendaten aus `../material_wnd.md` als UTF-8-kodierte TSV-Dateien. Felder sind durch echte Tabulatoren getrennt; mehrere Verben innerhalb eines Feldes sind mit Semikolon getrennt.

## Struktur

| Gruppe | TSV-Datei | Subtypen |
|---|---|---|
| Orte | `ort/liste-orte.tsv` | `ort` |
| Aufgaben | `aufgabe/liste-aufgaben.tsv` | `gefahr`, `sozial`, `technisch`, `hindernis` |
| Wörter | `wort/liste-wörter.tsv` | `nomen`, `adjektiv` |
| Figuren | `figur/liste-figuren.tsv` | `figur` |

Die Wortkandidaten ohne Karten-ID stehen separat in `wort/liste-wörter-kandidaten.tsv` und zählen nicht zum konkretisierten Kartenbestand. Nicht konkretisierte Aufgaben werden nicht als Platzhalterzeilen geführt.

Jede Kartenliste beginnt mit `anzahl` und `subtyp`. Konkretisierte Karten haben derzeit jeweils die Stückzahl `1`. Darauf folgen die kleingeschriebene Karten-ID und die gruppenspezifischen Daten. Die optionalen Spalten `bild_png` und `bild_ai` enthalten nur Pfade zu tatsächlich vorhandenen Dateien; andernfalls bleiben sie leer.

## Bilddateien

Jede Kartengruppe hat genau einen Ordner `img/` für editierbare Illustrator-Originale und normale PNG- oder JPG-Exporte ohne Beschnittzugabe. Separate `ai/`- und `bleed/`-Ordner sind nicht vorgesehen. Druckexporte mit Bleed sollen später vom Cardmaker erzeugt werden.

Die Karten-ID wird im Dateinamen großgeschrieben. Auf einen kurzen, lesbaren Kartennamen folgt bei normalen Exporten die Illustrator-Zeichenflächenkennung `-01`:

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

Bleed-Dateien wie `E01_Wüste-02.png` werden nicht versioniert. Kleine `.ai`-Quelldateien gehören ausdrücklich ins Repository.
