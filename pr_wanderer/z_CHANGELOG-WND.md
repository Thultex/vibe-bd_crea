# Changelog WND

## Stats

Ausgangsdatum: 2026-11-13

*Diese Woche (ca. 1,9h, 2 Tage, 12 Inhalte):*
WND: Projektgrundlage übernommen und auf die gemeinsame Kartenlisten-, Bild- und Pfadstruktur umgestellt.

*Letzte Woche (0,0h, 0 Tage, 0 Inhalte):*
Keine Einträge.

*Dieser Monat (ca. 1,9h, 2 Tage, 12 Inhalte):*
WND: Anleitung, Design, Materialbestand und Cardmaker-taugliche Kartenverzeichnisse aufgebaut.

*Letzter Monat (0,0h, 0 Tage, 0 Inhalte):*
Keine Einträge.

*Jahr (ca. 1,9h, 2 Tage, 12 Inhalte):*
WND: Projektgrundlage mit vollständiger Dokumentation und vereinheitlichten maschinenlesbaren Kartendaten erstellt.

*Insgesamt (ca. 1,9h, 2 Tage, 12 Inhalte):*
WND: Projektgrundlage mit vollständiger Dokumentation und vereinheitlichten maschinenlesbaren Kartendaten erstellt.

## Log

### 2026-11-15 - wnd, struktur, doku, material, assets (ca. 1,2h)

- Summary: Projekt und Kartenbestand auf das Kürzel `wnd`, sprechende gemeinsame TSV-Listen und eine Cardmaker-taugliche Bildstruktur umgestellt.
- Struktur: Projektordner in `pr_wanderer` und die fünf zentralen Projektdokumente auf das Kürzel `wnd` umbenannt.
- Material: Die zehn konkretisierten Karten vollständig in `liste-e.tsv`, `liste-a.tsv`, `liste-w.tsv` und `liste-f.tsv` zusammengeführt; keine neuen Karten ergänzt.
- Material: Alle Kartenlisten beginnen mit `anzahl`; die Stückzahl jeder konkretisierten Karte ist `1`, IDs bleiben kleingeschrieben.
- Material: `liste-w.tsv` auf die produktionsnahe Reihenfolge mit Punkten, Verben, Bildpfaden, Subtyp, Bildmotiv sowie `freq`, `komplex` und `breite` umgestellt; Adjektivverben ergänzt und `kalt` vorläufig mit 1 Punkt bewertet.
- Material: Die fünf Nomen-Kandidaten ohne ID in `liste-w-kandidaten.tsv` getrennt erhalten; ihre Stückzahl bleibt bis zur Konkretisierung leer.
- Assets: Je Kartengruppe genau einen gemeinsamen `img/`-Ordner für AI-Originale und normale Exporte vorgesehen; Benennung mit großgeschriebener ID und `-01` für normale Exporte dokumentiert.
- Assets: Bestand auf AI-, PNG-, JPG- und Bleed-Dateien geprüft; es waren noch keine Bilddateien vorhanden, daher wurden veraltete Scheinreferenzen aus den TSV-Daten entfernt und `bild_png` sowie `bild_ai` leer belassen.
- Doku: Projekt-README und Karten-README an Struktur, Dateinamen, Bildpfade, Bleed-Verzicht und spätere Cardmaker-Erzeugung angepasst.
- Doku: Design v1.16 und Material v1.06 dokumentieren Dateikürzel, Wortlistenschema und neue Materialwerte; die Spielanleitung bleibt inhaltlich unverändert auf v1.09.
- Test: TSV-Spalten, Kartenanzahl, Stückzahlen, IDs, Verweise, Altdateien und Medienbestand gegen die tatsächliche Projektstruktur geprüft.

### 2026-11-13 - wnd, struktur, doku, material (ca. 0,7h)

- Summary: Neues Spielprojekt mit den konsolidierten Quelldokumenten, Kartentabellen und vorbereiteten Bildpfaden angelegt.
- Struktur: Spielprojekt für „Wanderer und Träumende Götter“ erstellt.
- Doku: Spielanleitung v1.09, Designdokument v1.14 und Materialdokument v1.04 vollständig übernommen.
- Material: Konkrete Karten für Ort, Gefahr, Wort-Nomen, Wort-Adjektiv und Figur maschinenlesbar erfasst.
- Material: Nomen-Kandidaten ohne Karten-ID separat erfasst; sie bleiben außerhalb des konkretisierten Bestands.
- Assets: Versionierbare Bildordner für Orte, Aufgaben, Wörter und Figuren vorbereitet.
