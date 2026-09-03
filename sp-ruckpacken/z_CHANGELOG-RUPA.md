# Changelog Ruckpacken

## Stats

Ausgangsdatum: 2026-07-12

*Diese Woche (ca. 0,5h, 2 Tage, Inhalte):*
Eigene Bilder mit ARASAAC-Ergänzung in CardMaker eingebunden; Merkmalstabelle und Bilder-Checklisten ergänzt.

*Letzte Woche (0h, 0 Tage, Inhalte):*
Keine Einträge.

*Dieser Monat (ca. 0,5h, 2 Tage, Inhalte):*
Eigene Bilder mit ARASAAC-Ergänzung in CardMaker eingebunden; Merkmalstabelle und Bilder-Checklisten ergänzt.

*Letzter Monat (0h, 0 Tage, Inhalte):*
Keine Einträge.

*Jahr (ca. 2,1h, 5 Tage, Inhalte):*
Ruckpacken v1.00 begonnen, Drucklayout vorbereitet, eigene Bilder in CardMaker eingebunden und Bildplanung ergänzt.

*Insgesamt (ca. 2,1h, 5 Tage, Inhalte):*
Ruckpacken v1.00 begonnen, Drucklayout vorbereitet, eigene Bilder in CardMaker eingebunden und Bildplanung ergänzt.

## Log

### 2026-09-03 - rupa, assets, cardmaker, tools, doku (ca. 0,3h)

- Material: Eigenes Ball-Motiv aus `assets/img/objects/rp1_ball.concepts` und `rp1_ball.png` übernommen; die leere Größen-/Linien-TXT bleibt Orientierung.
- Tool: Wiederverwendbare Routine `sync_custom_images.py` erkennt Concepts/PNG-Paare, prüft Gegenstandsnummer und Name und dokumentiert alle 73 Zuordnungen in `files/data/custom-img_mapping.csv`; das Vorgehen für spätere Importe liegt in `files/routine_import-img.md`.
- Change: Eigene PNGs nach `tools/cardmaker/assets/images/custom/` kopiert; aktiver Bildsatz direkt unter `tools/cardmaker/assets/images/sym_1.png` bis `sym_73.png` besteht aus 1 Custom-Motiv und 72 ARASAAC-Ergänzungen.
- Change: Alle 657 Bildreferenzen in `cards.csv` auf den aktiven Bildsatz umgestellt; CSV-Generator und Projektvalidator berücksichtigen Custom-Vorrang und aktuelle Bildkopien.
- Test: Sechs Regressionstests sowie den CardMaker-Projektvalidator erfolgreich ausgeführt; Paarerkennung, Rückfallbilder, unveränderte Kartenbelegung und wiederholbarer Abgleich geprüft.
- Versionen: sync_custom_images v1.00.

### 2026-09-02 - rupa, assets, doku (ca. 0,2h)

