# Changelog WTG

## Stats

Ausgangsdatum: 2026-11-13

*Diese Woche (ca. 0,7h, 1 Tag, 5 Inhalte):*
WTG: Quelldokumente übernommen und konkrete Kartendaten nach Kartentyp als TSV mit Bildordnern strukturiert.

*Letzte Woche (0,0h, 0 Tage, 0 Inhalte):*
Keine Einträge.

*Dieser Monat (ca. 0,7h, 1 Tag, 5 Inhalte):*
WTG: Projektstruktur, Anleitung, Design, Materialbestand und Kartenverzeichnisse angelegt.

*Letzter Monat (0,0h, 0 Tage, 0 Inhalte):*
Keine Einträge.

*Jahr (ca. 0,7h, 1 Tag, 5 Inhalte):*
WTG: Projektgrundlage mit vollständiger Dokumentation und maschinenlesbaren Kartendaten erstellt.

*Insgesamt (ca. 0,7h, 1 Tag, 5 Inhalte):*
WTG: Projektgrundlage mit vollständiger Dokumentation und maschinenlesbaren Kartendaten erstellt.

## Log

### 2026-11-13 - wtg, struktur, doku, material (ca. 0,7h)

- Summary: Neues Spielprojekt mit den konsolidierten Quelldokumenten, Kartentabellen und vorbereiteten Bildpfaden angelegt.
- Struktur: Spielordner `sp-wanderer-und-traeumende-goetter` nach den Repository-Konventionen erstellt.
- Doku: Spielanleitung v1.09, Designdokument v1.14 und Materialdokument v1.04 vollständig übernommen.
- Material: Konkrete Karten für Ort, Gefahr, Wort-Nomen, Wort-Adjektiv und Figur in getrennte TSV-Dateien mit den Kürzeln `e`, `ag`, `wn`, `wa` und `f` überführt.
- Material: Alle Aufgaben unter `cards/aufgabe/` und alle Wortkarten unter `cards/wort/` gebündelt; Kategorien bleiben über getrennte TSV-Dateien und Präfixe unterscheidbar.
- Material: Leere TSV-Grundstrukturen `as.tsv`, `at.tsv` und `ah.tsv` für die noch offenen Aufgabentypen Sozial, Technisch und Hindernis angelegt.
- Material: Nomen-Kandidaten ohne Karten-ID separat erfasst; sie bleiben außerhalb des konkretisierten Bestands.
- Assets: Gemeinsame, versionierbare Bildordner für Orte, Aufgaben, Wörter und Figuren vorbereitet und Bilddateinamen nach dem Muster `<id>_<kurzname>.<endung>` in den TSV-Daten hinterlegt, zum Beispiel `ag01_haus-brennt.jpg`.
