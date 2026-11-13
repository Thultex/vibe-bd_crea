# Kartendaten

Die Unterordner enthalten die Kartendaten aus `../material_wtg.md` als UTF-8-kodierte TSV-Dateien. Felder sind durch echte Tabulatoren getrennt. Mehrere Verben innerhalb eines Feldes sind mit Semikolon getrennt.

## Struktur

| Ordner | Präfix | TSV-Datei |
|---|---|---|
| `ort/` | `e` | `e.tsv` |
| `aufgabe/` | `ag` | `ag.tsv` |
| `aufgabe/` | `as` | `as.tsv` |
| `aufgabe/` | `at` | `at.tsv` |
| `aufgabe/` | `ah` | `ah.tsv` |
| `wort/` | `wn` | `wn.tsv` |
| `wort/` | `wa` | `wa.tsv` |
| `figur/` | `f` | `f.tsv` |

Die drei noch offenen Aufgabentypen enthalten zunächst nur die gemeinsame Kopfzeile. Dadurch steht das spätere Datenschema bereits fest, ohne Platzhalterkarten zu erfinden.

## Bilddateien

Zu jedem Kartentyp gehört ein Ordner `img/`. Bilddateien werden nach folgendem Muster benannt:

```text
<karten-id>_<kurzname>.<endung>
```

Beispiele:

```text
ort/img/e01_wüste.png
aufgabe/img/ag01_haus-brennt.jpg
wort/img/wn01_eimer.png
```

Bevorzugte Endung ist `.png`; `.jpg` und `.jpeg` sind ebenfalls zulässig. Wenn sich die Endung ändert, muss der Wert in der Spalte `bilddatei` der zugehörigen TSV-Datei angepasst werden.