- Material: Merkmalsübersicht (#13) in `files/ruckpacken_merkmale.md` mit den Spalten Nr., Note, Typ, Name und Items ergänzt; 85 Merkmale sind nach Handlung, Eigenschaft und Ort geordnet und ihren Gegenständen zugeordnet.
- Doku: Bilder-Checklisten für 73 Gegenstände (#12) und 85 Merkmale (#13) angelegt; Gegenstands- und Merkmalsnamen in beiden Issues fett formatiert und Übersichten im README verlinkt.
- Change: Merkmalsliste (#13) und Markdown-Tabelle innerhalb jedes Typs nach Anzahl zugeordneter Gegenstände absteigend und bei Gleichstand alphabetisch sortiert; Nummerierung angeglichen, Issue in drei Typabschnitte gegliedert und Typangaben aus den Klammern entfernt.
- Test: 25 Handlungen, 40 Eigenschaften, 20 Orte und alle 584 Zuordnungen mit den CSV-Quellen abgeglichen; vier Eigenschaften ohne Gegenstände ausdrücklich gekennzeichnet.

### 2026-07-26 - rupa, tools, datenschutz (ca. 0,1h)

- Fix: Absoluten privaten Projektpfad im nanDECK-Startskript durch den relativen Pfad `%~dp0ruckpacken.nde` ersetzt; das Skript bleibt unabhängig vom lokalen Checkout-Ort nutzbar.

### 2026-07-13 - rupa, cardmaker, layout, druck (ca. 0,7h)

- Change: CardMaker-Projekt auf MPC Jumbo 3,5″ × 5″ bei 300 dpi umgestellt; 1120 × 1570 px Vollbeschnitt, 1050 × 1500 px Schnittfläche und 975 × 1425 px Sicherheitsfläche umgesetzt.
- Design: Symbolmittelpunkte auf X und Y proportional zur Schnittfläche skaliert; Symbolgrößen anhand des kleineren Achsenfaktors angepasst.
- Change: Laufzeitrotation auf den vollständigen Kreis (0° bis 359°) erweitert; Größenvariation bleibt auf ungefähr ±5 % begrenzt.
- Design: Vollflächigen weißen Hintergrund sowie rote, ungefüllte Schnitt- und Sicherheitsrahmen ergänzt; Rahmen sind nur im Editor sichtbar und werden nicht exportiert.
- Test: Layoutmaße, 300 dpi, Symbolgeometrie, Zufallstransformationen, Hilfsrahmen, weißer Hintergrund, 73 Karten und alle Bildreferenzen validiert.
- Doku: Bildmodell präzisiert: neun Layout-Bildplätze werden für 73 Karten wiederverwendet; 657 bezeichnet nur die daraus entstehenden Belegungen, nicht Layoutplätze oder Assets. Dauer: ca. 5 Minuten.
- Fix: CardMaker-Ursprungsfehler behoben: Symbolkoordinaten als linke obere Elementkante gespeichert und `centerimageonorigin` deaktiviert. JavaScript erzeugt nun pro Symbol einen gemeinsamen Größenwert und führt X/Y nach, sodass ±5-%-Skalierung und 360°-Rotation dauerhaft um denselben Mittelpunkt laufen. Dauer: ca. 20 Minuten.
- Refactor: Laufzeittransformationen verwenden die normalen CardMaker-Elementwerte `x`, `y`, `width` und `height` als Grundgeometrie; Verschieben und Größenänderungen im Editor werden damit automatisch zum neuen Standard. Dauer: ca. 5 Minuten.

### 2026-07-12 - rupa, struktur, regeln, design, assets, tools, doku (ca. 0,8h)

- Summary: Bestehende Sitzungsartefakte als regelkonformes Spielprojekt übernommen und dokumentiert.
- Struktur: Root-Ordner `sp-ruckpacken` mit dem Kürzel `rupa` angelegt.
- Material: Korpus mit 73 Gegenständen und neu berechnete Kategorienverteilung übernommen.
- Material: Vollständiges nanDECK-Paket mit perfekter 73-Karten-Matrix übernommen.
- Tool: Offizielles ARASAAC-API-Mapping für deutsche und englische Suchen übernommen.
- Material: ARASAAC-Mapping für alle 73 Gegenstände erzeugt; 73 Haupt- und 68 Alternativtreffer stehen zur visuellen Auswahl bereit.
- Struktur: CSV-, Mapping- und nanDECK-Dateien aus `assets/` nach `files/` verschoben; `assets/` bleibt echten Medien vorbehalten.
- Struktur: nanDECK-Archiv entpackt; Vorlage, Kartenmatrizen, Validierung und 73 Platzhalterbilder als geschlossenes Werkzeug unter `tools/nandeck/` eingeordnet.
- Struktur: Allgemeine CSVs nach `files/data/` und die unveränderte ZIP-Quelle nach `files/archive/` gegliedert.
- Material: 73 farbige ARASAAC-Piktogramme heruntergeladen und als aktive nanDECK-Bilder eingebunden; Trinkflasche und Karte auf passendere Alternativtreffer korrigiert.
- Material: Attribution, tatsächliche ARASAAC-IDs und Prüfhilfen ergänzt; Arztkoffer und Verkehrsschild bleiben zur Nachprüfung markiert.
- Fix: Vollflächige Fußballszene durch ein freigestelltes Fußballtor ersetzt; technische Prüfung meldet keine quadratfüllenden Bilder mehr.
- Tool: Kartengenerierung auf `nhmkdev/cardmaker` (`cm`) v1.4.0.0 umgestellt; Projekt, Reference-CSV, Overrides und Validator unter `tools/cardmaker/` ergänzt.
- Material: Verkehrsschild von Ampel/Stopp-Geste auf ein freigestelltes Stoppschild korrigiert; Verbandskasten als Arztkoffer akzeptiert.
- Doku: `cm` eindeutig als `nhmkdev/cardmaker` definiert; nanDECK als Legacy-Prototyp markiert.
- Change: CM-Kartenformat auf 57 × 88 mm (673 × 1039 px bei 300 DPI) gesetzt; Neun-Symbol-Raute mit drei Positionsgrößen und gespeicherten leichten Drehungen umgesetzt.
- Refactor: CM-CSV auf elf Spalten reduziert; Rotation, Größe, Namen, IDs und Overrides aus der Datenquelle entfernt.
- Test: 73 Karten, sauberes CSV-Schema, neun wiederverwendete Layout-Bildplätze und 73 eindeutige Bildassets validiert.
- Struktur: Toolordner von `tools/cm/` nach `tools/cardmaker/` ausgeschrieben; `cm` bleibt nur das dokumentierte Toolkürzel.
- Change: Hart codierte Symbolrotationen entfernt; CardMaker erzeugt Drehung (−20° bis +20°) und geringe Größenabweichung nun beim Rendern über Incept-`#random`-Overrides.
- Tool: `configure_runtime_transforms.py` ergänzt und Validator auf echte Laufzeittransformationen verschärft. Dauer: ca. 25 Minuten.
- Daten: Markdown-Übersicht aller 73 Gegenstände mit laufender Nummer, leerer Notizspalte und den drei Kategoriearten unter `files/ruckpacken_gegenstaende.md` ergänzt. Dauer: ca. 10 Minuten.
- Refactor: ARASAAC-Mapping und Downloader funktional unter `tools/arasaac/` gebündelt.
- Regeln/Design: Überdeckungsmechanik, A/B/C-Aufgaben und organisches Neun-Symbol-Layout dokumentiert.
- Test: CSV-Zeilen, ZIP-Struktur, Python-Syntax und Dobble-Validierung geprüft.
- Versionen: ruckpacken_arasaac_mapping_api_offiziell v1.00.
