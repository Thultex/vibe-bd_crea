# Changelog WND

## Stats

Ausgangsdatum: 2026-11-13

*Diese Woche (ca. 2,2h, 2 Tage, 15 Inhalte):*
WND: Projektgrundlage übernommen und auf die gemeinsame Kartenlisten-, Bild- und Pfadstruktur umgestellt.

*Letzte Woche (0,0h, 0 Tage, 0 Inhalte):*
Keine Einträge.

*Dieser Monat (ca. 2,2h, 2 Tage, 15 Inhalte):*
WND: Anleitung, Design, Materialbestand und Cardmaker-taugliche Kartenverzeichnisse aufgebaut.

*Letzter Monat (0,0h, 0 Tage, 0 Inhalte):*
Keine Einträge.

*Jahr (ca. 2,2h, 2 Tage, 15 Inhalte):*
WND: Projektgrundlage mit vollständiger Dokumentation und vereinheitlichten maschinenlesbaren Kartendaten erstellt.

*Insgesamt (ca. 2,2h, 2 Tage, 15 Inhalte):*
WND: Projektgrundlage mit vollständiger Dokumentation und vereinheitlichten maschinenlesbaren Kartendaten erstellt.

## Log

### 2026-11-15 - wnd, struktur, doku, material, assets (ca. 1,5h)

- Summary: Projekt und Kartenbestand auf das Kürzel `wnd`, sprechende gemeinsame TSV-Listen und eine Cardmaker-taugliche Bildstruktur umgestellt.
- Struktur: Projektordner in `pr_wanderer` und die fünf zentralen Projektdokumente auf das Kürzel `wnd` umbenannt.
- Material: Die zehn konkretisierten Karten vollständig in `liste-ort.tsv`, `liste-aufgabe.tsv`, `liste-wort.tsv` und `liste-figur.tsv` zusammengeführt; keine neuen Karten ergänzt.
- Material: Alle Kartenlisten beginnen mit `anzahl`; die Stückzahl jeder konkretisierten Karte ist `1`, IDs bleiben kleingeschrieben.
- Material: Das produktionsnahe Grundschema auf alle Kartenlisten übertragen; gruppenspezifische Inhaltsfelder stehen geschlossen nach `punkte`, gemeinsame Medien- und Bewertungsfelder folgen danach.
- Material: Bewertungsfelder in `frequenz`, `komplexität` und `spezifität` umbenannt und alle zehn Karten sowie fünf Kandidaten vorläufig auf der Skala 1–5 eingestuft; 1 steht für hochfrequent, sehr einfach beziehungsweise breit einsetzbar.
- Doku: `cards/info-listen.md` als Ersatz für die Karten-README angelegt und um Struktur, Bildkonventionen, Skalenrichtung, Ermittlungsgrundlage sowie alle aktuellen Materialbewertungen ergänzt.
- Material: Verbideen universell als abschließende Spalte `vorschläge-verben` vereinheitlicht; bisherige gruppenspezifische Verbspalten ohne Inhaltsverlust zusammengeführt.
- Material: Figurendarstellungen universell in `bildmotiv` überführt; gruppenspezifische Bild- und Pfadspalten vereinheitlicht.
- Material: Aufgabenphrasen auf „Ein Haus brennt!“ und „Ein Dieb klaut Geld!“ präzisiert.
- Material: Die fünf Nomen-Kandidaten ohne ID in `liste-wort-kandidaten.tsv` getrennt erhalten und an das gemeinsame Wortschema angeglichen; ihre Stückzahl bleibt bis zur Konkretisierung leer.
- Assets: Je Kartengruppe genau einen gemeinsamen `img/`-Ordner für AI-Originale und normale Exporte vorgesehen; Benennung mit großgeschriebener ID und `-01` für normale Exporte dokumentiert.
- Assets: Bestand auf AI-, PNG-, JPG- und Bleed-Dateien geprüft; es waren noch keine Bilddateien vorhanden, daher wurden veraltete Scheinreferenzen aus den TSV-Daten entfernt und die Bildpfade leer belassen.
- Doku: Projekt-README und Karten-README an Struktur, Dateinamen, Bildpfade, Bleed-Verzicht und spätere Cardmaker-Erzeugung angepasst.
- Doku: Anleitung v1.10, Design v1.17 und Material v1.07 dokumentieren Aufgabenphrasen, universelles Listenschema und Dateinamen.
- Test: TSV-Spalten, Kartenanzahl, Stückzahlen, IDs, Verweise, Altdateien und Medienbestand gegen die tatsächliche Projektstruktur geprüft.

### 2026-11-13 - wnd, struktur, doku, material (ca. 0,7h)

- Summary: Neues Spielprojekt mit den konsolidierten Quelldokumenten, Kartentabellen und vorbereiteten Bildpfaden angelegt.
- Struktur: Spielprojekt für „Wanderer und Träumende Götter“ erstellt.
- Doku: Spielanleitung v1.09, Designdokument v1.14 und Materialdokument v1.04 vollständig übernommen.
- Material: Konkrete Karten für Ort, Gefahr, Wort-Nomen, Wort-Adjektiv und Figur maschinenlesbar erfasst.
- Material: Nomen-Kandidaten ohne Karten-ID separat erfasst; sie bleiben außerhalb des konkretisierten Bestands.
- Assets: Versionierbare Bildordner für Orte, Aufgaben, Wörter und Figuren vorbereitet.
