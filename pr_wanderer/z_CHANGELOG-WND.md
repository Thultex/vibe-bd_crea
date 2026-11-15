# Changelog WND

## Stats

Ausgangsdatum: 2026-11-13

*Diese Woche (ca. 3,8h, 2 Tage, 17 Inhalte):*
WND: Projektgrundlage übernommen, Kartenlisten vereinheitlicht und getrennte CardMaker-Projekte für dunklen Print und platzsparenden A4-Paperdruck ergänzt.

*Letzte Woche (0,0h, 0 Tage, 0 Inhalte):*
Keine Einträge.

*Dieser Monat (ca. 3,8h, 2 Tage, 17 Inhalte):*
WND: Anleitung, Design, Materialbestand, Kartenverzeichnisse und getrennte CardMaker-Produktionswege aufgebaut.

*Letzter Monat (0,0h, 0 Tage, 0 Inhalte):*
Keine Einträge.

*Jahr (ca. 3,8h, 2 Tage, 17 Inhalte):*
WND: Projektgrundlage mit Dokumentation, vereinheitlichten Kartendaten und CardMaker-Ausgabe erstellt.

*Insgesamt (ca. 3,8h, 2 Tage, 17 Inhalte):*
WND: Projektgrundlage mit Dokumentation, vereinheitlichten Kartendaten und CardMaker-Ausgabe erstellt.

## Log

### 2026-11-15 - wnd, cardmaker, farben, paper (ca. 0,6h)

- Summary: Den Modusschalter durch zwei feste CardMaker-Projekte ersetzt und den Paper-Export auf platzsparende A4-PDF-Anordnung ausgerichtet.
- Material: `format_text` aus allen TSV-Listen entfernt und durch `col1`, `col2` usw. direkt vor `img` ersetzt; diese Spalten enthalten ausschließlich die hellen Ausgangsfarben für dunkle Karten.
- CardMaker: `wanderer-print.cmp` für dunkle Bridge-Karten mit Bild- beziehungsweise Text-Fallback und `wanderer-paper.cmp` für helle Bridge-Textkarten erzeugt.
- CardMaker: Alle eingezeichneten Crop-Zeichen entfernt; Exportmaße auf 675 × 1050 px bei 300 dpi festgelegt und beim Paper-Projekt nur den Export-Kartenrand ohne Kreuze aktiviert.
- CardMaker: CSVs um die abschließenden Spalten `format-hell` und `format-dunkel` ergänzt; der Generator dunkelt Farben für helle Karten automatisch ab und erkennt flektierte Formen in den Phrasen.
- Paper: Bridge-Layouts für CardMakers A4-PDF-Packung beibehalten; mit den dokumentierten Rändern passen bis zu neun Karten im 3 × 3-Raster auf eine Seite.
- Doku: CardMaker-README, `cards/info-listen.md`, Projekt-README, Design v1.19 und Material v1.09 an die getrennten Projekte und Farbverarbeitung angepasst.
- Test: TSV-Schemata, Farbwerte, zehn Karten, beide Formatspalten, zwei Projekte, acht Layouts, Exportmaße, fehlende Crop-Zeichen sowie Bild-Fallback validiert.

### 2026-11-15 - wnd, cardmaker, listen, export (ca. 1,0h)

- Summary: Minimalen CardMaker-Produktionsweg mit Paper-/Print-Schalter und typbezogenen Layouts ergänzt.
- Material: `format_text` in allen konkreten Listen und der Wortkandidatenliste direkt vor `img` eingefügt; sichtbare Wörter beziehungsweise Phrasen mit semantischen CardMaker-Farbtags versehen.
- Material: Hinter `ai` in allen Listen eine namenlose Leerspalte als sichtbare Grenze zu den Metadaten eingefügt.
- CardMaker: Generator unter `cardmaker/` angelegt; er liest die vier konkreten TSV-Listen und erzeugt vier CSV-Referenzen sowie genau ein Layout pro Kartentyp.
- CardMaker: Paper-Modus als A4 bei 300 dpi mit weißem Hintergrund, mittiger Bridge-Fläche, dunklem Text und acht Schnittmarken umgesetzt.
- CardMaker: Print-Modus als Bridge-Karte 675 × 1050 px umgesetzt; vorhandene Bilder füllen die Karte, fehlende Bilder schalten auf hellen, vertikal zentrierten Text auf Schwarz um.
- CardMaker: `Arial Rounded MT Bold` als klare Rundschrift hinterlegt und Exportmaße sowie Dateinamensmuster im Projekt gespeichert.
- Test: Beide Modi gebaut und validiert; TSV-Spalten, Farbmarken, Kartenanzahl, CSV-Referenzen, Layoutgrößen, Schnittmarken und Bild-Fallback geprüft. Eingecheckter Standardmodus bleibt `paper`.
- Doku: `cards/info-listen.md`, Projekt-README, Design v1.18 und Material v1.08 an Formattext, Leerspalte und CardMaker-Datenfluss angepasst.

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
